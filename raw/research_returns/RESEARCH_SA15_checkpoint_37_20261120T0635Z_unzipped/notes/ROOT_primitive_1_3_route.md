# Primitive type (1,3): live proof route, not a promoted assertion

Started in the actual 04:39–04:46 UTC interval on 20 November 2026. This note is research in progress. It is not an hourly gate reduction, and none of its assertions has yet been added to the canonical paper. The general primitive-system wall and every fixed degree17 full-image claim remain open.

## Candidate Frobenius stability lemma

Let A be an abelian surface over an algebraically closed field of characteristic2, F:A→A^(2) relative Frobenius, and L a line bundle with odd Euler characteristic. Put E=F_*L, a rank4 bundle. For any ample polarization on A^(2), E should be slope stable.

The complete canonical Frobenius filtration has graded pieces L, L⊗Ω_A^1, L⊗Λ²Ω_A^1. Thus U=F^*E⊗L^-1 is unipotent of rank4, with a filtration by O_A and graded multiplicities1,2,1. This is also the explicit local diagonal-ideal filtration with two generators whose squares vanish. The original full proof of Sun, arXiv:math/0608043v2, Definition3.1, Lemmas3.2,3.3,3.5 and Theorem3.6 was opened in the web source, printed pages5–9. No stability theorem for abelian surfaces is imported from Sun's curve theorem.

Since U is an extension of degree-zero line bundles, it is slope semistable, so E is semistable by flat pullback. Suppose a saturated proper subsheaf Q⊂E has equal slope and rank q. Then S=F^*Q⊗L^-1 is a saturated slope-zero subsheaf of U; its quotient is torsion free because F is flat.

Here are two proposed complete routes to χ(S)=0, awaiting independent review.

1. Intersect S with an O-filtration of U. Each nonzero graded piece is a rank-one subsheaf I_Z(-D)⊂O_A, with D effective and Z zero-dimensional. Equality of total degree with zero forces every D=0. Hence det S is trivial and χ(S)≤0. The torsion-free quotient T=U/S has slope zero; T* embeds in U*, so the same argument gives χ(T*)≤0. On the smooth surface T** is locally free, χ(T**)=χ(T*) by Riemann–Roch and trivial canonical bundle, and χ(T)=χ(T**)-length(T**/T)≤0. Since χ(U)=0, additivity gives χ(S)=χ(T)=0.
2. Mono's alternative: every unipotent bundle becomes trivial after some pullback by [2]^m. Induct along an O-filtration; after trivializing the previous part, one further [2] kills its extension class because [2]*=0 on H¹(O_A). The saturated pullback of S into O_A^4 has degree-zero determinant and a nonzero Pluecker section. That determinant is trivial, the Pluecker map is constant, and saturation makes the subbundle a fixed trivial summand. Thus S is locally free by faithful flat descent and χ(S)=0 by finite-flat Riemann–Roch. This route must retain the saturation argument at codimension2.

Either route gives c1(S)=0 numerically. Riemann–Roch then gives

    χ(S)=4χ(Q)-qχ(L)=0.

Because χ(L) is odd, 4 divides q, impossible for 1≤q≤3. This proves the proposed stability lemma if the displayed filtration and subsheaf arguments are fully checked.

## Candidate nonzero Cartier tensor in type (1,3)

Now assume L is ample, globally generated, of type(1,3), and A is nonordinary. Thus h0(L)=χ(L)=3 and L²=6. The relative Cartier trace pairing on E=F_*L has target L^(2), is perfect, and is alternating because C_rel(ω_A)=0. Its restriction to global sections is

    β:Λ²H0(A,L)→H0(A^(2),L^(2)).

Under a level3 theta structure, both sides are three-dimensional irreducible Heisenberg representations of central weight2. Therefore β is zero or an isomorphism. In Schrödinger bases, a nonzero tensor has β(e_i,e_j)=c e_k^(2), where {i,j,k}={0,1,2}, with one nonzero scalar c.

If β=0, the saturation Q of the evaluation image H0(L)⊗O→E is isotropic and has rank1 or2. If rank1, Q has at least three independent global sections. If rank2, the nonzero wedge-evaluation map Λ²H0(L)→H0(det Q) is injective by theta irreducibility, so det Q again has at least three sections. Stability gives (det Q).L^(2)<3q≤6.

An effective divisor H on an abelian surface is nef, by translating it away from each test curve. If H²>0 it is ample; then h0(H)=H²/2≥3, and Hodge gives H.L^(2)≥6. If H²=0 and h0(H)≥3, the expected standard description is H pulled back from a degree n≥3 line on an elliptic quotient, so H≡nE0 for an elliptic fibre E0. Global generation of L^(2) forces L^(2).E0≥2, because a degree1 line on an elliptic curve is not globally generated. Again H.L^(2)≥6. The full proof/source of this degenerate effective-divisor description must be read before promotion. This contradicts stability and proves β≠0.

## From the tensor to a family: remaining details

The nonzero Heisenberg tensor gives the usual alternating3x3 coefficient matrix. Its Euler Frobenius determinant is, up to nonzero scalar, the Fermat cubic s0³+s1³+s2³. The dual alternating matrix has rank2 at every nonzero functional. The cohomological full-radical calculation should therefore specialize to rank2, and the primitive theta-degree argument forces K=0. Every map and actual comparison with the smooth-curve local system still needs to be written, including nonemptiness of the smooth locus and existence of a suitable smooth wall member.

OC supplied a possible separability argument. If K=k(A), f=s1/s0 and g=s2/s0, then the induced subfield k(f,g) is rational of transcendence degree2 because L is ample and globally generated. Let τ:K→K² be the Cartier trace functional in the s0² volume trivialization, with τ(1)=0. Since β is invertible with target spanned by the Frobenius-twisted original sections, τ(f),τ(g),τ(fg) belong to k(f,g)² up to one common nonzero scalar. If df∧dg=0 and f is not a square in K, write g=A+Bf with A,B∈K². Projection formula gives B=τ(g)/τ(f), A=τ(fg)/τ(f), hence both lie in k(f,g)². This contradicts p-independence of f,g inside k(f,g). If both f,g are squares, every β value is zero. This needs precise relative-Frobenius typing but appears to prove generic separability.

CAUTION: generic separability of a finite basepoint-free map alone does not establish Bertini smoothness in characteristic2. A rank-zero critical divisor could still obstruct a smooth general member. Do not omit this last issue or silently assume a primitive polarization has smooth members. A theorem under an explicitly verified smooth-family hypothesis would be narrower and must be labelled as such.

## Literature queries actually executed

Queries: “Frobenius direct image line bundle abelian variety stable Euler characteristic coprime rank”; “abelian surface type (1,3) characteristic 2 Cartier Hasse Witt monodromy”; stronger follow-ups “Frobenius abelian line bundle stable direct image” and “Frobenius abelian coprime Euler”. The first batched output was partly truncated; only actually visible results were used for follow-up.

Sun (2006), *Stability of direct images under Frobenius morphism*, arXiv:math/0608043v2: introduction and complete higher-dimensional filtration proof opened, Definitions3.1/3.4, Lemmas3.2/3.3/3.5, Theorem3.6, printed pp5–9. The curve stability theorem is not invoked in dimension2.

Catanese and Sernesi, *The Hesse pencil and polarizations of type(1,3) on Abelian surfaces*, arXiv:2212.14877v1: introduction, Theorem0.1 statement and bibliographic pointers opened only. No characteristic2 theorem was identified, no proof imported, and no whole-paper audit claimed.

This note claims no priority and no completed A.4 reduction.
