# Independent audit: all affine-cover integral lattices and one inner conjugator

Auditor: OpenAI GPT-6 Astra, elliptic_splitting, 19November2026.
Read the full current `work/agent_affine_integral_automorphism_completion.md`.
Canonical result: E.2.28.
Verdict: AF1–AF7 pass, with the precise scope in AF8 retained. No production
edit, discrete-recognition claim or Galois implication is added.

1. **Actual embedded completions (AF1).** The subgroup mA_N is normal
and finite index in Gamma_N, and detects every nonzero integral vector.
Thus residual finiteness gives F intersect D_N=[K_N,K_N]. The finite
quotient argument identifies P_N with the profinite completion of this
actual Gamma_N. The induced topology on A_N is full because every
mA_N occurs. Density of K_N in N and continuity of commutators give
D_N=[N,N]^closure. For a cofinal chain, compatible P_N-coordinates
lift to nested nonempty closed cosets of D_N in compact G, whose
intersection is a singleton since D_N⊂N. Restricting these actual
coordinates gives H=lim Gamma_N, with the stated finer inverse-limit
topology; no equality with the subspace topology is needed.

2. **Every original integral cover lattice (AF2).** Given z∈H∩U,
choose normal N⊂core(U) and f∈F with zf^-1∈D_N. Then f∈F∩U, and
D_N lies in the kernel of U→U^ab, proving exact equality of the images.
For g∈G choose f∈F∩gU by density. Writing g=fu makes the two conjugated
covers equal, and ad(u) has trivial abelianized action. This is an
actual integral change-of-basepoint map, not a separate lattice choice.

3. **Abstract averaging quotient (AF3).** Although A_N is not closed
in P_N, it is normal: conjugation on Ahat_N factors through Q_N and
preserves A_N. The quotient P_N/A_N is legitimately used as an abstract
group. Ahat_N/A_N is uniquely divisible. Surjectivity of multiplication
by m comes from subtracting an integral residue representative modulo m;
injectivity comes from divisibility of an integral vector in every Z_p.
The two Gamma complements are genuine complements and their difference
is a Q_N-cocycle. Summing c(qr)=c(q)+qc(r) gives c(q)=v−qv with the
stated v, so conjugation by −v has the correct sign. The resulting
solution set is the left coset B_N t_N of the normalizer.

4. **Normalizer (AF4).** Ahat_N is abelian and its Q_N-invariant part
is central in P_N. After removing a Gamma_N element with the same
finite quotient, normalizing Gamma_N is precisely the finite family
(q−1)a∈A_N. Stacking these integral linear equations and taking Smith
normal form is sufficient: if an integral right side has a Zhat
solution, every diagonal divisibility condition holds in Z. Subtracting
an integral solution leaves exactly an invariant profinite vector.
Hence B_N=Gamma_N Z_N, with no cohomological saturation omitted.

5. **Transition map (AF5).** In the regular bouquet cover, A_N is the
literal integral cycle kernel inside the edge module. A deck-invariant
chain has constant coefficient on all edges of a fixed label, and
these sums are cycles because the initial and terminal vertex sums
agree. This proves both the integral and profinite invariant bases
directly in permutation coordinates. Under the actual map of covers,
each target edge has [N:M] preimages, giving e_j^M↦[N:M]e_j^N. Although
this map on invariant parts need not be onto, every invariant profinite
coordinate has an integral residue representative modulo that degree.
The integral residue lifts through Gamma_M, and its remaining multiple
lifts through Z_M. Multiplication of these actual lifts proves
B_M→B_N onto. Centrality makes the expression compatible with the
chosen Gamma lift.

6. **Global compatible conjugator (AF6).** A desired lower-level
solution differs from the image of any upper-level solution by an
actual element of B_N. AF5 lifts that element and therefore proves
surjectivity on S_N. Countable successive lifting yields compatible
coordinates; compactness is used only afterwards for the closed
D_N-cosets in G. Thus it produces one h∈G rather than unrelated local
conjugators. Preservation of H gives preservation of every cover
lattice by AF2; conversely the given lattice hypothesis supplies the
local averaging input. This proves all three equivalent conditions
within actual continuous automorphisms of G.

7. **Generator criterion (AF7).** Images of the specified free
generators in H force alpha_N(Gamma_N)⊂Gamma_N on every characteristic
level. The induced integral matrix on A_N has the original invertible
profinite completion, hence its integer determinant is a unit at every
prime and is ±1. Therefore A_N maps onto itself. Surjectivity on the
finite quotient then makes the entire image Gamma_N. The argument
does not require an unproved extension of arbitrary H-valued tuples
to automorphisms.

8. **Scope (AF8).** In the actual boundary-to-proper homology exact
sequence, integral splittings give the stated block matrix. Integral
boundary and proper blocks leave precisely the upper-right class
modulo integral Hom. Changing an integral splitting changes that class
by an integral map. The proof does not make that class vanish for a
Galois automorphism or identify the H-stabilizer with a discrete
surface automorphism group. These exact remaining maps are retained.

The proof audited here is elementary; no additional source theorem was
used in this audit, and no finite certificate was rerun. The source
scope observations about existing discrete automorphism theorems do
not enter the proof AF1–AF7.
