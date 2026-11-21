# Intake of DP_MULT (prompt 34), checkpoint 02: what is new since checkpoint 01, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), still going. The intake of checkpoint 01 is
`INTAKE_DP_MULT_20261121.md` in this folder; its verdicts on DP1-DP24 stand and are not repeated.

## 0. What was read, and the scope

- **Return folder:** `research_returns\DP_MULT_checkpoint_02_20261121T0120Z_unzipped` (packaged 01:20:53 UTC). Checkpoint
  01's folder has been retired from disk. Newest DP_MULT present at the start and the end of this intake.
- **Read:** the ledger blocks after checkpoint 01 (00:44, 01:08, 01:20 UTC), the new rows of `QUESTIONS.tsv` (Q2e, Q3m-Q3r),
  `TRANSCRIPTION_NOTES.tsv` (its new columns: note_kind, observed_autograph, editorial_action), and `DP_MULT.tex` lines
  406-570 (§"A genuine higher-height scalar kernel test": DP28, DP29, DP31), 720-730 (DP25), 769-836 (DP26, DP27, DP30
  statements), 870-960 (DP32 with its proof; DP33 statement).
- **Read in full, every step checked (3):** DP25, DP28, DP32.
- **Proof read, cited theorems carried (2):** DP29 (weight bound w_{r_0}(β) ≥ s), DP31 (Zink's biextension injection,
  Katz's isocrystal Hom vanishing).
- **Statement level (4):** DP26, DP27, DP30, DP33.
- **Independent computation (for DP1/DP3 of checkpoint 01, needed for the Hexagon test):** exact rational arithmetic on
  Honda groups (p,h) = (2,2), (3,2), (2,3): v(D^n(t^k)(0)) = v(n![z^n]E(z)^k) against max{E_h(n), ⌈c_h n − (h−1)⌉, 0}
  for k ≤ 5 and every n ≤ 40 (resp. 30) where the coefficient is nonzero: 115 checks, no failure; sharpness
  v(D^{q^r}t(0)) = c_h(q^r − 1) at n = 1, 4, 16 (p=2, h=2), n = 1, 9 (p=3, h=2), n = 1, 8 (p=2, h=3). Script in my
  scratchpad (`dp_check.py`).

**Settled and moving.** The scalar analytic question (Q2e, Q3p, Q3r) is now settled; DP32 settles the actual dual. Still
moving: Q3e, now the genuine 1 × (h−1) dual kernel with mixed CM type, its theta/minor/period data, and the global cost.

## 1. Verdicts on the new findings

| Id | Statement (short) | Verdict |
|---|---|---|
| DP25 | E ⊃ K imaginary quadratic, Φ induced from K, p unramified, full integral CM: p inert in K ⇒ every factor has slope 1/2 (a 1-dim factor has height 2); p split ⇒ slopes 0, 1. The CM blocks of the Lean theta construction have such induced types, so DP22's Jacobian cannot be substituted | **confirmed** (Frobenius on Hom(E, C) restricts to the swap of Hom(K, C) at inert p, so Φ-membership alternates along each orbit; Shimura-Taniyama). The source claim about the Lean blocks (`CMObj.typeP/typeM`, `IsTen`) is carried. |
| DP26 | for the DP17 ramps with A = p³: R_2 = (p−1)(p+1), R_3 = (p−1)(p+2), (p+1)R_3 = (p+2)R_2 (at p = 11: 24·130 = 26·120) | statement level (arithmetic checked: 24·130 = 3120 = 26·120). A numerical certificate only. |
| DP27 | the Lean `Ranks` needs an even lift count; deleting one lift changes the endpoint ranks by (t+1) and the auxiliary signature | statement level (source facts carried). |
| DP28 | (H1)-(H4) (the Lean `BHyp` with p² → p^h) do not imply v(β_{a,b}) + ρ_h(a+b) ≥ s − 1, for h ≥ 3 | **confirmed.** β = log(1 + E_h(X)^p E_h(Y)): torus invariance from E_h(ηX) = ηE_h(X) for η^{q−1} = 1; coboundaries are ratios of the unit 1 + S^pT; coefficient at X^q Y^{p^{h−1}} is ±1/p^{h−1}; the inequality 2 − h + (p^{h−1}+1)/(p^h−1) < s − 1 reduces to p < p^{h−1}. It refutes the intermediate `LemmaS` substitution, not the final estimate. |
| DP29 | under (H2)-(H4) a theta-type Θ has v(κ![t^κ]Θ) ≥ ρ_2 n − Σs_p(κ_i)/(p−1); an explicit Θ_h attains c_h(n−1) at n = q^r | **proof read** (s − r_0 = ρ_2 checked; the binomial argument for w_{r_0}(β) ≥ s read, not re-derived). |
| DP30 | the actual Cartier dual H of a height-h one-dimensional formal O-module: Lie(H_k) has basis with e_i^{[p]} = e_{i+1}, rank h−2; for h > 2 some primitive direction has a unit p-th derivative | statement level. |
| DP31 | for h > 2 over W(k), under (H2)-(H4), exp β(L_h(S), L_h(T)) ∈ 1 + ST·R[[S,T]] (integral), so Θ satisfies the full slope c_h | **proof read, cited theorems carried.** Structure checked: biextension of G × G by Ĝ_m from the integral coboundaries; Zink §4.4 Prop. 121 injects Biext¹ into Hom(G_n, G_n^t) = 0 (slopes 1/h ≠ (h−1)/h, Katz 1979 §1.3; the integral lifting induction is right); uniqueness of normalized splittings (J([p]S, T) = J(S,T)^p forces J = 1); the residual biadditive aXY is killed by torus invariance (ζ^{1−p} ≠ 1). Valid for two scalar copies of G, as the run says, not for the dual pair. |
| DP32 | the Cartier dual of the Honda group has integral coordinates X_1..X_{h−1} with directional slopes c_i = p^i/(p^h−1), sharp, Σ c_i = c_h | **confirmed.** I checked: the scaling exponents p r_{i−1} − r_i = 1 and p² r_d − r_1 = 1 (both reduce to (p−1)S_h = q−1 and (p+1)(q−1) − p(q−1) = q−1); the cycle exponent 2 + (d−1) = h, [p]^d = F^h on H_k, dually F_G^h = [p]_G, so G is Lubin-Tate for p over W(F_q) and ≅ G_h (Hazewinkel §5 uniqueness carried); Σ_{i=1}^{h−1} p^i/(q−1) = (q−p)/((p−1)(q−1)) = c_h. |
| DP33 | h = 3 dual: optimal affine errors 1 in both directions; mixed values v(D_X^{pq^r}Y(0)), v(D_Y^{p²q^r}X(0)) | statement level. |
| ABA-TN01-TN05 | the run fetched the public Montpellier PDFs: the autograph **has** the disputed readings (Ω_A in TN01; vertex V in TN02; the one-χ-short denominators in TN03, TN04; TN05 faint, compatible with n−1) | **agrees with my checkpoint-01 call** (author's slips, not misreadings). Editorial action, as the run now states: keep the diplomatic reading, add the emendation as a note. |

**Counts (new rows).** 10: confirmed every step 3 (DP25, DP28, DP32); proof read, cited theorems carried 2 (DP29, DP31);
statement level 4 (DP26, DP27, DP30, DP33); transcription status 1 (agrees). Refuted 0.

## 2. What is new
- DP31-DP32 are the first statements on the **actual Cartier dual** of the height-h line: its integral model and its
  directional slopes p^i/(p^h−1). The dual direction slopes sum to c_h, the line's slope; the mean over the h directions of
  G_h × G_h^D is 2c_h/h < c_2 for h > 2. So a naive equal-weight use of the dual loses against height 2. I know of no
  source for DP32; it is in the spirit of Hazewinkel's functional-equation lemma and Lubin-Tate theory.
- DP25 closes the "bigger CM field" substitution for the inspected Lean construction: induced CM types give slope 1/2 at
  inert primes, so a height-h line needs a CM type not induced from the quadratic field.
- DP28 locates the first height-two-specific step in Alpöge's Lean chain: `OneLetterRadiusIdentity.lean`,
  `weightQuantization`, lines 73-76, (p+1)ρ_2 = s.

## 3. Scope of the two proofs
Unchanged: every new finding is unconditional (U). The Lean files are used as sources of definitions and of the place where
height two enters, never as premises.

## 4. Grothendieck's frameworks
DP31 is a statement about biextensions of formal groups by Ĝ_m (SGA 7 VII-VIII, Grothendieck's biextensions; Zink's display
version). DP32 is a statement about the Dieudonné module of the dual (F, V exchanged, Cartier duality: cote 54 scan 5's
"comparer ... avec la dualité de Cartier"). The run names Zink and Katz, not SGA 7. Add "SGA 7 I, Exp. VII-VIII
(biextensions)" as the framework locator for DP31.

## 5. Integration
- **Text of record, cote 54 scan 7** (`text_of_record\pages\54\54_scan007.tex`, line 5): the autograph reading is V (the
  run's observed_autograph column), so `\unsure{V|A}` can be resolved to V, with the note "emendation: A (the diagram
  A → A^{(p)} → A requires codomain A)". This is the one text-of-record change; route it through the second pass.
- **Cote 54 scan 5 line 6 and cote 47 scan 9 lines 26-27, 36-38:** keep the text of record; add edition notes (author's
  slips), as in the checkpoint-01 intake §5.3.
- **Fable suggestion 2** (FABLE_PROGRAM_SUGGESTIONS_20261120.md): add "the dual direction: DP32 (slopes p^i/(p^h−1))".
- **Successor of 34:** Q3e is now precise. The attack: build the Poincaré/theta cocycle on G_h × G_h^D (a Zink biextension
  with nonzero End(G_h) target, DP31's remark) for a mixed CM type (DP25), on DP22's Jac(y² = x^7 − 1) at p = 11, and weight
  the dual directions by the theta construction rather than equally (DP32's remark).

## 6. Hexagon readiness (the five tests of `field_experts\HEXAGON_CANDIDATES.md`)
- **DP1-DP3 + DP32: "sharp p-adic divisibility of invariant derivatives on formal groups of height h and on their Cartier
  duals"** (slope c_h = 1/(p−1) − 1/(p^h−1), optimal constant h−1, floor sum Σ_{h∤j}⌊n/p^j⌋; dual slopes p^i/(p^h−1)).
  1 Complete: yes (DP1-DP3 every step checked; DP32 checked). 2 Self-contained: yes (classical inputs: Hazewinkel, Lubin-Tate,
  Tate; no RH). 3 Stable: **not yet**: the run is still going and its final may extend DP32/DP33; literature search not done
  (Bannai-Kobayashi cover the Lubin-Tate affine case; Katz 1981 the trace-zero case; Hazewinkel's book and Ditters should be
  searched). 4 Checked: intake targeted checks plus my independent computation (115 exact checks); every-page read still
  to do. 5 Of interest now: moderate to high, because it is the exact local mechanism of Alpöge's step 2 (the exponent
  a/p + a/p³ + … with error −1 instead of O(log a) and of the Lean −log_p c − 1).
  **Gate left:** the literature search and the run's final. One gate away after the final lands; worth a candidate entry
  (H06) now.
- The rest (DP25-DP28, DP30) are refutations of recipes for Alpöge's Lean chain: of interest only with a write-up of that
  chain; not post material on their own.

## 7. Prompt updates (successor of DP_MULT)
1. Make the mixed-CM-type dual kernel (Q3e) the main question, with DP22 at p = 11 as the test case and DP9's ceiling
   c_h/c_2 < 1 + 1/p in the prompt.
2. Ask for the theta cocycle as a biextension in SGA 7's sense, so the result is stated in Grothendieck's framework.
3. Ask for a literature check of DP1-DP3 and DP32 (Bannai-Kobayashi, Katz, Hazewinkel, Ditters) before the paper's "new"
   claims.
