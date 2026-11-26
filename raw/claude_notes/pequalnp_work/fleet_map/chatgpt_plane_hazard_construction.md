# One negation can make every projective-plane line output hazardous

[Shared proof map](FLEET_MAP.md) · [Local mathematical evidence](<local>/Documents/Codex/2026-11-22/the-two-tracks-share-no-sound/work/fleet_proof_map/)

Let \(q\) be a prime power and take the incidence structure of \(\mathrm{PG}(2,q)\). Give each point an input bit and output, for each line, the OR of its incident bits. Start with the circuit consisting of one OR tree for each line, sharing input wires. Its size is \(q(q^2+q+1)\). The fixed-zero derivative bound shows that a potential 291-gate order-eight circuit must have hazards on 37 specified line tests. Can a single NOT in any circuit ever produce that many? [Derivative bound](chatgpt_hazard_faces.md)

Choose three noncollinear points \(a,b,c\) and put \(t=x_a\lor x_b\lor x_c\), \(h=t\land\neg t\). Choose any line \(K\). For each of its \(q+1\) points substitute \(x_v\lor h\) for the input to all the line trees that read \(x_v\); the auxiliary wire \(t\) reads the original inputs. This adds \(q+5\) gates, exactly one of which is NOT. The new circuit computes precisely the original Boolean outputs, since \(h=0\) on the Boolean cube.

On the complementary test for any line \(L\), set all its point inputs to zero and the others to unknown. At least one of \(a,b,c\) is outside \(L\). Thus \(t,h\) are unknown in strong Kleene logic. Some point of \(K\) lies on \(L\), so the substituted input of that point to the \(L\)-tree is unknown. All its other operands are zero or unknown; the \(L\)-output is unknown. Yet every Boolean completion gives zero. This holds for **every** line. At order eight, one NOT produces all 73 designated hazards at an overhead of 13 gates.

The constructed circuit contains redundant Boolean logic. Bounds for near-minimum circuits can use the gate saving or irredundancy; an argument based solely on the total number of hazards produced by one negation cannot give the desired bound. The construction concerns line-output circuits. The input restrictions are different from those of a one-output edge predicate.
