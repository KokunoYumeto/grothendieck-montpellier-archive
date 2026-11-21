# A48 geometric singular-arrows corollary: independent whole-proof review

Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Date: 2026-11-21T06:54:08.009399+00:00.
Source: `work/row_audit/A48_GEOMETRIC_SINGULAR_ARROWS_COROLLARY.tex`.
Source SHA256: `621be08cff1bade89a711744b4182984e6e5e04ac2da11cd7df3d89724445714`.

## Verdict and scope

PASS. I read the entire statement, all four proof steps, and the concluding scope limitation. I also read the complete integrated A48 pullback supplement used for the actual-projector injection. This is an independent same-model mathematical reading, not formal verification, an explicit construction of equations, or a new arithmetic computation. No change to the source or to the matched 158-page final build is requested.

## Complete argument checked

Raynaud's genus-two characteristic-two choice is m=5,n=3. The first etale cyclic degree-five cover has genus six. With the usual principal polarization, n divides the restriction degree six, and 6/3=2 is at most (6-1)/(2-1)=5. The construction before Theorem 17 produces an actual etale Galois Heisenberg cover: its exact central extension has kernel mu_3 and quotient J[3] of order 3^12. Thus its group has order 3^13, not merely a quotient of that order. Taking all five conjugates over the cyclic base yields a Galois group embedded in H^5 and surjecting onto H, hence degree 5*3^a with 13<=a<=65. This is prime to thirteen.

The induced theta-less representation factors through this Galois closure. Proposition 1(4) preserves the absence of a theta divisor under induction, and Proposition 1(5) gives containment of the entire pulled-back Jacobian in the actual locally exact differential theta support. Choosing the cyclic thirteen-class on the relative Frobenius twist is justified by the etale equivalence; norm-pullback multiplication by the degree, prime to thirteen, retains exact order. All twelve nontrivial powers therefore lie in the theta support.

The covers of degrees thirteen and 5*3^a are geometrically linearly disjoint. Odd-degree pullback and norm commute with the actual primitive projector, and their composite is multiplication by an odd integer, so the geometric two-primary torsion of A32's ordinary dimension-twelve primitive factor injects into the new actual factor. This proves the lower two-rank bound twelve without replacing the factor by an arbitrary isogenous representative. Riemann--Hurwitz gives g(Y)=d+1 and primitive dimension 12d.

For each nontrivial character, both degree-zero line bundles in the locally exact differential sequence have no global sections. Its Frobenius kernel is exactly the corresponding H0(B tensor M^i), which is nonzero. Each coherent character space has dimension d. Frobenius may permute the characters, but their direct sum still has kernel dimension at least twelve, hence stable rank at most 12d-12. This is compatible with the lower bound twelve and explicitly refutes nilpotence despite all twelve singular arrows. There is no illicit genus-two one-dimensional-arrow inference after the high-genus pullback.

All finitely presented curves, morphisms and finitely many deck automorphisms over the algebraic closure of a finite field descend to one finite extension. Geometric connectedness, ranks and incidence survive that descent. A further extension can rationalize a chosen lift; the proof makes no original-field rational-unit claim after doing so.

## Direct primary-source reads

- Michel Raynaud, *Revetements des courbes en caracteristique p>0 et ordinarite*, Compositio Mathematica 123 (2000), 73--88, DOI 10.1023/A:1001840726893. I directly read the complete Proposition 1 statement and displayed proof (pp.74--75); the Heisenberg construction before Theorem 17 (pp.83--84); Lemma 16 and Theorem 17 with their displayed proofs, Corollary 18 (p.85); and the general proof of Theorem 2 through the characteristic-two m=5,n=3 case (pp.85--86). The complete published result is used as cited, not rederived from its Mumford/Hirschowitz inputs. In characteristic two the required degree-two line subbundle can also be read directly from the rank-one B of degree five. Local PDF SHA256 ad8cd27ee1169d46c9e79e902e02bc40fc66145ffe35b79b4c86f62b381b183f. Primary URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16AB72912D3CE32BFC5D012B1025A8E4/S0010437X00000440a.pdf/revetements-des-courbes-en-caracteristique-pandgt0-et-ordinarite.pdf . Own web reference: turn794971640view0.
- Florian Pop and Mohamed Saidi, *On the Specialization Homomorphism of Fundamental Groups of Curves in Positive Characteristic*, MSRI Publications 41 (2003), Section 1.3, printed p.112. I directly read the relative-Frobenius torsor setup immediately before Section 1.3 and its complete coherent-character/locally-exact-differential argument. Only these parts, not Proposition 2.1's unrelated torsion claim, are used. Primary URL: https://library.slmath.org/books/Book41/files/pop.pdf . Own web reference: turn547957809view0.

The A32 ordinary primitive rank twelve and the earlier pullback formalism are retained checked inputs. No new A32 enumeration or certificate replay was performed for this review. The entire pullback supplement was reread; its projector/norm injection is valid as stated.
