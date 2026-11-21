# Independent review: explicit two-unit auxiliary-field family

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

**PASS.** I read the entire `main_gate/explicit_two_unit_family.tex`, then reread its final revised class-number and primitive-character paragraphs. In the saved primary Benmerieme–Movahhedi arXiv:2007.04864v1 text I read Corollary 2.2 with its immediately preceding derivation on printed pages 4–5, the complete proof of Proposition 3.2 and equation (3.2) with its explanatory paragraph on pages 11–12, Theorem 4.1 and its surrounding paragraph on page 14, and the complete proof of Proposition 4.4 on page 15, including the first paragraph supplying the minus-field input. The source's cited Coates and p-adic L-function results remain imported inputs; they have not been re-proved here. No numerical experiment or Lean kernel build is part of this check.

## Exact result and remaining condition

For every prime ell at least seven congruent to three modulo four, take the square-free parts m_s of ell plus or minus two, and D_s=-4m_s. Both fields give units of B_(1,chi_D) and B_(1,chi_D*omega^e) for every e=(ell-3)/2+(ell-1)t with t nonnegative. One field is split and the other inert at ell. This is a uniform two-of-three-unit statement with this local choice; it does not prescribe other local data.

The third condition remains exactly the unit condition for B_(ell-2,chi_D)/(ell-2). It is neither proved by p-rationality of the real reflected field in this argument nor inferred from the first two units. No K-group or all-weight automorphic exclusion is claimed.

## Arithmetic checks

* Both ell+2 and ell-2 are positive odd integers congruent to one modulo four. Removing an odd square leaves m_s congruent to one modulo four. Thus -m_s is square-free and congruent to three modulo four, giving the fundamental discriminant -4m_s. The m_s=1 case is correctly the field of discriminant -4. The discriminants are prime to ell.
* Reducing m_s*u_s^2=ell+2s modulo ell and using (-1/ell)=-1 gives the two opposite Legendre-symbol signs exactly as stated. No assumed square-free value of ell plus or minus two is needed.
* The final proof uses the explicitly located primary Theorem 4.1. Since chi_D(2)=0 for D=-4m_s, its denominator is four, giving h(D)=(w/4) times the character sum from one through 2m_s. Every even term is zero, and at most m_s odd terms contribute values at most one. For m_s>1 one has w=2, so h(D)<=m_s/2<ell; m_s<=ell+2 and ell>2 suffice. This covers both signs and every small case.
* For m_s=1 the same formula gives h(-4)=1. The imaginary quadratic Bernoulli/class-number formula then gives the first unit, including the w=4 exceptional field. The older reduced-form bound was also mathematically valid, but it is not the argument retained in the final version.

## Imported real-field statement and transport

Proposition 3.2 proves ell-rationality of Q(sqrt(ell(ell+2))) for every ell greater than three. The first paragraph of the full Proposition 4.4 proof explicitly supplies the analogous Q(sqrt(ell(ell-2))) assertion; the rest of that proposition proves the biquadratic result. Thus using its minus quadratic subfield is within the primary source's stated and proved scope.

Corollary 2.2 identifies real quadratic ell-rationality with the unit of the p-adic L-value at one. For d=-m_s, the hypotheses of equation (3.2) hold: d is square-free and negative, prime to ell, and is not -ell. Its real field is exactly Q(sqrt(ell*m_s)), the same field as the appropriate ell(ell+2s) expression. The congruence therefore gives the unit of B_(n0,chi_D)/n0 with n0=(ell-1)/2.

The final proof explicitly states the character convention requested independently by the parent and this reviewer. The identity chi_F*omega^n0=chi_D is an identity of primitive Galois characters. If Dirichlet functions are multiplied at the larger, imprimitive modulus, the resulting L-value differs by the removed ell Euler factor. That factor is 1 modulo ell because n0 is at least three, so either convention gives the same displayed unit congruence. I reread the final correction; it is correct.

The already checked finite-character reduction applies with n0 odd and 3<=n0<=ell-2. It transports the unit to every displayed weight, including weights divisible by ell and weights larger than ell. Applying the same reduction to 2e+1, whose residue is ell-2 modulo ell-1, proves only the equivalence of the remaining third-unit tests.

Finally 2e is congruent to -2 modulo ell-1, so the required nondivisibility holds. Writing ell=4a+3 gives gcd(ell-1,e)=2; the order of omega^e is (ell-1)/2, an odd integer at least three, and squaring does not change it. These are nonquadratic twists as asserted.

The checked primary version is recorded in the accompanying manifest. This review does not claim that every hypothesis of an arbitrary auxiliary-field automorphy theorem has thereby been supplied: the statement itself correctly limits the local conditions and leaves the third unit open.
