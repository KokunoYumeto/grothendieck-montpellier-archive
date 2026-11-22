"""Record actual completed readings and update the next checkpoint narrative."""
import csv,json,re
from pathlib import Path

root=Path(__file__).resolve().parent.parent
review_path=root/'work/review_status.json'
reviews=json.loads(review_path.read_text())
new=[
 ('NN-C034','2026-11-22 00:27:08 UTC','Read the entire total-support permanent addendum. Checked the exact partial-matching partition, heavy-row bound h<=Cr/log^2r, original order r, light-minor scope, number of branches, formal degree at most2r, integral base change and actual torus-module direct sum.','work/complexity/c034_total_sparse_permanent_addendum.tex'),
 ('NN-C036','2026-11-22 00:24:15 UTC','Read the complete first-violation ordinary-ideal certificate and affine-coordinate addendum. Checked restricted prefixes with all unused variables retained, original n and arbitrary m, identity over Z without Boolean axioms, actual and formal degrees, both coordinate composites and their degrees. Freshly read Grochow--Pitassi Lemma4.2 full proof, equations4--6, pp1:26--1:28.','work/complexity/c036_ideal_certificate_addendum.tex; https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf; root retrieval turn398959546view0')
]
events_path=root/'work/root/CHECK_EVENTS.tsv'
with events_path.open() as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;events=list(reader)
for fid,date,scope,evidence in new:
 event={'statement_id':fid,'date_utc':date,'who':'/root','model':'GPT-6 Astra Pro','effort':'not exposed by runtime','type':'targeted proof check','outcome':'PASS; complete addendum proof read','scope_and_method':scope,'limitations':'Targeted complete deduction reading, not independent re-proof or formal verification. Classical results are imported with exact locators.','evidence':evidence}
 if not any(e['statement_id']==fid and e['date_utc']==date for e in events):events.append(event)
 if scope not in reviews[fid]['scope_and_method']:
  reviews[fid]['scope_and_method']+=' Addendum full proof checked at'+date+': '+scope
  reviews[fid]['evidence']+='; '+evidence
review_path.write_text(json.dumps(reviews,indent=2,ensure_ascii=False)+'\n')
with events_path.open('w') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(events)

p=root/'deliverables/README.md';s=p.read_text()
s=re.sub(r'The first formal movement review was completed.*?See work/reviews/review_01.json for every main row and the open track rows\.', 'The second formal movement review was completed at 2026-11-22 00:04:54 UTC. Ordinary ideal certificates and dimension-ring optimization had strictly smaller proved gates. The consecutive no-movement count is zero. The next review is due at2026-11-22 01:04:37 UTC; the next checkpoint after06 is due at2026-11-22 01:19:37 UTC. See work/reviews/review_02.json and its frozen formal baseline in work/gate_history/formal_review_02.json. Interim progress does not reset that baseline.',s)
s=re.sub(r'This snapshot contains123 findings.*?No P versus NP or VP versus VNP resolution is claimed\.', 'This snapshot contains128 findings, all with completed deduction-proof readings. The exact symmetric closed-table dimension-ring optimum is2744 cancelling pairs, with a unique parameter realization; the larger class allowing additional zero-trace table positions remains open. New integral formal counting circuits handle arbitrary fixed-width CNFs in the original variable parameter; the characteristic-two exponent is stronger. Sparse permanent circuits need only a total quasilinear support bound. Under A, at least one sixth of all positive-height zero occurrences of each fixed primitive Dirichlet L-function are simple and transverse; the left/right proportions remain open. General PIT, polynomial NP isolation, canonical GCT multiplicities and extreme gaps remain separately scoped gates. No P versus NP or VP versus VNP resolution is claimed.',s)
s=re.sub(r'The paper successfully compiles.*?Earlier build failures are retained in the work log\.', 'The complete TeX source and proof fragments are included. The current PDF page count and layout checks are recorded in work/pdf_qa/cp06_bounds_check.json after the checkpoint build. Every page receives a text-edge check and selected new pages are visually inspected. This is sampled layout QA, not a claim of visual inspection of every page. Source-locator verification and mathematical proof readings remain separate from compilation and layout checks. Earlier build failures are retained in the work log.',s)
p.write_text(s)

p=root/'deliverables/IMPLICATIONS.md';s=p.read_text()
s=s.replace('## Latest proved interfaces before checkpoint05','## Latest proved interfaces before checkpoint06')
old='In the rank-three closed table, the current interval is[1932,2744] (NN-G033–036). Every strict improvement must satisfy one of20 first-cell mass triples and38 base mass rows, with348 auxiliary increments. Those are necessary conditions, with arbitrary grading supports still allowed. The general symmetric problem permitting additional zero-trace positions is a larger class; its degree cutoff below2^9953 and fixed-parameter feasibility theorem remain separate from the closed-table lower bound.'
newtext='The rank-three symmetric closed-table optimization is solved (NN-G033–036):2744 cancelling pairs is the exact minimum, with a unique parameter realization. The proof excludes every remaining mass projection using integral-polynomial and coefficient arguments, with arbitrary grading supports and degrees allowed. This closes the closed-table gate. The general symmetric problem permitting additional zero-trace positions is a larger class; its degree cutoff below2^9953 and fixed-parameter feasibility theorem remain separate, and its numerical minimum is open.'
s=s.replace(old,newtext)
insert='''
NN-C035 removes the density restriction for characteristic-two formal assignment polynomials: every fixed-width CNF on its original n variables and arbitrary m clauses has a circuit of size polynomial(n+m) times2^{O_k(n(loglog n)^2/sqrt(log n))}. NN-C036 proves an integral construction for all coefficient rings with the weaker exponent O_k(n(loglog n)^{1+1/k}/(log n)^{1/(2k)}). Both preserve formal assignment weights. The integral construction also gives ordinary first-violation Nullstellensatz certificates over Z, without adjoining Boolean axioms, and explicit affine-space coordinates for the associated unsatisfiable hypersurfaces. The construction has polynomial formal degree; a polynomial-space claim is not made for these extensions.

The NN-C034 permanent application now assumes only O(r log^a r) allowed matrix entries in total, with no row or column degree restriction. Expanding along at most O(r/log^2 r) heavy rows leaves minors with polylogarithmic row scopes, at an absorbed subexponential cost. This is an identity over Z of formal degree at most2r, and therefore survives every commutative base change. The character module itself decomposes positively over partial matchings, while the circuits computing the minor characters use virtual differences.

NN-A035 proves strict left second-order bending for initially vertical multiple-zero branches in its stated zeta and Dirichlet settings. NN-A037 strengthens the transverse-zero gate: under A, for each fixed primitive Dirichlet L-function, the lower proportion of simple transverse zeros is at least1/6 of all positive-ordinate zero occurrences and1/4 of the simple occurrences. At a fixed normal margin eta<1/2 the corresponding lower bounds are (1-4eta^2)/(6(1-eta^2)) and (1-4eta^2)/(4(1-eta^2)). A new mixed Hardy-phase/Euler-phase mean is combined with the precise Rudnick--Sarnak simplicity input. The squared normal component discards the derivative sign, so the signed half-density gate remains open. General Dedekind products do not automatically inherit the primitive-function simplicity theorem.

'''
s=s.replace('## Boolean algorithms and algebraic complexity',insert+'## Boolean algorithms and algebraic complexity',1)
p.write_text(s)

p=root/'deliverables/LEDGER.md';s=p.read_text()
s=s.replace('The next formal movement review is due at2026-11-22 00:04:37 UTC. The first formal movement review is recorded below; it found movement and reset the no-movement count to zero.','The second formal movement review was completed at2026-11-22 00:04:54 UTC and found movement. The next formal movement review is due at2026-11-22 01:04:37 UTC; the consecutive no-movement count remains zero. The frozen comparison baseline is work/gate_history/formal_review_02.json.')
s+='\n## Reviewed extensions at 2026-11-22 00:27:26 UTC\n\nNN-C036 now includes the fully read ordinary integral first-violation certificate and explicit affine-coordinate maps for arbitrary-density fixed-width CNFs. NN-C034 now requires only a total quasilinear support bound for its permanent application. Full root readings were completed at00:24:15 and00:27:08 UTC respectively. These are extensions of existing findings; the catalogue has128 findings. The closed-table minimum2744 and the primitive Dirichlet transverse lower proportions are already integrated. The next formal comparison remains against review02 at01:04:37 UTC; this packaging update is not a formal movement review.\n'
p.write_text(s)
print(json.dumps({'reviews':len(reviews),'root_events':len(events),'updated':'checkpoint06 narrative and two full-proof addendum events'}))
