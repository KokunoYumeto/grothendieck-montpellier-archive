# Direct SNC model with nonzero triple periods: exact source audit

Status: unregistered research construction, NP.1–NP.8, submitted for independent review. This source record concerns geometry and a failure of a sufficient period condition. It asserts no nonzero ordinary Chow quotient and no survival of a K-theory class.

## Sources actually opened and read

1. Kollár, J. (2014). *Simple normal crossing varieties with prescribed dual complex*. Algebraic Geometry, 1(1), 57–68. https://doi.org/10.14231/AG-2014-004 . Full published primary: https://content.algebraicgeometry.nl/2014-1/2014-1-004.pdf . The current investigation freshly reopened and read Lemma 15, p. 63, Lemma 16 with its full local coordinate proof, pp. 63–64, and the proof of Theorem 2, p. 64. The arbitrary-field scope sentence on p. 59 was also inspected. The new construction independently writes both saturated small-resolution charts; no analytic, discrepancy, contraction, or gluing-class-preservation assertion is imported. Existing bibliography key: frKollarSNC2014.
2. The Stacks Project Authors. Lemma 37.50.3 (Tag 0B44), full statement and proof freshly opened/read: https://stacks.math.columbia.edu/tag/0B44 . A line bundle ample on a fibre of a proper morphism is relatively ample near that point; flatness is not required. Applied only to the proper map of exceptional surfaces and its point or projective-line fibres. New key: frSNCPeriodFibreAmple.
3. The Stacks Project Authors. Lemma 29.38.8 (Tag 0C4K), full statement and proof freshly opened/read: https://stacks.math.columbia.edu/tag/0C4K . Used for the sufficiently large weight M after the relative-ampleness check. Existing canonical key: frC3beStacksCompositeAmple.
4. The Stacks Project Authors. Lemma 33.47.3 (Tag 0FD6), full statement and proof freshly read during the C.3br audit immediately preceding this construction: https://stacks.math.columbia.edu/tag/0FD6 . Used for simultaneous nonempty smoothness/transversality opens of the very ample hyperplane and sextic systems. Existing key: D_StacksBertiniUniformHigher.

## Deliberately avoided source dependency

Kollár’s contraction proof cites Artin (1970), Corollary 6.12.a. Original-source attempts in this investigation produced metadata or inaccessible downloads, not the theorem text. No reading of that corollary is claimed. The present affine equation Q1 Q2 H − G6 provides an actual projective morphism to a local algebraic hypersurface, so no contraction theorem is needed.

## Independently supplied arguments

The explicit odd-characteristic and characteristic-two quadrics, the local-domain argument, the proper-local regularity argument, the exceptional-component allocation, the positive degrees 1,2,1 on the small curves, the dual complex, and the pair-incidence proof of nontorsion periods are proved in NP.1–NP.8. No external result claims nonvanishing of the ordinary quotient in this model.

## Finite algebra certificate

Program: code/check_SNC_nonzero_period_model.py. Output: output/SNC_nonzero_period_model_certificate.json and .out. Actual execution started 2026-11-19T18:11:45.705350+00:00 and ended 18:11:45.763918+00:00; runtime 0.05856967400177382 seconds. All 19 exact checks passed. They cover gradient determinants, affine elliptic equations, infinity-gradient independence, the two chart substitutions, node counts/allocation, small-curve degrees, and the finite dual-complex matrices. They do not verify generic Bertini, geometric normality, nontorsion, family equivalence, or Chow nonvanishing. Full code and complete JSON were inspected after execution.

## Separate Picard-span lemma NP.9

The new unregistered file C3_SNC_period_Picard_span_RESEARCH.tex proves only that the three elliptic period differences do not belong to the rational component-Picard restriction image. Its (2,2) Koszul resolution uses H1(P3,O(4))=H2(P3,O(2))=0. The exact primary Stacks Lemma30.8.1, Tag01XS, https://stacks.math.columbia.edu/tag/01XS, with its complete Cech monomial/homotopy proof was freshly reopened/read by18:19:36UTC. Canonical key frPrimitiveProjectiveCohomology is reused and its note updated. The Abel-fibre C^23 argument, free constant-S24 action in all characteristics, and transposition argument are supplied explicitly, not attributed to this cohomology source. Root read the entire NP.9 proof and returned mathematical PASS, retaining the exact limitation concerning arbitrary perfect-family corrections.

## Independent and visual receipts

Root read NP.1–NP.8, the complete19-case program/output and the full real_weil review; full proof/source PASS is retained at notes/ROOT_SNC_NONZERO_PERIOD_MODEL_REVIEW.md. Real_weil full independent PASS completed18:15:50UTC, saved at agents/real_weil/C3_SNC_nonzero_period_model_independent_REVIEW.md and matching events. The author read that complete receipt. Four-page standalone build completed18:14:53.115857UTC in4.04366693799966seconds, allfive commands returned0,124152bytes and no warnings. The author actually viewed allfour rendered pages by18:16:58UTC; no clipping or equation-layout defect observed. These build/visual checks concern NP.1–NP.8 only, not the separately typed NP.9 addition.

Final typographic C_12 edge-label repair rebuild: 2026-11-19T18:23:59.629441–18:24:04.250989UTC, runtime4.62148253700434seconds; allfive commands0, five pages144685bytes, no warnings. Current machine-readable metadata: output/SNC_nonzero_period_combined_build.json. The changed fourth page was rendered and actually inspected by18:24:15UTC, clean. The preceding allfive-page visual pass and the original four-page proof build are separately recorded above. No mathematical change was made.
