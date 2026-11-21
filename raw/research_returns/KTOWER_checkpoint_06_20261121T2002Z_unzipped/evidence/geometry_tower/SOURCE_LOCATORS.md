# Geometry and tower source locators

Run: **KTOWER**. Reviewer: `/root/geometry_tower`, **GPT-6 Astra Pro**, reasoning effort **not exposed**. Retrieval and review date: **2026-11-21 UTC**. `CHECK_EVENTS.tsv` records the actual scope of each check. A source statement being checked does not mean every cited foundational theorem was independently re-proved.

## Published and author-hosted sources

| Source | Exact locator used | URL / local location | Check scope |
|---|---|---|---|
| SGA 1, 2003 recomposition | Exp. IX, Th. 6.1, p. 195; Exp. X, Cor. 1.7 and proof, pp. 203–204; Exp. XIII, Prop. 4.6 and proof, pp. 310–311 | Supplied source copied to `SGA1_supplied_text.txt` | Fundamental arithmetic sequence; proper Künneth allows its other factor to be nonproper; prime-to-p Künneth for the affine construction. Full displayed proofs of X.1.7 and XIII.4.6 read. |
| H. Stichtenoth, *Algebraic Function Fields and Codes*, 2nd ed., GTM 254 (2009) | Prop. 3.7.8(c)–(d), p. 127 | [Full book scan](https://agorism.dev/book/math/alg/algebraic_function_fields_and_codes_henning-stichtenoth.pdf) | Artin–Schreier different and genus theorem statement directly inspected; the source is the original textbook, hosted by a third party. |
| J. Stix, *Rational Points and Arithmetic of Fundamental Groups*, LNM 2054 (2013) | Ch. 15, opening paragraph, p. 197 | [Publisher chapter](https://link.springer.com/chapter/10.1007/978-3-642-30674-7_15) | Publisher text explicitly confirms that extensions of the finite-field Galois group split. The elementary proof is supplied independently in `finite_field_sections.tex`. |
| A. Schmidt and J. Stix, *Anabelian geometry with étale homotopy types*, Annals 184 (2016), 817–868 | Definition 5.7, author manuscript p. 17 | [Author manuscript](https://www.math.uni-frankfurt.de/~stix/research/preprints/SCHMIDT-STIX-AnabGeomEtHoType20150405.pdf) | Definition checked. Its product-embedding requirement is retained; the paper's characteristic-zero reconstruction theorem is not imported into characteristic p. |
| S. Mochizuki, *The local pro-p anabelian geometry of curves*, Invent. Math. 138 (1999), 319–423 | Theorems A–B, author pp. 3–4; Th. 16.5 and following full-profinite comparison, p. 86; Th. 17.1 and proof, p. 87 | [Author manuscript](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf); supplied text copied to `Mochizuki1999_supplied_text.txt` | Statements, comparison and whole 17.1 proof read; entire 16.5 proof not independently reviewed. DOI: 10.1007/s002220050381. |
| P. Deligne, *Le groupe fondamental de la droite projective moins trois points*, in *Galois Groups over Q*, MSRI Publ. 16 (1989), 79–297 | §§15.19, 15.26, printed pp. 239, 242; PDF indices 160, 163 | [IAS-hosted original](https://publications.ias.edu/sites/default/files/61_LeGroupeFondamentalDroite.pdf) | Relative tangential specialization and formal-coordinate comparison paragraphs read directly. |
| H. Nakamura, *Galois rigidity of pure sphere braid groups and profinite calculus*, J. Math. Sci. Univ. Tokyo 1 (1994), 71–136 | §2.1, Th. 2.1.1, pp. 94–97; Lemmas 2.1.2, 2.1.4 | [Journal PDF](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf) | Entire displayed proof and its two lemmas read; foundational referenced inputs carried. |
| H. Nakamura, *Galois rigidity of the étale fundamental groups of punctured projective lines*, J. Reine Angew. Math. 411 (1990), 205–216 | §3 | Locator confirmed in Stix's paper below | Original 1990 proof not retrieved; no whole-proof check claimed. |
| J. Stix, *On cuspidal sections of algebraic fundamental groups*, author version 24 February 2012 | Prop. 16(2), Th. 17, p. 8; Cor. 19, p. 9; Cor. 32, p. 12; §5 attribution to Nakamura | [Author manuscript](https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf) | Statements and relevant hypotheses inspected; distinguishes cusp packets from actual Kummer images. |
| Y. Hoshi, S. Matsumoto and C. Nakayama, *Tangential morphisms via log arithmetic geometry*, RIMS-1995 (June 2026) | Props. 1–3 and Remark 1, text pp. 2–3 / PDF pp. 3–4 | [RIMS manuscript](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1995.pdf) | Tangential-functor statements and normal-cotangent-basis dependence checked. |
| M. Saïdi, *Good Sections of Arithmetic Fundamental Groups*, arXiv:1010.1313v1 | Ths. 2.6–2.7, pp. 33–39 | [arXiv PDF](https://arxiv.org/pdf/1010.1313) | Statements and slim/regular-field hypotheses checked; full proofs not reviewed. |
| M. Saïdi, *The cuspidalisation of sections of arithmetic fundamental groups*, Adv. Math. 230 (2012), 1931–1954 | Abstract; DOI 10.1016/j.aim.2012.04.002 | [Publisher](https://www.sciencedirect.com/science/article/pii/S0001870812001405) | Published abstract only; no transfer of preprint theorem numbering asserted. |
| M. Saïdi, *On complete families of curves with a given fundamental group in positive characteristic*, Manuscripta Math. 118 (2005), 425–441 | §§1–2, pp. 428–431; derivation before Prop. 2.2 and Prop. 2.2, p. 430; Th. 2.3, p. 431 | [Author-hosted published PDF](https://empslocal.ex.ac.uk/people/staff/ms220/Site/Publications_files/manuscripta.pdf) | Stable Frobenius rank, character decomposition and theta criterion read; DOI 10.1007/s00229-005-0592-z. |
| E. Ozman and R. Pries, *Ordinary and almost ordinary Prym varieties*, arXiv:1502.05959v3 | Th. 1.1, p. 2 | [arXiv PDF](https://arxiv.org/pdf/1502.05959) | Statement checked: generic ordinary-Prym result, not the prescribed-curve zero-rank assertion. |
| EGA IV₂ | Th. 5.10.5 and proof, pp. 115–116 | Exact locator supplied in K17 F149-GENERIC | Normality/Hartogs input carried via the supplied proof; the full EGA source was not separately retrieved by this subagent. |

## Supplied-result locators

All line numbers refer to the untouched input copies, not to a newly assembled master file.

| Result | File | Locator / treatment |
|---|---|---|
| F149-RELATIVE | `input/RETURN_K17_checkpoint_08_20261121T0616Z/K17.tex` | Lines 13494–13644, entire supplied proof read. |
| F149-GENERIC | Same | Principal statement starts line 13654; complete proof read. |
| F149-MARKED-RECOGNITION | Same | Principal statement starts line 13742; complete proof read. |
| F149-BARE-EXTENSION and F149-UNMARKED-CURVE | Same | Subsections “Generic recognition and the necessary profinite input” and “Why the generic marking cannot simply be omitted”; latter statement starts line 13908; complete proofs read. |
| AG-C149-NORMAL / FULLLIFT | `input/RETURN_GRH_NIGHT_checkpoint_07_20261121T0617Z/GRH_NIGHT.tex` | Lines 9063–9227, complete proofs read. |
| AG-C149-CUSP | Same | Starts line 9229; statement/proof comparison read, elliptic class calculation carried. |
| K17-VANDIVER-KERNEL | K17 input above | Starts line 9305; accepted theorem carried. |
| K17-GREENBERG-KERNEL | Same | Starts line 9678; accepted theorem carried. |
| K17-CUBIC-ODD / Triple-NV | Same | Starts line 10303; Triple-NV display (CU.1), lines 10429–10440. Hypotheses and conclusion located, no new arithmetic nonvanishing proof. |
| AN_GRH A05 | `input/RETURN_AN_GRH_final_20261121T0821Z/AN_GRH.tex` | Accepted prime-to-p point-separation theorem carried. Used only functorially in KT-PRODUCT-SEP. |
| AN_GRH A33–A52 | Same | Accepted route-2 reductions, failed routes and finite-field alternatives carried, not re-proved. |
| Cote 149 | Supplied scan references | Scans 79–82: normalizer comparison; 83–84: generic marking; 85: geometric subtorsor inside profinite tangent torsor. Scope follows the supplied archive transcription. |
| Esquisse / LM6 | Supplied source references | Esquisse §2; LM6 A.44–A.45: arithmetic pro-p Teichmüller-tower kernel question. No new transcription asserted. |

