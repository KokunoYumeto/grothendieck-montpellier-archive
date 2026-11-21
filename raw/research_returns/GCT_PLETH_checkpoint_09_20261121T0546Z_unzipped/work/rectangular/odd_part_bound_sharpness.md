# Sharpness of the odd-part occupancy constant

## R-051. One actual centered restriction kernel

Set
\[
\nu=(6,5,4,3,2,1),\qquad D=21,\quad t=6.
\tag{OS.1}
\]
Let \(U\) have dimension at least six, and use the centered
power-sum morphism \(\mathsf p_{12}\) of R-046 TM.6, restricted
to degree21. Then
\[
\boxed{[S_\nu U:\ker\mathsf p_{12}]=1,\qquad
[S_\nu U:\ker\mathsf p_{13}]=0.}
\tag{OS.2}
\]
The source can be restricted to moment generators of degrees2–6,
since its \(\nu\)-component lies there by the actual Pieri maps
in TM.7. Thus (OS.2) is a statement about specified finite algebra
morphisms, not only a difference of stable characters.

Here the odd-part count is three and the largest-part parity is zero.
The bound of R-049 is
\(\lfloor(21+6-\lceil3/3\rceil)/2\rfloor=13\).
Every positive replacement constant smaller than three would give
a bound at most12 on this tail, where the displayed actual map has
a nonzero kernel. Consequently the constant three is sharp for
this uniform centered power-sum faithfulness bound.
No assertion about a kernel of the canonical Foulkes–Howe map is
deduced from (OS.2); its factorization also contains the actual
independent-row image, as specified in HM.17.

## 1. The actual restriction sequence

Take \(T=\mathbb Q^6\), \(S=21\), and \(s=12\). Let
\(q:W_S\to W_s\) be the transpose of zero-padding, and extend it
by the averaged-extra-row map \(\widetilde q:E_S\to E_s\) of
OO.3. With the literal mean-line identifications,
\[
C_j=(\Lambda(E_j\otimes T))^{S_j}
=\Lambda T\otimes B_j,
\qquad B_j=(\Lambda(W_j\otimes T))^{S_j},
\]
the induced restriction is exactly
\(1_{\Lambda T}\otimes q_B\), by OO.4–OO.6.
Both restrictions are surjective. Therefore their actual kernels
satisfy
\[
\ker(C_S\to C_s)=\Lambda T\otimes K,
\qquad K=\ker(B_S\to B_s).
\tag{OS.3}
\]
The omitted occupied-row modules in OO.8 give the character of the
left side; they need not be its literal summands for this map.

At scalar degrees at most19 there is no omitted row tuple, because
its occupancy is at most \(\lfloor(19+6)/2\rfloor=12\).
Thus \(K_e=0\) for \(e\le19\), by (OS.3) degree induction.
At degree20 the only omitted tuple has
\(e_1=6,e_2=7\), and occupancy13. Consequently
\[
[K_{20}]=[\det T\otimes\operatorname{Sym}^7(\Lambda^2T)].
\tag{OS.4}
\]
At degree21 the only omitted tuples are
\((e_1,e_2,e_3)=(5,8,0)\) and \((6,6,1)\), both of
occupancy13. These follow directly from
\(21+6-2\cdot13=1=(6-e_1)+\sum_{i\ge3}(i-2)e_i\).
Equation (OS.3) in degree21 now gives the exact character identity
\[
\begin{split}
[K_{21}]={}&[\Lambda^5T\otimes\operatorname{Sym}^8(\Lambda^2T)]\\
&+[\det T\otimes\operatorname{Sym}^6(\Lambda^2T)\otimes\Lambda^3T]\\
&-[T\otimes\det T\otimes\operatorname{Sym}^7(\Lambda^2T)].
\end{split}
\tag{OS.5}
\]
This is obtained from actual kernels and their tensor decomposition.

## 2. The exact Schur multiplicity

The paired-row decomposition OI.8 is multiplicity free; its actual
highest vectors are the products of the leading Pfaffians. Every
constituent has alternating highest-weight sum zero. The first and
last terms of (OS.5) have alternating sum at most one, by the
displayed exterior pairing \(\Lambda^5T=\det T\otimes T^*\)
and one-box dual or ordinary Pieri map. The desired weight
\(\gamma=\nu'=(6,5,4,3,2,1)\) has alternating sum three,
so it occurs in neither of those terms.

In the middle term, remove the determinant character. The remaining
weight is \((5,4,3,2,1,0)\). The only vertical three-strip removal
that leaves equal consecutive pairs removes boxes in rows1,3,5,
and gives
\[
\mu=(4,4,2,2,0,0).
\tag{OS.6}
\]
This paired weight occurs once in
\(\operatorname{Sym}^6(\Lambda^2T)\). With
\(q_{ij}=e_i\wedge e_j\), its highest vector is the product
of the squared leading Pfaffians of sizes2 and4:
\[
q_{12}^{2}(q_{12}q_{34}-q_{13}q_{24}+q_{14}q_{23})^{2}.
\]
The exterior Pieri insertion, followed by the same rational Young
projector as in OO.11, gives the single copy indexed by this vertical
strip. The coefficient is one by the standard vertical-strip
tableau construction; its map is the column insertion into the
specified three rows. Thus (OS.5) gives
\[
[S_\gamma T:K_{21}]=1.
\tag{OS.7}
\]

The ordinary and skew-Cauchy multiplicity maps of \(q\) are the same
actual Schur morphism \(S_\nu(q)\), since the Young projectors
commute with \(q^{\otimes21}\). At \(S=21\), the ordinary
power-sum map is an isomorphism through degree21 by the explicit
row-orbit triangularity in TM.6. On every generator,
\(\mathsf p_s=\operatorname{Sym}(q\otimes1)\mathsf p_S\).
Therefore (OS.7) is exactly the first equality in (OS.2).
At \(s=13\), all occupied rows are present in degree21, and the
same kernel and Cauchy argument proves its second equality.

## 3. Exact finite character receipt and scope

The separate script verify_odd_part_bound_sharpness.py uses the
literal cycle eigenvalues on \(W_s\), constructs complete symmetric
traces, and evaluates the six-by-six Jacobi–Trudi determinant with
fraction-free integer elimination. Its rational class average gives
\[
\begin{array}{c|rrrrr}
s&11&12&13&14&21\\\hline
\dim(S_\nu W_s)^{S_s}&318&331&332&332&332.
\end{array}
\tag{OS.8}
\]
Every value is recorded in ODD_PART_BOUND_SHARPNESS_CHECK.tsv.
The full proof of the one-dimensional kernel is (OS.3)–(OS.7);
the finite calculation checks it independently.
All maps are rational and natural in \(U\), so (OS.2) extends to
every characteristic-zero field in the stated dimensions.
