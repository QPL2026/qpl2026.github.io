# scripts

Maintenance scripts for the QPL 2026 program booklet.

## verify_abstracts.py

Checks every abstract printed in `assets/pdfs/QPL_2026_Program.pdf` against its
original, and repairs the ones that have drifted.

The booklet is typeset from `assets/pdfs/abstracts.typ`, whose bodies were
lifted from the front matter of the submitted papers in `assets/submissions/`
and — where a submission carries no abstract — from the paper's arXiv version.
The script re-derives both originals and compares. An abstract that matches
*either* one is left alone; one that matches neither is replaced with an exact
copy of the original, preferring the submitted paper and falling back to arXiv.
The "Abstract from the arXiv version, arXiv:…" footnote is kept in step with
the body it labels.

Comparison ignores what a PDF extractor can legitimately change — ligatures,
hyphenation across line breaks, quote and dash shapes, `$…$` delimiters, case
and whitespace — so only a real difference in wording counts as a mismatch.

```sh
pip install pymupdf

./scripts/verify_abstracts.py            # report only; exit 1 if anything would change
./scripts/verify_abstracts.py --diff     # report + word diff for each mismatch
./scripts/verify_abstracts.py -v         # also list the abstracts that check out
./scripts/verify_abstracts.py --apply    # rewrite abstracts.typ

cd assets/pdfs && typst compile QPL_2026_Program.typ   # after --apply
```

Talks are matched to their submission through the schedule tables in
`program.md`, so re-scheduling a talk or swapping its PDF link needs no change
here.

### Outcomes

| state | meaning |
| --- | --- |
| `ok` | matches the submission or the arXiv version |
| `mismatch` | matches neither — rewritten with the original |
| `relabel` | body is right but the arXiv footnote is missing, stale, or spurious |
| `now-available` | printed as "[No abstract]" but a source has since appeared — filled in |
| `still-missing` | no abstract in the submission and no arXiv version known |
| `no-original` | nothing to compare against, so the printed text stands |
| `pinned` | listed in `abstract-pins.json`; never touched |
| `manual` | body splices in a formatted Typst variable; reported, never rewritten |
| `unmatched` | no talk in `program.md` with that title and time slot |

### Data files

- `arxiv-ids.json` — submission PDF → arXiv id. Seeded from the original build
  (fuzzy title/author matches, checked by hand). `--discover-arxiv` adds ids
  printed on the papers themselves; anything but arXiv's own stamp must agree
  with the talk's title or author list before it is trusted, so a preprint
  merely *cited* in the front matter is not mistaken for the paper.
- `arxiv-abstracts.json` — cache of fetched arXiv abstracts, so a re-check needs
  no network. `--refresh-arxiv` re-fetches.
- `abstract-pins.json` — talks whose printed abstract is authoritative even
  though it matches no source, e.g. text supplied directly by the authors.

## gen_posters.py

Writes `assets/pdfs/posters.typ`, the poster abstracts that close the booklet.
Talks and posters are kept in separate files because they come from different
places: a talk's abstract is read off the submitted paper, while a poster's is
the one its authors typed into EasyChair. `verify_abstracts.py` therefore has
nothing to say about posters, and does not look at this file.

Three inputs, none of which duplicates the others:

- the EasyChair abstract export (plain text) — the abstract of every
  submission, as its authors wrote it;
- the board-assignment spreadsheet (`.xlsx`) — which submission hangs on which
  board, i.e. which posters are actually being presented and in what order a
  visitor walks past them. Only submissions listed here are printed, and a
  submission spanning several boards is printed once, over the range;
- `accepted.md` — the canonical title and author list for each poster, matched
  on title, so that the booklet and the website agree. A poster the spreadsheet
  names but the page does not list is reported and skipped.

```sh
./scripts/gen_posters.py ~/Downloads/'qpl2026-abstracts posters.txt' \
                         ~/Downloads/'Indeling posters.xlsx'
cd assets/pdfs && typst compile QPL_2026_Program.typ
```

Unlike the talk abstracts, these arrive as LaTeX source rather than as typeset
text, so the markup has to be resolved before it can be set: `\emph` and
friends are unwrapped, TeX quoting and dashes become the characters they stand
for, and each maths span is rewritten into Typst maths. A span spelled in a way
the rewriter does not know raises rather than reaching the page as visible
markup — extend `MATH_SUBS` when that happens. A closing paragraph that only
links to the full version is moved out of the body and set as a footnote; the
handful that read awkwardly there are reworded in `NOTES`.

## abstract_extract.py

The PDF front-matter reader used by `verify_abstracts.py`. The submissions are
author-formatted with no common template, so the abstract is found
geometrically: an explicit "Abstract" label first, and failing that the first
prose block on page 1 that is set apart from the body text (indented, narrower,
smaller, or italic) and sits above the first section heading. It also reads the
arXiv id off a paper when there is one.
