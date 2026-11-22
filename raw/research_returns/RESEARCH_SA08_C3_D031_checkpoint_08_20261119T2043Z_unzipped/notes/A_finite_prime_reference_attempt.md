# Finite-prime reference induction: exact missing map

19 November2026,20:40UTC. Working approach; no main-gate reduction is claimed.

The completed AT29 proof is being checked separately. Its dyadic construction suggests using finitely many local references and a localization inverting their primes for a fixed degree range. The residue choices and coefficient corrections for a finite set can be compared using the actual Chinese-remainder maps. This note records the obstruction encountered before any such wider induction is claimed.

A fixed initial C21 source P contains a normalized coefficient edge x of some weight w0>0, with d1(x)=0 and d0(x)=T^[w0]. At a new prime p>w0, the standard local reference G_p has its first-simplex piece in weight w0 equal to the constant coefficient module S_(p)^w0. Its normalized degree-one piece in that weight is zero. Thus a proposed strict coefficient-preserving map P_(p)→G_p must send x to0, while compatibility with d0 would send d0(x)=T^[w0] to itself. That coefficient is nonzero in S_(p)^w0. These two equations contradict each other. This is the same actual edge obstruction already checked for the standard-tail and inverse-limit constructions; it applies to the proposed new-reference map before any completion step.

Consequently the current work has not supplied maps from one fixed initial P to the standard references G_p at all new primes. Their absence in this attempted construction is not a counterexample to common-source existence: a different local reference, source, or comparison may supply the missing data. Passing to a weight tail supplies an arrow from that tail into P, as in A-S09-24; it does not by itself produce the proposed map out of P. Any use of that tail must retain its actual comparison direction and prove transfer of the additional reference data.

The unresolved step of this approach is therefore explicit: construct compatible reference data at newly introduced primes, including the fixed low-weight coefficient edges, or replace the induction with a construction having proved comparison maps. No increasing-degree integral completion is inferred from the finite degree-three construction.
