from pathlib import Path
from urllib.request import Request,urlopen
import csv
import hashlib

ROOT=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
for name,url in [
 ('Kothe_I6','https://kalliope-verbund.info/de/ead?ead.id=DE-611-HS-3176137'),
 ('Kothe_I6_enclosure','https://kalliope-verbund.info/de/ead?ead.id=DE-611-HS-3140687'),
]:
    print('REQUEST',url,flush=True)
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:
            data=response.read()
            print('STATUS',response.status,'FINAL',response.url,'BYTES',len(data),'SHA256',hashlib.sha256(data).hexdigest(),flush=True)
        (ROOT/f'notes/category_date_{name}.html').write_bytes(data)
    except Exception as exc:
        print('FAILED',type(exc).__name__,str(exc),flush=True)

event=['geo-H-history','2026-11-20','GPT-6 Astra, inherited effort, crystalline_categories','primary archival catalogue and dated-letter lead check','Opened official KotheA201 correspondence record1950–1956, seven Grothendieck letters and two carbon copies; and I6 compact-operator manuscript1948–1952, folios21–27 titled On Grothendieck\'s problem; enclosure2 is Wielandt draft8Aug1949. No original contents or identification with cote1 obtained. Read Schneps chap4 dated-letter excerpts; career remarks do not date sheets. notes/category_kothe_date_audit.md']
events=ROOT/'notes/category_CHECK_EVENTS.tsv'
with events.open(newline='') as stream: rows=list(csv.reader(stream,delimiter='\t'))
if event not in rows:rows.append(event)
with events.open('w',newline='') as stream:csv.writer(stream,delimiter='\t',lineterminator='\n').writerows(rows)
print('EVENTS',len(rows)-1,flush=True)

for filename,line in [
 ('category_progress.md','- The new Kothe route identifies exact primary units SUBGottingenA201 (seven Grothendieck letters1950–1956) and I6 (compact-operator notes1948–1952, including OnGrothendieck\'sproblem). Records opened; originals not obtained and no connection to cote1 proved. notes/category_kothe_date_audit.md gives the exact remaining original-document lead.\n'),
 ('category_source_search_log.md','- Kothe follow-up: exact queries, actual catalogue-link path, opened/not-opened distinctions and source limits are preserved in notes/category_kothe_date_audit.md. Primary KalliopeA201 and I6/enclosure2 records opened. OfficialPDFfindingaidp39 opened viaweb, but directdownload404; no localPDFclaimed. The explicit identification needed to date the crossed trace sheets remains absent.\n'),
]:
    p=ROOT/'notes'/filename;s=p.read_text()
    if line not in s:p.write_text(s+'\n'+line)

p=ROOT/'notes/category_references.bib';s=p.read_text()
s=s.replace('pp254,257--258 visually checked2026-11-20. Primary comparison', 'pp254,257--258 visually checked2026-11-20 independently by category and geometry agents. Primary comparison')
p.write_text(s)
print('UPDATED_PROGRESS_SOURCELOG_SIMONFLAG',flush=True)
