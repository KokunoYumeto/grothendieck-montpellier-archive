# D-HES04–06: exact known-input and retrieval log

Run HODGE_DIVISION, 2026-11-21. Author /root/imprimitive, GPT-6 Astra Pro,
effort inherited/not exposed. Parent handles persistence of authored files;
third-party PDF caches are excluded from the deliverable.

## Unipotent ratio, with the corrected radical

M. W. Liebeck, *Character ratios for finite groups of Lie type, and
applications*, Contemporary Mathematics 694 (2017), 193–208.
Author PDF: https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf .
The simply connected/quasisimple definitions are on author pp.2–3, and
Theorem2.4(i) is on pp.3–4. It gives 3/4 for q≤4 and
1/(sqrt(q)−1) for q>4, for every noncentral unipotent element and every
nontrivial ordinary irreducible character. The exact original reference
named there is Gluck (1995); the published research survey is the
restatement actually read.

Frozen PDF: cache/Liebeck2017CharacterRatios.pdf, 383678 bytes,
SHA-256 e6e0a0148264d0b2a46a6a6e7fdc09096a6837155510a7482584ef99dd2300fc.
The rendered author p.4 is cache/Liebeck2017_p4.png. The radical was
visually rechecked, not inferred from text extraction.

An exploratory transcription used sqrt(q−1), and led to the proposed
q=8 comparison c<1/2. That expectation is refuted and is not a premise
of any canonical theorem. The correct comparison is c<9/16 for q≥8,
equivalent at q=8 to625<648. The completed q=2 theorem never used the
misread q>4 expression.

## The field automorphism at q=4

Cai Heng Li and Binzhou Xia, *Factorizations of Almost Simple Groups
with a Solvable Factor, and Cayley Graphs of Solvable Groups*, Memoirs
AMS279(1375)(2022), v+99pp., DOI10.1090/memo/1375.
The exact source read is the author-linked version
https://arxiv.org/pdf/1408.0350v3 (25February2016), §2.2.2,
Table2.1, numberedp14/PDFindex13. The complete preceding convention
q=p^f and the table were read and rendered. Its symplectic row states
Out(PSp2m(q))=C_(2,q−1)×C_f for(m,p)≠(2,2), hence OutSp2n4=C2 for n≥4.
The proof independently checks that entrywise Frobenius is noninner by
a natural trace witness, so no interpretation of an unlabeled outer
generator is required.

The author publication list https://sites.google.com/site/binzhouxia/research
lists the published memoir with this arXiv link. Publisher metadata at
https://doi.org/10.1090/memo/1375 independently confirms publication.
The publisher PDF request returned403; its pagination was not read.
The author page's unrelated correction to Lemma8.31 has no bearing on
Table2.1. This uses a known classification statement, not any of the
memoir's factorization results.

Frozen cache/LiXia2022_author_v3.pdf:1043141bytes,
SHA-2564ef16aa4308f8c487a06e9c8e84ece77247d0e763146f0215d8e109e443e3a93.
Actual retrieval2026-11-21T19:01:05.261104+00:00,
recorded in all_even_source_retrieval.json.
Web full text/render refs turn705547702view0, turn483920701view0,
turn483920701view1; publication list turn546158498view3.

## Previously reviewed inputs used with their scopes

- Gow1981, theorem p583 and full symplectic proof §3 pp589–591:
  every symplectic element in characteristic2 is a product of two
  involutions, hence every ordinary irreducible character is real.
  This does not assert Frobenius–Schur indicator+1.
- Hiss–Husen–Magaard2015, Chapter5 Table1 numberedp35: complete exceptional
  Schur-multiplier list; no Sp2n(q), n≥4, q even occurs. Combined with the
  usual multiplier(2,q−1), every quasisimple cover in this range is the
  simple group itself.
- D-ESC01 exact full generic Sp6.0.jl certificate: all65 nontrivial
  character-type degree polynomials at q4 have minimum378. The new
  checker evaluates all65 from the frozen previously verified coefficient
  input, SHA92e32ae7b01d49469f31464472ae044b320b59a6400fedaec5003fde2760a3b3.
- D-HES01–03: the already reviewed all-rank q2 theorem, including only
  essential ATLAS Sp8/Sp10 endpoints. Computed Sp12 is redundant.

No all-character proper-parabolic theorem from Gluck–Magaard1998, no
odd-characteristic-only automorphism source, and no assumed equality of
original and inducing character fields is used.
