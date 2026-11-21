# Independent audit of the explicit cofaces

**Verdict: PASS for the stated two boundary identities.** This audit does not assert the vanishing of either whole Steinberg homology group or of $K_{12}(\mathbb Z)$.

Reviewer: GPT-6 Astra Pro, run `K17/archive_kummer`, 2026-11-21. The complete mathematical text and complete standalone verifier were read. The exact verifier was rerun independently. The earlier cycle text and its complete standalone reflection verifier were also read and rerun.

## Exact reviewed artifacts

* `work/k12_survivor_coface_section.tex`: SHA256 `9a4723824697ad1ce3fcaf05666b8f356431f34a43735e9150f48f060857a0b2`.
* `work/k12_survivor_coface_certificate.py`: SHA256 `ed25a32a9f878b5a7c2e41c64f47abd3facf5e1cd5270e527feb3cefdae28a78`.
* `work/k12_survivor_coface_certificate.json`: SHA256 `09c273deb07fa90d9ddd058b7b8fa1490513c03882902bcfc5bc4441ee07fc4d`.
* `work/k12_survivor_boundary_section.tex`: SHA256 `959dce95fe47dafc01de2bd8a97a574ff4258b7aac8fec2adc46b19e97f66126`.
* `work/k12_survivor_boundary_certificate.py`: SHA256 `bbf194ea4cc6268a3871a119312cc0f9fe396ae69444288c897c69b4bb8f092f`.

The final coface matrix has denominator **720** and the exhaustive search visits **388 nodes**. Earlier discovery variants with other denominators or node counts are not the reviewed final certificate.

## Exact calculation

The displayed integer matrix is symmetric. The verifier constructs its rational Gram matrix, verifies the exact identity $Q=L D L^t$, and verifies that every rational pivot is positive. Its descending enumeration uses

\[
Q[z]=\sum_i D_i\left(z_i+\sum_{j>i}L_{ji}z_j\right)^2.
\]

For remaining budget $B$ and rational shift $a/b$, the bound on the next integer is exactly $(bz_i+a)^2\le (B/D_i)b^2$. The integer square-root bound and the two integer endpoints implement this inequality without rounding error. Every integer in the allowed interval is visited, and every final vector is checked directly. Thus this is a complete minimum enumeration, not a bounded-box search or a floating-point plausibility test.

The independent execution returned positive definiteness, exactly thirteen minimum pairs (the old twelve and $w=e_8+e_9$), and quadratic rank thirteen. All other single-ray deletions have full vector rank nine. The result agrees with the stored final JSON. The orthogonal rank-ten extension has no mixed-component minimum since each nonzero component has norm at least one.

## Cell and orientation argument

The full minimum set of a positive definite form gives a cell by the minimal-class/cell correspondence. This was freshly checked in the primary DEKM author text, Section 1.2.1, printed page 4, and Section 2.1, printed page 6. The thirteen independent quadratic rays make the rank-nine cell simplicial, so its facets are exactly the single-ray deletions.

For each deleted old ray, the prior explicit integral involution preserves the remaining old rays, exchanges two of them, and fixes every other one. Each printed functional vanishes on $w$: the only expressions involving coordinates eight or nine are $z_1+z_8-z_9$, which vanish on $e_8+e_9$. Thus every one of the twelve facets other than the old cell $\tau$ has an odd stabilizer. This was also checked by direct matrix arithmetic in the executed verifier. The independent cycle verifier confirmed all twelve integral involutions and their ray permutations.

The new cell's stabilizer must fix $\tau$, because the existence of an orientation-reversing integral stabilizer is invariant under lattice equivalence and $\tau$ is the unique facet without one. It then fixes the remaining ray. Its permutation on the first twelve rays is a stabilizer permutation of $\tau$, already proved even in the separately audited survivor calculation. Its permutation on all thirteen rays is consequently even. This proves that the new cell itself survives orientation coinvariants, without an unperformed exhaustive stabilizer calculation.

## Incidence and stabilizer factors

The full primary boundary convention in DEKM Section 1.2.1, printed page 4, equations (1) and (2), was freshly read. The coefficient is the sum of the signed incidences over the actual geometric facets equivalent to the target cell. There is exactly one such facet here: any other facet has an odd stabilizer, so cannot be equivalent to $\tau$. Its simplicial incidence is a unit $\pm1$, and appending the last ray to the ordered basis of $\tau$ gives the displayed positive sign in that convention.

The equivariant interpretation agrees. Since the new cell's stabilizer fixes $\tau$, the transfer index is

\[
[\Gamma_\eta:\Gamma_\eta\cap\Gamma_\tau]=1.
\]

The subsequent map on degree-zero coinvariants induced by inclusion in $\Gamma_\tau$ sends one generator to one generator; it does not introduce the index of the source stabilizer in the target stabilizer. There is no hidden target-stabilizer multiplier. Proposition 1.3 on printed page 5 identifies the described differential with the equivariant one, up to the global sign convention. Orientations may therefore be chosen so that $\partial\eta=\tau$.

## Rank-ten extension and scope

For $\eta^+=\eta\perp\mathbb Z$, deleting $w$ gives the prior cell $\sigma$. Deleting any old ray gives an odd stabilizer $g_i\perp1$. Deleting the new orthogonal axis leaves vector rank nine in ambient rank ten, hence lies in the relative boundary and contributes zero. Lattice equivalence preserves both vector rank and the odd-stabilizer property, so $\sigma$ is again the unique full-rank facet with a surviving orientation generator. The same unique-facet argument proves that $\eta^+$ is orientable and its coefficient on $\sigma$ is a unit. Choosing its orientation gives $\partial\eta^+=\sigma$.

Thus the two earlier explicit cycles are boundaries over $\mathbb Z[1/13!]$. Their construction does not produce a counterexample to homology vanishing. Conversely, filling these two cycles does not establish vanishing of all other cycles. The unresolved rank-eight, rank-nine and rank-ten inputs in the index-safe $K_{12}$ criterion remain unresolved by this calculation.

## Executed checks

`python work/k12_survivor_boundary_certificate.py` passed all twelve facet reflections and both cycle assertions, with `nonboundary_claim: false`.

`python work/k12_survivor_coface_certificate.py` passed with: positive definite; thirteen minimum pairs; 388 enumeration nodes; quadratic rank thirteen; twelve odd other facets; all reflections fix $w$; both boundary coefficients one; `whole_homology_claim: false`.

The full current TeX was read again after the final minimal-class/cell citation was added. No mathematical correction is requested.
