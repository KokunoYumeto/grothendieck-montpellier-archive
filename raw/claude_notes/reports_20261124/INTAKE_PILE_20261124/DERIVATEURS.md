# The Dérivateurs cluster of the intake pile, 24 Nov 2026: FREX, DER_LOCALIZERS, RESIDUE, S2COUNT, REVLOC, BISITE

Claude Opus 5.5 at effort high, a cluster reader launched by the main session 329fb1e6 (Claude Opus 5.5 at effort max),
24 Nov 2026 from about 21:15 UTC. Brief: `reports_20261124/INTAKE_PILE_20261124/BRIEF.md`. All six runs are GPT-6 Astra
(ChatGPT Pro mode), 11-18 Nov 2026, unrefereed outside this project. No run folder was changed; no git; no paid API.
Work file: `agent_notes/20261124T2112Z_Intake_pile_D_rivateurs_cluster_NOTES.md`. My programs and their outputs:
`INTAKE_PILE_20261124/DERIVATEURS_checks/` (three Python scripts, run with `python -I -B`).

**None of the six runs has a return newer than its last intake.** What this pile adds: (1) the first proof-level reading
and two computations for S2COUNT, whose earlier intake (17 Nov) read only titles; (2) a priority correction for the
footnote-56 chain (BISITE A.32 came first, on the literal axioms); (3) targeted checks of rows no intake had followed
(FREX A.13, REVLOC F.1, G.7, BISITE A.32, G.7, S2COUNT CD:alltargets, RESIDUE A.5 by computation, DER_LOCALIZERS B.4 by
computation); (4) a reading of where the cluster stands as a whole, for the conference.

Abbreviations: "Opus-max intake 19 Nov" = `derivateurs_companion_20261109/pro_prompts_max_20261112_work/INTAKE_FREX_DERLOC_REVLOC_RESIDUE_20261119.md`
(sub-agent a8081d1b, Claude Opus 5.5 at effort max); "Opus-max intakes 20 Nov" = the same agent resumed,
`field_experts/intake_20261120/intakes/{DER_LOCALIZERS,RESIDUE,REVLOC}/INTAKE_*_20261120.md`; "Fable intake 17 Nov" =
`.../INTAKE_S2COUNT_REVLOC_20261117.md` (a5ead5c6, Claude Fable 5.2 at effort high); "BISITE combined review" =
`derivateurs_companion_20261109/pro_reviews_20261110/7_BISITE/COMBINED_REVIEW.md` (ac003b3d, Claude Fable 5.2 at the
session's default effort, none set at launch).

## The cluster's most interesting items, ranked by usefulness

1. **Exactness of colimits and amenability are independent, both ways, for Fraïssé categories (FREX A.9-A.11, A.17-A.19,
   A.31-A.33).** The category of finite posets with an independent linear order is exact over every ring (so total), with
   all the structural hypotheses (Rig), (SA), (FA), (FA∅), (St), (Op), and its automorphism group is *not* amenable: the
   integer-valued signed weights of A.10 on linear extensions give an exact averaging (A.9) that no positive measure can
   give. Finite F₂-vector spaces with an independent order of their non-zero vectors are total, satisfy every structural
   hypothesis including (WEI), (Fin), have an amenable group, are exact over Q (A.33), and are *not* exact over F₂ or Z
   (a five-map parity identity, A.18). Why it matters: it separates, in the setting where Kechris-Pestov-Todorcevic
   dynamics and Grothendieck/Oberst/Isbell-Mitchell exactness of colimits meet, the two averaging notions (signed integer
   versus positive), and it is the cleanest statement of the difference between the conditions (CT) and (CC) of the
   companion. Check status: every step of A.9-A.11, A.17, A.18, A.33 followed and two programs run by the Opus-max intake
   19 Nov; not rechecked here. Location: FREX `sections/A.tex` (labels `A:signed-averaging`, `A:poset-weights`,
   `A:ordered-posets`, `A:ordered-vector-*`). Hexagon candidate (with item 2).

2. **Exact over every F_p but not over Q (FREX C.10-C.13), and the field profile of the cocycle classes.** For `r ≥ 2`
   and a countable abelian group Λ, the category `A_r(Λ)` of finite ordered Λ-valued `r`-cocycles is exact over F_p iff
   `p` is bijective on Λ, over Q iff Λ is torsion, over Z iff Λ = 0; `A_2(Q)` is exact over every prime field and not over
   Q, with `BA ≃ K(Q, 2)` (not total). This refutes the "all primes ⇒ Q" implication the prompt asked about (C.4); the
   version for *total* categories stays open, with eight construction families excluded (C.22-C.31; C.27: for
   Grothendieck assemblies of Kan simplex categories over an integrally exact base, total ⇔ exact over Z). Checked: the
   Opus-max intake 19 Nov followed C.10-C.13 step by step. Location: FREX `sections/C.tex`, `C4_addendum.tex`.

3. **A finite monoid whose classifying space is `⋁_{n≥2} Sⁿ`, and what it does to Grothendieck's finite-test programme
   (S2COUNT A.M0-A.M9, B:main, B:smallmonoids, B:smallcategories, CD:alltargets).** The six-element monoid
   `M_1 = {1, x00, x01, x10, x11, y}` with `vw = x_{row v, col w}` (Sweeney 2025, Example 5.2, with an identity) has
   `BM_1 ≃ ⋁_{n≥2} Sⁿ` by explicit sphere maps; `M_r` gives `⋁_n (Sⁿ)^{∨ r^{n−2}}`. Hence `[BM_1, S²]` and `[BM_1, S³]`
   have the cardinality of the continuum, so `C ↦ [BC, S²]` on finite categories is not a sequential colimit of
   representables by finite categories; six arrows is the least possible. More: a CW type `Y` has countably many
   classes on every finite-category test iff `π₀Y` is countable and each component is a Postnikov piece with countable
   finite-complex tests (CD:alltargets). Why it matters: it settles the S² question of V ms. 43-46, 51-52 and VII ms. 121
   negatively and exactly, by a five-line computation anyone can check; the monoid is the smallest finite category with
   a non-truncated classifying space. **Checked in this pile:** A.M1 (every face identification of the sphere maps
   followed), A.M3 by computation (my program: Betti numbers and F₂, F₃ dimensions of the bar complex agree with
   `H_n = Z^{r^{n−2}}` for `r = 0, 1, 2` up to degree 5, 5, 4; no 2- or 3-torsion), B:main, B:smallcategories (the case
   analysis), CD:wedgecriterion, CD:alltargets; the monoid census behind B:smallmonoids recomputed (item 8). External
   inputs not opened: Miller's Theorem A (Sullivan conjecture), Sweeney 2025 Thm 2.7, Serre 1953. Location:
   `derivateurs_companion_20261109/pro_prompts_max_20261112_work/S2COUNT/S2COUNT_final_20261116T0841Z_unzipped/S2COUNT/sections/A_agent.tex`,
   `B_root.tex`, `CD_agent.tex` (lines 300-440). Hexagon candidate (see the S2COUNT section for what to verify first).

4. **XVI ms. 118, footnote 56 and Corollaire 7.7.2, settled in all hypotheses (BISITE A.32 → RESIDUE B.2-B.4 → REVLOC
   F.1, F.1.1 → DER_LOCALIZERS A5.1-A5.4).** Absolute Theorem A (Loc 3) does not give relative Theorem A (Loc 3 bis):
   for the literal Loc (1)-(3) with moderate saturation (BISITE A.32, a triangle of finite groupoids over `BC₂`); for a
   strongly saturated class (RESIDUE B.3, `W_circ`; REVLOC F.1, `W†`, with Loc (8) and (9) as well); Loc (6′ a) + Loc (8)
   suffice without Loc (9) (REVLOC F.1.1, DER_FOLLOWUP G.9); Loc (8) is needed (DER_LOCALIZERS A5.3: the accessible
   class `W_fin` with Loc (1)-(3), (6′ a), (1 ter), (9) fails relative Theorem A over the discrete category N). So Loc
   (6′ a) and Loc (8) are each necessary and Loc (9) is irrelevant. Corollaire 7.7.2 is true as
   printed; of footnote 56, 'pas prouvé' was right and 'probablement faux' is not borne out, except when Loc (6′ a)
   or Loc (8) is dropped [corrected 25 Nov 2026; the earlier wording is in DERIVATEURS_before_fn56_fix_20261125.md]. Why it matters: it is the axiomatics of fundamental localizers (Grothendieck, Cisinski 2006), and the
   companion's reading of XVI. Checks: RESIDUE B.2-B.4 and DER_LOCALIZERS A5.2, A5.3 step by step (Opus-max intake 19
   Nov); REVLOC F.1 and BISITE A.32 step by step **in this pile**; the A5.3 homological key step re-derived here.
   Hexagon candidate (one note for the whole chain). **Priority correction:** see Problems, item P1.

5. **The reverse-excision dichotomy (DER_LOCALIZERS A.1-A.9, A2.1-A2.14, with REVLOC A-C, G).** At the level of
   fundamental localizers Grothendieck's strengthened reverse axioms of 105/052 (W7 bis, W8 bis, XII W(7 bis), XVI Loc
   (6 a, b, c), all equivalent, A.3) only say "reversible", and there is an accessible reversible localizer that is not
   a homology localizer `R(L)`: the sphere-null `W_S`, accessible in ZFC (REVLOC G.6-G.7, checked here). At the level of
   derivators either one-sided unrestricted half of Der 6 forces a homology localizer (A2.4, A2.9: Brown representability
   in the pointed envelope). Checks: A.1-A.5, A.7, A2.4, A2.9, A2.12-A2.14 followed by the Opus-max intakes 19-20 Nov;
   REVLOC A.1, A.3, A.5, B.1-B.4, C.1, G.5 followed 20 Nov; REVLOC G.7 followed here. The external Bousfield and
   Cisinski-Tabuada inputs have not been opened by anyone outside the runs.

6. **The predimension family classified (FREX D.1-D.12).** All `C(k, a, b)` are total; exact over any non-zero ring,
   amenable and extremely amenable all hold exactly when `b ≥ (k−1)a`. For `b < (k−1)a` the category is total and exact
   over no ring (a further family of total, non-exact categories beside TOTAL_EXACT_2's `C_δ`). Checked D.3-D.6 (Opus-max
   intake 19 Nov). Useful as a stock of examples.

7. **Totality of the strong embedding category is an invariant of the topological group `Aut(M)` (FREX A.24-A.26, G.12);
   exactness already was (A.1).** Checked step by step 19 Nov. Useful: it turns combinatorial questions about Fraïssé
   classes into questions about non-archimedean groups.

8. **The census of small monoids (RESIDUE A.5, S2COUNT B:smallmonoids).** Up to isomorphism there are 1, 2, 7, 35, 228
   monoids of orders 1-5; every monoid of order ≤ 5 has `BM ≃ BH` for a finite group `H`, except the rectangular-band
   monoid `1 ⊔ (2×2)`, with `BM ≃ S²`. **Checked here by computation:** my enumeration gives 1, 2, 7, 35, 228 iso classes
   (and 1, 2, 11, 156, 4122 tables with the identity fixed, equal to S2COUNT's C++ counts), and exactly one of the 228
   monoids of order 5 has non-zero rational homology in degrees 1-3 (the rectangular band, `H₂ = Q`). Marginal alone; it
   anchors items 3 and 4 (the "five-element monoid of type S²" of STRATA, PATHS, BISITE B.21, RESIDUE A.1).

9. **Interval generation fails for integral homology (DER_LOCALIZERS B.3, B.4, B.10)**, Grothendieck's hope at 105/020:
   a 17-vertex graph map detected by `K(S₃, 1)`. Checked step by step 19 Nov; the group-theoretic step confirmed here by
   program. Marginal-useful (a clean negative answer to a manuscript question).

10. **FE-1's odd-characteristic exactness is false (FREX A.13):** finite sets with an equivalence relation and an
    independent order have, for every `m ≥ 2`, an `m`-arrow family with no affine equalizer over any ring where `m` is
    not a unit (cyclic rotation of ordered class tuples acts freely). **Checked here** (every step). Marginal: it corrects
    one of our own conference claims.

## FREX (prompt `04_FRAISSE_EXACT`; final of 18 Nov 12:35 UTC; INCOMPLETE by the two-review stopping rule)

Location: `derivateurs_companion_20261109/pro_prompts_max_20261112_work/FRAISSE_EXACT/FREX_final_20261118T1235Z_unzipped/FREX/`
(prompt: `pro_prompts_max_20261112/ALREADY_RAN/04_FRAISSE_EXACT/PROMPT.md`).

1. **Useful.** The best mathematics of the cluster: a two-way separation of exactness and amenability under all the
   structural hypotheses, a coefficient profile, a classified parameter family, and two group-invariance theorems. It
   speaks to model theory and topological dynamics (KPT, Zucker) and to the exactness-of-colimits literature (Oberst
   1968, Isbell-Mitchell 1976) at once.
2. **What it proved.** 147 rows: 126 Proved, 13 Refuted, 8 Known. Main: A.1 with A.24-A.26 (exactness over a given ring
   and totality depend only on `G = Aut(M)` under (S)); A.11 (posets with an independent order: exact over every unital
   ring, total, `G` not amenable); A.19 with A.33 (independently ordered F₂-spaces: total, all hypotheses, `G` amenable,
   exact over Q, not over F₂ or Z); A.12, A.15, C.12 (`A_r(Λ)` field profile; `A_2(Q)` exact over every F_p, not over Q);
   A.23 (in setting (S), `G` amenable with metrizable universal minimal flow ⇒ exact over Q; no (Rig), (FA), (FA∅), (Op)
   needed); A.30 (a counterexample to A.3(iii) needs a finite affine-relation image with unit filling norm and ambient
   ℓ¹ norm → 0); D.9 (predimension table); C.25, C.27 (filtered colimits and Grothendieck assemblies of Kan simplex
   categories: total ⇔ integrally exact); C.28 (three arrows give a rational obstruction in every degree); E.1-E.7
   (lim¹ obstruction is `ker(lim¹K → lim¹X)`; uncountable directed surjective systems can fail); G.1-G.43 (free monoids
   over `C_δ`: reduced to the kernel of a transgression `H₂(Y) → A_cut`, G.33). Checks by others: Opus-max intake 19 Nov
   (targeted checks of A.9, A.10, A.11, A.17, A.18, A.19, A.23, A.24 once, A.25, A.26, A.31 at its encoding step, A.32,
   A.33, C.10-C.13, D.3-D.6, G.12; A.12 re-proved; programs `frex_a10_weights`, `frex_a18_parity`). The run's own
   CHECK_EVENTS files are in-run events.
3. **New since the last intake:** no new return. This pile: A.13 followed in full (sound); A.23 followed a second time
   (sound; Zucker 2016 Thm 8.14 not opened; the Hamel functional `ℓ: R → Q` with `ℓ(1) = 1` is where positivity is
   given up, which is the point).
4. **Open.** A.3(iii): (S) + (Rig), (FA), (FA∅), (Op) + `G` amenable ⇒ exact over Q? Gate: a non-metrizable universal
   minimal flow and a distorted affine-relation image (A.23, A.30). C.4: total + exact over every F_p ⇒ exact over Q?
   (counterexamples must have torsion saturations of unbounded exponent and no weakly terminal object, C.15, C.6.) G.1,
   G.2: injectivity of the transgression `d₂: H₂(Y) → A_cut` for smooth locally free monoids of `C_δ` (G.33; G.34 shows
   neither shortcut works). F.1 (literature: Isbell 1974, McDuff 1979 bodies not obtained).
5. **Relations.** Answers the prompt's Leads 1-12 (corrections at B.8, B.10, B.14, E.1); FE-1, FE-3, FE-4 of the
   conference (A.13, C.18, D.12); TOTAL_EXACT_2 (`C_δ`, total not exact) and D.9 give two independent families of total
   non-exact categories; PRETOT A.5. Literature: Kechris-Pestov-Todorcevic 2005; Zucker 2016 (Trans. AMS) Thm 8.14;
   Bodirsky 2014 Cor. 1.4(3); Hubička-Nešetřil 2019 Thm 4.46; Evans-Hubička-Nešetřil 2021 Thm 1.3; Oberst 1968 II.4.1
   (its unrestricted conjecture refuted, per the run); Isbell-Mitchell 1976 Cor. 4.4. Grothendieck: the exactness of
   `colim` over a category is the "totalement asphérique / quasi-filtrant" theme of Les Dérivateurs XII ms. 88 and of
   Pursuing Stacks; no tie to schemes, λ-rings, motives or weights.
6. **Candidates.** Hexagon: one note "Exactness and amenability separate for Fraïssé categories" (A.9-A.11, A.17-A.19,
   A.33, with C.12 and D.9 as the coefficient and parameter tables): all key steps already checked by two readings.
   Next prompt: A.3(iii) and the total version of C.4 (the 19 Nov intake's hunches 1-3, `PROMPT_UPDATES_20261119.md`);
   the conference should also weigh hunch 1 of that intake (exactness over Z as an integer state on `C(X, Z)_G`,
   amenability as a positive one). Correction to a source: Oberst 1968 II.4.1/II.4.4 (unrestricted conjecture and monoid
   reduction false; the run's claim, unchecked by us); Schochet's statement is Prop. 3.5, not Thm 3.5; Li's unqualified
   full-faithfulness assertion fails for a perfect matching (run's claim, unchecked).
7. **Problems.** None found in what was read. The register's "Refuted" label is used for rows that *prove* a negative
   answer (A.11, A.19, C.12): read them as theorems. The report's table lists A.3, C.4, F.1, G.1, G.2 as INCOMPLETE; the
   register has no Open row, so the open items are only in the report.

## DER_LOCALIZERS (prompt `06_DER_LOCALIZERS`; checkpoint 08 of 18 Nov 09:54 UTC, the last; INCOMPLETE)

Location: `derivateurs_companion_20261109/pro_prompts_max_20261112_work/DER_LOCALIZERS/DER_LOCALIZERS_checkpoint_08_20261118T0954Z_unzipped/DER_LOCALIZERS/`.

1. **Useful** for the companion and for the axiomatics of localizers; several manuscript questions answered exactly.
2. **What it proved.** 100 rows: 55 Proved, 15 Proved under stated hypotheses, 19 Refuted, 6 Known, 5 Open. A.3 (the
   reverse axioms are all equivalent for fundamental localizers; W8 bis (a) must read `f`); A.4 (`W_Z` is the least
   reversible localizer); A.5-A.7 (accessible reversible localizers that are not `RT`-fixed); A2.4, A2.9, A2.13, A2.14
   (derivator level: final Der 6, or either unrestricted half, forces `W_D = R(L)`); A2.12 (constant ⇏ locally constant
   coefficients for unpointed derivators); A2.8 (Grothendieck's replacement margin at 105/052 is false); A34.5 (every
   reversible localizer is the join of its rational and p-primary parts); A34.6, A4.5-A4.8 (the two open existence
   questions reduced to one prime and one generator); A5.1-A5.4 (Cor. 7.7.2); B.3, B.4, B.10 (intervals); C.1-C.29
   (the linear "Thm(?)" of 134-8: false in general, C.26; corollary case open); D.1-D.10 (local systems: the naive class
   fails two-out-of-three; the repaired class is Toën's schematization localizer). Checks by others: Opus-max intakes
   19-20 Nov, 28 rows followed (A.1-A.5, A.7, A2.4, A2.9, A2.12-A2.14, A34.1, A34.2, A34.5, A4.5, A5.2, A5.3 (A5.1 at its
   collage step), B.1-B.4, C.1-C.4, C.6-C.8, C.10, C.26, D.1), A.8 by program.
3. **New since the last intake:** no new return. This pile: B.4's group step by program (no `ψ: F(a,b) → S₃` with
   `ψ(a) = (23)`, `ψ(b[a,b]) = (12)`, both commutator conventions); A5.3's homological key step re-derived (the mapping
   torus `T` of a degree-two self-map of S² has `π₁ = Z` and the integral homology of a circle, while its universal
   cover has `H₂ = Z[t^{±1}]/(2t − 1) ≅ Z[1/2]`; so `S¹ → T` is a Π₁- and homology equivalence and not a weak
   equivalence, and an infinite coproduct of copies has infinitely many bad components).
4. **Open.** A3.decision (= REVLOC D.2.4): an accessible reversible localizer with non-zero stable part inside the
   rational one and not `RT`-fixed? Gate A34.6: one accessible reversible closure of `A = QΣ³V` with a non-contractible
   primary `A`-null H-space separator in the ideal of `Σ^∞A`. A4.equality/interval/size (= REVLOC D.3.2): gate A4.5,
   `P_{BC₂}H ≃ *` for every countable simply connected primary sphere-null H-space. C.raw_gate: the linear corollary
   with finitely presented projective generators, in the form of C.10 (`Lφ(GP) = 0` for acyclic projective `P`).
   Bare (non-∞) derivators with constant coefficients (beyond A2.14).
5. **Relations.** Rechecks REVLOC A-B, D.2.2, G.6-G.7 (A.9, A4.2), POLES B.5-B.6 and F.14 (1), TOTASPH A.13 and the
   expert's `W_S` (12 Nov). With BISITE A.32, RESIDUE B.3, REVLOC F.1 and DER_FOLLOWUP G.9 it closes Cor. 7.7.2 (item 4
   above). Literature: Cisinski 2006 (Astérisque 308) Thm 6.1.18, 4.2.15; Cisinski-Tabuada 2011 A.11; Bousfield 1996
   Thm 3.3, Key Lemma 1.6, 1997 Lemma 8.13; Chataur-Scherer 2006 Prop. 3.4; Toën (schematization); Hubert 2026 Thm 5.14.
   Cotes: 105/012-040, 105/047-052, 134-8/048-054, 133/006-008 (D.10: does not state the local-system conjecture).
   Grothendieck's frameworks: through motivic derivators only negatively (20 Nov intake §4: for `DM(k, Λ)`, `W_D =
   W_{HΛ}`, twists and weights invisible to the localizer); C's motivic instance is Voevodsky's `A¹`-localization, where
   the gate C.10 is supplied by homotopy invariance of presheaves with transfers, not by formal hypotheses.
6. **Candidates.** Hexagon: the footnote-56 chain (item 4), with A5 as its last step. Next prompt: A3.decision, A4, C.raw_gate,
   bare derivators, and "Cor. 7.7.2 with sums in place of filtered colimits" (19 Nov intake hunch 5), with the instruction
   to open Bousfield 1996/1997, Chataur-Scherer and Cisinski-Kan before use (20 Nov intake §5).
7. **Problems.** None in what was read. The run's R5 paraphrase of REVLOC D.2.5 was too broad (19 Nov intake §6b.2).

## RESIDUE (prompt `8_RESIDUE`; return of 11 Nov 18:32 UTC; "substantive but incomplete")

Location: `derivateurs_companion_20261109/pro_returns_20261110/8_RESIDUE/RESIDUE/` (prompt:
`pro_prompts_20261110/ALREADY_RAN/8_RESIDUE/PROMPT.md`).

1. **Marginal-useful.** Its lasting contributions are B.2-B.4 (the first strongly saturated counterexample in the
   footnote-56 chain), A.1 (equivalence-transport bifibrations over the rectangular band excluded), D.4, D.6, I.1, and
   second proofs of BISITE rows; much else is now superseded or out of date (F.5-F.7).
2. **What it proved.** 85 rows: 54 Proved, 11 Refuted, 7 Known, 13 Open. B.2-B.4: `W_circ` (the inverse image of
   isomorphisms under `(q, H₁(−; Q))`, `q: Hot → 𝒬` the quotient by maps through S¹) is strongly saturated, satisfies
   absolute Theorem A and fails relative Theorem A (crowns `C₈ → C₄` of degree 2 suspended over a three-object poset);
   B.8 (products), B.16-B.17 (XV 9.9-9.13 fail under the literal axioms); A.1, A.5 (census); C.1-C.6 (XII ms. 215-218,
   240: Lead 3; C.3 a five-object counterexample to (a)+(b) ⇒ (c)); D.4 (`Fib_W` is no lifting class for `W_∞ ⊆ W ⊆ W₀`);
   D.6 (rational local coefficients: only `π₂(B) → π₁(F)`); D.8, D.12; F.1-F.4 (total asphericity; full subcategories of
   `Δ_inj`); H.1-H.8 (second proofs of BISITE D.11, F.15-F.17, B.15; H.7 a program over 1,349,916 poset maps); I.1
   (discrete fibrations are the largest diagonal-stable smooth class); J.1. Checks by others: author checks of Part E on
   11 Nov (Claude Fable 5.2, `pro_reviews_20261110/8_RESIDUE/checks_author/`); Opus-max intakes 19-20 Nov (A.1, B.2-B.5,
   C.1, C.4-C.6, D.4, D.6, F.1, F.2, F.4, I.1, I.2 followed; B.8 and D.8 re-proved; D.5, F.3 in outline).
3. **New since the last intake:** no new return. This pile: A.5 by computation (1, 2, 7, 35, 228; only the rectangular
   band of order 5 has non-zero rational homology in degrees 1-3).
4. **Open.** A.8 (VIc-C022: a bifibration over the rectangular band with right-adjoint, non-equivalence transports and
   weakly contractible total category); B.10 (audit of XVI ms. 1-27, XV §9; partly answered by DER_FOLLOWUP G.11-G.14);
   C.8 (least number of objects, ≤ 5); E.6 (PATHS B.8, unverified proof in the PATHS intake to reconcile); G.3; I.7;
   J.2, J.3; D.7, D.9.
5. **Relations.** POLES A.16; BISITE A.32 (earlier, weaker saturation), REVLOC F.1, DER_FOLLOWUP Part G, DER_LOCALIZERS
   A5 (later); STRATA E.11 = PATHS E.11 = BISITE B.21 (the bifibration over the five-element monoid). Out of date in its
   register: F.5 (refuted by TOTAL_EXACT_2), F.6 (by PRETOT A.5), F.7 (answered by PRETOT F.6). Literature: Cisinski 2006
   §9.2, 2019 Thm 4.4.36; Lurie HA 4.7.3.5; Cnossen-Lenz-Ramzi 2025 Cor. 2.6(2); Jansen 2023; Ara-Maltsiniotis; OEIS
   A058129 (the census; my computation agrees). Grothendieck's frameworks: H.3-H.6 (forgetting a point on `M̄_{g,n}`,
   entrance-path categories) and I.1-I.9 (six operations on `Cat`, where `f^! = f^*`: no twist, no weights) are the
   places where the cluster touches the structure of étale cohomology; the 20 Nov intake's §4 states that link and its
   limits.
6. **Candidates.** Hexagon: none alone (B.2-B.4 goes into the footnote-56 note). Next prompt: A.8 (from A.1 and A.4,
   non-equivalence adjoint transports only).
7. **Problems.** The register's F.5-F.7 statuses are stale (above). Nothing wrong found in what was read.

## S2COUNT (prompt `S2COUNT`; final of 16 Nov 08:41 UTC; INCOMPLETE in E2-E4)

Location: `derivateurs_companion_20261109/pro_prompts_max_20261112_work/S2COUNT/S2COUNT_final_20261116T0841Z_unzipped/S2COUNT/`
(prompt: `pro_prompts_max_20261112/ALREADY_RAN/S2COUNT/`).

1. **Useful.** It answers the question it was built for (finite-category representability of `[−, S²]`) with a short,
   explicit, fully checkable proof, and adds the exact countability criterion for arbitrary targets. Before this pile
   only titles had been read (Fable intake 17 Nov, its doubt (a): "A.M1 carries the whole negative answer and was not
   read").
2. **What it proved.** 85 rows: 70 proved, 8 audited, 3 unresolved (E:E2, E:E3gap, E:E4gap), 3 undecided task rows, 1
   refuted (TASK.B3, "the universal question").
   - **A.M1** (Theorem `thm:Mr-wedge`): for `r ≥ 0` there are explicit based maps `s_w: S^{|w|+2} → BM_r`, `w` a word on
     `r` letters, whose wedge `⋁_w S^{|w|+2} → BM_r` is a homotopy equivalence; `BM_1 ≃ ⋁_{n≥2} Sⁿ`. Proof: the integral
     basis `e, u = 1−e, a, b, c, t_s` with `ab = c` the only non-zero radical product (A.M2); a projective resolution with
     `P_n = (Re)^{r^{n−2}} ⊕ (Ru)^{r^{n−1}}` (A.M3); dual integral cocycles `f_w` and cycles `z_w =
     [(x01−e)|(y_{s1}−e)|…|(x10−e)]` (A.M5); `z_w` is the image of the fundamental class of the join
     `S¹ * (S⁰)^{*(n−1)}` mapped simplexwise to bar simplices (A.M6); `BM_r` simply connected (all `x_ij` idempotent,
     `y_s e = e`); Whitehead.
   - **A.M7**: all positive cup products, Steenrod operations and triple Massey products vanish.
   - **B:main**: `|[BM_1, S³]| = |[BM_1, S²]| = 2^{ℵ₀}`; `C ↦ [BC, S²]` on finite categories is not a sequential colimit of
     representables by finite categories; six arrows is optimal (**B:smallmonoids**, **B:smallcategories**: every
     category with at most five arrows has countably many classes, via Miller's Theorem A).
   - **CD:alltargets / CD:countabletargets**: `[BC, Y]` countable for every finite `C` ⇔ `π₀Y` countable, each component
     a Postnikov piece, `[A, Y_c]` countable for finite `A`; for countable CW `Y`: each component a Postnikov piece.
     **CD:finiterepresentative**: the types represented by one finite category on finite tests are exactly the finite
     groupoid types.
   - E: INDLOCAL A.19, A.20 proved again; E:finite, E:infinitepositive, E:exact (resolutions of bound μ); E:tests (two-
     dimensional group tests cannot replace the tests of INDLOCAL B.7); E.11-E.22 obstruction lemmas (e.g.
     E:normalfinite: a perfect normal `N` in a group of geometric dimension ≤ 2 with `H₂(N) = Z^r`, `0 < r < ∞`, has
     finite quotient of order dividing `r+1`).
   Checks by others: none at proof level before this pile (Fable intake 17 Nov: statement level; main-session notes of
   15-17 Nov name it).
3. **New in this pile (no new return):** A.M1, A.M5, A.M6, B:main, B:smallcategories, CD:wedgecriterion, CD:alltargets
   followed in full, no fault; A.M3 confirmed by my program `DERIVATEURS_checks/s2count_monoid_homology.py` (ranks of
   the normalized bar complex over Q, F₂, F₃: `r = 0`: `H₂` only, through degree 5; `r = 1`: rank 1 in degrees 2-5;
   `r = 2`: 1, 2, 4 in degrees 2-4); B:smallmonoids supported by my census (one monoid of order 5 with non-zero rational
   homology). In B:smallcategories I checked each case: two objects with arrows both ways (one object a retract, since
   `f, g, gf, fg` with both identities would be six arrows), one-way cross arrows `c = 1` (join `BL * BL'`; only
   `BC₂ * BC₂` needs Miller), `c = 2` (cofibre of `B(S//L) → BL`: `BC₂`, `S¹ ∨ ΣBC₂`, a point or `S¹`), `c = 3`
   (`S¹ ∨ S¹`), three objects (a contractible V).
4. **Open.** E2: does a perfect group with an actual two-dimensional `K(G,1)`, `H₂ = Z` and no non-trivial countable
   image exist (the ℵ₀-resolution of S² in dimension two)? E3: the interval `ℵ₀ ≤ μ < 2^{ℵ₀}` for finite positive rank
   (CH reduces it to `μ = ℵ₀`). E4: `κ ≤ μ < κ^{ℵ₀}` for infinite rank κ. The run's exact next steps are in its report
   ("convert the essential pure extension into an actual two-dimensional relative homology equivalence ..."). The Fable
   intake 17 Nov judged this frontier closed off for the companion (it no longer bears on a manuscript statement).
5. **Relations.** Sweeney 2025 (Examples 5.2, 5.3, Thm 2.7, Cor. 2.8; the run audited his periodic resolution as exact);
   INDLOCAL A.19, A.20, A.31, B.7-B.9; CATHOT D.5 (`K(Z/2, 2)` countable) and the CATHOT expert's hunch H3 (proved here);
   RESIDUE A.1, A.5 and STRATA/PATHS/BISITE B.21 use the `r = 0` monoid (`BM_0 ≃ S²`). Literature: Miller 1984 Thm A;
   Serre 1953; Corson-Obraztsov (E.19); Brown-Leary; Farjoun-Orr-Shelah (the run found a one-pass existence-closure error
   with a finite counterexample, `notes/CD_E_FDOS_one_pass.md`). Manuscript: V ms. 43-46, 51-52; VII ms. 121-124,
   129-132 (the finite-test programme of Pursuing-Stacks-era homotopy types modelled by small categories). No tie to
   schemes, λ-rings, motives or weights.
6. **Candidates.** **Hexagon:** "A six-arrow monoid with `BM ≃ ⋁_{n≥2} Sⁿ` and countability on finite-category tests"
   (A.M1, B:main, B:smallcategories, CD:alltargets): every step now checked by a reader outside the run, with a
   computation. Before posting, open Sweeney 2025 to see whether the wedge decomposition (not only the homology) is
   already there; the countability consequences and the minimality are the run's. **Correction to a source:**
   Farjoun-Orr-Shelah (one-pass existence closure; the run's claim with a finite counterexample, not checked by us).
   **Next prompt:** none for the companion; E2-E4 only if the user wants the S² frontier pursued (`NEW_PROMPT_ITEMS_20261117.md`
   Part B).
7. **Problems.** None in what was read. The report's "Proved and independently checked by program" for A1 means that
   `code/A_monoid_verify.py` checks the algebra identities; the homotopy statements rest on the proof (which is
   complete).

## REVLOC (prompt `REVERSIBLE_LOCALIZERS`; checkpoint 17 of 16 Nov 02:57 UTC, the last; INCOMPLETE)

Location: `derivateurs_companion_20261109/pro_prompts_max_20261112_work/REVERSIBLE_LOCALIZERS/REVLOC_checkpoint_17_20261116T0257Z_unzipped/REVLOC/`.

1. **Useful** (A-C, F.1, G.5-G.7); the long D.2 computation (42 rows) is a superseded route.
2. **What it proved.** 152 rows: 136 Proved, 12 Refuted, 2 refuted as worded, 2 Open (D.2.4, D.3.2). A.1-A.7, B.1-B.4: in
   ZFC an accessible reversible fundamental localizer that is not `R(L)`; the reversible closure of any small set is
   accessible; the closure of `BZ/2 → *` is accessible and not `RT`-fixed. C.1 (closure description of `𝒜_rev`). G.5 (a
   non-total reversible localizer whose stable part is all spectra); G.6 (`W_S = Ŵ₂ ∩ W_Q`); G.7 (the full sphere-null
   localizer is accessible in ZFC: `N̂₂ = N̂₂^{ℵ₁}`, `Nul = Nul^{ℵ₁}`). D.1.7-D.1.9 (Moore targets `M(Z/p, n)` give
   desuspension-closed null classes exactly when `(p, n) ≠ (2, 1)`). E (fibrations of `W_Z`). F.1, F.1.1, F.2 (the
   literal axioms). H.1-H.4 (accessibility of `W^lc_D`: true under Vopěnka, false for some `D` without measurables),
   H5.1-H5.9 (group-quotient localizers), I.1-I.9 (cores; I.8b a unit of `Z[C₅]` of infinite order). Checks by others:
   DF intake 17 Nov (F.1 followed by hand); Fable intake 17 Nov (titles); Opus-max intakes 19-20 Nov (A.1, A.3, A.5, B.1,
   B.2, B.4, C.1, G.5 followed; I.8b's unit by computation); DER_LOCALIZERS (the same model, GPT-6 Astra (ChatGPT Pro
   mode), a second run) rechecked A.5-A.7, D.2.2, G.6-G.7.
3. **New in this pile (no new return):** **F.1 followed in full** (the class `W†`: Π₁-equivalence, `H_n` iso for `n ≥ 3`,
   `H₂ ⊗ Q` iso, `Tor H₂` iso; strongly saturated as an inverse image of isomorphisms under functors factoring through
   `Hot`; its aspherical objects are the contractible ones; the witness is the face-poset map of the degree-2 map
   `L₈ → L₄` of suspended polygons, `|P| = 50`, `|Q| = 26` (my count: 10 + 24 + 16 and 6 + 12 + 8), collages of 77 and 53
   objects, `B∫D` = the mod-2 Moore space; sound). **G.7 followed in full** (compact Kan model `Tot(R^{•+1}K)` of `Ŝⁿ₂`
   with finite levels in each cosimplicial degree, Reedy fibrancy by the explicit matching-map splitting, the compactness
   lemma `C_A = ∩_L C_{L,A}`, countable enlargement; sound, Bousfield 2003 §7.7 not opened). This settles, by a reader
   outside the runs, the accessibility of the expert's `W_S` of 12 Nov.
4. **Open.** D.2.4 and D.3.2, continued as DER_LOCALIZERS A3.decision and A4 (gates there). The D.2.11-D.2.61 computation
   ended without a conclusion and is not a route to resume (DER_LOCALIZERS A34.3-A34.6).
5. **Relations.** POLES B.5-B.6 and Lead 6 (the classification by localizing subcategories, false: B.3, B.4, G.5);
   RESIDUE B.3 and BISITE A.32 (footnote 56); DER_FOLLOWUP Part G (F.1 is its test class; F.1.1 = its G.9); OpenAI
   preprints 312, 317 audited (F.3, I.312; F.3c refuted as an unrestricted ZFC assertion). Literature: Boyde 2023 Thm
   2.2 (EHP), Miller 1984 Thm C, Kahn-Priddy, Snaith 1974, May 1972, Bousfield 2003, Heuts 2021, Cisinski 2006 Thm
   6.1.18. Cotes: XVI ms. 16′-27, 79, 118 (fn. 56); XII ms. 75-78. Grothendieck's frameworks: the image-of-J elements of
   D.2 and the cyclotomic unit of I.8b touch zeta values and regulators only formally (20 Nov intake §4).
6. **Candidates.** Hexagon: F.1 inside the footnote-56 note; G.7 as a remark in it ("the sphere-null localizer is
   accessible in ZFC"). Next prompt: none of its own (its open rows live in DER_LOCALIZERS).
7. **Problems.** The symbol `W†` names two different classes: BISITE A.32's (component bijection, weak equivalence on
   connected categories; weakly saturated) and REVLOC F.1's (Π₁, H, torsion tests; strongly saturated). Integration into
   the companion should rename one. F.1's statement "There is a strongly saturated class ... satisfying neither Loc (3
   bis) nor Loc (6′ a)" is correct; its title "even with Loc (8) and (9)" is the point that distinguishes it from RESIDUE
   B.3, which does not discuss Loc (8), (9).

## BISITE (prompt `7_BISITE`; return of 11 Nov 13:34 UTC)

Location: `derivateurs_companion_20261109/pro_returns_20261110/7_BISITE/` (prompt: `pro_prompts_20261110/ALREADY_RAN/7_BISITE/`).

1. **Marginal for mathematics, useful for the companion.** An audit of the fine theories over a base (XII ms. 215-261),
   the bisite and topological cases, six operations, and stable duality: mostly formal or known material made precise;
   its sharp new items are A.32, B.9, E.12, A.33.
2. **What it proved.** 126 rows: 72 Proved, 32 Refuted, 18 Known, 4 Open (B.21, C.10, D.12, F.18). A.32 (literal Loc
   (1)-(3) with moderate saturation ⇏ Loc (3 bis): `W†` = bijection on components and weak equivalence on connected
   categories, a triangle of finite groupoids over `BC₂`); A.33 (XII ms. 274, Théorème 3° and Corollaire 1 need
   conservativity: finite sets); B.6 (`𝓛^ = Liss_W`, XII ms. 222); B.9 (`Liss ∩ Prop ⊂ Fib_W` exactly for `W_∞` and the
   class of all functors, ms. 225); B.3, B.22 ("dualité parfaite" in simplicial sets); C.2-C.4 (no transport through
   categories of elements); D.1-D.4, D.11 (open tests on topological spaces, direct images on finite posets); E.12
   (XIIc B062 false: a six-element lattice with (a), (b) at every base and (c) failing); F.15-F.17 (forgetting a point of
   `M̄_{0,n}`; `BZ` at `n = 4`); G.1-G.14 (stable duality). Checks by others: REVIEW_author and COMBINED_REVIEW (Claude
   Fable 5.2, default effort, 11 Nov: no row labelled Proved/Known/Refuted found false; 44 rows unverified there, among
   them D.11, F.10, F.15-F.17); RESIDUE H.1-H.8 (GPT-6 Astra, ChatGPT Pro mode) gave second proofs of D.11, F.15-F.17,
   B.15 (H.7: a program over 1,349,916 poset maps); the ledger's §9 lists 30 rows no intake has checked (C.1, C.5-C.9,
   D.5, D.9, D.10, D.13, E.1, E.2, E.4, E.9, E.10, F.1, F.3, F.6, F.7, F.9, F.14, G.1, G.4-G.8, G.11, G.13, G.14).
3. **New in this pile (no new return):** A.32 followed in full (sound: `E` is the contractible groupoid on `Z/2`,
   `A = E × BC₂`, `E/c` has two contractible components, so `u/c ∈ W†` and `u ∉ W†`; `W†` fails Loc (1 bis), as the
   run says). Of the 30 unchecked rows: G.7 re-proved (for `S = BC₂`, `k = F₂`, `p_*` is homotopy fixed points; on
   `⊕_n Σⁿ HF₂ = ∏_n Σⁿ HF₂` its `π₀` is `∏_n Hⁿ(BC₂; F₂)` against `⊕_n` for the sum of the values, so countable
   coproducts are not preserved); E.2 checked (the inclusion `{1} → [1]` is right anodyne, hence a contravariant
   equivalence over `[1]`; its fibre over 0 is `∅ → e`). The other 27 are formal or Known and were left at statement
   level.
4. **Open.** B.21 (= STRATA E.11 = PATHS E.11 = RESIDUE A.8's question): a strict bifibration with contractible total
   category representing the path local system over the five-element monoid of type S² (invertible transitions excluded
   by the combined review §3(c) and RESIDUE A.1). C.10, D.12 (restriction to a closed subspace for open tests; first
   case the real line), F.18.
5. **Relations.** POLES A.16, E.2, E.5, G.17-G.19; STRATA D.8, F; GALOIS D.3-D.5; PATHS D.18; RESIDUE H; OpenAI preprints
   312, 317 (C.9 conditional on the unrefereed 317). Literature: Cisinski 2006, 2019; Lurie HTT 4.1.2.9; Anel-Weinberger
   2025 Def. 2.3.1 (F.14); Mann (six operations); Aoki (Verdier duality); Ara-Maltsiniotis 2018. Manuscript rows XIIc
   B062, XIIc-a C023, C033, Ib-C003; XII ms. 215-275; XIII ms. 57-74; VI ms. 84, 186. Grothendieck's frameworks: F.15-F.17
   and G (Verdier duality, the dualizing object) are the formal shadow of the six operations of étale cohomology, with no
   twist (the combined review §2.1).
6. **Candidates.** Hexagon: A.32 as the first step of the footnote-56 note. Corrections to report: none to an outside
   source beyond the edition misprints the run lists (XVI ms. 39 "cofibrations" in Loc (7 F); XII ms. 223 `Liss_W` for
   `Prop_W`; XII ms. 273 "cartésien" for "cocartésien"; ms. 222 the direction of `f`; XIII ms. 70, 71, 74), which belong
   to the companion. Next prompt: B.21 together with RESIDUE A.8 (non-equivalence adjoint transports over the rectangular
   band), if the user wants VIc-C022 decided.
7. **Problems.** See P1 and the `W†` collision under REVLOC.

## Problems across the cluster

- **P1. Priority in the footnote-56 chain.** The Opus-max intake 19 Nov (§1 finding 7 and §6b item 4) says "RESIDUE (11
  Nov) had refuted 'absolute ⇒ relative Theorem A' first". BISITE A.32 (return of 11 Nov 13:34 UTC, before RESIDUE's
  18:32 UTC) had already refuted it **for the literal axioms of XVI Définition 1.1** (moderate saturation), and the
  BISITE combined review (11 Nov 14:00 UTC) recorded POLES A.16 as answered by A.32. RESIDUE B.3 was first for a
  **strongly saturated** class. The correct chain: BISITE A.32 (literal Loc (1)-(3)) → RESIDUE B.2-B.4 (strong
  saturation) → REVLOC F.1 (strong saturation with Loc (8), (9)) → DER_LOCALIZERS A5.3 (Loc (8) needed even with Loc (6′ a),
  (9)); positive side REVLOC F.1.1 / DER_FOLLOWUP G.9. The companion's editors'-insights entries XV.9 and XVI.2 should
  credit all four.
- **P2. `W†` names two classes** (BISITE A.32 and REVLOC F.1).
- **P3. Stale rows:** RESIDUE F.5-F.7 (above); the ledger counts DER_LOCALIZERS as "13 of 100 checked" while the 19-20 Nov
  intakes followed 28 rows: the 20 Nov check events may not be in `results_register/CHECK_REGISTER.tsv` yet (to check
  when the register is rebuilt).
- **P4. External inputs never opened by anyone outside the runs:** Miller 1984 Thm A (S2COUNT B3b), Sweeney 2025 Thm 2.7,
  Zucker 2016 Thm 8.14 (FREX A.23), Bodirsky 2014, Hubička-Nešetřil 2019, EHN 2021 (FREX Ramsey inputs), Bousfield
  1996/1997/2003, Chataur-Scherer 2006, Cisinski-Tabuada 2011, Cisinski 2006 Thm 6.1.18 (REVLOC, DER_LOCALIZERS), Boyde
  2023 (EHP). They are standard; a successor prompt should ask for their exact statements before use.

## Not read, with the reason

- FREX: Parts B, E, G beyond what the 19 Nov intake read (G.tex alone is 209 KB); C.25-C.31 at statement level.
- DER_LOCALIZERS: C.11-C.29 except as above; A34/A4 reviews beyond the 20 Nov intake's rows.
- REVLOC: the D.2 computation (42 rows), D.1, D.3, E, H, I at statement level (superseded route or formal).
- RESIDUE: E, G, H, J at statement level.
- BISITE: 27 of the 30 unchecked rows (formal or Known).
- S2COUNT: E (75 KB) at statement level (its questions are closed off for the companion).
- No PDF check of any of the six papers (not asked of a cluster reader); no program of the runs was run; my own three
  programs are in `DERIVATEURS_checks/`.
