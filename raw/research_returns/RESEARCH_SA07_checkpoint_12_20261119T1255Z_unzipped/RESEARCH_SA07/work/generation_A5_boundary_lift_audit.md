# Independent audit of the A5 integral boundary-moving lift

19 November 2026. Checker: GPT-6 Astra / period_generation. **Verdict: passed at the stated one-cover, non-Galois scope, including the IA strengthening.**

I read the full work proof `A5_integral_boundary_to_proper_counterexample.md` and the complete current `build_A5_boundary_nilpotent.py`, including its added base-homology certificate. I also opened and read original BCL v3, printed pp. 4–5, for the exact automorphism-group domains, extension-class condition, Gaschütz lemma, Corollary 2.4, and proof of Theorem 2.1.

## Actual integral modules and matrices

The right Cayley-edge convention `(h,j):h->h x_j` and the left deck action commute exactly. The BFS tree gives a genuine integral graph-cycle basis: its non-tree coordinates are the identity matrix. The x, y, and z=(xy)^(-1) cusp chains follow the displayed oriented words; the z chains use Y inverse followed by X inverse, with the corresponding reversed-edge signs. The 44 cusp cycles have the single sum relation and rank 43. Together with the actual compactification exact sequence, their image is the saturated boundary lattice.

The five-letter sum-zero representation V is absolutely irreducible by the two-transitive permutation action. The equivariant boundary map is well-defined because the chosen vector is x-fixed, and it kills the sum relation. The unimodular minor supplies the actual integral left inverse used for P0 and T0. Averaging P0 produces E with E squared equal to 60 E and image in the actual boundary space. Hence Q=60I−E kills boundary. The maps S=Q A_H and T=T0 E are equivariant, TS=0, and division by the explicitly computed common divisor ten produces an integral N. The displayed nonzero detector q factors through proper homology because qB=0 and gives qNb=19440.

I independently checked the retained matrices using arbitrary-precision SymPy integers, in addition to running the construction: N squared is zero, EN=0, NE=60N, qB=0, qNb=19440, eta transpose equals N b0 transpose, and N eta transpose is zero. The actual script's matrix-product guards and the small graph/averaging entries prevent fixed-width overflow; the independent exact-object checks confirm the decisive equalities.

## Cocycle sign and actual lift

For the specified Schreier section, the multiplication is `(m,h)(n,k)=(m+h n+c(h,k),hk)`. Its cocycle identity is

`c(h,k)+c(hk,l)=h c(k,l)+c(h,kl)`.

Summing over l gives `delta b0(h,k)=60 c(h,k)` for `b0(h)=sum_l c(h,l)`. Equivariance of N then gives `delta eta=(gamma−I)c`. This is exactly the sign required for `(m,h)->(gamma m+eta(h),h)` to preserve the displayed multiplication. Its inverse subtracts eta because gamma inverse eta equals eta, using N eta=0. These literal formulas extend continuously from L to its profinite completion.

Original BCL Corollary 2.4 lifts the specified automorphism of the quotient `Fhat2/closed[R,R]`, not merely its abstract module action. Applying it to this extension automorphism gives an actual continuous automorphism of Fhat2 inducing the identity on the specified A5 quotient. The action on the closed relation-module quotient is exactly gammahat. BCL Theorem 2.1 is also an exact surjectivity statement with these domains and the fixed extension class. Thus the invoked lift is valid. The commutator notation here is the closed commutator required by the maximal abelian profinite quotient.

The proper-homology failure is the literal nonzero quotient value `q gamma(b)=1166400`; it cannot arise from any map on the fixed quotient L/P because b maps to zero there. Positive powers give the same nonzero value multiplied by the positive integer exponent. A Galois element fixing this finite quotient would preserve its cusp inertia classes and hence the completed boundary module; the displayed failure rules out such a Galois lift directly.

## The IA conclusion

The exponent-sum map A is the actual pushforward from cover homology to the base's integral homology. I computed it from the full 120-by-61 cycle matrix by summing X-edge and Y-edge coefficients, and checked exactly that AN=0. The indicated columns have matrix `[[2,1],[-1,-1]]`, determinant −1, proving integral surjectivity. I also evaluated the two displayed words in the actual A5 permutations and obtained the identity, with their asserted exponent vectors.

Naturality for the actual inclusion of the profinite cover group gives `alpha_ab Ahat=Ahat gammahat=Ahat`. Surjectivity of Ahat therefore forces alpha_ab to be the identity. No choice of profinite lift can invalidate this deduction once its relation-module action is gammahat.

## Fresh run and scope

I ran an isolated copy, so the canonical work matrix file was not rewritten by this audit. The newly generated JSON matched the current retained JSON byte for byte.

- Exit code: 0.
- External wall time: 1.779917296 s; internal program time: 0.956303676 s.
- Program SHA-256: `6d9624c231ef1bdc21ebfb3dc37fb97b68c3c1448d49684a5caffb862d58ed07`.
- JSON SHA-256: `ba0e10ed1fc1eb306fafdfbb2e77fe3ed38f17f5ba0f5593188f59203872b111`.
- Audit output and metadata: `work/code_generation_audit/A5_independent.output.txt` and `A5_independent.meta.json`.

The proof supplies one actual IA automorphism preserving the chosen affine integral lattice and finite quotient while moving its boundary lattice. It supplies no all-cover integral transporter and no Galois element. The parent and triangle were informed of the exact pass. One terminology repair was requested: `h<t>` is a left coset, equivalently an orbit of right multiplication; the formulas already used the correct orbit.
