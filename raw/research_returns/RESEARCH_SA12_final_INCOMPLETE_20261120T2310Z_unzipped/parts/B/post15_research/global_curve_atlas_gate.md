# Global curve-cover atlas: exact remaining gate

Recorded after the checked local Eisenstein and fixed-formal-fibre arguments on 20 November 2026. This is a research-status note, not a new theorem.

## What is now proved in this manuscript

For a totally ramified extension of degree `e` and different `d`, the local coefficient charts use at most `2d` polynomial coefficients. Their all-coefficient-ring isomorphism witnesses use at most `7d+6` coordinates and equations of degree at most `e²+1`. The separate unpointed refinement includes nilpotent translations of the formal source coordinate. These statements concern the specified integral formal-disc models; they do not algebraize arbitrary Laurent-series families.

For a fixed smooth proper base curve `E` of genus `h`, degree `n`, and fixed full completed local algebras of total discriminant `D`, the number of global covers is at most `(n!)^(2h) n^(2D)`. The proof chooses common local Witt lifts, patches finite free algebras at every nilpotent level by Beauville–Laszlo, algebraizes them, and obtains one common characteristic-zero discriminant. Generic geometric isomorphisms extend by uniqueness of normalization after a finite DVR extension. The characteristic-zero count weights an inertia permutation by its index: a permutation of index `d` has at most `n^(2d)` possibilities. No restriction prime to the characteristic on `n!` is used.

Thus, when `D=O(n)`, local coefficient dimensions are `O(n)`, local equation degrees are polynomial in `n`, local combinatorial chart choices are `n^O(n)`, and the number of global classes above one formal-data point is `n^O(n)`.

## Fried–Mézard: verified qualitative scope

Fried, M. D., & Mézard, A. (2002). Configuration spaces for wildly ramified covers. In *Arithmetic fundamental groups and noncommutative algebra* (Proceedings of Symposia in Pure Mathematics, Vol. 70, pp. 353–376). American Mathematical Society. https://doi.org/10.1090/pspum/070/1935413

Primary author PDF: https://www.math.uci.edu/~mfried/paplist-ff/fr-mez.pdf

Preserved artifact: `sources/Fried_Mezard_2002.pdf`, SHA-256 `ca5f46d2d1c94770eb3aa0938d514b89390d894fc39b45093987c3abef6e6a1c` (431,607 bytes), relative to this note's directory. Author B read the complete relevant text of Sections 6.5–6.6, author pages 21–22.

Proposition 6.7 obtains a map to the configuration variety after a finite pullback of unspecified degree. Proposition 6.8 treats a constant configuration and concludes isotriviality after another finite pullback. Both are accompanied by outline proofs. The text supplies no quantitative degree bound for these pullbacks or for a presentation of the global gluing relation. Problems 6.9–6.10 retain family Galois-closure issues. Therefore this source cannot be cited as an effective `n^O(n)` global atlas or surface-cover count.

## de Jong–Katz: original note found and checked

de Jong, A. J., & Katz, N. M. (n.d.). *Counting the number of curves over a finite field* [Unpublished note]. https://www.math.columbia.edu/~dejong/papers/curves.dvi

The authoritative author-hosted note is preserved under `parts/D/sources/DeJongKatzCurves/`. Author B read Proposition 4.2 and its complete written proof, pages 4–6, and the subsequent local-count statements; root read all twelve pages. Proposition 4.2 concerns maps to the projective line with source genus `g>=2`, degree `d>=2g-1`, the same discriminant, and formally isomorphic wild ramification. Its proof uses common characteristic-zero local lifting and sketches the formal-patching step. The new checked manuscript proposition supplies that patching step and treats an arbitrary fixed smooth proper target and every degree, while fixing the full local algebras. It does not claim priority for the common-lift method.

The Ellenberg–Venkatesh `BookFF.pdf` discussion on printed page 162 only reports the unpublished curve-count result; root separately verified its paper-wide prime-to-group-order hypothesis on printed page 153. That discussion was not used as a proof of a wild Hurwitz degree bound. The original de Jong–Katz note resolves the provenance of the reported finite-field count, but a finite-field point bound alone does not bound an arbitrary characteristic-p constrained locus.

## What is still missing

The fixed-fibre theorem does not give a bounded-degree finite-type presentation of the global gluing problem. Even if an appropriate global Hurwitz morphism is shown to be formally etale and to have fibres of the proved size, this only controls its intrinsic finite degree where applicable. It does not bound the equations of an additional locus requiring a curve cover to extend over a fixed surface neighbourhood.

The unresolved quantitative step is to construct such an extension locus with `O(n)` effective coordinates and equation degree polynomial in `n`, or an equally strong intrinsic intersection-degree bound. The checked degree-linear exceptional graph, geometric-genus, nonreduced-thickening cohomology, and canonical-energy estimates are numerical inputs toward this step. They do not construct the needed family, its equivalence relation, or its equations.

No inference from qualitative isotriviality, finite fibres, dimension alone, or finite-field specialization is being made. The general finite-generation questions D.1 and D.2 remain unchanged by the local charts and fixed-formal-data fibre bound alone.
