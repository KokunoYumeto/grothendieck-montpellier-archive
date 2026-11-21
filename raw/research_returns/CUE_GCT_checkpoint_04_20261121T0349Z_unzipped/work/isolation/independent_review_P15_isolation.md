# Independent complete proof review of P-15

Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I

Actual review completion: 2026-11-21T03:40:12+00:00

Reviewed source: work/purity/P15_width_three_one_pair_obstruction.tex

SHA256: 071d0ae09ab4a2238386086dbaac466e34065be05f8122e2afc618ff075d7a85

**Outcome: PASS; no revision requested.**

I rederived every coefficient in the width-three unipotent representation. All factors and intervals have determinant one; nilpotent products of length three vanish, and the six earlier-to-later two-step paths give exactly the displayed quadratic. The coefficient matrices at the three balanced partitions have ranks3,4,4 in characteristic zero, proving minimum width three over all orders.

For fourth-root nodes, I recomputed the Lagrange polynomials and their combinations S=y^2, U=(y^3+y)/2, V=i(y^3-y)/2. The identity2F=S^2-U^2-V^2 proves vanishing, while common-translation invariance and homogeneity give the full centered identity.

I checked all three ordered harmonic quadruples, the Möbius difference formula, and the common four-factor denominator. The constant-map and pole-domain qualifications are correct. Padding with identity factors gives the standard integer-abscissa example. The text correctly distinguishes balanced rational evaluation on the integer grid from ordinary centered SV1 at that grid.

P14 supplies two pairs for this full-rank width-three subclass; the example shows one pair is insufficient uniformly over valid node choices. It does not disprove two pairs for the full width-three class or a linear-pair bound at larger width. No fresh numerical execution or independent reopening of the HMM primary source is claimed in this review.
