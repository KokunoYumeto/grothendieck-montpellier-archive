# Exact finite-normal audit of the stable defect formula

Statement **A-048**. Complete proof review of T047, performed on
21 November 2026 by GPT-6 Astra Pro, run /root/archive_audit;
effort setting not exposed.

**Result: complete proof PASS.** The entire report
work/theta/outer5/stable_defect_cohomology_report.md, D.1–D.17,
and both its evaluator and check program were read. The proof
establishes its actual higher-cohomology isomorphism for every
\(s\ge2,\ k\ge3s-1,\ a=b+x,\ b,x\ge0\), with \(c=2k-s\).
Its stated zeroth-cohomology consequence is the exact Euler
character plus the evaluated correction. This audit gives that
assertion its precise stated scope.

## 1. The directional interpolation maps

The four tangent directions at a frame point form a projective
frame in \(\mathbf P^2\). The two quadrics
\[
f=z_1z_2-z_1z_3,\qquad
g=z_1z_2-z_2z_3
\]
have exactly the four displayed projective zeros and independent
gradients there. Their complete intersection is reduced and has
length four. In particular they form a regular sequence.
For \(r=s-1\), the generators \(f^{r-i}g^i\) and the adjacent
relations \(g e_{i-1}-f e_i\) give the exact complex
\[
0\longrightarrow S(-2r-2)^r
\longrightarrow S(-2r)^{r+1}
\longrightarrow J^r\longrightarrow0.
\]
The proof by successive division modulo \(f\) checks every
syzygy. Injectivity on the left follows in order from the
coordinates, since \(f\) and \(g\) are nonzero divisors.
After sheafification and twist \(d\ge2r\), the left summands
have twist at least \(-2\). Projective-plane cohomology proves
that evaluation onto all order-\(r\) directional jets is
surjective. This is the literal polynomial-evaluation map.

The independent calculation also formed those matrices directly
in affine charts for the four direction points. For every
\(1\le r\le8\), their ranks at \(d=2r\) are the full
\(4\binom{r+1}{2}\) row ranks. At \(d=2r-1\), their ranks are
the full column ranks, giving the predicted failure to cover
all jets at that lower degree. Each rank is witnessed by a
maximal nonzero minor modulo \(1000003\), and therefore proves
the same maximal rank over \(\mathbf Q\). These sixteen checks
are additional computations; the displayed resolution proves
the interpolation statement for every \(r\).

## 2. Finite normal restriction as an exact morphism

Fix a pair \(e\), use the stabilizer splitting \(E=P_e\oplus W_e\),
and set \(r=s-1\). The complement of \(\mathbf P(W_e)\) in
\(\mathbf P(E)\) is the total space of
\(W_e\otimes\mathcal O_{\mathbf P(P_e)}(1)\).
The image \(\mathcal B^r_{e,k}(c)\) of the ideal sheaf in the
order-\(r\) normal quotient is, as a module on the base line,
\[
\bigoplus_{0\le j<r}
\operatorname{Sym}^jW_e^*
\otimes (XY)^{k-j}\mathcal O(c-j-2(k-j)).
\tag{SD1}
\]
The exponent \(k-j\) is exactly the remaining endpoint
Taylor order. The other three frame points lie off this line
and impose no condition on its finite normal sheaf.

For precision, define a finite morphism of truncated normal
neighborhoods
\[
t:\operatorname{Tot}_{<r}(W_e\otimes\mathcal O(-1))
\longrightarrow
\operatorname{Tot}_{<r}(W_e\otimes\mathcal O(1)),
\qquad w=XYv.
\tag{SD2}
\]
The notation means that all monomials of normal degree at
least \(r\) have been set to zero. The map is finite because
both structure algebras are finite over the base line.
The coefficient map
\[
F\longmapsto (XY)^{-k}F(X,Y,XYv)
\]
defines an isomorphism
\[
\mathcal B^r_{e,k}(c)\simeq t_*\mathcal O(-s)
\tag{SD3}
\]
of modules for the original normal-neighborhood algebra.
Indeed each normal degree \(j\) in (SD1) contains
\((XY)^{k-j}\); substitution contributes \((XY)^j\),
and cancellation leaves an ordinary regular coefficient.
The inverse multiplies that coefficient by
\((XY)^{k-j}\). The original normal coordinate acts on the
right side by \(XYv\). This proves (SD3) at the endpoints
without inverting \(X\) or \(Y\) in their local rings.

The projection formula consequently gives the actual comparison
\[
\mathcal B^r_{e,k}(c)\otimes S_{(a,b)}Q
\simeq
t_*\bigl(\mathcal O(-s)\otimes S_{(a,b)}t^*Q\bigr).
\tag{SD4}
\]
This identifies exactly the bundle to which the report's
unipotent automorphism is applied.

Write \(p=X\ell_i+Y\ell_j\). On the source of (SD2), put
\[
T=I-\frac12\bigl((Yv)\otimes X^*+(Xv)\otimes Y^*\bigr).
\]
The products \(Xv,Yv\) are global regular \(W_e\)-valued
functions: their two homogeneous degrees cancel. Its
correction has square zero, since both coordinate
functionals vanish on \(W_e\). Thus \(T\) is invertible
with the displayed sign-reversed inverse, and
\[
T(p+XYv)=p.
\]
It is symmetric under endpoint interchange and equivariant
under the other three letters. The induced actual quotient
bundle isomorphism is
\[
t^*Q\simeq
(\det P_e)\mathcal O(1)\oplus W_e.
\tag{SD5}
\]
Equations (SD2)–(SD5) verify all normal couplings, including
the original linear-form differential.

## 3. The global cohomology comparison

For both twists \(C=c\) and \(C=c-1\), the report's binary
overlap functionals compare the coefficients of exponents
\(t\) and \(C-j-t\), with
\[
C-k+1\le t\le k-j-1.
\]
For a normal monomial of degree \(j<r\), its point Taylor
degree is \(t+j\). In the source it is at least \(k-s\),
which is at least \(2s-1\) in the stated range and hence
at least \(2r\). At each fixed total Taylor degree the
leading functionals are exactly a subset of the directional
jets from §1. Chart changes are triangular in the total
degree, with invertible leading coordinate changes.
Taking a largest degree in a proposed relation and descending
therefore proves that every overlap coefficient vanishes.
This proves surjectivity of both scalar restriction maps.

The target dimension is established by the already verified
Cox grading from A-028. Its six binary weights are
\((k-s)^5,k-3s\). For \(k\ge3s\), the binary weight difference is
\[
[z^{2k-s}]
\frac{(1-z^{k-s+1})^5}{(1-z)^4}
=
\binom{2k-s+3}{3}
-5\binom{k+2}{3}
+10\binom{s+1}{3}.
\]
Terms of numerator order at least three have negative
residual degree. At \(k=3s-1\), the sixth binary weight is
\(-1\); the component is zero. The displayed coefficient
also vanishes by the equality of binary weights \(-1\)
and \(1\), or by direct substitution into the binomial
expression. Hence the endpoint has the same formula.

Subtracting the fat-point length proves
\[
h^1(I^k(c))=10\binom{s+1}{3}.
\]
Each normal image has first-cohomology dimension
\[
\sum_{j=0}^{s-2}(j+1)(s-j-1)=\binom{s+1}{3}.
\]
The target scalar restriction is therefore an isomorphism
and the preceding source restriction is onto. The two
maps form the commuting diagram with the actual
locally split Schur complex. Its scalar twists have no
\(H^2,H^3\), so the cokernel on first cohomology gives
the full Schur-bundle first cohomology, and all groups
of degree at least two vanish. This verifies the
global-to-finite-normal comparison in full.

## 4. The exact summands and positive count

Applying the one-line branching maps to (SD5) removes a
horizontal strip of row lengths \(u,v\), with
\(0\le u\le x\), \(0\le v\le b\). Combining these maps
with (SD4) and the line Čech pairing gives
\[
\bigoplus_{\substack{j,u,v\ge0\\u\le x,\ v\le b\\j+u+v\le s-2}}
(\det P_e)^{u+v+1}
\operatorname{Sym}^{s-j-u-v-2}P_e
\otimes\operatorname{Sym}^jW_e^*
\otimes S_{(b+x-u,b-v)}W_e.
\tag{SD6}
\]
The factor \(\det P_e\) comes from
\(H^1(\mathcal O(-m))=\operatorname{Sym}^{m-2}P_e\otimes\det P_e\).
The ten pairs are transitively permuted, so their sum
is exactly induction from \(S_2\times S_3\).

The nine-variable inequalities D.17 were checked against
every factor in (SD6). The exponent \(u+v+1+p\) records the
endpoint sign. The exponent \(b-v+h\) records the
complementary determinant sign after the actual
Clebsch–Gordan map. The final equation
\[
2z_2+3z_3=j+x-u+v-2h-e
\]
counts precisely the three possible symmetric-power
multiplicity series on the two-dimensional standard
representation. The fixed horizontal/vertical strip
test gives the restriction multiplicity one or zero.
Each parity slack is uniquely determined and nonnegative
when its parity is correct, so it introduces no
extra multiplicity. All coordinates have the displayed
linear bounds, proving boundedness.

The independent program check_stable_defect_independent.py
uses literal two-by-two matrices for all twelve elements
of \(S_2\times S_3\). It computes the two-row factors by
Jacobi–Trudi and the outer restrictions by independent
Murnaghan–Nakayama characters. Frobenius reciprocity
then computes each desired multiplicity directly from
the twelve group elements, without Clebsch–Gordan
decomposition or Pieri on that comparison side.

All 2,744 tested correction coefficients agree.
All forty-two restriction-character identities agree.
The exact tag counts are
\[
2,\ 8,\ 10,\ 12,\ 10,\ 8,\ 2.
\]
An independent Cartesian enumeration of the exported
constraint matrices also agrees in forty-two cases,
with all 258 lattice points matching the lazy witnesses.
The receipt STABLE_DEFECT_INDEPENDENT_RECEIPT.json records
these checks and the sixteen directional-jet ranks.

## 5. Primary cohomology locator

Stacks Project, §30.8, Lemmas 30.8.1 and 30.8.2, was
opened and both complete proofs were read. The first
proof decomposes the actual Čech complex into monomial
weights and contracts the intermediate pieces. The
second identifies multiplication on top cohomology
with the contragredient polynomial multiplication
under the coefficient pairing. These give exactly
the projective-plane vanishing and the line
contraction used above.
Source: https://stacks.math.columbia.edu/tag/01XS .

The missing tensor-product backslash in the original
D.5 display was reported to the author and corrected.
The evaluator description was also updated to the
proved maximum of twelve retained tags.

