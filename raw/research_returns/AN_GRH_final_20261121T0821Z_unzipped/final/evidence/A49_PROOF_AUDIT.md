# A49 author complete-proof audit

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Source: A49_ODD_QUOTIENT_FOURIER.tex.  
Final SHA256: 5fecbadc1de4120af3591d0f760591a02fd1ccc3d01927fc898e9e922fa24483.

## Verdict and exact scope

PASS. I read the complete statement, four proof steps, both retained comparisons, and final supply qualification. This is an author complete-proof check. Separate whole readings by root and row_audit are recorded in their own fragments. The theorem is an exact finite-quotient criterion under its canonical-kernel and signed-unit hypotheses. It is not a proof that such a quotient exists for every curve or prescribed point.

The final one-sentence correction makes the conclusion explicitly conditional on the equivalent nonuniformity/witness assertions. The immediately preceding reviewed draft had SHA256 f109d30ce9a5c199b6e41d59e53af7cbed2d5cbaa4ac1c7151e39595d82a4e88. The sole mathematical-statement clarification was changing “Consequently A46 separates...” to “When these equivalent conditions hold, A46 separates...”. No proof or numerical comparison changed.

## Whole proof checked

1. Since the exponent of H is prime to p, its order is also prime to p. Every cyclic character image has odd degree m>1 dividing n. For a quotient a of J(k), the constant subgroup ker(a) is defined over k, and the Lang factorization produces an etale isogeny with constant kernel equal to the quotient. Milne's connected Abel--Jacobi pullback statement applies after geometric base change. The origin above the Abel image of P gives a rational point, and a constant deck group splits the entire fibre. Thus the field in the result really is the original field.

2. The recovered genus-two character formula is valid for every nontrivial character, including an imprimitive character of a larger group. Its quadratic term is q times the canonical character; q vanishes modulo p. The actual image of m e_m has precisely the faithful deck-character summands on an auxiliary Tate module. Its rational point count is the product of the faithful L-values, with no substitution of an arbitrary isogeny representative. This product is an integer, so nondivisibility by p is equivalent to all factors being nonzero at one fixed prime above p. Reduction retains every character's exact order because m is prime to p.

3. Units reduce surjectively from n to every divisor m. The signed-unit hypothesis therefore holds at every possible character conductor. Integer point multiplicities give p-power covariance. The condition b(kappa_P)=0 makes the hyperelliptic involution send each label to its negative, so inversion preserves the character value. Consequently any nonzero Fourier value controls all faithful characters of its own cyclic quotient. This is the precise extra step absent from an unqualified average-character argument.

4. Fourier inversion over the algebraic closure of Fp is valid because H has order prime to p. All nontrivial values vanish exactly for the stated uniform augmentation component. Thus nonuniformity gives a successful cyclic quotient, and a successful quotient proves nonuniformity. If p does not divide N+1 and |H|>N, P occupies zero and some nonzero coset is empty; its coefficient contradicts uniformity. A46 applies only after this equivalence or sufficient inequality has been established. Its hypotheses are satisfied by the original-field pointed odd cyclic cover.

## Recovered and primary inputs checked

I read the complete recovered successor A.10, A.26 and A.35 in ANABELIAN_SUCCESSOR_paper.tex, plus the current A26 and A29 up through their complete character-polynomial and faithful-factor arguments. Their prime-quotient Fourier identity, empty-coset argument and canonical symmetry are explicitly credited. The full-primary, all-conductor and signed-orbit combination here is not attributed to an earlier prime-only statement.

Milne, *Jacobian Varieties*, author version 12 June 2021, Proposition 9.1, printed p.30:
https://www.jmilne.org/math/xnotes/JVs.pdf

Fresh references: turn691928535view0 and turn691928535view1. I reopened the exact proposition, displayed proof setup, and its separation of prime-to-characteristic and characteristic-primary inputs. A49 only requires a prime-to-p kernel. The full Abel--Jacobi input and the elementary original-field Lang construction were also checked earlier in this run. This audit does not claim a new independent proof of Milne's theorem.

## Retained examples and finite execution

The A27 input is N=6, Jacobian order28, and a rational Weierstrass base point; the seven-primary quotient is therefore C7. The signed orbit of2 is all six units, although2 itself has order3. A31 already supplied a geometric witness for this same curve.

The A45 twist has N=4, Jacobian order18 and a retained rational exact-order-nine class, so its full three-primary quotient is C9. Its degree-three quotient is unique up to deck automorphism and has both L-values equal to6. The two other rational point labels are opposite units modulo9 because their retained reductions modulo3 are1 and2. This yields primitive-nine product norm(7+z+z^-1)=321^2=103041. Its proper conductor-three factor has order36. No new curve enumeration was used.

Executed verify_A49_finite_algebra.py successfully. It imports no prior curve-arithmetic code, verifies the unit orbits, checks s^3-3s+1 in Z[z]/Phi9, and computes the norm by an exact six-by-six multiplication matrix and fraction-free determinant. This is an algebraic cross-check of the derived product, not an independent reproduction of the retained curve counts or point labels.

Script SHA256: dec18039d196f659a3b155c4135360523fc3558a3fca09d6e2cf914b5c1f4dbb.  
Output SHA256: 44b2784778c7fd5a175c7fa759d13bb66ea0a6be859ed561ee790e309582a73e.

Both curves already have witnesses from earlier findings. These comparisons show the difference between sufficient tests, not a strict reduction of the full previously unresolved universal witness gate.
