"""Integrate fully read and independently audited higher symplectic/rank reductions."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
def sha(n): return hashlib.sha256((R/n).read_bytes()).hexdigest()
frozen={
 'agents/g34_eightfolds/bireflection/higher_odd_symplectic_section.tex':'eb760afa97ee57230236ce9058085a4225a78a502e2aa57df5c9efb9637a9ccc',
 'agents/imprimitive/unitary_nonweil/unitary_nonweil_section.tex':'10addbba497f6f924fb5925732fec27a6ca59308b4abe473220cdf0aac4d76c9',
 'agents/imprimitive/unitary_nonweil/linear_nonweil_section.tex':'8f66c40c4bb8c1e2f086ec1dcdc991afcfaad418924a4cf3c68f5af884fabea2'}
for n,h in frozen.items(): assert sha(n)==h,n
q=R/'QUESTIONS.tsv'
rows=list(csv.DictReader(q.open(),delimiter='\t')); fields=list(rows[0])
assert not {'Q2bk','Q2bl'} & {r['id'] for r in rows}
(R/'research/gates_before_hos_nonweil.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q2i'},indent=2)+'\n')

changes=[
 ('agents/g34_eightfolds/bireflection/higher_odd_symplectic_section.tex',
  'This is a complete new author derivation, submitted for independent\nwhole-proof review.',
  'This complete new derivation has passed whole author, root and\nindependent peer proof reviews, with separately executed exact certificates.'),
 ('agents/imprimitive/unitary_nonweil/unitary_nonweil_section.tex',
  'The complete proof and the exact constant certificate have been checked\nby the author; independent whole-proof review is requested.',
  'The complete proof, invoked primary sources and exact constants have\npassed author, root and independent peer reviews. The peer certificate\nindependently reconstructs every quantitative reduction.'),
 ('agents/imprimitive/unitary_nonweil/linear_nonweil_section.tex',
  'New author derivation, completely written and checked by the author,\nwith an executed exact constant certificate. Independent review is\nrequested.',
  'New derivation, completely read and checked by the author, root and\nan independent peer, with separately executed exact constant certificates.')]
for n,old,new in changes:
 p=R/n;s=p.read_text();assert old in s,n;p.write_text(s.replace(old,new))
bib='agents/imprimitive/unitary_nonweil/unitary_nonweil_bibitems.tex'
p=R/bib;s=p.read_text()
old='Corollary~8.6 with complete proof, pp.~67--68.'
assert old in s
s=s.replace(old,old+'\nComplete general-linear dual-pair argument, \\S8.1, pp.~55--61,\nincluding Lemma~8.2 and equations (8.9)--(8.11), pp.~59--60;\nlevel-one Weil identification, p.~61.')
p.write_text(s)

p=R/'HODGE_DIVISION.tex';s=p.read_text()
anchor=r'\input{research/exceptional_small_section.tex}'
assert anchor in s and all(n not in s for n in frozen)
s=s.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+n+'}' for n in frozen))
anchor=r'\input{research/exceptional_small_bibitems.tex}'
assert anchor in s and bib not in s
s=s.replace(anchor,anchor+'\n'+r'\input{'+bib+'}')
old='Other small-field higher-rank Lie representations remain outside these\nexclusions.'
new=r'''D-HOS-03--06 excludes every higher symplectic core
$\operatorname{Sp}_{2n}(q)$ with $n\ge4$ and odd $q\ge7$,
allowing arbitrary mixed fields and ranks, all compatible normalizers,
scalar actions and factor permutations. Its explicit elementary
normalizer estimate $9234/55223>1/6$ forces total degree
$e\le165669/181<916$, below every factor degree $1029$ or more.
Only $q=3,5$ remain in this higher odd-symplectic family.
D-UNW-01--03 and D-LNW-01 give the explicit natural-dimension cutoff
$n<10^{61}$ for transitive primitive factorwise tensor-indecomposable
unitary and linear cores. Above that cutoff all non-Weil factors have
full-normalizer support at least $11e/60$, forcing $e\le30$;
degree separation and the already proved Weil exclusions treat the
other alternative. In the nonsplit main-source scope the existing
field bound $q\le27$ also applies. This makes those remaining group
ranges finite but does not enumerate or settle them. Other small-field
higher-rank Lie representations remain outside these exclusions.'''
assert old in s;s=s.replace(old,new);p.write_text(s)
for r in rows:
 if r['id']=='Q2i':
  old='Other small-field higher-rank Lie cores remain.'
  new=('D-HOS-03--06 excludes arbitrary mixed higher symplectic Sp(2n,q) cores with n>=4 and every oddq>=7, all covers and compatible normalizers, without selfduality or determinant premises. Uniform support9234/55223>1/6 gives e<=165669/181<916 below degree1029; onlyq3/q5 remain in that family. D-UNW-01--03 and D-LNW-01 force naturaln<10^61 for transitive primitive factorwise tensor-indecomposable unitary and linear cores; all large-rank non-Weil factors have full-normalizer support11/60 and e<=30, while degree separation and earlier Weil exclusions treat levelone. The nonsplit main source also hasq<=27. These finite group ranges have not been enumerated. Other small-field higher-rank Lie cores remain.')
  assert old in r['finding_ids_or_current_gate']
  r['finding_ids_or_current_gate']=r['finding_ids_or_current_gate'].replace(old,new)
rows.extend([
 dict(zip(fields,['Q2bk','Prompt target2; higher odd symplectic normal cores','Can a mixed higher symplectic core over odd fields at least seven supply actual period rank nine?','refuted','D-HOS-03--06: arbitrary ranksn>=4 and oddq>=7, central covers and full compatible normalizers. Elementary shears, Heisenberg carriers, elliptic tori and explicitq9 descent yield support9234/55223 and e<916 below degree1029. Full root and independent peer reviews PASS; q3/q5 remain outside.'])),
 dict(zip(fields,['Q2bl','Prompt target2; general linear and unitary natural-rank cutoff','Can a transitive primitive factorwise tensor-indecomposable linear or unitary core have natural dimension at least10^61?','refuted','D-UNW-01--03,D-LNW-01: published explicit LT2024 exponent and exact GLT2020 dual-pair estimates yield all-non-Weil ratio4/15 and full-normalizer support11/60, includingq2. Actual source budget forces e<=30 below every factor. Degree separation and proved Weil theorems give naturaln<10^61. Main nonsplit fieldq<=27 gives finite, unenumerated groups; no complete residual classification. Whole author/root/peer reviews and separate exact certificates PASS.']))])
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)

events=[
 ('D-HOS-03--06','targeted proof check','Root previously read the entire436-line mathematical proof and both complete trace-form/row-normalizer expansions to the final448-line frozen proof, and now read the entire independent peer report. PASS primary-space trace forms, isotropic shears, Heisenberg moving carrier, all semisimple cases, diagonal involutions, q9 symplectic descent without diagonal-invariance assumption, tensor cycles and actual rank-nine budget. Only status text changes at integration.',list(frozen)[0]+'; agents/imprimitive/audit_higher_odd_symplectic/PEER_AUDIT.md'),
 ('D-HOS independent audit','independent re-proof','Peer completed whole proof/source/author-code review20:08:30UTC. Its independent exact checker passed1.410285s:5760GL2F9 matrices,240 scalar-square semilinear cocycles,19440 descent-vector identities and full729/6561/59049 row-weight sets, plus symbolic shears and Heisenberg identities and exact rational ceiling. Root read full report; no claim of a fresh root execution or whole peer-code reading.', 'agents/imprimitive/audit_higher_odd_symplectic/independent_check.py; agents/imprimitive/audit_higher_odd_symplectic/independent_checked.json'),
 ('D-HOS cited scopes','used and rechecked in this run','Root freshly reopened Liebeck2017 original full theorem context pp2--4 and inspected renderedp4 confirming1/(sqrt(q)-1). Li--Xia2022 section2.2.2 Table2.1p14 retains prior full root reading and fresh independent reading; HHM2015 complete multiplier tablep35 freshly reread. Gluck original proof is not newly reconstructed.', 'https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf; agents/imprimitive/audit_higher_odd_symplectic/PEER_AUDIT.md'),
 ('D-UNW-01--03 and D-LNW-01','targeted proof check','Root read entire unitary proof and complete156-line linear companion, whole bibliography and source record, both full author constant programs, entire independent report and independent constant code. PASS two-regime degree estimate, exact low-level errors, same-degree extension, q2 endpoint, full-normalizer commutator, tensor permutations, actual source budget, cover and degree-separation reductions. Three omitted display closings in initial UNW were repaired before final independent freeze; no mathematical change and no compilation claimed.', '; '.join(frozen.keys())+'; agents/g34_eightfolds/bireflection/NONWEIL_CUTOFFS_PEER_AUDIT.md'),
 ('LT2024 and GLT2020 explicit source estimates','used and rechecked in this run','Root freshly read LT accepted-author full Theorems4.4/5.5 with proofs onpp19--20,25--26, visually inspectedp26 constant, and verified Annals publication record. Root freshly read published GLT Definition2/Lemma7.1pp51--52, full used Theorem7.3(i)--(ii) scope/proofp52, full sections8.1pp55--61 and8.3pp65--67, and complete Cor8.6pp67--68. Exact8.11/8.18, evenq and degree denominators verified. Text requests lost to output truncation were reread in bounded calls before this event. Author-version/journal pagination and failed typeset LT retrieval remain explicit.', 'agents/imprimitive/unitary_nonweil/SOURCES.md; '+bib),
 ('D-UNW/D-LNW independent constants','independent re-proof','G34 peer complete proof/source/code audit20:13:34UTC PASS. Independently reconstructed published exponent, universal polynomial margins and both exact error ratios, normalizer11/60 and ceiling30; actual runtime0.124358891s. Root read entire independent program. No rank-range enumeration or new proof of published classification inputs is claimed.', 'agents/g34_eightfolds/bireflection/audit_nonweil_cutoffs.py; agents/g34_eightfolds/bireflection/audit_nonweil_cutoffs.json')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])

with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Higher odd symplectic exclusion and explicit linear/unitary rank cutoffs\n\n'+now+' — Q2bk and Q2bl refuted; Q2i strictly reduced. D-HOS-03--06 removes all higher symplectic oddq>=7 with arbitrary mixed factors and full compatible normalizers. D-UNW/D-LNW bounds remaining transitive linear/unitary natural dimension by10^61; combined with the earlier nonsplit field cutoff their group range is finite but unenumerated. Every proof and invoked source scope has complete root and independent peer review, with separate exact certificates. This integration is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('''\n## Higher-rank finite-cover supplier reductions\n\nD-HOS-03--06 removes every higher odd symplectic core overq>=7, with arbitrary mixed ranks/fields and all compatible normalizers. Its geometric finite-field proof leaves onlyq3/q5 in that family. D-UNW/D-LNW makes the transitive primitive linear/unitary core ranges finite under the already proved nonsplit field cutoff: natural dimension is below10^61 andq<=27. This enormous finite range has not been enumerated.\n\nThese are genuine restrictions on the actual finite-cover weight-one supplier gate for condition A, cote16 scan050. Exact representation support is compared with the established polarized intermediate Hurwitz factorization; parameter counts are used only as necessary constraints, never as a proof of dominance. The scheme-spreading and etale weight interpretations retain the precise EGA/SGA placements in the common framework section. No new detecting cycle, condition-I positivity proof, motivic L-function estimate or improved detector constant follows merely from these exclusions. Markman, Severn and032 remain conditional as previously recorded.\n''')
p=R/'research/frameworks.tex';s=p.read_text()
old='D-HOS, D-OC2, D-OC2-F, D-EXS,'
assert old in s;p.write_text(s.replace(old,'D-HOS-01--06, D-UNW, D-LNW, D-OC2, D-OC2-F, D-EXS,'))
out={'date_utc':now,'integrated':['D-HOS-03--06','D-UNW-01--03','D-LNW-01'],
     'whole_reviewed_sha256':frozen,'canonical_sha256':{n:sha(n) for n in frozen},
     'bib_sha256':{bib:sha(bib)},'new_rows':{'Q2bk':'refuted','Q2bl':'refuted'},
     'strictly_reduced_main_gates':['Q2i']}
(R/'research/hos_nonweil_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
