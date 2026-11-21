# F48 supplement: unlabeled spectral retuning excludes the full actual pure centralizer

Author: /root/gct_statements, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC. This is a separate extension to the already reviewed agent_tensor_weil_comparison.md, not an unnoticed change to that report. Parent has been notified. A fresh mathematical review is requested.

The rational labeled-branch theorem can be strengthened in pure weight zero without choosing labels or diagonalizing a parameter-dependent family. The resulting obstruction applies to the actual generic rank-three algebra of F19/F46.

## S1. Convergent unit-circle power sums

**Lemma.** Let alpha_1,...,alpha_N be nonzero complex numbers of modulus one, counted with positive integer multiplicities. If
\[
u_n=\sum_{j=1}^N\alpha_j^n
\]
converges as n tends to infinity, then every alpha_j equals one.

**Proof.** Group equal roots alpha with multiplicity m_alpha>0. The first difference tends to zero and is
\[
u_{n+1}-u_n=\sum_\alpha
  m_\alpha(\alpha-1)\alpha^n .
\]
For a finite set of distinct unit-circle roots, its Cesàro mean square tends to
\[
\sum_\alpha m_\alpha^2|\alpha-1|^2.
\]
Indeed a diagonal pair contributes its squared coefficient, while for alpha different from beta the average of (alpha conjugate(beta))^n tends to zero by the finite geometric-sum formula. Since the first difference tends to zero, its mean square tends to zero. Every nonnegative summand therefore vanishes. QED.

The positivity of the multiplicities is relevant: these are actual matrix eigenvalues. Virtual traces with exact cancellations do not satisfy this conclusion for the invisible eigenvalues.

## S2. Rational spectral retuning forces unipotence

**Theorem.** Fix a real b>1. Let F(v) be an invertible N-by-N matrix over C(v), regular and invertible at b and at all sufficiently large b^n. Suppose:

1. every eigenvalue of F(b) has modulus one;
2. for every sufficiently large integer n,
\[
\operatorname{Spec}F(b^n)
   =\operatorname{Spec}(F(b)^n)
\tag{S1}
\]
as multisets, with algebraic multiplicities.

Then every eigenvalue of F(b) equals one, and
\[
\det(TI-F(v))=(T-1)^N
\tag{S2}
\]
as a rational-function identity. Thus F(v) is unipotent over C(v).

**Proof.** Let t(v)=Tr(F(v)), a rational function. By (S1),
\[
t(b^n)=\sum_{j=1}^N\alpha_j^n,
\]
where the alpha_j are the unit-circle eigenvalues of F(b). The right side is bounded. A rational function bounded along b^n has a finite limit at infinity: write its leading Laurent term a v^m; a positive exponent m would make its values unbounded, whereas m=0 or m<0 gives a finite limit. Therefore this power sum converges. S1 proves that all alpha_j=1.

Consequently each characteristic polynomial of F(b^n), for all sufficiently large n, is (T-1)^N. Each of its coefficients is a rational function of v and agrees with the corresponding constant at infinitely many distinct v=b^n. Every coefficient is therefore that constant identically. This proves (S2). The Cayley–Hamilton identity gives (F(v)-I)^N=0. QED.

Only the trace rationality and a finite limit at infinity are needed for the conclusion about F(b). Rationality of the whole characteristic polynomial supplies the family identity (S2). No labeling of eigenvalues, generic diagonalizability or absence of collisions was assumed. Jordan blocks are allowed throughout.

## S3. The actual rank-three centralizer cannot satisfy these hypotheses

At b>1 put delta=b+b^{-1}, D=delta squared. The actual nonstandard rank-three algebra of F19 has
\[
A_b\simeq E\times E\times M_2(E)\times M_2(E),
\tag{S3}
\]
over its splitting coefficient field E of characteristic zero. This is because D>4, hence
\[
\Delta=(D-1)(D-4)/D^2\ne0,
\]
and the two center branches split. Thus A_b is semisimple and is not simple. This is the actual algebra, with its four blocks, not merely a numerical dimension comparison.

**Corollary.** No finite rational matrix family of any auxiliary rank can satisfy (S1), be pure of weight zero at b, and have
\[
\operatorname{End}_{F(b)}(E^N)\simeq A_b
\tag{S4}
\]
as its full Frobenius centralizer.

**Proof.** Base change to C through a coefficient embedding if necessary. Theorem S2 makes F(b) unipotent, so N_0=F(b)-I is nilpotent. It is also a central element of End_{F(b)}(E^N): every member of that centralizer commutes with F(b), hence with N_0. A semisimple finite-dimensional algebra has reduced center, so a central nilpotent in it must be zero. Therefore F(b)=I. Its full centralizer is then M_N(E), a simple algebra, contradicting (S3). This argument is unchanged after a splitting scalar extension. QED.

The obstruction already holds at the generic semisimple parameter b>1; it is independent of the collision radical and of F47's finite based rigid-category obstruction. It excludes rational replacements of the whole F46 full-centralizer model with the stated extension rule, including replacements that permute eigenvalues, use a different auxiliary rank, or retain Jordan blocks. It does not exclude faithful actions of A_b inside a larger Frobenius centralizer. The coherent fixed-parameter constructions of F46 and the faithful tensor constructions of F48 therefore remain valid.

For the convention v=Q^{-n/2}, replace F(v) by F(v^{-1}) and apply the same theorem with b=Q^{1/2}. The conclusion is identical.

**Fixed single-weight extension.** More generally suppose b=Q^{1/2}, and F(b) is pure of one fixed integral weight w, so every complex eigenvalue has modulus b^w. Set
\[
G(v)=v^{-w}F(v).
\]
This is again a rational invertible matrix family and has the identical full centralizer at every regular parameter. Its spectrum at b has modulus one. Moreover (S1) is preserved, since
\[
\operatorname{Spec}G(b^n)
 =b^{-nw}\operatorname{Spec}F(b^n)
 =\operatorname{Spec}\bigl((b^{-w}F(b))^n\bigr).
\]
The preceding corollary applies to G. Thus no rational finite matrix family of a fixed single integral pure weight, of any auxiliary rank, can satisfy all-extension spectral retuning and recover the actual nonsimple semisimple A_b as its full Frobenius centralizer. For v=Q^{-1/2} the normalization is v^w F(v), equivalently the same normalization after v is replaced by its inverse. This extension requires a single fixed weight and integral exponent; it makes no classification claim for mixed weights or multivalued algebraic normalizations.

## S4. A stronger matrix law has an exact classification

The spectral condition (S1) does not itself force F(v)=I: nonconstant unipotent families have constant spectrum. If a common fixed rational basis is part of the comparison, one can instead impose the stronger equality
\[
F(b^n)=F(b)^n
\tag{S5}
\]
of matrices for every sufficiently large n. In this case there is a complete elementary classification even without the purity assumption.

**Theorem.** Under (S5), there is a constant invertible complex matrix S and integers m_1,...,m_N such that
\[
F(v)=S\,\operatorname{diag}(v^{m_1},...,v^{m_N})\,S^{-1}.
\tag{S6}
\]
Conversely every family (S6) obeys (S5). In particular pure weight zero at b forces F(v)=I.

**Proof.** Choose a constant complex Jordan basis S for F(b) and put G(v)=S^{-1}F(v)S. Every diagonal entry g_j(v) is rational and, by (S5), satisfies
\[
g_j(b^n)=\alpha_j^n
\]
for the corresponding nonzero eigenvalue alpha_j of F(b). The scalar argument of F48 T10 applies directly: the ratio of consecutive values tends to b^{m_j}, where m_j is the order at infinity of g_j. Hence alpha_j=b^{m_j}; infinitely many evaluations then give g_j(v)=v^{m_j}.

Suppose a Jordan block had length at least two. Its first superdiagonal entry h(v) would satisfy
\[
h(b^n)=n\alpha^{n-1}.
\]
The ratio of consecutive values tends to alpha=b^m. Thus the leading Laurent exponent of h is the same integer m. But h(b^n)/b^{mn} tends to its finite leading coefficient, whereas the displayed expression equals n/alpha and is unbounded. This is impossible. Every Jordan block therefore has length one.

In the now diagonal constant basis, all off-diagonal entries of G(v) vanish at infinitely many b^n and hence vanish rationally. The diagonal identities give (S6). Its converse is direct. If every eigenvalue at b has modulus one, b^{m_j} has modulus one only for m_j=0. QED.

The stronger matrix condition depends on a fixed rational trivialization. Parameter-dependent changes of basis, mere conjugacy at each extension, or an isomorphism chosen separately for each n do not imply (S5), and are not excluded by its classification. The spectral obstruction S3 needs none of this additional fixed-basis hypothesis.

## S5. Verification and relation to the main question

These are elementary exact proofs, not experiments or a formal proof-kernel certificate. They use finite matrix spectra with their genuine positive multiplicities, the known actual split rank-three algebra, and rational dependence on the quantum parameter. The eigenvalue equalities are explicit comparison assumptions; they are not inferred from ordinary fixed-q purity.

The new gate is consequently precise. A fixed-parameter pure tensor action exists, but an exact full-centralizer realization of the actual semisimple nonstandard algebra cannot at the same time obey rational all-extension spectral retuning in one fixed integral pure weight. A successful geometric route must change one of those specifically stated requirements, or supply additional structures whose relevant endomorphisms are a proper subalgebra of the full point-Weil centralizer. This leaves geometric correspondences, extra actions, nonrational comparison data, mixed weights and the F24 sign-trace conditions open rather than silently ruling them out.
