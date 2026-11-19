"""Update the live item ledger without discarding the first checkpoint record."""
from pathlib import Path
import json,csv,datetime
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.3':('OPEN: positivity and eventual parenthesis proved','thm:all-X-explicit-positive-rank','Explicit eventual positivity for every X; projective-space generic rank exact. Exact generic rank and relative ordinarity for arbitrary X remain.'),
'A.4':('OPEN: characteristic-two plane case completely determined','thm:plane-char2-all-groups','All d in characteristic two: full GL in even degree, full canonical-covector stabilizer in odd degree. Geometric and arithmetic groups equal. Odd-characteristic and general-ambient determination remains.'),
'B.2':('OPEN: sharp tame and wild p=3 ranges written','thm:B-RD7; thm:B-RD8; thm:B-RD10','All-dimensional ordinary exclusion and sharp tame table audited. Defect twelve at p=3 verified; complete wild first-level table undergoing final small-case audit.'),
'B.3':('OPEN: all tame elliptic levels determined','thm:B-RD12; cor:B-RD13','Exact tame higher-level existence criterion and least good-forcing level proved. Wild p=3 and general abelian dimension remain.'),
'C.2':('OPEN: all normal bases proved','C_normal.tex','Normal locally noetherian bases, including nonexcellent, settled. General reduced finite geometrically unibranch cover case remains.'),
'C.4':('OPEN: normal bases proved','C_local_systems.tex','Normal locally noetherian local systems are effective. Reduced nonnormal and nonreduced cases remain. Negative-one nodal twisting is effective.'),
'E.7':('PROVED; proposed ramification prediction REFUTED','prop:DE-LT','Tangent exponent alpha(A)=0 for all A; full lattices need not agree. Exact counterexample pi^(p+1)=p; dictionary and comparison independently audited.'),
'E.8':('PROVED','thm:DE-hasse','Exact Hasse-invariant transport over arbitrary, possibly nonreduced characteristic-p bases.'),
'E.9':('PROVED; literal product-sign lead REFUTED','thm:DE-ordinary-sign','Positive Poincare biduality gives alpha_dual=alpha^-1. Hodge-first comparison beta=(-1)^(g(g+1)/2) alpha^-1 modulo p. Literature search recorded.'),
'E.10':('OPEN: literal integral test (a) REFUTED','prop:DE-old-site','A1 integral p-torsion mismatch proved. G_m rational counterexample under active source/comparison audit; proper test remains.'),
'Lead E7':('REFUTED; corrected answer PROVED','prop:DE-LT','Different does not force nonzero tangent exponent; full integral comparison can nevertheless fail.'),
'Lead E9':('REFUTED as literal product rule; corrected formula PROVED','thm:DE-ordinary-sign','Koszul factor (-1)^(gh) corrects the proposed multiplicativity.'),
'Lead E10':('OPEN: integral test REFUTED','prop:DE-old-site','Rational old-site comparison and proper comparison still active.'),
'Lead E11':('PROVED under the stated actual-lift hypothesis','cor:DE-BT-constant','Convergent F-isocrystals are constant; Galois intersection of Dieudonne lattices and full faithfulness also give constant p-divisible groups up to isogeny.'),
}
for r in rows:
 if r['item'] in changes:r['status'],r['where'],r['gate']=changes[r['item']]
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r[k] for k in ['item','status','where','gate'])+' |' for r in rows)+'\n'
p=w/'RESEARCH_SA15_report.md';s=p.read_text();i=s.index('# RESEARCH_SA15 research report');s='INCOMPLETE\n\n'+table+'\n'+s[i:]
s=s.replace('9. E.7 and E.10 newly written proofs remain audit-pending at this checkpoint.','9. E.7 is now independently audited: alpha=0 does not imply equality of the full lattices. E.10(a) is refuted integrally on the literal site; comparisons for a different modern site have not been substituted.\n10. The B.2 list omits defect twelve in residue characteristic three. An explicit full-rational-3-torsion example over Q3(i,zeta3) proves the correction.\n11. The E.9 product formula needs the Koszul factor (-1)^(gh); its genus-two case refutes the literal multiplicativity claim.')
s+='\n## Checkpoint 02 additions\n\nThe characteristic-two plane monodromy proof now covers every degree, with full contact-incidence, conductor, degeneration, primitive-divisor, and group-theoretic proofs. The independent low-degree proofs are retained as auditable base cases. New reduction computations and source ledgers are in `agents/reduction_descent/code/` and `SOURCE_RECORD.tsv`. Both first-level and all-level tame criteria have undergone independent root audit. The current item table takes precedence over the historical first-checkpoint descriptions above.\n'
p.write_text(s)
ledger=w/'PROGRESS_LEDGER.md';s=ledger.read_text();s+='\n## 2026-11-19 04:18 UTC: checkpoint 02 gates\n\n'+table+'\n### Movement since checkpoint 01\n\nA.4 in characteristic two is reduced from degrees at least six to no remaining plane-degree cases. A.3 eventual generic Hodge parenthesis follows from the explicit positivity bound. B.3 tame elliptic higher torsion is determined exactly. E.7, E.8, E.9 and the full literal Lead E11 changed from pending to proved/refuted as stated. C.2 and C.4 are reduced to nonnormal bases. The three-hour progress review remains due at 05:50:40 UTC. This checkpoint is not that review.\n';ledger.write_text(s)
events=w/'notes/root_check_events.tsv'
with events.open('a') as f:
 for sid,description in [
 ('A4-CHAR2-ALL','Independent reciprocal audits: root checked conductor/contact transitivity; monodromy agent checked root uniform Hering induction, primitive-divisor and H1 arguments. All plane degrees in characteristic two settled.'),
 ('B-RD7','Root read Carter-Strauch Theorem2.1.2 and Proposition2.2.3 and audited tame full-p torsion construction and necessity.'),
 ('B-RD8','Root checked exact defect12 example, all valuation computations and minimality via discriminant plus 2-division cubic.'),
 ('B-RD12','Root independently audited adapted-basis valuations, primitive-coordinate product, weighted Cohen specialization, integer criterion and least-level formula.'),
 ('E7','Root independently audited covariant/contravariant convention, inverse-different line, c=h/g comparison, tangent units and full-lattice counterexample.'),
 ('E8-E9','Root independently audited universal deformation Jacobi identity and Hodge/Poincare/Cech signs, including p-divisible degree and arbitrary base.'),
 ('E10a','Root independently verified H1(old site,A1,O)[p]=0 and nonzero integral MW class x^(p-1)dx of order p.'),
 ('E11-LEAD','Root audited finite Galois intersection of stable Dieudonne lattices and isogeny consequence of de Jong full faithfulness.')]:
  f.write(sid+'\t2026-11-19T04:15:00Z\tGPT-6 Astra (OpenAI); /root; inherited effort\tindependent re-proof\t'+description+'\n')
print('Updated checkpoint 02 item table, ledger and root check events.')
