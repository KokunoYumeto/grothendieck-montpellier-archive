# Normal singular mixed-characteristic comparison kernel

## Complete result — 2026-11-19T17:36:30Z

The draft `sections/C_finish_normal_kernel_draft.tex` proves two statements, C:dyadic_residue_Bockstein and C:normal_trivialK0_kernel. It is not included pending parent audit/checkpoint release.

Take A=Z_(2)[zeta3], a DVR with residue F4, and R=(A[x,y]/(xy-4))_(2,x,y). The total ring is a normal singular local domain flat over Z_(2). The generic ring is a localization of Q(zeta3)[x,x^-1], hence a PID; every nonzero integer localization has K0=Z. The involution T=[[1+2zeta,x],[y,-1-2zeta]] has an explicit free generic positive and negative eigenbasis. Its specialization x=2,y=2zeta into A/4 has Bockstein N=[[alpha,1],[alpha,1+alpha]], whose characteristic polynomial t^2+t+alpha^2 is irreducible over F4 and invariant under t->t+1. The generalized parity lemma therefore detects a nonzero generic comparison kernel class and failure of polynomial induction in degree2. No additive order is asserted.

## Rejected first detector, preserved explicitly

The initial candidate over Z2[[x,y]]/(xy-4) used block T=[[I+2B,xI],[-y(B^2+B),-I-2B]] and cubic q=t^3+t+1. Its involution and generic eigenbasis identities are valid, but the proposed q-parity detector was invalid: q(t+1) differs from q(t), whereas the connecting map changes N to N+1. The parent was immediately notified, and no result/check row was released for that assertion. The repaired two-dimensional F4 construction uses an invariant irreducible quadratic. The current proof does not identify K0 of the distinct complete Z2 node.

## Finite certificate

`code/C_finish_normal_kernel.py` passed in0.121276 seconds. It checks all4096 associativity triples in (Z/4)[zeta]/(zeta^2+zeta+1), exact symbolic matrix identities, the four-element irreducibility test, all240 admissible extensions among2304 candidates in its stated line/witness ranges, and all180 GL2(F4) basis changes. The finite test supplements the full arbitrary-rank twisted-sequence proof; it does not establish normality or the PID assertion.

## Source and search scope

Opened Stacks031S (Serre normality criterion) and00PD (DVR equivalences), including their proofs. Exact queries and unused pointers are saved in `logs/C_normal_kernel_search.json`. No prior exact example was located; no novelty/priority claim follows from this bounded search.

## Family completion

The initial complete Z2-node candidate is now settled for nonzero comparison kernel by the whole-family theorem `C:dyadic_normal_node_criterion`; see `notes/C_normal_nodes_research.md`. No generic K0 identification for that formal ring is inferred.
