# Rectangular hooks as ordinary cohomology of a split special linear group

**Status:** a concise application of a known rectangular hook formula and a displayed known motivic decomposition. This is not a new formula for Kronecker coefficients, and no identification with the nonstandard algebra, its canonical basis, or its tensor paths is asserted.

## 1. The actual Weil object

Let \(n,d\geq1\), \(N=nd\), and \(m=\min(n,d)\). For \(0\leq k<N\), put
\[
g_k=g((N-k,1^k),(d^n),(d^n)).
\]
Ikenmeyer--Panova, Proposition 6.4, gives the known identity
\[
\sum_{k=0}^{N-1}g_k t^k=\prod_{i=2}^{m}(1+t^{2i-1}).
\tag{H1}
\]
Its statement and proof are present in the supplied source `sources/LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/main.tex`, in the proposition immediately following the paragraph beginning “Here we give the proof of Theorem…”, and specifically the displayed generating function following the definition of \(g_k(d,n)\).

For a finite field \(\mathbb F_q\) and a prime \(\ell\nmid q\), take the ordinary split group scheme \(G=\mathrm{SL}_{m,\mathbb F_q}\). Its cohomology has the following actual decomposition as a Weil representation:
\[
H^k(G_{\overline{\mathbb F}_q},\mathbb Q_\ell)
\simeq
\bigoplus_{\substack{I\subseteq\{2,\ldots,m\}\\
                 \sum_{i\in I}(2i-1)=k}}
\mathbb Q_\ell\left(-\sum_{i\in I}i\right).
\tag{H2}
\]
Consequently, (H1) identifies \(g_k\) with the dimension of this particular geometric Weil object. This works for arbitrary rectangle heights and widths; the third partition is a hook. The group is affine, so this statement concerns ordinary cohomology, not a claim that a smooth projective variety has these odd Betti numbers.

## 2. Exact motivic input and deduction

The following formula is printed in Alexander S. Merkurjev, *Motivic decomposition of certain special linear groups*, Introduction, equation **(1.1), author PDF p. 1**:
\[
M(\mathrm{SL}_m)_{\mathbb Q}
\simeq
\bigoplus_{j=0}^{m-1}
\operatorname{Sym}^j\!\left(
 \mathbb Q(2)[3]\oplus\mathbb Q(3)[5]\oplus\cdots
 \oplus\mathbb Q(m)[2m-1]\right).
\tag{H3}
\]
The paper's base field is perfect. Its text attributes this known split-group formula to Biglari. The primary PDF used is <https://www.math.uni-bielefeld.de/LAG/man/530.pdf>, web reference `turn529644831view0` (also `turn912130151view0` in the earlier session). **The formula itself and perfect-field context were read; Biglari's original proof was not obtained or certified.** This is a citation of a precise displayed formula in a primary research paper, with its attribution preserved.

Here is the deduction from (H3). Each listed summand has odd cohomological shift. Under the symmetry in the rational derived motivic category, its transposition is therefore minus the identity. Its second and higher symmetric powers vanish. Expanding the symmetric powers of the direct sum in (H3) thus selects subsets, giving
\[
M(\mathrm{SL}_m)_{\mathbb Q}
\simeq \bigoplus_{I\subseteq\{2,\ldots,m\}}
\mathbb Q\!\left(s_I\right)[2s_I-|I|],
\qquad s_I=\sum_{i\in I}i.
\tag{H4}
\]
Ordinary cohomological \(\ell\)-adic realization of the summand
\(\mathbb Q(s)[a]\) gives \(\mathbb Q_\ell(-s)\) in degree \(a\). Applying that convention to (H4) gives (H2). In particular the splitting is defined over the finite field, so geometric Frobenius is the scalar \(q^{s_I}\) on the indicated summand. This is stronger than an inference from purity alone: the displayed motive supplies the Tate decomposition.

For an independently checked motivic-cohomology locator, Ben Williams, *The \(\mathbb G_m\)-equivariant motivic cohomology of Stiefel varieties*, **Theorem 2.7 and Corollary 2.7.1, printed p. 767**, give generator bidegrees \((2i-1,i)\) and the corresponding Stiefel subalgebras. Official PDF: <https://msp.org/agt/2013/13-2/agt-v13-n2-p03-p.pdf>, refs `turn575024295view0`, `turn906555825view1`, `turn906555825view3`. This is corroboration of the degrees, not a replacement of the actual-motive input (H3).

## 3. Fixed degree need not be pure

Every summand in (H2) is pure Tate, but its weight is
\[
2s_I=k+|I|.
\]
Subsets with the same degree \(k\) may have different cardinalities. For \(m=8\) and \(k=15\), exactly two subsets occur:
\[
I=\{8\},\qquad I=\{2,3,4\}.
\]
Thus
\[
H^{15}(\mathrm{SL}_{8,\overline{\mathbb F}_q},\mathbb Q_\ell)
\simeq \mathbb Q_\ell(-8)\oplus\mathbb Q_\ell(-9),
\]
with weights 16 and 18 and extension traces \(q^{8a}+q^{9a}\). The corresponding hook coefficient equals two for every rectangle with minimum side eight. A single Tate twist cannot make these two weights equal. There is no conflict with F20: its pure Satake multiplicity motive is a different geometric realization of the same integer.

## 4. Exact scope of the dictionary

This supplies a concrete split group scheme and ordinary scheme Frobenius for the entire rectangular hook family. The applicable classical framework is group schemes (SGA 3) together with rational motives and their \(\ell\)-adic realization. It does not turn reduction of a noncommutative bialgebra into a scheme Frobenius, does not identify the nonstandard canonical basis, and does not remove the all-extension comparison hypothesis in F26. It also does not claim the manuscript leaves contain (H1)--(H4): any archival connection is only the previously audited framework connection to motives, projectors, and operations.

**Author check:** the subset expansion, Tate sign convention, hook index range, and \(m=8,k=15\) example were checked directly. Known inputs (H1) and (H3) are cited, not claimed as reproved. No source beyond the exact inspected primary locations is represented as verified.


## 5. Stronger directly inspected theorem locator for the generated fragment

On reopening the primary Merkurjev PDF, I inspected Section5, Proposition5.2 and Corollary5.3 on printed p.7 and Corollary5.5 on printed p.8. Corollary5.5 directly states the canonical Tate-motive decomposition of split SL_n. Its index sequence 1≤j1<...<ja≤n−1 contributes 1(d+a)[2d+a], with d the sum of the indices. Reindexing i=j+1 gives exactly (H4). This theorem supplies the actual split decomposition over the stated perfect-field base, without relying solely on the introductory Biglari attribution. The general theorem is a known cited input, not newly reproved here. Primary URL remains https://www.math.uni-bielefeld.de/LAG/man/530.pdf ; newly reopened source reference turn949488080view0. The generated finding_F33.tex uses this stronger precise locator.
