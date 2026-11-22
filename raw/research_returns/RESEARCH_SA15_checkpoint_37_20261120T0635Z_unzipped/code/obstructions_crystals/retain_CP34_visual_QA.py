"""Retain the four actually viewed final CP34 images; no canonical/register edit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pdf_sha='7bb59e472c44e11f66ac8fc102e9e3b4afddb717529388335d0de3f2750ad5a5'
assert sha(root/'RESEARCH_SA15_paper.pdf')==pdf_sha
comments={
 415:'Actually opened and inspected: section2.131 heading, block-slice lemma and proof, proposition2.485, DE-DS1/2 and averaging display all legible. Tags, status text and right margins clear; no clipping or overlap.',
 416:'Actually opened and inspected: proof continuation, DE-DS3, full regular-Lang-lift comparison and final scope remark. Blue references, subscripts, superscripts and proof-end squares intact; page break and margins clear.',
 417:'Actually opened and inspected: section2.132, lemma2.487 and two-item list, maps DE-GOS1/2, list closure before Both are square matrices, and character displays DE-GOS3/4/5. All maps and tags legible and within margins; continuation at bottom is coherent.',
 418:'Actually opened and inspected: continuation of DE-GOS5 proof, proof-end square, proposition2.488 and DE-GOS6, complete source-wall argument. No missing glyphs, clipped lines, overlapping tags or broken list/proof formatting.'
}
now=datetime.now(timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'pdf_sha256':pdf_sha,'pdf_pages':743,
        'pages':[415,416,417,418],
        'inspection_method':'Each final PNG was opened and displayed through view_image, in two bounded batches of two. Every assigned page was actually inspected; no unassigned-page inspection is claimed.',
        'observations':[{'page':p,'image':f'outputs/qa34/page_{p:03d}.png',
                         'image_sha256':sha(root/f'outputs/qa34/page_{p:03d}.png'),
                         'observation':comments[p]} for p in comments],
        'scope':'Visual layout/math-glyph/reference/page-break QA of the four assigned final pages only; no source or PDF edits.'}
out=own/'CP34_visual_QA.json'
with out.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','actual_utc':now,'pdf_sha256':pdf_sha,'pages':record['pages'],'record':str(out.relative_to(root))}))
