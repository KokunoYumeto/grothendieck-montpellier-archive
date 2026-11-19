# Cote 136: close reading of the Codex continuation

Read in full on 2026-11-19: K136-01, lines 1–744 (scans 328–342); K136-02, lines 1–912 (scans 343,345,346,348–353,355,357–361); K136-03, lines 1–940 (scans 362–376). These lead files receive no NOTES_INDEX verdict rows. Scan numbering, not pencilled archive numbering, is authoritative for locators. No scan images of the manuscript have been supplied.

## Separate the layers

* 328 continues 326–327: Euler classes for SL2(R), its projective quotient, discrete groups and a genus-g curve. The half-class equation is cancelled; 2g−2 and g−1 remain alternatives. This is an unresolved normalization, not a proved formula. Signs also depend on orientation.
* 329–335: natural divided-power transformations for F_A=Hom_k(A,−), a coalgebra A, extra maps A→Γ^pA, polynomial-law extension, and transport of PD ideals. The partial sketch at331 is not a second theorem. The cancelled rational Sym construction at330 is recorded as cancelled.
* 337–343: binomial rank calculations, normalized simplicial cochains, double duals, natural transformations, and reconstruction. Actual Nat on all simplicial modules and morphisms of cochain realizations cannot silently be identified. For infinite X, the displayed bidual warns of the missing condition. Monoidal maps of free diagonal coalgebras over a disconnected ring can include idempotent combinations, so set reconstruction requires hypotheses on k.
* 345: simplex realization torsors and a comparison with a colimit are questions. The circle equalizer is an example, not a proof of the general homotopy assertion.
* 346: operator relations on PD forms, then attempts to split Γ^pΦ⊗Φ→Γ^pΦ⊗Ψ. The projection of the proposed derivative formula is multiplication by p, not automatically the identity. The return arrows remain marked '?'.
* 348,350,352: definition of a half differential algebra, cohomology product, resolution from 0→kT→Φ→Ψ→0 with flat Ψ, and extension of the product on cycles. The extension problem has an obstruction before its Hom-valued indeterminacy; the page does not assert a global solution.
* 349,351,353 are English reused typescripts. They concern Sullivan models and nonabelian periods; their source/author identification is bibliographical, not manuscript authorship.
* 355 resumes universal additive cocompletion. 357–361 is a review of Eilenberg–Zilber, normalized chains, homotopies, equivariant resolutions and Steenrod powers. 'pour X variable' is crucial on360: a fixed-X Hom complex is not an acyclic resolution in general. The exponent defining P^i on361 is literally blank.
* 362 corrects initial décalage formulae; 363 reviews Dold–Puppe/Dold–Thom and explicitly limits one comparison to one-degree complexes. 364–368 reviews Steenrod operations, Milnor dual algebra, stable symmetric-power weights and the bar construction. 369 is a blank ruled leaf, not a missing mathematical argument.
* 370 is an independent algebraic K-theory leaf. Its scheme statements need regularity and the appropriate descent/Gersten hypotheses. No such hypotheses are written next to 'X un schéma'.
* 371 adds the odd-prime excess-boundary qualification omitted in365. The stable range qualification at533 cannot be discarded when quoting the integral formulas at527–530. The sentence about all homology being prime torsion is false without removing H_n and controlling degree/range.
* 372 explicitly says Cartan imposes unspecified hypotheses on G,H and 'r assez petit'. An unconditional symmetry H_*(K(G,n),H)=H_*(K(H,n),G) is not justified; H_2(K(Z,1),Z/2)=0 but H_2(K(Z/2,1),Z)=0 is not a counterexample, whereas H_3 gives 0 versus Z/2. Stable symmetry has a spectrum-level explanation and a range must be specified.
* 373 gives a free-abelian cotriple resolution and connectivity estimates. Exponentiation notation Z^G is ambiguous against earlier direct-sum notation; do not silently turn all products into free groups. The displayed bound is false under the ordinary space-smash/integral-homology reading: n=p=4,G=Z gives H10=(Z/2)^2 at the source and Z/2 at the target, despite10<11. A simplicial-linear interpretation would be a different statement.
* 374 transports operations to characteristic-p structural sheaves; P^0 is Frobenius rather than identity. Its opening P_R^i=P^i⊗1 conflicts with p-semilinearity if it is the usual operation on R-cochains. Ext is in F_p-module sheaves at375, explicitly not arbitrary abelian sheaves. The Witt-vector extension at374 is therefore not a counterexample to Ext^1 in that category.
* 375–376 proposes Frobenius-torsion of higher Ext, perfect-site vanishing, an induction, two edge-map lemmas and a final numerical formula. Lemma2 is proved only for P^0. The final F-exponent v_p(i) is suspicious: it yields Ext^2=0 and must be checked against Breen with identical coefficient category and left/right Frobenius actions.

## Formula alarms requiring ink, not editorial replacement

1. K136-01:330 line112: Γ*(X)⊗Γ*(Y)→Γ^2(X×Y) should likely have Γ* on the right.
2. 333 line227: the PD product expansion has ordinary powers on every factor; one factor must retain γ_q. Compare the standard axiom γ_q(ab)=a^q γ_q(b).
3. 334 line317: for γ^p(γ^q x), the coefficient is (pq)!/[p!(q!)^p]; the written denominator (p!)^q q! belongs to the opposite nesting. A 2,3 test distinguishes 10 from15.
4. 335 line349: λ^p x^p differs from the calculation's λ^p x^(p).
5. 338 line484: the normalized C^m_(m+1) is rank1 but the displayed unnormalized Λ^(m+1)k^(m+2) is rankm+2; brackets/projection are missing.
6. 341 line678: the two case conditions conflict (j≠1,i+1 in the nonzero clause), and the shift i−1 versus i+1 needs the actual convention.
7. 345 lines72–73: rank(Ψ_m)=m in 0→kT→k^(m+1)→Ψ_m→0, so the displayed m+1 is inconsistent.
8. 349 lines388–390: Heisenberg matrices have bottom right0, making them noninvertible;351 line454 has1.
9. 357 lines651–652: for homological complexes, the differential of a degree2 homotopy is d l−l d, not d l+l d, unless conventions differ.
10. 357 line704: standard Alexander–Whitney has no extra (−1)^i; a degree1 check will test the written sign under the conventional total differential.
11. 359/361: Σ_n versus Σ_p interchanges in a p-fold construction; flag all exact occurrences.
12. 365 line200: Sq1 Sq2=Sq3; the extra Sq2 Sq1 is nonzero, detected on H*(RP∞;F2) in degree1. He marks this identity '(?)'.
13. 367 line311: L Sym^r=0 unless r=p^s is false unstably, including r=0 and n=0. The next lines suggest stable positive-weight interpretation.
14. 372 line649: Z+[S^m]=K(Z,m), not K(Z,n).
15. 374 line727: standard Steenrod operations over R are Frobenius-semilinear, hence scalar factor F is needed for all P^i; test a x^2 over F_p[t].
16. 376 line903: exact exponent and category to be compared with Breen, without changing text.

These are research judgments from the supplied transcription. They do not decide what is written in the missing manuscript images.
