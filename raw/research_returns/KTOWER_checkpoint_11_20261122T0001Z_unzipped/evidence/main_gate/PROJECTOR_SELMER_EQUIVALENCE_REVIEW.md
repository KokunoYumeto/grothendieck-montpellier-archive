# Independent complete-proof review: odd conormal = strict Selmer dual

Reviewer `/root/geometry_tower`, GPT-6 Astra Pro, effort not exposed, KTOWER,2026-11-21 UTC.

**PASS.** I read the entire241-line `../unitary_audit/projector_selmer_equivalence.tex`, SHA256 `8402e6ea3caab6a0495f89d2c137e53510d826eccb9339e5742a514dc443b891`.

The exact source's rational trivial character has modulusN=2. `ClassNumberThree.lean13–32` identifies Vlen with ShaU for the character epsilon^(−e) and parameter2ell; `ConjStableShaFam.lean94–96,167–169` imposes all inertia conditions and full decomposition-group conditions at2 andell. I read these definitions and the complete conjugacy proof displayed between them. I also read the entire shaInj_norm proof, the exact DatFacts Kill characterization, and used the independently whole-reviewed integral ordinary component and actual Cayley slice.

The inverse is valid for the following reasons:

- The marked g1 makes alpha(g1)−1 a unit, so global H0(K/O)=0. Hence H1(O/b) identifies with H1(K/O)[b], and normalization atg1 is unique and O-linear.
- At the base, odd weight−1 left cocycles are exactly t(E21−E32). The actual odd marking is(q+1)t(g1); Marked makes q+1 a unit. Thus both changes of slice are the identity on this normalized dual-number direction.
- The unique ordinary local flag has lower-unipotent coordinate1+epsilon W. Projecting its local conjugacy coboundary to odd weight−1 gives a scalar local coboundary, including inerteta. Conversely a local scalar coboundary gives an ordinary dual-number lift on the actual It component.
- On all away-prime inertia, alpha is trivial, Kill contains the index-at-most2 kernel ofeta, and a continuous additive map factoring through that quotient is zero because2 is invertible. The ramified quadratic place3 is included.
- At2, the class is unramified and H1_unr(Q2,K/O)=M/(2^(−e)−1)M=0. The nonzero scalar acts surjectively on the divisible module. This is deliberately not asserted for finite coefficients.
- Atell, GD supplies an inertia element acting nontrivially moduloell, hence H0(K/O)=0 locally. This makes H1(O/b)→H1(K/O) injective, so the strict local class is already a finite-coefficient coboundary.
- The explicit coefficient embedding u↦u/b makes the inverse maps compatible with the torsion-chunk transition maps. Finite generation of the cotangent gives its full dual as the union of the bounded chunks. Finiteness of the original Selmer module then removes any free cotangent summand and gives equality of lengths.

This theorem sharpens the **scope** of the projector result: the unit-minor criterion is exactly equivalent to the original strict Selmer vanishing problem. It has not produced a smaller arithmetic obstruction or evaluated a minor. No Lean compilation or new global vanishing theorem is claimed.
