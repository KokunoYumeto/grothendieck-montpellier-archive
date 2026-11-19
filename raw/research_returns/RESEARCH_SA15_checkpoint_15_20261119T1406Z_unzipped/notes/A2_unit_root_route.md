# A.2 all-degree stable-part route (active proof, 2026-11-19)

We checked R1 from the attached independent proof: Frobenius on H^j(I_Y) factors through H^j(O_X(-p^e d)), which vanishes for j<n and e large by Serre duality and Serre vanishing. Consequently p-etale cohomology restriction is iso below n-1 and injective in n-1 by Artin-Schreier and semilinear Lang.

Ogus (1975), Corollary 4.7, Theorem 4.9, Remark 4.10 and Corollary 4.11, opened at https://www.numdam.org/item/10.24033/asens.1289.pdf, identify the integral Frobenius-stable part of crystalline cohomology INCLUDING TORSION with H^i_et(X,Z_p) tensor W over algebraically closed k, for smooth proper X embeddable in smooth W_n scheme (projective X suffices). We use projective X/Y.

Let C=cone(RGamma_et(X,Z_p) -> RGamma_et(Y,Z_p)). The mod-p result implies C tensor^L F_p lies in D^{>=n-1}. Derived p-completeness then gives H^j(C)=0 for j<n-1 and H^{n-1}(C) p-torsion-free. Thus the map on H^{n-1}_et(Z_p) is injective with torsion-free cokernel. This needs a written elementary bounded-complex Nakayama proof, not a loose coefficient induction.

Exactness of stable extraction on finite W-modules with sigma-Frobenius follows first on finite W-length objects by Ogus 4.8, then by p-adic limits with induced filtrations (Artin-Rees) and Mittag-Leffler. Therefore the unit part of E=coker(Hcris^{n-1}X->Hcris^{n-1}Y) is free, even if E has non-unit torsion. This proves that (E/p)_SS counts rational slope-zero eigenvalues for EVERY smooth ample Y. In particular the admitted full integral weak-Lefschetz statements are unnecessary for 8.5's stable assertion.

Take stable UCT sequences for X and Y. The right term Hcris^n(Y)[p]_SS vanishes because dim Y=n-1 and Ogus gives etale p-cohomological dimension. On the left, integral etale saturation supplies mod-p injectivity. R1 supplies middle injectivity. The snake lemma gives
0 -> (Hcris^n(X)[p])_SS -> (E/p)_SS -> E(Y,O_Y)_SS ->0.
Hence phi bijective iff this torsion unit group vanishes, and dimension equality/inequality hold all d.

Need rational characteristic-polynomial equality between crystalline and l-adic in each degree (Katz-Messing Theorem 2), and rational weak Lefschetz for vanishing quotient. No standard conjecture on Lambda is needed. Exact conventional identification arithmetic Galois on fixed Frobenius vectors vs geometric Frobenius inverse must be stated.

Status: strong complete route, pending independent type check and source exact theorem verification.

## Simplification found after the first route

The exact sequence itself needs no integral stable-part comparison at all. Apply R2 to UCT to obtain 0 -> (Hcris^{n-1}(Z)/p)_SS -> H^{n-1}(Z,O)_SS -> Hcris^n(Z)[p]_SS -> 0. For Z=Y, the right term is zero: UCT in degree n gives (Hcris^n(Y)/p)_SS=0 since H^n(Y,O)=0; finite W-module stable extraction then gives Hcris^n(Y)[p]_SS=0. The middle vertical arrow is injective by R1, forcing left vertical injectivity too. The snake lemma gives the stated exact sequence; its middle cokernel is (E/p)_SS by right exactness of tensor and exactness of stable extraction. The etale integral argument remains needed only to exclude stable torsion in E for the eigenvalue count.

## Transcription correction
Both AI transcriptions actually preserve a crossed-out section 8.2 at scans 3-4, including (8.2.1). The prompt assertion that there is no section 8.2 needs qualification: the section is canceled, not absent from the witnesses. Without scans we cannot independently verify the crossing-out beyond their agreement.
