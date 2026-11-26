# Paper seeds: the K-groups of Z with Ihara's kernel question, and effective CM orbits

Seed by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at effort
max), 22 Nov 2026. The results come from runs of GPT-6 Astra (ChatGPT Pro mode): K17 (final, checkpoint 08), KTOWER
(checkpoint 11, 22 Nov 00:01 UTC) and ZETA_NEXT (final). "The run's checks" below means checks by that model in that run
(author, root and peer readings by its own agents). "Our checks" means checks by Claude Opus 5.5 at effort high.

Folders, written out once:

- `<KT>` = `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\KTOWER_checkpoint_11_20261122T0001Z_unzipped`
- `<K17>` = `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\K17_checkpoint_08_20261121T0616Z_unzipped`
- `<ZN>` = `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\ZETA_NEXT_final_20261121T0340Z_unzipped`
- `<IN>` = `<local>/Documents\field_experts\intake_20261121\intakes`

Citations are marked in one of three ways:

- "source opened": I opened the source.
- "from memory": I did not open it and no locator of the run supports it.
- "run's locator": the run gives the statement and page. I did not open the source, so a writer must treat it as from
  memory until it has been opened.

---

## Paper 1. K_{4k}(Z) = 0 for k ≤ 20, and the kernel of Galois acting on the pro-p fundamental group of the thrice-punctured line

### Main theorem

**Theorem A (from Alpöge's formalized archive and published theorems).** K_{4k}(Z) = 0 for every 1 ≤ k ≤ 20. So
K_12(Z), K_16(Z), ..., K_80(Z) vanish, besides the known K_4(Z) and K_8(Z).

**Theorem B (no input from Alpöge).** Let p be 2, or an odd prime with p ∤ h(Q(μ_p)^+) (Vandiver at p). Then the fixed
field of the kernel of G_Q → Out(π_1^{et}(P^1 − {0,1,∞})^{(p)}) is the maximal pro-p extension of Q(μ_p) unramified
outside p. For p = 2 it is the maximal pro-2 extension of Q unramified at every finite prime other than 2, with
complexification at the real place allowed. So Ihara's question has answer yes for every prime p < 2^31. For odd p the
hypothesis may be weakened to: X^+ is finite (Greenberg's conjecture for Q(μ_{p^∞})^+). No converse is asserted.

**The link.** For an odd prime p, Vandiver at p is equivalent to K_{4k}(Z){p} = 0 for all k, and it suffices that this
holds for 1 ≤ k ≤ (p − 3)/2. Theorem A and K_{4k}(Z) = 0 for all k are thus steps in one problem, whose full solution
would answer Ihara's question at every prime.

### The largest k at each strength of input

| Input | Range | Standing |
|---|---|---|
| Unconditional published work | k ≤ 2 | Rognes 2000, Theorem 0.1 (K_4; run's locator); Dutour Sikirić, Elbaz-Vincent, Kupers, Martinet, Theorem 6.4 (K_8; computer-assisted; arXiv v1 opened) |
| Alpöge's endpoint theorems alone (RH and Dirichlet GRH) | k ≤ 2 | neither run derives any new vanishing from RH or GRH; do not advertise Theorem A as a consequence of RH |
| The archive's intermediate theorem `OneCharU_s`, published automorphy and class-field theorems, Vandiver below 2^31, and a small certificate | k = 3 | our checks cover the deduction, the coverage proofs, 157899 and the classical certificate (cited theorems and the archive carried) |
| The same, with K17's larger exact Hecke computations | k ≤ 12 | the run's replays; not recomputed by us |
| The same, with KTOWER's computations | k ≤ 15, then **k ≤ 20** | we recomputed, for every k = 13-20, both classical halves and the gcd step, and read every deduction; the compact U(3) halves over both fields are the run's |
| Masullo's Hecke GRH draft | nothing more | not used |
| Every k | open | equivalent to Vandiver at every prime |

### Every hypothesis and input of Theorem A

1. **The Lean archive**, commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of
   https://github.com/CocoSgt/riemann-hypothesis-lean, with its theorems cited as theorems. It is unpublished. Neither
   the runs nor we compiled it or ran `#print axioms`. What is needed, exactly:
   - `UpperTheory.V.Z.J.OneCharU_s` (statement: `.../DenseThresholdCases/NumberU3US.lean`). It bounds the length of the
     strict negative-Tate-twist Selmer group by twice a sum of v_ℓ(tr ρ(s) − t) over the admissible three-dimensional
     Galois representations, under the arithmetic datum `GD`.
   - Its proof `oneCharU_of_katoTwoW_rig_admI_automorphy` (`FOneCharU.lean:75-95`) has nine hypotheses, each supplied
     inside the archive:

     | Hypothesis | Supplied by |
     |---|---|
     | `U3.CohInp` | `cohInp_alt hH.litN hK` |
     | `LemmaM` | `Alg.M.main_holds` |
     | `LemmaM'` | `Alg.M.mprime_holds` |
     | `LemmaP` | `Alg.lemmaP` |
     | `KatoTwoW` | `katoTwoW_of_printsH hH` |
     | `RigidityFirstCase` | `rigIUE_alt hC hH hL hE` |
     | `RigiditySecondCase` | `rigII_a_alt hC hH hL` |
     | `AdmI_s` | `admissible_typeI_even_level_alt hC hH hE` |
     | `AutomorphyUnramifiedCoefficientsAlt` | `automorphyUnramified_of_litN_of_gdEnd hH.litN (ends0_alt hH).1` |

     Here hH = `published_hypotheses_from_patching_alt` applied to `SmallClassNumbers.litN` and `Tf.SR.descWeak`,
     hK = `lemmaK_litN_alt hH.litN`, hC = the first row, hL = `adjoint_lifting_of_cohomology hH`,
     hE = `unlEnd3E (linkedUnlE_alt hH)`. The same inner term is written in `SmallClassNumbers/CorGKOf.lean:10-18`,
     and line 25 closes the record.
   - The definitions `GD`, `Level`, `KillsMu`, `Adm3Alt`, `Adm3U_s`, `Adm2A`, `IsAutCsdA`, `WitA`, `Th.Unl`, `Newform`,
     `algSat`, `FrobEig`, `KLev`. The statement means what the paper says only through these.
   - The lemmas used outside `OneCharU_s`: `ClassNumberThree.lean:gd` (GD for Q(√−3)), `level_twist_cyclotomic_pow`,
     `unlAll_of`, `Keep.levelKA_alt` (automorphy of level one), `mem_KLev`. GD for Q(√−7) is proved by hand in the run.
   - **`Keep.levelKA_alt` is not a closed theorem:** it takes `P : Af.Hypotheses'` (`KeepLevel.lean:95`), a record of ten
     literature hypotheses (`AutomorphicFormHyp.lean:12-22`). It is closed by P := `hH.toClassicalTheorems`, with the
     same hH as above (`HypothesesH'` extends that record, `AfDesc.lean:17`). Neither paper of the runs writes this
     step, though both coverage proofs rest on it. The paper must write it.
   - To close the gap: compile the pinned archive, compile a closed declaration of type `OneCharU_s` (the run's
     `OneCharUClosed_UNCOMPILED.lean` is a candidate), run `#print axioms` on it and on the five lemmas just named (`levelKA_alt` applied to that record), and
     record the toolchain and Mathlib commit.
2. **Comparison with K-theory:** Rost-Voevodsky; Kurihara 1992, Corollary 1.5 and Proposition 3.7; Weibel, *The K-book*,
   VI.8.2, VI.8.3, VI.10.9; Poitou-Tate (run's locators).
3. **Small primes:** Rognes-Weibel 2000, Theorem 0.7 at 2; Hart-Harvey-Ong, *Irregular primes to two billion*, §1 (2),
   Vandiver for p < 2^31 (run's locators).
4. **Coverage of the admissible representations by finite Hecke spaces** (run's locators): Kaletha-Mínguez-Shin-White,
   arXiv:1409.3731v3, Theorem 5.0.5, p. 206; Shin 2011, Theorem 1.2, pp. 1647-1648; Adler-Lansky, arXiv:0807.1528v2,
   Propositions 6.1 and 7.1, with math/0601695; Bellaïche-Chenevier, Remark A.11.8; Carayol 1986, Theorem A, pp.
   410-411; T. Saito 1997, as restated in his Theorem 3; Colmez-Fontaine 2000, Proposition 4.2. Kaletha-Mínguez-Shin-White
   is a preprint with stated conditional inputs. The paper must say which of them the generic pure-inner case uses. For Theorem B (no Alpöge): Gras-Jaulent
   Theorem 2, Hain-Matsumoto, Brown 2012, McCallum-Sharifi §8, Ferrero-Washington, and for odd p Fukaya-Kato, *On
   conjectures of Sharifi*, Theorem 7.2.8 (an author preprint) with Wake-Wang-Erickson (run's locators).
5. **Exact computation.** For each weight e = 2k: characteristic polynomials of T_7 and T_13 on level-one forms for
   compact U(3) over Q(√−3) and on S_{2e+1}(Γ_0(3), χ_{−3}); a gcd leaving a residual modulus; unit determinants
   modulo it for U(3) over Q(√−7) and for S_{2e+1}(Γ_1(7)). No RH, no zero of an L-function and no Masullo.

**Scope of "proved".** The word covers an implication from items 1-5. Item 1 is a source trace. In item 5 the
classical halves and the gcd step are recomputed by us for k = 13-20. The compact U(3) computations are the run's
(recomputed by us at k = 3 only), and so is all of item 5 for k = 4-12.

### What it implies

- The even eigenspaces A^{[−2k]} of Cl(Q(μ_p)){p} vanish for every odd p and every k ≤ 20. With reflection for the
  positive components: for every odd p and every k whose class mod (p−1)/2 has a representative j in [−16, 20],
  K_{4k}(Z){p} = 0 and the same component vanishes at every layer Q(μ_{p^n}).
- The full-domain Soulé character κ_{2k+1} is onto at every odd prime for k ≤ 20 (through κ_41).
- The strict Selmer groups of Q_ℓ/Z_ℓ in the twists Pontryagin dual to these K-groups vanish at every ℓ.
- It does not prove Vandiver at any prime at which it was not known for all components, and it gives no K_{4k}(Z) = 0
  beyond k = 20.

### Why it matters

The algebraic K-groups of Z are known in every degree except 4k, where their vanishing is Vandiver's conjecture. Two had
been proved to vanish, by homology computations in GL_n(Z). Eighteen more follow at once from a new kind of input: a
congruence criterion that came out of the formal proof of RH, whose hypotheses can be checked by finite computations
with modular forms on compact unitary groups. The same class groups decide the best general result known to us on
Ihara's question: how much of the Galois group of Q is seen by the loops on a sphere with three points removed.

### The works it continues, corrects or refutes

- Continues Rognes, *K_4(Z) is the trivial group*, Topology 39 (2000), Theorem 0.1 (run's locator).
- Continues DEKM, *Voronoi complexes in higher dimensions, cohomology of GL_N(Z) for N ≥ 7 and the triviality of
  K_8(Z)*, arXiv:1910.11598v1, Theorem 6.4 (source opened).
- Continues Soulé, *A bound for the torsion in the K-theory of algebraic integers*, Doc. Math. Extra Vol. Kato (2003),
  Theorem 2 and Proposition 4: the new bound is log|K_{2e}(Z)| < e^4/4 for even e (run's locator). It also corrects an
  intermediate statement there: Lemma 9, p. 778 (source opened in the return's text copy, with r = [F:Q]) says that an
  element of order p in Γ ⊂ GL_N(A) has p ≤ 1 + sup(r, N). Its proof takes the p-th cyclotomic polynomial to be
  irreducible over F whenever μ_p is not in F. Counterexample: p = 7, F = Q(√−7), N = 3, an element of order 7 in
  GL_3(O_F). Correct is p ≤ 1 + rN. F = Q is unaffected. The effect on the constants of his Theorems 1-2 for other
  fields has not been worked out by us.
- Continues Alpöge, *Remark*, step 17, and its Lean archive (archive sources opened at the lines cited).
- Continues Ihara's kernel question (Ihara 1986; from memory); Sharifi 2002, *Relationships between conjectures on the
  structure of pro-p Galois groups unramified outside p*, Theorem 1.1, with Brown 2012, which settle odd regular primes
  (run's locators); Sharifi 2007, Theorem 1.2 and Corollary 5.9 (run's locator).
- A possible correction: DEKM v1, Theorem 4.5, pp. 14-16, claims three endpoint vanishings (N = 8, k = 12; N = 9, 10,
  k = 11) that its displayed tables do not support, by an index shift between cone rank and projective dimension
  (source opened). This is a gap in support and not a refutation, and it does not touch K_8. It stays out of the paper
  until the published version (JIMJ 25 (2026)) and the authors' data have been read.
- Literature search, including hexagonmath.org: not done. Make no claim to be first on any statement before it is done.
- **Update 23 Nov 2026 (ad855737, Claude Opus 5.5 at effort high; NIGHT_AFTER_ALPOGE cp13 intake).**
  - Theorem B: the literature gate is done (`reports_20261123/h06b_note/GATE_H06b_ad855737_20261123.md`). The equality
    at irregular primes was open; Sharifi, RIMS Kokyuroku 2120 (2019), p. 222 calls it "a very interesting open
    question". The odd-prime form, with p = 2 left out, was deposited as hexagon:2611.00939 (WB-0006) on 23 Nov.
  - Theorem A: Pintar, hexagon:2611.00829 (21 Nov), gives conditional certificates for k <= 26 under the strict
    Selmer comparison, coverage and simultaneous residual traces. The main session's gate
    (`reports_20261123/h18_note/GATE_PINTAR_20261123.md`) finds that ours is not superseded, since ours is
    single-place and needs no simultaneity.

### The other results, in the order of the argument

1. The closed source chain to `OneCharU_s`, and the unit criterion.
2. The K-theory, Selmer and class-group dictionary.
3. Coverage: compact U(3) of level one, and the two rank-two spaces (levels 3 and 7, with the cubic twist).
4. Dimension and spectrum formulas for both families in every weight, and the endoscopic eigenvalues.
5. K_12(Z) = 0, as a certificate that fits on a page: the U(3) value at 7 is 157899/7^6, with 157899 = 7^6 + 40250, and
   every prime factor of the product of the differences is ≤ 271.
6. The second field Q(√−7), and the certificates through k = 20.
7. The periodic component corollaries and the Soulé characters.
8. The bound log|K_{2e}(Z)| < e^4/4 for every even e ≥ 2.
9. Uniformly in k: A^{[−e]} and K_{2e}(Z){p} vanish when ω^e has order 1, 2, 3, 4 or 6. At order 5 the four components
   have total length at most 1, so each strict group and its K-group is cyclic.
10. Ihara's question at p = 2, under Vandiver and under Greenberg's conjecture. Integral generation by the odd Soulé
    elements is a different question: it is claimed at 2 and at regular primes, and the run finds it false at
    irregular Greenberg primes. Keep the two apart.

### The research question of the prompt

**Prove K_{4k}(Z) = 0 for every k, that is, Vandiver's conjecture at every prime, by this criterion.**

Current gate (KTOWER checkpoint 11, questions Q1B and Q1C): a remaining rational component has ω^e of order 5 or at
least 7. At order 5 at most one class of order p is left among the four components. On the automorphic side three
auxiliary Bernoulli units are needed at once inside the archive's GD (two are constructed), and then only stable
rank-three sources that are not essentially self-dual remain to be excluded.

Routes not yet tried, as far as the ledger and the questions show:

- Choose the auxiliary prime, or several, as a function of (p, e) by Chebotarev in the field cut out by the finitely
  many residual systems. A fixed auxiliary prime fails along progressions (the CM factor N(1 − π^{2e})); a varying one
  is not excluded.
- A family of auxiliary fields Q(√−d) beyond 3 and 7, with the second unit criterion, and an average over d to show
  that some field has no congruence.
- A control theorem in weight (Hida families on U(3)) turning one unit at one weight into units along a class mod p − 1
  without the third unit.
- Order 5: Stickelberger or Euler-system input for the one possible class of the quintic field. The size bounds, unit
  norms and reciprocity pairing were tried and do not decide it.

The companion question for Theorem B: Ihara's question at primes where neither Vandiver nor X^+ finite is known. The
gate is arithmetic non-vanishing of the triple cup/Massey product, or a substitute in positive Iwasawa rank.

### Proof files, programs, and who checked

| Result | Proof (file, lines) | Programs | The run's checks | Our checks |
|---|---|---|---|---|
| `OneCharU_s` closed | `<KT>\KTOWER.tex` 134-282 | `<KT>\evidence\lean_chain\` | source extraction, read | source chain traced one level 21 Nov, statement and `CorGKOf.lean` reread 22 Nov; not compiled |
| Unit criterion | `<K17>\K17.tex` 2804-2852 | none | proof readings | targeted proof check, 21 Nov |
| Criterion for Q(√−7) | `<K17>\K17.tex` 6277-6436 | none | proof readings | targeted proof check, 22 Nov |
| Coverage | `<KT>\KTOWER.tex` 813-1052 | none | recheck with sources | targeted proof check, 22 Nov; cited theorems carried |
| 157899 | `<KT>\KTOWER.tex` 426-524, 1452-1475 | `<KT>\evidence\unitary_audit\` | second method | computation, 21 Nov: `<IN>\KTOWER\u3_second_check.py` (the run's coset representatives and normalization) |
| K_12 = 0 | `<K17>\K17.tex` 3807-3875 | K17's `evidence\work\hecke_level_one\` | readings, replays | targeted proof check and independent classical computation, 21 Nov |
| k = 4..12 | `<K17>\K17.tex` 4763-4829, 5132-5229, 6145-6242, 7002-7080 | `<K17>\evidence\work\hecke_uniform\` | readings, replays | carried |
| k = 13..15 | `<KT>\KTOWER.tex` 2487-2749 (theorem 2674) | `<KT>\evidence\higher4\`; `<KT>\evidence\gl2_uniform.py`; our four scripts named below | readings, replays | targeted proof check; classical halves and gcd step recomputed, 22 Nov; U(3) halves carried |
| k = 16 | `<KT>\KTOWER.tex` 3143-3320 | the same | readings, replays | the same |
| k = 17, 18, 19 | `<KT>\KTOWER.tex` 3387-3518, 3551-3688, 3720-3887 | the same | readings, replays | the same |
| k = 20 | `<KT>\KTOWER.tex` 3926-4091 | the same | readings, replays | the same |
| Components | `<KT>\KTOWER.tex` 4093-4128; `<K17>\K17.tex` 10975-11082 | none | readings | carried; Bernoulli numerators recomputed 21 Nov |
| e^4/4 | `<KT>\KTOWER.tex` 2357-2470 | none | readings | carried |
| Orders 1-4 | `<KT>\KTOWER.tex` 11699-11758 | none | readings | targeted proof check, 22 Nov; class-number bounds carried |
| Order 6 | `<KT>\KTOWER.tex` 11781-11844, 11846-11893, 11924-12057 | none | author, root, two peer readings | targeted proof check, 22 Nov; the bounds of Gras, Louboutin, Le and Moser-Payan carried |
| Order 5 | `<KT>\KTOWER.tex` 12107-12194, 12245-12355 | none | author, root, peer readings | targeted proof check, 22 Nov; Schoof-Washington Corollary 2.7 and Louboutin carried |
| Ihara at 2 | `<K17>\K17.tex` 8622-8826 | none | readings | targeted proof check, 21 Nov |
| Ihara, the pole theorem | `<K17>\K17.tex` 9041-9215 | none | readings | targeted proof check, 22 Nov, every step; Hain-Matsumoto, Brown, McCallum-Sharifi and Sharifi's averaging lemma carried |
| Ihara under Vandiver | `<K17>\K17.tex` 9305-9444, 9446-9455 | none | readings | targeted proof check, 21 Nov, given the pole theorem (now checked) and Fukaya-Kato, Wake-Wang-Erickson |
| Ihara under Greenberg | `<K17>\K17.tex` 9678-9971 | none | readings | carried |

Our programs of 22 Nov, in `<local>/Documents\reports_20261122\overnight_intake\KTOWER\`:
`j_alt_classical.py`, `j_alt_26_30.py` (the alternate classical determinants modulo every residual modulus),
`gcd_check.py`, `gcd_check_32_36.py` (the gcd step, from the run's U(3) values). The initial-field classical halves:
`<IN>\KTOWER\gl2_check.py`.

Check events: `<IN>\K17\INTAKE_K17_20261121*_CHECK_EVENTS.tsv`, `<IN>\KTOWER\INTAKE_KTOWER_2026112*_CHECK_EVENTS.tsv`,
and `<K17>\CHECK_EVENTS.tsv`, `<KT>\CHECK_EVENTS.tsv`.

### LaTeX sources to attach

- `<KT>\KTOWER.tex` and `<K17>\K17.tex`, with the programs named above, `<KT>\evidence\higher4\` and both
  CHECK_EVENTS files.
- arXiv: 1910.11598 (DEKM); 1409.3731 (Kaletha-Mínguez-Shin-White); 0807.1528 and math/0601695 (Adler-Lansky);
  math/0501236 (Sharifi 2007); 1102.1312 (Brown 2012); 1904.00179 (Brown). Hart-Harvey-Ong, Sharifi 2002,
  McCallum-Sharifi 2003 and Gras-Jaulent 2009 have arXiv versions (from memory; identifiers to be looked up).
- The Lean source closure, from `<KT>\evidence\lean_chain\source\` (for the model only).
- Our intakes, so that the check events are copied and not invented, and our programs.

### Not for GitHub (someone else's)

- In `<KT>\evidence\`: all of `lean_chain\source\`; every `.lean` under `unitary_audit\source\`,
  `unitary_audit\host_sign_source\`, `unitary_audit\projector_source\`, `main_gate\source\`,
  `main_gate\flatness_source\`, `main_gate\host_review_source\`; every third-party PDF, HTML, text or page image under
  `lean_chain\primary\`, `lean_chain\low_order_source_pages\`, `lean_chain\thorne_scope\`,
  `lean_chain\determinant_normalization\primary\`, `unitary_audit\primary\`, `unitary_audit\greenberg_cyclic_scope\`,
  `unitary_audit\*\primary*\`, `main_gate\literature\`, `main_gate\*\primary\`; `Soule_2003.txt`; `soule_pages\`;
  `geometry_tower\Mochizuki1999_supplied_text.txt`; `geometry_tower\SGA1_supplied_text.txt`; any file named in
  `PRIMARY_SOURCE_EXCLUSIONS.json` that is present; the same files again under `_from_earlier_checkpoints\`.
- In `<K17>\evidence\work\`: all of `lean_candidates\`, `hecke_coverage\interface\`, `hecke_uniform\source\`, the
  `.lean` files of `hecke_level_one\` and `quantitative_sources\`, `CorGKOf.lean`, `point_hv_composition.lean`;
  `k12_source_data\` (the authors' Voronoi data, program output and page image); the copy under
  `_from_earlier_checkpoints\`.
- Alpöge's remark, DEKM's and every other paper's PDF, Masullo's draft.
- Ownership was decided by folder and file name, not by opening each file. Anyone pushing a file not named here checks
  it first.

### Workbench

**Algebraic K-theory of the integers and cyclotomic fields** (with Galois actions on fundamental groups).

---

## Paper 2. Effective lower bounds for the Galois orbit of every CM point in A_g (Hexagon candidate H15)

> **Update, 23 Nov 2026** (NIGHT_AFTER_ALPOGE cp11 Parts A and C intake by ad855737, Claude Opus 5.5 at effort high; field_experts/intake_20261121/intakes/NIGHT_AFTER_ALPOGE/INTAKE_NIGHT_AFTER_ALPOGE_20261123_cp11_partsAC.md section 6). The main theorem below is superseded by the run's A.ORBIT: every CM point x of A_g satisfies |Gal x| >= c_g D_x^{1/(4g)}, D_x the discriminant of the centre of End(A_x), with the constants c_g, W_g, C_g of the run's main.tex section 1, all centre orders and products; inputs Gaudron-Remond 2023 and Faltings in place of GR14 Polarisations. The research question changes too: effective Andre-Oort for A_g is answered by Jaswal (Hexagon 2611.00339) with Cureton-Thorner (Hexagon 2610.00200), if those preprints hold; the open question is an unconditional or improved orbit exponent, and the effective format route (Binyamini, Log-Noetherian section 10.4).

### Main theorem

Input: RH for the L-functions of quadratic Dirichlet characters, a special case of Alpöge's Dirichlet GRH, whose Lean
proof is unpublished and is cited as a theorem. Only the absence of a real zero near 1 is used. No Masullo, no GRH for
CM fields, no individual Colmez conjecture. Every other input is published, or is the preprint of X. Wei named below.

For r ≥ 1 put

- c_r = (2/(173(2π)^r(2r)!))·γ_r, with γ_1 = 1 and γ_r = (4(r−1)/e)^{r−1} for r ≥ 2 (here e = exp(1));
- a_r = 2^{r−1}(75/2 + 16·r!), b_r = 4r(2^r − 1);
- α_r = 2^{10}r^3, B_r = (14r)^{64r^2}, η_r = 1/(16α_r), U_r = a_r + (b_r+1)/log 3, q_r = 2 + r/(2α_r),
  s_r = 2·3^{4r^2};
- f_r = c_r^{1/(2α_r)}/(2^{r/α_r}B_rU_r^2), ℓ_r = min{1, f_r(eη_r/q_r)^{q_r}}.

For g ≥ 1 put M_g = max_{r≤g} ℓ_r^{−16α_r}, A*_g = max_{r≤g} a_r, C*_g = max_{r≤g} b_r,
V_g = 1 + g(A*_g(log M_g + 16α_g) + C*_g), T_g = M_g^g(B_gV_g^2)^{4gα_g}, P_g = 28gα_g = 28672g^4.

**Theorem.**

1. Let x be a CM point of A_g(Q̄), A_x its principally polarized abelian variety and R_x = Z(End_{Q̄}A_x). Then
   |Gal(Q̄/Q)·x| ≥ s_g^{−1} T_g^{−1/P_g} |disc R_x|^{1/P_g}.
2. If A is geometrically simple of dimension g with End A = O_E, E a CM field of degree 2g, every field over which A
   and its endomorphisms are defined has degree ≥ ℓ_g D_E^{η_g}. For polarized A the field of moduli has degree
   ≥ (ℓ_g/s_g) D_E^{1/(16384g^3)}.

Every constant is computable. They are astronomically bad and not optimized. The theorem covers nonsimple points and
nonmaximal orders. It does not by itself make the André-Oort conjecture effective.

### What it implies

- For any bound d, an explicit bound on |disc R_x| for all CM points of A_g defined over a field of degree ≤ d. A
  finite list of CM points of bounded degree becomes computable in principle, given the standard finiteness
  algorithms for polarized lattices with given endomorphism order.
- The arithmetic input of Tsimerman's proof of André-Oort for A_g is effective. The o-minimal counting and reduction
  steps remain.

### Why it matters

Tsimerman proved that CM abelian varieties have large Galois orbits, the last missing input of André-Oort for A_g. His
constant could not be computed, because Siegel's lower bound for class numbers cannot be. A proof of GRH for quadratic
characters removes exactly that obstruction: Stark showed in 1974 that the only possible bad zero of the relevant
Dedekind zeta function comes from a quadratic subfield.

### The works it continues, corrects or refutes

None corrected or refuted. All locators are the run's, and none was opened by me.

- Tsimerman, *The André-Oort conjecture for A_g*, Ann. of Math. 187 (2018): Theorems 1.2, 4.2, 5.2 (p. 385), §2.2
  (p. 382), Lemma 4.1 (p. 384). Continued: the constants become effective.
- Stark, *Some effective cases of the Brauer-Siegel theorem*, Invent. Math. 23 (1974): Lemmas 3, 4 (11), 7, 8, 9,
  pp. 139-146; Theorem 1′, p. 148.
- Garcia-Lee, arXiv:2007.10313v4, §3, pp. 16-17: the same extraction of Stark's constant, so do not claim 173 as new.
- Louboutin, Canad. J. Math. 53 (2001), Theorem 1(1), p. 1195; (21), p. 1200.
- Yuan-Zhang, Ann. of Math. 187 (2018), Theorem 1.1, p. 535 (averaged Colmez; also proved by Andreatta, Goren, Howard,
  Madapusi Pera in the same volume, from memory).
- X. Wei, *Smallness of Faltings heights of CM abelian varieties*, arXiv:2111.00617v1, Proposition 5.3 and proof,
  pp. 19-20. A preprint: the constant 75/2 comes from its proof, so the paper should reprove that estimate.
- Gaudron-Rémond, *Polarisations et isogénies*, Duke 163 (2014), Theorem 1.4, p. 2060; *Théorème des périodes*,
  CMH 89 (2014), Theorem 1.1, p. 345.
- Rémond, *Variétés abéliennes et ordres maximaux*, RMI 33 (2017), Theorems 1.1 and 1.2.
- Binyamini, *Some effective estimates for André-Oort in Y(1)^n*, arXiv:1809.05302v2, §1.2 Theorem 1: effective for
  Y(1)^n once the exceptional quadratic field is excluded, hence under Alpöge's theorem.
- Earlier orbit bounds under GRH: Tsimerman 2012 and Ullmo-Yafaev 2015 (from memory).
- Literature search, including hexagonmath.org: not done. A published effective version under Artin or Dedekind GRH,
  or through an exceptional-zero hypothesis, would narrow what is new.
- **Update 23 Nov 2026 (ad855737): the literature pass is done.** The note is `reports_20261123/h15_note/h15_note.pdf`
  (8 pp.) with RECORDS.md, built on A.ORBIT (exponent 1/(4g)).
  - Effectivity alone is no longer new. Banks (arXiv:2610.15483, after an OpenAI manuscript) proves
    (1 - beta) log q >= 3.0e-3 for every real zero of every real primitive L(s, chi) (abstract read). Cureton-Thorner
    (hexagon:2610.00200) and Liu (hexagon:2611.00080) give similar zero exclusions.
  - What is new is the explicit exponent and constant for every centre order. Gaudron-Remond 2023 Thm 1.9(5) alone
    gives exponent 1/(4g^2); their Thm 1.8 gives 1/(2g).
  - Jaswal (hexagon:2611.00339) Prop. 3.3 has exponent 1/(16 t s n_T(n_T - 1)) in the Galois-closure discriminant.
  - Tsimerman 2018: the orbit bound is Thm 5.1 in arXiv v5, with exponent < 1/(4 c_g) and an ineffective constant.

### The other results, in the order of the argument

1. For every normal K ≠ Q, κ_K = Res_{s=1}ζ_K > 1/(173 log D_K). For every field of degree n,
   κ_K > 1/(173·n!·log D_K).
2. Effective Brauer-Siegel for normal fields, both sides, with Louboutin. Also h_K ≤ √D_K(1 + ½ log D_K)^{n−1}
   (classical in form).
3. For a CM field E of degree 2g, h_E ≥ h_E/h_F > c_g D_E^{1/4}/(log D_E)^g. For imaginary quadratic fields
   h > √D/(173π log D).
4. For A with CM by O_E, any type: h_Falt(A) ≤ a_g log D_E + b_g.
5. The orbit bound for maximal orders and simple A, by counting ideals below the isogeny bound.
6. The orbit bound for all CM points, by Rémond's maximal-order replacement.
7. A scope section: what is effective in André-Oort afterwards and what is not.

### The research question of the prompt

**Is André-Oort for A_g effective under Dirichlet GRH: can the special subvarieties maximal in a given subvariety
V ⊂ A_g be bounded by a computable function of g, deg V and the field and height of V?**

Current gate: item 6 supplies the orbits. Still needed are an effective point count on the definable set
π^{-1}(V) ∩ F and an effective reduction from positive-dimensional special subvarieties to points.

Routes not tried in the run (the first three from memory):

- Binyamini's point counting for foliations, applied to the Gauss-Manin foliation on A_g, with Galois orbits and
  heights as input.
- Effective Pila-Wilkie for sharply o-minimal structures (Binyamini, Novikov, Zak).
- The height bound for CM pre-images (Pila-Tsimerman) made explicit with item 4.
- The test case A_2, or a Hilbert modular surface, with V a curve, where only special points occur.

### Proof files, programs, and who checked

All our checks are targeted proof checks with the cited theorems carried.

| Result | Proof (file, lines) | Programs | The run's checks | Our checks |
|---|---|---|---|---|
| Residues (NX01, NX02) | `<ZN>\normal\findings.tex` 52-124 | `<ZN>\audit\check_stark_constant.py` | author, root and peer readings | 21 Nov, every step; 8C_4 recomputed |
| Brauer-Siegel (NX03, NX04) | `<ZN>\normal\findings.tex` 126-194 | none | the same | 21 Nov |
| Class numbers (NC01) | `<ZN>\cm\findings.tex` 20-101 | `<ZN>\cm\constant_audit.py` | the same | 22 Nov, whole constant chain |
| Height (NC02) | `<ZN>\cm\findings.tex` 117-181 | the same | the same | 22 Nov, proof read; Wei's estimate and averaged Colmez carried |
| Simple orbits (NC03) | `<ZN>\cm\findings.tex` 224-292 | the same | the same | 22 Nov, every step |
| All orbits (NC04) | `<ZN>\cm\findings.tex` 305-415 | the same | the same | 22 Nov, every step |

Check events: `<IN>\ZETA_NEXT\INTAKE_ZETA_NEXT_20261121_CHECK_EVENTS.tsv`, `<IN>\KTOWER\INTAKE_KTOWER_20261122_cp11_CHECK_EVENTS.tsv` (rows
NC01-NC04), and `<ZN>\cm\CHECK_EVENTS.tsv`.

### LaTeX sources to attach

- `<ZN>\normal\findings.tex`, `<ZN>\cm\findings.tex`, both `bibliography.tex`, the two programs and their outputs,
  `<ZN>\CHECK_EVENTS.tsv`, and our intake.
- arXiv: 2111.00617 (Wei); 2007.10313 (Garcia-Lee); 1809.05302 (Binyamini); 1506.01466 (Tsimerman), 1507.06903
  (Yuan-Zhang), both identifiers from memory. Gaudron-Rémond and Rémond: author versions (PDF only, as far as known).

### Not for GitHub (someone else's)

`<ZN>` holds no PDF, HTML or Lean file by extension. Keep out: every paper fetched for the prompt (all those above),
the Stark scans at GDZ, Alpöge's remark and Lean sources, and any quoted source text under `<ZN>\audit\`.

### Workbench

**CM abelian varieties and the André-Oort conjecture** (explicit class-number bounds).
