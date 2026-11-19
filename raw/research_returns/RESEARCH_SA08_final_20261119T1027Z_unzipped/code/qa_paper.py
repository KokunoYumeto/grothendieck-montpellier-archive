"""Parse real LuaLaTeX warnings and render all corrected-overflow locations.

This creates a review record, not an automatic visual approval. The human/model
inspection of the emitted page images must be recorded separately.
"""
from pathlib import Path
import argparse,re,json,hashlib
import fitz
from PIL import Image,ImageOps,ImageDraw

parser=argparse.ArgumentParser();parser.add_argument('build')
parser.add_argument('--extra-pages',type=int,nargs='*',default=[])
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
log=root/'logs'/args.build
content=log.read_text()
pattern=r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)'
warnings=[float(v) for v in re.findall(pattern,content)]
baseline=root/'logs/typeset_build_12_pass3.txt'
before=[float(v) for v in re.findall(pattern,baseline.read_text())]
if any(v>2 for v in warnings):raise SystemExit('Overflow above 2 pt remains')
if re.search(r'(undefined|Fatal error|duplicate destination|Package hyperref Warning)',content):raise SystemExit('Unresolved build warning')
pdf=root/'RESEARCH_SA08_paper.pdf';document=fitz.open(pdf)
anchors=['The result remains incomplete', 'specified strict interpretation','A-018.', 'proves (B-16)',
 'B-16. Proved','B-17. Proved','Finite verification and literature search',
 'Breen gives his','flasqueness after every tensor product','C10:',
 'original cote 136 PDF', 'Finite checks and the remaining gate']
new_content_anchors=['A-024:', 'D-025:', 'D-026:', 'C13:', 'A-026:', 'C14:', 'C15:', 'D-027:', 'C16:', 'C17:', 'D-028:', 'C18:', 'C19:', 'C20:', 'C21:', 'C22:', 'C23:', 'D-029:', 'D-030:', 'D-031:', 'C24:', 'C25:', 'C26:', 'C27:', 'C28:', 'C29:', 'C30:', 'C31:', 'C32:', 'C33:', 'C34:', 'C35:', 'C36:', 'Strict commutativity and the recovered higher operations', 'D032:', 'The script B_pd_square_normalization.py', 'Integral uniqueness: the remaining exact assertion']
texts=[' '.join(p.get_text().split()) for p in document]
locations={a:[i+1 for i,t in enumerate(texts) if a in t] for a in anchors}
new_locations={a:[i+1 for i,t in enumerate(texts) if a in t] for a in new_content_anchors}
missing=[a for a,v in locations.items() if not v]
if missing:raise SystemExit('Missing previous-overflow anchor: '+repr(missing))
sample=sorted(set([1,4,10,16,20,26,38,44,45,len(document)]))
pages=sorted(set(sample+args.extra_pages+[p for v in locations.values() for p in v]+[p for v in new_locations.values() for p in v]))
if any(p<1 or p>len(document) for p in pages):raise SystemExit('Invalid inspection page')
folder=root/'logs/pdf_qa'/log.stem;folder.mkdir(parents=True,exist_ok=True)
images=[]
for number in pages:
    out=folder/f'page-{number:03d}.png'
    pix=document[number-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False)
    pix.save(out);images.append((number,out))
montages=[]
for at in range(0,len(images),4):
    chunk=images[at:at+4];thumbs=[]
    for number,p in chunk:
        img=Image.open(p).convert('RGB');img.thumbnail((840,1188))
        tile=Image.new('RGB',(860,1230),'#dddddd');tile.paste(img,((860-img.width)//2,30))
        ImageDraw.Draw(tile).text((12,9),f'Page {number}',fill='black');thumbs.append(tile)
    sheet=Image.new('RGB',(1720,2460),'white')
    for j,tile in enumerate(thumbs):sheet.paste(tile,((j%2)*860,(j//2)*1230))
    path=folder/f'montage-{at//4+1:02d}.png';sheet.save(path);montages.append(str(path))
record={'build_log':str(log.relative_to(root)),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
 'pages':len(document),'baseline_log':str(baseline.relative_to(root)),
 'overfull_before':len(before),'overfull_before_above_2pt':sum(x>2 for x in before),
 'maximum_before_pt':max(before,default=0),'overfull_after':len(warnings),
 'overfull_after_above_2pt':sum(x>2 for x in warnings),'maximum_after_pt':max(warnings,default=0),
 'corrected_overflow_locations':locations,'new_content_locations':new_locations,'spread_sample':sample,'rendered_pages':pages,
 'rendered_page_count':len(pages),'montages':montages,'visual_review':'awaiting explicit image inspection'}
(folder/'qa_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
