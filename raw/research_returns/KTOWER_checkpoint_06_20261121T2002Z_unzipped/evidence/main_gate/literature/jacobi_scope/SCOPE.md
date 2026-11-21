# Jacobi nonvanishing scope check

Reviewer /root; GPT-6 Astra Pro; effort setting not exposed.

Primary source: Markus Schwagenscheidt, Nonvanishing modulo ell of Fourier coefficients of Jacobi forms, Research in Number Theory2 (2016), article4, DOI10.1007/s40993-015-0035-1. Publisher PDF https://link.springer.com/content/pdf/10.1007/s40993-015-0035-1.pdf.

Read: Theorem1.1 and its stated exception scope pp1–2; Eisenstein application and Corollary1.4 p3; Proposition3.1 statement and proof pp12–13; Proposition3.2 proof pp13–14; Lemmas3.3–3.4 and full Theorem3.5 proof pp14–16; exception equations(5)–(6) pp15–17. Earlier operator identities are imported, not independently checked; no whole-paper verification claimed.

The theorem concerns one Jacobi eigenform and retains an integral unit coefficient as input at a fixed prime. Its local-condition theorem excludes the explicit spectral primes in(5). For Bernoulli index b, put k=b+1 and substitute lambda_q=1+q^(2b−1). The product of its two signed differences is (q^(2b)−1)(q^(2b−2)−1). Thus if p−1 divides either exponent, p lies in that spectral exceptional set for every allowable q. This is the same obstruction already found for the half-integral-weight theorem. In the p=3 mod4 progression b1=(p−1)/2 it always occurs. For b2=p−2 and p≥7 neither exponent is divisible by p−1; choosing q in a primitive residue class removes this particular spectral obstruction, but does not supply the required primitive unit seed or a common discriminant with the other two values. Multiplying modular q-series gives convolution, not the required coefficientwise product.

No simultaneous unit theorem or main-gate reduction follows. This is an attempted source application with explicitly retained gaps.


## Subsequent proved construction

The later KT-JACOBI-TWO-UNIT-FIELD supplies an explicit seed condition B_(2b)/(2b) and uses the heat-filtration plus odd-theta/Sturm argument to extract a bounded discriminant. It does not invoke the fixed-prime spectral nonvanishing theorem audited above, so that theorem's additional spectral exceptions do not constrain this new proof. The same-D simultaneous two-twist gap still remains. See the completely reviewed jacobi_two_unit_fields.tex and source/review manifests.
