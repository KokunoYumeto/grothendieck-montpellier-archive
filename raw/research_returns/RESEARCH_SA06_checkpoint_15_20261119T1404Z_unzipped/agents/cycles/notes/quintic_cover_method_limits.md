# Complex quintic top quotient: two precise cover-method limits

Research note, 2026-11-19. These calculations delimit attempted methods; they do not prove that the general rational ordinary top quotient is nonzero. The positive Fermat theorem C.3au remains a separate, fully audited result.

Let V be a smooth quintic surface in P³ over C, H=O_V(1)=K_V. The first relative top K0 component of its split cone is H²(V,H) tensor Omega¹_C/Q. A proposed method is to use a smooth proper generically finite f:T→V, actual Picard first jets a in H¹(T,f*H), and degree-zero line bundles on T. The trace of their cup product is the relevant first-conormal invariant. Merely increasing q(T) does not ensure that this trace is nonzero.

## 1. Finite base change of one nodal pencil

Choose a transverse pencil in |nH|, n at least one. Its blow-up S is the divisor of bidegree (n,1) in V times P¹. Write pi:S→P¹ and H'=pullback H. The exact sequence

`0 → O_V(1-n) external O_P1(-1) → O_V(1) external O_P1 → H' → 0`

and the ACM cohomology H¹(V,O_V(a))=0 give

`R¹ pi_* H' = O_P1(-2) direct_sum O_P1(-1)^(h0(V,O(n))-2)`.

Indeed H²(V,O(1-n)) is dual to H⁰(V,O(n)), H²(V,H)=C, and the map to O_P1 is the row consisting of the two independent pencil sections. After choosing a basis its kernel is exactly the displayed bundle. The same computation for O_S shows that R¹ pi_* O_S is a subbundle of a sum of O(-1), hence all its splitting summands have strictly negative degree.

Suppose the pencil fibres are nodal and make a finite smooth-curve base change B→P¹. Resolving the resulting A-type rational double points does not change either pushforward calculation: R¹ of the resolution on O is zero, and projection formula treats H'. Flat cohomological base change pulls back the displayed bundles. They still have no global sections. Thus H¹(T,f*H) comes entirely from H¹(B,pi_*f*H), while H¹(T,O_T)=H¹(B,O_B). Pullback identifies Pic⁰(B) with Pic⁰(T) up to isogeny; over C its point map is surjective. Cup products of the two H¹ groups therefore factor through degree-two cohomology on the curve B and vanish. All Picard-first-jet times Pic⁰ products from this class of covers have zero invariant.

This calculation assumes exactly the nodal-pencil/rational-double-point resolution scope stated above. It does not apply to the non-nodal product domination used in C.3au.

## 2. Smooth product base change of a finite plane projection

Choose a point outside V and project to obtain a finite flat map rho:V→P² of degree five. In a fibre coordinate z of O_P2(1), its equation is monic of degree five, so

`rho_* O_V = O direct_sum O(-1) direct_sum ... direct_sum O(-4)`.

Let W=C times D be a product of smooth proper curves, and let g:W→P² be finite with M=g*O(1) an ample external product. Assume the fibre product T=V times_P2 W is smooth, and write q:T→W and f:T→V. Then

`q_* O_T = direct_sum_(j=0..4) M^(-j)`,

`q_* f*H = direct_sum_(j=0..4) M^(1-j)`.

For every positive j, H¹(W,M^(-j))=0 by the product Kunneth formula: each negative line bundle on a curve has zero H⁰. Hence

`H¹(T,O_T)=H¹(W,O_W)`,

`H¹(T,f*H)=H¹(W,M) direct_sum H¹(W,O_W)`.

The norm composed with pullback on Pic⁰(W) is multiplication by five, and the tangent dimensions agree. Consequently Pic⁰(W)→Pic⁰(T) is an isogeny and is surjective on C-points. All products under consideration therefore remain in the j=0 or j=1 summands of H²(T,f*H).

The relative dualizing line for q is q*M⁴. Thus

`K_T tensor (f*H)^(-1) = q*(K_W tensor M³)`.

The pullback of the generator of H⁰(V,K_V tensor H^(-1)) is q*Jac(g), and lies in the j'=0 summand of

`q_*(K_T tensor (f*H)^(-1)) = direct_sum_(j'=0..4) K_W tensor M^(3-j')`.

For a monic degree-five equation F(z), the finite-duality trace is normalized by the elementary identities

`Tr(z^j/F'(z))=0 for j=0,1,2,3; Tr(z^4/F'(z))=1`.

They follow from Lagrange interpolation on the generic separable fibre, hence extend as the dualizing trace. It follows that the Serre pairing with q*Jac(g) sees only the j=4 summand of H²(T,f*H). The Picard products occupy j=0,1, so their trace to H²(V,H) is zero.

This is a calculation for the stated smooth finite base changes with an ample external product M. It does not exclude a different cover, a modification with additional exceptional terms, or a nonexternal line bundle. No general statement about all ordinary families follows.

## Remaining task

For a general complex quintic, an actual family producing the missing first-conormal trace is still required, or a genuine invariant annihilating every actual ordinary family must be constructed. A cohomological linear span or a varying henselized family is not sufficient. C.3au succeeds for the explicit Fermat surface through a different cover and does not supply either universal conclusion.
