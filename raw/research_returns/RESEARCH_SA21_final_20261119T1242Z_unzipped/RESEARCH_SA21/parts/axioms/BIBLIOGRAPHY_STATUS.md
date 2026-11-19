# Sources actually used for B.1–B.2

We list opened status separately from whether a source was requested in the broader prompt. The parent bibliography supplies the shared BibTeX entries. Our fragment uses `Grothendieck1986`, `Barmak2011` and `Coste1999`.

## Grothendieck, A. (1986). Vers une géométrie des formes. Cote 156, Université de Montpellier archive.

**Opened:** the supplied transcriptions and correction tables; the official archive; the original 156-6 PDF; original 156-4 scans shared by the parallel agent; selected original 156-8/31. We distinguish actual image inspection from reading a transcription.

Official sources: <https://grothendieck.umontpellier.fr/>, <https://grothendieck.umontpellier.fr/156-4.pdf>, <https://grothendieck.umontpellier.fr/156-6.pdf>, <https://grothendieck.umontpellier.fr/156-8.pdf>.

Original images inspected in this run:

- **156-4/54:** equality-based complete join irreducibility, not bounded-join primality. We inspected `SA21_sources/bmodels/156-4-scan54.png`; the other agent independently inspected scans 54 and 55, including the following page's false join-to-union assertion.
- **156-4/72:** C6(a) unrestricted uniqueness, with stratum formula (b) as a separate marginal addition. We inspected `SA21_sources/bmodels/156-4-scan72-bottom.png`. This resolves the clause used in the redundancy proof.
- **156-6/34:** the shortened final At-star list omits membership in the chosen family. We inspected `parts/axioms/scans/156-6-034.png`. The longer scan-32 formulation explicitly has membership.
- **156-6/88:** the mixed-incidence clause has eta in all of F-prime. We inspected `parts/axioms/scans/156-6-088.png`. We distinguish and prove the literal and complementary-stratum versions.
- **156-8/31:** we inspected `SA21_sources/156-8_scan31_Mag4.png`. A separate preceding glyph is visible, but its identification as a negation remains uncertain. Both readings have complete proofs and finite certificates.

The exact source filenames and line ranges appear beside the mathematical assertions in `axioms.tex`. Central ranges include J156-4-07:84–115,153–155; J156-4-09:161–176,187–191; J156-4-11:49–77; J156-6-04:189–213,245–249; J156-6-05:4–34; J156-6-10:122–145; J156-6-12:4–24; H156-01:139–197,279–318; J156-8-01:243–263; J156-8-03:91–168; J156-8-04:199–247,280–300; and J156-5-02:70–115. These are relative to the supplied `156_Codex_web` transcription directory. They identify evidence, not an assumption that every transcription mark is correct.

## Barmak, J. A. (2011). Algebraic topology of finite topological spaces and applications. Lecture Notes in Mathematics, 2032. Springer. https://doi.org/10.1007/978-3-642-22003-6

**Opened:** the full original book PDF via the academic mirror <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/barmak2.pdf>.

**Exact result used:** Proposition 1.2.4, printed p. 5, PDF page 23: finite-space connectedness, order connectedness and path connectedness coincide. We do not appeal to this finite theorem for an infinite conclusion. Our proof explicitly extends the clopen/comparability argument to arbitrary admissible families and handles possibly nonsingleton residual fibers.

We reopened the exact proposition and its proof. The manuscript uses the stable bibliographic citation and printed-page locator.

## Coste, M. (1999). An introduction to o-minimal geometry. Author's lecture notes, Institut de Recherche Mathématique de Rennes.

**Opened:** the relevant primary-source PDF text at <https://perso.univ-rennes1.fr/michel.coste/polyens/OMIN.pdf>, including the statements and proofs needed here. Fresh direct fetches intermittently timed out, but the previously opened primary-source text was successfully reopened at the exact passages. We do not substitute a secondary theorem summary.

**Exact results used:**

- Theorem 3.4, printed pp. 26–27: closed and bounded definable sets have closed and bounded definable continuous scalar images. We derive boundedness and closedness of a path image explicitly, using coordinates and distance to a putative missing limit point.
- Theorem 3.9, printed p. 28: finitely many definable clopen, definably path connected components. We use the resulting definable path without assuming an injective-arc theorem.
- Theorem 4.4, printed p. 42, proof pp. 42–44: finite definable triangulation of a closed bounded set compatible with a finite family. We apply it to the path image and its two endpoints, and then use our per-figure connectedness theorem.

We reopened the exact passages and checked their stated hypotheses. The geometric assertion is definable connectedness over an arbitrary real closed field, not ordinary topological connectedness over a non-Archimedean field.

## Literature-search scope and attribution

We searched manuscript-specific combinations including Grothendieck with At14 and atelier, At9 Sigma, multistrates and connectedness, and Analysis situs/deuxième mouture/axiomes. These searches did not supply a primary published resolution of the specific implications. We make no claim that none exists. The parent independently found and records earlier attention to the manuscript and maintains the broader literature-search record.

We did not use a mathematical point from Michel Hua's project in this contribution. Other requested books and articles belong to the parent's or other agents' parts; we do not mark them opened merely because their bibliographic metadata is known.

Additional original-source inspection:156-6 scan12, formula(1.20), rendered from the opened official PDF to SA21_sources/156-6-scan12-primality.png. Both inequalities in the bounded-join-primality definition were visually confirmed.
