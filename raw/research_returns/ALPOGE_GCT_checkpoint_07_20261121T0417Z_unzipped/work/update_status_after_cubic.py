from pathlib import Path
import csv
from datetime import datetime
from zoneinfo import ZoneInfo
base=Path(__file__).resolve().parent.parent
now=datetime.now(ZoneInfo('Europe/Berlin')).isoformat(timespec='seconds')
p=base/'deliverable/IMPLICATIONS.md'
s=p.read_text()
a=s.index('**Research status:**'); b=s.index('\n\n## 1.',a)
s=s[:a]+'''**Research status:** the stronger canonical clause of ordinary plethysm PH3 is refuted by P-F19. Its weaker numerical positive-form clause, narrow PH2/SH and the asymptotic determinant/permanent obstruction remain open. P-F14–P-F15 also refute the broader rank-only subgroup-restriction index hypotheses. The supplied Alpöge and OpenAI results are used as cited theorems with their stated scopes. No P versus NP or ordinary complex-field VP versus VNP resolution is claimed. “Finding” denotes a deduction proved here, not a certified claim of historical priority.

All GCT VI hypothesis numbers below refer to the supplied arXiv:0704.0229v4 text. Its broad subgroup-restriction problem, irreducible-inner problem and ordinary GL_n plethysm subfamily are kept distinct.

## 0. A refutation inside ordinary cubic plethysm

**P-F19 refutes the canonical modular-index clause of GCT VI Hypothesis 1.6.7.** Put g=gcd(n,3), d0=n/g and W=Sym³ C^n. The family has fixed inner shape (3), outer partition (d0), and target partition ((3/g)^n. Its canonical algebra is the entire SL_n invariant ring of cubic forms, with its coefficient grading divided by d0. This identification preserves the actual multiplication.

The explicit point is the chain cubic

`F_n = x1² x2 + x2² x3 + ... + x_(n-1)² xn + xn³`.

Its gradient has no common nonzero zero, so its discriminant is nonzero. If an invariant of stretch degree s is nonzero at this point, its coefficient monomials must balance the diagonal-torus weights. The resulting recurrence forces `2^(n-1)` to divide s. A separate diagonal-stabilizer calculation gives the same divisibility. Every homogeneous system of parameters must contain an invariant nonzero at this point: otherwise its finite-dimensional quotient would force a power of the nonzero discriminant to vanish there. Consequently

`canonical modular index >= 2^(n-1)`.

The parameter in the printed hypothesis is `h = binomial(n+2,3)^2 + n + 1 = O(n^6)`. The lower bound is therefore superpolynomial in h, despite the inner shape remaining (3). It applies to every parameter system, so it applies in particular to the lexicographically minimal one used in the source's definition.

This settles a substantial part of the main positivity question negatively. A purity argument cannot establish this false canonical degree bound. The chain forms themselves occur in earlier literature, including Busé–Jouanolou Example 4.12, which cites Demazure; no priority claim is made for the forms or this consequence.

**The scope matters:** the first clause of PH3 asks only for some positive rational expression for the Hilbert series. Such an expression need not come from parameters of the canonical algebra. P-F19 alone does not refute that weaker clause, and does not prove a large positivity or saturation index. The work continues at those gates.
''' + s[b:]
s=s.replace('This is real movement of the main gate: on this route, it remains to prove PH3 and construct the required data, rather than separately prove PH3 ⇒ PH2.','The implication only needs a positive rational form with small numerical denominator weights; it does not require those weights to be degrees of canonical parameters. After P-F19, this weaker clause and uniform construction are the surviving route to PH2.')
insert='''
### Reconstruction and qualitative uniformity

**P-F13** turns a denominator promise into a finite reconstruction problem. If r<=R and all denominator weights are <=A, the common denominator D(T)=product_(a=1)^A(1-T^a)^R has degree M=R A(A+1)/2. The first M multiplicities determine the whole rational series. A proposed positive numerator and bounded denominator can then be checked by an exact polynomial identity. This does not provide a fast multiplicity oracle, a fast search through all denominators, or a proof of the denominator promise from a short prefix alone.

**P-F16–P-F17** give a finite bound for each fixed semisimple embedding. A finitely generated positive multigraded branching algebra contains the actual canonical ray algebras. A bound from its generator-degree matrix and minors gives bounded ray generators; a common multiple of their degrees supplies parameters in one degree. Rational singularities give Cohen–Macaulayness, and the positive Hilbert form gives bounded positivity and saturation indices. A prime-avoidance argument additionally bounds the source's lexicographically minimal parameter degrees. The graded GL-to-SL reduction preserves the canonical algebra on centrally balanced rays.

**P-F18** removes the remaining qualitative dependence on n and determinant twists when the inner dimension m is fixed. A nontrivial irreducible S^mu C^n of dimension m has n<=m and every consecutive highest-weight difference <=m-1. Only finitely many normalized SL_n representations remain. Thus one finite function of m bounds the indices and canonical parameter degrees for all ordinary plethysm rays of inner dimension m. P-F19 proves that the optimal canonical bound has an exponential subsequence; qualitative finiteness does not supply the polynomial growth conjectured in PH3.

### The broader rank-only hypotheses

**P-F14** uses the faithful torus embedding t↦diag(t^(N+1),t), with fixed λ=(1), π=2. Its stretch series is 1/(1-T^N), forcing a denominator weight at least N in every rational form of the indicated kind. Its source rank parameter stays 5. This refutes the broad rank-only PH3 of Hypothesis 3.3.4.

**P-F15** uses t↦diag(t,t³,t^(N+1)) for odd N. The actual multiplicity algebra is a polynomial ring on generators of degrees 2 and N, with series 1/((1-T²)(1-T^N)) and exact positivity and saturation indices N-2. The source rank parameter stays 6. Hence Hypotheses 3.3.2(a) and 3.3.3 fail in that broad formulation. The coefficients are nevertheless easy to compute, and this does not refute the density clause 3.3.2(b). These are reducible torus representations, so they must not be substituted for the ordinary irreducible-inner examples in P-F19. Including only the bit length of N in a repaired parameter still leaves exponentially large numerical indices.
'''
marker='\n## 2. What is actually refuted about purity and positivity'
if '### Reconstruction and qualitative uniformity' not in s:s=s.replace(marker,'\n'+insert+marker)
needle='Thus a normal cone with pure even Tate ordinary and intersection cohomology can have this PH1-violating graded Hilbert function.'
s=s.replace(needle,'''**PLE-F8** identifies that ring with the actual canonical highest-weight multiplicity algebra of the obstructing plethysm ray. Explicit cubic covariants supply the generators; an irreducible quadratic relation and a graded-dimension comparison prove the isomorphism. The basis U^i V^j Z^epsilon has nonnegative integral multiplication constants because Z²=UV²+4U⁴. The monic equation gives a flat model over Z, with the claimed finite-field geometry. It is not identified with the naive Lie-derivation kernel in every characteristic.

Thus the actual plethysm multiplicity algebra has normality, a positive multiplicative basis, and a pure even Tate model, while its graded Hilbert function violates homogeneous PH1.''')
a=s.index('## Next main step')
s=s[:a]+'''## Next main step

Prove or refute the weaker numerical positive-form clause for a specified irreducible-inner GCT family, or attack PH2 and saturation directly. Canonical parameter degrees cannot supply the requested polynomial bound in general, by P-F19. P-F11–P-F12 still turn any suitable numerical denominator bound into the revised positivity conclusion; P-F13 makes candidate verification finite under a bound. To reach an obstruction, this must be joined to control of actual coordinate-ring quotient ranks and a strict asymptotic comparison. Those tasks remain open in this run.
'''
p.write_text(s)
p=base/'work/root_questions.tsv'
rows=list(csv.DictReader(p.open(),delimiter='\t'));fields=list(rows[0])
for r in rows:
 if r['id']=='Q-COMMON-PERIOD':r['current_gate']='Complemented by P-F11; the period-based bound remains sharp on the weighted-plane examples.'
 if r['id']=='Q-MODULAR-INDEX':r['current_gate']='The implication needs only the weaker numerical positive-form bound. P-F19 refutes the stronger canonical parameter bound; efficient construction remains separate.'
 if r['id']=='Q-PH3':
  r.update(question='Does the canonical modular-index clause of revised PH3 hold for ordinary irreducible-inner plethysm?',state='refuted',finding_ids_or_counterexample='P-F19; fixed inner shape(3), canonical chi>=2^(n-1), h=O(n6)',current_gate='The weaker numerical positive-form clause is a separate question, Q-PH3-WEAK.')
 if r['id']=='Q-SH-REVISED':
  r['question']='Do the narrower irreducible-inner polynomial saturation indices and almost-everywhere zero-index condition hold?'
  r['current_gate']='A bounded numerical positive form would imply part(a); P-F19 does not refute it or the density assertion in part(b). Broad rank-only part(a) is separately refuted by P-F15.'
 if r['id']=='Q-ALPOGE-METHOD':r['finding_ids_or_counterexample']='P-F6; PLE-F7; PLE-F8; P-F19'
if not any(r['id']=='Q-PH3-WEAK' for r in rows):rows.append(dict(zip(fields,['Q-PH3-WEAK','GCTVI Hyp1.6.7 first clause, distinct from canonical clause','Does some positive rational expression for each irreducible-inner plethysm stretch have polynomially bounded numerical denominator weights?','current gate','P-F11-P-F13; P-F18; P-F19','Canonical parameter-degree lower bounds do not automatically give ordinary Hilbert poles or exclude other positive expressions. Investigate numerical poles, modules and direct positivity bounds.'])))
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=base/'work/root_later_checks.tsv'; rows=list(csv.DictReader(p.open(),delimiter='\t'));fields=list(rows[0])
if not any(r['statement_id']=='P-F19' for r in rows):rows.append(dict(zip(fields,['P-F19',now,'/root','targeted proof check','PASS','Read the entire two-proof cubic argument; independently checked smoothness including endpoints, dual-coordinate convention, full regraded invariant ring and Cartan multiplication, torus recurrence, stabilizer determinant order, parameter-ideal nilpotence, and exponential versus h=O(n6). Opened the primary discriminant source and its exact statement. Scope restricted to canonical clause.','GPT-6 Astra Pro','inherited/not exposed by runtime','/root'])))
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=base/'deliverable/README.md';s=p.read_text();a=s.index('This is research in progress.');b=s.index('\n\n',a)
s=s[:a]+'''This is research in progress. P-F19 refutes the stronger canonical modular-index clause of ordinary plethysm PH3, already for the fixed inner shape (3). The weaker numerical positive-form clause, narrow PH2/SH and an asymptotic determinant/permanent obstruction remain open. P-F11–P-F12 prove the positive-form implication to PH2; P-F14–P-F15 refute the broader rank-only subgroup-restriction index hypotheses. The paper makes no P versus NP or ordinary complex-field VP versus VNP claim. A checkpoint is a snapshot of the work at its stated time, not a declaration that every requested research target is complete.'''+s[b:];p.write_text(s)
print({'updated':5,'timestamp':now})
