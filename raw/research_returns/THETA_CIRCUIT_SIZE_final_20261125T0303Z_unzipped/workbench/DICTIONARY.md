# Boolean circuits, finite schemes, and the scope of the translation

The proved results concern Boolean circuits and finite graphs. There is an
exact elementary restatement using finite schemes over Z **with specified
Boolean operations and a labelled circuit diagram**. It does not produce an
intrinsic scheme, motive, K-theory or weight lower bound. The attached archive
provides no theorem linking these gate minima to the wider Grothendieck
programme, and no archive cote supporting such an implication is asserted.

## A precise translation over Z

Put B=Spec(Z[t]/(t²−t)). The ideals (t) and (t−1) are comaximal, so evaluation
at0 and1 identifies its coordinate ring with Z×Z. Thus B is the disjoint
union of two copies of Spec Z. Its n-fold product B^n has one component for
each Boolean n-tuple, and coordinate ring Z^(2^n).

Use three specified morphisms as the allowed operations:

- AND: B×B→B, with output coordinate xy.
- OR: B×B→B, with output coordinate x+y−xy.
- NOT: B→B, with output coordinate1−x.

Each displayed output is idempotent when its inputs are idempotent; alternatively
check it separately on the four (or two) components. The constant sections
are0 and1. Projections and repeated uses of a wire represent circuit wiring.
The designated edge function is the morphism B^n→B obtained by OR of xy over
the graph edges.

A legal straight-line program yields a labelled acyclic diagram of these
morphisms, with exactly one charged internal operation for each listed gate.
Interpret unavailable reads by the zero section at the moment of the read,
empty AND by one, empty OR by zero, and NOT by its specified first argument.
For a literal correspondence, the diagram must retain the complete ordered
indexed gate list, operand metadata (including ignored NOT operands), input
arity and output index. A bare acyclic graph with an unspecified topological
order would not be a bijection. With this full data retained, these diagrams
and the original circuit programs are the same presentations, with identical
gate counts. Charged unary identities and constant gates remain charged.
In particular, the geometric section1 is not a free wire or selectable
constant-one output: it must be produced by a legal charged gate when the
circuit needs it. An out-of-range selected output is zero, exactly as in
the original semantics.

Equality of their output morphisms is equivalent to equality of all Boolean
truth-table rows: the coordinate ring Z^(2^n) is determined by its components,
and a morphism to B has output0 or1 on each component. Hence the mathematical
circuit claims transport exactly to **these restricted diagrams**. This is a
proved translation of syntax and semantics, not a change of circuit basis.
Allowing arbitrary polynomial or scheme morphisms as a unit-cost operation
would invalidate the gate-count comparison.

## Restatements of the findings

| Claims | Restatement with the specified diagrams | Proof carrying the statement across |
|---|---|---|
| THETA-001–003,011 | The labelled twelve-input edge morphism admits an18-operation diagram and no diagram with at most17 charged operations. | Truth-table equality iff morphism equality, and the bijection above; the paper proves the circuit lower bound. |
| THETA-005–010,013–014,024 | Local normalization, one-bit terminal cuts, the residual-twin partition and the graph cover bound constrain those labelled diagrams. | Wiring is retained exactly; a one-bit factorization is a factorization through B; the paper proves the combinatorial restrictions. |
| THETA-012,021–023 | The theta morphism has minimum diagram size m+τ−1; at the deficient size the two-consumption condition would contradict the cover count. | The same finite graph and labelled diagram survive unchanged; no additional algebro-geometric theorem is invoked. |
| THETA-015–016 | The even-cycle morphism with two leaves has diagram size3k+1 for same-parity roots and3k+2 otherwise. | Fixing leaves to zero is pullback along the corresponding coordinate section; the diagram contraction argument bounds branches. |
| THETA-028–029 | The odd-cycle morphism with three separated roots at odd distances has diagram size3k+5, including17 for C9. | The same coordinate restriction and singleton-component arguments apply; the odd-cycle cover proof is in the paper. |
| THETA-004,017–020 | The finite matching/hazard checks and sampled search statements keep their stated finite or conditional scope. | Ordinary Boolean rows correspond to components. Strong-Kleene unknown values require extra combinatorial data and are not additional points of B. No unconditional geometric hazard theorem is inferred. |
| THETA-025–027 | The universal-proposal implication, conditional formal interface, and corrected normalization hypothesis retain their logical status. | A change of language cannot remove a hypothesis, certify an uncompiled file, or repair the rejected unnormalized carrier assertion. |

## Why this does not prove a statement about motives or weights

The graph of *any* such circuit diagram over its primary inputs is isomorphic
to B^n: eliminate internal coordinates successively using their defining
operation equations. Thus circuits of different sizes computing the same
function have the same input scheme and the same graph of the output map.
Their different costs lie in the chosen acyclic presentations, not in these
underlying schemes. An invariant of only the underlying abstract graph scheme cannot by this
translation alone distinguish circuits of different lengths. The labelled
output morphism together with the specified generators still determines the
truth table and hence its minimum circuit size; no claim to the contrary is
being made.

No result about lambda-rings, K-theory, motives, correspondences or weights is
proved here. A connection to those subjects would need an explicitly stated
invariant retaining the circuit restrictions and a theorem comparing that
invariant with the charged gate count. Neither is provided by the cited
archive. This is the precise remaining bridge, rather than an asserted analogy.

## Audit of the translation

A separate same-model targeted algebraic audit is recorded in
research/dictionary_audit.md. Its three precision corrections concerning
ordered syntax, charged constants, and the retained output morphism were
incorporated. The translation is THETA-030 in the statement table.
