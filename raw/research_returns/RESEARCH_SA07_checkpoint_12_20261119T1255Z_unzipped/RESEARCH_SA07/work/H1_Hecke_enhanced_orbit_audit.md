# Exact enhanced Hecke orbit and arithmetic bi-algebraicity audit

Completed proof: 19 November 2026, 12:47 UTC; independent elliptic audit passed, with the explicit xi/quasi-period sign correction incorporated before the clock check at 12:48:26 UTC. Work-only; no claim that H1 has been resolved.

## 1. The actual framed moduli space and period map

Let B be the smooth irreducible threefold of elliptic curves equipped with an ordered de Rham basis (omega,eta), with omega nonzero holomorphic and cup(omega,eta)=1 in a fixed algebraic trace convention. It has the usual Weierstrass presentation with three parameters and nonzero discriminant. Fix complex cycles delta_1,delta_2 of intersection one and write periods as rows:

P=((omega_1,omega_2),(r_1,r_2)), det(P)=kappa, where r_i is the period of the framed form eta,

where kappa is the fixed nonzero Legendre constant. No algebraicity of kappa or of any entry of P is asserted.

The exact source map is Movasati, arXiv:0806.3926v1, 24 June 2008, section 2 printed p.4 and Proposition 2 with proof printed p.7. His cycles are rows, forms are columns, and the matrix is divided by sqrt(2 pi i). Transpose and multiply back by that fixed scalar to obtain P. His four-dimensional period map is locally biholomorphic: the proof computes a nonzero derivative determinant. The concluding identity F_0(x)=det(x)^(-1) identifies the t_0=1 slice with the fixed-determinant period hypersurface. Therefore the period map of B is locally biholomorphic to the open period domain in {det P=kappa}, modulo the discrete cycle-change action. Only this local statement is used here.

Fresh original PDF opened as turn487882928view0, exact Proposition 2 and determinant identity read in turn613461898view1. Elliptic independently reopened the same primary pages and confirmed the transpose, normalization and determinant slice.

## 2. Degree-one rational quasi-isogenies give the actual matrices PM

Put Lambda=(omega_1,omega_2) Z^2. For M in SL_2(Q), let Lambda_M=(omega_1,omega_2) M Z^2. These lattices are commensurable and have the same oriented area. Choose an integer q>0 such that q Lambda is contained in Lambda_M. Then

phi_M: C/Lambda -> C/Lambda_M, [u] -> [q u]

is an actual isogeny. Its degree is

[Lambda_M:q Lambda]=q^2 Area(Lambda)/Area(Lambda_M)=q^2.

The rational quasi-isogeny f_M=(1/q)phi_M has degree one and is analytically induced by the identity on C. The symbol 1/q means multiplication by the rational scalar in Hom(E,E_M) tensor Q. On de Rham cohomology,

f_M^*=(1/q)phi_M^*: H^1_dR(E_M) -> H^1_dR(E)

is an invertible algebraic linear map. Define the target forms uniquely by f_M^*omega_M=omega and f_M^*eta_M=eta. Since cup(f_M^*u,f_M^*v)=deg(f_M)cup(u,v), this remains a symplectic frame. Relative to the lattice basis given by M, its period matrix is exactly PM.

For an algebraic source frame, the construction is algebraic over Qbar. More explicitly, the kernel of phi_M is a finite torsion subgroup of E, so the quotient exists over a finite algebraic extension; inverse pullback of the source forms and rational scaling give algebraic target forms. This construction does not assert that the analytic identity is itself an actual degree-one morphism; it is the specified rational quasi-isogeny, represented by phi_M/q.

If the source frame is defined over K, applying sigma in G_K gives sigma(phi_M)/q and the transported target frame; therefore the whole degree-one quasi-isogeny orbit is G_K-stable. This is the exact coherence, without commuting sigma with complex conjugation.

## 3. The full enhanced orbit is Zariski dense

Let O be this orbit of an arbitrary complex framed point b in B. Suppose a closed algebraic subvariety Z contains O. Work in a small period chart about P, where the source local isomorphism has an inverse psi. For M near I in SL_2(C), the function

M -> F(psi(PM))

is holomorphic for every local defining function F of Z. It vanishes for every rational M in that neighbourhood, because psi(PM) is the transported framed point constructed above. Rational points of SL_2 are dense in its real points: near I use the coordinates

(a,b,c) -> ((a,b),(c,(1+bc)/a)), a nonzero.

Hence the function vanishes on a real open box in those three coordinates. The one-variable identity theorem, successively in a,b,c, makes it zero on the complex neighbourhood. Right multiplication M -> PM is an isomorphism from SL_2(C) to {det Q=kappa}; thus Z contains an open subset of B. Irreducibility gives Z=B.

This proves, unconditionally and for every complex source point, that the enhanced degree-one rational quasi-isogeny orbit is Zariski dense. Algebraicity of the starting frame adds algebraicity and Galois stability of the orbit but does not change this computed closure.

Use the established Weierstrass convention xi=x dx/y, whose periods are minus the quasi-periods eta_i. The actual Hodge frame is eta_frame=xi+h omega, so its row r is minus c times the conjugate omega row. Real M preserves this identity, and det M=1 preserves the area and c itself. Thus the entire orbit still consists of actual Hodge frames, with the actual scalar c retained. Its real Hodge locus is a uniqueness set in the complex threefold; it need not be an algebraic locus.

This exact density theorem resolves the specific proposed use of a proper algebraic locus containing the entire transported orbit: such a locus is the whole B. It makes no assertion against the use of a separately constructed proper locus meeting a selected suborbit, and proves no H1 transcendence statement.

## 4. The same orbit does not produce a second point on the fixed-period leaf

The Ramanujan leaf used in the earlier audit fixes the two r_i periods of eta in a transported cycle chart. For the actual Hodge frame the real-linear map R^2 -> C with row r=(r_1,r_2)=-c(conjugate omega_1,conjugate omega_2) is invertible. Hence r M=r for a real 2x2 matrix M forces M=I, column by column. Allowing an integral cycle change only replaces M by that change and yields the same framed moduli point. Consequently this explicit degree-one orbit does not supply a second distinct point on the same fixed-eta-period leaf. The equality is checked on the full unscaled period row.

## 5. Exact substitution into the opened orbit theorem

Orr, *Families of abelian varieties with many isogenous fibres*, arXiv:1209.3653v4 (13 September 2016), Theorem 1.2 p.1, assumes a fixed algebraic curve in A_g containing a Zariski-dense intersection with an isogeny class. Its proof uses rational isogeny matrices, so growing degrees of the algebraic output points alone do not prevent its counting argument. The actual forgetful morphism here is

B -> M_1, (E,omega,eta) -> [E].

It removes the chosen eta complement. On M_1 the full isogeny orbit has closure the modular curve, and the conclusion that this curve is weakly special leaves no additional equation on eta. Upstairs, section 3 identifies the closure of the full framed orbit as B. A new application retaining the complement would need an additional fixed proper algebraic constraint or another theorem with a different, explicitly verified input.

The opened Orr version itself records a gap in the published Lemma 3.3 proof, repaired by Proposition 4.A, added in 2016. Read exact note p.4 and Proposition 4.A pp.21-22: the repair bounds the period matrix as well as the rational isogeny matrix. This audit uses the corrected v4; it does not label the uncorrected journal proof as independently checked.

## 6. The actual map to Gao's Betti algebraic structure

Gao, *Enlarged mixed Shimura varieties, bi-algebraic system and some Ax type transcendental results*, Forum Math. Sigma 7 (2019), e16, pp.2-3, defines the relevant arithmetic structure on the universal-extension uniformizer via H_1(E,Z) tensor Qbar. The canonical algebraic universal extension itself and its canonical model are discussed in Theorem 4.4 pp.29-31. Section 9, especially pp.60-62, uses special/arithmetic-bi-algebraic points; mere Qbar points of the algebraic target do not supply those input coordinates.

For this paragraph retain the fixed algebraic second-kind class xi=x dx/y, with periods -eta_i. The Hodge frame used above is eta_frame=xi+h omega and r_i=-eta_i+h omega_i. The actual Lie coordinates (u,s) are dual to the coframe (omega,-xi), so ds represents -xi; they are not dual to (omega,xi). In these explicitly named Lie coordinates the Betti-to-de Rham Lie isomorphism sends (z_1,z_2) to

(u,s)=(omega_1 z_1+omega_2 z_2, eta_1 z_1+eta_2 z_2).

The inverse image of L_h={s=h u} is therefore

(eta_1-h omega_1)z_1+(eta_2-h omega_2)z_2=0,

which becomes z_1+conjugate(tau)z_2=0 using eta_i-h omega_i=c conjugate(omega_i). Thus L_h is defined over Qbar in this Betti structure exactly when conjugate(tau) is algebraic. For an algebraic elliptic curve, the retained Schneider theorem identifies that case with CM. Algebraicity of h in the de Rham basis supplies the line in a different named vector space; the displayed comparison gives the precise unproved implication needed to turn it into the source's Betti-coordinate condition. No such implication is inferred here.

## 7. Scope and source status

The only new proved closure is the full enhanced degree-one quasi-isogeny orbit computation and its exact relation to the fixed-period leaf. H1, the non-CM algebraicity of the actual h, remains open. The differential scalar c is present throughout. No conditional theorem is asserted, and no main-gate movement is claimed.

New originals retained locally: work/sources_audit_next/Gao2019_EMSV.pdf/.txt (full final 65 pages), Orr2016_v4.pdf/.txt (full corrected 26-page preprint). Movasati2008 was reopened directly and is already represented by the existing elliptic bibliography key; its pp.4,7 exact local period map is the sole external input to section 3 beyond elementary complex analysis and the explicit isogeny construction.


### Consulted source gates and search record

The final Richard--Yafaev 2024 Compositio article *Height functions on Hecke orbits and the generalised Andre--Pink--Zannier conjecture*, DOI10.1112/S0010437X2400722X, was located by primary publisher metadata; its full theorem was not imported here. The 2025 Comptes Rendus article *Generalised Andre--Pink--Zannier conjecture for Shimura varieties of abelian type*, DOI10.5802/crmath.751, was located by primary metadata, but opening its journal page returned403. No statement from that inaccessible article is used. The exact corrected Orr target is sufficient for the substitution audit actually performed.

Queries in this continuation included Hodge splitting/Hecke algebraicity, almost-holomorphic E2 values, Ramanujan algebraic points/Hecke, generalised Andre--Pink--Zannier heights, and enlarged mixed Shimura/universal-vector-extension arithmetic bi-algebraicity. Spence's chi-star result and the Choi--Lim harmonic-form orbit result were found to have already been read and checked in the existing elliptic note; no duplicate result was claimed.

The Kleinman1994 primary PDF was opened during the separate F.3.36 source check but supplied no parsed text in that call. The parent is independently inspecting it. This agent's F.3.36 proof uses the fully read original Kleiman1968 Theorem2A11/Remark3.10 instead.
