# A-017. Cote 79: the exact scalar and determinant maps

The original public PDF pages47–51, particularly (114)–(125′), supply the definitions missing from supplied scan051. Write `R=Z/nZ`, `n≥2`, and let `M` be free of rank two over `R`. Let `M_prim` be its unimodular vectors, `D=Λ²_R M`, and `D_gen` the generators of this rank-one module. The source writes stars for these generator loci. Its objects are

`U=R×/{±1}`, `S=M_prim/{±1}`, `Π=D_gen/{±1}`, `L′=D/{±1}`.

Here `Π` is a `U`-torsor. The map

`β:S×S→L′`, `([u],[v])↦[u∧v]`

is well-defined. Changing either lift changes the wedge by a sign, and interchanging the lifts also changes it by a sign. Thus β is symmetric on the quotient, despite being induced by the alternating bilinear wedge map before quotienting. Define `A⊂P₂(S)` by `β(s,t)∈Π`, and define `τ:A→Π` by this value. A unit wedge already ensures `s≠t`.

For `i∈Π`, set `A_i=τ⁻¹(i)` and let `F_i` be the three-element subsets all of whose two-element subsets belong to `A_i`. These are the precise edge and face constructions in (120)–(121), defining the source's family `Σ(i)` on its vertex set. The statements that each is a particular connected regular surface and that one of them reconstructs all the rest are additional assertions; the maps below do not assume a classification of those surfaces.

## The action and its square on determinant types

For `λ=[a]∈U`, define `T_λ([u])=[au]`. This is independent of both representatives, has inverse `T_(λ⁻¹)`, and satisfies `T_λT_μ=T_(λμ)` and `T_1=id`. Bilinearity of the actual wedge map gives

`β(s,T_λt)=λβ(s,t)`,

and hence

`β(T_λs,T_λt)=λ²β(s,t)`.

Multiplication by units preserves generators of `D`, so `T_λ` preserves `A` and

`τ({T_λs,T_λt})=λ²τ({s,t})`.

Consequently the pair of maps `(T_λ, i↦λ²i)` is an automorphism of `(S,Π,A,τ)` and transports the actual simplicial structure `Σ(i)` to `Σ(λ²i)`. Faces are carried to faces because their three edge types are carried to the common new type. This proves the target page's formula (127), with every source and target specified. It also identifies the square in that formula by the explicit determinant map: `Λ²(a·id_M)=a²·id_D`.

## Recovery of the scalar action from the one-argument relation

The full wedge relation (125) determines each `T_λ` uniquely. Indeed, primitive `u` extends to a basis `(u,w)`. For `v=bu+cw`, equality of the classes of `s∧u` and `s∧v` for all primitive `s` first gives `c=0` by taking `s=u`, then `b=±1` by taking `s=w`. Therefore the map `S→(L′)^S` given by all wedge values is injective.

The restricted relation (125′) using only pairs whose wedge is a unit also determines each such permutation for every `n≠4`. To prove this, rescale and change the sign of `v` so that comparison with `s=w` gives `v=u+cw`. For every `t∈R`, the vector `w+tu` is primitive and has unit wedge with `u`; comparison gives `1−tc∈{1,−1}`. The additive subgroup `cR` is therefore contained in `{0,2}`. A nonzero such subgroup forces `2` to have additive order two, hence `n=4`. Thus `c=0` for `n≠4`. For `n=4`, the acting group `U` is trivial, so its group action is uniquely the identity. This proves the unique compatible `U` action in the actual rank-two module model for all `n≥2`.

The exception also explains why a bare point-separation assertion needs care. In `R=Z/4`, the distinct classes of `(1,0)` and `(1,2)` have exactly the same unit-wedge tests and unit-wedge types: the sole type is the class of `±1`, and both tests say that the second coordinate of the testing vector is odd. The full wedge map separates them by testing `(1,0)`, whose two wedge values are `0` and `2`.

Conversely, every `i∈Π` is the wedge type of a basis pair. The expression `τ({s,T_λt})` for such a pair of type `i` equals `λi`, independently of the chosen pair. It therefore recovers the torsor scalar action from the constructed action on vertices. This supplies actual inverse recovery maps in this module model, rather than an unproved comparison of structures.

## What remains a source question

The last paragraph of scan051 asks how a single abstract triangulation `P₀=(S,A₀,F₀)` determines every other `Σ(i)` and the `U` action. The preceding concrete construction starts with the rank-two module, its determinant line, and its scalar action; it does not reconstruct them from one unlabeled complex. The inspected pages do not provide that reconstruction. The displayed embedding `Aut(P₀)→Sym(S)` is injective directly: an automorphism is the vertex permutation preserving the specified edge and face subsets, so its action on vertices determines it.

The entire proof above was checked by expanding the wedge map on a basis, including the exceptional `n=4` separation calculation. No broader reconstruction theorem is asserted.
