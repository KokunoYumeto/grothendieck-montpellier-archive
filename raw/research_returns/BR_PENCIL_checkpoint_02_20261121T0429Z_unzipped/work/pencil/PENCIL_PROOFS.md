# Residual pencils: exact torus reduction and the two-dimensional minimum

Author: `/root/pencil`, GPT-6 Astra Pro, inherited reasoning configuration (the runtime does not expose a numeric effort setting). Run: `BR_PENCIL-20261121/pencil`. Draft begun 2026-11-21 UTC. This note gives full proofs, rather than relying on generic numerical samples.

## Conventions

Let `k` be an algebraically closed field. Border rank means Zariski closure of sums of pure tensors in the indicated, **ungrouped**, factors. The tensors have integral ordered-coordinate coefficients `+1` or `−1`; in the polynomial families these are the divided-power/coefficient tensors, with no division by a factorial. Over characteristic zero they are nonzero scalar multiples of the usual symmetric coefficient tensors. The signs coalesce in characteristic two, as they should.

For the row determinant/permanent family, let `Q_I` be the alternating/symmetric sum of all orders of a `b`-element subset `I` of the coordinate basis of `k^n`. For the polynomial determinant/permanent family, let `Q_{I,J}` be the corresponding ordered coefficient tensor of the minor/permanent on row set `I` and column set `J`, both of cardinality `b`. These are bases of the residual image `U_{n,b}` by predecessor GCT_GINEQ F-22/F-23, and also directly by their pairwise disjoint ordered-coordinate supports.

For a `j`-plane `W` with ordered basis `u_1,...,u_j`, put `P_W = Σ a_h ⊗ u_h`, in `k^j ⊗ E^{⊗b}`. Its border rank is independent of the basis, because a change of basis is an invertible map in the first tensor factor.

## P-01. Coordinate minima suffice, for every j and all four families

**Statement.** For every `1 <= j <= dim U_{n,b}`,

`min_{W∈Gr(j,U_{n,b})} BR(P_W) = min_{S⊂basis(U_{n,b}), |S|=j} BR(Σ_{Q∈S} a_Q ⊗ Q)`.

**Full proof.** In the row case act on the coordinate vector `e_i` by multiplication by `t^{d_i}`, where `d_i=2^i` (`i=0,...,n−1`). Every `Q_I` is an eigenvector with weight `w_I=Σ_{i∈I}d_i`, and these weights are distinct. In the polynomial case act on `e_{ij}` by multiplication by `t^{d_i+f_j}`, where `d_i=2^i` and `f_j=2^{n+j}`. Every `Q_{I,J}` has weight `w_{I,J}=Σ_{i∈I}d_i+Σ_{j∈J}f_j`, and the weights are distinct by binary expansion. These statements hold in every characteristic, since the integer exponents define characters of `G_m` and distinct integer exponents define distinct characters even in positive characteristic.

Order the residual basis `q_1,...,q_N` by increasing weights `w_1<...<w_N`. Choose an echelon basis of the given plane:

`u_h=q_{p_h}+Σ_{i>p_h} c_{hi}q_i`, for `h=1,...,j`,

where the pivot indices `p_h` are distinct; ordinary row reduction gives this form. Define

`u_h(t)=t^{−w_{p_h}}g(t)^{⊗b}u_h=q_{p_h}+Σ_{i>p_h}c_{hi}t^{w_i−w_{p_h}}q_i`.

Every exponent in the sum is a positive integer, so `u_h(t)` is polynomial in `t` and specializes to `q_{p_h}` at zero. For `t≠0` the tensor `P(t)=Σ a_h⊗u_h(t)` is obtained from `P_W` by the product of `g(t)` in the residual factors and `diag(t^{−w_{p_h}})` in the first factor. All these maps are invertible. Thus `BR(P(t))=BR(P_W)` for `t≠0`. The rank-at-most-`r` border-rank locus is Zariski closed by definition. Consequently `BR(P(0))<=BR(P_W)`, with `P(0)=Σ a_h⊗q_{p_h}` a coordinate-plane tensor. Since every coordinate plane is itself a plane in `U`, the two minima are equal. No claim of attainment by a generic plane is used. QED.

**Geometric dictionary.** This is an explicit one-parameter degeneration of a point of `Gr(j,U)` under the split torus inside `GL_n` (row families) or `GL_n×GL_n` acting on matrix coordinates (polynomial families). The row-echelon construction supplies a flat rank-`j` subbundle of the trivial `U`-bundle on `A^1`, because the pivot coefficient submatrix stays the identity. The associated tautological tensor specializes under a product of general linear group schemes. The proof uses the closed Segre secant cone, not an assertion that general fibers have fixed tensor rank. All group actions and the coordinate families are defined over `Z`; coefficients of an arbitrary input plane may require its base field.

## P-02. Two coordinate entries reduce to an adjacent pair, for all b

**Statement.** For `n>=b+1`, the minimum in P-01 for `j=2` equals the border rank of one fixed adjacent-pair tensor. In the row families it is

`a_1⊗Q_{[b]} + a_2⊗Q_{[b−1]∪{b+1}}`.

In the polynomial families it is

`a_1⊗Q_{[b],[b]} + a_2⊗Q_{[b],[b−1]∪{b+1}}`.

**Full proof, row case.** Take two distinct `b`-subsets `I,K`, and write their common part as `C`, of cardinality `c`. Their differences each have cardinality `d=b−c>=1`; enumerate these as `i_1,...,i_d` and `k_1,...,k_d`. Map the coordinates from `C` bijectively to `e_1,...,e_c`. For `1<=h<d`, map both `e_{i_h}` and `e_{k_h}` to `e_{c+h}`. Map `e_{i_d}` to `e_b` and `e_{k_d}` to `e_{b+1}`. Send other coordinates to zero. The restriction of this linear map to either selected coordinate set is injective. Hence applying it in every tensor factor maps `Q_I,Q_K` to the two displayed adjacent basis tensors, up to independent signs in the determinant case and exactly in the permanent case. Absorb any signs in the two-dimensional first factor. Border rank cannot increase under a product of linear maps, so every coordinate pair has border rank at least that adjacent pair. The adjacent pair itself occurs whenever `n>=b+1`, proving equality by P-01.

**Full proof, polynomial case.** Take distinct `(I,J),(K,L)`. If `J≠L`, choose a set map from the row coordinates such that its restrictions to `I` and `K` are bijections onto the same set `[b]`; this is possible by retaining their common coordinates and pairing the two equally sized differences. On the column coordinates use the preceding row-case construction to map `J,L` injectively to `[b]` and `[b−1]∪{b+1}`. The induced linear map on matrix-coordinate spaces sends `e_{ij}` to `e_{f(i),g(j)}` (or zero for unused indices). Because its restrictions to both selected row sets and both selected column sets are injective, it sends each selected minor/permanent tensor to the desired minor/permanent tensor, up to a nonzero sign in the determinant case. The construction never identifies two rows or two columns **within** either selected term. If `J=L`, then `I≠K`; interchange the roles of rows and columns first. Transposition is an invertible permutation of matrix coordinates and takes the resulting adjacent-row pair to the displayed adjacent-column pair. Again absorb signs in the first factor, use monotonicity, and note that the adjacent pair occurs. QED.

**Scope.** This is an exact reduction for every `b`, not a formula evaluating the adjacent-pair border rank when `b>2`. It sharply identifies the remaining smaller tensor. The requested `b=2` evaluation is given below.

## P-03. A star tensor has border rank k+1, in every characteristic

**Statement.** Let `k>=1`. For independent vectors `a_1,...,a_k` and `e_0,...,e_k`, and `δ=+1` or `−1`, define

`S_{k,δ}=Σ_{i=1}^k a_i⊗(e_0⊗e_i+δ e_i⊗e_0)`.

Then `BR(S_{k,δ})=k+1` over any algebraically closed field.

**Full lower-bound proof.** In the flattening from the last factor to the first two, contraction by `e_0^*` gives `δΣ_i a_i⊗e_i`, and contraction by `e_i^*` gives `a_i⊗e_0`. These `k+1` vectors are independent: the first has second-factor support in `Span(e_1,...,e_k)`, whereas the others have second-factor support in `Span(e_0)` and independent first factors. Thus the flattening has rank `k+1`. A pure tensor has flattening rank at most one, and determinantal rank conditions are closed, so border rank is at least `k+1`.

**Full upper-bound proof and certificate.** For `t≠0` put

`S(t)=t^{−1}[Σ_{i=1}^k a_i⊗(e_0+δ t e_i)⊗(e_0+t e_i)−(Σ_{i=1}^k a_i)⊗e_0⊗e_0]`.

This is a sum of `k+1` pure tensors. Expanding the displayed expression gives exactly

`S(t)=S_{k,δ}+δ t Σ_{i=1}^k a_i⊗e_i⊗e_i`.

It is therefore polynomial in `t` after cancellation and specializes to `S_{k,δ}` at zero. This gives border rank at most `k+1`, and completes the proof. The expression uses no division by an integer: `δ` is a unit in every field, including characteristic two where its two possible values coincide. QED.

## P-04. Exact two-dimensional minima for b=2

**Statement.** For every `n>=3`,

`min_{W∈Gr(2,U_{n,2}^{row det})} BR(P_W)=min_{W∈Gr(2,U_{n,2}^{row per})} BR(P_W)=3`,

and

`min_{W∈Gr(2,U_{n,2}^{poly det})} BR(P_W)=min_{W∈Gr(2,U_{n,2}^{poly per})} BR(P_W)=6`.

**Row proof.** By P-02 it suffices to use the adjacent pair on `{1,2}` and `{1,3}`. This tensor is `S_{2,−1}` for the determinant and `S_{2,+1}` for the permanent, up to harmless changes of signs or labels. Apply P-03. Equivalently, every coordinate pair has last-factor flattening rank the size of the union of its two supports, which is at least three, and this pair realizes equality. QED.

**Polynomial proof.** Let `a=e_{11},b=e_{12},c=e_{13},d=e_{21},e=e_{22},f=e_{23}`. The adjacent pair consists of the ordered coefficient tensors of `ae+σbd` and `af+σcd`, where `σ=−1` for determinant and `σ=+1` for permanent. Its tensor is

`P=a_1⊗(a⊗e+e⊗a+σb⊗d+σd⊗b)+a_2⊗(a⊗f+f⊗a+σc⊗d+σd⊗c)`.

It is the sum of `S_{2,+1}` on the coordinate set `(a,e,f)` and `σ S_{2,+1}` on `(d,b,c)`, using the same first-factor basis `a_1,a_2`. Summing the explicit rank-three curves in P-03 gives a rank-at-most-six curve with limit `P`.

For the lower bound, consider any coordinate pair `(I,J)≠(K,L)`. The coefficient matrix of one generator is nonsingular on the four-dimensional coordinate support `I×J`: it consists of two invertible off-diagonal `2×2` blocks. Its kernel is exactly the span of the coordinate vectors outside this support. Hence the intersection of the two slice kernels is exactly the span of the coordinates outside `(I×J)∪(K×L)`. The pencil flattening therefore has rank

`|(I×J)∪(K×L)|=8−|I∩K| |J∩L|`.

Distinctness excludes the value `|I∩K|=|J∩L|=2`, so the product is at most two, and the rank is at least six. The adjacent pair has product two and rank exactly six. P-01 (or P-02 followed by the explicit lower flattening) gives the uniform bound on every plane. QED.

## P-05. Exact pencil Koszul certificate

For a pencil `P=a_1⊗Q_1+a_2⊗Q_2∈A⊗B⊗C`, with `dim A=2`, define its `p=1` Koszul map

`K_P: A⊗B^* → Λ²A⊗C`, `a⊗β ↦ a_1∧a⊗Q_1(β)+a_2∧a⊗Q_2(β)`.

With basis `a_1∧a_2`, its block matrix is `[-Q_2 | Q_1]` (up to an overall sign convention). For a pure tensor the matrix has rank at most one, which equals the usual cost `binom(dim A−1,1)=1`. Thus `BR(P)>=rank K_P`. For the coordinate polynomial pencils the two symmetric slice matrices have images exactly their respective coordinate supports, so

`rank K_P=8−|I∩K| |J∩L|>=6`.

For coordinate row pencils its rank is the size of the union of the two edges, hence at least three. The adjacent pairs give ranks six and three. The lower certificates in P-04 are therefore also explicit Koszul certificates, including the atom cost. Here the two-dimensional Koszul map is an ordinary flattening after a basis change; no stronger nontrivial Koszul bound is needed to reach the exact minimum.

## Consequence when combined with border substitution

The generalized border-substitution inequality is `BR(T)>=q−j+min_{W∈Gr(j,U)}BR(P_W)`; the parent agent owns its full independent proof. With `j=2,b=2`, P-04 gives `BR(D_n),BR(P_n)>=binom(n,2)+1` and `BR(poly det_n),BR(poly per_n)>=binom(n,2)^2+4`, in particular the polynomial lower bound **40** at `n=4`. The result concerns CP border rank and therefore also lower-bounds symmetric border rank in characteristic zero. It makes no priority claim pending the parent's literature audit.

## P-06. Exact border rank for every anchored shape of quadratic minors/permanents

**Statement.** Let `H⊆{1,...,r}×{1,...,s}` be a nonempty bipartite edge set using every row and column vertex, with `h=|H|`. Let `a,x_1,...,x_r,y_1,...,y_s,z_ij ((i,j)∈H)` be an independent coordinate basis, and let `A` have basis `c_ij ((i,j)∈H)`. For `σ=±1` set

`T_H=Σ_{(i,j)∈H} c_ij ⊗ [(a⊗z_ij+z_ij⊗a)+σ(x_i⊗y_j+y_j⊗x_i)]`.

Then `BR(T_H)=h+r+s+1` over every algebraically closed field. These are precisely the coefficient tensors of a coordinate collection of minors/permanents all sharing the same anchor entry `a`, provided the row-pair and column-pair sets themselves are stars at the anchor.

**Lower-bound proof.** Every one of the `h+r+s+1` variables occurs in some slice. Each slice is a nonsingular signed matching on its four-variable support. Their common kernel is consequently the complement of the union of those supports, which here is zero. Thus the last-factor flattening has rank `h+r+s+1`. Closedness of matrix rank conditions gives the lower bound.

**Upper-bound proof and explicit certificate.** Introduce vectors

`v_00(t)=a`,

`v_i0(t)=a+t x_i`,

`v_0j(t)=a+t y_j`,

`v_ij(t)=a+t x_i+t y_j+σ t² z_ij`, for `(i,j)∈H`.

Define

`T(t)=σt^{−2}Σ_{(i,j)∈H} c_ij⊗[v_ij(t)⊗v_ij(t)−v_i0(t)⊗v_i0(t)−v_0j(t)⊗v_0j(t)+v_00(t)⊗v_00(t)]`.

For each edge, expansion cancels the constant and linear terms, and the quadratic coefficient is

`σ[(x_i⊗y_j+y_j⊗x_i)+σ(a⊗z_ij+z_ij⊗a)]`,

which equals the corresponding slice of `T_H`. The remaining terms have positive powers of `t` after multiplication by `t^{−2}`. Hence `T(t)` is polynomial after cancellation and `T(0)=T_H`.

For `t≠0`, group terms by their displayed second/third factor vector. There are `h` vectors `v_ij`, `r` vectors `v_i0`, `s` vectors `v_0j`, and one vector `v_00`, and each has a single (possibly zero) first-factor coefficient. This expresses `T(t)` as a sum of at most `h+r+s+1` pure tensors. The limiting argument proves the upper bound. Nothing in this calculation divides by two or by a characteristic-dependent scalar. QED.

**Examples relevant to the parent's finite enumeration.** A two-edge star has `(h,r,s)=(2,1,2)` and gives border rank six (P-04). Three entries in a common anchored row have `(3,1,3)` and give eight. The complete `2×2` anchored grid has `(4,2,2)` and gives nine. A five-edge anchored shape in a `2×3` grid has border rank eleven. These examples are upper witnesses; identifying them with global minima requires the corresponding uniform lower bounds over all coordinate subsets.

**Geometric dictionary.** The `h+r+s+1` vectors define sections of the affine vector space over `A^1`; their squares define a finite family of sections of the Veronese cone. The alternating four-term difference is a mixed second finite difference. It yields the second-order tangent terms of the Segre parametrization through the anchor, together with independent normal coordinates. The certificate is the displayed family in the secant cone, so it does not rely on a generic smoothability assertion or a classification of finite schemes.

## P-07. Determinant minima reduce further to order ideals

**Statement.** In either determinant family, the coordinate subsets in P-01 may be restricted to lower order ideals of cardinality `j`. The order is componentwise order on increasing `b`-subsets for the row determinant, and product componentwise order on pairs of increasing `b`-subsets for the polynomial determinant. This holds for every `n,b,j` and every algebraically closed field. No corresponding statement for the permanent is asserted.

**Full proof.** Fix two coordinate indices `v>u` and apply the elementary transvection `g(t):e_v↦e_v+t e_u`, fixing all other coordinate basis vectors. In `Λ^b` its action on a coordinate wedge has exactly the following forms. If its index subset contains `v` and does not contain `u`, it sends

`Q_I ↦ Q_I+ε_I t Q_{(I\{v})∪{u}}`, with `ε_I=±1`.

If the subset does not contain `v`, the vector is fixed. If it contains both `v,u`, the extra wedge has a repeated coordinate and is zero, so again the vector is fixed. The nontrivial actions form disjoint two-element chains, consisting of an upper basis vector and its fixed lower partner. In the polynomial determinant family, use this action on the row indices while holding the column index fixed, or on the columns while holding the row index fixed. The same disjoint-chain description follows from the exterior-power representation of minors (equivalently, expand each determinant along the affected row or column). All signs are units, including in characteristic two.

Now take a coordinate plane. In a chain where both upper and lower partners are selected, their span is unchanged by `g(t)` and one may choose the original two vectors as a frame of the transformed plane. In a chain where only the lower partner is selected, that vector is fixed. In a chain where only the upper partner is selected, put `t=s^{−1}` and replace the transformed frame vector by `sQ_upper+εQ_lower`; its specialization at `s=0` is `εQ_lower`. Distinct chains have distinct lower partners, and the latter are absent from the original selected subset in precisely these cases. Thus this procedure supplies a polynomial family of independent frames at `s=0`, with coordinate-plane limit obtained by replacing every selected orphan upper partner by its lower partner. For `s≠0` it is a product-group transform of the original residual tensor, including an invertible change of basis in its `j`-dimensional first factor. Border rank cannot increase in the limit.

Whenever a replacement occurs, the sum of the integer coordinate indices of all selected subsets strictly decreases. Repeat any available lowering transvection. The sum is a nonnegative integer, so the process terminates. At termination, replacing any selected index `v` by a smaller absent index `u` leaves a selected basis vector. These elementary replacements generate componentwise order on increasing `b`-subsets: for `J≤I`, replace the first unequal coordinate of `I` by the corresponding coordinate of `J`, and repeat (or use the usual monotone subset path). Hence the terminal coordinate subset is a lower order ideal. The same argument separately in rows and columns gives an ideal of the product poset.

Starting with P-01, every plane therefore degenerates to an order-ideal plane of no larger border rank. Conversely every such plane is an allowed plane, proving equality of the minima. QED.

**Geometric dictionary.** The torus and elementary lowering root subgroups generate the relevant split Borel group scheme inside `GL_n` or `GL_n×GL_n`. The terminal ideals are the coordinate subspaces stable under that Borel. The argument gives explicit degenerations realizing the usual Borel-fixed reduction on the Grassmannian; it does not assume semisimplicity in positive characteristic. The permanent residual image is not stable under these unipotent groups, because repeated-coordinate terms need not vanish, so the proof's exterior-power step fails there.

## P-08. A first-prolongation necessary condition for border rank

**Statement.** Let `T∈A⊗B⊗C`, let `U=T(C*)⊂A⊗B`, and suppose `dim(A⊗B)>=r>=dim U`. If `BR(T)<=r`, there is an `r`-plane `L⊂A⊗B` containing `U` for which both maps

`d_A:A⊗L→Λ²A⊗B`, `a⊗(x⊗y)↦(a∧x)⊗y`,

`d_B:L⊗B→A⊗Λ²B`, `(x⊗y)⊗b↦x⊗(y∧b)`,

have kernel dimension at least `r`. This holds over every algebraically closed field. The kernels are the first prolongations along the respective factors; in characteristic zero they can be identified with intersections with `Sym²A⊗B` and `A⊗Sym²B`. In positive characteristic the displayed exterior-power kernels are the definition, so no division by two is used.

**Full proof.** First suppose `T` has rank at most `r`, and choose a decomposition with at most `r` pure `A⊗B` atoms. Choose a basis of their span from these atoms. Since the pure `A⊗B` atoms span all of `A⊗B`, extend that independent list to `r` independent pure atoms `x_i⊗y_i`, and let `L` be their span. It contains `U`. The `r` tensors `x_i⊗(x_i⊗y_i)` lie in `ker d_A`. Choose a linear functional on `A` nonzero on all the finitely many nonzero vectors `x_i`; it exists because the algebraically closed field is infinite. Contracting the first `A` factor sends these tensors to nonzero scalar multiples of the independent atoms `x_i⊗y_i`, so they are independent. Thus `dim ker d_A>=r`. The same contraction argument on `B` proves `dim ker d_B>=r`.

On the Grassmannian `Gr(r,A⊗B)`, the maps `d_A,d_B` are morphisms of vector bundles built from the tautological rank-`r` bundle. The conditions `dim ker d_A>=r` and `dim ker d_B>=r` are closed determinantal rank conditions. The incidence condition `im T(C*)⊂L` is also closed. Their joint incidence variety in tensor space times the Grassmannian projects to a closed subset of tensor space because the Grassmannian is projective. The preceding paragraph places every rank-at-most-`r` tensor in this projection. Therefore it also contains their Zariski closure, proving the assertion for border rank. QED.

**Attribution and scope.** This is the elementary first-prolongation / low-degree border-apolarity necessity behind the `(210)` and `(120)` tests. It is not a sufficiency assertion. The proof is included to make the precise arbitrary-characteristic form and the atom-span padding explicit; the parent's literature audit supplies the Conner--Harper--Landsberg locator.

## P-09. The exceptional five-permanent tensor has border rank eleven

**Tensor.** Use the nine variable basis `a,b,c,d,e,f,g,h,i` in row-major order in a `3×3` matrix, and the five slice labels `c_1,...,c_5`. Let `T_5` have slices the ordered symmetric coefficient matrices of

`q_1=ae+bd`, `q_2=af+cd`, `q_3=bf+ce`, `q_4=ah+bg`, `q_5=ai+cg`.

**Lower-bound proof.** Set `A=k^5`, `B=C=k^9`, and `U=T_5(C*)⊂A⊗B`. The last-factor flattening has rank nine: every variable is used in a slice, each slice is a signed matching on its four-variable support, and their common kernel is zero. Hence `dim U=9`.

Let the split row/column torus have variable characters `w_{ij}=R_i+C_j`, for `0<=i,j<=2`. Give the slice basis vector corresponding to row pair `I` and column pair `J` the character `−Σ_{i∈I}R_i−Σ_{j∈J}C_j`. Give both `B` and `C` their variable characters. Every supported term of `T_5` has total weight zero, so this torus stabilizes `T_5`; consequently it preserves `U` and all conditions in P-08.

If `BR(T_5)<=10`, P-08 supplies an admissible ten-plane `L` containing `U`. The closed set of such admissible planes is projective and torus-invariant. Take its limit under a one-parameter subgroup which separates all distinct torus weights on `A⊗B`. This limit remains admissible and is a direct sum of weight subspaces (one may use echelon reduction weight by weight, as in P-01). Thus it is torus-invariant. Since `L/U` is one-dimensional, it has a single weight `w`; writing `V_w` for the full weight space in `A⊗B`, one has `L⊂U+V_w`.

The basis coordinates `c_q⊗e_v` give **28** distinct weights on `A⊗B`. The image `U` has nine distinct weights, namely the negatives of the nine variable characters. Two weight blocks have zero image in `(A⊗B)/U`; the other **26** are the complete possible list for `L/U`. Their quotient dimensions are one, two, or three. For each of those 26 weights set `L_w=U+V_w`. The complete certificate `per5_prolongation_certificate.json` constructs a basis of `L_w`, constructs both maps `d_A` and `d_B` for that basis, and supplies a square minor of one of those two maps of order

`dim(domain of d_A or d_B)−9`,

whose determinant over `Z` is `+1` or `−1`. Thus that map's kernel on `L_w` has dimension at most nine. Since the prolongation kernel for a subspace `L⊂L_w` is contained in the corresponding kernel for `L_w`, the same upper bound holds for the hypothetical ten-plane `L`. This contradicts P-08.

For complete reproducibility, the source script `per5_prolongation_certificate.py` builds the five slice matrices directly from their rectangles, not by importing the parent's Koszul script; creates the 28 weight classes by six-component integer character vectors; excludes the two zero quotient blocks; constructs the two wedge-map matrices by their defining formula; and evaluates each certified minor as an integer determinant. All 26 needed determinants are units. Therefore this proof holds in every characteristic, rather than merely away from primes detected by a modular computation. The modular elimination used to locate minors is followed by the exact integer determinant calculation. QED for the lower bound.

**Upper-bound proof and explicit eleven-term degeneration.** Let the parameters be `u,w,y,z` and put

`v(u,w,y,z)=(r_0+u r_1+w r_2)⊗(s_0+y s_1+z s_2)`

in the nine-dimensional matrix-coordinate space. In the tensor-valued polynomial `F=v⊗v`, the coefficients of the five squarefree parameter monomials `uy,uz,uyz,wy,wz` are exactly the five displayed ordered symmetric quadrics. This follows by expansion: for example the coefficient of `uy` is `a⊗e+e⊗a+b⊗d+d⊗b`, and that of `uyz` is `b⊗f+f⊗b+c⊗e+e⊗c`.

For a set `S` of parameters, define its finite difference

`D_S(t)=t^{−|S|}Σ_{R⊂S}(−1)^{|S|−|R|}F(t·1_R)`.

The Boolean inclusion-exclusion identity kills every monomial whose support is a proper subset of `S`, and parameters outside `S` are zero. Hence `D_S(t)` is polynomial in `t` after cancellation and its value at zero is the coefficient of the squarefree monomial with support `S`. Terms with the same support and larger total degree acquire positive powers of `t`.

Take `T(t)=Σ_{h=1}^5 c_h⊗D_{S_h}(t)`, with `S_h=uy,uz,uyz,wy,wz` in that order. Every evaluation `F(t1_R)` is a pure square tensor. The union of all subsets `R⊂S_h` consists of the eight subsets of `{u,y,z}` and the three further sets `{w},{w,y},{w,z}`, hence has cardinality eleven. Grouping the first-factor coefficients by these eleven evaluation points expresses `T(t)` for `t≠0` as a sum of at most eleven pure tensors. Its limit is `T_5`, so `BR(T_5)<=11`. The finite-difference identity is over `Z`, with no factorial division. Combined with the lower bound, this proves `BR(T_5)=11` over every algebraically closed field. QED.

**Related upper witness.** Adding the sixth slice `q_6=bi+ch` corresponds to the monomial `wyz`; its divisor set adds only `{w,y,z}`. Thus the analogous six-permanent tensor has border rank at most twelve, by an explicit twelve-term degeneration. A matching lower bound is a separate question.

**Geometric dictionary.** P-08 is a closed determinantal condition on the tautological bundle over a Grassmannian, followed by a proper image. P-09 uses the split torus of the row and column group schemes and the weight decomposition of their representation on `A⊗B`. The unit minors make the obstruction a scheme-theoretic statement over `Z`; the finite-difference family is an integral curve in the relevant Segre secant cone. The construction sits in the low-degree Hilbert-function tests of border apolarity, which use limits of ideals of reduced points rather than numerical norms.

## Proof-check status

All proofs above were read in full by their author after drafting, with the following checks: the torus has distinct characters on every basis vector; row-echelon normalization gives an actual polynomial degeneration; row/column identifications are injective on each selected term; signs are units in every characteristic; star approximants contain exactly `k+1` pure tensors; common slice kernels really are coordinate complements; and the Koszul atom cost is one. A separate symbolic checker is supplied for the star and polynomial degenerations and finite coordinate support ranks. The parent is asked to perform an independent whole-proof read before marking these findings fully checked in the final paper.
