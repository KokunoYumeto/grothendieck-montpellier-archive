# Programs named in the papers

The paper uses display names rather than local filenames. The paths and commands below are from the workbench root. All listed C verification programs use the Python 3 standard library. Their output, assertions where present, and saved certificates specify the exact check performed. They are finite checks, not substitutes for the general proofs. The programs in the B and A research directories are additionally named next to their theorem or certificate descriptions.

| Display name in Paper C | Entry point and command | Expected result |
|---|---|---|
| Replica coefficient verification | `python3 research/c_height_counting/verify_examples.py` | Prints the exact binary count T3 = 47362 and odd-prime gadget counts and congruences for p = 3, 5, 7. This entry point does not use assertions. The separate third-height program below gives 1002460. Independent replica method: `research/c_height_root/independent_replica_coefficients.py`. |
| Projective point-count precision | `python3 research/c_height_classical/point_count_precision_check.py` | Counts(15,85)and(15,89), exact coefficient and affine-cone checks. |
| Third-height inclusion–exclusion | `python3 research/c_height_root/height_three_inclusion_exclusion.py` | T3=1002460,T7=1382535756736336500,statusPASS. |
| Witness-degree matrix checks | `python3 research/c_witness_degree/matrix_checks.py` | All exact rational and finite-field rank checks pass. |
| Artin-rank checks | `python3 research/c_trace_rank/check_trace_rank.py` | Exact rational projector/rank/trace assertions pass; no complexity lower bound inferred from the computation alone. |
| Valuation disc calculations | `python3 research/c_arithmetic_root/div_disc_counts.py` | First example integrals(6,4,2); second multiplicity16 and leading shifted coefficient4406856960; statusPASS. |
| Odd affine families | `python3 research/c_theta/check_odd_affine.py` | Maximal-family counts1,15,315,11475 in genera1–4. |

Further independent arithmetic checks are recorded in `research/c_arithmetic_independent`, and finite-trace formula checks in `research/c_space_upper/check_trace.py`. Historical exploratory searches are labeled in their own reports. Running a program may rewrite its own reproducibility certificate; earlier returned ZIPs are immutable.
