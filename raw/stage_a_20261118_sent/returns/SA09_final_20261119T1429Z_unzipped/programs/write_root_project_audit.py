#!/usr/bin/env python3
"""Record narrowly read project correspondences, without importing proof claims."""
import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
links=[
 ['our projects','138/70,75; MPL_138_046-089_transcription.tex:1135–1139,1215–1236','LM4_FINITE_GROUP_ACTIONS C.12; LM4_return/LM4_FINITE_GROUP_ACTIONS_paper.tex:5610–5628; C.12.1 at5660','Ordinary surface isotopy versus the stronger operator-centralizer kernel question','Both source passages and the actual project statement read. C.12 records the hyperbolic kernel π1(C_A0(uΓ),1) and leaves the general zero-level decision open. No equivariant theorem is inferred from ordinary Homeo0 contractibility. Textual verification only; project proofs not endorsed.','MPL_138_046-089#23;MPL_138_046-089#24'],
 ['our projects','138/62,85; MPL_138_046-089_transcription.tex:802–829,1580–1605','LM4_FINITE_GROUP_ACTIONS D.12; paper.tex:28889–28905','A geometric reversal example versus conjugacy of all full profinite involutions','Both endpoints read at the exact question. D.12 retains the full GT0 involution-conjugacy question despite narrower torsion assertions. A particular outer reversal and its square do not classify all involutions. The detailed later project results are not used as established inputs.','MPL_138_046-089#14;MPL_138_046-089#36;MPL_138_046-089#37;MPL_138_046-089#38'],
 ['our projects','138/66–68; MPL_138_046-089_transcription.tex:885–1072','LM4_FINITE_GROUP_ACTIONS F.7; paper.tex:46183–46206','Classical spherical signatures versus the completed A5-centralizer comparison','Source tame classification and actual F.7 question read. F.7 explicitly leaves C_Mhat(A5)=closure(C_M(A5)) unsupported at its stated proof step and does not assert falsity. This is a verified correspondence between questions, not this dossier’s adjudication of the cited published papers.','MPL_138_046-089#16;MPL_138_046-089#17'],
 ['our projects','138/66–68; MPL_138_046-089_transcription.tex:885–1072','LM4_SUCCESSOR checkpoint40, sections/b_remaining.tex, B.38; matching results.csv row B.38','Finite spherical types versus full congruence-level membership','Both endpoints read. B.38 leaves K5 and levels7,11 undecided and expressly requires comparison maps for transfer across levels. The manuscript’s finite PGL2 calculation does not furnish those maps.','MPL_138_046-089#16;MPL_138_046-089#17'],
 ['our projects','138/66–68; MPL_138_046-089_transcription.tex:885–1072','LM4_SUCCESSOR checkpoint40, sections/b_remaining.tex, B.39; matching results.csv row B.39','Solvable versus nonsolvable profinite centralizer scope','Both endpoints read. B.39 still labels its nonsolvable question Open and says it does not refute the published centralizer assertions. The report’s claimed solvable repair is not independently certified here.','MPL_138_046-089#16;MPL_138_046-089#17'],
 ['folder','138/19; MPL_138_001-045_transcription.tex:580–600','138/78; MPL_138_046-089_transcription.tex:1365–1380','Explicit S3 quotient and the later diagram’s identical distinguished set','Both passages read in full. The formula is written on19; assigning it to the unlabelled φ on78 remains reconstruction. Exact factorization and invariance were independently recomputed by early and middle workers.','MPL_138_001-045#25;MPL_138_046-089#28'],
 ['folder','138/83; MPL_138_046-089_transcription.tex:1496–1514','138/93–95; MPL_138_090-133_transcription.tex:88–90,114–119,162–171','Repeated common cyclotomic inertia character','Both passages read, including the doubtful i/ν and the later unambiguous independence of i. The full local inertia inclusion on P1 needs at least two punctures.','MPL_138_046-089#33;MPL_138_090-133#13;MPL_138_090-133#14'],
]
with (ROOT/'root_verified_links.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['kind','from','to','what','evidence','note_ids']);w.writerows(links)

events=[]
for key,scope in [
 ('ProjectLM4Return2026','Read C.12 lines5610–5628, D.12 statement beginning28889 and its local scope discussion, F.7 lines46183–46206. Confirmed the exact questions and retained Open labels. No claim that their many later proof assertions were checked.'),
 ('ProjectLM4Successor40','Read the full sections/b_remaining.tex, especially B.38–B.39, and the exact corresponding register rows. The report leaves both unresolved. No project code was run or restoration instruction executed.'),
 ('SA09-230','Cross-checked ordinary isotopy versus operator-centralizer comparison against the actual C.12 statement; the earlier note’s scope limitation is confirmed.'),
 ('SA09-242','Cross-checked the specific outer reversal with the distinct full involution-conjugacy question in LM4 D.12; no implication from one to the other was found.'),
 ('SA09-222','Cross-checked classical tame sphere signatures with the separate completed centralizer and congruence-level questions in F.7 and B.38–B.39; the earlier note correctly treats them as leads, not consequences.'),
 ('CL-SA09-138L-004','Independent check of the all-rank refutation: named-peripheral automorphisms preserve the closed normal subgroup generated by forgotten punctures, giving Γν→Γ2. For real rational punctures, the full geometric image is C2 generated by reflection. A three-cycle in the arithmetic S3 dessin orbit conjugates that reflection outside C2. This does not decide oriented normality.'),
 ('CL-SA09-138L-006','Independent check: the same forgetting map kills the pure oriented geometric closure. An arithmetic commutator has cyclotomic multiplier1 and nontrivial three-cycle image on the sextic orbit. It lies in Γν° outside the geometric closure for everyν≥2.'),
 ]:
  typ='independent re-proof' if key.startswith('CL-') else 'used and rechecked in this run'
  events.append([key,'2026-11-19','GPT-6 Astra Pro; effort inherited/not exposed; SA09/root',typ,scope])
with (ROOT/'root_check_events.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement id','date','who(model,effort,run)','type','outcome']);w.writerows(events)

(ROOT/'root_project_references.bib').write_text('''@unpublished{ProjectLM4Return2026,
  author = {{GPT-6 Astra research run}},
  title = {LM4\_FINITE\_GROUP\_ACTIONS: project return included in LM4\_SUCCESSOR\_background.zip},
  year = {2026},
  url = {https://chatgpt.com/library?file_id=libfile_fde3_f-f4db4a6dceb88191afbb8b942eff4a43_c6789dc4b4d481919ad633aabe6d84d0&account_id=personal},
  note = {verified},
  annotation = {Verification is of the stated textual endpoints C.12, D.12 and F.7, not proof endorsement. The project is model-generated research, separate from the manuscript and published literature.}
}

@unpublished{ProjectLM4Successor40,
  author = {{GPT-6 Astra research run}},
  title = {LM4\_SUCCESSOR: checkpoint 40},
  year = {2026},
  url = {https://chatgpt.com/library?file_id=libfile_fde3_f-a5a272d225d88191a680ef02ef5b3310_c6789dc4b4d481919ad633aabe6d84d0&account_id=personal},
  note = {verified},
  annotation = {Selected actual text and register extracted from historical\_data.tar, with hashes in outputs/extract\_checkpoint\_targets.json and outputs/extract\_checkpoint\_remaining.json. B.38 and B.39 read; the report still labels them Open. No external project code was executed.}
}
''')

middle=list(csv.DictReader((ROOT/'workers/cote138_middle/links.tsv').open(),delimiter='\t'))
selected=[]
# These five exact grouped reports were individually read and classified by
# the root reviewer. Separate newly verified endpoint rows above and in the
# early worker are retained; unresolved mixed reports are not claimed links.
for row in middle[-5:]:
 if row['kind']!='our projects':raise ValueError('Unexpected middle link order')
 selected.append(dict(action='move_to_reported_leads',**{'from':row['from'],'to':row['to']}))
(ROOT/'project_link_decisions.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_links':len(links),'events':len(events),'reported_grouped_leads':len(selected)}))
