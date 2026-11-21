# A48 independent whole-proof review

Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Date: 2026-11-21T06:25:13.965663+00:00.
Source: `work/gt_certificates/positive_rank_theta/A48_TWISTS_AND_POINTING.tex`.
Whole-read source SHA256: `4a7d80fb137274077cf9b3a873b045e3e6a1aa3f92b2d237980ed44c54af07fe`.

## Verdict

PASS mathematically. I read the entire statement, all four proof steps, and the complete concluding supply/pointing scope. The one visible TeX typo `,qquad` in the nonconstant conjugation display was reported to the author and is an exposition-only correction pending final hash. No mathematical gap was found. This is an independent same-model whole-proof reading, not formal verification.

## Complete argument checked

The coherent character line bundles of a connected cyclic etale cover are nontrivial for every nontrivial character. Riemann--Roch gives character multiplicity g-1. The Artin--Schreier stable-part comparison is functorial for deck actions in arbitrary genus. Dualizing to geometric p-torsion only inverts characters. The actual primitive factor therefore has faithful-character multiplicities at most g-1 and p-rank at most (g-1)phi(n).

When deck transformations are constant, arithmetic Frobenius commutes with them. The n twists have actions sigma^t F. A faithful character and one Frobenius eigenvalue forbid at most one t; algebraic multiplicities provide a valid union bound even in the presence of Jordan blocks. Thus at most f_n twists have a primitive p-torsion fixed vector. For a finite rational p-primary group, nonzero is equivalent to containing a point of order p. This gives the claimed lower bound, including its positive genus-two specialization. The form count is over C and its geometric automorphism group there is exactly the deck group.

On the prescribed fibre, Frobenius is translation by a, so precisely t=-a splits the fibre. If another twist acquires a rational point after degree m constants, m(a+t)=0 modulo n. The displayed identity F_t^m=F_P^m then identifies the entire covers and their canonical actual primitive factors over that extension. The original pointed rational p-primary subgroup injects into the new rational group. This rules out obtaining pointed vanishing merely by a twist followed by such an extension.

For nonconstant deck action a, the fibre action is x -> a^m x+N_m(a)t. A fixed point means N_m(a)t=(1-a^m)x. I checked the exact sign in sigma^(-x)F_t^m sigma^x: its translation exponent is N_m(a)t-(1-a^m)x, hence zero. The resulting cover isomorphism over the constant extension identifies actual primitive subvarieties and preserves the original rational subgroup. No count of nonconstant twists is asserted.

The final paragraph correctly distinguishes this exact fixed-cover obstruction from varying the geometric cover, its conductor, or the base. It does not infer a universal pointed witness from an unpointed count, an average, or number-field prime density.

## Direct primary-source check

I directly reopened Katz, *Une formule de congruence pour la fonction zeta*, SGA7II, ExposeXXII, author scan `https://web.math.princeton.edu/~nmk/old/congzeta.pdf`, retrieval ref `turn262809055view0`. I read Proposition2.0 and Corollary2.1, and Propositions2.2.4--2.2.5 with their complete displayed proofs, printed pages406--409. Their hypotheses concern proper schemes and all cohomological degrees; no genus-two or ordinary hypothesis occurs. The Artin--Schreier exact sequence and canonical stable-part isomorphism make the claimed deck functoriality applicable here. The proof's preceding linear-algebra statements are displayed earlier in the same source, but this event does not claim an independent reread of every cited prerequisite.

## Final complete reread

Final source SHA256 `0f942d786563c2fabee27b995042a70d8567bd77f430dd4f656c25699ea8324c`. I read the entire final source again, including its explicit identification of H1_et with the dual of T_p J/p and T_p J/p with geometric J[p], the expanded exact Katz locators, and the corrected nonconstant display. The duality only inverts characters and preserves the multiplicity bound. The final complete proof passes, with no pending correction. The exposition/locator changes do not change any theorem hypothesis or conclusion.
