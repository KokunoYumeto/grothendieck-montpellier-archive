# Least-prime Chebotarev locator for the number-algorithm component

Run CX_GRH. Researcher `/root/koiran_gct`, GPT-6 Astra Pro, inherited effort not exposed. 2026-11-20 UTC. This is a **targeted source check**, not an independent reproof of an analytic theorem.

## Exact usable citation

Eric Bach and Jonathan Sorenson, *Explicit bounds for primes in residue classes*, Mathematics of Computation **65**(216) (October 1996), **1717–1735**, doi:10.1090/S0025-5718-96-00763-6, **§5.1 Theorem 5.1, printed p.1729**. Let E/K be Galois, E≠Q, d=[E:Q], Δ=|disc E|. For each prescribed Frobenius conjugacy class, there is a residue-degree-one prime ideal of K in that class with norm at most

`(4 log Δ + 2.5 d + 5)^2`.

The analytic convention is explicit at the end of **§2, printed p.1720, immediately after (2.10)**: the remaining paper assumes the zeta functions of **E and Q** have no zeros in Re(s)>1/2. This is not a statement assuming only rational Dirichlet GRH. The combined task premises H_M and H_A discharge both hypotheses. If minimizing to RH ζ_E alone is necessary, do not silently omit the printed ζ_Q hypothesis: use an appropriate known implication in the Galois case or the LO77 statement below.

**Theorem 3.2 and Corollary 3.3, printed p.1721**, explain reduction from general Galois E/K to cyclic E/E^{<σ>} and passage from σ to its conjugacy class. The top field E does not change. The Hecke factorization (2.2) is printed p.1720. No individual nonabelian Artin holomorphy hypothesis is introduced.

For the desired Kummer-field application E=Q(ζ_{2n},p^{1/n}), E/Q is Galois. Applying Theorem5.1 with K=Q therefore bounds a rational prime q in a prescribed nonempty conjugacy class by the displayed expression. The Galois/conjugacy conditions themselves must still be checked in the application.

## Primary copy actually consulted

The full original paper uploaded by coauthor Jonathan Sorenson:

https://www.researchgate.net/publication/220576951_Explicit_bounds_for_primes_in_residue_classes

The cached page identifies the author upload and supplies the original text and printed page breaks. Bibliographic page range independently matches the author repository https://digitalcommons.butler.edu/facsch_papers/1121/ . The AMS direct PDF returned 403; its content is not falsely reported as downloaded. No original-file visual inspection was performed for this supplemental source.

Web retrieval handles: `turn506479540view0` gives the complete Theorem5.1 statement and preceding printed p1729 break; `turn980061349view0` gives the explicit ζ_E/ζ_Q convention and Theorem3.2/Cor3.3; `turn258535806view0` identifies Sorenson's original upload.

## LO77 numbering caution

Lagarias–Odlyzko, *Effective Versions of the Chebotarev Density Theorem* (1977), **Corollary1.2** assumes RH ζ_L and gives an initial bound with an extra `(log log Δ_L)^4` factor. The final paragraphs of **§9** remove that factor using the smoothed integral (9.8)–(9.9), obtaining `N𝔭≪(logΔ_L)^2`. This refinement is not a separately numbered theorem. In the consulted transcription, Corollary1.2 appears on PDF p4, and the final refinement on PDF pp38–39.

https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf

Web handles `turn443992436view1` (Cor1.2) and `turn506479540view1` (final §9 refinement). Do not cite only Cor1.2 for the factor-free bound without also identifying the final refinement. For an explicit numerical constant, Bach–Sorenson Theorem5.1 is the cleaner locator.

The later paper's label “Theorem5” is not the numbering of the Bach–Sorenson original; the original locator is **Theorem5.1**.
