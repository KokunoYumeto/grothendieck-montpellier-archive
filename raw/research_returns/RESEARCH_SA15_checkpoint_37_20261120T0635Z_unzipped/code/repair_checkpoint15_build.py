"""Preserve CP15's first failed build before a display-whitespace repair."""
from pathlib import Path
import shutil,json,datetime
w=Path(__file__).resolve().parents[1]
folder=w/'outputs/failed_checkpoint15_build'
assert not folder.exists()
folder.mkdir()
for rel in ['RESEARCH_SA15_paper.tex','RESEARCH_SA15_paper.log',
            'sections/A_monodromy.tex','outputs/build_console.txt',
            'outputs/checkpoint15_preparation.stdout.txt',
            'agents/obstructions_crystals/A4_uniform_tangent_triple_type.tex']:
 p=w/rel
 shutil.copy2(p,folder/rel.replace('/','__'))
p=w/'agents/obstructions_crystals/A4_uniform_tangent_triple_type.tex'
t=p.read_text()
old='\\end{pmatrix}.\n\n\\]'
assert t.count(old)==1
p.write_text(t.replace(old,'\\end{pmatrix}.\n\\]'))
result={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'PRESERVED_AND_REPAIRED','failure':'Missing math delimiter caused by a paragraph break inside a display after the normalized3x3 matrix.',
 'repair':'Remove the single blank line inside the display; no mathematical text or identity changed.',
 'failed_build_exact_runtime_seconds':None,
 'runtime_note':'The failing build script exits before writing its timing summary. The retained build_summary.json before retry is the previous successful CP14 build and is not claimed as the CP15 failure runtime.'}
(folder/'metadata.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
