# Independent whole-proof review of N-010

Reviewer: `/root/plethysm_proof`; model: GPT-6 Astra Pro; effort setting: not exposed. Date: 2026-11-21.

**Result: PASS, conditional on the explicitly inherited dimension 114 and the stated Q(D)-form input.** This review read the entire `branches/nonstandard/rational_gt_rank4.tex` proof and the entire `rational_gt_rank4.py` script, replayed the script successfully, and checked the source definitions needed for the normalization statement. It does not identify the constructed matrix-unit basis with VIII's conjectural E(4).

## Actual ambient representations

The displayed A-matrices have entries in Q[D] and satisfy A_i²=DA_i, distant commutation, and A_i A_j A_i−DA_i=A_j A_i A_j−DA_j. With δ=v+v^{-1} and a=δv^{-1}, expansion of the braid relation for A_i−aI yields exactly the last identity, because a(a−D)=−D. The quadratic relation for T_i=A_i/δ−v^{-1}I follows directly. Thus these are representations of the full ordinary Hecke algebra after extending scalars to Q(v), not representations of an insufficient quadratic presentation.

Since C_i=C'_i−δI, the tensor formula 2A_i⊗B_i/D−A_i⊗I−I⊗B_i+DI is exactly the action of the actual P_i. Symmetric and alternating tensors are invariant because the tensor operator commutes with flip. The simultaneous D-eigenline is computed and checked exactly, and the complementary block is the legitimate quotient. The involution T_i↦−T_i^{-1} on one factor sends P_i to D−P_i, so the twisted five-dimensional model is also an actual ambient module. The two scalar characters come from the ordinary one-dimensional Hecke modules. No generic nonstandard simplicity is assumed at this stage.

The cell reconstruction is checked symbolically coefficient by coefficient, but the proof does not require a separate cell-module theorem: the explicit Hecke relations already establish representation validity. The displayed (31) and (22) labels have the expected transposition-character traces at v=1. The corrected C'-cell transpose convention is consistent with the actual matrices.

## Splitting and the rank certificate

The finite-field computation is a lower-bound certificate for the image of the actual algebra homomorphism. All specializations of denominators at D=7 are checked by inversion modulo 1000003; no rational denominator is silently discarded. The insertion procedure is ordinary exact echelon elimination of the flattened word images. It produces 114 independent vectors in the 114-dimensional product of matrix algebras. A nonzero specialized minor is a nonzero rational-function minor, so the generic image has full dimension. Combining this with the inherited upper bound dim=114 proves an isomorphism and hence absolute simplicity and distinctness of all nine modules.

The replay returned PASS, rank 114, and longest accepted word length nine. The queue's closure behavior is not being used to assert an integral presentation or integral generation bound. Only the independent word vectors are needed for the field-level isomorphism. The input dimension 114 and the Q(D)-form statement remain imported inputs; this review does not relabel their proofs as newly checked.

## Branching and GT lines

The polynomial identity and commutation checks for Z=(P_1−P_2)² make the Lagrange spectral projectors well-defined over Q(D). The three roots are distinct as rational functions. Their idempotence, sum, exact ranks and subsequent rank-one projectors are all replayed symbolically. The branch dimensions agree with every row of (N-31).

As an additional independent check, I verified E_0(P_1−P_2)=0 in all nine models. Thus the two zero-eigenvalue pieces are indeed the claimed scalar characters, not merely P_1 eigenspaces. I also verified E_j(P_1P_2P_1−(D²−z_j)P_1)=0 for j=1,2. These give the claimed parameters D and (D−2)² directly. The extra check receipt is `reviews/rational_gt_rank4_plethysm_additional.json`. The identity P_1Z=D²P_1−P_1P_2P_1 explains these parameters algebraically.

The nonzero projectors E_jP_1/D and E_j(I−P_1/D) are mutually complementary rank-one projectors. The selected columns are therefore well-defined rational vectors on the GT path lines. The script separately verifies that the transition matrix is invertible, that P_1 has the stated diagonal action, and that each of the three conjugated generators intertwines exactly. Matrix units can then be pulled back through the proved algebra isomorphism by rational linear algebra. This is a full GT matrix-unit construction over Q(D), without a claim about integral lattices.

## Constant normalization and the canonical gate

I read the relevant original source in `sources/LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex`: the coefficient rings near lines 495–510 and the complete GT/local-crystal/globalization construction near lines 1350–1550. They are rational coefficient rings, so every nonzero rational constant is a unit. Rational diagonal changes in module path vectors give corresponding constant changes of the algebra matrix units, with inverse changes on dual vectors. Such changes preserve the lattices, their bar transforms, and the type filtration. They scale the residue label and its fibre; the ambient coefficient degrees at infinity are unchanged. Therefore any unique minimum-degree lift transforms equivariantly by the same constant, and the optimization over the q-exponent has the same equivariance.

This is correctly stated as a normalization dependence, not a contradiction to the fixed-input minimum-degree conjectures. It does not prove the designated E(4) has coefficients in Q(D), nor any of its positivity or signed-factor assertions. Likewise the field-level split basis says nothing contradictory to the integral nonfreeness result N-009.

## Minor presentation requests

1. Add the checked identity E_0(P_1−P_2)=0, or cite the inherited rank-three semisimple classification explicitly at the point where E_0 is split into the two characters. The identity has now been independently checked in all nine models, so this is a proof-explication improvement rather than an unresolved gate.
2. The tag (N-24) appears already in the N-009 cardinality argument. Renumber the new displayed tags before compiling the combined nonstandard paper.

No mathematical gap was found in N-010 within its stated inherited-input scope.
