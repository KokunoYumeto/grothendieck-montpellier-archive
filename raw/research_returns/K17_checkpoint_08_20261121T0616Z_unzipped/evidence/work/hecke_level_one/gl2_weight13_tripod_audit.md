# Independent whole-proof audit of K17-GL2-MODEL

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro, 2026-11-21 UTC.
Reasoning effort: not exposed. **Verdict: PASS for the stated full modular-form
space and exact Hecke computations.** No conductor or K-group coverage is
inferred here.

I read the entire clean `gl2_weight13_section.tex` and every line of
`gl2_weight13_certificate.py`, then executed the standalone certificate.
All assertions passed. I had independently reconstructed the same series
by a different logarithmic-derivative recurrence, and the theta series by
direct norm enumeration, in `tripod_independent_check.py`; all coefficients,
both Hecke matrices, both characteristic polynomials and their evaluations
agree. Thus the two verifications do not merely rerun the same eta-product
routine.

The complete modular-form ring paragraph of Clery--van der Geer,
arXiv:2110.00849v2, printed p.12, and Remark15.2, printed p.33, were freshly
read both through the web and in the downloaded primary text during the
immediately preceding model audit. They identify the exact theta and eta
normalizations and the odd character. The fresh refs are
`turn460047228view1` and `turn392910988view1`; URL:
https://arxiv.org/pdf/2110.00849 .

I checked the division argument at both cusps. The eta transformation gives
`D(-1/(3 tau))=-27 tau^6 D(tau)`; the determinant-normalized weight-six slash
operator gives `D|W3=-D`. Consequently both cusp orders are exactly one.
The two local stabilizer translations have character one, so local orders
of the odd-character forms are integers. Eta is nowhere zero in the upper
half-plane. Division by D therefore introduces no pole and gives exactly
M7, whose three weighted monomials are the stated basis. The leading
coefficient matrix has determinant one; this also proves the claimed
integral Fourier-expansion lattice assertion, with no hidden index.

The Hecke coefficient formula has the character factor and exponent12
appropriate to weight13. At n=1,2,3 and p=7 or13 the second term vanishes,
so the first three coefficients and the proved complete basis determine
the whole operator. The additional n=7 check at p=7 includes the nonzero
second term and passes. I checked the displayed B matrices against the
executed report and reconstructed the triangular solve, the characteristic
polynomial formula, and the repeated roots. The complete prime products
are exactly the displayed evaluation integers; primality of each listed
factor is checked by trial division in the standalone certificate.

The exact full-space result is

    P7(X)  = (X-40250)^2 (X+153502),
    P13(X) = (X-1284050)^2 (X+9397582).

The statement retains all source-conductor, transfer and trace-normalization
requirements as separate hypotheses. The new TeX adds no unsupported
inference beyond the previously checked modular-form model. No correction
is requested.
