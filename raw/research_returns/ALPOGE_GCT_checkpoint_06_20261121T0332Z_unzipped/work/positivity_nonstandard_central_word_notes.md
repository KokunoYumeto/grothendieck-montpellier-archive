# P-F52: actual nonstandard multiplication, not an assigned spectrum

## Result

The central word

`Z=(Q1-Q2)^2+S-f^2`

in the actual cubic nonstandard algebra acts on its conjugate blocks by `-c,-c'`, where `c` is the source coefficient used in P36/P39. The initial leading-coefficient argument was strengthened at root's request: the complete source relation and all coefficients of the source cell element factor as `r(t)=prod(t-g_i)` and `p1(t)=prod_(i!=1)(t-g_i)`. Therefore `(G-g1)u=r(G)Q1=0` directly, independently of the split-block assertion. The split decomposition now only labels the full simple-algebra summands. This does not use an arbitrary assignment to central idempotents.

The explicit descended map `a -> a u1 + tau(a) u2` sends `(1,x)` to `(u1+u2, x(u1-u2))`. The resulting multiplication matrix is exactly P39's `M0`, including sign, orientation and normalization. Four copies act on the eight-dimensional descended two-sided ideal. The two-dimensional subspace is only asserted to be stable under the central operator; it is not silently called a left ideal or simple module.

The actual tensor action is positive for every real `q>0`. An explicit positive product Gram form makes the source's sixteen-dimensional rescaled projection matrix self-adjoint, and `Z` is a square of a self-adjoint difference plus the strictly positive scalar

`3v^4+23v^3+57v^2+48v+16`, `v=q^2+q^-2-2>=0`.

The generic rational intertwiners need not remain injective at exceptional specialization. This is stated explicitly. The positivity of the unscaled actual operator still does not imply Laurent-coefficient positivity: its two-dimensional determinant has P39's negative coefficients. The source's normalization, other coefficients, full canonical-basis category and any theta/cohomological comparison remain further inputs.

## Source audit and quarantined discrepancy

Freshly read GCT VII printed pp. 6–10, 14–22 and 29–36, plus Figure 11 p.40. Visually inspected original printed pp.20,30,31,36,40. Source URL: https://arxiv.org/pdf/0709.0749 ; fresh full web ref `turn332053315view0`. The exact theorem inputs are Section7.1.1–2 pp18–20, Figure2 p31 and Figure7 p36; tensor positivity is checked directly from Figure1 p30. Local renders are `work/nonstandard_sources/gct_vii_20.png`, `gct_vii_30.png`, `gct_vii_31.png`, `gct_vii_36.png`, `gct_vii_40.png`.

The two-by-two generator matrices printed on p.20 are both upper triangular. Taken literally, they have a common invariant line and cannot be the asserted generic irreducible modules. This was confirmed in the actual page image, not inferred from a text-extraction error. The display is quarantined. No correction is silently made, and the proof never uses it. The central eigenvalue instead follows from the independent original relation and word coefficients; it agrees with the displayed `g1` scalar in Figure11.

## Actual checks

At approximately 03:03–03:04 UTC, read the entire written proof in two output chunks and reconstructed every step. Centrality follows directly from `Qi^2=fQi`; comparison of the `w4` coefficient gives the exact scalar. The descent and eight-dimensional ideal arguments were reconstructed independently, including the distinction between four-dimensional simple algebra summands and two-dimensional simple left modules. Every Gram block and the positive scalar expansion were rechecked.

Ran `work/verify_nonstandard_central_word.py` successfully. It transcribes the actual Figure1 matrix and checks, over the rational-function field, `Gram*P=P^t*Gram`, `P^2=fP`, the same properties for its complement, the scalar positivity identity, and the exact change of basis producing `M0`. This is a finite exact verification of a concrete remaining normalization risk, not a numerical sample.

At 03:07 UTC, read the complete factor-certificate addition P-F52f1–f3 and reran the extended exact verifier. Every one of the six relation coefficients and five cell coefficients was transcribed independently from the original source, then compared with the compact factor table. All pass, as does the complete six-coefficient identity `(t-g1)p1(t)=r(t)` modulo `x^2=D`. This closes the robustness issue raised by the quarantined p20 display; the eigenvector calculation is independent of that display and of the simple-block assertion.

Plethysm subsequently reported a completed independent entire-proof and exact-primary review: PASS, no correction. Its review independently reconstructed the central word, leading coefficient, descent, four-copy ideal, every Gram block and scalar positivity, and visually inspected the relevant original figures. The separate event is recorded by plethysm; this sentence reports that received result.

Plethysm also independently rechecked the complete factor-certificate extension against every original coefficient, ran the extended verifier, and reported PASS. Root reports a whole-proof/source read and successful independent execution of that verifier.

## Normalization corollary and final whole-proof reread

At root's request, appended a precise within-example normalization comparison. The alternative `H=(q+1+q^-1)^4` gives positive actual action and two positive symmetric nonincreasing determinant coefficient vectors, printed in full. It has Laurent width8, while the source's `F` has width32, so `F` cannot divide `H`. Thus those strengthened finite properties do not characterize the prescribed source normalization. No claim is made that `H` satisfies the source's additional lattice/canonical-basis conditions or normalizes other coefficients.

At03:10:32 UTC read the **entire revised file**, including both extensions, and reconstructed all proof steps. Ran the complete verifier again: source matrix, full relation and cell coefficients, all intertwiner identities, and the alternative full coefficient certificates PASS. Plethysm has been asked to independently check the short final corollary.

## Exact spectral-denominator provenance

At root's request appended P52q–s, identifying the actual additional source rule. Freshly read original VII p27 equations32–35 and p28; visually inspected the p27 render and the previously audited p28 normalization. The source chooses the product of the two Lagrange denominators for the positive R-eigenspaces, not the smallest matrix denominator. Multiplying the actual four eigenvalue differences gives

`f_p=-q^-33(q10-1)^2(q6+1)(q12+1)(q4+1)(q²+1)`.

Dividing by the convenient `f`, removing the source's explicit `-(q-1)^2/q` factor and centering by `q11` gives exactly

`F=q^-16(1+q+...+q9)^2(1+q²)(1+q12)`.

The proof accounts for every sign and exponent and treats q1 by the canceled Laurent identity. It proves coefficient positivity of this actual source factor directly. The exact verifier independently multiplies the six eigenvalue differences after q=r² and compares the full33-term F vector; PASS. This fixes provenance once the specified interpolation rule is supplied, while the H corollary shows positive action and Lefschetz determinant coefficients do not impose that rule. It does not supply a categorical integral form or all-coefficient multiplication compatibility.

## Latest peer and obstruction checks

Plethysm independently checked both final m-s normalization/provenance corollaries, freshly read originalVIIpp27-28, and executed the complete verifier PASS. Root also whole-read and visually checked those source pages and executed the verifier PASS. The root-authored t-x ordinary/virtual lambda and fixed-operator all-extension obstruction was independently whole-read and reconstructed by bridges at03:21:32 UTC; separate event recorded in this file family’s checks. No purity/semisimplicity assumption is needed for that obstruction.
