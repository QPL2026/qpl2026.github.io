#!/usr/bin/env python3
"""Pull the abstract out of a submitted paper's front matter.

The submissions are author-formatted PDFs with no common template, so the
abstract is found geometrically rather than by markup: first an explicit
"Abstract" label, and failing that the first prose block on page 1 that is set
apart from the body text (indented, narrower, smaller, or italic) and sits
above the first section heading.

`extract(path)` returns `(text, how)`; `text` is None when the paper carries no
abstract of its own, with `how` explaining why.

Requires PyMuPDF (`pip install pymupdf`).
"""
import collections
import re
import statistics

import fitz

LIGATURES = {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl', 'ĳ': 'ij', '\xad': ''}

HEADING = re.compile(
    r'^\s*(?:'
    r'(?:\d+|[IVXL]+)[\.\)]?\s*[A-Z].{0,70}$'
    r'|(?:Introduction|INTRODUCTION|Preliminaries|PRELIMINARIES|Background|BACKGROUND|Motivation'
    r'|Overview|Contents|References|Acknowledgements?|Keywords?|Summary|Results|Discussion)\s*:?\s*$'
    r')')
TRAILING_HEAD = re.compile(
    r'\s+(?:\d+|[IVXL]+)[\.\)]?\s*'
    r'(?:Introduction|Preliminaries|Background|Motivation|Overview|Context)\b[^.]{0,50}$', re.I)
AFFIL_LINE = re.compile(
    r'@|\b(?:University|Universit|Universite|Universidad|Institut|Department|Dept\.|'
    r'Laborator|CNRS|Inria|INRIA|Centre|Center|College|School|Academy|Faculty|Ltd|Inc\.|GmbH|LLC|'
    r'Perimeter|Quantinuum|Google|IBM|Microsoft|Amazon|Xanadu|PsiQuantum|Riverlane)\b'
    r'|\b(?:Netherlands|France|Germany|Canada|Poland|Austria|Japan|China|Italy|Spain|Sweden|Denmark|'
    r'Norway|Finland|Belgium|Switzerland|Australia|Brazil|India|Israel|Singapore|Portugal|Czech|'
    r'Slovakia|Hungary|Greece|Ireland|Scotland|England|Mexico|Chile|Korea|Taiwan|Russia|Turkey|'
    r'United States|United Kingdom|USA|U\.S\.A\.|UK|U\.K\.)\s*$', re.I)
JUNK_LINE = re.compile(
    r'^\s*(?:Submitted to:?.*|©.*|Copyright.*|This work is licensed.*|EPTCS.*|'
    r'Creative Commons.*|arXiv:\S+.*|(?:(?:The|Full) (?:article|paper|full version|version).{0,80}'
    r'(?:available|found) at\s*\S+\.?)|Full paper available.*|[-–—\s]*Non-Proceedings Submission[-–—\s]*|'
    r'Preprint.*|To appear.*|\d{1,3}|[ivxlIVXL]{1,5}|.{0,3})\s*$')
POINTER_NOTE = re.compile(
    r'^.{0,140}?\b(?:manuscript|full (?:version|paper)|extended abstract|article|preprint)\b'
    r'.{0,80}?\b(?:can be found|is available|available at|follow|accompan)', re.I | re.S)
SENT_END = re.compile(r'[.!?][”"\')\]]?\s*$')

ARXIV_ID = re.compile(r'(?:arxiv[.:\s/]*(?:org/(?:abs|pdf)/)?)(\d{4}\.\d{4,5})(?:v\d+)?', re.I)
ARXIV_STAMP = re.compile(r'arXiv:(\d{4}\.\d{4,5})v?\d*\s*\[', re.I)


def norm(s):
    """Collapse a PDF text block to one line, undoing ligatures and hyphenation."""
    for k, v in LIGATURES.items():
        s = s.replace(k, v)
    s = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', s)
    s = re.sub(r'\s*\n\s*', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def head_of(b):
    return norm(b["text"])


def is_heading(b):
    """Section headings are short and comma-free; affiliation lines like
    '4Spotify, Dublin, Ireland.' otherwise match the numbered-heading pattern."""
    t = head_of(b)
    return bool(HEADING.match(t)) and "," not in t and "@" not in t


def blocks_of(page):
    """Page text as geometry-carrying blocks, in reading order."""
    out = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        lines, sizes, nital, ntot = [], [], 0, 0
        for l in b["lines"]:
            lines.append("".join(s["text"] for s in l["spans"]))
            for s in l["spans"]:
                n = max(1, len(s["text"].strip()))
                sizes += [round(s["size"], 1)] * n
                ntot += n
                if "Italic" in s["font"] or "Oblique" in s["font"]:
                    nital += n
        t = "\n".join(lines)
        if not t.strip():
            continue
        x0, y0, x1, y1 = b["bbox"]
        out.append(dict(text=t, lines=lines, size=statistics.median(sizes) if sizes else 0,
                        x0=x0, x1=x1, y0=y0, y1=y1, w=x1 - x0,
                        italic=(nital / ntot > .6) if ntot else False, n=len(t.strip())))
    out.sort(key=lambda b: (round(b["y0"] / 3), b["x0"]))
    return out


def two_column(page, bs):
    """x of the column gutter, or None on a single-column page."""
    pw = page.rect.width
    cols = [b for b in bs if b["n"] >= 150 and b["w"] < pw * .62]
    if len(cols) < 3:
        return None
    left = [b for b in cols if b["x0"] < pw * .45]
    right = [b for b in cols if b["x0"] > pw * .45]
    return pw * .45 if len(left) >= 2 and len(right) >= 2 else None


def body_geom(doc):
    """Typical size/width/left edge of body text, measured away from page 1."""
    cand = []
    for pno in range(1, min(len(doc), 5)):
        cand += [b for b in blocks_of(doc[pno]) if b["n"] >= 250]
    if not cand:
        cand = [b for b in blocks_of(doc[0]) if b["n"] >= 250]
    if not cand:
        return None
    size = collections.Counter(round(b["size"], 1) for b in cand).most_common(1)[0][0]
    same = [b for b in cand if abs(b["size"] - size) < .35] or cand
    return dict(size=size, w=statistics.median([b["w"] for b in same]),
                x0=statistics.median([b["x0"] for b in same]))


def is_affil_block(b):
    ls = [l for l in b["lines"] if l.strip()]
    return bool(ls) and sum(1 for l in ls if AFFIL_LINE.search(l)) >= max(1, len(ls) * .5)


def strip_front_junk(lines):
    out = list(lines)
    while out and (JUNK_LINE.match(out[0]) or (AFFIL_LINE.search(out[0]) and len(out[0]) < 90)):
        out.pop(0)
    return out


def tidy(t):
    t = TRAILING_HEAD.sub('', t).strip()
    if not SENT_END.search(t):                      # trim a dangling partial sentence
        cut = max(t.rfind('. '), t.rfind('? '), t.rfind('! '))
        if cut > len(t) * .5:
            t = t[:cut + 1]
    return t.strip()


def extract(path):
    """(abstract, how) for a submitted paper; abstract is None when it has none."""
    doc = fitz.open(path)
    page = doc[0]
    bs = blocks_of(page)
    if not bs:
        return None, "no-text"
    g = body_geom(doc)
    H, mid = page.rect.height, two_column(page, bs)
    title_size = max(b["size"] for b in bs[:5])

    def candidate_ok(b):
        """Abstract candidates are full-width or left-column, never right-column."""
        return mid is None or b["x0"] < mid or b["w"] > page.rect.width * .62

    # 1 -- explicitly labelled "Abstract"
    for i, b in enumerate(bs[:20]):
        m = re.match(r'\s*(?:\d+\s*)?(?:ABSTRACT|Abstract)\b\s*[\.\:\—\-–]?\s*', b["text"])
        if not m:
            continue
        rest = b["text"][m.end():].strip()
        chunk, j, blocked = ([rest] if len(rest) > 40 else []), i + 1, False
        while j < len(bs) and not chunk:
            # a section heading before any abstract text means this "Abstract" was
            # only a subtitle (e.g. "Abstract for QPL 2026 based on [1]")
            if is_heading(bs[j]):
                blocked = True
                break
            if bs[j]["n"] > 40 and candidate_ok(bs[j]):
                chunk.append(norm("\n".join(strip_front_junk(bs[j]["lines"]))))
            j += 1
        if blocked:
            continue
        base = bs[j - 1] if j - 1 < len(bs) else b
        while j < len(bs) and bs[j]["n"] > 150 and candidate_ok(bs[j]) \
                and abs(bs[j]["size"] - base["size"]) < .4 \
                and abs(bs[j]["x0"] - base["x0"]) < 6 and abs(bs[j]["w"] - base["w"]) < 20 \
                and bs[j]["y0"] - bs[j - 1]["y1"] < 40 \
                and not is_heading(bs[j]):
            chunk.append(norm(bs[j]["text"]))
            j += 1
        t = tidy(norm(" ".join(chunk)))
        if len(t) > 80:
            return t, "labelled"

    # 2 -- unlabelled: the first prose block that is set apart from body text
    first_head = None
    for i, b in enumerate(bs):
        if b["n"] < 150 and is_heading(b) and b["y0"] < H * .8:
            first_head = i
            break

    for i, b in enumerate(bs):
        if b["y0"] > H * .75:
            continue
        if b["size"] >= title_size - .2:
            continue
        if is_affil_block(b):
            continue
        # a section heading before any abstract => the paper opens straight into the body
        if b["n"] < 200:
            if is_heading(b) and not JUNK_LINE.match(head_of(b)):
                return None, "no-abstract (opens with section heading '%s')" % head_of(b)[:40]
            continue
        if not candidate_ok(b):
            continue
        if is_heading(b):
            return None, "no-abstract (opens with a section heading)"
        txt = norm("\n".join(strip_front_junk(b["lines"])))
        if len(txt) < 200:
            continue

        if g:
            tests = [("indent", b["x0"] > g["x0"] + 8), ("narrow", b["w"] < g["w"] - 15),
                     ("wide", b["w"] > g["w"] * 1.35), ("smallfont", b["size"] < g["size"] - .3),
                     ("italic", b["italic"])]
            why = ",".join(k for k, v in tests if v)
            distinct = bool(why)
        else:
            distinct, why = True, "no-body-ref"

        pre_intro = False
        if first_head is not None and i < first_head:
            n_prose = sum(1 for k, bb in enumerate(bs) if k < first_head and bb["n"] >= 200
                          and not is_affil_block(bb) and bb["size"] < title_size - .2
                          and candidate_ok(bb))
            pre_intro = (n_prose <= 1) and not POINTER_NOTE.match(txt)
        if not distinct and not pre_intro:
            return None, "no-abstract (first prose block is body text)"
        if POINTER_NOTE.match(txt):
            return None, "no-abstract (front matter is a pointer to the full paper)"
        tag = why if distinct else "pre-intro"

        chunk, j = [txt], i + 1
        lim = first_head if first_head is not None else len(bs)
        while j < lim and bs[j]["n"] > 150 and candidate_ok(bs[j]) \
                and abs(bs[j]["size"] - b["size"]) < .35 \
                and abs(bs[j]["x0"] - b["x0"]) < 6 and abs(bs[j]["w"] - b["w"]) < 20 \
                and bs[j]["y0"] - bs[j - 1]["y1"] < 40 \
                and not is_heading(bs[j]):
            chunk.append(norm(bs[j]["text"]))
            j += 1
        return tidy(" ".join(chunk)), f"unlabelled[{tag}]"
    return None, "no-abstract (no candidate block)"


def arxiv_id_in(path):
    """(id, how) if the paper itself names an arXiv id, else (None, None).

    Only page-1 front matter is searched: a reference list is full of *other*
    papers' arXiv ids.
    """
    doc = fitz.open(path)
    page = doc[0]
    m = ARXIV_STAMP.search(page.get_text())      # the vertical arXiv stamp is definitive
    if m:
        return m.group(1), "arxiv-stamp"
    bs = blocks_of(page)
    ycut = page.rect.height
    for b in bs:
        if b["n"] < 150 and is_heading(b) and b["y0"] < page.rect.height * .8:
            ycut = b["y0"]
            break
    m = ARXIV_ID.search(" ".join(b["text"] for b in bs if b["y0"] <= ycut))
    if m:
        return m.group(1), "front-matter"
    meta = " ".join(str(v) for v in (doc.metadata or {}).values() if v)
    m = ARXIV_ID.search(meta)
    return (m.group(1), "pdf-metadata") if m else (None, None)
