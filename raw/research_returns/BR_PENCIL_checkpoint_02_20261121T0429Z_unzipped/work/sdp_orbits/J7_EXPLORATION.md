# Seven-plane exploration: historical attempts and subsequent resolution

## Final verification 2026-11-21T03:54:07Z

P-15 is fully checked for the determinant S_A and both permanent S_A/S_B tensors. The self-contained exact-rational verifier passed all three cases; pencil independently replayed all three and read the full proof, and root read the full proof too. Earlier pending or unresolved notes below are historical. The final proof is `support9_sevenplanes.tex`; final checker and verification hashes are in `P15_HASHES.json`.

## Update 2026-11-21T03:51:58Z

The initial gates described below have since been closed for the determinant support9 tensor and both permanent support9 tensors by a complete degree210/120 torus extension calculation. The full result and proof are P-15 in `support9_sevenplanes.tex`; the standalone exact checker is `check_support9_sevenplanes.py`. Determinant and permanent-B standalone replays have passed independently; permanent-A standalone replay is pending at this update. The earlier unsuccessful approaches below are retained as a dated research record and are not the current gate.

The root computation leaves fourteen coordinate permanent seven-plane orbits below the desired lower bound14; support-factor Koszul flattenings subsequently settle three of them. The two support9 representatives are `[0,1,3,6,7,9,18]` and `[0,1,3,6,7,18,21]`. Both are seven-output restrictions of the9-output polynomial per3 tensor, equivalently row per3 tensor product row per3.

## Secondary substitution

`j7_secondary_substitution_probe.py` checks all coordinate support-factor residual k-planes for k=2,...,8 for those two representatives. None of the resulting uniform ordinary/Koszul bounds implies14. The output `j7_secondary_substitution_probe.json` records every residual subset and achieved ranks. This is only a failure of these tested certificates; arbitrary residual-subspace border ranks are not computed.

## Degree210/120 saturation

For a hypothetical border-rank13 decomposition, properness supplies an extension E of the9-dimensional contraction image U inside A7 tensor B9, with dim E=13. A torus-fixed extension quotient E/U has dimension4. The script `j7_weight_saturation.py` enumerates every possible support of up to four distinct weights whose total quotient capacities are at least4, saturates each support by all available vectors of those weights, and checks necessary prolongation nullities. The per-weight decomposition of the wedge maps reduces the computations to small exact finite-field ranks.

The first representative has33 quotient weights,46119 possible supports, and13762 unresolved saturated supports. The second has34 quotient weights,51985 possible supports, and11983 unresolved saturated supports. In both cases every support of size at most2 is excluded, and no unresolved saturated extension has dimension13. The large number of larger saturated extensions makes this basic saturation step insufficient. None of these files is a completed border-rank14 certificate.

A further line-increment exploration may strengthen the necessary conditions by treating the four-line supports directly. Any unfinished output remains exploratory.

## Earlier cyclic search

The numerical LP search `j7_cyclic_degenerate_search.py` used the earlier shape `[0,1,3,6,7,9,12]`. That shape does not occur in the root's final list of unresolved seven-plane orbits. Its96 candidate cyclic residue assignments yielded no LP-feasible degeneration, but this numerical search is neither a theorem nor a certified obstruction.

## Completed results unaffected

The proven and independently verified permanent five-plane obstruction R04, exact SDP certificate, orbit-supremum correction, Plucker norm statement, and main-substitution audit do not depend on these exploratory searches. The elementary propagation m_j(U)-j nondecreasing already gives exact m6=12 from m5=11 and the anchored complete2-by3 upper construction.
