# Independent whole-proof audit of SF-E831

**Outcome: PASS. No mathematical repair requested.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited/unexposed effort, HODGE_DIVISION. Actual record time: **2026-11-21 20:47:16 UTC**. Complete frozen draft: `agents/sixfolds/rm_vertexwise_coupling_gate_draft.md`, SHA-256 `870daf7349d51f72253507005b5048dbf6e3e9e3232d9cbc55175d85d50eed45`.

I read all 249 lines, the entire author certificate, and its output. I had just completed whole-proof audits of both dependencies, E829 and E830, including their rational product-isogeny, actual-entry support table, both actual boundary maps, and invariant normalized traces. This review therefore does not leave those new dependencies unchecked.

## Separate vertex spaces are valid

The passage from one common annihilator to a different `W_v` at each actual block is sound. For an A-block, every preceding diagonal coefficient is a sum of actual extension entries times reverse degree-one classes along its incident pairs. It lies in that block's own `Z_a`. Hence the A-diagonal direct sum injects, separately on every diagonal.

The next boundary contains only multiplication of each actual entry `e_ab` by the class chosen at its A-vertex. Since `W_a` is perpendicular to the sum of all incident support spaces, it kills every such entry. No equality of the choices at different vertices is needed.

For a selected B-block, its chosen `W_b` likewise kills all its incident actual entries in the lifting boundary. The A0 component still requires exactly the retained `Ext³(M_b,A0)=0` hypothesis. In the preceding B-boundary, each selected diagonal belongs to its own `Z_b`; the A0 term vanishes by the same Serre-duality argument. **Separate normalized trace maps modulo separate `Z_b`** detect the independent lifted identities. Thus these classes contribute to the kernel of the map whose image already contains the A-diagonal classes, and the dimensions add.

All of this uses the actual extension and actual preserved blocks. It does not infer a decomposition of the middle sheaf. The inherited translation/tensor action is trivial on `H²(O_X)`, so all the chosen vertex spaces are invariant; multiplicity identity matrices and normalized traces are fixed even in projective descriptions. Finite averaging and exact invariants give the claimed equivariant bound. No spectral-sequence degeneration, generic product rank, or higher-product vanishing is assumed.

## Coverage and weighted pair counts

I checked the exact conversion to the loss variables `ell_v=dim Z_v+dim rad(q|Z_v)`. The balanced-character bound gives `sum ell_v≥6N−18`. A vertex without nonzero actual exceptional support contributes six survivors, so at most three selected vertices can be uncovered. A component which is merely available in an Ext¹ space but is zero in the actual extension has `Z_ab=0` and supplies no coverage.

The inequality `ell_v≤2 dim Z_v≤2 sum_incident dim Z_ab` is valid for each vertex. Summing counts every pair once at its positive vertex, and a second time exactly when its negative vertex is selected. This gives the precise weighted inequality. The two coarse edge counts follow from the bounds on actual support dimension and the number of selected endpoints; no unselected negative vertex is silently counted twice.

For `N=32`, the exact integer consequences are 15 pairs in the maximal-rank elliptic allowance, or 44 pairs when each support dimension is at most one. These are necessary numerical capacities. The text correctly does not assert that such incidence data are realizable with the balanced character and the required unit vanishings. The original E826 line-to-line differences were indeed nondegenerate in the previously independently reconstructed cross-index certificate; this statement does not impose nondegeneracy on the auxiliary unit-resolution terms.

## Complete maximal-isotropic classification

Under `dim Z_v≤3`, zero survivors mean `dim Z_v=3` and a zero restricted wedge pairing. I checked the complete elementary classification supplied in the draft.

Every nonzero vector in such a space has wedge square zero, hence is decomposable in dimension four. Two independent decomposable two-vectors with zero mutual wedge have support planes meeting in a line; write them `a wedge b` and `a wedge c`, with `a,b,c` independent. If every support plane contains `a`, the whole three-space is `a wedge V`. Otherwise a third support plane meets the first two in distinct lines, lies in `H=span(a,b,c)`, and its two-vector has nonzero `b wedge c` coefficient. These three independent two-vectors therefore span exactly `Lambda² H`. Both displayed forms are conversely three-dimensional and totally isotropic.

This checks the universal classification, not just the two finite normal forms. The application is correctly confined to support span dimension at most three. For larger spans the full radical formula is retained. No rationality is asserted for arbitrary elliptic coefficient spans, and no irrational RM eigenspace is identified as a surface direction.

## Independent exact supplement

The independent `audit_vertexwise_coupling.py/.json` passed in **0.03343326699541649 seconds**. It imports no author helper or output. It reconstructs the wedge pairing and its annihilator ranks, both maximal-isotropic families under three invertible basis changes, the explicitly hypothetical six-vertex example, and all 97 exact integer budgets for `N=4,…,100`. It reproduces local survivors `0,0,6,6,6,6`, total 24, where the common-space calculation gives zero. That example remains abstract linear-algebra incidence data; no geometric object is claimed.

The author's initial SymPy-integer JSON serialization failure is retained in its own attempts record and was repaired only at serialization. It is not a failed mathematical bound. My independent exact run passed on its first execution.

There is no new external classification input. The source and supplied-compatibility statuses are exactly those verified in the immediately preceding E829/E830 reviews. In particular the balanced cap-rank consequence retains supplied S21 status and the already reviewed published BF scope. This is a necessary blockwise obstruction, with no constructed balanced semiregular seed or general sheaf classification claimed.
