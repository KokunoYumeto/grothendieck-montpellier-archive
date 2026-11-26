# Connection map, region GALOIS_ANABELIAN: Galois theory, anabelian geometry, Grothendieck–Teichmüller, Ihara, Vandiver

Written 24 Nov 2026 (about 21:45–22:30 UTC) by Claude Opus 5.5 at effort max, launched by the main session 329fb1e6
(Claude Opus 5.5 at effort max), following `MAP_BRIEF.md`. Work file:
`<local>/Documents\agent_notes\20261124T2142Z_Connection_map_Galois_and_anabelian_NOTES.md`. Row table:
`MAP_GALOIS_ANABELIAN.tsv`; my checks: `MAP_GALOIS_ANABELIAN_CHECK_EVENTS.tsv` (both in this folder). Scripts and their
outputs: `MAP_GALOIS_ANABELIAN_scripts\` in this folder (`c34_an.py`, `checks_su_irr.py`, standard library only).

**Region.** LONGUE_MARCHE_A and LONGUE_MARCHE_B (all twenty runs), ALPOGE's C.IHARA and the K-group items (C.K12/K80,
BD-K01), the Galois items of SWEEP3_A/B (SA05/SA06 gerbes, SA07 F.3.32, SA09 dessins, SA12 Iwasawa, SA14 F11, SA22
anabelian rows), and the outside results on anabelian geometry, Grothendieck–Teichmüller (GT), Chabauty–Kim, Ihara's
question and Vandiver's conjecture.

**Conventions.** Every run named is GPT-6 Astra (ChatGPT Pro mode) unless said otherwise. "Proof given here" means I wrote
the proof in this file; no second reader has checked it. Outside sources were opened at the statement where I say
"opened"; otherwise the locator is the run's or another intake's. GT̂ is Drinfeld's profinite group (relations I, II,
III), GT̂₀ the gentle group of Harbater–Schneps (I and II only), Λ₀ ⊂ GT̂ the normalized elements (λ = 1, ρ₂ = 0) of the
H17 note, K₂ = Q(μ_∞, 2^{1/∞}). U = P¹ ∖ {0,1,∞}. A = Alpöge's theorem (RH for Dirichlet L-functions).

---

## 1. The new knowledge, ranked by usefulness

### N1. GT̂ is the group of inertia-preserving outer automorphisms of every generic procongruence mapping class group; Lochak's chain collapses (H17 Theorem 1 + Lochak 2025, Theorem 5.10)

**Statement.** Let S be a surface of type (g, n) with g ≥ 1, 3g − 3 + n > 2, (g, n) ≠ (2, 0) ("generic type"), Γ̌(S)
the procongruence completion of the mapping class group Γ_{g,[n]}, and Č(S) its procongruence curve complex. Then
(a) in Lochak's notation, IΓs = IΓ = GT̂: every compatible pair (F₀, F₁) has F₀ = F₁, and every F ∈ GT̂ is F₀ of a
compatible pair; (b) Out*(Γ̌(S)) = Out(Č(S)) ≅ GT̂, where Out* is the group of inertia-preserving outer automorphisms;
every inertia-preserving automorphism of Γ̌(S) is of strict lego type (commutes with the elliptic involution);
(c) for every open normal subgroup Γ̌_λ there is a split exact sequence 1 → Γ(S)/Γ_λ → Out*(Γ̌_λ) → GT̂_λ → 1 with
GT̂_λ open in GT̂. For g ≤ 2 the procongruence completion is the profinite one (Asada, Boggi; not reopened here).

**Proof given here.** Lochak, *Automorphisms of profinite and procongruence curve complexes and the
Grothendieck–Teichmüller group*, Algebra i Analiz 37 (2025), no. 2 (author PDF `webusers.imj-prg.fr/~pierre.lochak/textes/
automorphisms.pdf`, opened and text-extracted), defines (Definition 5.4) F₀ = (λ₀, f₀), F₁ = (λ₁, f₁) ∈ GT̂ to be a
compatible pair if λ₀ = λ₁ and f₁(σ₁², σ₂²) = σ₂^{2a} f₀(σ₁, σ₂⁴) σ₁^{2b} (σ₁σ₂²)^{2c} in B̂₃ for some a, b, c ∈ Ẑ (5.1);
the pairs form a group IΓ ⊂ GT̂ via F₀, and F₁ is determined by F₀ (Proposition–Definition 5.6). IΓs ⊂ IΓ is the
subgroup with F₀ = F₁, equivalently the F satisfying (IV*): f(σ₁², σ₂²) = σ₂^{−8ρ} f(σ₁, σ₂⁴) σ₁^{−4ρ} (σ₁σ₂²)^{4ρ},
ρ = ρ₂(F) (text after Definition 5.8; Proposition 5.9). Theorem 5.10 (author PDF p. 60, read with PyMuPDF to keep the
asterisks): for S generic, Aut*(Γ̌(S)) = Aut(Č(S)), Out*(Γ̌(S)) = Out(Č(S)) = IΓ, every automorphism is of lego type,
and (iii)–(iv) on open subgroups. The H17 note (hexagon:2611.00940, Theorem 1) proves (IV) for every F ∈ GT̂ in the form
f(u, v⁴) = v^{8ρ₂} f(u², v²) u^{4ρ₂} (uv)^{−6ρ₂} in B̂₃. The two forms agree: in B₃, (uv²)² = uv·(vuv)·v = uv·(uvu)·v
= (uv)³, which is central, so Lochak's (IV*) rearranges to f(σ₁, σ₂⁴) = σ₂^{8ρ} f(σ₁², σ₂²) σ₁^{4ρ} (σ₁σ₂)^{−6ρ}, which is
H17's (IV) with u = σ₁, v = σ₂; both take ρ₂ from Nakamura–Schneps §5 (Furusho's survey, RIMS Kôkyûroku 1267 (2002),
pp. 190–191, opened, writes the same (IV) with Ψ₂⁽⁰⁾ = −ρ₂). Hence every F ∈ GT̂ satisfies (5.1) with f₀ = f₁ = f,
a = −4ρ, b = −2ρ, c = 2ρ: (F, F) ∈ IΓ, so IΓ = GT̂, and since F₁ is determined by F₀, IΓs = IΓ. Theorem 5.10 then gives
(b) and (c). ∎

**Status and gates.** The proof above is mine and short; its two inputs are H17 Theorem 1 (checked step by step by Claude
Fable 5.2 at effort max, 18 Nov; second reader Claude Opus 5.5 at effort max; the same theorem is EXIT_TOWER E.44, 16 Nov,
by the same Boggi–Zalesskii method) and Lochak's published Theorem 5.10 (statement read, proof not checked). Two gates:
(1) Lochak's proof uses Boggi–Funar, *Automorphisms of procongruence curve and pants complexes*, J. Topology 16 (2023)
(his [3], Theorems 5.3, 6.4); EXIT_TOWER E.14 says that Lemma 2.23 of "BF2026" (a 2026 version of a Boggi–Funar text)
is false as printed while the main theorems stand. Someone must check that Lochak's uses of [3] avoid that lemma.
(2) To close EXIT_TOWER E.45 one must check that EXIT_TOWER's map r_{g,n} (E.230) is Lochak's lego action; both are
determined by the actions on (0,4)- and (1,1)-pieces, so this is expected.

**What it changes.**
- It answers the three questions Lochak asks in the closing remarks of the same paper (author PDF pp. 61–62): whether
  IΓs = IΓ ("if (F₀, F₁) is a compatible pair … then in fact F₀ = F₁"), whether IΓ = GT̂ ("it would mean that 'everything'
  already happens in genus 0"), and whether "relation (IV) is actually redundant", which "would then reduce everything to
  pentagons, including in higher genus". All three: yes. Neither the H17 note nor the topicality pass
  (`TOPICALITY_LONGUE_MARCHE.md`) cites this paper.
- EXIT_TOWER E.45 (is GT̂ → Out^{I₀}(Γ̌_{g,[n]}) onto, g ≥ 3?) is settled for Out* ⊂ Out^{I₀}; what remains is whether an
  automorphism preserving the nonseparating twist class preserves all twist classes (a weak form of Lochak's "remove the
  star" question). This is an independent route to the Out*-part of Boggi's claim (arXiv:2011.15075v6, Out^{I₀}(PΓ̌(S)) ≅
  Σ_n × GT̂ for χ(S) < g − 2), whose Proposition 6.9 and Lemma 6.16 EXIT_TOWER E.14 says are false as printed.
- H17's open question 2 (does Λ₀·G_Q act on the tower as one group, [LNS §8]): for each generic S, GT̂ = Out*(Γ̌(S))
  acts as one group. Compatibility with forgetting points and subsurface inclusions is not part of Theorem 5.10 and
  stays open.

**A point to settle at the source (possibly larger).** Lochak writes (p. 61): "Note that IΓs is contained in the group
denoted by IΓ in [30]", [30] being Nakamura–Schneps 2000, whose group is cut out by (III′) and (IV) (Furusho 2002,
p. 190: (III′) is g(x₄₅, x₅₁) f(x₁₂, x₂₃) f(x₃₄, x₄₅) = f(σ₁σ₃, σ₂²) in B̂₅, and it implies (III)). Read literally,
with IΓs = GT̂ this would give (III′) on all of GT̂, hence Nakamura–Schneps's IΓ = GT̂, the question the H17 note lists
as open (its §"What remains open", item 1). Either the sentence means "contains", or the lego construction forces
(III′). Nakamura–Schneps §6 and Lochak §5 must be read before anything is said.

**Why it matters.** It identifies, for every generic type in positive genus, the inertia-preserving outer
automorphism group of the procongruence mapping class group with GT̂ itself, by a route independent of Boggi's v6
(whose claim covers χ(S) < g − 2 and two of whose steps EXIT_TOWER E.14 disputes). It is Grothendieck's two-level
principle of the *Esquisse d'un programme* (§2: the tower is governed by modular dimension ≤ 2) realized for
automorphisms: the genus-zero relations (pentagon) suffice, the genus-one relation (IV) being automatic. Paper
candidate: v2 of the H17 note (see §4, P1).

### N2. Tripod sections over Q integral at every odd prime are the three points −1, 2, 1/2; the recognition step of SECTIONS_OVER_Q reduced to potentially multiplicative cusp places

**Statement (Proposition L).** Let s be a noncuspidal Selmer section of U/Q (local restrictions point or cuspidal, real
convention as in SECTIONS_OVER_Q) in the class of SECTIONS_OVER_Q A.14: its local points are integral, x_p ∈ U(Z_p), for
every prime p outside a finite set S (2 ∈ S always, since U(Z₂) = ∅). Let λ₀ ∈ Q ∖ {0,1} be its integral Legendre
parameter (A.16). Then:
(a) λ₀ ∈ U(Z[S⁻¹]): λ₀ and 1 − λ₀ are S-units. The set is finite and effectively computable; for S = {2} it is
{−1, 2, 1/2} (all three give j = 1728, the curve y² = x³ − x), for S = {2, 3} it has 21 elements with
j ∈ {1728, 35152/9, 1556068/81, 21952/9} (`checks_su_irr.py`).
(b) At every prime p where s is locally cuspidal, E_{λ₀} has potentially multiplicative reduction (v_p(j(λ₀)) < 0) and
the local extension of s at p is non-split, with ramified Kummer class.
(c) If v_p(j(λ₀)) ≥ 0 for every p ∈ S, then s is the section of the rational point λ₀.
In particular (S = {2}): every noncuspidal Selmer section of U/Q whose local points are p-adically integral at every
odd prime is the section of −1, 2 or 1/2.

**Proof given here.** (a) For odd p ∉ S, x_p ∈ U(Z_p), so E_{x_p}: y² = x(x−1)(x−x_p) has good reduction at p and
L_{s,ℓ} = T_ℓ(E_{x_p}) is unramified at p for ℓ ≠ p. By A.16, T_ℓ(E_{λ₀}) ≅ L_{s,ℓ} as G_Q-modules for every ℓ, so
E_{λ₀} has good reduction at p (Néron–Ogg–Šafarevič), so v_p(j(λ₀)) ≥ 0 with j(λ) = 256(λ² − λ + 1)³/(λ²(1−λ)²); for odd
p this holds iff λ, 1 − λ are p-units (if v_p(λ) > 0 or v_p(1−λ) > 0 the denominator wins; if v_p(λ) < 0 then
v_p(j) = 2v_p(λ) < 0; checked on 20,000 random λ for p ≤ 13, no mismatch). (b) A cuspidal local section gives
L_{s,ℓ}|G_{Q_p} ≅ δ ⊗ (extension of Z_ℓ by Z_ℓ(1)) with δ quadratic (A.14's proof). If the extension class is unramified,
the representation is potentially unramified with Frobenius weights 0 and 2; V_ℓ(E_{λ₀})|G_{Q_p} is either potentially
good (weights 1, 1) or potentially multiplicative (infinite inertia image); neither matches. So the class is ramified,
the local representation has infinite inertia image, and E_{λ₀} is potentially multiplicative at p. (c) Under the
hypothesis, (b) leaves no cuspidal place; outside S the local sections are integral points and inside S they are
points. So s is an adelic section in Stix's sense; Stix, Invent. Math. 199 (2015), Corollary 6 (opened: for k = Q and
X with a nonconstant unit, X(k) = adelic sections) makes s = s_a for some a ∈ U(Q); the Legendre comparison of A.16
(level-two structures, Faltings) gives a = λ₀. For S = {2}: j = 1728 has v₂ = 6 ≥ 0, so (c) applies. ∎

**Status.** Conditional on SECTIONS_OVER_Q A.14 and A.16 (run results; A.14 uses Pan 2022 Theorem 1.0.4 and Helm–Voloch
2011 Proposition 6, opened by no one on our side; A.16's key step checked by the LONGUE_MARCHE_B reader). The S = {2}
case also follows from Betts–Kumpitsch–Lüdtke (arXiv:2305.09462v2, 11 Apr 2026, Theorem C, opened) and from Stix's
Corollary 6 *when the local section at 2 is a point*; the new input is (b), which excludes a cuspidal local section at
2. The run itself already cites Stix's Corollary 6 (`sections/birational_agent.tex` l. 23–34) and localized A.24 to the
locally cuspidal places; (a) and (b) sharpen that localization to "cusp places where E_{λ₀} is potentially
multiplicative, with matching ramified Kummer data", and (c) closes everything else.

**Why it matters.** SECTIONS_OVER_Q A.24 (recognition) is the one missing step of the Legendre route to Grothendieck's
Conjecture A for the tripod (cote 149, scan 56). This shows that what is left concerns only cusp-local behaviour at the
finitely many primes where λ₀ is p-adically close to a cusp, and that it is a finite problem for each S. Together with
SECTION_GHOSTS (ghosts have infinite support, so they lie outside the A.14 class), it says that inside the finitely
ramified class the only obstruction is a cuspidal one.

### N3. The fixed-ramification obstruction in the pro-ℓ section tower is a K-group of Z; SECTION_GHOSTS E.209 extended to every prime

**Statement.** Let ℓ be odd, S = {ℓ, ∞}, K = Q(μ_ℓ), A = Cl(K)[ℓ^∞] with its eigenspaces A(ω^i). For every w ∈ Z,
H²(G_{Q,S}, F_ℓ(w)) ≅ (A/ℓA)(ω^{1−w}); hence H²(G_{Q,S}, Z/ℓⁿ(w)) = 0 for all n iff A(ω^{1−w}) = 0, and for w ≥ 2,
H²(G_{Q,S}, Z_ℓ(w)) ≅ K_{2w−2}(Z) ⊗ Z_ℓ. Consequently the SECTION_GHOSTS obstruction to lifting a boundary-matched
class-r section of the pro-ℓ tripod tower to class r + 1, which B.25 places in H²_cts(G_{Q,S}, Z_ℓ(r+1))^{b_{r+1}}, lies
in (K_{2r}(Z) ⊗ Z_ℓ)^{b_{r+1}}, and it vanishes unless
- r is odd and ℓ divides B_k for the even k ∈ [2, ℓ − 3] with k ≡ r + 1 (mod ℓ − 1) (an irregular pair; Herbrand–Ribet),
- or r is even and the Vandiver eigenspace A(ω^{−r}) is nonzero, which does not happen for ℓ < 2³¹ (Hart–Harvey–Ong 2017)
  nor, for any ℓ, when r ≡ 2m (mod ℓ − 1) with 1 ≤ m ≤ 20 (K_{4m}(Z) = 0, NIGHT_AFTER_ALPOGE C.K12/K80, Alpöge's
  archive; m ≤ 30 by Mok–Zheng, hexagon:2611.00998, unrefereed).
For ℓ < 200 the possibly obstructed classes are r ≡ 31 (ℓ = 37), 43 (59), 57 (67), 67 (101), 23 (103), 21 (131),
129 (149), 61 and 109 (157) modulo ℓ − 1; for ℓ = 691, r ≡ 11 and 199 (K₂₂(Z) ≅ Z/691).

**Proof given here.** With S_K = {(1 − ζ)} ∪ {complex places}, the Kummer sequence on O_{K,S_K} gives
0 → Pic(O_{K,S_K})/ℓ → H²(G_{K,S_K}, μ_ℓ) → Br(O_{K,S_K})[ℓ] → 0 (Milne, ADT II.2). Br(O_{K,S_K})[ℓ] is the kernel of the
sum of invariants on the single finite place of S_K, so 0; (1 − ζ) is principal, so Pic(O_{K,S_K}) = Cl(K). As
G_{K,S_K} acts trivially on μ_ℓ^{⊗(w−1)} and [G_{Q,S} : G_{K,S_K}] = ℓ − 1 is prime to ℓ,
H²(G_{Q,S}, F_ℓ(w)) = (A/ℓ ⊗ ω^{w−1})^Δ = (A/ℓ)(ω^{1−w}). Since cd_ℓ G_{Q,S} = 2, H²(Z_ℓ(w))/ℓ = H²(F_ℓ(w)), and Nakayama
gives the integral statement; for w ≥ 2 the K-theory identification is Quillen–Lichtenbaum (Rost–Voevodsky; Soulé;
Kurihara 1992). The two bullet points are Herbrand–Ribet plus Mazur–Wiles for odd characters and Kurihara for even ones.
The list of irregular pairs ℓ < 200 is from my Bernoulli computation (`checks_su_irr.py`). ∎ For regular ℓ this is
E.209.1 (re-proved this way; the topicality pass marks E.209 as known in substance, correctly).

**Why it matters.** (FS)_nil (SECTION_GHOSTS A.2) concerns the full pronilpotent tower, i.e. all ℓ at once, while E.209
covered only regular ℓ. Now the fixed-ramification obstruction is zero at every ℓ except at explicit weights
r ≡ k − 1 (mod ℓ − 1), (ℓ, k) irregular, so the only all-depth obstruction is support matching (B.26) away from those
weights, and at those weights the obstruction group is an explicit cyclic Bernoulli group. In Grothendieck's terms the
weight-(r+1) graded piece of the tripod π₁ carries the Tate motive Q(r+1), and the obstruction is
Ext² of Tate motives over Z[1/ℓ], i.e. K_{2r}(Z). The same eigenspaces govern C.IHARA (only the even ones, through X⁺)
and the K_{4m}(Z) results (§3.D).

### N4. The question G_Q = GT̂ in the frame of Hatcher–Lochak–Schneps, and the "abelian tests" of the gentle group

**Statement.** (a) GT̂ = G_Q iff Λ₀ = G_{K₂} inside GT̂ (K₂ = Q(μ_∞, 2^{1/∞})); more precisely the coset spaces GT̂/G_Q and
Λ₀/G_{K₂} are in bijection, and Λ₀ is normal with GT̂/Λ₀ ≅ Gal(K₂/Q). (b) The decomposition holds in the gentle group:
GT̂₀ = Λ₀(GT̂₀)·G_Q with Λ₀(GT̂₀) = {F ∈ GT̂₀ : λ = 1, ρ₂ = 0}. (c) A continuous homomorphism from GT̂₀ (or GT̂) that is
trivial on G_Q is determined by its restriction to Λ₀(GT̂₀); it vanishes on GT̂ iff it vanishes on Λ₀. (d) If G_Q = GT̂
then GT̂^{ab} ≅ Ẑ^× through λ; and GT̂^{ab} ≅ Ẑ^× iff Λ₀ lies in the closed commutator subgroup of GT̂.

**Proof given here.** (b) H17 Lemma 5(c) (λ = 1 ⇒ ρ₂ ∈ 2Ẑ) uses only relation (II) and the frame of Lemma 4, both
available on GT̂₀; I re-derived it in the class-two quotient (f = [x, y]^e and (II) at λ = 1 give [x, y]^{3e} = 1, so f = 1
there; g = x^ρ y^ρ [x,y]^d gives g(y,x)⁻¹g(x,y) = [x,y]^{ρ²+2d}, so ρ² ∈ 2Ẑ, so ρ ∈ 2Ẑ). Given F, pick σ ∈ G_Q with
χ(σ) = λ_F, then τ ∈ G_{Q^ab} with κ₂(τ) = ρ₂(Fσ⁻¹) ∈ 2Ẑ = κ₂(G_{Q^ab}) (H17 §5); Fσ⁻¹τ⁻¹ is normalized by the cocycle
rule ρ₂(FG) = ρ₂(F) + λ_F ρ₂(G). (a) G_Q ∩ Λ₀ = {χ = 1, κ₂ = 0} = G_{K₂}; with GT̂ = Λ₀G_Q (H17 Theorem 2) the map
Λ₀/G_{K₂} → GT̂/G_Q is a bijection; normality and the quotient are GALOIS_GT §1.1 (ae4ae3dc, 23 Nov). (c) is immediate
from (b). (d) ker λ ∩ GT̂ = Λ₀·G_{Q^ab} and G_{Q^ab} = [G_Q, G_Q]‾ ⊂ [GT̂, GT̂]‾; a character of GT̂ not factoring through λ
gives, after subtracting θ∘λ, a nonzero character trivial on G_Q. ∎

**What it does to our items.** Every Galois-trivial character our runs built on GT̂₀ is an abelian test of G_Q = GT̂:
Δ (LM7_PUSH E.65), ε₅, ε₇, ε₁₃ (LM8_PUSH C.33, C.39), the ℵ₀ quadratic family (LM8_PUSH C.30 = GT_TOWER_CHECK B.2.25),
Δ_D, Δ_D² (C.31), and the much larger C.34–C.38 families. Each either vanishes on Λ₀ (consistent with G_Q = GT̂) or
proves G_Q ≠ GT̂. Those proved to vanish on GT̂ (Δ by H17 Corollary 4 and GT_TOWER_CHECK A.7; ε₅, ε₇, ε₁₃; the F₂
family) are tests GT̂ passes; the C.34–C.38 characters at p ≥ 17 are untested (N5). Since Λ₀ ⊂ HLS's Λ acts on the whole
pure tower by explicit formulas, each test is a statement about that action.

### N5. The arithmetic-trivial characters of LM8_PUSH C.34 count the even-weight generators of LM2's graded hexagon Lie algebra

**Statement.** The number a_n of LM8_PUSH C.34 (formula C34.1, an S₃-character sum) equals dim W_n, the graded
loop-and-symmetry space of LM2 B.g2–B.g3, for 2 ≤ n ≤ 12 (0,0,1,0,1,0,2,1,4,2,9,7 for n = 1..12), and b_n bounds the span
of brackets of lower weights; d_n = a_n − b_n is a lower bound for the number of indecomposables of W in weight n. At
n = 12, b₁₂ = 6 equals the bracket rank the LONGUE_MARCHE_A reader computed, so W₁₂/[W, W]₁₂ is exactly one-dimensional.
In even weights: d₁₂ = 1, d₁₄ = 10, d₁₆ = 37, d₁₈ = 143, d₂₀ = 513, d₂₂ = 1805, d₂₄ = 6312 (`c34_an.py`). So C.34's
"d_{p−1} arithmetic-trivial F_p-characters" are the weight-(p−1) generators of W, transported to the group by Lazard.

**Consequence and the step that remains.** grt₁ contains the free Lie algebra on σ₃, σ₅, … (Brown 2012) and equals it
by the Deligne–Ihara/Drinfeld conjecture (in low weights by machine computation; source not opened here). Wherever
grt₁,n is generated by brackets (all even n under that conjecture), every functional on W_n/[W, W]_n kills grt₁,n. C.35
turned this into vanishing on GT̂ for n = 12, p = 13, through the pentagon defect of the first nonzero graded term. The
same mechanism at n = p − 1 would give, for each prime p ≥ 13, d_{p−1} independent characters of GT̂₀ vanishing on GT̂,
so that GT̂₀/⟨⟨GT̂⟩⟩ would map onto ∏_{p≥13} F_p^{d_{p−1}}. What is missing is a mod-p statement at each p: the linearized
pentagon equations over F_p in weight p − 1 have only bracket solutions (a finite rank computation per p, which C.35's
script `pbc_weight12_pentagon.py` did at p = 13). Status: the identity a_n = dim W_n is a computation (mine, against
LM2's table, which the LONGUE_MARCHE_A reader computed two ways); the consequence is a program, not a theorem.

**Why it matters.** It gives one dictionary for three runs (LM2's graded table, LM8_PUSH's group characters, GT_TOWER_CHECK's
quadratic family) and an explicit, checkable next computation (p = 17: 37 candidate pentagon-trivial characters).

### N6. Corrections to our own posted text (H17 = hexagon:2611.00940)

- Line 158 of `reports_20261123/h17_note/h17_note_wb0007.tex`: "The inclusion GT̂ ⊊ GT̂₀ itself is known" carries no
  citation. Dolgushev–Guynee (arXiv:2401.06870, the note's [DG], p. 2, opened) say only that GT_gen "obviously contains
  GT as a subgroup"; the topicality pass found no printed proof; our runs claim it (LM8_PUSH C.35, C.39; GT_TOWER_CHECK
  A.7; SECTION_GHOSTS E.198), unrefereed. A v2 should cite those runs as unrefereed or drop "known".
- The note does not cite Lochak 2025, which asks exactly the questions its Theorem 1 answers (N1), nor EXIT_TOWER
  E.43–E.44 (16 Nov), which proved (IV) on GT̂ first, in Lochak's formulation.
- Lochak's p. 61 inclusion and relation (III′) (N1, last paragraph) must be settled before v2 repeats "Relation (III′)
  is not touched" as an open problem.

---

## 2. Outside results that change our items

| Outside result (opened unless said) | Our items | How it changes them |
|---|---|---|
| Lochak, Algebra i Analiz 37:2 (2025), Def. 5.4, Prop.–Def. 5.6, Prop. 5.9, Thm 5.10, closing remarks pp. 61–62 | H17 Thm 1–2; SECTION_GHOSTS E.177–E.181; EXIT_TOWER E.43–E.45 | Our (IV) answers his three questions; with his Thm 5.10 gives Out*(Γ̌_{g,[n]}) ≅ GT̂ (N1); E.45 settled for Out*; possible (III′) consequence to check |
| Boggi, arXiv:2011.15075v6 (22 Apr 2026), main theorem (from the topicality pass, not opened by me) | EXIT_TOWER E.45, E.14 | Claims Out^{I₀}(PΓ̌(S)) ≅ Σ_n × GT̂; N1 gives the Out* part without its Prop. 6.9/Lemma 6.16 |
| Stix, Invent. Math. 199 (2015), Cor. 5–7 (opened) | SECTIONS_OVER_Q A.24, A.32; LM6 B.14 | Adelic (no cusp place) noncuspidal sections of U over Q are rational points; with N2(b) closes every A.14-class section without potentially multiplicative cusp places |
| Betts–Kumpitsch–Lüdtke, arXiv:2305.09462v2 (11 Apr 2026), Thms A–E, Prop. 1.10 (opened) | SECTIONS_OVER_Q A.24; SECTION_GHOSTS A.2; ANABELIAN_149_PUSH D.U1–D.U4 | Refined Kim's conjecture for density-one p ⇒ S-Selmer section conjecture; S = {2} done (Thm C, already Stix); Stoll's finite-descent conjecture ⟺ Selmer section conjecture. The runs cite it; N2 extends Thm C to cusps allowed at 2 |
| Li–Lüdtke, arXiv:2608.20615 (20 Aug 2026), abstract | CYCLOTOMIC_KERNEL, SOQ over number fields | S-Selmer section conjecture for U over imaginary quadratic fields, S empty or one prime not fixed by conjugation |
| Zehavi, arXiv:2611.18218 (13 Nov 2026), abstract; Yap, hexagon:2611.00576 | LM6, SOQ, FERMAT_SUCCESSOR (curves of genus ≥ 2) | Kim's dimension inequality for all genus ≥ 2 curves over Q with a point ⇒ finite Chabauty–Kim loci ⇒ the p-adic localizations of Selmer sections lie in a finite set (already Betts–Stix, Annals 201 (2025), Thm A); no Selmer section conjecture without Kim's equality |
| Furusho, RIMS Kôkyûroku 1267 (2002) pp. 189–196 (opened) | H17 open question 1 | Gives (III′) explicitly; (III′) ⇒ (III); LNS's "new GT" = NS's IΓ |
| Nakamura–Schneps, Invent. Math. 141 (2000) (not opened by me) | H17 | Source of (IV), (III′); §6 needed for the (III′) question |
| Dolgushev–Guynee, arXiv:2401.06870 (opened) | LM4_SUCCESSOR C.30, C.31; H17 l. 158 | Defines GT_gen as the invertible elements of a monoid (Def. 2.5); C.30 shows invertibility is automatic for unit λ (answers Lochak–Schneps 2006 Q1.1, as the topicality pass found); does not support "GT̂ ⊊ GT̂₀ is known" |
| Pop–Topaz, arXiv:2104.10504v2 (29 Sep 2025), abstract | N4; EXIT_TOWER E.24 | A GT-variant built from hyperplane-arrangement complements and pro-ℓ 2-step nilpotent π₁ is G_Q; contrast with N4 (GT̂ = G_Q ⟺ Λ₀ = G_{K₂}) |
| Hart–Harvey–Ong 2017; Kurihara 1992; Mok–Zheng hexagon:2611.00998 (K_{4m}(Z) = 0, m ≤ 30, unrefereed); Pintar 2611.00829 (from the literature file) | C.IHARA; C.K12/K80; SECTION_GHOSTS E.209–E.210 | N3: the section-tower obstruction is K_{2r}(Z) ⊗ Z_ℓ; Vandiver eigenspaces up to index 30 vanish at every prime |
| Ishii, arXiv:2312.04196v3 (6 Jan 2026), abstract | C.IHARA; LM8_PUSH Part A; SA07 F.3.32 | The kernel question for the once-punctured CM elliptic curve over an imaginary quadratic field, assuming a Deligne–Ihara analogue; same object as LM8_PUSH Part A and F.3.32 (y² = x³ − x over Q(i)); C.IHARA's cup/pole method is the proposed route to weaker hypotheses (KTHEORY_CM_THETA §4.4) |
| Najman, hexagon:2611.00991 (24 Nov 2026), abstract | LM6 B.15 | The Conrad–Edixhoven–Stein conjecture (J₁(p)(Q)_tors generated by rational cusp differences, p ≥ 5), via Calegari–Dimitrov–Tang; AI-produced, not fully checked by its poster. B.15 rests on the 6 Oct local theorem; this gives the torsion part of its abelian layer a cuspidal description |
| Steklov arXiv:2602.17746v2; Carlson–Stix arXiv:2410.22474v2; Carlson–Haine–Wolf arXiv:2407.19920 (from the topicality pass) | LM6/LM8_PUSH/FERMAT_SUCCESSOR; LM5 F.50, A1_SUCCESSOR B.* | Fermat for Selmer sections claimed for ℓ ≥ 7 with two errors our runs found; reconstruction over sub-p-adic fields covers part of our reconstruction items |
| Gaifullin arXiv:2611.20353; Pshenichnyi arXiv:2611.24813 (from the topicality pass) | EXIT_TOWER D.50–D.106 | Neighbours for the genus-three Torelli chain (finite generation of H₂(I₃), [I₃, I₃]^ab) |

---

## 3. The links, by theme

Each link names the two statements, the kind (input, special case, generalization, obstruction, counterexample,
same object, parallel mechanism), and what it carries. The TSV has one row per link with locators.

### A. GT̂, the gentle group and the Teichmüller tower

- **H17 Thm 1 = EXIT_TOWER E.44 = SECTION_GHOSTS E.177–E.180** (same theorem, two runs, same method: Boggi–Zalesskii's
  Theorem A on a Klein four-group of the ten-point sphere). EXIT_TOWER states it as 𝒥(A) = A in Lochak's compatible-pair
  group (E.43 identifies Lochak's IΓ with the graph of 𝒥). Feeds N1.
- **H17 Thm 2 (GT̂ = Λ₀·G_Q) → GALOIS_GT §1.1 → N4**: the arithmetic quotient GT̂/Λ₀ ≅ Gal(K₂/Q); every invariant through
  (λ, ρ₂) is Galois; ρ₂ mod 2 = ε₈∘λ (Dirichlet: A governs effective realization; ρ₂ mod 4 needs Hecke GRH over Q(i)).
- **LM7_PUSH E.65 (Δ) → H17 Cor. 4 / EXIT_TOWER E.49 / GT_TOWER_CHECK A.7**: three routes to Δ|GT̂ = 0; E.65 and E.58 are
  the unrefereed inputs of Cor. 4 (H17 §"What remains open", item 3). DELTA_ON_GT A.103/A.112 give a fourth, different
  reduction (to the S₄ character ν₄ = κ_d mod 2); H17 Cor. 4 is the instance Δ of N4(c).
- **LM8_PUSH C.30 = GT_TOWER_CHECK B.2.25–B.2.30**: two runs give the ℵ₀-dimensional F₂-space of characters of GT̂₀
  vanishing on GT̂ (C.30's θ_p for p ≡ 5 mod 12).
- **LM2 B.g3 → LM8_PUSH C.33, C.34–C.39**: graded input (N5): a_n = dim W_n; weight-12 indecomposable → ε₁₃.
- **LM2 C.a16 (finite congruence images of GT̂₀, GT̂, G_Q coincide) ↔ DELTA23 F18 ↔ N4**: congruence quotients cannot
  separate; every separating test must be non-congruence (Kazalicki's ASD congruences, hexagon:2611.00822, live on that
  side; no mechanism found).
- **LM4_SUCCESSOR C.29–C.31 → Dolgushev–Guynee Def. 2.5, Lochak–Schneps 2006 Q1.1**: the monoid of hexagon solutions with
  unit λ is a group (C.30); the profinite PaB monoid is a group (C.31). C.29 (boundary-preserving endomorphisms of
  profinite surface groups are automorphisms) is the tool.
- **LM4_FINITE_GROUP_ACTIONS D.29–D.30 ↔ H17's use of Boggi–Zalesskii**: the positive finite-subgroup rigidity H17 needs
  (finite p-subgroups conjugate into the discrete group, genus ≤ 2) against the negative torsion-free statement
  (torsion-free C₂-extensions need not be surface completions): the boundary of the method.
- **LM4_SUCCESSOR Main A (involutions conjugate to c) ↔ GT_TOWER_CHECK B.3/B.6 ↔ Lochak–Schneps [LS2]**: one question in
  three runs; the H17 method (finite subgroups and two forgetting maps) is the natural tool, as for (IV).
- **N1 ↔ EXIT_TOWER E.45, E.14 ↔ Boggi v6**: E.45 closes in the Out* form; E.14's refutations bear on Boggi v6 and
  possibly on Lochak's input [3].
- **SA22 (run 2) A.6.q_test, A.6.049a ↔ SOQ/SECTION_GHOSTS cusp-local sections ↔ N2(b)**: the nodal Kummer parameter q is
  recovered from the tangential arithmetic action (A.6.q_test); N2(b) uses the same Kummer data at cusp places.
- **SA22 / SA22_run2 capping (67/074–082) ↔ H17/N1**: the 1980s letters on the Teichmüller tower (cotes 66–68) and the
  two-level principle; no mathematical mechanism beyond the shared tower.
- **SA09 B2.4 (Schneps's sextic trees, field of moduli Q(∛2)) ↔ N4**: a dessin orbit that sees the Kummer character of 2,
  which ρ₂ extends to GT̂; a GT̂-orbit larger than the Galois orbit would refute G_Q = GT̂. No computation made.

### B. Sections of the tripod and of Fermat curves over Q

- **SOQ A.14 → A.16 → N2 (a)–(c) → Stix 2015 Cor. 6 / BKL Thm C**: the realization λ₀ is an S-unit point; cusp places
  must be potentially multiplicative for E_{λ₀}; the rest is Stix.
- **ANABELIAN_149_PUSH D.30–D.31 → SOQ A.14–A.24 → N2**: the same Legendre route, first form and current form.
- **SOQ A.32, A.44 ↔ SECTION_GHOSTS A.2, E.101–E.102 ↔ N2**: ghosts have infinite support, so they lie outside the A.14
  class; N2 says that inside the class the only obstruction is cuspidal.
- **SECTION_GHOSTS B.25/E.209 → N3 → ALPOGE C.K12/K80, Mok–Zheng**: lifting obstruction = K_{2r}(Z) ⊗ Z_ℓ.
- **SECTION_GHOSTS D.2 ((FS)_nil ⇒ Conjecture A of cote 149 scan 56) ↔ BKL Thm A (refined Kim ⇒ S-Selmer section
  conjecture; Stoll's finite-descent conjecture ⟺ Selmer section conjecture)**: two conditional routes to the same
  statement; (FS)_nil is a pronilpotent finite-support statement, Stoll's conjecture an adelic one.
- **LM6 E.12 + LM8_PUSH D.23 + FERMAT_SUCCESSOR A.1–A.11 ↔ Steklov 2602.17746**: Fermat for Selmer sections (odd n);
  Steklov's proof carries the false step D.22 found.
- **FERMAT_SUCCESSOR A.52–A.53 ↔ BKL Thm E ↔ Stoll 2007 Thm 8.6**: A.53 puts a rank-zero, finite-Sha factor
  (Jac(y² + y = x⁵)³) in the Jacobian of the plus Fermat quintic; that is the hypothesis of BKL Theorem E (Chabauty–Kim
  loci inside a fixed finite subscheme for every good p) and of Stoll's Theorem 8.6, which BKL note already gives the
  Selmer section conjecture for such projective curves. A.52 is the affine, prosolvable form; the projective form is
  Stoll's theorem applied to A.53.
- **SECTION_GHOSTS E.100 (no pro-2 abelian section of the plus Fermat curve, n even) ↔ FERMAT_SUCCESSOR B.30 (Z₃-family of
  non-cuspidal pro-3 sections) ↔ ANABELIAN_A1 A.27 / SECTION_GHOSTS E.150 (single prime fails over F_q)**: one mechanism
  in three places: one coefficient prime does not determine the section; all primes (or the full profinite group) do.
- **LM7_PUSH C.4–C.7, F.1–F.5 and LM7_FERMAT_TOWER E.32 (phantom lim¹ classes) ↔ E.209 proof (Mittag-Leffler kills lim¹
  for fixed finite S)**: phantoms need unbounded ramification; with fixed S they cannot occur in H².
- **Zehavi / Yap / Betts–Stix ↔ LM6, SOQ**: finiteness of p-adic localization images of Selmer sections (genus ≥ 2).

### C. Sections over finite fields and reconstruction

- **ANABELIAN_SUCCESSOR A.3 = ANABELIAN_A1 A.1, A.33 = A1_SUCCESSOR A.1 (three proofs of A1) ↔ Saïdi–Tamagawa 2009
  Prop. 1.8(vi) ↔ FLAGGED_149 B9**: A1 removes the finite exceptional set (A.CR10) and closes B9; cote 149 scans 35–36.
- **ANABELIAN_A1 A.27, SECTION_GHOSTS E.150 ↔ A.CR10**: single-prime collisions mark why A1 needs a J_C-large prime set.
- **ANABELIAN_SUCCESSOR A.87 / ANABELIAN_A1 A.CF9 ↔ Mochizuki–Tamagawa 2008 Prop. 2.2**: the mixed-prime (prime-to-p)
  configuration fibre sequence is not exact; their exactness hypothesis (all primes or one prime) is necessary.
- **LM5 F.50, ANABELIAN_149_PUSH F.45, A1_SUCCESSOR B.137–B.147 ↔ Carlson–Stix 2410.22474v2, CHW 2407.19920**: outside
  results cover the sub-p-adic members; fields containing μ_∞ stay ours (topicality pass).
- **CYCLOTOMIC_KERNEL A6 ↔ SA07 F.3.32 ↔ LM8_PUSH A.1, A.3 ↔ Nakamura 1990**: four group-theoretic characterizations of
  cusp inertia / cuspidal sections (cyclotomic-kernel centralizer; open arithmetic normalizer and the weight-6 class;
  G_{K^ab}-fixed subgroups; weights). F.3.32 settles one half of LM6 A.22 (route to the LM expert, as SWEEP3_A said).

### D. Ihara's question, Vandiver, K-theory of Z, Iwasawa theory

- **C.IHARA (hexagon:2611.00939) ← Vandiver/Greenberg; ↔ K_{4k}(Z)**: Vandiver at p ⟺ K_{4k}(Z) ⊗ Z_p = 0 for
  1 ≤ k ≤ (p − 3)/2 (Kurihara; Quillen–Lichtenbaum). C.K12/K80 and Mok–Zheng give the eigenspaces of index ≤ 20 (≤ 30)
  at every prime, which settles Vandiver only for p ≤ 43 (≤ 63), already known; no new Ihara prime follows.
- **The eigenspace dictionary (N3)**: one group, H²(G_{Q,{p,∞}}, Z_p(w)) ≅ K_{2w−2}(Z) ⊗ Z_p ↔ A(ω^{1−w}), read three ways:
  C.IHARA needs only the even part (X⁺ finite); the section tower (E.209) needs all weights; K_{4k}(Z) = 0 is the even part
  index by index. At p = 37: C.IHARA holds, the pro-37 section tower has possible obstructions exactly at r ≡ 31 mod 36.
- **C.IHARA's pole/moment method ↔ Iwasawa main conjecture ↔ KTHEORY_CM_THETA §3.3**: separation by evaluation at the
  cyclotomic characters u^m (Weierstrass preparation); the same mechanism as Iwasawa's identity theorem.
- **C.IHARA ↔ Ishii 2312.04196v3 ↔ LM8_PUSH Part A ↔ SA07 F.3.32**: the CM-elliptic analogue (§3.E).
- **SA12 A:canonical-Iwasawa (cd question over Z[μ_{p^∞}, 1/p] ⟺ μ = 0 for every number field) ↔ C.IHARA**: both rest on
  the cyclotomic Iwasawa module; C.IHARA uses μ = 0 for Q(μ_p) (Ferrero–Washington), so its hypothesis is λ⁺ = 0
  (Greenberg); SA12 needs μ = 0 beyond abelian fields (open).
- **SA07 F.3.32 (weight-6 class, Nakamura's q_{g,6} with character χ³) ↔ σ₃ / Soulé κ₃ / K₅(Z) ⊗ Q**: the arithmetic
  weight-6 quotient is the Tate-twist-3 (σ₃) direction of the motivic Lie algebra; Ext¹(Q(0), Q(3)) = K₅(Z) ⊗ Q (Borel).
  Standard (Hain–Matsumoto, Nakamura); the identification of q_{g,6} with σ₃ was not checked at the source.
- **ALPOGE BD-K01 (K_{2e}(O_E)₍₃₎ for E = Q(ω, ∛269)) ↔ Ihara over number fields**: the same Quillen–Lichtenbaum
  dictionary over a non-abelian field (K_{2e}(O_E)₍₃₎ ≅ H²(O_E[1/3], Z₃(e+1))). An Ihara-type kernel statement for the
  outer action of G_E on π₁(U)^{(3)} would need the 3-adic Iwasawa module of E(μ_{3^∞}), which neither BD-K01 nor the
  7-adic supplement BD-R20 computes; E is not CM (Q(∛269) has a complex place), so there is no plus part to bound.
  Recorded as tried, no link.

### E. The two elliptic points: the curves y² = x³ − x and y² = x³ + 1 as common objects

- The j = 1728 curve y² = x³ − x (CM by Z[i]) appears in five places: the order-2 elliptic point of the modular orbifold in
  H17 Thm 3 and Δ (LM7_PUSH E.65; Q(E₃[4]) = Q(x(E₄[3])) = Q(i, (3/4)^{1/4}), LM7_FERMAT_TOWER D.25); SA07 F.3.32
  (X₀ = E₀ ∖ {O}); LM8_PUSH Part A (the punctured CM curve over Q(i)); N2 (all three Z[1/2]-points of the tripod give this
  curve); Ishii's kernel question. The j = 0 curve y² = x³ + 1 appears in H17's Proposition 18 (every Weierstrass curve's
  3-division double cover is Y² = Z³ + D/108) and in MOONSHINE_AFTER_ALPOGE (ψ₃₆). A conference session can treat
  "π₁ of the once-punctured CM curves over Q(i), Q(ω)" as one object: Galois kernel (Ishii; C.IHARA method), fixed
  subgroups (LM8_PUSH A), normalizers (F.3.32), and the GT̂-action at the elliptic points (H17, Δ).

### F. Sweep-3 Galois items without a cross-region mechanism

- **SA05 A:class ↔ SA06 D.3b**: two routes to the infinite-order class of Grothendieck's motivic gerbe over F_p (motivic
  Galois theory); no link to the π₁ items found.
- **SA14 F11 (metabelian quotients of the local π₁ of a char-p surface singularity are finitely generated) ↔ EXIT_TOWER
  E.54 (completed induction does not reflect finite generation)**: both are finite-generation statements for profinite
  groups; no mechanism carries one to the other.
- **SA15 thm:plane-char2-all-groups (monodromy of H¹(C, F₂) on plane curves)**: a Galois image computation in
  characteristic 2; no link to the π₁ items beyond the method of monodromy groups.

### G. Tried and found empty

ALPOGE A.ORBIT (Galois orbits of CM points on A_g) against the CM parity Δ: both concern CM points, but A.ORBIT is about
heights and orbit sizes and Δ about a 2-adic/3-adic frame bit; no map between the statements. Moonshine items against GT:
none. The S₅ Artin items against anabelian items: none.

---

## 4. Conference topics and paper candidates across clusters

**P1. "The procongruence Teichmüller tower is governed by genus zero" (H17 v2).** H17 Theorems 1–3, plus N1 (Lochak's
Theorem 5.10 ⇒ Out*(Γ̌_{g,[n]}) ≅ GT̂ for all generic types), the answer to Lochak's three questions, the credit to
EXIT_TOWER E.43–E.44, the correction of line 158, and the (III′) question settled one way or the other. Clusters:
LONGUE_MARCHE_B (SECTION_GHOSTS, EXIT_TOWER, GT_TOWER_CHECK), LONGUE_MARCHE_A (LM7_PUSH E.65). Gates: Lochak's use of
Boggi–Funar against EXIT_TOWER E.14; Nakamura–Schneps §6.

**P2. "GT̂ inside the gentle group" (the topicality pass's item 3), with N4 and N5 as its frame.** LM2 B.g3, LM8_PUSH
C.30–C.39, GT_TOWER_CHECK A.7/B.2.*, SECTION_GHOSTS E.198, LM7_PUSH E.65/E.58/D.50. N4 gives the organizing principle
(all Galois-trivial characters are abelian tests decided on Λ₀); N5 gives the dictionary a_n = dim W_n and the next
computation (p = 17, weight 16, 37 candidates). Gates: a referee pass on LM8_PUSH P.2–P.4, C.30, C.32 and the C.35
certificate.

**P3. "Sections of the tripod over Q: what the Legendre route leaves" (SOQ + SECTION_GHOSTS + N2 + N3).** N2 closes the
A.14 class away from potentially multiplicative cusp places and settles the S = {2} case with cusps allowed at 2; N3
makes the all-prime lifting obstruction explicit (K-groups of Z). Cross-cluster with ALPOGE (C.K12/K80) and the outside
Chabauty–Kim papers (BKL, Li–Lüdtke). Gates: Pan 2022 and Helm–Voloch 2011 opened against A.14.

**P4. "π₁ of the once-punctured CM elliptic curves" (session topic, §3.E).** Ishii's kernel question with the C.IHARA
method (KTHEORY_CM_THETA §4.4 proposed it), LM8_PUSH Part A, SA07 F.3.32, H17's elliptic points. A next prompt could ask
for the kernel field of the pro-p outer action of G_{Q(i)} on π₁(E₀ ∖ O) at Greenberg-type primes.

**P5. The eigenspace dictionary as a short expository note (N3 + C.IHARA + K_{4m}(Z)).** Mostly classical; its value is
the table that tells each run which eigenspace it uses. Not a Hexagon research note; a companion page.

**Next computations, cheap.** (i) For p = 17, the rank of the linearized pentagon in weight 16 over F₁₇ on
W₁₆/[W, W]₁₆ (N5). (ii) The list U(Z[S⁻¹]) for S = {2, 3, 5, 7} with the v_p(j) table (N2), to see which cusp places can
occur. (iii) The (III′) identity on Λ₀ tested at a finite level of Γ̂_{0,[5]} with the GT-shadows of Dolgushev et al.

---

## 5. What I read and checked

Read: MAP_BRIEF.md, BRIEF.md; LONGUE_MARCHE_A/B (.md and items); ALPOGE.md and its K/Ihara rows; SWEEP3_A/B (.md and
Galois rows); TOPICALITY_LONGUE_MARCHE.md; OLDER_RUNS.md §§A.3, B; LITERATURE_20261124.md §§A–B and the appendix titles;
GALOIS_GT.md and KTHEORY_CM_THETA.md (23 Nov maps); the H17 note (all statements, conventions, §§1–2, Lemmas 4–5,
bibliography); the Ihara paper §§1–2 and its theorem; SECTIONS_OVER_Q `legendre_agent.tex` (A.12–A.24, all 747 lines);
SECTION_GHOSTS `part_E_regular_coefficients.tex` (E.209 with proof); LM8_PUSH C.30, C.33–C.40 statements; EXIT_TOWER
E.43, E.44, E.45, E.14 statements; LM6 B.14–B.15 with proofs. Outside, opened: Lochak 2025 (Def. 5.4, Prop.–Def. 5.6,
Prop. 5.9, Thm 5.10, closing remarks, references), Stix 2015 (Thms A–C, Cors 5–7), BKL v2 (introduction, Thms A–E,
Prop. 1.10), Dolgushev–Guynee (introduction, Def. 2.5, Remarks 2.6–2.9), Furusho RIMS 1267 (Def. 2.1), Nakamura–Tsunogai
RIMS 1267 (to rule it out); abstracts of Zehavi, Yap, Ishii, Li–Lüdtke, Najman, Pop–Topaz.

Check events (`MAP_GALOIS_ANABELIAN_CHECK_EVENTS.tsv`): LM8_PUSH C.34 (computation against LM2 B.g3); H17 Lemma 5(c) on
GT̂₀ (independent re-proof); H17 Theorem 1 against Lochak's (IV*) and Furusho's (IV) (targeted check of the identity of
the forms); SECTION_GHOSTS E.209.1 (independent re-proof by the Kummer sequence); SOQ A.14's j-criterion (computation);
Lochak 2025 Thm 5.10 and Stix 2015 Cor. 6 (carried as background, statements read at the source). The new statements
N1–N5 are proofs written here; no one has checked them yet.
