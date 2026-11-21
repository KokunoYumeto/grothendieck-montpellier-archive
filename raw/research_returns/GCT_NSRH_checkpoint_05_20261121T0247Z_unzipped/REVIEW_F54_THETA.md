# Fresh review of F54

Reviewer: /root/rectangular_and_theta. Date: 21 November 2026 UTC.

This file records the precise scope and hash of each part as it is reviewed. A PASS on one part is not a claim to have checked a later part that has not yet been supplied.

## Part 1: algebraic genuine power traces and common radius

Target: agent_algebraic_trace_classification.md.

SHA256: bc84d0b8e8280daab3a0de007f020f957e956d65e4d3d18f28b954a5b59837b8.

**PASS.** I read the entire report and independently reconstructed all proofs T1--T21, including the optional relative-algebraic-closure argument and the scope/dictionary paragraphs. No mathematical correction is needed.

### Torsion and the exact Laurent identity

The finitely generated subgroup of nonzero complex numbers has a finite torsion subgroup. If m kills that torsion, its power-image Gamma^m is torsion free: a torsion element g^m would imply g itself torsion and hence g^m=1. Its group algebra is therefore an actual Laurent polynomial domain.

The element B=[b^m] is transcendental, since b>1 makes all its integer powers distinct. Evaluation of a finite group-algebra expression on all sufficiently large integer indices is injective by the finite Vandermonde argument. Applying the original relation on n=mr consequently gives P(B,U)=0 exactly, with U=sum m_i[alpha_i^m]. The relation remains nonzero as a polynomial in its second variable because B is transcendental.

### Euler derivations and support

A unimodular basis change sends the exponent vector of B to (d,0,...,0), where d is its positive coordinate gcd. Euler derivations in the other variables kill C(B). The minimal polynomial of U over that field is separable in characteristic zero, so differentiating it gives Q'(U)D_jU=0 with Q'(U) nonzero in the fraction field. Hence every such derivative vanishes.

After grouping, each Laurent monomial coefficient is positive. Its derivative coefficient is M_a a_j, and linear independence forces a_j=0 for j>=2. No original root is lost in the powered/grouped sequence. Thus alpha_i^m is a power z_1^(c_i), and raising to d gives alpha_i^(md)=b^(mc_i). The common exponent and integers in T4 are correct, including negative c_i and the rank-one case. Virtual or signed coefficients could disappear under powering; the report expressly does not recover them.

The optional rational-function derivative argument is also correct. For a coprime p/q, zero derivative forces p to divide p', and degree forces p constant; the same equation then makes q constant. Iteration proves the stated relative algebraic closure and Laurent intersection. This is supplementary to, not a hidden premise of, the direct support proof.

### The same algebraic element and the original base value

With one common radius, the integers a_i in alpha_i^L=b^(a_i) all coincide. On the L-multiple progression the trace is N b^(ar). Hence f^L-N^L v^a vanishes at infinitely many distinct base parameters at allowed regular places.

The report's finite-zero argument applies to the same algebraic element, despite allowing different sheets. A nonzero algebraic element has a monic minimal polynomial over C(v) with nonzero rational constant term. Away from finitely many coefficient poles, any regular zero of that element forces a zero of this constant term. Infinitely many distinct parameters are impossible. Therefore the displayed algebraic identity is exact.

Evaluating it at the original regular place over b is legitimate, and negative a causes no issue because b is nonzero. It gives absolute trace NR. Equality in the triangle inequality for N actual eigenvalues of common modulus R forces their phases to coincide. Jordan blocks are irrelevant to that trace calculation.

### Full centralizer and scope

Subtracting the resulting common eigenvalue makes a nilpotent central element of the full centralizer. A semisimple algebra has reduced center, so this nilpotent vanishes; the full centralizer is then a single full matrix algebra. The actual F19 generic algebra is semisimple and nonsimple, so the stated contradiction follows.

The negative-square-root example correctly shows that a common phase can survive at fractional spectral weight when sheets vary; it does not conflict with F51's integral-weight result.

The proof needs neither full spectral retuning nor regularity at v=1. It does not infer other-parameter characteristic polynomials or collision contact from trace retuning alone. Its base-root classification is explicitly necessary, not an assertion that every independently chosen collection of root phases realizes one irreducible algebraic family. The full-centralizer qualification is retained, as are the fixed-parameter and specified-subalgebra alternatives.

No new external source theorem is used in these deductions. Previously checked F19 algebra data and the standard module/coaction framework are used only in their declared roles. This is a fresh complete proof review, not a formal-kernel or numerical verification.

## Part 1 final source delta and fragment match

Final report SHA256: d02e3d2584d2a3fff644e2b179390f78d8d5db2dada1d02a3ab88a5e02e59fbc.

Final fragment: finding_F54_part1.tex, SHA256 e768c405f06e883d96cea21817da52588213d8de933643b144aba06bd40ba543.

**PASS.** I read the entire final fragment and separately read the report's two final changes: the explicit zero-rational-function case, and the effective representation-K0 dictionary. Neither changes a theorem. The fragment retains the complete proofs, all positive/virtual and trace/spectral distinctions, the fractional-radius example and the separate framework paragraph.

The K0 identification is used precisely: a genuine torus representation supplies an effective sum of weight characters, while a virtual class may cancel them. No gamma-filtration positivity is inferred. The SGA/archival citations remain framework anchors rather than claimed sources for the new trace theorem.

## Parts 2 and 3: full report review

Target: agent_marked_trace_frontier.md.

The entire first version read had SHA256 2cff0b740a60ae358a63cc35218125ef4b81c756ff2a0f1c402c978fd47c49c2.

Final reviewed report SHA256: 1546e73d971e55bc51f572fc344c64c04177e2b79c2cd41b2d6ef06e4298c58a.

**PASS.** I read and independently reconstructed all Sections 1--6. I also read both final deltas: the scope sentence preserving the established F50/F53 action/path constructions, and the scalar fractional-weight boundary example. No mathematical correction is needed.

### The exact trace-only model and coefficient base

I independently collected the coefficients in both trace identities and substituted v=1,2. The stated spectra and collision values are correct. The finite localization retains the center collision because d-c=k Delta is specifically not inverted.

The all-degree separation argument is a proof, not an extrapolation from samples. At v=4 the exact rational values have the stated order. For v>=8, Delta lies strictly between zero and one; the cubic upper bound for d-a is negative at 8 and has strictly negative derivative thereafter. Meanwhile the displayed lower bound for z is positive at 4 with positive derivative thereafter. These facts make every inverted scalar and cross-sector difference nonzero at every 2^n. The S0 factors are also nonzero at those points and at v=1.

The order-two center normalization is exact: Delta has a double zero at v=1 and its remaining factor is a unit. The additional localizations do not remove that point.

### Universal cyclic centralizer and actual module comparison

Since k is a unit, commuting with c+kx is equivalent to commuting with x on the regular module C. Thus its centralizer is End_C(C)=C after every coefficient base change. This is an actual cyclic-module calculation and does not require flat base change for an arbitrary kernel.

The scalar-sector differences and the two characteristic determinants are units. They eliminate every cross-sector intertwiner, including after coefficient base change. Hence End_F(H)=S×S×M2(C) is the actual relative algebra, with a genuine Jordan entry at the collision.

The same linear equation proves Hom_F(C²,L_i)=Hom_C(C²,L_i), with the original right row action by precomposition. The established regular F21 comparison therefore gives the actual rank64 tensor lattice and named generator matrices; the proof does not merely match multiplicities.

Over the domain S, Delta is a nonzero divisor, so cross-branch Hom vanishes. Multiplicity matrix units give the stated full left commutant. At collision, the branch targets merge and both sides acquire the same cross maps; the new dimension 816 is correct. This distinction is important: the four-block formula is the domain formula, whereas the report explicitly computes the specialization jump.

Both identity traces retune for all n by the polynomial identities and the base spectra. Full spectra fail already at n=2. Base weights 0,1,2,3 at Q=4 do not impose those weights on all evaluated matrices; the v=8 eigenvalue of modulus5 verifies the stated scope.

### The central marking is the actual element

I multiplied the idempotents directly. Z=e+f-ef-fe commutes with both e and f, and on each N(a) equals (1-a²/D²)I. The values z1,z2 and the polynomial B expression for X are correct.

The identification with the actual center coordinate is integral, not just a generic eigenvalue statement. On the matrix block the relation (Z-z1)(Z-z2)=0 gives

X-(z1-Z)=(z1-Z)(Z-z2)/z2=0.

Thus X is exactly x there, while it vanishes on the scalar blocks. Alternatively generic equality extends in the torsion-free order. On M, the regular F21 splitting gives X=0 or Delta I on the four sectors, hence X(1)=0 as a matrix and a generic marked sector of rank8. On the cyclic auxiliary H, its collision value is instead the nonzero center nilpotent. These two facts are correctly distinguished.

### Scalar lemmas

For a single exponential, expanding a nonzero polynomial relation gives nonzero coefficients on roots b^i alpha^j. Finite-power uniqueness forces two distinct monomials to have the same root; their j values differ, so alpha^L=b^m. Substitution on the L-multiple progression gives the rational identity after v=t^L. Irreducibility then makes the minimal polynomial divide Y^L-C^L v^m. This proves the stated unit property above v=1, including negative m and arbitrary permitted sheets.

The report's independent common-radius proof is also valid. Grouping by the real numbers i+j log_b R separates root radii. At sequence index zero each group has coefficient sum p_ij r^j. Irrational log_b R would make every group a single nonzero term; hence the exponent is rational, and the grouped identities give the claimed algebraic power relation. The fragment replaces this with the equivalent complete deduction from Part1's common-power theorem and finite-zero argument; that is a valid proved dependency.

For integral mixed weights, the expanded relation groups by integer exponent. Evaluating each vanished unit-circle sequence at zero produces the Laurent relation P(v,sum v^w)=0. Since that root is rational, irreducibility identifies the function itself and makes g(1)=r. This correctly retains negative weights and genuine multiplicities.

The scalar g=1+t on v=t² shows that arbitrary multiple fractional radii can permit a zero at a different place over v=1. Its report and fragment explicitly do not call it an actual module/action construction.

### Full relative centralizer and marked tensor-module obstructions

In the auxiliary case, F lies in the center of its full centralizer. In the actual relative order its matrix-block component is therefore c0+c1x with regular coefficients. Generically the center splits and F is a scalar tuple, so it is diagonalizable. If two primitive blocks had the same eigenvalue, the additional cross maps would enlarge the full centralizer. Within one block, fullness forces its underlying dimension to equal the matrix-block size, in particular two on the marked branch. This proves Tr(XF)=2 Delta d with d regular. It is not obtained by assuming that an arbitrary representation of M2 has multiplicity one.

The marked comparison at the base then has a nonzero single-exponential coefficient. The scalar lemma says its algebraic trace function is a unit above v=1, while the actual regular expression is divisible by Delta. This is the required contradiction without a weight hypothesis. The full relative order, its specified marking and regularity are essential and explicitly assumed.

For M64 no full-centralizer hypothesis is used. Commutation preserves the rank8 Delta-branch and its invertible Frobenius restriction. Dividing the marked trace by the fixed nonzero constant Delta(b) gives its genuine eight-eigenvalue power trace. Regularity and X(1)=0 give g(1)=0. The common-radius or integral-mixture scalar lemma supplies the contradiction. The nilpotent variant is valid because commuting X(1) and F(1) make their product nilpotent.

### The two fixed-word test

The pair of trace identities for P and P², together with the actual quadratic relations, forces (D(b^n)-D(b)) Tr(P_b F_b^n)=0. Strict monotonicity of D on v>1 makes this trace vanish eventually.

At the base, P_b/D(b) is an idempotent of rank40, and its image is invariant under the commuting invertible F_b. The inserted trace is therefore D(b) times the genuine power trace of an invertible rank40 restriction. Vandermonde uniqueness forbids eventual zero. The proof needs no commutation at other parameters, algebraicity, weights, collision point or full-centralizer claim.

The condition that the second insertion really is the fixed square of the first is retained. A grading coefficient object representing D(v) is a different comparison; the proof does not exclude it. Nor does it exclude F45's varying word objects or the fixed-parameter F50/F53 constructions.

## Exact execution check

I read and independently ran verify_trace_frontier.py at SHA256 ce0cf63a11559a538b14019e5e1bb26de1afeefc999bb5928b1eae13e4af5044.

Result: **PASS**, using Python 3.12.14 and SymPy 1.14.0. It verifies both rational trace identities, the base and collision values, the source row-matrix relations, central Z and X branch actions, the exact values supporting the all-n inequalities, and the marked-trace residual

-197896315512672/4359848400625.

The all-n inequalities, universal End/Hom identities and impossibility statements were separately proved and checked as described above; the finite execution is ancillary. No formal proof-kernel verification is claimed.

## Complete final-fragment matches for Parts 2 and 3

- finding_F54_part2.tex, SHA256 7452b1b9e11685908fb84831c78b4f7a5f6e175f29b72744f0969b4208e867ba.
- finding_F54_part3.tex, SHA256 a6f6d8b2bad685c971cde601acad3d430c6eff06969d4bbd4d87b2486714a8e2.

**PASS.** I read both final fragments in full. All hypotheses, exact model formulas, all-n localization proof, actual action comparisons, scalar deductions, marked and two-word proofs, separate dictionaries and limitations match the reviewed report. The auxiliary-H statement explicitly inherits algebraicity, invertibility and regular evaluations. The common-radius scalar consequence uses the proved Part1 dependency without omitting its finite-zero reasoning. No mathematical blocker remains in the three final F54 fragments at these hashes.

## Both-actions supplement

Target: agent_marked_trace_bimodule_supplement.md.

SHA256: 5b5e25588d18448eb9e32d4bcc07ce2fa1d91d47ba82b3d7a557c726448848e1.

**PASS.** I freshly read the complete note and reopened the full F43 P6, P8--P10 contexts. The marked branch is exactly (W1^V tensor W1^W) tensor N(D-2). On each W1, the named raising and lowering matrices are the two off-diagonal units, and their products give the diagonal units. The left image is therefore M4.

For the right two-dimensional factor, I independently reconstructed the displayed idempotent normal form. With r=a/D, first use the eigenbasis of P1/D and then rescale its zero-eigenvector by 1/r. This produces f with diagonal entries r² and 1-r², upper-right entry one, and lower-left entry r²(1-r²). Here 0<r<1 at b>1, so both off-diagonal matrix units are generated. This is exactly the stated z2 form, and the right image is M2.

Consequently the joint actual left/right image is M8, not merely an abstract irreducibility claim. A commuting base Frobenius is scalar and invertible on this branch. The marked trace is then a single nonzero exponential with coefficient 8 Delta(b). The proved scalar lemma contradicts its regular zero at the collision.

Only base left commutation is needed. The distinction between invariant ordinary left operators and coefficient-line covariance is retained, as is the possibility of a right-only fractional mixed escape. The highest-weight labels include the determinant twist and do not change polynomial degree. No mathematical correction is needed.
