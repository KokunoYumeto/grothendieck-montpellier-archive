# A-020–A-021. The modular rank and the mixed-characteristic lattice ring

These results answer two separate questions in the supplied study of cote133, scans28–29. Every Grothendieck group below uses all short exact sequences in the specified category. The maps are explicit; no assertion about the split group of isomorphism classes is substituted for this exact Grothendieck group.

## A-020. The rank over the prime field

For a prime `p`, let `G₀(F_p[S_n])` be the Grothendieck group of finite-dimensional modules. The composition-factor map identifies this group with the free abelian group on the simple modules: Jordan–Hölder makes the map well defined, and sending a simple label to its module class is its inverse.

James, *The Representation Theory of the Symmetric Groups*, Lecture Notes in Mathematics682 (1978), Theorem11.5, printedp40, classifies these simples by the p-regular partitions of `n`. Here p-regular means that no part occurs p or more times. For `n=p`, the only excluded partition is `(1^p)`. Hence

`rank_Z G₀(F_p[S_p]) = number_of_partitions(p) − 1`.

The source's alternative count by p-regular conjugacy classes gives the same answer: among cycle partitions of `p`, only `(p)` is excluded. James Lemma10.2, p36, proves the equality of these two counts by expanding `∏(1−t^(mp))/(1−t^m)` in the two ways. These are different label sets, linked by that coefficient identity; their equal cardinalities have not been inferred by identifying their individual partitions.

## A-021. Rationalization for lattices over a characteristic-zero DVR

Let `O` be a discrete valuation ring of characteristic zero, with uniformizer `π`, fraction field `K`, residue field `k`, and `G=S_n`. Write `L_O(G)` for the exact category of finitely generated `O[G]`-modules whose underlying `O`-module is free. Its admissible sequences are the short exact `O[G]`-sequences with all three terms in this category. Rationalization is the exact functor

`L_O(G) → Rep_K(G),    M ↦ K⊗_O M`.

It induces an isomorphism

`r_n : K₀(L_O(S_n)) → R_K(S_n)`.

Here is a direct proof, including the boundary construction that supplies injectivity.

### The torsion boundary

For a finite `O`-torsion `O[G]`-module `T`, choose a surjection `P→T` with `P` finite free over `O[G]`. Its kernel `L` is finite free over the discrete valuation ring `O`. Define

`δ(T)=[P]−[L] ∈ K₀(L_O(G))`.

This class is independent of the chosen presentation. Indeed, for presentations `P→T` and `P′→T`, their fibre product `Q=P×_T P′` lies in the lattice category. The exact sequences `0→L→Q→P′→0` and `0→L′→Q→P→0` give `[P]−[L]=[P′]−[L′]`. Both sequences split over `O[G]` because their quotients are free over `O[G]`, although their ordinary exactness already suffices for the displayed equality.

The assignment is additive on a torsion exact sequence `0→T₁→T₂→T₃→0`. Choose free presentations `P_i→T_i` for `i=1,3`, lift `P₃→T₃` to `T₂`, and combine this lift with `P₁→T₁→T₂`. The resulting surjection `P₁⊕P₃→T₂` has a kernel `L₂` in an exact sequence `0→L₁→L₂→L₃→0`. This gives `δ(T₂)=δ(T₁)+δ(T₃)`.

More generally, any exact sequence `0→A→B→T→0` with `A,B` lattices satisfies

`δ(T)=[B]−[A]`.

To verify this without choosing a new invariant, form `Q=P×_T B`. Its two lattice exact sequences are `0→A→Q→P→0` and `0→L→Q→B→0`. Thus `[A]+[P]=[L]+[B]`, which is precisely the formula.

For every lattice `M`, multiplication by `π` identifies `M` with the lattice `πM`. The last formula applied to `0→πM→M→M/πM→0` gives

`δ(M/πM)=0`.

### Specht reductions make the boundary zero

Let `S_O^λ` be the Specht lattice with its standard integral polytabloid basis, extended from `Z` to `O`. James Theorem8.4, pp29–30, and Corollaries8.6–8.11, pp30–31, give its freeness, integer action matrices and reduction `k⊗S_O^λ=S_k^λ`.

In residue characteristic `p>0`, James Corollary12.2, p42, shows that for a p-regular `λ`, the class `[S_k^λ]` equals `[D_k^λ]` plus a sum of classes indexed by strictly dominating p-regular partitions. Equivalently, Corollary12.3, p43, exhibits the unitriangular p-regular submatrix of the decomposition matrix. This works over the present arbitrary residue field: Theorem11.5, p40, explicitly states that every `D^λ` is absolutely irreducible and every field is a splitting field for `S_n`. Tensoring a composition series over `F_p` with `k` is exact and its simple factors remain simple. The standard polytabloid matrices identify that tensor product with the Specht module over `k`. Since the poset is finite, backward substitution over `Z` expresses every simple class `[D_k^λ]` as an integral linear combination of the classes `[S_k^μ]`.

In residue characteristic zero, the Specht modules themselves form the complete set of simple `k[S_n]`-modules by the characteristic-zero case of the same theorem. Their classes already form a basis. This supplies the same generation conclusion without a modular reduction argument.

The boundary vanishes on every `[S_k^μ]`, because it is the reduction of `S_O^μ`. Its additivity therefore makes it vanish on every finite-dimensional `k[G]`-module. A finite `O`-torsion module has the finite filtration by powers of `π`, whose successive quotients are finite-dimensional `k[G]`-modules. Consequently

`δ(T)=0` for every finite `O`-torsion `O[G]`-module `T`.

### Commensurability and the inverse on Grothendieck groups

Suppose lattices `M,N` have isomorphic rationalizations. Use an actual `K[G]`-isomorphism to place them inside one finite-dimensional `K[G]`-module. The intersection `I=M∩N` is a `G`-stable lattice, and both `M/I` and `N/I` are finite `O`-torsion. Applying the boundary formula gives `[M]=[I]=[N]` in the exact lattice group.

The algebra `K[S_n]` is split semisimple. Its irreducibles are the rationalizations of the Specht lattices. These facts prove surjectivity of `r_n`. An element of its kernel has the form `[M]−[N]`; equality of the rationalized classes in a semisimple category gives an actual rational isomorphism. The intersection argument proves `[M]=[N]`, and hence injectivity. More explicitly, the inverse sends the rational Specht class `[S_K^λ]` to `[S_O^λ]`; the preceding argument verifies that this inverse also recovers the class of every lattice.

### Induction multiplication

Form the graded group `R_O=⊕_{n≥0}K₀(L_O(S_n))`, with product

`[M]·[N]=[Ind_{S_a×S_b}^{S_{a+b}}(M⊗_O N)]`.

Tensor product is exact in each variable because the underlying modules are free. The group algebra of `S_{a+b}` is free over that of `S_a×S_b` on a coset basis, so induction is exact and preserves lattices. Rationalization commutes with these functors through the canonical tensor and induction isomorphisms. Thus `⊕r_n` is an isomorphism of graded rings.

The rational Frobenius characteristic sends the trivial representation `ρ_n` to the complete symmetric function `h_n`. Since `Λ=Z[h₁,h₂,…]`, this yields the concrete generator-preserving isomorphism

`Z[ρ₁,ρ₂,…] ≅ R_O`.

This includes `O=Z_p` and `O=Z_(p)` and resolves the study's expressly open `Z_p`-lattice case. No completeness or unramifiedness assumption is needed. The proof uses that submodules of finite free `O`-modules are free and that finite torsion modules admit the displayed residue-field filtration. The exact boundary of these steps is substantive: A-023 in `LOCAL_RING_COUNTEREXAMPLE.md` gives a characteristic-zero local ring with a rank-one representation outside the subgroup generated by the Young permutation classes. The broader classification of coefficient rings remains a question.

## Primary source and inspection record

James's original book: DOI `10.1007/BFb0067708`; public university-hosted scan: https://www-users.cse.umn.edu/~webb/oldteaching/Year2010-11/the-representation-theory-of-the-symmetric-groups-SLN.pdf . The cited pages29–31,36,39–40,42–43 were read. The standard-basis proof, the stated simple-module classification and its proof dependencies, and the unitriangularity argument were checked. The classification theorem's count invokes general modular representation theory explicitly cited by James; this report does not claim a new proof of that theory. The torsion boundary, pullback comparisons, commensurability argument and graded-ring compatibility above were independently checked in full in this run.
