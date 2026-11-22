# Rescaled genuine datum and induced-order scope certificate

Author: GPT-6 Astra Pro, effort inherited/not externally exposed, MAS_ARTIN `/root/pf26_audit`. Date: 2026-11-21.

## MA-FQ-007

The construction was suggested by the MAS_ARTIN `/root/s5_audit` agent. I independently checked every Booker axiom, using the exact primary Definition 1.3 and Examples 1.4 on printed pages 3–4 of the private Booker PDF. No outside author was contacted.

Start with the actual difference of the zeta and primitive even quadratic mod-five data. The scaling is `m2(z)=m0(2z)` and `f2(n²)=2f0(n)`, with zero at nonsquares. The explicit formula uses the old test `2g(2x)`, whose transform is `h(z/2)`. There is no Jacobian in discrete multiplicities. Including the value at one gives `f2(1)=log5`, analytic conductor `1/25`, and completion `5^(−s+1/4) zeta(2s−1/2)/L(2s−1/2,chi5)`.

The new function has nonnegative Dirichlet coefficients, exact abscissa `3/4`, and simple completed poles at `1/4` and `3/4`. A1 is especially easy: `f2(N)=O(N^(−1/4)logN)` and its mean square is `O(log³X)`. The full completed divisor remains integral and polynomially counted after scaling. Thus this is an actual L-datum, not just a formal Euler expression.

The example has nonnegative prime-power coefficients, but it is not positive in Booker's separate spectral sense. The already proved MA-LD-003 degree-zero argument supplies infinitely many negative masses, preserved by scaling. It invalidates the abstract replacement of real-height support by abscissa below one. It does not satisfy the S5 finite-image coefficient bound: at arbitrarily large nonsplit primes its `f2(p²)=4 logp/sqrtp` is too large by a factor proportional to `sqrtp`. Its good support is also at exponents `2 mod 4`, rather than the S5 odd exponents. No family-specific counterexample is claimed.

## MA-RB-004

The formal off-center order character is the genuine character `Theta=k(Veta+W)`. The proof expands the finite induction formula, proves the exact Frobenius reciprocity pairing for every subgroup and every genuine character, and obtains a nonnegative integer from the restriction decomposition. It covers all relative abelian Hecke holomorphy order constraints, not just a list of subgroups.

With the automorphic numerator order zero, the assignment has `v1=k`, `ordW=k`, all other irreducible orders zero, `q_gamma=r4=r5=0`, and regular order exactly `9k`. Hence neither the bound `v1+e>=k` nor the `9k` bound can be improved solely by these inequalities. This is a mathematical compatibility certificate, not a construction of a field or of L-functions realizing the orders. It does not shrink the remaining shared-real-zero gate. MA-RB-005 is owned by the S5 agent and concerns distinct quadratic Schur-functor checks.

## Proof and file status

The entire 351-line initial module was reread after writing; the later changes only split two long displays. All mathematical steps passed the author's complete proof QA. Eighteen equation tags are unique in the working modules and the environments balance. Root and S5 complete independent readings have been requested and are not yet claimed here. The private primary-source PDF is not included in deliverables. The parent owns master integration, PDF rendering, checkpoint archives, and final persistence.

Root completed an independent reading of the whole module and freshly reread Booker Definition 1.3 and Examples 1.4 on pages 3–4; both new proofs passed. Root is recording that independent event and integrating the module. The S5 peer reading remains pending.

The S5 agent has now also completed the entire independent proof reading, freshly rereading Booker pp3–4. Both FQ007 and RB004 passed; its three scoped review rows are in s5_scaled_datum_s5_review_events.tsv. Subsequent RB005 and RB006 retain the same formal witness under the additional stated quadratic Schur and Rankin constraints.
