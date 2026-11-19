# SA15 (Cristaux), sweep 3, cote 8 (scans 1-81): reading and working-through

Claude Opus 5.5 at effort max, SA15-c7_c8-part2, sweep 3 reader (launched by the SA15 c7_c8 reader, Claude Opus 5.5 at
effort max). Written 18-19 Nov 2026 (UTC). Shared brief: `sweep3/READER_BRIEF.md`. What sweep 3 already did on SA15
(cotes 4, 6, 100) is in `sweep3/SA15/STUDY.md` and is not repeated here.

**Sources read.** Pro transcription of every page (package `MPL_7_061-072+8_001-078`: scans 1-18 from run 32, scans
19-78 from its continuation 32b; package `MPL_8_079-081+9+4+100` for scans 79-81), through the reader tool and, where
the tool hides cancelled text or a reading matters, the raw `.tex` (with `keepdel`). Pro research notes for cote 8 (lines
89-646, cross-context register, reused-sheet table, references) and for 79-81 (notes 1-9). Codex/Work second witness
K8-01 (scans 79-81). Michel Hua's project, `transcripts/8/8.modern.tex`, grepped where a reading was in question. Scan
images rendered for 8:6, 8:30, 8:44, 8:50, 8:58, 8:75, 8:78, 8:81. 77 pages read: scans 1-81 except the four blank
scans 24, 28, 33, 77 (checked blank on 12 Nov, `DROPPED_SCANS_CHECK_20261112.md` rows 44-47).

**What the cote is.** Of the 77 pages, 47 are handwritten (his, except 8:30 whose hand I leave open; 8:58-60 are tables
without words), 29 are reused typed or printed leaves, which in this cote alternate with his sheets (he wrote on scrap),
and 8:1 is the cover. His pages form six pieces:

| # | Scans (his) | Subject | Item |
|---|---|---|---|
| A | 2, 4-6, 8, 10, 12-14, 16, 18, 20, 22 | finite locally free groups killed by p (and truncated BT of level 1) over a base of characteristic p: a crystal with F, V, two triangles on the crystalline site, a "descended" triangle of co-Lie complexes on the Zariski site, and the obstruction to the descent | SA15-2 |
| B | 17 (cancelled) | indeterminacy (a torsor under mu_2-torsors on the adeles) and rigidity of the enriched data of a motive over Z | SA15-6 (not SA15-13) |
| C | 25-27, 29, 31 | ordinary Barsotti-Tate groups over a smooth S_0 with a Frobenius lift: the "Dieudonne module" category C, gauge formulas, F-crystals with connection, rank one | SA15-3 (as sweep 2 names it) |
| D | 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56 | "Determination du module de Dieudonne filtre du groupe de Lubin-Tate": Dieudonne module of formal A-modules, the lift by deformation theory, Tate's Hodge-Tate decomposition and the periods | SA15-3 (sweep 2), better its own item |
| E | 61, 63, 65, 67, 69, 71, 73, 75 | Tannakian group of a category with a fibre functor to filtered F-isocrystals; motives over S in Spec Z with Betti, l-adic, de Rham, crystalline realizations, Frobenius elements, period points; an agenda of conjectures | SA15-6 |
| F | 78-81 | "Complexe de co-Lie des groupes de t.m.": the co-Lie complex of a group of multiplicative type, the canonical class in Ext^2, the obstruction to lifting over Z/p^2 ("d'apres Illusie") | SA15-8 |

Also: 8:1 is the institutional cover; 8:30 is a handwritten sheet on families of charts (not crystals); 8:58-60 are
squared-paper tables of fractions without words. The reused leaves are listed in section 2.

**Most important findings (details below).**
1. 8:81: his expectation that the universal lifting obstruction for GL(d, F_p) is "sans doute pas nulle" for d >= 2 is
   false in exactly three cases, (d, p) = (2, 2), (2, 3), (3, 2), and true in all others (proof for p >= 5; explicit
   sections for the three exceptions; a linear-algebra computation over F_p for (3, 3) and (4, 2); a block lemma for the
   rest). Michel Hua's project already notes the case (2, 2).
2. 8:78: the boxed formula (co-Lie complex of D(M) = M (x)^L O_S) is right; it matches Bergh-Rydh, Prop. B.4 (opened, see
   the literature route), and the transitivity triangle he credits to Mazur-Roberts is credited to them by Illusie, CCD
   II, VII 3.1.1.5 (opened). The heading reads "Complexe de co-Lie", not "cotie".
3. Errors on his pages, each with its correction: the sign of the gauge map in the rank-one classification (8:31); the
   cotangent space of the Lubin-Tate group written Omega/p Omega instead of Omega/pi Omega (8:44); the sign in
   "Omega = pi^alpha omega_G" (8:50); "si T_p est pleinement fidele (dans ce cas seulement) G est l'enveloppe
   algebrique" (8:63) holds only one way; the deformation step for Lubin-Tate (8:46) needs e < p-1, not e <= p-1.
4. 8:25-27: the datum Fil_0 in his category C is determined by the rest and always exists (S_0 smooth over a perfect
   field), so C is the category of ordinary Dieudonne crystals with connection; his question is answered by the later
   crystalline Dieudonne theory.
5. Placements: sweep 2's lists for cote 8 merge different reused typescripts and copy cote-7 scan numbers; SA15-13 joins
   a printed page of Lipman to his cancelled adelic note. Corrections in `c7_c8_part2_CORRECTIONS.tsv`.

## 1. The items, in page order

### 8:1 (cover)
"INSTITUT MONTPELLIERAIN ALEXANDER GROTHENDIECK" cover with a drawing. Nothing to work through.

### A. Finite locally free groups killed by p: crystal, triangles, Zariski descent (8:2, 4-6, 8, 10, 12-14, 16, 18, 20, 22)

**What he does.** S of characteristic p; the crystalline topos S_cris over F_p (later over Z_p) and two morphisms of topoi
phi: S_cris -> S_zar and epsilon: S_zar -> S_cris with phi o epsilon = F_S, the absolute Frobenius (margin of 8:2). In
characteristic p the Frobenius of a divided-power thickening T of U factors through U (x^p = p! gamma_p(x) = 0 on the PD
ideal), which is what makes phi^*(E)_T = O_T (x)_{O_U} E a crystal; so phi^* epsilon^* is the Frobenius pull-back of
crystals and epsilon^* phi^* = F_S^*, as he uses on 8:6 and 8:13.
- 8:2 boxes C: omega -> omega^(p) and Pi: g^(p) -> g (Cartier-type map on invariant differentials, p-power map on the Lie
  algebra) and writes the co-Lie complexes as two-term complexes; 8:5 (cancelled) is a first formulation: to G a crystal
  D^*(G) with F, V, FV = VF = 0, the co-Lie complexes l^G, l^(G*) on S (perfect, amplitude [-1, 0]) and one triangle on
  S_cris with H^0 = H^1 = D^*(G).
- 8:4 (live): a) a crystal M on S_cris/F_p with F: M^(p) -> M, V: M -> M^(p), FV = VF = p (= 0 here); a perfect complex
  Delta^*(M) with H^0 = H^1 = M and two triangles (I)_cris, (II)_cris; b) perfect complexes l, l' on S_zar, amplitude
  [-1, 0], a triangle (III), and isomorphisms phi^*(l[-1]) = [M^(p) -F-> M], phi^*(l'^dual) = [M -V-> M^(p)] identifying
  (I) with phi^*(III). 8:6 checks the compatibilities of (III) with F and V; 8:8 lists the relations among the six maps.
- 8:10: groups not necessarily killed by p: a crystal of finite presentation over S_cris/Z_p with F, V, and two triangles
  (I): M (x)^L/F -> M^(p) (x)^L/p -> M (x)^L/V, (II): M (x)^L/V -> M (x)^L/p -> M (x)^L/F; descent of (I) to S_zar;
  extension to a PD thickening S' with p in the ideal ("prolongement de la filtration").
- 8:12 questions: are these structures stacks; is the partial forgetful functor faithful; is (omega, F_omega, V_omega) ->
  (crystal, triangles) fully faithful ("NB il est fidele"), at least for F_omega = 0 or when Ker F = Im V; can one attach
  a finite locally free group to (omega, F, V)?
- 8:13-14: the case of truncated BT groups killed by p (Ker F = Im V): from b), on H^1, a filtration 0 -> omega -> M ->
  nu' -> 0 with phi^*(omega) = Im V; on H^0, 0 -> n -> M -> t' -> 0 with phi^*(n) = Ker F; since Ker F = Im V, n = omega
  and t' = nu' ("Cela determine omega de facon unique !"); then V_omega: omega -> omega^(p) and F_t': t'^(p) -> t'.
- 8:16, 8:18: the data 1)-4) (crystal, triangle T on S_zar, isomorphisms alpha: phi^*(T) = I(M), beta: T_1 = epsilon^*
  Delta^*(M)) and the functor (omega, F, V) -> (phi^* omega, ..., T(omega), alpha, beta): "est-il pl. fidele ?? L'est-il
  du moins ... avec F_omega = 0 ?"
- 8:20: the descent problem as an obstruction problem: the choice lies in Ext^1(S_zar mod S_cris; D~_0, D~_1), the
  automorphisms in Ext^0(...) = 0, the obstruction "au theoreme" in Ext^2(...). 8:22: the six-term sequence 0 -> n_(G*)
  -> D^*(G)^dual -> t_G -> omega_(G*) -> D^*(G*) -> nu_G -> 0 and "H^1(D^*(G)^dual) = 0, Ker(H^1(n_(G*)) ->
  H^1_cris(n_(G*))) != 0".

**Checked (re-derived).**
- 8:10, triangles (I) and (II): they are the octahedral triangles of the two factorizations p = F o V on M and p = V o F
  on M^(p). With C(f) the cone of f: C(V) -> C(p) -> C(F) -> C(V)[1] is (II) and C(F) -> C(p on M^(p)) -> C(V) -> C(F)[1]
  is (I), with i_I = (id, V), pi_I = (F, id), i_II = (id, F), pi_II = (V, id) in degrees (-1, 0). So both triangles exist
  as soon as FV = p and VF = p; nothing else is needed.
- 8:8, the boxed relations, computed on these cones: i_II pi_I = (F, F) = F_X, i_I pi_II = (V, V) = V_X, pi_II^(p) i_I =
  (V^(p), V) = V_A, pi_I i_II^(p) = (F, F^(p)) = F_B, all as he boxes them (A = C(F), B = C(V), X = C(p)). The two
  composites of connecting maps marked "nul?" (d_I d_II: A -> A[2], d_II d_I: B -> B[2]) are zero already at chain
  level in this model, because both triangles are built from the same cones (d_II is the identity of M^(p) in degree -1,
  d_I the identity of M in degree -1, and their composite has nowhere to go). In an abstract derived category the
  vanishing would not follow from the triangle axioms; it does here.
- 8:13, "phi^*(n) = phi^*(omega), d'ou n = omega": true when S is reduced. Applying epsilon^* gives F_S^*(n) =
  F_S^*(omega) inside F_S^*(M); the equalizer of the two classifying maps S -> Grass is a closed subscheme through which
  F_S factors, so its ideal consists of nilpotents, hence is zero. On a non-reduced S the Frobenius pull-back alone does
  not separate subbundles (S = Spec k[e]/(e^2), M = O^2, n = <(1, e)>, omega = <(1, 0)>: F_S kills e, so F_S^* n = F_S^*
  omega), and the step needs the full crystalline phi^* (on a PD envelope T the map a -> a~^p is not zero on e). The page
  does not settle the non-reduced case.
- 8:13-14: V_omega and F_t' are well defined: omega^(p) = Im(V_M) (from phi^*(omega) = Im V after epsilon^*), so V_M maps
  omega into omega^(p); t'^(p) = Coker(V_M) because 0 -> omega^(p) -> M^(p) -> t'^(p) -> 0, and F_M kills Im V_M (FV = 0
  mod p), so F_M factors through t'^(p) -> M -> t'. As on the page.
- 8:20: the pattern (choices in Ext^1, automorphisms in Ext^0, obstruction in Ext^2 of the relative complex, i.e. the
  fibre of RHom_zar -> RHom_cris) is the standard one; "Ext^0(S_zar mod S_cris; D~_0, D~_1) = 0" is the injectivity of
  Hom_zar(D~_0, D~_1) -> Hom_cris(phi^* D~_0, phi^* D~_1), which holds for locally free D~ on a reduced S (same
  argument as for 8:13).

**What is wrong.** Nothing in the live text. 8:6 has "eps^*(pi_II) i_0 [=|] V_l[-1]" with a vertical stroke through the
equals sign (Pro: "!="; the scan shows "=" crossed by a near-vertical stroke). The argument on the page uses the
equality, which 8:4 introduced by definition ("'='"), and concludes "OK"; read it as an equality with a mark, not as an
inequality (a reading question, not decided on the ink).

**What is open (on the page).** Whether the triangle (I) descends (obstruction in the relative Ext^2 of 8:20); full
faithfulness of the functor of 8:12/8:18; the non-reduced case of 8:13. For F_omega = 0 the groups are those of height
one and are classified by (omega, V: omega -> omega^(p)) (SGA 3 VII_A, locator unverified; the Pro note E.39 cites de
Jong 1993, Prop. 2.2, p. 93, locator unverified here). Later theory: Berthelot-Breen-Messing (LNM 930, 1982) for the
crystalline Dieudonne functor of finite locally free groups; de Jong (1993; 1995) and de Jong-Messing (1999) for
faithfulness and full faithfulness over regular or excellent bases (locators as in the Pro notes, unverified here).

### B. 8:17 (cancelled, his): indeterminacy and rigidity of the enriched data of a motive over Z

**What he does.** Points 3 and 4 of a list: for (M, T) fixed (a motive over Z with its realization T and extra data at
the finite adeles A', at infinity and at p), the category of the extra data is a torsor under mu_2-torsors on A, so
their isomorphism classes form a torsor under H^1(A, mu_2) = prod_p Q_p^*/Q_p^*2, corrected in the margin to the
restricted product relative to Z_p^*/Z_p^*2 ("modulo une legere restriction en 2, donnee a l'infini"); automorphisms
H^0(A', mu_2) = prod_p Z/2. Rigidity: the equivalences between two enriched objects form, if nonempty, a torsor under
mu_2-torsors on Q trivialized over A; classes H^1(Q mod A, mu_2) = _2(J_Q) = (prod_p Z/2)/(+-1) ("puissance du
continu"); H^0(Q mod A, mu_2) = 0; the image of H^1(Q mod A, mu_2) in H^1(Q, mu_2) is zero; "l'equivalence restreinte ...
est determinee a isom unique pres".

**Checked.** With A = A_f (finite adeles): H^1(A_f, mu_2) = A_f^*/A_f^*2 (Kummer; Pic(A_f) = 0), which is the restricted
product of the Q_p^*/Q_p^*2 relative to the Z_p^*/Z_p^*2: his margin is right and the unqualified product is not.
mu_2(A_f) = prod_p {+-1}. Q^*/Q^*2 -> prod_p Q_p^*/Q_p^*2 is injective (a rational square in every Q_p has even
valuations, so is +-r^2, and -1 is not a square in Q_3). The exact sequence of the pair then gives H^0(Q mod A_f) =
ker({+-1} -> prod {+-1}) = 0, H^1(Q mod A_f) = (prod_p {+-1})/(+-1), and the image in H^1(Q, mu_2) is zero. The 2-torsion
of A_f^*/Q^* is the same group (x^2 = q in Q^* forces q = r^2, then x/r in prod {+-1}). All as written.
**Wrong (minor, cancelled text).** "Determinee a isom unique pres": the restricted equivalence is unique up to
isomorphism (zero image in H^1(Q, mu_2)), but its automorphisms are mu_2(Q) = {+-1}, which is not trivial; rigidity holds
for the enriched equivalences (H^0(Q mod A) = 0), of which there are continuum many classes.
**Placement.** Not a note on rational double points (sweep 2's SA15-13 joins it to the printed Lipman page 8:3): it
belongs with the motives over Z of 8:71-75 (SA15-6) and with the mu_2 questions of SA05-18 and SA06-10.

### C. Ordinary Barsotti-Tate groups over a smooth base; F-crystals with connection (8:25-27, 29, 31)

**What he does.** 8:25 "Groupes de Barsotti-Tate ordinaires": S_0 smooth over a perfect field k, S a formal lift smooth
over W, F_S a lift of the absolute Frobenius compatible with sigma; BTO(S_0) the ordinary BT groups; C = C_(S, F_S) the
category of (P', Q', M, nabla, F_M, Fil_0): P', Q' twisted constant p-adic sheaves, locally free of finite type; M an
extension of P' (x) O_S by Q' (x) O_S; nabla flat, compatible with the canonical connections; F_M: F_S^*(M) -> M a map of
extensions inducing the canonical isomorphism on Q' and p times it on P'; Fil_0 a splitting of M_0 compatible with F_M0.
A contravariant functor D: BTO(S_0)^o -> C. "Question: Est-ce une equivalence de categories ?" 8:26-27: choose a
splitting; another differs by u = (id L; 0 id), L in Gamma(T (x) O_S), T = P'^dual (x) Q'; F_M has matrix (id Phi; 0 p.id);
connection matrix (0 omega; 0 0); gauge formulas Phi' = Phi + (pL - F_S^*(L)), omega' = omega - dL; conditions d omega = 0,
F_S^*(omega) - p omega = d Phi, Phi_0 = 0. 8:29: general F-crystal with connection on E_S: d Phi = Phi A^sigma - A Phi,
dA + [A, A] = 0, Psi Phi = p^i (isogeny); horizontal maps u A = du + A' u; a stray computation (i+p)(p+1) - (i+p-1)p =
2p + i. 8:31: morphisms (du = uA - A'u, F_M' u^sigma = u F_M) and rank one: d phi = phi(omega^sigma - omega), d omega = 0,
phi psi = p^nu; two objects isomorphic iff some unit u has omega' - omega = -du/u and phi'/phi = u/u^sigma; the
classification as the cohomology of Gamma(O_S^*) -> Gamma(Omega^1) x Gamma(O_S)^! -> Gamma(Omega^2) x Gamma(Omega^1)[1/p],
u -> (du/u, u/u^sigma), (phi, omega) -> (d omega, d phi/phi - (omega^sigma - omega)).

**Checked (re-derived).**
- Gauge formulas (8:26-27): with the basis order (Q', P') (sub first) u = (1 L; 0 1), F = (1 Phi; 0 p), nabla = d + (0
  omega; 0 0); F_(M,phi') F_S^*(u) = u F_(M,phi) gives Phi' + F_S^* L = Phi + pL; conjugating the connection gives omega'
  = omega - dL. The three conditions: curvature d omega (the matrix is nilpotent, so the quadratic term vanishes);
  horizontality of F gives d Phi = F_S^* omega - p omega; compatibility with Fil_0 for a splitting reducing to Fil_0 gives
  Phi_0 = 0. All as on the page. The displayed matrices are those of his coordinate formulas u(x, y) = (x, y + Lx), F(x,
  y) = (px, y + Phi x) written in the order (y, x); the Pro note L.03 calls this a convention inconsistency: it is only
  the order of the coordinates, the mathematics is consistent.
- 8:29: horizontality of F: E -> E is d Phi = Phi A^sigma - A Phi (apply both connections to a column vector); curvature
  dA + A ^ A (his [A, A] must be read as A ^ A; with the graded commutator it would be 2 A ^ A); morphisms: u A = du + A'u.
  The arithmetic identity is right.
- 8:31, rank one: d phi = phi(omega^sigma - omega), omega' - omega = -du/u, phi'/phi = u/u^sigma are right. **Wrong:** the
  first map of his classification complex, u -> (du/u, u/u^sigma), has the wrong sign: composed with his second map it
  gives (0, 2 du/u - 2 du^sigma/u^sigma), not 0. With u -> (-du/u, u/u^sigma) (the gauge action he boxes) the composite is
  0: d(-du/u) = 0 and d(u/u^sigma)/(u/u^sigma) - ((-du/u)^sigma + du/u) = 0. The target is written (one-form, function)
  and the element (phi, omega); the order must be (omega, phi). (Same as the Pro note L.10, confirmed.)
- **New on Fil_0.** The datum Fil_0 is determined by (M, nabla, F_M) and always exists, S_0 being smooth over a perfect
  field: F_S^* of any 1-form is divisible by p (F_S^*(dg) = d(g^p + p h)), so d Phi = F_S^* omega - p omega gives d Phi_0
  = 0, hence Phi_0 is a p-th power on S_0 (Cartier: Ker d = O^p); the change of splitting with L_0 = Phi_0^(1/p) gives
  Phi'_0 = Phi_0 - L_0^p = 0 (exactly his margin "des L ... nuls sur S_0 et des Phi itou" once the right splitting is
  chosen). Uniqueness: a compatible splitting A must satisfy F^*(A) = Ker(F_M0), and F_(S_0)^* separates subbundles on a
  reduced S_0 (argument of 8:13); morphisms then respect Fil_0 automatically. So C is isomorphic to the category without
  Fil_0: ordinary Dieudonne crystals (with their slope filtration) on S with connection and Frobenius.
- Rank one with P' = Q' = Z_p: (Phi, omega) = (log(F_S^*(q)/q^p), dlog q) satisfies d omega = 0, F_S^* omega - p omega =
  d Phi and Phi_0 = 0 (F_S^*(q)/q^p is congruent to 1 mod p and log(1 + p y) is divisible by p, also for p = 2); the gauge
  L = log c sends q to q/c. This is the Kummer (Serre-Tate) parameter of the extension of Q_p/Z_p by mu_(p^infinity) (the
  Pro notes L.06-L.07 point to de Jong 1995, 4.3.2-4.3.5 and Katz 1981, 4.3.1; locators unverified here).

**Open on the page; known since.** "Est-ce une equivalence de categories ?": yes for S_0 smooth over a perfect field, by
the crystalline Dieudonne theory over such bases (de Jong 1995, Main Theorem 1, and the equivalence of unit-root
F-crystals with lisse Z_p-sheaves, Katz 1973; locators unverified), together with the remark above that Fil_0 is not
extra data: an ordinary BT group gives the extension of D(G^mult) (F = p x unit) by D(G^et) (F unit-root), and the slope
filtration is forced on morphisms (an F-equivariant map from the unit-root part to the p-part is divisible by every p^n).

### 8:30 (handwritten, not about crystals)
Families of charts (sigma, (U, V)) with sigma(V) = sigma(U) cap R^n and A = {(sigma_i, (U_i, V_i))} of class C^r: "Familles
connexes C^r, r >= 0", "regulieres (quasi-regulieres) C^r, r >= 1", "naturelles", "normales" (C^(r-1)), with the overlap
conditions V_1 cap V_2 != empty, U_1 cap V_2 = V_1 cap V_2, U_2 cap V_1 = V_1 cap V_2, and drawings. Definitions are not
given, so nothing can be checked. It sits among the leaves of the Bourbaki "Varietes" draft n. 382 and is probably a note
on manifolds with boundary or corners made while reading it; the hand is larger and rounder than on his crystal pages
and I do not attribute it here.

### D. The filtered Dieudonne module of the Lubin-Tate group (8:34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56)

**What he does.** K/Q_p finite, A its integers, residue field F_q (q = p^f), h = [K:Q_p] = ef, W = W(F_q), uniformizer pi.
Classify BT groups G_0 over k of height h with an A-action such that pi acts as F^f: by Dieudonne theory, free W-modules M
of rank h with sigma-linear F, A-action commuting with F, F^f = pi (*), and V with FV = VF = p (*'). Then (8:36) A (x)_Zp W =
A^Sigma (Sigma = Z/f), sigma_A a cyclic shift, M = (M_nu), F = maps phi_nu: M_nu -> M_(nu+1), all M_nu invertible,
normalized to phi_nu = pi^(r_nu) id (nu <= f-2), phi_(f-1) = pi^(r_(f-1)) u (8:38); (*') means r_nu <= e; dim G_0 =
r_0 + ... + r_(f-1) <= h; dim 1 iff exactly one r_nu = 1 and F^f is a uniformizer. 8:40 Proposition: dim G_0 = 1 iff
F^f = pi_G0 for a uniformizer pi (uniquely determined) iff M = Omega (x)_Zp W with F = id (x) sigma + pr_nu[(pi - 1) (x)
sigma]; homomorphisms: nonzero A-homomorphisms exist iff varpi = varpi'; then they form H = {v_0 : val(v_0) + sum_0^nu r_i
- sum_0^nu r'_i >= 0}. 8:42: for dimension one, Hom = Hom(Omega', Omega) if nu <= nu', pi Hom(Omega', Omega) if nu > nu';
up to isogeny (any height and dimension) M = Omega (x) K_0 with F^f = varpi, effective iff varpi and p^f varpi^(-1) each
preserve a lattice. 8:44: omega_G0 = t_G0^dual = M_nu/pi^F M_nu = Omega/p Omega; the standard case G_0(A, pi) (nu = 0,
Omega = A), M = A (x) W, F_M = id (x) sigma + pr_0((pi - 1) (x) sigma). 8:44-48: lift G_0 to G over A with A acting by the
evident action on t_G; "D'apres Lubin Tate un tel relevement existe et est unique"; assuming divided powers on pi A, the
deformation theory turns the lift into a lift of the filtration of M_A = Omega (x)_Zp A; A-compatibility forces t_G =
Omega^dual (x)_(A(x)A, rho_0) A = Omega^dual, omega_G = Omega: "on a retrouve le th. d'existence et d'unicite de Lubin-Tate
(sous une forme moins forte ... et sous l'hyp. complementaire que il existe puiss. div. sur pi A)". 8:48-50: without
that hypothesis, up to isogeny: t_G (x) K = Omega^dual (x)_A K, so t_G = pi^(-alpha) Omega^dual, "i.e. Omega = pi^alpha
omega_G", alpha depending only on A; "on peut se demander si ces sous-reseaux sont les memes" (D^*(G) and M in M_K).
8:52-56: Tate's theorem for G: K_pi the Lubin-Tate extension with a generator e of T_p(G); T_p (x)_Zp C = prod_sigma
C_sigma, g acting on C_sigma through sigma(chi_pi(g)); compared with Tate's decomposition T_p (x) C = g (x)_A C(1) + g^*v
(x)_A C, the identity factor is the tangent one; periods x_sigma with g(x_sigma) = sigma(chi_pi(g)) x_sigma (sigma != 1),
g(x_1) = tau(g)^(-1) chi_pi(g) x_1; "Il n'existe pas de x'_1 in C^* tel que g(x'_1) = chi_pi(g) x'_1 ... (ni pour J
contenu dans l'inertie)", because the product with the other periods would be an eigenvector for N(chi_pi(g)) = tau(g)
on inertia, "impossible".

**Checked (re-derived).**
- 8:36-38: A (x)_Zp W = A (x)_W (W (x)_Zp W) = A^f. Rank: each factor A has W-rank e, so rank_W M = e sum_nu rank_A M_nu =
  ef forces rank_A M_nu = 1 (his "la somme des rangs ... est h" is right only for W-ranks, as the Pro note L.13 says).
  V = p F^(-1) is integral iff every r_nu <= e. M/FM = sum A/pi^(r_nu) has W-length sum r_nu (each A/pi has length 1), and
  dim G_0 = length(M/FM) in the contravariant convention (check: M(mu_(p^inf)) = W with F = p). So dim 1 iff one r_nu =
  1, the others 0, and then F^f = pi^1 u is a uniformizer. As on the page.
- 8:40-42, homomorphisms: an A (x) W-linear h: M' -> M commuting with F satisfies h_(nu+1) phi'_nu = phi_nu h_nu, hence
  h_0 varpi' = varpi h_0; between invertible A-modules this forces varpi = varpi' or h = 0; then h_(nu+1) =
  pi^(sum_0^nu (r_i - r'_i)) h_0 must be integral, which is his inequality; for dimension one the partial sums are 0 or +1
  if nu <= nu' and reach -1 if nu > nu', giving Hom(Omega', Omega) resp. pi Hom(Omega', Omega). As on the page.
- **8:44, wrong for e > 1.** The ink reads "Omega/p Omega" (decided on the scan, 200 and 450 dpi). The cotangent space
  of a one-dimensional G_0 is M/FM = A/pi at the one index with r_nu = 1, of k-dimension 1: omega_G0 = Omega/pi Omega.
  Omega/p Omega has dimension e and is not killed by pi. Likewise "M (x)_W k = sum M_nu (x)_A k" has dimension f, while
  M (x)_W k = M/pM has dimension h; it should be sum M_nu/p M_nu (as 8:46 then correctly uses M_A (x)_A k). Both are right
  when e = 1.
- 8:46-48, the deformation step. Divided powers on pi A exist iff e <= p - 1: in K, gamma_k(pi) = pi^k/k! has pi-valuation
  k - e v_p(k!) = k - e(k - s_p(k))/(p - 1). They are nilpotent on each pi A/pi^n A iff e < p - 1; at e = p - 1 the
  valuation is s_p(k), equal to 1 for k = p^m, so the PD are not nilpotent (example: Z_2 with p = 2). The
  Grothendieck-Messing theorem he invokes needs nilpotent divided powers (Messing, LNM 264, V.1.6, as the Pro note L.21
  reports; locator unverified here). So his argument covers e < p - 1, not the full range e <= p - 1 his hypothesis
  states; the result itself holds for every e by Lubin-Tate. Granting the theorem, the A-compatibility step is right: the
  tangent quotient of Omega^dual (x)_Zp A on which A (x) A acts through rho_0 is Omega^dual (x)_(A (x) A, rho_0) A =
  Omega^dual, of rank 1, so t_G = Omega^dual and the filtration is unique (a surjection of invertible A-modules is an
  isomorphism).
- **8:50, sign.** The ink reads "t_G = pi^(-alpha) Omega-check i.e. Omega = pi^alpha omega_G" (a blot over the first
  exponent). Dual lattices invert the scaling: (pi^(-alpha) L)^dual = pi^alpha L^dual, so t_G = pi^(-alpha) Omega^dual gives
  omega_G = pi^alpha Omega, i.e. Omega = pi^(-alpha) omega_G. (Confirms the Pro note L.27.)
- 8:52-56, periods. T_p(G) is invertible over A and its generators form an A^*-torsor permuted simply transitively by
  Gal(K_pi/K) (Lubin-Tate); T_p (x)_Zp C = A (x)_Zp C = prod_sigma C_sigma; with K/Q_p Galois each factor is Galois-stable
  and g acts on it by x -> sigma(chi_pi(g)) g(x) (he writes the scalar part only; the Pro note L.30). The A-equivariance of
  Tate's decomposition puts the tangent line t_G (x)_A C(1) in the identity factor (t_G has the evident A-action), which
  gives exactly his two period equations. The impossibility: if g(x'_1) = chi_pi(g) x'_1 on an open subgroup J of inertia,
  then x = x'_1 prod_(sigma != 1) x_sigma satisfies g(x) = N_(K/Qp)(chi_pi(g)) x = chi_cyc(g) x on J (the norm of the
  Lubin-Tate character is the cyclotomic character on inertia, by local class field theory), which Tate's theorem forbids
  (C(chi)^J = 0 when chi(J) is infinite; Tate 1967, section 3, locator unverified). So the identity period has weight 1 and
  the others weight 0. "J contenu dans l'inertie" must mean an open subgroup (for J = {1} the claim is false; the Pro
  note L.37).

**Open on the page.** 8:50: whether D^*(G) and M are the same lattice of M_K without divided powers, i.e. whether alpha =
0 ("cela ne depend pas du choix de pi, mais seulement de A"). See hunch H2-3.

### 8:58-60 (squared-paper tables, no words)
A grid numbered 1-17 with a diagonal, rows labelled n = 3, ..., 8 (or 13) with short broken lines, and columns of
fractions compared with each other (3/4 > 11/15, 2/3 < 11/16, 14/16 = 7/8 < ..., several x/17). The Pro note L.38 keeps
them uninterpreted; so do I (hunch H2-4).

### E. Tannakian structures, motives over Z and their realizations (8:61, 63, 65, 67, 69, 71, 73, 75)

**What he does.** 8:61: the Galois group of a Q_p-linear (graded, semisimple) Tannakian category C with a fibre functor
Phi to filtered F-crystals up to isogeny over a complete DVR V of mixed characteristic (residue field k perfect,
fraction field L, K = Frac W(k)): a) Phi to F-crystals over k up to isogeny ("couples (E, F) ... tel qu'il existe un
reseau invariant par F"); b) a filtration of Phi (x)_K L; the "foncteur fondamental (convenable)" T_p: C -> Mod_f(pi, Q_p),
pi = Gal(Lbar/L), a fibre functor over Q_p, hence C = Rep_Qp(G) with G pro-reductive. 8:63: a homomorphism alpha: pi ->
G(Q_p); "Si le foncteur T_p (ou, ce qui revient au meme, le foncteur Delta) est pl. fidele (dans ce cas seulement) G est
l'enveloppe algebrique de alpha"; the composite C -> Mod_f(pi, C) is bigraded (total degree and Hodge-Tate), whence
i_1, i_2: G_m,C -> G_C with i_1 i_2 = i central; a Hodge fibre functor T_Hdg, a G_L-torsor P, j_1, j_2: G_m,L -> G_L^P =
ad(P). 8:65: T_p(M) (x) C = sum T_Hdg(M)^(i,j) (x) C(-i); a choice rho: C(1) = C gives a point rho~ of P(C), with
"(u rho)~ = i_1(u^(-1))", hence a map of C^*-spaces with pi-action C(1)^* -> P(C). 8:67-69: a crystalline fibre functor
T_cr over K, a G_K-torsor Q, the filtration of T_cr (x) L with gr = T_Hdg, a torsor R under the unipotent U' in Isom(Q_L,
P), the Frobenius structure F: T_DR^sigma = T_DR, i.e. Q^sigma = Q. 8:71: "Structures sur categorie (C) de motifs ... sur
un ouvert S de Spec(Z)": Betti T_B with group G over Q, T_l = T_B (x) Q_l, pi = Gal(Qbar/Q) -> G(Q_p) and the local groups
at p and infinity, Hodge cocharacters i_1, i_2 at infinity and at p, T_DR with a G-torsor P and G' = ad(P), the filtration
j_2 up to U', Frobenius elements F_p in G'(Q_p) and F_infinity in G'(R) of order 2, period points rho^(infinity) in P(C)
and rho^(p)(j_2, lambda) in P(C^p), with equivariance for C^(p)* x U'(C^p) and Gal(Qbar_p/Q_p). 8:73: the realizations as
data a)-f) (module with integrable connection and filtration on S; crystalline Frobenius F_p; real-analytic bundle with
F_infinity; Betti local system; p-adic local systems; comparison f_infinity: M_C^an = T (x) C; "f_p) - - - - -" left
blank) and a sketch comparing Betti, de Rham, crystalline and Hodge. 8:75: an agenda: "Conj. de Hodge (simple,
generalisee)", "Conj. de Tate (simple, generalisee)", "Conj. des Frobenius dans Coh. de De Rham (a connexion)" [margin:
Frobenius cristallin], "? Conj. du double reseau (revoir)", "'Tate group' (simple, generalise) sur schem. de t.f. sur Z /
sur corps", "'Tate group' sur anneau local d'inegale car.".

**Checked.**
- 8:63, the envelope. "T_p fully faithful implies G is the algebraic envelope of alpha" is false as stated: for G = SL_2
  in characteristic 0 and B a Borel, Rep(G) -> Rep(B) is fully faithful (the B-invariants of Sym^n are 0 for n > 0, so
  Hom_B = Hom_G) while B != G (the Pro note T.09, re-derived). The converse direction (envelope implies fully faithful)
  is right, and full faithfulness plus "every subobject of T_p(X) comes from C" gives the envelope (Deligne-Milne,
  Prop. 2.21(a), locator as cited by the Pro note, unverified here). New refinement: if the Zariski closure H of
  alpha(pi) is reductive (e.g. if every T_p(X) is semisimple), full faithfulness alone suffices: then V^H = V^G for every
  G-module V, so O(G/H) = O(G)^H = k, and G/H is affine (H reductive), hence H = G. In the local setting of 8:61-63 the
  T_p(X) need not be semisimple (crystalline representations of an ordinary elliptic curve over L), so his "(dans ce cas
  seulement)" needs the subobject condition there.
- 8:63: i_1(lambda) i_2(lambda) = i(lambda) with i central forces i_1 and i_2 to commute (i_2(mu) = i(mu) i_1(mu)^(-1)), so
  the pair is one cocharacter once the grading i is fixed (the Pro note T.11, re-derived).
- 8:61, the target category: F-isocrystals with an F-stable lattice are not closed under duals (F = p on a line has one,
  its dual F = 1/p has none), so a fibre functor from a rigid C must land in all F-isocrystals (or allow Tate twists); the
  lattice condition reads as effectivity of the objects in view, not as the target category (the Pro note T.04, checked).
- 8:69/8:71: F_p in G'(Q_p) is consistent: over the residue field F_p, sigma is the identity of W(F_p) = Z_p, so the
  crystalline Frobenius is Q_p-linear and Q^sigma = Q becomes an automorphism of Q (the Pro note T.21, checked).

**What it is.** A programme, not proofs: the motivic Galois group with its Betti, de Rham, l-adic, crystalline and
Hodge-Tate fibre functors, the comparison torsors and Frobenius elements, organized as torsors and cocharacters; the
p-adic comparison is the "mysterious functor" problem (left blank as f_p on 8:73). Later: Fontaine's period rings and
the crystalline comparison (Faltings, Tsuji), Deligne's motivic Galois groups for absolute Hodge cycles. The reading
"Tate grou" on 8:75 is probably "Tate group" (the final stroke of the word descends like his p); with "(simple,
generalise)" next to "Conj. de Tate (simple, generalisee)" this reads as the l-adic (Mumford-)Tate group question.

### F. The co-Lie complex of a group of multiplicative type and the lifting obstruction (8:78-81)

**What he does.** 8:78 heading "Complexe de co-Lie des groupes de t.m." (the Pro reading "cotie" is the ink "coLie":
"co" followed by an L joined to "ie"; his own term is Illusie's "complexe de co-Lie", and l^G is what the page computes;
Michel Hua's project reads "co-Lie" too). G = D(M), M a lattice over S ("= groupe ct tordu"); the canonical flat
resolution 0 -> R -> Z[M] -> M -> 0 (u([m]) = m), its dual 0 -> G -> T = G_m^M -> T' = D(R) -> 0 "resolvant G par des
tores (evt de dim. relative infinie...)"; "Le triangle de transitivite de Mazur-Roberts donne un isomorphisme" l^G =
[omega_T' -> omega_T] = [R (x) O_S -> Z[M] (x) O_S], boxed (1.3) l^G = M (x)^L_Z O_S; (1.4) for a Lambda-algebra O_S, l^G =
(M (x)^L_Z Lambda) (x)^L_Lambda O_S; 8:79 (1.4') for Lambda a field the second L is useless; 1.5-1.8: M coming by descent
from a representation of pi (discrete or profinite) on M_0 via f: (S) -> (B_pi), M = f^(-1) M_0, l^G = f^*(M_0 (x)^L
Lambda) (x)^L_Lambda O_S. 8:80 (2.1) omega_G = M (x) O_S, n_G = Tor_1(M, O_S); in characteristic p, M_p (x) O_S and _pM (x)
O_S; (2.2') if pM = 0 both are M (x)_Fp O_S; a canonical class xi in Ext^2_(O_S)(M (x) O_S, Tor_1(M, O_S)), coming from
xi_Lambda in Ext^2_Lambda(M (x) Lambda, Tor_1(M, Lambda)); for Lambda = Z/n and M locally free over Lambda, xi_Lambda in
H^2(S, End(M)), xi in H^2(S, End(E)), E = M (x)_Lambda O_S (a hypothesis "si O_S est plat sur Lambda (p.ex. n = p)" is
struck out). 8:81: under 1.5, xi_Lambda is the image of xi_0 in H^2(B_pi, End(M_0)); by functoriality the universal case
pi = Aut(M_0) = GL(d, Z/n); "D'apres Illusie, c'est l'obstruction a remonter la representation de pi dans M_0 en une
representation dans un module libre sur Z/p^2 Z" (the ink: "p^2" in black written over "n^2", the black of the insertion
below); "[Lorsque n = p (premier),] Elle est evidemment nulle si M_0 est de rang <= 1, mais sans doute pas nulle si M_0
de rang d >= 2, dans le cas universel pi = GL(d, F_p)"; if S' is the universal covering, H^2(B_pi, -) -> H^2(S, -) is
injective, "donc on trouvera un element non nul xi_Lambda".

**Checked (re-derived).**
- (1.3): for 0 -> G -> T -> T' -> 0 with T, T' smooth, the transitivity triangle gives l^G = [omega_T' -> omega_T] in
  degrees [-1, 0]; omega_(D(N)) = N (x) O_S (dlog of characters); so l^G = [R (x) O_S -> Z[M] (x) O_S], which computes M
  (x)^L O_S because 0 -> R -> Z[M] -> M -> 0 is a free resolution. Tests: mu_n = D(Z/n) gives [O_S -n-> O_S]; G_m gives
  O_S. The infinite rank of Z[M] can be avoided locally with 0 -> Z^a -> Z^b -> M -> 0 (the Pro note E.36). (1.4) is
  associativity of (x)^L. **Literature:** Bergh-Rydh state exactly this (arXiv:1905.00872v1, Appendix B, Prop. B.4, PDF
  pp. 33-34, opened: Le^*L_(G/S) of a group of multiplicative type is O_S (x)^L_Z of its character sheaf), and prove it
  with the same group-algebra resolution Z_S[A]; so sweep 2's "matching Bergh-Rydh" holds, with that locator. Illusie,
  CCD II, ch. VII, 3.1.1 (p. 212, opened) introduces the co-Lie complex, says it was first introduced by Mazur-Roberts
  (S affine, G finite), and states the transitivity triangle l_K -> l_H -> l_G for 1 -> G -> H -> K -> 1 as Prop.
  3.1.1.5, "On leur doit notamment l'enonce ci-apres": the page's "triangle de transitivite de Mazur-Roberts" (ink clear
  on the scan) is the right attribution. This resolves the Pro note E.38.
- (2.1), (2.1'), (2.2') follow from (1.3): H^0 = M (x) O_S, H^(-1) = Tor_1^Z(M, O_S); over F_p, M (x) O_S = (M/pM) (x)_Fp O_S
  and Tor_1^Z(M, O_S) = _pM (x)_Fp O_S (O_S flat over F_p). For mu_p: omega = n = O_S.
- 8:80, the struck-out hypothesis: when M is locally free over Lambda = Z/n and O_S is a Lambda-algebra, M (x)^L_Z Lambda
  has Lambda-flat cohomology (M and M), so (x)^L_Lambda O_S keeps the truncation triangle and xi is the image of xi_Lambda
  without O_S being flat over Lambda; his deletion is right.
- 8:81, "d'apres Illusie" (independent re-proof of the vanishing criterion). For Lambda = Z/n and M_0 a Lambda[pi]-module
  free over Lambda, K = M_0 (x)^L_Z Lambda has H^(-1) = M_0, H^0 = M_0 and k-invariant kappa in Ext^2_(Lambda[pi])(M_0, M_0)
  = H^2(pi, End(M_0)). By adjunction RHom_(Z[pi])(M_0, N) = RHom_(Lambda[pi])(K, N); the long exact sequence of the
  truncation triangle gives Ext^1_(Z[pi])(M_0, M_0) -> Hom(M_0, M_0) -> Ext^2_(Lambda[pi])(M_0, M_0), the second map
  sending id to kappa, and the first sending an extension 0 -> M_0 -> X -> M_0 -> 0 to the map induced by
  multiplication by n. id is in the image iff kappa = 0, and an X with that map equal to id is a Z/n^2[pi]-module, flat
  over Z/n^2 (Ker n = nX), with X/nX = M_0, i.e. a free lift. So kappa = 0 iff M_0 lifts to a free Z/n^2-module with
  pi-action; kappa is the obstruction (up to sign). This is the general statement (Z/n^2); the black correction to Z/p^2 is
  its case n = p, which his insertion "Lorsque n = p (premier)" then assumes.
- Rank <= 1, n = p: pi -> F_p^* lifts by the Teichmuller section F_p^* -> (Z/p^2)^*, so the class is 0, as he says. For n
  not prime this fails already in rank 1 ((Z/64)^* -> (Z/8)^* has no section: the elements of order 2 of (Z/64)^* map to
  1 and 7 only), which is why the insertion "Lorsque n = p" is needed.
- **"Sans doute pas nulle si M_0 de rang d >= 2, dans le cas universel pi = GL(d, F_p)": false in exactly three cases.**
  The universal class is the class of the extension 1 -> M_d(F_p) -> GL_d(Z/p^2) -> GL_d(F_p) -> 1 (a lift of the
  tautological representation is a section), so it is nonzero iff this extension does not split.
  (a) p >= 5, every d >= 2: non-split. Let u = 1 + E_12. For any lift u + pX, (u + pX)^p = u^p + p (Ad(u) - 1)^(p-1)(X) u^(-1)
  mod p^2 (in characteristic p, sum_(i<p) T^i = (T - 1)^(p-1)), and (Ad(u) - 1)^3 = 0 on gl_d (with N = E_12: (Ad u - 1)X =
  [N, X] - NXN, (Ad u - 1)^2 X = -2NXN); so for p - 1 >= 3, (u + pX)^p = u^p = 1 + pE_12 != 1, and no lift of u has order p.
  (b) (d, p) = (2, 2), (2, 3), (3, 2): split, so the universal class is 0. GL_2(F_2) = S_3 lifts to GL_2(Z) by the
  reflection representation; GL_2(F_3) lifts to GL_2(Z/9), e.g. by the subgroup generated by (1 1; 6 7) and (0 4; 7 0),
  of order 48 (computed; GL_2(F_3) also embeds in GL_2(Z_3) through the Hurwitz quaternion units and the involution
  (i + j)/sqrt(-2), sqrt(-2) in Z_3); GL_3(F_2) lifts to GL_3(Z/4): the Steinberg relations of SL_3(F_2) have a solution
  over Z/4 generating a subgroup of order 168 (computed).
  (c) (3, 3) and (4, 2): non-split. Lifting the Steinberg generators x_ij = 1 + E_ij by x_ij + pY_ij turns the Steinberg
  relations (x_ij^p = 1, [x_ij, x_jk] = x_ik, [x_ij, x_kl] = 1 for j != k, i != l) into an affine system over F_p in the Y_ij;
  it is inconsistent for (3, 3) (54 unknowns, rank 46) and (4, 2) (192 unknowns, rank 177), so no section exists over
  SL_d(F_p), hence none over GL_d(F_p). (Also inconsistent for (3, 5), (4, 3), (5, 2), as (a) and (d) predict.)
  (d) Block lemma: if GL_d(Z/p^2) -> GL_d(F_p) splits, so does GL_d'(Z/p^2) -> GL_d'(F_p) for d' <= d (restrict a section
  to the block diagonal diag(g, 1) and take the top-left block, a homomorphism modulo p^2 because the off-diagonal blocks
  are divisible by p). Hence non-split for p = 3, d >= 3 and p = 2, d >= 4.
  So: the universal class is nonzero for d >= 2 except (d, p) = (2, 2), (2, 3), (3, 2). Michel Hua's project notes the
  case (2, 2) ("l'extension est scindee et xi_0 = 0") and that other small split cases exist, without listing them. The
  computation is the script `split_check.py` (scratchpad of this run, not kept); it is short and can be redone.
- Injectivity of H^2(B_pi, -) -> H^2(S, -) for the universal covering (S connected, etale or fppf topology): in the
  Hochschild-Serre spectral sequence of the pro-Galois covering S' -> S, E_2^(0,1) = H^1(S', End(M_0)) = Hom(pi_1(S'),
  End(M_0)) = 0, so E_2^(2,0) = H^2(pi, End(M_0)) injects into H^2(S, End(M)). Right. "Donc on trouvera un element non
  nul" needs xi_0 != 0 for the given pi_1(S) -> GL(M_0): true when pi_1(S) = GL_d(F_p) acting tautologically with (d, p)
  outside the three exceptions (such S exist, e.g. quotients of simply connected varieties by a free action; Serre 1958,
  locator unverified).

**What is open.** Whether xi (the image in H^2(S, End(E)), coherent cohomology) is nonzero for some S; the page claims
nonvanishing only for xi_Lambda. See hunch H2-1.

## 2. Reused material (not studied)

One line each; typed page numbers in brackets. None of it bears on his crystal pages.
- 8:3: J. Lipman, "Rational singularities ...", section 24 "Explicit description of pseudo-rational double points"
  (draft p. 132; Publ. IHES 36, 1969, pp. 256-257 per the Pro note ER.02, locator unverified). Not his; sweep 2's
  SA15-13 rests on it.
- 8:7, 9, 11, 15: M. Artin's draft of SGA 4 XII (proper base change: Theorem (5.1)(i)-(iii), Lemmas (8.3), (8.4),
  reduction to f projective) [35, 37.1, 32, 33]; 8:9 and 8:11 are cancelled typed pages with a drawn box or arrow.
- 8:19: Bourbaki, "Tribu n. 66", "Decisions sur l'integration (Redactions n. 446 et 447)".
- 8:21, 23: a typescript in Bourbaki style on holomorphic functions (Schwarz's lemma, equicontinuous sets, variation of
  the argument) [65, 53]; source not identified.
- 8:32: his own SGA 7 IX draft [55 ter]: end of the proof of 5.13 c) and Remarque 5.13.1; the printed text is SGA 7 I,
  pp. 388-389 (opened in the corpus; the wording matches).
- 8:35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57: Bourbaki redaction n. 382, "Varietes differentielles et analytiques"
  draft (4.11-4.13 fibre products, group varieties, weakening of structure; 6.8-6.9 tensor bundles; section 7 jets and
  jet bundles) [84, 83, 82, 81, 79, 78, 77, 76, 73, 43, 42, 40]; the "Tribu" label of sweep 2 does not apply.
- 8:62, 64, 66, 68, 70, 74: M. Artin's draft of SGA 4 XVI section 3 (smooth base change, cohomological purity, the
  classes (3.9) and Theorem (3.10)) [35, 34, 33, 29, 28, 31]; 8:70 carries pencil remarks ("demonstration peu
  naturelle", "!"), hand not attributed.
- 8:72, 76: Bourbaki redaction n. 357 (convolution of measures and functions, L^p estimates with the modular function)
  [35, 33].

## 3. Hunches

- **H2-1 (8:80-81).** Grothendieck's class xi in H^2(S, End(E)) is the image of the lifting class xi_Lambda under
  H^2(S, End(M)) -> H^2(S, End(M) (x) O_S), whose kernel is the image of H^1(S, End(E)) under the Artin-Schreier boundary
  (0 -> End(M) -> End(E) -1-F-> End(E) -> 0). So xi = 0 can happen while xi_Lambda != 0. What may be true: for S proper
  over a perfect field with pi_1(S) = GL_d(F_p), (d, p) outside the three split cases, xi != 0, i.e. the co-Lie complex of
  D(M) is not formal (not n_G[1] + omega_G) although omega_G and n_G are isomorphic. Grounds: 8:80-81 compute exactly up
  to xi_Lambda; Bergh-Rydh, Prop. B.6 (Tor_0 and Tor_1 isomorphic as representations) concerns only the graded pieces.
  Links: SA15-8; SA18-7/SA18-8 (Frobenius kernels, Cartier duality); Illusie CCD II, VII (co-Lie complexes of truncated
  BT groups).
- **H2-2 (8:2-22).** For S smooth over a perfect field the relative groups Ext^i(S_zar mod S_cris; D~_0, D~_1) of 8:20
  vanish for i = 0, 1, 2 by Cartier descent, so the Zariski triangle (III) exists and is unique, giving his
  description of BT_1 groups over smooth bases; the nonzero kernel Ker(H^1(n_G*) -> H^1_cris(n_G*)) of 8:22 points to
  non-reduced bases. Links: Berthelot-Breen-Messing 1982; de Jong 1993; de Jong-Messing 1999 (faithfulness fails in
  general; true over l.c.i. bases), all locators unverified.
- **H2-3 (8:48-50, 8:75).** The integer alpha (t_G = pi^(-alpha) Omega^dual, depending only on A) measures the gap between
  the crystalline lattice and the Lubin-Tate tangent lattice; 8:48 gives alpha = 0 when e < p - 1. What may be true:
  alpha is governed by the different of A over W (as in Fontaine's 1982 bound for the Hodge-Tate map of p-divisible
  groups over O_K, locator unverified) and is nonzero for some e >= p - 1; this is the "double reseau" item of the 8:75
  agenda. Links: Breuil 2000, Kisin modules, Bhatt-Morrow-Scholze (the Pro notes L.25, T.29).
- **H2-4 (8:58-60).** The fractions x/17 and the comparisons 3/4 > 11/15, 2/3 < 11/16, 7/8 < ... may be slope bookkeeping
  (Newton polygons of the A-modules of 8:34-42, slopes r/h) or unrelated arithmetic; nothing on the sheets decides it.
- **H2-5 (8:25-31).** His (Phi, omega) are Katz's Serre-Tate parameter: Phi = log(F_S^* q/q^p), omega = dlog q, the
  gauge L = log c acting by q -> q/c; for ordinary abelian schemes this is the canonical-coordinates picture of
  Deligne-Illusie, "Cristaux ordinaires et coordonnees canoniques" (1981, locator unverified). Links: SA15-17 (6:33-37,
  the ordinary extension class), SA16-14 (connections on the elliptic moduli).
- **H2-6 (8:17, 8:71).** The indeterminacy (prod_p Z/2)/(+-1) of the enriched data of a motive over Z is the 2-torsion of
  the finite idele class group, i.e. the sign ambiguity of comparison isomorphisms of motives that have the
  automorphism -1. Links: SA05-18 (the mu_2 factor of the motivic group over finite fields), SA06-10 (real fibre
  functors and gerbes), SA07-2 (period torsor).
- **H2-7 (8:81).** The three split cases are those where the tautological representation comes from characteristic 0:
  S_3 (reflection representation), GL_2(F_3) (Hurwitz units over Z_3), GL_3(F_2) = PSL_2(7) (the 3-dimensional
  representation over Z_2, -7 a 2-adic square). I expect the classification found here to agree with Sah's work on
  cohomology of split extensions (J. Algebra, 1974/1977; locator unverified), and the p >= 5 case is the lemma behind
  Serre's result that a closed subgroup of SL_2(Z_p) onto SL_2(F_p) is everything (Abelian l-adic representations, IV,
  locator unverified).
- **H2-8 (8:63, 8:71).** In the global setting of 8:71 (motives over S in Spec Z) his "dans ce cas seulement" would hold
  if the l-adic realizations are semisimple (Tate's semisimplicity conjecture): the Zariski closure is then reductive
  and full faithfulness suffices (refinement in E). Links: SA05-8, SA06-15, SA07-1.
- **H2-9 (8:13).** On a non-reduced S the crystalline phi^* is injective on subbundles when S is locally a complete
  intersection (the map a -> a~^p into a PD envelope is then flat enough), and fails in general; this would match the
  l.c.i. hypothesis of de Jong-Messing (locator unverified).

## 4. Dependencies (item ids from sweep2 WHAT_IS_WHERE)

- A (8:2-22, SA15-2) uses SA15-1 (the topoi S_cris, S_zar and phi, epsilon with phi epsilon = F_S: 8:2, 8:4-5),
  SA15-14 (divided powers: "epaississement p. div.", 8:10), SA15-8 (the co-Lie complexes l^G, l^(G*): 8:2, 8:5, 8:22),
  SA15-16 (Dieudonne crystals, truncated BT groups: 8:13), SA18-7 and SA18-8 (Frobenius kernels, height one, the p-map
  Pi: g^(p) -> g: 8:2, 8:12, 8:18).
- B (8:17) is used by E (8:71, the data at A', infinity and p); related to SA05-18, SA06-10.
- C (8:25-31) uses SA15-2 (F-crystals with connection: 8:29), SA15-16 (the Dieudonne module of a BT group: 8:25), SA15-17
  (the ordinary extension class: 6:33-37).
- D (8:34-56) uses SA15-16 (Dieudonne theory over k and lifting through the Hodge filtration: 8:34, 8:46), SA15-14
  (divided powers on pi A: 8:46), SA15-18 (Tate's Hodge-Tate decomposition: 8:52-56); SA19-6 (formal groups) nearby.
- E (8:61-75, SA15-6) uses SA15-2 (F-crystals up to isogeny: 8:61), SA15-18 (Hodge-Tate: 8:63, 8:65), SA05-8 (motivic
  Galois group), SA05-20 (tannakian formalism), SA06-15 (fibre functors in characteristic p), SA07-1 (realizations at
  places), SA07-2 (period torsor: 8:65, 8:71), SA07-7 (real Frobenius: 8:71), SA06-4 (Tate conjecture: 8:75), and B.
- F (8:78-81, SA15-8) is used by A (co-Lie complexes in the crystalline programme: 8:2, 8:5); it uses Illusie's co-Lie
  complex (CCD II, VII 3.1) and nothing else of the topic.

## 5. Deliverable state

- **Passes.** Pro first pass by GPT-6 Astra (ChatGPT Pro mode): package 32 (started 12 Nov 20:50 UTC; cote 7 scans 61-72
  and cote 8 scans 1-18) and its continuation 32b (cote 8 scans 19-78; final checks 13 Nov 15:02 UTC: 86/86 pages, 604
  doubt rows, research notes); package 33 (cote 8 scans 79-81 with cotes 9, 4, 100), 13 Nov. Sample check: none for
  32/32b (no `returns/MPL_7_061-072+8_001-078_check`; packages 30, 31 and 33 have one; `COVERAGE_AUDIT_20261117.md` lists
  32b as not covered by its audit); package 33 sample check by Claude Fable 5.2 at effort max, 13 Nov: 8 pages including
  8:80 (two low items), 0.10 errors per 100 words over the package. Second witness: K8-01 for scans 79-81 by GPT-6.2 Astra
  at reasoning effort max (ChatGPT Work), 18 Nov 11:13-11:45 UTC (independent transcription, witness check against
  Michel Hua's batch: 6 places changed, 1 alternative added, 33 unchanged; math notes and 7 check events).
  `COVERAGE_20261118.md`: cote 8, 81 scans, 4 blank, 77 read, 3 with a second reading. Michel Hua's project has a
  modernised reading of the whole cote. Sweep 2 (Claude Opus 5.5 at effort max, a28ea31fa17dd65e1) placed the entries;
  this file is sweep 3.
- **Open readings.** 8:6 the relation sign "=|" (the mathematics uses "="); 8:30 the hand; 8:58-60 the tables; the
  doubt marks of his 47 handwritten pages (dense on 8:2-22 and 8:61-75: overwritten twists, subscripts cr/DR, primes, xi or zeta);
  decided here: 8:78 "co-Lie" and "Mazur-Roberts", 8:81 "p^2" over "n^2", 8:44 "Omega/p Omega" and 8:50 "Omega = pi^alpha
  omega_G" (both as written, both wrong), 8:75 "Tate group" (probable).
- **Ready for an edition?** Not yet. The transcription is complete (every page, doubts marked), but scans 1-78 have had
  one reading only (no sample check, no second witness apart from Michel Hua's project), and his pages are formula-dense
  with many doubtful symbols. Needed: a sample check of 32/32b, a second reading of the 47 handwritten pages, and the
  readings decided here entered. The 29 reused leaves need only their one-line identification in an edition.

## 6. Corrections

All in `c7_c8_part2_CORRECTIONS.tsv` (24 rows): eleven to sweep 2's placements and descriptions for cote 8 (SA15-1, -2,
-3, -4, -6, -7, -8 twice, -12, -13, and the duplicated cote-7 lists), four transcription readings, two Pro notes (E.38,
L.03), and seven mathematical corrections to his pages (8:17, 8:31, 8:44, 8:46-48, 8:50, 8:63, 8:81).

## Literature route

Queries (`query_corpus.py --layer research_literature --limit-per-layer 5`): "co-Lie complex group of multiplicative type
cotangent complex" (no hit); "Bergh Rydh functorial destackification weak factorization orbifolds" (no hit); "Illusie
complexe cotangent et deformations" (CCD I and CCD II); "Mazur Roberts local Euler characteristics" (no hit); "Messing
crystals associated to Barsotti-Tate groups" (no hit for LNM 264); "de Jong crystalline Dieudonne module theory formal
rigid geometry" (no hit); "SGA 7 Groupes de monodromie Modeles de Neron et monodromie" (SGA 7 I); "Lipman rational
singularities unique factorization" (no hit).

Opened:
- Illusie, Complexe cotangent et deformations II (LNM 283), ch. VII, 3.1.1 and Prop. 3.1.1.5, p. 211-212
  (`Papors/OS/Complexe Cotangent et Deformations II (Luc Illusie (auth.)).pdf`, text layer): definition of the co-Lie
  complex l_G = Le^* L_(G/S), amplitude [-1, 0], first introduced by Mazur-Roberts, transitivity triangle credited to them.
- Bergh-Rydh, "Functorial destackification and weak factorization of orbifolds", arXiv:1905.00872v1 (2 May 2019),
  Appendix B, Definition B.1, Remark B.2, Prop. B.3, Prop. B.4 (PDF pp. 31-34), Prop. B.6 (pp. 34-35); fetched from
  arxiv.org (not in the corpus).
- SGA 7 I, Expose IX, proof of 5.13 c) and Remarque 5.13.1, printed pp. 388-389
  (`Papors/OS/Groupes de monodromie en geometrie algebrique (Grothendieck, A. (Alexandre)).pdf`).
Cited and not opened (marked unverified in the text): Lipman 1969; Artin SGA 4 XII and XVI (Orgogozo re-edition);
Messing 1972; de Jong 1993, 1995; de Jong-Messing 1999; Berthelot-Breen-Messing 1982; Katz 1973, 1981; Deligne-Illusie
1981; Lubin-Tate 1965; Tate 1967; Deligne-Milne 1982; Fontaine 1982; Breuil 2000; Sah; Serre 1958 and Abelian l-adic
representations; SGA 3 VII_A.

## Appendix: the splitting computation (8:81)

Method, enough to redo it. For n >= 3 take the Steinberg generators x_ij = 1 + E_ij (i != j) of SL_n(F_p) and the
relations x_ij^p = 1, [x_ij, x_jk] x_ik^(-1) = 1 (i, j, k distinct), [x_ij, x_kl] = 1 (j != k, i != l). Put X_ij = x_ij +
p Y_ij over Z/p^2 with unknown Y_ij in M_n(F_p). For each relation word w, w(X) = w(x) + p L_w(Y) mod p^2 with L_w linear
(products of two p-terms vanish), and (w(x) - 1)/p mod p is E_ij for the power relations and 0 for the others; L_w is
computed column by column by setting one entry of one Y to 1. Solve L(Y) = -c over F_p by Gaussian elimination.
Results: (n, p) = (3, 2): consistent, the solution generates a subgroup of GL_3(Z/4) of order 168 (split); (3, 3): 54
unknowns, rank 46, inconsistent; (4, 2): 192 unknowns, rank 177, inconsistent; (3, 5), (4, 3), (5, 2): inconsistent. For
n = 2 a direct search over lifts of (1 1; 0 1) and (0 1; 1 0): 8 pairs generate a subgroup of order 6 in GL_2(Z/4), 27
pairs a subgroup of order 48 in GL_2(Z/9) (e.g. (1 1; 6 7), (0 4; 7 0)); no lift of (1 1; 0 1) to GL_2(Z/25) has order 5
(625 lifts checked). Pure Python, a few minutes.
