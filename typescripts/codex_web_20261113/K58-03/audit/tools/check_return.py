from collections import Counter,defaultdict
import csv,re,hashlib,importlib.util,sys
from pathlib import Path
from datetime import datetime
from PIL import Image
root=Path('out')
sys.path.insert(0,str(root))
from tex_elements import arguments,stamp
read=lambda path:list(csv.DictReader(open(path),delimiter='\t'))
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
scans=[*range(20,29),*range(30,36)]
out=root/'K58-03_transcription.tex'
for ns in ['transcription','standalone','doubts','audit','notes','mathnotes','hand_log','blind_compare']:
 assert (root/('K58-03_'+ns+('.tex' if ns in ['transcription','standalone'] else '.md'))).is_file()
assert len(read(root/'CHECK_EVENTS.tsv'))==7
assert (root/'PREAMBLE.tex').read_bytes()==next(Path('upload').glob('PREAMBLE*.tex')).read_bytes()
src=out.read_text(); assert re.findall(r'\\scanpage\{(\d+)\}',src)==list(map(str,scans))
assert src.count(r'\cotefile{58}')==1 and src.startswith('\\cotefile{58}\n\\scanpage{20}')
assert not any(p.suffix.lower() in ['.png','.jpg','.pdf','.zip'] for p in root.rglob('*'))
manifest=read('MANIFEST.tsv')
assert len(manifest)==60
for r in manifest:
 p=Path(r['file']);assert p.is_file() and p.stat().st_size==int(r['bytes']) and h(p)==r['sha256']
 with Image.open(p) as im:assert im.size==(int(r['width']),int(r['height']))
for n in scans:assert {r['part'] for r in manifest if int(r['scan'])==n}=={'whole','s1','s2','s3'}
with (root/'K58-03_inventory.csv').open() as f:inv=list(csv.DictReader(f))
assert all(r['transcribed']=='yes' for r in inv) and set(int(r['scan']) for r in inv)==set(scans)
assert all(r['hand'] in {'typed','Grothendieck','other hand','unknown'} for r in inv)
assert all(r['sheet_kind'] in {'text','cover','reused_typed','cancelled_draft','letter'} for r in inv)
types=Counter(x[2] for x in arguments(src,{'unsure','illegible','deleted','inserted','handwritten','margin','diagram'}))
invtypes=Counter(r['kind'] for r in inv)
for macro,kind in [('inserted','insertion'),('handwritten','handwritten'),('margin','margin note'),('deleted','deletion'),('diagram','diagram')]:assert types[macro]==invtypes[kind]
assert invtypes['display']==len(re.findall(r'(?<!\\)\\\[',src))
doubts=(root/'K58-03_doubts.md').read_text()
rows=read(root/'audit/witness_places.tsv');ids={r['id'] for r in rows}
assert len(ids)==178 and len({r['comparison crop'] for r in rows})==178
witness=doubts.split('## Witness check')[1];original=doubts.split('## Local doubts')[1].split('## Slips')[0]
for r in rows:assert '| '+r['id']+' |' in witness and '| '+r['id']+' |' in original and r['comparison crop'] in witness
assert re.findall(r'^## (.*)$',(root/'K58-03_mathnotes.md').read_text(),re.M)==['What the pages do','Statements left without proof','Questions and conjectures','Slips','Pointers','Remarks of the model']
assert len(re.findall(r'^## ',(root/'K58-03_notes.md').read_text(),re.M))==2
assert re.findall(r'^scan (\d+) done', (root/'progress.log').read_text(),re.M)==[str(n).zfill(3) for n in scans]
assert re.findall(r'^scan (\d+) audited', (root/'progress.log').read_text(),re.M)==[str(n).zfill(3) for n in scans]
print('Source attachment manifest verified: 60 names, byte counts, dimensions and SHA-256 digests.')
print('All 15 expected scan fragments, ordered assembly, source preamble, standalone wrapper, and required English sections present.')
print(f'Inventory: {len(inv)} entries, all marked yes. Scans 20–28 and 30–35 complete; no listed page unfinished.')
print('Final marks:',', '.join(f'{types[k]} '+k for k in ['unsure','illegible','deleted','inserted','handwritten','margin','diagram'])+'.')
print('Each of the 178 original doubt locations has a unique crop and an individual witness disposition or coverage statement.')
print('Doubt macros counted in the final assembled transcription, excluding the copies in the audit.')
