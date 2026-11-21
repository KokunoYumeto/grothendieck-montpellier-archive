# Independent whole-proof audit of the two-class U3 model over −7

**Verdict: PASS.** Agent /root/vandiver_k, GPT-6 Astra Pro; effort not exposed;
21 November 2026, run K17.

I read the complete u3_minus7_section.tex and reconstructed the entire
proof. I freshly read Loeffler's §§2.1–2.2 (printed pp3–4), Lemma2.5,
and the full §3 (pp6–7). I read every line of the independent 319-line
verify_schur.py and its actual PASS output. The output hashes were
recomputed against every current input and all matched. I did not rerun
the approximately20-second verifier a further time: root and the author
already executed it, and this audit does not invent an additional run.

Reviewed TeX hash:
b3def8f65fde4fa3540d5ce2a2e2fd95b790550cd9a18acb93187b520d6240c0.
Reviewed independent verifier hash:
2a62bcae93ce3d57829353a4ddb1a626d1df71da42b61619be00c4e9c73dcf6d.

## Complete reconstruction

The exact source supplies the group G=U(I3), the full integral level,
two adelic classes 1 and alpha, their stabilizers of sizes48 and336,
and containment Gamma1 in Gamma2 of index7. The completeness follows
from mass1/42=1/48+1/336. Thus W1 plus W2 is the entire modular-form
space. The second class is retained throughout.

For the actual positive minuscule cosets, the scalar norm bound proves
the stated finite enumeration exhaustive. Canonical column signs and
permutations quotient exactly the right integral signed-permutation
group. For norm2 frames, the determinant congruence has valuation1
at the omega embedding. For norm4 frames it has valuation2, and the
column parity condition is exactly integrality after multiplication by
alpha inverse. The remaining determinant valuation is1. Integral
matrices with determinant valuation1 have Smith type(0,0,1).
Unitary duality treats the conjugate prime; outside2 all matrices and
inverses are integral. The actual6 and7 distinct frames, together with
the source's missing alpha coset, give all7 neighbors in each row.

The upper-right block is inclusion because that coset has rational
multiplier1. The lower-left block maps W1 into W2 by the genuine
Hecke correspondence, not by fitting evaluations. This validates the
block matrix used for the Schur elimination.

For the coefficient module, the contraction identity is correct:
C(R^(j+1) C^j F) has coefficient (j+1)(2k+1−j) on R^j C^jF.
The stated recurrence is a right inverse. At k15 its denominators
have prime factors at most31, so it remains split at the large prime.
The harmonic module is the entire highest-weight(15,0,−15) module,
with dimension16³. Its lattice over Z_(q)[omega] is free and commutes
with reduction. The residual polynomial is irreducible by the exact
Legendre-symbol check, giving F_(q²), as required for inert q.
Orders48 and336 are units, so Reynolds averaging proves invariant
reduction compatibility. The same denominators2 in the finite group
and neighbor matrices prove lattice preservation.

All signed-permutation invariant orbit sums are exhausted by the
parity condition and simultaneous permutations. Counts795 and624
are independently reconstructed by the verifier. The full contraction
is reconstructed directly on monomials. The saved171 columns lie in
its kernel and have independent free coordinates. I additionally
checked that every actual sparse column has distinct row indices;
there is no duplicate-index ambiguity in that free-coordinate claim.
Surjectivity of contraction on invariants gives dimension795−624=171,
so these are the full reduced W1.

E0=4295032833 is a unit. Eliminating the W2 coordinate gives exactly
D=E0²−E0*2^15*S11−2^30*inc*S21. Block elimination works on both
the coefficient lattice and its residue field, with only unit scalar
factors. Consequently invertibility of D suffices for the full
two-class operator; no dimension or basis of W2 is being guessed.

For a norm2 frame, the two homogeneous denominators are omega^15
and bar(omega)^15, whose product is2^15. For norm4 they are the
squares and the product is2^30. The resulting substitutions are
U* z,U^t w and V* z,V^t w. They agree exactly with the program's
column conventions. Thus the three evaluation determinants have
the correct relative scaling.

Evaluation is used only after actual preservation of W1 has been
proved. The first171 rows have nonzero determinant9611653439256081,
so they identify the endomorphism on the full module. The independently
recomputed Schur evaluation determinant18272413515919144 and the
operator determinant13187546903051047 have the verified quotient
relation. All173 rows and all13 frame substitutions are checked;
the last2 rows are extra consistency checks, not completeness claims.

Complex conjugation preserves the full adelic level and exchanges
the two minuscule directions. The coefficient swap J(z,w)=(w,z)
satisfies the required intertwining identity. Conjugate-class
comparison multipliers are integral at q because both class
representatives are identity there. Hence the opposite operator is
integrally conjugate on the full class space. The Satake scale
2^15*T2=2^16*trace is the standard GL3 positive-minuscule normalization.

## Verifier and numerical scope

The Python verifier uses arbitrary-precision integer arithmetic in
F_q[omega]/(omega²−omega+2). The norm inverse is valid because the
polynomial is irreducible. It proves primality of q by full
factorization of q−1, primality of all those factors by trial division,
and multiplicative order q−1 for3. It independently reconstructs all
frames and orbits, proves agreement of all text and JSON inputs,
checks the kernel, and recomputes every saved transformed evaluation.
Its column elimination is independent of the producer's row
elimination and verifies all three determinants.

I do not claim to have reviewed the separate C++ producer in this
event. The complete independent verifier checks its entire
mathematical output. I also do not infer K32 from this finite theorem
alone: the separate actual source/GD, U3 transfer, and all-twists GL2
bridge are required. Those were separately whole-read and logged.
