# Independent audit of the complete GL2 models in further odd weights

**Verdict: PASS for K17-GL2-GENERAL and the displayed finite comparison identities.**
Checker: `/root/tripod_integral`, GPT-6 Astra Pro; effort not exposed.
Actual whole-proof read and independent replays: 2026-11-21 04:28 UTC.

I read the entire `gl2_general_section.tex`, every line of
`gl2_general_certificate.py`, `hecke_combined_certificate.py`, and
`gl2_e10_p19_certificate.py`, then reran all three successfully. I reconstructed
the completeness, lattice, and normalization arguments independently. No
mathematical correction is requested. These are complete models of the stated
modular-form spaces; arithmetic source coverage is not part of this audit.

## 1. The whole modular-form space and its integer lattice

The normalized generators are the same ones freshly checked in my preceding
weight-thirteen audit: the Eisenstein norm theta series `a`, the weight-three
eta quotient `b=eta(3tau)^9/eta(tau)^3`, and
`D=eta(tau)^6 eta(3tau)^6`. The primary ring statement in Cléry–van der Geer,
arXiv:2110.00849v2, printed p.12, identifies the complete ring with `C[a,b]`,
of weights one and three, and identifies its odd part with character
chi_{-3} on Gamma_0(3). Their Remark 15.2, printed p.33, supplies the cusp
form D. Primary retrievals from that preceding source read are
`turn396569473view1`, `turn460047228view1`, and `turn392910988view1`.
I do not claim a new retrieval during the present finite audit.

I checked the eta transformation directly. D has no interior zeros,
has order one at infinity, and satisfies
`D(-1/(3tau))=-27 tau^6 D(tau)`, so its weight-six Fricke transform is -D.
It therefore also has order one at the other cusp. The cusp stabilizer
translations have character one, so all relevant local orders are integers.
Division by D identifies the entire cusp space of weight 2e+1 with the
holomorphic space of weight 2e-5, for every e>=3. The weighted monomials
`D a^(2e-5-3j) b^j`, for `0<=j<=floor((2e-5)/3)`, exhaust that space.

Their leading terms are `q^(j+1)`. Thus the matrix of their first r
coefficients is integral lower triangular with diagonal one. An arbitrary
form with integer Fourier coefficients has integer coordinates in this
basis by exact triangular elimination; conversely these basis forms have
integer expansions. This proves the asserted integral Fourier lattice,
not merely a rational or complex basis. The dimensions 3,4,6,7 for
e=6,8,10,12 follow without a computed dimension assumption.

## 2. The exact full Hecke operator

The coefficient rule is the classical normalized one:
`a_n(T_p f)=a_(pn)(f)+chi(p)p^(2e)a_(n/p)(f)`, with the latter term zero
unless p divides n. It preserves the already proved whole space.
Consequently its first r coefficients and the invertible leading matrix
identify every column of the full operator, not a projection onto a
subspace. All entries are integers.

The certificate constructs the theta coefficients by the Eisenstein ideal
divisor formula and the eta products by exact finite binomial expansions.
I checked truncation at precision 182, the product shifts, the negative
binomial exponents, and the powers used for every basis monomial.
The maximum identifying index is p*r<=91, below that precision.
The additional coefficient checks extend through n=26 for p=7 and n=14
for p=13. In particular e=12 has r=7, and the correction at identifying
coefficient n=7 is explicitly present; it is not lost by an assumption
that the first r coefficients have n<p.

I read the exact integer triangular solve, checked the matrix orientation
`L M = raw_coefficients`, and verified that the separate extra coefficient
checks use the same classical formula. Faddeev–LeVerrier checks each exact
division and its terminal Cayley–Hamilton zero. Independent Bareiss
determinants verify the polynomial at 0, 1, and the comparison point.
The weight-thirteen control is reproduced exactly. The code has a harmless
comment saying two determinant checks although three are actually executed;
the theorem accurately says three.

## 3. Polynomial products, comparison integers, and primality

The combination program reads the complete stored polynomial coefficients,
not just a factorization or a trace. It multiplies every displayed GL2
factor in the theorem and verifies equality with the full characteristic
polynomial. It evaluates the U3 polynomial at `1+p^e+p^(2e)` and the GL2
polynomial at `1+p^(2e)`, matches each separate model report, then computes
the gcd of the two product values at p=7 and p=13.

The independently replayed exact factorizations are:

| e | gcd of the combined comparisons |
|---:|---|
|6|`2^15 3^19 *7*13^5*37*47^3`|
|8|`2^29 3^31 *23^3*401^3*809*13687^3`|
|10|`2^54 3^54 *43*241^3*1847*9496386083^3`|
|12|`2^58 3^71 *5^2*7*13^8*37*47*28447^3*300455201^3`|

Every prime factor is proved prime by integer trial division through its
square root. The largest required bound is below 100000. Exact product
equality then proves that no further factor is omitted. The comparisons
for e=6,8,12 have all factors below 2^31. The e=10 factor 9496386083 does
not lie in that range. The proof correctly avoids inferring a larger
Vandiver computation or a K-group conclusion from these arithmetic facts.

## 4. The additional e=10 test at 19

The separate program reconstructs the weight-21 space from the same
series routines at precision 380; it does not reuse a stored Hecke matrix.
It checks the first six identifying coefficients and all coefficients
through n=20, including the correction term at n=19. Three independent
Bareiss evaluations again agree with the characteristic polynomial.
The exact value at `1+19^20` is divisible by 9496386083. Its positive
character value chi(19)=1 is correctly used. This shows precisely that
the third-prime product unit criterion retains this prime. It is not an
assertion that a corresponding Selmer group or K-group is nonzero.

## 5. Actual files checked

SHA256 values at this audit:

```
gl2_general_section.tex
2a2299a6ca7f0344bf1689eaa2eeb1ccd10068a8c270bf0c7260b2c185dfbfd3
gl2_general_certificate.py
481ef0fc65444aa0e62e7c6c92d11efacfaf32b14ac62c588d1e3c2ff1aa0b14
gl2_general_certificate.json
6dd4d587cda8778893651cf11bd50c2f605dbb62d9c866f693916037e18d55af
hecke_combined_certificate.py
3d16bbaf4a662c50c99eb6b461195d7b6721d69488c67643abc5d296f57c0613
hecke_combined_certificate.json
83f19b284d993de20267846c265a3eeb10f382ac5ffa707dc0b94376073abea5
gl2_e10_p19_certificate.py
c0fefff6f69f29713dbe698489e47bd352b3ec39f20a4fcc6529201fcdac03f4
gl2_e10_p19_certificate.json
2a988b2df642d7a1994010a83383210739539835db99bdd591a24e7552001887
```

The independent U3 computation and its complete replay were checked
separately. This report does not replace that proof, an automorphic packet
coverage proof, or the manuscript's Selmer interface.
