# A47: one bounded probe and the remaining quantitative supply obstruction

Date: 2026-11-21. GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

## The one requested degree-117 probe

The full cyclic order-nine quotient and order-thirteen quotient from A45 give an actual cyclic117 quotient of the same Jacobian over F256. The Frobenius action over F4 is 73 modulo117, of order four. Every point label is obtained by CRT from the retained and independently checked a9/a13 labels. No new Jacobian arithmetic is needed.

`probe_A47_conductor117.py` and its JSON retain all117 counts, all256 CRT labels, the exact cyclotomic reduction and a binary Bezout certificate. They prove that L117(1) is a unit in the full primitive cyclotomic algebra at2. Thus the actual primitive117 rational two-primary exponent is **one**. It is already an A46 witness, and **does not** give the sought positive-exponent strict example for A47 over the existing union of criteria. This was the single bounded probe requested; no additional example search was started.

## Why the coarse Weil estimate does not supply the new gate in genus two, characteristic two

Consider a constant pointed cyclic cover over F_q, q a power of2, of odd degree n>1. Put B=(sqrt(q)+1)^2 and f=ord_n(2). The pointed abelian class-field quotient gives n dividing #J_C(F_q), hence n<=B^2 by the genus-two Weil bound.

The actual primitive factor has dimension phi(n). Its rational two-primary group is a module over Z_2[Z]/Phi_n(Z), a product of unramified discrete valuation rings of common residue degree f. A component containing an element of order2^a has an O-span of cardinality at least2^(fa): its annihilator ideal is exactly(2^a). Therefore, if its exponent is M_n,

    M_n^f <= #P_n(F_q) <= B^phi(n),

and the coarse estimate is M_n<=B^(phi(n)/f). Since phi(n)/f>=1 and 2^omega(n)>=2, substituting this estimate in A47 asks for a threshold at least(2B-1)^2, larger than the available n<=B^2. The direct substitution never certifies the criterion.

Even rounding this upper estimate down to the largest permitted power of2 cannot fix the mismatch. For q>=8 the coarse bound permits M_n=q; then 2q-1>B. The latter follows from q-2sqrt(q)-2>0 at q=8 and monotonicity thereafter. At q=2 the largest power of2 not exceeding B is4; at q=4 it is8. Their respective minimal thresholds7 and15 also exceed B. A larger value of phi(n)/f only makes the permitted coarse exponent larger.

For a nonconstant-deck cover, its primitive exponent is unchanged at its own minimal deck field by SD.10. Applying only the same coarse estimate after that field extension has the same failure. This is an obstruction to this particular estimate, not a theorem that the actual exponent is large and not an absence theorem for useful covers. Rank information or exact local character values can make the actual exponent much smaller, as earlier findings demonstrate.

The finite-field group-action assumptions in the order lower bound matter: before deck constantization the rational points need not themselves be a module over the full cyclotomic algebra. The descent equality is used first; no illicit full-algebra action over the original field is assumed.

## Remaining input

The exact open sufficient input on each ordinary O5 genus-two target and prescribed point is a pointed cyclic cover with actual primitive exponent M_n<(sqrt(n)+1)/2^omega(n), or one of the other already proved alternatives. Hooley's arithmetic density does not bound this exponent. Coarse Weil estimates cannot bridge the gap above. A useful universal supply theorem would need finer control of the actual local character values, a geometry forcing their p-adic units or small valuations, or a different prescribed-point separation construction. No such theorem is asserted by A47.
