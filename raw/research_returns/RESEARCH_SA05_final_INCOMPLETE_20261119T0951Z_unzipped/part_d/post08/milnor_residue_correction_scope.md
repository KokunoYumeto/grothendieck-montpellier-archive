# Divisible residues and the missing correction in degree three

19November2026. Part D's bounded independent check for Part B.

## Exact primary passages read

Colliot-Thélène and Schreieder, *Divisibility phenomena in motivic
Bloch–Ogus theory*, current retained author version2026: Theorem6.1,
Lemma6.2, diagram(6.4), and the complete Theorem6.1 proof, pp.27–29;
the complete AppendixB, including TheoremB.1, LemmaB.2 and the alternative
proof of Theorem1.1, pp.32–33. The primary source was already retrieved
and hashed by Part B. This check used its retained extracted primary
text, not a new PDF retrieval.

Schreieder, *Remarks on Milnor K-theory and Tate's conjecture for
divisors*, retained author version: complete Lemma4.1 proof, pp.11–12.
The use of the quotient of proper cohomology by coniveau in degrees1
and2 is essential in that proof; in the separately listed higher-degree
case, vanishing of finite-coefficient unramified cohomology is assumed.

## The distinction that survives the new theorem

Let C be a Gersten-type cochain complex, with degree-zero field Milnor
K-group C0 and the residue map d:C0→C1. The desired extension would
say that an integral alpha in C0 whose residue is infinitely l-divisible
already lies in every l^r C0. The supplied integral unramified theorem
starts with d alpha=0, which is a stronger hypothesis.

To divide d alpha by l^r and correct alpha, a chosen divided residue
must be the boundary of a degree-zero cochain, after accounting for
torsion and subsequent residues. This is a lifting question. It is not
the assertion that the image of integral H1(C) in its finite-coefficient
inverse limit is torsion. In particular, the latter can hold even when
the divisible l-primary torsion in H1 is nonzero.

Here is an exact elementary certificate showing that these two input
statements do not formally supply the desired lifting. Take

    C0 = Z,       C1 = Z[1/l],       d = inclusion,       C2 = 0.

Then H0(C)=0 and H1(C)=Z[1/l]/Z, the l-primary Prüfer group. Both
terms C0,C1 have zero, hence divisible, l-primary torsion. For every r,
reduction gives the complex

    C0/l^r = Z/l^r  →  C1/l^r = 0,

so H1(C/l^r)=0. The analogues of both the degree-zero and degree-one
integral-to-inverse-limit reduction maps in Theorem6.1 are therefore
zero, stronger than merely having torsion image. Nevertheless alpha=1
is not l-divisible in C0, while d alpha=1 is infinitely l-divisible in
C1.

The missing information is visible in the Bockstein sequence. Since
the terms are l-torsion-free, the exact sequence of complexes
0→C --l^r→ C→C/l^r→0 gives

    H0(C/l^r) ≅ H1(C)[l^r] ≅ Z/l^r.

The connecting class of1 modulo l^r is represented by1/l^r in
Z[1/l]/Z. These form a nonzero element of the Tate module
T_l H1(C) ≅ Z_l. By contrast, the l-adic completion of H1(C) is zero,
because that group is divisible. A reduction/completion assertion on
H1 cannot simply be substituted for a statement annihilating this
Tate-module obstruction.

This is an abstract complex, not a geometric Gersten complex. It does
not disprove the higher-degree residue-divisibility statement or rule
out an additional geometric weight argument. It establishes only that
the exact new reduction theorem and termwise torsion-divisibility
result, without an additional lifting or Tate-module argument, do not
justify the proposed extension of Lemma4.1. No B1 universal-gate
movement is claimed.

## Subsequent geometric resolution of the residue implication

The abstract distinction above remains valid, but Part B subsequently
supplied the additional geometric input that it explicitly leaves open.
Induction on Milnor degree, the ordinary generic continuous regulator,
the strictly negative refined weights of Proposition3.7 in diagonal
twist, and torsion-freeness prove the residue-divisibility assertion in
every degree n>=1. Part D read those exact primary proofs and the
complete integrated proposition and passed the argument. The detailed
actual audit is `b1_milnor_geometric_and_completion_audit.md` in this
directory. Thus this note is a failed inference from the inverse-limit
inputs alone, not a remaining gap in that now-proved geometric lemma.
The completed invariant-colimit B1 gate is still separate.
