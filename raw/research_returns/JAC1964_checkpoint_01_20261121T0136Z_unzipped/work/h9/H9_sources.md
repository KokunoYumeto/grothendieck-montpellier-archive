# H9 source record

Run: JAC1964-20261121. Agent: /root/h9_height. Model: GPT-6 Astra Pro;
reasoning effort not exposed. All source references below were actually read
in this run, with the limits specified. No entire external proof was formally
checked. Original attached results are taken as source hypotheses where the
task directs this.

## Attached sources

* `sources/ARCHIVE_44_scan004.tex`, Th. 5 and its margins: **algebraically**
  equivalent to zero; geometrically integral fibres; uncorrected formula.
  Read entire file. No scan image was supplied, so no palaeographic claim.
* `sources/ARCHIVE_44_scan002.tex`, Th. 3--4: domain of algebraic cycles and
  claimed canonical autoduality. Read entire file.
* `sources/ARCHIVE_44_scan008.tex` and `scan009.tex`, letter to Serre:
  primitive qualification and correspondence divisor. Read entire files.
* `sources/WARGAME_MATH_HUNCHES_20261112.md`, H9(a),(b): read entire H9.
* `sources/HODGE_BRIDGE_SKETCH_20261121.md`, Route 3, 3.4--3.5: read relevant
  entire section. These are unchecked proposals, not background theorems.
* 032 Corollary 8.4 is used only through the root agent's independent reading
  of the attached source. The H9 agent has not reread that PDF and therefore
  does not claim a source check of it.

## External primary sources and exact locators

1. Bruno Kahn, *Refined height pairing*, arXiv:2009.00533v7 (6 Dec 2023),
   later Algebra & Number Theory 18 (2024), 1039--1084.
   https://arxiv.org/pdf/2009.00533
   Read Definition 2.2 (admissibility), Proposition 2.8 and equation (2.9)
   (descent of intersection pairing), Theorem 5.6 (algebraically trivial
   cycles admit admissible lifts up to isogeny), Theorem 5.10 (elliptic
   normalization is the opposite of Silverman's), plus introduction's
   explicit comparison caveat. Web references available to root after its
   own open: `turn853292442view0`, `turn844745141view1`,
   `turn844745141view2`, `turn844745141view4`.
   Downloaded `work/h9/kahn_refined.pdf` for local reference; no need to
   redistribute this PDF in the final package.

2. Tetsuji Shioda, *On the Mordell--Weil lattices*, Comment. Math. Univ.
   St. Pauli 39 (1990), 211--240; Theorem 8.6, equations (8.11)--(8.15),
   printed p. 228. Original scan:
   https://rikkyo.repo.nii.ac.jp/record/10027/files/AA00610867_39-02_05.pdf
   Downloaded and rendered PDF page 18; image `work/h9/shioda_p18.png`
   was actually inspected. Theorem 8.6 verifies the inverse intersection
   matrix and the negative geometric sign. Web search ref:
   `turn853471825search35`; web open was rate limited but direct download
   succeeded. Do not use OCR alone for mathematical signs.

3. SGA 7 II, LNM 340, original scan:
   https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf
   Downloaded `work/h9/sga7_ii.pdf` (444 PDF pages). The programme-audit
   agent directly rendered/read:
   * XVII 2.2: definition of Lefschetz pencil (EGA IV 17.13.7 for transverse
     axis is cited there). Our quadric proof directly verifies its conditions.
   * XVIII 5.3.2 p. 287, 5.3.4--5.3.5 p. 288: condition (A).
   * XVIII Proposition 6.2 p. 319: (A) iff nontrivial inertia at every
     singular fibre.
   * XX Theorem 4.1 p. 355 and Remark 4.3 p. 356: Griffiths-group obstruction
     for high-degree pencils. Original pages are in `work/programme/`.
   The H9 agent relies on the programme audit for this direct image check;
   a modern online transcription was used only to locate pages, because
   there are detectable degree errors in some of its adjacent sections.

4. Shou-Wu Zhang, *Positivity of heights of codimension 2 cycles over function
   field of characteristic 0*, arXiv:1001.4788, Theorem 1 and Remarks 2.
   https://arxiv.org/pdf/1001.4788
   Read entire four-page extracted text. It motivated the explicit
   orthogonality gate but is not required in the proofs delivered here.
   Web ref `turn853292442view1`. Do not list it as a theorem used if the final
   paper omits this alternate approach.

5. Damian Rössler and Tamás Szamuely, *A generalization of Beilinson's
   geometric height pairing*, Documenta Math. 27 (2022), 1671--1692,
   DOI 10.4171/dm/x15, author PDF
   https://pagine.dm.unipi.it/tamas/beilpairing7.pdf
   Search retrieved Proposition 6.1, Corollary 6.2, Remark 6.3, for smooth
   models; not invoked for singular pencils. It is an alternative
   cohomological approach, not a claimed proof of the full Bloch/Beilinson
   comparison. Web refs `turn968503326search24`, `turn968503326search26`.

## Approaches tried and their outcomes

1. Treating geometrically integral fibres as eliminating all corrections:
   **refuted**, H9-C1. Integral cones contain middle-dimensional vertical
   cycles with nonzero intersection. Each of the two cones contributes +1
   in signed normalization.
2. Defining the height from arbitrary homologically trivial generic cycles
   by raw intersection of any closures: **not valid** without admissible
   lifts. Repaired by H9-T1, exact Schur-complement formula and radical
   compatibility condition.
3. Strengthening integral-fibre to nonzero vanishing cycles/condition (A):
   **proved**, H9-T2, sufficient to eliminate corrections on ambient
   primitive cycles. It gives an isometry between primitive algebraic
   cohomology of an abelian X and the geometric-height quotient R/R0 under
   032 Corollary 8.4. No abelian-Jacobian target is needed.
4. Replacing homological triviality by algebraic triviality silently:
   **refuted as a domain assertion**, explicit E^4 primitive cycle and SGA7
   XX 4.1. The defining map for an algebraic representative cannot be
   applied to that restriction.
5. Identifying primitive classes with a subgroup of J(K)/trace solely from
   a positive polarization: **invalid** without injectivity and height
   comparison. H9-T3 proves the exact quotient assertion once these maps
   exist. The quadric example has nonzero primitive classes in the kernel.
6. Deriving full H9(b) from corrected geometric height via a larger
   intermediate Jacobian or projection: **unresolved** as an arithmetic
   abelian-variety statement. The construction cited in cote 44 has only
   the algebraically trivial domain. For general homologically trivial
   cycles one must retain the full normal-function/motivic extension,
   not assume an unspecified map to P^m.

## Transcription conclusion

The quadric contradiction does not justify changing the reading
`fibres sont géom. intègres`. It establishes that the stated mathematical
hypothesis is insufficient. A corrected theorem needs admissibility or
condition (A), or explicit local correction terms. There is no supplied
manuscript image supporting a textual replacement.
