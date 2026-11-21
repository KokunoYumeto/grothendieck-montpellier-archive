# F56: a coherent coefficient-kernel realization and its exact completion limits

Author: /root/gct_statements, GPT-6 Astra Pro. Inherited effort is not exposed. Date: 2026-11-21 UTC.

This report develops the concrete coefficient-object alternative left open by F54. The quadratic isomorphism was already noted briefly in F43; it is not presented here as a new discovery. The additions are an explicit full presentation-relation lift, the ordered overlap comparison, an exact split-Grothendieck-ring statement, the complete Karoubi calculation for the actual 64 states and faithful six states, adjoint exclusion, and a fixed-q arithmetic coefficient realization. These are not identifications with VIII's designated bases or a categorical presentation supplied by GCT.

## 1. Category and actual matrices

Let k be a characteristic-zero field and let V be the category of finite-dimensional Z-graded k-vector spaces, with degree-preserving maps. Use ordinary tensor symmetry, with no Koszul signs: the grading here is formal quantum degree, not cohomological parity. Let k<d> have degree d. Set

\[
\Lambda=\mathbb Z[v,v^{-1}],\qquad
\operatorname{ch}(U)=\sum_d\dim_k(U_d)v^d.
\]

For a finite state set I, define the category Mat_I(V) of matrices of graded spaces. Morphisms are entrywise degree-preserving linear maps. Convolution is

\[
(K\star L)_{ij}=\bigoplus_{h\in I}K_{ih}\otimes L_{hj}.
\tag{C1}
\]

The unit has k on the diagonal and zero elsewhere. This is an additive monoidal category. It acts on row vectors of graded spaces by

\[
(T_K X)_j=\bigoplus_i X_i\otimes K_{ij},
\]

with T_L composed with T_K naturally isomorphic to T_(K star L). All maps below are actual natural transformations of these functors.

Take the 64 states of the regular positive F43 basis. The actual right action decomposes as 20 scalar-plus states, 4 scalar-minus states, 16 copies of N(delta), and 4 copies of N(D−2). Define coefficient spaces

\[
A_1=k<-1>\oplus k<1>,\qquad
A_2=k<-2>\oplus k<2>,\qquad
\mathcal D=A_1\otimes A_1.
\tag{C2}
\]

Their characters are delta, D−2, D, respectively, where delta=v+v^−1 and D=delta². In particular D has two separate degree-zero basis labels.

On a two-state N(A) block, with A=A_1 or A_2, use the kernels

\[
K_1=\begin{pmatrix}\mathcal D&0\\A&0\end{pmatrix},
\qquad
K_2=\begin{pmatrix}0&A\\0&\mathcal D\end{pmatrix}.
\tag{C3}
\]

These follow the source's right-row convention exactly. On each plus scalar state both kernels are D, and on each minus state both are zero. Their entrywise characters are the actual P_1,P_2 matrices, not merely matrices with matching traces.

The F43 basis is a basis of the actual tensor lattice after the proved finite localization. Its global change of basis need not preserve the original tensor-monomial integral form. The category below therefore makes no new global-lattice assertion.

## 2. Concrete monoidal coherence

For a word of kernels K_1,...,K_m, every parenthesized convolution has the canonical flattened expression

\[
\bigoplus_{i_1,\ldots,i_{m-1}}
(K_1)_{i_0i_1}\otimes\cdots\otimes(K_m)_{i_{m-1}i_m}.
\tag{C4}
\]

The associator is the map preserving the state sequence and the ordered list of tensor factors. Every route around an associator pentagon has precisely this same action on every pure tensor in every state summand. Thus the pentagon commutes. The unit maps have the same direct verification. This proves the monoidal coherence used here without a dimension-only argument.

Coefficient spaces are central by the ordinary tensor symmetry. A permutation of a list of coefficient factors acts by permuting the corresponding pure tensors. Adjacent swaps satisfy the square, distant-commutation, and braid relations because they give the same permutation of positions. Therefore all comparisons which have the same labeled factor permutation agree.

These are concrete category/action statements. They do not assume that every rewriting loop in an unspecified higher presentation must be the identity.

## 3. Quadratic maps and their actual overlap

On a two-state block, K_i is a reset to state i. Its only nonzero column is i. For an initial state h,

\[
(K_i\star K_i)_{hi}=(K_i)_{hi}\otimes\mathcal D.
\]

This gives the natural quadratic isomorphisms

\[
K_i\star K_i\simeq K_i\otimes\mathcal D
                 \simeq\mathcal D\otimes K_i.
\tag{C5}
\]

The first map is the explicit path identification; the second is tensor symmetry. On the scalar-plus blocks the same statement is D tensor D, and on scalar-minus blocks it is zero.

For every m>=1, the unique reset state sequence gives

\[
K_i^{\star m}\simeq K_i\otimes\mathcal D^{\otimes(m-1)}
\tag{C6}
\]

by preserving the initial edge and the chronological list of the subsequent m−1 loops. This map is independent of convolution parenthesization by (C4).

There is a real overlap to record if one moves every extracted coefficient to the left. Let q be the left-coefficient version in (C5), so on a tensor V_h tensor D it flips the two factors. In a triple word label the factors by

\[
u\otimes d_1\otimes d_2
 \in (K_i)_{hi}\otimes\mathcal D_1\otimes\mathcal D_2.
\]

Reducing the first pair and then the remaining pair gives

\[
d_1\otimes d_2\otimes u.
\]

Reducing the last pair, moving its central coefficient left, and then reducing the remaining pair gives

\[
d_2\otimes d_1\otimes u.
\tag{C7}
\]

Thus the comparison is the ordinary transposition of the two D factors. It is not the identity: take their two distinct degree-zero basis labels. It is also not an obstruction to categorical coherence. The symmetry is exactly the comparison that the ordered factors require.

More generally, any binary reduction tree gives a permutation sigma_T of the m−1 labeled internal D factors, with the original initial edge retained. This follows inductively because every local map is a factor permutation and never changes the labels or the retained edge. Comparing two normal forms by sigma_T' sigma_T^−1 gives actual natural coefficient permutations. All normal-form comparison pentagons telescope to the identity permutation. The same maps agree with the elementary symmetric-group relations just checked.

Consequently the repeated-power maps have coherent ordered coefficient bookkeeping. They do not assert gratuitous strict confluence after forgetting the labels. Changing to another quadratic isomorphism would change these comparison maps and would require its own check.

## 4. The actual degree-five relation has an explicit natural lift

The precise source input is IV Theorem 11.16, equations (111)–(112), printed p65. With a_1=delta, a_2=D−2 it reads

\[
P_i^2=DP_i,\qquad
P_1(P_2P_1-a_1^2)(P_2P_1-a_2^2)
=P_2(P_1P_2-a_1^2)(P_1P_2-a_2^2).
\tag{C8}
\]

Let V_1=K_1 star K_2 star K_1 and W_1=K_1 star K_2 star K_1 star K_2 star K_1; use V_2,W_2 for the mirrored words. Put

\[
U=A_1^{\otimes2},\qquad V=A_2^{\otimes2},\qquad
\mathcal S=U\oplus V,\qquad \mathcal T=U\otimes V.
\]

The positive rearrangement of the second relation is the pair of kernel objects

\[
L=W_1\oplus(V_2\otimes\mathcal S)\oplus(K_1\otimes\mathcal T),
\]

\[
R=W_2\oplus(V_1\otimes\mathcal S)\oplus(K_2\otimes\mathcal T).
\tag{C9}
\]

Here is an explicit natural isomorphism L to R.

On an N(A) block, every internal step of an alternating word is the A edge. Therefore

\[
V_j\simeq K_j\otimes A^{\otimes2},\qquad
W_j\simeq K_j\otimes A^{\otimes4},
\tag{C10}
\]

with maps preserving all chronological edge factors.

For A=A_1, expand S in its displayed order. The four left and right summands are

\[
L=(K_1UU,\ K_2UU,\ K_2UV,\ K_1UV),
\]

\[
R=(K_2UU,\ K_1UU,\ K_1UV,\ K_2UV).
\]

Map them by the permutation (1 2)(3 4), using identities on each coefficient tensor. Juxtaposition here means tensoring the displayed coefficient spaces on the right.

For A=A_2, the lists are

\[
L=(K_1VV,\ K_2VU,\ K_2VV,\ K_1UV),
\]

\[
R=(K_2VV,\ K_1VU,\ K_1VV,\ K_2UV).
\]

Map left positions 1,2,3,4 to right positions 3,4,1,2, respectively. The 1-to-3 and 3-to-1 maps are identities. The other two maps interchange the U and V coefficient blocks by ordinary tensor symmetry.

On scalar-plus blocks K_1=K_2=D, so use the termwise identical expressions D^5, D^3 S, D T. On minus blocks all terms are zero. These blockwise maps define a degree-preserving natural isomorphism of the full 64-state kernels. The same maps on every multiplicity copy commute with its matrix-unit action.

This construction uses no equality-of-dimensions shortcut: every summand and every tensor-factor map has been specified. Exchanging the two generator labels gives the inverse map. This can be checked directly from the two lists: the permutations reverse, and the U/V interchange is inverted by the opposite interchange. Tensoring these maps with arbitrary kernel contexts gives the usual natural relation maps; maps applied in disjoint contexts commute by the interchange law for linear tensor maps.

The degree-five maps introduce only the displayed direct-summand permutations and coefficient-factor symmetries. Within the concrete matrix-kernel category all associator and symmetry coherence already holds by Section 2, and the repeated quadratic reductions have the ordered comparisons of Section 3. A particular additional higher relation among overlapping degree-five 2-morphisms has not been specified in the GCT algebra presentation. No assertion that every possible rewriting loop is the identity is being substituted for such a missing specification. What has been constructed is a coherent monoidal category/action with explicit isomorphisms for both defining algebra relations.

## 5. Exact split Grothendieck algebra

Let P_64 be the full additive subcategory of Mat_64(V) whose objects are finite direct sums of grading shifts of convolution words in I,K_1,K_2. Include all isomorphic objects; do not close under arbitrary direct summands. The full morphism condition means that every entrywise graded linear map between the chosen objects is included.

It is closed under convolution and shifts, so it is an additive monoidal category with the already proved coherence. Use its split exact structure. Let

\[
A_\Lambda^{\mathrm{act}}
  =\Lambda\langle P_1,P_2\rangle
       \subset\operatorname{Mat}_{64}(\Lambda)
\tag{C11}
\]

be the concrete actual algebra image in the F43 basis, including the identity. Then

\[
K_0^{\mathrm{split}}(P_{64})
       \simeq A_\Lambda^{\mathrm{act}}
\tag{C12}
\]

as rings, with K_i mapping to the actual named P_i and a grading shift mapping to v.

Here is the full cancellation argument. Isomorphism classes of finite graded matrix kernels are determined by the entrywise graded dimension matrix. If two such matrices agree, choose an isomorphism in every homogeneous entry; because P_64 is full, the resulting isomorphism belongs to P_64. Thus its object monoid embeds into Mat_64(N[v,v^−1]) and is cancellative. Its image is exactly the semiring of finite nonnegative Laurent combinations of actual word matrices.

Group completion is injective into Mat_64(Lambda): if two formal differences have the same image, cross-addition gives identical graded dimension matrices, hence an actual kernel isomorphism and the same class in the split group. Its image is exactly the Z-linear span of all shifted word matrices, which is (C11). Convolution respects the matrix product, proving (C12).

This is an actual split-K0 algebra realization, not the full ambient matrix algebra. Over Q(v), the four actual generic simple types all occur in the tensor representation. Thus the actual rank-three algebra acts faithfully; its generic dimension is ten. Equivalently, removing redundant multiplicity copies preserves exactly the same word relations. After the previously proved finite localization, (C11) is the actual order of F19.

The split qualifier is essential. P_64 is not being asserted abelian, semisimple with its own simple-object decomposition, idempotent complete, or a category with the prescribed canonical bases. Its positive object monoid is not automatically a free canonical-basis cone.

## 6. Exact Karoubi completion on the actual 64 states

The unit kernel already has 64 independent state idempotents in its endomorphism algebra. P_64 is full, so these morphisms exist, although their images need not yet be objects of P_64.

In its Karoubi completion they split and give E_ii for every state. On any two-state block, E_22 star K_1 star E_11 has the A edge in its (2,1) entry. Projection onto one homogeneous basis line and an inverse grading shift gives E_21. Similarly K_2 gives E_12. Together with E_11,E_22 this supplies every elementary two-by-two matrix kernel, in every grading. Each scalar state supplies its one elementary diagonal kernel.

No word kernel has entries between distinct displayed copies of the scalar or two-state blocks. An entrywise idempotent summand cannot create a new nonzero matrix entry. Therefore the Karoubi category is exactly the block-diagonal matrix-kernel category

\[
\operatorname{Kar}(P_{64})
 \simeq V^{24}\times \operatorname{Mat}_2(V)^{20},
\tag{C13}
\]

as additive monoidal categories. To see fullness of the object assertion, every block-diagonal finite graded matrix is a direct sum of the elementary shifted kernels just constructed. Conversely every idempotent image remains such a block-diagonal matrix. The full ambient morphisms give the asserted equivalence.

Consequently

\[
K_0^{\mathrm{split}}\operatorname{Kar}(P_{64})
 \simeq \Lambda^{24}\times M_2(\Lambda)^{20}.
\tag{C14}
\]

This has rank 24+4(20)=104 over Lambda. There are 104 elementary simple-kernel families up to grading shift, and 64 simple summands of the unit. It is not M_64(Lambda): the chosen right generators never connect distinct multiplicity copies.

Thus the actual ten-dimensional algebra image in (C12) changes substantially upon this natural semisimple completion. The new elementary positive basis belongs to (C14), not to the actual algebra.

## 7. Faithful six-state completion: the normalization order

Remove redundant multiplicities and keep one copy of each scalar type and each two-state type. This gives six states and a faithful auxiliary representation with exactly the same word-algebra relations. The analogous category P_6 still has split K0 equal to the same actual algebra image.

Its Karoubi completion is

\[
V^2\times\operatorname{Mat}_2(V)^2,\qquad
K_0^{\mathrm{split}}\operatorname{Kar}(P_6)
 =\Lambda^2\times M_2(\Lambda)^2.
\tag{C15}
\]

It has ten simple-kernel families up to shift, so in this smaller representation the generic rank remains ten. The integral order changes.

Localize over R=Q[v,v^−1]_(v−1), where all the previously used regular comparisons are defined. The actual center is

\[
C=R[x]/(x(x-\Delta)).
\]

Its map to the split branch center R×R is

\[
f_0+f_1x\longmapsto(f_0,f_0+\Delta f_1).
\tag{C16}
\]

Its image consists exactly of pairs congruent modulo Delta, and its cokernel is R/(Delta). Since ord_(v−1)(Delta)=2, the center cokernel has length two; the matrix-factor cokernel has length eight. After the regular F21 branch changes of basis, the completed kernel algebra is exactly the split normalization order

\[
R^2\times M_2(R)^2.
\]

The actual special fiber has center Q×Q×Q[epsilon]/epsilon² and a four-dimensional matrix radical, with dimensions over Q; the same statements hold after extension to C. The completed split order has a reduced split center. The specialization of the actual embedding kills precisely that four-dimensional radical and has six-dimensional image. This follows either directly from (C16) on four matrix entries or from the already proved F19 specialization map.

Thus equal generic rank does not repair the collision comparison. The six-state completion has forgotten precisely the branch contact carried by the actual order.

## 8. Adjoints exist in the ambient category but not in the word category

For finite graded coefficient spaces, the left and right adjoint kernels are both the transpose graded dual:

\[
(K^\dagger)_{ij}=(K_{ji})^*.
\tag{C17}
\]

Indeed, the usual finite-dimensional tensor-Hom adjunction, applied entrywise to (C1), gives the natural adjunction isomorphisms. Graded dual reverses degree. The chosen D,A_1,A_2 are self-dual as graded spaces, so on N(A),

\[
K_1^\dagger=\begin{pmatrix}\mathcal D&A\\0&0\end{pmatrix},
\qquad
K_2^\dagger=\begin{pmatrix}0&0\\A&\mathcal D\end{pmatrix}.
\tag{C18}
\]

Neither K_i is isomorphic to its adjoint, even after any grading shift: their matrix supports differ.

More strongly, neither adjoint is an object of P_64 or P_6. For a nonempty right-generator word w=i_1...i_L, its actual two-state matrix is

\[
P_w=D^{L-1-t}a^t u_{i_1}e_{i_L}^{T},
\quad
u_1=(D,a)^T,\quad u_2=(a,D)^T,
\tag{C19}
\]

where t counts ordinary adjacent changes. This follows by multiplying the rank-one matrices, or directly from the unique reset path. At v=1, D=4 and a=2, so both rows of every such word are nonzero. The identity also has both rows nonzero. Every nonzero object of the word category is a positive sum of shifted words, and shifts evaluate to one at v=1. Its restriction to either two-state block therefore has both rows nonzero. There is no cancellation.

But K_1 dagger has zero second row, and K_2 dagger has zero first row, while each is nonzero. This contradiction proves exclusion from the word category. Adjoints thus force an enlargement even before requiring arbitrary idempotent splittings.

This is not a claim that the adjoint's linear operator is outside every localization of the actual algebra; the conclusion is precisely about the positive word-kernel object category. The Karoubi completion does contain the transpose-dual kernels and all their elementary summands.

## 9. Fixed-q arithmetic coefficient objects

The formal graded construction has an exact arithmetic coefficient interpretation. Fix a prime power q and a prime ell different from its characteristic. Choose the algebraic number lambda=sqrt(q)>0 under a specified complex embedding, and choose its ell-adic realization in a finite coefficient field E. Let L be the one-dimensional Weil representation with geometric Frobenius lambda. Send

\[
k<r>\longmapsto L^{\otimes r},
\tag{C20}
\]

using E-linear graded spaces. This extends by direct sums and tensors to an exact symmetric monoidal functor to finite Weil representations.

It is fully faithful onto the semisimple subcategory generated by these lines: lambda^r=lambda^s forces r=s, since an archimedean conjugate has magnitude q^((r−s)/2), and morphisms between distinct Frobenius characters vanish. Equal-degree Hom spaces are the same coefficient-linear maps. Every map constructed in Sections 2–4 is degree preserving, so it is a Frobenius morphism under (C20).

The lines are also continuous unramified representations of the finite-field Galois group. Since ell does not divide q, lambda is an ell-adic unit; its powers lie in the compact profinite unit group of a finite coefficient extension. The homomorphism from Z generated by lambda extends to its profinite completion. This is the explicit continuity criterion already used in F46.

For every n,

\[
\operatorname{Tr}(\operatorname{Frob}^n\mid
 \bigoplus_r V_r\otimes L^r)
 =\sum_r\dim(V_r)q^{rn/2}.
\tag{C21}
\]

Thus coefficient traces make exactly the substitution v=q^(n/2). The coefficient object D becomes L² direct-sum two trivial lines direct-sum L^−2. The quadratic and degree-five object isomorphisms survive at every extension degree. The original quantum relation is thereby retained as a tensor relation with a changing coefficient object, not as the fixed scalar D(sqrt(q)) on one finite space.

If one instead sends degree one to Q_ell(−1), with geometric Frobenius q, the construction uses an honest full Tate step and substitutes v=q^n. The half-step line above is a Weil coefficient line; it is not asserted to be a geometric Tate object.

The direct sums of different degrees are generally mixed in weight. The kernels are changing functors and a word has its own finite trace object. This is not a simultaneous realization of all word traces as fixed endomorphisms of one finite pure tensor representation; it therefore does not contradict F42 or F54. Nor does it identify the coefficient category with a nonstandard geometric category having VIII's designated integral forms.

### 9.1 Actual perverse kernels by the established Gaussian functor

Assume q is odd and retain the fully proved F53 functor J from finite Weil spaces to its full perverse Gaussian image P_psi. It is exact, fully faithful, and symmetric strong monoidal for the specified convolution star_psi, with image unit J(E). Its symmetry is the transported one of F53, not the naive odd-shift kernel swap.

For matrices of objects in P_psi, define

\[
(\mathcal K\star\mathcal L)_{ij}
 =\bigoplus_h\mathcal K_{ih}\star_\psi\mathcal L_{hj}.
\tag{C22}
\]

The unit is diagonal J(E). Apply J entrywise after (C20). Its direct-sum comparisons and the specified maps J(C) star_psi J(C') isomorphic to J(C tensor C') give

\[
J_I(K\star L)\simeq J_I(K)\star J_I(L).
\tag{C23}
\]

These comparisons are coherent: expand an iterated matrix product by its intermediate state sequence, and on each tensor summand use the already proved F53 strong-monoidal comparison. Every associator pentagon agrees on every summand, and finite direct sums preserve those equalities. Entrywise full faithfulness and exactness are inherited from J. The matrix action on P_psi^I follows by the same formula.

Consequently all the explicit quadratic, degree-five, inverse, tensor-context, and ordered-overlap maps in this report become actual perverse morphisms, with the same coherence comparisons. This is stronger input than a Laurent K0 equality: the coefficient maps have been constructed before applying J.

A homogeneous degree-d coefficient line is the Weil line L^d of weight d under the half-step convention. F53 makes J(L^d) perverse pure of weight d. Arbitrary coefficient spaces are the specified finite direct sums of these known-weight pieces; no single purity weight is asserted for their total. Under the full Tate-step convention the weights are 2d.

The split-K0, Karoubi, and adjoint conclusions carry to this full image by equivalence. They do not describe every perverse sheaf in the ambient constructible category. After forgetting arithmetic descent, the lines L^d become ordinary constant coefficient lines, so their Gaussian images have the same underlying geometric rank-one constituent; the degree labels remain arithmetic/grading data, not new geometric cell labels.

This supplies actual geometric operations for the rank-three coefficient-object construction. It does not supply compatible positive graded kernels through all tensor degrees, or the prescribed global/local lattices, canonical simple labels, or independent pointwise weight bounds. The fixed-parameter all-degree realization of F53 and the present rank-three graded realization remain distinct statements.

## 10. Exact coherence and canonical-basis scope

The construction supplies:

- a concrete additive monoidal category and its actual action;
- full associator/unit coherence by flattened path tensors;
- explicit quadratic and degree-five relation isomorphisms;
- ordered coefficient-overlap comparisons satisfying their permutation pentagons;
- an exact split-K0 algebra identification with the actual Laurent word algebra;
- exact completion and adjoint calculations;
- an all-extension arithmetic coefficient-object interpretation.

It does not supply a source-prescribed higher 2-presentation, a semisimple category whose designated simple classes are the actual canonical basis, a summand-complete category preserving the collision order, or the global and local lattice comparisons required by VIII. In fact the Karoubi and adjoint results show concrete reasons that the present positive word category does not already have those additional properties.

The ordinary positive matrices, bar, and regular basis used as input are the verified F43 construction. Their existence does not establish general canonical positivity, and the actual rank-three canonical-basis discussion already present in IV is not being renamed as a new solution.

## 11. Separate Grothendieck dictionary paragraph

The split Grothendieck ring records the actual chosen additive category and its effective object monoid. Here positive multiplicities arise from finite graded coefficient spaces, and cancellation is proved at that level. SGA 6 V, Sections 2–3, with cote133 scan18, supplies the previously audited representation/lambda/sigma vocabulary for the symmetric coefficient category V. No lambda-ring structure is asserted on the noncommutative split K0 of P_64, and no gamma-filtration positivity theorem is inferred.

The actual algebra/action and its coherent center lie in the affine module framework of EGA I Theorem1.3.7 p86, Corollary1.3.8 p87, Theorem1.4.1 pp90–92, and SGA3 I 4.7.2–3/cote90 scan17. The normalization comparison is proved explicitly by (C16). The chosen finite Weil lines use the usual point-Weil convention, with the continuity argument supplied above.

The sharp distinction is between the effective split object monoid, its group completion, and its Karoubi completion. They have different positive generators and, in the present example, different integral algebra orders. None can be substituted for another without the demonstrated change in the canonical-basis and collision questions.

## 12. Verification record

Every new proof is displayed above. The primary degree-five presentation was reread in the full proved F19 source context, and the complete F43 positive bimodule report was reread before using its action matrices. The calculations are exact symbolic/path arguments; no finite numerical sample is being used to assert all-word or categorical coherence.

Independent fresh whole-proof review is requested before integration. Particular check targets are the precise degree-five summand maps, the scope of the ordered quadratic overlap, cancellativity and the image in split K0, the 104-versus-10 Karoubi counts, adjoint exclusion, and the distinction between arithmetic coefficient objects and fixed point-Weil operator traces.

An additional reproducible exact certificate is saved as verify_kernel_coherence.py, SHA256 cc1b7f73cf76be163c428cb767355afb728c0df27d79f02aade87aed29caa91b, with successful output verify_kernel_coherence_output.txt, SHA256 579340649f227d8c23f9588096fc1389739b9430d99a6e158936e958e0372927. It checks the triple coefficient transposition, the five four-factor pentagon permutations, both explicit degree-five mirror/inverse maps, the exact symbolic presentation identities on both branches, and the two Karoubi counts. The report's all-length and categorical proofs are separate and are not inferred from this finite certificate.

