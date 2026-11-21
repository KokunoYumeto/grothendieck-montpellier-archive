# Independent full review of the Cayley End/Hom realization

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; reasoning effort not exposed. Date: 21 November 2026 UTC.

**Result: PASS. No mathematical blocker.**

The complete original report agent_cayley_weil_realization.md, SHA-256 cfeca3c4e4c15e578164ce9fd48cf7a5aed39a26168cf764c19bff896032851e, was read in full. The subsequently added complete C15a paragraph was separately read and reconstructed. The resulting reviewed report hash is 06c90390243ec91ec86527ea2cd8cc1023e026f45b400ed94b43fea8cd41bf9e.

This review independently reconstructs every new elementary argument, including arbitrary coefficient base change, relative coherent geometry, both crossed extensions, arithmetic purity, continuity, and the two explicit comparison limits. F19/F21 supply the previously proved actual algebra and lattice; F43 supplies the known commuting ordinary action. No proof-kernel certification or numerical experiment is claimed.

## 1. Coefficient ring and cyclic operator

For real nonzero v, D>=4 and Delta=(D-1)(D-4)/D² lies in[0,1). Thus all stated finite localizations admit v=q^(1/2), q^(-1/2), and1. The two added inverses have genuine roles: 1+Delta² makes both Cayley denominators units, and1-Delta separates the i scalar sector from the moving branch. No inverse of the colliding difference Delta is used.

The finite coefficient ring is important. Localizing instead at every function nonzero at1 could exclude the later arithmetic evaluations. The chosen S avoids that issue.

In C, x²=Delta*x. Expanding the Cayley fraction gives F=1+s*x with s=2i/(1-i*Delta), a unit, and lambda=1+s*Delta. The displayed column matrix and characteristic polynomial are correct. Since x=s^(-1)(F-1), commuting with F is exactly C-linearity, over S and after every S-algebra base change. End_C(C)=C gives the centralizer. The alternative inverse using F+1 is valid because that element is a unit. At Delta=0 the lower off-diagonal entry2i remains nonzero, so the regular dual-number Jordan block is retained.

## 2. Exact End, Hom, and arbitrary base change

The separation identities are exact:

F+1=2/(1-i*x), and F-i=(1-i)(1-x)/(1-i*x).

The element1-x is a unit because its norm is1-Delta. The difference between the two fixed scalar eigenvalues is also a unit. These identities force all scalar-versus-C intertwiners to vanish, even over a coefficient base with zero divisors. The branch quotients inherit the same unit identities.

The C sector of H is C² and its endomorphisms are M2(C). Maps to a branch line are C-linear maps from C² and form the usual right row module. With the scalar multiplicities this gives exactly End_F(H)=A of rank10 and Hom_F(H,K)=M of rank64. The source rank6 and target rank44 are correct. The column-source/row-Hom convention makes precomposition the stated right matrix action, without an opposite-algebra error.

All these arguments use identities with units and the regular C-module, rather than generic eigenvalue splitting. They therefore commute with every coefficient base change, including nonflat and nonreduced bases and the collision. This is stronger than a generic dimension argument.

End_F(K) behaves differently: over the domain S, lambda-1=s*Delta is a nonzerodivisor, so the off-diagonal branch Hom groups vanish. The four matrix blocks have ranks400+16+256+16=688. At the collision the branch lines have the same scalar operator, giving400+16+400=816 and exactly128 new off-diagonal maps. This jump is compatible with the constant End/Hom ranks above because H's regular block remains cyclic.

## 3. The added commuting-action comparison C15a

The postcomposition map End_F(K) to End_A(M) is an algebra isomorphism. On the C sector, set N=L1^16 plus L2^4. Commuting with the diagonal matrix units forces a module endomorphism of N² to preserve both coordinates; commuting with the off-diagonal matrix units forces the same map on both. Commuting with scalar C matrices forces that map to be C-linear. It is precisely postcomposition by a unique End_C(N) element.

This proof works over every base ring. In particular it includes the new branch-mixing maps after specialization; it does not assert that those maps were available before specialization. The product scalar blocks are immediate. Thus the comparison retains the full actual commuting left action from F43, as stated, with the same commutant jump.

## 4. Smooth proper geometry over the coefficient base

The monic degree-two polynomial defines a finite flat Cartier divisor on P1_S, with no point at infinity. Its constant term lambda is a unit, so its support also lies in the multiplicative chart. Substituting T=1+s*x identifies its relation with s²*x(x-Delta); the unit s gives the exact inverse and preserves the nonreduced fiber.

Each section has its O(-1) to O resolution and the divisor has its O(-2) to O resolution. These define perfect coherent objects on the smooth proper relative projective line. The notation T-a means the corresponding homogeneous linear section when used in this global resolution.

The supported sheaves are finite over the affine coefficient base, so their global sections are the specified free modules and higher cohomology vanishes. Coherent Hom on the common affine chart is exactly the commuting-coordinate Hom. It gives the actual A and M, including the named action. Multiplication by T is a separate linear automorphism of these supported objects.

The report correctly says that P1_S is smooth and proper over S, not that a finite-field variety with the desired geometric Frobenius has thereby been constructed. The characteristic-zero evaluation v=q^(1/2) cannot be substituted into the same characteristic-p coefficient ring as an invertible v when the integer q becomes zero. That distinction is explicit and necessary.

## 5. Both crossed coherent extensions

Applying Hom of the section resolution into O_b gives the two-term complex S to S with differential b-a. The finite support over affine S eliminates further global cohomology. Thus Hom is the annihilator and Ext1 the quotient by b-a, with no higher Ext. For equal sections both groups are S.

All cross differences involving the fixed scalar supports are units. The two branch orientations have differences plus or minus s*Delta and both give S/(Delta). The multiplicities therefore give

Ext1(K,K)=S^688 plus (S/(Delta))^128.

The free term counts four self-blocks. The torsion term counts16*4 in both directions. In the local ring at v=1, Delta has order two, so the torsion length is256. This retains both original crossed torsion groups, while the additional free self-Ext makes clear that no full derived equivalence is asserted.

## 6. Purity, Jordan data, and Galois continuity

At q^(plus or minus1/2), D and Delta are rational, and every complex embedding sends i to plus or minus i while fixing Delta. It therefore sends lambda to lambda or its inverse, both of absolute value one. The sign conjugate of sqrt(q) changes neither D nor Delta. Every eigenvalue of H,K, and their internal Hom is thus pure of weight zero in the stated all-conjugate sense.

At the collision, the same statement permits the size-two Jordan block. The report properly distinguishes arithmetic Frobenius data from the semisimple vector-space category on the geometric point, and does not infer arithmetic semisimplicity from purity.

The internal Hom has dimension6*44=264, whereas its fixed subspace is the actual64-dimensional module. The internal End has dimension36, whereas its fixed subalgebra has dimension10. These dimensions and roles are not conflated.

The continuity criterion is valid. Necessity follows from compactness of the image and boundedness of positive and negative powers. For sufficiency, unit eigenvalues give a lattice stable under the matrix and its inverse after a finite extension, so the closure of the powers is a compact profinite matrix group. Reduction modulo congruence subgroups gives the compatible extensions from Z to its profinite completion. Equivalently one can construct a stable lattice from the integral characteristic polynomial with unit constant term. The original coefficient-field closure is also preserved under conjugating back.

Only finitely many places can be bad for a fixed algebraic lambda. Excluding their underlying rational primes and the finite-field characteristic gives good continuous realizations. The report correctly claims neither every coefficient prime nor one uniform prime for all q. The q=2 checks at3 and5 are correct: at3 both Cayley numerator and denominator are units; at the two places over5 exactly one is divisible by5.

## 7. The two comparison limits and their primary source

For q>1, lambda(q) is not one. Delta(q^n) tends to1 and lambda(q^n) tends to i. Equality of lambda(q)^n with lambda(q^n) for all sufficiently large n would force their consecutive ratios to tend to1, hence force lambda(q)=1. This contradiction proves the stated failure of the named-branch retuning law. It does not invalidate the fixed-q Weil object.

The q=2 arithmetic was independently recomputed:

D=9/2, Delta=7/81, lambda=(3256+567i)/3305, and lambda+lambda^(-1)=6512/3305.

The last fraction is reduced and its odd denominator is not a unit in Z[1/2]. If lambda were integral over that ring, so would its conjugate and rational sum; integral closedness would put that sum in Z[1/2], a contradiction. Multiplication by powers of2 cannot repair it.

I reopened the original French primary text, Deligne, La conjecture de Weil I, https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf, retrieval turn474125951view0. Theorem(1.6) on printed page276 and the discussion on pages276–277 were read in turn474125951view1. The stated characteristic polynomial is det(tI-F), with integer coefficients for each smooth projective cohomology degree. Its monic convention gives algebraic-integral eigenvalues. Tate twists introduce only powers of the field cardinality, so at F2 the eigenvalues remain integral over Z[1/2]. The report's exclusion follows with exactly those hypotheses. No broader integrality theorem or complete proof of Weil I is claimed checked.

## 8. Final scope

The report supplies exact ordinary coefficient constructions retaining the algebra, actual actions, collision nilpotent, commutant jump and crossed coherent extension torsion. It does not mistake its chosen linear operator for absolute scheme Frobenius, the F44 algebra lift, cyclotomic TP Frobenius, or the geometric Frobenius of a new finite-field variety. Pure finite coefficients are therefore available in this exact fixed-parameter sense; the designated positive basis, all-extension parameter comparison, and path-sign gates remain separate.

The complete report and C15a addition pass.

## 9. Complete corrected fragment match

The entire generated fragment was read and matched against the checked report, including the complete C15a postcomposition isomorphism and its arbitrary-base-change scope. The initial fragment had two wording issues, which were reported and corrected: only z1, z2 and Delta belong to S0 before the extra Cayley denominators are inverted; total reality is a sufficient condition for the general algebraic-parameter purity statement, and is not asserted necessary. The latter distinction is real: v=2^(1/4) has nonreal conjugates, while D and Delta still have real conjugates.

The entire corrected final fragment at SHA256 4f78dd6e27145a6016e9f40718102d8e418cecd8ba24b51806ce26ea133ff2c4 passes. It includes the exact EGA I affine module/sheaf locators, original SGA6 I Definition4.7/Example4.8 perfect-complex locators, SGA3 I4.7.2--3 and cote90 scan17 framework anchors, and BBD5.1.2/5.1.8 weight conventions. Those additions correctly identify frameworks, not primary proofs of the new Cayley construction. The corrected report hash is 1767e68f7821d61d9d493b767486bfa9795c13cfd551a873ee0dad0f863e837a.
