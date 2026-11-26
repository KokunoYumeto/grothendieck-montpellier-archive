# Intake of KTOWER (prompt 47): checkpoint 11, by diff from checkpoint 09, with the checks behind the paper seed

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max), 22 Nov 2026. The run: GPT-6 Astra (ChatGPT Pro mode). Checkpoint 11 (22 Nov, 00:01 UTC) is the newest
filed return at 18:00 UTC. By the three-hour rule it is the run's last return. Its review at 23:30 UTC found no
movement; a second such review would have stopped the run.

Seed: `<local>/Documents\reports_20261122\paper_seeds\SEED_KTOWER.md`.
Programs and diff: `<local>/Documents\reports_20261122\overnight_intake\KTOWER\`.

## 0. What was read, and what was not

**Diff by content (`diff_09_11.py`).** Checkpoint 09 survives only as its PACKAGE_MANIFEST, with a SHA-256 for each
member. The paper is assembled from 112 sections: 93 are unchanged since 09, 16 are new, 3 changed (framework, open
gates, the ordinary Eisenstein-ideal attempt). All 1080 certificate and Lean-source members of 09 that I compared
(`evidence/higher4`, `evidence/gl2*`, `evidence/lean_chain/source`) are unchanged. Questions, implications and check
events changed. Their old text is not available, so questions were compared with my part-2 notes of 09. Check events
were not compared row by row.

**Proofs read in full (22 Nov):**
- `KTOWER.tex`: 134-282 (source chain), 813-1052 (both coverage theorems), the proofs of K52-K56-K60, K64, K68, K72,
  K76 and K80, 11781-11893 and 11924-12057 (order six), 12107-12194 and 12245-12355 (order five).
- `K17.tex`: 6277-6436 (the criterion over Q(√−7)), 9041-9215 (the pole theorem).
- `ZETA_NEXT` `cm\findings.tex`: the whole file (NC01-NC04).

**Also read:** the abstract and introduction; LEDGER 326-419; the question rows Q1B (truncated in my display), Q1C, Q5,
Q7; the openings of the statements of the other 13 new named results (first 14 lines at most, no proofs); the sign
paragraph KTOWER.tex 13843-13909; in Lean, `NumberU3US.lean`, `CorGKOf.lean`, `KeepLevel.lean`, and the signatures of
`gd`, `unlAll_of`, `mem_KLev`, `level_twist_cyclotomic_pow`, `Hypotheses'`, `HypothesesH'`; Soulé 2003, Lemma 9 and
the definition of r, in the return's text copy.

**Not read:** the U(3) models, native reports and replays; KT-HIGHER4's supporting structural lemmas; the proofs of
e^4/4, of Ihara under Greenberg, of integral generation and of K17's k = 4-12 certificates; the 3 changed sections;
the proofs of the 13 other new results; IMPLICATIONS beyond matched lines. No cited paper other than Soulé's lemma was
opened. Berger-Klosin was not opened. Nothing was compiled.

## 1. What moved since checkpoint 09

- **No new degree.** K_{4k}(Z) = 0 for k ≤ 20 stands. The run says that no higher degree is claimed.
- **The all-weight gate moved twice:**
  - rational components with ω^e of order 6 vanish (KT-ORDER-SIX-COMPONENT-REDUCTION);
  - at order 5 the four class components have total length ≤ 1 (KT-ORDER-FIVE-LENGTH-ONE), so each strict group and
    K-group is cyclic (KT-ORDER-FIVE-STRICT-CYCLIC).

  The gate was "order ≥ 5". It is now "order 5, at most one class of order p, or order ≥ 7".
- **The rest is counted by the run as no movement:** exponent ≤ p at order 5 when p | e; the unit-norm/capitulation
  criterion; an abstract norm system; Iwasawa and tame descriptions of the one possible quintic class; three
  coefficient-method limits; the GMA conormal estimate; the long-root sign for the archive's actual image; the RM
  theta stabilizer.
- **A source gap claimed:** Berger-Klosin, arXiv:2611.19007v1, Lemma 6.8, the sign inference in the M_2 × F case. The
  run calls it a counterexample to an inference and not to their theorem, and says no finite certificate depends on it.
- **Questions:** none changed state. Open: Q1B, Q1C, Q5; open reduced: Q7.

## 2. Verdicts

| Id | Verdict |
|---|---|
| KT-ONECHAR-CLOSED | **source trace confirmed, not compiled.** The nine terms are literally in `CorGKOf.lean:10-18`; line 25 closes hH. The statement of `OneCharU_s` gives the unit criterion as K17 uses it. |
| K17-U3-COVERAGE, K17-U3-GENERAL-COVERAGE, as rechecked in KTOWER | **proof confirmed given the cited theorems, with one omitted step.** `Keep.levelKA_alt` takes `P : Af.Hypotheses'` (ten literature hypotheses). It is closed by P := `hH.toClassicalTheorems`, since `HypothesesH'` extends that record. K17's work note `step17_unit_interface.md:102` knows this hypothesis; neither paper states it. The paper must. |
| K17-GL2-CONDUCTOR | **confirmed given Carayol, Saito, Colmez-Fontaine.** |
| K17-MINUS7-GENERAL-SOURCE | **confirmed given the same inputs:** GD for Q(√−7), both coverages, both normalizations, the cubic twist. |
| **KT-K52-K56-K60-VANISH, KT-K64 ... KT-K80-VANISH** | **deductions confirmed; finite inputs partly recomputed.** Recomputed for e = 26, 28, ..., 40: (a) the characteristic polynomials and comparison values at 7 and 13 on S_{2e+1}(Γ_0(3), χ_{−3}) (16 of 16 agree); (b) J_e on S_{2e+1}(Γ_1(7)) modulo all 16 residual moduli, in my own model (16 of 16 agree, all units; side gcd conditions hold); (c) the gcd step from the run's U(3) values: the part of gcd(C_7, C_13) outside primes < 10^6 comes from M_1M_2^3 in every weight. Carried: the U(3) values over Q(√−3), the U(3) determinants over Q(√−7), VK-PT, K17-U3-RESIDUAL-RING. |
| k ≤ 12 | K17-K12-VANISH as checked in part 4 and part 1. The coverage it rests on is now checked. k = 4-12 carried. |
| **K17-POLE-GENERAL** | **confirmed, every step**, given the cited theorems: the free basis and presentation, the unit cup coefficient, (G.7), the partial fractions, the Laurent separation with maximal pair set and pole orders. This was the open proof under K17-VANDIVER-KERNEL. |
| KT-SEXTIC-CLASS-PRODUCT, -REGULATOR-RATIO-FOUR | **confirmed** (linear disjointness by Minkowski; the three residues recomputed). |
| **KT-ORDER-SIX-COMPONENT-REDUCTION** | **confirmed, bounds carried:** J ≤ (p/3)((log p + κ)/log((p−20)/4))² < 49p/108 for p ≥ 2^31, so p ∤ h_6. |
| **KT-ORDER-FIVE-LENGTH-ONE, -STRICT-CYCLIC** | **confirmed, bounds carried:** h(F) < p²/6; idempotents; the injection of the p-torsion of the strict group; finiteness gives cyclicity. |
| **NC01, NC02, NC03, NC04** | **confirmed given the cited theorems.** The whole constant chain was redone by hand, including the exponents 1/(16384g³) and 28672g⁴. NC02 carries Wei's 75/2 and averaged Colmez. |
| Soulé 2003, Lemma 9 | **refuted, source now read:** r = [F:Q] (text line 74); p = 7, F = Q(√−7), N = 3 gives an element of order 7 > 1 + sup(2, 3) = 4. Refined statement: p ≤ 1 + rN. F = Q unaffected. |
| Berger-Klosin Lemma 6.8 | the run's matrix identities are correct (recomputed by hand: CC^{−t} = diag(−1,1,−1), τ_C(E_13) = −E_13). Whether this contradicts the lemma is **not judged**: the paper was not read. Do not tell the authors on this alone. |
| The other 13 new named results | statement opening read; carried. |

## 3. How it bears, and the attack it opens

- **H18.** The theorem is now checked to a clear boundary: the archive (uncompiled), published theorems, and the
  compact U(3) computations. An independent U(3) computation at one large weight (best e = 40, over both fields) would
  remove the largest unchecked step. The order of the remaining gates: compile and `#print axioms`; U(3); literature.
- **All k (Vandiver).** Orders 1-4 and 6 were closed without Alpöge, by class number < p. Order 5 fails by one factor of
  p: h(F) < p²/6. The regulator lower bound there has only the size (log p)^4, as at order six, and the discriminant
  gives p² in place of p. So analytic size bounds stop here even under GRH, and the next attack has to be arithmetic:
  one Euler-system or Stickelberger annihilator for a single class of order p, or the automorphic criterion with an
  auxiliary prime chosen for (p, e). For order ≥ 7 the same size argument gives worse exponents.
- **Ihara.** The proof chain under Vandiver is now read from end to end at the level of the run's own arguments. What
  is carried is Fukaya-Kato with Wake-Wang-Erickson and the motivic inputs. Every K_{4k} component killed at a prime p
  is a step toward the hypothesis at p. The gate beyond is triple non-vanishing or a positive-rank substitute.
- **H15.** Two of the three gates (a full read of NC02 and NC04; the constants) are closed at the level of a targeted
  proof check. The literature search is left. The next theorem is effective André-Oort for A_g. For Y(1)^n the run
  already records that Binyamini's theorem becomes effective under Alpöge's.

## 4. In the project's terms

- **LM6 A.44-A.45 and the Longue Marche tower:** Theorem B of the seed is faithfulness of the pro-p tower action of
  G_Q on the tripod, the situation of Esquisse d'un programme §2, at every prime where Vandiver holds, so below 2^31.
  The vanishing of K_{4k}(Z) is the statement that the Soulé characters in that action are integrally onto
  (κ_{2k+1}, k ≤ 20).
- **Cote 149:** nothing new on scans 35-36 or 83-85 since 09. Q6A and Q6B stay refuted as recorded, and H16 is
  untouched. Q7 (route 2, AN_GRH A33/A46) gets the theta stabilizer, which is no movement.
- **SA06 B.4a-e and SA07:** NC01 and NC02 are now checked as the effective class-number and height bounds.
- **No claim here comes from RH.** The K-groups use the Galois-cohomological and automorphic interior of the archive.
  CM orbits use quadratic Dirichlet GRH only. Masullo is used nowhere.

## 5. Integration, and the successor prompt

- Register H18: k ≤ 20; the checks of §2; the gates of §3. H06a: "C not evaluated" is superseded by e^4/4 (carried).
  H06b: the pole theorem is read; "every prime below 1000" is superseded by every prime below 2^31 and the Greenberg
  form. H15: two gates closed. (Not edited.)
- Successor: the seed's research question, first. Items to attach as work: write the `levelKA_alt` closure; compile;
  independent U(3) at e = 40; say which conditional inputs of Kaletha-Mínguez-Shin-White the case used; read
  Berger-Klosin 6.8 before anyone is told; check the published DEKM.
- The run's CHECK_EVENTS.tsv has 19 rows (between lines 596 and 708) with the date in the statement-id column. Repair
  the column order before any event is copied into a paper.

## 6. False or superseded in what we hold

1. **KTOWER part 2, §5, my attack on order six, false:** I wrote that the missing input was a relative regulator lower
   bound of order p^{1−ε}, with A. A bound of order log²p suffices and is known (Gras), and no A is needed. The run has
   proved order six.
2. **KTOWER part 2, §4.2 and §5, false:** "level 9" for 3 ∤ e. The Größencharakter α ↦ α^{2e} then has conductor (3)
   of norm 9 in Q(ω), so the theta series has level 3·9 = 27 (by hand).
3. **KTOWER part 2, §3, overstated:** "a uniform proof must remove them by reflection ... a proved fact". What is
   proved is that a fixed auxiliary prime gives non-unit CM factors along progressions. A varying prime or field is not
   excluded.
4. **KTOWER part 1 and register H18, overstated:** "157899 confirmed two ways". My code is independent; the coset
   representatives and normalization are the run's, and the endoscopic identity is a consistency check.
5. **Any wording "K_{4k}(Z) = 0 follows from RH" is false.** Register H06a, H06b and H18 (k ≤ 15) are superseded as
   in §5.
6. **K17 part 4 addendum and H18, "`OneCharU_s` is the gate", incomplete:** coverage also needs
   `levelKA_alt hH.toClassicalTheorems`.
7. **My consult CONSULT_ad855737_ZETA_LABELS.md and its report:**
   - "the exact criterion matched all 1,849 zeros" was never computed. Only the simplified claim was tested (zeros
     1-300, 100001-100400), and it fails at n = 1169 by the file's own account.
   - "every collision is at t < 0" needs simple zeros at t = 0. Without that, t ≤ 0.
   - The (log T)^{-1/4} rate does not follow from a central limit theorem without a rate. The contour estimates of
     Proposition 3 were only sketched.
   - The background run of zeros 1-5000 was never read.
8. **DEG_L part 2 and the unsent prompt 46b:** S-30-S-41 and B22a were read in ledger summaries only. The prompt
   states the rank constraints for all survivors, while the ledger restricts their hypotheses, and "must pass
   S-30-S-36" for Markman's construction is unjustified. Correct 46b before it is sent.
9. **"Statement level" in my intakes of 21 Nov** often meant the register or ledger row only (K17 k = 4-12 and KTOWER
   k = 16-19 among them).
10. **ZETA_NEXT intake §2:** "earlier effective versions assumed GRH (Tsimerman 2012)" and the Binyamini route for A_g
    were from memory, unmarked.

## 7. Hexagon readiness

- **H18 with H06b (one paper):** complete as the run's proofs; checked to the boundary of §2; the run has ended at 11.
  Gates: compiled axioms check, independent U(3), literature search including Hexagon.
- **H15:** complete, final, checked by targeted proof reading. Gate: literature search including Hexagon, with a look
  at Wei's preprint estimate.
