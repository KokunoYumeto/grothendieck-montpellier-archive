# A-087. Whole-proof audit of T060

**Status: PASS.** I read all of `work/theta/varying_hook/first_hook_report.md`, FH.1–FH.18 and all seven sections, and the complete `first_hook_positive.py` implementation. Its extra module-freeness statements, first-hook support and coin-polytopes pass. The common all-leg character, tableau and binary-degree arguments are also independently checked in A086.

## 1. Exact kernel and invariant-algebra section

The stable-chart and determinant-column maps give the stated sign-twisted first hook. The multiplication map $P\otimes E\to P_+$ is the actual differential, and the natural polarization satisfies $\delta\nabla=D$ in total degree $D$. Thus $1-\nabla\delta/D$ is the indicated projection onto its hook kernel.

The homogeneous coinvariant section is chosen over $\mathbb Q$ and averaged over the finite group; multiplication gives the graded equivariant free $I$-module isomorphism. For a nontrivial Specht label, its isotypic component contains no degree-zero target, so the kernel sequence surjects onto the full free multiplicity module.

For each homogeneous free target generator, the lift $\nabla/D$ is specified. Extending these chosen lifts $I$-linearly is an actual section. The proof does not require the gradient itself to be $I$-linear on arbitrary products. Its resulting direct summand is a finitely generated graded projective module.

Choosing lifts of a basis modulo $I_+$ gives a graded free cover. Graded Nakayama gives surjectivity; the projective splitting makes the quotient sequence exact modulo $I_+$. Its kernel has zero quotient, so graded Nakayama makes the kernel zero. This proves the claimed graded freeness through the actual chosen maps. Rational row reduction specifies every lift in finite degree. No polynomial-time claim is attached to constructing this potentially large free basis.

## 2. Numerator and trivial cycle module

The exterior trace specialization removes the factor at $(1,1)$. In exterior degree one, the nontrivial label has the specified $(2,1)$ term of content $-1$; multiplying by $q$ and subtracting the target cancels precisely that term. The remaining shifted fake degrees are nonnegative, with nonnegative exponents. The numerator degree bound $M+1$ follows from its exact coinvariant expression, whose two fake degrees lie in degrees at most $M$.

For the trivial label, Solomon's actual differential basis has scaled generators $\xi_i=de_i/i$ with $\delta\xi_i=e_i$. In a fixed positive invariant monomial degree, all available basis vectors map to the same monomial. Subtracting the unique least-support-index vector gives the explicit star basis FH.15. The least index and remaining exponent tuple are unique, proving the positive cell decomposition FH.16.

At $m=4$, multiplying that exact series by the specified invariant denominator gives $q^5+q^6+q^7-q^9$. A finite graded free module over this invariant algebra would have a numerator equal to the sum of its homogeneous basis degrees with nonnegative coefficients. The negative coefficient therefore proves precisely the stated failure of graded freeness for this trivial module. The positive star basis supplies its actual alternative presentation.

## 3. Support, polytopes and complexity

For every non-row label with $m\ge4$, the numerator has both its lowest degree and the next one. A nonrectangle supplies the next fake-degree coefficient; for a rectangle the retained cell weights supply adjacent minima. The stated column and two-row rectangle endpoints have those two cells. Coins two and three then give all subsequent degrees. The trivial branch has minimum five and also degree six, the latter from the $(2,4)$ tag. This is why the declared restriction $m\ge4$ is appropriate.

Each exported piece records the exact numerator-degree selector and a positive-weight coin equation, or one least-support-index pair. Every such polytope is bounded by that equation and the selector bound. The tag count and variable bounds follow from the proved numerator degree and index ranges.

The hook-product algorithm has degree $O(m^2)$ and polynomial coefficient bit lengths. The integer parity extraction keeps the full relevant numerator and squares denominator roots. The direct bound in A086 also proves the claimed polynomial bit complexity here. The explicit-size qualification at $t=0$ is retained.

## 4. Source and execution scope

In addition to the Macdonald, Solomon and Bostan–Mori readings recorded in A086, I independently read Stanley's primary article: Proposition 3.1, p482; Theorem 3.10 and its proof, p485; and §4 pp486–489, including the polynomial invariant ring and coinvariant quotient. The precise homogeneous quotient-basis criterion is the one used for the multiplication section. The source is work/theta/end_node/stanley_1979_invariants.pdf, publicly at https://sites.math.washington.edu/~billey/classes/reflection.groups/presentations/archive/stanley.1979.pdf.

The original 8,380 coefficient/parity comparisons, 7,920 support comparisons and its polytope/witness sweep remain attributed to theta's executed receipt. They were not rerun. A086's independent tableau, coin, matrix and huge-degree recurrence checks cover the common first-leg cases at $m=4,5,6$ as part of its explicitly recorded scope.
