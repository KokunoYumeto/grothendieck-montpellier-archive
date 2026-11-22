from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work');own=root/'agents/reduction_descent'
expected='8ee230dfe7b2f9c158426266a505adbfd9af67caee6782e6521ccce607b8aaf8'
actual=hashlib.sha256((root/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert actual==expected,(actual,expected)
obs={
700:'Actually opened the complete individual PNG. B95 final eight-gap table, scope and audit paragraph are clear; the long code path wraps within the text block. The new B96 heading and standing field assumptions fit without clipped glyphs or a crowded footer.',
701:'Actually opened individually. The repaired B96.1 field/degree display is split clearly into two rows. The repaired B96.2 valuation/displacement display has distinct rows and a separate tag, with no overlap. Matrix B96.3, quotient point B96.4 and proof continuation are legible.',
702:'Actually opened individually. Quotient matrix B96.5 and its exact stabilizer prose fit. The opposite-field coordinate display B96.6, five-pair list B96.7 and conductor table B96.8 are fully visible; subscripts, inequality signs and table rules are clear.',
703:'Actually opened individually. The mixed-coefficient boundary proof and B96.9–10 displays are readable. Proposition B96.11 and the five-row conductor/threshold table B96.12 fit with no tag collision, clipped fraction or footer overlap.',
704:'Actually opened individually. Conductor ordering B96.13 and two-line Herbrand formula B96.14 are clear. The Colmez citation renders normally. The totally ramified degree25 hypothesis in the gap lemma and both B96.15 bounds are readable; the proof continues normally.',
705:'Actually opened individually. Gap formulas B96.16–17, the residual-wild exclusion theorem, two-row ten-pair census B96.18 and unequal-gap formula B96.19 all fit. The closing scope begins clearly and continues to the next page without overlap.',
706:'Actually opened individually. The B96 certificate path and exact audit runtimes fit. B97 section heading, actual division-field display B97.1, point-field degrees B97.2 and evaluation statement B97.3 are all clear and within margins.',
707:'Actually opened individually. The fixed-coordinate overline expression B97.4 renders correctly. The actual Galois-group display B97.5 and valuation display B97.6 are legible; the long proof and proposition status wrap without collisions.',
708:'Actually opened individually. Leading maps B97.7, boundary definition B97.8, coefficient identity B97.9 and boundary inequality B97.10 are fully visible. The B97.8 tag is placed below the long equation rather than over it. The conductor lemma and B97.11 display fit at the bottom.',
709:'Actually opened individually. The terminal bound B97.12, two-break formula B97.13, and complete field-intersection/degree display B97.14 are clear. The Colmez reference and start of the trace proposition have normal spacing and no missing glyphs.',
710:'Actually opened individually. The cyclotomic restriction B97.15 and positive difference B97.16 fit. The two remaining layer shapes B97.17, Lie-algebra proof and scope paragraph are legible. The program filename wraps safely inside the text block.',
711:'Actually opened individually. The B97 audit ending and B98 heading are clear. The two-break field lemma, bounds B98.1–2, Cohen-field definitions B98.3 and extension degrees B98.4 fit; superscripts, fractions and theorem statuses are legible.',
712:'Actually opened individually. Different estimates B98.5, Eisenstein derivative B98.6, cyclotomic different B98.7, aligned transitivity B98.8 and upper-break formula B98.9 are fully visible. Exact source citations render and the main theorem statement fits without clipping.',
713:'Actually opened individually. Repaired B98.10 is a clear four-line conductor display with a separate tag. The actual terminal-column argument, bounds B98.11–12 and restriction formula B98.13 fit with no collisions. The exact index equation B98.14 is fully visible and readable.',
714:'Actually opened individually. The exact upper/lower index proof and mu5 containment paragraph are clear. The source-scope, certificate path, rational-break counts and both audit runtimes wrap within the margins. No missing citation, glyph, overlap or clipping was observed.',
715:'Actually opened individually. Transition to Section C and its first three statements is clean. The displayed nilpotent-base and elliptic-curve examples, theorem statuses, citations and proof continuation are fully visible; no boundary-layout defect follows the new B section.'}
now=datetime.now(timezone.utc).isoformat()
rows=[]
for n,s in obs.items():
 p=root/f'outputs/qa36/page_{n:03d}.png'
 rows.append({'page':n,'png':str(p),'png_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'PASS','observation':s})
record={'status':'PASS','actual_utc':now,'pdf_sha256':actual,'pdf_pages':793,'pages':list(obs),
 'scope':'All sixteen complete PNGs700–715 were actually opened as separate images via view_image, at most two per call, and visually inspected. Includes all B96/B97/B98 displays, tables, tags, citations, source/program paths, proved statuses, page continuations, margins and the transition to Section C. No canonical source or PDF edit.',
 'page_observations':rows,'defects':[]}
out=own/'outputs/CP36_visual_QA.json';assert not out.exists(),'Preserve any prior QA before replacing'
out.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 f.write('\t'.join([now,'CP36_VISUAL_QA','PASS','Actually opened every complete page700–715; all repaired displays, tags, conductor tables, references, glyphs and paths are clear. No clipping or overlap.','outputs/CP36_visual_QA.json','Final PDF and every actually viewed PNG hashed; no canonical/source/PDF edit'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':now,'pages':list(obs),'pdf_sha256':actual,'record':str(out),'record_sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
