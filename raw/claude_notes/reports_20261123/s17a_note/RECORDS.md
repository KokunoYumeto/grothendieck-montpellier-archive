# S17a: records

The note is `s17a_note.tex`, with its PDF `s17a_note.pdf`: 7 pages, three pdflatex passes, 0 overfull boxes. Every
page was rendered at 70 dpi and read by the editor on 23 Nov 2026.
- SHA-256 of the PDF: e8b03294b8f00b6a761a540ca33cfb4eb2eec8172f143573cc65010e1d6610b9.
- Editor: Claude Opus 5.5 at effort max (agent ac8bd2a26d00b4f37).
- The source of the mathematics is the research run RESEARCH_SA17 at checkpoint 12, GPT-6 Astra (ChatGPT Pro mode).
  The relevant statements are B:crystal-counterexamples, B:finite-PD, B:positive-exclusion and B:base-kinds.

## 1. Literature, with locators (the gate)

Each entry says whether it was read at the source (R), through a page fetch summary (F), or from memory or citation
only (M).

| Work | Locator | What it gives | How read |
|---|---|---|---|
| A. J. de Jong, *Barsotti-Tate groups and crystals*, Doc. Math. Extra Vol. ICM 1998, II, 259-265 | pp. 260-261, list (i)-(xi); item (x) | (x): "D is not fully faithful in general. This fails even over the ring F_p[x,y]/(x^2,xy,y^2). See [2, 4.4.1]", where [2] is Berthelot-Messing III. The list has no reduced counterexample. | R: fetched PDF, text extracted; SHA-256 bb3aec42...cf3a |
| A. J. de Jong, *Crystalline Dieudonné module theory via formal and rigid geometry*, Publ. Math. IHÉS 82 (1995) 5-96 | Introduction (Main Thms 1-2); Thm 5.1.1; Cor. 5.1.2 | Reduced S of finite type over a field with finite p-basis: Hom(D(G2), D(G1)) = (torsion subgroup) ⊕ D(Hom(G1,G2)). The torsion is "known to be zero ... if S is a l.c.i."; no example of nonzero torsion. Cor. 5.1.2: fully faithful up to isogeny. | R: the run's text extraction of the Numdam PDF; SHA-256 a528ce44...17e7 |
| A. J. de Jong, W. Messing, *Crystalline Dieudonné theory over excellent schemes*, Bull. SMF 127 (1999) 333-348 | Introduction; Section 1; Remark 1.4; Thm 4.6 | Fully faithful over excellent lci; up to isogeny over excellent local rings. Remark 1.4: failures for finite and truncated groups (BBM 4.4.1, Koblitz-Ogus; F_p[t]/(t^p)). | R: the run's text extraction (Numdam); SHA-256 aae95d8e...c4e5 |
| E. Lau, *Divided Dieudonné crystals*, arXiv:1811.09439v2 | Cor. 1.6 (= Cor. 9.5); Cor. 1.7 (= Thm 7.9); Cor. 1.8; Thm 1.9; Remark 3.4; Def. 4.3 | Fully faithful on F-finite PD-torsion-free schemes; up to isogeny, cokernel killed by p, on F-finite F-nilpotent schemes. Remark 3.4: not fully faithful over k[X,Y]/(X,Y)^2 (citing Berthelot-Ogus). | R: the run's text extraction; SHA-256 a52550a5...f1ed |
| T. Zink, *A Dieudonné theory for p-divisible groups*, Class field theory - its centenary and prospect, Adv. Stud. Pure Math. 30 (2001) 139-160; https://www.math.uni-bielefeld.de/~zink/CFTpaper.pdf | Introduction, p. 2 | "the crystalline Dieudonné functor is not fully faithful in this case [rings with nilpotent elements] ... On the other hand for a reduced ring the prime number p is a non-zero divisor in Ŵ(R) and therefore V^{-1} may be recovered from the relation pV^{-1} = F." | R: fetched PDF, text extracted; SHA-256 1f164a93...c3a9 |
| The Stacks project, Section 60.22, Example 60.22.1 (Tag 07LJ); Prop. 60.21.3 (Tag 07LG); https://stacks.math.columbia.edu/tag/07LI | Example 60.22.1 | τ_0 = γ_p(x²)γ_p(y²) − γ_p(xy)² on F_p[x,y]/(x²,xy,y²): pτ_0 = 0, dτ_0 = 0, F*(τ_0) = 0, and a detector B with δ_p(ax²+bxy+cy²+du+ev+fuv) = a^p u + c^p v sending τ_0 to uv. This δ_p fails the addition axiom at p = 2 (see section 3). | F: page fetch summary of the statements and formulas |
| P. Berthelot, W. Messing, *Théorie de Dieudonné cristalline III*, Grothendieck Festschrift I (1990) 173-247 | 4.4.1 (per de Jong's ICM survey) | The non-reduced counterexample; full faithfulness for schemes with locally a p-basis | M: not accessible (no free copy); known only through de Jong's citations |
| P. Berthelot, L. Breen, W. Messing, *Théorie de Dieudonné cristalline II*, LNM 930 (1982) | construction of D; base change | Definition of D; full faithfulness listed as an open question in the introduction | M: through citations and a search snippet; not opened |
| J. Anschütz, A.-C. Le Bras, *Prismatic Dieudonné theory*, Forum Math. Pi 11 (2023) | Thm 4.74 | Fully faithful over quasisyntomic rings | M: opened by the run, not by the editor today |
| Hexagon (hexagonmath.org), searched 23 Nov 2026 | search "Dieudonné"; "crystalline"; "p-divisible" | "Dieudonné": 1 result, 2610.00662 (crystalline Tate classes of Mumford's fourfolds, unrelated). "crystalline": 7 results, none on Dieudonné functors. "p-divisible": 0. | R: search result pages |
| Web search (extended), 23 Nov 2026 | "crystalline Dieudonné functor not fully faithful reduced base counterexample"; "de Jong torsion subgroup ... two planes" | No reduced counterexample found | R |

**Conclusion of the gate.**
- The non-reduced example is classical: Berthelot-Messing III 4.4.1, and the Stacks project Example 60.22.1.
- The reduced example (two planes) and the non-noetherian variant were found nowhere in the works read.
- Residual gap: Berthelot-Messing III could not be read. De Jong's survey cites only its non-reduced ring.

**Kind: clear.** No neighbouring post on Hexagon or elsewhere in recent weeks.

## 2. Checks the results received

All checkers are Claude Opus 5.5 at effort max, agent ac8bd2a26d00b4f37, unless stated. Types are the seven check
types.

| Statement (note) | Run id | Date | Check type | Outcome |
|---|---|---|---|---|
| Prop. 4.1: pτ = 0, dτ = 0, σ(τ) = 0 (with the R_0 specialisation) | B:crystal-counterexamples | 19 Nov 2026 (intake of cp02) | targeted proof check | confirmed: pτ = 0, dτ = 0, φ(τ) = 0, the compatibility pτ = φ(τ), Hom = 0, and the bases outside the positive classes |
| Lemma 5.1: divided powers on B_p, all p, with the p = 2 correction | B:finite-PD | 20 Nov 2026 (intake of cp12) | independent re-proof | confirmed by hand: basis, xK = yK = 0, K² = F_p·uv; additivity, scalars, products (Lucas), composition; τ ↦ uv |
| Theorem 1.1 (two planes) and Cor. 1.2(4) | B:crystal-counterexamples | 20 Nov 2026 | targeted proof check | confirmed: refutation of full faithfulness stands, with τ ≠ 0 from the detector |
| Positive classes exclude R (Cor. 1.2(2)) | B:positive-exclusion, B:base-kinds | 22 Nov 2026 (full intake) | targeted proof check | confirmed |
| Prop. 4.1, again | B:crystal-counterexamples | 23 Nov 2026 (editor) | independent re-proof | p!·X = (ac)^p γ_p(bd) = γ_p(abcd) = p!·Y; the da-coefficient is a^{p-1}/(p-1)!·(γ_p(bcd) − γ_p(bcd)) = 0; γ_p(s^p) = (p!)^{p-1}γ_p(s)^p from γ_p(s)^p = p!·γ_p(γ_p(s)); σ(τ) = (p!)^{2p-2}(X^p − Y^p) = 0 |
| Lemmas 3.1, 3.3 (direction and convention; Hom in both directions) | B:crystal-counterexamples | 23 Nov 2026 (editor) | targeted proof check | F- and V-compatibility both give pτ = φ(τ). Hom(Q_p/Z_p, μ) = 0 over reduced rings. Hom(μ, Q_p/Z_p) = 0 over any F_p-algebra (infinitesimal to étale). New remark 3.2: the result does not depend on the convention. |
| Lemma 5.1, again, as written in the note | B:finite-PD | 23 Nov 2026 (editor) | targeted proof check | every case of the product and composition identities rechecked against the explicit series, including p = 2 (indices 1+2 = 3 = p+1, 2+2 = 4 = 2p) |
| Remark 5.2: the Stacks formula fails at p = 2 | (run's observation) | 20 and 23 Nov 2026 | refuted, with the refined statement's id (Lemma 5.1) | δ_2(u+v) = 0 but γ_2(u+v) = uv. The correct γ_2 adds δε·uv |
| Remark 6.2: τ vanishes on p-torsion-free thickenings | new in the note | 23 Nov 2026 (editor) | targeted proof check | the value is p-torsion in a p-torsion-free ring; W(A) → A for reduced A is such a thickening (W(A) p-torsion free, VW(A) carries divided powers) |
| Cor. 1.2(2): R is not Cohen-Macaulay | new in the note | 23 Nov 2026 (editor) | targeted proof check | the punctured spectrum of the two planes at the origin is disconnected, and Hartshorne's connectedness theorem then rules out Cohen-Macaulay in dimension 2 |

No human has checked any of this.

## 3. Faults found and repaired

1. **Credit.** The run presented R_0 = F_p[x,y]/(x²,xy,y²) as one of its own three bases.
   - Repair: it is credited to Berthelot-Messing III 4.4.1 and to the Stacks project Example 60.22.1.
   - In the note it appears only as a remark (Remark 6.1) and as the target of the specialisation used to prove τ ≠ 0.
2. **Stacks Example 60.22.1 at p = 2.**
   - Fault: the displayed δ_p is not a divided-power operation for p = 2.
   - Repair: Lemma 5.1 gives the correct formula with a full proof for every p.
   - This is a correction to send to the Stacks project; the example's conclusion stands.
3. **Convention.** The direction of the morphism depends on the convention for D. Repair: Remark 3.2. Both Hom groups
   vanish over reduced bases, so the theorem holds in either convention.

## 4. Whom to write to when it is posted

- **Eike Lau.** Divided Dieudonné crystals: the note shows that his Remark 3.4 has a reduced analogue, and that the
  cokernel in his Cor. 9.5 can be nonzero over a reduced base.
- **A. J. de Jong and William Messing.** The torsion term of de Jong's Main Theorem 2 occurs, and the lci hypothesis of
  their Theorem 4.6 cannot be weakened to reducedness.
- **The Stacks project** (a comment on Tag 07LJ, or their GitHub). The p = 2 correction of the δ_p formula in Example
  60.22.1.
- **Johannes Anschütz and Arthur-César Le Bras**, for context: their quasisyntomic theorem, and the reduced
  non-quasisyntomic boundary.
- **Thomas Zink**, as a courtesy (Remark 6.2 on displays).

Send nothing before the user's word.

## 5. What is left before posting

- The user's word.
- A second reader's re-proof from the statements alone: the note's main theorem has been re-proved by hand only by
  the same model (Claude Opus 5.5 at effort max).
- Optionally, a sighting of Berthelot-Messing III, to close the residual gap.
- The workbench entry for the record address.
