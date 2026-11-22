# C.3 canonical-template construction: source audit and derivation

Run: RESEARCH_SA17_FINISH-20261119. Agent: dieudonne.
Model: GPT-6 Astra (OpenAI, ChatGPT Pro mode).
Written 2026-11-19; exact event times are in checks_C_templates.tsv.
This is a source adaptation and an elementary derivation, with no priority claim.

## Deliverable and scope

Full proofs: sections/C_finish_canonical_templates.tex.
Reference: references/C_templates.bib.
Five numbered statements:

- C:canonical-polynomial-elimination: finite elimination of polynomial
  existential conditions over an algebraically closed field, in all characteristics.
- C:canonical-tuples: the checked specialization of known Belitskii--Sergeichuk
  canonical reduction to simultaneous matrix tuples and finite template generation.
- C:Om-canonical-templates: explicit finite templates for indecomposable rational
  O_m representations at each dimension and minimal coefficient degree.
- C:Om-canonical-WG: an explicit indexed basis of the split orthogonal ring and
  finite algorithms for multiplication and all exterior operations.
- C:Om-canonical-example: the O_3 standard, exterior-square, and symmetric-square
  example in characteristics3 and5, with a complete centralizer proof.

The draft is separate from C.tex and is not to be included before root review.
The parent owns combined tables, the paper driver, report, and ledger.

The field is algebraically closed of characteristic p>2. The algorithm uses
exact field arithmetic, equality tests, univariate factorization/root access, and
comparison in a fixed total order on the field. This is an algebraic access model,
not a uniform Turing assertion about arbitrary fields or orders. The polynomial
computations are constructive; no orbit quotient remains. Eigenvalue-order
conditions are additional set-theoretic conditions, so the full ordered domains
are not called Zariski-constructible sets. Their polynomial parts are constructible.
Empty domains may be retained; no decision algorithm for nonemptiness in an
arbitrary ordered field structure is asserted.

Finiteness is per(n,d), not per n over all coefficient degrees. No efficiency bound
is asserted. This does not classify nonclosed fields or general nonfield bases.
Root is pursuing finite fields separately.

## Primary canonical source, actually read

Vladimir V. Sergeichuk, Canonical matrices for linear matrix problems,
Linear Algebra Appl.317(2000),53--102, DOI10.1016/S0024-3795(00)00150-6;
author version arXiv:0709.2485v1.

- Primary PDF opened: https://arxiv.org/pdf/0709.2485 .
- Primary abstract/DOI metadata independently reopened:
  https://arxiv.org/abs/0709.2485 .
- Local full primary TeX read:
  ../external_sources/Sergeichuk0709.2485_source/paper.tex .
- Algebraically closed hypothesis: author version printedp1, source line83.
- Chosen total eigenvalue order: Section1.3, printedp7.
- Algorithm: Section1.4, printedpp10--13; source lines1178--1350.
- Canonical uniqueness: Theorem1.3, printedp13; source label t1.1.
- Canonical direct sums: Theorem2.2, printedpp23--24; source label t3.1.
- Parameter domains and determinantal construction: Theorem2.3,
  printedpp27--28; source label t2.2, lines2528--2645.
- Finite box patterns: Remark2.1, printedp28; source lines2664ff.

The parent independently reopened these sections. The source supplies a finite
construction of polynomial parameter conditions, not merely an abstract choice
of orbit representatives.

Our explicit specialization encodes(T1,...,Tr) as the first block row of an
rn-square matrix and uses the reduced algebra diag(S,...,S). This is exactly
simultaneous similarity. The remaining rows stay zero under the action.
Finite generation enumerates bounded box patterns and rank/Weyr shapes, then
replays the actual algorithm using minor tests and fixed pivots.

Terminal stable scalar cells must also be included as parameter slots. This
addresses n=1, when every tuple is already stable. A free scalar slot remains a
slot at value0 or1. Distinct free boxes have distinct slots even if the specialized
values agree. Deterministic records, ordered slots, disjoint first-pivot branches,
and omission of zero-width subdivisions remove duplicate descriptions. Repeated
descriptions of the same record are merged by finite unions of their domains.

### Unused literal criterion in the source

Theorem1.4(b), printedp16, is not used. Read literally, it would make any
changeable current box a marked zero, whereas the algorithm distinguishes an
admissible additive change from row/column equivalence or similarity.
For example take Lambda=diag(k,k) and M=[[0,0],[1,0]]. Its first box M21 is
the canonical rank-one block under independent scalar row/column changes.
Conjugating by diag(a,1), with a nonzero scalar other than1, changes that box,
while there are no preceding boxes to preserve. The printed condition(b) would
demand a marked zero. The actual three-case algorithm does not: there is no
admissible additive term, so it uses its rank-reduction case. Our proof cites
Section1.4 and Theorems1.3,2.2,2.3,Remark2.1 directly, never that criterion.

## Polynomial elimination: complete elementary proof

Searches before writing included:

- "Ierardi" "88-948" pdf quantifier
- quantifier elimination algebraically closed fields positive characteristic algorithm
- Cohen Mahboubi "A Formal Quantifier Elimination" pdf
- comprehensive Groebner bases Weispfenning quantifier elimination

The official Cornell metadata for Ierardi TR88-948 was opened and confirms
an algebraic algorithm for arbitrary algebraically closed fields; the full PDF
fetch failed after a CDN redirect. The official REDUCE CGB manual was opened,
Sections20.12.1,20.12.5,20.12.7:
https://reduce-algebra.sourceforge.io/manual/manualse138.html .
Publisher/author metadata for Cohen--Mahboubi2010 were opened; attempts to open
the HAL and CiteSeer full versions were blocked. None of these unopened papers
is invoked as the proof of the draft's elimination lemma.

Instead the paper proves the complete elementary algorithm. For
exists z: P_i(y,z)=0 and Q(y,z)!=0, branch Euclidean gcd computations on
leading coefficients. If every P_i is identically zero, require Q nonzero
as a polynomial. Otherwise, with G the gcd and D a bound for deg(P_i),
require degG>0 and G not dividing Q^D. Algebraic closedness makes this
equivalent to a root of G which is not a root of Q, including inseparable
cases. Divide and clear denominators already known nonzero. Iteration
eliminates every matrix variable. This standard idea is rederived completely;
no novelty is claimed.

For the optional comprehensive-Groebner implementation, express f!=0 as
w f-1=0 on each Boolean branch. A specialized system has a solution exactly
when its ideal is proper; specialization-correct Groebner branches decide
whether1 belongs to it. The elementary proof suffices independently.

## Adaptation: every step written in the paper

1. Degree-compatible standard monomials in H=k[x_ij]/(X^t J X-J) of degree<=d
   span nested finite coalgebras C_d. Delta has degree<=d in each tensor factor,
   antipode is linear on generators, and C_d C_e is contained in C_(d+e).
   The determinant relation already gives invertibility of X.
2. Dual multiplication constants gamma and counit coefficients e give exactly
   T_a T_b=sum gamma_c^{ab}T_c and sum e_c T_c=I.
3. Filter canonical tuple templates by these relations, minimal degree, and
   absence of a nonzero nonidentity idempotent in the centralizer. The last
   condition is the complement of an explicit existential polynomial formula.
4. Antipode gives Tdual_a=sum s_ac T_c^t. Duality preserves minimal degree.
   Forms satisfy B T_a=Tdual_a B and B^t=+/-B. Finite pivot strata give bases
   for these solution spaces; nonvanishing of the determinant polynomial
   is a finite coefficient test.
5. The QSS specialization already proved as C:algebraically_closed_WG gives
   the exclusive types and injectivity of forgetting forms. The canonical
   module and its type leave no additional isometry quotient.
6. Basis weights are1 for symmetric indecomposables,2 for alternating ones,
   and1 on both members of a non-self-dual pair. Orient pairs by the fixed
   lexicographic order on canonical indices.
7. Compute tensor entries as products and exterior entries as minors in H;
   reduce in C_(d+e) or C_(rd), canonically decompose, minimize summand degrees,
   and apply the weights. These are exact ring coefficients. Exterior minors
   require no division by r! and no special lambda identity is assumed.

## O3 example and executable certificate

Root supplied code/C_finish_coalgebra_canonical.py and
logs/C_finish_coalgebra_canonical.json. The code uses the coordinate Hopf algebra,
not just O3(F_p), and checks p=3 and p=5 separately.

Per prime: Groebner basis27; dim C_d for d0..3 equals1,10,44,119;400 coproduct
terms in C2;44 coassociativity,88 counit,88 antipode,18 orthogonality,
7744 module products,4 module units,176 invariant-form coefficient equations,
and10 Hodge/determinant equations. Endomorphism dimensions are1,2,1 for
V,Sym2V,exterior2V. Root's execution took2.568092418994638 seconds; the separate
dieudonne rerun records its actual time in logs/B_finish_C_coalgebra_recheck.json.

The paper also gives a complete argument: sign changes and permutations constrain
End(Sym2V), and a plane rotation yields End(Sym2V)=kI+kK, with
K(A)=tr(A)I and K^2=3K. This is dual numbers at p3, hence absolute
indecomposability, and k x k at p5, giving summand dimensions1 and5.
The trace form and Hodge identity give the product and exterior identities.
The code is a bounded certificate, not a full canonical-template implementation.
