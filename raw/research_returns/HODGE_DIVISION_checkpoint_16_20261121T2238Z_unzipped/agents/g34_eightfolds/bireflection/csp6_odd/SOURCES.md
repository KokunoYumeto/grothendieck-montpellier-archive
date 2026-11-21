# Exact sources for D-C3-01–03

All source work below was completed before the clock-recorded time2026-11-21 19:18:55UTC. The full proof, code and source-scope qualifications are retained separately from the source computations.

## Complete generic CSp6 table

Frank Lübeck, *Charaktertafeln für die Gruppen CSp6(q) mit ungeradem q und Sp6(q) mit geradem q*, Heidelberg dissertation1993. Original author PDF:
https://www.math.rwth-aachen.de/~Frank.Luebeck/preprints/CharTabCSp6.pdf

The actual retained PDF is794539bytes, SHA-256 `5d336441c90390b3f2072ed7ceaaacdfb83776549954d9d830dbabe4967af070`, in the sibling's `lie_small_fields/cache/Luebeck1993.pdf`. The browser rejected the application/x-pdf content type; the original downloaded PDF and text were read locally. This is not reported as a successful browser PDF opening.

Freshly read in full: Introduction numberedpp3–4, the complete construction overview§2.2 numberedpp18–21, and§9 numberedpp78–79. These explicitly cover all ordinary irreducible characters, including nonuniform Lusztig-series pieces, and supply the complete values through mathematical CHEVIE files. The printed appendix alone contains only selected subtables. The entire underlying character-table construction was not independently reproved or completely reread.

Official complete-table inventory was freshly opened and read at:
https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/

The exact C3 entry identifies `CSp6.1` as the complete generic table; it distinguishes the first12 unipotent types and the separate `uniCSp6.1` subtable. The neighboring C2 warning about a preliminary erroneous full odd-CSp4 table does not apply to CSp6.1; no such CSp4 input is used here.

Immutable original mathematical source:
https://raw.githubusercontent.com/oscar-system/GenericCharacterTables.jl/87231738271ed548f62e7f1c98ff2bbfc1ed30d3/data/Tables/C3/CSp6.1.jl

Size1196534bytes; SHA-256 `f5e68e9429054370df7376f174a095bc548cf1ecf7ce44f5446f1eaebba250dc`. The complete extracted JSON and exact rational inequalities are retained. The final checker asserts equality of every original cell, degree, class length and class-type pair with a fresh extraction from this source. It does not execute external Julia.

The degree and ratio bounds are **new derived inequalities**. The table is a dissertation/official mathematical-data premise, not mislabelled as a separately refereed journal theorem.

## Complete q3 cover and outer data

Official CTblLib1.3.11 complete tables `2.S6(3)` and `2.S6(3).2`, both carrying `origin: ATLAS of finite groups, tests: 1.o.r.`. Fresh official pages:

- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.S6%283%29.html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.S6%283%29.2.html

The pages confirm orders9170703360 and18341406720,141 and138 classes, source strings and stored normal fusion. The pages are generated under version1.3.10 on20May2025; this metadata is distinguished from the actual retained package1.3.11. All original character values, powers, class orders/sizes, fusion, indicators and exact provenance are exported. GAP full orthogonality passes, and the separate rational-Fourier checker covers all selected rows and nonscalar classes. No independent construction of the original ATLAS character tables is claimed.

## Covers and full automorphisms

Hiss–Husen–Magaard, *Imprimitive irreducible modules for finite quasisimple groups*, MemoirsAMS234(2015),no1104, doi:10.1090/memo/1104. Complete author PDF at https://arxiv.org/pdf/1211.6350v2 is retained in this agent's `bireflection/sources/`. Chapter5 introduction and full Table1, numberedp35, were freshly reread. They give the complete exceptional-multiplier list; no odd-field PSp6(q) is exceptional. The ordinary universal cover is Sp6(q), with center2. No imprimitive-character classification theorem from this monograph is used.

Li–Xia, *Factorizations of Almost Simple Groups with a Solvable Factor, and Cayley Graphs of Solvable Groups*, MemoirsAMS279(2022),no1375, doi:10.1090/memo/1375. Author arXiv1408.0350v3,§2.2.2/Table2.1, numberedp14, was freshly read and rendered in the immediately preceding HES audit. It gives Out(PSp2m(q))=C_(2,q−1)×C_f outside(m,p)=(2,2). The standard inner, diagonal and field description applies to rank3, with no graph automorphism. Retained author PDF SHA-256 `4ef16aa4308f8c487a06e9c8e84ece77247d0e763146f0215d8e109e443e3a93`; no publisher-pagination verification is claimed. The lifting, cyclic-extension normalization and projective q9 descent used here are proved in the new text.

## Unipotent estimate

Liebeck, *Character ratios for finite groups of Lie type, and applications*, ContemporaryMathematics694(2017),193–208. Author PDF:
https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf

Definitions and quasisimple conventions numberedp2 and Theorem2.4(i) numberedpp3–4 were freshly read and visually checked in the HES audit. The exact bound for q>4 is `1/(sqrt(q)-1)`, with the subtraction outside the radical. This gives1/2 atq9 and at most1/4 forq≥25. It is the published restatement actually read of Gluck's original estimate. Gluck1995's full original proof was not newly retrieved. The theorem's nonunipotent part is not substituted for its unipotent part.

Vinroot/Wonenburger reality and factorization papers were considered during exploration but are not premises: the final q9 support proof avoids a selfduality assertion altogether. No unrefereed manuscript theorem is used.
