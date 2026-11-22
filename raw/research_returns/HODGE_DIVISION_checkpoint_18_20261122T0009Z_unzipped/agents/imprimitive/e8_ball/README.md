# Compact E8 analytic dominance certificate

This directory contains the mathematical inputs and reviewed verification code for D-E8R-01–06 in ../e8_period_section.tex. It certifies a smooth point with period rank nine for an actual connected μ4W(E8) cover, and hence dominance onto its nonsplit Gaussian Weil-sixfold component.

It does not identify that component with the separate doubled-pair tuple in ../e8_tuple_section.tex. It also does not construct algebraic detecting cycles or bound their degree.

## Provenance

The candidate center, fixed gauge and three target matrices originate in Benjamin Severn's unrefereed qi-m3-certificates-v1.0 deposit, Zenodo record 23549514. They are retained as compact mathematical input, not treated as proof of existence or dominance.

cert_lib.py is the source implementation, read and audited in this run, with an explicit exact-endpoint assertion added. verify_M.py and verify_L.py are reviewed adaptations: missing continuation dependencies were removed, the saved gauge is read directly from JSON, exact dyadic centers are asserted, and the final interval outputs are recomputed. check_group_and_paths.py was newly and independently written.

The full third-party archive is not required and should not be included in the final deliverable. PROVENANCE.json and MANIFEST.json retain the source and hashes.

## Reproduction

Run from this directory with Python, python-flint 0.9.0, NumPy, SciPy and SymPy available:

~~~sh
python check_group_and_paths.py
python e8_path_tube_certificate.py
python verify_M.py
python verify_L.py
~~~

The third command takes about three minutes in the present environment; the others take seconds. The code uses 256-bit Arb complex balls for the certification. Approximate linear algebra selects preconditioners and pivots; success is determined by interval inequalities and a determinant enclosure excluding zero.

The fresh outputs from this run are:

- group_and_path_check.json: exact target-group generation, local determinant data, all allowed rational eight-dimensional eigenvalue orders, winding paths and endpoint checks;
- e8_path_tube_certificate_output.json: the independent exact rational tube comparison between the actual rounded adaptive paths and the intended polygon edges;
- certM_rerun_g.json: contraction, omitted-equation pivots, rigorously isolated infinity exponents and input hashes;
- certL_rerun_g.json: the final 9×9 codifferential determinant enclosure;
- verify_M_final.log and verify_L_final.log: final executed logs.

The final M verification gave η≈1.05281185×10⁻³⁵, radius ρ≈1.05281185×10⁻³⁴ and contraction bound κ≈0.00558986. All side pivots were nonzero.

The final L determinant enclosure is approximately
\[
(0.10557441259506563\pm6.51\cdot10^{-18})
+i(-0.04409991368479836\pm3.88\cdot10^{-18}),
\]
with certified absolute lower bound greater than 0.11441485472524.

The theorem proof explains the Taylor-tail bound, finite-dimensional contraction inequalities, exact finite-monodromy target, resonant local-frame normalization, identification of the actual Hodge eigenspaces, and the geometric period codifferential. An interval containing zero for a redundant equation is only a consistency check; exact redundancy is proved geometrically.

## Review status

The author of this reconstruction, /root/imprimitive (GPT-6 Astra Pro; effort inherited/not externally exposed), read the full source programs and reconstructed all mathematical error bounds. The parent /root reported a whole-proof and whole-program mathematical audit PASS, independent group/path checks, and fresh M/L reruns. The peer /root/sixfolds independently read the whole proof and every line of the four programs; his isolated fresh M run passed in about 177.9 seconds and L gave an absolute determinant lower bound greater than 0.11441485472524891. He also independently authored the tube certificate: every adaptive vertex is within 10^-12 of its intended edge and every intended edge is more than 1/10 from every pole. This closes the actual-path homotopy check. His full report is ../../sixfolds/E8_PERIOD_PEER_AUDIT.md relative to this directory.

This is an exact finite interval certificate with a written mathematical proof, not a proof-assistant formalization or a newly authored interval arithmetic library.
