# H15 note: records

Note: `h15_note.tex` / `h15_note.pdf` (8 pages; three pdflatex passes; 0 overfull boxes; all 8 pages rendered and read
by the editor). Editor: Claude Opus 5.5 at effort high (agent ad85573792c61a914), 23 Nov 2026.

**Title:** "Galois orbits of CM points in A_g with an explicit exponent, after Tsimerman and Gaudron–Rémond".

**Kind:** needs a pass, now done. Jaswal, Cureton-Thorner, Liu and Banks posted in the last weeks, and all four are
integrated in §2.

## 1. Literature, with locators

**Opened at the source** means I opened the text at that place. **Abstract** means I read only the abstract page.
**Gate** means the main session read it at the source today (`GATE_JASWAL_GR23_20261123.md`). **Run** means the
producing model's locator, with the source not opened by us.

| Work | Locator used | How it bears | Read |
|---|---|---|---|
| Gaudron-Rémond, *Nouveaux théorèmes d'isogénie*, Mém. SMF 176 (2023); preprint https://lmbp.uca.fr/~gaudron/art20.pdf (SHA-256 4ac73d953938fb6ceb5b2359fdfa7de85456d15b9a03d26e4237faede14b05d8) | Notations 1.1-1.2 and "2 ≤ d ≤ Υ^{2n}" (pp. 10-11); Thm 1.5(2) (p. 13); Thm 1.8 and Thm 1.9(5) (p. 15, rendered); Prop. 13.7 (p. 89) | carries the exponent. Thm 1.9(5) alone gives exponent 1/(4g²), Thm 1.8 gives 1/(2g); no orbit bound stated | **opened at the source** (editor; Prop. 13.7 and Thm 1.5(2) also by the gate) |
| Tsimerman, *The André-Oort conjecture for A_g*, Ann. Math. 187 (2018); arXiv:1506.01466v5 (SHA-256 ccc5f8be…3ee9c) | Thm 1.1 (p. 1); §3 (Brauer-Siegel, ineffective); Thm 4.1 and proof (pp. 5-6: any exponent < 1/(4c_g), c_g Masser-Wüstholz); Thm 5.1 (orbit bound, b_g unspecified); Thm 5.2 (AO) | the theorem made explicit here | **opened at the source** (arXiv v5; the Annals page numbers were not seen) |
| Jaswal, hexagon:2611.00339v3 | Prop. 3.3: \|Im ρ_L\| ≥ c(δ) d_L^{δ'}, δ' = 1/(16 t s n_T(n_T−1)); Thms 1.1-1.4: effective AO | neighbour: all Shimura varieties; Galois-closure discriminant; cited, not claimed | gate |
| Cureton-Thorner, hexagon:2610.00200v2, Thm 1.1 | Re s > 31/32 zero-free for every Dedekind zeta | alternative input; makes Jaswal unconditional | listing and run; theorem as quoted by the run and the gate |
| Banks, arXiv:2610.15483 (Oct 2026), "On the OpenAI proof that Landau-Siegel zeros do not exist" | abstract: (1−β) log q ≥ 3.0·10⁻³ for primitive real χ, q ≥ 3 (with Lu-Zaman-Zhao) | alternative input (Remark 7: a_r with max{16 r!, 1/δ}) | abstract |
| Banks, arXiv:2610.31402, "Landau-Siegel zeros over a base field and effective Brauer-Siegel" | abstract: effective Brauer-Siegel for Galois K/k | adjacent; no CM-orbit application stated; **not cited in the note** (could be added) | abstract |
| Liu, hexagon:2611.00080v2 | abstract: (1−β){log D_K + n log 2n + 6n + 1} ≥ 1/1370 for every real zero of ζ_K | alternative input | abstract |
| Tsimerman, JAMS 25 (2012); arXiv:1103.5619 | abstract: orbit bounds for Weyl CM points, unconditional for g ≤ 5, under GRH for CM fields in general | earlier result, not explicit | abstract |
| Binyamini-Schmidt-Yafaev, arXiv:2104.05842, Math. Ann. 2023 | abstract: new proof of Tsimerman's bound for abelian type by point counting; general case conditional on height bounds | earlier result, not explicit | abstract (search summary) |
| Pila-Shankar-Tsimerman (Esnault-Groechenig appendix), arXiv:2109.08788 | abstract: André-Oort in full generality | context | abstract |
| Ullmo-Yafaev, Bull. SMF 143 (2015), Thm 6.1 | orbit bound under GRH | source of Jaswal's Prop. 3.3 | run and gate |
| Yuan-Zhang, Ann. Math. 187 (2018), Thm 1.1; AGHMP, Ann. Math. 187 (2018) | averaged Colmez | carries the height | run |
| Wei, JNT 242 (2023); arXiv:2111.00617v1, Prop. 5.3, pp. 19-20 | explicit height estimate (75/2) | its zero sum is written out in Lemma 3 | run |
| Stark, Invent. Math. 23 (1974), Lemmas 3, 4, 9 | exceptional-zero square; descent to quadratic subfields | used | run |
| Gaudron-Rémond, CMH 89 (2014), §2.3 and Cor. 8.4 | height normalization; h_W ≥ −(r/2) log 2π | used | run |
| Rémond, Rev. Mat. Iberoam. 33 (2017), Thm 1.2 | maximal-order varieties split | used | run |
| Raynaud, Astérisque 183 (1990) | isogeny height estimate | used | **from memory**: pages and statement not checked |
| Faltings 1983 | Tate, semisimplicity | used | standard |
| Binyamini, Crelle 767 (2020); Log-Noetherian, arXiv:2405.16963 §10 | effective AO for Y(1)^n; open analytic data | context | run |

**Hexagon search, 23 Nov.** I read the listings for 2610 and 2611 (all four pages, through 2611.00829). The relevant
entries are:
- 2610.00200 (Cureton-Thorner);
- 2611.00080 (Liu);
- 2611.00339 (Jaswal);
- 2611.00200 (Reilly, a formalization of the OpenAI Landau-Siegel interpolation lemma; not cited).

No Hexagon post states an explicit-exponent Galois-orbit bound for CM points of A_g.

**Web searches (general terms only):**
- "explicit exponent lower bound Galois orbits CM points A_g effective": no such result found.
- "OpenAI Landau-Siegel zeros 2026": found Banks 2610.15483 and 2610.31402, Kerr 2610.21099, arXiv:2610.30476.

## 2. Checks, by model and effort

| Statement (note) | Check | Who |
|---|---|---|
| Thm 1 (orbit bound) | statement-only re-proofs by separate workers ("independent analytic and geometric re-proofs; targeted integral audit") | GPT-6 Astra (ChatGPT Pro mode), the producing run |
| Thm 1, Lemmas 3, 5, 6, Prop. 4 | targeted proof check, every step; published inputs carried | Claude Opus 5.5 at effort high (ad855737), 23 Nov (intake check events) |
| Thm 1, GR23 inputs | targeted proof check: the three GR23 statements read at the source and their use rechecked (C_g ≥ 241(en)^{2n}n^5, exponent 2n ≤ 2g) | Claude Opus 5.5 at effort high (editor), 23 Nov |
| Table, Cor. 2 | computation: constants for g = 1..6 reproduced to every printed digit; cutoff ≈ 10^78.1 < 10^80 | Claude Opus 5.5 at effort high, 23 Nov (`partA_check.py` in the intake folder) |
| Remark 7 (other inputs) | new in this note; targeted proof check by the editor; replaces only the exceptional-zero step of Prop. 4 | Claude Opus 5.5 at effort high, 23 Nov |
| Comparison with Jaswal and GR23 | targeted check of the literature | Claude Opus 5.5 at effort max (main session), 23 Nov, gate |
| Elliptic examples (163, 427; class numbers 1 and 2) | computation (reduced forms) | Claude Opus 5.5 at effort high, 23 Nov |

**Faults and repairs.** No change to a statement or proof.
- **Citation:** the run gave the orbit bound as Tsimerman "Thm 5.2". In arXiv v5 it is Thm 5.1, and Thm 5.2 is
  André-Oort. Repaired in the note; recorded as a source-scope correction.
- **Framing:** effectivity is not the contribution. Repaired in §2 and Remark 7.

**Not done:** no independent re-proof by another model family; no human check.

## 3. Whom to write to when it is posted

1. **Éric Gaudron and Gaël Rémond.** Their Theorems 1.5(2) and 1.8 carry the exponent. Tell them how their theorem is
   used, and that their Thm 1.9(5) already yields an explicit exponent 1/(4g²).
2. **Jacob Tsimerman:** the theorem made explicit.
3. **Manvir Jaswal:** his Prop. 3.3 stated beside ours, and his effective AO credited.
4. **Xinyue Wei:** her Prop. 5.3 constant is used and written out.
5. **Levent Alpöge:** his theorem is the input at one place.
6. **Optionally William Banks, and Dean Cureton and Jesse Thorner:** their zero-exclusion results are named as
   alternative inputs.

The authorship line is left for deposit.

## 4. Before posting

- The user's word.
- Optionally:
  - open Wei's Prop. 5.3 and GR14 Cor. 8.4 at the source (run's locators so far);
  - check the Raynaud locator (from memory);
  - fix the workbench URL, set to the general records repository for now.
