# Root audit after checkpoint 11

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), `/root`, on 19 November 2026. No priority is claimed. This note records the proof and source checks behind the current production additions. It performs no progress review and creates no checkpoint.

## The new elliptic statements

Root read the complete work drafts and integrated A.4.36–A.4.40. The five elliptic work programs and the formal-graph coefficient program were read before their production copies were run. Their mathematical scope is recorded in `COMPUTATION_RECORD.tsv`.

For A.4.36, the actual isomorphism is `Sym²(V)⊗det(V)⁻¹ → sl(V)`, sending `T` to `TJ`. Its comparison identity is `(PTPᵀ/det P)J=P(TJ)P⁻¹`. Substituting the actual rectangular period matrix yields the specified projector and the projective Betti ratio `−τ²`. Root checked the conjugate universal-extension map on both actual period generators, its determinant `−1`, and its conjugate involution. Its nonzero vertical-to-elliptic derivative is the precise obstruction to an algebraic group map.

For A.4.37, root checked the second-kind pullback as an equality of de Rham classes, the corresponding Lie-coordinate map, and the difference identity after fixing the stated embedding into `C_p`. The connected-depth factorization gives differential valuation `m`; the integral ordinary line then gives the exact negative valuation `max(0,2m−n−b)`. The primitive cyclic-line counts exhaust the actual subgroups. Their parity sums and the finite-index orbit inequality are exact. Root reopened Lombardo's final 2015 source at the restatement on p.2348 and Corollary 9.3 on p.2393. These are local Néron-frame norms; the result does not identify them with a global height.

For A.4.38, root checked all dimensions of a proper connected algebraic subgroup in the actual product `E†×conjugate(E)`. An elliptic subgroup projecting nontrivially to `E†` would split its nonzero extension after isogeny; injectivity of pullback on `H¹(O)` excludes it. The two-dimensional subgroup case uses the same pullback obstruction. The rank in Waldschmidt's theorem is the rank after exponentiation, with period rank retained separately. The two periods alone meet the theorem's numerical conclusion.

For A.4.39, root checked the complete-elliptic-integral parameter convention, all four period/quasiperiod formulas, the Wronskian and the exact second-jet identity. The joint exclusion of algebraic `h,c` proves that the first two normalized jets cannot both be algebraic. The logarithmic family has value `1` and derivative `4M` at the actual ordinary point `1/(4M)`, inside its convergence disc. None of these statements decides the first jet of the fixed non-CM curve.

For A.4.40, root read the original Bost–Chambert-Loir version 3, Theorem 3.1(b), Proposition 3.5(2), Proposition 3.6 and Definition 3.7, printed pp.10–13. The positive local convergence radius and the unit linear coefficient required by Proposition 3.5(2) are supplied respectively by the nonsingular differential equation and the integral determinant-one shear. Root independently checked that the bad inverse coefficient cannot enter the graph coefficient through its zero linear term. Thus the degree-`p` graph coefficient has exactly one factor of `p` in its denominator at every transverse restricted-Lie failure. The source's lower bound then proves the exact local size.

Root also read André's original publisher preview: normalization and Lemma 5.1.1 on pp.70–71, the series coefficient invariant on p.74, and Theorem 5.4.3 on p.76. The infimum, upper limit and sum occur in the order written in A.4.40. Partial summation converts the weighted upper harmonic density from A.4.32 into the stated lower bound for this coefficient invariant. No lower-density statement and no equality with a connection invariant are used. The finite-place size product is zero and the coefficient invariant is positive for the actual fixed graph, including the established CM coefficients.

## Proper completion and the actual cusp conjugator

E.2.30 was integrated after root's independent re-proof of the actual proper-homology quotient system, all-cover lattice formula, self-normalizers and one compatible conjugator. The coordinate solutions form the specified left-action orbit; surjective transition maps give a single profinite element. The mixed-sign peripheral exponent proves the strict inclusion of the affine completion in the proper completion. It supplies no arithmetic automorphism.

For E.2.31, root read the full text and finite certificate. The actual degree map of compactified covers agrees with the quotient map on their homology kernels. Oriented Poincaré duality gives an integral umkehr even for branched covers, and its composition with pushforward is multiplication by the covering degree. These maps are equivariant for the actual deck generator. Smith normal form identifies completed fixed spaces with completed invariant lattices. The transition maps on the specified subsets are onto; no assertion that those subsets are subgroups is needed.

The regular `A₅` cover has inertia orders `(3,5,5)` and genus nine. The order-five quotient has genus one. The exact class `v` is invariant and is detected by the integral functional `q` with value `540`. The specified scalar with 2-adic component zero and every odd component one makes `av` nonintegral. The shortlex recursion and integral transfers give one compatible element of the original full free profinite group. Root reopened the original Bux–Ershov–Rapinchuk article, Corollary 2.3 on p.332, and read its relation-module proof. This identifies the entire cusp centralizer. The construction still supplies neither the full peripheral automorphism nor the required arithmetic Galois membership.

## Cycle-theorem scope and correction of an omission

F.3.35 was checked against the original Broe preprint, including its fourfold statements and the actual specialization direction. Root checked the explicit auxiliary elliptic curves in both characteristic cases, the projection and zero-section identities, correspondence codimension, matrix Hom spaces and projector lift. The arbitrary-characteristic result supplies the indicated dimension bound. It does not establish a fixed-frame Mumford–Tate equality.

The direct primary arXiv record of Li's manuscript states that it was withdrawn on 8 October 2026. The earlier all-powers abstract was not used. The retrieval script and exact HTTP records are retained in `work/code_root/`.

F.3.36 repairs the omission of the full established characteristic-zero range. Root obtained the complete original Kleiman 1968 PDF from Mainz, 28 pages, SHA-256 `e96e2465e0fb3a05084cc7472e6edec44a4cff920b199b271caed9251cab825a`. Theorem 2A11 on p.377 and Proposition 3.8, Corollary 3.9 and Remark 3.10 on p.380 were read and visually inspected. The last statement explicitly covers every complex abelian variety and every smooth projective complex variety of dimension at most four. Original Kleiman 1994 Proposition 5-1, p.17, was also reopened and visually inspected.

Root checked the finite-extension degree factor and the flat-family refined-intersection argument extending numerical triviality from the actual base field to `C`. The identity on every product's cycle classes then identifies all Hom spaces, including arbitrary tensor products, twists and projectors in the abelian category. The two relevant canonical rows remain OPEN for their general all-smooth-projective obligations; their proved scope and dependencies have been expanded.

Lieberman's separate 1968 article was not obtained as an original full text. Both the web and direct JSTOR PDF requests returned HTML. The direct request was HTTP 200 but had content type `text/html`, 3038 bytes. F.3.36 uses the opened original Kleiman statement. This failed access is explicitly recorded in the bibliography and literature record.

## Recheck of the previously completed normalizer bridge

Root reread the actual normalizer-to-cover maps in F.3.31 and F.3.33 and the original Nakamura 1996 printed pp.115–117. The degree-six rank sandwich has both endpoints one. Lemma 4.5 concerns the actual fibre-image map and records invariance under finite base extension. Equations 4.7.1–4.7.2 identify the geometric kernel, universal arithmetic quotient and actual fibre inclusion. These are the maps used for the nonzero derivation on the chosen finite cover. The full-logarithm inner correction preserves the specified nonzero homology class. This check retains the conclusion credited at actual review 06; it is not new progress.

## Integration, typesetting and retained dispositions

Seven newly registered programs passed their isolated production runs. There are now 55 registered programs. Their external wall times were respectively 1.144721, 1.281022, 1.357077, 0.140017, 1.071052, 1.091305 and 0.925650 seconds in the order recorded in the integration script. General proofs remain separate from the finite certificates.

The first integration build stopped on an unescaped underscore in a bibliography filename. Escaping the two underscores repaired it. The first completed build had two overflows, 39.89973pt in a list of program filenames and 19.16591pt in a hash paragraph; the earlier interrupted build had the unbroken hash overflow of 198.23315pt. Breakable filename paths and two displayed hash rows repaired those lines. Final log, page, visual and hash checks are recorded separately in `code/checkpoint12_qa.json` after inspection.

The new duplicate bibliography key `EllBakkerPilaTsimerman2026Jets` was removed in favor of the already retained `EllBakkerPilaTsimerman2026`. The corresponding agent note now labels the new jet calculation as a continuation of its earlier source audit; its initial description as a fresh source was corrected. No mathematical passage or source access was discarded by this consolidation. The earlier preprint record remains separately identified by its edition and pagination.

The four work TeX snippets under `work/elliptic_tex_next/` are now explicitly included by both packaging programs. Their production counterparts contain the current integrated proofs. Original retrieved sources, supplied material and temporary inspection images remain outside the checkpoint archives as requested.

All main unresolved gates retain their quantified premises. These proof additions, source-scope corrections and verification records do not constitute an hourly progress review. The next actual review is due at 12:55 UTC, and checkpoint 12 is due at 12:55:12 UTC.
