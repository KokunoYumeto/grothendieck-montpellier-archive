# Canonical surjectivity from the complete finite degree-five kernels

## R-032. Five explicit families below the full degree-five base

Let \(a\ge6\), put \(C_a=\binom a2-10\), and use the
normalized canonical map

\[
h_{b,a}:\operatorname{Sym}^b(\operatorname{Sym}^aV)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^bV)
\tag{FK.1}
\]

over a characteristic-zero field. For a partition \(\lambda\),
write \(\lambda'_2=\#\{i:\lambda_i\ge2\}\), with missing
parts zero. Every target \(\lambda\)-isotypic component is reached
in each of the following unconditional parameter families:

\[
\boxed{
\begin{gathered}
1\le t\le4,\qquad b=C_a+t,\qquad\lambda\vdash ab,\\
\lambda_2\le t,\qquad \lambda_2+\lambda'_2\le t+2;
\end{gathered}}
\tag{FK.2}
\]

and

\[
\boxed{
\begin{gathered}
b=C_a+5=\binom a2-5,\qquad\lambda\vdash ab,\qquad\lambda_2\le5,\\
\lambda_2\le4\quad\text{or}\quad\lambda_3\le3
\quad\text{or}\quad\lambda_4\le2\quad\text{or}\quad\lambda_5=0.
\end{gathered}}
\tag{FK.3}
\]

These assertions retain every target multiplicity and every
dimension. A target shape with more than \(a\) rows is zero by
the symmetric-power inclusion and Pieri rule, so it causes no
exception. The full degree-five base in R-024 starts at
\(b=C_a+6\); (FK.2)–(FK.3) use its five preceding integer
degrees, with their complete finite lower kernels. At the fifth
degree, (FK.3) contains the earlier \(\lambda_2\le4\) result
and adds the displayed parts of the \(\lambda_2=5\) band.

The proof gives an actual injection of the remaining annihilator
into a finite sum of explicit Pieri modules, stated in (FK.10).
It also gives the positive lattice-point upper bound (FK.11) for
every remaining cokernel in these second-row bands. No historical
novelty is asserted for these consequences.

## 1. Exact lower kernels and their minimal tails

Put

\[
\mathcal K_{s,d}(W)=\ker h_{s,d}(W),\qquad
\mathcal K_{s,d}^{\le t}=
\bigoplus_{\eta_2\le t}(\mathcal K_{s,d})_\eta.
\tag{FK.4}
\]

The exact tensor-pairing identity \(h_{d,s}(V)^*=h_{s,d}(V^*)\)
in R-024 (P.6), also proved with scalar one in R-031 (OF.6),
identifies this kernel with the image annihilator of (FK.1).
The polynomial isotypic notation in (FK.4) includes complete
multiplicity spaces.

R-031 gives the complete multiplicities of
\(\mathcal K_{5,t}\) at \(1\le t\le5\). For \(t\le4\)
they are \(a_{5,t}^\mu-a_{t,5}^\mu\), from actual injectivity
of the transpose canonical map. At \(t=5\) they are the eight
published Cheung–Ikenmeyer–Mkrtchyan kernel summands, each once.
Restricting to \(\mu_2\le t\) yields respectively
\(0,3,4,19,2\) distinct summands. The complete 28-row table is
included at the end of this report; the sole multiplicity two is
\(\mu=(10,4,4,2)\) at \(t=4\).

For each surviving \(\mu\), remove its first row and pad the
tail to four coordinates. The componentwise minimal tails are

\[
\begin{array}{c|l}
t&\text{minimal tails}\\\hline
1&\varnothing\\
2&(2,2,0,0)\\
3&(3,2,0,0),\ (2,2,2,0)\\
4&(4,2,0,0),\ (3,2,2,0),\ (2,2,2,2)\\
5&(5,4,3,1).
\end{array}
\tag{FK.5}
\]

The finite arithmetic input here is exhaustive: R-031 independently
computed both characters for every partition of size \(5t\) and
length at most five at \(1\le t\le4\), using both literal
Murnaghan–Nakayama and a monomial-multiset/Weyl-alternant extraction.
The archive agent independently reconstructed every coefficient by
the G-027 restriction complex. The executable
`verify_finite_base_tail_ranges.py` extracts exactly the nonzero
differences in the stated second-row bands, verifies their minimal
tail antichains, and checks the explicit tail conditions in all
251 sorted bounded four-tuples. The general inequalities below
are proved directly and do not depend on sampling an unbounded
parameter. The exact input and receipt are
`FINITE_BASE_KERNELS.tsv` and `FINITE_BASE_TAIL_CHECK.tsv`.

## 2. The actual iterated annihilator injection

For \(r\ge5\), set \(C_5=0\), \(C_{r+1}=C_r+r\),
and \(b_s=C_s+t\). Thus \(b_{r+1}-r=b_r\ge t\ge1\).
For the symmetric \((r+1)\)-slot space, let

\[
\delta(w_0\cdots w_r)=\frac1{r+1}
\sum_i\left(\prod_{j\ne i}w_j\right)\otimes w_i,
\qquad
T_{r,r,b}f=[z_1^r\cdots z_r^r]
 f(v_1+z_1x,\ldots,v_r+z_rx).
\tag{FK.6}
\]

Multiplication is a left inverse of \(\delta\). The normalized
map \(\Theta_{r+1,b}=(T_{r,r,b}\otimes1)\delta\) has the
following actual restriction, proved in R-024 (P.11)–(P.16):

\[
\Theta_{r+1,b}:\mathcal K_{r+1,b}(W)
\longrightarrow
\operatorname{Sym}^{r^2}W\otimes
\mathcal K_{r,b-r}(W)\otimes\operatorname{Sym}^{b}W.
\tag{FK.7}
\]

Here is the exact kernel-membership argument. Represent \(F\)
by its symmetric \((r+1)\)-linear form \(\mathcal A_F\) on
\(\operatorname{Sym}^b V\). For a product \(Q\) of \(b-r\)
linear factors, the form \((x^r+c y^r)Q\) splits into \(b\)
linear factors over \(\mathbb C\). The coefficient of \(c\)
in the defining diagonal vanishing, divided by \(r+1\), is
\(\mathcal A_F(x^rQ,\ldots,x^rQ,y^rQ)=0\).
Apply the \(b-r\) ordinary directional derivatives corresponding
to the factors of \(Q\) to
\(\mathcal A_F(x^rQ,\ldots,x^rQ,y^b)\). The result is
\(b!/r!\) times that zero expression. Before the \(i\)-th
derivative the degrees in its two exchanged vector variables are
\(b-i+1,r\), whose difference is \(b-r-i+1\ge1\).
The one-step \(GL_2\) string calculation in R-024 (P.14)
makes each such derivative injective. Removing them successively
shows \(\mathcal A_F(x^rQ,\ldots,x^rQ,y^b)=0\).
Thus the middle \(r\)-linear form lies in the stated lower
canonical kernel. Its actual coefficient is

\[
\Theta F(v_1,\ldots,v_r;x,y)=
\binom br^r\mathcal A_F
 (x^rv_1^{b-r},\ldots,x^rv_r^{b-r},y^b).
\tag{FK.8}
\]

Evaluation at every \(x,y\) separates the outer symmetric
factors and proves (FK.7) as a tensor identity. The construction
and its coefficients are rational.

Now apply (FK.7) with \(b=b_{r+1}\), restricting to
\(\lambda_2\le t\). Every first-factor type \(\nu\)
occurring after \(\delta\) has \(\lambda/\nu\) a horizontal
strip by Pieri; in particular \(\nu_2\le\lambda_2\le t\).
R-018 proves injectivity of \(T_{r,r,b}\) on every entire
type with \(\nu_2\le b-r\). Since \(t\le b-r=b_r\),
the restriction of \(\Theta\) to the entire second-row band
is injective. Different isotypic components remain distinct
under this equivariant map.

In the codomain of (FK.7), every lower type \(\eta\)
contributing to a type \(\lambda\) is contained in it:
two applications of Pieri add the horizontal strips of sizes
\(r^2\) and \(b\). In particular \(\eta_2\le t\).
Consequently the actual injective restriction is

\[
\mathcal K_{r+1,b_{r+1}}^{\le t}
\hookrightarrow
\operatorname{Sym}^{r^2}W\otimes
\mathcal K_{r,b_r}^{\le t}\otimes
\operatorname{Sym}^{b_{r+1}}W.
\tag{FK.9}
\]

Iterate (FK.9) on its middle factor, retaining the other factors
and using only ordinary tensor-factor permutations. Tensoring an
injective linear map preserves injectivity. This gives the fully
specified composite injection

\[
\boxed{
\mathcal K_{a,b_a}^{\le t}(W)
\hookrightarrow\mathcal K_{5,t}^{\le t}(W)\otimes
\bigotimes_{r=5}^{a-1}
 \left(\operatorname{Sym}^{r^2}W\otimes
       \operatorname{Sym}^{b_{r+1}}W\right).}
\tag{FK.10}
\]

Its total degree is correct at every step:
\((r+1)b_{r+1}-r b_r=r^2+b_{r+1}\).
This proves (FK.10) in every dimension and, by extension from
its rational matrices, over every characteristic-zero field.

## 3. Explicit support exclusion and proof of the families

Every type in the codomain of (FK.10) contains at least one of
its base shapes \(\mu\), because each successive factor adds
a horizontal strip. For a nonzero target in (FK.2) or (FK.3),
\(\ell(\lambda)\le a\), so

\[
\lambda_1\ge ab_a-(a-1)t=aC_a+t\ge30+t>5t\ge\mu_1.
\]

Thus \(\mu\subseteq\lambda\) depends only on their tails.
The tail containment conditions are exactly the upward closures
of (FK.5).

For \(2\le t\le4\), write \(p=\lambda_2\le t\)
and \(q=\lambda'_2\). For \(p\le1\), none of the tails
in (FK.5) is contained and \(p+q\le t+2\) holds. For
\(2\le p\le t\), the tails in question are
\((t-j,2^{j+1})\), \(0\le j\le t-2\). The first
coordinate permits precisely \(j\ge t-p\); the remaining
coordinates require \(q\ge j+3\). Some such tail is
contained exactly at \(q\ge t-p+3\). Its exclusion is
therefore exactly \(p+q\le t+2\). At \(t=1\), the base
kernel is zero and the same displayed inequality holds
automatically on \(\lambda_2\le1\). This proves that the
codomain in (FK.10) has zero \(\lambda\)-isotypic component
for every parameter in (FK.2).

At \(t=5\), the unique minimal tail is \((5,4,3,1)\).
Its exclusion on \(\lambda_2\le5\) is exactly the
disjunction in (FK.3). Again the codomain has zero component.
Injectivity of (FK.10) then forces the actual annihilator
component to vanish. The perfect pairing (FK.4) proves the
surjectivity assertions (FK.2)–(FK.3), including all
multiplicities.

## 4. A positive explicit upper bound for the remaining cokernel

The same injection gives a further unconditional quantitative
statement. Let \(1\le t\le5\), \(a\ge6\),
\(b=C_a+t\), and \(\lambda\vdash ab\) with
\(\lambda_2\le t\). Let \(m_t(\mu)\) be the base
multiplicities in the complete table. Set \(N_{\mu,\lambda}\)
equal to the number of partition chains starting at \(\mu\),
ending at \(\lambda\), and successively adding horizontal
strips of sizes
\(25,b_6,36,b_7,\ldots,(a-1)^2,b_a\).
Then

\[
\boxed{
0\le\operatorname{mult}_\lambda\operatorname{coker}h_{b,a}
\le\sum_{\mu}m_t(\mu)N_{\mu,\lambda}.}
\tag{FK.11}
\]

For explicit polytopes, pad every intermediate partition to
\(\max\{a,\ell(\lambda)\}\) rows. Thus the same codomain
count is retained even when the actual target is zero because
\(\ell(\lambda)>a\). For each adjacent pair \(\eta,\theta\)
impose
\(\theta_i\ge\eta_i\ge\theta_{i+1}\), nonnegativity,
and \(\sum_i\theta_i-\sum_i\eta_i\) equal to its
specified strip size. Fix the endpoints. These are bounded
integer polytopes whose lattice points are precisely the chains;
the inequalities themselves prove the horizontal-strip
bijection. A label of multiplicity two is counted with two
separate tags. Pieri identifies this positive count with the
codomain multiplicity in (FK.10), proving (FK.11) for the
actual cokernel.

For a concrete nonzero value in (FK.3), every \(a\ge6\),
\(b=\binom a2-5\) has

\[
\rho_{b,a}^{(ab-5,5)}=a_{a,b}^{(ab-5,5)}=2.
\tag{FK.12}
\]

Indeed the target's binary weight \((ab-j,j)\), for
\(j=4,5\), has a monomial basis indexed by partitions of
\(j\) with at most \(a\) parts, each at most \(b\).
Here \(a\ge6\) and \(b\ge10\), so these counts are the
unrestricted partition numbers \(p(4)=5\), \(p(5)=7\).
Each binary Schur module with second row at most \(j\)
contributes once to this weight, giving the multiplicity
\(p(5)-p(4)=2\). Schur–Weyl functoriality preserves this
two-row multiplicity in every dimension at least two.
Surjectivity (FK.3) then gives the exact actual image value.
This calculation is included as a concrete consequence, without
a novelty claim for the two-row coefficient.

## Complete finite lower-kernel table

| t | Base kernel partition | Multiplicity |
|---:|---|---:|
| 2 | (6,2,2,0,0) | 1 |
| 2 | (4,2,2,2,0) | 1 |
| 2 | (2,2,2,2,2) | 1 |
| 3 | (10,3,2,0,0) | 1 |
| 3 | (9,2,2,2,0) | 1 |
| 3 | (8,3,2,2,0) | 1 |
| 3 | (7,2,2,2,2) | 1 |
| 4 | (14,4,2,0,0) | 1 |
| 4 | (13,4,3,0,0) | 1 |
| 4 | (13,3,2,2,0) | 1 |
| 4 | (12,4,4,0,0) | 1 |
| 4 | (12,4,3,1,0) | 1 |
| 4 | (12,4,2,2,0) | 1 |
| 4 | (12,2,2,2,2) | 1 |
| 4 | (11,4,4,1,0) | 1 |
| 4 | (11,4,3,2,0) | 1 |
| 4 | (11,4,2,2,1) | 1 |
| 4 | (10,4,4,2,0) | 2 |
| 4 | (10,4,2,2,2) | 1 |
| 4 | (9,4,4,3,0) | 1 |
| 4 | (9,4,4,2,1) | 1 |
| 4 | (8,4,4,4,0) | 1 |
| 4 | (8,4,4,2,2) | 1 |
| 4 | (7,4,4,4,1) | 1 |
| 4 | (6,4,4,4,2) | 1 |
| 4 | (4,4,4,4,4) | 1 |
| 5 | (12,5,4,3,1) | 1 |
| 5 | (11,5,4,4,1) | 1 |
