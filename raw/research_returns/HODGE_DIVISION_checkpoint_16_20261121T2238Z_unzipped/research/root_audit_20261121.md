# Root whole-proof checks, 2026-11-21

Checker: /root, GPT-6 Astra Pro; effort inherited and not externally exposed.
These are mathematical proof readings, not claims of formal verification.

## D-G34-01--07 and supplied HECKE_DIV SQ1--SQ7

Read the complete G34_PROOF_DRAFT.md, all seven statements and proofs.
Checked: group identification by containment plus order; faithful natural
representation and Chevalley--Weil multiplicities; cocycle action derivation;
nested/disjoint boundary intervals; positive Kummer powers and common sign;
weight-one limiting-MHS transversality; passage from limiting tangent minor
to actual interior rank; splitness from the image of geometric square-zero
monodromy; primitive exceptional local-system vanishing; full orthogonal
parity in Brauer induction; nonzero rational supplier embedding components;
U-invariant contraction and rational descent. No defect found.

Then read HECKE_DIV.tex SQ1--SQ7 in full. Checked the integral idempotent
Ge, polarization annihilator, integer supplier coefficient bound, orbit-sum
mass estimate, middle tensor contraction, full U invariant generators,
globally generated divisors and nef inequalities, mixed-degree projection,
and both directions of the Hermitian basis-change denominator calculation.
The old proof's geometric premises are now supplied by D-G34-01--06;
no Severn main theorem is used for the new conclusion. PASS.

## D-IM-05--07

Read all three complete proofs. Checked the nodal residue conditions,
ramified line-bundle/gluing conventions and the factor1/x, connectedness
of the nodal cyclic cover, negative-degree duals for base change,
equivariant smoothing, the eigenspace multiplication codifferential,
primitive-vector and point-push transitivity, and the map-lifting
obstruction H1(f*T_P1)=0. The resulting theorem gives maximal image ranks,
not the rank of every Nielsen class. PASS as stated. Arithmetic was
independently recomputed by the G34 agent; root does not count that as its
own separate computation.

## SF-CM01--03

Read the whole cm_transport.md. SF-CM01 finite-etale descent, invariant
Ext, naturality/injectivity of pullback and negative-Ext argument are sound.
SF-CM02 checks the entire even character using SL6 exterior invariants;
the a=b, (6,0), (0,6) alternatives include the top and constant terms.
The rational decomposition follows from its rational invariant spaces.
SF-CM03 is a valid conditional deduction from the explicitly named
Markman assertions: even d removes the gerbe problem, rational symplectic
density gives an existence choice of good CM Jacobian, and equality of
the elliptic CM field with the secant field permits balanced conjugation
in M6(K). This is no evaluated CM equation and no prescribed principal
polarization. PASS in precisely that conditional scope; the Markman
semiregularity theorem is not independently established by this check.
