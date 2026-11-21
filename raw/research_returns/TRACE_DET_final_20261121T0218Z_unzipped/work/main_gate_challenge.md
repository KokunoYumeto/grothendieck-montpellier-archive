# Main determinant gate: challenge pass after DET-16–19

Date: 2026-11-21. GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_bridge_check.

## Outcome

The broad gate “no arithmetic specification of Xi weights / no actual source finite approximants” is now too strong. DET-16 supplies an exact arithmetic prescription from the actual scalar endpoint, under the stipulated RH, with full zero multiplicities recovered from Fourier atom masses. DET-15 realizes those repeated weights by actual finite source convolutions on one fixed Bessel space, with exact trace-norm tails. These constructed finite operators are finite spectral analogues of B, and their determinants converge to G. This affirmative statement must appear before the remaining historical qualification.

The independent direct-sign step remains distinct. In DET-16 the positive-type property of the arithmetic kernel is RH-equivalent; it is obtained using the stipulated RH, not from an independently matched sign theorem for the historical finite matrices. The actual finite determinant correspondence still needs a precise statement. This is a limit of the present evidence, not a claim that no such statement exists or can be proved.

DET-17 also means one should not say that no positive arithmetic weights are available. The prime weights are positive independently of RH and give the exact arithmetic trace -zeta'/zeta on the actual source model. Their ordinary determinant has a demonstrably different zero count. The missing property is the right Xi spectral identity together with an independent sign proof, not arithmeticity or positivity in isolation.

DET-18's weighted-character integrality analysis was in progress at this read and no saved proof was available. This pass does not presume its conclusion. An exact weighted-character scalar identity must retain its character coefficients, central blocks, completion constants and window quantifiers; it must not automatically be replaced by the single zeta kernel or an ordinary integer-multiplicity determinant.

## A concrete new route was pursued: DET-19

The source's natural one-parameter group gives a test stronger than merely requiring full representation invariance. I read the exact Decay and opn definitions and proved the complete result in `work/paper_bessel_boost.tex`, with source/proof notes and events in the adjacent `bessel_boost_obstruction` files. The full independent review reports PASS.

For the actual middle-coordinate Lorentz boost g_t, the source Euclidean norm is exp(|t|). Decay on the dense orbit span, followed by unitarity and approximation, makes every coefficient of sigma(g_t) vanish at infinity. The same holds for every trace-class trace coefficient. The arithmetic k has nonzero Cesaro atoms and cannot vanish at infinity; this last conclusion is unconditional, since boundedness itself would imply RH before the atom contradiction.

Consequently the arithmetic flow has no nonzero bounded intertwiner into this boost representation. The boost compact commutant is zero. These statements hold on H_sigma and its isometric closed Bessel image only; the exact coefficient covariance eta_u(xg)=eta_(sigma(g)u)(x) proves the action there without inventing unitarity on all ambient quotient L².

This rules out the particular proposed dictionary that keeps the source boost as the arithmetic translation flow, or takes a nonzero compact spectral function of its generator. It also rules out a fixed-boost trace-coefficient approximation with a trace-norm limit: the inequality

|Tr((T_N-T)V_t)| <= ||T_N-T||_1

would give uniform convergence in t to a function vanishing at infinity, whereas the arithmetic kernel does not. It does not rule out pointwise limits without this topology, changing models or flows, or the non-equivariant source embedding already constructed in DET-16. No evidence was found that the historical note claimed the ruled-out covariance.

## What exact missing statement would settle the direct-sign question?

There are two sufficient targets; demanding the stronger one as necessary would overstate the gate.

1. **A scalar sign certificate is enough for the RH consequence.** For t=log X, the exact candidate test is

   W_std(q_0+q_(-t)) = 2 k(0)+2 k(t).

   If a specified actual source determinant D_X has nonnegative sign and an explicit identity with a positive multiple of this quantity for all sufficiently large X, its sign gives

   G_zeta(X) >= b(X)-k(0) sqrt(X) = b(X)-2 lambda_1 sqrt(X).

   The already-proved global Landau lemma then gives RH, and B>=0 follows. A suitable quantified error would also suffice. This route does not require the source Gram matrix itself to be positive, or require that it be a compression of B. Balanced inertia can be a scalar sign mechanism. The present missing datum is which determinant/declaration, normalization and specialization supplies the displayed identity. For the actual weighted-character/power-window endpoint, its own correct specialization and pole/window argument must be retained instead of substituting this global zeta statement.

2. **A direct positive-kernel/operator correspondence is a stronger target.** One could prove that the source finite data yield all finite Gram forms

   sum_(i,j) conjugate(c_i)c_j k(t_j-t_i)

   with the exact arithmetic normalization, or positive finite operators whose specified trace-norm limit has determinant G. DET-16 then handles the arithmetic spectral reconstruction, including integer multiplicities. The source must supply the data/test map and actual equality or convergence; positivity of a single signed top determinant is not enough to assert positivity of every Gram form. DET-19 shows that this correspondence cannot additionally preserve the natural source boost on the fixed Bessel image.

An exact historical declaration and specialization would therefore be materially useful: the convention for W (linear zero functional or quadratic form), the meaning of S/test family, the finite matrix or determinant line and parameters, its relation to the scalar G_zeta/G_chi terms including b, and the sign/window passage. A dependency path alone cannot determine the meaning of a symbol which the note does not define. This is not a reason to re-run broad keyword searches and report absence as proof.

## Current wording for root to update

These are observations about the files at the time of this pass; no master or status file was edited by this agent.

| Location | Assessment / precise update |
| --- | --- |
| `work/paper_core.tex`, opening summary near line 34 | “Leaving the independent arithmetic choice ... unestablished” is stale as a global summary. State DET-16's scalar arithmetic reconstruction under RH, then retain independent sign and historical correspondence. |
| `work/paper_end.tex`, U-LIMIT first and third paragraphs | The remaining question is no longer whether any arithmetic weighting realizes Xi. Distinguish the now-proved RH-conditional construction from the independent sign/source-family identification. Add DET-17 and the scoped DET-19 flow obstruction. |
| `work/paper_weil_bridge.tex`, final sentence | “The arithmetic construction of the operator open” is overbroad after DET-16. Historical attribution/direct finite-sign reconstruction remains open in the present evidence. |
| `deliverables/QUESTIONS.tsv`, Q-DIRECT-BRIDGE | Replace the broad remaining independent arithmetic-weights gate with DET-16's affirmative result and the remaining independent positivity/historical matching. |
| `deliverables/QUESTIONS.tsv`, Q-PERIOD-FRAME-LIMIT and Q-BESSEL-XI | Their end clauses say independent arithmetic weighting / Xi weight derivation remains. They need the same qualification; finite-target restrictions themselves remain correct. |
| `deliverables/IMPLICATIONS.md`, paragraphs near lines 25 and 148 | Independent arithmetic weighting is no longer wholly missing. DET-16 and DET-17 distinguish arithmetic Xi weights under RH from independently positive prime weights with the wrong determinant. |
| `work/paper_bessel_projector.tex`, opening paragraph | Correct as a description of DET-15's original zero-input specialization, but cross-reference DET-16 so it is not read as the paper's final status. |
| `work/paper_core.tex`, B-01's “zero set is an input to both kernels” paragraph near line 93 | Correct for the two B-01 kernels. Preserve the scope; a cross-reference to the separate DET-16 arithmetic construction is enough. |
| DET-12's direct signed-kernel counterexample, DET-13's unspecified Xi measure, and DET-14's finite-target restriction | These remain valid in their exact scopes. They are not universal obstructions to every scalar sign certificate, positive arithmetic reconstruction, or model with changing target. |

## Read scope and limits

The current pass read complete `paper_bessel_weights.tex` (DET-15(d)/DET-17), complete `paper_end.tex`, complete `QUESTIONS.tsv`, the relevant full passages of `IMPLICATIONS.md` and `paper_core.tex`, complete `ALPOGE_remark.txt`, complete `step4_adaptive.md`, exact source definitions listed in the DET-19 note, and the DET-15/16 proof material cited above. The construction and global positivity implications of STEP6 and DET-11 were read completely in the preceding DET-16 author check. No Lean replay or new historical document discovery is claimed.
