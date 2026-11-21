# Independent whole-proof review of G25

Reviewer: /root/rectangular_bridge; GPT-6 Astra Pro; effort inherited/not exposed.
Date: 2026-11-21T05:54:32.909259+00:00
Fragment: work/root/g25_fragment.tex
SHA256: `fc9f1d04de445260affc8973373abd2a0ac8acd4adcd1d289c2905719e05e506`
Outcome: PASS.

I read and rederived the complete theorem, proof, and scope paragraph. R29 and the already reviewed G23 are treated as established inputs; this review checks the extension, not a second fresh audit of every source theorem behind G23.

- R29 supplies the common stable and no-scaling points in the enlarged row range. G21 and R28 dimension formulas already apply for every r>=4 in the stated size range, so the quotient dimensions and parameter degrees are unchanged.
- The replacement lower bounds for u and v are valid: r-2>=r/2, r<=2m-2, and n>=m+1 give the displayed u bound; substitution r<=2m-2 gives the v bound. Both exceed2 for m>=17.
- The action and independent-parameter degrees, Derksen constants, common invariant semigroup, Veronese grouping, image-degree estimate, and every-residue Hilbert comparison have no further r<=m dependence. The no-integer-equality congruence also has no such dependence.
- For r>m, direct expansion at n=m+1 gives Delta=2m(m-r+1)+1. Monotonicity in n proves that r=n=m+1 is the only new positive case. At r=m+1, the next n subtracts (m-1)(2m+3), as stated.
- The explicit partition (3,2^(m-1),1) has exactly m+1 parts, size2m+2 and strict first part3>2; thus s2 and Delta1 are correct. Both multiplicities occur eventually, so the positive inequality is a genuine multiplicity gap rather than an occurrence claim.
- No rectangular strict direction exists when r>m and n>m is integral. The equality-face and earlier-degree limitations are correctly retained.

No finite computation or external independent verification is claimed in this review.
