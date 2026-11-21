# A12–A14: Lang quotient criterion, ordinary 4159 example, fixed-prime barrier

Date: 2026-11-21. Checker/author: GPT-6 Astra Pro; effort not exposed;
agent /root/effective_galois.

## Deliverables and status

- lang_weil_criterion.tex: complete main-ready statements and proofs of A12,
  A13 and A14.
- lang_weil_4159_certificate.py: standard-library exact arithmetic certificate.
- lang_weil_4159_certificate.json: PASS output from the actual execution.
- Parent independently produced work/root/verify_ordinary_4159_independent.py
  and work/root/ordinary_4159_independent_check.json.

The author's complete mathematical recheck passes. This is a mathematical
argument plus exact finite arithmetic, not formal proof-assistant verification.
Independent parent whole-proof review was requested immediately after the first
complete source was written. The parent subsequently reported PASS for the
entire A12–A14 source, explicitly checking connectedness, rational-fibre
orientation, floor/ceiling bound, recurrence and multiplicative order, matrix
valuation growth and the monotone cutoff. This is recorded separately in the
check-event fragment.

## A12 complete proof checks

The Raynaud sheaf B is a degree-one line bundle on the relative Frobenius twist
in characteristic two. Its theta support is the actual translate
R -> O(R) tensor B^{-1}; a rational basepoint makes the translation rational
without requiring B to have a rational effective representative.

The isogeny factor has the correct direction:
J -> J/H -> J, with composite Frobenius minus identity and second degree
[J(F_Q):H]. Its kernel is the constant quotient of rational points.
The pullback of this isogeny by the theta translate is geometrically connected,
including when its degree has a characteristic-primary part. The written proof
derives this from the Jacobian's Albanese property: a disconnected pullback gives
a nontrivial intermediate isogeny with a section over the curve, hence a split
isogeny of abelian varieties of equal dimension, which must have degree one.
Milne Proposition 9.1 supplies an independently checked exact published locator
for the same full abelian étale fundamental-group assertion.

For x in J(F_Q) and (F-1)y=x, Frobenius displacement of pi_H(y) is pi_H(x).
Thus each rational curve point over H contributes exactly a rational fibre of
size a, and every other fibre contributes zero rational points. Unramified
Riemann–Hurwitz gives genus a+1, so the ordinary Weil bound and integer rounding
give the exact lower bound. At most one counted point is the origin. For an
ordinary curve, H^0(B)=0 excludes it entirely. If the point in H=G[ell^r] has a
smaller exact order ell^s, the unit-group generation condition descends to s.
The subsequent cover/point-separation result explicitly invokes A11.

## A13 arithmetic and geometry

The three distinct simple Artin–Schreier poles give genus two and rank two.
Both finite-field counts are exactly three; the producer enumerates the polynomial
model over F2 and F4. Newton identities and the functional equation yield
T^4-T^2+4. The beta-root recurrence gives
[2,1,-7,-11,17,61,-7,-251] and Jacobian order 16636 over F128.
The prime 4159 has exact order of 2 equal to 2079, and adjoining -1 gives the
full unit group. The group index is four and the exact integer Weil bound is four
theta points. They are all nonzero because the curve is ordinary.

The parent reports and has saved an independent check using an 11-by-11
Sylvester determinant to obtain 16636, independently of the recurrence.
The present agent read that script and its PASS output; it was not imported by
the producer certificate. The producer additionally checks the multiplicative
order by a direct doubling loop independently of the prime-factor criterion.

## A14 complete proof checks

The matrix binomial expansion is valid integrally after dividing its coefficients
by t because j-1-v_ell(j)>=1 for odd ell and j>=2. Thus its residual matrix is
identity modulo ell and has unit determinant. This proves the exact four-dimensional
valuation growth formula without a semisimplicity assumption.
Using F_{q^m} inside F_{q^{dm}} gives a uniform C_ell*m^4 upper bound for the
entire rational ell-primary subgroup, hence for every exponent r.

The Weil lower bound gives a cofactor at least (q^{m/2}-1)^4/(C_ell*m^4).
Rearranging the A12 sufficient inequality gives the incompatible requirement
a < (q^{m/2}-1)^2/(2q^{m/2}+1).
The integer cutoff q^{3m}>=4*C_ell^2*m^8 is sufficient for failure, and its
left/right ratio is increasing for all integral m>=4. The first such m>=4
therefore gives an effective cutoff for failure of this numerical criterion.
It does not prove geometric nonexistence of theta points for fixed ell.

## Primary sources checked in this run

1. Bjorn Poonen, *Multiples of subvarieties in algebraic groups over finite
   fields*, IMRN 2005, no.24, 1487–1498.
   https://math.mit.edu/~poonen/papers/multiples.pdf
   Exact input: Lemma 5.1, author PDF p.6, including its complete Lang-quotient
   proof; also the preliminary connectedness statement and Lemma 4.3.
   Web references: turn562014750view0, turn621969926view0.
   This source already contains the qualitative coset-intersection argument.
   A12 is its explicit genus-two specialization and pure-primary application.

2. J. S. Milne, *Jacobian Varieties*, author version 12 June 2021.
   https://www.jmilne.org/math/xnotes/JVs.pdf
   Proposition 9.1, author p.30: connected étale covers of the Jacobian pull back
   connected; full geometric abelianized fundamental groups agree.
   The characteristic-primary completion is on pp.31–32, through the
   Artin–Schreier/Witt-vector discussion and Lemmas 9.4–9.5.
   Exact statement and the surrounding argument read. The source's cited
   underlying external cohomological results were not re-proved here.
   Web references: turn678081862view0, turn678081862view1.

3. Pierre Deligne, *La conjecture de Weil. I*, Publ. Math. IHES 43 (1974),
   273–307. https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf
   Formula (1.5.1), p.275 and Theorem 1.6, p.276: trace formula and purity for
   smooth projective varieties. Exact statements and Frobenius conventions read;
   no claim to have re-proved the entire Weil theorem.
   Web references: turn562014750view1, turn153898672view1.

4. Rachel Pries and Hui June Zhu, *The p-rank stratification of Artin–Schreier
   curves*, Ann. Inst. Fourier 62 (2012), 707–726.
   https://www.numdam.org/item/10.5802/aif.2692.pdf
   Lemma 2.6, p.712, exact genus and p-rank formulas and its immediate proof read.
   Web references: turn562014750view2, turn153898672view2.

The recovered ANABELIAN_SUCCESSOR A.10–A.11 are credited as existing related
finite-field counting inputs; no novelty claim is made for the general method.
The full recovered A.10 statement and proof were read again for comparison.
Its rational prime-cover criterion N>=2|K| and ell>N requires 2 to be primitive,
whereas A12 supplies a pure-primary theta point and permits generation by
2 together with -1. The new text does not assert numerical optimality.

## Analytic scope

No number-field GRH, Artin holomorphy, Masullo premise or Hooley theorem is used.
A density result for primes with prescribed order of 2 does not itself establish
large pure prime-power factors in det(1-F^m), or theta incidence. This is the
specific missing implication in using analytic prime supply alone for this route.
The proof does not claim that no other geometric or arithmetic route can work.
