# K17-POLE-NV-VK: independent audit

Reviewer: /root/vandiver_k, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

**PASS.** I read the entire work/pole_nonvanishing_gate.md and checked each deduction. The weaker hypothesis suffices for the same multi-Laurent argument: the extracted coefficient is a product in the fraction field of a domain, so nonzero restrictions suffice. A unit constant was a convenient stronger arithmetic test, not a necessary condition for this separation argument. The selected ordered pair may depend on the root because different selected pairs occupy disjoint variables. Repeated poles are still handled by the same Pareto-maximal order vector. The note correctly makes no claim of an additional verified arithmetic prime.

For the first basis change, two lifts of the same even abelian class differ by a closed commutator. At target length two only commutators of two odd orbit letters contribute. Their coefficients are bounded integral measure transforms A. Thus B'=B+A and C'=C+qA hold as bounded analytic identities, after checking them on the Cartesian weight grid. On z=alpha the restrictions coincide.

For a different cyclic generator, the companion basis identifies T_e with Z_p[z]/(q_e). The new generator corresponds to a unit b in that ring. Its representative can be chosen polynomial of degree below lambda. The product of companion lifts has target length-two coefficient b(z)B; its correction to an actual lift has an analytic term A. Hence C'=b(z)C+q(z)A. Evaluating a polynomial inverse of b modulo q at any root proves b(alpha) is nonzero (indeed an O_L-unit). This remains valid at repeated roots and proves precisely the claimed divisor-restriction invariance.

Changing an odd Lambda basis multiplies each matching normalized linear moment by a Lambda unit f_a(T). Re-normalizing the rational target letters therefore multiplies the even quadratic coefficient by the inverse product f_a(T_1)f_b(T_2). Both factors remain formal units under every displayed divisor substitution. A different odd lift has no additional linear target coefficient; parity also prevents an odd quadratic target term. Possible even-lift corrections are exactly the qA terms already considered. Thus this basis change preserves the condition.

Scalar extension preserves nonzero power series. The proof deliberately fixes gamma and makes no claim about changing that choice. The example C=p correctly distinguishes the two analytic conditions without being presented as arithmetic evidence.

The proof and this audit were each read in full. This is an extension of the independently audited conditional pole proof, not a separate proof of the unverified arithmetic nonvanishing condition.
