from pathlib import Path
import json,hashlib,datetime,shutil,difflib
B=Path(__file__).resolve().parent
D=B/'evidence/checkpoint11_table_fix';D.mkdir(exist_ok=True)
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n in ['KTOWER.tex','KTOWER.pdf','sections/framework.tex']:
 shutil.copy2(B/n,D/Path(n).name)
manifest=json.loads((B/'pdf_review11_postnotes/render_manifest.json').read_text())
r={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root; GPT-6 Astra Pro; effort setting not exposed','pdf_sha256':h(B/'KTOWER.pdf'),'tex_sha256':h(B/'KTOWER.tex'),'pages_inspected':list(range(181,249)),'contact_sheets':[x['path'] for x in manifest['sheets'][30:]],'result':'Layout correction required in framework table: pages237 and239 oversized rows extend too close to footer. Other pages181-248 fit; all12sheets31-42 actually inspected. Mathematical proof checking is separate.'}
(B/'evidence/root_pdf11_postnotes_review.json').write_text(json.dumps(r,indent=2)+'\n')
p=B/'sections/framework.tex';old=p.read_text();s=old
# Split oversized table rows at semantic boundaries; retain every assertion.
def splitrow(s,start,splitid,thirdsplit):
 a=s.index(start,s.index('\\begin{longtable}'))
 z=s.index('\\\\',a)+2
 row=s[a:z]
 cells=row[:-2].split(' &\n')
 assert len(cells)==3,len(cells)
 ids,obj,prose=cells
 k=ids.index(splitid);j=prose.index(thirdsplit)
 new=ids[:k].rstrip(';\n')+' &\n'+obj+' &\n'+prose[:j].rstrip()+'\\\\\n'+ids[k:]+' &\n'+obj+' &\n'+prose[j:]+'\\\\'
 return s[:a]+new+s[z:]
s=splitrow(s,'KT-GMA-REDUCIBILITY-DOES-NOT-BOUND-EXTENSIONS;','KT-CUBIC-EXCISION;','The exact shuffle preserves')
s=splitrow(s,'KT-JACOBI-ODD-COEFFICIENT;','KT-EISENSTEIN-HECKE-EVALUATION-IDEAL;','The senary genus trace realizes')
p.write_text(s)
(D/'framework_layout.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='framework-before',tofile='framework-after')))
print('Split two oversized rows; all mathematical text retained. Before',h(D/'KTOWER.pdf'))
