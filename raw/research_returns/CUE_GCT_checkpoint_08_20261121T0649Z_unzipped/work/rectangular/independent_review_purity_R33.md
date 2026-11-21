# Independent complete proof review: R-33

Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Actual review completed: 2026-11-21 06:33:32 UTC.

Reviewed file: `work/rectangular/r33_fragment.tex`, SHA256 `c74d38fab563468c4d9ccb8f9c2c56be952bc6e8bc1c1c109d69f1d64eb0abcf`.

**Outcome: PASS, complete proof read and rederived from the stated G21 exact-rank input.**

The exact differential dimension gives the claimed kernel dimension. On the all-nonzero-entry open, the constrained row-column diagonal variations have precisely the one-dimensional redundancy displayed, so their dimension matches that kernel. The independent-frame, full-Plucker-support and maximal-differential-rank conditions are nonempty opens in the same irreducible parameter space, and the additional nonzero-form condition is harmless.

Subtracting the scalar infinitesimal action on a degree-m form reduces a projective symmetry to an actual differential-kernel vector. Its coefficient variation comes from a diagonal matrix-unit operator preserving the pencil span. The induced exterior line is an eigenline. Full Plucker support makes every q-element sum of its weights equal. Since q is strictly less than the matrix-space dimension, exchanging two indices forces all individual weights equal. The zero-character constraint then forces that common weight to be zero in characteristic zero. Independence of the coefficient matrices makes the original infinitesimal symmetry scalar. The resulting projective Lie stabilizer is zero, hence the algebraic projective stabilizer is finite. Upper semicontinuity gives the stated generic property.

The enhanced pure-tensor stabilizer maps into this finite projective stabilizer, and the center of SL_q is finite, so the generic enhanced orbit has the full group dimension. The dominant invariant quotient has generic fiber meeting that dense open and containing its orbit. Generic fiber dimension therefore gives the asserted upper bound, without any closed-orbit, stability or scalar-period conclusion. The enhanced-cone dimension is the previously checked Segre-Veronese-Cartan dimension. The q<m squared restriction is used exactly at the Plucker exchange step and is retained.

No new primary source was opened and no numerical test was used. The exact G21 differential-rank theorem and the registered generic-fiber framework were treated as the stated already checked inputs.
