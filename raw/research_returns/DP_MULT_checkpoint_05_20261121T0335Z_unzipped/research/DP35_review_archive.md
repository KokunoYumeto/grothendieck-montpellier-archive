# DP35: independent complete-proof review

Reviewer: `/root/archive_binomial`, GPT-6 Astra Pro, inherited model; runtime reasoning effort not exposed. Date: 2026-11-21 UTC. Review interval **01:51:02--01:56:30 UTC**. Event **ABA-CE34**. No main-paper edits were made.

## Outcome and exact scope

**PASS. The current complete draft proves its stated denominator-rigidity results and their application to rational compatible splittings of the actual nonzero Poincaré class.** I read all statements and proofs in §§1--6, challenged them, directly checked the pertinent Zink statements/formulas, and then read the complete saved version after the author incorporated three explicitness suggestions at 01:54:59 UTC.

Those incorporated additions are: returning from additive logarithm coordinates to the original integral group coordinates; proving identity-class $p$-primitivity by its differential rather than treating nonzero reduction as a primitivity criterion; and justifying existence of the display lifts by Lemma 111 and normal decomposition (145). No remaining mathematical gap was found.

This is a manual whole-draft review, not a check of a later main-paper integration or an audit of the complete proofs of Zink's cited classical results.

## 1. Bounded denominators and contraction

The minimum Gauss valuation of a bounded-denominator series exists over the stated discrete value group. Its multiplicativity follows from reduction of suitably rescaled series to the residue power-series domain. It does not require restricted analytic series or a least-degree coefficient realizing the valuation.

The repeated-addition formula (P2) has the correct factors and orientation. Integral substitution cannot decrease the minimum valuation; multiplication by the constant-one integral unit contributes zero. Thus the inequality $\nu(B)\le p\nu(B)$ correctly forces $\nu(B)\ge0$. The constant coefficient one then makes $B$ an integral unit. The argument uses only the first coboundary and is valid over ramified complete DVRs.

For positive rational $t$, the auxiliary finite extension with $v(\lambda)=t$ exists. The rescaled group law is integral because each nonlinear coefficient receives the nonnegative power $\lambda^{d-1}$. Scaling all the variables gives exactly the stated new coboundary. A finite weighted infimum would therefore give a bounded-denominator contracted series and, by part (a), an integral one. Its constant term ensures the infimum is zero. This proves the dichotomy.

The degree argument in (P4)--(P5) is valid: unboundedly negative weighted coefficients must have unbounded total degrees, and their valuation-to-degree ratios give a liminf at most $-t$. Taking rational $t$ up to the threshold proves the claimed positive rate. It gives neither a canonical best rate nor a rate uniform over all choices of splitting.

## 2. Units and primitive initial forms

The unit-frame argument applies the integral inverse of the frame unit and is immediate. The primitive-initial-form extension does not assume that the unknown factor is bounded. Its homogeneous-degree induction works with finite homogeneous polynomials at each step; the primitive first piece has Gauss valuation zero, so its product cannot conceal a negative valuation in the next unknown homogeneous piece.

The counterexample with $p-z$ correctly shows why an arbitrary multiplier is not covered. It is expressly an algebraic warning, not a proposed cocycle satisfying the formal-group hypotheses. A primitive coefficient somewhere else in a jet matrix does not automatically give the required primitive first homogeneous part of a scalar section.

## 3. Rational splitting and its coordinate normalization

The scalar cocycle identity differentiates with the displayed sign. Integrating its derivative gives $\delta_x\beta_0=A$. The interchange identity then makes the remaining error additive in the scalar variable, hence linear in that variable.

For the vector cocycle, commuting the differentiated identities makes $\partial_jb_i-\partial_ib_j$ constant; symmetry of the cocycle kills that constant at the origin. The radial primitive consequently has the stated derivatives, and normalization gives $\delta_y\gamma=d$. Thus $\beta=\beta_0-x\gamma$ solves both equations with the correct signs and axes. The differences of two normalized solutions are precisely the stated rational bilinear gauges.

The author has now made explicit that the series to which the integral-coordinate rigidity theorem applies is

\[
B(S,T)=\exp\beta(\log_F(S),\log_H(T)).
\]

This is necessary bookkeeping: rational logarithm coordinates do not by themselves preserve the integral function ring. The amended proof uses the original integral cocycles after returning to those coordinates, so the application of §§1--2 is legitimate.

## 4. Integral frames and their inverse limit

Zink's **Lemma 111, printed p. 230**, has the stated exact-functor/prorepresentable-base hypotheses. The formal multiplicative group is exact on nilpotent test algebras, so it applies to the underlying formal torsor. The resulting frame is distinguished from a section compatible with both partial group laws.

The newly explicit compatible-frame construction is sound. Two axis-normalized frames modulo $p^n$ differ by a unit equal to one on both axes. Such a unit has a lift with the same normalization modulo $p^{n+1}$, by lifting its mixed coefficients. Adjusting the chosen higher-level frame makes the reduction agree. Thus the frames, cocycles and their identities have a coefficientwise inverse limit over $R$; the argument is not attempting to pass unrelated trivializations to the limit.

The nilpotent-base and connected-dual conditions in the application match Zink's **Proposition 121, (243), diagram (244) and Theorem 122**. The identity class is nonzero. Its claimed $p$-primitivity is now explicitly justified: the differential of $p$ times an integral endomorphism is divisible by $p$, whereas the identity differential is one. Nonzero reduction is correctly treated as a separate assertion.

An integral normalized compatible $B$ would trivialize both partial laws, contradicting this nonzero class. Consequently the purely algebraic rigidity and contraction conclusions apply to every such rational splitting. The argument for nonzero integral powers and, at odd $p$, half-integral powers is also valid: their integral cocycles exist, and their classifying homomorphisms are nonzero in the torsion-free endomorphism group.

## 5. Display cocycles and signs

I directly read the primary extracted text of **Zink Theorem 81 and (145)--(146), printed p. 204**, **Proposition 106, p. 226**, **Lemma 111, p. 230**, and **(216)--(218), pp. 238--239**. Normal decomposition makes the functors denoted $Q,Q'$ exact, so Lemma 111 supplies the normalized set-theoretic lifts. Injectivity of the displayed resolution map supplies uniqueness of the defects.

The quotient relation in Proposition 106 has the sign used in (P8). In multiplicative notation it gives

\[
e(g,h)e(g',h)=\alpha_1(\kappa_G(g,g'),\tau(h))\,e(g+g',h).
\]

For a compatible section $B e$, the equation is therefore $B(g+g',h)/(B(g,h)B(g',h))=\alpha_1$, exactly the convention in (P1). The second partial law uses $\alpha_2$; the minus sign in Zink (218) becomes an inverse. Thus both (P8) and (P9) have the correct signs. The interchange terms are already encoded in the agreement of these maps on the two kernel functors.

## 6. Scope that remains essential

The conclusion concerns all coefficients of a rational compatible splitting in the specified integral group coordinates. It does **not** prove nonintegrality of a prescribed selected jet family, an exponential-conjugated differential expression, or a harmonic projection. Such operations can retain or restore integrality without making the entire splitting integral. The draft explicitly preserves this limit.

Neither the nonintegrality result nor the positive denominator-rate result supplies a global theta-cost obstruction by itself. No universal normalization-independent numerical rate is asserted. These qualifications are mathematically appropriate and remain present in the reviewed version.

## Exact checked version

The complete current draft is preserved in `late_proof_snapshots/DP35_draft_checked.md`, 15,640 bytes.

| Scope | SHA-256 |
|---|---|
| Entire draft | `4a7273b5788a7bc533b39995f1ef845f6003efd3ac3d51080d9c910c1e9573e9` |
| Complete statements and proofs, §§1--6 | `3c031008966fed92a8a86a9bd090b40fb8481284f7e564f0d3c73f5e94f0c1fe` |

The section hash starts at `## 1. Algebraic statement` and stops immediately before `## 7. Primary-source provenance`, preserving all original intervening whitespace. Actual event **ABA-CE34** records this full review in both reviewer logs. The three author amendments are included in these hashes.
