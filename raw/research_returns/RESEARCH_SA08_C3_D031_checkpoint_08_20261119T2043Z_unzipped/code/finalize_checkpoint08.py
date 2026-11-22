#!/usr/bin/env python3
"""Record the checked checkpoint08 PDF and the scheduled fourth review.

This script writes records only. The immutable ZIP is created separately at
the scheduled boundary, never by an early invocation of this script.
"""
from pathlib import Path
import argparse, csv, datetime, json, re, shutil

p=argparse.ArgumentParser()
p.add_argument('--review', action='store_true')
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
qa=root.parent/'qa_checkpoint08_committed'
now=datetime.datetime.now(datetime.timezone.utc)
stamp=now.strftime('%Y-%m-%d %H:%M:%S UTC')

if not a.review:
    data=json.loads((qa/'render_log.json').read_text())
    assert data['rendered_pages']==181
    assert data['overfull_boxes']==0
    assert data['undefined_reference_warnings']==0
    assert data['latex_warnings']==0
    assert 'Root viewed' in data['visual_inspection'], 'Record actual image inspection first'
    shutil.copyfile(qa/'render_log.json',root/'logs/typesetting_checkpoint08.json')
    shutil.copyfile(qa/'contact.png',root/'qa/checkpoint08_contact.png')
    report=root/'RESEARCH_SA08_C3_D031_report.md'
    s=report.read_text()
    s=s.replace('The main154-page PDF remains the separately checked build38 until the next integrated build.',
                'At that historical audit the main154-page PDF was build38; the checkpoint08 integration is recorded below.')
    marker='## Checkpoint08 typesetting and current integration boundary'
    block=f'''{marker}

Build46 contains181 pages and integrates A-S09-28–31, AT26–28 and A-L20–21, together with all earlier completed sections. Its final log has zero overfull boxes, zero undefined references and zero LaTeX warnings. The before/after overfull counts for this integration are0/0. Earlier syntax failures were corrected at their exact sources: the unsupported mathscr command and an overfilled split alignment in A-S09-28, then a missing display terminator after the opening generator list in A-L21. The complete repeated-pass build succeeded after each final correction; diagnostic logs are retained.

All181 pages were rendered from a fixed copy of build46 in{data['seconds']} seconds. The root viewed the35-page contact sheet and the individually identified new-proof pages recorded in logs/typesetting_checkpoint08.json. The image review found no clipping, overlap or missing glyphs. The main source and this PDF agree. The two newly retained standalone PDFs for AT26 and AT27 have six pages in total, with their independent render and image review recorded in logs/A_integral_AT26_AT27_visual_review.json; they supplement the earlier45-page audit of13 retained standalone PDFs.

The renewed Cenkl–Porter source audit is recorded in notes/A_cenkl_porter_followup.md. The three primary PDF downloads used code/fetch_sources.py and took7.426,9.027,9.042 seconds for1,026,193;420,657;490,914 bytes respectively; their exact hashes are in the corresponding logs. The1982 range and actual comparison maps, the1989 displayed hypotheses, and the1984 finite-type/tame inputs were checked at the stated pages. No strict PD comparison for arbitrary targets is inferred from those readings.

AT29 and AT29b are complete working sections outside this181-page main PDF. The root full proof check and an independent written referee passed by20:42UTC. They construct an integral completion through form three in every simplex, with all eventual horizontal rows, from the displayed reference data over Z_(2), and verify those data for the actual global free-cell family. The source includes dyadic-root saturation, exact integral endpoint corrections, and full horizontal prism extensions. Their text and checks are preserved for the next integration. Higher form degrees and the strict C34 truncation agreements remain unconstructed. Both original PartA assertions remain undecided; PartB remains completed.
'''
    if marker in s:s=s[:s.index(marker)]+block
    else:s+='\n'+block
    report.write_text(s)
    print(json.dumps({'stage':'typesetting_recorded','utc':stamp,'pages':181}))
else:
    due=datetime.datetime(2026,11,19,20,43,12,tzinfo=datetime.timezone.utc)
    assert now>=due, 'Formal review is not yet due'
    with (root/'RESEARCH_SA08_C3_D031_results.csv').open(newline='') as f:
        rows=list(csv.DictReader(f))
    with (root/'CHECK_EVENTS.tsv').open(newline='') as f:
        events=list(csv.DictReader(f,delimiter='\t'))
    marker='## Formal review04 — 19 November2026'
    ledger=root/'PROGRESS_LEDGER.md';s=ledger.read_text()
    if marker not in s:
        s+=f'''
{marker}, {stamp}

This is the fourth scheduled review, at the six-hour boundary. We compare the current state with review03 and count only a changed initially open row or a strictly smaller equivalent main gate.

| Initially open row | Current status | Strongest proved gate or completed result | Qualifying movement since review03 |
|---|---|---|---|
| A-CS | Undecided | A-S09-29: the common-source assertion is equivalent to sources and targets internal to E_omega^[d], the countable single-disk class, for every fixed finite d. | Yes: countability is a proper further restriction, with actual finite-diagram subobjects and both internal-source implications. |
| A-TL | Undecided | A-S09-30: terminality of the all-arrow localization of F_3,omega^[d], with countable objects and one, two or three first-skeleton disks per weight, equivalent to the original localization. | Yes: this is a strictly smaller equivalent gate than C^[d] at review03. |
| A-SA09 | Reconstruction proved; application undecided | A2.2/A3.1/A3.2 remain independently verified; the requested general strict comparison or separating invariant remains absent. | No status change. |
| B-D031 | Completed | D-031 and B-001–008 retain the full independent counterexample, source/dependency audit and exact corrected lifting criteria. | Already closed at review01. |

**Qualifying movement: yes, for both main gates.** A-S09-29 constructs actual countable subobjects of each finite diagram, closes under every specified PD/simplicial operation and every required primitive, and retains the original uniform bounds. Its explicit uncountable square-zero extensions prove properness. A-S09-30 constructs the strict pair/triple/fold maps and an actual comparison functor on each finite-object full subcategory; its finite-word and finite-equality-witness proofs give the localization equivalence. The infinite-rank first-skeleton witness proves properness of the three-copy class. The root and independent referees checked the complete proofs before this review.

The single-copy localization obstruction of A-S09-28, the integral simplex-two cleanup A-S09-31, the full prism and reference-controlled completion AT26–27, the strict-truncation counterexample with actual paths AT28, and the all-odd-prime next repair A-L20–21 are not counted as additional movement. They supply actual constructions or exact limitations, while leaving the two displayed reduced questions undecided.

The consecutive no-movement review count remains zero. The two-review stopping condition has not occurred. Work continues on the coherent integral completion and the required higher-degree/truncation control. Next formal review:21:43:12UTC /22:43:12Europe/Berlin. Next checkpoint after this one:21:28:12UTC /22:28:12Europe/Berlin.

## Checkpoint08 — 19 November2026, scheduled20:43:12UTC

The eighth scheduled snapshot contains the181-page clean build46, {len(rows)} consolidated statement records and {len(events)} check events at this preparation, together with all current working sections, code and logs. All181 pages were rendered and the recorded sample inspected. The main PDF integrates the results through A-S09-31, AT28 and A-L21; later working sections retain their own exact check state outside that PDF. This is an ongoing-work checkpoint with review04 recorded above. Both original integral questions remain open.
'''
        ledger.write_text(s)
    print(json.dumps({'stage':'review_recorded','utc':stamp,'statement_rows':len(rows),'check_events':len(events)}))
