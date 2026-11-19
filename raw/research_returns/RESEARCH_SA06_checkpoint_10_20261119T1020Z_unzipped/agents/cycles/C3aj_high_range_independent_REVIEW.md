# Independent full audit of C.3aj

**Outcome: PASS.** We read the entire high-range draft (now finalized as agents/real_weil/C3_high_range_surjectivity.tex) and agents/frobenius/C3_product_Hodge_inputs.tex. The audit concerns every \(r\ge2\) and \(N\ge2r+2\), ordinary algebraic equivalence by actual fixed-product families, and the stated countable-field Picard quotient. The final source checks were completed on 2026-11-19, after 09:25 UTC.

## Incidence geometry and the countable-field invariant

We checked the dimension conventions \(s=r-1\), \(m=N-2r\ge2\). Generic \(m+1\) sections of the very ample bundle have a smooth transverse base locus of the expected codimension, or an empty one. At a base point their independent differentials make the incidence hypersurface smooth for every projective \(x\). The exceptional locus has codimension \(m\ge2\); the projective-bundle open is dense and integral. The deformed-cone construction, finite normalization, unique point over the vertex, ideal equality, regular model and transverse principal section are the constructions already audited in C.3ae, now with the stated product of surfaces. We found no additional component or hidden shrinking choice.

The integral operator is well defined on cycles on the incidence hypersurface before passage to the quotient. Its exact pushforwards are \(p_*h^{m-1}=1\), \(p_*h^m=a\), and \(p_*h^{m+j}=0\) for \(j\ge1\). For a boundary family of codimension \(r-1\), weak Lefschetz lifts only the needed cohomology component, not the Chow class. This is sufficient: the boundary's mixed image is exactly

\[
\operatorname{pr}_{C,*}\bigl(\tau(2a\zeta_0+a^2\zeta_1)\bigr).
\]

We rederived the missing-factor argument. The odd degree lies on \(C\). Each K3 factor must contribute total cohomological degree four after multiplication by its \(\tau_\nu\). A degree-four input already vanishes; a degree-zero input must receive an \(H_\nu\) from the indicated power of \(a\), which gives \(\tau_\nu H_\nu=0\) after integration. There is at least one such missing input in both terms. A \(K_C\) insertion kills the curve's degree-one component. Thus the boundary map kills every mixed class, not only algebraic classes. The resulting Picard family has zero differential and is constant, integrally.

The field argument is consequently legitimate. It is applied only to cycles on the smooth projective exceptional section \(H\). A Hilbert component containing a complex point is the base change of a component over the algebraically closed countable field; a point over that field exists. A chain of proper curves, normalized, and the universal flat family show ordinary algebraic equivalence to a cycle over that field. The boundary's image is therefore contained in \(\operatorname{Pic}(C)(\overline K)\). No finite-type parameterization of cycles on the strict-local puncture is assumed.

Localization and self-intersection then define \(\rho\) on all target Chow classes modulo the stated Picard subgroup. Its compatibility with parameter fibres follows by using the same closure on the fixed proper model times the parameter. The quotient is uniquely divisible: division is inherited from complex Jacobian points, and a point whose nonzero multiple is defined over the algebraically closed \(\overline K\) is itself defined there, since multiplication is finite.

## Product-Hodge input

The independently varying period domains supply the jointly Hodge-generic tuple with rank-two Néron–Severi groups, scalar transcendental endomorphisms and no pairwise transcendental Hodge isomorphisms. The chosen complex embedding is explicitly part of the data.

We verified the subdirect Lie-algebra argument in full. A proper subdirect semisimple Lie algebra would identify two \(\mathfrak{so}_{20}\) factors. In type \(D_{10}\), every diagram automorphism fixes the standard-vector highest weight. The representations would therefore have a nonzero intertwiner after scalar extension; the intertwiner equations are rational, so one exists over \(\mathbf Q\). Connectedness turns it into a Hodge isomorphism, contradicting the chosen tuple. Thus the Hodge group is the full product. The CM factor is independent because the derived group kills a torus and surjects onto the semisimple product.

For each nonempty transcendental support \(I\), the corresponding tensor representation with the CM elliptic \(H^1\) is rationally simple, after taking account of the two conjugate torus characters. The Néron–Severi factors and the three elliptic copies produce multiplicities. Every such constituent has level \(2|I|+1\ge3\). Hence the exact selected Künneth tensor has the asserted level-one part, uniformly for every parameter curve. This does not require the parameter curve to descend to \(\overline K\).

## Chern obstruction, source families and target witness

The three-section rank condition is nonempty: choose one linear form on each quartic whose multiplication does not kill its primitive \(\tau_\nu\), then use their product times the three curve coordinates. The generic section tuple satisfies this rank open and the independent geometric open simultaneously. The class and minors are defined algebraically over the countable coefficient field.

We checked the degree-\(r\) conormal exterior sequence, the rational Chern-character lift and the selected Künneth projection against the already audited C.3ae/C.3af arguments. Each factor's cohomological and differential degree is preserved, and the contraction acts only on the curve. The product-Hodge lemma reduces the relevant algebraic component to the Néron–Severi tensor, whose sole fully primitive line is killed by the rank-three obstruction. The source image is exactly \(\operatorname{pr}_{C,*}(\tau(b_0+ab_1))\); the \(ab_1\) term vanishes on the mixed component by the same missing-factor argument. Thus the image of every actual ordinary source-family difference is zero.

The target divisor construction uses legitimate line-bundle pullbacks even when the incidence projection is not flat. Its composite with \(\rho\) is \((-9)^s\) times the quotient map. Divisibility gives the integral cokernel surjection. The specified curve point with coordinate transcendental over \(\overline K\) has no nonzero multiple in \(\operatorname{Pic}^0(C)(\overline K)\); finite multiplication and the Abel closed immersion prove this. The target witness survives rationally.

## Exact primary source checks

The five K3/CM sources were independently read for C.3ag and are retained in that review: Brevik–Nollet, Huybrechts, Cattani–Deligne–Kaplan, Zarhin and Beauville, with the same exact locators and scope limitations.

For this audit we freshly opened the complete Milne *Reductive Groups*, version 2.00, 10 March 2018, and read 18.26–18.27 (pp. 91–92), 20.3–20.4 (pp. 102–103), 20.33 (p. 108) and 21.4 (p. 112). These are the precise root, highest-weight, integration and outer-automorphism inputs used above.

We also freshly opened Grothendieck's Bourbaki Exposé 221, the complete 29-page primary PDF, and read Theorems 3.1–3.2 (printed pp. 259–260), the projectivity argument (pp. 264–265), and the Hilbert specialization/universal-flat-family description (pp. 265–266). The separate 1962 erratum, printed p. 302, was opened and read. Its corrections do not remove or weaken the projective fixed-polynomial Hilbert scheme used here. The draft's field argument relies on these actual projective Hilbert schemes, not on an unsupported assertion about strict-local parameter spaces.

No change to a shared proof file was made by this audit. The result is ready for final owner formatting and integration.
