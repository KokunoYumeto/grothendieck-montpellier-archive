from pathlib import Path
import hashlib
import csv

root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
print('Prior fetch execution: category_cartan_weil_sources.py was cancelled by write_stdin Ctrl-C; executor returned exit_code130. Ordered pool output had not emitted a result. The recovered1940 letter was saved before cancellation; the complete2011 book and IRMA notebook PDF were not saved. Primary book and inventory were independently opened using web retrieval, whose complete returned records are retained.')
for relative in [
 'notes/category_date_CartanWeil2011.pdf',
 'notes/category_date_CartanNotebooks2014.pdf',
 'notes/category_date_CartanWeilRecovered1940.pdf',
 'notes/category_date_CartanWeilRecovered1940.txt',
 'notes/category_cartan_weil_web_records.json',
]:
    path = root / relative
    if path.exists():
        print('FILE', relative, 'BYTES', path.stat().st_size, 'SHA256', hashlib.sha256(path.read_bytes()).hexdigest())
    else:
        print('NOT SAVED', relative)
event = ['geo-H-history','2026-11-20','GPT-6 Astra, inherited effort, crystalline_categories','bounded published-correspondence dating check','Opened Audin2011 Cartan–Weil edition; checked1953–1955 table/index and letter/enclosure passages, with explicit1952–most1953 gap recorded atp616note333.8. Grothendieck letter mentionsp380/p393 concern later reprints/Foundations, not trace sheets. IRMA inventory intro identifies Académie correspondence; archive portal AccessDenied, originals not opened. notes/category_cartan_weil_date_audit.md']
with (root / 'notes/category_CHECK_EVENTS.tsv').open('a', newline='') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerow(event)
print('EVENT', repr(event))
for relative in ['notes/category_source_search_log.md','notes/category_progress.md']:
    addition = '\n- Fresh bounded Cartan–Weil route completed in notes/category_cartan_weil_date_audit.md: public2011 published letters opened;1952–most1953 gap explicit; checked1953–55 enclosure contexts give no trace-draft identification. Current Académie archive portal denied access; no originals claimed read. Exact queries/tool records and direct-download cancellation bounds retained; no section or bibliography change before scheduled checkpoint.\n'
    with (root / relative).open('a') as f:
        f.write(addition)
    print('APPENDED', relative)
