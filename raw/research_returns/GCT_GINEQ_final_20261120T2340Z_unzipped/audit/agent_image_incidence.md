# Image-subspace substitution and its incidence dictionary

Run: GCT_GINEQ. Agent: /root/geometry_dictionary, GPT-6 Astra Pro; effort setting not exposed. Started2026-11-20 23:19UTC. This file extends, and does not replace, G-01–G-07 in agent_geometry.md. The arguments below are complete proofs by this agent. The substitution principle has established antecedents; no novelty claim is made merely for its incidence reformulation.

All projective spaces in this file parametrize lines. All analytic norm statements are over C with the specified product Hermitian metric. Border rank means complex border rank, equivalently membership in the relevant projective secant variety. The scheme formulation is stated separately from the metric argument.

## GI-01 — The Grassmannian secant-incidence locus is closed

**Statement.** Let W be a finite-dimensional complex vector space, let Y⊂P(W) be a nondegenerate projective variety, and let 1≤q≤dim W and s≥1. Put Z_s=σ_s(Y), and define

 D_{q,s}(Y) = { U∈Gr(q,W) : P(U)∩Z_s≠∅ }.

Then D_{q,s}(Y) is Zariski closed. In particular, if U_ν→U in Gr(q,W) and every U_ν contains a nonzero vector of Y-border rank at most s, then U does as well.

**Proof.** Let S_q⊂W⊗O_Gr be the tautological rank-q subbundle. The incidence correspondence

 I_{q,s} = { (U,[u])∈Gr(q,W)×Z_s : [u]∈P(U) }

is closed. For a bundle description, pull back O_{P(W)}(−1) and W/S_q to Gr(q,W)×P(W). The universal inclusion O(−1)→W⊗O followed by the quotient to W/S_q is a bundle morphism. Its zero scheme is the usual line-in-q-plane incidence correspondence P_Gr(S_q). Intersecting with Gr(q,W)×Z_s gives I_{q,s}.

Since Z_s is projective, the projection Gr(q,W)×Z_s→Gr(q,W) is projective, hence proper. Its restriction to the closed subscheme I_{q,s} is proper. Therefore its image, which is exactly D_{q,s}(Y), is closed. A complex Zariski-closed set is also closed in the ordinary topology, proving the limit assertion. Equivalently, choose [u_ν]∈P(U_ν)∩Z_s; projective compactness provides a convergent subsequence, and the closed incidence conditions put its limit in P(U)∩Z_s. ∎

**Metric-free content.** The condition is an existential algebraic incidence condition on the actual q-plane U. It is not determined just by q or by the class [S_q] in a Grothendieck ring. The latter is a bundle on the Grassmannian, whereas the condition uses its embedding into W⊗O and the secant subscheme Z_s.

## GI-02 — Border substitution for an image subspace

**Statement.** Let H,W be finite-dimensional complex vector spaces and let Y⊂P(W) be nondegenerate and projective. Let T∈H⊗W be nonzero and let

 f_T:H*→W,  U=im(f_T),  q=dim U.

Let Rbar_{H,Y}(T) denote border rank relative to Seg(P(H)×Y), so its atoms are a⊗y with a∈H and y in the affine cone over Y. Then

 Rbar_{H,Y}(T) ≥ q + min_{0≠u∈U} Rbar_Y(u) − 1.                  (GI.1)

More precisely, if Rbar_{H,Y}(T)≤r, then r≥q and

 U∈D_{q,r−q+1}(Y).                                           (GI.2)

For an ordinary tensor, group any chosen factors into H and leave the remaining factors in W. Taking Y to be the Segre variety of those remaining factors gives the same lower bound for the original CP border rank, because every original CP atom becomes an allowed a⊗y atom. Any additional constraint on the H-factor only restricts the original atoms and does not invalidate the lower bound.

**Proof.** Suppose Rbar_{H,Y}(T)≤r. Choose tensors T_ν→T with decompositions

 T_ν = Σ_{j=1}^r a_{νj}⊗y_{νj},   y_{νj}∈hat(Y),

allowing zero terms. Such a sequence exists over C: the rank-at-most-r set is constructible, and its Euclidean and Zariski closures agree. The flattenings f_{T_ν} have rank at most r. Since rank-at-most-r is closed by minors, q≤r.

Choose λ_1,…,λ_q∈H* for which f_T(λ_1),…,f_T(λ_q) are a basis of U. These q columns remain linearly independent for all sufficiently large ν. Define

 U_ν=span{f_{T_ν}(λ_1),…,f_{T_ν}(λ_q)}.

Then dim U_ν=q and U_ν→U in Gr(q,W). This construction is essential: im(f_{T_ν}) itself can have dimension larger than q, so one cannot simply regard all full image spaces as points of the same Grassmannian.

Let S_ν=span{y_{ν1},…,y_{νr}} and put p_ν=dim S_ν. We have U_ν⊂S_ν, hence q≤p_ν≤r. Select p_ν linearly independent nonzero y_{νj} from the decomposition, giving a basis of S_ν consisting of Y-atoms. Let L_ν be the span of any p_ν−q+1 vectors of that basis. Then

 dim(U_ν∩L_ν) ≥ dim U_ν + dim L_ν − dim S_ν
                 = q+(p_ν−q+1)−p_ν = 1.

Thus some nonzero u_ν∈U_ν∩L_ν has Y-rank at most p_ν−q+1≤r−q+1. Consequently U_ν∈D_{q,r−q+1}(Y). The closedness from GI-01 gives U∈D_{q,r−q+1}(Y). There is therefore a nonzero u∈U of Y-border rank at most r−q+1. Rearranging yields (GI.1). ∎

**Why S_ν matters.** The proof uses a basis of the span of the remaining-factor atoms in a decomposition. It never asserts that these atoms belong to im(f_{T_ν}), or that the latter is itself spanned by pure tensors. Such an assertion would be false in general. Nor does the proof require the individual decomposition atoms or their coefficients to converge.

**Established principle and exact locator.** This is a border-substitution argument. In the three-factor concise case, its one-dimensional-restriction version is the a′=1 case of Landsberg–Michałek, arXiv:1608.07486v1, Proposition2.3, printedp3 / PDF zero2: restricting the first dual space to a′ dimensions costs at most a−a′ in border rank. Their §4 also constructs closed compression loci using Grassmannian bundles. Primary source: https://arxiv.org/pdf/1608.07486. The proof above is self-contained, handles a general residual projective atom variety Y, and supplies the required actual-image and atom-span qualifications. This citation is contextual; no full proof audit of the cited paper is claimed.

## GI-03 — A projector norm certifies avoidance of the incidence locus

**Statement.** Let W=B_1⊗…⊗B_b with b≥2, equipped with its product Hermitian metric. Let 0≠U⊂W and let P_U:W→W be the orthogonal projection. Write ε_b for the ordinary b-factor injective norm and define

 α(U)=max_{||z_i||=1} ||P_U(z_1⊗…⊗z_b)||².

Then 0<α(U)≤1 and

 α(U)=max_{u∈U, ||u||_F=1} ε_b(u)².                          (GI.3)

If P_U is identified with its tensor in W⊗bar(W), with all 2b factors kept separate, then its 2b-factor injective norm equals α(U), not its square root:

 ε_{2b}(P_U)=α(U).                                          (GI.4)

Every nonzero u∈U satisfies

 Rbar_CP(u) ≥ ceil(α(U)^(−1/(b−1))).                         (GI.5)

Consequently, with U and q as in GI-02 and with the residual atom variety equal to Seg(PB_1×…×PB_b),

 Rbar_CP(T) ≥ q−1+ceil(α(U)^(−1/(b−1))).                     (GI.6)

Any proved upper bound α(U)≤a gives the valid, possibly weaker bound q−1+ceil(a^(−1/(b−1))).

**Proof of the projector identities.** For each unit product vector z, the maximum of |⟨u,z⟩| over unit u∈U is ||P_Uz||, by Cauchy–Schwarz, with equality at the normalized projection when it is nonzero. Taking maxima over u and z in either order proves (GI.3). Since product vectors span W and U is nonzero, α(U)>0; contractivity of the projection gives α(U)≤1.

For (GI.4), the tensor/operator identification gives

 ε_{2b}(P_U)=max_{x,y unit product vectors}|⟨x,P_Uy⟩|.

Positivity and idempotence imply

 |⟨x,P_Uy⟩|=|⟨P_Ux,P_Uy⟩|
             ≤||P_Ux||·||P_Uy||≤α(U).

The reverse inequality follows by taking x=y at a product vector attaining the maximum. This argument also specifies the required complex conjugate factors; an unqualified bilinear identification should not be substituted for it.

**Proof of the rank inequality.** If a residual b-tensor v has CP rank at most s, its mode supports each have dimension at most s. Choose orthonormal bases in its first b−1 mode supports and expand

 v=Σ_β e_{β_1}⊗…⊗e_{β_{b−1}}⊗v_β.

There are at most s^(b−1) terms. Orthogonality gives ||v||_F²=Σ_β||v_β||². Each coefficient vector has norm at most ε_b(v): fix the corresponding first b−1 basis vectors and choose the last unit test vector along v_β. Therefore

 ||v||_F²≤s^(b−1) ε_b(v)².                                 (GI.7)

Both norms are continuous, so (GI.7) also holds for every v of CP border rank at most s. Now take unit u∈U and set s=Rbar_CP(u). Equations(GI.3) and(GI.7) imply

 1≤s^(b−1) ε_b(u)²≤s^(b−1)α(U).

Thus s≥α(U)^(−1/(b−1)), and integrality gives (GI.5). Applying GI-02 proves (GI.6). ∎

**Equivalent incidence certificate.** For an integer s≥1, a strict inequality α(U)<s^(−(b−1)) proves P(U)∩σ_s(Segre)=∅. If m=ceil(α(U)^(−1/(b−1))), this strict test applies to s=m−1 when m≥2. This explains the ceiling and prevents an erroneous extra unit at equality. Norm computations must control rounding if they are numerical rather than exact.

## Scheme and group-scheme dictionary

Let S be a noetherian base scheme, W a finite locally free sheaf, and Z_s⊂P_S(W) a chosen closed projective secant model, for example the integral model from G-01 after projectivizing. The relative Grassmannian Gr_S(q,W) carries S_q⊂W⊗O. The zero scheme of O(−1)→W/S_q gives the relative incidence correspondence. Its fiber product with Z_s is projective over the Grassmannian. The scheme-theoretic image is therefore a closed incidence scheme; its underlying point set is the proper image. At geometric points it records the existence of a line in the q-plane lying in the chosen fiber of Z_s.

The construction is compatible with changes of frame, and is equivariant for the residual product group scheme ∏GL(B_i). It uses the universal subbundle together with its inclusion into W, not just its K0 class. The relative projective-bundle and incidence construction commutes with base change. Formation of the scheme-theoretic image, and identification of a chosen integral secant model with independently formed secants in each small characteristic, require the usual separate base-change checks; neither is asserted automatically.

On the locally closed determinantal rank-q stratum—where every (q+1)-minor vanishes scheme-theoretically and the q-minors generate the unit ideal—the flattening image is a rank-q subbundle and defines a morphism to Gr_S(q,W). This precise determinantal condition is needed over nonreduced bases; merely having rank q on all geometric fibers need not suffice. The low-border-rank implication is then membership in the pullback of the incidence locus. Over C, the projector norm supplies a sufficient certificate that a particular point lies outside that locus. The projector itself requires metric data and is not supplied by an arbitrary scheme or by its lambda-ring.

The geometric construction needs only a Grassmannian and a projective incidence correspondence. Full Hilbert-scheme machinery is optional here. If desired, a relative Grassmannian is a special quotient parameter space; FGA Exp221, Theorems3.1–3.2 supplies the general Quot context already documented in G-03.

## Exact scope relative to linear-flattening barriers

The certificate uses q=rank(f_T) and also the position of im(f_T) inside the residual tensor space. The second datum is not determined by q. For a matrix X whose columns form a basis of U, the orthogonal projector is X(X*X)^(−1)X*. Thus T↦P_im(f_T) on a rank chart is generally nonlinear and involves the chosen Hermitian structure. Its injective-norm estimate is not a singular-value refinement of rank(f_T) alone.

Algebraically, the additional test is avoidance of D_{q,s}(Y), a proper-image incidence condition. Its equations on a Grassmannian or their pullbacks along rank charts need not be minors of a single fixed linear map of the original tensor. Accordingly, the EGOW/Lovitz potency barriers for a linear map L(T) with a uniform bound on rank L(atom) do not, by themselves, bound this substitution-plus-subspace argument. This is a limitation of applicability, not a claim to have exceeded every rank-method barrier or to have established a numerical improvement over the strongest known tensor bounds.

In particular, an M_n conclusion n²+n−1 would improve the ordinary flattening bound n² but remain below the classical stronger matrix-multiplication lower bounds documented in B-01. The specific projector constants for M_n, row determinant/permanent, and symmetric determinant/permanent are being checked separately by the tensor and SDP agents; they are not assumed proved in this file.

## Symmetric-rank convention

If T is symmetric but the conclusion concerns ordinary CP border rank, approximating decompositions may be nonsymmetric. The residual variety in GI-02 must therefore be the full Segre variety. A residual image lying in Sym^b(E) does not force the atoms in an arbitrary CP decomposition to be pure powers.

For Waring border rank one may instead start from pure-power approximants and take the residual Y to be the Veronese variety, since a degree-n pure power factors across a k|(n−k) grouping as ℓ^k⊗ℓ^(n−k). Avoiding a Veronese secant alone gives a Waring statement; avoiding the corresponding Segre secant gives an ordinary CP statement. The projector bound in GI-03 is stated for the full residual Segre atom set and therefore supports the ordinary CP conclusion when its constant is established for that full injective norm.

## Source and verification status

- GI-01–GI-03 are proved in full above; no appeal to an unproved new external theorem is needed for their substantive inequalities.
- Properness background: EGA II, Definition 5.4.1 (proper = separated, finite type, universally closed) and Proposition 5.4.2 (closed immersions, compositions and base changes), printed p.100, zero-based scan index96 / one-based leaf97; Theorem 5.5.3(i) (projective implies proper), printed p.104, zero-based scan index100 / one-based leaf101. NUMDAM archive ID PMIHES_1961__8__5_0, DOI10.1007/BF02699291, primary record https://www.numdam.org/item/PMIHES_1961__8__5_0/ and original scan https://www.numdam.org/article/PMIHES_1961__8__5_0.pdf. Both original pages were visually inspected at the final-draft geometry review on 2026-11-20; these are verified indices, not inferred from printed-page offsets.
- Border-substitution antecedent: Landsberg–Michałek, Proposition2.3, arXiv:1608.07486v1, printedp3/PDFzero2, https://arxiv.org/pdf/1608.07486. Statement checked in primary source; whole external proof not independently re-proved.
- This file does not establish the target-specific α constants and does not treat the image-substitution mechanism as a novel general principle.

**Author review.** GI-01–GI-03 were read in full and checked at2026-11-20 23:24:44UTC. All passed; the relative scheme dictionary was sharpened to use the actual determinantal rank stratum over nonreduced bases. Events are in work/agent_image_incidence_check_events.tsv. There is no formal certificate or external human verification.

