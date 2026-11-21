# Intake of AN_GRH (prompt 30), part 2: checkpoint 03, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); it writes "effort not exposed". It is still going. Part 1 is
`INTAKE_AN_GRH_20261121.md` (checkpoint 02).

## 0. What was read, and the scope

- **Return folder:** `research_returns\AN_GRH_checkpoint_03_20261121T0232Z_unzipped`. It was made at the 02:30 UTC
  boundary and was the newest present when I started. The checkpoint 02 folder has been retired.
- **Read:** final/LEDGER.md from "New approaches active at 01:44 UTC" to the end. In final/AN_GRH.tex (4,609 lines, up
  from 2,991):
  - **A18, in full** (lines 2454-2714);
  - **A19, in full** (lines 2715-2932);
  - the statements of A12, A15, A16, A17 and A20.
- **Statement level:** A12, A13 (whose Jacobian order I recomputed), A14, A15, A16, A17 and A20.
- **Changes to part-1 findings:**
  - A01-A06 sit at the same relative positions, with the same lengths to within two lines.
  - The T01-T07 block differs from checkpoint 02 by 48 diff lines, which I could not inspect because checkpoint 02 is
    retired. The ledger records no correction to T01.
  - No ledger entry withdraws or corrects A01-A06 or T01. **Part 1 verdicts stand.**
  - The run's first three-hour review is due at 03:15 UTC and is not in this checkpoint.

## 1. Verdicts on the new findings (A12-A20)

All of them concern route 2, the theta-incidence condition in characteristic 2. Since A05 proves A1 unconditionally,
route 2 is now a question about genus-two curves in its own right, not a gate on A1.

| id | statement (short) | uses | verdict |
|---|---|---|---|
| A12 | a curve-dependent sufficient test: for a subgroup H ⊆ J(F_Q) of index a, #(Θ(F_Q) ∩ H) ≥ ⌈(Q + 1 − ⌊2(a+1)√Q⌋)/a⌉ (Lang-cover/Weil) | none | statement level. |
| A13 | C: y² + y = x + 1/x + 1/(x − 1), ordinary genus two; #J(F₁₂₈) = 16636 = 4·4159; ⟨2, −1⟩ = (Z/4159)^×; at least four theta points of order 4159 | none | **computation: the arithmetic confirmed by my own independent code.** I counted N₁ = N₂ = 3 over F₂ and F₄ from the Artin-Schreier trace criterion with three rational poles, got the Frobenius polynomial T⁴ − T² + 4 (ordinary, since the middle coefficient is odd), and found #J(F_{2^7}) = Res(P, T⁷ − 1) = 16636 = 2²·4159. ord₄₁₅₉(2) = 2079 and ⟨2, −1⟩ has order 4158. The theta-point count was not checked. |
| A14 | the A12 test fails eventually at any one fixed prime, by polynomial growth of the primary part in the extension degree | none | statement level. |
| A15 | on a genus-two base of 2-rank 1, a cyclic étale cover of any odd degree n whose primitive factor has 2-rank 0 separates points; it suffices that Θ carries a point of exact odd order n with ⟨2, −1⟩ = (Z/n)^× | none (Poonen 2007 Prop 2.1, Lemma 2.2, Cor 2.3) | statement level. Its Steps 2-4 (the projector function of degree 2^{ω(n)}, Castelnuovo-Severi induction) are used inside A18 and were not re-read. |
| A16 | over F₈, C: Y² + X²Y = X⁵ + (z+1)X³ + X, R = (z², z): O(R − P) has exact order 15 and lies on Θ; the degree-15 cover has genus 16 and 2-rank 7, primitive factor of dimension 8 and 2-rank 0, ordinary conductor-3 and conductor-5 factors | none | statement level. The run records independent norm certificates. The genus 16 = 15·1 + 1 and the dimension count 8 = φ(15) are consistent. |
| A17 | under M: Q = {q ≡ 5 (8) prime, ord_q 2 = q − 1} has density A/2 (Artin's constant), and n = 3q satisfies ⟨2, −1⟩ = (Z/3q)^× | M (Hooley for the Kummer fields K_n(2)) | statement level. The density is right: q ≡ 5 (8) makes 2 a non-square automatically, so the 2-factor of Artin's product drops out, giving A·(1/4)/(1/2). **Scope:** M only. A_D does not give it. |
| **A18** | **for every genus g ≥ 2 in characteristic 2: if some cyclic étale cover of odd degree n > 1 has a primitive conductor-n factor of geometric 2-rank 0, then point separation holds.** The exceptional "bielliptic" outcome of the A15 projector argument is impossible, because it forces f(P_n) = rφ(n) > 0. On a genus-two base the exceptional case makes the whole new factor ordinary | none | **confirmed for the new part (Steps 1 from "e > 1" onward, and Steps 2-4).** The A15 inputs used at the start are carried as background. Checked: e = 1 is impossible (g(D) ≥ n + 1 > (d − 1)²); the action on Z is free, so g(Z) = g(Z/G) = 1; e = 2 from the reduced fibre in two free orbits; D = C ×_E Z by (GP.4); f(Z_m) = f(E) because odd isogenies are isomorphisms on 2-primary Tate modules; Deuring-Shafarevich gives f(D_m) = 2f(E) − 1 + mr; Möbius inversion gives f(P_n) = r·Σμ(n/m)m = rφ(n) since Σ_{m\|n}μ(n/m) = 0 for n > 1. The genus-two specialization r = 1 (total different 2, each ramified point exponent ≥ 2) is right. |
| **A19** | **for a genus-two curve over F_Q in characteristic 2 and any finite set S of odd primes, every geometric S-primary torsion point on the Raynaud theta divisor is already rational over F_{Q^d}, where Φ^d = 1 on J[ℓ] for ℓ ∈ S** (one may take d = lcm_ℓ \|GL₄(F_ℓ)\|); so the search is finite and exact | none | **confirmed in full.** (FS.5): #(Θ ∩ (Θ + T)) ≤ 2 for T ≠ 0, because two moving degree-two classes are canonical and the degree-one effective divisor K − R₁ is unique. (FS.6): (U^{ℓ^{s−1}} − 1)v = ℓ^{s−1}w for U ≡ 1 (ℓ), by the binomial valuation estimate, with ℓ odd used in j − 2 ≥ v_ℓ(j). Step 3: a non-rational z yields σ with σz = z + T, T ∈ J[ℓ]∖0 fixed by σ, so the ℓ ≥ 3 points z + jT lie in Θ ∩ (Θ + T), a contradiction. The Weil bound and the resultant formula for h_d are right. A Boxall-type statement, credited by the run to Boxall (1995) with the caveat that his theorem text was not inspected. |
| A20 | on the A09 curve Y² + X²Y = X⁵ + X, Θ contains no nonzero geometric 3-primary point | none (A19, A10) | statement level. It is a finite computation over F_{2^20}, by the run's three implementations, not rerun by me. |

**Counts for part 2.**
- Confirmed with every step checked: 2 (A18 in its new part, A19).
- Confirmed by my own computation: 1 (A13, the arithmetic).
- Statement level, no fault found: 7 (A12, A14, A15, A16, A17, A20, and A13's theta count).
- Gaps: 0. Refuted: 0. Changes to part 1: none.

## 2. What is new

- **The theta-incidence question (route 2) is reduced to a sharp geometric form.** By A18, for any genus in
  characteristic 2, one odd cyclic cover with a primitive factor of 2-rank 0 suffices, with no bielliptic exception.
  On genus two (A15 + A18) it suffices to have a theta point of exact odd order n with ⟨2, −1⟩ = units.
  - Examples exist: A09 (order 13), A13 (order 4159, ordinary), A16 (order 15).
  - A19 makes each fixed-support search finite.
  - A20 and A14 show that fixed small supports can fail.
  - The open question is whether every genus-two curve over F̄₂ admits such an n. It is now independent of A1, which A05
    proves.
- **Literature.** A19 is of Boxall type, and the run says so. A18 rests on Deuring-Shafarevich and Castelnuovo-Severi and
  is plausibly new as stated; not searched by me.
- **Against tonight's other runs.** No other run treats theta incidence. GRH_NIGHT checkpoint 02, read in this same
  round, touches cote 149 only through Kummer classes of normal bundles (AG-Q27, AG-Q28) and the class comparison, not
  route 2. A17 is the only use of M here; it is the same Hooley transfer as A02 (GRH_NIGHT NT-A01/NT-A02 states it
  too).

## 3. The scope of the two proofs

- **A17 uses M**, through Hooley for the non-abelian Kummer fields. That is correctly marked.
- Everything else in part 2 is unconditional.
- No finding claims more than its input gives.

## 4. Integration, with the attack each opens

1. **Cote 149, scans 33-38.** No change to part 1's integration: A1 is answered by A05. Route 2 becomes a separate row in
   our anabelian ledger: "theta incidence in characteristic 2". Its proved reductions are A11, A15 and A18, with
   finiteness per support from A19 and examples A09, A13 and A16.
2. **The anabelian successor rows (ANABELIAN_A1_SUCCESSOR A.10, A.14, A.16; B.23, B.28-B.29).** A15 and A18 supersede
   the elliptic-double-quotient exception of Successor A.14. The run's ledger shows that the B.28-B.29 constant-twist route
   keeps a pointing gate.
3. **The attack this opens.** The existence of theta torsion of odd order n with ⟨2, −1⟩ = (Z/n)^× on every genus-two
   curve over F̄₂ is a question about the Raynaud theta divisor, a curve in J, meeting torsion.
   - Over F̄₂ every point of J is torsion, so Θ(F̄₂) consists entirely of torsion points. The question is only about which
     orders occur.
   - Concretely: for a point z ∈ Θ(F_{Q^d}), its order divides #J(F_{Q^d}) = Res(P, T^d − 1).
   - The attack: vary d, and use the distribution of prime factors of Res(P, T^d − 1), cyclotomic-like values of the Weil
     polynomial, to produce a prime q with ⟨2, −1⟩ = (Z/q)^× dividing the order of some z ∈ Θ(F_{Q^d}).
   - Under M, Hooley-type density for the primitive part of #J(F_{Q^d}) as d varies is the analytic input. That is the
     form in which route 2 genuinely meets GRH: an Artin-type problem for the sequence #J(F_{Q^d}), studied for elliptic
     curves by Lenstra and others, with no Kummer field over Q.
   - This is where A17's density result should be aimed, instead of at a fixed curve.
4. **Prompt 30's successor.** Make theta incidence the main question, framed as in item 3. Keep A1 as settled.

## 5. Prompt updates

- State the open question precisely: for every genus-two C/F̄₂, there is an odd n with ⟨2, −1⟩ = (Z/n)^× and a point of
  exact order n on the Raynaud theta divisor. Give A09, A13, A15, A16, A18, A19 and A20 as known data.
- Ask for the Artin-type attack on the orders of points of Θ(F_{Q^d}) as d varies, with the exact L-functions needed:
  Kummer-type fields over the CM field of the Frobenius, which A_D does not reach and M does.
- Ask for a literature check of A18 and A19 (Boxall 1995; Pop-Saïdi; Raynaud's theta divisor; Tamagawa).

## 6. Hexagon readiness

- **A05 (part 1)** remains the candidate. Gates: a literature search and an independent re-proof of Steps 1-2. Nothing in
  checkpoint 03 changes it.
- **A18.** Complete and self-contained, and it has my check of its new part. Not stable: A15's steps are not yet checked
  by an intake, and the run is still moving on route 2. Of interest only once route 2 closes. **Wait.**
- **A19.** Of Boxall type. Fails test 3 (literature) until Boxall 1995 is read. **Not a post.**
- **A13 and A16 examples.** Of interest only as data for the route-2 post. Not posts on their own.
