# Allen–Newton–Thorne II: exact applicability to the Tate triple

**Verdict:** the theorem allows three rank-one constituents in principle, but does not apply to the residual system `1 ⊕ χ^e ⊕ χ^(−e)` used here. The decisive failed hypothesis is pairwise distinction after restriction to the cyclotomic extension. There is also an individual-polarization failure in the present GD range. This is a theorem-scope audit, not a new proof of any automorphy or integral comparison theorem.

## Primary source and exact locators

Patrick B. Allen, James Newton, Jack A. Thorne, *Automorphy lifting for residually reducible l-adic Galois representations, II*, Compositio Mathematica 156 (2020), 2399–2422, DOI `10.1112/S0010437X20007484`. Publisher PDF downloaded verbatim as `allen_newton_thorne_2020.pdf`; layout text is `allen_newton_thorne_2020.txt`. The publisher PDF includes a cover page: printed page 2400 is PDF index 2.

Primary URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/91B814A109E34CC8DA2A5689BFA5CFA4/S0010437X20007484a.pdf/automorphy_lifting_for_residually_reducible_ladic_galois_representations_ii.pdf

Theorem 1.1 (printed 2399–2400; local text lines 56–104) equals Theorem 6.1 (2418–2419; lines 1262–1301). For continuous semisimple `ρ:G_F→GL_n(Qbar_l)`, its hypotheses are:

| Clause | Required condition |
|---|---|
| (i) | `ρ^c ≅ ρ^∨ ε^(1−n)` |
| (ii) | Finite ramification |
| (iii) | Ordinary of some dominant integral weight |
| (iv) | `ρbar^ss=⊕ρbar_i`; constituents absolutely irreducible, pairwise nonisomorphic, **each** satisfying `ρbar_i^c ≅ ρbar_i^∨ εbar^(1−n)` |
| (v) | Some prime-to-`l` place `v0` has `ρ|G_v0^ss=⊕_(i=1)^n ψ ε^(n−i)`, with `ψ` unramified |
| (vi) | An ordinary RACSDC `π` has the same residual semisimplification and is an unramified Steinberg twist at `v0` |
| (vii) | `F(ζ_l) ⊄ Fbar^(ker ad ρbar^ss)`; `F ⊄ F^+(ζ_l)`; constituents remain absolutely irreducible and pairwise distinct over `F(ζ_l)`; residual system primitive; residual image has no quotient of order `l` |
| (viii) | `l>3`, `l ∤ n` |

The conclusion is automorphy of `ρ`, not vanishing of a specified Selmer group. No Selmer-vanishing assumption occurs in that statement.

## Concrete obstruction for the actual triple

Write `χbar=εbar` on `G_E`. The normalized residual representation is

`rbar = 1 ⊕ χbar^e ⊕ χbar^(−e)`.

In the paper's rank-three normalization, take `ρbar=rbar⊗χbar^(−1)`. The three exponents are `−1`, `e−1`, and `−e−1`. Over `G_(E(ζ_l))`, **all three characters are trivial**. They therefore fail Theorem 6.1(vii), regardless of their original distinction. A common character twist changes them all to the same restricted character, so cannot repair the failure. Nor does passing to a larger CM field repair this cyclotomic-restriction distinction: the cyclotomic characters again agree on its cyclotomic kernel.

There is a second direct obstruction. Since the cyclotomic character is invariant under conjugation, the individual-polarization condition for exponent `a` becomes `χbar^(2a+2)=1`. It holds for the middle exponent `a=−1`; for either outer exponent it demands `χbar^(2e)=1`. In the actual auxiliary fields, `l` is prime to the discriminant, so `E∩Q(ζ_l)=Q`; hence `χbar|G_E` has order `l−1`. GD explicitly excludes `(l−1)|2e`. Thus clause (iv) fails for the two outer constituents, even though the **whole** triple has the required polarization by exchanging them. This distinction between polarization of the sum and of each summand is essential.

These are already decisive failures; we do not assert an independent obstruction from every other clause. In particular, existence of an ordinary automorphic source alone does not supply the specified Steinberg place or an integral Selmer comparison.

## Internal variants do not remove these hypotheses

The deformation/Hecke setup of §4.2 explicitly imposes the individual constituent condition (printed 2414–2415, local lines 964–1000). Theorem 5.1 retains this setup and the Schur condition after cyclotomic restriction (2416, lines 1064–1093). The finiteness Theorem 6.2 repeats the same constituent and cyclotomic conditions in (iv)–(v) (2420–2421, lines 1386–1420). Consequently neither its finite-Iwasawa-algebra conclusion nor §5 can be substituted as an applicable integral comparison here.

## Actual review scope

Read the full main statements, §3.1 setup, §3.2 setup, §4.2 hypotheses and Theorem 4.1 statement, Theorem 5.1 setup/statement, and the complete printed proofs of Theorems 6.1 and 6.2. The imported deformation and automorphy results invoked in those proofs were not independently re-proved or whole-proof audited in this task. No Lean/kernel execution. The elementary failure of (iv)/(vii) above was checked directly. No source files from other agents were changed.
