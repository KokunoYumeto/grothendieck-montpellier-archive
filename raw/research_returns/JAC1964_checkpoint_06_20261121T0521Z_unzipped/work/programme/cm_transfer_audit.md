# CM modular-motive transfer audit

Run JAC1964-20261121; /root/programme_audit; GPT-6 Astra Pro; effort setting not exposed. This note records a checked source boundary and a small transfer lemma. It does not claim a new infinite-rank theorem for the Fermat motive.

## What would suffice

Let W be a smooth projective threefold carrying cycles z_j with independent Abel–Jacobi images in the component of H³(W) attached to the Gaussian weight-four form. Let N be the actual Chow summand of JAC-P13/P17. Suppose a rational algebraic correspondence Gamma from W to J induces an isomorphism from that cohomological component onto H(N), and kills the other components used by these images. Then Gamma_* z_j are independent modulo algebraic equivalence in CH²(N), provided the selected Abel–Jacobi target already factors through the Griffiths quotient, as in the relevant source.

The reason is functoriality of Abel–Jacobi under algebraic correspondences: a relation among the image cycles would induce the corresponding relation among their images in the selected intermediate Jacobian, and Gamma is injective there up to finite kernel. Rational coefficients remove that finite kernel. A Chow inverse is not needed for this argument. An isomorphism of realizations or of absolute-Hodge motives without an algebraic correspondence is insufficient, since it does not define the needed map on cycles.

This formulation also identifies a second, independent check: an infinite-rank theorem for the whole Kuga–Sato Griffiths group does not automatically give infinite rank on one fixed newform component. The proof must preserve independence after that projection.

## Directly read source boundary

Flapan–Lang, *Chow motives associated to certain algebraic Hecke characters*, arXiv:1708.03145v2, Section3.4.1–3.4.2, authorp18, constructs separate Chow realizations. Its displayed comparison with the standard Hecke-character motive is explicitly in the numerical abelian-type category. The following short modular-form paragraph does not exhibit an algebraic correspondence from a Kuga–Sato variety to the product-of-curves realization. Primary URL: https://arxiv.org/pdf/1708.03145 .

There is also a concrete scope restriction for applying that paragraph here. Their initial exponents e,f are coprime and both at least2. For the indexed CM fields, put a=e/d' and b=f/d. Properness of the divisors gives a,b>=2, and gcd(a,b)=1. Hence

\[
 K_{d,d'}=\mathbf Q(\zeta_a,\zeta_b)=\mathbf Q(\zeta_{ab}).
\]

Their explicit imaginary-quadratic modular comparison assumes [K_{d,d'}:Q]=2. Thus phi(ab)=2, so ab is3,4 or6. The coprime lower bounds leave only ab=6. Consequently that literal case has CM field Q(sqrt(-3)); it does not directly cover Q(i). Their higher-dimensional CM factors can still have imprimitive CM type, but extracting such a factor does not by itself supply the missing Kuga–Sato correspondence.

Scholl, *Motives for modular forms*, Sections1.2.2–1.2.4 and Remark1.2.6, authorpp2–3, distinguishes the Chow motive of the full modular-form space from its fixed-newform decomposition modulo homological equivalence. This exact distinction is part of the original source, directly read at https://www.dpmms.cam.ac.uk/~ajs1005/preprints/mf.pdf . It prevents treating a fixed-newform Chow projector on Kuga–Sato as an automatic consequence of the usual modular realization theorem.

The accepted032 results concern abelian varieties. Applying JAC-P16 to the Kuga–Sato object first requires an actual presentation of the relevant Chow motive as geometric abelian type. Knowing its CM Hodge structure or its compatible Galois character does not supply that presentation. The checked sources have therefore not closed either the algebraic-correspondence gate or the fixed-component infinite-rank gate for N.

