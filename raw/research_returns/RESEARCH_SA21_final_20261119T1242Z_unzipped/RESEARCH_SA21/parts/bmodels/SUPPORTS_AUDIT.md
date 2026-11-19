# Independent audit of the supports part

19 November 2026. GPT-6 Astra (OpenAI, ChatGPT Pro mode), bmodels.

Read parts/supports/supports.tex in full, prioritizing the root-requested statements. No files in the supports part were edited.

- SA21-A03: Pass. Basis-generation equivalence uses all closed sets, Zorn extension and no hidden finiteness.
- SA21-A04: Pass. Point-neighbourhood condition is exact; zero meet implies orthogonality, then the supplied lattice argument proves distributivity.
- SA21-A05: Data coherent; typesetting defect identified: a<x<b,qquad should have a backslash before qquad.
- SA21-A06: Pass. Nonisolated point singleton closures separated by an incident interval. Core-chain sufficiency and isolated-vertex top replacement handle arbitrary infinite and empty cases.
- SA21-A09: Pass. Finite endpoints form a chain; original interval endpoints are consecutive; incomparable traces on alternating flag are contiguous, disjoint traces give positional separation.
- SA21-A10: Pass. Rational-cut order is transitive; all possible point/interval symbols excluded from N(F); explicit complementary subflag witness valid.
- SA21-A16: Pass. Pointwise two-neighbourhood condition equivalent to all top-relative complements; nonempty-meet formula valid for arbitrary families; empty meet distinction correct.
- SA21-A17: Pass. Orthogonal pair law gives orthomodularity by applying to b-perp and a; zero cases trivial. Actual versus universal figure quantifier separated.
- SA21-A22: Pass. Closed-valued bond condition exactly preserves closure-generated joins; adjoint dagger and categorical full faithfulness check. Morphisms are relations, not ordinary maps.
- SA21-A23: Pass under explicit typed spatial target and Raff assumption. Nonzero orthogonal labels force unique carrier; lifting, antisymmetry, monotonicity verified. Does not prove raw set-label variant.

The audit concerns the written proofs under their explicit definitions; manuscript/literature source attribution remains the responsibility of the root source audit. A05 typo was reported to root. No unsupported extension from finite flags to infinite figures or from actual to universal spatial figures was found.

## SA21-A15 extension: connected interval scope and a divisible disconnected counterexample

Independent targeted audit, 19 November 2026: pass, with one literal wording correction sent to the root. In the sentence concerning points outside rational interval interiors, point must read rational point; the isolated point c is outside every such interior but is orthogonal to none.

For a comparability-connected poset with at least two elements, every point is nonisolated. The A06 criterion therefore becomes exactly totality. Empty and singleton cases satisfy both Booleanity and totality, so no degenerate exception is introduced. Point symbols are the lieux and their orthogonality is strict comparability.

For L=Q disjoint union {c}, all intervals have rational endpoints. The open-lieu sets are U(P_q)={P_q}, U(P_c)={P_c}, and U(I_ab)={P_q:a<q<b}. Density makes all interval sets nonempty, proving divisibility. Among rational points every unequal pair is orthogonal. Consequently cross orthogonality of two rational open-lieu sets is equivalent to disjointness of those sets. Two rational open intervals are disjoint exactly when b<=d or e<=a: if these inequalities both fail, max(a,d)<min(b,e) and density supplies a common rational point. This is precisely positional interval orthogonality. For a rational point and interval, disjointness is q<=a or b<=q, including either endpoint. Two point symbols give the remaining direct test.

For every pair involving P_c, symbol orthogonality is false. The open-lieu cross test is also false, because the other open-lieu set is nonempty and c has no orthogonal point. The self-pair P_c,P_c is included. Thus MagL2 holds for all pairs. The nonisolated core is Q, so A06 gives Booleanity, while P_c is nonorthogonal to every rational point. Its singleton support is the top, because its neighbourhood is empty. This verifies the counterexample within the genuine interval construction, with its full infinite scope, and identifies the loss of point separation. No finite enumeration is being used to justify this infinite example.
