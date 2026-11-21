# F65: direct canonical multiplicities, parameter weights, and Lefschetz

Author /root; GPT-6 Astra Pro; effort not exposed. Date 2026-11-21 UTC.

This is an application of the already proved pure-point trace criterion to the actual individual canonical coefficient printed in VIII. It removes any need to assume that the named right generators P_i are effective. It does not refute VIII's signed/factored positivity, which does not assert the geometric comparison below.

## Exact premise

Work with mixed constructible ell-adic complexes over a finite field F_q and characteristic-zero coefficient field E, enlarged as necessary. Suppose one proposed canonical product is T=Rf_*L, with f proper and L pure of an integer complex weight W. Let S_gamma be a geometrically absolutely simple perverse Weil sheaf, pure of weight w_gamma, which represents the proposed output canonical label. Require that its geometric isomorphism class is Frobenius stable and has the specified Weil form over F_q. This holds for an IC label with a fixed pure Weil local system on its dense smooth stratum; if descent requires a finite base extension, make that extension explicitly.

For each i, let V_i be the geometric multiplicity space

V_i = Hom(S_gamma, pH^i(T))

in the geometric perverse category, with the conjugation Frobenius obtained from the two specified Weil structures. Here the Hom is taken on the geometric base, not the space of Frobenius-fixed morphisms. Assume the finite-extension coefficient comparison is the ordinary Euler trace

f_gamma(q^(n/2)) = sum_i (-1)^i Tr(F^n | V_i), for every n>=1,

or for every sufficiently large n. This is the usual multiplicity-complex comparison; it is stronger than equality of one numerical dimension or one specialization. No insertion of a further operator is included.

## Proposition

Under these hypotheses, C_gamma = direct sum_i V_i[-i] is a pure point complex of weight W-w_gamma. Consequently, if f_gamma is an integral Laurent polynomial, then

(-1)^(W-w_gamma) f_gamma(-v)

has nonnegative integral coefficients. In particular a nonzero f_gamma divisible by v-v^-1 is impossible. The conclusion is unchanged by a common integral grading translation, a common Tate twist, or an overall shift, provided the comparison is adjusted accordingly.

## Proof

Proper pushforward preserves the pure complex weight W. BBD Theorem5.4.1 then says pH^i(T) is pure of weight W+i. BBD Theorem5.3.8 makes its geometric perverse sheaf semisimple. Its S_gamma-isotypic summand is canonically S_gamma tensor V_i; the Frobenius-stable isotypic decomposition and conjugation action make this an isomorphism of Weil perverse sheaves. This argument does not assert arithmetic semisimplicity. Nontrivial Jordan blocks can act on V_i.

The isotypic summand is pure of weight W+i, since it is a perverse subquotient of that pure object (BBD5.3.1). To compute the multiplicity weight, restrict to a nonempty smooth dense stratum U of the support of S_gamma, of dimension d, on which S_gamma is a pure lisse sheaf M[d]. Then M is pointwise pure of weight w_gamma-d. On this same stratum the isotypic summand is (M tensor V_i)[d], and its lisse sheaf has pointwise weight W+i-d.

For completeness, this last passage uses no unsupported assertion that arbitrary restrictions preserve both weight inequalities. Regard the isotypic summand as a perverse sheaf on its closed support, using the fully faithful closed-immersion pushforward. Closed pushforward and its inverse on supported objects preserve its weight bounds; its restriction to U is an open restriction, for which j^*=j^! preserves both bounds. These are the six-operation weight statements BBD5.1.14. Equivalently, the usual IC description and pure subquotient theorem give the same lisse weight.

Choose a closed point of U of degree m. Every eigenvalue alpha of its Frobenius on M has, under every relevant embedding, absolute value q^(m(w_gamma-d)/2). If beta is any eigenvalue of F on V_i, then alpha beta^m is an eigenvalue on the tensor product and has absolute value q^(m(W+i-d)/2). Division gives |beta|=q^((W+i-w_gamma)/2) in every embedding. Thus V_i is pure of weight W+i-w_gamma. Its Jordan form is irrelevant to this calculation.

By the shifted definition of complex purity, the point complex direct sum_i V_i[-i] is pure of weight W-w_gamma: its degree-i cohomology has weight W-w_gamma+i. Its Euler trace is the required coefficient. The already fully proved F57 pure-point trace criterion now gives the nonnegative-coefficient condition, also for eventual extension degrees.

If a nonzero Laurent polynomial is divisible by v-v^-1, it vanishes at v=-1. Its asserted nonnegative transform would therefore vanish at v=1, impossible for a nonzero Laurent polynomial with nonnegative coefficients. A monomial translation and an overall sign preserve the vanishing; Tate twists and shifts simply change the corresponding pure weight and trace normalization. This proves the stated obstruction. QED.

## The actual VIII coefficient

VIII Figure2 p34 and Section5.1.2 p29 print

c(gamma_2^1,gamma_1^1;gamma_21^1) = -(q_src^2+q_src+1)(q_src-1)^2/q_src^2.

Under q_src=q^n and v=q^(n/2), the coefficient is

f(v)=-(v-v^-1)^2(v^2+1+v^-2),

which is nonzero and vanishes at v=-1. Therefore this one actual individual canonical constant already excludes the direct proper-pure multiplicity comparison above, even with arbitrary perverse-cohomological degrees and without any assumption about named-generator effectivity. It does not exclude a pure coefficient before nonproper compact pushforward, a mixed coefficient complex, inserted-operator traces, or a realization only of the normalized positive factor. The latter factor is explicitly the proper Lefschetz object RΓ(P2,E)(1), and F62 constructs a mixed torus-times-projective-plane trace model for the full coefficient.

No step proves that the conjecture's intended nonstandard geometry must satisfy the tested proper-pure premise. The statement instead identifies exactly where an unmodified KL proper-pure multiplicity argument fails for the displayed raw coefficient.

## A necessary normalization distinction, and the separate Lefschetz test

The preceding contradiction uses q_src=q^n. It must not be called variable-independent. If the source parameter is instead assigned q_src=q^(n/2), the same source coefficient becomes

c(v)=-v^2+v+v^-1-v^-2.

It passes the pure-point criterion for odd weight, since -c(-v)=v^2+v+v^-1+v^-2. Let L_e be an arithmetic Weil line of weight e with eigenvalue q^(e/2). Then

C_alt = L_2[-1] direct sum L_1 direct sum L_-1[2] direct sum L_-2[3]

is a point complex pure of weight one and has precisely this Euler trace. Its cohomology degrees are 1,0,-2,-3, with weights 2,1,-1,-2 respectively. This is an actual bounded Weil-complex construction, not a proof of a canonical proper-geometric realization. Odd-weight lines are arithmetic coefficients; no geometric half-Tate motive is asserted. The source's actual variable conventions must be retained when applying either conclusion.

More generally assign q_src=q^(d n/2), for a nonzero integer d. Replacing d by -d does not change the bar-invariant coefficient, so take d>0. The trace is c(v^d)=-v^(2d)+v^d+v^-d-v^(-2d). If d is even, all exponents are even with mixed signs, and no pure point complex of any weight exists. If d is odd, the pure-point criterion allows exactly odd complex weights, and the same four-line construction with degree e-w gives a pure model.

There is nevertheless no realization of any of these nonzero traces by a pure point complex carrying a hard-Lefschetz operator with a single center. Precisely, suppose C is pure of some weight w, its ordinary Euler traces equal c(q^(d n/2)), and there is an integer h and a Frobenius-compatible degree-two operator ell with ell^r:H^(h-r)(C) -> H^(h+r)(C)(r) an isomorphism for every r>=0. The same assertion remains false after multiplying the trace by an overall sign or a monomial v^m and allowing h,w to change.

Here is a full proof. The pure-point Vandermonde argument fixes every spectral root and its unique cohomological degree; hidden roots cannot cancel across degrees of a pure complex. Thus a realization of epsilon v^m c(v^d) has nonzero cohomology only at degrees m-2d-w, m-d-w, m+d-w and m+2d-w, with one-dimensional cohomology in each. The outer signs may already contradict their required parities; if they do not, the displayed support is still forced. Hard Lefschetz forces the support to be symmetric about h. Its smallest and largest degrees therefore give h=m-w. But H^h(C)=0, while H^(h-2d)(C) and H^(h+2d)(C) are nonzero. The asserted isomorphism ell^(2d) between these outer groups factors through H^h(C) after d applications of ell, so is zero. This is impossible. No semisimplicity of Frobenius is used.

For an actual projective pushforward of a pure perverse input, BBD5.4.10 p144 supplies the relative hard-Lefschetz maps; taking a Frobenius-stable geometric isotypic multiplicity preserves them. Hence the displayed raw coefficient also fails this stronger projective pure-perverse multiplicity comparison under every nonzero integer weight assignment q_src=q^(dn/2), even where mere point-complex purity is possible. The normalized positive factor remains distinct. This is an explicit additional Lefschetz premise, not a claim that all proper pure complexes satisfy hard Lefschetz.

## Separate Grothendieck dictionary and primary locators

The multiplicities V_i are actual Weil representations, not merely virtual coefficients or invariant-morphism spaces. Their coefficient category and Euler class fit SGA6 I Definition4.7 pp121-122 and Example4.8 p122. The formal grading and its effective cone use SGA3 I4.7.2-3 and archive cote90 scan17; the distinction between actual and virtual coefficient classes is anchored by SGA6 V Sections2-3 and cote133 scan18. No commutative lambda structure is inferred for the noncommutative convolution algebra.

The actual proper pushforward, perverse subquotients and IC restriction use BBD5.1.14 p128,5.3.1 pp134-135,5.3.8 p138,5.4.1 p141, Remark5.4.9 p143, and5.4.10 p144. The Frobenius-stable isotypic decomposition and its geometric Hom multiplicity are described explicitly in the proof of BBD5.3.9 pp139-140, using5.1.2; the Jordan example immediately after5.3.8 p138 explains why no arithmetic semisimplicity is assumed. These original local primary contexts were read for this refinement. SGA5 III4.7 supplies the trace framework; it does not identify a canonical basis automatically.

The new consequence is the conditional proper-canonical obstruction for the actual VIII coefficient. Neither the archive nor BBD states a nonstandard canonical-basis comparison. Independent whole-proof review is requested before integration.
