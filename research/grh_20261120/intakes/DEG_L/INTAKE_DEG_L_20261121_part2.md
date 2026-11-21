# Intake of DEG_L (prompt 41), part 2: checkpoint 06, the run's final return, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode). By the user's rule of 20 Nov, **checkpoint 06 (05:17 UTC) is the
final return of DEG_L**. Part 1 read checkpoint 03.

## 0. What was read, and the scope

- **Return folder:** `research_returns\DEG_L_checkpoint_06_20261121T0517Z_unzipped\DEG_L\` (paper now 10,254 lines).
- **Read:** `LEDGER.md` from the 03:00 UTC entry to the end (entries 03:28, 03:42, the scheduled review 01 at 03:47, 04:21,
  04:30, the scheduled review 02 at 04:47), the open rows of `QUESTIONS.tsv`, and the opening paragraphs of T6.23, T6.24 and
  T6.25. For the Hodge line: `reports_20261120\hodge_bridge\HODGE_DIVISION_ATTACK_20261121.md` §0 and §2.3 (Theorem E, Lemma H).
- **Statement level:** all new findings (T6.16-T6.25, B22-B26 with B22a and B25a, S-19-S-41). No proof read in full in this part,
  because my context budget is near its limit; part 1's checked findings (T6.1-T6.3, T6.14, B1, B19, S-01, S-05, S-06) stand,
  and none is withdrawn or corrected in the final.

## 1. Verdicts on the new findings (all statement level)

| Id | Statement (short) | Verdict |
|---|---|---|
| T6.16, T6.17 | the distinct indecomposable switch exists with fixed real cocycle and prescribed globalization; integer balancing in four fixed CM isogeny classes gives bounded period-normalized energy and finite theta data | statement level. |
| T6.18 | the integral coefficient eigenline is the dual maximal-order hull; the four-factor Betti period ideal has index ∏ J_iH_i (H_i = J_i for compatible principal targets) | statement level. |
| T6.19-T6.21 | exact normalized Chow cancellation of the input period presentation; output saturation; one maximal-order output factor gives a uniform primitive-orbit multiplier | statement level. |
| T6.22 | every proper block of 1, 2, 3 output factors, and every mixed divisor kernel, fails to return to the anchor | statement level. |
| T6.23 | intrinsic degree growth for exact integral full-CM orbit projections (fixed good split prime, product principal polarization of volume 1) | statement level. |
| T6.24 | every fixed-order quadratic Weil lattice W_A ∩ H^g(A, Z) (any imaginary quadratic K, dimension g = 2n, signature (n,n)) has a bounded-norm basis | statement level. |
| **T6.25** | sharp √J growth for **every** proper transport from a maximal-order source, and for reduced images of bounded multiplicity (extends B19/B21 of part 1) | statement level. |
| B22, B22a | explicit stabilizer bound, improved to D²/(4(n!)²V_0), so source degree must grow at least like J^{1/4} | statement level. |
| B23, B24 | integral combinations of multiplicity-preserving transports keep an index-J Weil-content ideal; bounded-index polarized CM targets with fixed field, type and volume form a finite set (with a count) | statement level. |
| B25, B25a, B26 | an unbounded-stabilizer escape needs a target-sized intermediate core; calibrations | statement level. |
| S-19-S-25 | named secant and external-product seeds excluded, also under arbitrary derived equivalence and correlated finite actions (Markman source checks) | statement level. |
| S-26-S-29 | a simple gluable balanced real-multiplication object needs Ext¹ of dimension 8 or 9; an amplitude-[0,2] two-sheaf cone branch | statement level. |
| **S-30-S-36** | every simple gluable nonequivariant rank-one balanced-RM object excluded (S-30); integral B-normalizers excluded in every rank; rank divisible by the squarefree RM radicand, vector bundles of rank ≥ 4; all nonequivariant ranks excluded in the principal maximal-local-order, minimal-divisor setting (S-32, S-33); rank-one equivariantly simple seeds excluded for every effective finite action (S-34); rank divisible by the radicand for every effective group, even rank when Euler characteristic 2 (S-35); denominator conditions (S-36) | statement level. |
| S-37-S-41 | further replacement exclusions (named in the open-row list) | statement level. |

**Counts.** About 45 new ids in 14 rows, all statement level. Refuted 0; withdrawn 0.

## 2. What the run settled in the end, and what it left open

**Settled:**
- **T6 (degree as L-value):** the literal T6 is refuted (part 1, T6.2, T6.3); the exact formula is a finite sum of Rallis
  L-values (T6.11 Hecke at 3/2, bounded with no GRH; T6.13 U(2) standard L at 1); the remaining Rallis gates (distinct switch,
  normalization, integral content) are closed (T6.16-T6.18).
- **Transport:** every fixed-source or maximal-order-source transport has Weil-witness degree of exact order √J (B19, B21,
  T6.25), and the source degree must grow at least like J^{1/4} to escape it (B22a). Bounded-index CM targets are finitely many
  (B24).
- **T7 universal:** refuted (S-05, S-06).
- **The semiregular replacement:** a long list of candidate objects is excluded (S-19-S-41); the survivors are constrained
  (rank divisible by the RM radicand, rank ≥ 4 for bundles, higher-rank residual actions, nonsplit or nonsimple lifts,
  virtual-rank-zero or other full characters).

**Left open (the four open rows at the end):** Q-BOUNDS (intrinsic bounded cycle realizations, nonmaximal sources, unbounded
image multiplicities, new joint correspondences); Q-T7-FIXED (the conormal surjectivity of S-02 for a specified smooth image);
Q-DIV (bounded division on generic Weil families); Q-T7-REPLACEMENT (the surviving semiregular objects).

## 3. What DEG_L's final adds to the Hodge line

- **To Theorem E of HODGE_DIVISION_ATTACK (§2.3).** Theorem E proves that on the principal component S_0 of Weil fourfolds over
  Q(ω) the detector degree δ_W is bounded (by Schoen's construction) while J_W → ∞ (Lemma H). The attack cites DEG_L B19/B21 at
  statement level for "fixed-source transport has degree of order √J". DEG_L's final strengthens that citation: T6.25 extends
  the √J law to every maximal-order-source proper transport and bounded-multiplicity reduced image, and B22a shows that even a
  growing source must grow like J^{1/4}. Together with Theorem E this makes the attack's conclusion exact: **bounded division is
  never achieved by transport, and J is not the controlling quantity**; the minimal detector is target-dependent (Schoen's
  Pryms). My part 1 checked B19 in full; T6.25 and B22a are statement level, so the attack's citation should say "B19
  checked, B21/T6.25 statement level".
- **To Proposition O and the semiregular route (S-14).** The attack's Proposition O says that for n ≥ 4 the source must be a
  Hurwitz family of P¹-covers with a large irreducible representation, or a non-curve source such as Markman's semiregular
  sheaves. DEG_L's S-14 is the exact form of the second option (one weakly G-semiregular perfect complex at one fibre, with
  e^{B_0}ch(E_0) = λt + P(θ), gives bounded division on the whole family, with DER4/DER7's explicit multiplier), and S-19-S-41
  are the necessary conditions any such object must meet. **So prompt 46 should take S-30-S-36 as the constraints on its
  semiregular branch**: no rank-one balanced RM object, no integral B-normalizer, rank divisible by the RM radicand, bundles of
  rank ≥ 4, and the denominator conditions of S-36 on the principal locus.
- **Q(i) (§5 of the attack).** DEG_L works over general imaginary quadratic K (T6.24's bounded-norm basis holds for every K), so
  its constraints apply to the attack's Q(i) family as well; it adds no Q(i)-specific construction.

## 4. Scope of the two proofs
Unchanged from part 1: neither A nor M enters the main line; GRH appears only in unused edge bounds (B2). All new findings are
unconditional (U).

## 5. Integration
- **HODGE_DIVISION_ATTACK §2.3:** cite "DEG_L B19 (checked by intake), B21, T6.25, B22a (statement level)".
- **HODGE_BRIDGE_SKETCH:** Route 2: as part 1, plus "transport is exactly √J for every maximal-order source (T6.25); source degree
  must grow like J^{1/4} (B22a)". T7: as part 1.
- **HECKE_DIV intakes:** B19/T6.25 next to P2b; S-30-S-36 next to any semiregular proposal there.
- **Prompt 46 (HODGE_DIVISION, running):** S-14 as the target theorem of its semiregular branch, with S-30-S-36 as the necessary
  conditions; T6.24 as the bounded basis of the Weil lattice.

## 6. Prompt updates (the successor of DEG_L, or prompt 46's next round)
1. **Main question:** construct one surviving semiregular object (rank divisible by the RM radicand; for a bundle, rank ≥ 4;
   nonsplit or nonsimple; full compatible character) on one Weil fibre, or prove that the surviving class is empty, which would
   close S-14 as a route. Start from Markman's fourfold construction: ask the successor to check it against S-30-S-36 at n = 2 (which
   it must pass, since Markman's theorem holds) and to locate what fails at n ≥ 3.
2. **The intrinsic bound:** the target-dependent detectors of HODGE_DIVISION Theorem E (Schoen's Pryms) are the model; ask for
   their analogue in the families where Proposition O allows it.
3. **Do not re-derive** T6, B19-B26 or S-1-S-41; attach the run's paper and check events.
4. An intake read of T6.25, B22a and S-30-S-36 in full is still owed (this part read them at statement level).
5. Model and effort: GPT-6 Astra (ChatGPT Pro mode).

## 7. Hexagon readiness (changes to list; I have not edited the register)
- **The B19 candidate of part 1** ("Weil witnesses of degree Θ(√J) in a CM isogeny class"): the final strengthens it (T6.25,
  B22a) and it now pairs with HODGE_DIVISION Theorem E ("J is not the quantity"). Test 3 is now met on DEG_L's side (the run has
  ended). Gates left: an intake read of T6.25, B21 and B22a; the B6-B8 constants; a literature search. Better posted together with
  Theorem E than alone.
- **S-14 with S-30-S-36** is not post material yet: it is a route with constraints, not a theorem about the Hodge conjecture.
- No new candidate passes the tests.
