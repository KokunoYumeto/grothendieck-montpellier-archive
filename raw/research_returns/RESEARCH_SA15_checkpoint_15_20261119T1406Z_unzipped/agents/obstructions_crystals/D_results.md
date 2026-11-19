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
