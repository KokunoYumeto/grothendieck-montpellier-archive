## STUDY

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

## HUNCHES

- **H90-1 (new).** The notes of 90/2-24 prove the equivariant resolution property for a flat affine G with A[G] a filtered union of finite projective subcoalgebras, acting on X with a G-linearized ample sheaf. The method is the stable hull through Γ^• and the algebras U_i = B̌_i, the route of R. W. Thomason, Adv. Math. 65 (1987), 16-34 (locator to be checked). The leaves are versos of the EGA IV §18 typescript (print 1967), so the notes date from about 1966-68, the years of J.-P. Serre's "Groupe de Grothendieck des schémas en groupes réductifs déployés" (Publ. Math. IHÉS 34, 1968), which the title "KG(X)" fits. Grounds: content and versos. We claim no priority.
- **H90-2.** His NB of 90/10 should be true: for G flat of finite type over a Dedekind ring, the conditions of Lemma 1 on A[G] hold iff every irreducible component of G meets every fibre. That would make A[G] projective, by e) and countable generation. Grounds: the example (identity) ⊔ (generic point) ⊂ (ℤ/2)_A, whose algebra A × K fails b). Literature: Raynaud and Gruson, Invent. Math. 13 (1971), part I, §3 (locator to be checked).
- **H91-1 (new).** Condition R (91/9) is the group form of Raynaud-Gruson purity, and the corrected adic conditions (L) of 91/8 and 91/12 are purity conditions: every point, resp. every associated point of E_T, specializes into the special fibre. The theorems of 91/5-12 are then noetherian forms of Raynaud-Gruson I, §4 (locators to be checked), written by 1967 (the cover dates a letter of 1967 in the cote). Grounds: the statements as corrected; the dates.

## PACKAGES

- **P91-1: purity and representability without projective hypotheses (91/5-14).**
  - **Question:** prove that, for a flat group scheme of finite type over a locally noetherian base, condition R is equivalent to S-purity. Then prove the representability criteria for ∏_{X/S} Y/X and for the flattening functor in the corrected form (L) (special fibre), together with Corollary 3 and its consequences (Cent, Transp, Norm, pseudo-torsors with G flat, G/N).
  - **Why it matters:** these are the "méthodes non-projectives" announced on 91/3, and the base of the Hom theorem continued in SA03.
  - **What it rests on:** 91/5-14 as read and checked here (SA02-R91-01..04; corrections SA02-K91-01..03).
  - **Strongest reduction on the pages:**
    - the adic condition ⇔ (L) with the special fibre, by the local flatness criterion;
    - for groups, R reduced to discrete valuation rings;
    - Corollary 3 as the engine of the quotient statements.
  - **Material:** `cotes90_91-2-18.md`; K91-01; MPL_90+91_002-018 (second block); the stage-A dossier §4.1; SGA 3 VIII §6; Raynaud and Gruson 1971.
- **P90-1: the scope of the KG(X) notes (90/2-24).**
  - **Question:** decide for which flat affine G over a Dedekind ring A[G] satisfies Lemma 1 a) (H90-2). Then state and prove the resulting resolution theorem for equivariant coherent sheaves in the generality of the notes, and compare it with Thomason 1987.
  - **Why it matters:** it fixes the reach of the KG(X) method and its place relative to Serre 1968.
  - **What it rests on:** 90/2-24 (SA02-R90-01, R90-02); the correction SA02-K90-01.
  - **Strongest reduction on the pages:** Lemma 2 (stable saturated finite subcoalgebras under a)) and the U_i-module argument.
  - **Material:** `cotes90_91-2-18.md`; K90-01, K90-02; MPL_90+91_002-018 (first block); the stage-A dossier §3.
