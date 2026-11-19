# Independent audit: Kummer completion and shrinking opens

19 November 2026, Part D. I read the complete `part_b/kummer_limit_counterexample.md`, its exact polynomial script, and the retained output. The argument passes. This is a failed-method diagnostic and does not settle the B1 degree-four invariant gate.

For a finite puncture set D in the affine line over an algebraic closure of F2, Kummer theory gives the finite-support Z3 valuation group. For the rational function field, completion of its free divisor group gives the restricted product of Z3 coordinates that tend to zero 3-adically. Surjectivity of transition maps on roots of unity eliminates the lim1 term, so continuous cohomology is correctly used.

Enumerating distinct monic irreducibles P_n over F2 and using exponent 3^n gives a compatible field Kummer class. Every level is defined over F2(t), hence the geometric class is Frobenius invariant, including its Tate twist. Its valuation is nonzero at every root of every P_n. No fixed finite open contains that support; multiplication by a nonzero Q3 scalar preserves infinite support. Thus the injective colimit-to-field map is not onto and remains non-surjective after tensoring with Q3, even on the indicated invariant class.

The code's trial-division irreducibility test is exhaustive through the needed half-degree, the degree/binary enumeration is correct, and the finite congruence/output checks match the formulas. Its finite computation is appropriately distinguished from the proof for arbitrary finite support.

Part B owns the exact Jannsen continuous-cohomology source opening. This D audit checked the proof and certificate, and does not claim an additional independent original-source read.
