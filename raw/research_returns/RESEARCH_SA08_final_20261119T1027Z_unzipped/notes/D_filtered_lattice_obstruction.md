# Full filtered numerical lattice obstruction: audit record

GPT-6 Astra (OpenAI), agent /root/shadows_coalgebras, 19 November 2026.
The complete proof is in sections/A_all_models_obstruction.tex, A-026.
The general argument was proposed by the parent agent and independently
re-proved here; no priority is claimed.

## What closed the remaining gate

For an exhaustive filtered R=Int(Z)-module with gr M_i=I_i, successive
filtration quotients are free of rank one. Choose integral basis m_n,
n>=i, representing T^[n]. Rationalization is Q[T] times the bottom
basis vector. Normalizing that vector to1 gives leading coefficient
i!/n! in degree n-i. Crucially, Tm_n=(n+1)m_(n+1)+integer lower terms
forces EVERY polynomial coefficient of m_n to belong to(i!/n!)Z.
This eliminates arbitrary extra denominators in lower coefficients.

At any odd prime p, f=p m_p of M1 modulo p divides P=T^p-T, with
degree p-1: pF_(p+1) modulo p is span(f,Tf), and contains p beta_p.
Thus f is nonzero at exactly the missing root a of its p-1 roots.
For M2, the reduction of p^2F_(2p) is a single line. Multiplication
beta_p m_p, whose top coefficient is binom(2p,p), identifies that
line with the multiples of P g, where g=p m_p of M2 modulo p.
Any filtered bilinear pairing is rationally multiplication by an
integer c. If c is nonzero, choose p not dividing c. Then its value
on m_p squared would give c f^2 in that line, impossible at a.
Hence every filtered pairing M1 tensor_R M1 -> M2 is zero.

For the intended cup, c=2 and p=3 suffices. This covers arbitrary
filtered rank-one lattice deformations, not only the numerical
evaluation ideals J_i. No classification of Int(Z)-ideals, no
Prüfer property, and no p-adic valuation-domain theorem is used.

## Independent finite enumeration

The program code/D_filtered_lattice_gate.py enumerates all 3-local
filtered lattice possibilities through M1 weight5 and M2 weight6.
It uses the binomial basis beta_d. The next leading-coefficient
index is binom(d+i,i), so an index3^e extension has generator
(beta_d + sum a_j v_j)/3^e with0<=a_j<3^e; this is a complete list
modulo old lattice changes. Every R multiplication staying within
the cutoff is tested with exact rational arithmetic.

Surviving counts by polynomial degree:

- M1:1,1,9,3,3.
- M2:1,3,3,3,3.
- Compatible pairs among the final3 by3 possibilities:0.
- Exact membership checks:2005.

All bases and outputs are in logs/D_filtered_lattice_gate.json.
Three explicit assertions check these counts and the empty pairing
list. The latest runtime is in that JSON. The initial exploratory
floor-division error, caught before using its result, and its exact
fix are documented in logs/D_filtered_lattice_gate_runs.txt.

## All-space passage

Only S1 and S1 times S1 are needed. For S1 the coefficient maps lift
every associated-graded H0 class, so finite-stage cofiber long exact
sequences give gr H1=I1. For the torus, its two projections lift all
associated-graded H1 classes from the circle; hence the same long
exact sequences give gr H2=I2. Filtered colimits are exact, so no
unbounded spectral-sequence convergence claim enters. The cross
cup product is R-bilinear with bottom coefficient2, contradicting
the lattice theorem.

The hypotheses are retained explicitly in A-026: exhaustive
nonnegative filtration, coefficient maps, natural pullbacks,
R-bilinear products, and an actual associated-graded equivalence
to the weighted PD cochains. The constant total-derived numerical
object in D-026 fails the last condition already at weight0 on S1,
and therefore remains a valid weaker shadow construction.

## Exploratory routes not used in the proof

The modulo-p T eigenspace calculation alone only gives one missing
residue for M1 and two for M2; it permits support containment and
does not prove the pairing obstruction. An attempted classification
by evaluation ideals was not established. Searches of regular-basis
and Prüfer-domain literature supplied no required classification.
Those approaches were superseded by the elementary coefficient
bound above. The proof must not be described as depending on such
an unproved classification.
