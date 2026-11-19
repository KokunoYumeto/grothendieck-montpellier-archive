# Independent audit of C.3p

The current fragment research/agents/real_weil/C3_etale_picard.tex passes the independent proof and exact-source audit. The finite-etale assertion and the separate henselized local-Picard comparison have different scopes, and the fragment preserves that distinction.

## Finite-etale Lefschetz

For the excellent normal strictly henselian local domain R, its completion A is a normal complete local domain of the same dimension. The completion map is regular by excellence. Every point of the completed puncture lies above the original puncture, since the closed fibre has a single point; regularity of that puncture therefore gives regularity of the completed puncture. In particular A_f is regular and satisfies S2. The complete local ring has a dualizing complex.

The argument that A is f-adically complete is valid: an f-adically Cauchy sequence is maximal-ideal-adically Cauchy, and all ideals (f^r) are closed in the latter topology. Thus the maximal-ideal-adic limit has the required f-adic residues. No claim that the two topologies coincide is needed.

Stacks Lemma58.19.5, Tag0EK5, applies for N at least3: the henselian-pair condition follows from f-adic completeness, A_f is S2, and the sole component of Spec A not contained in V(f) has dimension N. It gives full faithfulness. For N at least4, Lemma58.24.1, Tag0EK9, has the same applicable dimension alternative and asks additionally for purity at the maximal points of Spec A_f.

That purity check is correct. The punctured spectrum of a noetherian local ring is Jacobson by Lemma28.6.4, Tag02IM. Hence a closed point in its open Spec A_f is closed in the puncture. Its prime p has dim(A/p)=1. Catenarity and equidimensionality of the complete local domain then give dim A_p=N-1, so A_p is regular of dimension at least3. The categorical purity statement in Lemma58.21.3(1), Tag0BMA, applies already in dimension at least2. The proof deliberately does not use clause(2) with arbitrary finite normal algebras and possible extra closed-point components. Lemma58.24.1 supplies essential surjectivity.

Elkik's SectionIII Theorem5, pp577–579, is indeed stated for the noetherian henselian pair fixed earlier in that section, with no principal-ideal restriction. It is an equivalence for finite algebras etale off the ideal; its fundamental-group corollary is on p579. Consequently the comparisons for the punctures of R and R/(f) with their completions are the required finite-etale equivalences. These comparisons are compatible with restriction. The conclusion therefore descends from A to R. No coefficient field or algebraizability hypothesis is used in this part.

## Picard torsion

When the divisor puncture is regular, the finite-normalization argument already checked in C.3k gives its ring of global sections as a product of normal strictly henselian local rings. Normal Hartogs extension gives the source sections R. All units in these rings have nth roots for n invertible. Kummer therefore identifies Pic[n] naturally with H1_et(mu_n) on both punctures. The equivalence of finite-etale categories preserves the specified finite-etale group mu_n, its group actions, and its torsor property, and gives the asserted isomorphism. In dimension3, full faithfulness gives injectivity. This also works in mixed characteristic when n is a unit; regularity of the divisor puncture is correctly retained for the unit calculation.

## The separate local-Picard completion comparison

For every finite-type k-algebra B, both R tensor B and Rhat tensor B are noetherian, since they are finite type over their respective noetherian first factors. Henselization along the indicated ideals remains noetherian and preserves all quotients by powers of those ideals. Their completions are therefore canonically the same inverse limit of (R/m^r) tensor B. Elkik's Picard corollary, printed p573, explicitly states the required bijection between the Picard groups of the ideal complement and its completed counterpart. Applying it twice gives the functorial bijection on finite-type B.

Etale sheafification preserves this identification on finite-type parameter rings. Under the already checked Boutot representability hypotheses, the group schemes are locally of finite type. Testing on finite-type affine opens constructs the inverse by Yoneda and glues it by uniqueness. This is a legitimate proof of the isomorphism of represented functors; it does not require an unproved extension of their definition to a new class of arbitrary families.

Crucially, these are the local Picard functors defined by henselizing the tensor pairs. This proof does not algebraize an arbitrary henselized family to a line bundle on the fixed product X times T. Thus no ordinary algebraic-equivalence surjectivity follows merely from this isomorphism or from the prime-to-characteristic Picard torsion result. The caveat at the end of C.3p is necessary and correctly stated.

## Fresh primary openings

- Elkik, R. (1973). Solutions d'equations a coefficients dans un anneau henselien. Annales scientifiques de l'Ecole Normale Superieure,4e serie,6(4),553–603. https://numdam.org/item/10.24033/asens.1258.pdf ; full retrieval turn895494495view0; exact Theorem5 and Picard-corollary finds turn302711976view0–1. Local source: research/agents/real_weil/sources/elkik1973.pdf and .txt. Theorem3 is printed p569, Picard corollary p573, Theorem5 pp577–579. The global noetherian convention is on p554.
- Stacks Project, Lemma58.19.5, https://stacks.math.columbia.edu/tag/0EK5 ; turn613284751view0.
- Stacks Project, Lemma58.24.1, https://stacks.math.columbia.edu/tag/0EK9 ; turn613284751view1.
- Stacks Project, Lemma58.21.3(1), https://stacks.math.columbia.edu/tag/0BMA ; turn613284751view2.
- Stacks Project, Lemma28.6.4, https://stacks.math.columbia.edu/tag/02IM ; turn613284751view3.

No shared file was edited.
