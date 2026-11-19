# C.3ai: every low-dimensional ordinary restriction range

The full proof in `suspended_calabi_yau.tex` covers every pair (r\ge1), (r+2\le N\le2r+1). Set (d=2r-N+2\ge1) and (k=N-r-2\ge0). A Fermat Calabi–Yau (d)-fold is embedded in a Fermat hypersurface of dimension (d+2k) by adding (k) paired coordinate sets. Two distinct roots of (-1) define joins with complementary vertices. Their incidence resolutions give integral Chow correspondences with composite exactly the diagonal of the Calabi–Yau base.

The specified geometric generic point minus a specified algebraic point yields an ordinary algebraically trivial class. A hypothetical hyperplane relation spreads and norms to a correspondence equation. The proof retains both the constant correspondence and the proper-parameter-support correction explicitly. They kill the holomorphic top form. The remaining correspondence has codimension (r-1), so it sends that form into Hodge type ((d+k-1,k-1)), in degree two below the middle of the Fermat hypersurface. This is zero by weak Lefschetz, or by a negative Hodge index at (k=0). The transverse left inverse contradicts vanishing of the original incidence action. This proves the required non-torsion in the hyperplane quotient.

The regular ambient strict local ring and its principal Fermat equation are specified. Source Chow vanishing is integral by the freshly opened Skalit Corollary 6.4(i), author p. 27. The target survives by C.3e. The curve-family and incidence constructions preserve the fixed-product definition of ordinary algebraic equivalence.

The root and `/root/frobenius` both read and passed the complete typed proof. Frobenius independently reopened Skalit Corollary 6.4(i) and checked its precise hypotheses. The endpoints recover C.3ah and C.3r, but the entire interval is proved, not inferred from endpoint examples. No high-dimensional assertion is included in this fragment.

The exact certificate `code/check_suspended_calabi_yau.py` retains 210 range cases, twenty Fermat degrees, pair equations, complementary tangent determinants, cycle codimensions and Hodge shifts. Runtime: **0.10279798600095091 seconds**. Complete JSON and stdout are in `output/`. The finite checks do not establish the non-torsion result by extrapolation.

The standalone four-pass build in `output/C3ai_check.pdf` is clean after repairing prose and filename overflows. Runtime: **2.953216986999905 seconds**. All earlier and final logs are retained by `code/compile_suspended_calabi_yau.py`.
