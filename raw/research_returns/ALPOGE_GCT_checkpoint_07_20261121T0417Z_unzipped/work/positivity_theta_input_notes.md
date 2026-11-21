# P-F46: exact positive input, output, and a disproved direct coefficient dictionary

Author/checker: `/root/bridges`, GPT-6 Astra Pro, inherited/undisclosed effort.
Full proof: `positivity_theta_input.tex`.

## Established comparison

The actual E6 quasi-pullback used in P41 is, by Ma's theorem, the Borcherds lift of the vector-valued input Theta_E6/delta. The unimodular ambient lattice makes the gluing the graph of an isometry A_M→A_E6; the contraction has coefficient one in each coset, with no factor1/3 or further overlattice averaging. The convention is M of signature(2,20), positive E6, discriminant q=(x,x)/2, and rho(T)e_mu=exp(2pi i q(mu))e_mu. Its two nonzero discriminant values are2/3. This sign convention is the reverse of CML's (20,2) lattice convention and is explicitly stated.

The input has weight-9 and all Fourier coefficients are nonnegative integer counts of a lattice vector together with a24-colored partition. Its complete nonpositive terms are `(q^-1+96)e0+27q^(-1/3)(e++e-)`. Half the constant term is48, the known output weight. Its ball restriction maps to the degree80 cubic discriminant, stretch degree16, up to a nonzero scalar. No scalar normalization is silently fixed.

The proof derives the E6 root and coset counts directly. E6 is A2^3 glued by (v,v,v), with v=(2,-1,-1)/3. An explicit six-root basis has the E6 Cartan graph. This gives72 roots; each nonzero dual coset has27 vectors of norm4/3. These are mathematical counts, not a finite numerical experiment.

Two precise limits are proved for this same input. First, the q^-1 term forces exponential cusp growth and divergence of its ordinary weight-9 Petersson norm, so it cannot be inserted unchanged as an L2 modular input. This does not assert that every theta integral diverges or that no regularized comparison exists. Second, every component, on its own Fourier lattice, dominates the24-colored partition function. An elementary subset-and-padding argument gives an exp(c sqrt(s)) lower bound under every positive affine reindexing. The actual cubic multiplicity f5(s) is at most binom(5s+34,34). Thus a direct coefficient/dimension dictionary is false, including compatible rational affine reindexings on arithmetic progressions. Subquotients, different spaces, and nonlinear transforms remain outside that exclusion.

## Primary sources actually read

- Shouhei Ma, *Quasi-pullback of Borcherds products*, arXiv1801.08333v2 (11 October2019), https://arxiv.org/pdf/1801.08333. Theorem1.1 and equation1.1 p2; exact Weil conventions and theta coefficients pp4–5; pullback equation2.1 pp5–6; theta contraction equation3.1 p12; Example3.13 p18. Fresh refs `turn347065160view0`, `turn874678622view1/2`, `turn611356170view0`. The two key pages were visually read in `theta_sources/ma_quasipullback_2.png` and `_18.png`. The Witt-index hypothesis is checked: at most2<20, and rank22. The scalar input has integral principal part and constant24; the resulting constant96 is even as required.
- CML Proposition7.5 p25 and the exact P41 sources were already freshly read and visually audited in that theorem's source log. These identify the actual primitive embedding, the quasi-pullback, and its ball restriction, rather than an unrelated E6 theta series.
- For corroboration only, Hulek–Kondo–Maeda arXiv2403.18345, Section8.5 p46, explicitly lists the same E6 theta expansions. Fresh refs `turn892568773view0/1/2`. That paper's subsequent product uses E6+A2 and a different ball, so it is **not** used as the output-identification premise here. Our E6 counts are independently proved in full.
- Supplied `ALPOGE_remark.pdf`, printed pp3–4, was reread in full. Item8 specifies the iterated definite-unitary lifts; items9–10/12 discuss norms/divisibility/periods. No theorem for a map from those lifts to this particular g or its multiplicative regularization is invented.

## Whole-proof self-check

I read the entire written proof, then the growth addition, and reconstructed all steps: primitive gluing, discriminant signs, coefficient-one pullback, Ma's hypotheses, actual output identification, A2^3 Cartan basis, every root/coset count, finite coefficient convolution, growth bounds, compatible reindexings, and the cusp lower bound. A literal formatting artifact was corrected before completion. The final proof does not turn Fourier coefficients into invariant-ring dimensions; the growth argument proves that exact proposed direct interpretation cannot work.

Root suggested the useful growth obstruction after the theta-contraction input was identified. Complexity was asked to independently review the complete resulting proof and sources. Its event is to be logged separately by that checker. No historical novelty is claimed for the known theta-contraction construction.

## Exact unitary interpretation added after the core review

Hofmann's *Borcherds Products on Unitary Groups*, https://arxiv.org/pdf/1210.2542, Theorem8.1 printedp24 and definition(28) printedp25, identify this very form as a **unitary Borcherds lift**. It is not necessary to leave the known construction described only as an orthogonal lift followed by restriction. The explicit Hermitian form in(P-F46l) has trace exactly the existing quadratic form, so there is no lattice rescaling, new discriminant module, or dual Weil representation hidden in the interpretation. The lattice is integral in the inverse-different convention and even; the dual is precisely M^vee. The two required isotropic vectors are constructed. The source's general nonunimodular theorem applies with m10, inputweight-9, constant96 and integral principal part. Its exact definition Xi_g=alpha*Psi_M(g) gives phi and the cubic discriminant, up to the already acknowledged scalar. The initial discriminant-kernel group is not silently identified with the exact period group; the established equality with phi supplies the latter extension and multiplier. The multiplicativity clause gives the discriminant powers after consistent normalization.

Freshly read primary locators: Hofmann lattice conventions/Assumption2.1 p6; group p7; underlying trace lattice and holomorphic embedding pp13–15; Weil equation20 p19; Theorem8.1 p24; defining equation28 p25. Actual rendered p24 and25 inspected in theta_sources/hofmann_unitary_24.png and _25.png. Web fullref turn762643369view0, exact theorem/find refs turn703086924view0/view1. Fresh CML Prop7.5 p25 lattice decomposition read. The general theorem, rather than the introductory unimodular case, is essential.

The complete extension was self-read and each algebraic/hypothesis step reconstructed. Complexity was asked for a separate independent extension check. This identification sharpens the remaining task: it is now a comparison with this particular regularized multiplicative **unitary** lift, not a broad distinction of group names. The supplied note's specific iterated operations are still not identified with it.
