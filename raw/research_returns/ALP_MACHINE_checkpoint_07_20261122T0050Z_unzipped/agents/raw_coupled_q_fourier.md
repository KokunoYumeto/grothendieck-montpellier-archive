# ALP-LIFT-23: exact Fourier contraction of the prescribed coupled Q family

Author: GPT-6 Astra Pro, ALP_MACHINE /root/lift_accounting.
Date: 22 November 2026 UTC. Inherited reasoning effort is not exposed.

This finding evaluates the entire literal local Y sum in the two
coupled finite kernels for m=2 at a degree-one Q place. The auxiliary
depth disappears. The resulting finite function is nonzero, has an
explicit Gauss-sum scalar, and has primitive content at every coefficient
place over11 when q is different from11. This is an identity of the
specified finite Schwartz functions. It is not a claim that the second
automorphic theta integral is injective on the preceding image.

## 1. Literal source data and conventions

Use the pinned source tree work/research/alpoge_source at commit
7cbf7a0c32fca1badf05931879a37c3f8a2b03b4. Put
\[
 m=2,\quad r=k+1,\quad d=t+1,\quad b=k+d=r+t,\quad N=b+d.
 \tag{Q1}
\]
The first edge has ranks k,b, and the second edge has ranks b,N.
Let Q be a relative split place whose local field F is the rational
q-adic field, so q is a rational prime and a uniformizer. Write O for
its ring of integers. This explicit unramified degree-one hypothesis
is retained; residue degree one alone would not imply it.
Take the actual standard frames and the forced initial and terminal
frame choices of ChIdx.Ok.zero_h and last_h. The limited-depth
character is trivial on O and nontrivial on q^{-1}O. Its induced
nontrivial residue additive character is
\[
             \psi_0(z)=\psi(q^{-1}\widetilde z).
 \tag{Q2}
\]
Only the finite argument range prescribed by LocCst.Ok is used.

Let chi be the actual tame residue character of the tuple at Q.
We first assume chi is nontrivial, and extend it by zero at0.
The trivial-character version is given in section5. Let
\(\mathsf M=\mathrm{cst.M}\ge1\), with depth at least \(2\mathsf M\).
The actual local parameter set, by the already checked DO032, is
\[
       Y_Q=q^{-\mathsf M}O^b/q^{\mathsf M}O^b.
 \tag{Q3}
\]
Representatives may be changed within these cosets because both
literal factors are unchanged by that change.

The exact source locators are:

- Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean
  (FS): entB684–694; unitV669; PhiQ711–715;
  omPhi939–941; joinCol982–983 and PsiAt985–986;
  zero_h1020, last_h1025; XiCpl11134–1138;
  PhiTop1142–1147 and ftY1150–1156; XiCpl21160–1167.
- The same file: ybSet1125–1129, and the actual coupled Y action
  and CplKer in1216–1237.
- Accepted and checked DO031.3–DO031.5 and DO032.2–DO032.10 give
  the literal terminal last-row normalization and finite quotient,
  including the source scalar \(q^{-\mathsf M b}\).
- The Q middle group is the reduction preimage of
  \(P_{r,t}\), by Jat909–913, last_h, and grpQ1062–1066.
  It does not generally fix an individual chosen class \(y=e_k\).
  The present calculation retains the whole prescribed family.

The actual terminal last row in these frames is denoted by
\(\eta\in F^{1\times b}\); any piT unit already absorbed by the
source frame remains absorbed here. No further coordinate rescaling
is introduced.

## 2. The two literal functions

Write the first matrix as
\[
                 X=\begin{pmatrix}A\\C\end{pmatrix},
 \qquad A\in M_{r,k}(F),\quad C\in M_{t,k}(F),
 \qquad y=\begin{pmatrix}z\\w\end{pmatrix}.
 \tag{Q4}
\]
Because the Q exponent in lamYat is zero and the two relevant frames
are the identity, entB of joinCol is precisely the ordinary matrix
\([X,y]\), with the added column in position k. Thus the first raw
factor is exactly
\[
 F_X(y)=
 \mathbf1_{M_{r,k}(O)}(A)\mathbf1_{qM_{t,k}(O)}(C)
 \mathbf1_{O^r}(z)\mathbf1_{qO^t}(w)
       \chi\!\left(\det[\bar A,\bar z]\right).
 \tag{Q5}
\]
In particular it is zero when \(\bar A\) has rank smaller than k.
This includes all support conditions, including the lower auxiliary
column condition; it is not just the specialization \(y=e_k\).

Write the second matrix as \(\binom Z\eta\), with
\(Z\in M_{N-1,b}(F)\). Its terminal factor is
\[
 H(Z)\,q^{-\mathsf M b}
 \mathbf1_{q^{-\mathsf M}O^b}(\eta)\psi(-\eta y),
 \qquad H(Z)=\Phi_{\mathrm{Top},Q}(Z).
 \tag{Q6}
\]
Here H has all of the literal PhiQ conditions: Z is integral, its
bottom-left \((N-1-r)\)-by-r block is divisible by q, and its leading
r-by-r determinant is a unit, on which chi is evaluated.

The actual local contraction over its entire allowed Y set is therefore
\[
 {\cal C}_{\mathsf M}(X,Z,\eta)
   =H(Z)q^{-\mathsf M b}
     \mathbf1_{q^{-\mathsf M}O^b}(\eta)
        \sum_{y\in Y_Q}F_X(y)\psi(-\eta y).
 \tag{Q7}
\]
The source writes a finite sum, not a Haar integral over Y. The scalar
in (Q7) is exactly its ftY scalar.

## 3. Closed formula and independence of depth

For a matrix \(\bar A\) of rank k define its nonzero cofactor row
\(\ell_A\in\kappa^{1\times r}\) by
\[
                  \ell_A z=\det[\bar A,z].
 \tag{Q8}
\]
Put
\[
                    G(\chi,\psi_0)=
                       \sum_{s\in\kappa^\times}\chi(s)\psi_0(s).
 \tag{Q9}
\]
If the support conditions on A,C in (Q5) hold and \(\bar A\) has
rank k, then the exact answer is
\[
 \boxed{
 {\cal C}_{\mathsf M}(X,Z,\eta)=
 \begin{cases}
 H(Z)\,q^{-d}G(\chi,\psi_0)\chi(-c)^{-1},
 &\eta\in q^{-1}O^b,\quad
   \overline{q\eta_{\mathrm{top}}}=c\ell_A,\quad c\in\kappa^\times,\\
 0,&\text{otherwise}.
 \end{cases}}
 \tag{Q10}
\]
It is also zero when those A,C support or rank conditions fail.
There is no condition on \(\overline{q\eta_{\mathrm{low}}}\).
In particular the entire answer is independent of
\(\mathsf M\ge1\).

Proof. Because of (Q5), the contributing representatives in (Q3)
are exactly
\[
       z\in O^r/q^{\mathsf M}O^r,\qquad
       w\in qO^t/q^{\mathsf M}O^t.
\]
The determinant character depends only on \(\bar z\).
The sum over all higher lifts in both blocks is zero unless
\(\eta\in q^{-1}O^b\). When this condition holds, those sums
contribute \(q^{(\mathsf M-1)b}\). The lower residue block is zero.
Multiplication by the source scalar \(q^{-\mathsf M b}\)
therefore leaves
\[
       H(Z)q^{-b}\sum_{z\in\kappa^r}
            \chi(\ell_Az)\psi_0(-az),
       \qquad a=\overline{q\eta_{\mathrm{top}}}.
 \tag{Q11}
\]
This argument also works for \(\mathsf M=1\): there are no higher
lifts, and the support of ftY is already \(q^{-1}O^b\).

If \(a\) is not a scalar multiple of \(\ell_A\), there is a vector
\(z_0\in\ker\ell_A\) with \(az_0\ne0\). Translation by a suitable
multiple of \(z_0\) preserves the determinant factor and multiplies
the character sum by a scalar different from1. The sum is zero.
If \(a=c\ell_A\), every fibre of \(\ell_A\) has \(q^k\) elements,
so the sum equals
\[
           q^k\sum_{s\in\kappa^\times}\chi(s)\psi_0(-cs).
 \tag{Q12}
\]
For \(c=0\), it vanishes because chi is nontrivial.
For \(c\ne0\), substitute \(u=-cs\); the answer becomes
\(q^k\chi(-c)^{-1}G(\chi,\psi_0)\).
Since \(b-k=d\), (Q10) follows. Every manipulation takes place
inside the specified finite additive quotient, so no unrestricted
extension of the source psi has been assumed.

A concrete nonzero value is obtained with
\(A=\binom{I_k}{0}\), C=0, \(\eta=q^{-1}e_k^\vee\),
and Z having identity leading b-by-b block and all remaining
rows zero. Then \(\ell_A=e_k^\vee\), H(Z)=1, and
\[
      {\cal C}_{\mathsf M}(X,Z,\eta)
                       =q^{-d}G(\chi,\psi_0)\chi(-1)^{-1}\ne0.
 \tag{Q13}
\]

## 4. Exact norms, content, and height of this scalar

All measures in this section give integral additive matrix lattices
volume1. The standard finite Gauss identity is proved here in the
needed normalization. For \(c\in\kappa\) put
\(G_c=\sum_{s\ne0}\chi(s)\psi_0(cs)\).
Then \(G_0=0\), and substitution shows all \(|G_c|\), \(c\ne0\),
are equal. Additive orthogonality gives
\(\sum_c|G_c|^2=q(q-1)\). Hence
\[
                       |G(\chi,\psi_0)|^2=q.
 \tag{Q14}
\]
This proof applies after every complex embedding of the finite
coefficient field, since both induced characters remain nontrivial.

For fixed supported X of full residue rank, the nonzero eta set
in (Q10) has measure \((q-1)q^t\): there are \(q-1\) top fractional
classes and \(q^t\) arbitrary lower fractional classes, each followed
by the integral lattice of volume1. Thus
\[
 \int_F\cdots\int_F
   \left|{\cal C}_{\mathsf M}(X,Z,\eta)\right|^2\,d\eta
       =|H(Z)|^2(q-1)q^{-d}.
 \tag{Q15}
\]
This also equals \(|H(Z)|^2\int|F_X(y)|^2dy\), since the first
support has lower volume \(q^{-t}\) and the determinant is nonzero
on the proportion \((q-1)/q\) of its top residue classes.
Thus the depth-independent contraction is exactly the additive
Fourier transform in this variable, including its normalization.

For the finite counting measure on (Q3), the number of nonzero
first values is
\[
                 (q-1)q^{\mathsf M b-d}.
 \tag{Q16}
\]
The number of nonzero transformed values, modulo
\(q^{\mathsf M}O^b\), is \((q-1)q^{t+\mathsf M b}\).
Their squared amplitude \(q^{1-2d}\) gives the same number
(Q16), as required by the actual unitary finite Fourier matrix.

The upper terminal factor has norm
\[
 \Gamma_{\mathrm{top},Q}
  =q^{-r(N-1-r)}\prod_{i=1}^r(1-q^{-i}).
 \tag{Q17}
\]
The probability that an r-by-k residue matrix has rank k is
\(\prod_{i=0}^{k-1}(1-q^{i-r})\).
Integrating also in X and Z gives the exact joint Schwartz norm
\[
 \boxed{
 \|{\cal C}_{\mathsf M}\|_2^2
   =q^{-tk}(q-1)q^{-d}
       \prod_{i=0}^{k-1}(1-q^{i-r})\,
       \Gamma_{\mathrm{top},Q}.}
 \tag{Q18}
\]
This is the norm of the contracted raw array in its product matrix
variables; it is not the norm of an automorphic composite operator.

Both G and its complex conjugate are algebraic integers, and (Q14)
is the algebraic identity \(G\overline G=q\). Consequently G is a
unit at every coefficient place above11 if \(q\ne11\).
Every nonzero value in (Q10) is then an11-adic unit. Its minimum
valuation is exactly zero, by (Q13). No division by \(q-1\),
a finite general linear group order, or a class mass has been
introduced.

The magnitude of the scalar in (Q10) is \(q^{1/2-d}\).
Its absolute logarithmic Weil height is exactly
\[
                  h\!\left(q^{-d}G(\chi,\psi_0)\right)
                               =(d-\tfrac12)\log q.
 \tag{Q19}
\]
Indeed its inverse is \(q^{d-1}\overline G\), an algebraic integer,
and every complex conjugate of that inverse has absolute value
\(q^{d-1/2}>1\). Computing the height of this algebraic integer and
using \(h(x^{-1})=h(x)\) proves (Q19). This is the height of the
specified finite scalar. It must not be renamed the source global H.

## 5. Trivial residue character and exact scope

If chi is trivial, still extended by zero at0, (Q11) remains valid.
The value is zero unless \(a=c\ell_A\), and its two remaining values are
\[
 {\cal C}_{\mathsf M}=
 \begin{cases}
 H(Z)q^{-d}(q-1),&c=0,\\
 -H(Z)q^{-d},&c\ne0.
 \end{cases}
 \tag{Q20}
\]
The norm (Q15) remains the same. The main primitive-value conclusion
remains true for \(q\ne11\), because the \(c\ne0\) value is a unit,
although the \(c=0\) value can have positive valuation if11 divides
\(q-1\). The nontrivial-character height formula(Q19) is not asserted
for the trivial case.

The full allowed global Y set factors into these local finite quotients
and the G quotients by the already checked CRT statement DO032.2.
Therefore a finite product of the literal Q contractions is exactly
the corresponding partial global Y sum. At sharp G, LIFT22 shows that
the first factor leaves just its single forced local class.
These statements remove cancellation in the raw finite array and retain
the exact Q Fourier scalar and its norms.

They do not show that this raw function survives the next automorphic
integral. At Q the two stages have the same tuple residue character,
so the all-ramified boundary exclusion used in LIFT21 at G is not
available. The fixed-Q-class first theta function is also not generally
in the full prescribed middle parabolic type by itself: that covariance
belongs to the coupled family. An argument for the second image must
retain this family or supply the exact local quotient comparison.
No claim about a globally pinned scalar, the iterated integral row
lattice, the complete D7 data, or a DP44 gain is made.

## 6. Checks

The exact finite replay is raw_coupled_q_fourier_certificate.py.
It compares the literal finite Y sum with (Q10)/(Q20), including
the nontrivial M=2 higher-depth cancellation, in cyclotomic integer
coordinates. It also checks the support counts, Parseval factors,
the cofactor orientation, and the unit normalization. Small finite
examples are diagnostics of the identity, not full Ranks data.
Whole-proof reading and replay events are recorded separately.

