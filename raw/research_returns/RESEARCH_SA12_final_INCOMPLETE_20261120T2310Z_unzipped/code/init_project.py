"""Initialize the research record; run once. All timestamps use UTC internally."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, shutil

ROOT = Path(__file__).resolve().parents[1]
for name in ['parts/A','parts/B','parts/C','parts/D','sources','logs','code/output','build','qa']:
    (ROOT/name).mkdir(parents=True, exist_ok=True)
started = '2026-11-20T00:10:00+00:00'
items = ['A.1','A.2','A.3','A.4','A.4.margin','A.5','A.5.NB','A.6.i','A.6.ii','A.7.i','A.7.ii','A.7.iii.affine','A.7.iii.general','A.8.i','A.8.ii','A.9.corollary','A.9.NB','A.9.regular','A.9.margin.regularity','A.9.margin.characteristic','B.1','B.1.variants','B.2','B.3','C.1.general','C.1.i','C.1.ii','C.1.iii','C.1.Nori','C.2.etale','C.2.flat','D.1','D.2.i','D.2.ii','D.3','D.4','D.5','D.6','D.7.alpha','D.7.prop5','D.7.roots','D.8','D.9.units','D.9.GLn','D.10.curves','D.10.general','D.10.tame'] + [f'L{i}' for i in range(1,11)]
with (ROOT/'RESEARCH_SA12_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
    for item in items: w.writerow([item,'See attached task, exact statement to be restated in paper','Under investigation','','','','No conclusion asserted'])
(ROOT/'RESEARCH_SA12_report.md').write_text('INCOMPLETE\n\n# Research report: SA12\n\nWork in progress, started 20 November 2026 at 01:10 CET (00:10 UTC).\n\n## Outcome table\n\n| Item | Current state | Statement/proof |\n|---|---|---|\n' + ''.join(f'| {item} | Under investigation | Pending |\n' for item in items) + '\n## Scope and attribution\n\nAI-produced by GPT-6 Astra (OpenAI). No priority claim. The actual environment is ChatGPT Work with parallel research agents; the requested Pro-mode label is not asserted as an observed execution mode. All inherited results are provisional until rechecked.\n\n## Records\n\nThe evidence and computations will be listed here as completed.\n')
(ROOT/'PROGRESS_LEDGER.md').write_text('# Progress ledger\n\nInternal timestamps are UTC; user-facing equivalent is CET (UTC+1).\n\n## Start: 2026-11-20 00:10 UTC\n\nAll items are under investigation. Root owns Part A; parallel agents own B, C, and D. The full item list is in RESEARCH_SA12_results.csv. No completed proof or refutation is claimed at initialization.\n\n### Review protocol\n\nThe first formal review is due approximately 03:10 UTC, then hourly. Movement is a changed open-item status or a strictly smaller proved residual gate for a main question. Two consecutive reviews with no movement trigger finalization under the user\'s explicit stopping rule. Checkpoint archives are due every 45 minutes from the start; no event-based checkpoint archives will be made.\n')
(ROOT/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho\ttype\toutcome\n')
(ROOT/'RESEARCH_SA12_references.bib').write_text('% Entries are appended only with opened/not-opened annotations.\n')
(ROOT/'logs/run_metadata.json').write_text(json.dumps({'started_utc':started,'model':'GPT-6 Astra','run':'SA12-20261120-root','effort':'not externally exposed','source_archive':'SA12_SGA_cd_of_affines_and_pi1_cotes_29-31_night.zip','input_extraction':'inputs/','checkpoint_minutes':45,'first_progress_review_minutes':180},indent=2)+'\n')
print(json.dumps({'created_root':str(ROOT),'initial_item_count':len(items),'started_utc':started},indent=2))
