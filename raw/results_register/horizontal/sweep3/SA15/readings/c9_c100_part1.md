# SA15, cote 9 (part 1 of c9_c100): the reduced Dieudonné module and its duality, the inertia character of a Barsotti-Tate group, canonical stratifications and the Hasse invariant, and a canonical isomorphism det T_p(A)_ét = det T_p(A*)_ét

Claude Opus 5.5 at effort max (the SA15 c9_c100 reader, sweep 3), 19 Nov 2026 (UTC). Launched by agent
a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max) at the main session's word. Brief: `sweep3/READER_BRIEF.md`.
Companion files: `c9_c100_part1_CHECK_EVENTS.tsv`, `c9_c100_part1_CORRECTIONS.tsv`. Part 2 (cote 100, scans 3-45) is
`c9_c100_part2.*`, by the sub-reader SA15-c9_c100-part2 (agent a8d91f19c2d8f19c1, Claude Opus 5.5 at effort max); the
merge is `c9_c100.*`.

**Read:** all 29 scans of cote 9 (package `MPL_8_079-081+9+4+100`), in page order, from the Pro transcription (reader
tool, then again with the struck text kept, and the raw `.tex` where the tool hides figure nodes: the insertion "à corps
résiduel parfait" on 11 and the margin "à préciser" on 18 sit in such nodes); the Pro notes #10-#97; the Codex web
witnesses K9-01 (scans 2-15) and K9-02 (16-29), notes and math notes in full; Michel Hua's project (`9.modern.tex`, its
list of departures and the passages used below, credited where used; his page p is our scan p + 1). Ink checked on the
images: 3 (corollary and margin), 5, 7 (exponent, at 600 dpi), 8, 14, 16, 18, 24, 25, 29.

## 0. What the cote is

- **9:1** the archive's folder cover (IMAG logo). **9:2** his title sheet: "Dualité des modules de Dieudonné de groupes de
  B.T. duaux l'un de l'autre", "Le module de Dieudonné réduit M ⊗_W k".
- **9:3-8** handwritten, on stationery of the Istituto Matematico "Leonida Tonelli", Università di Pisa (printed face on 4
  and 6; the heading shows through, mirrored, on 3, 5, 7). 9:6 is the stationery used as scrap: an Italian vocabulary
  list (buon giorno, buona sera, buona notte, per favore, "mangare", "collazione") and a street plan with "Corso Italia".
  Grothendieck was in Pisa in May 1966 (his letter to Tate "Pise, Mai 1966", 6:2-32, `readings/c5_c6.md`), so 9:2-8
  are most likely of spring 1966 (hunch H1-8).
- **9:9** a whole struck sheet (written upside down): a lemma for constructing the Gauss-Manin connection.
- **9:10** a cover, "Caractères des groupes de B.T. à réduction semi-stable virtuelle essentielle"; **9:11-14** a blue
  typescript with his ink and pencil corrections, "Caractère d'un groupe de B.T. sur un corps local". The typescript
  says Tate's theorem is "démontré pour l'instant seulement dans le cas d'inégales caractéristiques", so it is later
  than Tate's Driebergen lecture (1966).
- **9:15** a cover, "Déformations des groupes de B.T. ordinaires" struck, then "Détermination des 'stratifications
  canoniques' sur les déformations", and the boxed "L'isom. de nature globale: dét T_p(A)_ét ≅ dét T_p(A*)_ét".
  **9:16-29** handwritten, his page numbers absent (the corner numbers are the archive's, scan - 1); 9:26 is a struck
  page.

Items (ids from `sweep2/SA15/WHAT_IS_WHERE.md`): SA15-10 (9:2-8), SA15-15 (9:9, struck), SA15-19 (9:10-14),
SA15-11 (9:15-29), SA15-12 (9:1, 4, 6 as documents). SA15-17 does not occur on cote 9; 9:13-14 lead into it (section 3).

## 1. SA15-10: the reduced Dieudonné module and duality over the truncated rings A_n (9:2-8)

### 9:3: the two Hodge-type sequences and the corollary

**What he writes.** k a field of characteristic p, G p-divisible, G* its dual, g = dim G, g* = dim G*; G̃ the universal
extension ("grp enveloppant") 0 → V(t_{G*}) → G̃ → G → 0. Two pairs of rows: H(G) in 0 → ω_G = t_G^∨ → H(G) → t_{G*}
→ 0 (dimensions g, g + g*, g*) with F_0 = H(F): H(G)^(p) → H(G) and V_0 = H(V): H(G) → H(G)^(p); and the "dual" rows
0 → ω_{G*} → t_{G̃} → t_G → 0 with V_0, F_0. NB: H(G) = t_{G̃*} (the Lie algebra of the universal extension of G*).
1) the two sequences, for t_{G̃} and t_{G̃*}, are transposed by a canonical functorial pairing which exchanges F_0 and V_0.
2) Ker F_0 = Im V_0 = ω_G^(p); Ker V_0 = Im F_0 = "ce que ça peut (innovation intéressante)". 3) F_0, V_0 on H(G) are
the reduced Dieudonné module mod p. 4) the composite t_{G*}^(p) → H(G) → t_{G*} is "la puissance p-ième des
dérivations [et correspond: Frobenius dans H²(G, G_a)]". **Corollaire:** G purely infinitesimal ⟺ F_0 nilpotent
("i.e. G* sans tore"); G* purely infinitesimal ⟺ V_0 nilpotent ("i.e. G sans composante toroïdale"); both ⟺ both.

**Checked** (check events 9:3-a, 9:3-b). With the convention V(E) = Spec Sym E (EGA II 1.7.8), Lie V(t_{G*}) =
t_{G*}^∨ = ω_{G*}, which is the left term of his right-hand rows, so the two diagrams agree. Ker F_0 ⊇ ω_G^(p) because
Frobenius kills differentials (F*(df) = d(f^p) = 0), with equality by rank, and Im V_0 = Ker F_0 is the
standard F-V exactness of H¹_dR-type modules (Oda, Ann. Sci. ENS 2 (1969), locator unverified). Item 4 is right: F_0
factors through H(G)^(p)/ω^(p) = t_{G*}^(p), and the induced map to t_{G*} = Lie G* is the linearized p-power of the
p-Lie algebra; "H²(G, G_a)" (the ink is a 2) is the Hochschild group whose symmetric classes are Ext¹(G, G_a) = t_{G*}.
The corollary, tested on the two basic cases: for G = μ_{p^∞} (g = 1, g* = 0), H = ω_G and F_0 = 0; for G = Q_p/Z_p
(g = 0, g* = 1), H = t_{G*} and F_0 is bijective. In general F_0 is nilpotent iff G has no étale part, i.e. G connected,
i.e. G* has no multiplicative ("toric") part; V_0 nilpotent iff G* connected iff G has no multiplicative part. **The ink
reads "i.e. G* sans tore"** (500 dpi; K9-01 and Michel Hua's project read the star too); the Pro transcription drops the
star, which makes the line false (correction 1). The margin reads "des dérivations", not "dans l'algèbre" (correction 2).

**Status.** Known: the contravariant Dieudonné module mod p as Lie of the universal extension of the dual (Messing, LNM
264, 1972; Mazur-Messing, LNM 370, 1974; locators unverified). "Innovation intéressante": Im F_0 = Ker V_0 is the
conjugate filtration, a second flag next to the Hodge flag; the pair is what later became an F-zip (hunch H1-5).

### 9:5: the trace form on A_n

**What he writes.** ⟨x, y⟩ = φ_n(xy) with φ_n: A_n → W_n; a) φ_n is W-linear on the left and on the right; boxed:
φ_n(1) = 1, φ_n(F^i) = φ_n(V^i) = 0 (i ≥ 1), "∃!"; b) φ_n(Fz) = φ_n(zF)^π; c) φ_n(zV) = φ_n(Vz)^π (a struck "π·" before
each right side); d) the φ_n glue. The working writes z = a + Σ λ_i F^i + Σ V^i μ_i and φ_n(z) = a, with "OK" for
φ_n(λz) = λφ_n(z) and φ_n(zλ) = φ_n(z)λ.

**Checked** (9:5, independent re-proof). Here A = W[F, V] with Fλ = λ^σ F, λV = Vλ^σ, FV = VF = p, and his π is σ.
Every element has the normal form a + Σ_{i≥1} λ_i F^i + Σ_{j≥1} V^j μ_j, so "constant term" is a well-defined map;
it is left W-linear (λz has constant term λa) and right W-linear (F^iλ = λ^{σ^i}F^i keeps the F-part an F-part), and
any left-linear φ with the boxed values equals it, since 1, F^i, V^j generate A as a left W-module: existence and
uniqueness ("∃!"; the ink admits ∃! or ∃1, the mathematics is ∃!). b): Fz has constant term pμ_1 (from FVμ_1), zF has
constant term pμ_1^{σ^{-1}} (V μ_1 F = VF μ_1^{σ^{-1}}), so φ(Fz) = φ(zF)^σ. c): zV and Vz have constant terms pλ_1
and pλ_1^{σ^{-1}}, so φ(zV) = φ(Vz)^σ. All correct.

### 9:7-8: two dualizing functors, and the bimodule A_n ≅ its W-dual

**What he writes.** A_n = A/(F^{n+1}, V^{n+1}) (exponent n + 1, checked at 600 dpi), I_n = A_n as an A-bimodule,
I = lim I_n along I_n → I_{n+1} (labelled p); D: M ↦ Hom(M, I) "foncteur dualisant", with the warning that it turns
left modules into right modules, repaired by the involution s of A exchanging F and V. "A_n est fini sur W_n." A second
dualizing functor for M killed by F^n, V^n: D'(M) = Hom_{W_n}(M, W_n) with the right A-structure "transposée", and
Hom_{W_n}(M, W_n) = Hom_{A_n}(M, Hom_{W_n}(A_n, W_n)). "Je dis qu'on a un iso I_n = A_n ≅ Hom_{W_n}(A_n, W_n)." On 9:8:
the right structure u.F = π^{-1}(u∘F), u.V = π(u∘F) [sic], u.λ = u∘λ, with u.F.V = u.V.F = pu; on D'(A_n) =
Hom_{W_n}((A_n)_g, W_n) the bimodule structure u.F = π^{-1}(u∘F_g), u.V = π(u∘V_g), u.λ = u∘λ_g, Fu = u∘F_d,
Vu = u∘F_g [sic], λu = u∘λ_d; "Attention les deux structures de W_n-module ... ne sont pas les mêmes"; A_n →? Hom
"iso. de bimodules" with a question mark; then the conditions on a bi-additive pairing A_n × A_n → W_n that make it
right A_n-linear (⟨x, yλ⟩ = ⟨λx, y⟩, ⟨x, yF⟩ = π^{-1}⟨Fx, y⟩, ⟨x, yV⟩ = π⟨Vx, y⟩) and left A_n-linear (⟨x, ay⟩ =
⟨xa, y⟩ for a = λ, F, V), with ⟨x, y⟩ = ⟨1, xy⟩ = ⟨xy, 1⟩.

**Checked** (9:7-a computation; 9:7-8 independent re-proof; 9:8 targeted check).
- The right action u.F = σ^{-1}∘u∘F, u.V = σ∘u∘V, u.λ = u∘λ is well defined on left-W-linear u (u(Fλx) = λ^σ u(Fx),
  so σ^{-1} restores linearity) and satisfies the relations of A (u.(Fλ) = u.(λ^σF): both are x ↦ λσ^{-1}u(Fx));
  u.F.V = pu as he computes. That computation needs u.V = π(u∘V), so "u.V = π(u∘F)" on 9:8 (the ink has F) is a slip,
  and so is "Vu = u∘F_g" (the left action is precomposition with right multiplication: Vu = u∘V_d). Corrections 3, 4.
  Read through s, D'(M) is the usual Dieudonné dual (F u = σ∘u∘V, V u = σ^{-1}∘u∘F).
- The pairing ⟨x, y⟩ = φ(xy) satisfies all six conditions: the right ones by b), c) and the right linearity of φ, the
  left ones by associativity. So y ↦ ⟨-, y⟩ is a bimodule map A_n → Hom((A_n)_g, W). It is injective: ⟨F^iλ, -⟩ is
  non-zero only on V^iW, where ⟨F^iλ, V^iμ⟩ = p^iλ^{σ^i}μ, and similarly for V^j; the pairing between the summands
  F^iW and V^iW is perfect. Bijective by length.
- **But the index is off by one.** In A/(F^{n+1}, V^{n+1}) the two-sided ideal has constant terms in p^{n+1}W only
  (V^jF^{n+1} = p^jF^{n+1-j}), so A_n = W_{n+1} ⊕ ⊕_{i=1}^n W_{n+1-i}F^i ⊕ ⊕_{j=1}^n V^jW_{n+1-j}, of length
  (n+1)², and p^n·1 ≠ 0 in A_n. A module with an element of exponent p^{n+1} is not isomorphic to a W_n-module, so
  "A_n ≅ Hom_{W_n}(A_n, W_n)" is false as written; φ_n takes values in W_{n+1}, and the true statement is A_n ≅
  Hom_{W_{n+1}}(A_n, W_{n+1}), equivalently A/(F^n, V^n) ≅ Hom_{W_n}(A/(F^n, V^n), W_n), which is the form his D'
  needs ("si M tué par F^n, V^n"). Michel Hua's project makes the same remark ("the trace form takes values in W_{n+1},
  not W_n as written"). The transition I_n → I_{n+1} by p is well defined (pF^n = VF^{n+1}, pV^n = FV^{n+1}) and
  compatible with φ (φ_{n+1}(px) = pφ_n(x) under W_{n+1} → W_{n+2}, x ↦ px), which is his d). Correction 5.
- With the corrected index the adjunction on 9:7 gives D(M) = Hom_A(M, I) = Hom_A(M, I_{n-1}) = D'(M) for M killed by
  F^n, V^n: the two dualizing functors agree, which is what the sheet is after.

**Status.** Known in substance: duality of finite Dieudonné modules corresponding to Cartier duality (Fontaine,
"Groupes p-divisibles sur les corps locaux", Astérisque 47-48, 1977; Demazure, LNM 302, 1972; locators unverified).
The self-duality of the truncated Dieudonné ring as a bimodule is the clean way to see it (hunch H1-6).

## 2. SA15-15: the struck lemma for the Gauss-Manin connection (9:9)

**What he writes** (the whole sheet struck; Michel Hua's project gives it too). "Question: Comment définir directement une
connexion intégrable sur R*f_*(Ω•_{X/S}) ??" Lemma: X a topos, K•, L• complexes, 𝒢 an abelian sheaf with i: 𝒢 →
Hom(K•, L•)^{-1}, P a 𝒢-torsor, Θ: P → Z(Hom(K•, L•)^0) with Θ(g.p) = Θ(p) + (d∘i(g) + i(g)∘d). Then there is a
morphism φ = φ(K, L, 𝒢, P, i, Θ): K• → L• in D(X) with 1°) functoriality in L•, 2°) invariance under (u, v): (𝒢, P) →
(𝒢', P') with i = i'∘u, "Θ = vΘ'", 3°) "Si P admet une section, alors" (unfinished).

**Checked** (9:9, independent re-proof). The lemma is true. The data (P, Θ) are exactly a global section of the
two-term complex C = [𝒢 → Z⁰Hom(K, L)] (degrees -1, 0; differential δ∘i): a 𝒢-torsor with an equivariant map to Z⁰.
The map of complexes C → Hom•(K, L) (i in degree -1, inclusion in degree 0) commutes with the differentials, so
H⁰(X, C) → H⁰(X, Hom•(K, L)) → H⁰(X, RHom(K, L)) = Hom_{D(X)}(K, L) gives φ. 1°) and 2°) are the functoriality of
this construction (2° needs Θ = Θ'∘v, not "vΘ'": correction 6, on a struck page). 3°) if p is a global section, φ is
the class of the map of complexes Θ(p). This is the Cartan-homotopy route to Gauss-Manin: local liftings form a torsor
under derivations, a lifting gives a map of de Rham complexes, and changing it by a derivation D changes the map by
d∘i_D + i_D∘d. Known since Katz-Oda (J. Math. Kyoto Univ. 8, 1968) and Grothendieck's "Crystals and the de Rham
cohomology of schemes" (1968) (locators unverified). Links: cote 7's lectures on Gauss-Manin (SA15-15, `c7_c8.md`).

## 3. SA15-19: the character of a Barsotti-Tate group on inertia (9:10-14)

### 9:11-12: the construction

**What he writes.** V a complete DVR "à corps résiduel parfait" (inserted), residue characteristic p, K of characteristic
0 or p; M = (M(ν))_{ν≥0} a p-BT group over K (his M(ν) is the kernel of p^{ν+1}, so M(0) = _pM, as the text itself
writes and as Michel Hua's project notes). M satisfies the "condition de monodromie" if it has a composition series by
BT groups whose graded pieces N acquire good reduction over a finite separable K'; by Tate's theorem ("démontré pour
l'instant seulement dans le cas d'inégales caractéristiques") N_{K'} comes from a BT group N over S' unique up to unique
isomorphism, so G = Gal(K'/K) acts on N over its action on S'. Then (1) K_BT(K; K') → K_BT(S'; G), (2) → K_BT(s'; G),
(3) → K(W(k'), G) by the Dieudonné module (margin "et = vers Cris(k')"), (4) the composite; restricting to the inertia
I ⊂ G, K(W(k'), G) → K(W(k'), I)^G ≅ R_{W(k')}(I)^{G/I}, and (5) the trace to central functions on I: "le caractère
du groupe de B.T. M", independent of K' and viewed as a function on the inertia subgroup of Gal(K̄/K).

**Checked / remarks.** The construction is right granted two points he passes over (Pro notes #28, #30): (1) needs the
class of Σ[N_i] to be independent of the composition series, which follows from Tate's full faithfulness once one knows
that sub-BT groups of a BT group with good reduction over S' have good reduction (true in mixed characteristic, e.g. via
schematic closure and Raynaud for e < p-1 and Breuil-Kisin in general; not available in 1967); and "≅
R_{W(k')}(I)" should be a homomorphism, which is all the trace needs (Michel Hua's project weakens it the same way).
Why the character can be computed "via les T_ℓ" (9:13): on the special fibre, I acts by k'-automorphisms of N_{s'}, and
for an abelian variety the trace of an automorphism on the Dieudonné module equals its trace on T_ℓ (the characteristic
polynomial of an endomorphism is the same on both). Check event 9:11-12.

### 9:12-13: the comparison with the Brauer character of _pM, and its failure

**What he writes.** If M_{K'} is constant, T_p(M) is a locally constant p-adic sheaf and the character of M agrees, on the
elements of I of order prime to p, with the modular character of I on M(0). Is the character always determined by M(0)
= _pM? "Il n'en est rien": by Brauer's theory of virtual liftings it would then equal the modular character of M(0) for
every M; for M with good reduction the character is constant on I, so the modular character of M(0) would be trivial;
"or c'est déjà faux en prenant M = Z_p(1), donc M(0) = μ_p, en se plaçant dans le cas où K ne contient pas les racines
p-èmes de 1". If K contains them, no trouble for good reduction of constant or multiplicative type; the ind-unipotent
case remains. Margin NB: then the character would be Z_p-valued once μ_p ⊂ K (on a subgroup of I of index dividing p-1).

**Checked** (9:12-13 targeted checks).
- Constant case: the model N over S' is étale, D(N_{s'}) = T_p(M) ⊗ W(k') with I acting through T_p(M); the ordinary
  character of a lattice on p-regular elements is the Brauer character of its reduction. Correct.
- The Brauer argument: the decomposition map from Z_p-representations to F_p-representations of a finite group is
  surjective on Grothendieck groups (Serre, "Représentations linéaires des groupes finis", Part III, Thm. 33; locator
  unverified), every lattice representation of G occurs as T_p of an étale BT group over K constant over K', and both
  sides are additive (M ↦ M(0) is exact on BT groups). So "determined by M(0)" forces "equal to the Brauer character of
  M(0)", as he says.
- The counterexample needs more than "K ne contient pas les racines p-èmes de 1": the character of μ_{p^∞} on I is
  trivial, and the Brauer character of μ_p on I is that of ω|_I, so the contradiction needs **the inertia** to act
  non-trivially on μ_p, i.e. K(μ_p)/K ramified. If K = Q_p(π) with π^{p-1} = -pu, u a unit that is not a (p-1)-th power
  mod p, then μ_p ⊄ K but K(μ_p) = K(u^{1/(p-1)}) is unramified over K, and μ_p gives no contradiction. The hypothesis to
  write is "e(K/Q_p) not divisible by p-1" or simply "I acts non-trivially on μ_p" (e.g. K unramified over Q_p, p > 2).
  Michel Hua's project makes the same point. Correction 7.
- With μ_p ⊂ K: for multiplicative good reduction M(0) = X/p ⊗ μ_p = X/p as a Galois module and both characters are those
  of X; by additivity over the connected-étale sequence over S' (G-stable), the ordinary case follows too. The margin is
  right: the eigenvalue multiset of an F_p-representation is stable under x ↦ x^p, so its Brauer character is fixed by
  σ and lies in Z_p; without μ_p ⊂ K one restricts to the kernel of I → Aut(μ_p) = F_p^*, of index dividing p-1.

### 9:13-14: the "cas test", and the pencil "faux par Tate"

**What he writes.** Two elliptic curves over K with potentially good reduction, _pE_1 ≅ _pE_2, μ_p ⊂ K: are their trace
functions on inertia (computable "via les T_ℓ") equal, "sur les éléments premiers à p" (inserted)? "Le cas intéressant est
celui où l'une au moins des deux courbes, après extension K → K', se réduit en une courbe à invariant de Hasse nul." Or
again: if _pA_K is constant, is the trace "égale à n = dim A_K" (typed over a struck "nulle") on the elements of I prime
to p? "Seul le cas de réduction non semi-stable de A offre un problème; donc il faudrait ici trouver un exemple où le
critère de réduction semi-stable de Raynaud est en défaut pour ℓ = p !" For an elliptic curve with residue characteristic
≠ 2, 3, K' the smallest extension with semi-stable reduction, G ⊂ Aut(A_{s'}), "lequel est cyclique à 2, 4 ou 6
éléments donc est premier à p", and the question is whether φ_E is constant equal to 2 when _pA is constant;
"il suffit de regarder le cas où la courbe elliptique réduite ... est d'invariant de Hasse nul". In the left margin, in
pencil, beside this paragraph: **"faux par Tate"**.

**Slips.** The trace of the identity on T_p(A) is 2 dim A, so "n = dim A_K" should be 2n, as his own elliptic case
("égale à 2") shows (correction 8; Michel Hua's project reads 2g). "G est un sous-groupe de Aut(A_{s'})" holds for the
inertia subgroup (all of G if k is algebraically closed); its order divides 2, 4 or 6, and 3 occurs (correction 9).

**The answer, worked out (check events 9:14-a, 9:14-b).**
1. **Ordinary reduction gives no counterexample (proved).** Let A/K have potentially good reduction with ordinary
   reduction over K', residue characteristic p ≥ 3, and A[p] unramified (in particular if _pA_K is constant; then μ_p ⊂
   K by the Weil pairing). Work over the completion of K^ur; let L/K^ur be the minimal extension with good reduction,
   Φ = Gal(L/K^ur), which acts on the Néron model 𝒜 over O_L and faithfully on Ā by k̄-automorphisms (Serre-Tate,
   Ann. of Math. 88 (1968), §2; locator unverified). 𝒜[p]^0 has special fibre μ_p^g, so it is of multiplicative type
   (SGA 3 X, rigidity; locator unverified), ≅ μ_p^g over O_L. A semilinear automorphism of μ_p^g over φ ∈ Φ is the
   canonical one composed with some a ∈ GL_g(F_p); on generic points it acts by ζ ↦ ζ^a since μ_p ⊂ K, so the
   hypothesis forces a = 1, and the reduction of the canonical one is the identity because φ acts trivially on k̄. So Φ
   acts trivially on Ā[p]^0; on Ā[p]^ét it acts as on the generic points (étale specialization), trivially. Over k̄,
   Ā[p] = Ā[p]^0 × Ā[p]^ét, so each α ∈ Φ acts trivially on Ā[p], hence α = 1 + pβ in End(Ā), and an automorphism of
   finite order congruent to 1 mod n ≥ 3 is 1 (Serre's lemma; Mumford, Abelian Varieties, §21, Thm. 5; locator
   unverified). So Φ = 1: A has good reduction over K and the trace is 2g. For elliptic curves the last step can be
   replaced by the action on Lie(Ā) = Lie(Ā[p]^0): a non-trivial α ∈ Aut(Ē) acts on the invariant differential by a
   non-trivial root of unity (p ≥ 5). This is his own reduction ("il suffit de regarder ... invariant de Hasse nul"):
   the ordinary case is covered by additivity from the constant and multiplicative cases.
2. **Supersingular reduction does give counterexamples (construction).** Take p ≥ 3 and K = Q_p(ζ_{p²}), so e = e(K/Q_p)
   = p(p-1) and μ_p ⊂ K; χ the ramified quadratic character of K(√π)/K, whose restriction to I is θ^{(p-1)/2} (θ the
   tame character of level 1). Let m = (p-1)/2, c = pm (so e = 2c), and let 𝔐 be the free k[[u]]-module with basis
   f_1, f_2 and φ(f_1) = u^c f_1, φ(f_2) = (1 - u^{c-m}) f_1 + u^c f_2. Then:
   - the matrix of 1⊗φ has elementary divisors 1 and u^{2c} = u^e, so 𝔐 is a Kisin module of E-height ≤ 1, hence a
     finite flat group scheme 𝒢 over O_K killed by p (Kisin's classification, p > 2; locator unverified);
   - 𝔐[1/u] has basis e_1 = f_1, e_2 = f_2 - u^{-m}f_1 with φ(e_i) = u^c e_i, so the generic fibre restricted to
     G_{K_∞} is ψ ⊕ ψ with ψ given by u^c; solving x^{p-1} = u^{-c} gives x = u^{-p/2}, so ψ = χ on inertia; by full
     faithfulness of restriction to G_{K_∞} on flat representations (Breuil, Kisin; locator unverified) the generic
     fibre of 𝒢 is χη ⊕ χη with η unramified;
   - mod u, φ is f_1 ↦ 0, f_2 ↦ f_1 and V = E(u)(1⊗φ)^{-1} is f_1 ↦ 0, f_2 ↦ -f_1 (this uses e = 2c exactly), so Ker F
     = Im V and Ker V = Im F are lines: the special fibre is the BT_1 of a supersingular elliptic curve.
   Lift 𝒢 to a BT group over O_K (truncation BT_{n+1} → BT_n is smooth and surjective: Illusie, Astérisque 127 (1985),
   Thm. 4.4; locator unverified); by Serre-Tate and algebraization it is E_0[p^∞] for an elliptic curve E_0/O_K with
   supersingular reduction. Put E = E_0 ⊗ χ (quadratic twist): E[p] ≅ η ⊕ η is unramified (det = η² = 1, consistent
   with the Weil pairing), so _pE is constant over a finite unramified extension of K, which still contains μ_p; but E
   has additive, potentially good reduction, inertia acts on T_ℓ(E) through χ by ±1, and φ_E takes the value -2 on
   elements of order prime to p. So the expectation fails, in the supersingular case he singled out, and so does
   Raynaud's criterion with ℓ = p; the same E refutes "character = Brauer character of M(0) when μ_p ⊂ K" in the
   ind-unipotent case. This is presumably what "faux par Tate" records; Tate's own argument is not on the page and is not
   reconstructed (hunch H1-1). The construction rests on Kisin's theory and Illusie's lifting theorem; the Kisin-module
   dictionary (character of u^c, special fibre = 𝔐/u𝔐) is used, not re-derived.

**Status of 9:10-14.** The character is the inertial part of what Fontaine later attached to potentially crystalline
representations (the inertial type of the Weil-Deligne representation, Fontaine, Astérisque 223 (1994); locator
unverified); his question "is it determined by _pM?" is the question of how the inertial type relates to the reduction mod
p (hunch H1-2). Open on the page: the ind-unipotent case, which the construction above settles negatively.

## 4. SA15-11: canonical stratifications on deformations, the Hasse invariant, and α_A (9:15-29)

### 9:16-18: a functorial stratification on DR¹ forces ordinarity and splits the Hodge filtration

**What he writes.** A_0 an abelian variety over k of characteristic p. Question: when can one attach ("d'associer", ink;
the Pro reading has "d'avoir", correction 10) to every infinitesimal deformation A/Λ (Λ local artinian k-algebra) a
k-stratification of DR¹(A/Λ), compatible with base change and functorial in A? On the formal moduli M with universal
A_M, H = DR¹(A_M/M) must have a formal stratification compatible with F: H^(p) → H and V: H → H^(p). Then the geometric
type of (H_x, F_x, V_x) is constant on M, which "implique sans doute" that A_0 is ordinary (Frobenius bijective on
H¹(A_0, O) = t_{A_0*}). Then for every A/Λ the extension H of H^{01} by H^{10} splits canonically by H' = Im F, stable
under the stratification; Im V = Ker F = H^{10(p)} is stable too. "Attention", this does not give H^{10} itself: on T =
S × S with the two pull-backs, G = u(F_1) and G' = F_2 satisfy G^(p) = G'^(p) as sections of Grass(E), i.e. they agree
after the p-th power base change π: T → T, which is not an epimorphism in general; but if S, hence T, is formally
smooth over k, π is faithfully flat and G = G'; this suffices by reduction to S = M. So H ≅ H^{10} ⊕ H^{01}, functorial
and stable under the stratification, and the problem moves to t_A^∨ and t_{A*}; on t_A there is already a stratification,
from the non-degenerate p-th power structure, "qui permet d'introduire le gpe structural discret Gl(g)_k" (margin
"à préciser"), and it is the only one compatible with the p-th power. **Remarque:** the position of the filtration with
respect to the stratification can give no classification principle for infinitesimal deformations in characteristic p.

**Checked** (9:16-a targeted, 9:16-18 re-proof, 9:18 re-proof).
- Necessity of ordinarity: if A_0 is not ordinary, the generic point of the universal deformation space is ordinary (the
  ordinary locus is dense; Norman-Oort, Ann. of Math. 112 (1980); locator unverified), so the type of (H, F, V) is not
  constant. "Sans doute" is right; it is the mechanism of 6:27 (section 2.7, the F² = 0 argument for elliptic curves,
  STUDY.md §2).
- The splitting: F kills ω^(p) (Frobenius kills differentials), so F factors through H^(p)/ω^(p) = (H^{01})^(p); the
  composite (H^{01})^(p) → H → H^{01} is the linearized Frobenius of H¹(A, O), bijective over Λ because it is on the
  closed fibre; hence H = H^{10} ⊕ Im F over Λ.
- Descent through Frobenius: for T = Spf k[[x_1, ..., x_n]] with k perfect, k[[x]] is free over k[[x^p]] = image of
  Frobenius, so π is faithfully flat and two sections of a Grassmannian equal after π are equal. M is formally smooth
  (deformations of abelian varieties are unobstructed). Correct.
- Uniqueness on t_A: write t_A = Φ_A ⊗ O with the p-th power 1 ⊗ (a ↦ a^p). Two stratifications compatible with it
  differ by g ∈ GL(pr_1^* t_A) with g ≡ 1 mod the diagonal ideal I and g∘Fr = Fr∘g; in a basis from Φ_A this says G =
  G^(p) entrywise, hence G = G^(p^n) ≡ 1 mod I^[p^n] for all n, so G = 1. Existence: the two pull-backs of an étale
  F_p-sheaf to the formal neighbourhood of the diagonal are canonically identified. The "discrete structural group" is
  GL_g(F_p), the Frobenius-fixed points of GL(g)_k; his "Gl(g)_k" carries his own "à préciser".
- The Remarque follows: the only candidate makes the Hodge filtration horizontal. It is the characteristic-p
  counterpart of 6:27 (2.7): without divided powers, no stratification can see deformations; with them, the Hodge
  filtration in the Dieudonné crystal classifies liftings (Grothendieck-Messing; Messing, LNM 264; locator unverified).
  The splitting is the unit-root splitting of an ordinary family (Katz, "Serre-Tate local moduli", LNM 868 (1981);
  locator unverified).

### 9:19-20: the F_p-structures, and the polarization class

**What he writes.** For an ordinary abelian prescheme A/S of characteristic p: DR¹(A/S) ≅ t_A^∨ ⊕ t_{A*} canonically,
t_A ≅ Φ_A ⊗_{F_p} O_S, t_{A*} ≅ Φ_{A*} ⊗ O_S with Φ étale locally free F_p-sheaves of rank g; over a perfect field
Φ_{A*} = (t_{A*})^F = H¹(A, O_A)^F = H¹(A, Z/p) = Hom(_pA, Z/p) = _pA(k)^∨ and Φ_A(k) = _pA*(k)^∨; in general _pA →
S factors uniquely as _pA → (_pA)_ét → S (radicial surjective, then étale), and Φ_A = (_pA*)_ét^∨, Φ_{A*} =
(_pA)_ét^∨. NB: a polarization φ (or a section of NS_{A/S}) gives φ' ∈ ∧² DR¹(A/S) = ∧²t_A^∨ ⊕ (t_A^∨ ⊗ t_{A*}) ⊕
∧²t_{A*}; φ' lies in the middle term and is the tangent map t_A → t_{A*} of φ̃: A → A*, determined by Φ_A → Φ_{A*},
the transpose of (_pA)_ét → (_pA*)_ét induced by _pφ̃.

**Checked** (9:19-20 targeted). H¹(A, Z/p) = H¹(A, O)^{F=1} by Artin-Schreier (k̄; Galois-equivariantly over perfect k),
and H¹(A, Z/p) = Hom(π_1(A), Z/p) = Hom(_pA(k̄), Z/p). Relatively, the connected part of _pA is of multiplicative type
for ordinary A and is Cartier dual to (_pA*)_ét, so t_A = Lie((_pA)^0) = Hom((_pA*)_ét, Lie μ_p) = (_pA*)_ét^∨ ⊗ O.
φ' in the middle term: both summands of H¹ are isotropic for the polarization form, H^{10} as usual and Im F because F
is zero on H^{2g}_dR in characteristic p, which is the argument of his struck draft. The tangent-map identification is
then forced. Correct. (His struck draft wrote the map t_{A*} → t_A; the live text has the right variance, as Michel
Hua's project also notes.)

### 9:21-22: the Hasse invariant, and ω_A ≅ ω_{A*}

**What he writes.** ω_A = (dét t_A)^{-1} = ∧^g t_A^∨ carries a non-degenerate p-structure (it comes from the rank-one
F_p-sheaf dét (_pA*)_ét), so ω_A^{⊗(p-1)} has a canonical section on the ordinary locus U; in fact it extends to all of
S as the determinant of t_A^(p) → t_A, σ_A ∈ Γ(ω_A^{⊗(p-1)}), "l'invariant de Hasse de A", whose zero set is exactly
the non-ordinary locus. From 0 → t_A^∨ → DR¹ → t_{A*} → 0 and DR^{2g} ≅ O_S: ω_A ≅ ω_{A*} canonically. "Je dis" that
this isomorphism is compatible with the p-structures, carries σ_A to σ_{A*}, and on the ordinary locus induces
dét (_pA)_ét ≅ dét (_pA*)_ét.

**Checked** (9:21-22 targeted). For a rank-one F_p-sheaf L_0, x^{⊗(p-1)} is independent of the local generator x
((ax)^{⊗(p-1)} = a^{p-1} x^{⊗(p-1)} = x^{⊗(p-1)}), so the section is canonical. The linearized p-th power of Lie(A) is
Lie(V_A), so σ_A is the classical Hasse invariant (dually, det of V on ω), non-zero exactly where (_pA)^0 is
multiplicative, i.e. where A_s is ordinary; on U it is the canonical section. ω_A ≅ ω_{A*} from the determinant of the
Hodge sequence: correct. **Open on the page**: "transforme σ_A en σ_{A*}". Reduction: with Im V = Ker F = ω^(p) and
Ker V = Im F, σ_A = det(V|ω) factors through V̄: H/Im F ≅ ω^(p) and the transversality determinant det(ω ⊕ Im F → H);
σ_{A*} = det(F on H/ω) factors through F̄: (H/ω)^(p) ≅ Im F and the same determinant; F̄ and V̄ are adjoint under
the de Rham duality, so the claim reduces to the compatibility of that duality with the trace H^{2g}_dR ≅ O. I have not
completed it (also listed as "never established" by Michel Hua's project).

### 9:23-29: the canonical isomorphism α_A: dét T_p(A)_ét ≅ dét T_p(A*)_ét

**What he writes.** For ordinary A, T_p(A) is an extension of T_p(A)_ét by T_p(A)_rad; by Cartier duality the middle
terms for A and A* are dual compatibly with the filtrations, so T_p(A)_rad ≅ D(T_p(A*)_ét) and conversely; the two
étale modules determine T_p(A) over a perfect base (in general "il y aurait lieu d'expliciter la structure
d'extension"). He wants a canonical dét T_p(A)_ét ≅ dét T_p(A*) [sic, without "ét"]. For ℓ ≠ p, dét T_ℓ(A) ≅ dét
T_ℓ(A*) ≅ Z_ℓ(g) (α_ℓ), and α_ℓ = β_ℓ(φ)/deg φ with β_ℓ(φ) = dét T_ℓ(φ̃). By analogy β_p(φ) = dét(T_p(φ̃)_ét) and
α_p(φ) = β_p(φ)/√(deg φ̃): dét T_p(A)_ét ⊗ Q_ℓ [sic] → dét T_p(A*)_ét ⊗ Q_ℓ. À prouver: a) α_p(φ) does not depend on φ.
A struck lemma (u an endomorphism: deg u a perfect square, dét T_p(u)_ét = √deg u) carries his "faux". 9:25: ψ̃ = φ̃u,
u ∈ End(A) ⊗ Q, ψ̃' = -ψ̃ and φ̃' = -φ̃ give u' = φ̃uφ̃^{-1}; with δ = √deg and Δ = dét T_p(·)_ét, a) is Δ(u) = δ(u);
"Or par Serre(?) on a Δ(u)Δ(u*) = δ(u)² = deg u"; Δ(u*) = Δ(u); so Δ(u) = ±δ(u); "Il faut encore exorciser le signe"
(ink; correction 11): prove u > 0 (u = Σ v_i v_i') ⇒ Δ(u) = +δ(u) [deg u is a square if u = u']. 9:26 (struck): the
same via "la théorie p-adique de Serre (ou th. cohomologique de Weil)" and a sign homomorphism ε. 9:27: Δ is a polynomial
in Z_p[T_1, ..., T_N] on the hermitian part of End(A), integer-valued at integer points, hence with coefficients in Q (a
struck line adds "Z_p[T] ∩ Q[T] = Z[T]"); over R every u ≥ 0 is v² with v hermitian, so Δ(u) = Δ(v)² ≥ 0, "cqfd". b)
α_p(φ) is an isomorphism of the integral lattices, i.e. v_p(card Coker T_p(φ̃)_ét) = v_p(√deg φ̃); 9:28: Coker T_p(φ̃)_ét
≅ (Ker φ̃)(p)_ét, Ker φ̃ is self-dual, so its étale and radicial p-parts have the same order and card((Ker φ̃)(p)_ét)²
= deg(φ̃)(p). Boxed: α_A: dét T_p(A)_ét ≅ dét T_p(A*)_ét, compatible with base change and isomorphisms. For an
automorphism u: dét T_p(u)_ét · dét T_p(u*)_ét = 1; for an endomorphism in general dét T_p(u) ≠ dét T_p(u*) even for an
elliptic curve, so α is not functorial in homomorphisms, but dét T_p(u)_ét · dét T_p(u*)_ét = deg u (margin: also for
homomorphisms between abelian schemes of the same dimension). c) "Il faudrait vérifier que α_{A*} = α_A^{-1}" "[sans signe
(?)...]" (ink; correction 12); "Noter aussi le comportement par somme de VA." d) the isomorphism "(_pA)_ét → (_pA*)_ét"
induced by α_A should be the one deduced from de Rham duality (9:22) "(à vérifier ...)". Two slips on 9:24: "⊗ Q_ℓ"
for ⊗ Q_p (the Tate modules are p-adic; the ℓ is carried over from the ℓ-adic model above; correction 14, also Michel
Hua's project) and "dét T_p(A*)" without "ét" in the opening display (correction 15, also K9-02 and Michel Hua's project).

**Checked** (9:24-28 re-proof; 9:24 computation; 9:29 targeted).
- The key identity Δ(u)Δ(u*) = deg u: for ordinary A over k̄ the rational Dieudonné module of A[p^∞] is the sum of the
  étale part (on which u acts as T_p(u)_ét) and the multiplicative part, whose Tate module is the Z_p(1)-dual of
  T_p(A*)_ét (on which u acts as the transpose of T_p(u*)_ét); the determinant of u on the whole is deg u (equality of
  characteristic polynomials on the Dieudonné module and on T_ℓ). Serre's Witt-vector cohomology of abelian varieties
  (Amer. J. Math. 80 (1958); locator unverified) is presumably "la théorie p-adique de Serre". Test over F_q with u =
  π_A, the Frobenius endomorphism: Δ(π_A) = α_1⋯α_g (the unit-root eigenvalues); u* is the dual isogeny of Frobenius,
  the Verschiebung q·π_{A*}^{-1}, which acts on T_p(A*)_ét with eigenvalues q/α_i (A* is isogenous to A); the product
  is q^g = deg π_A, as it must be.
- a): Δ(u*) = Δ(φ̃uφ̃^{-1}) = Δ(u) (conjugate matrices over Q_p) since u is Rosati-symmetric (Michel Hua's project
  notes that u' = φ̃uφ̃^{-1} is u* on A*, the involution being Rosati); Δ(u)² = deg u. Rationality: Δ is a degree-g
  polynomial on the free Z-module of symmetric elements with Z_p coefficients and integer values at integer points,
  hence an integer combination of binomial polynomials, so its coefficients are rational. Positivity: on End(A)_sym ⊗ R,
  a totally positive u is v² with v symmetric (spectral theory in the semisimple algebra with positive involution);
  Δ(v²) = Δ(v)² holds on rational points by multiplicativity, hence identically; so Δ(u) ≥ 0, and Δ(u) = ±δ(u) ≠ 0
  gives Δ(u) = +δ(u). The polarizations ψ correspond to totally positive symmetric u (Mumford, AV §21; locator
  unverified). **a) is proved**, granting Δ(u)Δ(u*) = deg u. The struck coefficient line is wrong (the intersection is
  Z_(p)[T]; 1/4 at p = 3 is in both and not in Z[T], as K9-02 computes), and he struck it.
- b): for an isogeny f, Coker(T_p(f)) ≅ (Ker f)(p); on étale parts, f maps (A[p^∞])^0 onto (A*[p^∞])^0, so the kernel
  of the map of étale quotients is N_ét for N = (Ker φ̃)(p), and Coker T_p(φ̃)_ét ≅ N_ét. N is self-dual (Mumford, AV
  §23; locator unverified) and over an ordinary base N^0 is multiplicative, Cartier dual to N_ét, so card N = (card
  N_ét)². Hence β_p(φ) = p^v·(unit) with p^v = card N_ét, and dividing by √deg φ̃ = p^v·m (m prime to p) gives an integral
  isomorphism. **b) is proved.**
- The struck lemma is false, as his "faux" says: for an ordinary elliptic curve with CM by O_K and u = π, Nm(π) = p
  (p split), deg u = p is not a square. The same u shows dét T_p(u) ≠ dét T_p(u*) (π and π̄ = p/π in Z_p), with
  product p = deg u, as boxed on 9:29.
- c): with ψ̃ = nφ̃^{-1} (n the exponent of Ker φ̃) as polarization of A*, Δ(ψ̃) = n^g Δ(φ̃)^{-1} and δ(ψ̃) = n^g/δ(φ̃),
  so α_{A*} = α_A^{-1} up to dét(-1) = (-1)^g coming from the biduality sign convention (his ψ̃' = -ψ̃). So "sans signe
  (?)" is right up to (-1)^g, depending on the convention for A ≅ A**.
- d): α_A is an isomorphism of determinant lines only, so d) must read dét (_pA)_ét → dét (_pA*)_ét (correction 13; the
  same remark is K9-02's R29-det). Open on the page. Reduction: both maps are isomorphisms of rank-one F_p-sheaves on the
  ordinary locus, compatible with base change, so they differ by a locally constant F_p^*-valued function on the ordinary
  locus of the moduli space; for elliptic curves, where α_E is (_pφ̃)_ét for the principal polarization, the de Rham
  isomorphism is its inverse up to sign if Serre duality ω × H¹(O) → H¹(Ω¹) matches the polarization on tangent spaces
  up to sign (hunch H1-3).

**Status.** a) and b) are proved on the pages (granting the determinant identity, which is known); c) holds up to the sign
(-1)^g; d) and the σ_A ↦ σ_{A*} compatibility are open. I have not located the canonical isomorphism α_A as a published
statement (not searched beyond the corpus at hand); its ingredients are standard.

## 5. Hunches

- **H1-1 (9:14).** "Faux par Tate" records a counterexample to Raynaud's criterion with ℓ = p, necessarily with
  supersingular (more generally non-ordinary) reduction: section 3 proves the ordinary case positive and constructs a
  supersingular counterexample over Q_p(ζ_{p²}). Grounds: his own pointer to Hasse invariant zero; the construction;
  ramification e ≥ p(p-1) is used, while for e < p-1 Raynaud's uniqueness of prolongations rules such models out. Links:
  SGA 7 I, exp. IX, Prop. 4.7 (Raynaud's criterion; whether a remark there cites Tate is to be checked; locator
  unverified); Kraus, Manuscripta Math. 69 (1990), on the semistability defect (locator unverified); SA15-17 (6:33-37) and
  the cote 100 text (part 2).
- **H1-2 (9:11-13).** The character is the inertial type of the potentially Barsotti-Tate representation, defined twenty
  years before Fontaine's D_pst; his question whether it is determined by _pM is the inertial-type versus mod-p-reduction
  question behind Serre weights and Breuil-Mézard. The section 3 example (isomorphic _pE with different traces: E and a
  good-reduction curve with E[p] trivial) answers the "cas test" negatively too.
- **H1-3 (9:22, 9:29 d)).** The two isomorphisms dét (_pA)_ét ≅ dét (_pA*)_ét (de Rham, and α_A mod p) agree up to a
  constant sign c_g, multiplicative in products, so c_g = c_1^g. Grounds: rigidity of rank-one F_p-sheaves on the
  connected ordinary locus (the Igusa cover of level p is connected for g = 1).
- **H1-4 (9:16-18).** The result of the sheet is the characteristic-p half of the crystalline philosophy: a functorial
  stratification on DR¹ compatible with F and V exists iff A_0 is ordinary, is then unique, and freezes the Hodge
  filtration. Read with 6:27 (2.7), it is a second reason why the theory needs divided powers. Links: SA15-16, Katz's
  unit-root splitting, Deligne's canonical liftings (Serre-Tate coordinates).
- **H1-5 (9:3).** "Innovation intéressante" names the conjugate flag Im F_0 = Ker V_0; the pair (Hodge flag, conjugate
  flag with F, V) is the F-zip of Moonen-Wedhorn and the source of Ekedahl-Oort strata (locators unverified).
- **H1-6 (9:5-8).** The truncated Dieudonné ring A/(F^n, V^n) is self-dual as a bimodule over W_n (with the index
  corrected), so I = lim A_n is a dualizing bimodule; this gives Dieudonné duality of finite modules without choosing
  Hom_W(-, K/W) by hand. Possibly the form meant for truncated Barsotti-Tate groups.
- **H1-7 (9:9).** The struck lemma is an abstract Katz-Oda construction; placed between the duality sheets and the
  character typescript, it dates his interest in a direct Gauss-Manin construction to the period of the cote 7 lectures
  (November-December 1966).
- **H1-8 (dating).** 9:2-8 are on Pisa stationery with an Italian vocabulary list and a Pisa street plan ("Corso Italia"),
  so they are most likely of his stay in Pisa in spring 1966 (letter to Tate, "Pise, Mai 1966"); 9:11-14 postdate Tate's
  Driebergen lecture (1966); part 2 dates the cote 100 manuscript to 1968.

## 6. Dependencies

- SA15-10 (9:2-8) uses SA15-16 (the universal extension G̃ of 6:25-26, his "grp enveloppant" on 9:3; the Dieudonné crystal
  of 6:22-23) and SA15-2 (F_0, V_0).
- SA15-15 (9:9, struck) is the Gauss-Manin question of cote 7 (`c7_c8.md`), with SA15-1.
- SA15-19 (9:10-14) uses SA15-16 (BT groups over S' and their Dieudonné modules), Tate's theorem (also cited in the
  100:48-51 typescript, STUDY.md §3) and leads to SA15-17 (6:33-37: reduction of elliptic curves, Hasse invariant zero).
- SA15-11 (9:15-29) uses SA15-16 (DR¹ as a Dieudonné crystal and the obstruction of 6:27, 2.7), SA15-2 (F, V on DR¹) and
  SA15-9 (4:5-6: semisimple parts, Frobenius on H(X, O); 9:19 writes Φ_{A*} = H¹(A, O)^F, the same object, Pro note #57).
- Across topics: SA14-2 (universal vector extension, H0A1) for 9:3; SA06-8 (supersingular elliptic curves, 15:34-78) for
  the Hasse invariant of 9:21-22 and the supersingular case of 9:14.

## 7. Deliverable state of cote 9

- **Passes:** Pro (`MPL_8_079-081+9+4+100`, transcription and 88 notes for cote 9); Codex web K9-01 (2-15) and K9-02
  (16-29), GPT-6.2 Astra at reasoning effort max (ChatGPT Work), with notes, math notes and check events; Michel Hua's
  project (batches and modernised reading) as a credited witness; this sweep-3 reading.
- **Readings decided here:** "i.e. G* sans tore" (3), "des dérivations" (3), "d'associer" (16), "exorciser" (25),
  "sans signe (?)" and "le comportement par somme de VA" (29), the exponent n + 1 (7).
- **Open readings:** "Or par Serre(?)" or "lemme" (25; context and 9:26 favour Serre); ∃! or ∃1 (5); the arrow direction
  of the inserted ⊗Q_ℓ line (24); "implique" or "indique" (16, K9-02); the gutter labels on 8.
- **Ready for an edition:** yes, once corrections 1, 2, 10, 11, 12 are applied to the transcription and his slips
  (corrections 3-9, 13-15; 6 is on a struck page) carry editorial notes. Scans 1, 4, 6 are documents (SA15-12).
