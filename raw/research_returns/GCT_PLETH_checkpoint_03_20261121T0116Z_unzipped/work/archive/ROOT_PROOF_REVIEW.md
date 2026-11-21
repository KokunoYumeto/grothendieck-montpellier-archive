# Independent full proof review of root constructions

Reviewer: `/root/archive_audit`, GPT-6 Astra Pro; effort setting not exposed. Reviewed `work/root/root_report.md` in full, including G-001–G-005. This is a human-readable mathematical proof review by a separate agent, not a formal proof-assistant verification.

## G-001: PASS

The degree-one Pieri decomposition is applied in characteristic zero. The multiplication map is equivariant and surjective; its kernel is precisely `S_(4,1)E`. The `(1^5)`-weight source is exactly the five-dimensional permutation representation with the displayed basis, and all basis vectors map to the same nonzero target monomial. Its kernel is the sum-zero representation. Tensoring by determinant shifts each of five highest-weight and torus-weight coordinates by one, while permutation matrices acquire their actual sign determinant. Thus the representation is `sgn⊗U_5`, with no missing twist.

A monomial basis of four vectors does give an action on four lines, hence a homomorphism `A_5→S_4`. The class-size proof of simplicity is correct: none of the proper nontrivial unions with the identity has order dividing 60. A nontrivial homomorphism from the simple group would be injective, which the target's size forbids. The residual diagonal image is abelian and thus trivial, whereas a 3-cycle acts nontrivially on the sum-zero space. This proves failure of every monomial basis, so in particular of one indexed by the four balanced GT patterns. The number four is its computed weight multiplicity, combined with the usual GT-basis interpretation.

## G-002: PASS

All Specht action matrices in the integral standard polytabloid basis are integral. Over Q, averaging has image the invariant subspace without any orthogonality assumption. The grid conventions are consistent: `H` first symmetrizes the `n` entries within each of `m` rows and then the rows; `K` symmetrizes the transposed column arrangement. Thus the named normalized map is the actual composition of row averaging, inclusion into the full tensor space, and column projection. Its multiplicity map is `P_K|_[λ]^H`, and its image equals that of `P_KP_H`. Scaling to `A_KA_H` changes no rational rank.

The determinant identity follows from principal-minor expansion and Cauchy–Binet. The coefficient of degree `j` is a sum over a pair of `j`-element index sets of squared integer minors. Over R/Q this coefficient is positive exactly when at least one such minor is nonzero. Therefore the highest nonzero coefficient is exactly the rank. No invariant positive-definite form on the Specht lattice was silently assumed. The formulation makes no unproved complexity or efficient-positive-formula inference.

## G-003: PASS

### Integral part

Write `F=E∨`. The affine scheme underlying `SymⁿE` has coordinate algebra `Sym((SymⁿE)∨)`, so its degree-`d` piece really is `SymᵈΓⁿF`. The product of input vectors has multidegree `(1,…,1)`, and therefore its degree-`d` coordinate pullback has multidegree `(d,…,d)`. This component is `(SymᵈF)^⊗n`, and the input permutation invariance puts the image inside its `S_n` invariants.

For a finite free module, the tensor-word orbits form a free basis of its symmetric tensors. The divided-power monomial with exponent vector `α` maps to the corresponding orbit sum. The defining shuffle product gives the divided-power multiplication constants, so the indicated identification with `Γⁿ` is canonical, not merely a dimension count. Dualizing the symmetric coinvariant quotient gives `(SymⁿE)∨=(F^⊗n)^S_n`, which gives the other `Γⁿ` appearing in the source.

### Exact normalization of the rational map

For a tensor of linear forms `ℓ_(ij)` arranged in `d` rows and `n` columns, normalized averaging of the `i`th row represents the functional whose value on `v_1⋯v_n` is

`(1/n!) Σ_(σ∈S_n) Π_j ℓ_(ij)(v_(σ(j)))`.

Multiplying these functionals over the rows is exactly the coordinate pullback. Its value is the sum over independent row permutations, with denominator `(n!)^d`, of the corresponding products of all `dn` linear forms. Grouping the factors belonging to each input vector is the transposed column arrangement. The resulting tensor of `SymᵈF` is invariant under permutation of the `n` input vectors. Applying the quotient from those invariant tensors to `Symⁿ(SymᵈF)` gives exactly column projection of row averaging. Averaging the outer `d` rows makes no change after column projection, since each column is already symmetric in those row factors. This proves equality with the normalized wreath/grid map, including all factorials.

As a concrete coefficient check in rank two and `n=d=2`, the source `(xy)²`, with `xy` sent to `(x⊗y+y⊗x)/2`, pulls back and then projects to

`(1/2)[(x²)(y²)+(xy)²]`.

Direct row averaging and transposition gives those same four tensor terms and the same coefficient `1/2` on both target monomials.

### Image and flatness

The source and target affine coordinate algebras identify the scheme image with `Spec(im μ*)` by EGA I 9.5.2; affineness supplies quasi-coherence. The image is torsion-free over Z as a subgroup of the polynomial algebra. Every finitely generated subgroup is free, their directed union is the whole group, and filtered colimits preserve flatness. Each fixed multidegree piece is a subgroup of a finite free group and is therefore finite free. The report correctly keeps the specialization map `A_Z⊗k→im μ_k*` visible: base change may kill information through saturation, even though `A_Z` is flat.

For `r≥n`, ordered independent `n`-tuples form a dense open subset of the source and `GL_r` acts transitively on them. Their products therefore form one orbit; its closure is the entire schematic image over Q. This proves the stated Chow-cone identification with the declared vector/coordinate dual convention.

The final Hilbert/Quot sentence can be made more precise by saying that those functors parametrize flat projective closed subschemes and coherent quotients with fixed Hilbert polynomial. General graded algebras can have different irrelevant torsion with the same Proj; no uniqueness assertion about all graded quotients is needed here.

## G-004: PASS

After geometric base change, the finite étale scheme has exactly two points. Its degree-zero cohomology is the two-dimensional function space and has no higher cohomology. Geometric Frobenius also exchanges the two points, since inverse and direct Frobenius coincide in the quotient of order two. The two displayed rational idempotents have eigenlines with eigenvalues `±1`. Both are pure of weight zero by Weil II Definitions 1.2.1–1.2.2 and Variants 1.2.3–1.2.4; only the plus line has invariants. Coefficients in `Q_2` cause no exception. These are actual idempotents of the rational finite étale/Artin object. The example tests the specified invariant-projector map and does not assert the absence of other geometric relationships.

## G-005: PASS for the polytope reformulation; two local source-proof typos repaired

The root formulas match PPS Definitions 3.2, 3.5, 3.8, 4.4 and 5.1. Splitting the minimum bound

`z_(i+1)−z_i ≤ min(A_i−2z_i,a_(i+1))`

gives exactly `z_(i+1)+z_i≤A_i` and `z_(i+1)−z_i≤a_(i+1)`. Together with endpoints and monotonicity, this is an identity bijection on marking vectors and a bounded rational polytope. A negative endpoint yields no points. For one leaf, the two endpoint equations require `r=s(T)` and give one point; this agrees with the single q-integer difference.

The center shift is always integral and nonnegative, as can also be checked directly. At a KOH vertex, writing `α=μ′`,

`ab−Σ_j m_j(μ)a^(j) = 2(Σ_j α_j²−b)=4b(μ)`.

Summing over the tree cancels internal terms. At a GOH root, put `α^(i)=(ν^(i))′`. The identity

`Σ_j m_j(ν^(i))Q_j(ν^(h))=Σ_j α_j^(i)α_j^(h)`

is a telescoping sum. It gives the root center defect `2τ`, where `τ=Σ_i,j α_j^(i)(α_j^(i)−α_j^(i+1))`. This integer is nonnegative, since it equals half the sum of the squares of all successive vector differences plus half `||α^(1)||²`. Thus the half-center expression used for `s(T)` is an integer. The KOH recursion terminates: all children have nonnegative products `a^(j)b^(j)` whose sum is strictly smaller than `ab` unless the partition is one row, in which case its sole child is a leaf.

The determinant shift for a two-row inner partition follows from the actual `GL_2` isomorphism and homogeneity of the outer Schur functor. Inner partitions of length at least three vanish on rank two. The one-dimensional `k=0` case is handled correctly. Specify a nonempty outer partition in the tree convention, or treat the empty partition separately by its one-dimensional degree-zero Schur functor.

### Source typo 1: Lemma 4.2 induction, p.9

The printed inequality has `|a|−2k_t`. Substitution `i=k_(t−1)` into Lemma 4.1 gives `|a|−2k_(t−1)`. The statement of Lemma 4.2 and both marking definitions use the correct index, as does G-005.

### Source typo 2: Lemma 4.1 interval-product calculation, p.8

The displayed negative term is printed with leading exponent `r+s−i−j`; it needs `r+s−i−j+1`. The original PDF page was rendered and visually inspected (`pps_p8_review.png`), confirming that this is not a text-extraction error. For `r=s=1` and `i=j=0`, the true left side is `1+q−q²−q³`, while the printed right side is `1−q²`.

The corrected identity, with `L=min(r−2i,s−2j)`, is

`(1−q)(q^i+⋯+q^(r−i))(q^j+⋯+q^(s−j))`

`=q^(i+j)(1+⋯+q^L)−q^(r+s−i−j+1)(1+⋯+q^(−L))`.

This identity is obtained by multiplying two finite geometric sums. The smallest negative exponent is `i+j+max(r−2i,s−2j)+1`, strictly beyond the midpoint `(r+s)/2`. Thus Lemma 4.1's actual coefficient statement is correct. The corrected index then proves Lemma 4.2 by induction, and the tree-to-polytope formula remains valid. The two erroneous local proof lines should be reported as repairs, not silently reproduced.

## G-006: PASS

Read the complete proof in `work/root/degree_three_report.md`. The natural-transformation decomposition has constant multiplicity maps independent of evaluation rank. Evaluation on rank two removes precisely the Schur factors of length greater than two, while every retained Schur representation is nonzero. Therefore invertibility of the evaluated natural map implies invertibility of every retained multiplicity map in all ambient ranks.

The independent geometric proof is complete: factorization of every binary form over C makes the multiplication morphism surjective on geometric points. A polynomial function vanishing on its image is therefore zero, so the coordinate pullback is injective. The source and target of its degree-`m` map have dimensions `binom(m+n,m)` and `binom(m+n,n)`, which are equal. G-003 proves that this pullback is exactly the normalized canonical map after the displayed rational identifications. This establishes the specified map's invertibility, not just an abstract equality of characters.

## G-007: PASS

Read every line of the formula and proof in `work/root/degree_three_report.md`. Interlacing from rank three to rank two with last-coordinate weight `n` gives `μ_1+μ_2=2n`, so `μ=(2n−k,k)`. The inequalities `λ_1≥μ_1≥λ_2≥μ_2≥λ_3`, together with the nonzero `(n,n)` weight requirement `k≤n`, give exactly the displayed `L` and `U`. The rank-two representation is `det^k⊗Sym^(2n−2k)`, whose balanced monomial is fixed by the swap in its symmetric-power factor and receives the determinant factor `(-1)^k`. This proves the transposition trace, including its sign.

For the 3-cycle, only torus weights fixed by the cycle can contribute to the trace; at total degree `3n` that is exactly `(n,n,n)`. Evaluation of the alternant at three distinct cube roots of unity has nonzero denominator. Reducing row exponents modulo three either repeats a row, giving zero, or permutes the denominator rows, giving the stated sign. The `S_3` character inner products and class sizes yield all three quotients with their correct factors (including the dimension-two character for `(2,1)`). Their nonnegative integrality follows from those actual multiplicity spaces.

The interval count is then exact because its explicitly computed numerator equals its denominator times the corresponding nonnegative integer. On each of finitely many min/max and congruence chambers, the numerator is affine linear. This is a nonhomogeneous chamberwise lattice-point formula; it makes no false dilation assertion. For output partitions with more than three rows, all three coefficients vanish because the full tensor product `(SymⁿV)^⊗3` has only partitions of length at most three by repeated one-row Pieri. The displayed formula treats every remaining output.

## Independent quaternary quartic seed computation: PASS

The root weight-counting implementation was not imported or called. `check_quaternary_seeds.py` expands `h_k[h_4]` in power-sum cycle types and evaluates `χ^((k^4))` by the separately developed Murnaghan–Nakayama recursion from `work/rectangular/verify_rectangular.py`. The identity used is

`h_k[h_4]=Σ_(α⊢k) z_α^(-1) Π_(a∈α)(Σ_(β⊢4) p_(aβ)/z_β)`

and `⟨p_γ,s_λ⟩=χ^λ(γ)`. The code uses exact rational arithmetic and explicit connected, square-free rim-strip removals, with the height sign.

Results: `a_(4,4)^((4^4))=1` from 109 cycle types, `a_(6,4)^((6^4))=1` from 503 types, and `a_(7,4)^((7^4))=1` from 995 types. All class-by-class rational summands were saved, as well as a summary TSV. This verifies precisely those three finite seeds. The root's other degrees were not independently recomputed by this run.

## G-008: PASS

Read the whole proof in `work/root/invariant_polytope_report.md`, together with the exact module in T-010 of `work/theta/few_columns_report.md`. The preceding independent computation verifies all three finite inputs. In the domain `Sym(Sym⁴C⁴)`, products of nonzero invariant vectors remain nonzero. They therefore give an invariant in each degree of the numerical semigroup generated by 4, 6 and 7. Its asserted description follows by inspecting 0 through 9 and then using the four consecutive elements 10 through 13.

The power-sum proof of the involution identity is exact: for homogeneous inner degree four, `ω(p_r[h₄])=p_r[e₄]`. Expanding the outer complete function consequently gives `ω(h_k[h₄])=h_k[e₄]`. Conjugation sends `(k⁴)` to `(4^k)`, so every invariant just constructed supplies the claimed `det⁴` constituent in `Symᵏ(Λ⁴Cᵏ)`. Its powers remain nonzero in the polynomial algebra `Sym(Λ⁴Cᵏ)` and have highest weights `4jω_k`. By the explicit character equality T10.3 these prove the rectangular stable nonvanishing statements.

For a general asserted tail, write its conjugate weight as `Σ_i m_iω_i`. Embed each rank-`i` quartic highest vector into the first `i` coordinates of `Cʳ`, where `r=λ₁`. For an upper-triangular positive root operator `E_ab` with `a<b`, any operator involving a coordinate beyond `i` has source index `b>i` and annihilates these vectors because they contain no such basis coordinate; the operators on the first `i` coordinates already annihilate them. All repeated-odd-part contributions occur in the one domain `Sym(Λ⁴Cʳ)`, so their product, also with any contribution from the even part four, is nonzero. Every other even part contributes a power of `e₁∧⋯∧e_i` in its own symmetric-algebra factor. Each residual odd part occurs at most once and contributes that vector in degree one of its exterior-algebra factor. The tensor product of these nonzero vectors is nonzero over C, highest, and has weight exactly `λ′`. The scalar degree is `|λ|`. Thus the vector lies in precisely the graded part used by T10.3. No domain property is required or asserted for the exterior-algebra factors.

## G-009: PASS — the finite positive-polytope procedure is complete in its stated scope

Read the entire construction and proof in `work/root/invariant_polytope_report.md`, including the rank-two example. The conclusion supplies a terminating finite sum of bounded rational polytope counts for every symmetric-outer, symmetric-inner plethysm coefficient. The precomputation depends only on the positive integer `m`. Nothing in the proof supplies a bound polynomial in varying `m`, and the report accurately makes no such assertion.

### The actual algebra and its equivariant generators

The convention `P=Sym(E⊗F)` gives the standard actions on both factors. For upper unipotent matrices acting on `F`, the span of its first `j` standard vectors is preserved and its top exterior vector is fixed. Accordingly, minors in the first `j` columns are precisely right highest vectors of weight `ω_j`. Their row spans are `ΛʲE`. Cauchy decomposition makes each fixed right highest-weight component an irreducible left `GL(E)` module with multiplicity one. Products of the fundamental components map nontrivially into it, since the polynomial algebra is a domain, and the product image is a left submodule. Irreducibility proves surjectivity onto that component. This verifies flag-minor generation with the declared action convention.

The equality with plethysm can also be checked without appealing to T-002. The left weight `(n,…,n)` in `P` is canonically `(SymⁿF)^⊗m`, by taking the degree-`n` polynomial component in each row. The actual row permutation matrices permute these tensor factors. Their invariants are `Symᵐ(SymⁿF)` in characteristic zero. The right unipotent group commutes with them and with the left diagonal torus. Taking its highest-weight line of weight `λ` gives precisely the multiplicity `a_(m,n)^λ`. This proves the displayed dimension equality through concrete subspaces and actions.

The polynomial map `Q[z_I]→R` is equivariant. Extraction of the zero character for the split torus `T₀` is exact, by direct decomposition into character spaces. Its invariant monomials are exactly the balanced monoid `H_m`. This pointed rational monoid has a unique minimal set of nonzero indecomposable generators, and permutations of the row coordinates preserve that set. The sorting determinant signs give a genuine signed permutation action on the corresponding `Y` variables; they are not lost when products of minors are taken. The map `Y_l↦q_l` is therefore equivariant and surjective onto `R^T₀`. Each `q_l` is nonzero, although the different `q_l` need not be algebraically independent. Every generator has positive common row degree `n_l`.

Every row permutation preserves both that common degree and the right highest weight. Thus each Reynolds average used in the construction is homogeneous in the full indicated multigrading. Averaging is an exact projector over Q, so the images of generators of `Q[Y]^{S_m}` generate exactly `A_m`.

For completeness, Noether's degree bound here has a short direct proof. Let a finite group `G` of order `g` act linearly on a polynomial algebra `S` over Q. For each linear form `ℓ`, the orbit polynomial `∏_(h∈G)(T−hℓ)` has invariant coefficients of degrees at most `g`; substituting `T=ℓ` puts `ℓ^g` in the ideal generated by positive-degree invariants of degree at most `g`. Polarization shows that the powers `ℓ^g` span `S_g`, so that ideal contains every homogeneous component of degree at least `g`. Express an invariant of degree greater than `g` in that ideal and apply Reynolds to its coefficients. Induction on degree then expresses it as a polynomial in the invariants of degrees at most `g`. In each such degree, the Reynolds images of monomials span the invariant space. This proves exactly the bound and generating list in G9.4 for `g=m!`.

### Presentation, grading and disjoint standard-monomial cells

The kernel of `Q[Z]→Q[X]`, `Z_j↦f_j(X)`, is precisely the intersection of the graph ideal with `Q[Z]`. This gives the stated finite effective elimination calculation. To check homogeneity rigorously, grade `Q[X]` by both full diagonal tori. Each `f_j` has left weight `n_j(1,…,1)` and right weight `λ^(j)`. Assign those same weights to `Z_j`. The graph ideal and its elimination ideal are homogeneous. The map `(n,λ)↦(n(1,…,1),λ)` is injective, proving the claimed `D_m` homogeneity. A homogeneous Gröbner basis and its division remainders preserve this grading for any chosen monomial order.

Standard monomials give a homogeneous vector-space basis of `Q[Z]/J`. For each exponent coordinate, the partition into the values below `B_j` and the final interval starting at `B_j` is disjoint and exhaustive. On a final interval, divisibility by every minimal leading monomial is automatic in that coordinate, because its exponent is at most `B_j`; on the other cells that coordinate is fixed. Therefore membership in `J₀` is constant on every product cell. Testing the lower corner retains exactly, and without multiplicities, all standard monomials. This also covers `J₀=0`, coordinates with `B_j=0`, and cells with no free coordinates.

In each retained cell the exponent vector is uniquely `u+z`, with free coordinates indexed by `S`. Its degree equation is exactly `D_(m,S)z=(n,λ)−D_mu`. The first row is a sum of the free coordinates with strictly positive integer coefficients. A nonnegative real solution consequently has each free coordinate at most `n`; a negative right-hand side gives no solution. Thus every displayed polyhedron is bounded, including empty sets and zero-dimensional points. Its integer points are in bijection with the standard monomials of the required degree. This proves the positive sum for all parameters. Outputs with more than `m` rows vanish by the one-row Pieri decomposition of `(SymⁿF)^⊗m`.

The explicit `m=2` algebra is consistent: row interchange fixes `u=x₁x₂` and negates the determinant `v`, giving `Q[u,v²]` and the displayed two degree vectors. This separately checks the determinant sign in an instance where omitting it would change the formula. A monomial initial ideal also gives the asserted flat multigraded Gröbner degeneration. A finite weight vector realizing the finite Gröbner comparison suffices; adding a multiple of the positive first grading makes its entries nonnegative without changing the homogeneous comparisons.

## G-010: PASS, with the graph-elimination variables made explicit

Read the complete statement and proof in `work/root/general_polytope_extensions.md`. Let `A=Q[X,Z]`, where `X` are matrix entries and `Z` now denotes the auxiliary basis of `W∨`. For the computed homogeneous invariant generators `f_j(X,Z)`, introduce separate presentation variables `T_j`. The precise kernel calculation is

`(T_j−f_j(X,Z): all j) ∩ Q[T]`.

Both `X` and auxiliary `Z` must be eliminated. The initial wording “eliminate the matrix variables” should be expanded to include `Z`; this is a presentation-algorithm clarification and does not change the invariant algebra or proof.

The wreath module `W=[ν]^⊗m⊗Inf[μ]` uses the ordinary place permutation of its tensor factors under the outer symmetric group. Its dual is the actual contragredient rational representation. The balanced degree-one piece of the flag algebra has left weight `(1^N)` and is the multilinear Specht module `[λ]` under the literal row permutations, without a determinant twist. This can be tested in the extreme shapes: the full symmetric power gives the trivial module, and the top exterior power gives the sign module. The auxiliary-degree-one piece is exactly `W∨`, and the standard map `v⊗φ↦(w↦φ(w)v)` identifies the `H` invariants with `Hom_H(W,[λ])`. The wreath-product Schur–Weyl isomorphism then gives the asserted coefficient. No entire auxiliary symmetric algebra is mistaken for its degree-one piece.

The polynomial algebra in Hilbert-basis variables and auxiliary variables maps equivariantly and surjectively onto `B_N⊗Sym(W∨)`. The finite group action on its variables is linear, even though its auxiliary part need not be a signed permutation action. The elementary orbit-polynomial and polarization proof of Noether generation in the G-009 review applies to every such linear action. All three degrees `(b,λ,k)` are preserved by `H`; orbit averages of individual monomials are homogeneous. Thus the finite explicit Reynolds list generates precisely the target invariant algebra, and the corrected graph elimination presents it.

Every nonconstant generator has `b+k≥1`, since the balanced variables have positive `b` and the auxiliary variables have positive `k`. The target has `b+k=2`. After subtracting a cell corner, the sum of each free coordinate times its strictly positive integer degree is at most two, or the polytope is empty. This proves boundedness and the exact standard-monomial count, including all zero coefficients. The smaller row-inner construction uses the same proof with balanced target degree `n` and auxiliary degree one. The actual sheaf correspondence is the auxiliary-degree-one covariant module on the invariant affine base; its stated multiplicity is the indicated graded component in characteristic zero.

## G-011: PASS

Read the complete module construction and proof in `work/root/general_polytope_extensions.md`. Every Hilbert-basis generator `q_i` of `B` satisfies a monic polynomial of degree `|G|` whose coefficients lie in `C=B^G`, namely its orbit polynomial. Reducing powers separately therefore shows that the box monomials `q^u`, `0≤u_i<|G|`, generate the entire algebra `B` as a `C` module. These reductions treat the orbit coefficients as coefficients in `C`; they do not require expanding them again as powers of the `q_i`.

For every `c∈C`, both Reynolds operators satisfy `P_H(cf)=cP_H(f)` and `P_K(cf)=cP_K(f)`. Their consecutive images of the finite box hence generate exactly `P_K(B^H)`. They remain homogeneous because both actions preserve the right highest weight and the balanced left degree. On balanced degree one and right weight `λ`, this is the image of the actual operator `P_K|_[λ]^H`, by the same multilinear Specht identification as G-010. The proof consequently preserves a possible zero scalar on a multiplicity-one block and never replaces the map by an arbitrary homomorphism between equal-dimensional modules.

The proposed presentation algorithm is exact. In `S=Q[Z,X]`, the projection onto the first `t` positions of the syzygy module of `(g_1,…,g_t,Z_1−c_1,…,Z_q−c_q)` is precisely the submodule of vectors `a` for which `Σa_i g_i` lies in the graph ideal. Intersecting that projected module with `Q[Z]^t` imposes exactly the coefficient restriction in the stated map. One implication follows by reading a syzygy; the other follows by writing the graph-ideal membership and adding its coefficients to form a syzygy. Projecting a finite generating set and applying a module elimination order computes this intersection. All rings are Noetherian polynomial rings over Q, so the computations terminate.

Assigning each free basis vector the actual degree of its image makes the kernel homogeneous. Its leading submodule splits into a direct sum of monomial ideals times those basis vectors. The ordinary monomial threshold partition applies separately to each such ideal, with a whole position discarded when its leading ideal contains 1. This gives a homogeneous vector-space basis and proves the displayed degree equation with both the generator shift and cell-corner shift. All coefficient variables have positive balanced degree; at target balanced degree one this again gives bounded polyhedra, or empty ones. The constant box monomial has degree zero and causes no exception because it is a module generator, not a polynomial coefficient variable.

The kernel/cokernel extension is also effective from these data. The box generates `B^H` after `P_H`, and `B^K` after `P_K`. Applying an element of `H` to a box monomial gives, up to the known determinant sign, another box monomial, since the full symmetric group permutes the Hilbert-basis generators and preserves their exponent bounds. Thus the image of every source module generator has an explicit rational linear expression in the target module generators. Standard module kernel and quotient calculations then give homogeneous presentations and the same positive counts. This completes the stated computation for every fixed pair `(m,n)` while preserving the distinction between a finite terminating procedure and a theorem about all open injectivity parameter ranges.

## G-012: PASS — four explicit polytopes follow from the verified presentation

Read all of `work/root/rank_three_presentation.md`. The first relation is exactly `x₁p₂₃−x₂p₁₃+x₃p₁₂=0`, a determinant with two repeated columns. Its polynomial is irreducible: as a linear polynomial in the `y_i`, its coefficients `x_i` have no common nonconstant factor, and the corresponding linear polynomial over `Q(x₁,x₂,x₃,z)` is irreducible. The six independent parameters can be checked directly. On `x₁y₃≠0`, choose the first column `(x₁,x₂,x₃)`, second column `(0,y₃/x₁,−y₂/x₁)`, and third column `(0,0,z/y₃)`. This realizes arbitrary values of the six quantities `x₁,x₂,x₃,y₂,y₃,z`, with `y₁` then forced by the relation. Together with flag-minor generation, this proves that the displayed principal relation is the complete flag-algebra kernel.

The left diagonal weight of `x^a y^b` in coordinate `i` is `a_i+Σ_j b_j−b_i`. It is balanced exactly when all `a_i−b_i` coincide. Factoring a power of `u=∏x_i` or `v=∏y_i` leaves a monomial in `t_i=x_i y_i`. The normal forms containing at most one of `u,v` are distinct monomials in `x,y`, so `uv=t₁t₂t₃` is the sole relation before imposing the flag relation. The latter is torus-invariant; exact weight extraction therefore gives the stated quotient by `Σt_i`, with no additional invariant-ideal assumption.

A row permutation acts on the oriented minors by `y_i↦sgn(σ)y_(σi)`. Thus `u` is fixed, `v,z` have the sign character, and the `t_i` carry the sign-twisted permutation action on their sum-zero plane. The displayed `s` is invariant, `f` has sign, and the two sign factors on the cubic Vandermonde `d` cancel. Its discriminant equation is exactly `d²=−4s³−27f²`.

The alternating subgroup acts as the usual alternating subgroup on that plane. Its invariant ring is `Q[s,f]⊕dQ[s,f]`: symmetrization under an ordinary transposition gives the symmetric part, and every alternating polynomial is divisible by the Vandermonde with symmetric quotient. A twisted transposition fixes `s,d` and negates `f`. Its even and odd subspaces in this ring are consequently `Q[s,d]` and `fQ[s,d]`, after using the discriminant relation to remove even powers of `f`. The variables `s,d` are algebraically independent: `s,f` are independent, and the discriminant equation makes `f` algebraic over `Q(s,d)`.

With the two sign variables `v,z`, the even monomials are generated by `v²,vz,z²`, and the odd monomials multiply the plane's sign subspace. This proves the asserted generating list before the relation `uv=f`. Finite averaging is exact on the stable quotient by that relation. Its images satisfy `fv=uV` and `fz=uW`, proving the claimed surjection from the six-generator, two-relation algebra.

The injectivity proof is complete. Localizing at `v` identifies the fraction field with `Q(t₁,t₂,v,z)`, with `u=f/v`. The variables `u,s,V=v²,Z=z²` are algebraically independent. Over `F=Q(u,s,V,Z)`, the element `D=−4s³−27u²V` has odd valuation `−3` at `s=∞`, so it is a nonsquare. The element `VZ` has odd valuation at `Z=0`, and `D/(VZ)` has odd valuation `−1` there. Hence their two square classes are independent. More explicitly, an element of `F(d)` whose square lies in `F` has either its `1` coefficient or its `d` coefficient zero, since the cross term is twice their product. Thus a square root of `VZ` in `F(d)` would force either `VZ` or `VZ/D` to be a square in `F`, which the valuations exclude. The actual `d,W` therefore generate a degree-four extension, making `1,d,W,dW` linearly independent over `F`.

The abstract quotient is free over `Q[u,s,V,Z]` on these same four elements, by its two monic quadratic relations. Its map to the actual invariant algebra is injective by that independence, and was already shown surjective. This proves the presentation. Directly from the minors, the six weights are exactly those in G12.2. Its free monomials therefore give the four degree systems in G12.3, and the first equation bounds every nonnegative real coordinate. The case `n=0` gives one point for the empty shape; the other cases are included without exception. Outputs with more than three rows have coefficient zero by repeated Pieri. No finite numerical comparison is needed for this proof; this reviewer has not rerun the separately reported 34,150-case computation.

## G-014: PASS — the actual canonical map is surjective in the stated first-row range

Read the complete `work/root/chow_first_row_report.md`. The coordinate variance is correct: multiplication on `(V*)^a` pulls a linear coefficient functional in `(Sym^a V*)∨` to a polynomial of multidegree `(1,…,1)` in the ordered linear forms. Its degree-n pullback is the canonical map `h_(n,a)` with the already checked symmetric/divided-power convention of G-003. The coefficient coordinate `C_β` pulls back to `uE_β`, with `u=∏x_i`, so the displayed homogenization uses the actual map rather than an arbitrary homomorphism between plethysm modules.

Every balanced multidegree-n target monomial becomes `u^n` times its row-normalized monomial. A target torus-weight vector with first coordinate `λ₁` has exactly `d=an−λ₁` degrees in the other coordinates. The localization expression is therefore polynomial in the row ratios, homogeneous of degree d, and invariant under the actual row permutation action.

The distinct-row identity C.7 is exact. For a fixed assignment of row indices, the compatible partitions refine its equality classes. On each class, the Möbius weight sums the signs of all permutations grouped by cycle decomposition, giving zero for a class of size at least two. Ordinary monomial orbit sums divide the distinct-row sum by the factorials of repetitions among the nonzero exponent vectors. There is no extra zero-row factorial: the distinct-row tuples have already removed permutations of unused rows. Newton's identity C.8 holds as a formal power-series identity with constant denominator term one. Its coefficient of `y^α` is precisely the nonzero multinomial coefficient times `P_α`. Dividing by that integer is legitimate over the stated characteristic-zero field. The weight equals the total tail degree throughout; every coefficient generator has positive weight, so the number of factors in each resulting monomial is at most d.

For `n≥d`, the source exponent `n−k` is nonnegative for every term, and C.9 gives an actual degree-n preimage. Equality on the principal open `u≠0` implies polynomial equality because the ambient polynomial ring is a domain. Every target highest-weight vector of weight λ is lifted. The image is GL-stable, so it contains the full submodule generated by every such vector, and hence the entire λ-isotypic component. The preimage itself need not be highest weight; this causes no deficiency in the image argument. Characteristic-zero isotypic projection also produces a preimage in the same block.

The reported image-multiplicity equality, bounded first-row range, and finite rational-denominator spreading-out conclusion follow. No integral-surjectivity conclusion is drawn at excluded primes. For the zero-dimensional ambient vector space the assertion is immediate directly; for `n=0`, use the empty partition convention `λ₁=0`. The source's chart/generator attribution was not independently rechecked during this proof review; the complete displayed argument itself supplies the generation and lift being reviewed.
