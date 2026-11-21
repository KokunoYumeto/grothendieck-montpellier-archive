# Complete independent review of MO023

The complete 124-line proof in `polar_critical_line_obstruction.tex` was read and checked. It passes.

Every critical-line Mellin value is a continuous functional in the exact two-sided exponential and polynomial Hilbert norm for a>0. The original theta identity makes it vanish on the smooth ideal and hence its closure. Thus the argument needs only value constraints at known critical-line zeros, rather than a full-strip retention hypothesis.

I checked the exact residues inherited from MO020. The two Gaussian Mellin transforms are (1/2-z) Gamma_R(1/2+z) and (1/2+z) Gamma_R(1/2+z). They give the displayed numerator E_c, whose values at the two real endpoints are -c1 and -c0. Therefore E_c is nonzero for c nonzero, regardless of the source cutoff shape. Multiplication by the two endpoint factors is harmless at the critical-line points used in the proof.

The product G E_c is a nonzero entire function of finite exponential type, with only a linear polynomial factor. Jensen on a doubled disk bounds all its zeros by O(T). Conrey's known simple critical-line subset supplies at least c T log T distinct points; no multiplicity or general distinct-zero estimate is substituted without proof. This contradiction proves the required two-dimensional injectivity.

The outgoing formula is algebraic on the actual smooth source and uses its two Gaussian sections, so the smooth-column rank statement does not assume an unproved bounded extension. When the MO016 extension exists, the same finite quotient map has rank two and the orthogonal correction attains the minimum rank. The proof correctly leaves the full matrix and its prime-trace extension conditional.

## Exact external-source scope

The two original Conrey pages were actually viewed. Printed p.3 equations (8), (11) and (12) define the full count, simple critical-line count, and its liminf proportion. Printed p.4 Theorem 1 gives kappa-star at least 0.401. These imply the weaker eventual c T log T bound used here. This was a theorem-statement and counting-interface check, not a fresh audit of the complete mollifier proof. It is a known published partial zero-location theorem and is correctly distinguished from A/M and from an assertion that all zeros lie on the line.
