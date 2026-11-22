from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
root=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
own=root/'agents/reduction_descent'
expected='7bb59e472c44e11f66ac8fc102e9e3b4afddb717529388335d0de3f2750ad5a5'
actual=hashlib.sha256((root/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert actual==expected,(actual,expected)
obs={
660:'Actually opened the complete page individually. B92 audit continuation and long code path wrap within the text block. B93 heading, field conventions, Lemma 4.295, and displays B-RD93.1–2 are clear and unclipped; normal bottom proof continuation.',
661:'Actually opened the complete page individually. Cyclotomic formulas B-RD93.3–4, both ramification tables B-RD93.5 and .7, and matrix displays .6 and .8 fit within the margins. All subscripts, fraction bars, table rules and tags are legible.',
662:'Actually opened the complete page individually. The quotient-average fraction B-RD93.9 fits and its tag is separate. Proposition proof and terminal-bound lemma flow normally; bounds B-RD93.10 and the primitive-point discussion are clear without overlap.',
663:'Actually opened the complete page individually. Both actual point-field arguments, formulas B-RD93.11–15, the fractional conductor estimate, and final proof square are legible. No clipping, crowded equation tags or displaced footer.',
664:'Actually opened the complete page individually. The crossing theorem, cyclotomic lower bound B-RD93.16, determinant formula and contradiction are fully visible. Proved scope and retained-code path wrap cleanly; blue citations render correctly. Audit paragraph continues normally to page 665.',
665:'Actually opened the complete page individually. B93 audit continuation is readable and completes before the next section. Section 5 heading and following propositions/displays fit with normal spacing, glyphs, proof squares and footer; no clipping or overlap.'}
now=datetime.now(timezone.utc).isoformat()
rows=[]
for n,s in obs.items():
 p=root/f'outputs/qa34/page_{n:03d}.png'
 rows.append({'page':n,'png':str(p),'png_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'PASS','observation':s})
record={'status':'PASS','actual_utc':now,'pdf_sha256':actual,'pdf_pages':743,'pages':list(obs),'scope':'All six complete PNGs actually opened individually via view_image and visually inspected. Checked text, displayed formulas, tables, tags, conductor bounds, proof continuations, statuses, citation glyphs, path wrapping, margins and footers. No canonical source or PDF changes. An earlier truncated batch was not counted; pages 660–662 were individually reopened before this verdict.','page_observations':rows,'defects':[]}
out=own/'outputs/CP34_visual_QA.json'
assert not out.exists(), 'Preserve any prior QA before replacing'
out.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 f.write('\t'.join([now,'CP34_VISUAL_QA','PASS','Actually opened and inspected all six pages 660–665; no clipping, overlap, missing glyph, table/tag/path-wrap or conductor-display defect.','outputs/CP34_visual_QA.json','Actual individual image openings; final PDF and each PNG SHA256 retained; no source edits'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':now,'pages':list(obs),'pdf_sha256':actual,'record':str(out),'record_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
