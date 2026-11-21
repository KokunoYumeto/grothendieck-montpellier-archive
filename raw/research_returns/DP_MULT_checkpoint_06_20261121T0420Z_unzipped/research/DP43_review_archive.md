# DP43: independent complete proof and integrated-version review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Events **ABA-CE44** (independent original complete proof) and **ABA-CE45** (complete integrated proof and preservation). The complete original memo was first read at **02:36:47 UTC**, challenged throughout, and reread at **02:40:24 UTC**. The integrated fragment was read in full during **02:39:58–02:40:45 UTC**. Review closed **02:40:45 UTC**. No main-paper edits.

## Outcome and exact versions

**PASS for both versions.** All mathematical gates in the original proof remain explicit in the integrated proof. The original memo is unchanged from the author's reported version. The entire integrated fragment occurs exactly once, byte-for-byte, in the current main paper.

| Scope | SHA-256 |
|---|---|
| Entire original memo, all §§1–8 | `e2eb37649b5dd23cbb30304722d259c0027265c1071a5f495d570d6d16ab8492` |
| Complete statement and proof, §§1–7 | `a2eb8c919ece70aed9ef5d948173c6669ad690206155db8410d58e4f47317608` |
| Entire integrated fragment | `ae55a48b5264529d8adeb4bb6888e20adaa734667a4fd8efdb8dc0673c779f34` |
| Complete integrated theorem and proof | `1465ce2640efa8e4d91d7d492a62267f485318bc2773337fea97b9be59caea9c` |

Frozen versions are `late_proof_snapshots/DP43_complete_checked.md` and `late_proof_snapshots/DP43_integrated_complete_checked.tex`; metadata is in `late_proof_snapshots/DP41_DP43_DP45_integrated_check_metadata.json`.

## 1. Periodic rounding and exact floor sum

I checked the weights at all cyclic positions, including the exponent-zero complementary contribution. The series `c_a=Σ_(u≥1) ε_(a+u)p^(−u)` has the stated orientation and produces `p^t c_i=b_i(t)+c_(i+t)` with an integer digit prefix. The coefficientwise DP40 factorial bound at `p^t` is precisely `p^t c_i−s`. Because the coefficient lattice is unramified and `−1<c_(i+t)−s<0`, its ceiling is the desired integer prefix, also for `p=2`.

Composition of the integral operator inclusions is valid coefficientwise. Interchanging the finite digit sums gives exactly the displayed periodic floor sum, not just an asymptotic estimate. The selected-index hypothesis is used when `u=h`, and was not silently extended to nonselected indices as a derivative assertion.

## 2. The normalized q-operator is genuinely primitive modulo p

The identity `E_i(q)=C_i=c_i(q−1)` is correct because `i` is selected. Thus `p^(−C_i)D_i^q` is an integral continuous operator. For `0<k<q`, the binomial valuation is `h−v_p(k)`. The floor-pair identity subtracts exactly one at positions beyond `v_p(k)`. There are at most `h−v_p(k)−1` such positions below `h`, so every Leibniz cross term retains at least one factor of `p` after the normalization.

This establishes the full derivation identity modulo `p`. Translation invariance and continuity survive the construction, and differentiating translations identifies an invariant derivation with its tangent vector. A single sharp coordinate value alone would have been insufficient; the proof correctly establishes the entire operator statement first.

## 3. Torus character and arbitrary unit arrows

After a finite unramified extension, the diagonal Teichmüller action commutes with every display arrow, including arbitrary Witt-unit coefficients: Frobenius sends the scalar at position `a` to the scalar at position `a+1`, and the unit coefficient commutes with both. The exact coordinate action induces the stated character of each normalized invariant derivative.

The `q`th power has the same character as the original direction. The `h` characters are distinct modulo `p`, including at `p=2`, so the reduced normalized operator lies in that one eigendirection. DP40's exact `q`th coordinate coefficient makes its scalar a unit. Defining that scalar by the coordinate value already over the original ring justifies descent and gives the recurrence with an extra factor of `p` in the error.

The error operator preserves all integral coefficient ideals. In the original memo it is explicitly noted to commute with the derivative; the integrated proof does not repeat that sentence, but the recurrence can be right-composed with `D_i^(n−q)`, which is sufficient for its displayed induction. In any event, commutation follows immediately because the error is the scalar linear combination of `D_i^q` and `D_i` defining it. This omission is not a gap.

## 4. Affine induction

For `n<q`, the base-digit error equals `Σ n_t c_(i+t)` and is at most `(p−1)Σ c_a=h−m`. The equality counts every complementary position once against all cyclic powers. In the recurrence, the first term exactly preserves the slope; the second gains `1−c_i>0`. Thus strong induction, integrality and upward rounding give the affine estimate for every order. Combining it with the independently established floor bound is valid.

## 5. Exact common witness and optimality

The selected-edge identity `p^(g_a)r_a−r_next(a)=1` gives `Σ(p^(g_a)−1)r_a=m`. For input direction `i`, torus equivariance forces the first possible nonzero degree in output coordinate `a` to be `N_a=p^[a−i]_h`. This is indeed the least positive solution of the character congruence; no lower degree is missed.

The reduced contracted inverse has exactly one path before completing a cycle that realizes this degree. Its coefficient is a product of nonzero unit-arrow residues, so the degree occurs with the stated exact valuation. The degree telescope across the final wrap gives `Σ(p^(g_a)−1)N_a=q−1`. Multiplying the leading terms of the coordinate powers yields a unique first product coefficient, hence no cancellation. Legendre's formula at `q−1` then subtracts precisely `h` and gives affine loss `h−m`.

Because `c_i(q−1)` is an integer, any strictly smaller real affine constant would give a false ceiling bound at this witness. The witness valuation is nonnegative, as is also forced by the integral derivative, so the extra maximum with zero does not hide that contradiction. The slope's sharp sequence is exactly the previously proved DP40 `q^r` sequence.

## Scope, sources and limits

This is a new theorem for the actual arbitrary-unit cyclic display family over the unramified lattice. It uses the already independently checked DP40 construction and coefficientwise contraction, whose source inputs are explicitly listed in the original memo. It does not appeal to an unproved assertion about all deformations with the same rational Newton polygon. No numerical enumeration, Lean execution, or machine proof was performed or claimed.

All primes are covered. Singleton and complementary-singleton types reproduce affine losses `h−1` and `1`. The floor sum and affine expression are separate valid lower bounds; the theorem does not claim an exact universal optimum at every order. Neither the local optimal constant nor the directional slopes determine a global theta cost or selected harmonic value without an additional geometric interface.
