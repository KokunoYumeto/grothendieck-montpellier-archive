# L1 after the main counterexample

The precise user request is constructibility of M(T,eta) for T locally of finite type, under the manuscript axioms. The counterexample to A.1 does not logically refute this separate assertion. Its modularity locus is in fact open, as proved completely in sections/A_finish_L1.tex (A:hensel-L1-open). The base opens are U0 where t is locally nilpotent, and U1=D(t). P is alpha_p and terminal respectively. A modular point outside these opens would have a finite formal alpha_p hull; after completing the local base, quasi-finiteness and Zariski Main yield a finite local actual modular pair, contradicting the previously audited nonexistence argument.

This does not repair the proposed noetherian induction: modularity after closed base change remains distinct from the original local test condition. A potentially positive general route would apply the uniform Artin-Rees propagation pointwise, starting from an actual modular point, rather than requiring actual representing models for every point of the functor. No complete proof of that adaptation has been supplied here.


## Pointwise uniform-AR route: remaining distinction

An actual modular point produces a finite actual branch after completing its local base, so literal7 makes that branch modular at all its points. However the uniform-AR propagation in A:local-models-suffice uses an actual representing finite local model D at every later point w. Condition5 and condition4 alone give a finite pro-hull D_w; modularity modulo I^N identifies its quotient with the finite source quotient, and AR can identify the complete rings, but this does not upgrade the pro-hull to actual modularity. The main P counterexample is exactly a warning against that upgrade. A separate all-point modular-chart descent or saturation argument remains needed.

A direct sum of P_f over infinitely many distinct irreducible f does not give an L1 counterexample under all axioms: although its zero-chart modularity locus on the base is the complement of the selected closed points, if those points are dense it violates condition8 already at the generic zero section. This attempted route is rejected, not a claimed example.


## 16:15 UTC: general L1 proof closes the remaining gate

The conceptual obstruction above is resolved by tracking the weaker Artinian formal-etale locus E and its maximal open interior U. The completed actual branch supplied by literal7 is a represented etale chart; an open fpqc refinement lemma descends formal lifting (not actual modularity) to the original local scheme, giving pro-generization from each actual point. At a generic boundary point, the finite-thickening base is Artinian, so A:artinian-base supplies the actual generic representation required to invoke8. Uniform Artin-Rees at later points only needs a finite pro-hull and proves E there. The maximal-open boundary argument then gives M subset U. The chart on U has an open represented, separated, locally quasi-finite image, and the local-ring-isomorphism locus is open.

Read the complete sections/A_finish_L1_general.tex and independently audited all four statements; all pass. Detailed events are saved in checks_A_L1_general_audit.tsv. Earlier statements in this note recording general L1 as open are historical and are superseded by A:L1-general. No inference from main-theorem failure to L1 was used: the two conclusions are main criterion false, L1 true.
