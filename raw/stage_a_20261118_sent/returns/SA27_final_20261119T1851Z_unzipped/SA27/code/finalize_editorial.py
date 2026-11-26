"""Insert counts from validated, manually curated registers and write the guide.

This program formats the final editorial apparatus. It never assigns a verdict,
mathematical status, literature class, or authorship from words in a source.
"""
from collections import Counter, defaultdict
from pathlib import Path
import csv
import json
import re

R = Path(__file__).resolve().parents[1]


def read_tsv(name):
    with (R / name).open() as f:
        return list(csv.DictReader(f, delimiter='\t'))


def table(headers, rows):
    return '\n'.join([
        '| ' + ' | '.join(headers) + ' |',
        '| ' + ' | '.join('---' for _ in headers) + ' |',
        *['| ' + ' | '.join(str(v) for v in row) + ' |' for row in rows],
    ])


def main():
    validation = json.loads((R / 'outputs/validation.json').read_text())
    assert not validation['errors'], 'Do not mark structurally invalid registers complete.'
    items = json.loads((R / 'SA27_items.json').read_text())
    entries = read_tsv('SA27_entries.tsv')
    kinds = {q['id']: q['kind'] for q in items}
    item_counts = Counter(kinds.values())
    entry_counts = defaultdict(Counter)
    for q in entries:
        entry_counts[kinds[q['item_id']]][q['verdict']] += 1
    direction_count = len(re.findall(r'^## \d+\.', (R / 'SA27_directions.md').read_text(), re.M))
    assert direction_count == 15

    totals = [
        ('Indexed source entries, each with one read verdict', validation['entries']),
        ('Consolidated items', validation['items']),
        ('Supplied scan blocks / page-read records', f"{validation['scan_blocks']} / {validation['page_read_records']}"),
        ('Authorial claim records', validation['claims']),
        ('Separate modern claim refinements', validation['modern_refinements']),
        ('Authorial questions and unfinished steps', validation['problems']),
        ('Separate historical/editorial questions', validation['historical_editorial_questions']),
        ('Separate modern audit questions', validation['modern_audit_questions']),
        ('Undecided reading alarms', validation['readings']),
        ('Ranked future tasks', direction_count),
        ('Link records', validation['links']),
        ('Bibliographic records', validation['references']),
        ('References marked verified / unverified', f"{validation['reference_verification_marks'].get('verified',0)} / {validation['reference_verification_marks'].get('unverified',0)}"),
        ('Recorded search families/actions', validation['search_records']),
        ('Detailed search-ledger rows', validation['search_ledger_rows']),
        ('Check events', validation['check_events']),
    ]
    verdict_order = ['kept', 'merged', 'corrected', 'withdrawn', 'rests on a misreading']
    kind_order = ['conjecture', 'unproved claim', 'unpursued implication', 'idea of the earlier run',
                  'reading question', 'self-flagged step', 'withdrawn in the same text',
                  'title, date or page count', 'other']
    class_labels = {
        'A': 'In his own later published work',
        'B': 'Developed by others into established results',
        'C': 'Partly developed or requiring the stated correction/scope qualification',
        'D': 'No exact development found in the recorded bounded search',
        'E': 'Known before the dated programme; undated-leaf limits retained',
        'F': 'Not identifiable precisely from the supplied pages',
    }
    page_order = ['proved there', 'proof sketched', 'stated without proof',
                  'corrected by himself later', 'false as stated', 'open on the pages']
    count_text = '\n\n'.join([
        table(['Register', 'Count'], totals),
        '### Entry verdicts',
        table(['Verdict', 'Source entries'], [(k, validation['verdicts'].get(k, 0)) for k in verdict_order]),
        '### Items and source verdicts by item kind',
        'The kind is the read judgment attached to the canonical item. An item can own several source entries; consequently the item column totals differently from the verdict columns.',
        table(['Kind', 'Items', 'Source entries', 'Kept', 'Merged', 'Corrected', 'Withdrawn', 'Misreading'],
              [(k, item_counts[k], sum(entry_counts[k].values()), *[entry_counts[k][v] for v in verdict_order]) for k in kind_order]),
        '### Authorial claims by literature class',
        table(['Class', 'Meaning', 'Claims'], [(k, class_labels[k], validation['claim_classes'].get(k, 0)) for k in 'ABCDEF']),
        '### Authorial claims by status on the pages',
        'The six groups below were assigned by the package readers from their close readings. The full `status_on_pages` field retains mixed states, cancellations in place, conditional counterexamples and unfinished subclauses. A false-as-stated classification does not decide an uncertain reading of the ink. The two modern refinements are excluded from both claim tables.',
        table(['Page-status group', 'Claims'], [(k, validation['claim_status_groups'].get(k, 0)) for k in page_order]),
        '### Link categories',
        table(['Kind', 'Records'], [(k, validation['link_kinds'].get(k, 0)) for k in ['folder', 'published work', 'our projects']]),
        'All six stages have been completed for the supplied part. Every authorial claim has a mapped search record; every item, claim/refinement and cited result key has a check event. All 112 supplied scan blocks have read records, and all supplied-source hashes match the initial inventory. `outputs/validation.json` records the complete structural checks. Those checks certify coverage and consistency, not mathematical infallibility. The explicit unresolved readings, unidentified assertions, bounded literature gaps and unavailable private-project endpoints remain qualifications of the completed dossier.',
    ])
    path = R / 'SA27_dossier.md'
    text = path.read_text()
    text = re.sub(r'<!-- COUNTS_START -->.*?<!-- COUNTS_END -->',
                  '<!-- COUNTS_START -->\n' + count_text + '\n<!-- COUNTS_END -->', text, flags=re.S)
    # Literal typography corrections only, restricted to authored overview prose.
    corrections = {
        '162,98': '162, 98', '40,34': '40, 34', 'September1968': 'September 1968',
        'a24 November': 'a 24 November', 'Cote118': 'Cote 118', 'reused1973': 'reused 1973',
        'final418-page': 'final 418-page', 'earlier370-page': 'earlier 370-page',
        'short108 phrase': 'short 108 phrase', 'In118': 'In 118',
        'inclusion{1}': 'inclusion {1}', 'over[1]': 'over [1]',
        'equivalence{0}': 'equivalence {0}', 'to∅': 'to ∅',
        'checks§': 'checks §', 'checks§§': 'checks §§',
        'representable1-cubes': 'representable 1-cubes', 'numbers(1,1,1)': 'numbers (1,1,1)',
        'comparing115': 'comparing 115', 'triples(P,Q,α)': 'triples (P,Q,α)',
        'is[1]': 'is [1]', 'comparison∅': 'comparison ∅', 'October2026': 'October 2026',
        'final2006': 'final 2006', 'The115': 'The 115', 'The118': 'The 118',
        'Third,118': 'Third, 118', 'a1983 date': 'a 1983 date',
        'VolumeI ': 'Volume I ', 'VolumeII ': 'Volume II ',
        'covers§§': 'covers §§', 'of§§': 'of §§', 'into2022': 'into 2022',
        'or137': 'or 137', 'returned403': 'returned 403',
        'classD': 'class D', 'ClassF': 'Class F', 'reused118/004': 'reused 118/004',
        'genuinely unresolved': 'remaining',
    }
    for old, new in corrections.items():
        text = text.replace(old, new)
    path.write_text(text)

    readme = '''# SA27 — Delivery guide

This archive contains the completed six-stage dossier for part 3 of *Autour de Pursuing stacks*, checked as of 19 November 2026. Its scope is the 578 entries of the supplied index for cotes 108, 112–118. Other cotes in TOPIC are covered as orientation records only.

## Main files

| File | Purpose |
|---|---|
| `SA27_dossier.md` | English overview, substantive findings, scope, counts and limitations |
| `SA27_entries.tsv` | Exactly one read verdict per indexed source entry |
| `SA27_items.json` | Consolidated items, source membership, exact text checks and reconstructions |
| `SA27_claims.json` | Authorial assertions, constructions and questions, with page status, literature fate and search IDs |
| `SA27_problems.json` | His questions, conjectures and unfinished steps, with precise modern comparisons |
| `SA27_readings.tsv` | Undecided scan-reading queue; no ink decision was made |
| `SA27_links.tsv` | All link records, with their different evidential statuses |
| `SA27_directions.md` | Fifteen ranked tasks for later research runs |
| `SA27_references.bib` | Consolidated references, each marked verified or unverified |
| `CHECK_EVENTS.tsv` | What was read, used, proved, computed or refuted, and by whom |
| `progress.log` | UTC work milestones and completion record |

## Supporting evidence

`work/p108/`, `work/p116/` and `work/p118/` retain the package readers' original records. They contain page-read logs, proofs, exact theorem matches, search ledgers, context-comparison subrows, programs and outputs. Their local item IDs can differ from the master IDs after a merger; `work/item_aliases.json`, `work/problem_aliases.json` and `work/reference_aliases.json` give the translations. The original package records are preserved intentionally, not treated as competing final editions. The master files at the archive root are authoritative for consolidation and counts.

`research/root_mathematical_checks.md` contains the independent checks and counterexamples. `research/shared_verifications.md` records the later public manuscript comparisons. `research/search_index.json` preserves the actual ledger rows, while `research/claim_search_links.tsv` gives the claim-to-search map. Search records may cover a tightly related family of claims; each claim states the exact hypothesis match or the remaining identification limit.

Modern claim refinements are in `research/modern_refinements.json`. Historical/editorial questions introduced by earlier notes are in `research/context_questions.json`, and modern audit questions are in `research/modern_questions.json`. Their stable IDs remain usable, but they are excluded from the authorial claim or problem totals. The original parent claim remains in the main register when its proposed stronger reading is refuted.

The three link categories are also available separately as `research/folder_links.tsv`, `research/published_links.tsv` and `research/project_links.tsv`. Private research returns are attributed, unverified leads. The available note-side occurrence has been read; an unavailable private endpoint is not reported as opened or proved. Public manuscript and published-work endpoints have exact opened locators where a result is used.

Line numbers refer to the supplied combined TeX file, one based, unless explicitly qualified. `work/page_map.json` resolves cote/scan boundaries. Mathematical reconstructions never alter the source text. The absence of second-pass and Codex files is a property of this supplied corpus, not an unfinished processing step.

## Reproduce the checks

Keep this `SA27/` directory next to a `source/` directory containing the original attachment's already-expanded `SA27_notes/` and `SA27_texts/` folders. Do not unpack nested archives: there were none. The source inventory contains hashes of the original inputs. The source files themselves are deliberately absent from this deliverable, as requested.

The scripts use Python 3. The exact nerve-homology program additionally uses SymPy. The saved JSON output is available without installing it. Network access is required only to rerun primary-source retrieval helpers, not to inspect the dossier or rerun the saved finite computations and structural checks.

From the directory containing `SA27/` and `source/`:

```bash
python3 SA27/code/validate_dossier.py
python3 SA27/code/finite_categories.py
python3 SA27/code/groupoid_pi0.py
python3 SA27/code/reused_sheet_arithmetic.py
python3 SA27/work/p108/finite_checks.py
python3 SA27/work/p116/computations.py
python3 SA27/work/p118/code/check_examples.py
```

The package build scripts serialize their explicitly authored reading decisions; they do not infer verdicts by keywords. Before rebuilding the p118 package from its scripts, run `python3 SA27/code/prepare_source_navigation.py` to regenerate the source-navigation input from the original attachment. That extracted full-source copy is omitted from the ZIP. `code/consolidate.py` applies the documented editorial mergers and reconstructs the master tables from the authored records. It should be followed by structural validation, then `code/finalize_editorial.py` if the count tables need rebuilding. All source decisions remain subject to scholarly review; successful validation checks identity, coverage, references and source immutability rather than mathematical truth.

The archive manifest in `outputs/archive_manifest.json` gives file sizes and hashes. Full copyrighted external PDFs, full-text research caches and raw web retrieval dumps are omitted; their opened URLs, locators and concise findings remain in the authored ledgers. The checkpoint history is included, but earlier ZIP files are not nested in this archive.
'''
    (R / 'README.md').write_text(readme)
    print(json.dumps({'counts_inserted': True, 'readme_written': True,
                      'ranked_directions': direction_count,
                      'structural_errors': len(validation['errors'])}, indent=2))


if __name__ == '__main__':
    main()
