# General number-field open-image bound and the actual LM8 factors

Date: 2026-11-21. Checker: GPT-6 Astra Pro, `/root/effective_galois`; effort not exposed.

## Published theorem checked

I opened the primary publisher PDF of Davide Lombardo, *Bounds for Serre's open image theorem for elliptic curves over number fields*, Algebra & Number Theory 9(10) (2015),2347–2395, DOI10.2140/ant.2015.9.2347. Corollary9.3 is on p2393, repeated on p2348. I checked the surrounding definitions and Theorem2.1's isogeny input, and rendered p2393 to verify the exceptional-sized constant visually.

For a number field K, a geometrically non-CM elliptic curve E/K, d=[K:Q], and stable Faltings height h_F(E) in the source's convention, the adelic index is strictly less than

exp(10^21483) d^(2.4·10^10) max{1,h_F(E),log d}^(4.8·10^10).

This is the published unconditional statement. The output labels it G-LOMBARDO as a cited result, not as a new proof. The entire Lie-theoretic and isogeny proof was not independently repeated. The smaller constants in Remark9.4 depend on then-unpublished inputs and have not been substituted.

Primary URL: https://msp.org/ant/2015/9-10/ant-v9-n10-p06-p.pdf . Web references: turn528945879view0, turn575869752view1. The local rendered page is lombardo_cor93.png.

## Actual row hypotheses

I read the arithmetic setup and Serre application in the complete recovered `sections/A_nonstable_D3_fixed.tex`, and the non-CM argument in A.14 of `sections/A_prol_normalizers.tex`. The elliptic factors are explicitly

F_a/Q: y²=x³−3x+a, a=±6.

They descend to Q even though the proof later chooses a larger number field L. That distinction permits both a direct unconditional general-K application of Lombardo and the sharper M-dependent Mayle–Wang result over Q before restriction.

The source's non-CM test uses two ordinary reductions, not a classification of CM j-invariants. Direct enumeration confirms:

| a | p | #F_a(F_p) | trace | trace²−4p |
|---|---:|---:|---:|---:|
| 6 | 5 | 7 | −1 | −19 |
| 6 | 11 | 9 | 3 | −35 |
| −6 | 5 | 7 | −1 | −19 |
| −6 | 11 | 15 | −3 | −35 |

The primes are good and the traces nonzero modulo p, so the reductions are ordinary. The source's specialization argument excludes a geometric CM field because it could not embed into both distinct quadratic fields. The signs are geometric twists. Both j-invariants are −216; this value by itself is not the non-CM argument.

## New G06 proof check

The integral discriminant is −16(4(−3)^3+27·6²)=−2^9·3^3. Good reduction holds outside two and three. At these two primes, the exponents 9 and3 are below12, so no integral model can have a lower nonnegative discriminant exponent: an isomorphic Weierstrass change changes the exponent by a multiple of12. Both exponents are therefore minimal and positive. Hence rad(2N)=6.

Mayle–Wang Theorem1 gives full mod-ell image over Q for ell>964 log6+5760 under the stipulated M premise. For any finite L/Q, the map of coset sets from G_Q/G_L to the quotient of their images is surjective, so the restricted image has index at most [L:Q]. This remains valid when L/Q is not Galois. It does not assert full image over L.

The same coset inequality for the adelic representation, combined with Lombardo over Q, proves the stronger actual-row unconditional bound

I(F_a/L) < [L:Q] exp(10^21483) max{1,h_F(F_a)}^(4.8·10^10).

The stable height does not change on field extension. The rows' existing commutator Zariski-density conclusion is already unconditional and needs none of these numerical bounds. The addition supplies explicit refinements for the actual factors without changing that status.

**Outcome:** Full targeted check of the newly written G06 proof: PASS. Primary cited-result statement and hypotheses: PASS. No independent reproof of Lombardo's full theorem or the general CM-specialization theorem is claimed.
