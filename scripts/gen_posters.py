#!/usr/bin/env python3
"""Build assets/pdfs/posters.typ — the poster abstracts in the program booklet.

Three inputs, none of which duplicates the others:

  * the EasyChair abstract export (plain text)  — the abstract of every
    submission, as its authors wrote it;
  * the board-assignment spreadsheet (.xlsx)    — which submission goes on
    which poster board, i.e. which posters are actually being presented and
    in what order a visitor walks past them;
  * accepted.md                                 — the canonical title and
    author list for each poster, already checked by hand for the website, so
    the booklet and the site agree.

Only submissions that appear in the spreadsheet are printed, ordered by board
number. A submission occupying several boards is printed once, over the range.

    ./scripts/gen_posters.py ~/Downloads/'qpl2026-abstracts posters.txt' \
                             ~/Downloads/'Indeling posters.xlsx'
    cd assets/pdfs && typst compile QPL_2026_Program.typ

The abstracts arrive as LaTeX source rather than as typeset text, so the
markup an author used has to be resolved before it can be set: see `clean`.
"""

import argparse
import html
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCEPTED = os.path.join(ROOT, "accepted.md")
OUT = os.path.join(ROOT, "assets/pdfs/posters.typ")

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def key(s):
    """Comparison key for a title: everything but the letters and digits goes."""
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s.lower()))


# --- inputs -----------------------------------------------------------------

def read_boards(path):
    """[(board number, submission id)] from the board-assignment spreadsheet."""
    z = zipfile.ZipFile(path)
    shared = ["".join(t.text or "" for t in si.iter(M + "t"))
              for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS)]
    rows = []
    for row in ET.fromstring(z.read("xl/worksheets/sheet1.xml")).iter(M + "row"):
        cells = {}
        for c in row.findall("m:c", NS):
            v = c.find("m:v", NS)
            if v is None:
                continue
            col = re.match(r"([A-Z]+)", c.get("r")).group(1)
            cells[col] = shared[int(v.text)] if c.get("t") == "s" else v.text
        # the header row has a label in A, every poster row a board number
        if cells.get("A", "").isdigit() and cells.get("B", "").isdigit():
            rows.append((int(cells["A"]), int(cells["B"])))
    return sorted(rows)


def read_submissions(path):
    """{submission id: (title, abstract)} from the EasyChair export.

    The export is a flat text file: each submission opens with a
    "Submission #N: <title>" line, which may wrap and is underlined with '=',
    and its labelled sections ("Abstract", "Authors", …) are underlined with
    '-'.
    """
    lines = open(path, encoding="utf-8").read().split("\n")
    subs = {}
    i = 0
    while i < len(lines):
        m = re.match(r"^Submission #(\d+): (.*)$", lines[i])
        if not m:
            i += 1
            continue
        title = [m.group(2)]
        j = i + 1
        while j < len(lines) and not re.match(r"^=+\s*$", lines[j]):
            title.append(lines[j])
            j += 1
        k = j + 1
        while k < len(lines) and not re.match(r"^Submission #\d+: ", lines[k]):
            k += 1
        subs[int(m.group(1))] = (re.sub(r"\s+", " ", " ".join(title)).strip(),
                                 section(lines[j + 1:k], "Abstract"))
        i = k
    return subs


def section(lines, want):
    """The body of one labelled, dash-underlined section."""
    out, label = [], None
    n = 0
    while n < len(lines):
        nxt = lines[n + 1] if n + 1 < len(lines) else ""
        if lines[n].strip() and re.match(r"^-{3,}\s*$", nxt):
            if label == want:
                return "\n".join(out).strip()
            label, out = lines[n].strip(), []
            n += 2
            continue
        out.append(lines[n])
        n += 1
    return "\n".join(out).strip() if label == want else ""


def read_accepted():
    """{title key: (title, [authors])} for the posters listed on the website."""
    body = open(ACCEPTED, encoding="utf-8").read().split("## Posters", 1)[1]
    rows = re.findall(r"<tr>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>",
                      body, re.S)
    out = {}
    for authors, title in rows:
        title = html.unescape(title.strip())
        names = [html.unescape(a.strip()) for a in authors.strip().split("<br>")]
        out[key(title)] = (title, [n for n in names if n])
    return out


# --- turning a submitted abstract into something that can be set ------------

# The LaTeX maths these submissions actually use, rewritten into Typst maths.
MATH_SUBS = [
    (r"\\mathcal\s*\{([^}]*)\}", r"cal(\1)"),
    (r"\\mathcal\s+([A-Za-z])", r"cal(\1)"),
    (r"\\mathrm\s*\{([^}]*)\}", r'"\1"'),
    (r"\\subseteq", " subset.eq "),
    (r"\\to", " -> "),
    (r"\\!", ""),
    (r"\\,", " "),
    (r"\{([^{}]*)\}", r"\1"),       # leftover grouping braces: ^{*}, _{...}
]


def to_typst_math(m):
    """Rewrite one maths span. Anything left unrecognised raises rather than
    reaching the page as broken markup."""
    for pat, rep in MATH_SUBS:
        prev = None
        while prev != m:
            prev, m = m, re.sub(pat, rep, m)
    m = re.sub(r"\s+", " ", m).strip()
    if "\\" in m or "{" in m or "}" in m:
        raise ValueError(f"unhandled LaTeX maths: {m!r}")
    # A span with no variable in it is maths only by accident of how it was
    # typed — the star of a C*-algebra, of weak*, of a *-isomorphism. Set as
    # maths it either fails to compile (a superscript with no base) or reads
    # as an operator, so it stays in the running text.
    if not re.search(r"[A-Za-z0-9]", m):
        return m.replace("^", "")
    return "$" + m + "$"


def is_link_matter(p):
    """True for a short closing paragraph whose only point is a link to the
    full version. Such a paragraph is not part of the abstract."""
    if len(p) > 220 or not re.search(r"https?://|doi\.org|arXiv:", p):
        return False
    prose = re.sub(r"https?://\S+|arXiv:\S+", "", p)
    return len(re.findall(r"[A-Za-z]+", prose)) <= 18


def clean(text):
    """(body, note) for one submitted abstract, with its LaTeX resolved."""
    notes = []
    text = re.sub(r"\\(?:emph|textit|textbf|texttt|textsc)\s*\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\url\s*\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\footnote\s*\{(.*?)\}(?=\s|$)",
                  lambda m: notes.append(m.group(1)) or "", text, flags=re.S)
    text = re.sub(r"\\\((.*?)\\\)", lambda m: to_typst_math(m.group(1)), text, flags=re.S)
    text = re.sub(r"\$([^$]*)\$", lambda m: to_typst_math(m.group(1)), text)

    # TeX quoting: ``…'' and `…' are opening and closing marks, not backticks.
    # A pair is sometimes closed with a straight quote instead of two primes.
    text = re.sub(r"``(.*?)(?:''|\")", "“\\1”", text, flags=re.S)
    text = re.sub(r"`(.*?)'", "‘\\1’", text, flags=re.S)

    # A blank line separates paragraphs; a single newline is a soft wrap, and
    # runs of spaces — including the no-break spaces that survive a copy and
    # paste — are invisible to TeX but not to a typesetter.
    text = text.replace(" ", " ")
    paras = [p for p in (re.sub(r"[ \t]+", " ", re.sub(r"\s*\n\s*", " ", p)).strip()
                         for p in re.split(r"\n\s*\n", text)) if p]
    while paras and is_link_matter(paras[-1]):
        notes.insert(0, paras.pop())

    body = "\n\n".join(paras)
    body = re.sub(r"(?<![-\w])---(?![-\w])|(?<=\w)---(?=\w)", "\u2014", body)
    body = re.sub(r"(?<=\w)--(?=\w)|(?<![-:/\w])--(?![-\w])", "\u2013", body)
    # every dollar left is one of ours, delimiting a maths span; an odd count
    # would mean an author typed a stray one, which the booklet would then set
    # as maths from there to the end of the paragraph
    for p in body.split("\n\n"):
        if p.count("$") % 2:
            raise ValueError(f"unpaired $ in: {p!r}")
    return body, re.sub(r"\s+", " ", " ".join(notes)).strip()


# A note is the author's own aside, so it is printed as written; these few are
# rephrased to read as the booklet's other source lines do, and the bare link
# to a personal file share is dropped, being of no use on paper.
NOTES = {
    13: "Full version: https://doi.org/10.1103/29z2-15bm",
    55: "Full version: https://arxiv.org/abs/2510.20452",
    90: "Author's footnote: refer to https://doi.org/10.48550/arXiv.quant-ph/0104027",
    170: "See arXiv:2410.09226 (not the most recent version; recently submitted to Quantum).",
    176: None,
}


# --- output -----------------------------------------------------------------

def tstr(s):
    """A Typst string literal. Nothing in the submitted text can escape it, so
    nothing in it can be reinterpreted as Typst markup."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


HEADER = '''// Auto-generated by scripts/gen_posters.py.
// The abstracts of the posters presented at the poster session, in the order
// of the boards they hang on. Bodies come from the abstract each submission
// was entered with; titles and author lists come from accepted.md, so the
// booklet and the website list the same posters the same way.
// Included via `#include`, which gives this file its own scope, so it repeats
// the few styles it needs rather than sharing them with the program file.

#let c-band  = rgb("#dfeefa")
#let c-title = rgb("#7e1b1b")

// Titles, authors and abstract bodies arrive as plain strings, so nothing in
// the submitted text can be reinterpreted as Typst markup. The one exception
// is maths: the generator rewrites each span an author typed in LaTeX into
// Typst maths source and returns it between dollars, which `eval` sets rather
// than printing verbatim. It emits no other dollar sign, so the split below
// is always balanced; a span is boxed so it is not broken across lines.
#let setmaths(s) = {
  let parts = s.split("$")
  assert(calc.odd(parts.len()), message: "unbalanced $ in: " + s)
  let out = ()
  for (i, part) in parts.enumerate() {
    out.push(if calc.even(i) { part } else { box(eval(part, mode: "math")) })
  }
  out.join()
}

// A body that keeps its own paragraphs separates them with a blank line.
#let posterbody(body) = {
  show "⅋": $amp.inv$
  show "⊗": $times.o$
  show "⊢": $tack$
  for (i, p) in body.split("\\n\\n").enumerate() {
    if i > 0 { v(0.4em) }
    par(justify: true, text(size: 9.5pt, setmaths(p)))
  }
}

#let posterentry(board: "", title: "", authors: "", body: "", note: none) = block(
  width: 100%, above: 0.9em, below: 0.9em, breakable: true,
  {
    text(size: 8.5pt, fill: rgb("#5f6875"), board)
    linebreak()
    text(size: 10.5pt, weight: "bold", fill: c-title, title)
    linebreak()
    text(size: 9pt, style: "italic", authors)
    v(0.3em)
    posterbody(body)
    // the author's own pointer to the full version, kept out of the body
    if note != none {
      v(0.15em)
      text(size: 8pt, style: "italic", fill: rgb("#5f6875"), note)
    }
  })

#pagebreak()

= Poster abstracts

All posters are presented at the poster session on Tuesday, August 18th, 17:30 -- 19:30,
in the central hall on the first floor of the A-building. Each poster hangs on the
numbered board given with its abstract below, and the abstracts run in board order.
'''


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("abstracts", help="EasyChair abstract export (.txt)")
    ap.add_argument("boards", help="board-assignment spreadsheet (.xlsx)")
    ap.add_argument("-o", "--out", default=OUT)
    args = ap.parse_args()

    boards = read_boards(args.boards)
    subs = read_submissions(args.abstracts)
    accepted = read_accepted()

    # one entry per submission, keeping every board it occupies
    order, seen = [], {}
    for board, sid in boards:
        if sid not in seen:
            seen[sid] = []
            order.append(sid)
        seen[sid].append(board)

    missing = [sid for sid in order if sid not in subs]
    if missing:
        sys.exit(f"not in the abstract export: submission(s) {missing}")

    out, unlisted = [HEADER], []
    for sid in order:
        # accepted.md records no submission ids, so the two are matched on the
        # title the poster was submitted under
        submitted_title, abstract = subs[sid]
        listing = accepted.get(key(submitted_title))
        if listing is None:
            unlisted.append((sid, submitted_title))
            continue
        title, authors = listing
        body, note = clean(abstract)
        note = NOTES[sid] if sid in NOTES else (note or None)
        bs = seen[sid]
        label = f"Board {bs[0]}" if len(bs) == 1 else f"Boards {bs[0]} – {bs[-1]}"
        fields = [f"  board: {tstr(label)},",
                  f"  title: {tstr(title)},",
                  f"  authors: {tstr(', '.join(authors))},",
                  f"  body: {tstr(body)},"]
        if note:
            fields.append(f"  note: {tstr(note)},")
        out.append("#posterentry(\n" + "\n".join(fields) + "\n)\n")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"{len(out) - 1} posters over {len(boards)} boards -> "
          f"{os.path.relpath(args.out, ROOT)}")
    for sid, title in unlisted:
        print(f"  skipped #{sid}: not listed under ## Posters in accepted.md — {title}")


if __name__ == "__main__":
    main()
