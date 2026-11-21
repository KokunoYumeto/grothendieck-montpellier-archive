# DP41-M: a nonzero bounded multiplier cannot clear the exponential

Finding scope: strengthening of the elementary lemma in **DP41**, available to **DP42**. Proposed by `/root` and independently checked and written out by `/root/archive_binomial`, GPT-6 Astra Pro; runtime reasoning effort not exposed. Date: 2026-11-21 UTC. This is not a new global theta claim.

## Statement

Let \(R\) be a complete discrete valuation ring of mixed characteristic \((0,p)\), with p odd, fraction field \(K\), uniformizer \(\pi\), and residue field \(k\). Normalize \(v(p)=1\), and put \(s=1/(p-1)\). Let \(\mathbf Z=(Z_1,\ldots,Z_m)\) be finitely many variables. Suppose

\[
z\in K[[\mathbf Z]],\qquad z(0)=0,\qquad
\nu(z)=t\in[0,s),
\]

where \(\nu\) is the infimum of coefficient valuations and the coefficients of z are bounded below. Choose \(\mu\in K\) with \(v(\mu)=t\), and suppose

\[
Q=\overline{\mu^{-1}z}\in k[[\mathbf Z]]
\]

has a nonzero formal partial derivative. Then, for every nonzero series f with bounded coefficient valuations,

\[
\boxed{\quad\nu\bigl(f\exp z\bigr)=-\infty.\quad}
\]

No unit-constant-term or primitive-initial-form hypothesis on f is needed. The derivative hypothesis is invariant under changing the normalizing scalar \(\mu\). No perfection hypothesis on k is needed.

## Complete proof

Let

\[
\mathcal B=R[[\mathbf Z]][1/\pi],\qquad
\mathcal F=\operatorname{Frac}(\mathcal B).
\]

Because the value group is discrete, \(\mathcal B\) is exactly the ring of formal series whose coefficient valuations are bounded below. For a nonzero element of this ring the minimum coefficient valuation is attained. The Gauss minimum is multiplicative: divide two series by scalars realizing their respective minima and reduce modulo \(\pi\); the product of two nonzero series in \(k[[\mathbf Z]]\) is nonzero. Consequently \(\nu\) extends to a valuation on \(\mathcal F\) by

\[
\nu(A/f)=\nu(A)-\nu(f).
\]

Its valuation ring is

\[
\mathcal V=R[[\mathbf Z]]_{(\pi)},
\]

and its residue field is \(\operatorname{Frac}(k[[\mathbf Z]])\). Indeed, remove the powers of \(\pi\) realizing the numerator and denominator minima. A quotient has nonnegative valuation exactly when it can be written with integral numerator and a denominator whose reduction is nonzero. Reducing such fractions inverts every nonzero element of \(k[[\mathbf Z]]\), proving the residue-field description. This argument does not require \(\mathcal V\) itself to be complete.

Put \(E=\exp z\). The estimate from DP41 is valid coefficientwise:

\[
\exp(pz)\in R[[\mathbf Z]]^\times,
\qquad
\nu(\exp(pz)-1)=1+t,
\qquad
\overline{\frac{\exp(pz)-1}{p\mu}}=Q.
\tag{M1}
\]

For completeness, the first exponential term has valuation \(1+t\). Every term of exponential order \(n\ge2\) has valuation at least

\[
n(1+t)-v_p(n!)
\ge1+t+(n-1)(1+t-s)>1+t,
\]

because p is odd. This proves all assertions in (M1); each fixed formal coefficient receives only finitely many exponential terms.

Suppose, toward a contradiction, that a nonzero \(f\in\mathcal B\) satisfies \(A=fE\in\mathcal B\). Then \(E=A/f\) belongs to \(\mathcal F\). The formal identity

\[
E^p=\exp(pz)
\]

and the constant-one integral unit on its right imply \(p\nu(E)=0\). Therefore \(E\in\mathcal V^\times\). Reducing the identity gives \(\overline E^p=1\) in the residue field, hence \(\overline E=1\). Since z is nonzero and has zero constant term, \(E\ne1\). Thus

\[
\delta=\nu(E-1)>0
\]

is finite.

If \(\delta\ge s\), the binomial expansion gives

\[
\nu(E^p-1)\ge\min(1+\delta,p\delta)
\ge1+s>1+t,
\]

contradicting (M1). If \(\delta<s\), the last binomial term \((E-1)^p\) has valuation \(p\delta\), strictly smaller than every term \(\binom pj(E-1)^j\) for \(1\le j<p\). Thus \(p\delta=1+t\).

Choose \(\alpha\in K\) with \(v(\alpha)=\delta\), and put

\[
r=\overline{(E-1)/\alpha}
\in\operatorname{Frac}(k[[\mathbf Z]])^\times,
\qquad
c=\overline{\alpha^p/(p\mu)}\in k^\times.
\]

The unique lowest binomial term and (M1) now give

\[
Q=c\,r^p
\quad\text{in }\operatorname{Frac}(k[[\mathbf Z]]).
\]

Every formal partial derivative on \(k[[\mathbf Z]]\) extends to its fraction field by the quotient rule. In characteristic p it kills \(c r^p\), since c is a scalar in k. This contradicts the assumed nonzero partial derivative of Q, whose image in that fraction field remains nonzero. Therefore \(fE\notin\mathcal B\), proving the claimed unbounded coefficient denominators. ∎

## Exact scope for later use

The lemma applies after a chosen contraction if z satisfies the displayed boundedness, minimum, and derivative conditions there, and if the contracted multiplier is nonzero and bounded. A multiplier may vanish to positive order at the origin. An identically zero restriction is excluded, since it trivially kills the product.

The result does not prove those hypotheses for a geometric path or theta section. It also does not prevent a selected differential functional or harmonic projection from missing all coefficients of negative valuation. Those are separate questions.

## Check record

The root proposed the fraction-field argument after the complete DP41 review. This reviewer independently verified the localization, residue field, valuation normalization, reduction of E, both binomial cases, and the derivative extension, then wrote and read this complete proof. The exact closing time, complete-proof hash, and actual event **ABA-CE38** are recorded in the reviewer logs and companion metadata. This is a checked extension of the proof, not a claim that it was already present in the earlier DP41 snapshot.
