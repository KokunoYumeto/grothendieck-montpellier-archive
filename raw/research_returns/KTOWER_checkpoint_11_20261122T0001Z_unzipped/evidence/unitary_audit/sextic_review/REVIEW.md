# Independent cyclic-sextic comparison audit

Reviewer: `/root/unitary_audit`, GPT-6 Astra Pro. Model effort setting is not
exposed. Review performed on 2026-11-21 UTC. No Lean kernel execution is claimed.

## Completed order-six theorem: whole-proof review

The entire `evidence/lean_chain/order_six_reduction.tex`, SHA-256
`36da7f893a98bdf2db26fc39a9c90ff78baa241f062bf291c46deb3e2def9b64`,
was read after it was completed. KT-ORDER-SIX-COMPONENT-REDUCTION passes the
independent whole-written-proof review, not merely an ingredient check.
The order-six character and even exponent force the real prime-conductor
sextic field; the carried small-prime result covers p < 2^31. The exact
normalizations and inequality OS6.2-8 agree with the primary audits below.
The imported quadratic and cubic class-number bounds, combined with the
positive integral ratio smaller than p, exclude p from h(F). The identity
jN(x)=sum(gx) and p not dividing [Q(mu_p):F] then kill the relevant invariant
cyclotomic class group and its order-six component. The last K-group step
uses the explicitly carried K17-(K2) comparison. No upper bound on e in
terms of p is assumed. The small-prime verification, quadratic/cubic class
bounds, and K17-(K2) are accepted prior inputs, not freshly reproved here.

## Whole proof reviewed

`evidence/main_gate/sextic_class_product.tex`, SHA-256
`cd00cb2698d3add71ca7ecb729e2e2812e09d48ae5da54d488114f7e7aea99fc`.

Both KT-SEXTIC-CLASS-PRODUCT and KT-SEXTIC-REGULATOR-RATIO-FOUR pass the
independent whole-written-proof review. The first theorem is restricted to
real cyclic sextic fields of prime conductor, as stated. The ordinary Hilbert
class fields split all real places. Their intersections with the sextic field
are trivial over the respective subfields because the conductor prime is
totally ramified. On the common compositum quotient, the two Galois actions
factor through groups of coprime orders two and three, and therefore vanish.
A central extension of a cyclic group is abelian. The inertia subgroup at the
conductor prime has order exactly six. The resulting everywhere finite
unramified quotient of Q is trivial by Minkowski. This proves the required
linear disjointness and the divisibility of ordinary class numbers.

The regulator and analytic class-number factors in the corollary were
checked independently. In particular, there is no unit-signature hypothesis
or additional factor four in the relative regulator. The corollary's C6 is
defined by the displayed analytic expression; no identification with a
circular-unit index is needed or inferred.

## Primary-source read scopes

1. M.-N. Gras, *Familles d'unites dans les extensions cycliques reelles de
   degre 6 de Q* (1986), primary PDF
   <https://www.numdam.org/article/PMB_1986___2_A2_0.pdf>, SHA-256
   `59ea4f150c5a3dc2c132182a44bcca1656e5ba83487d379c5f42087924b3995b`.
   Read the complete Section 2 unit-module setup and the full Lemma (2.6)
   and Theorem (2.5) proofs, printed pp. 3-6. All four pages were also
   visually read from their rendered PDF images, including every displayed
   formula. The earlier general theorem cited as [G] is imported, not
   independently reconstructed. The stated bound applies to general real
   cyclic sextic fields; the simplest-field family begins later in Section 3.
   The source states f >= 28. Its E_chi is norms +/-1, and
   E_chi = {+/-1} times E_* with E_* having both exact relative norms one.

2. S. Louboutin, *Explicit upper bounds for |L(1,chi)| for primitive even
   Dirichlet characters*, Acta Arith. 101.1 (2002), primary PDF
   <https://www.impan.pl/shop/publication/transaction/download/product/82711>,
   SHA-256
   `9eb61fd6cc97d0034851a273dd11bfb6c0ee74a9aba453b117bb4511a02b1a4f`.
   Theorem 1(1), equation (3), printed p. 2 was textually and visually
   checked. The entire Section 3 proof, printed pp. 5-8, was read from the
   extracted text, including Lemma 7 and the r=0 completion on p. 7.
   The bound is exact, not asymptotic, and applies to complex as well as
   real primitive even characters. Later Theorems 4 and 5 are not needed.

3. S. Louboutin, *Class numbers of real cyclotomic fields*, Publ. Math.
   Debrecen 64 (2004), primary PDF
   <https://publi.math.unideb.hu/paper/1169/download/10_5486_PMD_2004_2976.pdf>,
   SHA-256
   `87211ce37d1ceed964535d4565019e5bb55dece21120dfdad08eec0609c517fa`.
   Read and visually checked the complete Section 3.1 relative-unit setup,
   Lemma 3 and its complete proof, printed pp. 454-455. The subsequent
   paragraph explicitly states the product class-number divisibility and
   cites Cornell-Washington. No claim to have read that cited paper is made:
   the direct prime-conductor proof above supplies the needed assertion.
   Later analytic lower bounds and simplest-sextic examples are not imported.

## Independent normalization and inequality

For a relative unit with logarithms x,y,y-x,-x,-y,x-y, put
R = x^2+y^2-xy and t = max(|x|,|y|,|x-y|). The three completions of squares
show R >= 3t^2/4. Applying Gras's Lemma (2.6) to a generating relative unit
gives exp(2t) >= (p-20)/4. Consequently

    R_* >= (3/16) log^2((p-20)/4).

This also independently recovers the needed consequence of Gras's Theorem
(2.5). It does not replace the published lemma's arithmetic input.

Louboutin gives |L(1,chi_6)| <= (log p+kappa_0)/2, with
kappa_0=2+gamma-log(4pi)<1. The determinant/unit-index identity and the
analytic class-number formula yield

    H := h(F)/(h(F2)h(F3))
      = Q p |L(1,chi_6)|^2/(48R_*)
      <= (p/3) ((log p+kappa_0)/log((p-20)/4))^2,

where Q divides 12. For p >= 2^31, write t=log p. Strict convexity of 1/x
on [1,2] gives log 2>2/3, so t>20. Also p>100 gives
(p-20)/4>p/5, and log 5<2. Therefore

    H < (p/3) ((t+1)/(t-2))^2 < 49p/108 < p.

The function (t+1)/(t-2) decreases for t>2. The proof of kappa_0<1 uses
only gamma<1 and log(4pi)>2. No floating-point approximation is needed.
The class-number ratio is a positive integer by the reviewed direct lemma.
To deduce p does not divide h(F), one must additionally use the appropriate
quadratic and cubic class-number exclusions; those are not reproved here.

## Finite exact checks

`independent_checks.py` verifies the complete symbolic five-by-five
regulator determinant, three quadratic-form square identities, the
nonnegative polynomial identity used in Gras's estimate, the analytic
factor 48, the combined constant 1/3, and the final rational bound 49/108.
Its complete fresh result is in `independent_checks.json`. This is a finite
algebra check, not a proof-assistant verification or a numerical computation
of class numbers.
