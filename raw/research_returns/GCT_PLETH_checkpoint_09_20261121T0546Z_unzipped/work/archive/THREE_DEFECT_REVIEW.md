# Independent review of the complete defect-three positive formula

Statement **A-049**. Checked on 21 November 2026 by GPT-6 Astra Pro,
run /root/archive_audit; effort setting not exposed.

**Result: complete proof PASS; all 120,960,000 constants in the
\(b\ge1\) branch independently reconstructed.** The full report
work/theta/outer5/three_defect_positive_report.md, F.1–F.11, was
read, together with the two certificate programs and the shared
certificate engine.

## Exact modules and correction characters

The partition and degree in F.1 give point order
\(\lambda_2-n=k\), first-line twist \(b+x+2k-3\), and
relative quotient weight \((b+x,x,0)\). The explicit
complementary-column contraction therefore gives exactly
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq
\varepsilon^{d+b+x}
H^0(I^k(2k-3)S_{(b+x,b)}Q).
\]
The remaining partition inequality is
\(2b+x+k\ge9\). The stable-defect comparison in A-048
applies because \(k\ge8=3\cdot3-1\), including \(k=8\).
All higher cohomology of index at least two vanishes.

For \(s=3\), the four terms of the actual normal cohomology
are
\[
\det P\otimes P\otimes S_{(a,b)}W,\qquad
\det P\otimes W^*\otimes S_{(a,b)}W,\qquad
S_{(a-1,b)}W,\qquad S_{(a,b-1)}W.
\]
The third term is absent at \(x=0\), and the fourth at
\(b=0\). These are precisely the four index choices
in D.2; both determinant powers in the last two terms
are even. If the endpoint and complementary signs are
\(\delta,\eta\), and the complementary standard trace
is \(e\), their sum is
\[
(1+\delta+\delta e)\eta^b h_x
+\eta^b h_{x-1}
+\mathbf1_{b\ge1}\eta^{b-1}h_{x+1}.
\]
The convention \(h_{-1}=0\) gives the third-term endpoint.
Counting fixed two-element subsets yields F.6 and F.7
with their exact signs. In particular, on a transposition
there are three fixed singleton pairs and one two-cycle
pair. On a three-cycle the sole fixed pair has
\(\delta=1,e=-1\), and on a three-two cycle its pair
has \(\delta=-1,e=-1\). The identity
\(\tau(x-1)+\tau(x)+\tau(x+1)=0\) gives the displayed
cancellations. This also verifies the two separate
formulas at \(b=0\).

The zeroth-cohomology character is therefore exactly
the ambient/jet Euler expression plus this actual
higher-cohomology correction. The twist is
\(\varepsilon^{d+b+x}\), so the conversion of an
outer label to its transpose has the stated parity.

## Polynomial phases and an independent positivity proof

The independent reconstruction uses
\[
\varepsilon(g)^a
s_{(a+c,a,x,0)}(E)(g)
-m_1(g)h_{k-1}(E)(g)s_{(a,b)}(E-\mathbf1)(g)
+J^{(3)}_g(x,b).
\tag{TD1}
\]
The first term is the actual complementary-column ambient
module, and the second is the actual five-point jet module.
A \(3\times3\) Jacobi–Trudi determinant computes the first
term, with \(h_r(E-\mathbf1)=h_r(E)-h_{r-1}(E)\) in the
second. Thus this calculation does not use the three
separable Euler products in the original certificate.

Substitution \(b=B+1,\ k=K+8,\ c=2K+13\) gives exactly
the identity polynomial F.8. All its ordinary coefficients
are positive and its downset has fifty-five orders.
From (TD1), the transposition, double-transposition and
three-cycle phases have total degrees at most three,
two and one, respectively. The independent construction
checks all eight, eight and twenty-seven phases. The
three remaining classes are periodic; their absolute
trace bounds are one.

For a monomial \(X^m\), the exact difference formula used is
\[
\Delta_{60}^{\,r}X^m
=\sum_{j=r}^m
\binom mj60^j\,r!\,
\left\{\begin{matrix}j\\r\end{matrix}\right\}
X^{m-j}.
\tag{TD2}
\]
The braces denote Stirling numbers of the second kind.
The product of these operators in the three variables
computes every mixed difference without a numerical
finite-difference subtraction.

At each of the fifty-four positive active orders,
the identity difference polynomial minus the weighted
coefficientwise absolute phase maxima for the other
classes has nonnegative coefficients and a positive
constant. The class weights are \(10,15,20\), with
the remaining periodic traces killed by a positive
order. The minimum constant margin is \(411165\).
Since \(|\chi_\nu(g)|\le\dim[\nu]\), this proves
strict positivity of every such irreducible difference
at every nonnegative residue directly.

The same coarse domination at order zero has a negative
constant, so it proves no zeroth-order assertion.
The complete exact residue cube, independently
reconstructed below, proves the required zeroth
positivity. The report and receipts keep these two
steps separate.

## Complete independent numerical reconstruction

The program check_three_defect_full_constants.py evaluates
the exact phase polynomials from (TD1), applies (TD2),
and combines them with independent Murnaghan–Nakayama
characters of \(S_5\). A common denominator of twenty-four
makes each phase polynomial integral before array
evaluation. The character numerator is then divided
by \(24\cdot120\), with exact divisibility checked
at every entry.

All 120,960,000 constants agree with the author's
certificate. In particular:

- all seven serialized table hashes agree;
- every minimum and maximum agrees;
- all twenty-five inactive orders vanish;
- all fifty-five active orders are positive on every
  residue cube, including the zeroth order;
- the minimum positive-order constant is \(3477\);
- the maximum constant is \(177897162600\);
- every zero list is empty.

An absolute coefficient sum evaluated at residue bound
fifty-nine proves a bound of \(512343828288000\) on all
signed-64 intermediate numerators. This is established
with Python integers before the corresponding array
operations. The full receipt is
THREE_DEFECT_INDEPENDENT_RECEIPT.json.
The independent phase and complete domination polynomials
are retained in THREE_DEFECT_DOMINATION_RECEIPT.json.

## The \(b=0\) branch and the lattice maps

The actual symmetric quotient sequence gives F.9,
including \(x=0\). Its initial negative index is
\(-1\), and each closed trace is exactly zero there.
The identity has total degree five and separate degrees
at most three. Nonidentity \(x\)-degree is at most two.
These facts prove that only order \((3,3)\) vanishes
among the sixteen candidate orders.

The complete two-variable certificate program was read,
including all recurrences, exact divisibility checks,
overflow bound, hash order and all listed zeros. Its
403,200-entry stream was not independently rerun in
A-049; the rectangular agent separately reported its
own complete replay. That event belongs to its own
ledger and is not counted as a computation by this
agent. A-048 independently checked the underlying
cohomology corrections using literal stabilizer
matrices.

For both branches, the finite Newton identity uses
the stated residues modulo sixty. Its binomial factors
are exactly increasing-subset chains. The coefficient
interval has precisely the constant's number of
integer points. This verifies the exported polytope
dimensions: at most ten variables for the three-variable
branch and eight for the two-variable branch. The
effective outer label uses the sign already checked.

The valid \(b=0\) zeros in F.11 exclude the invalid
origin \((x,K)=(0,0)\). Positivity of each first-order
constant excludes any further zero beyond the residue
square. The seven valid exceptions, the complete
support claim for \(b\ge1\), and every partition
endpoint therefore follow with exactly the stated
ranges.

