"""Integrate the whole-reviewed Sp3 closure and common-square local obstruction."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
paths={'HOS20-22':'agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_semisimple_section.tex','E837':'agents/sixfolds/rm_square_artin_matrix_obstruction_section.tex'}
frozen={'HOS20-22':'700d6e80b8e7d7183dfd698627b36b116bf0b8a7235b9e8fccc2c17ff294bf6b','E837':'de73e564fba81ab92c9196067bf27ac50e8be2ef3e4960c5f6b291cce1c75373'}
for k,p in paths.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==frozen[k]
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
def replace_range(s,start,end,new):
 a=s.index(start);b=s.index(end,a);return s[:a]+new+s[b:]
p=R/paths['HOS20-22'];s=p.read_text();s=change(s,'This is a separate complete new derivation, submitted for independent\nwhole-proof review.','This separate complete new derivation has passed whole-proof reviews\nby /root and /root/imprimitive, with separate exact supplements.');p.write_text(s)
p=R/paths['E837'];s=p.read_text();before=s;s=change(s,r'''\textbf{Status:} new complete proof submitted for independent
whole-proof review. It uses the opposite-order companion equations
proved in E836 sections 2--3, whose separate independent review is in
progress.''',r'''\textbf{Status:} complete new proof checked in full by the author,
/root and /root/g34\_eightfolds. The root also read the complete
canonical conversion, with all seventeen display blocks unchanged.
It uses the opposite-order companion equations proved in E836
sections 2--3, whose separate whole-proof reviews have passed.''');assert re.findall(r'\\\[(.*?)\\\]',s,re.S)==re.findall(r'\\\[(.*?)\\\]',before,re.S);p.write_text(s)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert not {'Q2by','Q5ak'}&{r['id'] for r in rows}
(R/'research/gates_before_symplectic_closure_square_artin.json').write_text(json.dumps({r['id']:r for r in rows if r['id'] in ('Q2i','Q5i')},indent=2)+'\n')
hos=('D-HOS-20--22 now closes ALL remaining ordinary higherSp(q3), n>=4, in the transitive main sixfold-source scope. Each odd-prime>=5 semisimple element has support>=4a/15: nonzero symmetric-form orbits have fixed fraction<=1/9, stable isotropic primary pairs use LST restriction, and multiplicity-one selfreciprocal primaries have full torus centralizer<=(10)^(n/2). Together with HOS13/18 every noncentral inner element has support>=2a/9 for evenn and>=19a/104 for oddn. Nonselfdual compatible normalizers are scalar-inner; arbitrary mixed ranks/central quotients/tensor permutations satisfy sourceceilings9 or156/5 against floors27/81. HOS12 treats selfdual transitive factors. The earlier residual rank4..283 and odd-prime inertia gates are superseded by exclusion, not retained as open. Smalln<4 stays in its earlier separately stated results; no new arbitraryq5/nonselfdual mixed-family theorem asserted. ')
square=('SF-E837 excludes every nontrivial common formal square-thickening defect A=R/(u1²,u2²,u3²,u4²), for arbitrary nonlinear mixed regular parameters and all multiplicities. The two actual companion equations give a pencil; four distinct pair monomial annihilators force any square matrix invertible by the all-size filtered dimension/omitted-edge lemma. Constant Pluecker identities exclude support<=3; invertibility forces proportional complementary bivectors, contradiction. This strictly adds HD-CI-B1 beyond E836 commuting triples, without invalidating that scalar-inference counterexample. Actual rank32 coherent balanced examples have Extdimension96m² but no weakly semiregular action in E819 scope. Arbitrary Artin modules and other CIs remain outside. ')
for r in rows:
 if r['id']=='Q2i':
  t=r['finding_ids_or_current_gate'];t=replace_range(t,'D-HOS-13--15 proves','D-UNW-01--03',hos);t=replace_range(t,'D-HOS-17--19 further restricts','D-OL-09','');r['finding_ids_or_current_gate']=t
 if r['id']=='Q5i':r['finding_ids_or_current_gate']+=' '+square
rows.extend([dict(zip(fields,['Q2by','Prompt target2; complete higher characteristic-three symplectic prime classes','Can any residual ordinary higherSp3 transitive main sixfold source have period rank nine?','refuted',hos+'Whole author/root/imprimitive proof/source/code reviews PASS; exact supplements separate from universal proof.'])),dict(zip(fields,['Q5ak','Prompt target5; actual companion matrices over square Artin quotients','Can an arbitrarily oriented formal square-thickening point modification evade the local balanced semiregularity obstruction?','refuted',square+'Whole author/root/G34 proofs PASS and independent graph/nonlinear polynomial supplements PASS.']))])
with q.open('w',newline='') as f:w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,extra in [('agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_involution_section.tex',paths['HOS20-22']),('research/ci_integrable_cross_minor_boundary.tex',paths['E837'])]:
 a=r'\input{'+anchor+'}';s=change(s,a,a+'\n'+r'\input{'+extra+'}')
s=replace_range(s,'Nonselfdual\nhigher $q=3$ factors are further restricted','D-UNW-01--03 and D-LNW-01',r'''D-HOS-20--22 now excludes every remaining nonselfdual higher $q=3$
source. For every odd prime at least five, symmetric-form weight
orbits have fixed fraction at most $1/9$. Stable isotropic primary
pairs and the published restriction bound give support $4a/15$;
when no such pair exists the full centralizer is a norm-one torus
of order at most $10^{n/2}$, and column orthogonality is stronger.
Combining all projective-prime cases gives support $2a/9$ for even
half-rank and $19a/104$ for odd half-rank. Scalar-inner compatible
normalizers, tensor convolution and factor cycles preserve these
bounds. Twelve genuine inertias force degree at most $9$ or $156/5$,
contradicting respectively $27$ or $81$. Together with D-HOS-12,
this closes all ordinary transitive higher $q=3$ cores, $n\ge4$;
the prior rank and inertia restrictions are now superseded.
Small ranks retain their separately stated earlier results. No new
arbitrary mixture of $q=5$ with nonselfdual higher-field cases is
asserted here.
''')
anchor='It does not solve the stronger matrix equations or produce a supplier.'
s=change(s,anchor,anchor+r'''
SF-E837 now uses those stronger equations to exclude every common
formal square thickening, with arbitrary nonlinear mixed parameters.
A square matrix whose cokernel is killed by four distinct pair
monomials must be invertible, by its filtered degree-two image and
the two omitted-edge constraints. The bracket-support alternatives
then force proportional complementary bivectors, a contradiction.
This includes the HD-CI-B1 ideal without altering its counterexample
to the scalar inference. It does not extend to arbitrary Artin modules.''')
p.write_text(s)
events=[('D-HOS-20--22 peer audit','targeted proof check','Root entire imprimitive report SHA83a3fbdbd5c245bf36d2ec35abb628d8c7bddafca9e73fbe40175fbfb927d8a9 read. Whole frozen proof/source/author-code PASS; independent0.219303451s supplement21:56:06UTC:59049 Gauss-sum forms, two729unitriangular families, different order11 primaries,6561prime41centralizer operators/82isometries. Initial SymPy factor-sorting API failure retained; FLINT extraction repair, no mathematics failure. Root has not whole-read peer code.','agents/imprimitive/audit_symplectic_three_semisimple/PEER_AUDIT.md'),('SF-E837 peer audit','targeted proof check','Root entire G34 report SHAd625e2ae09fb9b146ca972bce8dc9b78b40095e3e7eab73d034948b071cf9a8e read. Whole frozen196-line draft/author-code/JSON PASS; full E836 companion interface reread. Separate0.137928210s graph-linear-algebra/generic four-parameter nonlinear certificate21:55:17UTC. Output truncation retained, full saved JSON later inspected by peer; no math failure. Root has not whole-read peer code.','agents/g34_eightfolds/bireflection/SQUARE_ARTIN_MATRIX_PEER_AUDIT.md'),('D-HOS-20--22 and SF-E837 integration','targeted proof check','Root earlier whole mathematical, author checker, complete JSON and primary-source scopes recorded before checkpoint15; complete peer reports now read. Status-only proof edits, existing bib inputs reused, E837 seventeen displays unchanged. Sp3 main gate closed in exact scope; square-Artin main gate strictly reduced. No TeX compilation or new numerical rerun claimed.','scripts/integrate_symplectic_closure_square_artin.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,t,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',t,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Higher Sp3 closure and arbitrary square-thickening restriction\n\n'+now+' — Q2by and Q5ak refuted; Q2i and Q5i strictly reduced. '+hos+square+'After review09/checkpoint15; no formal review or off-schedule checkpoint.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Eliminating a full remaining group family and a new actual local family\n\n'+hos+square+'These are restrictions on actual condition-A suppliers (cote16 scan050; SIGN_NEXT SN-C03/C04), preserving the geometric period-rank/induction and coherent-action interfaces. Neither yields a new detector. The local result is an Artin-scheme/perfect-resolution and K-theoretic obstruction; the group result is a finite-local-system/weight-one variation restriction. Condition I scan049/cote44 Th4, Cayley-Hamilton division scans048-049 and the common SGA/EGA/FGA/realization/motive/L-function framework remain as stated. Markman, Severn and032 are not new premises.\n')
out={'date_utc':now,'integrated':list(paths),'frozen_reviewed_sha256':frozen,'canonical_sha256':{k:hashlib.sha256((R/v).read_bytes()).hexdigest() for k,v in paths.items()},'new_rows':{'Q2by':'refuted','Q5ak':'refuted'},'strictly_reduced_main_gates':['Q2i','Q5i']}
(R/'research/symplectic_closure_square_artin_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
