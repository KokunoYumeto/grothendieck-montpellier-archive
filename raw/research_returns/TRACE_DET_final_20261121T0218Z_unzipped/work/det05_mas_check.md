# DET-05 independent coefficient and continuity check

2026-11-21; GPT-6 Astra Pro; /root/masullo_trace; effort not exposed; TRACE_DET.

Use the symmetric normalized polarization a_n(A,...,A)=Tr(Λ^n A). For T_i(z)=u_i〈v_i,z〉, the coefficient of t_1...t_n in det(I+Σ t_i T_i) is det(〈v_i,u_j〉), by the finite Sylvester determinant identity. On the other hand that coefficient is n! a_n(T_1,...,T_n). Exterior-product Cauchy–Schwarz gives |det(〈v_i,u_j〉)|≤||v_1∧...∧v_n|| ||u_1∧...∧u_n||≤∏||v_i||||u_i||. Therefore |a_n(T_1,...,T_n)|≤(1/n!)∏||T_i||_1 for rank-one inputs.

For general trace-class T_i, expand each in its singular-value series Σ_r s_{i,r} u_{i,r}〈v_{i,r},·〉 with unit singular vectors. The mixed rank-one series is absolutely convergent, bounded by (1/n!)∏_i Σ_r s_{i,r}=(1/n!)∏_i||T_i||_1. Finite partial sums agree with the Fredholm coefficient; hence their continuous extension is the standard trace-class polarized coefficient. This proves the inequality on the entire trace class. Coordinate projections T_i=|e_i〉〈e_i| show that the constant 1/n! is sharp. It would not be the same formula if one defined a mixed coefficient without division by n!.

Writing δ=||A−T||_1 and M=max(||A||_1,||T||_1), replace one argument at a time in a_n(A,...,A)−a_n(T,...,T). There are n terms; each has one A−T and n−1 factors of norm at most M. The resulting bound is δM^{n−1}/(n−1)!. For |w|≤R, absolute summation of the determinant expansions yields |det(I−wA)−det(I−wT)|≤Rδ exp(RM). Trace-norm convergence makes δ→0 and keeps M bounded, proving locally uniform convergence. Operator-norm convergence follows from ||·||≤||·||_1; hence the positive selfadjoint cone is closed and the limit of positive A_N is positive.

The entire proof was reread and checked after writing. Cote 1 scan78 Eq.(15) matches the normalized mixed coefficient with trace/nuclear norms. No trace-class re-proof for arbitrary Banach norms is intended.
