# Independent whole-proof review of G-23

Reviewer: /root/rectangular_bridge; GPT-6 Astra Pro; effort inherited/not exposed; run CUE_GCT-20261121.

## Outcome and scope

**PASS.** Read the entire statement, parameters, proof, rectangular consequence, and limits. The proof is checked as a deduction from the explicitly cited G10/G18 degree and Hilbert methods, G21, G22, and R28; this review does not claim a fresh full-source proof audit of G10 or G18. No new numerical search was executed.

## Re-derivation

Checked u=(r−2)n²+r_eta−r²+3 and v=rm²−2m+r+r_eta−r²+2, including their positivity in4<=r<=m<n. The action degree L=ns+(r−1)e uses inverse-transpose degree r−1 on SL_r; the independent parameter degree is p=ns+e. Derksen's finite-kernel bound gives sigma<=r L^(r²−1), followed by the stated integer beta. The center acts trivially because ns−e=r nu_r, and R28's no-scaling point gives gcd-one degrees shared by both domains.

Rechecked the standard-Veronese grouping with E=rT beta!, all parameter degrees, and the generic image-degree uses. The common nonzero invariants of degrees E+t and2E−t give the two exact injections into/out of degree Ek+t. The binomial ratio is k(k+1)(k+2)/(u(k+u)(k+u+1)), bounded below by k/(4u) for k>=u+1. The two integer thresholds are therefore sufficient for strict inequalities. The same sandwich and standard Hilbert polynomial yield an all-integer expansion with positive leading coefficient and relative error O(1/j).

The no-equality argument is uniform: even r makes Delta odd; for odd r, Delta0 forces m,n same parity and then r1mod4; reducing modulo r−2 gives (2m−1)²=−1, impossible modulo a prime3mod4 dividing r−2. Checked the floor boundary, which uses the absence of equality. For rectangles, n<rm/(r−1) gives the claimed strictly positive completed square; s=r/gcd(n,r) captures precisely every admissible coordinate degree. The statement carefully leaves the first-row equality face, r>m, and finite early degrees undecided.

Reviewed file SHA256: 421a759a42556e2108fb94b0e24ac069cdc1fb0e800f4da02eaacc307bbb17e8

Checked UTC: 2026-11-21T05:39:07.695110+00:00
