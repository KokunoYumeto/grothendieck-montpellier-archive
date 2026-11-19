# Ordinary Milnor divisibility and completion: independent audit

Recorded 19 November 2026, after the actual integrated proof was read
at 09:20 UTC. This note distinguishes a proved geometric lemma from a
formal obstruction to a subsequent completion argument.

## Geometric lemma

The complete actual text of
`sections/b1_milnor_divisibility.tex`, including
`prop:B-Milnor-divisible-kernel`, passes the independent written audit.
The assertion about the kernel of the ordinary generic regulator holds
for degrees n at least zero. The separate assertion that infinitely
divisible divisorial residues force infinite divisibility requires n
at least one; degree zero would otherwise give an immediate exception.

The induction is on Milnor degree and applies simultaneously to every
finitely generated field over the algebraic closure of a finite field.
For a smooth projective model, vanishing of the ordinary generic
regulators of the residues permits one finite-open localization step:
only finitely many boundary divisors occur, and each zero generic
residue vanishes on an actual dense open of that divisor. Removing the
finitely many remaining codimension-two subsets then lifts the class
across every codimension-one point. There is no exchange of the
filtered open colimit with a coefficient inverse limit.

The refined unramified regulator has weights in
[-n, max(-n,-2)], strictly negative for n at least one. An ordinary
Milnor element has a finite Frobenius orbit. The resulting weight-zero
finite-orbit span must therefore vanish. Torsion-freeness of the
ordinary integral generic group gives integral vanishing. A smooth
projective alteration handles arbitrary residue fields; finite-extension
restriction followed by trace multiplies by the degree, which can be
cancelled in this torsion-free target. Prime-to-ell alteration degree
is not needed. The final residue assertion then follows from the proved
degree-(n-1) assertion and the same localization and weight argument.

The exact primary passages independently read were Colliot-Thélène--
Schreieder, definitions (2.7)--(2.8), p.11, and Proposition 3.7 with its
complete proof, p.16; Schreieder, Theorem 2.2 and Corollary 2.3 with
their complete proofs, pp.6--7, and Lemma 4.1 with its complete proof,
pp.11--12. The earlier audit also read the complete Theorem 6.1 proof,
Lemma 6.2 and diagram (6.4), pp.27--29, and Appendix B with its
alternative proof of Theorem 1.1, pp.32--33. Primary files and exact
URLs are retained by Part B. No fresh audit of all norm-residue theorem
foundations is claimed.

## Free quotient consequence

Let D_ell be the kernel of the ordinary regulator. The quotient
K_n^M(K)/D_ell is torsion-free. It injects under restriction to the
function field of any smooth projective alteration, because trace and
torsion-freeness make the regulator restriction injective. On a smooth
projective model the residue lemma embeds that quotient into the direct
sum of the corresponding degree-(n-1) quotients of divisor fields.
Induction from K_0^M=Z therefore makes it a countable free abelian group.
The sum is countable and each ordinary element has finite residue
support. Also D_ell is ell-divisible: if ell b=a lies in D_ell, then
ell rho(b)=0 implies rho(b)=0. This argument supplies neither saturation
of a particular permutation embedding nor an equivariant basis.

## Stronger completion diagnostic

Part D supplied the construction now fully written in Part B's
`b1_milnor_divisibility_attempt.md`, Section 7. Put
D=Z[1/3]/Z with F acting by four, and
N=direct sum over r>=1 of Z[C_(3^(r-1))], with F cycling each basis.
The map e_(r,j) to 4^j/3^r modulo Z is equivariant and surjective.
Its kernel M is a countable free subgroup of a direct sum of finite
permutation modules, and every element of M has finite F-orbit.

Nevertheless, reduction gives

    0 -> D[3^r] -> M/3^r M -> N/3^r N -> 0.

The transition on the left is multiplication by three and is
surjective. Inverse limits therefore give

    0 -> T_3 D -> Mhat_3 -> Nhat_3 -> 0.

The first term is Z_3 with F acting by four. Explicit compatible
representatives are lambda_r=3^r e_(r,0) modulo 3^r M. They have exact
order 3^r: divisibility of 3^s lambda_r by 3^r inside M forces
3^s e_(r,0) in M, which occurs precisely when s>=r. Compatibility and
the eigenrelation follow respectively from
3 e_(r+1,0)-e_(r,0) in M and F e_(r,0)-4 e_(r,0) in M.

Part B independently checked the infinite proof, wrote the complete
Section 7 and executed the supplementary finite-level certificate
`part_b/code/permutation_submodule_completion.py`. Part D subsequently
read the actual Section 7 and retained JSON output, but did not rerun
that script. No geometric Milnor identification is asserted. The
example shows exactly why freeness and a permutation-submodule
embedding do not by themselves exclude new completed eigenvalues.

Neither the geometric lemma nor this formal diagnostic closes the
universal B.1 invariant-colimit gate or is counted as qualifying review
movement.
