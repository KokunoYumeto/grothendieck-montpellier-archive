# A29 complete-proof and delta review

Date: 2026-11-21. Reader: GPT-6 Astra Pro, /root/row_audit; effort not exposed.

**PASS.** The full proof at SHA256 `92585ca4d2939062fd0c294d4906c6b454a210108aa357531a70722e6f00a2c0` was read from its statement through the residual-scope paragraph. The appended actual-curve strictness corollary at SHA256 `feb70cad020af94c8d471e4c97741eaf68e8d28a8381c09da164c38df46bb6b7` was then checked as a narrow delta. This is a targeted proof check by another reader, not an independently authored re-proof or formal verification.

The finite-group projection detects a nonzero primary component without requiring survival modulo r. Cyclicity of the odd prime-power unit group gives inversion for the actual order, independent of Wieferich behavior. The Lang cover is connected by the Jacobian universal property and is constant with rational split fibre. The genus-two Euler polynomial follows coefficient by coefficient from Riemann--Roch; its canonical symmetry forces faithful factors to be p-units. Exact cancellation of imprimitive factors identifies the top-step Prym point count. The image of tau-1 is that connected Prym, so a rational p-primary collision class is fixed by a free order-r deck automorphism. Its degree-two pencil is separable, unique at genus at least four, and forces a geometric deck fixed point, a contradiction.

I reopened and read all complete retained proofs of recovered A1 B.1/B.2/B.13/B.14 and successor A.25/A.26. Their scope agrees with the argument; no unseen geometric realization of the B.14 module examples is used. The source detector at prime degree is credited. Rational p-primary vanishing, geometric p-rank zero, and absence of all cover witnesses remain distinct.

For the strictness corollary, the exact13 class on A09 remains nonzero after rationalizing a [13]-division point. It becomes divisible by every odd prime in the larger rational group, but retains a detectable nonzero13-primary component. A detecting13-power quotient must then have order at least13^2. The argument explicitly leaves the existing geometric prime13 witness available. No mathematical correction was needed.
