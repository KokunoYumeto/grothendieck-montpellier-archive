# Part D: checked results

AI-produced by GPT-6 Astra (OpenAI); research sub-run `/root/obstructions_crystals`, 19 November 2026. No priority claimed. All group calculations below were rerun; no earlier computational output was trusted.

## D.1. Classification (proved, with finite certificates)

For a prime p and d>=1, reduction GL_d(Z/p²)->GL_d(F_p) splits exactly when d=1 or (d,p) is (2,2),(2,3),(3,2). Reduction SL_d(Z/p²)->SL_d(F_p) splits exactly when d=1 or (d,p) is (2,3),(3,2). Reduction Sp_{2g}(Z/p²)->Sp_{2g}(F_p), for g>=1, splits exactly when (g,p)=(1,3).

### General obstruction

Let N=E_12 and U=1+N. Every lift is U+pX. Modulo p²,

    (U+pX)^p = U^p + p sum_{i=0}^{p-1} U^i X U^{p-1-i}.

On matrices over F_p, conjugation by U has (Ad(U)-1)^3=0. Since sum_{i=0}^{p-1} T^i=(T-1)^{p-1} in F_p[T], the correction term vanishes for p>=5. Thus every lift has p-th power 1+pN !=1. This already excludes GL and SL in every d>=2 for p>=5, and also symplectic groups because their natural rank-two transvection has the same matrix.

For p=3,d=3 and p=2,d=4, the retained program `code/splitting_check.py` writes the necessary identities for lifts of elementary matrices:

    x_ij^p=1;
    x_ij x_kl=x_kl x_ij if j!=k and i!=l;
    x_ij x_jk=x_jk x_ij x_ik for pairwise distinct i,j,k.

Writing a lift as (1+E_ij)+pX_ij makes every entry of every relation affine linear over F_p. No sufficiency of this presentation is used. The systems have respectively 54 variables/rank 46 and 192 variables/rank 177, and are inconsistent. `certificate_n3_p3.json` and `certificate_n4_p2.json` give linear combinations of the original scalar equations whose left side is zero and right side is nonzero. The program verifies both identities exactly. The equation counts 270 and 1920 include harmless duplicate/trivial relations; these differ from the previous run's 216 and 1728 counts but have the same ranks and conclusions.

Restriction to a block diag(g,1) and projection to its top-left block preserve multiplication modulo p²: both off-diagonal blocks are divisible by p, so their product vanishes. This propagates the obstructions to all larger dimensions, for both GL and SL; in the latter case the projected lift need only lie in GL, and the displayed elementary-matrix obstruction already forbids that. It does not propagate SL_2(F_2) nonsplitting to SL_3(F_2), and we do not claim that it does.

### Positive cases and the remaining small obstruction

Rank one GL splits by Teichmüller representatives. GL_2(F_2) is lifted by the two integral matrices [[0,1],[1,0]] and [[0,-1],[1,-1]]. Closure modulo 4 has order 6 and reduction order 6. GL_2(F_3) is lifted modulo 9 by A=[[1,1],[6,7]] and B=[[0,4],[7,0]]. Closure has order 48 and reduction order 48. Since det(A)=1 and det(B)=-1, the inverse image in this complement of SL_2(F_3) has determinant 1, hence gives the SL_2 splitting.

For GL_3(F_2), the program solves the linear system and prints all six lifted elementary generators. Their subgroup modulo 4 and its reduction both have order 168, proving that reduction is an isomorphism. All six printed determinants are 1 modulo 4 (also immediate from perfectness of GL_3(F_2)); hence this gives the SL_3 splitting.

For SL_2(F_2), any lift A=U+2X with determinant 1 modulo 4 has square either 1+2E_12 or -1; neither is 1. All eight lifts are listed in `splitting_output.json`, so no section exists.

Finally, Detinko, Flannery, and Hulpke (2018), Theorem 2.5, opened in arXiv:1611.05921v4, says that for g>=2 the kernel in Sp_{2g}(Z/p²) has no proper supplement. A section would supply a proper supplement, so it is impossible. For g=1 use Sp_2=SL_2. The theorem also provides an independent literature check for SL except that its SL_2(Z/4) and SL_4(Z/4) exceptions have proper supplements, not complements. Our calculations exclude complements in those two cases. The logical distinction is essential.

Computation scope: exact finite matrix arithmetic only. Runtime 0.174457 s on this run; full inputs are in the script and full output in its JSON. R5's GL classification is confirmed.

## D.2. Nonzero coherent obstruction: an explicit generic construction (proved)

Let p be prime and d>=2 outside the three GL split cases. Put Gamma=GL_d(F_p), m=|Gamma|, and take the regular permutation representation W_0=F_p[Gamma]^8, of dimension D=8m. Coordinates of W_0 are v_{h,j}, h in Gamma, 1<=j<=8. The action is g(v)_{h,j}=v_{g^{-1}h,j}. Introduce formal variables z_{h,j}, and define invariant homogeneous polynomials P_alpha(v) by

    product_{g in Gamma} (sum_{h,j} z_{h,j} v_{g^{-1}h,j})
       = sum_{|alpha|=m} z^alpha P_alpha(v).

All coefficients lie in F_p; zero coefficients can be retained. For each 1<=a<=D-4 and each alpha with |alpha|=m, let c_{a,alpha} be algebraically independent over F_p. Let k be an algebraic closure of their rational function field. In P(W_0)_k define

    Y = V(sum_alpha c_{a,alpha} P_alpha(v) : 1<=a<=D-4),
    S = Y/Gamma.

These formulas specify the field, the equations of Y, and the finite quotient defining S for every (d,p). They do not hide a choice of unspecified general polynomials: the coefficients are independent indeterminates.

### Verification of the construction

(1) Each nonidentity element g of order r has eigenspaces of dimension at most D/r<=D/2 on W_0 over k. Indeed, each regular permutation block is a union of r-cycles; even if p divides r, an eigenspace of an r-cycle has dimension at most one. Its projective fixed locus therefore has dimension at most D/2-1. The union B of all nonfree loci has this same upper bound.

(2) The linear system spanned by the P_alpha is base-point-free. At any nonzero v one can choose a linear form nonzero at every gv because k is infinite. Its norm then does not vanish at v.

(3) On P(W_0) minus B this linear system separates tangent directions. If v+epsilon w gives zero projective differential of the norm map, write L_g(z)=sum z_{h,j}v_{g^{-1}h,j} and M_g(z)=sum z_{h,j}w_{g^{-1}h,j}. Then

    sum_g M_g product_{h!=g} L_h = a product_h L_h.

The L_g are pairwise nonassociate linear forms because the projective stabilizer of v is trivial. Reducing modulo L_g proves L_g divides M_g. For g=1 this says w is proportional to v, i.e. the projective tangent vector is zero. This argument is valid in characteristic p and involves no division by |Gamma|.

(4) Generic successive members are consequently transverse on the free locus, by the ordinary incidence proof of Bertini: vanishing and any specified first-order tangent condition impose the expected independent linear conditions on the coefficients. Since D-4 > dim B, base-point-freeness also ensures that D-4 generic members have empty intersection with B. Thus Y is a smooth projective complete intersection threefold, entirely in the free locus. It is connected: the Koszul resolution, together with H^q(P^{D-1},O(-a))=0 for 0<q<D-1, gives H^0(Y,O_Y)=k. The same resolution gives H^1(Y,O_Y)=0. This is the finite-constant-group instance of the projective approximation construction used in Bhatt–Morrow–Scholze, Integral p-adic Hodge theory, Section 2; its proof has been given here to avoid a tameness assumption.

(5) The finite quotient S exists as a projective scheme. Because Gamma is a constant finite étale group and acts freely, Y->S is a finite étale Gamma-torsor. Thus S is smooth projective and connected over the perfect field k. The connected torsor supplies a surjection pi_1(S)->Gamma. Let M be the associated rank-d F_p-local system for the tautological representation, and E=M tensor_Fp O_S.

### Obstruction calculation

The natural isomorphism of Bergh–Rydh, Proposition B.4 (attached source, opened), identifies the co-Lie complex of D(M) with M tensor_Z^L O_S, in degrees [-1,0]. Its two cohomology sheaves are E. The class of its truncation triangle is the coherent image of the representation-lifting class

    kappa in H^2(Gamma, End_Fp(F_p^d)).

Here is a direct verification of that interpretation. For a free F_p-module V with Gamma-action, the triangle for V tensor_Z^L F_p, and derived tensor–Hom adjunction, give an exact sequence

    Ext^1_{Z[Gamma]}(V,V) -> End_{F_p[Gamma]}(V)
      -> Ext^2_{F_p[Gamma]}(V,V).

The second arrow sends id to kappa. The first sends an extension 0->V->L->V->0 to the endomorphism induced by multiplication by p on L. Its value is id exactly when L is free over Z/p² and reduces to V. Thus kappa vanishes exactly when the representation lifts, equivalently when the GL reduction extension splits. Part D.1 proves kappa!=0 in the present cases.

Set T=End_k(k^d), with conjugation action. Flat scalar extension gives kappa_k!=0 in H^2(Gamma,T): finite-group cohomology is computed by finite-dimensional cochains in each degree, and extension of scalars from F_p to k is exact. For the finite étale cover Y->S, coherent Cartan–Leray yields

    H^a(Gamma,H^b(Y,O_Y) tensor_k T) => H^{a+b}(S,End(E)).

Since H^0(Y,O_Y)=k and H^1(Y,O_Y)=0, its edge map H^2(Gamma,T)->H^2(S,End(E)) is injective. Functoriality of the co-Lie computation identifies the image of kappa_k with xi. Therefore xi!=0. In particular the co-Lie complex is not isomorphic to E direct-sum E[1] in D(O_S).

This settles the existential question in D.2 for every nonsplit pair (d,p), including d=2,p>=5, d=3,p=3 and d>=4,p=2. In the split cases the universal lifting class is zero, so every associated coherent class is zero on every base.

### Correction to Lead D's universal assertion

The assertion that properness plus surjective monodromy forces xi!=0 is false. Repeat exactly the displayed construction with D-2 equations instead of D-4. It gives a connected smooth projective curve C covered by a connected finite étale Gamma-torsor and thus with full GL_d(F_p) monodromy. But H^2(C,End(E))=0 for every vector bundle E on a curve, hence xi=0. This does not contradict the threefold example. It also illustrates why nonvanishing on B_Gamma need not survive pullback along an arbitrary surjection pi_1(C)->Gamma.

The Artin–Schreier description of the kernel of H^2_et(S,End(M))->H^2(S,End(E)) is correct: use the exact étale sequence 0->End(M)->End(E) --(F-1)--> End(E)->0. Its long exact sequence says precisely that the kernel is the image of the preceding boundary map H^1(S,End(E))->H^2_et(S,End(M)). No conclusion of injectivity follows from properness alone.


## Residual-pencil boundary, promoted 2026-11-19T21:18:01.208781+00:00

`A3_mixed_positive_index_residual_boundary.tex` proves the symmetric-square resolution and exact factorization of the actual surface cup-wedge map through the residual-pencil multiplication and two-step boundary, including diagonal squares in characteristic two and nonreduced Cartier D. For integral D the multiplication has dimension-three image. The actual boundary and its Delta restriction remain the unresolved gate; no generic-rank theorem or nonvanishing follows. Root and reduction/descent full audits are retained in `positive_index_residual_boundary_promotion.json`. The actual determinant-direction kernel is K tensor P; the different same-weight Koszul contraction cannot replace it.

## Primitive mixed unipotent bundle and exact boundary kernel — 2026-11-19T22:24:39.064676+00:00

`A3_mixed_positive_index_unipotent.tex` gives the actual O/O extension of End^0(V)/O, with explicit class gamma=b²/(a²+b²h) and fully typed complementary-isogeny proof. The extension is nonsplit at actual local index zero and split at positive actual local index. `A3_mixed_positive_index_boundary_kernel.tex` proves F(gamma)=0, computes Sym²G and its cohomology, and gives the exact kernel sequence retaining H0(D,A G|D). The known norm section proves this additional domain is nonzero; acyclicity of G does not remove it. Complete root and companion audits and the seventeen-identity certificate are retained. No variation-image lower bound or new generic-rank assertion is made.


## Product dual-Cartier blocks — 2026-11-20T00:49:54.615784+00:00

`A4_ss_product_dual_Cartier.tex` proves uniform perfect twisted cross blocks on the supersingular elliptic product, including one trivial Picard coordinate, and generic dual alternating rank 9n−1 for every odd étale pullback of its cubic principal bundle. All odd rectangles follow by the previously proved odd self-isogenies. The direct relative-Cartier table, Schur complement, rank-eight trivial block, and character-open intersection have full root and monodromy proof/code audits. This is auxiliary: no fixed indecomposable principally polarized surface determinant, positive-index mixed cup lower bound, or new full monodromy follows.


## Universal Moore determinant classification — 2026-11-20T01:37:44.505387+00:00

`A4_Moore_singular_parameters.tex` classifies every identically singular characteristic-two9-by-9 Moore parameter as lying in one of81 explicit translated character-scaled alternating projective3-spaces. The full9! determinant reconstruction excludes400 supports by retained monomial witnesses; the remaining2/4/6/8-support cases are proved by cube ratios, an elementary reflection-matching lemma and exact root-of-unity polynomial substitution. Root, reduction/descent and monodromy each fully audited the proof and reran the unchanged exhaustive symbolic certificate. This theorem is set-theoretic and algebraic; its actual Cartier/theta bridge is a separate result. The failed40-basis coordinate-product shortcut and all earlier probes remain retained.


## Actual common Cartier incidence — 2026-11-20T01:50:25.969749+00:00

`A4_common_Cartier_incidence.tex` proves that the same actual section and its actual left kernel attain maximal multiplication rank and maximal dual alternating rank. The exact Moore tensor reindexing supplies every nontrivial character multiplication determinant; the degree-one symmetrizer makes the trivial left kernel a fixed linear function of the section. Their nonempty opens meet in one nine-dimensional section space. The chosen etale pullback is smooth, connected and relatively Frobenius-bijective. The previously proved differential criterion then makes the dual kernel map birational for every fixed odd principal-cube degree. The wall-intersection, divisorial-inertia and full-group requirements remain separate. Root and reduction/descent completed full independent proofs; no additional numerical experiment is used.


## Exact Moore/Fermat nondivisibility — 2026-11-20T02:41:36.593751+00:00

`A4_Moore_Fermat_nondivisibility.tex` proves that the Fermat cubic divides a characteristic-two 9-by-9 Moore determinant exactly when that determinant is identically zero. The lower-support argument uses actual remainder coefficients. The missing eight-support cube identities are repaired by the four zero-position orbits of a nonconcurrent affine-line configuration. Full support is excluded by three cubed product equations forcing a product of nonzero coordinates to vanish. The standalone universal checker retains all support and phase witnesses; the initial failed ideal expression and all exploratory limits are preserved. The separate same-coordinate Cartier bridge remains necessary for any geometric wall consequence.


## Exact group structure, irreducible Lang polar, and the main orbit — 2026-11-20T03:18:29.507126+00:00

`sections/A_full_radical_image_structure.tex`: Exact pointwise-stabilizer and block structure; K remains undetermined. The root record is an author check; OC and monodromy are independent full proof audits.

`agents/obstructions_crystals/A4_Lang_polar_irreducibility.tex`: Geometric irreducibility of the reduced Lang polar and the unique maximal-dual-rank Lang component; exceptional lower-rank components are not excluded.

`agents/obstructions_crystals/A4_Lang_main_orbit.tex`: The unique maximal-dual-rank component is the large orbit V minus K, of degree 2^r minus 2^dimK. No parity or K=0 conclusion.

All mathematical candidate text is retained unchanged. The coordinated include and CP33-input edit preserves the exact prior files and diffs. No build, current-table refresh, or checkpoint finalizer was executed.


## Actual deck-slice quotient bound — 2026-11-20T03:47:47.519835+00:00

`A4_Lang_deck_slice_bound.tex` proves K is contained in the nontrivial deck part on the actual cubic principal slice, so the radical-generated quotient has dimension at least8. The proof uses the F2 averaging projector, full projected degree-one image after dense-open restriction, and unique henselian lifts of regular wall Lang vectors. It does not specialize the full generic fibre across a rank drop or compare different deck slices. The source-scope correction and both complete audits are retained.


## Arbitrary odd cubic-pullback source — 2026-11-20T04:00:27.038007+00:00

`A4_general_odd_source_Cartier.tex` proves the exact relative twisted blocks and simultaneous same-Fermat wall witnesses for M=eta*3Theta with arbitrary positive odd deg(eta)=a, without assuming the source is principally polarized. If that source has full geometric image, the outer odd-cover slice forces K into its nontrivial deck part and gives quotient dimension at least9a-1. The source full-image hypothesis remains explicit. The earlier narrower candidate is retained and not separately promoted.


## Determinant wedge and theta-degree bound — 2026-11-20T04:22:34.634564+00:00

`A4_Lang_wedge_pole_theta_bound.tex` proves a new quantitative restriction on the canonical residual module. The actual invariant wedge is regular at every full-radical common wall; its poles elsewhere are bounded by the full determinant orders. The theta commutator forces the nonempty regular-wall union to have degree at least the larger polarization elementary divisor. Exterior-Euler vanishing then gives the stated quotient bounds. All extra-wall poles remain allowed; no complete A.4 claim is inferred.


## Compatible residual modules and the rounded prime bound — 2026-11-20T04:29:02.731173+00:00

`A4_compatible_residual_modules.tex` proves that projection of the target residual module to an odd source lands in that source's canonical residual module, without assuming the source image is full. Compatible cyclic intermediates place all these modules in disjoint sectors of one actual fibre. The wedge bound and the exact Frobenius-orbit dimension of nontrivial cyclic modules yield the rounded bound; at degree17 the quotient has dimension at least872 and the residual module at most1728. Both canonicals are now wired for CP35. Full image remains unproved in that degree.


## Primitive type-(1,3) full image — 2026-11-20T05:11:22.456119+00:00

Every fixed nonordinary abelian surface with an ample globally generated line bundle of type (1,3) has a nonempty smooth/sharp family and full geometric relative GL2(F2)=S3 image. Global generation is an explicit hypothesis; no general type-(1,ell), degree17, or general A.4 closure follows.

Canonical: `A4_primitive_type_1_3_full_group.tex`. The seven-label exact candidate and complete source/code audit records are retained. The canonical changes only the statuses and is now included in CP36.


## Odd-polarization Cartier/evaluation — 2026-11-20T05:33:36.051633+00:00

For every ample globally generated L of odd N=chi(L)>1 on an abelian surface in characteristic two, the Frobenius-pushforward evaluation has generic rank at least three, and has rank four when gcd(N,6)=1. On a nonordinary surface the actual global Cartier tensor is surjective. No everywhere-generation, individual global-contraction rank, smooth-member or full-monodromy conclusion follows from this theorem alone.

Canonical: `A4_odd_Cartier_evaluation.tex`. Full audit and status-only promotion records are retained; the CP36 input follows its primitive stability dependency.


## Actual type-(1,5) evaluation fibres — 2026-11-20T06:16:06.338454+00:00

For any ample globally generated type-(1,5) line in characteristic two, the actual rank-four Frobenius evaluation kernel map is generically finite exactly when there is no elliptic curve of line degree two. If such an elliptic quotient exists, the map factors through it via an injective-on-geometric-points curve map. In the nonordinary case the actual theta evaluation image lies in the polar quintic. No separability of that kernel map, exceptional coefficient exclusion, common wall, full monodromy or embedding assertion is made.

Canonical: `A4_type_1_5_evaluation_fibres.tex`. The exact candidate and status-only mathematical promotion are retained. Shared checkpoint integration is reserved to root.
