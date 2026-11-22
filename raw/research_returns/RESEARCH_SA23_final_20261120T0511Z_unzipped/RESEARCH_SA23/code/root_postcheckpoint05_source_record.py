"""Record source readings and bounded retrieval outcomes actually completed."""
from pathlib import Path
import csv,datetime,json,time
root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
target=root/'logs/root_postcheckpoint05_source_record.json'
if target.exists():
    raise SystemExit('Post-checkpoint source record already exists.')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
events=[
 ('Read both original 1954 Comptes rendus notes in full native text and displayed all six original pages. They concern tensor norms and operator factorizations, without the spectral trace/genus-zero proof or an identification of the target sheets. Their distinct running-header and starred-note dates are retained. No date-gate movement.',
  'notes/root_1954_cr_date_audit.md;logs/root_history_fetch14.json;logs/render_source_pages_root_cr1954_1.json;logs/render_source_pages_root_cr1954_2.json'),
 ('Read indexed Russian1958 translation metadata, two independent public scan listings, and actual advertised-link results. Original translation remains unopened: MathNet403, Yandex login redirect stopped, linked DjVu404, no public Wayback snapshot returned for the exact checked URLs. These retrieval bounds supply no date witness.',
  'notes/root_russian_translation_date_audit.md;logs/root_history_fetch09.json;logs/root_history_fetch10.json;logs/root_history_fetch11.json;logs/root_history_fetch12.json;logs/root_history_fetch13.json'),
 ('Root independently displayed R187 first-page pencil-margin crop and R230 physical pages1,2,133 (contents, Commentaires88, Remarks219). Confirmed that R230 distinguishes Hermitian genus zero from the general Hilbert announcement in the thesis. This is a documentary comparison, not a date for Montpellier cote1.',
  'notes/category_bourbaki_r187_r230_date_audit.md;notes/category_bourbaki_r230_fredholm_date_audit.md;notes/geometry_r230_hilbert_date_audit.md'),
]
with (root/'notes/root_CHECK_EVENTS.tsv').open('a',newline='') as handle:
    fields=['statement_id','date','who','type','outcome','where']
    writer=csv.DictWriter(handle,fieldnames=fields,delimiter='\t')
    for outcome,where in events:
        writer.writerow({'statement_id':'geo-H-history','date':'2026-11-20',
         'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
         'type':'used and rechecked in this run','outcome':outcome,'where':where})
with (root/'notes/root_source_log.md').open('a') as handle:
    handle.write('\n\n## Source follow-up after the fifth checkpoint\n\n')
    handle.write('The two original 1954 Comptes rendus notes were read completely and all six pages displayed. Their exact date and scope findings are in notes/root_1954_cr_date_audit.md. The independent Russian-translation copy routes are recorded in notes/root_russian_translation_date_audit.md; the original translation is still unopened. Root also independently viewed the R187 margin and R230 contents, commentary and typed page219, confirming the distinction between proved Hermitian genus zero and the general Hilbert announcement. None of these records supplies a date for the target leaves.\n')
record={'created_utc':stamp,'new_events':len(events),
        'cr1954_visual_pages':{'I':[1,2,3],'II':[1,2,3]},
        'r230_root_visual_physical_pages':[1,2,133],
        'r187_root_visual':'page02 enlarged pencil-margin crop',
        'russian_translation_original_opened':False,'date_gate_changed':False,
        'elapsed_seconds':time.perf_counter()-start}
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
