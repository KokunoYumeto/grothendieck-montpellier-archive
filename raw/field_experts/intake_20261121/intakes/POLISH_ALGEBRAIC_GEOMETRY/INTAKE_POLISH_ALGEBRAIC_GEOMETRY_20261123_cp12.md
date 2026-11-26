# Intake: POLISH_ALGEBRAIC_GEOMETRY (prompt 90), checkpoint 12

Intake by Claude Opus 5.5 at effort high, 23 Nov 2026 (about 11:06 to 12:40 UTC), launched by the main session
(Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode). The run's own records give its effort as
"inherited reasoning settings" and do not state it further. The run is **still going**: checkpoint 12 was saved at
10:00 UTC, and movement review 07 at 10:00 UTC found movement, so the no-movement count is 0.

Work file: `<local>/Documents\agent_notes\20261123T1106Z_Intake_POLISH_ALGEBRAIC_GEOMETRY_cp12_NOTES.md`.

## 0. What I read, and my scope

Return folder:
`grothendieck_archive_transcription_20261110\research_returns\POLISH_ALGEBRAIC_GEOMETRY_checkpoint_12_20261123T1000Z_unzipped\`
(top level; it holds README.md).

**Read in full:**
- PROMPT.md as sent (`TO_SEND\PRO\1_Archive_research_by_topic\SENT\90_POLISH_ALGEBRAIC_GEOMETRY\PROMPT.md`).
- README.md, FINAL_READS.md, LEDGER.md and CORRECTIONS_FOR_AUTHORS.md (all 498 lines).
- From the records:
  - `igusa_corrections/FULL_CHECK.md` §2 (the flatness proof, which the dossier leaves out);
  - `ROOT_DIFFERENTIAL_PICARD_EXCLUSION.md`;
  - `papers_5_6/PAPER6_DISPOSITION.md`;
  - the heads of `ROOT_PROOF_CORRECTIONS.md`, `ROOT_MODULARITY_BASE_CORRECTION.md` and `CURRENT_PROOF_GAPS.md`.

**Read in part** (the parts named in §1):
- LITERATURE.md: the Paper 1 entries, polarization, very ample, representability, roots of a basis and the correction
  targets.
- CHECK_EVENTS.tsv: its type counts only.

**Papers:** I read each main proof named in §1 line by line, deriving each step before I compared it with the text.
- Paper 1: `introduction.tex`, `arithmetic.tex`, `wild.tex`, and `boundary.tex` up to Proposition finite-wild.
- Paper 2: main.tex lines 23–322 (Section 1, G1, the whole A3 construction). Its other seven input files I read only
  at the level of their statements in Section 1.
- Paper 3: Section 1 (statements) and lines 179–253 (fpqc descent, the counterexample). `representability.tex` and
  `descent.tex` were not read.
- Paper 4: Section 1, the proof of Theorem 1.1, and the algebra part of Theorem 1.2 (lines 99–238). The module-condition
  lemmas and Theorem 1.3 were not read.
- Paper 5: Section 1, the torsion lemma and the proof of Theorem 1.1 (lines 41–250). Theorems 1.2 and 1.3 were read at
  statement level only.

**Opened online for the corrections:**
- the live Stacks pages for Tags 07BV, 0BTP and 02W8;
- Popescu 2022 (PDF SHA-256 `30510243…6141b`, matching the run's), pp. 506 and 510–511;
- Lauritzen–Rao, alg-geom/9604012, pp. 1–2.

**Not done:**
- REGISTER.tsv was not checked row by row (1,524 of its 1,577 rows are reconstructions the run has not re-verified).
- No PDF was rendered or looked at by me.
- No source behind the other corrections was opened by me (Milne, Ekedahl, Liedtke, Cossec–Dolgachev–Liedtke,
  Cotner–Zavyalov, Achter–Casalaina-Martin, Chai, Chai–Oort, Partsch). For those I checked the run's mathematics against
  the claims as the run quotes them.

## 1. The papers' main theorems: verdicts

The verdicts use the rubric's terms. "Confirmed" means a targeted proof check after exposure, with each step rederived.
"Statement only" means not read in full.

### Paper 1. Counterexamples to Grothendieck's cohomological-dimension conjectures (13 pp)

- **Theorem 1.1 (A2, the arithmetic counterexample): targeted proof check, confirmed.** I found no gap. Checked:
  - the wreath lemma: Σ is a homomorphism; A₀ is elementary abelian; the action is v·(b,u)=(b,u+bv); φ is equivariant
    and surjective; the transfer is (x+y,x+y); and (b,u;v)²=(0,bv;0);
  - the quadratic step: the field M is the class field of C_F; Chebotarev in the ray class field of M gives 𝔓=(η)
    with η/b≡1 mod 𝔪; Gal(Ñ/F)=𝔽₂[V]⋊V is split by permuting the radicands;
  - the inertia (1,σ) lies outside H, so N/L is unramified over 𝔭;
  - inertness in both Frobenius cases, via the square formula;
  - the transfer composite v↦(v,v), which is independent of ε;
  - Q(√−35) has h=2 and 2 inert (−35≡5 mod 8);
  - Dedekind by finite splitting; Br(T)[2]=0 because local degrees are even and by Brauer–Hasse–Noether;
  - cd₂K=1 via a pro-2 Sylow subgroup; the upper bound from SGA 4 X 4.4.

  Literature: Popescu 2022 §5 (the eventual-inertness tower) is credited. The run found no persistent-Pic/2 example in
  print; that is a bounded negative search, not proof of novelty. The run also has a statement-only re-proof by the
  same model (via Q(i)) and reran the certificate (111,784 assertions) plus a new 37,889-check program.
- **Theorem 1.2 (wild, H³(U,𝔽₂)≠0 for U=Spec W(k̄)[[t]][1/t]): targeted proof check, confirmed at reading level.**
  Checked:
  - excision H³_z(U)=H²(L), since H²(D)=H²(E)=0;
  - Kato's gr⁰=E^×/E^{×2} and gr¹=Ω¹_E (with e′=2);
  - the shape a+{t,u} of the image;
  - the t-valuation parity argument;
  - c={1+2/t,t} has gr¹ image t⁻²dt, which lies outside B·dt+k·dlog t.

  The Suzuki 2024 locators (Props 6.1.2, 8.1.4, 8.2.1, 8.2.3) were not opened by me; the run opened them.
- **Theorem 1.3 (L6c and Pic^τ birational invariance): known.** It is Ishii–Yoshida arXiv:2410.15282v3 Cor. 1.4,
  p. 3, and Li–Wang 2026 Cor. 4.6, p. 7. The paper cites both and does not claim novelty. The purity gate is closed by
  Marrama 2026 Thm 6, p. 433 (Moret-Bailly). I did not re-check these.
- **Theorem 1.4 (boundary with a quasi-projective neighbourhood): targeted proof check, confirmed at reading level.**
  Checked:
  - the Bertini curve section avoiding T, with Abhyankar's tame Kummer charts;
  - Martinelli–Naranjo–Pirola connectedness;
  - Raynaud's Chow-lemma blow-up with its centre outside N, so that the boundary divisors are unchanged and
    Q(X′,Y′)↠Q(X,Y);
  - the non-normal descent.

  The MNP and Raynaud locators were not opened by me.

### Paper 2. Picard schemes, very ample surfaces and metabelian local groups (49 pp, still growing)

- **Theorem 1.1 (G1, universal polarization class iff at most one dᵢ odd): targeted proof check, confirmed.**
  - The rank-2 formula (q=0 on the radical, 1 off it) satisfies q(x+y)=q(x)+q(y)+b(x,y) in all four cases, because
    e^λ is alternating.
  - Necessity: T_v(x)=x+E(x,v)v preserves E, and b=E mod 2 on Λ/2Λ. Invariance forces q(v)=1 on W∖0. Two orthogonal
    independent vectors then contradict this.

  Literature: the positive half is Poonen–Rains Prop. 3.12(f) (p. 1314, with its proof on p. 1315), now credited;
  principal type over ℂ also follows from Fringuelli–Pirisi Thm C. What is ours is the synthesis plus the elementary
  transvection converse. The run makes no priority claim.
- **Theorem 1.6 (A3, a very ample L on a smooth surface in characteristic 2 with h¹(L⁻¹)=1): targeted proof check,
  confirmed.** I recomputed every invariant:
  - g(C)=7, from Artin–Schreier conductor 15;
  - div t=7P₀+∞−8P₁;
  - C″ is smooth at ∞ (valuation 13−12=1);
  - M=O_P(−1)⊗N²;
  - f_*Q=N⊕N³, with h⁰=2+4=6 (Weierstrass semigroup ⟨2,15⟩);
  - for Q⁻¹ the R¹ summands are N⁻² and O, so h¹=1; for n≥2 all quotient degrees are at most 1−n<0;
  - h¹(O_S)=7+2=9;
  - h⁰ of B, BM, BM² is 210, 186, 160, total 556;
  - after the 556 ninth roots: h⁰(L)=6+556=562, h¹(L⁻¹)=1, h¹(O_Y)=9+556=565;
  - very ampleness via the charts S_u with z_i=t_i/u, which are closed immersions.

  The relative-duality display that was wrong earlier (Sym^r E^∨ in place of (Sym^r E)^∨) is fixed in the current
  text. Literature:
  - Lauritzen–Rao (pp. 1–2, read by me) answer Raynaud's very-ample question only in dimension at least 6, credit
    Lauritzen's homogeneous spaces, and explicitly ask for examples of smaller dimension;
  - neither the run nor my web search found a surface example;
  - the root-of-a-basis step is credited to Bhatt 2012 Prop. 7.2 (for global generation).

  Status: no prior surface example located; novelty is not proved.
- **Theorems 1.2–1.5, 1.7–1.9, Props 6.1 and 9.x, Cor. 6.2** (E4 pushout and full Picard, the surface-torsor
  modification, the normal-base projective bundle, smooth torsors, the A2 Picard-kernel constraints, K3,
  tame coefficients, abelian inertia, metabelian): **not read in full; statements read.** By the run's own records:
  - the normal-base projective-bundle theorem still lacks its statement-only re-proof;
  - the A2 equality-case reduction (Ekedahl I.2.4(ii)) is the newest movement, with its reciprocal record still
    pending;
  - the K3 refinements, the Ekedahl a=1 branch, a>1, the strict inequality and the general Picard-point question are
    open. The paper states them as open in "Further questions".

### Paper 3. Grothendieck's locally quasi-finite representability criterion and Murre's announced analogue (19 pp)

- **Theorem 1.2 (the henselian counterexample P): targeted proof check, confirmed for every axiom check and for
  non-representability.**
  - R^h=0 when t is a unit, so P is terminal on D(t).
  - Axioms 4–6 hold.
  - Lemma no-model: the Artin–Schreier root f^p−f=tu is not in R₀, and ε·f is an extra section.
  - Condition 7 holds: F_p[t]_(g) is not complete, which forces s to be generic.
  - (7_rel) and 8 hold.
  - Non-representability: on F_p[t,ε]/(ε^p) the sections 0 and ε agree on the schematically dense D(t).

  The arbitrary-fpqc descent proof was read. It rests on Prop. integral-descent (lines 135–178, **not read**) and on
  de Jong–Olander Thm 2.
- **Theorem 1.3 (H: the fixed-base openness counterexample) and Theorem 1.4 (relative openness): statements read.**
  This is the run's own refutation of our earlier SA17 theorem; see §3. I did read the run's root reconstruction of
  H's axioms. Its key step: on a local ring with t in the maximal ideal, 1−ta is a unit, so H=0; at the generic point
  H=α_p. Hence M(S,0)={(t)}. That step is sound.
- **Theorem 1.5 (the criterion under (7_pro)), Theorem 1.6 (finite semilocal descent, cote 128): not read; statements
  read.** By the records, each has a fresh statement-only re-proof and a root comparison that passed.

### Paper 4. Cohen lifting for Grothendieck's adic algebras and Deligne's algebraic extensions (10 pp)

- **Theorem 1.1 (EGA 0_IV 19.3.12, withdrawn in Err_IV 8, p. 347, restored): targeted proof check, confirmed.**
  - Linear compactness over C: the derivation and compatibility equations are affine and C-linear.
  - Continuity comes from V² being open.
  - The closed-powers tower J_n gives C≅lim C/J_n.
- **Theorem 1.2 (A16, nonlocal noetherian adic Cohen lifting): targeted proof check of the algebra assertions,
  confirmed at reading level.**
  - P_n is projective, by lifting through B_n⋉N.
  - The derived fibres are computed by completion, Popescu's theorem and Neeman Lemma 2.12.
  - Ext^{>0}(L,N)=0 via R lim (Mittag-Leffler).
  - The Ext² obstruction is killed; Tor₁ gives flatness; completeness; Exalcomm gives the splitting.

  The module-condition lemmas were not read. Literature: Pérez Rodríguez 2008/2016 needs pseudo-finite type, which is
  not needed here.
- **Theorem 1.3 (Deligne's question, transfinite triangular presentations): statement read.** The finite case is
  Stacks 07BV.
- The three EGA "corrections" that prompt 90 listed (III 4.3.6; IV 20.1.3 ×2) are **known**: EGA III/2 errata, and
  Kleiman 1979, pp. 203–204. The paper cites them as known. This is correct.

### Paper 5. Grothendieck's Albanese equivalence and his conjectures on algebraic cycles (13 pp)

- **Theorem 1.1 (E.3e, 14:37–38 Theorem 3.1 in characteristic p, integral premise): targeted proof check, confirmed.**
  - All finite witnesses are spread out.
  - On an 𝔽̄_p fibre, CH₀⁰ is torsion.
  - β_j is a prime-to-ℓ isogeny, from the integral H¹ isomorphism.
  - Bloch 4.2 kills the ℓ-part, so z_s=0.
  - Bloch 3.8 specialization.
  - Zero on Q_ℓ/Z_ℓ, hence zero rationally, hence zero integrally, since H¹(A,Z_ℓ) is torsion-free.
  - Sharpness: E: y²=x³−x over 𝔽̄₅, where u_Z is the identity on the torsion group E(k).
- **Theorem 1.2 (universal range modulo algebraic equivalence), Theorem 1.3 (gcd bounds for s_J(A)): statements
  read.**
- Points to settle before any publication:
  - the citations [OpenAICM], [OpenAIRationality] and [EngelSix] should have their locators verified (I could not
    confirm them);
  - E.3q's literature scope is corrected (dossier).

### Paper 6 (the gerbe of 𝔽_p): withdrawn as a research paper

All its conclusions are known from Milne, *Gerbes and Abelian Motives*, Props 3.5(b), 3.10 and 4.3, and Thm 6.3. A
comparison note is kept in the records. I agree with that disposition.

### Applies to every paper

- **Box 8:** no paper has a section headed "Proof overview" (HOW.md box 8 since 22 Nov). The mechanism prose sits in
  Section 1 instead.
- The run's CHECK_EVENTS.tsv has 6 rows whose types fall outside the rubric ("two full reading passes; targeted
  checks", "targeted reciprocal comparison …", "current-run finite certificate …"). A finishing prompt should map them
  onto the rubric.

## 2. Corrections to published work

| Item | My check | Already known? | Report? |
|---|---|---|---|
| EGA III 4.3.6 (K′=K⊗Â) | witness y−Σx^{n!} rederived: correct | yes, EGA III/2 errata, Liste 2 A | no |
| EGA IV 20.1.3 (two) | follows Kleiman's examples | yes, Kleiman 1979, pp. 203–204 | no |
| EGA 0_IV 19.3.12 | deleted in Err_IV 8; restored by Paper 4 Thm 1.1 | not an error of statement | no |
| Esnault–Kindler 2016 Thm 6.1 | — | yes, the authors' erratum of 29 Sep 2016 | no |
| Stacks 07BV (x_r → x_d, twice) | **confirmed on the live page** today | no comment on the page | **yes** (draft 1) |
| Stacks 0BTP (cites 02W8, which is fppf-only, for an fpqc step) | **confirmed live**: 0BTP cites 37.57.1, and 02W8 assumes an fppf covering; the repair (0AP9 + 0APK) was not opened by me | not seen | **yes** (draft 1) |
| Popescu 2022 §4, claims (a), (c) on p. 510 | **confirmed from the PDF**: the counterexample Z_(3), L=Q(√q_i), q_i≡1 (3), F={V} makes A Dedekind but A* not, with S_q finite and S*_q infinite; Thm 2 stands (via Thm 1) | none found (bounded search) | **yes** (draft 2) |
| Liedtke arXiv:0912.4291v4 p. 27 (abelian surface: χ(O)=1, b₂=2 printed) | true values 0 and 6, by Künneth; table not opened by me | unknown | **yes, conditional on a look at the table** (draft 3) |
| Cossec–Dolgachev–Liedtke, *Enriques Surfaces I* (19 Apr 2024 version), p. 366 | Leray + Riemann–Roch recomputed: deg L=−χ(O_X)−h⁰(T); E×P¹ shows the printed lines fail | unknown | yes (draft 3) |
| Cotner–Zavyalov, Compositio, Ex. 3.4.6(ii), fn. 6 | **confirmed**; my first worry (is F nilpotent?) is settled by ampleness: F^m x lies in the image of H¹(O(−p^mD))=0 | no | yes, as a remark (draft 4) |
| Milne, *Abelian Varieties* Rem. 8.5 (2022 and 1986) | **confirmed**: y²+y=x³ over 𝔽̄₂ has dim Lie E[2]=1, whereas a product of μ₂/α₂ factors would have 2 | not in the errata lists searched | **yes** (draft 5) |
| Milne, *Gerbes and Abelian Motives* p. 23 (integrality missing; W(p^{nn′}) should be W(p^{n′})) | **confirmed**: u=(3+4i)/5 has weight 0, is a 2-unit, u+u⁻¹=6/5, so u is not a root of unity | the repair is in Milne's Seattle notes, Def. 2.5(b) | yes, as a small note (draft 5) |
| Ekedahl 1988, p. 112 (two inverse signs) | the repair follows the run's (1.9) argument; I did not check the source | no erratum found | **no: the author died in 2011.** Keep it in the dossier. |
| Voisin, book manuscript, p. 41 (CH²/alg should be CH²_hom/alg) | trivial slip; the published 2014 book was not checked | unknown | no, unless the published book has the same slip |
| Achter–Casalaina-Martin, "Putting the P back in Prym", §1.7.2, p. 13 | **confirmed**: C: y²+x⁴+z⁴=0 in P_ℝ(1,1,2) has genus 1 and no real point, while every Pic^d_E has the real point O(d·0) | no | **yes** (draft 6) |
| Chai, "Mumford's example of non-flat Pic^τ", Thm 2.4(iii); Chai–Oort 2017 §3.9(iv), p. 35; Partsch 2013 Prop. 6.6, Thm 6.7, Prop. 6.9 | **targeted check, no gap found at reading level** (see below) | the first-order incompatibility is in FGA VI Rem. 3.4 (credited) | **yes, after one more check** (drafts 7, 8) |

**The Igusa correction.** This is the strongest claim in the dossier. It says that **every** Artinian deformation of the
ordinary Igusa surface has flat Pic^τ, contrary to the published claims.

The proof (FULL_CHECK.md §2), as I read it:
- the étale double cover lifts, and the lifted A is abelian (GIT 6.15);
- in Katz's Serre–Tate coordinates the involution equation forces q₂₁=1;
- G=ker(1−σ^∨) is then an E^∨[2]-torsor over F^∨, and Pic^τ→G is a μ₂-torsor, so Pic^τ is finite flat over F^∨.

I found no gap. The step that carries the weight is Katz's pushout recovery [2]c₀=(q₂₁,q₂₂) and its row convention.
The non-lifting of the Albanese fibration checks: q_B(x,0)=1, while q_A(e_E,e_F^∨)=1+ε; σ lifts because (1+ε)²=1 in
characteristic 2.

The run records no statement-only re-proof of the flatness. Chai's note was read only through an indexed text: the
author PDFs returned 403. Before any e-mail, Chai's own text should be read directly and one independent re-proof made.
Drafts 7 and 8 carry that condition.

## 3. Corrections to our own work (no edits made)

1. **SA17, `RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped\RESEARCH_SA17\sections\A_finish_L1_general.tex`, line 248,
   Theorem A:L1-general (`\status{Proved}`): false.** Its fixed-base generization lemma (SA17:A:actual-pro-generization)
   is false too. The counterexample is H(R)={x : x^p=0, x∈(tx)} over 𝔽_p[t], where M(S,0)={(t)}.

   Edit: set the status to "Refuted". Add "superseded by ROOT:L1-relative-openness (Paper 3, Thm 1.4): premise and
   conclusion of condition 7 for F_A on A-schemes; counterexample ROOT:L1-fixed-base-counterexample (Paper 3,
   Thm 1.3)". Do the same in `sections/A_finish_L1.tex` and `sections/unresolved.tex` where they cite it. Our intake of
   SA17 (`ours/intakes_sweep3/…`) confirmed this theorem; that intake's verdict should be marked as withdrawn.
2. **SA12 locator, `RESEARCH_SA12_final_INCOMPLETE_20261120T2310Z_unzipped\parts\A\paper_A.tex`, lines 33 and 94:
   "31/085".** That is the PDF page. The archive sheet is **84**; sheet 85 is a reversed, unrelated draft.

   Edit: "cote 31, sheet 84 (PDF p. 85)". Prompt 90's own title ("cote 31, sheet 85") and any registry or Hexagon
   entry that uses 31/85 need the same fix.
3. **SA06 locator "14:38", in `sections/E3_albanese.tex:170`, `agents/cycles/effectivity_albanese.tex:320,486` and
   `agents/cycles/morphic_counterexample.tex:108`.** These merge two items. Theorem 3.1 is on cote 14, sheets 37–38.
   The letter to Serre of 27 Aug 1965 is on sheets 43–45 (Conjecture A on 43, B on 44).

   Edit: "14:37–38" for Theorem 3.1 and "14:43–45" for the letter's conjectures. Check which item the morphic
   counterexample's "14:38–39" means before changing it.
4. **E4 locator: "cote 57, sheet 315" is PDF page 315, archive sheet 314.** The run keeps the internal ids
   E4-315schemeNormal/Integral for continuity. Any prose citation in SA14_SA19 or in our notes should read "57:314".
5. **Novelty claims to withdraw in our records:**
   - L6c is known (Ishii–Yoshida Cor. 1.4);
   - the Pic^τ birational invariance is a consequence of Li–Wang Cor. 4.6;
   - the three EGA corrections of SA23 (D-11, D-12, D-13) are already published (EGA III/2 errata; Kleiman 1979);
   - the gerbe results of SA05 are Milne's;
   - the positive half of G1 is Poonen–Rains 3.12(f).

   Every registry, Hexagon-candidate and plan entry that lists these as new results of ours should say "known; cited".
6. **SA14_SA19 A3 working text:** the general relative-duality formula with Sym^r(E^∨) is wrong; the correct form is
   (Sym^r E)^∨. The run says `A3_very_ample.tex` and `sections/A.tex` already have the correct form. Only the
   pre-05:27 Paper 2 draft had the error, so nothing in our earlier files needs to change.

## 4. What is new, against the literature (main theorems)

- **Plausibly new** (bounded searches found no prior):
  - the A2 persistent-Pic/2 arithmetic counterexample (Paper 1, Thm 1.1);
  - the wild H³ example (Paper 1, Thm 1.2);
  - the A3 very ample surface (Paper 2, Thm 1.6);
  - the henselian counterexample to the locally quasi-finite criterion, and the pro-modular criterion over every
    locally noetherian base (Paper 3);
  - the nonlocal adic Cohen lifting (Paper 4, Thm 1.2), as against Pérez Rodríguez's pseudo-finite-type results;
  - E.3e (Paper 5, Thm 1.1);
  - the Paper 2 E4/torsor theorems. For these, the Achter–Casalaina-Martin §1.7.2 first paragraph is a located
    precedent for the Picard conclusion over a connected noetherian base.
- **Known, cited correctly:**
  - L6c and Pic^τ invariance (Paper 1, Thm 1.3);
  - the G1 positive half;
  - EGA III 4.3.6 and IV 20.1.3;
  - the Paper 6 gerbe statements;
  - E.3u (Walker) and E.3q (Bloch–Srinivas scope);
  - the finite case of Paper 4 Thm 1.3 (Stacks 07BV).
- **Restored, not new:** EGA 0_IV 19.3.12 is a withdrawn assertion of Grothendieck's, now with a proof.

## 5. Hexagon readiness (the five tests, and HOW.md's boxes)

A shared gate for every paper: HOW.md box 8 ("Proof overview" section) is missing.

| Candidate | Complete | Self-contained | Stable | Checked | Interest now | Gate left |
|---|---|---|---|---|---|---|
| **A3: a very ample counterexample to Kodaira vanishing on a surface (char 2)**, answering Raynaud's 1978 Rem. 3, p. 278, in the smallest dimension | yes | yes (Stacks, Bertini, Riemann–Roch; Bhatt credited) | yes (unchanged since its fix at 05:27) | yes (this intake + the run's same-model re-proof + two computations) | **high**: an open question of Raynaud's, and Lauritzen–Rao asked for lower dimension | a short standalone note (it is buried in a 49-page omnibus); one more literature pass (Raynaud's original text, which the run could not open; recent char-p surface papers); box 8 |
| **A2: persistent Pic/2 counterexample to Grothendieck's cd conjecture (cote 31, sheet 84)** | yes | yes | yes | yes (this intake + the run's re-proof + certificates) | moderate to high (cd of affine schemes; the archive) | literature (Hasse 1925 and Schilling 1950 leads); box 8; the locator fix of §3.2 |
| Ordinary Igusa surface: Pic^τ flat (correction to Chai, Chai–Oort, Partsch) | yes | yes (Katz, GIT) | yes | **no**: targeted check only, no independent re-proof | high, for experts | an independent re-proof; Chai's text read directly; the authors written to first (Numdam model) |
| Henselian counterexample to the locally quasi-finite criterion (Paper 3) | yes | yes | yes since review 03 | partly (Prop. integral-descent not read by me) | moderate | my read of Prop. integral-descent; box 8 |
| E.3e, integral Albanese equivalence in char p (Paper 5) | yes | yes (Bloch 1979) | yes | yes | moderate | box 8; citation verification ([OpenAICM], [EngelSix]) |
| Nonlocal adic Cohen lifting + 19.3.12 restored (Paper 4) | yes (the parts I read) | yes | yes | yes for Thm 1.1, and for Thm 1.2's algebra part | moderate | the module-condition lemmas read; box 8 |
| G1 | yes | yes | yes | yes | low (the positive half is known) | none worth a post on its own |

**Flag for the main session.** A3 passes tests 1–4, and test 5 is strong. It is one gate away: a standalone short note
and one more literature pass.

## 6. What a finishing or successor prompt needs

1. **Box 8:** a section headed "Proof overview" in every paper.
2. **Paper 2 is an omnibus** (49 pp, nine themes). Split it:
   - (a) G1 with E4, schematicity and Picard;
   - (b) A3 alone, as a short paper;
   - (c) the A2 Picard-kernel constraints, which are still open research;
   - (d) the local groups (tame coefficients, abelian inertia, metabelian).
3. **Close the gates the run lists:**
   - the statement-only re-proof of the normal-base projective-bundle theorem;
   - the reciprocal record of the Ekedahl a=1 reduction;
   - the K3 reciprocal record.
4. **Map the six off-rubric check-event types** onto the rubric.
5. **The Igusa correction:** an independent statement-only re-proof of ordinary flatness. Also a decision whether to
   write it up: as a note, or kept to the dossier and sent to the authors.
6. **Verify the bibliography entries** [OpenAICM], [OpenAIRationality], [EngelSix] (Paper 5) and [AjitLee],
   [FeldPurity], [FeldCohen], [HexagonPicard] (Papers 1–4): exact existence and locators.
7. **Open questions to keep exact in the final papers:**
   - A2 Picard-point (the a>1 and strict-inequality cases, the two Ekedahl branches);
   - E4 over non-normal bases;
   - F13 (the wild-coefficient bound);
   - B.1 in characteristic p beyond the finite-flat purity input.
8. **Do not carry these over as new:** L6c, the gerbe note, the three EGA corrections, the G1 positive half.

## Status addendum, 23 Nov 2026 ~19:30 UTC (Claude Opus 5.5 at effort high, a018e2d2)

- A3 was written up as P90a and posted as hexagon:2611.00936 (WB-0003). Kweon's Question 7.7 (arXiv:2008.01908v2,
  p. 19) raises its usefulness: see `INTAKE_POLISH_ALGEBRAIC_GEOMETRY_20261123_cp20.md` §1.4 and `p90a_note_v2`.
- The edits of §3 above lie inside returns, so they remain **unapplied, for the main session**. They are listed in
  `INTEGRATION_POLISH_ALGEBRAIC_GEOMETRY_20261123.tsv`.
- Papers 1, 3, 4 and 5 are unchanged at checkpoint 20, so their verdicts here stand.
