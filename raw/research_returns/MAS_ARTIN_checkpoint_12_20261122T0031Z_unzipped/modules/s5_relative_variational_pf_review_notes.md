# Independent review of MA-RB-012

Reviewer: /root/pf26_audit, GPT-6 Astra Pro.  
Date: 2026-11-22 UTC.  
Final proof: s5_relative_variational.tex, 638 lines, MA-RB.170--199
(tags178--180 reserved and unused).  
SHA256: 61a618d4eb481c727719620023170ab4f0fe2aec94a585190a06ba331aeb20a1.

## Complete written-proof reading

I read every line of the original684-line proof, independently rederived its
new calculations, and then read all final changes: the citation-only
Aramata application, corresponding source wording, and positive-product
optimality paragraph. The final proof passes. No mathematical correction
is requested.

### Actual relative completion and positive divisor

For every nontrivial subgroup H, L/L^H is normal with group H even if the
fixed field is not normal over Q. Aramata's theorem therefore applies to
the full Dedekind quotient. The quotient of the two completed functions
cancels both s(s-1) factors. The archimedean exponents are exactly
60-r_1-r_2 and60-r_2, are nonnegative, and add to120-[K_H:Q].
The relative completion is nonzero at zero and one.

The finite quotient's holomorphy gives genuine containment of completed
zero divisors. The genus-one factors cancel locally normally, including
all multiplicities. The remaining zero count and canonical-product estimates
give order at most one without a bound for an inverse near zeros.
The reflection symmetry fixes the real Hadamard constant as minus the
convergent sum of Re(1/rho), so the logarithmic derivative is exactly the
positive real-part zero sum. There are no leftover pole terms.

The gamma/Euler asymptotic proves that the excess divisor is nonempty.
At sigma=1 the series extends continuously; reflection supplies a zero with
real part below1 and hence strict positivity at that endpoint. Thus the
new variational functions have finite minima on[1,infinity), allowing a
minimum at1.

### Actual residual multiplicities and strict improvement

I freshly reread the actual pointwise order argument in MA-RB.19--26.
All orders discarded in MA-RB.188 are nonnegative at the particular
residual real point, including W eta through its degree-six permutation
quotient. No general holomorphy of W is substituted for its forced order.
Frobenius reciprocity gives the stated coefficients dim(U)-dim(U^H).
The constraint v_1+e>=k yields m_H k exactly, and faithfulness of W
ensures m_H>=1.

For H=A_5, the only invariant irreducibles are1 and eta, so m_H=9.
The real quadratic base field contribution is subtracted exactly.
In particular its possibly nonzero order b is removed from the existing
bound ord(zeta_L)>=b+5n+9k; no use of A is needed.

I freshly reread MA-RB.95--96. The exact full zero sum for L is bounded
above by the old discriminant-aware denominator. Subtracting the strictly
positive completed quadratic zero sum makes the relative denominator
strictly smaller at every sigma>1. Evaluating the new expression at an
attained old interior minimizer therefore proves a strict decrease of
the old bound. The proof does not assume an interior minimizer for the
new function, and it does not assert that the new minimum is nonpositive.

The three subgroup examples have the stated invariant dimensions and
signatures. The finite Euler coefficients include ramified primes.
The absolute tail estimate follows from the decreasing function
log(x)x^(-sigma) for x>=3, with the displayed integral and sign.
The finite certified upper bounds recover the exact infimum by rational
approximation at sigma>1 and then N tending to infinity, including a
possible minimum at the endpoint by approaching it from the right.

The added positive-product statement is exactly a positive weighted-average
inequality for m_H/H_H. It uses the guaranteed multiplicities only. For
integer weights it applies to actual holomorphic products; for real
nonnegative weights it asserts scalar algebra only. It does not create
fractional holomorphic powers or exclude improvements using additional
arithmetic multiplicity information.

## Fresh primary-source reading

I freshly viewed and read all four rendered pages31--34 of:

Aramata, H. (1933). Über die Teilbarkeit der Dedekindschen Zetafunktionen.
*Proceedings of the Imperial Academy, 9*(2),31--34.
https://doi.org/10.3792/pia/1195580866

The main statement on p.31 is the full finite Dedekind quotient for a normal
number-field extension. The source's Sätze1--6 construct the positive
cyclic-induced character combination, and the final proof on p.34 gives
the analytic divisibility conclusion. I checked that normality is exactly
the hypothesis used here and that the result is not an imprimitive
Euler-product assertion. The module now cites this classical theorem
rather than reproducing it.

This fresh four-page reading does not claim a new full audit of every
earlier Artin induction or nontrivial Hecke holomorphy theorem used by
Aramata. The module's inherited categorical and conductor locators are
likewise not new primary readings in this review. No source page or PDF
has been copied into the deliverable.

## Scope

The finite relative-zeta envelope is a strictly smaller necessary interval
for the actual comparison-failure branch, and hence a weaker sufficient
shared-zero exclusion condition. The proof does not establish nonpositivity
of every new minimum, prove R_B, or construct an arithmetic positive-excess
example. Its positivity is positivity of a completed excess zero divisor,
not coefficientwise positivity of the relative Euler series.
