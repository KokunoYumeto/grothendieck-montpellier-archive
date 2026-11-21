# Independent whole-proof review: I-29

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T02:38:59Z.

Scope: complete reading and independent mathematical rederivation of `I29_two_ranks.tex`, including the local-ring coefficient-space assertion, the revised sharpness example for every active and passive dimension, the rank-preservation construction, and the interpolation count. I read the whole original version, then read and rederived the replacement section 2. This is a targeted independent agent proof review, not a formal certification or external peer review. No numerical matrices were needed for this argument; I read `check_I29.py` but did not rerun it or certify its reported finite outputs independently.

## Verdict: PASS

The promised internal interval ranks `{r,w}` are sufficient for the complete proof. In particular, no bounded count of singular factors, simultaneous diagonalization, or commutativity assumption is used. The conclusion has a polynomial number of interpolation pairs in the width, while its evaluated hitting-set cardinality remains exponential in that pair count, exactly as stated.

## Persistent core and stable segments

When the full constant product has rank `r`, a chosen active `r`-space is transported injectively through every prefix. A suffix of rank `r` has image exactly the terminal active space, while an invertible suffix has a `c`-dimensional inverse image of a chosen terminal complement. Thus every pullback complement has dimension `c=w-r`, complements the transported active space, and is preserved by the next constant factor. The constant blocks become `diag(I_r,Q_i)`. Since each factor's constant rank is either `r` or `w`, its passive block is exactly zero or invertible; this is the decisive use of the two-rank promise.

On a stable active-projection segment with invertible constants, constant transport makes coefficient spaces nested inside the fixed space `pi^(-1)(T)` of dimension `dim(T)+c`. If the initial kernel has dimension `k>0`, the initial cost is at most one and at most `c-k` strict dimension increases can occur; this gives cost at most `1+c-k <= c`. With zero initial kernel, there are at most `c` increases starting from cost zero. At a growth layer, multiplying by one local nonconstant coefficient increases support by at most that single variable position, regardless of its exponent or the dimension gained.

If a zero passive block occurs, choosing its last position is legitimate. The suffix beginning there has a unit `r`-minor, and all `(r+1)`-minors vanish because its first factor has rank `r`. Its upper-left block is invertible in the local ring, and its rows form the graph of `U^(-1)V`. Stability expresses the active projections of both `BP` and `sP` in the same basis `H`; the coefficient matrix for `BP` has identity constant term. The resulting identity `sP=eta A^(-1)BP` is exact. Taking coefficients gives one span inclusion, while the chosen rows of `B` already belong to the previous coefficient span and give the other. If the projected space is zero, the graph identity kills the output, as required.

At the restart, the constant rows of `BB_a` supply lifts of `T` at cost zero; all additional coefficient rows involve only the single variable at position `a`. A kernel basis consequently has cost at most one. The remaining passive blocks are invertible, so the preceding stable-segment bound applies with total cost at most `c`. Formal power-series inverses in the untruncated case cause no issue: each fixed coefficient is a finite sum of coefficients of `BP`. In the truncated case, all inverses exist because their constant terms are units.

## Actual support bound and sharpness

For a nonzero initial active projection, there are at most `r-1` projection-growth layers. The stated total `c+(r-1)(c+1)=rc+r-1` follows. If the initial row is purely passive, the first stable segment has at most `c-1` dimension-growth layers unless a zero passive block kills it. There can then be at most `r` active-growth layers, giving `(c-1)+r(c+1)=rc+w-1`.

The accounting concerns actual coefficient rows. Initial lifts at any restart are linear combinations of previously retained coefficient rows; propagation through constants keeps their supports, and a new local coefficient introduces only its own, distinct variable. The suffix replacement does not require retaining arbitrary rows with unbounded earlier support. Thus the proof establishes the displayed support-spanning equality, including in the product truncated ring.

The revised sharpness example works for every `r,c`. The initial `c-1` unipotent edges carry the starting passive coordinate to the last passive coordinate only through their complete product. Each reset has rank `r`, retains earlier active coordinates, kills all passive coordinates, and transfers only that last coefficient into a fresh active coordinate multiplied by its new variable. The following `c` unipotent edges return that coefficient through the passive chain. Earlier active coordinates do not participate, and the new active coordinate had no prior coefficient. Induction therefore gives precisely the product of all `h=rc+w-1` variables in the final last-passive coordinate.

An interval without resets has invertible factors and identity constant matrix. An interval with a reset has rank at most `r` from that factor and rank at least `r` from its constant product `P`. Thus all interval ranks agree with their constants and satisfy the promise. Every coefficient row of smaller support is annihilated by the last-passive coordinate functional, whereas the full-support row is not. This proves the claimed sharpness for every `r,c`, including the quadratic balanced case and the corank-one value `2(w-1)`. The qualification that this monomial survives one generic dense direction is correct and prevents an invalid generator lower-bound interpretation.

## Generator and scope

The common transcendental center preserves all full-rank intervals. Minimal local rank-`r` tests have invertible internal chunks under the promise. Their selected compound endpoints are nonzero at the common center, and the left compound row is decomposable, so the independently reviewed I-28 applies with `r(w-r)=rc` pairs, including both endpoints. A finite product of selected nonzero minors proves simultaneous preservation over one parameter field; previous full-rank minors survive by setting the added amplitudes to zero.

After this rank-preserving center, translation by independent residual variables gives the hypotheses of the coefficient-space lemma for the complete internal word. Contracting with the constant final column leaves some nonzero scalar monomial of support at most `h=rc+w-1`; otherwise that column would annihilate the full coefficient-row span. Another `h` fresh pairs detect it. Therefore the total is `K=2rc+w-1`, and the parameter-degree and interpolation count follow from I-21. The proof remains valid in arbitrary characteristic with its stated field-extension convention.

The restriction to one singular rank is explicit and essential to this proof: with several singular ranks, passive blocks need not be zero or invertible, and the last-zero replacement no longer follows. No claim that such a replacement is necessary for all possible dense generators is made.

As a useful specialization, `w=3,r=2` yields six pairs for the promised internal profile `{2,3}`. This is narrower than the arbitrary-width-three eight-pair theorem and does not replace its treatment of rank-one internal intervals.
