# Independent proof review by the formulas worker

Run: `GCT_KRON_20261120`. Reviewer: `/root/positive_formulas`, GPT-6 Astra Pro; effort setting is not exposed. Review completed on 21 November 2026, Europe/Berlin time. The companion TSV records the actual event times. The snapshot hashes identify the files read.

This review reads the complete proofs in `proofs/root_findings.tex`, `proofs/projection_bound.tex`, and `agents/obstructions/obstructions_findings.tex`. It is a targeted proof check, not a claim to have independently re-proved every cited theorem or rerun computational bases in the literature. Each proof below was read in full. The precise new arguments were checked from their definitions; the dependencies on established results remain explicit. No unresolved mathematical gap was found in these versions.

## Root findings

### M-001: signed orbit formula

The Jacobi–Trudi permutation has the correct margin `lambda_i-i+pi(i)`. Negative margins contribute zero, and the sum of each margin remains the common degree. Triple intersection cardinalities classify the diagonal symmetric-group orbits: disjoint bijections of the cells give a permutation and every admissible table can be realized. Self-duality identifies the tensor invariant with the Kronecker coefficient. The empty partition at degree zero is compatible with the conventions. This is a signed expression, and the text correctly makes no cancellation-free or binary polynomial-time claim.

### M-003: rational gamma filtration

The rational class `e=[C[G]]/|G|` is the idempotent with character supported at the identity. Thus the augmentation ideal after rationalization is the idempotent ideal `(1-e)R_Q`, so every positive power equals that ideal. The two containments `I^r ⊆ F_gamma^r ⊆ I` follow respectively from `gamma^1(x)=x` and the rank-zero condition on all positive gamma operations. Rationalization is flat, so the associated graded positive pieces vanish. This proves only the stated rational result. No integral vanishing or assertion about arbitrary scheme K-groups follows or is claimed.

### M-004: invariant scheme and base change

The integer span of all group translates of a rational basis is a finite free full stable lattice. Adjacent-transposition equations are equivalent to all invariance equations, including the case `N=1` with no equations. Localization identifies the rational kernel with the desired invariant space. After inverting `N!`, the Reynolds projector is an idempotent over every base algebra, so its image is finite projective and commutes with arbitrary, not merely flat, base change. Connectedness of the base fixes its rank. The statement correctly separates finite étaleness of the constant group scheme from linear reductivity at bad primes.

### M-005: Artin sign

Geometric Frobenius swaps the two geometric points of the quadratic finite extension. Its eigenvalues are `1,-1`, so the exterior square has trace `-1` and weight zero. The rational Artin idempotents exist after division by two. This is a genuine counterexample to an inference from purity to nonnegative traces, with no reliance on a conjectural general motivic category.

### Dictionary paragraphs

The three products—induction across symmetric-group degrees, internal tensor product in a fixed degree, and coherent-sheaf multiplication—remain distinguished. The lattice/projector statements are only semisimple after the indicated localization or characteristic-zero base change. Contracting a rational homogeneous ideal to a polynomial ring over the integers gives a torsion-free quotient and therefore a flat integral model; special fibers are not identified with orbit closures. The Adams-operation interpretation does not imply positivity in the irreducible basis. These qualifications are mathematically necessary and present.

## Projection and determinant findings

### M-006: comparison of all multiplicity copies

The decomposition of `Sym^d Sym^n V` is natural in linear maps, with a common multiplicity factor `M_lambda`. For a partition with at most `r` rows, `S_lambda U` is nonzero. Every element of `S_lambda U ⊗ J_X,lambda` vanishes on `Y` because its evaluation factors through the projection and the projected variety lies in `X`. Reducedness over the algebraically closed ground field turns pointwise vanishing into ideal membership. Taking the general-linear-group span gives the entire `S_lambda V ⊗ J_X,lambda`, hence the inclusion of multiplicity subspaces. The direction of the quotient multiplicity inequality is correct. This compares all copies and does not assume containment of `Y` in `X`.

The equivalent highest-weight explanation is sound: nonnegative polynomial weights with zero coordinates outside `U` can use no tensor coordinates outside `U`. The full proof already follows from the natural Schur decomposition, so no choice of Borel affects the conclusion.

### M-007: balanced two-trie determinant

The prefix and suffix vertices are disjoint except for their roots. The unique-parent rule on multi-indices gives precisely one prefix path and one suffix path for each monomial. A non-loop cycle must meet the central vertex, because prefix edges point away from it, suffix edges toward it, and every coefficient edge goes from prefix to suffix. A simple cycle contains exactly one coefficient edge. Therefore a cycle cover contains either the central loop or exactly one such nontrivial cycle, with loops everywhere else.

For total monomial degree `k`, the cycle has length `k+1`; its permutation sign and the `k` negative variable labels cancel. The coefficient edge contributes one `L` and the unused loops contribute `S-k-1`, giving `L^(S-k)`. The central loop gives the same formula at `k=0`. Summation proves the universal identity `det M=L^(S-m)f` over the integers in the coefficient variables. The count `S=binom(m+p,p)+binom(m+q,q)-1` is exact, and `S≥m+1` for `r≥2`. The zero padding form, one-variable form, and degree-one cases are handled separately in the text.

The computational check is supplementary to this proof. `check_balanced_determinant.py` produces five exact symbolic zero-residual identities (three with independent coefficient symbols; two with fixed signed coefficients and symbolic variables), followed by twenty exact integer evaluations, including padding value zero. The results are in `balanced_determinant_certificate.json`. These finite computations do not substitute for the all-parameter cycle argument.

### M-008: actual multiplicity bounds

An `r`-variable restriction of a translated padded permanent has the claimed form `L^(n-m)f`. The zero case is zero because `n>m`. A linear matrix pencil is an endomorphism substitution into the determinant, and density of the invertible endomorphisms places its image in the determinant orbit closure. Closedness extends the projection containment from the orbit to its closure. Consequently M-006 applies to the actual coordinate rings, with no replacement of closure multiplicities by ordinary Kronecker coefficients.

The ratio `2 binom(m+c,c)/m^c` decreases with positive `m`, and its value at `m=2` is `(c+1)(c+2)/2^c`. This is less than one for `c≥6`, and at `c=4` it is `15/8<3`. Thus the stated row exclusions, nine rows in the Ikenmeyer–Panova numerical range and fifty-one rows in the Bürgisser–Ikenmeyer–Panova range, follow. The ambient tensor-power/Pieri argument bounds row length by degree `d`, giving the corresponding lower degree bounds. The separate inequality `d>n/m` is correctly reserved for the stronger sufficient test `q>g`.

## Obstruction findings

### O-001 and O-002

For O-001 all six imported vanishing conditions are homogeneous except for the explicit parity and exceptional residue conditions. Stretching twice clears the three parity conditions. The exceptional pair would require the unstretched pair to be `{0,1}`, impossible because both column counts have the common-size parity. This proves factor two throughout the stated `2×2×4` family, not factor-one saturation. The smaller three-two-row interval gives exactly the stated boundary parity holes.

For O-002 the second row is `t`, and the rectangle width `td` is at least `t`; the width constraint therefore disappears at both required partition coefficients. Removing the part of size one gives exactly the displayed generating series. The positive support is the even integers at height two and all integers at least two at larger heights. The ambient-hook vanishing prevents these coarse padded shapes from being misidentified as actual occurrence candidates.

### O-003

Restriction to diagonal traceless matrices is injective on invariant polynomials by density of the distinct-eigenvalue locus. Symmetric polynomials modulo the trace relation yield the freely generated coefficient algebra. Averaging justifies passage to the quotient in characteristic zero. The trace pairing and the explicitly stated stable-width hypothesis connect its Hilbert series to the rectangular coefficient. The grading has nonsaturated support even though the underlying algebra is polynomial and its ordinary affine-space cohomology is pure Tate. The text correctly distinguishes this graded-support example from the normal semigroup-algebra theorem.

### O-004

The import from IP Proposition 5.2 is for every integer stretch greater than one, not just even stretches. Monotonicity followed by stability gives positivity for each stretched-column tail. Rowwise summation of the columns then uses the ordinary Kronecker semigroup property and passage to a common stable width. The final inequality `td≥|t rho|` is exactly the stability condition. The asserted shape is valid since `h≥7` and `d≥|rho|`. The statement does not claim positivity outside this stable-tail range. Published finite computational base cases in the imported proposition have not been rerun by this review.

### O-005

For the permutation module on `s` points, exterior invariants vanish in degree at least two because a transposition inside the chosen subset changes its orientation. Dividing the exterior-series identity by the trivial line removes the remaining positive-degree invariant. Under the base subgroup of the wreath product, only the block-constant augmentation exterior algebra remains; the top symmetric group removes its positive degrees. The cases with one block or singleton blocks reduce directly to the same calculation. Schur–Weyl invariants then give the ambient hook vanishing and hence the permanent-side vanishing.

The additional near-hook criterion and length restriction agree with Giannelli's exact stated results. Their source statements, rather than the full proof of Theorem 1.2, were rechecked.

### O-006 and O-007

The subspace criterion is natural on each Schur summand. Restriction onto a nonzero `S_lambda U` forces the ideal multiplicity subspace to vanish, so it preserves every ambient copy. Every binary form is a product of linear factors and hence a diagonal determinant. Binary weight multiplicities are the rectangle partition numbers, and their consecutive difference agrees with the rectangular Kronecker coefficient. The inequality chain then gives all four equalities in O-006.b.

For O-007 the genus-zero bundle is the degree-minus-one line bundle on the smooth conic, and for positive genus the effective degree-`g-1` classes form a proper subset of the Picard variety. Beauville Proposition 3.1(a) yields a linear determinant for every smooth ternary form. Smooth forms are dense and the orbit closure is closed, so all ternary forms lie in the closure. Applying the subspace criterion gives the asserted three-row equality; no equality with ordinary rectangular Kronecker coefficients is inferred.

### O-008

The restriction morphism sends the full endomorphism-substitution image to the four-variable determinant image. Continuity and closedness therefore give `Omega ∩ L = D_U`, including points on the orbit boundary. On a dense open parameter set, diagonalizing the second normalized matrix and normalizing `n-1` entries of the third yields the parameter count `2n²+2`. Finite choices of ordered eigenvalues do not affect the dimension bound. The image of this dense open set is dense in the image closure, so the bound applies to the entire closed locus, not just its generic image.

The ambient dimension exceeds that bound for every `n≥4`. Pulling back a nonzero homogeneous equation yields a nonzero ideal vector supported on at most four-row isotypic components. Stability of the ideal under the group and O-007 remove the components with at most three rows, leaving an exactly four-row component. This is an ambient multiplicity loss, not an actual permanent obstruction.

### O-009

The contradiction proof uses ambient positivity to invoke IP Corollary 1.9 if `g=0`. The resulting degree inequality supplies `d>3m³`. IP Theorem 1.10(a) excludes the six exceptional tails and part (b) then applies with all its strict and weak inequalities as stated. Thus ambient positivity really is enough for the stated nonvanishing variant; no permanent coordinate-ring membership is used.

### O-010

The same generic gauge works for every `r≥3`, leaving `r-3` unrestricted matrices and yielding `(r-2)n²+2` parameters. The case `n=1` has the exact same dimension bound directly. Multiplication by a fixed nonzero padding power is injective, so the full padded-form family has dimension `binom(m+r-1,r-1)`. Containment forces the displayed inequality. Substituting `n=m^c` and comparing polynomial degrees proves `r≤2c+1` for fixed `r` and all sufficiently large `m`.

Together with M-007 this proves that, for `c≥6`, `2c+1` is the optimal asymptotic fixed-variable threshold for this universal-form containment method. It does not give a limitation on methods exploiting the much smaller family of projected permanents. In particular it does not claim that a specific projected permanent lies outside the determinant closure in fifty-two variables.

## Distinction between the two multiplicity tests

The actual obstruction is `q_lambda > K_n(lambda)`. The sufficient test `q_lambda > g(lambda,(d^n),(d^n))` is stronger because `K_n ≤ sk ≤ g`. Therefore failure of the sufficient test alone cannot exclude actual obstructions. O-006 and O-007 exclude actual obstructions because `K_n` equals the full ambient multiplicity; M-006–M-008 do so more broadly by comparing the two actual coordinate rings directly. O-008 only records a loss from the ambient algebra. O-009 only proves positive `g`. The documents preserve all these distinctions.

## Primary sources independently reopened during this review

- Beauville, *Determinantal Hypersurfaces*, author-hosted published PDF: <https://math.univ-cotedazur.fr/u/beauvill/pubs/det.pdf>. Proposition 3.1(a) and paragraph 3.2 are printed page 46, PDF page 8. The statement gives the exact linear resolution used in O-007.
- Giannelli, *On the decomposition of the Foulkes module*, <https://arxiv.org/pdf/1207.6300>. Theorem 1.1 is page 1; Theorem 1.2 is page 2; Proposition 2.7 is page 3. The parameter substitutions in O-005 agree with these statements.

These reopened sources supplement the formula worker's earlier exact-locator checks of the supplied IP source, GCT IV vanishing conditions, Macdonald's functorial Schur decomposition, and the classical rectangular/two-row formula. They do not upgrade imported published proofs to independently re-proved findings.

## Later complete-proof reviews

### M-009: highest-weight box truncation

Read the complete proof in `proofs/weight_box_bound.tex`. For the stated upper Borel, the explicit first-row unipotent matrix sends the padding linear form to a scalar multiple of the first coordinate under the dual action. A highest-weight polynomial is unchanged by that unipotent action. Its coefficient monomials have total nonnegative multidegree lambda, so deleting coefficients outside the individual tail bounds preserves its evaluation exactly. The capped trie sets are downward closed. Their cycle identity is correctly written term by term when the number of vertices is smaller than m. Generic nonzero first padding coordinate is a nonempty open condition on the irreducible group parameter space, so vanishing extends to the whole orbit closure. Inclusion of every highest-weight copy gives the stated inclusion of multiplicity subspaces. No gap found.

### O-011: Hessian multiplicity-one family

Read the complete proof in `agents/obstructions/hessian_family.tex`. The upper-triangular chain rule gives exactly the claimed character. The determinant Hessian is nondegenerate at the identity, and its radial vector has nonzero square. I recomputed the inverse Gram entries for the permanent Hessian rank-two update and expanded its 2×2 determinant, obtaining the displayed factor `(m+s−1)/(m−1) · (1−(m²−3m+1)s)`.

For the exceptional internally padded `(m,n)=(3,4)` case, I checked the Hessian blocks at `X11=2`, all other entries one, directly from the six permanent monomials. The 4×4 block has an antisymmetric eigenvalue −4 and complementary 3×3 determinant −144, giving determinant 576. Each 2×2 sign block has determinant −8 and the remaining scalar is 4; their product is 147456. The padded form value is 16. The nondegenerate-subspace argument applies in every dimension up to m², and the internal-padding length bound eliminates larger d. Thus the proof covers every `n>m`, including `(3,4)`, with no unresolved exceptional case.

### O-012: degree splitting and all-copy padding

Read all four complete proofs in `padding_full_multiplicity.tex`. In the graph, the two copies of the same-variable monomial tree are distinct except at the roots. The variable removed from a top-degree monomial is placed on its coefficient edge; consequently the cycle loses one tree edge and its determinant sign still cancels exactly. The `b=1` central-loop case is included. For padding, the highest-weight lift is Borel equivariant up to a character, but the actual restriction map is its differential transpose. Their composition has the nonzero factorial diagonal stated in the proof. This suffices for independence of every lifted copy without falsely equating the maps.

The last-row rectangle removal uses the irreducibility of the Cauchy column module to justify divisibility of every vector by the determinant power. The residual total lower-row degree bounds each column separately; division and inverse multiplication commute with column permutations, retaining the sign twist. All endpoint and partition checks pass. The four-copy example has precisely the partition difference four. F-014 subsequently strengthens the base-degree bound, but does not invalidate this specialization.

### O-013 and O-014: all-degree Hessians and a bounded coefficient space

Read `hessian_all_degrees.tex` in full. Upper triangular congruence has a dense open orbit on quadratic forms with all leading principal minors nonzero. Ratios of two polynomial highest-weight functions of the same character are constant there, so each multiplicity is at most one. The stated Hessian product realizes the relevant even partition and survives on both orbits in the claimed ranges. The cases `r=1`, `r=d`, and the exact `m²` length endpoint are covered.

Read `boxed_degree_split.tex` in full, along with its script and saved arithmetic certificate. Restricting the two degree-split trees to the coefficient box preserves every root path and every chosen split. Both the positive-permanent function and the ambient four-dimensional seed multiplier have the claimed degree and weight, and multiplication in the ambient domain preserves four copies. The exact `m=256` example lies below the Grenet size, above `m^25`, below the uncapped graph size, and below the stated lower bounds for the older box-variable counts. Two wording corrections were requested and applied: entries are linear in the form variables, with polynomial coefficient dependence; the restricted coefficient space is only torus-stable, so its restriction map is not called generally Borel equivariant. The later upgrade from positive permanent multiplicity to at least four uses M-012, independently checked below.

### M-011: a cut in terminal support

Read `nested_tail_bound.tex` in full. The complete flag-minor span gives the terminal-row inequality for each column monomial; disjoint column-permutation orbit sums transfer it to each coefficient generator. Alignment, deletion of unsupported degree-m monomials, and the variable-split determinant preserve the value of every highest-weight vector in the determinant ideal. The termwise exponent argument remains polynomial when the graph has fewer vertices than m. Density then gives the inclusion of the entire ideal multiplicity space.

The IP and BIP inequalities have the correct binomial parameters, including the slack variable. The general exponent-c consequence uses the factorial bound with each numerator at most r and `floor(c/2)≥3`; its small endpoint c=6 is valid. The proof never assumes `n≥lambda2`. A harmless scope clarification was suggested: first discard `q=0`, so the positive case explicitly has `r≤m²<n²` before choosing the coordinate subspace.

### M-012: binary permanent containment and several surviving copies

Read `binary_permanent_seed.tex` in full. In the sparse permanent matrix the last-row column forces all other choices, giving the displayed sum. Its distinguished entry is exactly L, so internal padding is preserved. The endomorphism-substitution image is contained in the orbit closure by density of invertible endomorphisms. The padding inequality and second-row stabilization identify all two-row copies up to second row m, not only one nonzero class.

At second row six and degree six the partition difference is four. The higher-row multiplier has degree `d−6`, second-row increment `b−6`, and the stated later rows. A single Hessian point admits a basis in which all needed leading minors and the first coefficient are nonzero. The closure is irreducible and reduced, so its coordinate ring is a domain and multiplication preserves the independence of the four seed classes. The first-row partition inequality and all nonnegative exponents check. The higher-row paragraph should explicitly retain `n>m≥6`, as in the section hypotheses.

### O-015: arbitrary downward-closed supports

Read `nested_support_graphs.tex` in full. Coordinate projections of a downward-closed set agree with its zero-extended coordinate sections, and the split or removed-variable endpoints stay in the set. The cycle-size proof handles `b=1`, the zero support, and graph size smaller than b. The terminal-sum counts and the `b+binom(r,2)` bound for a later tail of twos are exact as stated. In the strict example, `m=256`, `n=2^200`, `d=3n`, `b=2n`; the matrix size is `256+binom(65536,2)=2147451136`. The four-copy multiplier has degree `3n−6` and the stated weight. Its second row exceeds n, so all stabilization-based full-equality criteria are genuinely unavailable, whereas the degree-m comparison applies. The adaptive threshold simplifies to `4n²+n−1`, and all other stated comparisons are valid. This is an excluded actual multiplicity-four family, not an obstruction.

### M-013: compressed-tree Taylor-jet dominance

Read `jet_dominance.tex` in full. Each inward-to-outward path is unique after its bridge is fixed, so the stated inverse entry is a single monomial, not an uncontrolled sum. The entries span every degree through `2ell+1`; multiplying by a linear entry perturbation gives the whole next-degree jet. The cofactor derivative has the correct transposed inverse entry. The formal lowest-homogeneous-part argument proves dominance without any unstated smoothness assumption on the determinant orbit closure.

The size is at least the jet order and also ensures the variable space fits in `n²`. A highest-weight polynomial with second row at most the jet order depends only on those detected coefficients. Injectivity of the jet-map pullback therefore removes the entire ideal multiplicity space. The uniform ratio is exactly `5/8` at `ell=3,m=2`, decreases thereafter, and handles odd c by jets and even c by the earlier exact degree-split construction. The resulting endpoint `lambda2≥27` at the BIP scale and its combination with F-017 are valid.

The independent computation builds the actual compressed polynomial matrices, checks determinant one and their symbolic inverses, and ranks the cofactor-linear-perturbation coefficient matrices. Five cases give full ranks `6,15,35,70,7`. In the six-by-six example, a directly computed perturbed determinant has derivative `z^6`. These meaningful finite checks are saved in `jet_jacobian_certificate.json`; they supplement rather than replace the all-parameter proof.

### F-019: the known full square of a two-row rectangle

Read `agents/archive/rectangle_square_known.tex` in full and independently read the supplied GCT IV notation definition at line 1535, the BWZ positive sum at lines 7778–7784, and the following proposition. The constant coefficient has exactly the first sum's `j=0` term and no term from the second sum. Its three even-difference conditions are precisely equality of the four padded row parities. Schur–Weyl in dimension four handles all longer partitions. Stretching preserves or clears these parity differences exactly as stated. The finding is correctly marked as a known rule, with no new GCT comparison claimed.

Independent exact character inner products for all 159 partitions of `2h`, `1≤h≤6`, agree with the rule, including the smallest rectangle and every longer-than-four-row output. The script and certificate are `check_rectangle_square.py` and `rectangle_square_certificate.json`.


### O-018 and O-019: a strict full-profile improvement and a jet dimension boundary

Read `full_profile_example.tex` in full. The joint condition lambda3 at most 138 and lambda52 at most two has support bounded by `binom(187,49)*m^5`, and the Grenet necessary size m at least 190 makes that at most m^25. The exact integer comparison with `190^20` fixes the stated endpoint. In the strict profile example, the degree and weight of the common Hessian multiplier preserve four independent genuine permanent classes. The support count uses both nested bounds simultaneously. The three ranges of cuts exhaust all possible one-cut enlargements, and each dimension lower bound exceeds the closed pencil-image dimension. This does not claim failure of other determinant architectures or an actual obstruction. The separately cited grouped Chow threshold was used only through its stated formula, not independently re-proved in this event.

Read `jet_dimension_boundary.tex` in full. The target coefficient dimension and closed pencil-image bound give a necessary condition for dominance. Substitution r=m^2 and n=m^c yields the eventual boundary b at most c+1. The exact m=10^15,b=27 example satisfies the claimed strict inequality. The conclusion restricts dominance onto the whole jet target, not ranks on a smaller highest-weight support or an actual permanent multiplicity.

### A-024: a genuinely positive highest-weight algebra in the rectangle-square family

Read `POSITIVE_HW_ALGEBRA.tex` in full. The invariant tensor is the inverse bilinear form, as required for the stated covariant tensor convention. Its Gram principal minors and the four-column volume have the claimed independent highest weights and are nonzero. Cauchy and the verified F-019 rule give multiplicity-free support; every supported highest weight is attained by exactly one nonzero monomial in the four generators. This proves the polynomial highest-weight algebra and its positive monomial basis. The weight lattice has index four in the even-total lattice, and the support is saturated relative to its generated lattice while having ordinary parity holes. The normality proof uses the invariant fraction inside the normal polynomial algebra and does not assert unproved integral splitting or residue-characteristic base change.

### M-013: integral refinement

Read the added endpoint and base-change paragraphs in full. The inequality J_b(r) at least b follows from the monomial-tree count. Every target jet monomial has an elementary source coordinate with derivative exactly that monomial; distinct target monomials can be assigned distinct source coordinates. The selected Jacobian minor is therefore the identity over the integers. Translating the integral base point gives F(t)=t+terms of degree at least two. For a nonzero polynomial over any commutative ring, its lowest nonzero homogeneous part survives substitution, so the pullback remains injective after arbitrary base change. This does not imply an algebraic section, flatness, or semisimplicity outside characteristic zero.

### O-020: transverse binary-plane jets

Read the entire revised `binary_transverse_jets.tex`, including the sharper threshold n at least 2r minus 4. The displayed Walecki paths on 2R vertices have alternating endpoint sums 2j minus 1 and 2j, so they partition the complete graph and provide R edge-disjoint spanning trees. Additional vertices can be attached as leaves with separate original attachment points in each color. The R=1,n=2 endpoint is valid.

The rational-residue map identifies degree n minus 2 binary forms with the zero-sum hyperplane, and edge differences of any tree form a basis. Diagonal pencil variations span all transverse orders zero and one; lower-entry variations opposite colored edges span every quadratic transverse monomial with an arbitrary binary coefficient. Longer paths vanish in the transverse two-jet projection. The source directions are independent coefficient coordinates and the image has all three target summands. Dominance then combines with F-016 terminal support to eliminate every highest-weight ideal copy, with no bound on the second row or outer degree. The characteristic-zero restriction in the Vandermonde step is explicit.
