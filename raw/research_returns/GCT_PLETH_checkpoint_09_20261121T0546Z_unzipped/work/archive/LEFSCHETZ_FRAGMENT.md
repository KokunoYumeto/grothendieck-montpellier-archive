# A-016. Exact operators and a counterexample on cote16, scan038

The original Montpellier PDF is `public_scans/16.pdf` (21,774,525 bytes). The target is PDFpage38/sitepage37. The current run visually inspected PDFpages33,34,36,38, including a240-dpi crop of the target's final formulas. PDFpage33/site32 supplies the previously missing definitions; PDFpage36/site35 supplies the identification `(α)` and the pushforward description. Unrelated printed versos were recognized as such and are not used in the argument.

## Definitions recovered from the original

PDFp33 calls `X` a smooth connected projective variety of dimension `n`, polarized by a class in `H²(X)`, and `Y` a smooth hyperplane section. The map `φ:Y→X` is the immersion. Its `p_i^X` are the projections onto the primitive **bottom and top pieces**, indexed from0 through2n. They are not the projectors onto whole cohomological degrees. The actual operator convention is fixed by the source equations

`Λ_X L_X=1−Σ_(n≤i≤2n)p_i^X`,

`L_X Λ_X=1−Σ_(0≤i≤n)p_i^X`.

Thus `Λ` removes one `L` from a primitive string with coefficient one. PDFp34/site33 identifies restriction with truncation of each string and defines the extra middle piece `E^(n−1)`. PDFp36/site35 writes `(α)` and identifies `φ_*` with multiplication by `L_X` on the shared string pieces, zero on `E`.

The following explicit construction verifies the resulting operator statements and makes their maps unambiguous. It also supplies a precise reading of the source's decompositions. It does not assert algebraicity of any of these cohomological projectors or of `Λ`.

## The full explicit string model

For a positive integer `n`, choose finite-dimensional rational vector spaces `P_0,…,P_n,E`. Form

`V_X=⊕_(0≤i≤n) ⊕_(0≤j≤n−i) P_i[j]`,

`V_Y=(⊕_(0≤i≤n−1) ⊕_(0≤j≤n−1−i) P_i[j]) ⊕ E`.

Place `P_i[j]` in degree `i+2j`, and `E` in degree `n−1`. On each string define `L` to move `j` to `j+1`, and `Λ` to move `j` to `j−1`, both zero at the relevant endpoint; both operators kill `E`. Define `r:V_X→V_Y` to be the identity on the shared pieces and zero on the last term `P_i[n−i]` of every `X` string. Define `g:V_Y→V_X` by `g(P_i[j])=P_i[j+1]`, and `g(E)=0`.

The bottom projector `p_X^i`, `0≤i≤n`, projects onto `P_i[0]`. For `n<i≤2n`, the top projector `p_X^i` projects onto `P_(2n−i)[i−n]`. The analogous definitions for `Y` use dimension `n−1`; its middle projector also contains `E`. These are explicit direct-sum projectors. In this model `g r=L_X` and `r g=L_Y`, checked on every displayed summand, exactly as on PDFp36.

The kernel descriptions are

`ker L_Y=(⊕_(i=0)^(n−1) P_i[n−1−i])⊕E`,

`ker Λ_Y=(⊕_(i=0)^(n−1) P_i[0])⊕E`.

The operator `Λ_Y` is injective on all remaining shared string pieces. The first kernel is related to the high primitive pieces of `X` by the actual isomorphism

`rΛ_X : ⊕_(j=n+1)^(2n) im(p_X^j) → ⊕_(i=0)^(n−1) P_i[n−1−i]`.

Consequently a display identifying these two spaces must use this degree-minus-two map, rather than a literal equality of subspaces of one graded object.

## Corrected operator identities and their complete proof

Put `Q_X^top=Σ_(j=n+1)^(2n)p_X^j`, `Q_Y^top=Σ_(j=n−1)^(2n−2)p_Y^j`, `Q_X^bottom=Σ_(i=0)^(n−1)p_X^i`, and `Q_Y^bottom=Σ_(i=0)^(n−1)p_Y^i`. Then the concrete maps satisfy

`Λ_Y r=rΛ_X(1−Q_X^top)=(1−Q_Y^top)rΛ_X`,

`gΛ_Y=(1−Q_X^bottom)Λ_Xg=Λ_Xg(1−Q_Y^bottom)`.

For the first line, a nonfinal shared `X` term is lowered identically on both sides. A final `X` term is killed by `r`, while `rΛ_X` would send it to the final `Y` term; either displayed top projector removes exactly this contribution. The isolated middle `P_n[0]` is already killed by both lowering and restriction. This checks every summand of `V_X`.

For the second line, on a `Y` term with `j≥1`, both composites land in `P_i[j]⊂V_X`. On a `Y` bottom term, `gΛ_Y` is zero but `Λ_Xg` returns the corresponding `X` bottom; either bottom projector removes exactly this contribution. Every composite kills `E`. This checks every summand of `V_Y`.

The same basis check gives, for every nonnegative integer `m`,

`Λ_Y^m r=rΛ_X^m(1−Q_X^top)`.

It also gives the correctly typed projector identities

`rΛ_X p_X^j=p_Y^(j−2) rΛ_X` for `n+1≤j≤2n`,

`p_X^i Λ_Xg=Λ_Xg p_Y^i` for `0≤i≤n−1`.

The first carries the final term of an `X` string onto the final term of its truncated `Y` string. The second selects exactly its bottom term. These descriptions prove the identities on every summand and give the exact relation between the source's indices.

## The target's final chain fails on an actual hyperplane section

The supplied target's final chain uses `φ*` in positions whose source must be `H(Y)`; the original crop retains the problematic star placement. Even after the natural type repair replacing those two occurrences by `g=φ_*`, its additional equality

`p_X^i Λ_X φ_* = p_X^i φ_* Λ_Y`

is false. Take `X=P¹_C`, `Y` one point, `n=1`, `i=0`. Write `h` for the hyperplane class, so `H*(X,Q)=Q[h]/(h²)`, `φ_*(1)=h`, `Λ_X(h)=1`, and `p_X^0(1)=1`. Since `Y` has only degree-zero cohomology, `Λ_Y=0`. Thus the two displayed maps send `1` to `1` and `0` respectively. In the full string model the right side is always zero, while the left side identifies the selected bottom piece. This is a complete concrete-map counterexample, not only a typing objection.

Two other bounds in the supplied transcription can be settled in the same elementary models. The expression for `ker L_Y` must include the middle projector `p_Y^(n−1)`; the transcribed range starting at `n` fails already for the same `P¹/point` pair. The transcribed bound `0≤i≤n+1` for `ker Λ_Y` includes unwanted top pieces: for `X=P²`, `Y=P¹`, it includes `h∈H²(Y)`, whereas `Λ_Y(h)=1`. The exact correct range is `0≤i≤n−1`. The corresponding image readings remain distinguished from these mathematical repairs; no uncertain handwritten sign has been silently normalized.

The source's first corrected pullback line also prints `p_X` next to `id_Y`. The explicit model above proves its well-typed version with `p_Y`. These corrections and counterexamples close the operator-level questions in the supplied fragment. They do not supply the algebraicity assertions about Lefschetz projectors that the neighboring archive discussions treat separately.
