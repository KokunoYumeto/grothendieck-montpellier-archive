# Intake of RESIDUE (return of 11 Nov 2026), the rows of packet 76

Claude Opus 5.5 at effort max, the Dérivateurs intake sub-agent of 19 Nov, resumed by the main session; 20 Nov 2026
(from 19:26 UTC). Brief: `field_experts/intake_20261120/INTAKE_BRIEF.md`. The run is GPT-6 Astra (ChatGPT Pro mode),
11 Nov 2026; unrefereed outside this project. My agent id is not shown to me.

## 0. Scope

**Return read:** the return of 11 Nov 18:32 UTC (no checkpoints), folder
`derivateurs_companion_20261109/pro_returns_20261110/8_RESIDUE/RESIDUE/`; prompt as sent
`pro_prompts_20261110/ALREADY_RAN/8_RESIDUE/PROMPT.md`; sort `SORTED/RESIDUE.md`. Earlier: my intake of 19 Nov
(`INTAKE_FREX_DERLOC_REVLOC_RESIDUE_20261119.md`, §5) and the author checks of Part E of 11 Nov
(`pro_reviews_20261110/8_RESIDUE/checks_author/`, Claude Fable 5.2).

**My rows:** the 41 RESIDUE rows of packet 76.

**Read in full, every step followed (16):** A.1, B.2, B.4, B.5, C.1, C.4, C.5, C.6, D.4, D.6, D.8, F.1, F.2, F.4, I.1,
I.2. (B.2, B.4, B.5 were read on 19 Nov; D.8 was re-proved by hand on 19 Nov; the rest today.)
**Read with their cited inputs not opened, or in outline (2):** D.5 (Known; the argument followed, Lurie HA 4.7.3.5
and Rivera–Wierstra–Zeinalian 2021 not opened), F.3 (the gap-polynomial induction followed in outline).
**Open records (3):** B.10, C.8, I.7: read; no proof to check.
**Statement level only (20):** A.5, B.12, B.15, C.3, D.1, D.10, D.11, D.12, G.5, H.2, H.3, H.5, H.6, I.3, I.4, I.5, I.6,
I.8, I.9, J.1.
**Not opened:** the cited sources (Cisinski 2006 and 2019, Maltsiniotis, Lurie HA and HTT, Rivera–Wierstra–Zeinalian,
Jansen 2023, Cnossen–Lenz–Ramzi 2025, Ara–Maltsiniotis); no program of the run was run; no PDF check.

## 1. Verdicts, row by row

Locators are `sections/<file>:<line>`.

| Row | Run's status | My check | Verdict |
|---|---|---|---|
| A.1 | Proved | confirmed | equivalence transports: the classifying map factors through the 2-type `B Eq(C)`, so connecting maps vanish for `r ≥ 2`; a contractible total category forces `BC` a 1-type and `BB` a 2-type; none over the rectangular band (`BM ≃ S²`, `π₃ ≠ 0`) (`A.tex:4`) |
| A.5 | Proved | statement | the monoid census of orders ≤ 5 (1, 2, 7, 35, 228; only the rectangular band is not a 1-type); counts agree with the published count of monoids (OEIS A058129, from memory: to verify) (`A.tex:102`) |
| B.2 | Proved | confirmed (19 Nov) | the quotient `𝒬` of `Hot` by the maps through `S¹` (`B.tex:54`) |
| B.4 | Proved | confirmed (19 Nov) | crowns `C₈ → C₄` of degree 2, suspended over a three-object poset: relative Theorem A fails for `W_circ` (`B.tex:138`) |
| B.5 | Known | confirmed (19 Nov) | homotopic functors and adjunctions under the literal axioms, by absolute Theorem A on `A × [1] → A` (`B.tex:186`) |
| B.10 | Open | open record | the statement-by-statement audit of XVI ms. 1–27 and XV §9 (`B.tex:332`); partly answered since by DER_FOLLOWUP G.11–G.14 |
| B.12 | Proved | statement | the formal decomposition and finite localization statements of XVI 2.1–2.6, XV 9.4–9.6 (`B.tex:390`) |
| B.15 | Refuted | statement | Lemma 2.5 for an arbitrary class `W` (four-object diamond) (`B.tex:395`…) |
| C.1 | Proved | confirmed | with enough `W`-then-intrinsic factorizations, `W ∩ Fib_W` = universally weak maps, and weak maps between intrinsic fibrations stay weak under base change (XII axiom (b)) (`C.tex:3`) |
| C.3 | Refuted | statement | a five-object, sixteen-arrow category with pullbacks where (a), (b) hold and (c) fails (`C.tex:90`) |
| C.4 | Proved | confirmed | finite categories with pullbacks have only monomorphisms but unboundedly many arrows (cyclic groups) (`C.tex:182`) |
| C.5 | Proved | confirmed | the fence path category gives a strictly functorial perfect replacement; lifting categories have initial/terminal objects stagewise (Cisinski 2019 Thm 4.4.36, not opened) (`C.tex:207`) |
| C.6 | Proved | confirmed | every intermediate full subcategory between `Parf` and `Cat/S` has the same localization, for every fundamental localizer (`C.tex:277`) |
| C.8 | Open | open record | the least number of objects (at most 5) (`C.tex:351`) |
| D.1 | Known | statement | Cisinski 2006 Props 6.2.3–6.2.4, §9.2.1, Cor. 9.2.15 (not opened) (`D.tex:3`) |
| D.4 | Refuted | confirmed | `Fib_W` is no lifting class for `W_∞ ⊆ W ⊆ W₀`: each fence fibration `p_r: C_r^▷ → [1]` is intrinsic, their product is not (`∏C_r` is disconnected by the distance argument, `∏A_r` connected) (`D.tex:51`) |
| D.5 | Known | argument followed | `W^lc_{D(k)}`: bijective on components, `π₁`-isomorphism, `k`-homology equivalence of universal covers; `W^lc_{D(Z)} = W_∞`; sets give `W₁`, groupoids `W₂` (`D.tex:64`) |
| D.6 | Proved | confirmed | rational local coefficients need only the vanishing of `π₂(B) → π₁(F)`; necessity by degree-`m` maps of `S²`; the path fibration over `S³` shows no higher condition (`D.tex:73`) |
| D.8 | Refuted | confirmed (re-proof, 19 Nov) | a covering with monodromy through a finite p-group is intrinsic for mod-p homology (`D.tex:93`) |
| D.10 | Proved | statement | BISITE B.15's 48 entries recomputed, no change (`D.tex:108`) |
| D.11 | Proved | statement | the fibration-axiom table for `W₀, W₁, W_n, W_Q, W^lc_{D(Q)}, W_∞` (`D.tex:135`) |
| D.12 | Proved | statement | for HZ and HQ, exactly the coverings with trivial monodromy are intrinsic (`D.tex:104`…) |
| F.1 | Proved | confirmed | total `W_∞`-asphericity (XII ms. 88) ⇔ every action component weakly contractible ⇔ integrally acyclic; exactness implies it (TOTASPH C.5, ours, reproved independently) (`F.tex:2`) |
| F.2 | Proved | confirmed | totality gives common successors and affine equalizers of original pairs (`F.tex:17`) |
| F.3 | Proved | key steps / outline | full subcategories `A_S ⊂ Δ_inj`: total iff `S` singleton or unbounded (integral affine cones `C_{n,k}`); FI and `Inj(N)` not total; free categories total iff filtered (`F.tex:33`) |
| F.4 | Proved | confirmed | a total category with a weakly terminal object is filtered (the period argument for monoids); the finite-object Cat-colimit case (`F.tex:62`) |
| G.5 | Proved | statement | local product projections preserve the open-test class (`G.tex:75`) |
| H.2 | Refuted | statement | the one-object idempotent example (`H.tex:142`) |
| H.3 | Proved | statement | forgetful lifting categories of stable curves are contractible or `BZ` (`H.tex:202`) |
| H.5 | Proved | statement | the entrance forgetful functor is `W_∞`-proper for every stable `(g,n)`, smooth only for `(0,3)` (`H.tex:321`) |
| H.6 | Proved | statement | direct image = right Kan extension for the universal curve (moduli stack) (`H.tex:409`) |
| I.1 | Proved | confirmed | `p` and `Δ_p` smooth ⇔ `p` a discrete fibration: the largest diagonal-stable smooth class (`I.tex:3`) |
| I.2 | Proved | confirmed | space coefficients: universally ambidextrous discrete fibrations are isomorphisms (`I.tex:40`) |
| I.3 | Proved | statement | the correspondence functor for smooth right legs (Cnossen–Lenz–Ramzi 2025 Cor. 2.6(2), not opened); completes BISITE F.10 (`I.tex:61`) |
| I.4 | Proved | statement | Mann's Prop. A.5.10 does not apply as such (finite cancellation counterexample) (`I.tex:133`) |
| I.5 | Proved | statement | the opposite formalism on proper right legs (`I.tex:149`) |
| I.6 | Proved | statement | pointed spaces: unions of components (`I.tex:161`) |
| I.7 | Open | open record | the reversible classification and `D ↦ D′` (`I.tex:183`) |
| I.8 | Proved | statement | spectra and `D(k)`: finite discrete bifibrations (`I.tex:201`) |
| I.9 | Proved | statement | second stages: `W^{(2)}_{Sp} = W_∞`; for `D(F_p)` the test (I.9.4) on `π₁, π₂` and the 2-connected cover (`I.tex:194`) |
| J.1 | Proved | statement | strict 2-categories over a 1-category base: the fine theories (Ara–Maltsiniotis, not opened) (`J.tex:3`) |

**Counts (41 rows):** 16 confirmed, 2 read with uncited inputs or in outline, 3 open records, 20 at statement level; no
row refuted by me, no gap found. The run's labels for these 41 rows: 30 Proved, 5 Refuted, 3 Known, 3 Open.

## 2. What is new

- **The strongly saturated `W_circ` (B.2–B.4) and the failures under the literal axioms (B.8, B.15–B.17)** were the
  first in our programme (11 Nov), before REVLOC F.1 and DER_FOLLOWUP Part G; see the 19 Nov intake §6b item 4.
- **A.1** (no equivalence-transport bifibration with contractible total category over a base whose classifying space is
  not a 2-type) settles Lead 2 of the RESIDUE prompt and the equivalence case of VIc-C022; the non-equivalence adjoint
  case stays open (A.8, treated 19 Nov).
- **D.4** (intrinsic fibrations are never a lifting class between `W_∞` and `W₀`) and **D.6** (rational local systems:
  only the `π₂ → π₁` boundary) are new to us; D.8/D.12 show the homology case depends on the coefficients.
- **C.1–C.6** prove Lead 3 (XII ms. 215–218, 240) and the intermediate-subcategory statement for every fundamental
  localizer; C.3 improves BISITE E.12 to five objects.
- **F.1–F.4** reprove TOTASPH C.5, C.13 by other routes and add the classification of the full subcategories of
  `Δ_inj` and of free categories. F.5 (total ⇒ exact) was refuted since by TOTAL_EXACT_2 (`C_δ`).
- **I.1** identifies the discrete fibrations as the largest diagonal-stable class of `W_∞`-smooth maps; new to us.

## 3. Implications

**Archive.** VI ms. 186 (row VIc-C022): equivalence-transport bifibrations over the rectangular band are excluded
(A.1). XII ms. 215–218 and 240–241 (row XIIc B062): Grothendieck's "je présume que pratiquement …" is right under his
factorization hypothesis (C.1, C.2, C.7), and (a), (b) do not imply (c) in general (C.3, five objects). XII ms. 225
(row XIIc-a C033) and I ms. 99–100: the intrinsic fibrations of `W_n` (D.1–D.3) and of the coefficient localizers (D.5,
D.6) are determined, with D.4 against a lifting-class description. XII ms. 88 (row II-C-003): F.1–F.4. XVI ms. 1–27,
XV §9: B.12, B.15 (with the 19 Nov rows B.3, B.8, B.16, B.17).

**Programme.** Nothing here contradicts later returns. The open records B.10, C.8, I.7 and the rows A.8, D.7, D.9,
E.6, G.3, J.2, J.3 (19 Nov) are the leftovers (`PROMPT_UPDATES_20261119.md` §4).

## 4. Bridges

Criterion of the brief as corrected on 20 Nov. `BRIDGE_FLAGS.tsv` has no row of this run; the rows below meet the
structure of six operations, coefficients and weights. Locators from memory are marked "to verify".

1. **H.3–H.6 (forgetting a point on `M̄_{g,n}`; constructible coefficients by exodromy).** Over `F_q`, Deligne's purity
   (*Weil* II), with the stability of pure complexes under `f_* = f_!` for proper `f` (BBD 5.1.14; to verify), makes
   `Rπ_*Q_ℓ` pure for the proper universal curve `π: M̄_{g,n+1} → M̄_{g,n}`, and the decomposition theorem splits it into
   shifted intersection complexes. At a boundary stratum the weight filtration on `H¹` of the nodal fibre is the
   monodromy filtration of the node (weight 0 from the loops of the dual graph; Picard–Lefschetz). [Correction:
   ordinary H¹ of the singular fibre C is H¹(Γ) (weight 0) extended by ⊕_v H¹(C_v) (weight 1), from
   0 → H¹(Γ) → H¹(C) → ⊕_v H¹(C_v) → 0 for a split nodal curve; the weight-2 quotient belongs to the nearby fibre, not
   to H¹ of the singular fibre (ALPOGE_BRIDGES BR-NODE-01, confirmed) (corrected 21 Nov 2026 after the intake of
   ALPOGE_BRIDGES, Claude Opus 5.5 at effort high).] What the rows give
   back: H.3 locates exactly where the entrance-path model has a non-contractible lifting category, `BZ`, namely where
   forgetting the mark contracts a rational bridge and the exit arrow smooths the new node: the combinatorial locus of
   that Dehn-twist monodromy. H.6 identifies `Rπ_*` on constructible coefficients with the right Kan extension on the
   entrance categories. So these rows give the stratified combinatorics on which purity puts the weights; they use
   neither purity nor RH. (Rows read at statement level.)
2. **I.1–I.9 (the six operations on small categories).** In the motivic six operations (Ayoub; Cisinski–Déglise),
   relative purity for smooth `f` of relative dimension `d` gives `f^! ≅ f^* ⊗ Λ(d)[2d]`: the Tate twist is the
   dualizing object, of Frobenius weight `−2d` in the ℓ-adic realization over `F_q` (Deligne). What the rows give back:
   in the Kan formalism on `Cat`, the largest diagonal-stable smooth class is the discrete fibrations (I.1, confirmed),
   and for all allowed maps `f^! = f^*` (I.5): the twist is trivial; for spectra and `D(k)` the ambidextrous maps are the
   finite discrete bifibrations (I.8). The categorical formalism has no twist and no weights, so the dictionary "Tate
   twist = dualizing object" has no counterpart there and purity and RH (L. Alpöge, *Remark*,
   https://alpo.ge/remark.pdf) carry nothing to these rows.
3. **D.5, D.6, I.9 (locally constant coefficient localizers `W^lc_{D(k)}`).** Purity concerns the Frobenius weights of
   lisse `Q_ℓ`-sheaves, which are locally constant `D(Q_ℓ)`-coefficients with a Frobenius action. The rows determine,
   on homotopy types without Frobenius, which maps induce equivalences on all such coefficients (D.5: `π₀`, `π₁`, and
   `k`-homology of universal covers) and which maps are intrinsic fibrations for `k = Q` (D.6: only the boundary
   `π₂ → π₁`). A Frobenius-equivariant map of étale homotopy types of `F_q`-varieties in `W^lc_{D(Q_ℓ)}` then induces
   weight-preserving isomorphisms by functoriality; the rows say which maps qualify, and purity enters nowhere.
4. **The rest** (A: bifibrations over monoids; B: the literal axioms; C: the fibre axioms; F: total asphericity; G:
   spaces over `R`; J: 2-categories) concern classes of functors defined by homotopy types alone, with no coefficient
   carrying a twist or a Frobenius; the link carries nothing.

## 5. Prompt updates

As in `PROMPT_UPDATES_20261119.md` §4. Add: A.1, C.1, C.4–C.6, D.4, D.6, F.1, F.2, F.4, I.1, I.2 confirmed by this
intake (Claude Opus 5.5 at effort max, 20 Nov); a successor taking A.8 (VIc-C022) starts from A.1 and A.4 and treats
only non-equivalence adjoint transports.
