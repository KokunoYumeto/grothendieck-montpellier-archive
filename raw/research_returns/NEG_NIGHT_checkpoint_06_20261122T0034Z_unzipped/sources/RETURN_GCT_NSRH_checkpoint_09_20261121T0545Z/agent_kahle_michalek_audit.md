# Primary-source and independent proof audit: the known PH1 Ehrhart obstruction

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 UTC. Check type: complete primary-paper read, exact statement/version match, and an independent coefficient derivation plus reciprocity proof. No priority claim, numeric interpolation or formal-kernel check is made.

## 1. Known result and exact scope

Thomas Kahle and Mateusz Michałek, *Obstructions to combinatorial formulas for plethysm*, Electronic Journal of Combinatorics **25(1)** (2018), P1.41, **Theorem 5 and Remark 6, printed p.4**, give a non-Ehrhart stretching ray. The paper explicitly identifies the fixed-inner-weight question with VI Hypothesis 1.6.4 on p.2. Its pp.3–4 separately discuss the 2011 inhomogeneous amendment: their result excludes a one-dimensional inhomogeneous model, but does not settle every higher-dimensional inhomogeneous model. This is the paper's stated scope, not a claim about its status after 2018.

Primary source: <https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p41/pdf/>. Independently retrieved source reference: `turn599140166view0`. The complete nine-page source was read, including the full theorem proof and following qualifications.

In VI's outer/inner/output notation the relevant fixed labels are

\[
\lambda=(4),\qquad \mu=(3),\qquad \pi=(7,5).
\]

The known ray is

\[
\phi(s)=a_{(4s),(3)}^{(7s,5s)}
=\frac{s+r(s)}3,
\qquad
(r(0),\ldots,r(5))=(3,-1,1,0,2,-2),
\tag{K1}
\]

where `r` is periodic of period six. This matches VI's fixed-inner-weight stretch exactly. The source also gives the Hermite-reciprocal presentation with outer degree three and stretched inner degree `4s`; that second presentation is not needed for the contradiction to VI.

## 2. Independent derivation of the exact ray

Here is a direct calculation of (K1) from binary weights, without relying on the interpolation route mentioned in the source proof. Work in `Sym^(4s)(Sym^3 C^2)` and extract the irreducible with highest weight `(7s,5s)`. The second part `5s` is at most half the total degree `12s`, so the adjacent-weight rule gives

\[
\phi(s)=[t^{5s}](1-t){4s+3\brack3}_t
=[t^{5s}]
\frac{(1-t^{4s+1})(1-t^{4s+2})(1-t^{4s+3})}
     {(1-t^2)(1-t^3)}.
\tag{K2}
\]

This adjacent-weight rule follows directly because every GL2 irreducible of fixed total degree contains each weight between its two extreme weights once. It is also the complete two-variable calculation in PPS Lemma 1.3, independently read for the F34 audit.

Let

\[
p(n)=\#\{(a,b)\in\mathbb Z_{\ge0}^2:2a+3b=n\},
\]

with `p(n)=0` for negative `n`. No product of two numerator exponents in (K2) can contribute at degree `5s`, since the least such exponent is `8s+3>5s` for every `s>=0`. Therefore

\[
\phi(s)=p(5s)-p(s-1)-p(s-2)-p(s-3).
\tag{K3}
\]

For `n=6t+j`, `0<=j<=5`, direct enumeration of the parity-compatible possible `b` gives

\[
p(6t+j)=t+\epsilon_j,
\qquad (\epsilon_0,\ldots,\epsilon_5)=(1,0,1,1,1,1).
\tag{K4}
\]

The formula is valid for every `n>=0`; it also assigns the required zero to `n=−1,−2,−3`, the only negative arguments needed in (K3). Substitute `s=6t+j` into (K3) and apply (K4). The six residue calculations give

\[
\phi(6t+j)=2t+\eta_j,
\qquad (\eta_0,\ldots,\eta_5)=(1,0,1,1,2,1).
\tag{K5}
\]

For example, these constants can be checked uniformly from

`eta_j=floor(5j/6)+epsilon_(5j mod6)−sum_(h=1)^3(floor((j−h)/6)+epsilon_((j−h) mod6))`.

Since `r(j)=3 eta_j−j`, equation (K5) is exactly (K1). This derivation establishes the complete ray and its quasipolynomial extension, not just finitely many sampled multiplicities.

## 3. The ordinary Ehrhart contradiction

The quasipolynomial gives

\[
\phi(1)=0,\qquad \phi(-1)=\frac{-1+r(5)}3=-1.
\]

If a rational polytope `P` had this Ehrhart function, Ehrhart–Macdonald reciprocity would identify `|phi(−1)|` with the number of integral points in its relative interior, while `phi(1)` counts all integral points in `P`. The former set is contained in the latter. Here it would have one point while the containing set has none, a contradiction.

This excludes every rational polytope, with no dimension assumption. Allowing a rational unbounded polyhedron does not help: at an index with a nonzero finite count, an integral point together with any nonzero rational recession direction would give infinitely many integral points after multiplying that direction by an integer. Thus a rational polyhedron producing all these finite nonzero counts must be bounded.

The underlying coefficient is still nonnegative for every nonnegative stretch. The obstruction is specifically to one ordinary dilation-polytope formula, not to representation multiplicities, positivity, or every possible combinatorial interpretation.

## 4. Check of the source's stronger one-variable inhomogeneous argument

The source's proof additionally treats a system of rational inequalities in one counting variable. I checked the eventual-interval reduction, the common-period extension of its counting quasipolynomial, and the endpoint-increment contradiction. There is one small implicit justification worth making explicit when reproducing it: extend the floor/ceiling formula quasipolynomially first; eventual equality then gives equality on all residue classes, and nonnegativity of `phi` ensures the formula also agrees with the actual count when the initial interval could be empty.

The period-six values have an increment of two from `s=5` to `s=6` and a drop from `s=0` to `s=1`. After an integral translation normalizes the lower-endpoint slope into `[0,1)`, the first increment forces the upper-endpoint slope to exceed one, which makes every increment nonnegative. This contradicts the drop. The source's conclusion for its one-variable inhomogeneous interval model therefore passes. It must not be upgraded to nonexistence of every higher-dimensional inhomogeneous model.

## 5. Consequence for the report's claims

The paper should cite this established theorem for the historical failure of universal ordinary Ehrhart existence in the supplied VI target. The independently reconstructed F34 family makes a separate point: even a ray with a positive simplex model can require dimension exponential in the compact input length. Neither fact becomes a new purity theorem, and neither justifies treating every later amendment as refuted without checking its own exact parameters.

Suggested event: `KNOWN-KM-PH1-GCT-SOURCE-PROOF`, complete primary read, exact fixed-inner-weight match, independent coefficient calculation and reciprocity contradiction, PASS. The proof of the source's inhomogeneous one-variable assertion was checked with the explicit initial-interval clarification above. No long external theorem proving Ehrhart reciprocity itself was re-proved in this check.
