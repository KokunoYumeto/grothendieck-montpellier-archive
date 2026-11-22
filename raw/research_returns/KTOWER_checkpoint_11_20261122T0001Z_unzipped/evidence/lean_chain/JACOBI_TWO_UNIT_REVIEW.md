# Independent whole-proof review: Jacobi two-unit fields

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; reasoning effort not exposed.

## Verdict and frozen object

**PASS** for the complete current proof in `main_gate/jacobi_two_unit_fields.tex`, SHA-256 `a03b614b8101e3696ad3e6cceef0f0b216af728cf14f9a2e5c742ee5fc3977a1` (326 lines). All five statements and their complete proofs were read, including the final source paragraph and restored display closings. This is a mathematical proof and exact primary-source-scope review. No Lean kernel build or reconstruction of the imported analytic foundations was performed.

Reviewed statements: KT-SMALL-DISCRIMINANT-CLASS-BOUND; KT-JACOBI-ODD-COEFFICIENT; KT-JACOBI-TWO-UNIT-FIELD; KT-JACOBI-TWO-UNIT-GD; KT-JACOBI-TYPEII-FIELD.

## Elementary class-number estimate

The ideal-class-to-norm-form injection is justified: a proper equivalence yields an orientation-preserving similarity of the complex ideal lattices; its multiplier lies in the quadratic field by taking the ratio of corresponding nonzero lattice elements. Choosing a minimum primitive vector, extending to an oriented basis, and shifting the second vector gives |b| <= a <= c and 3a^2 <= |D|. Oddness of D gives at most a+1 choices for b. Summing yields R(R+3)/2 and the displayed upper envelope. For |D|<4p and p>=29 the strict inequality 2p/3+sqrt(3p)<p is correct. The class-number formula has only the prime-to-p denominator w(D)<=6.

## Half-period projection and Sturm step

I independently derived the multiplier in (JF.2). For g(tau,z)=Phi(tau,z+1/2) and gamma in Gamma_0(4), the integral elliptic translate (c/2,(d-1)/2) cancels the z-dependent terms; the remaining multiplier exp(2 pi i c(d-2)/4) is one. The translation lattice and cusp-holomorphy conditions are therefore satisfied. The exponent identity n+r lambda+lambda^2=(n-r^2/4)+(lambda+r/2)^2 proves holomorphy at the rational translates.

Schwagenscheidt's exact q-expansion theorem applies with N=2,m=1 and p odd after multiplication by a common denominator prime to p. The explicit S-transform is Phi-q^(1/4) zeta Phi(tau,z+tau/2). If the odd-r component vanished modulo p, the two summands would have disjoint parity in zeta and force Phi itself to vanish. This checks the potentially delicate odd-component assertion without importing a nonvanishing theorem with extra local exceptions.

The specialization f=h1 theta1(tau,0) is nonzero modulo p because theta1 begins with 2q^(1/4). Thus cancellation among the odd-r coefficients cannot destroy the specialization. It is a holomorphic modular form on Gamma_0(4) with trivial character and p-integral coefficients. The ordinary Sturm bound gives n<=K/2 because the index is six. A unit sum of finitely many p-integral coefficients contains a unit summand; Jacobi support excludes n=0 for odd r.

## Eisenstein coefficients, integrality, and heat filtration

The two primary EZ scans were independently viewed. At s=1-b, the definition of L_D(s) on printed p.19a gives precisely v^(b-1) and sigma_(2b-1). Theorem 2.1 on printed p.20 gives E_(b+1),1 coefficient L_D(1-b)/zeta(1-2b), so multiplication by zeta(1-2b) produces exactly (JF.8), including its zero-discriminant coefficient. No missing factor of two occurs.

The displayed Bernoulli-polynomial calculation proves p-integrality for every fundamental discriminant, including p|D0. In the latter case v_p(f)=1; all j>=1 terms are integral and the possible j=0 numerator is zero modulo p. The CRT factor from f/p has zero complete character sum unless f=p, where the finite-field power sum is zero except b=(p-1)/2. This is exactly the excluded value. The ordinary Bernoulli recurrence uses j+1<p throughout and justifies integrality of B_j. The constant coefficient is a unit by the stated rational Bernoulli hypothesis.

Richter's weight-congruence theorem gives filtration k=b+1. In the endpoint k=p-1 the only lower congruent weight is zero, and J_(0,1)=0 follows from the recalled free E_(4,1),E_(6,1) decomposition. The condition p does not divide 2k-1 fails in the stated range exactly at the already excluded b. Richter's Proposition 2 and its proof therefore yield a nonzero heat image of filtration k+p+1. The explicit modular lift (JF.11) has that weight and integral coefficients; the Eisenstein congruences give Phi=L1(phi) modulo p.

The unit coefficient from the odd-component lemma forces both the heat factor and the original coefficient to be units. Its odd negative discriminant has size <=2K-1<=4p-1 and is prime to p. Passing from D'=D u^2 to the fundamental D uses an integer multiplier and an integral L-value, so the L-value is a unit. The elementary class bound supplies the other unit. The already-reviewed field-character reduction transports it to every indicated original weight, including weights beyond p.

## Exact consequences and limits

The GD corollary uses all twelve clauses of the pinned Counts.lean definition through the previously checked odd-discriminant verification: odd discriminant, p-free discriminant and class number, positive even e, N=2, trivial finite character, and explicit genericity. The eta clause is justified by a ramified prime q|D different from p; no splitting-at-p condition is silently assumed.

For p=3 mod4, b=(p+3)/2 satisfies all restrictions; the ordinary Kummer congruence sends B_(p+3)/(p+3) to B4/4=-1/120. The character-order calculations gcd(2q,q+2)=1 and gcd(2q,q+1)=2, q=(p-1)/2 odd, are correct. This is a nonquadratic mirror family and does not assume the rational reflected component vanishes.

For the TypeII corollary, b represents 2e+1 and the constructed unit is precisely B1(chi_D omega^(2e)), so the already whole-reviewed actual-source TypeII exclusion applies. The p=7 mod8 specialization has even e and the claimed genericity. The construction supplies only the class-number unit and one twist unit in a field. It does not prove that the exponent-e and exponent-2e units hold in the same field, does not exclude generic rank-three sources, and does not imply K-group vanishing on its own.

## Actual primary reading scope

- Richter (2009), *The action of the heat operator on Jacobi forms*: entire paper text read, with detailed reading of the free decomposition p.871, Proposition 1 p.872, and Proposition 2 with its complete proof p.873. Imported antecedent theorems are not independently reproved.
- Schwagenscheidt (2016): Theorem 1.2 full statement p.2 and complete proof pp.11-12 read, plus the Eisenstein normalization and bounded-denominator statement p.3. Theorem 1.1 is not used in this proof or certified by this event.
- Eichler-Zagier, MPIM preprint 1983(8): independently viewed the complete scans of printed p.19a (PDF p.24) and printed p.20 (PDF p.25), covering the general L_D definition and Theorem 2.1. This is a precise formula/theorem-scope check, not a claim to have read the whole monograph or every preceding analytic derivation.
- Choi-Choie-Kikuta (2013), p.129: exact ordinary elliptic Sturm theorem statement read. This imports Sturm in the explicitly quoted coefficient-field generality; no reading of the original 1987 Sturm proof is claimed.
- Existing field-character reduction, Sun transport, GD verification, and actual-source TypeII theorem are previously whole-reviewed project inputs. This event checks their exact use here and does not claim a fresh kernel check.
