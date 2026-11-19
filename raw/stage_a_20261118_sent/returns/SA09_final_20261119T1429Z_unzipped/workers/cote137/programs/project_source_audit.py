"""Hash opened project endpoints; no mathematical classification or proof checking."""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parents[1]; ROOT=W.parents[2]
jobs={
'project_sources/cote137_endpoints/GALOIS/GALOIS/README.txt':'1-3',
'project_sources/cote137_endpoints/GALOIS/GALOIS/sections/E.tex':'722-751',
'project_sources/cote137_endpoints/GALOIS/GALOIS/sections/G.tex':'182-196',
'project_sources/cote137_endpoints/GALOIS/GALOIS/GALOIS_results.csv':'61;75',
'project_sources/cote137_endpoints/RESIDUE/RESIDUE/README.md':'1-3',
'project_sources/cote137_endpoints/RESIDUE/RESIDUE/sections/I.tex':'183-198',
'project_sources/cote137_endpoints/RESIDUE/RESIDUE/sections/F.tex':'73-75',
'project_sources/cote137_endpoints/RESIDUE/RESIDUE/RESIDUE_results.csv':'59;81',
'project_sources/cote137_endpoints/TOTASPH/TOTASPH/README.md':'1-3',
'project_sources/cote137_endpoints/TOTASPH/TOTASPH/sections/C.tex':'155-162',
'project_sources/cote137_endpoints/TOTASPH/TOTASPH/sections/D.tex':'100-114',
'project_sources/cote137_endpoints/TOTASPH/TOTASPH/TOTASPH_results.csv':'38;49',
'project_sources/cote137_endpoints/TOTEX2_checkpoint_03/TOTEX2/TOTEX2_README.md':'1-3',
'project_sources/cote137_endpoints/TOTEX2_checkpoint_03/TOTEX2/sections/statements_sources.tex':'1-140',
'project_sources/cote137_endpoints/TOTEX2_checkpoint_03/TOTEX2/TOTEX2_results.csv':'1111-1145',
'project_sources/cote137_endpoints/CATHOT/CATHOT/README.md':'1-3',
'project_sources/cote137_endpoints/CATHOT/CATHOT/sections/F.tex':'374-413',
'project_sources/cote137_endpoints/CATHOT/CATHOT/CATHOT_results.csv':'69',
'project_sources/LM4_SUCCESSOR_background/LM4_return/README.md':'1-70',
'project_sources/LM4_SUCCESSOR_background/referee/REFEREE_A_LM4_D32.md':'1-50',
'project_sources/LM4_SUCCESSOR_background/referee/REFEREE_A_D50_E58.md':'1-35',
'project_sources/LM4_SUCCESSOR_background/MANIFEST.tsv':'1-25',
}
out=[]
for path,lines in jobs.items():
 p=ROOT/path;b=p.read_bytes()
 out.append({'path_from_workspace':path,'one_based_lines_read':lines,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'lines':len(b.decode().splitlines()),'verification':'textual endpoint and metadata; not proof certification'})
(W/'outputs/project_source_files.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'opened_files_hashed':len(out),'mathematical_certificates':0}))
