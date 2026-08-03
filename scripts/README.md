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

## abstract_extract.py

The PDF front-matter reader used by `verify_abstracts.py`. The submissions are
author-formatted with no common template, so the abstract is found
geometrically: an explicit "Abstract" label first, and failing that the first
prose block on page 1 that is set apart from the body text (indented, narrower,
smaller, or italic) and sits above the first section heading. It also reads the
arXiv id off a paper when there is one.
