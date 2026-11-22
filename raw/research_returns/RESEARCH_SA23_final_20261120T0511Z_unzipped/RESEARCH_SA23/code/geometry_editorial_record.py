from pathlib import Path
import csv, datetime, hashlib, json

base=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
note=base/'notes/geometry_editorial_course_date_audit.md'
prefix='Summa/course editorial date route:'
events=[
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro, inherited effort, geometry_analysis','used and rechecked in this run',
  prefix+' visually inspected the actual Circle course link: Ask.pdf is a request notice, not the course scan. CSG course editions and secondary January 1953 Dieudonne letter narrative were checked without treating them as original folio evidence. FDF original link returned404, mirror request403, and Archive course metadata reports is_dark with no file list. Exact bounded search and all retrieval limits are in geometry_editorial_course_date_audit.md; no new manuscript date, theorem, or proof is certified.'],
 ['SA23-49','2026-11-20','GPT-6 Astra Pro, inherited effort, geometry_analysis','used and rechecked in this run',
  prefix+' no dated draft, enclosure, or item-level entry identifying physical cote1 pages79-80/111-112 was obtained. January1953 correspondence remains a secondary lead without the original. Repeated Dieudonne inventory checks are explicitly cross-referenced to category rather than presented as a new discovery. The exact sheet-date assertion remains unproved.']
]
path=base/'notes/geometry_CHECK_EVENTS.tsv'
with path.open(newline='') as f:
 old=list(csv.reader(f,delimiter='\t'))
new=[row for row in events if not any(x[0]==row[0] and len(x)>4 and x[4].startswith(prefix) for x in old)]
with path.open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerows(new)
records=[]
for i in range(1,17):
 p=base/f'notes/geometry_editorial_search{i:02}.json'
 raw=p.read_bytes()
 obj=json.loads(raw)
 records.append({'file':str(p.relative_to(base)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'is_error':obj.get('isError')})
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'note':str(note.relative_to(base)),'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'search_outputs':records,'new_event_count':len(new),'event_type':'used and rechecked in this run','core_sections_changed':False,'new_numbered_statements':0,'manuscript_date_gate_closed':False,'archive_created':False}
(base/'logs/geometry_editorial_route_record.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
with (base/'notes/geometry_research_log.md').open('a') as f:
 f.write('\n## Summa editorial and Sao Paulo course dating route\n\nBounded public search preserved in geometry_editorial_course_date_audit.md and sixteen raw output files. The original course link was visually found to be a request notice, not a course scan. Public catalogue editions and secondary January1953 correspondence narrative identify no particular cote1 enclosure or sheet. Already checked Dieudonne inventory material is marked as a repeated check. Inaccessible or missing originals remain unopened; no contact or account action was taken. No core mathematics, result status, or numbering changed; the folio-date gate remains open.\n')
print(json.dumps({k:v for k,v in out.items() if k!='search_outputs'},ensure_ascii=False))
