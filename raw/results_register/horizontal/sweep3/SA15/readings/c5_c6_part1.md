# SA15, cote 5 (all scans): sweep 3 reading, stretch c5_c6_part1

Claude Opus 5.5 at effort max, c5_c6_part1 reader, sweep 3 reader (launched by the SA15 stretch reader c5_c6,
Claude Opus 5.5 at effort max). Begun 18 Nov 2026 (UTC). Package `MPL_5+6_001-037`, cote 5, scans 1 and 3-53 (there
is no scan 2), read in page order on the Pro transcription with the reader tool, the Pro notes and doubts as a first
witness, and the scan images wherever a reading was in doubt (whole scans and halves, and renders of
`02_cristaux/5.pdf` at 250-500 dpi). Check events are in `c5_c6_part1_CHECK_EVENTS.tsv`, corrections in
`c5_c6_part1_CORRECTIONS.tsv`. Scripts used for the computations (scratchpad, not kept): `wnu_check.py` (p-adic
elementary divisors of W^(nu) and W^(nu,r)), `misc_checks.py` (Legendre, the DVR thresholds, the coefficients of 5:39
and 5:41).

Item ids are those of `sweep2/SA15/WHAT_IS_WHERE.md`.

---

## 5:1 — cover

The institutional cover of the cote (IMAG, "Institut Montpelliérain Alexander Grothendieck"). Nothing of his. SA15-12.

## 5:3 — a cube of topoi, and the crystalline Chern class (SA15-1)

**What is on the page (his hand, pencil).** A diagram of ringed topoi: X_zar at the top maps to X_conn and X_ℙ-conn;
X_conn -> X_strat labelled "équiv car 0", X_conn -> X_cris and X_ℙ-conn -> X_ℙ-cris labelled "équiv si X/S lisse";
X_strat, X_cris -> X_inf; X_cris, X_inf, X_ℙ-cris -> X_zar; dashed arrows X_conn -> X_ℙ-conn, X_cris -> X_ℙ-cris,
X_ℙ-conn -> X_strat, X_ℙ-cris -> X_inf, "définis si X de torsion sur Z". Margin: "morphismes de topos annelés", "NB S
sous-entendu dans notations", and down the left edge "détermination des points de ces topos ?". Then:
- "Les flèches à valeurs dans X_zar donnent lieu à des isomorphismes de localisation **zariskienne**, resp. des suites
  spectrales intéressantes". The Pro reading "gerbienne(?)" (doubt: galoisienne) is wrong: on the 500 dpi render the
  first letter has exactly the form of the subscript z of "X_zar" in the line above (a z with a descending loop), and
  the letters fit z-a-r-i-s-k-i-e-n-n-e. This also gives the sentence its sense: for u: X_? -> X_zar the cohomology
  localizes over the Zariski topology (Leray, R^q u_*). Reading decided on the image.
- "Les flèches en provenance de X_zar donnent lieu à une suite exacte 0 -> J -> O_𝒳 -> O_{𝒳_0} -> 0", with a margin,
  separated by a slanted stroke: **"dire que Mod(X_zar) ⥲ Mod(O_{𝒳_0})"** (the arrow carries a double tilde). The Pro
  .tex has this text inside a tikz figure, which the reader tool prints as "[figure]"; the reading is right (checked on
  the image). Readers of this stretch should know that the reader tool hides every text node inside a tikz figure
  (also the boxed equivalences of 5:13 and the bibliographic note of 5:37).
- "Pour un module inversible L sur X_zar, on définit une classe de Chern c^1(L) dans H^2(X_cris) et H^2(X_ℙ-cris), qui
  sont compatibles si X de torsion. Sur X_cris, son annulation est NS pour que L provienne d'un Module inversible sur
  X_cris [donc dans le cas relatif lisse qu'il admette une connexion intégrable]." The superscript is the "1" of c^1
  written like a prime (c'(L)); the Pro "c^{1(?)}" is right.

**Worked through.**
1. *The obstruction.* With i: X_zar -> 𝒳 (𝒳 = X_cris, X_inf, ...), O_{𝒳_0} = i_*O_X = O_𝒳/J. Since the thickenings are
   nilpotent (or PD with p nilpotent), J is locally nil, so 1 -> 1+J -> O_𝒳^* -> i_*O_X^* -> 1 is exact. i_* is exact
   and has the exact left adjoint i^{-1}, so it preserves injectives and H^1(𝒳, i_*O_X^*) = H^1(X_zar, O_X^*) = Pic(X).
   The coboundary δ(L) in H^2(𝒳, 1+J) vanishes iff L is i^*ℒ of an O_𝒳^*-torsor, i.e. of an invertible O_𝒳-module.
   So the "NS" statement is right **provided c^1(L) is read as δ(L) in H^2(X_cris, 1+J)**, the multiplicative class.
   On the PD site the logarithm log(1+x) = Σ (-1)^(n-1)(n-1)! x^[n] (a finite sum when p is nilpotent) carries it to
   H^2(X/S_cris, J) and then to H^2(X/S_cris, O): this is the crystalline Chern class of Berthelot-Illusie ("Classes de
   Chern en cohomologie cristalline", C. R. Acad. Sci. Paris 270, 1970; locator unverified). On a site without divided
   powers there is no logarithm in characteristic p, so on X_cris (no ℙ) the class must stay multiplicative; his
   "compatibles si X de torsion" goes through the dashed arrow X_cris ⇢ X_ℙ-cris. Check event: independent re-proof.
2. *"dans le cas relatif lisse qu'il admette une connexion intégrable".* An invertible O_𝒳-module is locally
   isomorphic to O_𝒳, hence a crystal; for X/S smooth crystals are modules with a stratification (infinitesimal site),
   resp. with an integrable quasi-nilpotent connection (PD site, Berthelot-Ogus, Notes on crystalline cohomology, 1978,
   Thm 6.6, locator unverified). So the bracket is exact in characteristic 0, and in characteristic p it needs
   "stratification" (non-PD) or "connexion intégrable quasi-nilpotente" (PD). In characteristic 0 the class is the image
   of c_1(L) in H^2(X, Ω^{>=1}_{X/S}) = F^1 H^2_DR, the classical obstruction to an integrable connection.
3. *The margin "dire que Mod(X_zar) ⥲ Mod(O_{𝒳_0})".* (In the .tex O_{X_0}; on the image the X is the script 𝒳 of
   O_𝒳 in the sequence.) As an equivalence onto all O_𝒳/J-modules this is **false** for
   the crystalline and infinitesimal topoi: i_* is fully faithful (i^{-1}i_* = id) and exact, but J/J^2 is an
   O_𝒳/J-module (J kills it) with value I_T/I_T^2 on (U,T) and 0 on (U,U), so it is not i_*E for any E (on i_*E the
   transition along (U,U) -> (U,T) is the identity). Example: X = S = Spec k, T = Spec k[ε]/(ε^2) with γ_n(ε) = 0
   (n >= 2). Correct statement: i_* identifies Mod(X_zar) with the O_𝒳/J-modules F whose maps F_(U,T) -> F_(U,U) are
   isomorphisms (the O_𝒳/J-modules that are crystals). Check event: refuted, with the refined statement.
4. *The diagram.* "ℙ" is not defined on the page. On the reading ℙ = with divided powers, the labels match what is
   known: connections and stratifications agree in characteristic 0 (X/S smooth); PD-connections (integrable,
   quasi-nilpotent) and PD-crystals agree for X/S smooth (Berthelot 1974, IV; Berthelot-Ogus Thm 6.6; locators
   unverified). The label "équiv si X/S lisse" on X_conn -> X_cris (no ℙ) holds in characteristic 0; in characteristic p
   connections without divided powers are not crystals (a stratification carries more data), so that label needs
   characteristic 0 or a PD reading of X_cris. Since the page does not define X_conn, X_strat and X_inf, I record this
   as a reading of the labels, not as a correction.

**Open on the page.** "détermination des points de ces topos ?" (his question; not settled here).
**Uses:** SA15-14 (divided powers, through X_ℙ-cris). **Place:** SA15-1.

## 5:4 — "THEOREM 12", a typescript leaf of Serre-Tate (SA15-19 placement; SA15-12 as a document)

Decided on the image: a **typescript** leaf, page "-32-", typewriter text with the Greek letters, subscripts and
reference numbers ([18], [7]) filled in by hand in the typing hand, and typed underlining. It is a preprint page of
J.-P. Serre and J. Tate, "Good reduction of abelian varieties", Ann. of Math. 88 (1968), 492-517, §7 (abelian varieties
with complex multiplication: the Grössencharakter χ_σ, Theorem 12 on the conductor; locator unverified). **Nothing of
his is on it**: no annotation, mark or correction in his hand; the "3" at the foot is the archive's sheet number. Not
studied (shared brief, item 6). Its place in this folder fits his use of Serre-Tate in "Bonne réduction" (cote 100,
SA15-19).

## 5:5-5:8 — the universal PD-Artinian ring W^(ν) and its normal form (SA15-14)

**What he does (his hand, ink).** W = W(k), k perfect, ν >= 1. Category: Artinian rings with residue field k whose
maximal ideal carries "ν-nilpotent" divided powers; "On va construire un objet initial". Every such Λ is a W-algebra
(Cohen) in which p goes into m_Λ, so Λ receives
W^(ν) = W[Λ_0..Λ_ν]/(Λ_i^p - c_i Λ_{i+1} (0 <= i < ν), Λ_ν^p ; Λ_0 - p), c_i = (p^{i+1})!/((p^i)!)^p,
"[W-algèbre avec idéal J = (Λ_0..Λ_ν) à puiss. div. ν-nilpotentes, universel ...]. NB Λ_ν = γ^{p^ν}(Λ_0); on utilise le
fait que dans W les nbs premiers l ≠ p sont inversibles." W^(ν) is Artinian with residue field k and maximal ideal J.
To compute it: A^(ν) = the same ring without Λ_0 - p, λ_r = p^{p^r}/(p^r)! (the habitual γ_{p^r}(p)), Λ_i = λ_i + Θ_i;
A^(ν) is free over W on Θ^a (0 <= a_i <= p-1). **Lemma (5:6-7):** Σ w_a Θ^a lies in I = (Θ_0) iff (a) w_a ∈ p^i W when
a ≠ 0 has first nonzero coordinate a_i, (b) w_0 ∈ p^{c(ν)} W, with c(ν) = ν + p[p^ν - (p^{ν-1} + ... + 1)].
Sufficiency from p^i Θ_i ∈ I (induction, using v_p(c_i) = 1) and p^{c(ν)} ∈ I (from (λ_ν + Θ_ν)^p = 0 times p^ν);
necessity: "l'ensemble I' ... est bien un idéal ... La vérification est facile et laissée au lecteur" (margin "!").
**Corollary (5:7-8):** normal form of W^(ν): Σ w_a Θ̇_1^{a_1}...Θ̇_ν^{a_ν}, w_a ∈ E_i (representatives of W/p^i) for
first nonzero a_i, w_0 ∈ E_{c(ν)}. **Lemma (5:8):** for W^(ν,r) = W^(ν)/(Θ̇_1..Θ̇_r): conditions w_a ∈ p^{i-r}W (first
nonzero index i > r) and w_0 ∈ p^{c(ν)-r}W, with the corresponding normal form.

**Checked.**
1. *W^(ν) is initial (independent re-proof).* The map Λ_i -> x^[p^i] identifies A^(ν) with W<x>/Γ^{>=p^{ν+1}}, the
   divided power polynomial algebra cut off in degree p^{ν+1} (the relations hold there, and the basis Λ^a goes to unit
   multiples of the basis x^[n], n < p^{ν+1}, because Π (x^[p^i])^{a_i} = (n!/Π((p^i)!)^{a_i}) x^[n] with a p-adic unit
   coefficient when the a_i are the base-p digits of n). So A^(ν) carries a PD structure on its augmentation ideal J
   with γ_n(J) = 0 for n >= p^{ν+1}, and Λ_i = γ_{p^i}(Λ_0) exactly. Since p is a non-zero-divisor in W, I ∩ J =
   J·(x - p), and γ_n(j(x - p)) = (x - p)^n γ_n(j) ∈ I, so I ∩ J is a sub-PD-ideal and W^(ν) = A^(ν)/I inherits the PD
   structure, with γ_{p^i}(p) = Λ_i and γ_n = 0 on m for n >= p^{ν+1}. For (Λ, m, δ) in the category, the unique
   W-algebra map W -> Λ and the universal property of W<x> give a unique PD-morphism x -> p, which kills Γ^{>=p^{ν+1}}
   and x - p. So W^(ν) is initial, with "ν-nilpotent" read as γ_{p^{ν+1}} = 0 on m (equivalently γ_n = 0 for all n >=
   p^{ν+1}, since γ_{p^i}, i > ν, is a unit times an iterate of γ_{p^{ν+1}}). The PD structure on W^(ν) is not the
   habitual one on pW: Λ_i = λ_i + Θ̇_i with Θ̇_i ≠ 0.
2. *The Lemma, both directions (independent re-proof).* Sufficiency as on the page; the arithmetic v_p(c_i) = 1 and
   v_p(p^ν λ_ν^p) = ν + p(p^ν - (p^ν - 1)/(p-1)) = c(ν) is right. For "la vérification ... laissée au lecteur": I' is
   stable under multiplication by each Θ_j. Reducing Θ_j^p = c_j Θ_{j+1} - Σ_{α=1}^{p-1} C(p,α) λ_j^{p-α} Θ_j^α (j < ν;
   for j = ν the first term is -λ_ν^p) carries a coefficient lying in p^{min(i(a''), j)} to coefficients lying in
   p^{min(i(a''), j)+1}; the invariant "the coefficient of Θ^b lies in p^{i(b)}" survives every carry, and a carry
   that empties the monomial produces a constant in p^ν λ_ν^p W = p^{c(ν)} W. So I' is an ideal containing Θ_0, and
   I = I'. The margin "!" does not mark an error.
3. *Computation.* For (p, ν) = (2,1), (2,2), (2,3), (2,4), (3,1), (3,2), (5,1), (7,1) and every r = 0..ν, the p-adic
   elementary divisors of A^(ν)/(Θ_0..Θ_r) (multiplication matrices in the basis Λ^a, λ_i as p-adic numbers) are exactly
   those of the normal forms: W/p^{c(ν)-r} once and W/p^{i-r} with multiplicity (p-1)p^{ν-i} for i > r. Lengths: W^(ν)
   has length c(ν) + Σ_{i=1}^ν i(p-1)p^{ν-i} (4, 8, 16, 32 for p = 2, ν = 1..4; 9 and 27 for p = 3; 25 for p = 5; 49 for
   p = 7). Example: p = 2, ν = 1 gives W^(1) = (W/8)[Θ]/(2Θ, Θ^2 + 4), with γ_2(2) = 2 + Θ, γ_3(2) = 4/3, γ_4 = 0.

**Wrong or to correct.**
- 5:6, the expansion of (Θ_i + λ_i)^p - c_i(Θ_{i+1} + λ_{i+1}): the sum must run over α = 1..p (the Θ_i^p term is
  needed). On the image the bound is "p" with a trace of an overwritten mark, and the struck-out left side "Θ_i^p ="
  shows that he moved Θ_i^p into the sum; the Pro reading "p-1(?)" should read "p". The coefficient written "C_i^p" is
  the binomial C(p, α) (his index slip). The right side "(++ c_i Θ_{i+1})" is his "(-λ_i^p + c_i λ_{i+1} + c_i Θ_{i+1})"
  with the two cancelling terms struck through.
**Open:** nothing; 5:5-8 are complete and right.

## 5:9 — weighted nilpotence (SA15-14)

"Λ_0^{a_0}...Λ_ν^{a_ν} = 0 si Σ a_i p^i >= p^{ν+1}", by carrying a_i >= p into Λ_{i+1} (Λ_i^p = c_i Λ_{i+1}), which
keeps Σ a_i p^i, down to b_i <= p-1 (i < ν), b_ν arbitrary; then Σ b_i p^i >= p^{ν+1} "(et alors seulement)" b_ν >= p,
and Λ_ν^p = 0. **Checked** (independent re-proof): each carry lowers Σ a_i strictly, so the process ends; Σ_{i<ν} b_i
p^i <= p^ν - 1 gives the "alors seulement"; and conversely, when Σ a_i p^i < p^{ν+1} the monomial is a nonzero integer
multiple of a basis element, so the threshold is sharp. **Slip on the page (in the ink, faithfully transcribed):**
"Λ_i^{a_i} = (Λ_i^p)^{a'_i} Λ_i^{α_i} = (c_i Λ_{i+1})^{a'_i} Λ_i^{α_i}" should read (Λ_i^p)^{q_i} Λ_i^{a'_i} =
(c_i Λ_{i+1})^{q_i} Λ_i^{a'_i} for a_i = p q_i + a'_i; the next line and the digit identity a'_i p^i + (a_{i+1} +
q_i)p^{i+1} = (a'_i + q_i p)p^i + a_{i+1}p^{i+1} use the right exponents.

## 5:10, 5:12, 5:34, 5:36 — leaves of a typescript on quasi-functions and heights (SA15-12)

Typescript leaves numbered 34 (5:10, upside down in the scan), 45bis (5:12), 41 (5:34) and 39 bis (5:36), in French:
quasi-functions on abelian varieties, the homomorphism ξ_o: Q*_ℓ(A) -> B*(A), μ(q,a) "définie sur K", the relations
(15), and the estimate |φ(2^h m) - 2^h φ(m)| <= (2^h - 1)d for quasi-linear sequences. From the content, a typescript of
A. Néron, "Quasi-fonctions et hauteurs sur les variétés abéliennes", Ann. of Math. 82 (1965), 249-331 (identification
from the notions and notation, locator unverified). The marks "ⓧ" and "-> ⓧⓧ p.45" on 5:12 are routing marks for the
inserted page 45bis. Nothing of his mathematics; not studied.

## 5:11 — Legendre's formula by digit sums (SA15-14)

His hand: v_p((p^{μ+1})!) = (μ+1) + (p-1)[v_p((p^μ)!) + ... + v_p(p!)] (from the step N-1 -> N, N = Σ_{i>μ} a_i p^i),
the values v_p((p^ν)!) = (p^ν - 1)/(p-1) for ν = 1..4 and in general, and the boxed v_p(n!) = (n - Σ a_i)/(p-1). He
writes "v_p(p^ν)" for v_p((p^ν)!) throughout (also on 5:32); the Pro transcription keeps this, rightly. **Checked**
(independent re-proof of the recursion, and computation for p <= 7, n < 400): right. Known: Legendre (1808).

## 5:13 — when are the π^n/n! integral, and when do they tend to 0 (SA15-14)

His hand: with chif(n) the base-p digit sum, (p-1)v_p(π^n/n!) = n[(p-1)v_p(π) - 1] + chif(n); boxed: "v_p(π^n/n!) >= 0
pour tt n <=> v_p(π^n/n!) > 0 pour tt n (n >= 1) <=> v_p(π) >= 1/(p-1), i.e. π^{p-1} ∈ pV" (this box is in the .tex
inside a tikz figure, hidden by the reader tool), and boxed "v_p(π^n/n!) -> +∞ <=> v_p(π) > 1/(p-1), i.e. p = unit·π^r
avec r < p-1". **Checked** (independent re-proof; computation for p <= 7, e < 2p): for a DVR with absolute ramification
index e, the maximal ideal has divided powers iff e <= p-1, and they tend to 0 (exp converges, topologically nilpotent PD)
iff e < p-1; at e = p-1 the subsequence n = p^k gives (p-1)v = 1. The middle equivalence (">= 0 for all n" <=> "> 0 for all
n >= 1") holds because chif(n) >= 1. **Slip:** "chiff n <= (p-1)ν" for n with top digit a_ν should be (p-1)(ν+1) (ν+1
digits; a struck "+1" is visible after it); the limit chif(n)/n -> 0 is unaffected. Known: Berthelot-Ogus 1978, §3
(locator unverified). Uses: 5:11.

## 5:14 — a list of printer's corrections (SA15-12)

His hand, with red ticks and three long diagonal strokes: corrections to pages 64-76 of an unidentified printed text
("S̄ = Spec(k̄)", "noethériens", "7.9.4)", "le composé", "X_K (K maj.)", "Compléter bibliographie par [6]"). No
mathematics. The paper shows a vertical watermark in its lower half.

## 5:15-5:20 — "General non-sens sur Frobenius": the topos L(α, β) (SA15-2)

5:15 is a cover sheet with the heading "Frobeniuseries" (the end of the word is uncertain; the Pro reading is kept).

**What he does (his hand).** 1) For a square of topoi g f_X ≅ f_Y g and E on X: the base change map c_E: f_Y^* g_* E ->
g_* f_X^* E (1.1); with F_E: f_X^* E -> E (1.2) the composite g_*(F_E)∘c_E: f_Y^* g_* E -> g_* E (1.3) (also for
groups, and "fait analogue" in derived categories); dually c^G: f_X^* g^* G ⥲ g^* f_Y^* G (1.4) and g^*(F_G)∘c^G (1.6).
2) For α, β: X' ⇉ X, L(α,β) = pairs (E, F_E: α^*E -> β^*E) [resp. F_E iso]; "oubli" ω^*(E, F_E) = E. **Prop.** L(α,β)
is a topos and ω^* is the inverse image of ω: X -> L(α,β); F: ωβ -> ωα canonical; for every topos Y, g ↦ (g∘ω, g*F) is
an equivalence Hom_top(L(α,β), Y) -> Hom_top(X, α, β; Y) = {(φ: X -> Y, f: φβ -> φα)}. Proof sketch (5:18): Giraud a)-c)
are clear, ω^* is left exact and commutes with colimits; the only point is a small generating family: in the "resp" case
L = cartesian sections of the evident fibred topos over x' ⇉ x, "et on peut appliquer SGA4 I 9.25"; in the other case
"les arguments de SGA4 I 9.21 et suite donnent le résultat" (margin "à vérifier"). Functoriality L(u): L(α,β) ->
L(λ,μ) for a square u (5:18-19). 5:19-20: the base change maps ω^*(R^i v_* ℰ) -> R^i u_{0*}(E) "et on aimerait savoir
que ce sont des isoms"; this needs E acyclic when ℰ = (E, F_E) is injective; "Il suffit pour ceci que α et β commutent
aux produits infinis (i.e. α_!, β_! existent), auquel cas il en est de même de ω_X, i.e. ω_{X!} existe."

**Checked.**
1. (1.1)-(1.6): right (targeted check; the base change map is the usual adjunction composite).
2. *The Proposition* (targeted proof check). ω^* creates finite limits and all colimits (α^*, β^* are exact and
   cocontinuous), so Giraud's exactness conditions hold in L(α,β). L(α,β) is the inserter of the accessible functors
   α^*, β^* between locally presentable categories, hence locally presentable (inserters are among the constructions
   that preserve accessibility: Adámek-Rosický, Locally presentable and accessible categories, 1994, 2.72, locator
   unverified), so a small generating family exists: L is a topos in both cases, and his "à vérifier" is settled
   positively. The universal property follows: (φ, f) gives the left exact cocontinuous functor G ↦ (φ^*G, f_G) from Y to
   L. The references read "SGA4 I 9.25" and "SGA4 I 9.21" on the image (Roman I, "SGA4" inserted above); the Pro note
   locates them in SGA 4 I §9 (Corollary 9.25, 9.21-9.23; locators not opened by me).
3. *The acyclicity (5:19-20).* In the Frobenius case of n°1 (β = id) the claim holds without hypothesis: a structure
   α^*E -> E is an algebra for T = α^*, the free one on E is ⊔_n (α^*)^n E, so on abelian objects ω_! = ⊕_{n>=0}
   (α^*)^n is exact, ω^* preserves injectives, and E is injective, hence acyclic; the comparison ω_Y^*(R^i v_*ℰ) ≅
   R^i u_{0*}(E) follows. In general ω_!^{ab} = ⊕_n (β_!^{ab} α^*)^n, which is exact when β_!^{ab} is exact; the
   existence of α_!, β_! alone does not give that (β_!^{ab} can be a non-exact cokernel, e.g. for the morphism of
   presheaf topoi induced by a pair of parallel arrows -> point). So his sufficient condition is unproved on the page and
   I have not settled it; the case he needs (n°1) is true.

**Slips in the ink (the Pro (?) marks are right to doubt them):** 5:17 "Hom_top(X, L(α,β))" for ωα, ωβ should be
Hom_top(X', L(α,β)); 5:17 last line "Hom_top(L(α,β), X)" should be Hom_top(L(α,β), Y); 5:19 "ω_X^*(R^i v_*(ℰ))" should be
ω_Y^*(R^i v_*(ℰ)) (v_*ℰ lives on L(λ,μ)). All three checked on the images.
**Uses:** SGA 4 I §9, V (his page). **Used by:** SA15-2 (F-objects; the Frobenius structures of cote 8).

## 5:21 — cover "Th de De Rham (à puissances divisées)" (SA15-1)

A cover heading only (Th|Alg uncertain, Th preferred). It heads the PD sheets 5:22-27 and the de Rham site of 5:28-31.

## 5:22-5:27 — §1-§3: divided-power pseudo-rings, Γ(M), the PD envelope, log and exp (SA15-14)

**What he does.** §1 (5:22-23): a pseudo-ring with operations π^n, n >= 1, axioms 1.1-1.5 (1.2 additivity without π^0;
1.3 π^n(xy) = x^n π^n(y); 1.4 π^m∘π^n = (mn)!/((n!)^m m!) π^{mn}; 1.5 products), (1.5.bis) multinomial, (1.5.ter)
n!π^n(x) = x^n; a Λ-algebra with divided powers adds 1.6 π^n(λx) = λ^n π^n(x), margin "N.B. C'est tjs vérifié si
Λ = Z"; a PD structure on an ideal J of A. §2 (5:23-24): Γ*(M) = ⊔ Γ^n(M), π^n extended from M to Γ^+(M) by (x^(p))^(n) =
(pn)!/((p!)^n n!) x^(pn); "On vérifie" 1.1-1.6; M -> Γ^+(M) "joue un rôle universel". §3 (5:24-25): the universal (B,
J) with u: A -> B, u(I) ⊂ J: Γ_A^+(I) modulo (x.y)^(n) - x^n * y^(n) gives J', then the extension A × J'/α(J). 5:26:
Γ(Sym_Λ M, Sym^+_Λ M) ≅ Γ_Λ(M); bracket: the quotient by the ideal K generated by the π^n(x_i), "et pour un idéal K
stable (et pour un tel seulement), les π^n passent au quotient". 5:27: n-truncated PD (x^(i) = 0, i > n), hence x^{n+1}
= 0 and J^{Nn+1} = 0 for N generators; "nilpotent" PD (∀x ∃n); log and exp, "deux isom de groupes inverses l'un de
l'autre" 1 + J ⇄ J.

**Checked.**
- The axioms and 1.5.bis, 1.5.ter: standard and right (Berthelot 1974, I 1; Roby 1965; locators unverified).
- The margin of 5:23 (independent re-proof): for integers k, π^n(kx) = k^n π^n(x) follows from 1.2 and 1.5 by induction
  (π^n((k+1)x) = Σ k^a C(n,a) π^n(x)), π^n(0) = 0, and π^n(-x) = (-1)^n π^n(x) from π^n(x + (-x)) = 0. Right.
- §2: the extension is forced by 1.2 and 1.3 (every element of Γ^+ is a sum of products x_1^(p_1)...x_r^(p_r)), and
  the formula is 1.4. That it is well defined is Roby's theorem (Roby, Bull. Sci. Math. 89, 1965; locator unverified).
  The phrase "application polynomiale homogène de degré p" for x ↦ π^n(x^(p)), M -> Γ^{np}(M): the map has degree np;
  the ink after "degré" is a single small letter, so I leave the reading and note the degree.
- 5:26 (targeted check): Γ_Λ(M) has the universal property of the PD envelope of Sym^+(M) in Sym(M) (PD morphisms
  Γ_Λ(M) -> (B, J) = Λ-linear maps M -> J = algebra maps Sym(M) -> B sending Sym^+ into J). Right. The bracket: the
  ideal generated by the π^n(x_i) is PD-stable (π^m(λπ^n(x)) = λ^m (mn)!/(m!(n!)^m) π^{mn}(x), sums by 1.2), and the
  converse holds. Right (Berthelot I 1.6, locator unverified).
- 5:27: x^{n+1} = (n+1)! x^(n+1) = 0; J^{Nn+1} = 0 by pigeonhole. Right. log/exp (independent re-proof): exp(x+y) =
  exp x · exp y is 1.2; the sums are finite under elementwise nilpotence (for log((1+x)(1+y)) the terms γ_a(x)γ_b(y)
  γ_c(xy) = x^c γ_a(x) γ_b(y) γ_c(y) vanish once a + b + c > N_x + N_y); log∘exp = id and exp∘log = id hold in Z<x>,
  which is torsion-free, hence everywhere.
- §3 (5:24-25): the route through J' = Γ_A^+(I)/((x.y)^(n) - x^n*y^(n)) is the PD envelope in substance, but "On
  constate que les opérations π^n passent au quotient J'" is asserted, not shown; I did not complete a proof on this
  route. The standard route (5:32 below) is proved.

**Wrong.** 5:27, the logarithm: the ink reads log(1+x) = Σ_{n>0} (-1)^n (n-1)! x^(n) (checked at 500 dpi); the sign
must be (-1)^{n-1}. As written the map is -log, still a group isomorphism 1+J -> J but inverse to x ↦ exp(-x), not to
exp; "inverses l'un de l'autre" needs (-1)^{n-1}. (The Pro note flagged the discrepancy; it is in the ink.)

## 5:28-5:31 — §4 the de Rham site, the stratifying site, Leray and the cosimplicial computation (SA15-1)

**What he does.** (X/S)_DR: objects (U, U', i, π), U open in X, i: U -> U' a nilpotent S-immersion, π a truncated PD
structure (for suitable n) on J = Ker(O_U' -> O_U); Zariski topology. The restricted ("stratifying") site: objects
with local retractions U' -> U (not part of the data). Diagram (5:29) Zar(X) ⇢ DRstrat(X) -> Strat(X), DRstrat(X) ->
DR(X), Strat(X) -> Cris(X), DR(X) -> Cris(X): "Si X est formt. lisse sur S, alors les flèches verticales sont des
équivalences de Topos. Si X est de car. 0 ... les flèches horizontales sont des équivalences". Fibre products and
kernels exist in DR(X), DRst(X), "Mais il semble douteux que ce soit le cas pour Cris(X) et Strat(X)". In DRstrat the
object X̃ covers the final object, so a Leray (Čech) spectral sequence E_2^{pq} = H^p(ν ↦ H^q(X̃^{ν+1}, O)); X̃^{ν+1} is
ind-represented by the PD envelopes Δ̃^{(ν)}(i, j) of the infinitesimal neighbourhoods of the diagonal of X^{ν+1},
truncated at j; "H^q(DRst/(U,U'), O) ≅ H^q(U', O_U')" (margin "à vérifier"); for X affine H^q(X̃^{ν+1}, O) = 0 (q > 0),
H^0 = lim_{i,j} H^0(Δ(i,j)), so H^n(X_DRstrat, O) = H^n of the cosimplicial ring ν ↦ H^0 of the completed PD
neighbourhood of the diagonal; in general H^*(X_DRstrat, O) ≅ H^*(X_zar, ℰ^*) for a cosimplicial PD ring ℰ^*.

**Checked.**
- Vertical arrows (targeted check): for X/S formally smooth, every object has locally a retraction (lift U -> X along the
  nilpotent thickening U ⊂ U' on affines; the lift lands in U since U and U' have the same space), so the restricted
  site is the whole site. Right.
- Horizontal arrows: over Q every nilpotent ideal has exactly one PD structure (x^n/n!), truncated as soon as the ideal is
  nilpotent; "X de car. 0" suffices (units lift through nilpotent thickenings). Right.
- Fibre products: in the site of nilpotent thickenings of opens of X, (U_1, T_1) ×_{(U_3, T_3)} (U_2, T_2) is T_1
  ×_{T_3} T_2, a nilpotent thickening of U_1 ∩ U_2 (its ideal is J_1 + J_2, and O_U ⊗_{O_{T_3}} O_U = O_U); with divided
  powers one uses the PD structure of the tensor product (Berthelot 1974, I 1.7, locator unverified); equalizers are
  quotients by the (PD-)ideal generated by f^*a - g^*a. So on the natural reading (Cris(X) = the same site without
  divided powers, Strat(X) its restricted version, both not defined on these sheets) his doubt about Cris(X) and Strat(X)
  is not warranted. With truncated PD the truncation level of the fibre product may grow ("pour n convenable" allows
  that).
- Leray/Čech spectral sequence for the covering X̃ -> e: right (SGA 4 V, locator unverified). Affine vanishing: the
  index set (i, j) is countable and the transition maps between the affine Δ(i, j) are surjective, so lim^1 = 0
  (Mittag-Leffler) and higher lim vanish; with the localization formula this gives his display. The localization
  formula "à vérifier" holds for the crystalline topos (Berthelot 1974, III; locator unverified). The resulting complex
  is what is now called the Čech-Alexander complex (Bhatt-de Jong 2011, locator unverified). His sketch is right.
**Uses:** SA15-14 (PD envelopes, 5:24-26, used on 5:30: "le fourbi augmenté à puissances divisées").

## 5:32-5:35 — the PD envelope by generators and relations; the p-local presentation (SA15-14)

**What he does.** B = A[{Γ^n(x)}_{x ∈ I, n >= 2}]/relations (additivity, Γ^n(xy) = x^n Γ^n(y), products), J generated
by the Γ^n(x); "Il faut introduire sur J des puiss. div ...". For A over Z_(p): with n = Σ a_i p^i, γ^n(x) = C_n Π
γ^{p^i}(x)^{a_i}, C_n = "partie première à p de Π((p^i)!)^{a_i}/n!", so B is generated by the [x, ν] = Γ^{p^ν}(x);
"Quelles sont les relations?"; margins "ne faut-il en passer par les Γ^n(x+y), tous n?" and "On se demande s'il suffit
Γ^{p^ν}(x)^p = (p^{ν+1})!/((p^ν)!)^p Γ^{p^{ν+1}}(x)". For I = (λ) principal (5:33-35): B = A[Γ^n(λ)]/(α: products, α*:
(x^n - y^n)Γ^n(λ) for (x - y)λ = 0), with the derivations of Γ^n(λx) and of additivity from α; p-locally, "Les premières
relations se réduisent, semble-t-il, à" a boxed carry relation, "pour p <= e < 2p-1, donc pour e = p + a (0 <= a <= p-1)".

**Checked (independent re-proofs).**
- The presentation is Roby's presentation of Γ_A(I) with x^[1] identified with x, i.e. D = Γ_A(I)/(x^[1] - x); the PD
  structure descends because 𝔍 ∩ Γ^+ = Σ (x^[1] - x)Γ^+ (an element Σ (x_i^[1] - x_i)a_i with a_i ∈ A lies in Γ^+ only
  if Σ a_i x_i = 0, and then it is 0) and γ_n((x^[1] - x)g) = (x^[1] - x)^n γ_n(g). So the presentation solves the
  universal problem; no iteration relation is needed (Roby). Right.
- C_n: by 1.5.bis Π γ_{p^i}(x)^{a_i} = (n!/Π((p^i)!)^{a_i}) γ_n(x), and v_p of the ratio is 0 (5:11), so C_n = Π((p^i)!)^{a_i}
  /n! is already prime to p and his formula equals it. Right.
- **His two questions answered: yes.** Over Z_(p), Γ_A(M) is presented by generators [x, ν] (ν >= 0, [x, 0] = x^[1]) with
  (a) additivity at p-power indices only, (b) [λx, ν] = λ^{p^ν}[x, ν], (c) the carry relation [x, ν]^p =
  ((p^{ν+1})!/((p^ν)!)^p)[x, ν+1]. Reason: Z_(p)[y_0, y_1, ...]/(y_ν^p - c_ν y_{ν+1}) -> Z_(p)<t>, y_ν ↦ t^[p^ν], is an
  isomorphism (bases correspond up to units), so all product relations hold; after eliminating [x+y, ν] by (a), every
  identity of Roby's presentation is an identity in Z_(p)<s> ⊗ Z_(p)<t> = Γ(Z_(p)^2), where it holds. So "ne faut-il en
  passer par les Γ^n(x+y), tous n?" — no; "s'il suffit Γ^{p^ν}(x)^p = ..." — yes.
- Principal case (5:35): B = A[Γ^n(λ)]/(α, α*) is Γ_A(λA)/(e^[1] - λ), since Γ_A(A/Ann λ) has exactly the relations α and
  α*; right. p-locally the relations α reduce to the carry relation Γ^{p^ν}(λ)^p = c_ν Γ^{p^{ν+1}}(λ), ν >= 0 (the case
  a = 0 of his box; the cases a >= 1 follow on multiplying by Γ^{p^ν}(λ)^a), and α* is needed only for n = p^ν (then
  x^n Γ^n = Π(x^{p^i}Γ^{p^i})^{a_i} = y^n Γ^n). Example: A = Z_(p)[λ] gives Z_(p)<λ>. The box itself is heavily revised
  (exponent "p+a", coefficient struck); its range e = p + a is redundant, not wrong.
**Slips in the ink (checked on 5:32):** the scalar relation is written "Γ^n(xy) - x^n Γ^n(y), x ∈ I, y ∈ A"; it must be
x ∈ A, y ∈ I; the generators are written with "x ∈ J" where I is meant. "ν_p(n)" for v_p(n!) and "ν_p(p^ν)" for
v_p((p^ν)!) (5:32) are his shorthand of 5:11.

## 5:37 — "Lemme de Poincaré vrai" for six local k-algebras, char 0 (SA15-1)

**What he does.** "Lemme de Poincaré vrai pour les k-algèbres suivantes (k corps de car. nulle)": k[[x]][Y]/(Y^p - x^q),
k[[x]][Y]/(Y^2 + P(x)Y + Q(x)), k[x_1..x_n]/(x_i^{p_i}) (e.g. k[x]/(x^p)), k[x,y]/m^2, k[x,y]/(x^3, y^2, x^2 y),
k[x,y]/(x^3, y^2, xy); "Si A local sur k, ext. résiduelle triviale, alors pour tt x ∈ m avec d_{A/k}x = 0, on a x ∈ m^3."
A note hidden in a tikz figure: "Ann. Éc. N. Sc. 65 ou|à 66 ou J. de Liouville" (a reference he meant to look up).

**Checked.** Every algebra in the list is quasi-homogeneous (the second after completing the square, Y'^2 = x^m·unit,
then a change of variable; or Y'^2 = 0), and in characteristic 0 the Euler derivation E gives the contraction
w^{-1}ι_E of the de Rham complex in positive weight, so the Poincaré lemma holds for all six (targeted check; e.g.
k[x]/(x^p): ker d = k and x^{p-2}dx = d(x^{p-1}/(p-1))). The final claim (independent re-proof): in B = A/m^3, choose V
complementary to m_B^2; B = k ⊕ V ⊕ m_B^2 is graded, and ι_E(dx) = x_1 + 2x_2 for x = x_1 + x_2; dx = 0 forces x_1 = x_2 =
0, i.e. x ∈ m^3. Right (needs 2 invertible). Context: by K. Saito (Invent. Math. 14, 1971) an isolated hypersurface
singularity satisfies f ∈ (∂f) iff it is quasi-homogeneous, and the Poincaré lemma fails without it (the Pro note's
test A = Q[x,y]/(f_x, f_y, (x,y)^7), f = x^5 + y^5 + x^3y^3, has df = 0 with f ≠ 0 constant-free). So his examples are
exactly of the kind where the lemma is true; the page states no general criterion.

## 5:38, 5:46, 5:48 — EGA typescript leaves (SA15-12)

5:38: typescript page "-18-" on the reductions in the proof of (6.14.4) "sans utiliser (6.14.1)" and (17.5.7): EGA IV
material (an addendum to IV 6.14, locator unverified). 5:48 and 5:46: typescript pages "IV-977 -22-" and "-23-" (in
that order; the scans reverse them), (18.13.4)-(18.13.5), on the module Ω̄^1_{B/A} of a semi-local noetherian
topological algebra (the quotient of Ω^1_{B/A} by the intersection of the kernels of maps to finite B-modules) — a draft
of EGA IV §18 not in the published text as far as I know (locator unverified). Handwritten corrections and margins,
in a hand like his: 5:48 "à quoi servent ces hypothèses ? Prendre un anneau topologique plus général ?" and "On a donc
Hom_B(Ω̄^1_{B/A}, L) = Hom_B(Ω^1_{B/A}, L) pour tout B-module de type fini L" (right, by the definition of Ω̄^1); 5:46
"style ambigu". On his question: continuity D(r^{j+1}) ⊂ r^j L holds for any ring and ideal; the semi-local noetherian
hypothesis is used for (0, 20.4.5) (canonical topology of Ω^1 = r-preadic) and for the equivalence of the two
descriptions of the kernel intersection (L noetherian). Not studied further.

## 5:39 — the divided powers are determined by π_p (SA15-14)

His hand: when the residue characteristics are p: a) π_{m+n} = C(m+n, n)^{-1} π_m π_n for p | m, 0 <= n <= p-1; b) with
c_n = (pn)!/((n!)^p p!), v_p(c_n) = Σa_i - 1; with d_m = (pm)!/((p!)^m m!), v_p(d_m) = 0, so π_{pm} = d_m^{-1} π_m∘π_p;
"a) et b) ensemble nous montrent que les π_n sont connus quand on connaît π_p". **Checked** (re-proof and computation for
p <= 7): C(m+n, n) ≡ 1 mod p (Lucas); both valuations right; by induction on N = pm + r, π_N is determined by π_p and
π_r = x^r/r!. Right. The "ν_p(m!)" in the first valuation line is a slip for ν_p(n!) (the computation uses n).

## 5:40, 5:42 — a typed course programme (SA15-12)

Pages -4- and -3- of a programme of lectures: N. H. Kuiper, "Variétés Hilbertiennes" (Bessaga, Palais-Smale, Morse
theory, Eells-Elworthy); a course on K-theory, Fredholm operators and Banach categories (citing Séminaire Cartan
1963/64, C. R. t. 263 and t. 267, and Séminaire Bourbaki 1968/69); J. J. Kohn, "Complexes différentiels" (to
complement Kuranishi and Spencer). So 1969 or later; the school is not identified. Not his; not studied.

## 5:41 — can π_p alone define divided powers? (SA15-14)

**What he does.** π = π^p with π(x + y) = πx + πy + Σ_{0<i<p} x^i y^{p-i}/(i!(p-i)!) and π(fx) = f^p πx; "peut-on
définir les π^(n) satisfaisant les conditions (1.1):(1.5), avec π^(p) = π?"; "On va construire π_n(x) = c_n x^{a_0}
π(x)^{a_1} π^2(x)^{a_2} ... π^r(x)^{a_r}" (π^k the k-th iterate, a_i the digits of n), c_n ∈ Q ∩ Z_p^*; "Il serait
intéressant de connaître c_n mod p ... Est-ce tjs 1?" (a struck induction on N above it).

**Checked.**
- c_n = (p!)^{v_p(n!)}/n! (formally π^k(x) = x^{p^k}/(p!)^{(p^k - 1)/(p-1)}, so Π π^k(x)^{a_k} = x^n/(p!)^{v_p(n!)});
  verified by computation for p <= 7, n < 300 (with the iteration coefficient E_{k+1} = E_k^p e_k).
- **His question "Est-ce tjs 1?" — no for p >= 3:** c_n ≡ 1/(a_0! a_1! ... a_r!) mod p (from n!/p^{v_p(n!)} ≡
  (-1)^{v_p(n!)} Π a_i! mod p and Wilson), so c_n ≡ 1 mod p iff every digit is 0 or 1; c_2 = 1/2 for p >= 3. For p = 2
  it is always 1. Verified by computation (p = 2, 3, 5, 7, n < 300).
- His two conditions imply x^p = p! π(x) (independent re-proof): iterating the addition rule gives π(kx) = kπ(x) +
  ((k^p - k)/p!) x^p, and π(kx) = k^p π(x); with k = p+1 (whose Fermat quotient is a unit) the factor k^p - k = p·unit
  cancels to give p! π(x) = x^p.
**Slip in the ink:** the addition rule is written with x^i y^i; it must be x^i y^{p-i} (degree p).
**Open.** The existence (that his π_n satisfy 1.1-1.5 for every such π) is not settled on the page or by me (hunch 2).

## 5:43 — homogeneous polynomial maps and their multihomogeneous parts (SA15-14, toward Γ)

His hand: Φ(Σ t_i x_i) = Σ Φ_{p_1..p_r}(x) t^p defines multihomogeneous φ_{p_1..p_r}: M^r -> N with refinement relations
(margin: "il suffit quand un des argts est remplacé par une somme de deux termes"), "Plus relations de symétrie. On
suppose que l'on a une réciproque ......" (unfinished). **Checked** (targeted): the forward relations follow by
comparing expansions; for the converse (rebuilding Φ, equivalently a linear map Γ^n(M) -> N) one also needs the diagonal
relations φ_{..q,q'..}(..x, x..) = C(q+q', q) φ_{..q+q'..}(..x..), which are the product relations of Γ; they follow
from the listed ones when Φ is a polynomial law (his indeterminates t_i presuppose that) or A is an infinite domain,
not for bare maps over finite rings. With them the converse is Roby's theorem (Roby, Ann. ENS 1963, Thm IV.1; locator
unverified). The "il suffit" margin is right (induction on the number of terms; independence of the splitting order
then follows from associativity of the expansion).

## 5:44 — a typescript leaf on Spin(p, q) and K-theory (SA15-12)

Clifford algebras C^{p,q}, Spin(p,q) -> SO(p,q), Théorème 1.1 (t: K^{V_1+V_2}(X) -> K^{V_2}(B(V_1), S(V_1)) an
isomorphism), spinorial bundles and Banach categories: the style of M. Karoubi, "Algèbres de Clifford et K-théorie",
Ann. Sci. ENS 1968 (identification from content, locator unverified). Not his; not studied.

## 5:45, 5:47 — "Cristaux": divided powers on a principal ideal; the DVR condition e <= p-1 (SA15-14)

**What he does (his hand; heading "Cristaux").** J = πA: formally (πy)^n/n! = (π^n/n!)y^n, so define π^(n) ∈ πA (n >= 1),
π^(1) = π, with α) π^(m)π^(n) = (m+n)!/(m!n!) π^(m+n) and π^(p)(π^(q)/π)^p = (pq)!/(p!(q!)^p) π^(pq) (p, q any
integers here); NB the second is well defined since π^(p) ∈ πA kills the ambiguity of π^(q)/π; then x^(n) = π^(n)y^n
for x = πy is a PD structure. Exemple 1: A torsion-free: π^n = n!π^(n) determines them, "et leur existence équivaut au
fait que π^n ∈ n!A ∀n >= 2"; α) automatic. Exemple 2: A over Z_(p), π = p: the p^n/n! give a canonical PD on pA.
Exemple 3 (5:47): A integral with residue characteristics p and 0; for a DVR, v(π^n/n!) >= 0 for all n iff v(π) >=
e·sup_n v_p(n!)/n = e/(p-1) ("Legendre"), so for a uniformizer: boxed e <= p-1.

**Checked (independent re-proofs).**
- The principal-ideal criterion: with γ_n(πy) = π^(n)y^n, axiom 1.1, 1.3 and the addition axiom (by the first relation)
  hold, and 1.4 is exactly the second relation for (m, n); well-definedness: π^(n)((y+u)^n - y^n) = 0 when πu = 0, as
  π^(n) ∈ πA. Conversely a PD structure gives such π^(n). Right: PD structures on πA = such families.
- **Exemple 1 is incomplete:** the condition must be π^n ∈ n!·πA (i.e. π^n/n! ∈ πA), not π^n ∈ n!A. Counterexample (the
  Pro note's, checked): A = Z ⊕ Zx ⊕ Zy with x^2 = 2y, xy = y^2 = 0, π = x: x^n ∈ n!A for all n, but γ_2(x) would have to
  be y (torsion-free), and y ∉ xA = Zx ⊕ 2Zy, so πA has no PD structure. With π^n ∈ n!πA the relations α) are automatic
  (torsion-free), as he says.
- Exemple 2: v_p(p^n/n!) >= 1 for n >= 1; right.
- Exemple 3: v(N) = e·v_p(N), sup_n v_p(n!)/n = 1/(p-1) (not attained, approached at n = p^k), so the condition is
  v(π) >= e/(p-1), and e <= p-1 for a uniformizer. Right; with 5:13 (e < p-1 for convergence to 0). The letter read
  "r(?)" in "v(π) >= e/(r(?)-1)" is the p of the line above (context; not re-read on the image).
**Readings left:** the faint left-margin marks of 5:45 transcribed "Canson(?)" (Canson is a paper maker; on 5:14 the
same kind of paper shows a watermark) — on the 300 dpi render they are faint and carry nothing legible; I did not decide
whether they are show-through or writing. No mathematics in them.

## 5:49-5:53 — the letter of 10 December 1965 "sur coh. p-adiques" (SA15-20, SA15-15)

**The docket (5:49), decided on the image (500 dpi).** His hand, top right of a blank cover sheet: **"Lettre à Deligne /
sur coh. p-adiques"**. The small mark between "Lettre" and "Deligne", which the Pro transcription drops, is his "à": a
small hook with a dot, written exactly like the "à" of "lieu à des" and "flèches à valeurs" on 5:3. The surname reads
"Deligne" (the final "gne" is quick, as the Pro note says, and the letter itself opens "Cher Deligne").

**Whose letter, and whose hand (decided on the images).** The letter (5:50-53) is a **typescript**, not a manuscript: a
typed copy on thin paper (the next sheet shows through), with typing errors struck over by the typewriter ("gagne", "faisceaux", "beaucoup"), words
typed in above the line with a pen caret ("alg clos", "K", "homo"), blank spaces left for the arrows that were never drawn
("f: X  Y"), and **no signature** after "Bien cordialement". The only handwriting on it is the date "10.12.1965" (top
right of 5:50), a bracket opening at "Je vous propose" (5:50) and closing after "constant Z/nZ." (5:51) — it marks off
the duality part — and the insertion carets. So the question "whose hand" is answered by the form and the content, not
by a script: it is **his own letter to Deligne, the file copy he kept** (an unsigned typed copy with the date added by
hand), and not "another's letter" as sweep 2 recorded. Grounds: (1) the docket in his hand says "Lettre à Deligne";
(2) the letter is addressed "Cher Deligne" and was kept, unsigned, in his papers, as a sender's copy is; (3) the voice:
"Vous vous rappelez qu'on était réduit au cas ...", "Je pense qu'il vaut le coup d'inclure cette forme générale du
théorème de dualité, soit de prime abord, soit à la fin dans un numéro-rattrapage" — directions to the redactor of the
duality exposé of SGA 4 (Deligne's XVIII), from the director of the seminar; "Je crois me rappeler que Tate m'avait dit
..."; (4) the programme (a p-adic analogue of the transcendental comparison, rigid spaces, "la vraie cohomologie
p-adique") is his of 1965-66. The date digits are compatible with his numerals on 5:11 (the flagged 1, the 2), which
is weak evidence; the attribution rests on (1)-(3). Readings decided on the images: "que Tate **m'avait** dit" (not
n'avait) and "la **"vraie"** cohomologie p-adique" (not vcaie) are clearly typed.

### Part 1 (5:50-51): étale duality without relative purity, and general coefficient rings (SA15-20)

**What the letter says.** A simplification of the proof of the duality theorem "qui permet d'éviter tout recours au
théorème de pureté relative": one is reduced to f: X -> Y smooth of relative dimension 1, F = A_X, G = A_Y; by the limit
argument of SGA 4 VI §6 the base can be taken noetherian, even of finite dimension (of finite type over Z); induction on
"n = dim X" (read: dim Y, since the step uses dim(Y - y) < n and the case n = 0 is a point); localize to Y strictly
local with closed point y; "comme on est réduit à prouver le théorème séparément pour X ×_Y (Y - y) et X ×_Y y, on
gagne". Second remark: the theorem holds with the same statement for f: (X, B) -> (Y, A) smooth compactifiable, A any
sheaf of rings killed by an n prime to the residue characteristics, with f^!(K) = RHom_{f^{-1}A}(B, f^{-1}(K) ⊗
T_{X/Y}^{⊗d}[2d]); trace and proof split into the case f^{-1}A ⥲ B (as for Z/n) and the case f = id (trivial); include
it "soit de prime abord, soit à la fin"; it probably does not follow from the Z/n case "comme simple corollaire, mais
ça m'étonnerait"; the same for global duality.

**Worked through.** The step "réduit à prouver le théorème séparément pour X×(Y-y) et X×y" is right, but it needs one
ingredient the letter does not name. Let C be the cone of the map A_X(1)[2] -> f^!A_Y. By induction C vanishes over
Y - y, so C is supported on X_y and C = i_*i^!C (i = i_X: X_y -> X). Now i_X^! f^! = f_y^! i_Y^! (upper shrieks compose),
and i_X^! f^* = f_y^* i_Y^! **by the smooth base change theorem** (SGA 4 XVI 1.1, through the triangle i_*i^! -> id ->
Rj_*j^*; locator unverified). So i^!C is the cone of f_y^*(M)(1)[2] -> f_y^!(M) with M = i_Y^!A_Y, the case n = 0 with
coefficients M. M is a bounded complex because dim Y is finite, which is exactly why he asks for finite dimension. So
relative purity is replaced by smooth base change plus the closed-fibre case with complex coefficients (and the
compatibility of the trace with this base change, which the letter takes for granted). The restriction to X_y is
through i^!, not i^*: with i^* the step would need base change for Rf_* along a closed point, which fails for
non-proper f. The general-coefficients form is formally right (the factorization (X, B) -> (X, f^{-1}A) -> (Y, A) and
RHom_{f^{-1}A}(B, -) as right adjoint of restriction of scalars). Whether SGA 4 XVIII (Deligne, 1973) follows this
route and states the general-coefficient form: not checked (locator unverified).

### Part 2 (5:51-53): p-adic cohomology before crystals (SA15-15)

**What the letter says, and what is true.**
1. The hope: for X over an algebraically closed complete non-archimedean K of characteristic 0 with residue
   characteristic p, a natural Z_p-linear map H^*(X, Z_p) -> H^*_DR(X) with H^*_DR(X) ≅ H^*(X, Z_p) ⊗_{Z_p} K, as over C.
   *Status:* the dimensions agree, but no such natural map exists in general; the comparison needs Fontaine's period
   rings: H_ét(X, Q_p) ⊗ B_dR ≅ H_dR(X) ⊗ B_dR with filtrations and Galois action, for X proper smooth over a
   p-adic field (Faltings 1988-89; Tsuji 1999; for rigid spaces Scholze 2013; locators unverified). His "excès
   d'optimisme" is the right word.
2. "On espère que les arguments habituels prouveront que pour des faisceaux de torsion, la cohomologie de X_ét coïncide
   avec celle de X^an", where X^an is Tate's rigid space with its G-topology ("un site qui ne peut être défini par une
   topologie au sens ordinaire"). *Status:* true for the **étale** site of the analytic space (Berkovich 1993; Huber
   1996; prime-to-p and, for proper X, p-torsion coefficients; locators unverified), false for the G-topology itself,
   which is too coarse: H^1 of a smooth projective curve with constant coefficients in the G-topology is the H^1 of its
   reduction graph (skeleton), 0 for good reduction and of rank 1 for a Tate curve, not rank 2.
3. The hope that H(X^an, Z_p) = lim H(X^an, Z/p^n) = H(X_ét, Z_p), then Z_p -> constants -> de Rham, with rigid GAGA
   (Kiehl 1967, locator unverified) identifying analytic and algebraic de Rham cohomology. The "excès" would be justified
   by a rigid Poincaré lemma: the de Rham complex of X^an resolves the constants. "certainement trivial pour l'analytique
   p-adique ordinaire ... mais ... pour la topologie rigide-analytique (beaucoup plus grossière) est plus délicate";
   "j'ai de grands doutes ... que la cohomologie rigide-analytique à coefficients constants tout bêtes donne les "bons"
   nombres de Betti". *Status:* his doubts are right. The rigid Poincaré lemma fails on affinoids (on the closed disc a
   convergent Σ a_n x^n need not have a convergent primitive, because of the 1/(n+1)), which is why Monsky-Washnitzer
   use overconvergent functions and Berthelot's rigid cohomology overconvergent de Rham complexes; the germ-level lemma
   ("analytique p-adique ordinaire") is true.
4. "Je crois me rappeler que Tate m'avait dit que c'était déjà faux pour le H^1 des courbes elliptiques ...
   apparemment, on trouverait un peu plus que pour la cohomologie étale, mais quand même pas toute la cohomologie."
   *Status:* the recollection is right in substance (constant-coefficient G-cohomology gives rank 0 or 1 for H^1 of an
   elliptic curve, never 2); "un peu plus que pour la cohomologie étale" makes sense only as "more than Zariski
   cohomology (0)" — as typed it reads oddly; I record it as said.
5. "Il reste plausible ... que la topologie rigide-analytique aura son rôle à jouer": borne out (rigid cohomology;
   p-adic Hodge theory on the pro-étale site of rigid spaces).
6. Characteristic p (5:52-53): "un homomorphisme évident de H^*(X, F_p) dans la cohomologie de De-Rham", computing de
   Rham cohomology étale-locally (the same result, the terms being quasi-coherent) and using the spectral sequence
   H^p(X, H^q(Ω)) => H^*(X); it factors through H^*(X, F_p) -> H^*(X, O_X), which maps to H^*(X) by f ↦ f^p,
   "induisant un isomorphisme O_X ≅ H^0(Ω)"; and the composite H^n(X, O_X) -> H^n(X) -> H^n(X, O_X) "ne peut guère être
   autre chose que l'homomorphisme de Frobenius". *Checked* (independent re-proof): at the level of complexes O_X[0]
   -(f ↦ f^p)-> Ω^• -> O_X[0] composes to f ↦ f^p, since d(f^p) = 0; so the composite is the p-linear Frobenius of
   H^n(X, O_X) — this is exactly Lemma 8.4.3 of cote 4 (F_DR = βα, F_O = αβ; sweep 3 STUDY §1, SA15-9). The
   identification F: O_X ⥲ H^0(Ω^•) needs X smooth over a perfect field (Cartier); it fails for non-reduced X (the
   Pro note's test X = Spec F_p[ε]/(ε^2)). "Il faut dire que tout ça est bien éculé, et qu'on ne pourra dire des choses
   vraiment intéressantes et nouvelles qu'en faisant appel à la "vraie" cohomologie p-adique" — the crystalline
   cohomology he found the next year.

**Place.** The earliest dated piece of the SA15 dossier (10 Dec 1965), a year before the crystalline site (the letter
of 1966 to Tate, the 1966 IHES lectures written up by Coates and Jussila; dates from the literature, locators
unverified). It sits with 5:3 (the topoi with and without divided powers) and 5:37 (Poincaré lemmas for Artinian
algebras).

---

## Hunches (mine; none is a statement of the pages)

**H1. The divided-power sheets of cote 5 are his reading-in to divided powers after the failure of the infinitesimal
Dieudonné crystal (6:27, §2.7), and W^(ν) is his test object for it.**
Grounds: 5:5 builds the universal Artinian ring with ν-nilpotent divided powers, the condition under which the later
theory works (nilpotent PD thickenings: Messing 1972, Berthelot 1974); 5:13 and 5:47 find e <= p-1 (PD) and e < p-1
(nilpotent PD), the ramification bounds of that theory; 5:45 is headed "Cristaux"; 5:21 "Th de De Rham (à puissances
divisées)". Links: SA15-16 (6:22-27), SA15-1. Dating the sheets against 6:27 and the 1966 lectures would settle it.

**H2. The answer to his existence question of 5:41 is yes: for a Z_(p)-algebra A and an ideal I, the PD structures on I
are exactly the maps π: I -> I with π(fx) = f^p π(x) and π(x+y) = π(x) + π(y) + Σ_{0<i<p} x^i y^{p-i}/(i!(p-i)!).**
Grounds: these conditions force x^p = p!π(x) (proved above with k = p+1); the π_n are then forced (5:39); in the
monogenic free case Z_(p)[x, π(x), π^2(x), ...]/(π^k(x)^p - p! π^{k+1}(x)) is Z_(p)<x> (the bases correspond, as in
5:5), so every PD identity holds there; what is missing is that identities involving several elements follow from the
two rules alone. I have not found this statement in the literature (search not done).

**H3. The topos L(α, β) of 5:16-20 is the coinserter (lax coequalizer) of α, β in the 2-category of topoi; with
β = id and α a Frobenius it is the topos of F-objects, and his comparison problem (5:19) has a positive answer there.**
Grounds: the universal property of 5:17-18 is the coinserter's; the case β = id is proved above. Link: SA15-2 (the
F-crystals of cote 8), and the Weil-sheaf formalism of SGA 7 / Weil II, where a sheaf with Frobenius structure is
exactly such a pair.

**H4. The list of 5:37 is a list of quasi-homogeneous singularities, and "dx = 0 ⇒ x ∈ m^3" is the first step of the
Euler-field proof; the reference "Ann. Éc. N. Sc. 65 ou 66 / J. de Liouville" is to a paper on the de Rham complex of
singular spaces.**
Grounds: every listed algebra is quasi-homogeneous (checked), and the true criterion for isolated hypersurface
singularities is quasi-homogeneity (K. Saito 1971); 1965-66 fits Reiffen's and Brieskorn's work on the holomorphic
Poincaré lemma, but I have not identified the paper. Link: SA15-1 (the analytic comparison and its Poincaré lemma,
cote 7) and the rigid Poincaré lemma of the letter (5:52).

**H5. The duality argument of the letter (5:50) is the one that reached SGA 4 XVIII.**
Grounds: it avoids relative purity at the cost of smooth base change and finite dimension of the base, and Deligne
wrote XVIII after December 1965; the general-coefficient remark matches the generality of XVIII as I remember it.
To be checked against SGA 4 XVIII 3.2 (not opened).

**H6. The letter's characteristic-p remark (5:52-53) is the seed of Lemma 8.4.3 of cote 4 (SA15-9).**
Grounds: the letter states that H^n(X, O_X) -> H^n_DR -> H^n(X, O_X) is Frobenius; cote 4 (8.4.3) uses exactly
F_DR = βα and F_O = αβ to compare semisimple parts. Cote 4 does not cite the letter.

**H7. The EGA typescript leaves with Ω̄^1 (5:46, 5:48) are a cut draft of EGA IV §18 on "analytic" differentials, and
his margin "Prendre un anneau topologique plus général ?" is why the section was cut or rewritten.**
Grounds: numbering (18.13.4)-(18.13.5) and "IV-977"; the published §18 does not contain this material as far as I
remember (not checked).

## Dependencies (ids of sweep2/SA15/WHAT_IS_WHERE.md)

| Piece | Uses | Basis |
|---|---|---|
| 5:3 (SA15-1) | SA15-14 (the ℙ = divided-power topoi; the log for the Chern class) | his page (5:3), proof |
| 5:5-9 (SA15-14) | 5:11 (valuations of factorials) | his page (5:6, 5:7 use v_p(c_i) = 1, v_p(λ_ν)) |
| 5:13, 5:47 (SA15-14) | 5:11 | his page (5:13 uses v_p(n!) = (n - chif n)/(p-1); 5:47 "Legendre") |
| 5:15-20 (SA15-2) | SGA 4 I §9, SGA 4 V | his page |
| 5:28-31 (SA15-1) | SA15-14 (PD envelopes 5:24-26, truncated PD 5:27) | his page (5:28 "puissances divisées tronquées", 5:30 "fourbi augmenté à puissances divisées") |
| 5:32-35 (SA15-14) | 5:11, 5:22-23 (axioms 1.2-1.5) | his page (5:32 "comme plus haut", the NB on v_p) |
| 5:39, 5:41 (SA15-14) | 5:22 (axioms 1.1-1.5), 5:11 | his page (5:41 "(1.1):(1.5)") |
| 5:43 (SA15-14) | 5:23-24 (Γ(M)) | our note (the polynomial maps are the universal property of Γ^n) |
| 5:50-51 (SA15-20) | SGA 4 VI §6 (his page); SGA 4 XVI 1.1 smooth base change (proof) | his page, proof |
| 5:52-53 (SA15-15) | — ; used by SA15-9 (4:5-6, Lemma 8.4.3) | proof (same mathematics) |
| SA15-14 as a whole | used by SA15-16 (nilpotent PD thickenings, 6:27) and SA15-1 | proof, our note |

## Deliverable state of the stretch (cote 5, scans 1, 3-53)

- **Passes:** the Pro transcription and notes (package `MPL_5+6_001-037`, frozen 12 Nov 2026); no Codex web return and no
  Work notes exist for cotes 5-6; sweep 2 placement; this sweep 3 reading (all 52 scans, the mathematics worked through,
  images consulted on 5:3, 5:4, 5:6, 5:9, 5:11, 5:12, 5:13, 5:14, 5:15, 5:17-19, 5:23, 5:27, 5:32, 5:35, 5:41, 5:45,
  5:48, 5:49-53).
- **Readings decided here:** 5:3 "zariskienne" (not gerbienne|galoisienne); 5:6 the sum runs to p; 5:49 "Lettre à
  Deligne" (the "à" was dropped); 5:52 "m'avait"; 5:53 "vraie". The 5:3 margin and the 5:13 boxes are in the .tex (in
  tikz figures that the reader tool hides).
- **Readings still open:** 5:15 the end of "Frobeniuseries"; 5:13 the line "chif(n) <= 1"; 5:23 "de degré p" (np?);
  5:35 the heavily revised box; 5:45 the faint "Canson(?)" margin marks; 5:47 "r(?)" (p by context, not re-read on the
  image); 5:21 Th|Alg.
- **Mathematical state:** everything he states on the divided-power sheets is right except the sign of log (5:27) and the
  criterion of Exemple 1 (5:45); his own open questions answered here: 5:33 (yes), 5:35 (the box is redundant), 5:41
  "Est-ce tjs 1?" (no for p >= 3), 5:18 "à vérifier" (yes), 5:30 "à vérifier" (yes, known); open: 5:41 existence (H2),
  5:19-20 the general sufficient condition, 5:3 "détermination des points de ces topos ?".
- **Ready for a transcription edition:** yes for his handwritten sheets once the readings above are applied; the reused
  leaves (5:4 Serre-Tate; 5:10, 5:12, 5:34, 5:36 Néron; 5:38, 5:46, 5:48 EGA; 5:40, 5:42 a course programme; 5:44
  Clifford/K-theory) need only the identification lines and, on 5:46/5:48, his margins; the letter (5:50-53) is a typed
  file copy, faithfully transcribed with its typing errors, and its authorship line should read "Grothendieck to
  Deligne, 10 Dec 1965 (unsigned typed copy; docket in his hand)".
- **Changes to sweep 2's records proposed:** SA15-15 and SA15-20 status "another's letter" -> his letter to Deligne (file
  copy); SA15-14 status refined (see CORRECTIONS); 5:4 is a typescript leaf with nothing of his.
- **Not consulted in this stretch:** Michel Hua's project (transcripts/5/5.modern.tex) as a witness, and the SGA 4,
  Berthelot, Roby and Saito texts cited above (all locators marked unverified); the context budget went to the pages,
  the images and the computations.

Counts: 52 scans read (1, 3-53); 48 check events; 19 corrections; 7 hunches.
