# Deposit sheet

## Identity

**Title:** Valiant's conjecture after the Anthropic and OpenAI preprints: the Euclidean square as a price, strict shortenings, and the padded permanent

**Subtitle:** Tree prices, strict shortening, and the Hurwitz exponent dichotomy.

**Authors:** left blank for the registry owner, matching the paper.

**Date:** 25 November 2026.

**Subject:** algebraic complexity theory, asymptotic tensor spectra, nonpositive metric curvature, and geometric complexity theory.

**Keywords:** Valiant's conjecture; VP versus VNP; tensor restrictions; spectral prices; real trees; Euclidean square; strict shortening; partial transpose rank; Hurwitz composition; padded permanent; characteristic two; CAT(0) spaces.

**Registry status:** no official work number or permanent paper page assigned. The workbench and permanent-record base addresses are the ones requested by the registry owner. No public deposit, push, or author notification has been made.

## Abstract

The preprints of Claude at Anthropic and of OpenAI claim superpolynomial arithmetic circuit lower bounds over every field through tensor-network identities and spectral geometry. We study their unresolved question of whether a Euclidean square is a price, meaning a limit of scaled spectral wire metrics. Assuming the Anthropic price-space theorem, either every finite price is a tree pseudometric or every finite Euclidean planar metric is a price. Thus any strict violation of the tree four-point rule already answers the square question positively. The square and the square with its centre are equivalent tests. More generally, a Euclidean cross-polytope is a price exactly when every finite configuration in that dimension is a price, and exactly when no strict shortening exists in that dimension. With spectral cover duality, the asymptotic exponent of partial-transpose crossing rank always exists and is either $1$ or $\sqrt2$: the square is a price exactly in the second case. Over the complex numbers the same dichotomy holds for Hurwitz's bilinear sum-of-squares problem, and its exponent can be tested in a Temperley--Lieb centralizer with only a polynomial rank overhead in the number of tensor factors. An elementary weight-block restriction preserves the exponent over every field. Using Strassen duality and the terminal-selector argument of the Anthropic preprint, we prove that every finite failure of the price property has a finite algebraic certificate with a strict length gap. We show that price cones depend only on characteristic and that a finite complex nonprice remains a nonprice in all but finitely many characteristics. We classify the wire metrics of specified spectral families, exclude the ordered crossing-cut quantum expression even after tensor-power regularization, and prove that homogeneous linear inequalities cannot exclude any Euclidean metric. Thus failure of flatness is equivalent to strict shortening, and implies contraction if the Anthropic alternative is granted. Contraction itself is equivalent to the failure of one specified finite square-root-rank metric to be a price. We compare the two direct exponent calculations within their specified accounting rules and give explicit conditional reductions to the padded-permanent problem. The square-price question and the implication from contraction to strict shortening remain open. The mathematics and text were produced by GPT-6 Astra (ChatGPT Pro mode); the recorded checks are by the same model, and no human has checked them.

## Note on method and checking

The mathematics and text were produced by GPT-6 Astra (ChatGPT Pro mode). Separate workers of the same model attacked the main statements from statement-only packets before receiving the author proofs. Their inherited effort setting was not exposed by the system, and is not guessed. The records distinguish those reconstructions from targeted whole-proof comparisons, exact computations, scoped source checks and unverified source claims. No human has checked the paper. The complete Lean developments of the two VP/VNP preprints were not rerun. Our original text and programs are dedicated to the public domain under CC0 1.0.

The source identity and full version identity have distinct, explicit scopes. The paper's printed source-manifest SHA and Git revision identify the editable source. The complete version manifest also covers the generated identity, PDF, proof records, programs and certificates. See workbench/FORMAT_1_PREPARATION.md for the self-reference issue and filing commands.

## The eight opening requirements

| Requirement | Place in the paper | Content supplied |
|---|---|---|
| 1. Title names the question and programme | Title and subtitle, first page | Valiant's conjecture, the two preprints, square prices, strict shortening and padded permanent; subtitle names the tree/exponent results. |
| 2. Abstract starts with the source work and ends with checking status | Abstract, first page | Both preprints' claimed bounds; explicit conditional results and open scope; same-model production/checking and no human check. |
| 3. Each main theorem stated fully, then explained | Section 1, displayed theorems and principal-result paragraphs | Non-tree/planar alternative; square and centre; dimensionwise shortening; exponent dichotomy; complex centralizer criterion; finite certificates, characteristic and GCT results with hypotheses. |
| 4. Why the results matter | Section 1, opening paragraphs and the explanations after the main theorems | The geometric alternative in the circuit claims, the strict-witness simplification, the near-linear versus square-root-two exponent, and the padded-permanent consequence. |
| 5. Credit separated from the present arguments | Section 1, context paragraphs; geometric, duality and crossing section introductions | C3 and A6, selector ideas, classical CAT(0) tangent geometry, Liu's prior sharp branch, Khoruzhii's upper bound, and the conditional exponent-one deduction are identified separately. |
| 6. Earlier and neighbouring work compared by statements | Section 1 and exact source locators throughout | Valiant; Mulmuley–Sohoni; Strassen; quantum/support functionals; operator means; crossing/PT/Hurwitz literature; no-occurrence theorem; current preprints treated as claims. |
| 7. Scope stated beside the conclusions | Abstract, Section 1, and What remains open | Neither square branch is decided; contraction-to-shortening remains open; finite and family-restricted results are not generalized; circuit conclusions are conditional. |
| 8. Prose proof overview before proofs | Section 2, Proof overview | Non-tree tangent limits, tree four-point covers, the exponent gap, normalization and finite certificates, rigidity, field descent, structured matrix searches and GCT reductions. |

## Principal mathematical state

The strongest exact planar gate is now a strict non-tree four-point price. Assuming the price-space theorem, either every finite price is a tree pseudometric or every finite Euclidean planar metric is a price. With cover duality, the crossing exponent limit exists and is 1 or sqrt2, with the square price selecting the latter branch; the complex Hurwitz exponent has the same alternative. These statements have separate same-model reconstructions.

The square over C, the square in characteristic two, higher-dimensional membership, and contraction implying strict shortening remain open. The two-cut operator-mean route requires a uniform lower bound over both grouped tensor powers and arbitrary GHZ factors. A raw determinant witness does not pass those two infima. Fixed algebra barriers and finite decompositions have only their stated scopes.

## Authors and works carried by the paper

This list is for the registry owner to use when deciding whom to notify; no messages have been sent. Names follow the bibliography as written, retaining initials rather than guessing expanded names. All 54 current bibliography entries are represented below; repeated source authors are retained beside the particular works. The two supplied workbench references have no named author in the bibliography, so their notification recipient still needs to be supplied by the owner.

### Proof inputs, reproduced arguments, and explicit construction sources

| Authors or source | Work | Role and scope |
|---|---|---|
| L. G. Valiant | Completeness classes in algebra | Permanent projection completeness used in the conditional circuit-to-permanent transfer; also the underlying complexity question. |
| Claude (Anthropic) | VP ≠ VNP over every field | Price-space and cover-duality inputs, selector and crossing arguments, and conditional circuit consequences. The two main preprint developments were not rerun in Lean. |
| OpenAI | VP and VNP are different | Strict-shortening definitions and accounting; claimed stretch and border-circuit consequences used conditionally. |
| V. Strassen | The asymptotic spectrum of tensors | Asymptotic spectral duality and extension-field invariance; the paper supplies the finite-cover and descent arguments it needs. |
| F. Bruhat and J. Tits | Groupes réductifs sur un corps local: I. Données radicielles valuées | The squared-distance curvature framework used in the price geometry. |
| M. R. Bridson and A. Haefliger | Metric Spaces of Non-Positive Curvature | First variation, completed tangent cones, parallel-set splitting and the classical CAT(0) geometric inputs. |
| I. D. Berg and I. G. Nikolaev | Quasilinearization and curvature of Alexandrov spaces | Quadrilateral comparison and its CAT(0) interpretation. |
| B. Kleiner | The local structure of length spaces with curvature bounded above | Classical geometric-dimension context for the non-tree weak-plane argument; the finite-configuration argument is written out. |
| G. Dragomir and A. Nicas | The quasi-hyperbolicity constant of a metric space | The scale-free quadrilateral constant, its CAT(0) bound, and the precise literature context for the tree/plane threshold. |
| Urs Lang and Viktor Schroeder | Kirszbraun’s theorem and metric spaces of bounded curvature | The Lipschitz-extension input in the cross-polytope filling proof. |
| Stephanie Alexander, Vitali Kapovitch and Anton Petrunin | Alexandrov geometry: foundations | A precisely located form of the Kirszbraun extension theorem used in that proof. |
| T. Haettel, D. Kielak and P. Schwer | The 6-strand braid group is CAT(0) | The modular-lattice orthoscheme result used to realize the subspace and square-root-rank metrics in a CAT(0) space. |
| Matthias Christandl, Péter Vrana and Jeroen Zuiddam | Universal points in the asymptotic spectrum of tensors | Quantum/support definitions and universal points; wire evaluations and ordered crossing-projector tests use these exact definitions. |
| Alonso Botero, Matthias Christandl, Thomas C. Fraser, Itai Leigh and Harold Nieuwboer | On quantum functionals for higher-order tensors | Higher-party limitations and laminar constructions, with their stated hypotheses; the ordered-upper counterexamples are separately proved. |
| Keiya Sakabe, Mahmut Levent Doğan and Michael Walter | Strassen’s support functionals coincide with the quantum functionals | The modern complex support/quantum equality and its effect on the scope of the wire computations. |
| Josh Alman, Baitian Li and Kevin Pratt | The edge of the asymptotic spectrum of tensors | Edge support points, their uniqueness on the relevant three-party boundary, and higher-party extension scope. |
| Avi Wigderson and Jeroen Zuiddam | Asymptotic spectra: theory, applications, and extensions | Spectral extension from subsemirings and the precise single-flattening scope of log-star interpolation. |
| D. Bugár and P. Vrana | Interpolating between Rényi entanglement entropies for arbitrary bipartitions via operator geometric means | Operator means, upper functionals, exact evaluations in their proved range and spectral regularization. Narrow local formula corrections and both unresolved regularization infima are recorded. |
| Péter Vrana and Matthias Christandl | Entanglement distillation from Greenberger–Horne–Zeilinger shares | Graph minimum-cut asymptotic subrank; the four-cycle case is reproved and the general formula is an explicit input to the five-point scale bound. |
| B. Li | Semidirect sums of tensors and the matrix multiplication exponent | The shared-leg untwisting construction examined in the copied-output test; the newly claimed matrix-multiplication exponent is used only in the stated comparison. |
| H. Zhou | Asymptotic rank of weighted graph tensors via completely positive bounds | The external complete-graph rank bound, and the partial-direct-sum construction and entropy inequality reproduced with their structural requirements. |
| B. Rossman and D. Zhu | Multi-quadratic sum-of-squares lower bounds imply VNC1 ≠ VNP | Partial-transpose rank and SOS comparisons. The safe factor-two comparison is proved, and the arbitrary-matrix factor-one qualification is documented. |
| K. Khoruzhii | Crossing decomposition for subquadratic noncommutative circuits | The previously established square-root-of-two upper exponent for crossing decompositions. |
| P. Hrubeš | A subquadratic upper bound on Hurwitz’s problem and related noncommutative polynomials | The Hurwitz upper-bound construction and the full-word parity-correction amplification examined in the paper. |
| Y. Liu | Stretched-exponential circuit lower bounds for the noncommutative permanent and determinant | The prior no-planar-shortening sharp Hurwitz branch and two-hub argument, credited explicitly; stronger circuit claims remain source claims. |
| P. Hrubeš, A. Wigderson and A. Yehudayoff | Non-commutative circuits and the sum-of-squares problem | The all-field central-width reduction used for the conditional noncommutative permanent consequence. |
| Chi Zhang and Haoran Zhu | The Hurwitz sum-of-squares problem depends on the base field | The complex [12,12,18] identity. Its polarized equations and seed spectrum are checked exactly; imported coefficient tables are not bundled. |
| Eric Naslund | The partition rank of a tensor and k-right corners in F_q^n | The earlier crossing problem and its exact identification with the two-cut formulation. |
| Arth Singh | Lower bounds for Naslund’s crossing problem | The all-field linear lower bound is source-proof checked; larger finite bounds and separately pinned Lean results retain their stated non-replay scope. |
| S. J. Berkowitz | On computing the determinant in small parallel time using a small number of processors | The division-free determinant recurrence underlying the paper’s explicit arithmetic-circuit count. |
| P. Bürgisser, C. Ikenmeyer and G. Panova | No occurrence obstructions in geometric complexity theory | The occurrence-obstruction limit, with the distinction from multiplicity and highest-weight separation kept explicit. |
| The Stacks Project Authors | The Stacks Project | Curve normalization and discrete valuation rings; smooth plane-curve genus and Riemann–Roch in the Laurent-approximation and two-point reconstruction proofs. |
| Author not named in the bibliography; supplied workbench manuscript | Border rank at least fifty-two for the four-by-four determinant and permanent | Multiple exterior maps and integral border witnesses, used only with their original party structures and calibrated pure-tensor costs. |
| Author not named in the bibliography; supplied workbench notes | The all-field multidimensional substitution statement; Exact two-dimensional residual minima; A characteristic-free obstruction for the exceptional permanent plane | Residual-subspace, pencil and exceptional-plane statements; the specified finite counts and characteristic-two certificates are separately checked. |
| C. R. Rao | Factorial experiments derivable from combinatorial arrangements of arrays | Credit for the character-moment mechanism behind the coding support bound; the complex-weight operator argument is written out. |
| D. R. Stinson | Bounds for orthogonal arrays with repeated rows | A primary modern statement of the same orthogonal-array moment mechanism and its precise source context. |
| K. Audenaert, B. De Moor, K. G. H. Vollbrecht and R. F. Werner | Asymptotic relative entropy of entanglement for orthogonally invariant states | The local flip–cup projectors and their partial transposes; no positivity-based conclusion is imported into the rank argument. |
| J. S. Christiansen and E. Koelink | Self-adjoint difference operators and classical solutions to the Stieltjes–Wigert moment problem | The bilateral quadratic-weight kernel context; the characteristic-two formal identity and valuation bound are proved separately. |
| V. Strassen | Gaussian elimination is not optimal | The seven integral matrix-multiplication products, used to bound simultaneous rank-metric diameter values over every characteristic. |
| A. R. Calderbank, E. M. Rains, P. W. Shor and N. J. A. Sloane | Quantum error correction via codes over GF(4) | The quaternary MacWilliams transform underlying the exact Hodge/Fourier reformulation; code positivity hypotheses are not assumed. |
| G. I. Lehrer and R. B. Zhang | The second fundamental theorem of invariant theory for the orthogonal group | The classical identification of the full orthogonal centralizer with the image of the Brauer algebra, without a faithfulness assertion. |
| T. Cruz and K. Erdmann | Quasi-hereditary covers of Temperley–Lieb algebras and relative dominant dimension | The dimension-two centralizer identification and exact generator-sign convention used in the TL crossing gate. |
| R. M. Wilson | A diagonal form for the incidence matrices of t-subsets vs. k-subsets | Prior integral rank theory for the special degree blocks; the required binary-power case also receives an elementary proof. |
| E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori and M. Mohammad-Noori | Inclusion matrices and chains | The precise Corollary 3 statement and proof of Wilson’s diagonal form cited beside the exact family computation. |
| L. Manivel | A note on certain Kronecker coefficients | Schur–Weyl identification in the rectangular Specht commutant argument, and the height-two multiplicity-free comparison; the general barrier does not assume that comparison. |
| R. P. Stanley | Irreducible symmetric group characters of rectangular shape | The hook formula used to bound the ranks of nonzero Specht blocks; the entropy and polynomial-factor estimates are written out. |

### Comparison and context only

These works remain relevant to attribution and possible notification, but their inclusion is not a claim that their theorems are needed as unproved inputs to the displayed arguments.

| Authors or source | Work | Role and scope |
|---|---|---|
| K. D. Mulmuley and M. Sohoni | Geometric complexity theory I: An approach to the P vs. NP and related problems | The padded-permanent orbit-closure programme; the elementary padding and circuit reductions used here are proved in the paper. |
| Y. Liu | A uniform exponent bound for asymptotic tensor rank | Neighbouring application of the Anthropic geometry to rank; not a substitute for the paper’s crossing or price arguments. |
| J. M. Landsberg, L. Manivel and N. Ressayre | Hypersurfaces with degenerate duals and the geometric complexity theory program | Established quadratic border-determinantal bound compared with the conditional asymptotic ranges and their different quantifiers. |
| Alexander Lytchak | Euclidean filling inequalities in CAT(0) spaces | A stronger recent variance-rigidity result is compared with the cross-polytope lemma; the supplied classical proof does not depend on that preprint. |
| NIST Digital Library of Mathematical Functions | Chapter 18: Orthogonal polynomials | Distinguishes the quadratic argument of Racah-type polynomials from a quadratic auxiliary grading. |
| C. Albanese and S. Lawi | Poisson kernels as expansions in q-Racah polynomials | The linear-index Poisson-kernel factor is compared with heat eigenvalues; no alternative crossing identity is inferred. |
| E. M. Rains | Quantum shadow enumerators | Shadow-enumerator and positivity context for the Hodge reformulation; no positive-code bound is transferred to arbitrary complex coefficients. |

Exact source locators and scope notes are in the bibliography and the version-root SOURCES.tsv under workbench/work/_pending/v1/. This list does not authorize notifications and makes no claim of priority. External papers, books, scans, source extractions and attached originals are not included in the deliverable.
