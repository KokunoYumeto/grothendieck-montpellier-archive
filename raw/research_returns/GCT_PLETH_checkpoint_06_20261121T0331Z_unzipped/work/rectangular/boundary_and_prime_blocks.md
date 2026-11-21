# Canonical-map boundary checks and prime rectangular blocks

Run: /root/rectangular_cases, 21 November 2026 (Europe/Berlin).
Model: GPT-6 Astra Pro. The inherited reasoning-effort setting is not exposed.

This supplements rectangular_report.md. The scalar normalization and the
determinant tensors \(I_{a,b}\) use that report's R-001 and R-002. The new
formulas below are explicit consequences of established results of Glynn,
Drisko, Howe, and the algebra morphism defining the canonical map. No claim
of priority is made for their nonvanishing content. The full surjectivity
bound proved in Sra III remains \(b\ge(a-1)^2\); the results below prove
specified components at smaller degrees.

## Exact map and coefficient conventions

Put \(V=\mathbb C^a\), with its orthonormal basis \(e_1,\ldots,e_a\), and

\[
 R_a=\bigoplus_{b\ge0}\left((\operatorname{Sym}^b V)^{\otimes a}\right)^{S_a}.
\]

The product is componentwise multiplication. Symmetric powers are realized
as invariant tensors by normalized averaging. There is a graded algebra
morphism

\[
 \mu_a:\operatorname{Sym}(\operatorname{Sym}^aV)\longrightarrow R_a,
 \qquad \mu_a(v^a)=v^{\otimes a}.
 \tag{B1}
\]

Its degree-\(b\) component is \(h_{b,a}\). Thus

\[
 h_{b,a}(u_1^a\cdots u_b^a)=(u_1\cdots u_b)^{\otimes a}.
 \tag{B2}
\]

For even \(b\), let \(I_{a,b}\) be obtained by putting the unnormalized
alternating \(a\)-tensor in each of \(b\) columns, and averaging within
the \(a\) rows. Permuting the rows has sign \(\operatorname{sgn}^b=1\),
so further outer averaging makes no change. This tensor satisfies

\[
 \langle I_{a,b},v_1^b\otimes\cdots\otimes v_a^b\rangle
       =\det(v_1,\ldots,v_a)^b.
 \tag{B3}
\]

The inner product is conjugate-linear in its first argument. All tensors
appearing in the coefficient calculations have rational real coefficients.
The coefficient at the tensor having row \(i\) constantly \(e_i\) is one.
The determinant line in \(R_{a,b}\) is one-dimensional by R-001. Products
of the determinant tensors satisfy the actual equality in the algebra

\[
 I_{a,b}I_{a,c}=I_{a,b+c}\qquad(b,c\text{ even}).
 \tag{B4}
\]

Indeed, evaluation on arbitrary \(a\) covectors turns both sides into
the product of determinant powers. Such evaluations determine the tensor.

## R-007. Prime-adjacent square scalars and periods

Let \(p\) run through the odd primes, and write

\[
 \mathcal P_n=\int_{\operatorname{SU}(n)}\prod_{i,j=1}^{n}u_{ij}\,du,
 \qquad
 B_n=\prod_{j=0}^{n-1}\frac{(n+j)!}{j!}.
\]

The normalized square scalar from R-002 satisfies

\[
 \boxed{c_{p-1}\in1+p\mathbb Z_{(p)},\qquad
        p^{p-1}c_{p+1}\in1+p\mathbb Z_{(p)}.}
 \tag{R-007a}
\]

In particular these are nonzero scalars, with exact valuations

\[
 v_p(c_{p-1})=0,\qquad v_p(c_{p+1})=1-p,
 \qquad
 v_p(\mathcal P_{p-1})=2-p,\qquad
 v_p(\mathcal P_{p+1})=-p.
 \tag{R-007b}
\]

Here \(\mathbb Z_{(p)}\) denotes the rational numbers whose denominator is
coprime to \(p\); the integral is the rational number identified by the
coefficient formula of R-002.

### Source statements and proof of this normalization

Glynn, *The conjectures of Alon--Tarsi and Rota in dimension prime minus
one*, Theorem 3.2, states

\[
 E_{p-1}-O_{p-1}\equiv(-1)^{(p-1)/2}\pmod p.
\]

Drisko, *On the number of even and odd Latin squares of order \(p+1\)*,
Theorem 9, pp. 33--34, states

\[
 E_{p+1}-O_{p+1}\equiv(-1)^{(p+1)/2}p^2\pmod {p^3}.
\]

Both use row-times-column parity. R-002 proves

\[
 \Delta_n=(-1)^{n(n-1)/2}(E_n-O_n),\qquad
 c_n=\frac{\Delta_n}{(n!)^n},\qquad \mathcal P_n=\frac{\Delta_n}{B_n}.
\]

For even \(n\), \(n(n-1)/2\equiv n/2\pmod2\). Consequently the two
source congruences become

\[
 \Delta_{p-1}\equiv1\pmod p,
 \qquad \Delta_{p+1}\equiv p^2\pmod {p^3}.
\]

Wilson's theorem gives \((p-1)!\equiv-1\pmod p\), and

\[
 \frac{(p+1)!}{p}=(p+1)(p-1)!\equiv-1\pmod p.
\]

The exponents \(p-1\) and \(p+1\) are even. Dividing by the corresponding
factorial units proves (R-007a), and its first two valuation assertions.
In \(B_{p-1}\), the numerator factorials from \(p!\) through
\((2p-3)!\) each contain exactly one factor of \(p\), while all denominator
factorials are prime to \(p\). Thus \(v_p(B_{p-1})=p-2\).
In \(B_{p+1}\), the \(p-1\) factorials \((p+1)!,\ldots,(2p-1)!\)
have valuation one, the two factorials \((2p)!\) and \((2p+1)!\)
have valuation two, and the denominator contributes the one factor in
\(p!\). Thus \(v_p(B_{p+1})=(p-1)+4-1=p+2\). This proves the period
valuations. The ranges include \(p=3\).

These calculations use the established prime-adjacent Alon--Tarsi cases;
they do not supply further orders for that conjecture.

## R-008. A canonical determinant block for every prime-minus-one width

For every odd prime \(p\), every \(2\le a\le p-1\), and \(b=p-1\), put

\[
 m_a=e_1\cdots e_a\in\operatorname{Sym}^aV,
 \qquad
 q_{a,b}=\langle I_{a,b},h_{b,a}(m_a^b)\rangle.
\]

Then

\[
 \boxed{q_{a,p-1}\in1+p\mathbb Z_{(p)}.}
 \tag{R-008a}
\]

In particular the canonical map \(h_{p-1,a}\) has rank one on the
target determinant isotypic component \(S_{((p-1)^a)}V\). The tensor
\(m_a^b\) is an explicit test vector for that component.

More explicitly, in tensor degree \(ab\) set

\[
 e_{(b^a)}=\frac{f^{(b^a)}}{(ab)!}
       \sum_{\sigma\in S_{ab}}\chi^{(b^a)}(\sigma)\sigma,
 \qquad N_{a,b}=\langle I_{a,b},I_{a,b}\rangle>0.
\]

This is the central Schur projector, with \(f^{(b^a)}\) the dimension
of the indicated Specht module. Define the concrete source vector

\[
 u_{a,p}=\frac{N_{a,p-1}}{q_{a,p-1}}
             e_{((p-1)^a)}m_a^{p-1}.
 \tag{B5}
\]

It satisfies the exact equality

\[
 h_{p-1,a}(u_{a,p})=I_{a,p-1}.
 \tag{R-008b}
\]

### Proof of the unit contraction

Glynn's Theorem 3.1, together with the formula defining his modular
hyperdeterminant immediately before that theorem, gives the following
coefficient congruence. For an \(a\times a\) matrix \(E=(e_{ij})\)
of nonnegative integers having every row and every column sum \(b=p-1\),

\[
 C_E=[X^E]\det(X)^b
       \equiv\frac{(-1)^a}{\prod_{i,j}e_{ij}!}\pmod p.
 \tag{B6}
\]

Every denominator in (B6) is a unit modulo \(p\). Write a general
degree-\(b\) vector as

\[
 P=\sum_{|\alpha|=b}P_\alpha e^\alpha,
 \qquad
 F(P)=\langle I_{a,b},P^{\otimes a}\rangle.
\]

Let \(M(\alpha)=b!/\prod_j\alpha_j!\). Evaluation of (B3), first on
independent row vectors and then on their monomial expansions, gives
the exact coefficient formula

\[
 F(P)=\sum_E \frac{C_E}{\prod_i M(E_i)}\prod_i P_{E_i},
 \tag{B7}
\]

where \(E_i\) is row \(i\) of \(E\). This accounts for the normalized
embedding of each symmetric monomial. Wilson's theorem gives

\[
 \prod_iM(E_i)\equiv
 \frac{(-1)^a}{\prod_{i,j}e_{ij}!}\pmod p.
\]

Thus every ratio in (B7) is one modulo \(p\). Equivalently, with
\(P(x)=\sum P_\alpha x^\alpha\),

\[
 F(P)\equiv[x_1^b\cdots x_a^b]P(x)^a\pmod p.
 \tag{B8}
\]

Now introduce independent \(z_{ij}\), \(1\le i\le a\), \(1\le j\le b\),
put \(\ell_j=\sum_i z_{ij}e_i\), and substitute
\(P=\ell_1\cdots\ell_b\) in (B8). By (B2), the left side becomes

\[
 \left\langle I_{a,b},h_{b,a}(\ell_1^a\cdots\ell_b^a)\right\rangle.
\]

Its coefficient at the squarefree monomial \(\prod_{i,j}z_{ij}\)
is \((a!)^b q_{a,b}\), since the squarefree coefficient in
\(\ell_j^a\) is \(a!m_a\). On the right side of (B8), the same
coefficient in \(\prod_j\ell_j(x)^a\) is
\((a!)^b(x_1\cdots x_a)^b\), so it becomes \((a!)^b\) after
coefficient extraction in \(x\). The integer \(a!\) is prime to \(p\).
Cancelling it proves (R-008a).

All tensor averages used here have denominators prime to \(p\), because
\(a,b<p\), so the stated congruences are in the specified local ring.

### Proof of the actual preimage

The central projector \(e_{(b^a)}\) commutes with every tensor-position
permutation and every averaging idempotent. In particular it preserves
both nested symmetric powers and commutes with \(h_{b,a}\). On the target
it is orthogonal projection onto the line spanned by \(I_{a,b}\).
Character orthogonality gives this projector formula, and R-001 supplies
the target multiplicity one. Therefore

\[
 h_{b,a}(e_{(b^a)}m_a^b)
   =e_{(b^a)}h_{b,a}(m_a^b)
   =\frac{q_{a,b}}{N_{a,b}}I_{a,b}.
\]

The scalar \(q_{a,b}\) is nonzero by (R-008a). Multiplication by the
factor in (B5) proves (R-008b). Thus the proof identifies the particular
canonical morphism and an explicit source vector.

## R-009. Products and first-row extensions below the full bound

For every odd prime \(p\), \(2\le a\le p-1\), \(t\ge1\), and
\(s\ge0\), set

\[
 b=t(p-1)+s,\qquad
 \lambda=(as+t(p-1),\;\underbrace{t(p-1),\ldots,t(p-1)}_{a-1}).
\]

The following source and image are explicit:

\[
 \boxed{
 h_{b,a}\bigl(u_{a,p}^{\,t}(e_1^a)^s\bigr)
   =I_{a,t(p-1)}(e_1^{\otimes a})^s\ne0.
 }
 \tag{R-009a}
\]

Both sides are highest weight vectors of weight \(\lambda\). Moreover

\[
 [S_\lambda V:\operatorname{im}h_{b,a}]
   =[S_\lambda V:\operatorname{Sym}^a(\operatorname{Sym}^bV)]=1
 \tag{R-009b}
\]

in every ambient dimension at least \(a\).

### Proof

The image equality follows by applying the algebra morphism (B1), using
(R-008b), (B4), and \(\mu_a(e_1^a)=e_1^{\otimes a}\). Evaluation on
\(a\) covectors gives the nonzero polynomial

\[
 \det(X)^{t(p-1)}\prod_{j=1}^a x_{1j}^{s}.
\]

This proves the asserted nonvanishing without a cancellation assertion.
The determinant vector is highest weight of weight \((t(p-1)^a)\);
the added factor has weight \((as)\) and is killed by the upper triangular
raising operators. The same is true of the source vector (B5), which
lies in a determinant representation over \(\mathbb C^a\). Embedding
\(\mathbb C^a\subseteq V\) gives highest weight vectors in every larger
ambient space, since the additional raising operators differentiate basis
directions absent from these tensors.

For the target multiplicity, set \(\ell=t(p-1)\). The inner-degree
lifting map \(\kappa^a_{\ell,b}\), obtained by multiplying each inner
factor by \(e_1^s\), maps the unique highest weight vector of weight
\((\ell^a)\) to the displayed image. BIP Proposition 5.6(1) applies
because the second part of \((\ell^a)\) is \(\ell\). It identifies the
two highest weight spaces. Howe Proposition 4.3, equivalently R-001,
gives dimension one because \(\ell\) is even. This proves (R-009b).

### Actual boundary families and examples

For each prime \(p\equiv1\pmod4\), \(p\ge13\), put

\[
 a=(p-1)/2,\qquad t=(a-2)/2,\qquad s=0.
\]

Then \(a\) is even, and (R-009) proves the entire determinant component
at

\[
 b=t(p-1)=a(a-2)=(a-1)^2-1.
 \tag{B9}
\]

Examples are \((a,b)=(6,24),(8,48),(14,168),(18,288),(20,360),
(26,624),(30,840)\). The case \(a=26\) uses \(p=53\) and \(t=12\);
its base rectangle has width \(52\).

Boundary examples in odd outer degree are obtained with \(t=1\) and
positive \(s\). For \((a,b,p)=(7,35,31)\), the image has its unique
component \(S_{(65,30^6)}V\). For \((a,b,p)=(9,63,61)\), the image has
its unique component \(S_{(87,60^8)}V\). The degree sums are respectively
\(65+6\cdot30=7\cdot35\) and \(87+8\cdot60=9\cdot63\).

The square scalar yields a second exact form. For every
\(n\in\{p-1,p+1:p\text{ odd prime}\}\) and \(k\ge1\),

\[
 h_{kn,n}(I_{n,n}^{\,k})=c_n^{\,k}I_{n,kn}\ne0.
 \tag{B10}
\]

This follows directly from R-002 and (B1). For \(n=6,k=4\), the scalar
is \(699840000^{-4}\), since \(c_6=-699840000^{-1}\). This verifies the
determinant component at \((a,b)=(6,24)\) by an explicit rational scalar.

## R-010. What the last common-power step proves at the boundary

Write \(r=a-1\), and consider the actual differential operator

\[
 \Psi_{r,b}=\prod_{i=1}^r(x\cdot\partial_{v_i})^r
\]

on polynomials initially independent of \(x\), separately of degree
\(b\) in each \(v_i\). Sra III Lemma 2.1 and the proof of Theorem 1.3
give its injectivity for \(b\ge r^2\). The supplement's Corollary S8.1
records the quantitative estimate; immediately after it, p. 36, the
author gives the example \(r=5,b=24\).

For every odd \(r\ge3\), put \(b=r^2-1\) and \(V=\mathbb C^r\). Then

\[
 f(v_1,\ldots,v_r)=\det(v_1,\ldots,v_r)^b
 \quad\text{is nonzero and symmetric,}\qquad \Psi_{r,b}f=0.
 \tag{R-010a}
\]

Indeed \(b\) is even, so the determinant power is symmetric. Every term
in the differentiated expression inserts \(r^2=b+1\) copies of the
same vector \(x\) into \(b\) determinant factors. A determinant receiving
two copies of \(x\) vanishes, and every term has such a factor. For even
\(r\), the same determinant polynomial is alternating because \(b\)
is odd. Thus its projection to the symmetric \(r\)-slot input is zero.
This last parity calculation does not classify the other kernel
components.

The arbitrary-common-power full-tensor kernel admits nonrectangular
components. A concrete example of the analogous operator with \(r=3\), power one, and input degree two per slot has an
additional kernel vector on \(V=\mathbb C^2\). Write
\([ij]=x_i y_j-y_i x_j\) and set

\[
 g=[12][13][23].
\]

It has degree two in each vector and transforms by the sign of the slot
permutation. Under \(v_i\mapsto v_i+t_i x\), each bracket is at most
linear in the \(t_i\), and direct expansion gives

\[
 [t_1t_2t_3]\,
 [v_1+t_1x,v_2+t_2x]
 [v_1+t_1x,v_3+t_3x]
 [v_2+t_2x,v_3+t_3x]=0.
 \tag{R-010b}
\]

The two possible terms are
\(-[x,v_2][x,v_3][x,v_1]\) and
\(+[x,v_1][x,v_2][x,v_3]\), which cancel. The vector has
\(\operatorname{GL}_2\)-weight \((3,3)\), whereas the height-three
rectangle of degree two vanishes on \(\mathbb C^2\). This is an exact
counterexample to a uniform rectangular-kernel classification across
arbitrary common powers. It does not
decide the symmetric-input kernel at \(r\) even and power \(r\).

The current proof does not establish full canonical-map surjectivity at
\(b=(a-1)^2-1\) for general odd \(a\). The unconditional improvements in
this report are the specified canonical-map components (R-008--R-009).

## Independent finite coefficient checks

Let \(D_E=[X^E]\operatorname{per}(X)^b\). The coefficient of
\(\prod_{i,j}z_{ij}\) in \(\prod_iP_{E_i}\), after
\(P=\prod_{j=1}^b\ell_j\), is \(D_E\): each of its \(b\) columns
assigns the \(a\) symbols bijectively to the \(a\) tensor rows, and
the resulting row multiplicities are \(E\). Combining this with (B7)
and its \((a!)^b\) squarefree coefficient gives

\[
 q_{a,b}=
 \frac{\sum_E C_ED_E\prod_{i,j}e_{ij}!}
      {(a!)^b(b!)^a}.
 \tag{B11}
\]

The numerator is the Fischer pairing of the determinant power and
permanent power. The program verify_prime_blocks.py computes their
coefficient tables by exact monomial multiplication, checks (B6) at
every exponent matrix, and evaluates (B11). It imports no source-paper
implementation.

| \(a\) | \(b=p-1\) | Exponent matrices checked | Exact \(q_{a,b}\) |
|---:|---:|---:|---:|
| 2 | 2 | 3 | \(1/4\) |
| 2 | 4 | 5 | \(1/16\) |
| 3 | 4 | 120 | \(1/1296\) |
| 3 | 6 | 406 | \(1/87480\) |
| 4 | 4 | 10147 | \(1/331776\) |
| 3 | 10 | 2211 | \(1/88179840\) |
| 3 | 12 | 4186 | \(281/838061199360\) |

All seven residues are one modulo the indicated prime. The two square
cases also equal \(c_a^2\), using the independently enumerated Latin
scalars in rectangular_report.md. The nondivisible case \((a,b)=(3,4)\)
checks that the general coefficient argument does not require \(a\mid b\).

## Source audit and exact locators

* Suvrit Sra, *The q-Foulkes problem III: On Foulkes' conjecture with a
  graded inner factor*, v1, Theorem 1.3, Lemma 2.1, and §2.2, pp. 3--5.
  Author's repository: <https://github.com/suvrit/preprints/blob/main/preprints/qfoulkes3/v1/qfoulkes3-v1.pdf>.
* Sra, *Supplement to the q-Foulkes project*, S8, p. 36, Corollary S8.1
  and its following paragraph. Author's repository:
  <https://github.com/suvrit/preprints/blob/main/preprints/qfoulkes3/v1/qfoulkes3-v1-supplement.pdf>.
* David G. Glynn, *The conjectures of Alon--Tarsi and Rota in dimension
  prime minus one*, SIAM J. Discrete Math. **24** (2010), 394--399,
  Theorems 3.1--3.2 and the definition immediately before Theorem 3.1.
  DOI: <https://doi.org/10.1137/090773751>.
  The author's full manuscript was read through its publicly indexed
  transcript at <https://www.academia.edu/25562085/The_Conjectures_of_Alon_Tarsi_and_Rota_in_Dimension_Prime_Minus_One>.
* Arthur A. Drisko, *On the number of even and odd Latin squares of order
  p+1*, Adv. Math. **128** (1997), 20--35, Theorem 9, pp. 33--34.
  Publisher record:
  <https://www.sciencedirect.com/science/article/pii/S0001870897916236>.
  The original article's full transcript, including its page numbers,
  was read at <https://studyres.com/doc/19593200/on-the-number-of-even-and-odd-latin-squares-of>.
* The 1998 assertion extending prime cases by powers of two is not used.
  Glynn's introduction explicitly identifies the error in the preceding
  doubling argument. No such enlargement is included in these parameter
  families.
* Howe Proposition 4.3 and BIP Proposition 5.6(1) are located and checked
  in rectangular_report.md, R-001 and R-005.
