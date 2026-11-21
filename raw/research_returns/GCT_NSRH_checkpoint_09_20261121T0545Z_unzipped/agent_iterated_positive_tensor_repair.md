# F66 — A regular positive four-state model for the actual iterated tensor

Author: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This is a constructive supplement to frozen F63. It constructs a positive model for its whole four-dimensional tensor, while retaining the negative simple projector. It does not change F63 or construct the entire k=4 tensor module, every iterated simple, a source canonical basis, or a categorical iteration functor from the two binary categories.

## 1. The exact actual module being retained

Use F63's notation
\[
 \delta=v+v^{-1},\quad D=\delta^2,\quad
 a=D-2,\quad d=D^2,\quad A=D^2-8D+8.
\]
The actual restriction of N(D-2) tensor N(D-2) through Blasiak's
Delta^(2,2) has the left-column matrices
\[
 R_1=\begin{pmatrix}
 d&Da&Da&2a^2\\0&0&0&-Da\\0&0&0&-Da\\0&0&0&d
 \end{pmatrix},\quad
 R_2=\begin{pmatrix}
 d&0&0&0\\-Da&0&0&0\\-Da&0&0&0\\2a^2&Da&Da&d
 \end{pmatrix}.
 \tag{PT1}
\]
These are actual named generators, not a dimension-only replacement.

F63 proved that the matrix B with columns
\[
 (d,-Da,-Da,d)^T,\quad(0,1,-1,0)^T,\quad
 (A,-Da,-Da,d)^T,\quad(d,-Da,-Da,A)^T
 \tag{PT2}
\]
satisfies
\[
 B^{-1}R_iB=\operatorname{diag}(d,0,N_i(A)),
\quad
 N_1(A)=\begin{pmatrix}d&A\\0&0\end{pmatrix},
\quad N_2(A)=\begin{pmatrix}0&0\\A&d\end{pmatrix},
 \tag{PT3}
\]
and
\[
                 \det B=128D(D-2)(D-1)^2.
\]
It is therefore a basis change over R=Q[v,v^{-1}]_(v-1). The complete source and proof audit is the frozen F63 report, SHA256
8ee2ba3448005df2ed9a4e39df8103e4d86d80ddad852227b30766cb7edbb224.
Source references: Blasiak arXiv1010.0421v2, Definition2.5 and equations8–11 p6, equation13 p8, Theorem3.4 p12, Theorem3.7 pp13–14. The strand rank is3 and the iteration parameter is4.

## 2. A positive regular change of basis

Put
\[
 x=(D-2)^2=v^4+2+v^{-4},\qquad
 y=4(D-1)=4v^2+4+4v^{-2}.
 \tag{PT4}
\]
Then
\[
                         x+y=d,\qquad x-y=A.
 \tag{PT5}
\]
Consider the two four-state matrices
\[
 S_1=\begin{pmatrix}
 x&y&0&0\\
 x&y&0&0\\
 0&0&y&x\\
 0&0&y&x
 \end{pmatrix},\qquad
 S_2=\begin{pmatrix}
 x&0&y&0\\
 0&y&0&x\\
 x&0&y&0\\
 0&y&0&x
 \end{pmatrix}.
 \tag{PT6}
\]
All entries belong to N[v^2,v^{-2}].

### Proposition PT-A

There is a simultaneous basis change over R carrying the actual named matrices R_i to S_i. It preserves the tensor bar transported from the binary F43/F56 basis.

### Proof

Let C have columns
\[
 c_+=(1,1,1,1)^T,\quad
 c_-=(y,-x,-x,y)^T,\quad
 f_1=(1,1,-1,-1)^T,\quad
 f_2=(1,-1,1,-1)^T.
 \tag{PT7}
\]
Direct multiplication gives
\[
\begin{array}{c|rrrr}
 &c_+&c_-&f_1&f_2\\ \hline
 S_1&d c_+&0&d f_1&A f_1\\
 S_2&d c_+&0&A f_2&d f_2 .
\end{array}
 \tag{PT8}
\]
For example S_1f_2=(x-y,x-y,y-x,y-x)^T=A f_1; the other entries are equally direct. Expanding the determinant gives
\[
                              \det C=-8(x+y)=-8d.
 \tag{PT9}
\]
This is a unit at v=1, where d=16. Equations PT3 and PT8 imply
\[
            T=B C^{-1},\qquad T^{-1}R_iT=S_i.
 \tag{PT10}
\]
Both T and its inverse are regular at v=1. Hence this is a change of the same actual parameter-local lattice and named action.

The original four-state tensor basis is fixed by the bar inherited from the verified binary basis. Every entry of B and C is a rational expression in D, which is invariant under v -> v^{-1}. The same is true of T. Therefore every new basis vector is bar-fixed. This is the actual transported formal bar, not a positive Hermitian polarization or a statement about VIII's global integral lattice. QED.

In particular the positive whole-tensor model whose existence F63 left open is supplied here for this specified four-dimensional summand. Its construction uses the available scalar-plus and scalar-minus components together with N(A); it does not make N(A) itself positive.

## 3. The projector remains explicitly non-effective

In the new basis, the actual regular projector from F63 becomes
\[
 E=C\operatorname{diag}(0,0,1,1)C^{-1}
  =\frac12\begin{pmatrix}
   1&0&0&-1\\
   0&1&-1&0\\
   0&-1&1&0\\
   -1&0&0&1
  \end{pmatrix}.
 \tag{PT11}
\]
One may verify this without inversion: E kills c_+,c_- and fixes f_1,f_2. Thus E is independent of v, is idempotent, and commutes with both S_i. Its image is the actual N(A) summand.

The inserted trace is still
\[
                  \operatorname{Tr}(E S_1S_2)=A^2.
 \tag{PT12}
\]
F63's mixed Laurent trace proves that no simultaneous basis makes E and the two S_i effective Laurent matrices. PT11 exhibits the negative entries in this particular positive generator basis.

An arbitrary linear idempotent in the four-dimensional module is different from an effective object of the coefficient-kernel category. Its existence does not supply the latter. This is why the positive construction and F63's simple/projector obstruction are compatible.

## 4. Actual positive kernels and coherent quadratic maps

Let V_even be the category of finite graded vector spaces over a characteristic-zero coefficient field, supported in even internal degrees, with degree-zero linear maps. For the arithmetic realization below the coefficient field is a finite extension E of Q_ell, ell not dividing Q.

Choose graded coefficient spaces X and Y with characters x and y in PT4. Explicitly X has one line in each degree4,-4 and two in degree0; Y has four lines in each degree2,0,-2. Let
\[
                              Z=X\oplus Y,
                       \qquad\operatorname{ch}Z=d.
 \tag{PT13}
\]
Define matrix kernels K_1,K_2 by replacing x,y,0 in PT6 by X,Y,0. Our entry K_ab sends state b to state a; matrix convolution is
\[
                     (K\circ L)_{ac}
                         =\bigoplus_b K_{ab}\otimes L_{bc}.
 \tag{PT14}
\]
It therefore has exactly the source left-column multiplication convention. Its associator and pentagon are the usual finite-sum/tensor identifications, before taking characters.

For K_1 the two blocks of states are {1,2} and {3,4}; rows are constant within each block. The two target-entry coefficient spaces in a block are X,Y in one order or the other. Composing twice therefore gives, entry by entry, the actual distributivity isomorphism
\[
                             K_1^2\simeq Z\otimes K_1.
\]
For K_2 the blocks are {1,3} and {2,4}, with the same property. Thus
\[
                             K_i^2\simeq Z\otimes K_i.
 \tag{PT15}
\]
The scalar coefficient is the actual iterated quadratic coefficient d=delta^4.

These maps have a coherent repeated-power description. A path of length r using only K_i has r-1 independent intermediate-state choices inside its block. List those choices in their path order. The corresponding coefficient decomposition gives
\[
                        K_i^r\simeq
                           Z^{\otimes(r-1)}\otimes K_i.
 \tag{PT16}
\]
All parenthesizations use the same labeled intermediate choices. Raw quadratic reductions may extract their Z factors in different orders: already at length three, the left-first and right-first reductions differ by transposing the two extracted factors. Compare each reduction with PT16 using the canonical coefficient permutation that restores the chosen path order, together with the usual associativity maps. These corrected comparisons agree: adjacent coefficient transpositions satisfy the symmetric-group relations, and each sends the same labeled path factors to the same ordered positions. This is ordinary symmetric-monoidal coherence, not a claim that the two uncorrected length-three maps are identical. There is no dimension-only inference of these quadratic maps.

For mixed words all compositions already exist in the concrete matrix category with its associativity. Their characters give the actual S_i products. In particular the complete source algebra relations hold after taking characters, since PT10 intertwines the actual module. No source-prescribed higher categorical presentation is asserted. Choosing extra presentation isomorphisms or a categorical iteration functor would need its own comparison; PT15 alone does not provide them.

## 5. The split Grothendieck image, completion, and adjoints

Let P be the full additive monoidal subcategory of Mat_4(V_even) generated by the identity kernel, K_1,K_2 and their even internal shifts. Its morphisms are all the ambient graded kernel morphisms.

### Proposition PT-B

The split Grothendieck group of P injects by character into Mat_4(Z[v^2,v^{-2}]), with image precisely the algebra generated by I,S_1,S_2 over Z[v^2,v^{-2}]. Its generic dimension over Q(v) is6.

Its full Karoubi closure is Mat_4(V_even), whose split Grothendieck group has rank16 over Z[v^2,v^{-2}]. The transpose-dual of K_1 is not an object of P.

### Proof

Two objects of P are isomorphic exactly when all corresponding graded coefficient dimensions agree, because morphisms are the full entrywise graded linear maps. Thus its additive isomorphism monoid is identified with its character matrices in the cancellative monoid N[v^2,v^{-2}]^{16}. If two formal differences have the same character, adding their opposite terms gives equal character objects, hence an actual isomorphism. This proves injectivity on the split Grothendieck group.

Objects are finite direct sums of shifted words, so the image is exactly the indicated algebra. Over Q(v), PT3 identifies the representation as epsilon_+ plus epsilon_- plus N(A). The last two-dimensional block is absolutely irreducible since A^2 is neither0 nor d^2. The regular projector PT11 and its complementary scalar projectors separate these blocks; explicitly (I-E)S_1/d is the plus projector and (I-E)-(I-E)S_1/d is the minus projector. Hence the image is Q(v) times Q(v) times M_2(Q(v)), of dimension6.

For the Karoubi claim, the unit splits into the four state matrix units E_aa. Then E_aa K_i E_bb isolates one coefficient entry. Every nonzero x or y has a nonzero degree-zero component, so a degree-zero line can be split from it. Consequently E_ab is obtained for every directed edge in the support of S_1 or S_2. These supports contain both directions of 1--2, 3--4, 1--3, and2--4, hence connect all states in both directions. Composing these matrix units yields every E_ab. Their even shifts and finite direct sums give every matrix kernel in Mat_4(V_even). Conversely that ambient category is already idempotent complete. Its split group has the sixteen matrix units as a basis over the coefficient Laurent ring.

For the last assertion, every matrix in the original algebra image preserves the common line spanned by c_+=(1,1,1,1)^T, because S_i c_+=d c_+. The coefficients x,y are bar-invariant, so the transpose-graded-dual kernel of K_1 has character S_1^T. But
\[
                       S_1^T c_+
                           =(2x,2y,2y,2x)^T
\]
is not proportional to c_+ over Q(v), since x-y=A is nonzero. Therefore this character is outside the actual algebra image, and the adjoint kernel cannot belong to P. QED.

This is an exact closure boundary, not an assertion that adjoints do not exist in the ambient matrix category. Karoubi completion introduces independent state objects and enlarges the character algebra. It does not recover the designated source simple labels as an effective basis of the original six-dimensional action image.

## 6. An ordinary Tate pure-complex realization

Fix Q, ell and E as above. On V_even define
\[
                   \Phi(V)_e
                    =V_e\otimes E(-e/2)[-e],
                  \qquad e\in2\mathbb Z.
 \tag{PT17}
\]
The multiplicity spaces have trivial Frobenius. Each summand is pure of complex weight zero: its degree is e and its point weight is e. Every shift is even. Consequently ordinary tensor symmetry has no additional Koszul sign, and the canonical degree-addition maps make Phi a symmetric strong monoidal functor.

Its Euler trace is
\[
       \operatorname{Tr}_{\rm Eul}(F^n;\Phi(V))
                     =\operatorname{ch}(V)(Q^{n/2}).
 \tag{PT18}
\]
No odd arithmetic line or geometric half-Tate motive is used. Negative e are implemented by ordinary inverse Tate twists and bounded negative cohomological degrees.

Apply Phi entrywise to PT14. Finite direct sums and tensor products preserve purity of weight zero on the point. The actual coefficient-kernel compositions and the coherent quadratic maps PT15–PT16 therefore lift to pure derived kernels. Every closed-word trace object is pure of weight zero and has the unmarked actual word trace under v=Q^(n/2).

Entrywise graded duality corresponds under Phi to ordinary point duality: the dual of E(-e/2)[-e] is E(e/2)[e], exactly the image of degree -e. The symmetric self-dual choices for X and Y preserve the formal bar on the generating kernels. This is different from the transpose-dual adjoint excluded in PT-B.

Purity of complex weight zero does not give one common Frobenius radius on total cohomology: its degree-e cohomology has point weight e. The path-sign upper/dual comparison, Hard Lefschetz, designated canonical labels and effective simple projector are not supplied. A fixed finite Weil space with all named operator traces is also not inferred; this is the coefficient-object, changing-composition realization.

## 7. The remaining iteration comparison

The character-level action is the actual four-dimensional restriction via Delta^(2,2), with the same local lattice and bar. The positive basis is a regular linear change of that module. A basis change of a vector representation is not by itself a monoidal functor between the two original binary matrix-kernel categories and this four-state category.

In particular the source formula uses Q_i=D-P_i, whose class is virtual in the strict effective kernel category. The present construction replaces the whole four-dimensional restricted action by an explicitly equivalent positive matrix model. It does not make those Q_i effective or supply a coherent all-k coproduct comparison. The whole 4096-dimensional tensor of four two-dimensional ordinary factors contains this module, but no positive model for all its other summands is claimed here.

The actual simple/projector obstruction of F63 remains. PT11 shows precisely where the effective completion or projector premise would fail. This positive example therefore narrows the obstruction to retaining designated summands and operations, rather than the mere existence of a positive model for the whole tested tensor.

## 8. Separate Grothendieck dictionary

The regular matrix T and named-action comparison are finite locally free module data over the parameter-local ring. EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90–92 provide the affine module dictionary. The formal bar is transported by an explicit invariant matrix, not supplied by an unpublished categorical theorem.

The even grading is a split-torus character grading in SGA3 I4.7.2–3 and cote90 scan17. Its effective coefficient ring is N[v^2,v^{-2}]. SGA6 V Sections2–3 and cote133 scan18 supply coefficient representation/lambda/sigma language for the symmetric coefficient category, not a lambda-ring structure on the noncommutative word algebra. The difference between the six-dimensional action image and the sixteen-dimensional completed matrix algebra is proved in PT-B.

The arithmetic coefficient functor uses ordinary Tate lines and bounded complexes in SGA6 I Definition4.7 pp121–122 and Example4.8 p122. BBD5.1.5 and5.1.8 pp125–127 give the exact integral-weight and pure-complex convention. PT17 is proved directly; it does not identify these auxiliary states with source canonical simples. No proper geometric generator correspondence, all-r quantum family or effective projector is inferred.

## 9. Verification

The exact certificate verify_iterated_positive_tensor.py checks PT5, both action tables, detC, the named R-to-S intertwining, projector formula and trace, quadratics, and the positivity of x,y.

The proofs of split-K0 injection, full Karoubi closure, adjoint exclusion, repeated quadratic coherence, actual formal bar and arithmetic purity were reconstructed by hand. They are not claimed as formally verified.

The frozen F63 report/source proofs provide the actual tensor occurrence and restriction normalization. The new result is the explicit positive regular realization of that same module and its precise closure/purity boundaries.

Fresh independent whole-proof review is requested. No frozen report, fragment or root master artifact has been edited.

