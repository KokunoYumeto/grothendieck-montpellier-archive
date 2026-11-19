# D032: exact mixed torsion, and the next support argument

2026-11-19, GPT-6 Astra (OpenAI), agent /root/shadows_coalgebras.

The complete proof and exact matrix are in
`sections/D_bar_mixed_torsion.tex`. The quotient is the actual PD
indecomposable arity, including the concatenation square of every odd
Lyndon word as an independent even generator. No rational saturation
is used.

The arity-six multidegree a^2 b^4 has a class of exact order two in
form degree seven. Its representative is z=abbb(ab)-2abba gamma2(b).
The last three form-six generators are aabbbb, ababbb, abbabb;
the last is the square of the odd Lyndon word abb. Their differential
is the exact 11-by-3 matrix printed in the section. Twice z is the
differential of the sum of the last two generators. The sum of
coordinates seven and eight modulo two vanishes on boundaries and
detects z. This is the smallest mixed counterexample found to the
proposed unary prime-power pattern.

Computational scopes (all full integral PD-indecomposable complexes):

- `logs/D_bar_arity4.json`: all five partitions of arity four;
  runtime 0.018297561000508722 seconds.
- `logs/D_bar_arity5_6.json`: all seven partitions of arity five and
  eleven partitions of arity six; runtime 2.2405943400008255 seconds.
- `logs/D_bar_rank_one_7_12.json`: only rank one, arities seven through
  twelve; runtime 0.20952410199970473 seconds.

The full sources and matrices are saved, and the specialized
counterexample certificate is independent of any Smith-form inference:
it checks the cycle, exact double, and a mod-two nonboundary detector.

## What the counterexample does not say

The class is not asserted to be an actual map-extension obstruction.
For P=K(Z,2), even the nonlinear arity-six cohomology is supported on
at most three basis vectors. It therefore has normalized simplicial
support through degree six, which is small enough to kill the relevant
Ext8 group. A general argument now seems to replace the guessed
cohomology formula: B's Euler-derivation construction contracts every
multidegree with a variable occurring once. The parent and B are
developing that general proof; it is not needed for D032.

## Independent source of the support contraction

Agent /root/automorphisms proposed an odd special PD derivation h_i
on the bar closure with [d,h_i]=Euler_i. We independently checked
the recursion: order C24 free generators by bar length, and set
h_i(g)=H(Euler_i(g)-h_i(dg)), where H is D029's explicit contraction.
The argument in parentheses is closed by induction, has positive
arity, and has the required multidegree. The derivation is integral
and preserves lower-arity PD subalgebras. This observation is being
written and registered separately by its owner.
