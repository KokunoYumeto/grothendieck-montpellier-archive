# Three complete finite boundary kernels

Statement **R-016**, completed and independently checked on 2026-11-21 UTC by GPT-6 Astra Pro, /root/rectangular_cases; effort setting not exposed.

For the coefficient-extraction morphism

\[
 T_{r,L,b}:\operatorname{Sym}^r(\operatorname{Sym}^bV)
 \longrightarrow
 \operatorname{Sym}^{rL}V\otimes
 \operatorname{Sym}^r(\operatorname{Sym}^{b-L}V),
 \quad
 f\longmapsto[t_1^L\cdots t_r^L]\,
 f(v_1+t_1x,\ldots,v_r+t_rx),
\]

the following are the exact kernels for every finite-dimensional complex \(V\):

\[
 \boxed{\ker T_{3,2,5}=0,}
 \qquad
 \boxed{\ker T_{3,3,8}=S_{(8,8,8)}V,}
 \qquad
 \boxed{\ker T_{5,1,4}=S_{(4,4,4,4,4)}V.}
\]

In the last two formulas the right-hand side denotes the unique embedded Schur summand in the displayed source. It is specified concretely below. Thus it is zero when the ambient dimension is smaller than its number of rows.

## Exact embedded rectangular kernel

In dimension \(r\), the polynomial \(\det(v_1,\ldots,v_r)^b\) has degree \(b\) in each of the \(r\) slots. For even \(b\) it is invariant under slot permutations. It is a nonzero highest-weight vector of weight \((b^r)\). Its source multiplicity is one: the corresponding \(GL_r\)-module is \(\det^b\), and the balanced-weight/permutation realization gives precisely its sign character \(\operatorname{sgn}^b=1\).

For the two pairs \((r,L,b)=(3,3,8)\) and \((5,1,4)\), one has \(rL=b+1\). In a term contributing to \(t_1^L\cdots t_r^L\), exactly \(b+1\) columns of the \(b\) determinant factors are replaced by the common vector \(x\). Some determinant factor receives at least two copies of \(x\), and that term is zero. Hence the entire displayed determinant power lies in the kernel.

For any ambient \(V\) of dimension at least \(r\), choose the first \(r\) basis directions and use the determinant of the corresponding \(r\times r\) coordinate minor. The \(GL(V)\)-span of its \(b\)-th power is the embedded Cartan module \(S_{(b^r)}V\): the polynomial is a nonzero highest-weight vector of that weight, and the source multiplicity is one by the stable Schur-functor multiplicity-space realization. This defines the actual inclusion in the source. Equivariance places its entire span in the kernel.

The selected-minor certificates below prove injectivity on every other source summand, so this explicit inclusion accounts for the complete kernel.

## Complete rank certificates

| \((r,L,b)\) | Source constituents | Source highest-weight dimension | Certified image highest-weight rank | Largest source multiplicity | Independent selected entries |
|---|---:|---:|---:|---:|---:|
| \((3,2,5)\) | 13 | 13 | 13 | 1 | 13 |
| \((3,3,8)\) | 36 | 39 | 38 | 2 | 44 |
| \((5,1,4)\) | 95 | 142 | 141 | 4 | 263 |

The source dimensions in ambient dimensions \(r\) are respectively 1,771; 16,215; and 16,108,764.

The producer small_boundary_candidates.py computes the complete source characters from Newton's recurrence, extracts every Schur multiplicity by the Weyl alternant, and checks the full Weyl-dimension sum against the dimension of the symmetric power. The independent program recheck_small_boundary.py obtains every source multiplicity, including all zeros, by power-sum plethysm expansion and Murnaghan–Nakayama character sums. It checks all 27, 61 and 192 partitions of the respective degrees and permitted lengths.

For each nonrectangular highest weight, the supplied source vectors are signed, normalized Reynolds sums of products of flag minors. Their complete definition is the same one proved in R-015, with \(r\) slots: average all \(r!\) literal slot permutations, collect the determinant signs, divide the integral coefficients by their gcd, and choose the first nonzero coefficient positive. The seeds come from semistandard tableaux of content \((b^r)\). Each seed's row weights and every slot degree are independently verified.

The primary C++ program check_small_boundary.cpp evaluates \(T_{r,L,b}\) by multiplying the exactly linear shifted minors and retaining the exponents \(0\le\deg t_i\le L\). It selects a square matrix of size equal to the full source multiplicity in each nonrectangular block. Every selected determinant is nonzero modulo the prime \(1,000,003\). The rectangular blocks are handled by the explicit polynomial proof above, not by a numerical inference from sampled zeros.

The independent Python program recomputes every selected matrix entry with a separate NumPy Taylor-array implementation, reverses the factor order, generates every Reynolds sum independently, and computes all small and selected determinants by recursive Laplace expansion. The programs agree on all 320 selected entries. They made 40, 183 and 20,402 independent Taylor evaluations respectively. The largest selected matrix has size four, so the Laplace checks are exhaustive exact calculations. Array intermediates are bounded by \(6P^2\), inside the signed 64-bit range.

A nonzero determinant modulo \(P\) proves that the corresponding integer polynomial-image columns are linearly independent over \(\mathbb Q\) and \(\mathbb C\). Thus every nonrectangular highest-weight multiplicity space is injective. Complete reducibility then proves the stated kernels in dimension \(r\).

Finally, the source has only Schur functors of length at most \(r\), by iterated Pieri multiplication of \(r\) one-row representations. The coefficient-extraction map is defined by the same tensor permutations and averages in every dimension. Its Schur-multiplicity matrices are therefore dimension-independent once all source partitions fit, exactly as proved in R-011. This transfers the complete kernel descriptions to every larger \(V\). Naturality under an inclusion handles smaller \(V\).

The data are fully specified in the three files POLARIZATION_R3_L2_B5.selected.gz, POLARIZATION_R3_L3_B8.selected.gz, and POLARIZATION_R5_L1_B4.selected.gz, together with their source and rank TSV tables. SMALL_BOUNDARY_INDEPENDENT_CHECK.tsv is the independent receipt. Decompress the selected files and run recheck_small_boundary.py from any directory to reproduce the independent character and entry checks.

These finite kernels agree with the rectangular obstruction at these actual parameter pairs. No assertion about all remaining boundary parameters is inferred from the calculation.
