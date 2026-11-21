# Structural check for a fixed-field geometric Z_ell tower

Date:2026-11-21. GPT-6 Astra Pro; effort not exposed; `/root/row_audit`. This checks the structural question requested by `/root/effective_galois`; it does not duplicate that agent's Iwasawa-literature search and is not a new numbered finding.

Assume ell is odd and different from the finite-field characteristic p. Suppose a Frobenius-stable rank-one Z_ell quotient of the geometric abelian fundamental group has Frobenius multiplier a in Z_ell^×. Such a quotient is a quotient of the covariant ell-adic Tate module of the Jacobian. Thus a is an eigenvalue of its Frobenius polynomial, hence an algebraic Weil number of weight1. The opposite Frobenius convention gives its inverse. In either convention it is not a root of unity, since q>1.

Put t=ord(a mod ell), and s=v_ell(a^t−1). Then t divides ell−1 and s is a finite positive integer. The elementary ell-adic lifting identity gives

    ord(a mod ell^r) = f_r = t ell^max(0,r−s).

Indeed, a power yielding1 modulo ell^r must be divisible by t; for a^t=1+ell^s u with u a unit, binomial expansion gives v_ell((a^t)^h−1)=s+v_ell(h) for every positive integer h. Thus the minimal deck constantization degree grows on the order of ell^r. This conclusion is conditional on the displayed stable rank-one quotient; no claim that a quotient exists for every selected ell is made.

## Additional consequences of the checked integral descent lemma

Let B_r be the actual primitive conductor ell^r factor of the corresponding geometrically cyclic cover D_r→C over k, and let k_(f_r) be its own minimal deck field. Write

    O_r = Z_p[Z]/Phi_(ell^r)(Z),
    tau_r(Z)=Z^a,       R_r=O_r^tau_r,
    U_r=B_r(k_(f_r))[p^infinity],
    N_r=B_r(k)[p^infinity].

The entire checked lemma SD.1–SD.10 applies: U_r = O_r tensor_(R_r) N_r. The algebra O_r is finite etale of constant rank f_r over R_r. Since R_r is a product of unramified discrete valuation rings, O_r is free of rank f_r as an R_r-module (component by component). Consequently, as finite additive groups, U_r is noncanonically isomorphic to the direct sum of f_r copies of N_r. In particular

    #U_r=(#N_r)^f_r,
    dim_Fp U_r[p]=f_r dim_Fp N_r[p],
    exp U_r=exp N_r.

The geometric p-rank of B_r is at most its dimension (g(C)−1)phi(ell^r). Therefore

    dim_Fp B_r(k)[p] <= (g(C)−1)phi(ell^r)/f_r.

For r≥s the right side is the constant

    (g(C)−1)(ell−1)ell^(s−1)/t.

Thus semilinear descent does provide a uniform bound on the number of rational p-primary generators along such a tower, beyond equality of exponents with the deck field. It does not force the group to be zero or bound its exponent.

## Exact formal limitation

For every integer e≥1, the abstract module U_r=O_r/p^e O_r with semilinear action F=tau_r satisfies F^f_r=1. Its invariants are R_r/p^e R_r by the same finite-etale torsor descent, and have exponent p^e. This gives examples satisfying all the coefficient-algebra/semilinear hypotheses with arbitrary exponent and a nonzero rational fixed group. These are abstract finite modules, not asserted to arise from curves or form a compatible geometric tower.

Any exponent stabilization, vanishing, or geometric supply conclusion therefore needs extra information about the actual family of Frobenius operators. The preceding generator-rank bound alone does not imply any A46/A47 witness.

Checked against retained `work/row_audit/NONCONSTANT_PRIMITIVE_DESCENT.tex`, especially SD.3, SD.5–SD.6 and SD.9–SD.10. That lemma's finite-etale descent input is Stacks Project Proposition35.3.9, Tag023N. The Weil-eigenvalue premise is the standard Frobenius theorem for abelian varieties (Milne, *Abelian Varieties*, Theorem19.1), already used and checked in the main source. No new primary-source theorem or whole-publication audit is claimed here.
