# Independent higher2 GL2 and combined-comparison audit

**Verdict: PASS for the full models at e=14,16,18 and the stated exact
comparison integers.** Reviewer /root/tripod_integral, GPT-6 Astra Pro,
effort not exposed; 2026-11-21 04:42 UTC.

I read every line of gl2_higher2_certificate.py and
combined_higher2_certificate.py and independently executed both. I
reconstructed their use of the already completely audited uniform
modular-form basis and the elementary primality argument. No
mathematical correction is requested.

## Full space, precision, and normalization

For e=14,16,18 the proved basis is D*a^(2e-5-3j)*b^j, with
0<=j<=floor((2e-5)/3). Thus its dimensions are 8,10,11 and its
leading Fourier coefficient matrix is integral lower unitriangular.
The general basis proof applies to all e>=3, so this is an actual
full-space extension, without a new guessed basis or dimension.

The new program imports only the previously audited exact integer
series and matrix routines; it does not import a saved Hecke matrix.
It uses precision 260, exceeding the maximum identifying index
13*11=143. The theta/divisor series and eta products are reconstructed,
and the polynomial exponents agree with every basis monomial.
All first-r Hecke coefficients include the correction
chi(p)*p^(2e)*a_(n/p) whenever p divides n. In particular all three
new dimensions exceed seven, and the correction at n=7 is present.

The exact triangular solve identifies the whole classical operator
because Hecke stability and the full basis are already proved.
The relation L*M=the raw coefficient matrix is checked. Additional
checks extend through n=37 at seven and n=20 at thirteen, including
each applicable multiple-of-p correction. Faddeev–LeVerrier verifies
every exact division and its terminal zero matrix. Three independent
Bareiss determinant evaluations, at 0,1 and the target, reproduce
the complete characteristic polynomial.

## Combined values and exact primality

The combination script takes the full frozen U3 and GL2 polynomial
coefficients. It checks their degree and monicity, evaluates them
respectively at 1+p^e+p^(2e) and 1+p^(2e), and matches each separate
model output. It takes the gcd of the two products at p=7,13.
This correctly requires one auxiliary prime to cover both branches;
it does not replace that gcd by a combination of separate gcds.

The three exact factorizations agree with (HH.2). All factors for
e14 are below 2^31. The sole factors above that threshold for e16
and e18 are respectively 25078104767246023 and 8361790201.
All smaller factors are verified by exact trial division.

For the 17-digit prime, the program verifies

    n-1 = 2 * 3^3 * 10487 * 44284289839

and proves each of those factors prime by trial division. Its
witness a=3 satisfies a^(n-1)=1 modulo n and
a^((n-1)/q)!=1 modulo n for every prime q dividing n-1.
The first congruence makes a a unit. The subsequent congruences
force its order in (Z/n)^times to equal n-1. Hence phi(n)>=n-1,
which is impossible for a composite n. This proves primality;
the argument does not need to strengthen those inequalities to
gcd conditions because it works in the full unit group.

As a separate crosscheck, the other comparison verifier uses a
59-node recursive Lucas certificate with the stronger gcd condition
at every node. That certificate and the complete U3 replay also
pass. The two independent arithmetic implementations agree on every
gcd exponent and prime factor.

## Scope and actual files

Checked file hashes:

    gl2_higher2_certificate.py
    80424d6d8031b9b4538d05f18417600b13d6b90acc5fa00f915fd4b4b974ad81
    gl2_higher2_certificate.json
    8434c5e4eb97662ed9c42b756223c60833a3614d96f295c2a0d3fc8e732dea4b
    combined_higher2_certificate.py
    16dc3cd687ee2cf391cd568fff43b22ed14777004c013c8cc2813ab6790426bd
    combined_higher2_certificate.json
    91ab323906aec549c0068e18d97a056bb2e4195a3bb1d1146f3b1abc6ac19df9

The complete-space modularity input is the same primary
Cléry–van der Geer ring theorem p.12 and eta cusp-form statement
Remark 15.2 p.33 already freshly checked in the preceding audits.
No new primary-source claim is introduced by this uniform extension.
The global arithmetic coverage and the two residual-prime
Bernoulli/reflection tests remain separate inputs.
