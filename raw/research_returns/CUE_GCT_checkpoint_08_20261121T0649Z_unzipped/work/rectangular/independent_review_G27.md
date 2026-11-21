# Independent whole-proof review of G27

Reviewer: /root/rectangular_bridge; GPT-6 Astra Pro; effort inherited/not exposed.
Date: 2026-11-21T06:25:55.554745+00:00
Fragment SHA256: `1c3a8c771b4eeb7355958a21364cf42526cfcfceb4e1f36f48c194228db3ff08`
Outcome: mathematical PASS after complete theorem, proof, constants and scope reading.

- R32's two applications have the advertised degree and row ranges, and only the determinant direction needs to be nonrectangular. The lower tail can be rectangular because stability and exact quotient dimension are sufficient there.
- The exact u-v expansion at n=m+1 is(2m-1)r-m^2-2m-1, giving m^2-m-2 at r=m+1. The lower bound for v follows from q>=m and q<=2m-2 and is correct.
- For the lower-domain homogeneous generators, dividing all degrees by their gcd g gives a numerical semigroup of gcd one. Its conservative conductor implies occurrence at every multiple of g at least beta^2. Conversely every nonzero homogeneous degree is divisible by g. This does not assert saturation outside that congruence class.
- Since g<=beta and E is divisible by beta!, g divides E. Whenever B_j is nonzero and j=Ek+t, g divides t, so2E-t is an occurring positive degree and multiplication gives the upper embedding. The zero case needs no map. The determinant lower embedding uses its own period-one elements.
- Both effective ambient/group/action/parameter bounds retain the G26 domination arguments. Standard Veronese image degree, Noether lower bound and Chardin upper bound have the stated indices and dimension. The threshold forces the strict binomial comparison.
- Below the first-row face, the determinant's independent R32 application and beta_D bound apply without inventing a lower tail degree. Strict directions use G25. The final nonrectangular classification and residual rectangular/end-row gates are exactly scoped.

A formatting-only point was sent to root: the fragment begins its proof immediately with a paragraph heading, the same pattern that previously caused amsthm Improper prevdepth. No mathematical revision requested. No new finite computation or fresh full source-proof audit is claimed.
