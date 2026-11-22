# Primary-source scope audit for K-018

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro,
effort not exposed, run GCT_POS.

## Finding and limitation

Exponential denominators of axial-assignment vertices are established literature.
The directly inspected dyadic constructions below have denominator
`2^(n-1)` or `2^(n-k-1)`. They give denominator 256 at `n=9`, whereas
the independently checked K-018 construction gives 512. This is a comparison
with specified formulas, **not a historical priority claim**. The full text of
the 2008 paper was not available in this audit; its precise denominator theorem
remains an explicit source gate. None of these papers is a dependency of the
self-contained K-018 gadget proof.

## Bibliographic corrections and exact reading scope

### Kravtsov and Lukshin (2008)

Kravtsov, **M. K.**, & Lukshin, **E. V.** (2008). Polyhedral combinatorics of
multi-index axial transportation problems. *European Journal of Operational
Research, 189*(3), 920–938.
https://doi.org/10.1016/j.ejor.2007.02.059

Primary publisher record:
https://www.sciencedirect.com/science/article/abs/pii/S0377221707006674

The correct DOI is **10.1016/j.ejor.2007.02.059**. The proposed
`10.1016/j.ejor.2007.05.029` belongs to a different article about lattice-system
reliability and must not be used. Author initials, title, volume, issue, pages,
date, DOI, abstract, and the full publisher-visible introduction were checked.
The introduction locates exponential denominator growth for general integral
marginals in Section 4. It does not state the numerical growth rate in the
accessible text. The full Section 4, its theorem numbers, proofs, and examples
were **not read**. Therefore this audit does not assert that 512 at dimension 9,
or a larger exponential base, is absent from that paper.

### Kravtsov (2010)

Kravtsov, **V. M.** (2010). On the characterization of noninteger vertices of
the relaxation polyhedron in the multi-index axial assignment problem.
*Computational Mathematics and Mathematical Physics, 50*(9), 1615–1626.
https://doi.org/10.1134/S0965542510090125

Primary English publisher record:
https://link.springer.com/article/10.1134/S0965542510090125

The English title above follows the publisher. Math-Net translates it slightly
differently as “On a characterization … relaxational polyhedron.” The original
Russian article is *Zhurnal Vychislitel'noi Matematiki i Matematicheskoi Fiziki,
50*(9), 1697–1708, titled “О характеризации нецелочисленных вершин
релаксационного многогранника многоиндексной аксиальной задачи о назначениях.”
The original primary PDF was recovered through indexed full-text extraction:
https://www.mathnet.ru/links/82f8206bb752a36e9d9c58a01b3d9692/zvmmf4941.pdf

Reading covered the definition of `M(p,n)`, the preliminary setup, **all of
Section 3**, and the surrounding references. Theorem 4, printed page 1703,
reproduces a three-index family with an entry `1/2^(n-k-1)` and all denominators
dividing that number, for `0<=k<=n-2`. Theorem 5, page 1704, extends that family
to more indices. Theorem 6 on the same page is a `p>=4` construction, also with
denominators dividing `2^(n-1)`. These displayed families do not yield 512 at
`n=9` or a three-index rate exceeding `2^(n-1)`. This is a source-scope check,
not an independent verification of every theorem in that article.

### Franks and Reichenbach (2021)

Franks, **W. C.**, & Reichenbach, **P.** (2021). Barriers for recent methods in
geodesic optimization. In V. Kabanets (Ed.), *36th Computational Complexity
Conference (CCC 2021)* (LIPIcs, Vol. 200, Article 13, pp. 13:1–13:54).
Schloss Dagstuhl–Leibniz-Zentrum für Informatik.
https://doi.org/10.4230/LIPIcs.CCC.2021.13

Primary full PDF:
https://drops.dagstuhl.de/storage/00lipics/lipics-vol200-ccc2021/LIPIcs.CCC.2021.13/LIPIcs.CCC.2021.13.pdf

Read the complete Lemma 2.5, its proof and preceding attribution, Example 2.6,
the surrounding margin argument, and references 37–38. Lemma 2.5 is on printed
page **13:15**, PDF index 14. Its array has an entry `2^(-n+1)` and every entry
is an integer multiple of it, so its common denominator is exactly `2^(n-1)`.
This is an existence construction, not an upper bound on every vertex.
The source explicitly attributes the array to **Kravtsov (2007), Theorem 1,
case k=0**, and notes the earlier **Kravtsov–Lukshin (2005), Theorem 9**.
These are not the 2008 and 2010 bibliographic entries. The 2021 paper also has
other varying-number-of-factors constructions; these must not be interpreted
as a stronger fixed-three-factor denominator statement.

## Earlier sources identified through the primary references

Kravtsov, **V. M.** (2007). Combinatorial properties of noninteger vertices of
a polytope in a three-index axial assignment problem. *Cybernetics and Systems
Analysis, 43*(1), 25–33. https://doi.org/10.1007/s10559-007-0023-0

The primary publisher metadata and abstract were read. The Russian original
appears in *Kibernetika i Sistemnyi Analiz*, No. 1, pp. 33–44; these are not
the English translation's pages. Its full proof was not separately inspected
here. The relevant array is reproduced explicitly in the inspected 2010 and
2021 primary sources.

Kravtsov, **M. K.**, & Lukshin, **E. V.** (2005). On some properties of
noninteger vertices of a three-index axial transportation polytope.
*Trudy Instituta Matematiki NAN Belarusi, 13*(2), 31–36.

This entry was identified from the 2007 publisher's reference 12 and the 2021
paper's reference 37. The latter reverses Lukshin's initials as “V. E.”; the
2007 primary reference and 2008 publisher record give “E. V.” The 2005
primary article itself was not obtained, so that spelling reconciliation is
recorded rather than hidden. No theorem-level independent check of 2005 is
claimed.

## Consequence for the research ledger

K-018 remains a proved explicit counterexample to the proposed universal
`2^(n-1)` stabilizer-period ceiling within this project, with its own exact
support, balance, determinant, and denominator certificates. Its theorem must
not be labeled the first exponential denominator construction or the first
construction exceeding that rate. The finer historical question requires the
unread 2008 Section 4 and any additional relevant denominator literature.

