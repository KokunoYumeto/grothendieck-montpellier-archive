# SA02: Géométrie et topologie combinatoire, part 2 (cotes 84, 90, 91/2-18): sweep 3, wave 1

**Lead:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026, by sweep3/WAVE1_LEAD_BRIEF_20261119.md. Reader messages: `READER_PROMPTS.md`.

**Readers** (all Claude Opus 5.5 at effort max; method: _tools_a6d42bf6/READER_BRIEF.md):
- R4, agent a774f5c4e87a59ea4: cote 84 (K84-01 to -07 for scans 2-111; Pro MPL_84_097-145 and MPL_84_146-193 for 112-193, compared with the Codex text from 97) (`readings/cote84*`).
- R3, agent a5723c09c05df9eda: cote 90 (scans 2-25) and cote 91, scans 2-18 (K90-01, K90-02, K91-01 against Pro MPL_90+91_002-018, scan by scan) (`readings/cotes90_91-2-18*`).
- Both used the stage-A dossier of these pages (GPT-6 Astra, ChatGPT Pro mode; `grothendieck_archive_transcription_20261110/stage_a_20261118_sent/returns/SA02_part2_final_20261119T1453Z_unzipped/`) as a witness, checked where used.

**Sources:**
- the Pro packages in `inputs/SA02/pro/`;
- the Codex-web folders K84, K90 and K91-01 in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/`;
- the scans in `grothendieck_archive_montpellier/`;
- the maps in `sweep2/SA02/WHAT_IS_WHERE.md`, `TOPIC_NOTES.md` and `sweep2/REPORTS/cote84_*.md`.

**Not yet read in full** (to be read): the typescript backs of cote 84 (84/5, 7 and the odd scans 125-193: Récoltes et Semailles, October 1984), identified but not read; the odd versos of cote 90 (typed EGA IV §18), identified against the print by number but not transcribed; the remaining items listed at the end of each reading.

**Ink still to decide on the scans:** the corrections marked "not viewed" in CORRECTIONS.tsv.

**Where the questions go** (one prompt per cluster of related questions):
- cote 84, with cote 77 (from SA04) and cote 83 (from SA01): RESEARCH_SA02, the theory of quadratic covers over an arbitrary base, their contracted product and his generalized Arf-Stiefel-Whitney invariants;
- cotes 90 and 91/2-18: the working-through objects H01J (KG(X)), H01K (the EGA IV typescript) and H01L (Hom functors) have unsent prompts; the readers' results go into those prompts.

The items below are the readers' integration blocks, one per stretch.

<!-- reading:cote84 -->
### From the reading cote84

**Extent.**
- Every transcribed mathematical scan was read: 2-122 and the even scans 124-192.
  - 2-111 in the Codex-web folders K84-01 to K84-07.
  - 112-193 in the Pro packages (GPT-6 Astra, ChatGPT Pro mode), with the two witnesses compared scan by scan from 97.
- The typescript backs (84/5, 7 and the odd scans 125-193, Récoltes et Semailles, October 1984) were identified, not read.
- The stage-A dossier (GPT-6 Astra, ChatGPT Pro mode) was checked where used.
- The checks are 20 check events (re-proofs, sympy, a witness comparison) and 13 corrections.

**Dating.** The mathematics of 124-192 is on the backs of the October 1984 typescript, so it dates from late 1984 or later. That fits cotes 79 (1982 or later) and 81 (1981 or later).

**What the cote is.** A sustained theory of quadratic covers over an arbitrary base, aimed at "invariants d'Arf-Stiefel-Whitney généralisés" (title sheet 84/43).

1. **Binary forms (84/9-42, a draft).**
   - Similitude structures ↔ subalgebras 𝒜 ⊃ O of End(E).
   - The quadratic algebra 𝒜_Q of a binary form ("l'invariant d'Arf").
   - Equivalences: (E, Q) primitive ↔ (𝒜, invertible 𝒜-module) ↔ (X', Λ'), which is Kneser's and Wood's correspondence.
   - The uniqueness of the canonical involution, and reflections.
   - Two corrections: a sign he flagged himself (Q_u = x ∧ u(x)), and a topology margin, fppf ≠ étale for non-étale A in characteristic 2 (the dossier's example, rechecked).
2. **Quadratic covers through (L, P_1, Q) (84/44-62).**
   - When 2 is regular, covers ↔ (L, δ, T_0) with T_0² ≡ δ (4). This is the (L, D, b_0) classification of cote 77, so my cote 77 question belongs here.
   - The explicit 𝒜 = {(b, r)} with N = (b² - r²δ)/4.
   - Characteristic 2: covers as torsors under G_T = ker(u ↦ u² + Tu).
3. **The contracted product (84/63-66, 84/87-106, 172-192).**
   - b = b_1b_2 and c = b_2²c_1 + b_1²c_2 - 4c_1c_2, with u = 2u_1u_2 + b_2u_1 + b_1u_2 (checked by sympy). This is cote 83's ∗-composition.
   - Th. (84/90): the admissible form with Q(y_1 ∗ y_2) = Q_1δ_2 + Q_2δ_1 + 4Q_1Q_2, proved for all points. δ = δ_1δ_2.
   - The product is the fixed ring of σ_1 ⊗ σ_2 iff 2O + b_1O + b_2O = O (checked over Z).
   - The relative trace and norm, and "quasi-quadratic" algebras.
4. **χ-trivialized extensions (84/66-87, 124-170).** A monoidal structure on extensions with a χ-retraction. In his final convention b = π(x), b_{x_1∗x_2} = b_1 ⊗ b_2 ("Il n'y a pas plus simple !").
   - The sign questions of 130-140 stand as decided in sweep 2: the plus convention, a missing χ, and "2 - χ = 1", corrected by himself on 152.
   - New: the "signe étrange" of 134-136 is consistent. It is exactly what makes his map Φ: E → Hom^!(E, L) (-id on L) multiplicative.
5. **Three quadratic algebras (84/4, 111-122).**
   - The seven quadratic and seven rank-4 subalgebras of A_1 ⊗ A_2 ⊗ A_3.
   - Quasi-biquadratic systems, and the étale case with the lemma of 120 (false as written, corrected in sweep 2).
6. **A graded monoid with parities (84/2, 54-56).** Even triples (L, δ, T_0), odd pairs (L, δ), β(L, δ) = (L, 4δ, 0). Associativity reduces to two identities, which hold.

**Links.**
- Cote 77 (SA04-25): the (L, D, b_0) classification.
- Cote 83 (SA01): the ∗-product and the λ-split extensions.
- Within SA02: SA02-1 ↔ SA02-4 at χ = 2, and SA02-14 ↔ the parity product.
<!-- /reading:cote84 -->

<!-- reading:cotes90_91-2-18 -->
### From the reading cotes90_91-2-18

Reader R3 (Claude Opus 5.5 at effort max) of a6d42bf6fe2b0d8a8, 19 Nov 2026. Read: cote 90 (scans 2-25) and cote 91, scans 2-18, every scan in both witnesses: Codex-web K90-01, K90-02, K91-01 and the Pro package MPL_90+91_002-018 (GPT-6 Astra, ChatGPT Pro mode), compared scan by scan. The stage-A dossier (GPT-6 Astra, ChatGPT Pro mode) was used as a witness. 12 check events, 9 corrections.

**Cote 90 (SA02-10, SA02-11).** The cover reads "KG (X) : notes manuscrites (s.d.)"; "Verso: mention d'EGA 4". The leaves alternate.

*Grothendieck's notes (even scans): representations of flat affine group schemes.*
- Lemma 1 (90/2) is on flat modules over a Dedekind ring: saturations of finite submodules are finite ⇔ M is a filtered union of saturated finite submodules. His further "equivalent" condition, no submodule ≅ A^{(p)}, is only necessary. M = Σ_p p^{-1}ℤ ⊂ ℚ is a counterexample. We found it independently; the stage-A dossier has the same one.
- Lemma 2: saturated stable finite subcoalgebras exist.
- A faithful representation in finite type.
- Comodules over B_i = modules over U_i = B̌_i, so every G-module of finite type is a quotient of one that is projective of finite type.
- Over a base with an ample G-linearized sheaf, the stable hull F' of a quasi-coherent F, and every equivariant coherent sheaf as a quotient of an equivariant locally free one, via Γ^•.
- All checked. This is the equivariant resolution property behind KG(X) (Serre 1968; Thomason 1987, by name; locators to be checked).

*The versos (odd scans): typed EGA IV §18, upside down.*
- IV-950..953 = print 18.6.6-18.6.12; IV-962..965 = print 18.8.10-18.9.4; an insert -3-/-4- = 18.9.5; typed "Rabiots" = 18.9.7-18.9.9.
- The typescript is an earlier state: its 18.8 numbers run one behind the print from print 18.8.12 on, its internal references say 18.8.7 where the print has 18.8.10, and print 18.8.18 is absent.
- The Rabiots' 18.9.9 says "universellement caténaire" where the print has "universellement japonais" (a slip; the stage-A dossier agrees).
- Grothendieck's margins criticize the typescript ("« séparés » inutile !", "pas très clair", "vider ... ou bien arranger").

*Witnesses.*
- K90 omits two paragraphs of the typed page 90/7 and an item d) "(R_n)" on 90/13. The ink and the Pro have both (viewed).
- Mean similarity 0.93.

**Cote 91/2-18 (SA02-12): Hom functors without projective hypotheses ("Autour de Néron").**
- *The theorem on ∏_{X/S} Y/X* (X flat of finite type, Y → X a monomorphism): representable, by a closed subscheme for closed Y, iff it commutes with adic limits of artinian rings. Conditions 1°-8° checked.
- *The adic condition (L)* for groups reduces to discrete valuation rings, and to "condition R" (open subgroups containing the special fibre are everything). R holds for connected fibres and under a finiteness condition. Then Cent, Transp and Norm are representable.
- *The flattening functor:* the same criterion. His reformulation (L) says "voisinage de la fibre générique", in the ink and in both witnesses. It must be the special fibre: the counterexample is a skyscraper on P¹ over a discrete valuation ring, and with "générique" his own Corollary 1 (proper) fails. The stage-A dossier does not note this.
- *Corollary 3:* f factors as a faithfully flat map followed by a monomorphism iff pr_1: X ×_S X → X is flat.
- *Corollaries of 91/14:* the pseudo-torsor corollary needs G flat (counterexample S ⊔ V(t) ⊂ (ℤ/2)_S; the stage-A dossier agrees). G/N exists for N = Ker u flat.
- *The relative unramified Hom theorem* (91/16-18): the unramified locus is open (corepresenting modules M_u, M_w, Nakayama). The deformation proof breaks off at 91/18 and continues in SA03.
- *Witnesses:* mean similarity 0.89, no statement-changing difference.
<!-- /reading:cotes90_91-2-18 -->
