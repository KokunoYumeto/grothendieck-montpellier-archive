# DP41: independent complete-proof review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Actual review interval: **02:10:05–02:14:48 UTC**. Event **ABA-CE37**. Main paper not edited.

## Outcome and exact scope

**PASS for the complete corrected memo identified below.** I read its whole statement, §§2–6 proofs, §7 scope, and §8 source attribution, independently recomputed the decisive algebra, and then reread the entire current version after the finite-support and inverse-limit refinements. The theorem proves, for odd primes, every stated height, the specified invariant primitive splitting, and every unit scalar \(\lambda\),

\[
w_{a\mathbf r}(\exp(\lambda\beta))=
\begin{cases}
-\infty,&0\le a<p,\\
0,&a\ge p,
\end{cases}
\]

for nonnegative rational \(a\). The same threshold holds in the specified integral group coordinates and after the stated integral-unit prefactor. This is the exact threshold in the given family of multivariate weights. It does not supply sharpness on a prescribed diagonal, after a chosen harmonic projection, or for a global theta construction.

No remaining mathematical gap was found in this scope. This is a new substantive proof check, not a repetition of the DP38 finite-coefficient check.

## 1. Scope refinements during the review

The first live full-file read at **02:10:05 UTC** still stated the exponential obstruction over an arbitrary complete discretely valued extension using only a non-pth-power initial form. I identified the scalar-normalization issue over an imperfect residue field. The author reported an independent derivative-based correction at **02:10:36 UTC**, and the first saved snapshot already contains that correction. This review does not claim exclusive credit for prompting an edit already made independently.

The corrected lemma assumes a **nonzero formal partial derivative** of the initial residue series. This is exactly what the theorem's polynomial has. Over perfect residue fields it is equivalent to the stated non-pth-power condition; over imperfect fields it avoids a real problem. For example, let \(R\) be the completion of \(\mathbb Z_p[T]_{(p)}\), with residue field \(\mathbb F_p(T)\), and adjoin \(u\) with \(u^p=pT\). For odd \(p\),

\[
z=\log(1+uX)
\]

has minimum coefficient valuation zero and initial residue \(\overline T X^p\), which is not a pth power in that residue power-series ring, but \(\exp z=1+uX\) is integral. The nonzero-derivative hypothesis correctly excludes this example. The actual DP41 initial form has derivative \(-S^p\), so the main theorem never needs the overbroad version.

I also requested that finite ghost support be tied explicitly to the finite-support nilpotent Witt functor, rather than asserted for arbitrary infinite Witt vectors. The current memo does this. Finally, I supplied the quantitative divided-ghost bound in the next section to make the passage from the actual completed integral display quotient to the rational calculation explicit. The author incorporated that argument before the final complete reread.

## 2. Divided ghosts and the actual coordinate logarithms

I directly read **Zink (147)–(156), printed pp. 204–207**, including the divided-ghost description, the extended display operator, its shift formula, and the quotient exponential. The exact negative `hex` convention and quotient pairing formulas were directly checked in the preceding DP35/DP38 reviews: **Proposition 106, p. 226; (196), p. 232; (211), p. 236; and (218), p. 239**. The proof does not apply a theorem requiring a p-nilpotent base directly to a field where p is invertible.

For the constant cyclic display matrices, ordinary Witt Frobenius shifts ordinary ghosts. Dividing the nth ghost by \(p^n\) therefore makes the extended display operator exactly \(AT\), with \(T\) the left shift. Hence

\[
(AT-1)^{-1}=-\sum_{m\ge0}(AT)^m
\]

has the correct sign. The normal-decomposition condition is precisely the vanishing of the \(T\)-component of the zeroth ghost. The projected sum in (ER4) telescopes to minus that component on a display coboundary, and has identity differential.

The added inverse-limit argument is valid. On an ordinary-degree truncation with \(N^D=0\), put \(C=\lfloor\log_p(D-1)\rfloor\) for \(D>1\). Directly from the ghost polynomial,

\[
u_n(z)=\sum_{r=0}^{\min(n,C)}\frac{z_{n-r}^{p^r}}{p^r}.
\]

Thus the divided ghosts of integral Witt vectors have a uniform denominator bound, including in the completed resolution. Since \(A^h=p^d I\) and \((A')^h=pI\), the matrix powers tend p-adically to zero. The projected series converges and its telescoping boundary vanishes. It consequently descends through the actual integral inverse-limit quotient, before rationalization. For the specific Teichmüller and ghost-zero rational lifts later used, finite nilpotence and finite support make the displayed resolvent sums finite. These two observations justify the completed and rational calculations without silently interchanging their domains.

The line cycle has multiplier \(p^{md}\) after \(mh\) steps and ghost denominator \(p^{mh}\), giving exactly \(S^{q^m}/p^m\). On the dual side, the displayed recursion for the full ghost sum yields

\[
C=p^{-1}L_d(Y^p),\qquad
L_1=Y_1+p^{-1}L_d(Y^{p^2}),\qquad
L_i=Y_i+p^{-1}L_{i-1}(Y^p).
\]

These uniquely determine the normalized formal series and are precisely the DP32 equations. Thus the new calculation genuinely identifies the whole Teichmüller-coordinate logarithm with that model; it is stronger than matching special fibres or tangent characters. The complementary component has first path length \(h-j\) and one numerator factor p per subsequent cycle, giving denominator \(p^{dl+h-j}\) in (ER6).

## 3. Rational sections, exact pairing sign, and cycle counts

The lifts with only a zeroth divided ghost are additive in the logarithm variables. Their scalar-one quotient section is compatible with both partial laws. The resolvent lifts \(k,l\) in (ER7) have the required zero zeroth-ghost projection, so lie in the appropriate rationalized \(Q\) modules.

I recomputed the frame comparison in both stages. The Teichmüller frame differs from the additive frame by

\[
\operatorname{hex}\langle V^{-1}k,\tau\rangle\,
\operatorname{hex}\langle g_0,l\rangle^{-1}.
\]

The representing splitting is its inverse. Using the negative source convention and the factor \(p^n\) from multiplying ordinary ghosts gives the negative double sum and positive \(L_0C\) in (ER9), exactly as stated. In particular no extra factor p, no inverse-sign error, and no missing bilinear term occurs.

For the first sum, a path of length \(lh+j\) has matrix multiplier \(p^{dl+j-1}\). Combining it with both divided-ghost denominators and their pairing factor leaves \(p^{-n-l-1}\), proving the first denominator and exponents in (ER10). The separate computation of \(C\) gives the second sum. At fixed ordinary degree all contributions are finite; possible support overlaps are permitted and are not mistaken for disjointness.

Every term has the required actual torus character. The additive lifts are equivariant, both axes are normalized, and no invariant bilinear gauge exists. Consequently the formula is the unique invariant splitting of the same actual primitive display biextension, not a scalar series guessed from its first terms.

## 4. Exact contracted minimum and its residue polynomial

All direction weights are positive. Choosing input scales as powers of one uniformizer makes each first monomial's scalar exactly the same \(\mu\), because

\[
p^jr_0+r_j=s,\qquad r_0+pr_d=s.
\]

This is an equality of the chosen powers, not merely an equality of their valuations. Dividing by p gives \(v(\mu)=as-1=t\).

For the first family I independently obtained

\[
a s(p^n-1)-n+a p^{n+j}\rho(q^l-1)-l.
\]

At \(a\ge p-1\), its first part is bounded below by \(p^n-1-n\), strictly positive for \(n>0\) because p is odd. The other part is strictly positive for \(l>0\). Thus only \(n=l=0\) remains at the minimum, for every j.

For \(L_0C\), the weight decomposition (ER13) and its three lower bounds give exactly

\[
(p-2)u+(q-p-d)l+(p^k-p-k+1).
\]

Each summand is nonnegative and positive off \(u=l=0,k=1\). In particular \(q-p>d\) is valid at the smallest boundary \(p=3,h=2\) and increases thereafter. This leaves only \(+\mu SY_d^p\). The surviving monomials are distinct, while every other contributing summand has strictly larger valuation; overlaps cannot cancel the minimum. Therefore

\[
\nu(b_a)=t,\qquad
\overline{\mu^{-1}b_a}=-\sum_{j=1}^dS^{p^j}Y_j+SY_d^p.
\]

Its \(Y_1\)-derivative is \(-S^p\), including at \(d=1\). Multiplying by the residue of a unit scalar retains that nonzero derivative.

## 5. Exponential obstruction and both endpoints

For the corrected elementary lemma, \(\exp(pz)-1\) has exact minimum \(1+t\), because all exponential orders at least two have strictly larger valuation. If \(E=\exp z\) were integral, reduction gives \(\overline E=1\). The minimum \(\delta=\nu(E-1)\) exists by discreteness.

If \(\delta\ge s\), every term of \(E^p-1\) has valuation at least \(1+s>1+t\), a contradiction. If \(\delta<s\), its uniquely dominant binomial term is \((E-1)^p\), whose residue initial form has all partial derivatives zero even after an arbitrary scalar normalization. This contradicts the nonzero derivative of the initial form of \(pz\). Bounded denominators are also impossible: Gauss multiplicativity and \(E^p=\exp(pz)\) would force \(\nu(E)=0\), hence integrality. The conclusion is genuinely \(-\infty\), not merely a negative finite bound.

This applies to the full interval \(p-1\le a<p\), including its lower endpoint \(t=0\). At \(a=p\), the minimum reaches \(s\), and the factorial estimate makes the exponential integral, including this endpoint. Its constant coefficient forces minimum zero. The lower range \(a<p-1\) follows by monotonicity. The proof does not extrapolate its strict odd-prime inequalities to p=2.

## 6. Coordinate equivalence, units, and limits of the result

I reread the relevant DP32 contraction formula. Its m-step weight increment is at least m. Thus for every \(a\ge1\), the contracted dual logarithm and line logarithm are integral identity-linear maps, with integral inverses. Substitution preserves the extended Gauss infimum: use both inequalities in the bounded case, and apply the inverse to a hypothesized bounded transformed series in the unbounded case. This proves equality of the two coordinate versions of the radius assertion. Monotonicity handles \(a<1\).

An integral group-coordinate unit and its inverse remain integral under contraction; after the integral exponential-coordinate change they remain so for \(a\ge1\). Multiplication therefore preserves the finite minimum or its failure to be bounded. Monotonicity again covers the remaining range. The prefactor assertion is valid for the stated integral unit, and does not silently assume that an arbitrary rational gauge is integral.

The result fixes the invariant representative and the indicated weight family. It does not imply the same threshold after an arbitrary rational bilinear gauge, after specialization to a fixed path, or for selected harmonic values. In height two the two opposite first monomials can already cancel on the diagonal. An exact multivariate threshold therefore does not prove optimality of the sufficient one-variable residual, nor a lower bound for a global theta or chain cost.

## Exact checked version

The complete final memo was read and captured after all refinements, at the closing clock **02:14:48 UTC**.

| Scope | SHA-256 |
|---|---|
| First saved intermediate snapshot, already containing the author's independent derivative correction | `888f9c4f947bff9e9f31598607240645339a96f47fc19e388cb36c1df6c34772` |
| Complete corrected memo | `fc4df00d49ae3041955208877cb70429c6a49471633565f138bfccf6ca916185` |
| Complete statement, proofs, and scope, §§1–7 | `1d0959f208bc50d52aed297ba94d44b63abc3e64e9a74f655f6581b49aa80ba5` |

The final snapshot is `late_proof_snapshots/DP41_complete_corrected_checked.md`, with metadata in `late_proof_snapshots/DP41_check_metadata.json`. The proof-scope hash begins at `## 1. Statement` and stops immediately before `## 8. Sources`, preserving whitespace. This record is a manual independent complete-proof challenge; it does not certify later main-paper integration, cite a numerical experiment as proof, or claim a machine formalization.
