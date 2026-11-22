from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
root=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
own=root/'agents/reduction_descent'
expected='d951489941df01521c8f1309fa88a77580a9cc0248672284f0bfaf9cc649d738'
actual=hashlib.sha256((root/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert actual==expected,(actual,expected)
obs={
675:'Actually opened the complete PNG individually. B93 audit ending, B94 heading, field assumptions, displays B-RD94.1–3 and actual matrix group are clear. Tags, braces, subscripts and proof continuation fit the text block.',
676:'Actually opened individually. The quotient matrix B-RD94.4, long conductor ordering .5, break congruences .6 and conjugation formula .7 all fit; no tag collision, clipped glyph or overlap.',
677:'Actually opened individually. The commutator inequality .8, point-coordinate display .9, pair list .10, common-high formula .11 and two-case coefficient table .12 are legible. The bottom table and footer remain separated.',
678:'Actually opened individually. Mixed coefficient inequalities .13, parameter lists .14–15 and lower-break formulas .16–17 fit. The repaired .16 list visibly has proper spacing, with no literal quad text or missing backslash artifact.',
679:'Actually opened individually. Cyclotomic conductor .18, compositum discussion and terminal-bound table .19 are fully visible; fraction bars, inequality signs, table headings and proof continuations are clear.',
680:'Actually opened individually. Actual point-field definitions and stacked degree display .20, Newton valuations .21, high-point bound .22 and conductor estimates .23–24 are clear and within the margins.',
681:'Actually opened individually. Low-point bounds .25–26, theorem pair lists .27–28, both positive-gap formulas, determinant expression and scope remark are legible. No table, equation tag, prose or footer overlap.',
682:'Actually opened individually. B94 program path wraps safely within the text block and its audit runtimes are readable. B95 heading, remaining-pair display .1, critical-coefficient lemma and display .2 are clearly laid out.',
683:'Actually opened individually. B95 coordinate table .3, first-degree equation .4, inequalities .5–6, profile table .7 and fractions .8 are fully visible; tables and equation tags remain distinct.',
684:'Actually opened individually. B95 break list .9, conversion definitions .10, terminal-bound table .11, shared-diagonal relation .12 and lower-break tables .13–14 fit. The corrected between-breaks surviving-kernel sentence is readable; the wide .14 table does not clip.',
685:'Actually opened individually. Both actual-field conversions .15–17 and threshold table .18 are clear. The full-Iwahori theorem and group display .19 fit at the bottom with a separate footer and normal proof continuation.',
686:'Actually opened individually. B95 eight-gap table .20, minimum-gap prose, final scope and audit record are legible; long code path wraps without overflow. The transition to Section 5 and its opening proposition have normal spacing and no clipped glyphs.'}
now=datetime.now(timezone.utc).isoformat()
rows=[]
for n,s in obs.items():
 p=root/f'outputs/qa35/page_{n:03d}.png'
 rows.append({'page':n,'png':str(p),'png_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'PASS','observation':s})
record={'status':'PASS','actual_utc':now,'pdf_sha256':actual,'pdf_pages':765,'pages':list(obs),'scope':'All twelve complete PNGs were actually opened individually via view_image and visually inspected. Scope includes B94/B95 equations, actual fields, conductor tables, gap tables, tags, proof continuations, proved statuses, glyphs, path wrapping, margins and footers. No canonical source or PDF change.','page_observations':rows,'defects':[]}
out=own/'outputs/CP35_visual_QA.json'
assert not out.exists(), 'Preserve any prior QA before replacing'
out.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 f.write('\t'.join([now,'CP35_VISUAL_QA','PASS','Actually opened and inspected every complete page 675–686; no clipping, overlap, missing glyph, table/tag/path-wrap or conductor-display defect.','outputs/CP35_visual_QA.json','Actual individual image openings; final PDF and each PNG SHA256 retained; no source edits'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':now,'pages':list(obs),'pdf_sha256':actual,'record':str(out),'record_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
