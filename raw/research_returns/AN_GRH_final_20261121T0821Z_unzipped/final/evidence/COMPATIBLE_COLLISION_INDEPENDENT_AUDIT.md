# Complete independent reading: compatible collision classes

Date: 2026-11-21. Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Reviewed note: work/row_audit/COMPATIBLE_COLLISION_SCOPE.md.
SHA256: d76c0fb25e1ecb299cc9e949ef9aa4d16bbdd4a105d34548a1bc1bfb168c796d.
Outcome: PASS; no mathematical correction requested.

## Exact source reading

I read the complete recovered A1 claim A.31 and its proof directly in recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex, lines 1653–1700. The note correctly uses its covering implication and independent uniqueness proof, without invoking its last appeal to A.1 as a premise for the hypothetical collision analysis. The inherited geometric prime-to-p topology, the norm-one/Hilbert90 invariant-divisor degree argument, and uniqueness-driven compatibility have the stated scope.

## Whole-note mathematical check

All five sections were read in full. For a prime-to-p refinement, h_*h^*=[d] gives a section d^{-1}h^* on the actual rational p-primary groups. The two displayed summands are genuinely disjoint, so the exact order formula is m'=lcm(m,ord(b)); no arbitrary realizability of b by two points is inferred.

A rational principal divisor descends to a rational function by Hilbert90. Exact p-power point-difference order makes its function geometrically separable over the perfect finite field. The norm divisor gives N_h(f')=c f^{m'/m}. The example (z-1)/(z-zeta) has norm one and simple zero and pole, but is explicitly confined to the unrestricted norm inference: its ramification and same-image support prevent its being misrepresented as a pointed-etale-cover counterexample.

The constant-deck hypothesis supplies both complete rational fibres, hence at least 2n rational points. A degree-m function with a single rational point in each of its zero and pole fibres gives #D(k)<=(q-1)m+2. The resulting ceiling lower bound is correctly stated only in this constant-deck setup, and is not an upper bound on the Prym exponent.

For the coprime constant cyclic common refinement, connectedness follows from disjoint Galois extensions. The identity h_i^*h_{i*}=sum_{K_i} gamma kills the actual top conductor projector. Pullback is injective on p-primary groups because the refinement degree is prime to p. Consequently the actual faithful primitive component is invisible to both norm constraints. This does not prove an arbitrary invisible component can occur as a point difference; that exact limitation is retained.

The final three missing geometric inputs and the no-counterexample/no-universal-improvement conclusions follow from the preceding scope distinctions. No computation, new arithmetic example, numerical search, or formal proof-assistant verification was performed. This is a complete mathematical reading of the note and specified recovered source, not a separately constructed proof of the universal point-section theorem.
