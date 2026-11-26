# Intake of DER_LOCALIZERS (checkpoint 08), the rows of packets 73–74

Claude Opus 5.5 at effort max, the Dérivateurs intake sub-agent of 19 Nov (author of
`derivateurs_companion_20261109/pro_prompts_max_20261112_work/INTAKE_FREX_DERLOC_REVLOC_RESIDUE_20261119.md`),
resumed by the main session; 20 Nov 2026, from 19:26 UTC (clock read). Brief:
`field_experts/intake_20261120/INTAKE_BRIEF.md`. The run is GPT-6 Astra (ChatGPT Pro mode); unrefereed outside this
project. My agent id is not shown to me; the registry maps it from the 19 Nov intake.

## 0. Scope

**Return read:** checkpoint 08 (18 Nov 09:54 UTC, the run's last; INCOMPLETE by its own first line), folder
`derivateurs_companion_20261109/pro_prompts_max_20261112_work/DER_LOCALIZERS/DER_LOCALIZERS_checkpoint_08_20261118T0954Z_unzipped/DER_LOCALIZERS/`.
Prompt as sent: `pro_prompts_max_20261112/ALREADY_RAN/06_DER_LOCALIZERS/PROMPT.md`. Sort: `SORTED/DER_LOCALIZERS.md`.

**My rows:** the 65 DER_LOCALIZERS rows of packets 73 and 74. The other 35 rows of the register (A2.1, A2.8, A34.3, A34.6,
A3.decision, A4.equality, A4.interval, A4.size, A4.2, A4.8, A5.1–A5.4, A.6, A.8, A.9, B.3–B.5, B.8, B.10, C.5, C.12,
C.29, C.raw_gate, C.general_M, D.3–D.10) were treated on 19 Nov (see the 19 Nov intake and its `ROWS_20261119.tsv`).

**Read in full, every step followed (27 rows):** A2.4, A2.9, A2.12, A2.13, A2.14, A34.1, A34.2, A34.5, A4.5, A.1, A.2,
A.3, A.4, A.5, A.7, B.1, B.2, C.1, C.2, C.3, C.4, C.6, C.7, C.8, C.10, C.26, D.1. For A2.4, A2.13, A2.14, A34.5, A4.5,
A.1–A.3, A.7 and C.26 "every step" means every step of the argument the return writes; the external theorems it cites
were not opened (named row by row below). A.1–A.5, A.7, A2.4 and D.1 were read on 19 Nov; the rest today.

**Read once in outline (1 row):** C.11 (Smith recognition, Dold–Kan realization, the derived counit).

**Statement level only (37 rows):** A2.2, A2.3, A2.5, A2.6, A2.7, A2.10, A2.11, A34.4, A3.1, A4.1, A4.3, A4.4, A4.6, A4.7,
B.6, B.7, B.9, B.11, B.12, B.13, C.9, C.13–C.25, C.27, C.28, D.2: the register row, the claim statement in its section
and the report's sentences on it were read; the proof was not.

**Not opened:** every external source the proofs cite (Cisinski–Kan 2004, Cisinski–Tabuada 2011, Brown 1962/1963,
Bousfield 1996, 1997, Chataur–Scherer 2006, May–Ponto 2012, Groth–Ponto–Shulman, Beke 2000, Hubert 2025/2026, Toën);
no program of the run was run; no PDF check.

## 1. Verdicts, row by row

"Confirmed" = targeted proof check, every step of the written argument followed, no fault found. "Statement" = not
read in full; the statement and the run's own status were read. Locators are `sections/<file>:<line of the claim>`.

| Row | Run's status | My check | Verdict and what it rests on |
|---|---|---|---|
| A2.2 | Proved | statement | unrestricted provisional Der 6 and Der 6′ are the two halves of stability (`A2_review.tex:78`) |
| A2.3 | Proved | statement | final Der 6 does not force pointedness (slices of spectra over a non-zero E) (`:141`) |
| A2.4 | Proved | confirmed (19 Nov) | final Der 6 ⇒ `W_D` is RT-fixed: derived pointing stable, free pointing conservative by the square (A2.4.3), spectral action (Cisinski–Tabuada A.11, not opened) (`:183`) |
| A2.5 | Proved | statement | Der 8: first two implications automatic; third from final Der 6; finite lattice examples (`:299`) |
| A2.6 | Proved | statement | ∞-categories with pushouts = pullbacks are slices of stable ones (`:363`) |
| A2.7 | Proved | statement | bare-derivator characterization of final Der 6 (`:413`) |
| A2.9 | Proved | confirmed | either one-sided unrestricted half ⇒ RT-fixed: in the pointed envelope Σ is fully faithful, the groups `h^n_{P,N}(X) = Hom(Σ^r(X⊗P), Σ^{r+n}N)` form a reduced cohomology theory (wedge and cofiber axioms from cocontinuity and strongness), Brown representability gives spectra `E_{FM,N}`, and `W_D = R(L)` for `L` their common kernel; dual case by `D^op`. Cites Cisinski–Kan Cor. 4.19, Thm 5.22 and Brown (Hatcher 4E.1), not opened (`:489`) |
| A2.10 | Proved | statement | pointed derivators: constant = locally constant = arbitrary coefficients (`:617`) |
| A2.11 | Proved | statement | constant Der 6′ makes the pointed envelope unrestricted (`:740`); used by A2.13, A2.14 as input |
| A2.12 | Refuted | confirmed | the labelled slice `C ⊂ (D(Z)_{≥0}/Z[0]) × {0<1}` (label 1 allowed only for non-zero augmentation): coreflector `R(q,s) = (q, min(s, z(q)))`, colimits created; constant Der 6′ holds (the label resets exactly when the upper-left comma category is empty); the five-object locally constant test (A2.12.6) fails with comparison `M_0 → M_1`; `W = W_Z` (`:842`) |
| A2.13 | Proved | confirmed | locally constant ⇒ unrestricted: the five-object test reconstructs `X = TX ×_{T²X} TX`, `T = 1 ⊔ −`; with A2.11, `TS`, `T²S` cartesian, hence `S` (`:1028`). A2.11 taken as given |
| A2.14 | Proved | confirmed | ∞-categorical derivators: constant half ⇒ RT-fixed, `W = ∩_M W_{E_M} = R(∩ L_M)` over retractive slices; empty cases handled (`:1077`). A2.9, A2.11 used as inputs |
| A34.1 | Proved | confirmed | `𝒜_{W_A} = {X : P_A(Σ^dX) ≃ *}` when `A` kills d-connected p-primary GEMs: desuspension through Bousfield's ⟨ΣU⟩ = ⟨Σ^kU ∨ SP^∞ΣU⟩ (Bousfield 1996 Thm 3.3, not opened) (`A34_reduction.tex:10`) |
| A34.2 | Proved | confirmed | the bounds `d = 1` for `K(F_p,2)` and `BC_p ∨ V`, `d = r+1` for `QΣ^rK(F_p,2)`; rests on Bousfield 1997 Lemma 8.13 and 1996 Cor. 3.2(ii), not opened (`:96`) |
| A34.4 | Proved | statement | cyclotomic completion separates `loc Σ^∞K(C_{p^∞},2)` from `loc Σ^∞K(F_p,2)` (`:380`) |
| A34.5 | Proved | confirmed | every reversible localizer is the join of its rational part and its p-primary parts `W_p = W ∩ R(loc S/p)`; RT-fixed iff every `W_p` is. Steps followed: telescope localizations of `Z = Σ³X`, the arithmetic fibres `G_p(Z)` simply connected and p-primary, `G_p(Z) ∧ ΩZ[1/p] ≃ *` so the Ganea comparison (Chataur–Scherer 3.4, not opened) makes them cofibres, `⋁_p G_p(Z) ≃ F(Z)`, membership test (A34.5.8) (`:543`) |
| A3.1 | Proved | statement | recheck of REVLOC D.2.4 (first half) and D.2.6 (`A34.tex:2`) |
| A4.1 | Proved | statement | the inclusions of the primary interval (`A34.tex:21`) |
| A4.3 | Proved | statement | capping multiplicities for products (`A4_product_review.tex:9`) |
| A4.4 | Proved | statement | a primary countable product of Postnikov sections of `M(F_p,2)` reaches the upper endpoint (`:11`…) |
| A4.5 | Proved | confirmed | for a simply connected p-primary H-space `H`: `P(ΣH) ≃ * ⇔ PH ≃ *`, `P = P_{BC_p}`: `Z = PH` is an H-space with `Map_*(ΣZ, Z) ≃ *`, so Bousfield's Key Lemma 1.6 (not opened) makes `Z` a retract of the p-primary GEM `SP^∞Z`, which is `BC_p`-acyclic; so `Z ≃ *`. The A.4 equality reduces to countable H-spaces `J(ΣX)` (`A4_hspace_review.tex:10`) |
| A4.6 | Proved | statement | finite Steenrod generation forces `BC_p`-acyclicity (CCS Thm 7.2) (`:213`) |
| A4.7 | Proved | statement | finite non-zero mod-p cohomology gives the upper endpoint (`:324`) |
| A.1 | Proved | confirmed (19 Nov) | span/sieve comparison with the canonical `α ⊣ q` (`A.tex:7`) |
| A.2 | Proved | confirmed (19 Nov) | reversibility ⇔ the pointed cofiber criterion, no accessibility (`A.tex:35`) |
| A.3 | Proved | confirmed (19 Nov) | W7 bis, W8 bis, XII W(7 bis), W(7), XVI Loc (6 a,b,c) equivalent; W8 bis (a) must read `f` (`A.tex:60`) |
| A.4 | Proved | confirmed (19 Nov) | `W_Z` is the least reversible localizer (`A.tex:80`) |
| A.5 | Proved | confirmed (19 Nov) | `W_S` satisfies every axiom; `RP^∞ → e ∈ W_S`, the 7-object `RP²` category not (`A.tex:89`) |
| A.7 | Proved | confirmed (19 Nov) | the countable-enlargement class: accessible, reversible, not RT-fixed (`A.tex:147`) |
| B.1 | Proved | confirmed | hypotheses (1)–(5) give `TC ⊆ C ∩ W`, `TF ⊆ W` (section pushout; Lawvere-interval homotopy and Loc (1c)); a set of intervals gives both weak factorization systems (`B.tex:23`) |
| B.2 | Proved | confirmed | `TC = C ∩ W ⇔ F ∩ W ⊆ TF ⇔ W = TF ∘ TC` (retract arguments) (`B.tex:79`) |
| B.6 | Known | statement | Cisinski's thesis 2.3.4 / Astérisque 308 1.4.3–1.4.4 (not opened) (`B.tex:280`) |
| B.7 | Proved under hypotheses | statement | the two tests for a bunch (`B.tex:304`) |
| B.9 | Proved | statement | BISITE A.27, A.28, PATHS D.18 do not supply the recognition (`B.tex:404`) |
| B.11 | Proved | statement | a set of intervals encoded by one wedge interval (`B.tex:609`) |
| B.12 | Refuted | statement | on `Δ × [1]` a proper ordinary localizer has a trivial cofibration changing support (`B.tex:649`) |
| B.13 | Refuted | statement | the chaotic `C_2` category into its cone: componentwise case (b) fails (`B.tex:739`) |
| C.1 | Proved | confirmed | projectives of `Ch_{≥0}(𝒜)` are split complexes `H_0P[0] ⊕ ⊕D^n(B_{n−1}P)` (`C.tex:10`) |
| C.2 | Proved | confirmed | Lemme 1 under the weaker hypothesis `H_jΛ(P) = 0` (bicomplex, finite diagonals) (`C.tex:21`) |
| C.3 | Proved | confirmed | Lemme 2 and (i) ⇔ (ii) ⇔ (ii′) ⇔ (ii″) (`C.tex:38`) |
| C.4 | Proved | confirmed | adjunctions descend when both functors preserve the inverted classes; answers 134-8/053 lines 10–12 (`C.tex:67`) |
| C.6 | Proved | confirmed | the corollary's hypotheses give an exact `F` representing `Lφ` and an exact right adjoint `G` (`C.tex:101`) |
| C.7 | Proved under hypotheses | confirmed | raw equivalence when projective k-modules have bounded injective dimension (finite injective resolutions of split acyclic complexes, injectives of 𝓜 are summands of `J ⊗ Q`), or when the interval images split degreewise (`C.tex:118`) |
| C.8 | Refuted | confirmed | dropping degree-zero nullity or monicity of the interval fails (identity functor on `Mod k`); "exact limits" cannot mean all inverse limits (`C.tex:144`) |
| C.9 | Known | statement | Hubert 2026 Thm 5.14, Thm 6.15 for strong Whitehead test categories (not opened) (`C.tex:153`) |
| C.10 | Proved | confirmed | the remaining gate is `Lφ(GP) = 0` for acyclic projective `P` (C.3, C.1, normalization) (`C.tex:174`) |
| C.11 | Proved under hypotheses | read once in outline | underlying localization over every ring via Smith recognition (Beke 1.7, not opened) and simplicial realization; no fault seen (`C.tex:192`) |
| C.13–C.25, C.27, C.28 | (see register) | statement | conditional raw-adjoint cases (C.13–C.17, C.19, C.21–C.23, C.25, C.27), refuted proof routes (C.18, C.20, C.24), C.28 (no flat interval or countable scalar form in general) (`C.tex:252`–`1322`) |
| C.26 | Refuted | confirmed at its key steps | the three-sort square-zero monad `H(U_0,U_1,U_2) = (E(U_2), U_0, U_1)`, `E(V) = V**/V`: the exact sequences give the periodic resolution of `κW`, `L_{3n}φ(κW) = Eⁿ(W)`; `κW[0]` is `𝒲`-local, so an equivalence would force `Lφ(κW) ≃ W[0]`, false for infinite-dimensional `W`. The symmetric monoidal coherence of `⊠` was followed in outline (the run's certificate `C_three_sort_coherence.py` not run) (`C.tex:1092`) |
| D.1 | Refuted | confirmed (19 Nov) | the naive finite-dimensional local-system class fails two-out-of-three over every field (`D.tex:26`) |
| D.2 | Proved | statement | the naive test is full faithfulness on perfect local systems; equivalence needs affine `π_1` data (`D.tex:82`) |

**Counts (65 rows):** 27 confirmed by a targeted proof check (none refuted, no gap found), 1 read once in outline, 37 at
statement level. The run's own labels for these 65 rows: 40 Proved, 14 Proved under stated hypotheses, 9 Refuted,
2 Known.

## 2. What is new

Against the literature (nothing below was searched today; "to verify" where a precedent may exist):
- **The localizer/derivator dichotomy for reverse excision** (A.3 with A.5–A.7 against A2.4, A2.9, A2.13, A2.14): at the
  level of fundamental localizers, Grothendieck's strengthened reverse axioms (105/052) say only "reversible", and
  reversible localizers need not be homology localizers (the sphere-null `W_S`, ours since 12 Nov); at the level of
  derivators, either one-sided unrestricted provisional Der 6 already forces a homology localizer, by a Brown
  representability argument inside the pointed envelope. New to us and, as far as I know, not in the literature (to
  verify).
- **Coefficient strength** (A2.10–A2.13): constant ⇒ locally constant fails for unpointed derivators (A2.12, an
  explicit accessible example), and locally constant = arbitrary always (A2.13). New to us.
- **The arithmetic decomposition of reversible localizers** (A34.5) and the reduction of A.4 to `BC_2`-acyclicity of
  countable H-spaces (A4.5): new to us; the inputs are Bousfield's nullification theory.
- **The linear "Thm(?)" of 134-8** is false in full generality (C.26), true under each of the sufficient hypotheses of
  C.7, C.11, C.13–C.17, C.19, C.21–C.23, C.27, C.29; the necessary repair is normalization on every scalar module. New.
- B.1, B.2: elementary and standard in form (the recognition hypothesis is the classical one of Cisinski's theory).

Against our own results: A.4, A.5, A.7 recheck POLES B.5–B.6, the expert's `W_S` (RESULT_REVERSIBLE_NOT_STABLE, 12 Nov)
and REVLOC B.1–B.4; A3.1, A4.1 recheck REVLOC D.2.4/D.2.6 and D.3.

## 3. Implications

**For the reading of the archive.**
- Cote 105, scans 047–052 (Der 6, Der 6′, Der 8, W7 bis, W8 bis): the companion can state that the "provisional" and
  "final" Der 6 differ in strength exactly as A2.2–A2.4 say, that W8 bis (a) must read the total map `f` (A.3; the
  transcription's uncertain glyph `f | f_a`), and that the margin "Complètement faux" at 105/052 is right while the
  replacement conjecture beside it is false (A2.8, 19 Nov).
- Cote 105, scans 012–040 (trivial cofibrations from intervals): Grothendieck's hope at 105/020 fails for integral
  homology even with all acyclic intervals (B.4, 19 Nov); B.1–B.2 give the exact extra hypothesis.
- Cote 134-8, scans 048–054 (the linear "Thm(?)", Lemmes 1–3): Lemme 1 holds under a weaker hypothesis (C.2); Lemme 2
  holds with all four conditions equivalent (C.3); the marginal question at 053 lines 10–12 is answered yes (C.4);
  Lemme 3 needs the degree-zero normalization (C.5); the theorem is false in full generality (C.26) and true under
  bounded injective dimension of projectives (C.7: fields, `Z`, noetherian rings of finite self-injective dimension).
- *Pursuing Stacks* §134: C.9 places the question beside Hubert's theorem for strong Whitehead test categories.

**For the programme.** The successor items of the DF intake §7: A.1 refuted (19 Nov), A.2 settled with the coefficient
classification (A2.1–A2.14), A.3 and A.4 open with sharper gates (A34.5, A34.6; A4.5–A4.8), A.5 settled, B.1 settled,
C.1 settled negatively in general with the corollary gate open, D.1 settled.

## 4. Bridges (RH, GRH, purity, weights, Weil conjectures, L-functions, Tate motives)

Criterion of the brief as corrected on 20 Nov (~21:1x UTC). `BRIDGE_FLAGS.tsv` has no row of this run. Three groups
of my rows touch the motivic side; literature locators below are from memory and marked "to verify".

1. **A2.2–A2.14 (stable and pointed derivators).** Motivic categories are stable derivators of exactly this kind
   (Ayoub's algebraic derivators; `DM(k, Λ)` of Cisinski–Déglise), and Tate twists and weights live in them. What the
   rows give back, as mathematics: for the derivator `D(I) = Ho Fun(I^op, 𝒞)` of a stable Λ-linear motivic category
   `𝒞 = DM(k, Λ)`, A2.4/A2.9 give `W_D = R(L_D)` with `L_D = {V ∈ Sp : V ⊗ 1_𝒞 = 0}`. Since the unit functor
   `D(Λ) → DM(k, Λ)` is fully faithful (motivic cohomology of `k` in weight 0 is `Λ` in degree 0; to verify), `V ⊗ 1_𝒞 = 0`
   iff `V ∧ HΛ = 0`, so `W_D = W_{HΛ}`: the constant-coefficient localizer of any such motivic derivator is ordinary
   Λ-homology. Tate twists `Λ(n)`, weights and L-values are invisible to the localizer. So RH or GRH (cited to Alpöge)
   and purity (Deligne, *Weil* I, II) carry nothing to these rows, and the rows give nothing back to them beyond this
   negative statement.
2. **C.1–C.29 (the linear "Thm(?)" of 134-8: localization of a k-linear category by an interval `J`).** Its motivic
   instance is Voevodsky's `DM^eff`: Nisnevich sheaves with transfers localized at the interval `A¹`, where
   `Z(1) = Z_tr(G_m)[−1]` is born [correction: read the *reduced* motive, `M̃(G_m)[−1] ≃ 𝟏(1)`, since
   `M(G_m) ≃ 𝟏 ⊕ 𝟏(1)[1]` (Voevodsky 2000; Mayer-Vietoris on P¹) (ALPOGE_BRIDGES BR-DER-02, confirmed) (corrected
   21 Nov 2026 after the intake of ALPOGE_BRIDGES, Claude Opus 5.5 at effort high)]. In that instance the remaining gate C.10 (`Lφ(GP) = 0` on acyclic projective
   complexes) is supplied not by the formal hypotheses (a)–(d) but by a property of the category: homotopy invariance of
   the cohomology of homotopy-invariant presheaves with transfers over a perfect field (Voevodsky, *Triangulated
   categories of motives over a field*, Thm 3.1.12; to verify), with the Suslin complex as resolving functor. What the
   rows give back: C.26 proves that (a)–(d) alone cannot replace such a theorem, and C.10 states exactly what has to be
   proved. RH and purity carry nothing here: the statement is about categories, not about weights or L-values.
3. **D.1–D.10 (Toën's schematization).** Over a finite field, Deligne's purity (*Weil* II) is what puts a weight
   decomposition on the ℓ-adic pro-algebraic (schematic) homotopy type of a smooth proper variety and makes it formal,
   the ℓ-adic analogue of Deligne–Griffiths–Morgan–Sullivan (Pridham, weight decompositions on étale fundamental
   groups; Olsson; to verify). What the rows give back: D.3–D.4 identify, on all small categories, the class of maps
   that schematization inverts (equivalences of perfect local systems, with the affine-`π₁` data D.2 shows are needed),
   i.e. the localizer on which those weight decompositions are defined. Purity itself is not used by any row.

The other rows (A.1–A.7, A34, A4, B) are about unstable and chromatic homotopy and interval generation; they touch no
Tate twist, weight, L-value or K-group, and the link carries nothing.

## 5. Prompt updates (for a successor of DER_LOCALIZERS)

Unchanged from `PROMPT_UPDATES_20261119.md` §3, with these additions from today's reading:
1. Add to the state: A2.9, A2.12, A2.13, A2.14, A34.1, A34.2, A34.5, A4.5, B.1, B.2, C.1–C.4, C.6, C.7, C.10, C.26
   followed by this intake (Claude Opus 5.5 at effort max, 20 Nov).
2. Ask the run to open and check, before use, the external inputs these rest on: Bousfield 1996 Thm 3.3, Key Lemma 1.6,
   Cor. 3.2(ii); Bousfield 1997 Lemma 8.13; Chataur–Scherer 2006 Prop. 3.4; Cisinski–Kan Cor. 4.19, Thm 5.22.
3. For C.raw_gate, give it the exact form of C.10 and the list of sufficient conditions already proved, and ask for the
   decision under the corollary hypotheses (finitely presented projective generators), which C.26 does not meet.
