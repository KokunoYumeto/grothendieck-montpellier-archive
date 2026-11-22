# Independent geometric audit for the proposed A.127

**Auditor:** `/root/lie_theory`  
**Time:** 2026-11-19 17:40 UTC; exact tool clock checked before saving.  
**Scope:** The repaired PL proof that the bottom-fixed concordance group of the real projective plane has trivial component group. This is an independent proof audit, not an endorsement of the published boundary-relative mapping-class assertion. The author's full revised draft was subsequently read and passed, as recorded below.

## 1. Sources actually opened

1. Boyle–Chen, *Negative amphichiral knots and the half-Conway polynomial*, Revista Matemática Iberoamericana **40** (2024), 581–622, Appendix A, Theorem A.6 and its proof, printed pp.614–615. Full original opened: https://ems.press/content/serial-article-files/47105?nt=1 . The displayed map is `T_1(r,theta,y)=(r,theta+pi y,y)` in the disk model of RP². It moves the point `(r,theta,y)=(1/2,0,1)` to the distinct interior-disk point `(-1/2,0,1)`. Thus it is not fixed on the top RP² boundary. The asserted boundary-relative group and the winding-invariance argument cannot be used. In particular, an ambient isotopy need not preserve the comparison annulus C.
2. J. W. Alexander, *On the Subdivision of 3-Space by a Polyhedron*, PNAS **10** (1924), 6–8, DOI 10.1073/pnas.10.1.6. Original theorem on p.6 and its proof pp.7–8 opened in full at https://www.pnas.org/doi/pdf/10.1073/pnas.10.1.6 . This supplies the polyhedral three-dimensional Schoenflies theorem. Web reference: `turn539757620view1`. The alternative PMC PDF URL failed to open in the web tool; the publisher original succeeded.
3. D. B. A. Epstein, *Curves on 2-manifolds and isotopies*, Acta Mathematica **115** (1966), 83–107. Original opened at https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6005-11511_2006_Article_BF02392203.pdf . Theorem 3.1, p.89, gives PL ambient isotopy of proper arcs homotopic relative endpoints; Theorem 6.3, p.99, gives PL isotopy from a proper PL homotopy of a surface homeomorphism to the identity, with no projective-plane exception. Theorem 5.2, pp.95–96, is the relative PL Alexander construction already used in A.123. The statement in Section 7, p.104, also explicitly says a projective-plane homeomorphism is isotopic to the identity. Web references: `turn468853813view0`, `turn786417968view1`.

No original statement has been silently strengthened. In particular, the polar formula in Boyle–Chen is not being declared jointly PL.

The exact rational point certificate for the printed generator is `code/check_boyle_chen_top_boundary.py`; its actual output is `logs/check_boyle_chen_top_boundary.txt`. Runtime was 0.000053159 seconds. It verifies that `(1/2,0)` and `(-1/2,0)` lie strictly inside the disk, so the boundary antipodal identification cannot identify them.

## 2. Irreducibility of RP² × I

Let M=RP²×I and let S be an embedded PL two-sphere in its interior. The orientation double cover is N=S²×I, with deck involution a(x,t)=(-x,t). Since the sphere is simply connected, its inverse image is the union of two disjoint spheres S₁ and S₂ interchanged by a.

Cap both boundary spheres of N with three-balls to obtain S³. Polyhedral Schoenflies gives the two complementary balls of each Sᵢ in S³. If the two end caps lie on the same side of Sᵢ, its opposite complementary ball lies wholly in int(N). If the caps lie on opposite sides, Sᵢ separates the bottom and top of N. These alternatives are exhaustive.

The involution preserves the two ends individually. If S₁ separates the ends, so does S₂. Two disjoint end-separating spheres are strictly ordered from the bottom end to the top end. The order can be defined by inclusion of the closed component on the bottom side. An end-preserving homeomorphism preserves that order, and therefore cannot exchange two distinct members. This contradicts a(S₁)=S₂. Hence S₁ and S₂ each bound a unique interior ball Q₁ and Q₂ in N.

The balls Q₁ and Q₂, whose boundary spheres are disjoint, are either disjoint or strictly nested: choose a point in a bottom end cap as the point at infinity and use the bounded components in R³. Since a interchanges the balls and a²=id, either strict nesting would imply its reverse after applying a, a contradiction. The balls are disjoint. The covering projection is consequently injective on Q₁ and maps it to an embedded PL three-ball in M with boundary S. This proves irreducibility without assuming orientability of M.

## 3. The exact intersection argument

Use the disk model RP²=D²/(antipodal boundary). Let C be the image of ∂D² crossed with I, and let A₀ be the image of a diameter crossed with I. Both are proper one-sided annuli. Their intersection is a single spanning arc.

For a bottom-fixed PL concordance h, its top restriction a is homotopic to the identity by `(x,t) -> pr_RP² h(x,t)`. This is a PL homotopy of a compact surface. Epstein Theorem 6.3 supplies a jointly PL isotopy of a to the identity. The collar cutoff of A.123 extends it to M, with the whole bottom fixed. Thus h can first be assumed fixed on both boundary components.

Put B=h(A₀) in PL general position with C by an ambient perturbation relative the entire boundary. The boundary curves B∩∂M=A₀∩∂M meet C∩∂M in exactly one point on each of the two ambient boundary components. These intersections are transverse within the boundary surfaces. Proper local flatness and relative general position imply that B∩C is a compact PL one-manifold with exactly these two boundary points. Therefore it consists of exactly one arc and finitely many circles. The arc joins the two ambient boundary components, so it spans both B and C.

Every circular component is disjoint from this spanning arc in each annulus. An essential embedded circle in an annulus separates its two boundary circles and therefore meets every spanning arc. Consequently each circular component is inessential in each annulus, and bounds a disk in each. This is an intrinsic fact about annuli; ambient orientability is irrelevant.

Choose a circle innermost in C, bounding a disk D_C whose interior misses B. Let D_B be the disk it bounds in B. Then D_C∪D_B is an embedded PL sphere, after harmless corner straightening, and lies in int(M). By the preceding irreducibility argument it bounds a ball Q in int(M). The closure of B\D_B is connected, meets ∂M, and is disjoint from the sphere except along the common circle. Since Q lies in int(M), this remaining annulus part lies outside Q. Thus int(Q) misses B. The standard ball push moves D_B across Q to a disk close to D_C, removes the chosen circle and any circles in int(D_B), preserves the spanning arc, and creates no new intersections with C. A sufficiently small final collar of D_C is disjoint from the rest of C. Repetition leaves precisely one spanning arc.

## 4. A fully PL twist model

This replaces the source's polar formula. Let D be a centrally symmetric polygonal two-disk, with antipodal linear involution J. Parametrize its polygonal boundary by R/2Z so that J is theta -> theta+1. For s in I, the circle translations c_s(theta)=theta+s form a jointly PL family, since addition followed by reduction modulo2 is PL on a finite subdivision. Every c_s commutes with J on the boundary.

Choose a PL collar ∂D×[0,delta] of the disk boundary. Define

`r_s(theta,v) = ( c_{max(0,s-v/delta)}(theta), v )`

on this collar, and the identity off the collar. Here v=0 is the boundary and v=delta is the inner edge. This is a jointly PL isotopy from the identity. Each slice preserves v, its inverse uses the inverse circle translation at the same parameter, and the formulas glue at v=delta. Its endpoint r₁ agrees with J on ∂D.

The disk homeomorphism b=J⁻¹r₁ is PL and fixes ∂D. A relative Alexander isotopy deforms b to the identity. Concatenate r_s with J times that isotopy. The resulting disk isotopy R_s runs from id to the exact linear half-turn J, and its boundary commutes with the antipodal identification at every time. During the first segment its boundary makes one half-turn; during the second it stays equal to J. Therefore R_s descends to a jointly PL isotopy k_s of RP² preserving C.

Repeat the path, composing by the appropriate powers of J, or use its reversed inverse path for negative integers. This constructs k^i_s from id to J^i with winding i on the projective boundary circle C. Let

`T_i : M -> M,       T_i(x,y)=(k^i_y(x),y).`

It is a jointly PL level-preserving homeomorphism, fixes the bottom, and its top restriction J^i preserves the diameter A₀∩(RP²×{1}) as a set. Put A_i=T_i(A₀). Then A_i and A₀ have the same boundary subsets, and A_i∩C is a spanning arc of winding i. Moreover T_i is in the identity component of the bottom-fixed concordance group: replace y by `rho(s,y)=max(0,s+y-1)`, retaining y and s as output coordinates. This starts at id, ends at T_i, and fixes the entire bottom throughout.

## 5. Proper disks with common boundary in a ball

Each proper PL disk in a PL three-ball Q cuts it into two PL three-balls. Indeed, append the disk to either of the two disks in ∂Q bounded by its boundary circle, and apply polyhedral Schoenflies to the resulting sphere; the side contained in Q is the required ball. The local corner along the circle can be straightened in a collar.

Now let D₁,D₂ be proper PL disks in Q with identical boundary. Choose any PL homeomorphism j:D₁→D₂ fixed on that boundary. On each of the two complementary balls of D₁, glue j to the identity on its complementary boundary disk in ∂Q. This gives a PL homeomorphism of its boundary sphere to that of the corresponding complementary ball of D₂. Cone extension through chosen PL ball parametrizations extends it over the ball. The two extensions agree on D₁ and glue to a PL homeomorphism H:Q→Q fixed on all of ∂Q and carrying D₁ to D₂.

The relative PL Alexander isotopy joins H to id. Its joint PL property is explicit: on any piece where H(x)=Lx+b, the coning formula tH(x/t)=Lx+tb is affine in (x,t), on a finite conical polyhedral subdivision. Reversing that isotopy gives the required ambient disk isotopy relative ∂Q. No ambient winding invariant is used.

## 6. Applying the disk lemma and removing the annulus action

By Epstein's proper-arc theorem, the unique intersection arc B∩C can be carried to the unique arc A_i∩C with the same winding, by a PL isotopy of C fixed on ∂C. Extend this isotopy to M relative ∂M using the normal-bundle formula below. Cut M along C. The result is a PL three-ball D²×I. Each annulus B and A_i, cut along its spanning intersection arc, becomes a proper PL disk, and the two disks have identical boundary in the cut ball. The disk lemma supplies an ambient isotopy fixed on the cut-ball boundary. Gluing it back gives an ambient isotopy relative ∂M carrying B to A_i.

After this isotopy and composition with T_i⁻¹, the resulting concordance g preserves A₀ setwise. Its restriction to A₀ is a bottom-fixed annulus homeomorphism. A.123 proves that such a map is isotopic to the identity through bottom-fixed annulus homeomorphisms. Extend an inverse such isotopy to M using the normal-bundle formula. The resulting g fixes A₀ pointwise.

The normal-side cover of A₀ is the connected two-sheeted cover of this one-sided annulus. A map fixing A₀ pointwise acts on that cover by one constant deck choice. At the bottom this choice is the identity, because g fixes the entire bottom RP² pointwise. Thus it is the identity on the whole side cover. Cutting M along A₀ yields a three-ball on which g fixes the side double-cover of A₀ and the bottom disk. Its only possible nonidentity boundary map lies on the top disk, where it fixes the boundary circle. A disk Alexander isotopy, extended over an upper collar, removes this top map while preserving the bottom and side. The remaining ball map fixes all its boundary and is contracted by the relative PL Alexander isotopy. Gluing back contracts g through bottom-fixed concordances.

## 7. Explicit extension from a one-sided annulus

Let A be either one-sided proper annulus, with its connected side cover q:tilde A→A and deck map d. A PL regular neighborhood has the model

`N(A)=(tilde A × [-delta,delta]) / ((p,v)~(d(p),-v)).`

Given a jointly PL annulus isotopy c_s starting at id, lift it uniquely to tilde c_s starting at id. The lifts commute with d. Set tau(s,r)=max(0,s-r/delta). On N(A) define

`[p,v] -> [ tilde c_{tau(s,|v|)}(p), v ].`

The formula is invariant under the quotient relation. It is the desired c_s on the zero section and the identity on the outer neighborhood boundary. Its inverse uses tilde c_tau⁻¹ at the same unchanged |v|. It is jointly PL by composition of finite PL maps, including absolute value and max. Extend it by the identity off N(A). If c_s fixes a boundary circle, the lifted isotopy fixes its full inverse image, so the ambient extension fixes the corresponding entire boundary surface. Thus both arc alignment and the annulus-restriction correction have exactly the required relative boundary behavior.

## 8. Audit conclusion and remaining editorial check

The geometric proof is valid with the stated PL twist replacement and the explicit annulus-action correction. Neither the published infinite cyclic mapping-class assertion nor its ambient winding invariant is used. All constructed maps preserve their claimed boundaries and have finite PL total maps. The actual A.127 draft should include these corrections before promotion. This note is separate research material during checkpoint09's source freeze.

## 9. Full revised draft read: PASS

**Completed:** 2026-11-19 17:42:46 UTC, actual clock-tool value. The approximate 17:45 in a preliminary message was an overestimate and was corrected to the parent immediately; it is not a verification timestamp.

Read the entire `agents/singularities_duality/logs/A127_projective_plane_draft.tex` after the author integrated the fully PL twist construction. The proof passes. In particular, its choice `min(u,t)` also has the required endpoint and bottom conditions and is jointly PL. The normal-bundle extension retains the normal absolute coordinate, so its inverse uses the same parameter and is well defined. All cut-ball isotopies fix the entire side cover before descent.

Minor exposition corrections sent to the author: the punctured annulus has the additional boundary circle ∂D_A on the auxiliary sphere, so one should use its connected complement of that circle, containing the two original boundary circles on ∂M, to show it lies outside the ball. If a_u is the top-map isotopy from a to id, the explicit ambient correction uses c_u=a_u a⁻¹ and `(x,t) -> (c_min(u,t)(x),t)`. The zero twist uses the constant path. The normal-side action is initially known to be the identity *at* the bottom, from which local constancy gives identity everywhere. These are local wording clarifications and do not alter the proof or create additional hypotheses.
