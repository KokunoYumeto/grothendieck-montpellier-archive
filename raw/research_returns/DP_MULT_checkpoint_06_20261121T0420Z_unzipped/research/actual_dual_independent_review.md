# Independent whole-proof review: actual Honda dual models

Reviewer: `/root/formal_bound`, **GPT-6 Astra Pro**. Runtime reasoning effort is **not exposed**. Date: **2026-11-21 UTC**. The first whole read of the height-three mathematical proof was completed before the observed clock reading **01:15:44 UTC**; a fresh read of the saved general-height proof and the complete height-three remainder was made at **01:21–01:23 UTC**. Exact snapshot hashes were recorded at **01:22:38.723283 UTC** in `actual_dual_independent_review_metadata.json`. These are mathematical reading/rederivation events, not Lean compilation or machine formalization.

## Reviewed snapshots and verdict

| File | SHA-256 at capture | Verdict |
|---|---|---|
| `actual_dual_height3_asymptotics.md` | `44c38a5d3c9e868b67e5c9c416e198a29cf65321444d286ab32d6a390685ecd3` | PASS: all statements (A1)–(A22), including the actual-dual identification and optimal affine constants |
| `actual_dual_all_heights_DP32.md` | `f239e38a268218ea5909db06ef36483ab2fe3792144cce647d4a139bdbeeb325` | PASS: all-height actual-dual model, coefficientwise mixed bound, exact directional sequences, and qualified dimension-average comparison |

## ADIR-1: integral group and actual-dual identification

I checked the precise functional-equation matrices against the logarithm. Hazewinkel's Lemma 2.3 applies with power parameter `p`, coefficient Frobenius `id` on `Z_p`, and entries `1/p`; its congruence clause (2.8) is needed and correctly invoked for `[p] mod p=M`. Merely subtracting rational logarithms would not have justified that congruence.

The finite-free argument is complete. Modulo `p`, the specified monomial basis has exactly `p^h` elements and is a free basis for the monomial substitution. Both power-series rings are `p`-adically complete and separated, and the target has no `p`-torsion. Successive lifting gives a surjection from the finite free source module; reduction and repeated division by `p` proves injectivity. No topological Nakayama hypothesis is being silently substituted for the explicit proof.

The Frobenius/Verschiebung calculation is performed over `F_p`, where all Frobenius twists are canonically the same base and the coordinate Frobenius is the usual `p`-power map. `M^(h−1)=F^h` gives `V_G^h=p^(h−1)`. Multiplication by `F_G^h` and cancellation of `p^(h−1)` in BT homomorphisms is valid because multiplication by that power is an epimorphism of fppf sheaves. The consequence `F_G^h=p` makes the dual connected and one-dimensional, and gives the exact special-fibre `p`-series `T^(p^h)`. After the specified base change to `W(F_(p^h))`, the residue cardinality is exactly the required Lubin–Tate `q`; the uniqueness theorem therefore identifies the integral group, not merely its isogeny class. I checked that the primary theorem really requires this base change and that both drafts provide it.

## ADIR-2: scaling and sharp coefficients

The general weights satisfy `p^(e_i) r_prev−r_i=1` on every arrow, including the exceptional exponent-two arrow. The scaled coefficient of an `n`-step iterate has valuation

`1+p^(e_1)+…+p^(e_1+…+e_(n−1))−n`,

which is zero for the first arrow and positive for all later arrows. Thus the exact reduction is `Id+M`, and its inverse is the convergent formal geometric sum `Σ(−1)^n M^n`. It is legitimate in residue characteristic two as well. Every diagonal `q^r` coefficient is a nonzero sign, so no possible cancellation can remove the sharp coefficient. The output scaling factor is correctly included in both drafts.

For height three, I separately checked the off-diagonal factorial calculations in (A12), including `D_X^pY(0)=−(p−1)!`. The coefficientwise extension of the at-zero derivative estimate through integral translation is valid. These results concern arbitrary integral formal functions and do not identify a prescribed theta entry.

## ADIR-3: height-three affine recurrence

I rederived all three translation identities (A13) by extracting precisely the required source monomials. Every coefficient operator is integral and commutes with the others, justifying the binomial expansion and the iteration of divisibility. The units `a,b` have the asserted valuations.

For the `X` recurrence, all interior binomial terms and the endpoint `j=p^2` have valuation at least `p+1`; the displayed split according to `j mod p` is correct, including `p=2`. For the `Y` recurrence, both interior and final terms have the required valuation. The induction uses only the already-proved coefficientwise integrality and `c<1`. The integer ceiling is justified over the stated unramified coefficient ring; the stronger operator divisibility persists under integral base change.

The monomial in (A20) has a unique contribution at its lowest degree on either logarithmic axis. Its factorial valuations are exactly those claimed, so affine constant `1` is attained in both directions. A larger asymptotic slope is separately excluded by (A2).

## ADIR-4: scope and further deduction

Both drafts correctly distinguish an actual Cartier-dual formal group from a normalized geometric Poincaré/theta kernel. The dimension-average comparison is explicitly conditional on equal weighting and does not assert a geometric cost theorem. No correction to the reviewed mathematical blocks was required.

The same operator method extends the constant-one affine bound to every height. That further result is developed independently in `actual_dual_general_affine.md`; it is not part of the snapshots reviewed above and should receive its own check record.
