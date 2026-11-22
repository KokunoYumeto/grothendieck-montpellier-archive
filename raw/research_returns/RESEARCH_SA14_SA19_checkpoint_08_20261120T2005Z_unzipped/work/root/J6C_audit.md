# Root audit of J6C

Date: 2026-11-20. Checker: GPT-6 Astra (OpenAI, ChatGPT Pro mode); effort inherited, not exposed.

Outcome: PASS, after reading the complete proof in `work/dgj/section_J6_cubic.tex` and independently checking every geometric and correspondence step. This is an audit of the literal middle fixed-part clause, not of the separate stable- and high-range assertions.

The characteristic-five cubic fourfold has empty projective gradient zero locus. A finite pencil member has empty singular locus when 1+t^3 is nonzero and a single singular point when it is zero. The member at infinity is the cone over a smooth cubic surface and has only its vertex singular. In P4, two hypersurface components meet in dimension at least two, so these singular-locus computations exclude reducibility and repeated components, over every geometric parameter. The regular-sequence axis ensures that the incidence pencil has exactly these scheme fibres.

For the generic smooth threefold, its cone axis has multiplicity three at the smooth vertex: in the chart x3=1 its local equation is v(1+a v^2)=-f3(u). Its strict transform is the smooth ruled resolution of the elliptic cone. The divisor class is H-3D, whose degree on a ruling fibre is 1-3=-2. On Pic0(E), the typed algebraic-correspondence composite q_* i^* i_* q^* is therefore multiplication by -2, with no identification of E and its dual hidden in the sign. The point-blowup adds a free integral exceptional summand to CH2 and adds nothing to algebraically trivial cycles; its pushforward and pullback are inverse on A2. The same composite consequently exists through Ab2(Y).

The outgoing correspondence is an actual Picard incidence test, so the nonzero elliptic image survives incidence equivalence as well. It is defined over k(t) from a constant elliptic curve and hence lies in the fixed trace part. Weak Lefschetz gives H3(X,Q_l)=0; the already-opened incidence dimension bound gives P_inc2(X)=0. Thus zero ambient image and nonzero fixed part contradict the literal clause.

The supplied two transcriptions of 44:4 were checked again: the pencil insertion requires geometrically integral fibres and states no smooth-axis condition. Taking Z=Z'=0 satisfies the cycle conditions inherited from Theorem 5. The example has a singular axis, so it is compatible with the proved smooth-axis replacement J6P.

The finite gradient checks support only the explicitly computable geometry; the fixed-part conclusion is proved by the correspondence calculation. BCE supplied a separate complete proof audit and an independently written chart certificate. No priority claim is made.
