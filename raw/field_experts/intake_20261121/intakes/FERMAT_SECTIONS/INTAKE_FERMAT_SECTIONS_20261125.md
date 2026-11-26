# Intake of FERMAT_SECTIONS, checkpoint 13 (prompt 100)

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 25 Nov 2026, for the main session 329fb1e6, under the brief
`agent_notes/INTAKE_NEW_RETURNS_BRIEF_20261125.md`.
- **The checkpoint:**
  `grothendieck_archive_transcription_20261110/research_returns/FERMAT_SECTIONS_checkpoint_13_20261125T1152Z_unzipped/`.
  The run is GPT-6 Astra Pro (ChatGPT Pro mode).
- **Check events:** `INTAKE_FERMAT_SECTIONS_20261125_CHECK_EVENTS.tsv`.

**Before this intake.**
- `who_checked.py --source FERMAT_SECTIONS` gives 27 ids, every check by the run's own workers.
- The run's mathematics was checked before it ran: my attack-read of LM8_PUSH D.23 (`CONFERENCE/ATTACK_D23.md`, 25 Nov,
  19 events), which prompt 100 was built on. I also wrote prompt 100's follow-up message.

**The checkpoint.** Two papers:
- `workbench/papers/fermat/`, the Selmer theorem;
- `workbench/papers/quotients/`, smaller quotients.

**What I read.** CHECKPOINT.md (question table) and the crosswalk. The Fermat paper's statements, and in full its new or
changed proofs, listed in §1. The quotients paper's abstract only.

## 1. Verdicts

| Statement (run's id) | Claim | Verdict |
|---|---|---|
| FS.001, Thm 1 (`thm:fermat`) | For every odd n ≥ 3, every Selmer section of U_n/Q is cuspidal. The Selmer sections are three disjoint cusp packets, each a torsor under H¹(Q, Ẑ(1)). No local section conjecture is an input | **Holds.** The proof is D.23 with both repairs of the attack-read made. I reread the changed steps (below). The rest is as checked in ATTACK_D23 |
| FS.002/FS.010, Cor. (`cor:all`) with Prop. `prop:local-affine` | Under OpenAI's local theorem (Hypothesis 1, their Thm 1.1, version of 6 Oct 2026, unrefereed), every section is Selmer, hence cuspidal | **Holds as a conditional statement.** Prop. local-affine is the step the follow-up flagged (OpenAI's theorem is for proper curves only). The run proves it correctly: genus ≥ 2 neighbourhoods are cofinal (Riemann-Hurwitz); the proper theorem gives a unique point at each level; injectivity makes the points compatible; the limit puts s(G_k) in a decomposition group. D.56's original file is missing from the archive, and the run rebuilt the deduction independently |
| FS.003, Thm (`thm:other`), modular-curve part | If X₁(N) has positive genus, every Selmer section of Y₁(N)/Q is cuspidal at a rational cusp (strengthens LM6 B.15) | **Holds.** Stoll, Cor 8.8 for X₁(N), the finite-support lemma, and Mazur's Theorem (7), p. 35. I checked Theorem (7) at the Numdam source: "genus of X₁(m) > 0 (m = 11 or m ≥ 13) … the only rational points … are the rational cusps" |
| FS.004, even exponents | For even n, U_n has no section at all (F_n(R) = ∅; real section theorem on a high-genus neighbourhood; covers n = 2) | **Holds.** The real section theorem is cited as "[real], unnumbered Theorem, p. 2"; I did not open it |
| FS.006/ERR.001, ERR.002, §"The two corrections to Steklov" | Prop. 4.6 needs the leading constant to be an e-th power, which fails (2⁻⁸). The split description in the proof of Prop. 5.10 is false, its conclusion true, so ℓ ≥ 11 stands once 5.10 is re-proved. ℓ = 7 is unproved as printed (Y₁(7)(Q) ≠ ∅; P = (0,0) of order 7 on y² − xy − 4y = x³ − 4x²) | **Holds.** It agrees with ATTACK_D23 §5 and the follow-up, word for word in substance |
| FQ.* (quotients paper) | See §2 | **Carried as background without fault found**: abstract and question table read, proofs not checked |

**Changed steps I reread in the Fermat paper.**
- **Prop. `prop:reducible`.** The modularity input now has the citations the attack-read asked for:
  - Khare-Wintenberger (I), Thm 9.1 (author version p. 18); (II) §§10.2-10.3; Kisin, Thm 0.1 and Cor 0.2;
  - Ribet 1990, Thm 1.1, p. 432; Edixhoven, Thm 4.5;
  - Diamond, Thm 6.4. The run did not retrieve Diamond's chapter.
  - The precise form used is Wiles 1995, **Theorem 2.14, pp. 503-504**. I have not opened Wiles at that place; it must be
    opened before posting.
  - The step S₂(Γ₁(2)) = 0 is right, and the twist patching now says the residual difference is an unramified character.
- **Remark `rem:infinity`.** The twist at the cusp over λ = ∞ depends on the section (−c₄/c₆ = t^ℓ/4). This is the
  attack-read's §3.2 point, now in the text.
- **Lemmas `lem:finite-support` and `cor:descent-map`.** These are the finite-support argument of D.23, which I re-proved
  in the attack-read. They are stated with W(A_k)^{f-ab}_• = W(k), as in Stoll's Corollary 8.8.

## 2. What is new

- **Against the pile** (INDEX A3: "Gates: a full read of D.23 and of n = 3, 5, 7; an e-mail to Steklov").
  - Both gates are passed: the attack-read and the e-mails of 24 Nov and 25 Nov 01:16 UTC.
  - The theorem now exists as a written paper with the repairs made. Every odd n ≥ 3 is covered, with the packet
    description of the Selmer sections, the conditional all-sections corollary, Y₁(N) and even n.
  - FERMAT_SUCCESSOR A.53 is now proved: rank zero and finite Sha for the quintic, by an interval certificate for the
    central L-value and Nekovář's Hilbert-modular theorem. A.52 was reconstructed whole.
- **Against Steklov** (arXiv:2602.17746v2).
  - His Theorem A stands for ℓ ≥ 11 once Prop. 5.10 is re-proved; the paper says so.
  - New here: ℓ = 3, 5 and 7; composite n (new when every prime factor is 3, 5 or 7); and the packet description.
- **Smaller quotients (quotients paper; run-only).** The prosolvable and finite-derived Selmer statements hold for every
  odd n divisible by 3, 5, 7, 11, 13 or 19. The inputs:
  - 3 and 7: modular quotients;
  - 5: Jac ~ Jac(v²+v=u⁵)³;
  - 11: a genus-five factor with an interval certificate;
  - 13: a Prym, with Mazur-Rubin and Loeffler-Zerbes;
  - 19: a CM sixfold, with McCallum-Tzermias and Zhang.

  Further:
  - The full pro-3 classification holds for n = 3^r, 5·3^r, 7·3^r.
  - The pro-17 classification holds at 17^r.
  - Noncuspidal pro-3 sections exist (via Hoshi's free source) and fail local geometry at 3, so they are not Selmer.
  - These are new against BKL's Theorem E, as the run distinguishes them. They rest on certificates and deep published
    theorems I have not checked.
- **For Grothendieck's questions.** The section-conjecture form of Fermat's theorem asked for in *La Longue Marche*
  §51.16 is proved for Selmer sections, unconditionally. For all sections it is proved under the unrefereed proper p-adic
  theorem. The run viewed cote 140-4, ff. 733-736v, for that passage.

## 3. Consequences for the waiting prompts

- **Q03_INTAKE_A_ANABELIAN_SECTIONS, l.184-190.** Now: "Two steps of its proof fail: Proposition 4.6, as used in
  Proposition 5.10, …; 'Y₁(ℓ) and Y(μ_ℓ) have no Q-points for ℓ ≥ 7' is false at ℓ = 7". It becomes statable as:
  - Prop. 4.6 is false as stated, and the splitting in the proof of 5.10 is false.
  - The conclusion of 5.10 holds, so Steklov's Theorem A stands for ℓ ≥ 11. ℓ = 7 is unproved as printed.
  - FERMAT_SECTIONS (checkpoint 13) proves the Selmer statement for every odd n ≥ 3, with the packets, and the
    all-sections statement under OpenAI's local theorem. The Selmer statement was checked by Claude Opus 5.5 at effort
    max (attack-read and this intake).
  - The prompt's request to compare SECTIONS_OVER_Q A.20 with D.22 stands.
- **Q06_30_SA31, l.173-179.** It cites Li-Lüdtke on S-Selmer sections and noncuspidal Selmer sections at potentially
  multiplicative places. The quotients paper adds a run-only statement that can be cited there: for every odd n ≥ 5, a
  hypothetical noncuspidal prosolvable Selmer section has open 2-adic and 3-adic Frey images with common rational
  Frobenius polynomials on a density-one set.

## 4. Candidates for Hexagon

1. **"Fermat's theorem for Selmer sections, after Steklov"** (the Fermat paper). This is the strongest candidate of the
   two runs: the argument has been attack-read and rechecked. Still needed:
   - open Wiles 1995, Thm 2.14 (pp. 503-504), or Diamond 1995, Thm 6.4, at the statement used;
   - open the real section theorem source at its theorem;
   - a reader of another model family;
   - the final build and page check.

   Under our errata policy, the corrections section is our own text. Its wording is factual ("defective steps"). It could
   be softened to "two steps that need another input", in the courteous form, before posting.
2. **The quotients paper.** Not yet. Its theorems at 5, 11, 13 and 19 rest on interval certificates and on deep
   published theorems (Nekovář, Loeffler-Zerbes, Mazur-Rubin, McCallum-Tzermias, Zhang). Each needs a check at the
   source and a rerun of its certificate.

## 5. Not checked here

- The quotients paper's proofs.
- The run's L-value interval certificates.
- Wiles 1995, Thm 2.14.
- The real section theorem source.
- OpenAI's proof: it is an explicit hypothesis, as it should be.
