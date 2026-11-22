from pathlib import Path
from datetime import datetime, timezone
import csv
root=Path('/workspace/scratch/6b22741c5cd2/RESEARCH_SA20')
own=root/'agents/singularities_duality'
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
draft=own/'logs/A135_base_four_comparison_fibre_draft.tex'
s=draft.read_text()
s=s.replace('all relative PL structures have the original PL isomorphism type.', 'all relative PL structures have the original PL isomorphism type.\nThe connecting maps and any resulting extension data in (A.135.3)\nremain unevaluated; the abstract homotopy type of $F_A$ alone does\nnot determine $F_P$.')
s=s.replace('\\begin{proof}\n\\textbf{The exact', '\\begin{proof}\n\\textbf{The exact')
s=s.replace('\\begin{proof}\n\\textbf{Top restriction', '\\begin{proof}\nIf $B$ is empty, every space in the statement is a point, so suppose\nthat $B$ is nonempty.\n\\textbf{Top restriction')
s=s.replace('is a weak equivalence in both categories. This argument also provides\na common collar for each finite parameter family.', 'is a weak equivalence in both categories. Here a simplex of\n$H_C^{\\mathrm{col}}$ fixes one common collar for its whole parameter\nsimplex; the collar may shrink when passing to a different simplex.\nA finite family of simplices admits a common smaller collar. This is\nthe direct-limit complex with this convention, not an unproved\nidentification with the singular complex of a union of topological\ngroups. This argument also provides a common collar for every finite\nrelative nullhomotopy.')
draft.write_text(s)
part=own/'part_base_four_comparison.tex'
assert not part.exists()
part.write_text('% AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).\n\\subsection{The comparison fibre in base dimension four}\n\n'+s[s.index(r'\begin{saresult}'):])
bib=own/'references.bib'
b=bib.read_text()
needle='so they do not directly treat a cylinder with a free four-dimensional top. Accessed2026-11-19.}'
replace='so they do not directly treat a cylinder with a free four-dimensional top. For A135, EssayV equation1.5 and its relative-neighbourhood paragraph p229; relative classification3.2 p240; Theorem5.5(I) p251; universal Kirby--Siebenmann square and chosen-lift untwisting pp252--253 were all visually checked by the author and independent reviewer. Root also independently read the original source and checked the based orbit-component restriction. Accessed2026-11-19.}'
assert needle in b
bib.write_text(b.replace(needle,replace))
with (own/'results.csv').open('a',newline='') as f:
 csv.writer(f).writerow(['A.135','For closed PL4 base B the fully boundary-fixed PL-TOP comparison fibre is Map(B K(Z/2 1)); a based fibre sequence relates it to free-top and ordinary-aut comparison fibres','Proved under stated hypotheses','agents/singularities_duality/part_base_four_comparison.tex A.135','KS1977 EssayV1.5 relative p229;3.2 p240;5.5(I) p251;5.6 pp252-253; explicit joint collar and horn constructions','119/148; 121/002-003; A.1(b); Lead L1','Exact structural reduction only. Standard-structure orbit component and common-collar simplex convention explicit. Connecting maps and extension data unevaluated; no full comparison or component-surjectivity claim. Base3 extension fails H4 relative both ends=H3(B;Z2).'])
rows=[
('A.135','singularities_duality','complete proof and source audit','PASS: explicit evaluation Kan lifts, common-collar conjugation, neighbourhood-fixed orbit component, open5D relative classification, universalKS untwisting, two loop shifts and exact segment. Original229/240/251/252/253 visually inspected.'),
('A.135','root','independent full mathematical and original-source audit received','PASS with precise common-collar convention and unknown connecting/extension data added. Original229/240/252 visually inspected; related5.5 input already opened. Authorized structural theorem promotion after checkpoint12; no main full-space closure inferred.'),
('A.135','higher_comparison2','independent full proof and source audit received','FULL PASS; agents/higher_comparison/A135_independent_audit.md. Viewed original229/240/251/252/253; read241. Checked collar inverse, exact horn maps, base orbit restriction, homotopy fibre commutation and all loop indices. Stronger stabilization model and base3 variant excluded from PASS.'),
('A.1(b)','singularities_duality','remaining gate precision after A135','Fully boundary-fixed base4 comparison fibre computed; free-top fibre still requires ordinary4D automorphism comparison and actual connecting data. No claim of surjectivity on components or full TOP model. Base3 both-end relative H4 obstruction explicit.')]
with (own/'checks.tsv').open('a') as f:
 for sid,who,kind,outcome in rows:f.write('\t'.join([sid,now,who,kind,outcome])+'\n')
with (own/'report.md').open('a') as f:
 f.write(f'''\n## {now} — A.135: exact relative comparison fibre in base dimension four\n\nA.135 computes the homotopy fibre of fully boundary-fixed joint PL-to-TOP automorphisms of B4×I as Map(B,K(Z/2,1)). An explicit parameter-preserving horn lift gives the evaluation fibrations. A finite, jointly PL collar-compression formula turns pointwise boundary fixing into a common fixed collar for each simplex and each finite relative family. The relative structure theorem is applied to the open5-manifold B×R with BOTH exterior ends fixed, so no uncontrolled4-dimensional boundary is silently discarded. Only the standard-structure component of the automorphism orbit is used. The original universal KS square, with the chosen standard PL lift, supplies the untwisting of the section space.\n\nThe resulting based homotopy-fibre sequence relates this computed fibre to the free-top comparison fibre and the ordinary automorphism comparison fibre of B4. The right-hand comparison, the connecting maps, and any extension data remain unevaluated. Its abstract homotopy type alone would not determine the free-top fibre, and no component-surjectivity assertion is made. Root and the resumed independent higher-comparison agent passed all steps after the two precision edits. No new main-row full computation is counted.\n\nThe tempting base3 transfer has an exact failure: extending relative structures from a fixed bottom to a prescribed top germ requires the dimension4 restriction theorem with BOTH ends controlled. Its required H4 relative group is H3(B3;Z/2), nonzero for a nonempty closed connected base. The vanishing for the bottom-only pair does not justify that fibration. A stronger base4 collar-square model remains a separate research candidate.\n''')
(own/'logs/A135_promotion_receipt.txt').write_text(now+'\nPromoted A135 after root and independent full audit.\nNew included candidate part: agents/singularities_duality/part_base_four_comparison.tex\nUpdated own references.bib/results.csv/checks.tsv/report.md. Root should input after A134.\n')
print(now)
