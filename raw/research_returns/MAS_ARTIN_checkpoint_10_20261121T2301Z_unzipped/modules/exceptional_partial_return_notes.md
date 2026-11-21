# Exceptional-width return: proof and scope notes

## Result

MA-PR-006 gives a necessary and sufficient topological criterion for an actual continuous translation-equivariant return from the literal all-weight two-sided Hilbert quotient to the full smooth Meyer quotient. The test must satisfy the exact PR004 boundary-module vanishing conditions, and its attained minimum finite-block lifting costs must decrease faster than every power of the block height. Every continuous return is then nuclear of every positive order and has an actual continuous lift to E.

The finite costs are not an estimate silently imported from generic widths. They use the original M18 holomorphic quotient norms and the exact Gram matrix of the retained Mellin jets on the whole Hilbert quotient. The identities F_n = F_n P_n and R_n = R_n P_n are retained; P_n need not be orthogonal. The Gram matrix can equivalently be computed on H, since the retained jets annihilate the closed ideal and the Hilbert quotient map is a coisometry.

MA-PR-007 constructs width-dependent linear regularizers, chosen independently of the test, using the actual finite cost of one explicit linear module-solution selector in each block. Its tail damping is exp(-nu_n)/A_n, where A_n is allowed to grow arbitrarily fast. The regularizers converge to the identity in E uniformly on bounded test families. Every locally eligible test consequently has actual regularized returns at every width, with all-order nuclearity at each fixed regularization index.

A fixed ideal element b = varphi * varphi-dagger / integral(abs(varphi)^2), with varphi = T_a psi, has b(0)=1. Subtracting the error in the value at zero preserves all the already damped spectral jets and restores g(0). This uses the convolution ideal property and does not assume that the ideal is stable under the involution.

The actual quotient convolutions converge in S1. A common rank-one series gives trace cyclicity before any zero sum is evaluated, and the actual smooth correction traces converge. For a compact original test, the existing ambient cutoff theorem and Meyer geometry are applied only to that original test. The regularizers generally are not compact, and no new ambient S1 result for them is asserted.

MA-PR-008 supplies a precise conditional obstruction: a fully retained and a discarded zero in one full block force the minimum lifting cost to dominate the transform value divided by their separation, up to the full-block boundary clearance and the actual value-functional norm. The selected-height bound controls only the full-block boundary clearance. No arithmetic occurrence of an obstructing pair sequence is claimed.

## Complete author reading

The entire written module was read in three untruncated chunks after creation. The checks covered the local module maps and their free coefficients, finite minimum attainment, the Gram/coisometry identity, the dense-block argument needed for F_n = F_n P_n, common all-order nuclear rescaling, the exact centering in the Mellin multiplier, test-independent damping, the ideal value correction, actual trace pairings, the separate convergence statements, and the Cauchy lower bound. No mathematical defect was found.

Pure TeX alignment changes and one clarification that the ideal correction preserves the jets of D_N g, rather than the undamped jets of g, were made during author QA. Root and /root/pf26_audit subsequently completed full independent readings of all three proofs and passed them. PF also freshly reread the complete M18 proof and the relevant M19 nuclear-series proof. The explicit closed-eligibility corollary was checked by PF before its addition; the older PR scope now contains a historical forward reference.

## Exact inputs reread

- The complete MA-PR-001–005 module, including the sharp local module criterion.
- The complete MA-WP-001–003 module, especially actual projections and common-kernel removal, exact boundary jets, and the continuous E-to-S1 quotient map.
- The full supplied MT-M18 proof in sources/RETURN_GRH_NIGHT_checkpoint_07_20261121T0617Z/work/root/block_arithmetic_synthesis.tex, including M18.1–4, M18.7, and M18.10–13.
- MT-M19's nuclear-series proof through its finite trace calculation, in the same return's work/root/block_trace_hilbert.tex, including M19.3–5.
- The relevant actual half-line finite-block and trace-synthesis portions of MA-GW were reread to preserve the distinction from the two-sided quotient. No unsupported map from the smooth quotient to a finite-PW level was substituted.

The actual Meyer-sector isomorphisms and common-space signs are the previously checked MT-M22/MT-M24, MA-HM-002 and MA-MEY.15–16. The cote 1 scan locators 079–080 and 111–112 are inherited framework locators, not a newly claimed primary reading.

## Remaining scope

The unregularized all-test claim is not proved. Its exact remaining issue is the rapid-decay condition on the attained minimum costs. No uniform bound in the regularization index is claimed for the return maps, and no convergence of those maps in the full smooth quotient is inferred from quotient S1 convergence.

The actual off-diagonal maps of Meyer's original common-space projections retain their separate domain questions. Neither a boundary module section nor a smooth direct-sum splitting is asserted. The Grothendieck group is explicitly that of finite-length C[w]-modules, and its length relation does not split the truncated local extension.

No A, M, generic-edge condition, simplicity premise or new outside preprint is used. Arithmetic deficiency is not asserted absent or present.
