# Jacobi selected-field third-unit counterexample: independent review

PASS after whole-proof and whole-code reading and a fresh complete replay in a separate reviewer directory. The author script and report were left unchanged; the replay copied the exact source bytes and its complete JSON object equals the author's report.

The example uses p=31, b=17, e=16 and D=-79. The primitive character is the Legendre character modulo79, since79=3 mod4. Exact Bernoulli-polynomial recurrence gives B1=-5, normalized B3=992 divisible by31, and normalized B17=-23090968227437542810000061098240 congruent20. The independent full conductor2449 sum modulo961 correctly implements the Teichmuller lift a^31 and agrees on20.

Here k=18 and the heat-lift weight K=50. At (n,r)=(20,1) the fundamental discriminant is -79, so the normalized Eisenstein coefficient is minus normalized B17, and the heat factor is79. Their product is1 modulo31. Thus this is an actual unit coefficient inside n<=25 and |D|<=99, rather than an arbitrary field not selected by the construction. The class-number formula gives h(-79)=5. Since2e=32 is congruent2 modulo30, the third generalized Bernoulli unit is equivalent under the already reviewed transport to normalized B3, which vanishes modulo31.

The proposition's scope is exact: one field selected by the Jacobi two-unit method can fail the third unit. It makes no claim that every possible selected field fails, that no three-unit field exists, or that a rational K-group is nonzero. No Lean kernel build or broad numerical scan was performed.
