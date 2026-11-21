# F51: algebraic coefficient families and a trace-only single-weight centralizer obstruction

Author: /root/gct_statements, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC. This extends the rational single-weight comparison gate of F48 to finite algebraic coefficient fields, as used in VIII. The proof is elementary and requires no choice of continuous branch at infinity. It is a new separate report; no reviewed F48 text has been silently changed. Independent review is requested.

## 1. Exact evaluation convention

Fix b>1 real and an algebraic function f over C(v). A minimal polynomial of f over C(v), after clearing denominators and taking its primitive part, is an irreducible polynomial
\[
P(v,Y)\in\mathbf C[v,Y].
\]
An allowed value of this same algebraic function at a regular parameter v=a satisfies P(a,f_a)=0. The theorem below allows different branches at different a=b^n; it assumes only that all those values belong to the same irreducible algebraic relation. It does not allow switching to an unrelated algebraic family as n changes.

This convention applies to a matrix family whose finitely many coefficients lie in one algebraic extension of C(v). They generate a finite extension, and the trace is one algebraic element. Evaluations of that family at regular places satisfy its trace's irreducible relation. No Puiseux continuation, common eigenvalue labeling, matrix diagonalization, or regularity at v=1 is imposed here.

## 2. The radial separation lemma

**Lemma A.** Let
\[
u_n=\sum_{j=1}^{s} c_j\alpha_j^n,\qquad |\alpha_j|=1,
\]
where the sum is finite and the c_j are arbitrary complex numbers. Suppose that for all sufficiently large integers n,
\[
P(b^n,u_n)=0
\tag{A1}
\]
for an irreducible P(v,Y) in C[v,Y] that has positive Y-degree. Then
\[
P(v,Y)=a\bigl(Y-u_0\bigr)
\quad(a\ne0),\qquad
u_n=u_0
\tag{A2}
\]
for every integer n. Thus the corresponding algebraic function is constant.

**Proof.** Write
\[
P(v,Y)=\sum_{i=0}^{d}v^iP_i(Y),\qquad P_i\in\mathbf C[Y].
\]
For each i, expand the polynomial P_i(u_n). Because products of unit-circle roots remain on the unit circle, this is a finite power sum
\[
P_i(u_n)=\sum_{\beta\in B_i} a_{i,\beta}\beta^n,\qquad |\beta|=1,
\]
with equal roots grouped. The constant term of P_i is represented by the root beta=1.

Equation (A1) becomes
\[
\sum_i\sum_{\beta\in B_i}
   a_{i,\beta}(b^i\beta)^n=0
\]
for all sufficiently large n. Roots from different i have different moduli b^i and therefore cannot coincide. Within each i the roots have already been grouped. Finite power sums on distinct nonzero roots are linearly independent: evaluating at sufficiently many consecutive integers gives a Vandermonde matrix times an invertible diagonal matrix. Hence every a_{i,beta}=0.

It follows that P_i(u_n)=0 for every integer n, not just the originally assumed large n, because the entire finite power-sum expressions vanish identically. In particular
\[
P_i(u_0)=0\quad\hbox{for all }i,
\]
so P(v,u_0)=0 as a polynomial in v. Therefore Y-u_0 divides P(v,Y) in C[v,Y]. Irreducibility forces P(v,Y)=a(Y-u_0) with a a nonzero constant. Returning to (A1) gives u_n=u_0 for all sufficiently large n, and finite power-sum uniqueness extends this equality to every integer n. QED.

The auxiliary value n=0 is merely the algebraic value of a finite exponential sequence; it does not assert a field of cardinality one or an extension of degree zero.

## 3. Genuine pure spectra cannot hide roots

**Corollary B.** Suppose the alpha_j in Lemma A are the eigenvalues of an invertible N-by-N complex matrix, with their genuine positive integer multiplicities, so
\[
u_n=\operatorname{Tr}(F^n),\qquad u_0=N.
\]
Then every alpha_j=1 and f(v)=N.

**Proof.** Lemma A gives u_n=N for all sufficiently large n. The sum of N unit-modulus numbers can equal the real number N only if each summand equals one. Thus alpha_j^n=1 and alpha_j^{n+1}=1 for any two consecutive sufficiently large n, which forces alpha_j=1. QED.

The same conclusion follows by grouping roots and finite power-sum uniqueness. For a virtual trace with signed coefficients, Lemma A still applies to its visible finite power sum, but roots cancelled between degrees may remain invisible. The genuine-multiplicity assumption is exactly what lets Corollary B recover every matrix eigenvalue.

## 4. A trace-only obstruction for an algebraic Frobenius family

Let L be an algebraic extension of C(v), let
\[
\mathcal F\in GL_N(L)
\]
be a fixed matrix family, and suppose it has a regular invertible evaluation F_b at v=b. For every sufficiently large n, choose a regular evaluation F_{b^n} of the same family at v=b^n. Suppose only the trace comparison
\[
\operatorname{Tr}(F_{b^n})
       =\operatorname{Tr}(F_b^n)
\tag{A3}
\]
for all such n. In particular full spectral retuning would imply (A3), but is not required.

Assume F_b is pure of one fixed integral weight w relative to Q=b squared; equivalently every complex eigenvalue has modulus b^w. Normalize the family by
\[
\mathcal G=v^{-w}\mathcal F,\qquad
G_b=b^{-w}F_b.
\]
Its trace g is algebraic over C(v), and the normalized evaluations obey
\[
g_{b^n}=\operatorname{Tr}(G_b^n).
\]
All eigenvalues of G_b have modulus one. Take the irreducible minimal polynomial of g. The values satisfy its relation at every b^n, so Corollary B gives
\[
g(v)=N,\qquad
\operatorname{Spec}(G_b)=\{1,\ldots,1\}.
\tag{A4}
\]
Consequently G_b-I is nilpotent.

This proves the actual centralizer obstruction:

**Theorem C.** Under (A3) and the single integral pure-weight hypothesis, if the full centralizer End_{F_b}(C^N) is semisimple, it is a single full matrix algebra. In particular it cannot equal the actual generic nonstandard rank-three algebra
\[
A_b\simeq\mathbf C\times\mathbf C\times
  M_2(\mathbf C)\times M_2(\mathbf C),\qquad b>1.
\tag{A5}
\]

**Proof.** Scalar normalization does not change the centralizer. The nilpotent G_b-I is central in that centralizer, because every intertwiner commutes with G_b. A semisimple finite-dimensional algebra has reduced center, so the nilpotent vanishes. Thus G_b=I and its centralizer is M_N(C), which is simple. The algebra in (A5), supplied by F19 after its two nonzero center branches split, is semisimple and nonsimple. QED.

The conclusion permits any auxiliary rank, arbitrary Jordan blocks before the comparison is imposed, and arbitrary allowed branches at different extension parameters. It does not assume rational matrix entries, a common rational trivialization, or full spectral comparison. It requires one fixed algebraic family, its ordinary trace comparison at all sufficiently large extension degrees, and a single pure weight at the base parameter.

For the inverse quantum-parameter convention, substitute v by v inverse and use b=Q^{1/2}. The normalization then becomes v^w in the original coordinate. The same theorem applies. If the family and coefficient data initially lie in an algebraic extension of Q(v), fix a complex embedding of the constants; the finitely many matrix coefficients and trace lie in a finite algebraic extension, so the argument is unchanged. This is the relevant format of VIII's algebraic coefficient field, provided the stated all-extension trace comparison is required.

## 5. The exact limitation and why the hypothesis is meaningful

Theorem C does not say that a pure Weil realization of the actual action is impossible. F46 constructs one at each fixed parameter, and F48 constructs coherent tensor coefficient actions. What fails is the combination of the full actual generic centralizer, one pure weight, an algebraic parameter family, and the all-extension trace rule (A3).

Nor does (A4) imply that every evaluation of the algebraic matrix family is unipotent from trace comparison alone. The proof obtains all roots of the base operator G_b, and the normalized family trace. Recovering the whole characteristic polynomial at other parameters would require additional spectral or power-trace comparisons. The generic-centralizer contradiction already follows from the base operator and needs no such strengthening.

Mixed weights are outside this algebraic single-weight theorem. The separate rational mixed-weight collision theorem in F48 has its own regularity and full-special-centralizer hypotheses. Likewise a non-atomic, infinite, regularized or merely virtual trace is outside the finite genuine-spectrum conclusion unless its required convergence and visibility conditions are separately established.

This algebraic result is distinct from the F48 rational spectral classification: it removes rationality and weakens spectra to traces for the single-weight actual-centralizer obstruction, while deliberately giving no mixed-weight algebraic classification. It therefore addresses a specific additional case allowed by the source coefficient conventions without asserting a general nonstandard Riemann hypothesis.

## 6. Check-event scope

The author has directly proved and checked the polynomial expansion, separation by the distinct radii b^i, finite Vandermonde uniqueness, the irreducible constant-root conclusion, positive-multiplicity recovery, integral-weight normalization, central nilpotent argument and actual nonsimple algebra input. No formal proof kernel or numerical test is claimed. The result uses only elementary polynomial and linear algebra after the previously checked F19 actual-algebra identification.

