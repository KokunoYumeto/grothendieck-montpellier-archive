# Narrow integral pullback caution in Asvin 2023

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Primary: Asvin G., On the variation of Frobenius eigenvalues in a skew-abelian Iwasawa tower, Algebra & Number Theory17(12)(2023),2151–2179, https://msp.org/ant/2023/17-12/ant-v17-n12-p03-p.pdf .

## Exact additional reading

After the narrow passage review in ASVIN2023_NARROW_SCOPE_REVIEW.md, I read the complete printed Lemma11 and Lemma12 statements/proofs, pp2157–2158, and checked the paper's Notation1 definition of a curve. I individually displayed the source page2157. The definition does not exclude genus one. This record supplements the previous scope review; it does not retroactively turn that earlier review into a check of all geometric inputs.

## Explicit countercheck

Let ell be an odd prime different from the field characteristic and let E be any elliptic curve over a finite field. A finite constant extension can make E[ell] rational and satisfy the paper's q=1 mod ell assumption. The étale map

    f=[ell]: E→E

is a finite geometrically connected curve map of degree ell^2. Its natural pullback on H1_et(E_bar,Z_ell) is multiplication by ell. This follows from the natural Tate-module duality and the identity T_ell([ell])=[ell]; H1_et(E_bar,Z_ell) is free of rank two. Hence the natural image has quotient (Z/ell)^2 and is not a direct summand.

The printed proof of Lemma11 infers surjectivity on Tate modules from surjectivity of a map of abelian varieties. This precise inference fails for [ell]: the abelian-variety map is surjective but the Tate-module map is multiplication by ell. The free rank-two module maps injectively with a nontrivial finite cokernel. Thus Lemma11's natural integral direct-factor conclusion, in the sense used for the subsequent quotient M_n, is false as stated. An abstract free summand of the same rank is a different assertion and does not repair the natural quotient.

This same example tests Lemma12. Its geometric deck transformations are translations by E[ell], which act trivially on H1_et(E_bar,Z_ell). Thus the invariant submodule is the entire upstairs H1, whereas the natural pullback image is ell times that module. The integral equality in Lemma12 fails. In the Hochschild–Serre sequence, H1(G,Z_ell)=0 does not remove the following H2(G,Z_ell) obstruction. Rational coefficients remove this finite-index issue, but that does not establish the asserted integral lattice statement.

For the CaseB tower with C=A=E and the identity map to A, the level map is [ell^n]. Consequently its literal integral quotient H1(E_bar,Z_ell)/[ell^n]^*H1(E_bar,Z_ell) is (Z/ell^n)^2, not a free Z_ell module. This specifically prevents silently treating the printed preliminary argument as a checked integral geometric model. It does not by itself determine how the geometric statements could be repaired by changing lattices or passing to rational cohomology.

## Scope retained

The abstract power-series results in §3 are logically separate and were not refuted by this example. Their inspected statements remain tower-prime ell congruences involving a full Frobenius-orbit product. No claim is made here that the entire paper, its abstract congruence proofs, or every possible rational-cohomology formulation is false. Our main negative conclusion—that the inspected results do not supply a characteristic-p primitive exponent bound—does not depend on Lemmas11–12. The source page remains local review material and is not copied into the deliverables.

Root and /root/gt_certificates independently read the printed arguments and confirmed this narrow countercheck. Their separate events are their own records; the present event records this agent's actual reading and calculation. No numerical computation or new geometric witness construction was performed.
