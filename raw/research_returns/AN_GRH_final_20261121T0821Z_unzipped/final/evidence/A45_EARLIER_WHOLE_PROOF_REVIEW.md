# A45 and the primitive-conductor descent lemma

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

## A45 — separate-reader whole-proof check

Source: `work/effective_galois/nonconstant_deck/A45_NONCONSTANT_DECK.tex`.

SHA256: `249a89734a7da96a8c4d4e207c69c0f84483a026f2b98ca55f38f5c9b8ea45a8`.

**PASS.** Read the entire statement, exact scope and all five proof steps. This is a targeted whole-proof review, not an independent re-proof or a formal verification.

The pointed-cover implication applies to this cover because its geometric monodromy is odd; neither a constant arithmetic deck group nor splitting of the entire base-point fibre is needed. The chosen rational point fixes the relevant pointed neighbourhood. A hypothetical equal point section supplies a rational lift of the other point and a two-primary Jacobian difference, as in the already checked covering formulation.

The integer inverse of n is used only on a finite rational two-primary group. The projected class is consequently k-rational. I checked the norm identity, the proof that `im(sigma-1)=B`, and the exact congruences in ND.5; these place the projected class in the connected norm kernel, not just in the whole norm kernel. The geometric deck difference has order dividing the original-field exponent M even though the difference itself need not be rational.

The exact order m gives the displayed four-point principal divisor. Its four supports are distinct, and exactness excludes a square; when m=1 the simple poles exclude a square directly. Thus the resulting degree-2m function is separable in characteristic two. The controlled-subfield application uses degree-d conjugate functions, and Poonen's integer is correctly identified as d/e. The inequality forces e>1, with e a power of two.

The induced cyclic action on the intermediate curve is faithful because its kernel order divides both n and e. A fixed-point stabilizer of odd prime order would divide the fibre degree e, since its orbits on the original curve are free and retain their multiplicities. Hence the action is free. The genus bound and Riemann–Hurwitz then force an elliptic intermediate curve and total different 2n.

For e>2, a zero fibre is supported on at most the two positive divisor points; their equal multiplicities force all ramification indices to be powers of two at least two. Each local different exponent is at least the corresponding index. The n disjoint translated fibres exceed the total different. At e=2, distinct images of the two positive points give two disjoint full deck orbits of ramified points and again exceed the total different. A shared positive fibre is unramified; equivariance and the pole divisor then force a shared negative fibre and a fixed point of sigma² on the intermediate curve. This is the required contradiction. These geometric steps do not use rationality of sigma.

Primary source reopened: Poonen, *Gonality of modular curves in characteristic p*, Proposition2.1 statement, Lemma2.2 and its complete displayed proof, Corollary2.3 and its complete displayed proof, author pp3–4, https://math.mit.edu/~poonen/papers/gonality.pdf . The proof of Castelnuovo–Severi in the external book cited by Poonen was not separately retrieved. The exact tame/wild Riemann–Hurwitz and local different framework was checked earlier in this run; the local derivative inequality here was checked directly.

## Semilinear descent — author whole check and final narrow addition

Source: `work/row_audit/NONCONSTANT_PRIMITIVE_DESCENT.tex`.

First complete source SHA256: `64e60ad7f333d51b28f92e9c347409ebbbddae66dea21d1a38b13c88d6686de9`.

Final source SHA256: `168ab38996a126a749114583ac82d5d72c3b82e9e9f4c0b17b299a0921c7b939`.

**PASS, author complete-proof check.** The final addition is the actual-subvariety realization in SD.9a; its display was then wrapped onto two lines. The other proof and the original-field projection paragraph are unchanged.

The full cyclotomic algebra `O_n=Z2[Z]/Phi_n(Z)` is essential. A single chosen unramified field factor need not be stable under the arithmetic deck action. After an unramified splitting base change, the cyclic action is free on the primitive-root index set. Invariants commute with this flat base change as the kernel of tau-1. The resulting product-ring map is a finite etale torsor of the exact deck degree, also when that degree is even.

A tau-semilinear operator F with F^f=1 is therefore genuine module descent data. Stacks Proposition35.3.9, Tag023N, applies to arbitrary modules, so neither freeness of the finite two-primary module nor division by f is required. Its descended module is precisely the fixed subgroup, and the tensor isomorphism proves equality of exponents.

For each conductor, the integral Ramanujan projector `p_d=n e_d` satisfies `p_d²=n p_d`. Its coefficients are rational algebraic integers and hence integers. Frobenius preserves it, so its image B_d is an actual k-subvariety. The relation restricts p_d to multiplication by n on B_d; n is invertible on two-primary cyclic groups, proving that the canonical module T_d is exactly B_d's geometric two-primary torsion. The exponent assertion is thus not an assertion about an arbitrary isogeny representative.

At the minimal field defining a conductor-d deck action, F^f_d=1 holds on precisely the rational module to which descent is applied. This proves equality of the base-field and minimal-deck-field exponent. For prime n the whole Prym has only that nontrivial conductor. For composite n, a proper-conductor factor can have a smaller deck degree; F^f=1 on its larger-field rational module does not imply F^f_d=1. The coefficient-action kernel can still act nontrivially on the module. No unjustified full-Prym exponent equality is asserted in that case.

The last paragraph independently checks the rational projection and the needed connected-kernel assertion using `n x=sum(1-sigma^i)x`. The image of each summand is connected in the norm kernel. This proves that its component group is killed by odd n and hence that a two-primary norm-zero class lies in B.

Exact primary input: Stacks Project Proposition35.3.9, Tag023N, statement and complete displayed proof reopened/read at https://stacks.math.columbia.edu/tag/023N . The prior lemmas cited within that proof were not all reread independently. No numerical experiment or actual-cover strictness claim forms part of this lemma. The companion bibliography is `NONCONSTANT_DESCENT_BIB.tex`.
