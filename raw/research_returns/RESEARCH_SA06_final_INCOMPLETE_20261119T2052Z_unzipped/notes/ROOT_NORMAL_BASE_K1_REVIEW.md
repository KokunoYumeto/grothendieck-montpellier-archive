# Root independent audit of C.3bv

**Mathematical PASS in the stated fixed local-base scope; auxiliary only.** Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode; /root; effort setting not separately exposed. No priority claim. Audit completed 19 November 2026, 20:08–20:22 UTC.

We read the entire research proof `agents/frobenius/C3_normal_base_K1_family_RESEARCH.md`, SHA256 `72496a0cbf47d83d3796cd7ff3a6e186b5268830e31c0bc9f96337c7341b38a4`, and independently reconstructed NK.1–NK.10, including the residue-zero condition in NK.9a. At 20:20 UTC we read the entire final TeX, SHA256 `7aa938a79c885b669f2df35f5671aeea8bae3191d4c2c37892abc2c86b766336`. Its transfer is faithful. We also read both complete independent peer receipts, from cycles and component_families; those reads do not substitute for our reconstruction.

For any noetherian local coefficient-k algebra R with algebraically closed residue field k, the incidence argument on the closed proper curve supplies a nowhere-zero section of every sufficiently twisted vector bundle of rank at least two. The zero locus on the actual product is proper over R, so its missing the closed fibre makes it empty everywhere. The resulting line filtration proves additive line generation in perfect K0. The proof uses actual sections on the original product, not only sections after completion.

The two Cartier zero schemes representing a line difference are finite over R. Their rings are semilocal, so all line restrictions are trivial. The precise Cartier identity, with the positive and negative twists cancelled on these supports, gives `[M]-1=[O_D+]-[O_D-]`. The projection formula then kills its product with every line difference. Rank and determinant are inverse on these generators, and the gamma-series expansion proves the integral F_gamma^2 bound, not merely a rational filtration assertion.

For a proper integral birational modification of a normal domain, the height-one valuation criterion gives g_*O=O. Field-flat base change of a finite affine Cech equalizer proves this on the product with the proper curve. The invertible-sheaf projection formula gives Picard injectivity. Rank and determinant on the source alone therefore give the required K0 injection. The characteristic-p fixed-product abstract-blow-up exact sequence then lifts the entire prescribed K1 class after inverting p; its parameter summand is absorbed by actual pullback to the modification.

At a point, exactness must be applied to `(a,0)`. Its preimage is a local unit with zero residue, not an arbitrary local unit. Stable elementary reduction over a commutative local ring identifies K1 with the units, so the kernel has Adams weight one. Multiplying a weight-two class by a constant unit has weight three. The actual-family operation `(psi^2-2)/6` therefore kills the kernel discrepancy and preserves the desired literal endpoint. No semisimplicity assertion for the singular group's entire K-theory is used.

Fresh primary reads by root at 20:08 UTC: complete printed proofs of Stacks Lemma31.19.9, Tag062Y; Lemma37.44.2, Tag02UP; and Lemma37.44.1, Tag02LS. We independently supplied the elementary semilocal argument; the cited Tag02M9 has proof hints, not a full printed proof. The previously completed AE/WP/FF and KST/GH/TT audits are reused at their recorded scopes. The owner's later fresh Weibel III Lemma1.4 proof read is accurately attributed to the owner. Root freshly reread Weibel IV Theorem5.9 with its complete displayed proof and Example5.9.1 at 20:21 UTC. We do not claim a fresh complete rereading of every foundational source.

The scalar extension R tensor_k k(u) is generally nonlocal. Neither the closed-fibre generation proof nor henselian descent applies to it without another argument. The theorem also starts from an exact exceptional endpoint and does not turn a merely componentwise endpoint into an exact one. It is an auxiliary strengthening; UK.7 and every main-row status remain unchanged.

## References and exact scopes

The Stacks Project Authors. (2026). *Relative effective Cartier divisors*, Lemma31.19.9. https://stacks.math.columbia.edu/tag/062Y

The Stacks Project Authors. (2026). *Applications of Zariski's Main Theorem, I*, Lemmas37.44.1–37.44.2. https://stacks.math.columbia.edu/tag/02LS ; https://stacks.math.columbia.edu/tag/02UP

Weibel, C. A. (2013). *The K-book: An introduction to algebraic K-theory*. American Mathematical Society. ChapterIV, Theorem5.9 and Example5.9.1. https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf
