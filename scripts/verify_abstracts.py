#!/usr/bin/env python3
"""Check every abstract printed in the QPL 2026 program against its original.

The program booklet (assets/pdfs/QPL_2026_Program.pdf) is typeset from
assets/pdfs/abstracts.typ, whose bodies were lifted from two places: the front
matter of the submitted paper in assets/submissions/, and — where the
submission carries no abstract — the paper's arXiv version.

This script re-derives both originals and compares them with what the program
actually prints.  An abstract that matches *either* original is left alone; one
that matches neither is rewritten with an exact copy of the original, preferring
the submitted paper and falling back to arXiv.  The provenance footnote
("Abstract from the arXiv version, arXiv:…") is kept in step with the body.

    ./scripts/verify_abstracts.py              # report only
    ./scripts/verify_abstracts.py --diff       # report + show what differs
    ./scripts/verify_abstracts.py --apply      # rewrite abstracts.typ

After --apply, re-typeset the booklet:

    cd assets/pdfs && typst compile QPL_2026_Program.typ

Talks are matched to their submission through the schedule tables in
program.md, so the two stay in step automatically.  arXiv ids live in
scripts/arxiv-ids.json (fuzzy title/author matches from the original build,
verified by hand) and fetched abstracts are cached in
scripts/arxiv-abstracts.json so a re-check needs no network.

Requires PyMuPDF (`pip install pymupdf`).
"""
import argparse
import difflib
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.request

import abstract_extract as X

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TYP = os.path.join(ROOT, "assets/pdfs/abstracts.typ")
PROGRAM = os.path.join(ROOT, "program.md")
IDS = os.path.join(HERE, "arxiv-ids.json")
CACHE = os.path.join(HERE, "arxiv-abstracts.json")
PINS = os.path.join(HERE, "abstract-pins.json")

ARXIV_API = "http://export.arxiv.org/api/query"
SOURCE_NOTE = "Abstract from the arXiv version, arXiv:{}."


# --------------------------------------------------------------------------
# comparing two renderings of the same paragraph
# --------------------------------------------------------------------------

def cmp_key(s):
    """Fold away everything a PDF extractor or a TeX-to-text pass can change:
    ligatures, hyphenation, quote and dash shapes, maths delimiters, case."""
    s = unicodedata.normalize("NFKC", s or "")
    for k, v in X.LIGATURES.items():
        s = s.replace(k, v)
    s = re.sub(r'[^0-9a-z]+', ' ', s.lower())
    return " ".join(s.split())


def same(a, b):
    return bool(a) and bool(b) and cmp_key(a) == cmp_key(b)


def ratio(a, b):
    return difflib.SequenceMatcher(None, cmp_key(a), cmp_key(b)).ratio()


# --------------------------------------------------------------------------
# abstracts.typ  <->  structured entries
# --------------------------------------------------------------------------

def typst_quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def read_string(text, i):
    """Read a Typst string literal starting at text[i] == '\"'; return (value, i)."""
    out, i = [], i + 1
    while i < len(text):
        c = text[i]
        if c == "\\":
            out.append(text[i + 1])
            i += 2
        elif c == '"':
            return "".join(out), i + 1
        else:
            out.append(c)
            i += 1
    raise ValueError("unterminated string in abstracts.typ")


def split_args(text):
    """Split an argument list on top-level commas, honouring string literals."""
    args, depth, start, i = [], 0, 0, 0
    while i < len(text):
        c = text[i]
        if c == '"':
            _, i = read_string(text, i)
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == "," and depth == 0:
            args.append(text[start:i])
            start = i + 1
        i += 1
    if text[start:].strip():
        args.append(text[start:])
    return args


def parse_value(text, lets):
    """Evaluate a `body:`/`title:`/… value.

    Returns (text, markup) where markup is True if the value splices in one of
    the file's content variables — those carry formatting a plain string cannot,
    so such an entry is reported but never rewritten automatically.
    """
    parts, markup, i = [], False, 0
    while i < len(text):
        c = text[i]
        if c.isspace() or c == "+":
            i += 1
            continue
        if c == '"':
            s, i = read_string(text, i)
            parts.append(s)
            continue
        m = re.match(r'[A-Za-z_][\w-]*', text[i:])
        if not m:
            raise ValueError(f"cannot parse value: {text[i:i + 40]!r}")
        name = m.group(0)
        i += len(name)
        if name == "none" and not parts:
            return None, False
        if name not in lets:
            raise ValueError(f"unknown identifier {name!r} in abstracts.typ")
        parts.append(lets[name])
        markup = True
    return "".join(parts), markup


def parse_lets(lines):
    """Plain-text rendering of the file's `#let name = [content]` variables."""
    lets = {}
    for l in lines:
        m = re.match(r'#let\s+([A-Za-z_][\w-]*)\s*=\s*\[(.*)\]\s*$', l)
        if m:
            lets[m.group(1)] = re.sub(r'#\w+\[(.*?)\]', r'\1', m.group(2))
    return lets


def parse_typ(path):
    """Every #absentry(...) block, with the line span it occupies."""
    lines = open(path, encoding="utf-8").read().split("\n")
    lets = parse_lets(lines)
    entries = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#absentry("):
            j = i + 1
            while j < len(lines) and lines[j].rstrip() != ")":
                j += 1
            if j >= len(lines):
                raise ValueError(f"unterminated #absentry( at line {i + 1}")
            body = "\n".join(lines[i:j + 1])[len("#absentry("):-1]
            fields, markup = {}, {}
            for arg in split_args(body):
                m = re.match(r'\s*([A-Za-z_][\w-]*)\s*:(.*)', arg, re.S)
                if not m:
                    raise ValueError(f"cannot parse argument {arg!r} at line {i + 1}")
                fields[m.group(1)], markup[m.group(1)] = parse_value(m.group(2), lets)
            entries.append(dict(lo=i, hi=j, fields=fields,
                                markup=any(markup.values())))
            i = j + 1
        else:
            i += 1
    return lines, entries


def render_entry(f):
    """An #absentry block, in the layout the generator emits."""
    out = ["#absentry(",
           f'  time: {typst_quote(f["time"])},',
           f'  title: {typst_quote(f["title"])},',
           f'  authors: {typst_quote(f["authors"])},']
    if f.get("body"):
        out.append(f'  body: {typst_quote(f["body"])},')
        if f.get("source"):
            out.append(f'  source: {typst_quote(f["source"])},')
    else:
        out.append("  body: none,")
        out.append(f'  note: {typst_quote(f.get("note") or "")},')
    out.append(")")
    return out


# --------------------------------------------------------------------------
# program.md schedule -> which paper each talk is
# --------------------------------------------------------------------------

def strip_tags(s):
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()


def parse_schedule(path):
    """Ordered talks with their submission link, from the schedule tables."""
    txt = open(path, encoding="utf-8").read()
    days = re.findall(
        r'<details class="day-section"[^>]*data-date="([\d-]+)"[^>]*>\s*'
        r'<summary>([^<]+)</summary>(.*?)\n</details>', txt, re.S)
    talks = []
    for date, dayname, body in days:
        for tbl in re.findall(r'<table class="schedule-table">(.*?)</table>', body, re.S):
            headers, band = None, None
            for attrs, row in re.findall(r'<tr([^>]*)>(.*?)</tr>', tbl, re.S):
                cells = re.findall(r'<td([^>]*)>(.*?)</td>', row, re.S)
                if not cells:
                    continue
                if len(cells) == 1 and 'class="band"' in cells[0][0] and 'colspan' in cells[0][0]:
                    band = strip_tags(cells[0][1])
                    continue
                if len(cells) > 1 and all('class="band"' in c[0] for c in cells):
                    headers, band = [strip_tags(c[1]) for c in cells], "Parallel sessions"
                    continue
                if 'session-chair' in attrs:
                    continue
                if len(cells) == 1 and 'break-row' in cells[0][0]:
                    continue
                slot = strip_tags(cells[0][1])
                for ci, (cattr, cell) in enumerate(cells[1:], start=1):
                    if 'break-row' in cattr:
                        continue
                    title = re.search(r'<span class="talk-title">(.*?)</span>', cell, re.S)
                    if not title:
                        continue
                    authors = re.search(r'<span class="talk-authors">(.*?)</span>', cell, re.S)
                    links = re.findall(r'href="([^"]+)"', title.group(1))
                    titles = re.findall(r'<a [^>]*>(.*?)</a>', title.group(1), re.S) \
                        or [strip_tags(title.group(1))]
                    track = headers[ci] if headers and ci < len(headers) else ""
                    for k, ttl in enumerate(titles):
                        talks.append(dict(
                            date=date, day=dayname, band=band, track=track, time=slot,
                            authors=strip_tags(authors.group(1)) if authors else "",
                            title=strip_tags(ttl),
                            pdf=links[k] if k < len(links) else None))
    return talks


def slot_key(t):
    """The `time:` string the generator writes, used to line talks up with entries."""
    return t["time"] + (" · " + t["track"] if t["track"] else "")


# --------------------------------------------------------------------------
# arXiv
# --------------------------------------------------------------------------

STOP_TITLE = re.compile(r'\$[^$]*\$')


def title_score(a, b):
    def n(s):
        return " ".join(re.sub(r'[^a-z0-9 ]', ' ', STOP_TITLE.sub(' ', s or "").lower()).split())
    return difflib.SequenceMatcher(None, n(a), n(b)).ratio()


def surnames(s):
    out = set()
    for part in re.split(r',| and ', s or ""):
        toks = [t for t in re.split(r'\s+', part.strip()) if len(t) > 2]
        if toks:
            out.add(re.sub(r'[^A-Za-z]', '', toks[-1]).lower())
    return {x for x in out if len(x) > 2}


def author_score(a, b):
    x, y = surnames(a), surnames(b)
    return len(x & y) / max(1, min(len(x), len(y)))


def arxiv_fetch(ids, cache, sleep=3.0):
    """Fill `cache` with {id: {title, abstract}} for any id not already there."""
    todo = [i for i in ids if i not in cache]
    for k in range(0, len(todo), 25):
        batch = todo[k:k + 25]
        url = f"{ARXIV_API}?id_list={','.join(batch)}&max_results={len(batch)}"
        print(f"  fetching {len(batch)} abstract(s) from arXiv…", file=sys.stderr)
        with urllib.request.urlopen(url, timeout=60) as r:
            xml = r.read().decode("utf-8", "replace")
        for e in re.findall(r'<entry>(.*?)</entry>', xml, re.S):
            def field(tag):
                m = re.search(rf'<{tag}>(.*?)</{tag}>', e, re.S)
                return html.unescape(" ".join(m.group(1).split())) if m else ""
            m = re.search(r'(\d{4}\.\d{4,5})', field("id"))
            if m:
                cache[m.group(1)] = dict(
                    title=field("title"), abstract=field("summary"),
                    authors=", ".join(html.unescape(" ".join(a.split())) for a in
                                      re.findall(r'<author>\s*<name>(.*?)</name>', e, re.S)))
        if k + 25 < len(todo):
            time.sleep(sleep)
    return cache


# --------------------------------------------------------------------------
# the check
# --------------------------------------------------------------------------

def load(path, default):
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else default


def save(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="rewrite abstracts.typ (default: report only)")
    ap.add_argument("--diff", action="store_true",
                    help="show a word diff for each abstract that matches neither original")
    ap.add_argument("--only", metavar="SUBSTR",
                    help="restrict to talks whose title contains SUBSTR")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="also list the abstracts that check out")
    ap.add_argument("--discover-arxiv", action="store_true",
                    help="scan submissions for arXiv ids not yet in arxiv-ids.json")
    ap.add_argument("--refresh-arxiv", action="store_true",
                    help="re-fetch every arXiv abstract instead of using the cache")
    ap.add_argument("--typ", default=TYP)
    ap.add_argument("--program", default=PROGRAM)
    args = ap.parse_args()

    lines, entries = parse_typ(args.typ)
    talks = parse_schedule(args.program)
    ids = load(IDS, {})
    cache = {} if args.refresh_arxiv else load(CACHE, {})
    pins = {p["pdf"]: p.get("reason", "pinned") for p in load(PINS, [])}

    by_slot = {}
    for t in talks:
        by_slot.setdefault((slot_key(t), cmp_key(t["title"])), []).append(t)

    # pair each entry with its talk
    for e in entries:
        f = e["fields"]
        hits = by_slot.get((f["time"], cmp_key(f["title"])), [])
        e["talk"] = hits[0] if len(hits) == 1 else None
        e["pdf"] = e["talk"]["pdf"] if e["talk"] else None

    todo = [e for e in entries
            if not args.only or args.only.lower() in e["fields"]["title"].lower()]

    if args.discover_arxiv:
        # An id printed on the paper is a candidate, not a fact: the front matter
        # may be citing somebody else's preprint. Anything but arXiv's own stamp
        # has to agree with the talk's title or author list before we trust it.
        cand = {}
        for e in todo:
            pdf = e["pdf"]
            if not pdf or pdf in ids or not pdf.startswith("/assets/"):
                continue
            aid, how = X.arxiv_id_in(ROOT + pdf)
            if aid:
                cand[pdf] = (aid, how, e)
        if cand:
            arxiv_fetch(sorted({a for a, _, _ in cand.values()}), cache)
            save(CACHE, cache)
        kept = 0
        for pdf, (aid, how, e) in sorted(cand.items()):
            meta = cache.get(aid) or {}
            ts = title_score(e["fields"]["title"], meta.get("title"))
            asc = author_score(e["fields"]["authors"], meta.get("authors"))
            ok = how == "arxiv-stamp" or ts >= .82 or (ts >= .5 and asc >= .67)
            print(f"  {'keep' if ok else 'drop'}  arXiv:{aid} ({how}, title {ts:.2f}, "
                  f"authors {asc:.2f})  {e['fields']['title'][:52]}", file=sys.stderr)
            if ok:
                ids[pdf] = dict(arxiv=aid, found_by=how, arxiv_title=meta.get("title"),
                                title_score=round(ts, 3), author_score=round(asc, 2))
                kept += 1
        print(f"discovered {kept} new arXiv id(s) from {len(cand)} candidate(s)", file=sys.stderr)
        save(IDS, ids)

    wanted = {ids[e["pdf"]]["arxiv"] for e in todo if e["pdf"] in ids}
    if wanted:
        arxiv_fetch(sorted(wanted), cache)
        save(CACHE, cache)

    edits, report = {}, []
    for e in todo:
        f, pdf = e["fields"], e["pdf"]
        title = f["title"]
        rec = dict(entry=e, title=title, time=f["time"], pdf=pdf)

        if pdf is None:
            rec.update(state="unmatched",
                       detail="no talk in program.md with this title and time slot")
            report.append(rec)
            continue

        sub, how = (None, "external link, not a local submission")
        if pdf.startswith("/assets/"):
            try:
                sub, how = X.extract(ROOT + pdf)
            except Exception as exc:                       # a corrupt or image-only PDF
                sub, how = None, f"{type(exc).__name__}: {exc}"
        aid = ids.get(pdf, {}).get("arxiv")
        arx = (cache.get(aid) or {}).get("abstract") if aid else None
        rec.update(sub=sub, how=how, arxiv=aid, arx=arx)

        cur = f.get("body")
        if not cur:
            # an entry the booklet prints as "[No abstract - …]"
            best = sub or arx
            rec.update(state="still-missing" if not best else "now-available",
                       detail=how if not best else
                       ("the submission now yields an abstract" if sub else
                        f"arXiv:{aid} now has an abstract"))
            if best:
                nf = dict(f, body=best,
                          source=None if sub else SOURCE_NOTE.format(aid))
                nf.pop("note", None)
                edits[e["lo"]] = (e, nf)
            report.append(rec)
            continue

        if pdf in pins:
            rec.update(state="pinned", detail=pins[pdf])
            report.append(rec)
            continue

        matches_sub, matches_arx = same(cur, sub), same(cur, arx)
        if matches_sub or matches_arx:
            origin = "submission" if matches_sub else f"arXiv:{aid}"
            rec["origin"] = "submission" if matches_sub else "arXiv"
            want_source = None if matches_sub else SOURCE_NOTE.format(aid)
            if (f.get("source") or None) != want_source:
                rec.update(state="relabel", detail=f"body is the {origin} text, "
                           f"but the footnote says {f.get('source') or 'nothing'}")
                edits[e["lo"]] = (e, dict(f, source=want_source))
            else:
                rec.update(state="ok", detail=f"matches the {origin} abstract")
            report.append(rec)
            continue

        if sub is None and arx is None:
            rec.update(state="no-original",
                       detail=f"nothing to compare against ({how}"
                              + ("" if aid else "; no arXiv id known") + ")")
            report.append(rec)
            continue

        if e["markup"]:
            rec.update(state="manual",
                       detail="body splices in a formatted variable; fix by hand")
            report.append(rec)
            continue

        best = sub if sub else arx
        rec.update(state="mismatch", replacement=best,
                   detail=f"replaced with the {'submission' if sub else f'arXiv:{aid}'} abstract "
                          f"(closest match {max(ratio(cur, sub or ''), ratio(cur, arx or '')):.2f})")
        nf = dict(f, body=best, source=None if sub else SOURCE_NOTE.format(aid))
        edits[e["lo"]] = (e, nf)
        report.append(rec)

    # ---- report ----------------------------------------------------------
    order = ["mismatch", "now-available", "relabel", "manual", "unmatched",
             "no-original", "still-missing", "pinned", "ok"]
    counts = {s: 0 for s in order}
    for r in report:
        counts[r["state"]] += 1

    for state in order:
        rows = [r for r in report if r["state"] == state]
        if not rows or (state == "ok" and not args.verbose):
            continue
        print(f"\n=== {state}  ({len(rows)}) ===")
        for r in rows:
            print(f"  {r['time']:<28} {r['title'][:70]}")
            print(f"      {r['detail']}")
            if args.diff and state == "mismatch":
                a = (r["entry"]["fields"]["body"] or "").split()
                b = r["replacement"].split()
                d = [w for w in difflib.ndiff(a, b) if w[0] in "-+"]
                head = " ".join(d[:60])
                print(f"      diff: {head}{' …' if len(d) > 60 else ''}")

    print(f"\n{len(todo)} abstract entries checked")
    for state in order:
        if not counts[state]:
            continue
        note = ""
        if state == "ok":
            n_sub = sum(1 for r in report if r["state"] == "ok" and r.get("origin") == "submission")
            note = f"  ({n_sub} match the submission, {counts[state] - n_sub} match arXiv)"
        print(f"  {counts[state]:3d}  {state}{note}")
    n_arx = sum(1 for r in report if r.get("arxiv"))
    print(f"       {n_arx}/{len(todo)} talks have a known arXiv version to cross-check against")

    # ---- apply -----------------------------------------------------------
    if not edits:
        print("\nnothing to change.")
        return 0
    if not args.apply:
        print(f"\n{len(edits)} entr{'y' if len(edits) == 1 else 'ies'} would change; "
              f"re-run with --apply to write {os.path.relpath(args.typ, ROOT)}.")
        return 1

    out, i = [], 0
    while i < len(lines):
        if i in edits:
            e, nf = edits[i]
            out += render_entry(nf)
            i = e["hi"] + 1
        else:
            out.append(lines[i])
            i += 1
    with open(args.typ, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"\nwrote {os.path.relpath(args.typ, ROOT)} ({len(edits)} entries updated).")
    print("re-typeset with:  cd assets/pdfs && typst compile QPL_2026_Program.typ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
