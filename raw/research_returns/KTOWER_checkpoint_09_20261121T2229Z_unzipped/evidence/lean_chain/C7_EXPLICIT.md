# KT-C7-EXPLICIT: an evaluated, very coarse seventh-power constant

Date: 2026-11-21. Investigator: GPT-6 Astra Pro, `/root/lean_chain`; effort not exposed.

## Statement

Under the prompt's stipulated use of Alpöge's archive theorems and K17's `VK-PT` and `VK-EXP7` source reconstruction, one may take

\[
\boxed{C_7=10^{\,10^{3500}}}
\]

in

\[
\log|K_{4k}(\mathbf Z)|\le C_7(2k)^7\quad(k\ge1).
\]

This is an explicit upper bound for an admissible constant, not the least constant. It is intentionally very large. The bound is obtained from explicit integer bounds in the archive's Hermite-normal-form and cohomology arguments; it does not require enumerating automorphic spaces. A substantially sharper estimate, if separately proved using the exact compact-unitary spaces, supersedes its numerical usefulness but not the source-constant evaluation requested here.

All archive paths below are relative to `src/Development/AutomorphicArithmetic/AutomorphicVarieties/`, at commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`.

## 1. Why the top-level constant is not a numeral

`AutomorphicForms/TemperedLocalComponents/CohBoundFree.lean:69–91` proves `cohBound_of`. At line 75 it obtains a natural number `c` from `gen`; line 79 returns

\[
(c\,3^{dn^2},dn^2),\qquad d=[F:\mathbf Q].
\]

`gen`, lines 28–60, gets `c` by an existential elimination from `AbsBound`. In turn `BuildingsResidueChars/AbsoluteBoundOfPartialBoundOfOrbitBound.lean:6–9` chooses stabilizer constants and returns their finite sum. `BddArith.lean:39–49,59–72` ultimately uses a nerve of Hermitian minimal-vector data. The top-level witness is therefore not a literal integer expression that can simply be printed. Nevertheless, the lower proofs contain enough explicit bounds to replace it with the following expression.

## 2. A uniform explicit cohomology constant for GL_n(O_F)

Let F be imaginary quadratic of absolute discriminant D, and let n≥1. Define positive integers

\[
I=D^n(2n)^{2n},\quad R=n^nI^2,\quad T=(2R+1)^{2n},
\]
\[
A=I^{1+2n^2},\quad B=(T+1)^{2n^2},\quad H=AB^2T^n,
\qquad b(D,n)=HA B^H.
\tag{1}
\]

**Claim KT-COH-EXPLICIT.** For every finite-dimensional complex representation V of GL_n(O_F),

\[
\sum_{q\ge0}\dim_{\mathbf C}H^q(\mathrm{GL}_n(O_F),V)
\le b(D,n)\dim_{\mathbf C}V.
\tag{2}
\]

### Source inputs

The source defines `dd=d*n`, `I0=|disc F|^n dd^dd`, `RR=n^n I0^2`, and

\[
\operatorname{orbBound}(q)=I0^{1+dd\,n}
\bigl((2RR+1)^{dd}+1\bigr)^{dd\,n(q+1)}
\]

in `HermiteNormalForms/SmulStrictMono.lean:17–19,244–249`. Thus, for d=2, its orbit bound is exactly AB^{q+1}.

`HermiteNormalForms/ColsMinSmul.lean:34–75` bounds the number of group orbits of its ordered q-simplices by AB^{q+1}. `HermiteNormalForms/Nearvec.lean:9–38` gives a finite set `nearVec(A0)` of size at most T whenever the n columns of a nonsingular matrix A0 are common minimal vectors. `HermiteNormalForms/Stabfin.lean:24–50` chooses such a matrix for a vertex and proves that a vertex stabilizer injects into ordered n-tuples of minimal vectors. Exactness of the nerve's augmented chain complex is the archive theorem cited as `ConeExtensionAcyclic.sx_exact` in `BuildingsResidueChars/BoundedComplexOfBoundedSimplicialComplex.lean:18`. Its permutation terms are projective over C because their stabilizers are finite, as used explicitly in `BddArith.lean:41–49`.

### Proof of the claim

Fix a vertex v. The matrix A0 chosen in `Stabfin.lean:24–26` has all columns among the minimal vectors of v, and these columns are linearly independent over F. Every minimal vector of v lies in `nearVec(A0)` by the definition `SmulStrictMono.lean:258–259`. The latter set has size at most T. A stabilizer element is determined by the images of the n columns of A0: two elements with the same images have equal products with A0 and hence are equal because det(A0)≠0. Thus

\[
|\operatorname{Stab}(v)|\le T^n.
\tag{3}
\]

This is the quantitative version of the exact injection in `Stabfin.lean:35–50`; replacing its merely finite ambient set by `nearVec(A0)` gives (3).

Choose one representative from each orbit of ordered 1-simplices. There are at most AB² of them. The proof of `BuildingsResidueChars/AdelicRepDimensionBounded.lean:22–68` injects the q+1 distinct vertices of an injective ordered q-simplex into the disjoint union, indexed by these edge representatives, of the stabilizers of their first vertices. By (3), that disjoint union has at most AB²T^n=H elements. Consequently there are no injective q-simplices for q≥H.

For precision, the nerve resolution also includes repeated tuples. The source handles this with the normalized alternating endomorphism. `BuildingsResidueChars/RepHomAlternatingSumEqZero.lean:10–57` proves that it is the identity on the augmentation and is zero in a degree where every tuple repeats a vertex; `AltChainOfPermSplit.lean:5–46` proves it is a chain map. `ExtVanishingOfResolutionEndo.lean:32–38` then gives H^q=0 for q≥H. No assumption that the original tuple complex literally terminates is needed.

In degree q, the permutation term has at most AB^{q+1} orbits. A homomorphism from that term to V is determined by one vector per orbit, so its dimension is at most AB^{q+1}dim V. This is exactly `BuildingsResidueChars/PermutationModuleHomologyRank.lean:4–34`. Cohomology is a subquotient of this Hom term. Summing the bounds for 0≤q<H,

\[
\sum_q\dim H^q\le
\left(\sum_{q=0}^{H-1}AB^{q+1}\right)\dim V
\le H A B^H\dim V.
\]

This proves (2). The source's total-cohomology summation is `AdelicRepBoundedOfDegreeBounded.lean:16–26`. All new arithmetic here is inequality (3), retention of the displayed orbit bounds, and the finite geometric-sum estimate.

## 3. Explicit level bound when the class number is one

For class-number-one F, write K(m) for the principal congruence subgroup of GL_n(O_hat_F) of level m, and let Γ=GL_n(F). Then

\[
\operatorname{cohDim}(\Gamma,K(m),\xi)
\le b(D,n)\,m^{2n^2}\dim\xi.
\tag{4}
\]

Here `cohDim` is the same total group-cohomology quantity used by `CohBoundFree` and by `KlevThree.lean`; this is not a claim about one individual cohomology degree.

To justify the one-orbit assertion needed for (4), an adelic matrix g determines a full O_F-lattice L in F^n with completion g O_hat_F^n. One may construct L by choosing a positive integer a with
a O_hat_F^n⊆g O_hat_F^n⊆a^{-1}O_hat_F^n, taking the appropriate submodule of the finite quotient a^{-1}O_F^n/a O_F^n, and pulling it back. Chinese remainders show that its completion is the prescribed lattice. Since O_F is a PID, L is free, so L=γO_F^n for some γ∈GL_n(F). Hence g=γk with k∈K(1). Thus Γ acts transitively on GL_n(A_f)/K(1), and its stabilizer is GL_n(O_F).

The fiber over that orbit under GL_n(A_f)/K(m)→GL_n(A_f)/K(1) has cardinality [K(1):K(m)]≤m^{2n²}. The latter inequality is `BuildingsResidueChars/LevelSubgroupIndexBoundOfCardOhat.lean:22–38`. Apply the source's Shapiro fiber argument, `OrbitBoundOfShapiroFunctorial.lean:3–23`, with the cohomology constant b(D,n) from (2). It gives (4) directly. This is also the proof of `CohBoundFree.lean:gen` specialized to one orbit and base level one.

## 4. Fixed auxiliary fields and class-number check

Use F0=Q(sqrt(-3)) for rank three. For the six rank-two auxiliary fields in K17's `VK-EXP7` argument choose absolute discriminants

\[
\mathcal D=\{3,7,11,19,43,67\}.
\]

They are pairwise coprime, so they meet the same six-field condition as the illustrative choices in K17. Each has class number one. For completeness, this can be checked directly from the Minkowski bound (J. S. Milne, *Algebraic Number Theory*, version 3.08, Theorem 4.3, printed p.70): every ideal class has an integral representative of norm at most (2/π)sqrt(D). For D=3,7 this bound is <2. For D=11,19 it is <3, and 2 is inert because -D≡5 mod 8. For D=43 the bound is <5; 2 and 3 are inert, so the only possible nonunit ideal norm below 5 is 4, represented by the principal ideal (2). For D=67 the bound is <6; 2,3,5 are inert, so again the only possible nonunit norm is 4 and its ideal is (2). Therefore every ideal-class representative is principal.

These inequalities and inertness checks are replayed by `check_c7_arithmetic.py`. The class-number deduction is the short specialization just proved, not a claim that the computation alone proves Minkowski's theorem.

## 5. Substitution into the carried exponent-seven proof

K17's `evidence/work/k_quantitative_refinement.md`, §§4–5, allows the fixed cohomology constants B0 for rank three at level 6 and B_i for rank two at level 18. By (4), choose

\[
B_0=6^{18}b(3,3),\qquad
B_D=18^8b(D,2)\quad(D\in\mathcal D).
\tag{5}
\]

The source check that these are the relevant levels and that Γ=GL_n(F) is explicit in `AutomorphicForms/TemperedLocalComponents/KlevThree.lean:18–28` and `GaloisLibrary/CrystallineBaseChange/KlevThree.lean:17–27`: both call `cohBoundFree ... n ⊤ inferInstance` and pass from M to 3M.

The carried proof then gives the fully explicit valid choice

\[
C_7^*=20\left(6^{18}b(3,3)
 +32\,18^8\sum_{D\in\mathcal D}b(D,2)\right).
\tag{6}
\]

No cohomology dimension, orbit cardinality, class number, or existential constant remains in (6): b(D,n) is the integer expression (1). This is an exact closed arithmetic expression, though far too large to write out in decimal.

## 6. A simpler evaluated decimal-power bound

For (D,n)=(3,3), I=1,259,712<10^7 and 2R+1<10^14. Hence

\[
T<10^{84},\quad A<10^{133},\quad B\le10^{1512},
\quad H<10^{3409},\quad \log_{10}b(3,3)<10^{3413}.
\]

For n=2 and D≤67, I≤1,149,184<10^7 and again 2R+1<10^14. Thus

\[
T<10^{56},\quad A<10^{63},\quad B\le10^{448},
\quad H<10^{1071},\quad \log_{10}b(D,2)<10^{1074}.
\]

The +1 in B is harmless: if T is an integer less than 10^u, then T+1≤10^u. Also 6^18<10^15, 18^8<10^11, and
20(10^15+192·10^11)<10^18. Equation (6) is therefore less than

\[
10^{18+10^{3413}}<10^{10^{3414}}<10^{10^{3500}}.
\]

This proves the stated explicit choice C7. The script verifies the small-integer inequalities without attempting to materialize any double-exponential integer.

## 7. Check and limitations

The complete proof above has been read after writing, including the repeated-tuple issue, the uniform stabilizer bound, transitivity over a PID, the exact levels 6 and 18, the six-field replacement, and every numerical inequality. It uses archive theorems as stipulated and carries K17's arithmetic and automorphic exponent-seven argument. It is not a Lean kernel proof, and no claim of numerical sharpness is made. The relevant previous gate, unspecified B0 and B_i in K17-VK-EXP7, is replaced by the explicit integers (5)–(6).

Geometrically, the new explicit constants come from arithmetic quotients of a Hermitian reduction complex and from finite étale congruence-level fibers; the motivic conclusion remains the bound on the finite integral Tate pieces of the K-theory of Spec Z supplied by K17's Poitou–Tate/K-theory comparison. It does not prove that those pieces vanish.
