# Independent review of the complete outer-five canonical rank law

Statement **A-053**, reviewing R-031,
work/rectangular/outer_five_canonical_rank_law.md,
OF.1–OF.11 and every section and table.
Checked 21 November 2026 by GPT-6 Astra Pro,
run /root/archive_audit; effort setting not exposed.

**Complete proof PASS after the exact right-multiplication correction
described below.** The law concerns the specified canonical map and
is established in every degree and on every output type. The primary
fourth-square matrix and the complete low-degree multiplicity table
were independently reconstructed and checked.

## 1. Tensor pairings and the actual incidence map

The nested symmetric pairing is the restriction of the ordinary
tensor evaluation pairing under averaging. Its quotient map is
therefore the adjoint of averaging inclusion. The averaging
idempotents are self-adjoint; the tensor-grid permutation has its
inverse as adjoint. These facts prove the exact transpose identity
\[
h_{d,e}(V)^*=h_{e,d}(V^*)
\]
with scalar one. In particular, each subsequent use of transpose
identifies the rank of the particular map being studied.

For the multilinear block basis \(q_L\) of
\(\operatorname{Sym}^v\operatorname{Sym}^u\), its tensor
inclusion gives coefficient \(1/[v!(u!)^v]\) to every ordered
row arrangement. A transverse unordered column partition has
exactly \(v!u!\) such arrangements: choose the order of its rows
and columns, after which each cell is prescribed by the unique
intersection element. Hence its coefficient is
\[
(u!)^{1-v}.
\]
A nontransverse column partition cannot arise. Thus the incidence
matrix is related to the normalized canonical map by the exact
formula OF.8, and in the fourth square the scalar is \(24^{-3}\).

The passage to every dimension retains these same multiplicity
matrices. The multilinear tensor weight in \((\mathbf Q^N)^{\otimes N}\)
is a regular permutation module on the distinct tensor words.
Every primitive Young projector has a nonzero image there.
Consequently every Schur multiplicity map is detected by this
weight. Injectivity on the entire multilinear weight proves
injectivity of every such matrix, and these same matrices act
in every ambient dimension. This verifies the specified
Schur–Weyl transfer, including the disappearance of Schur
functors whose lengths exceed that dimension.

## 2. Jacob's original matrix and the corrected multiplication side

The primary source was opened and its relevant text read:
Juby Jacob, Representation Theory of Association Schemes (2004),
Definition 1.1.11 p.9; Definition 4.1.1 p.92;
§4.2 pp.95–99; Table 4.4 pp.104–106.
https://publications.rwth-aachen.de/record/51990/files/Jacob_Juby.pdf .

Definition 1.1.11 explicitly gives
\[
(B_i)_{j,k}=p^k_{j,i}.
\]
The first R-031 draft reversed the two lower indices and called
the map left multiplication. The report has been corrected and
the changed paragraph reread: in column coordinates \(B_{42}^t\)
represents \(B\mapsto BA_{42}\). Solving
\(BA_{42}=A_0\) gives an inverse in its faithful finite-dimensional
matrix representation. This is the exact algebra map that transfers
the collapsed determinant to the full incidence operator.

I independently retrieved all three published column blocks from
the primary PDF's indexed text. The page-header joins after the
last entries 64 and 48 were separated explicitly. The resulting
43-by-43 matrix, saved as JACOB_TABLE_PRIMARY_RECONSTRUCTION.tsv,
agrees in all 1,849 entries with the rectangular agent's transcription.

Ordinary rational Gaussian elimination using Python Fraction
arithmetic, independently of that agent's fraction-free Bareiss
calculation, gives
\[
\det B_{42}=2^{223}3^{67}.
\]
The exact integer, source locator and file hash are in
the primary independent receipt JSON. The companion script is the independent Jacob primary checker.

The original 2,627,625-point orbital enumeration has not been rerun.
A direct local download returned an HTML challenge, retained under
its descriptive HTML filename; no local primary PDF is asserted.
The source was read through the public web PDF text. Screenshot
requests yielded only image placeholders in this tool surface,
so this event does not claim visual inspection of those pages.

## 3. Every degree in the rank law

At \(n=1\), the canonical map is the identity.
At \(n=2,3\), the previously fully read Sra III Theorem 1.3,
equation (1.1), and its entire polarization/annihilator proof
apply at \((b,a)=(5,2),(5,3)\). Both satisfy
\(b\ge(a-1)^2\). Their surjections transpose under OF.6 to
the required injective maps. The precise primary source and
whole-proof event are A-REF-SRA13.

At \(n=4\), the established fourth square is injective by the
preceding source matrix and exact morphisms. McKay propagation
then gives injectivity at \((4,5)\). Its whole proof and the
auxiliary scalar and spectator-factor corrections were already
read and independently checked in A-047 and A-REF-MCKAY.
No change to the normalized canonical map is introduced by
those auxiliary normalizations.

At \(n=5\), the eight CIM types in OF.4 agree exactly with the
previously inspected primary Theorem 6(b). Each occurs once in
the actual kernel. Since this is the square map, subtracting
that kernel multiplicity gives the displayed rank on every type.
The four strict cases and target multiplicities were separately
reconstructed in A-052 by two character methods.

For every \(n\ge6\), the actual CIM \((5,6)\) injectivity result
and the same propagation theorem give injectivity of \(h_{5,n}\).
The exact transpose identity then gives surjectivity of \(h_{n,5}\).
These parameter ranges exhaust every positive integer \(n\);
the degree-zero scalar map is correctly handled separately.

All multiplicity matrices are rational, so base extension to any
characteristic-zero field preserves their ranks. The natural
inclusion of ambient vector spaces commutes with averaging and
grid permutations. Together with the fixed Schur matrices, this
justifies every stated finite-dimensional specialization.

## 4. Independent complete low-degree table

The independent program check_outer5_canonical_independent.py
evaluates the exact selected-subset restriction complex of G-027,
with its orientation signs and Weyl coefficient extraction.
This differs from both the root cycle-alternant algorithm and
the rectangular agent's monomial-multiset expansion.

For outer degrees at least three it computes the character of
the actual fat-arrangement module in the balanced flag dictionary.
For outer degree one it uses the identity. At degree two the
balanced weight in
\(\det^{\lambda_2}\operatorname{Sym}^{\lambda_1-\lambda_2}\mathbf Q^2\)
has its sole monomial fixed by slot exchange up to
\((-1)^{\lambda_2}\), giving multiplicity one exactly when
\(\lambda_2\) is even. This supplies the explicit remaining
small-rank calculation.

All 313 partitions of \(5n\), \(1\le n\le4\), with length at
most five were enumerated independently and matched to the table.
Both source and target were computed: all 626 comparisons pass.
Their cokernel differences also agree. Shapes of greater length
are excluded by the actual inclusion into the tensor product of
the indicated number of row symmetric powers and its successive
Pieri decompositions.

There are 38 strict cases. Their complete independent summary is:

| Degree | Strict shapes | Positive images | Positive targets | Nonzero targets reached in full |
|---|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 | 0 |
| 3 | 7 | 0 | 3 | 0 |
| 4 | 30 | 16 | 27 | 4 |

At degree four, all positive image multiplicities are one.
The four fully reached nonzero targets are exactly the four
types listed in R-031. The remaining degree-five and higher
strict conclusions follow from the already established actual
rank law and A-052, with all determinant shifts included.

The receipt is OUTER5_CANONICAL_INDEPENDENT_RECEIPT.json.
The finite calculations verify multiplicities and table completeness;
the actual rank identification is supplied by the particular
injective, kernel and transpose maps proved above.
