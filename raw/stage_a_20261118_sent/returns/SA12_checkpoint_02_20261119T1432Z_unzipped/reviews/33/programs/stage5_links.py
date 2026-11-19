"""Links assessed from both available passages; quarantined targets stay unavailable.
Only transcription of already-read project-register rows is mechanical below.
"""
import csv,re,json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
ROOT=O.parents[2]/'source'
L=[]
def add(kind,fr,to,what,evidence,notes=''):
 L.append([kind,fr,to,what,evidence,notes])
add('folder','33/12:371','33/22:575–598;24:626–646','Requested local fundamental class followed by its divisor/product construction','Both passages read. The later construction answers the definition request; regular-sequence independence remains asserted.','MPL_33_002-049#12,#24,#26,#27')
add('folder','33/14:409','33/26:708–720','Absolute-purity question and qualified low-vanishing applications','Both passages read. Smooth, regular/excellent characteristic-zero and normal codimension-one regimes are kept separate.','MPL_33_002-049#15,#38')
add('folder','33/14:405','33/32:863–871','Noncanonical Tate twists become the relative orientation sheaf','Both passages read; componentwise relative dimension is inserted at32. Primitive-root rescaling convention needs separate scan check.','MPL_33_002-049#17,#18')
add('folder','33/14:417–423;16:444–450;18:484–504;20:504–534','33/42:1092–1123','Restarted degreewise compact-support construction is promoted to a derived functor','Both sides read, including cancelled portions and revised finite-amplitude hypothesis; no chronology beyond local source order inferred.','MPL_33_002-049#21,#43,#44')
add('folder','33/24:626–646;26:690–704','33/28:754–777;30:823–837','Local class, support edge map and global class','Both sides read. The edge isomorphism needs low local-cohomology vanishing; proper-support passage needs support proper over the base.','MPL_33_002-049#26–#32')
add('folder','33/20:522–534','33/34:890–908','Étale trace gives the relative-dimension-zero normalization of global trace','Both formulas read. Trace is summation on finite geometric fibres.','MPL_33_002-049#23,#33,#34')
add('folder','33/28:773–777;30:823–830','33/34:890–908','Promised point-class basis result and normalized global trace','Both passages read. Rational points and geometric connectedness retained; the curve case is recalled, not reproduced.','MPL_33_002-049#31,#34,#35')
add('folder','33/24:642–646;34:890–908','33/36:923–959','Local/global Gysin–trace compatibility','Both sides read. The overwritten diagram is not certified arrow by arrow; modern derived square is a reconstruction.','MPL_33_002-049#27,#34,#36,#37')
add('folder','33/38:1004–1036;40:1056–1078','33/44:1144–1161;48:1241–1261','Derived pullback/Hom formalism supports base change and duality','Both sides read. Correct support functor and base coefficient are needed; all-degree duality does not justify the partial-range conclusion.','MPL_33_002-049#39–#50')
add('folder','33/7:186–202;5:140–150','33/15:425–441;17:467–479;21:541–570','Coxeter diagram restrictions and promised realization','Both sides read despite nonchronological source pagination; the original typescript is n°391, author/date unverified.','MPL_33_002-049#51,#58,#59')
add('folder','33/19:497–501','33/23:603–623;25:653–685;27:726–751;29:783–819;31:845–858;37:966–1001;49:1266–1291','Lattice criterion and exceptional root data','All displayed source passages read and numerical data rechecked by exact code. New E6 quotient-generator error distinguished from the previously noted exponent error.','MPL_33_002-049#53–#57,#60–#64')
add('folder','33/41:1083–1089;43:1127–1141;45:1166–1190','33/39:1041–1053','Product-of-stalks/sheafification argument reconstructed in original English source-page order','Both ends read: source pages34,38,39,40, with35–37 absent. The full-faithfulness step fails on Sierpinski; enough-injectives statement is not thereby disproved.','MPL_33_002-049#67–#70')
add('folder','33/47:1206–1233','33/47:1199–1204','Filtered-module construction lies below an unresolved preceding implication','Both parts read. The concrete filtration distinction is checked; it does not identify absent conditionsb,c. Whole-sheet cancellation preserved.','MPL_33_002-049#71,#72')
pub=[
 ('33/4:128–156;6:156–167','SGA4 XII5.1;XVI1.1,1.6; Stacks095T/0EYU','Proper/smooth base change and separably closed extension invariance','Exact modern theorem hypotheses opened. No invertibility restriction added to proper base change.','#3,#45'),
 ('33/6:169–181','SGA4 XVI4.1; SA12_SGA4III','Complex comparison','Both leaf and theorem read; publication requires proper f or constructible F. The unrestricted leaf wording needs correction.','#4,#5'),
 ('33/10:280','SGA4 XVI2.1–2.2; Milne20.2','Proper smooth local constancy','Both statements read; finite local constancy does not imply free modules overZ/n.','#9'),
 ('33/10:282–296','Milne15.1; SGA4 XIV3.1','Cohomological-dimension and affine bounds','Source inequality and modern strict bound checked.','#10'),
 ('33/12:346–355','Stacks09XP; Hartshorne Local Cohomology §§1–2, LNM41(1967), Harvard seminar1961','Support cohomology and the explicit Hartshorne1961 margin','Support theorem opened; Hartshorne official metadata confirms seminar date but exact1961 circulated text not collated.','#11,#14'),
 ('33/12:358–371;14:409–415','SGA4 XVI3.7–3.10; Riou XVI3.1.1,3.1.3–3.1.4','Geometric/absolute purity and normal crossings','Exact published statements opened; latter theorem is not the same as one-stratum purity for a union of components.','#15,#16'),
 ('33/16:462;18:482','ILO XIII1.1.1','Nonproper constructibility','Both leaf and modern theorem read. Quasi-excellence and invertible coefficients are explicit in the modern statement.','#20'),
 ('33/18:484–504;20:504–534;42:1092–1123','SGA4 XVII5; Stacks0F7J,0G2A,0GL0','Compact-support functor, composition, amplitude and constructibility','Primary statements opened; bounds and coefficient scope retained.','#21,#43,#44'),
 ('33/22:575–598;24:626–646;26:690–704','SGA4 XVIII; Riou XVI2.3.1–2.3.2','Regular-immersion fundamental class, base change and products','Exact construction properties in Riou opened; divisor-unit invariance re-proved here.','#24,#26–#29'),
 ('33/34:890–908;36:923–959','SGA4 XVIII2.9–2.10; Riou XVI2.5.13','Trace and compatibility with Gysin','Both formulas and source results opened. Ordinary versus geometric fibre connectedness separated.','#33–#37'),
 ('33/38:1004–1036;40:1056–1078','Stacks06YV,0B6E','Derived pullback and global/internal Hom','Exact current results opened. Modern unbounded methods distinguished from the notebook’s bounded classical construction.','#39–#42'),
 ('33/48:1241–1261','SGA4 XVIII3.2.5–3.2.6; Riou XVI3.1.3','Duality and the failed partial-range extrapolation','Duality theorem and Z/n self-injectivity statement opened; punctured-divisor formula supplies the counterexample. No published unrestricted partial-range theorem identified.','#46–#50'),
 ('33/5:140–150;7:186–202;15:425–441;21:541–570','Coxeter1934 §9, classification tables; Bourbaki Lie IV–VI(1968)','Finite reflection/root classification','Coxeter primary text opened; Bourbaki publication/chapter metadata opened, exact n°391 draft unlocated.','#51–#64'),
 ('33/9:237–277','Bourbaki Lie II–III(1972); Wehler2017 Theorem3.5 lead','Formal groups, tangent bracket, editorial placement','Bourbaki metadata and WehlerPDF opened; exact Tribu62 source/missing definitions unlocated. No attribution proof.','#65,#66'),
 ('33/39:1041–1053;41:1083–1089;43:1127–1141;45:1166–1190','Kleisli–Wu1964 pp415–423, especiallyp422 and reference5; Gray Columbia mimeograph lead','Category-valued sheaves source family','Kleisli–Wu primary text opened, naming right-perfect/enough-small-objects hypotheses and Gray mimeograph. Gray1965 full article access failed; exact English fragment not identified.','#67–#70'),
 ('33/47:1199–1233','EGA IV4(1967) §19.6; missing preceding §19.5 conditions','Regular sequences relative to a filtered module','Official publication metadata opened. Primary PDF too large for the available open operation; exact b,c remain unavailable.','#71,#72'),
]
for fr,to,what,evidence,notes in pub:
 add('published work',fr,to,what,evidence,'MPL_33_002-049'+notes)
# Every project-register row was manually read. Preserve the entire row as provenance;
# no mathematical status is inferred from its text or from parsing.
notes_path=ROOT/'SA12_notes/pro/MPL_33_002-049_notes.md'
txt=notes_path.read_text(); sections=[('### A. Individually listed register entries: 29 of 29',86),('### B. Claims explicitly named in the referee paragraph: 10 of 10',87),('### C. Other IDs and locators mentioned inside summaries',88),('### D. Run-state entries',89)]
Q=[]
for heading,num in sections:
 start=txt.index(heading); end=txt.find('\n### ',start+5)
 if end<0: end=txt.find('\n## ',start+5)
 if end<0:end=len(txt)
 for line in txt[start:end].splitlines():
  if not line.startswith('| **'): continue
  cells=[c.strip() for c in line.strip('|').split('|')]
  name=cells[0].replace('**','')
  evidence='Origin note read in full; target documents are absent from the complete attached file inventory. No target proof/status checked. The supplied status remains an earlier-run report, not a result of SA12.'
  add('our projects',f'MPL_33_002-049#{num}',name,'Quarantined earlier-run lead; target unavailable. '+ ' | '.join(cells[1:]),evidence,f'MPL_33_002-049#{num}')
  Q.append(dict(note_id=f'MPL_33_002-049#{num}',target=name,source_row=line,target_status='unavailable in attachment',review_status='origin read; no target verification or promotion'))
context_rows=[]
entry=0
for chunk in re.split(r'(?m)(?=^### )',txt):
 if chunk.startswith('### '):entry+=1
 for para in chunk.split('\n\n'):
  if not para.startswith('**Context / register comparison:**'):continue
  body=para.removeprefix('**Context / register comparison:**').strip()
  add('our projects',f'MPL_33_002-049#{entry}','Exact external targets/locators in the retained comparison: '+body,'Earlier-run context comparison, quarantined verbatim; not a theorem of the present source.','Origin note and corresponding current transcription passage read. Both named context files (same_cote_33/MPL_33_098-146_notes.md and notes/RESULTS_STATE.md) are absent from the attachment. Every target named in this paragraph therefore remains unavailable; no target proof or status verified.',f'MPL_33_002-049#{entry}')
  context_rows.append(dict(note_id=f'MPL_33_002-049#{entry}',comparison=body,target_status='unavailable in attachment',review_status='origin read; no target verification or promotion'))
for row in L:
 expanded=[]
 for a,b in re.findall(r'#(\d+)(?:–#?(\d+))?',row[5]):
  expanded += [f'MPL_33_002-049#{n}' for n in range(int(a),int(b or a)+1)]
 row[5]=';'.join(dict.fromkeys(expanded))
with (O/'links.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['kind','from','to','what','evidence','note_ids']);w.writerows(L)
(O/'PROJECT_LEADS.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
(O/'PROJECT_CONTEXT_PARAGRAPHS.json').write_text(json.dumps(context_rows,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(L)} links: {len(Q)} quarantined project/register rows plus {len(context_rows)} individual earlier-run comparison paragraphs; {len(L)-len(Q)-len(context_rows)} checked local/published comparisons.')
print('Project target availability checked against attached source file inventory, not inferred from a failed keyword search.')
