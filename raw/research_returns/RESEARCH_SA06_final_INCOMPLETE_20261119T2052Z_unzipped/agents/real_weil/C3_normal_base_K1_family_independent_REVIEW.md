# Independent audit: rank/determinant and whole proper K1-family lifting

**Verdict: PASS for NK.1–NK.10 at the stated hypotheses and exact-endpoint boundary. Auxiliary theorem; no main-gate movement.**

Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, run `/root/component_families`; effort setting not separately exposed.

## Exact scope and artifact

Freshly read the entire `agents/frobenius/C3_normal_base_K1_family_RESEARCH.md`, including its scalar-extension and finite-closure limitations and full source ledger. Reviewed SHA256: **72496a0cbf47d83d3796cd7ff3a6e186b5268830e31c0bc9f96337c7341b38a4**. The full FF.1–FF.4 proof and complete AE/WP dependencies were freshly reread earlier in the same continuation for the WP review; their exact source-audit boundaries are reused.

## Independent reconstruction

For a rank at least two bundle on B=Spec(R)×P, the finite-dimensional incidence over the closed curve has smaller dimension than the coefficient space. Its properness makes the bad locus closed, so a nowhere-zero closed-fibre section exists. Coefficient-field lifting gives an actual section, whose zero set cannot exist elsewhere: its proper closed image in a local scheme would contain the closed point. The resulting line subbundle has locally free quotient. Induction proves additive generation of K0 by line classes, with no splitting-as-objects assertion.

For a line bundle, the two sufficiently positive sections need only be nonzero on the integral closed curve. Their zero schemes are locally principal and fibrewise Cartier. Stacks062Y(3) makes them relative effective Cartier in neighbourhoods of the entire closed fibre; the same proper-local argument covers all of B. Stacks02UP makes them finite over an open containing the closed point, hence finite over all of Spec(R). Finite algebras over a local ring are semilocal. The rank-one Chinese-remainder/Nakayama argument applies without an Artinian assumption, so every line restriction is trivial there.

The Cartier sequences therefore give NK.3 in perfect K0, and projection formula gives NK.4 exactly. Since line classes generate, these identities prove rank/determinant isomorphism and I²=Fγ²=0. The gamma and Adams assertions follow directly from line-element identities. No normality, regularity or henselian property was used in this first part.

For proper birational g over normal integral R, g_*O=O follows either by the DVR intersection characterization or by proper coherent finiteness and integral closedness. The finite affine Čech calculation commutes with tensoring over k, proving the corresponding product statement. The projection formula then gives Picard injectivity. Together with rank/determinant on the source, this proves K0 injection without any rank/determinant assertion for the target.

The every-degree FF exact sequence then has an injective K0 boundary target, so K1(Z×P)⊕K1(P) maps onto K1(E×P) after inverting p. The second summand is already supplied by the actual projection Z×P→P. Thus NK.7 is a whole fixed-product lift and has the stated dimension-independent scope.

At a point, exactness applies to the pair (a,0). Its preimage unit has residue zero, giving precisely NK.9a, rather than equality with every image of K1(R). Local commutative K1 is the unit group and has Adams weight one. If the exceptional endpoint is exactly {u}β with β of weight two, its unique henselian point lift has weight three after multiplication by the unit. The residual endpoint error has weight one, so (ψ²−2)/6 kills the error and fixes the desired product. This is a polynomial used on the actual family and its two endpoint summands; no global spectral projector or semisimplicity is required.

## Fresh primary-source reads

Freshly opened and read the complete displayed statements and proofs of:

- The Stacks Project Authors (2026), Lemma31.19.9, Tag062Y, including part(3) and its comparison of the local principal generators: https://stacks.math.columbia.edu/tag/062Y .
- The Stacks Project Authors (2026), Lemma37.44.1, Tag02LS, all four equivalent finiteness conditions and the displayed descent proof: https://stacks.math.columbia.edu/tag/02LS .
- The Stacks Project Authors (2026), Lemma37.44.2, Tag02UP, entire proper/finite-closed-fibre proof: https://stacks.math.columbia.edu/tag/02UP .

Retrievals turn877337893view0–2. The supporting flatness/algebra and Zariski Main foundations cited on those pages were not all reopened. The semilocal rank-one proof is explicitly reconstructed above. FF's KST/GH/TT source proofs and the Weibel unit/product Adams proofs are reused from their stated earlier audits; this receipt does not claim new complete external reads of them.

## Boundary retained

The argument uses the original local R and proper curve P. It neither applies unchanged to R tensor_k k(u) nor extends a K1 automorphism from a nonproper open by coherent closure. NK.10 assumes the exceptional endpoint exactly, not merely its componentwise image. Therefore neither the symbolic-unit specialization nor the remaining C.3bt component quotient is settled by this theorem.

Receipt saved: 2026-11-19T20:12:00.811600+00:00
