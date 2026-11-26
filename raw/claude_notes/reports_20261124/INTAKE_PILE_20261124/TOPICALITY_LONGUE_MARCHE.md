# Topicality pass, group LONGUE_MARCHE (clusters LONGUE_MARCHE_A and LONGUE_MARCHE_B), 24-25 Nov 2026

By Claude Opus 5.5 at effort high, launched by the main session 329fb1e6 (Claude Opus 5.5 at effort max), following
`TOPICALITY_BRIEF.md`. Input: `LONGUE_MARCHE_A.md`, `LONGUE_MARCHE_B.md` and their `_ITEMS.tsv` (all 139 rows: every
useful item, every marginal one, and the open questions, so that the conference sees which questions newer work has
touched), and `LITERATURE_20261124.md`. Row table: `TOPICALITY_LONGUE_MARCHE.tsv` (same folder). Work file:
`<local>/Documents\agent_notes\20261124T2136Z_Topicality_Longue_Marche_NOTES.md`.

All results under review are by GPT-6 Astra (ChatGPT Pro mode); checks named below say who made them. I checked no
mathematics in this pass; I checked literature. A source is cited below only where I opened it at the statement, unless
the row says "not opened".

**Verdict counts (139 rows):** STILL NEW 88, PARTLY 11, KNOWN BEFORE 9, UNSETTLED 8 (plus E.45 inside the E.24/E.45
row), OPEN questions not settled by newer work 20, settled inside the programme 3. **Nothing in the group is overtaken
by work posted after the runs.** The two outside works that matter most are older than the runs, and both runs knew
them: Steklov's *Fermat's Last Theorem for Selmer sections* (arXiv:2602.17746v2, March 2026), which already claims the
prime-exponent case of our Fermat item and carries two errors our runs found; and Carlson-Stix (arXiv:2410.22474v2,
20 Sep 2026), which proves étale reconstruction over every sub-p-adic field and so covers part of our reconstruction
items.

---

## Worth a paper now (ranked by usefulness)

**1. Answer to Lochak-Schneps 2006, Question 1.1: unit hexagon solutions are automorphisms, and the profinite GT
monoid is a group (LM4_SUCCESSOR C.29, C.30, C.31).** *What:* C.30: a pair (λ, f) with λ ∈ Ẑ^×, f ∈ F̂', satisfying
duality and the hexagon, already defines an automorphism of F̂₂ (no invertibility hypothesis), while an arbitrary unit
pair need not (f = [x,y]², image of order 12 in an A₅ quotient). C.31: every object-fixing endomorphism of the profinite
parenthesized-braid operad has unit λ, so the monoid is its group of units. C.29 is the tool: a peripheral-preserving
endomorphism of a profinite surface group with boundary is an automorphism. *Why it matters:* Lochak and Schneps list
this as Question 1.1 of their *Open problems in Grothendieck-Teichmüller theory* (Proc. Symp. Pure Math. 74 (2006),
§1; opened at Lochak's page, `textes/farb.pdf`): "Does x ↦ x^λ, y ↦ f⁻¹yf extend to an automorphism, or can it
actually determine a non-invertible endomorphism? One can ask the same question when (λ, f) satisfies (I), (II), (III)",
and they note that it "pertains to the full profinite setting only". C.30 answers both halves, and needs only (I), (II).
Every definition of GT̂ and of its gentle version still carries the invertibility as a separate condition: Dolgushev-
Guynee 2024 (arXiv:2401.06870, Definition 2.5, "the group of invertible elements of the monoid") and Dolgushev-Le-Lorenz
2020 (arXiv:2008.00066). *Novelty evidence:* no work found that answers Question 1.1 (searches S-ARX-GT, S-HEX, S-WEB2,
S-WIN below); the run itself claims no priority. *Proof:* `longue_marche_pro_pilot_20261104\answers\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped\LM4_SUCCESSOR\historical_data.tar`,
`LM4_SUCCESSOR/work_CE/C_further.tex` lines 474-740. Checked step by step (C.29, C.30) and the torsion argument of C.31
by the cluster reader, Claude Opus 5.5 at effort high, 24 Nov; C.31's inputs from Boavida de Brito-Horel-Robertson 2019
(Def. 6.4, Props 7.3, 7.7, 8.1) and the goodness of braid groups were not opened. Residual risk: C.29 could be folklore
in the profinite rigidity literature (Wilkes, Boggi-Zalesskii); I found no statement of it (Wilkes arXiv:1710.00730
grepped). Short paper; the cleanest of the group.

**2. Fermat's theorem for Selmer sections, corrected, for every odd exponent (LM6 E.12 with LM8_PUSH D.22, D.23 and
FERMAT_SUCCESSOR A.1-A.11, A.4, A.52; LM6 E.10, B.15).** *What:* every Selmer section of the affine Fermat curve U_n
over Q is cuspidal for every odd n ≥ 3; with the 6 Oct local section theorem (OpenAI's "The p-adic section conjecture",
openai/math, 24 Sep/6 Oct 2026) the section set is the three cusp packets; for even n there are no sections. *Topicality:*
Benjamin Steklov, arXiv:2602.17746v2 (19 Feb, v2 3 Mar 2026), Theorem A = Theorem 5.14, claims the statement for prime
ℓ ≥ 7 (opened). His proof has two faults, both found by our runs and both still in his latest version: (a) the
Kummer-divisibility step (Prop. 4.6, used in Prop. 5.10): at the Fermat cusp q = 256⁻¹t^{2n}(1 + O(tⁿ)), so the class
κ(256⁻¹) has 2-adic valuation −8 and is not divisible by n (LM8_PUSH D.22, FERMAT_SUCCESSOR A.4; recomputed by the
cluster reader, Claude Opus 5.5 at effort high); (b) his proof of Theorem 5.14 uses "the stacks Y₁(ℓ) and Y(μ_ℓ) have no
Q-points for ℓ ≥ 7", false at ℓ = 7 (LM6 E.10: (0,0) of order 7 on y² − xy − 4y = x³ − 4x²); his own Corollary 5.6
says ℓ ≥ 11. So the verdict is PARTLY: the prime case ℓ ≥ 7 is claimed in print, but no correct proof is in print, and
n = 3, 5, 7 and composite n are ours. *Why it matters:* this is the form of Fermat's theorem Grothendieck asks for in
the Longue Marche (§51.16), and it would be the first correct proof of the Selmer-section statement. *Proof:*
LM6 `answers\LM6_POINTS_AS_SECTIONS_final_20261114T1613Z_unzipped\` (E.6-E.12, with E.8 carrying the false step), the
repair in `answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped\sections\D.tex` lines 1560-1790 (D.22, D.23; local part
read by the cluster reader), FERMAT_SUCCESSOR `checkpoint_06\deliverable\` (A.1-A.11, A.52, A.53). E.6-E.12 were followed
by Claude Fable 5.2 at effort high on 14 Nov (who passed the false step). Before writing: a full read of D.23 and of the
n = 3, 5, 7 cases, and an e-mail draft to Steklov under the outreach rule. A.52 (n = 5, prosolvable) rests on Stoll's
finite descent and a certified L-value, not checked.

**3. Where GT̂ sits inside GT̂₀: Drinfeld's two relations do not imply the pentagon profinitely (LM8_PUSH C.33, C.35,
C.39, C.31; LM2 B.g2-B.g4; GT_TOWER_CHECK A.7, B.2.25-B.2.30; SECTION_GHOSTS E.198; LM7_PUSH E.65, E.58, D.50).**
*What:* continuous surjective characters of the gentle group GT̂₀ to F₅, F₇, F₁₃, trivial on G_Q and on GT̂, so
GT̂₀/⟨⟨GT̂⟩⟩ maps onto C₅ × C₇ × C₁₃ × C₂^ℕ; the F₂-characters vanishing on GT̂ form a space of dimension ℵ₀; GT̂ ⊊ ker Δ
⊊ GT̂₀ for the CM parity Δ; the graded shadow: the loop-and-symmetry Lie algebra W (dimensions 0,0,1,0,1,0,2,1,4,2,9,7
through weight 12) is strictly larger than grt₁ from weight 7 and has an indecomposable in weight 12. *Novelty evidence:*
Dolgushev-Guynee 2024 (arXiv:2401.06870, p. 2) say only that GT_gen (= Harbater-Schneps GT̂₀) "obviously contains GT as
a subgroup", calling it "(possibly more tractable)"; Lochak-Schneps 2006 §1 records no such result; Furusho (math/0702128)
proves the opposite implication (pentagon ⇒ hexagons) and records its profinite form as open; I found no printed
statement, graded or profinite, that the 2- and 3-cycle relations fail to imply the pentagon (S-WEB1, S-WEB3, S-ARX-GT,
S-HEX). *Residual risk:* Ihara's special-derivation papers of the 1990s and Harbater-Schneps 2000 were not opened; the
graded table (B.g3) may be partly there. *Why it matters:* the first structural facts on the gap between GT̂ and GT̂₀,
which every GT-shadow computation (Dolgushev et al.) works inside. *Proof and checks:* LM8_PUSH `sections\C.tex` (C.30-C.39,
in-run audits only), `code\pbc_weight12_pentagon.py`; LM2 `sections\B_graded.tex` (B.g3 recomputed two ways by the
cluster reader); GT_TOWER_CHECK cp10 (A.7, B.2.*); LM7_PUSH E.65, E.58, D.50 refereed by Claude Opus 5.5 at effort max on
14 Nov. Not yet checked by anyone outside the run: the passage from W to the group (LM8_PUSH P.2-P.4, C.30, C.32) and the
pentagon certificate of C.35. Worth the paper now, with that referee pass as the first step.

**4. A1: points of curves in characteristic p are separated by the prime-to-p fundamental group (ANABELIAN_SUCCESSOR
A.3, ANABELIAN_A1 A.1, A.33, A.CR10, ANABELIAN_A1_SUCCESSOR A.1, A.50).** *What:* for genus ≥ 2 over a finite field (and
for hyperbolic curves over fields finitely generated over F_p) the point-section map into the geometrically prime-to-p
arithmetic group is injective; the Saïdi-Tamagawa exceptional set is empty for every J_C-large prime set, where the
literature has finiteness (Saïdi-Tamagawa 2009, Prop. 1.8(vi), opened by the main session on 17 Nov). It answers
Grothendieck's question of cote 149, scans 35-36. *Novelty evidence:* the main session's search of 17 Nov
(`pro_intake_20261116\LITERATURE_A1_MAIN_20261117.md`) and mine (S-ARX-AN, S-WEB6, S-HEX): nothing from 2018 to 24 Nov
2026 proves it. *Hexagon:* drafted, board row H07, `reports_20261123\h07_note\h07_note_v3.pdf` (9 pp.), stage W, waiting
for the user's look and word; the gates left on the board (Stix LNM 2054 ch. 7; journal locators) are about credit, not
the proof. *Proof and checks:* chain read in full by two copies of the Longue Marche expert, Claude Fable 5.2 at effort
max; Steps 1-6 of the AN_GRH rebuild checked by Claude Opus 5.5 at effort max; A.50's certificate reproduced by the
cluster reader's program. Still new; worth posting as drafted.

**5. Étale reconstruction beyond sub-p-adic fields (LM5 F.50, F.49; ANABELIAN_149_PUSH F.45; ANABELIAN_A1_SUCCESSOR
B.137-B.147, B.49-B.55; ANABELIAN_SUCCESSOR F.3, F.7).** *Topicality:* Carlson-Haine-Wolf (arXiv:2407.19920, Theorem 0.1)
proved Grothendieck's conjecture over infinite finitely generated fields; Carlson-Stix (arXiv:2410.22474v2, revised
20 Sep 2026, Theorems A and B) over every sub-p-adic field, with the same pinned morphisms our runs use (opened). That
covers the sub-p-adic members of our classes (finitely generated fields over Q; the henselizations D^h and their finite
extensions). What stays new: fields containing μ_∞, which are never sub-p-adic: subfields of finitely generated
extensions of Q^ab (F.50), finitely generated extensions of Q̄ of positive transcendence degree (F.45), K_{p,nil} and the
infinite Galois extensions of D^h (B.137-B.143); and the negative classes (henselian residue-characteristic-zero fields
B.49/B.55, the trdeg-2 field B.50, finite and centred fields F.49), beyond CHW's Example 2.31 (algebraically closed
fields). ANABELIAN_A1_SUCCESSOR compared itself with Carlson-Stix v2 correctly (paper line 16693). *Why it matters:* a
direct continuation of the newest work on Grothendieck's topos conjecture, and the answer to cote 149, scan 52.
*Checks:* F.47's integrality lemma and the first half of F.45 read by Claude Fable 5.2 at effort high; B.46-B.50 read
for sense by Claude Fable 5.2 at effort max; B.123-B.147 run-only. Worth one paper, after a proof read of F.50, F.45 and
B.137-B.143.

Already posted, no new paper needed: **relation (IV) of Nakamura-Schneps on all of GT̂ (SECTION_GHOSTS E.177-E.191)** is
hexagon:2611.00940v1 (23 Nov 2026). Its novelty holds after the runs: Lochak-Nakamura-Schneps (arXiv:2602.12462v1, p. 2,
opened) write that "it is unclear, however, whether the additional condition actually defines a proper subgroup of GT";
nothing on arXiv or Hexagon after 23 Nov touches it. A v2 can add the check of Corollary 4's two inputs (LM7_PUSH E.65,
E.58).

---

## Overtaken or known

- **Overtaken by newer work:** none.
- **Known before (in substance):** CYCLOTOMIC_KERNEL D2 (the run's proof is Tsujimura 2022 Props 1.2(ii), 4.2 with
  Hoshi-Mochizuki-Tsujimura Prop. 6.4; not opened by me), D5 and SECTIONS_OVER_Q C.3 (Clark 2006 with cd Q^ab = 1, as the
  runs say), SECTION_GHOSTS E.209-E.210 (regular primes: the maximal pro-ℓ extension of Q(ζ_ℓ) unramified outside ℓ is
  free; Shafarevich, Koch, Neukirch-Schmidt-Wingberg Ch. X; from memory, not opened: the run should label it Known),
  LM6 E.10 (7-torsion over Q is classical; new only as the correction of Steklov), LM6 E.8 (Steklov's statement, with its
  false step), EXIT_TOWER E.60, LM4_FINITE_GROUP_ACTIONS D.21, LM7_FERMAT_TOWER B.10 (elementary).
- **Partly covered:** LM8_PUSH D.23, LM6 E.12, B.15, FERMAT_SUCCESSOR A.52 (Steklov); LM5 F.50, F.49, ANABELIAN_A1_SUCCESSOR
  B.137-B.147, B.49-B.55, ANABELIAN_SUCCESSOR F.7/F.3 (CHW, Carlson-Stix); LM4_FINITE_GROUP_ACTIONS D.29 (Haran 1985);
  LM4_SUCCESSOR A.6 (the normalizer of c in GT̂ is ⟨c⟩: Lochak-Schneps [LS2], as LS2006 Q1.4 says).

## Not settled here

- **EXIT_TOWER E.45** (surjectivity of GT̂ → Out^{I₀} of procongruence groups, g ≥ 3): Boggi's arXiv:2011.15075v6
  (22 Apr 2026) main theorem claims Out^{I₀}(PΓ̌(S)) ≅ Σ_n × GT̂ whenever χ(S) < g − 2, which covers every g ≥ 3 and would
  give E.45; EXIT_TOWER E.14 says two steps of that paper are false as printed (Prop. 6.9, Lemma 6.16). Deciding it means
  refereeing Boggi v6 §6. This bears on how E.14 is reported to Boggi.
- **EXIT_TOWER D.50-D.106** (genus-three Torelli chain): two new neighbours in the window, Gaifullin arXiv:2611.20353
  (16 Nov: H₂(I₃; Z) finitely generated) and Pshenichnyi arXiv:2611.24813 (18 Nov: [I₃,I₃]^ab finitely generated). Neither
  proves or contradicts the chain; the referee the cluster file asks for should read the chain against them.
- **FERMAT_SUCCESSOR A.53** (Jac of the Fermat quintic Q-isogenous to Jac(y² + y = x⁵)³): probably classical
  (Koblitz-Rohrlich, Gross-Rohrlich 1978, Faddeev 1960); I could not open them.
- **CYCLOTOMIC_KERNEL A6** (needs Stix 2008 Thm 14 and Nakamura opened), **LM5 D.7** (Antieau-Williams), **LM6 B.34**
  (Mochizuki-Tsujimura Thm F(ii)), **LM6 D.6** (Porowski arXiv:2509.15660), **SECTION_GHOSTS P.3** (Hoshi-Tsujimura 2021),
  **SECTION_GHOSTS E.100** (Wickelgren's 2-nilpotent real section conjecture): each is a correction or a known-in-substance
  question that only the source decides.
- Open main questions of the programme touched by outside work: the tripod section conjecture over Q (LM6 B.27,
  ANABELIAN_149_PUSH D.U1-D.U4, SECTIONS_OVER_Q A.24): special cases are now in print by the Chabauty-Kim route,
  Betts-Kumpitsch-Lüdtke arXiv:2305.09462v2 (revised Apr 2026; locally geometric sections over Z[1/2]) and Li-Lüdtke
  arXiv:2608.20615 (S-Selmer sections over imaginary quadratic fields, S empty or one prime). These should be cited by any
  write-up of the Legendre route; they do not settle our questions.

## Searches made (codes used in the TSV)

- **S-HEX**: the Hexagon API (`/api/v1/works`), every work published 1 Sep-24 Nov 2026 (1,530 works, the whole catalogue),
  regex over title, abstract and tags for Grothendieck-Teichmüller, anabelian, section conjecture, sections of the
  fundamental group, Drinfeld associator, pentagon/hexagon equation, braid operad, parenthesized braid, Ihara, Nakamura,
  Schneps, Belyi, dessins, profinite free/surface/braid/mapping, mapping class group, Fermat curve, Selmer section, Kummer
  class, Legendre, prime-to-p/tame fundamental group, étale homotopy, Torelli, Chabauty, three points. Relevant hits: only
  our own 2611.00939 and 2611.00940. Dump: scratchpad `topLM/data/hexall.json`.
- **S-LAB**: openai/math preprints (752 entries; relevant: *The p-adic section conjecture* 24 Sep/6 Oct, *The
  Deligne-Drinfeld conjecture* 23 Sep, *Open homomorphisms of global solvably closed Galois groups* 5 Oct, all older than
  the runs and known to them) and anthropics/formal-math (nothing in these fields), as listed by the literature agent.
- **S-ARX-GT**: arXiv API, newest first: abs:"Grothendieck-Teichmüller" (81 hits), abs:"Grothendieck-Teichmuller" (10),
  ti:Grothendieck AND ti:Teichm* (43), abs:Teichmüller AND abs:profinite (17), "GT-hat"/widehat{GT} (4), Drinfeld AND
  profinite AND braid (2), "Grothendieck-Teichmüller" AND monoid (2), au Nakamura AND Schneps (2). Read: every title back to
  2019; abstracts of 2602.12462, 2606.01466, 2607.09231, 2607.18793, 2610.17482, 2603.02848, 2401.06870, 2405.11725,
  2004.08860, 1904.06749; full text grepped of 2602.12462, 2401.06870, 2008.00066.
- **S-ARX-SEC**: abs:"section conjecture" (69 hits, titles read to 2013), "Selmer section(s)" (4), "cuspidal section(s)"
  (1), "Fermat curve" AND "fundamental group" (4); abstracts of 2602.17746 (full text read at Thm A, Prop 4.6, 5.10,
  Thm 5.2, Cor 5.6, Thm 5.14), 2611.09080, 2610.24986, 2604.26131, 2509.15660, 2305.09462, 2608.20615, 2409.07923.
- **S-ARX-AN**: abs:anabelian AND "finite field" (9), "prime-to-p" AND "fundamental group" AND curve (8), Saidi AND Tamagawa
  (1); abstracts of 0801.1452, 1708.08773, 1507.00622, 2505.06826, 2604.23485.
- **S-ARX-PROF**: "profinite surface group" (3), au:Boggi (27), au:Wilkes AND profinite (8), Corob Cook (16); abstracts and
  version dates of 2011.15075, 2311.17025, 2406.08639, 1907.05063, 1408.5419, 1804.07800; 1710.00730 grepped.
- **S-ARX-TOP**: "étale topos/topoi" (12), au:Carlson AND au:Haine (1); full text of 2407.19920 and 2410.22474 grepped at
  their theorems and examples.
- **S-WIN**: the literature agent's arXiv dump of 13-23 Nov (596 papers in math.AG, NT, AT, KT, CT, cs.CC; 2,435 in 20
  further categories), regex-filtered for the same terms: relevant only Gaifullin 2611.20353, Pshenichnyi 2611.24813,
  Holzschuh 2611.23061 (profinite shape; not on our items), Wu-Zhu 2611.29541 (Fermat cubic twists; not on our items).
- **S-WEB1-7** (web searches, 24 Nov): (1) GT_0, Harbater-Schneps, pentagon implied by two relations; (2) GT monoid,
  invertible elements, Lochak-Schneps open problems; (3) two-/three-cycle relations not implying the pentagon, special
  derivations; (4) torsion-free profinite extensions of surface groups; (5) Fermat quintic Jacobian isogeny over Q;
  (6) prime-to-p sections over finite fields, exceptional set, 2024-2026; (7) Prym p-rank of odd cyclic covers in
  characteristic 2. None returned a source that proves one of our items.
- **Not covered:** math.GR and math.QA were not in the window dump (the arXiv API searches above cover them by keyword);
  the arXiv API rate-limited three author queries (Tsujimura, Minamide, Hoshi); printed classical sources were opened
  only where named (Lochak-Schneps 2006 yes; Harbater-Schneps 2000, Ihara 1990s, Stix 2008/2012, Gross-Rohrlich, Clark
  2006, Haran 1985 no).

---

## Every item, with its verdict

Columns: item; statement (short); verdict; worth a paper now; Hexagon. Evidence for each row is in the TSV.


### LONGUE_MARCHE_A / LM8_PUSH

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| C.33 | Continuous surjective character GT0-hat -> F13, trivial on G_Q, nonzero on multiplier one, not through the metabelian image | STILL NEW | yes, as part of one paper 'GT-hat inside GT0-hat' (with C.35, C.39, LM2 B.g3, GT_TOWER_CHECK A.7, SECTION_GHOSTS E.198); a referee pass on the profinite steps P.2-P.4, C.30, C.32 first | none |
| C.35 | The order-13 character of C.33 vanishes on GT-hat; GT0-hat/<<GT-hat>> maps onto C13 x C2^N | STILL NEW | yes (same paper as C.33); the pentagon certificate of C.35 needs an outside rerun | none |
| C.39 | Characters to F5, F7, F13 vanishing on GT-hat; GT0-hat/<<GT-hat>> onto C5 x C7 x C13 x C2^N (Drinfeld's (I),(II) do not imply the pentagon profinitely) | STILL NEW | yes (headline of the GT-hat-in-GT0-hat paper) | none |
| C.31 | Delta, Delta_D, Delta_D^2: three independent arithmetic-trivial quadratic characters of GT0-hat | STILL NEW | yes, inside the same paper | none |
| C.46 | Multiplier-one gentle element with D=1, Delta=1, identity on F/F^(3) (witness value 5I or I by sign convention) | STILL NEW | no (detail; a remark in the GT paper, with the sign convention named) | none |
| C.47 | Delta has derived depth exactly 4 on multiplier-one gentle pairs; finite detector of order 2^293 3^193 | STILL NEW | no (detail) | none |
| A.1 | Punctured CM curve over Q(i): fixed subgroup under a cusp-packet section restricted to G_{K^ab} is the cusp inertia | STILL NEW | no (tool for the sections line) | none |
| A.3 | Virtually fixed homology under G_{K^ab} = boundary + E-isotypic part orthogonal to cusp-divisor Kummer classes | STILL NEW | no (tool) | none |
| D.22 | Refutes the Kummer-divisibility step of Steklov Prop 4.6/5.10 (and LM6 E.8): q = 256^-1 t^(2n)(1+O(t^n)), v_2 = -8 | STILL NEW (a correction; the error stands in the latest version) | yes, inside the Fermat-through-sections paper; erratum to Steklov under the outreach rule | none |
| D.23 | Every Selmer section of affine Fermat U_n/Q, odd n>=3, is cuspidal (repaired cusp step); full section set = three cusp packets given the 6 Oct local theorem | PARTLY | yes: 'Fermat's theorem for Selmer sections, corrected and for every odd exponent' (with LM6 E.12, FERMAT_SUCCESSOR A.1-A.11) | none |
| C.3 | Does the pentagon imply the §47 descent fixed-point equation? | OPEN (not settled by newer work) | no | none |
| A.45 | Universal fixed-subgroup and normalized-procyclic classification for arbitrary finite covers | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_A / LM2_LOOP_EQUATIONS

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| B.m2 | Grothendieck's §46 loop system is exactly Drinfeld's (I),(II) by an explicit change of variables | STILL NEW (edition result on the manuscript) | no alone; it goes into the GT paper's introduction and the companion notes | none |
| B.g2 | S3-invariant special outer derivations = antisymmetric psi with J(psi)=0 (n>1) | STILL NEW (residual risk: Ihara's special-derivation papers of the 1990s not opened) | yes, as the graded half of the GT paper | none |
| B.g3 | Dimensions of W through weight 12 (0,0,1,0,1,0,2,1,4,2,9,7) against grt1; W_12 has an indecomposable | STILL NEW (same residual risk) | yes (graded input of C.33); checked by Claude Opus 5.5 at effort high (two computations) | none |
| B.g4 | q4 solves the 2-/3-cycle equations but lifts to no solution of (I),(II) | STILL NEW | no (remark in the GT paper) | none |
| B.g15 | Finite solution of (I),(II) of class 12, exponent 13, order 13^747, with a pentagon obstruction | STILL NEW | no (supporting example) | none |
| C.a16 | GT0-hat acts on the full linear congruence tower via GL2 conjugation with det mu; finite outer images of GT0, GT, Galois coincide | STILL NEW | no alone (section of the GT paper) | none |
| E.3 | Does GT imply the corrected orbifold compatibility of §47? | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_A / CYCLOTOMIC_KERNEL

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A6 | Cyclotomic-kernel centralizer of a section is nontrivial exactly for cuspidal sections, then = its inertia | UNSETTLED | no (tool) | none |
| D2 | Point-section map injective over K(mu_inf) and its finitely generated extensions | KNOWN BEFORE (in substance) | no | none |
| D5 | Conjecture A fails over Q(mu_inf): t^6+2y^3+4=0 | KNOWN BEFORE (in substance) | no | none |
| D7 | Theorem 3 fails over cyclotomic bases (1 and zeta6 on G_m have one section class) | STILL NEW (elementary; re-proved by the cluster reader) | no | none |
| D13 | Discontinuous actions normalizing no deck group; affine commensurator completion | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_A / LM4_FINITE_GROUP_ACTIONS

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| D.30 | Torsion-free C2-extension of the genus-2 profinite surface group with H^2(E;F3)=F3, H^2(E;F5)=0: no surface completion | STILL NEW | no for now (construction of E unchecked); a short note once refereed | none |
| D.29 | Torsion-free C2-extension of pi_{0,4}-hat preserving the loop structure, no surface completion (from Haran 1985) | PARTLY | no (with D.30 later) | none |
| D.21 | A torsion-free profinite group with an open Zhat need not be Zhat | KNOWN BEFORE (in substance) | no | none |
| D.78 | B = C_F(w) = K x\| Zhat, K pro-odd; B procyclic iff K = 1 | STILL NEW | no | none |
| C.92 | Point stabilizers of operator groups on the disk; noncompact case = uniform-tail condition | STILL NEW (not searched beyond the general sweeps) | no | none |
| D.12 | Is every nonidentity torsion element of GT0-hat conjugate to (-1,1)? | OPEN (not settled by newer work) | no | none |
| F.7 | C_{M-hat}(A5) = closure of C_M(A5) (gap in Boggi Thm C(iii), Boggi-Zalesskii Thm 5.1(iii)) | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_A / LM4_SUCCESSOR

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| C.29 | Endomorphism of a full profinite surface group with boundary sending boundary loops to conjugates of unit powers of boundary loops is an automorphism | STILL NEW (folklore risk) | yes, inside the C.29-C.31 paper (checked step by step by Claude Opus 5.5 at effort high) | none |
| C.30 | A unit pair (lambda,f) with duality and hexagon gives an automorphism of F2-hat (no invertibility hypothesis); an arbitrary unit pair need not | STILL NEW: answers Lochak-Schneps 2006 Question 1.1 in both halves | yes (strongest small GT result of the pile: a 20-year-old listed question, short proof, checked) | none |
| C.31 | Every object-fixing endomorphism of profinite PaB has unit lambda: the GT-hat monoid is a group | STILL NEW | yes (same paper as C.30); open BHR2019 Def. 6.4, Props 7.3, 7.7, 8.1 first | none |
| A.6 | C_P(c) = N_P(<c>) = {1,c}; conjugators from c into GT0-hat lie in GT0-hat | PARTLY | no alone (a lemma of the involution question) | none |
| C.34 | Furusho's Question 14, literal prescribed-root form, is false (S4 example) | STILL NEW | no (remark/erratum) | none |
| A.79 | Finite action passing every iterated source-central refinement with no full involutory lift | STILL NEW | no | none |
| B.28 | K = C_{P-hat}(A5) = closure(H_T) cap closure(H_5), H_T = F13, H_5 = F6, H_T cap H_5 = 1 | STILL NEW | no (reduction of an open question) | none |
| A.14 | Main A: every involution of P, GT0-hat, GT-hat conjugate to c | OPEN (not settled by newer work) | no | none |
| B.38 | Main B: K = 1 (gate B.75.6) | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_A / LM5_MULTI_GALOIS_TOPOI

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| F.50 | Pinned etale reconstruction for every subfield of a f.g. extension of Q^ab | PARTLY | yes, folded into one reconstruction paper (with 149_PUSH F.45, A1_SUCCESSOR B.137-B.147, B.49-B.55), after a proof read | none |
| F.49 | Pinned reconstruction fails over algebraic extensions of finite fields, fields with nontrivial Galois centre, algebraically closed fields | PARTLY | with F.50 (same paper) | none |
| A.20 | Finite covers do not distinguish shift and identity on finitary symmetric-group topoi | STILL NEW (elementary; re-proved by the cluster reader) | no | none |
| D.7 | (w2,p1) does not determine a map to the fourth stage; M(Z/4,3) carries four bundles (corrects Antieau-Williams v2) | UNSETTLED | no (erratum to the authors, after a source check) | none |
| F.44 | Pinned reconstruction beyond F.50 (G_m over Q^solv) | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_A / LM6_POINTS_AS_SECTIONS

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| E.12 | Every Selmer section of U_n/Q, odd n>=3, is cuspidal; with Tool (1) the section set is the three cusp packets | PARTLY | yes (the Fermat paper) | none |
| E.8 | Mod-l Legendre representation of a Selmer section of U_l is reducible (after Steklov) | KNOWN BEFORE as a statement (Steklov), with a false step in its proof (LM8_PUSH D.22) | inside the Fermat paper | none |
| E.10 | Y1(7)(Q) is not empty (refutes Steklov Thm 5.14 as used): (0,0) of order 7 on y^2-xy-4y=x^3-4x^2 | KNOWN BEFORE (classical: elliptic curves over Q with 7-torsion exist, Mazur's list includes Z/7); new only as the correction of Steklov | inside the Fermat paper (erratum) | none |
| B.15 | For g(X1(N))>=2 every section of Y1(N)/Q is cuspidal | PARTLY | no alone (a section of the Fermat paper) | none |
| B.34 | Mochizuki-Tsujimura Thm F(ii) as stated is false (tangential section at 2) | UNSETTLED | no (erratum after a source check) | none |
| B.27 | Every non-cuspidal section of the tripod over Q comes from a rational point | OPEN (not settled by newer work); special cases known | no | none |
| D.6 | Gap in the density step of §8 of the 6 Oct local section preprint | UNSETTLED | no | none |

### LONGUE_MARCHE_A / LM7_PUSH

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| E.65 | Delta: GT0-hat -> F2 continuous, zero on G_Q, Delta=1 on E.58's element | STILL NEW | yes, inside the GT paper (refereed by Claude Opus 5.5 at effort max, 14 Nov) | none |
| D.50 | Multiplier-one pronilpotent peripheral automorphisms of F-hat/R_nil with boundary conjugators lift to F-hat | STILL NEW | inside the GT paper | none |
| E.58 | Relative pronilpotent lifting for every open normal U; an element of GT0-hat in the extra CM coset | STILL NEW | inside the GT paper | none |
| C.5 | Phantom (lim^1) subgroup for Z3(2) torsion-free; restriction injective on it | STILL NEW (small) | no | none |
| E.3 | Is Delta zero on GT-hat? | SETTLED inside the programme (GT_TOWER_CHECK A.7; hexagon:2611.00940 on normalized elements); no outside work | see SECTION_GHOSTS E.182-E.191 | none |

### LONGUE_MARCHE_A / LM7_FERMAT_TOWER

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| E.32 | Cubic class-two section fibre empty or three classes by a lim^1 criterion; nonzero global obstruction with all local/finite ones zero | STILL NEW | no alone (could join a 'phantom sections' note with LM7_PUSH C.4-C.7, F.1-F.5) | none |
| D.25 | Q(E3[4]) = Q(x(E4[3])) = Q(i,(3/4)^(1/4)); twelve finite GT0 shadows in the extra coset | STILL NEW (field identity elementary) | no | none |
| B.10 | H^0, H^1 of S3 on I^3/I vanish | KNOWN BEFORE (in substance; elementary) | no | none |
| E.123 | Positional tower at 53: 3-primary S-class norms, class groups C9^2 | STILL NEW (not useful) | no | none |
| E.23 | Class-three and metabelian section sets of the Fermat cubic | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_A / FERMAT_SUCCESSOR

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.53 | Jac of the plus Fermat quintic is Q-isogenous to Jac(y^2+y=x^5)^3 | UNSETTLED (probably classical) | no | none |
| A.52 | Every Selmer section of the maximal prosolvable arithmetic pi_1 of plus U5 is cuspidal | PARTLY | inside the Fermat paper | none |
| A.71 | Cubic twists X^3+Y^3=dZ^3 with flex origin and a nontorsion point: only the unchanged integer exponent lifts through the joint level-three quotient | STILL NEW | no alone | none |
| A.4 | Refutes the cusp divisibility of LM6 E.8 / Steklov (independently of LM8_PUSH D.22) | STILL NEW (correction) | inside the Fermat paper | none |
| A.49 | X0(27) has a Z5-family of global sections point-induced at every completion except Q5 | STILL NEW | no | none |
| B.30 | Z3-family of full pro-3 sections unramified outside 3,7, non-cuspidal (refutes our task B.10(b)) | STILL NEW | no | none |
| B.42 | Common rational cusp colour at ramified inert q with v3(q+1) <= 3+v3(b); 27 sharp | STILL NEW | no | none |
| B.14 | Full profinite metabelian section sets; cross-prime cusp colours; full pro-3 equivalence | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_B / SECTION_GHOSTS

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| E.177-E.180 | Relation (IV) of Nakamura-Schneps holds for every element of GT-hat | STILL NEW (posted by us) | already posted; no new paper (a v2 if Corollary 4's inputs are checked) | POSTED hexagon:2611.00940v1 (23 Nov 2026) |
| E.181 | Every GT-hat element = Galois element x element of Lambda (lambda=1, rho=0) | STILL NEW (posted) | already posted | POSTED hexagon:2611.00940v1 |
| E.182-E.191 | Delta vanishes on normalized elements of GT-hat | STILL NEW (posted) | already posted | POSTED hexagon:2611.00940v1 (application); board row H17 |
| E.198 | GT-hat strictly inside ker Delta strictly inside GT0-hat (11-primary witness) | STILL NEW | yes, inside the GT paper | none |
| E.195 | A finite five-point level excludes every gentle element with Delta=1 from the pentagon | STILL NEW | no (corollary) | none |
| E.150 | Over F_q (3 not dividing q) Galois-conjugate points over degree-d extensions, gcd(d,3e)=1, share their full pro-3 section | STILL NEW (no source found; mechanism elementary) | no alone (an example in the A1 note, which already uses ANABELIAN_A1 A.27) | none |
| E.192, E.194, E.218 | Over every F_q and l != char, an explicit finite pro-l quotient separates interior point sections from cusp sections | STILL NEW | no | none |
| E.209-E.210 | For odd regular l, H^2(G_{Q,{l,inf}}, Z/l^n(w)) = 0 for all w | KNOWN BEFORE | no (the report should label it Known) | none |
| A.2 | (FS)_nil: an ordinary completed pair surviving the pronilpotent tower has finite support | OPEN (not settled by newer work) | no | none |
| E.174, E.214, E.215 | Infinite-support ordinary pair with class-two support matching; factorial outputs fail at class 4; primitive-five family to class 8 | STILL NEW | no | none |
| E.100 | For even n the plus Fermat curve has no pro-2 abelian section over Q (real obstruction) | UNSETTLED (likely known in substance) | no | none |
| P.3 | Hoshi-Tsujimura 2021 Prop 1.4(ii) omits the cusp at infinity; corrected criterion | UNSETTLED | no (erratum after the source check) | none |
| D.2 | (FS)_nil implies Conjecture A of cote 149 scan 56 for ordinary tripod sections over Q, with birational lifts | STILL NEW (conditional) | no | none |

### LONGUE_MARCHE_B / ANABELIAN_SUCCESSOR

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.3 | A1: point-section map into the geometrically prime-to-p group injective, curves of genus>=2 over finite fields (first proof) | STILL NEW | yes: the H07 note (drafted, 9 pp.), with provenance naming ANABELIAN_SUCCESSOR A.3 (16 Nov) and ANABELIAN_A1 A.1 (17 Nov) | drafted: board H07, reports_20261123/h07_note/h07_note_v3.pdf (stage W, not posted) |
| A.86 | Supersingular genus-two curve over F_{2^38}: every odd cyclic etale cover has primitive part of positive 2-rank | STILL NEW | no alone (a section of the H07 note's discussion of the cover route) | none |
| A.87 | Full prime-to-p configuration fibre map is not injective (genus>=2, every p) | STILL NEW | no alone (in the H07 note) | none |
| A.70, A.34 | y^2+y=x^5 over F16: degree-13 P-split cover with odd relative class number, ordinary new part | STILL NEW | no | none |
| F.7, F.3 | Candidate F3(b) false; closed-point-preserving relative etale-topos morphisms over F_q need not come from morphisms | PARTLY | with the reconstruction paper | none |

### LONGUE_MARCHE_B / ANABELIAN_A1

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.1 (A.R1) | A1, the version read end to end | STILL NEW | yes (H07 note) | drafted (H07) |
| A.33 (A.R5) | Point-section injectivity for hyperbolic curves over fields finitely generated over F_p (prime-to-p) | STILL NEW | yes (H07 note) | drafted (H07) |
| A.CR10 (A1_SUCCESSOR A.22) | Saïdi-Tamagawa exceptional set empty for every J_C-large prime set | STILL NEW (sharpens Saïdi-Tamagawa 2009 Prop 1.8(vi), finiteness) | yes (H07 note) | drafted (H07) |
| A.25 (A.CR12) | y^2+x(x+1)y=x^5+1 over F2: P, Q collide in the abelianized prime-to-2 quotient | STILL NEW (example) | no alone (in H07) | drafted (H07, as example) |
| A.27 (A.CR14) | A single prime does not separate points | STILL NEW (example) | no alone (in H07) | none |
| A.CR15 (item A12) | Point separation for prime sets neither singleton nor J_C-large | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_B / ANABELIAN_A1_SUCCESSOR

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.1 (A.42-A.49, B.68) | A1 by a direct characteristic-p route (no lifting comparison, no finite exceptional set) | STILL NEW | yes, as a second proof in the H07 note once an intake reads it | none |
| A.50 | Cyclic-19 Lang cover certificate separating P and Q (relative class number odd) | STILL NEW (certificate) | inside H07 | none |
| B.88 | Degree 3^7 pointed pro-3 separator over F16 of the same pair | STILL NEW | no | none |
| A.51 | Non-nilpotent fibre quotient of order 75 with a non-central cusp | STILL NEW | no | none |
| B.23 | Every genus-two curve in char 2 has an odd cyclic cover with primitive 2-rank zero: false | STILL NEW | no alone | none |
| C.2 | Char-p extension of cote 149 scan 32 Théorème 3 fails; kernel = G(K)[p^inf] | STILL NEW (edition-level correction) | no (companion note to cote 149) | none |
| B.93 | Uniqueness expectation of cote 142 scan 096 false for finite markings | STILL NEW (edition-level) | no | none |
| B.137-B.147 | Reconstruction over K_{p,nil}, normal-core fixed fields, proper Galois extensions of D^h; negative wild-procyclic fields | PARTLY | yes, in the reconstruction paper after a proof read | none |
| B.49-B.55 | Reconstruction fails over fields with a henselian rank-one valuation of residue char 0, and over a countable trdeg-2 field with trivial centralizers | PARTLY | yes, in the reconstruction paper | none |
| B.141, B.145 | Genus-two marked-curve criterion (y^2=x^6+1, p=2,5 mod 9); automorphism-eigencharacter criterion; genus-3 instance over F27 | STILL NEW | no | none |
| B.52 | Classification of fields over which reconstruction holds | OPEN (not settled by newer work) | no | none |

### LONGUE_MARCHE_B / ANABELIAN_149_PUSH

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.C2.20 | A1 holds if C has an odd cyclic etale cover prime to p whose primitive Prym factor has p-rank zero | STILL NEW (superseded by A1 itself) | no | none |
| A.C2.26 | A1 for every genus-two curve over F4 (certificates) | STILL NEW (superseded) | no | none |
| D.30, D.31 | Non-cuspidal tripod sections over Q: absolutely irreducible Legendre representations; finite ramification iff integrality; one cusp label gives a point | STILL NEW (conditional on Pan 2022 and the 6 Oct local theorem) | no (continued in SECTIONS_OVER_Q) | none |
| F.45 | Reconstruction over every f.g. extension of Qbar of positive trdeg and its subfields of positive trdeg over Q | STILL NEW | yes, in the reconstruction paper (second half of F.45 still unread) | none |
| D.U1-D.U4, F.9 | Conjecture A and variants for the tripod; classification of reconstructing fields | OPEN (not settled by newer work); special cases known | no | none |

### LONGUE_MARCHE_B / FLAGGED_149

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| F1-F20 table | Verdicts with exact scope on each passage Grothendieck flagged in cote 149 | STILL NEW (edition commentary) | no (companion notes to cote 149) | none |
| B4 | The open-subset translation lemma of scan 37 is false in type (1,1) | STILL NEW (edition-level) | no | none |
| B15 | y^2=x^5+(x^2+1)^2 over F5: [P-Q] of order 5, separated by a degree-16 prime-to-5 cover | STILL NEW (example) | no | none |
| B9 | Prime-to-p (*) for every hyperbolic curve over a field f.g. over F_p | SETTLED inside the programme (ANABELIAN_A1 A.1, A.33); no outside work | see H07 | drafted (H07) |

### LONGUE_MARCHE_B / SECTIONS_OVER_Q

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.14 | Four equivalent forms of bounded ramification for noncuspidal Selmer sections; rational Tate-system realization | STILL NEW (uses Pan Thm 1.0.4 and Helm-Voloch Prop 6 beyond their stated forms; sources not opened) | no (reduction; check Pan and Helm-Voloch first) | none |
| A.16 | Integral Legendre realization prod T_l(E_{lambda0}), lambda0 in Q-{0,1} | STILL NEW | no alone | none |
| A.24 | Recognition: a section with an integral Legendre realization is the section of lambda0 | OPEN (not settled by newer work) | no | none |
| A.32, A.44 | Finite-support ordinary completed pair is a rational point; infinite-support ghosts exist | STILL NEW | no alone (a 'ghosts' note is possible once (FS)_nil moves) | none |
| A.201, A.204 | Locally point-or-cusp-matching class-two sections lift to class three; r to r+1 | STILL NEW | no | none |
| A.178 | Fixed abelian cover + full metabelian quotient detect finite support (hyperbolic curves over number fields) | STILL NEW | no (check against Harari-Stix Thm 2.1 first) | none |
| C.3 | The section conjecture fails over Q(mu_inf), explicit witness | KNOWN BEFORE (in substance) | no | none |

### LONGUE_MARCHE_B / EXIT_TOWER

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| E.44 | J(A) = A for every A in GT-hat (two forgetting maps give the same elliptic parameter) | STILL NEW | no alone (feeds the h17 line) | none |
| E.49 | Delta vanishes on GT-hat | STILL NEW (our own posted note proves it on normalized elements) | inside the GT paper / already in the posted note | POSTED in part (hexagon:2611.00940, Corollary 4 route); board H17 |
| D.50-D.106 | Genus-three Torelli chain: kernel of the completion map of I3, arithmetic action, finite central extensions | UNSETTLED | no (referee first) | none |
| E.54 | Completed induction does not reflect finite generation (F3, metabelian G); refutes Corob Cook-Vannacci p.4 and FIM at 3 | STILL NEW (a correction; the assertion stands in the latest version) | no paper; an erratum note to the authors after the source check | none |
| E.60 | hat(Pi_g) -> prod_p Pi_g^(p) surjective with nontrivial kernel; the product finitely presented, strong PD2 at every p | KNOWN BEFORE (in substance; elementary) | no | none |
| E.48, E.14 | Boggi 2014 Thm 6.3 diagonal Bers model not injective; Boggi 2026 Prop 6.9, Lemma 6.16 and Boggi-Funar 2026 Lemma 2.23 false as printed | STILL NEW (corrections; unfixed in the latest versions) | no paper; inform the authors after a referee (outreach rule) | none |
| B.25 | Realization of cote 148: 542 objects, 1620 arrows, 1080 relators | STILL NEW (edition-level) | no (edition notes for cote 148) | none |
| E.24, E.45 | G_Q = GT-hat; GT-hat -> Out^{I0} of procongruence groups surjective for g>=3 | E.24 OPEN (not settled by newer work); E.45 UNSETTLED | no | none |

### LONGUE_MARCHE_B / DELTA_ON_GT

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.112 | nu_4 is a continuous character of the gentle group; the pentagon forces epsilon_2(W) = nu_4 on GT-hat | STILL NEW | no alone | none |
| A.84 | Delta\|GT-hat = 0 | SETTLED inside the programme (GT_TOWER_CHECK A.7; hexagon:2611.00940) | see E.182-E.191 | POSTED in part (hexagon:2611.00940) |
| A.98, A.110 | Delta detected on N^ab (rank 97, N = ker q12) mod 576; full-multiplier finite detector | STILL NEW | no | none |
| B.15 | Repaired lift of LM7 D.46 with Delta=1, parities (0,1) | STILL NEW | no | none |

### LONGUE_MARCHE_B / GT_TOWER_CHECK

| Item | Statement | Verdict | Worth a paper now | Hexagon |
|---|---|---|---|---|
| A.7 | Delta\|GT-hat = 0 and G_Q in GT-hat strictly in ker Delta strictly in GT0-hat | STILL NEW | yes, inside the GT paper | none |
| B.2.25-B.2.30 | Continuous characters GT0-hat -> F2 vanishing on GT-hat form a space of dimension aleph_0 | STILL NEW | yes, inside the GT paper (with LM8_PUSH C.39) | none |
| B.5 | Cote 148 folios 30-32: lower fractional twist 1/4, not 1/3 as in our transcription | STILL NEW (transcription question) | no (edition correction) | none |
| A.4.1 | By compactness a finite five-point quotient excludes Delta=1 elements from the pentagon | STILL NEW | no | none |
| A.4 | An independent finite census of pentagon shadows | OPEN (not settled by newer work) | no | none |
| B.3/B.6, B.4/B.7 | Every involution of GT-hat conjugate to c; a separator of G_Q from GT-hat | OPEN (not settled by newer work) | no | none |

---

Files: this file; `TOPICALITY_LONGUE_MARCHE.tsv` (139 rows, with the evidence column). Scripts and the
Hexagon dump in the scratchpad folder `topLM` of session 329fb1e6 (not durable); the searches are listed above so that
they can be rerun.
