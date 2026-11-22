from pathlib import Path
import csv,json
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
row=['geo-H-history','2026-11-20','GPT-6 Astra, inherited effort, crystalline_categories','used and rechecked in this run','Retrieved exact 156-page IECL/Delsarte original R230 from public archived catalogue link; directly read physical1-3,118-135,156, including complete Fredholm typed204-221. Typed219 Remarks2 proves Hermitian genus-zero case by earlier corollary and attributes arbitrary Hilbert case to Grothendieck thesis announcement, without its proof here. No cote1 enclosure/leaf identification. March1956 is catalogue evidence from a different ENS copy, not an observed date in this IECL scan. Geometry independently owns typed188-203 reading. notes/category_bourbaki_r230_fredholm_date_audit.md']
p=r/'notes/category_CHECK_EVENTS.tsv'
if row[-1] in p.read_text(): raise SystemExit('Refusing duplicate event')
with p.open('a',newline='') as f: csv.writer(f,delimiter='\t',lineterminator='\n').writerow(row)
entry='\n\n## 2026-11-20 04:00 UTC — R230 original section comparison complete\n\nThis supersedes the earlier R230-unopened/in-progress statements. Exact archived IECL/Delsarte original obtained,156 pages. Category directly read physical1-3,118-135,156, including all Fredholm typed204-221; geometry separately read Hilbert188-203. Typed219 Remarks2 identifies the arbitrary Hilbert genus-zero theorem as an announcement in Grothendieck\'s thesis; the displayed proof gives the Hermitian case and the general Banach genus-at-most-one theorem. No three-sector proof, cote1 identification, dated letter or enclosure found in these inspected sections. Catalogue March1956 attribution is based on handwriting in a different ENS copy, not a date read in this IECL scan. Full architecture, exact original-page images, hashes, URLs, programs and limits: notes/category_bourbaki_r230_fredholm_date_audit.md. catBourbaki230 added. The actual Montpellier sheet-date gate is unchanged.\n'
for name in ['category_source_search_log.md','category_progress.md','category_bourbaki_r187_r230_date_audit.md']:
    with (r/'notes'/name).open('a') as f: f.write(entry)
b=r/'notes/category_references.bib'
s=b.read_text()
for key in ['catBourbaki179','catBourbaki187']:
    start=s.index('@misc{'+key+',')
    end=s.find('\n@',start+1)
    if end<0: end=len(s)
    old=s[start:end]
    new=old.replace('Opened2026','Opened 2026').replace('mai53','mai 53').replace('sept53','sept 53').replace('cote1','cote 1')
    s=s[:start]+new+s[end:]
if '@misc{catBourbaki230,' in s: raise SystemExit('Refusing duplicate bibliography entry')
s+='''\n@misc{catBourbaki230,
 author={Dieudonn\\'e, Jean},
 title={R\\'edaction 230: Rapport sur la th\\'eorie spectrale (partie I B), Op\\'erateurs compacts et produits tensoriels topologiques},
 year={1956},
 url={http://web.archive.org/web/20260213200334if_/https://archives-bourbaki.ahp-numerique.fr/files/original/49e6e904fbc99a10207673c09e068fa7.pdf},
 note={Opened 2026-11-20: 156-page IECL/Delsarte scan, IECNR BKI05-3.1. Category read title, comments p88, pp204--221 and final p242; geometry independently read pp188--203. At p219 Remarks2 the general Hilbert genus-zero result is attributed to an announcement in Grothendieck's thesis. Author and March 1956 date are catalogue attributions based on an inscription in a different ENS copy, not observed in this scan; no Montpellier cote 1 identification}}
'''
b.write_text(s)
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
with p.open(newline='') as f: rows=list(csv.reader(f,delimiter='\t'))
invalid=[(i+2,x[3]) for i,x in enumerate(rows[1:]) if len(x)<4 or x[3] not in allowed]
print(json.dumps({'added_event':row,'events':len(rows)-1,'invalid_taxonomy':invalid,'bib':'catBourbaki230','spacing_fixed':['catBourbaki179','catBourbaki187'],'note':'notes/category_bourbaki_r230_fredholm_date_audit.md'},ensure_ascii=False))
