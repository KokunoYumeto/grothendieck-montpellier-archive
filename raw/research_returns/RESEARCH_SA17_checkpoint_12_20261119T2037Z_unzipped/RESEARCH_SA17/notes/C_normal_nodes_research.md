# Whole-family normal dyadic-node criterion

## Proved and independently audited

The final section `sections/C_finish_normal_nodes.tex` proves C:dyadic_normal_node_criterion for every characteristic-zero DVR A with maximal ideal(2), every unit u, every exponent n≥1, and either the localized polynomial node or the formal power-series node xy=2^n u. Polynomial induction in all degrees, degree-two surjectivity, n=1, and total-ring regularity are equivalent. For n≥2 the explicit difference from free sign lines is nonzero in the generic comparison kernel, of rank2 when n≥3 and rank6 when n=2. No additive order or complete kernel group is asserted.

The target residue field is transcendental kappa'(s), not the original residue field. Thus the Artin–Schreier simple-pole test works even if kappa is algebraically closed. The n=2 companion cubic X^3+X+1 either already splits in kappa or is irreducible; in the latter case its monic lift gives a finite local DVR extension with maximal ideal2. The three distinct beta_i^2+beta_i give three distinct invariant quadratic primaries, one detected with length1. All base changes and formal power-series evaluation are written explicitly.

Normality of formal nodes is proved directly, not inferred from completion preserving normality: regular ambient power-series UFD, x=0 specialization excludes a factorization, and the derivative test makes localizations away from2 regular. Polynomial nodes have generic PID and all integer-localized K0=Z. The proof deliberately does not identify K0 of formal generic rings. It does establish the nonzero degree-two kernel for Z2[[x,y]]/(xy-4), the original proposed candidate.

A particularly small concrete case is R=(Z_(2)[x,y]/(xy+8))_(2,x,y), T=[[3,x],[y,-3]]. The specialization x=y=2 gives the original F2 quadratic Bockstein t^2+t+1; no coefficient-field extension is needed in that example.

## Validation and scope

Root and representations each read the complete actual proof and passed. `checks_C_normal_nodes_representations_audit.tsv` is separate. Exact code `code/C_finish_normal_nodes.py` passed in0.10201 seconds: symbolic n2..10 identities, all7 nonzero F8 residue units, three primary blocks over F8[s], and the elementary xy+8 example. These are bounded checks, separate from the arbitrary-exponent and arbitrary-residue proofs.

Primary source newly opened: Stacks0AG0, Lemma15.123.2, regular local rings are UFDs. Stacks031S and00PD were already opened and applied in the normal-kernel section. The positive direction explicitly reuses and rechecks C:regular_noetherian for characteristic-zero regular local rings.

## Remaining scope

This is a regularity criterion within one entire normal modular-singularity family. It is not a necessity theorem for all singular mixed-characteristic rings. Ramified dyadic nodes and odd-prime nodes remain possible next families; the relative singularity-category route remains a separate research avenue.
