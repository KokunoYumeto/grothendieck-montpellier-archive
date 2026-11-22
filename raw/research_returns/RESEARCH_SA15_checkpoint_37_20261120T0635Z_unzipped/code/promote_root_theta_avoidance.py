"""Promote the fully audited auxiliary theta-torsion proof after CP30."""
from pathlib import Path
import csv,datetime,difflib,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
source=w/'notes/root_theta_torsion_avoidance_candidate.tex'
target=w/'sections/A_theta_torsion_avoidance.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='a9bec7ff6b14a3420bca6cd043efe4085088c338d2845ed09d25555d49498480'
assert sha(source)==expected and not target.exists()
audits=[w/'agents/monodromy/outputs/independent_theta_torsion_avoidance_audit.json',w/'agents/obstructions_crystals/root_theta_torsion_avoidance_independent_audit.json']
for p in audits:
 r=json.loads(p.read_text());assert 'PASS' in r['status'];assert r.get('source_sha256',r.get('candidate_sha256'))==expected
folder=w/'notes/root_theta_avoidance_promotion';assert not folder.exists();folder.mkdir()
shutil.copy2(source,folder/'candidate.tex')
original=source.read_text()
canonical=original.replace('Candidate; complete direct proof supplied.','Proved; two complete independent written-proof audits passed.')
canonical=canonical.replace('Candidate scope; no new monodromy theorem.','Proved scope statement; no new monodromy theorem.')
old='''original proof of Theorem C for genus two in
\\emph{Torsion points on theta divisors and
semihomogeneous vector bundles}, arXiv:2007.12252v3,
printed pp.~9--10.'''
new='''original genus-two proof of Theorem C
\\cite[Theorem C, printed pp.~9--10]{Pareschi2021ThetaTorsion}.'''
assert old in canonical;canonical=canonical.replace(old,new)
assert '\\status{Candidate' not in canonical
target.write_text(canonical)
(folder/'canonical.diff').write_text(''.join(difflib.unified_diff(original.splitlines(True),canonical.splitlines(True),fromfile='audited candidate',tofile='canonical')))
bib=w/'notes/root_references.bib';before=bib.read_text();(folder/'root_references_before.bib').write_text(before)
assert 'Pareschi2021ThetaTorsion,' not in before
bib.write_text(before+r'''
@misc{Pareschi2021ThetaTorsion,
 author={Pareschi, Giuseppe},
 title={Torsion points on theta divisors and semihomogeneous vector bundles},
 year={2021}, eprint={2007.12252}, archivePrefix={arXiv},
 url={https://arxiv.org/pdf/2007.12252},
 note={Opened the complete original arXiv v3, 22 October 2021, 11 pages. Read the introduction and Theorems A, B, C; complete Proposition 2.1 proof; the complete Theorem A proof; Theorem 4.1 and its stated reduction to the cited external theorem; the complete Theorem B proof; all of Section 5 including the genus-two proof of Theorem C on printed pp.9--10; and the references. The source works over the complex numbers. Its external Mukai, Oprea and Pareschi--Popa dependencies were not all newly opened. The present auxiliary theta-torsion proof is a separate direct normalization and local-delta argument over its explicitly stated field, not an imported characteristic-two extension of those semihomogeneous-bundle theorems. No final journal metadata or priority claim is asserted for this inspected preprint version.}
}
''')
con=w/'code/consolidate.py';oldcon=con.read_text();(folder/'consolidate_before.py').write_text(oldcon)
needle="   out.write('\\n\\\\input{sections/A_route_limitations_29}\\n')"
assert oldcon.count(needle)==1
newcon=oldcon.replace(needle,needle+"\n   out.write('\\n\\\\input{sections/A_theta_torsion_avoidance}\\n')")
con.write_text(newcon)
(folder/'consolidate.diff').write_text(''.join(difflib.unified_diff(oldcon.splitlines(True),newcon.splitlines(True),fromfile='before',tofile='after')))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:root-theta-torsion-delta-bound','prop:root-theta-avoiding-Lagrangian','rem:root-theta-avoidance-scope']
record={'status':'PROMOTED_AFTER_TWO_FULL_INDEPENDENT_AUDITS','actual_utc':now,'candidate_sha256':expected,'canonical':str(target.relative_to(w)),'canonical_sha256':sha(target),'labels':labels,'audit_records':[str(p.relative_to(w)) for p in audits],'changes_from_audited_candidate':'Status wording and formal bibliography citation only; mathematical proof unchanged.','scope':'Auxiliary bound and avoiding subgroup only; no nodality, fixed-target quotient, Cartier coefficient or monodromy theorem is inferred.','main_gate_movement':False,'mathematical_programs_executed':[]}
(w/'outputs/root_theta_avoidance_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in labels:writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','promotion after two complete independent written-proof audits','PASS: exact audited candidate hash and both proof records verified; only status and citation formatting changed. No mathematical computation or main-gate advance claimed. See outputs/root_theta_avoidance_promotion.json.'])
print(json.dumps(record,indent=2))
