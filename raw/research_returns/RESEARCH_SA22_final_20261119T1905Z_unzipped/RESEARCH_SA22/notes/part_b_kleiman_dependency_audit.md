# Independent scope audit of the algebraic Lefschetz input

19 November 2026, 15:27–15:34 UTC. Reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode, agent `part_b_cycles`.

## Outcome

The dependency used in `thm:B1b-abelian` and `prop:B1b-criterion` is valid. The opened original Kleiman1968 theorem proves the algebraicity of the Lefschetz operators for abelian varieties in arbitrary ground-field characteristic. Its standing convention is an **algebraically closed ground field**, which must be retained when citing it. The geometric use in the manuscript is legitimate: numerical triviality of a fixed cycle survives extension by `lem:B-basechange-num`, and the finitely many auxiliary cycles can be spread after enlarging the field of definition. The complete finite-field theorem is applied after every necessary finite extension, not falsely ascended from one finite base field without an argument.

The main paper now states these scope points in `sections/part_b.tex`, lines220–233 at this audit revision. No theorem status or statement count changes. This is a substantive dependency check and a clarification, not a new source-gate closure or a claimed independent verification of Broe's entire preprint.

## Original passages actually inspected

The original scan is `sources/kleiman1968.pdf`, *Algebraic cycles and the Weil conjectures*, in *Dix exposés sur la cohomologie des schémas* (1968), pp.359–386. Its opened public scholarly copy is:

https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf

The audit reread the original field conventions on printedp359; Theorem2A9, especially(3),(5), onp376; Theorem2A11 and its proof onp377; and Lemma2A12 with its proof continuing onp378. All four corresponding images were actually viewed:

- `qa/part_b_kleiman1968_audit_359.png`
- `qa/part_b_kleiman1968_audit_376.png`
- `qa/part_b_kleiman1968_audit_377.png`
- `qa/part_b_kleiman1968_audit_378.png`

The source's earlier formal steps were also reread in the full original extraction: Propositions2.1–2.3, pp.369–370; Proposition2.7, p.370; Theorem2.9, p.371; and the operator formulas in§1.4, pp.367–368. The separately opened Kleiman1994 Proposition4-3(2)(c), printedp16, agrees and refers back to the1968 appendix.

Onp359 the **ground field** is algebraically closed without a characteristic-zero restriction. The **coefficient field of the Weil cohomology** has characteristic zero. These two conditions must not be conflated. In particular, the theorem applies to geometric rational ℓ-adic cohomology when the ground field has positive characteristic different fromℓ.

## Why the original algebraic construction works in positive characteristic

Let A have dimensiong over an algebraically closed field. Theorem2A11 first separates the Künneth components of an algebraic class on A×Y. Multiplication by an integer m on A acts on H1 as multiplication bym, and on Hp as multiplication bym^p. For a class of fixed total degree, finitely many distinct integersm give a Vandermonde system. Its inverse has rational coefficients, so each Künneth component is a rational combination of pullbacks of the original cycle class. All these classes are algebraic.

This step does not require the integer multiplication maps to be étale. The inverse Vandermonde coefficients lie inQ, and the cohomology coefficient field has characteristic zero even when the ground field has characteristicp. Thus choosing integers whose differences are divisible byp introduces no invalid division in the coefficient field.

The isogeny/divisor construction in Theorem2A9 supplies an algebraic isomorphism from H^(2g−1)(A) to H1(A). After extracting the divisor's(1,1)Künneth component, Lemma2A12 identifies the exponential of that class as a map from the Pontryagin algebra to the cup-product algebra. Both are exterior algebras generated in their respective degree-one positions; hence its degree-i component gives an algebraic isomorphism

ν_i:H^(2g−i)(A)→H^i(A).

The rational factors1/i! cause no characteristic problem for the same reason. A prioriν_i need not be the inverse of the particular chosen Lefschetz isomorphism. The source explicitly supplies that missing step: the Künneth projectors are algebraic, so Proposition2.7 gives rational coefficients for the characteristic polynomial of the algebraic automorphism

u=ν_i∘L^(g−i):H^i(A)→H^i(A).

Its nonzero constant term and Cayley–Hamilton expressu^−1 as a rational polynomial inu. Thereforeu^−1∘ν_i is an algebraic correspondence inducing exactly(L^(g−i))^−1. This is Theorem2.9, and it is the step used in the proof of Theorem2A11. Merely asserting that some algebraic isomorphism exists would have omitted this necessary argument; the opened original contains it.

The field twists were suppressed by Kleiman's explicit convention onp359. For the fourfold map actually needed below, the correctly twisted statement is

L²:H²(A,Q_ℓ(1))→H⁶(A,Q_ℓ(3)),

with inverse induced by a rational codimension-two correspondence on A×A. Its domain, target and cycle codimension agree: a codimension-r correspondence on a g-fold shifts cohomological degree by2(r−g) and twist byr−g, hereg=4,r=2.

## Optional explicit descent of the needed operator to an arbitrary field

The manuscript can work geometrically and does not need this stronger packaging. Nevertheless, the required inverse can also be represented by a rational correspondence over the original fieldk, which verifies that no hidden algebraic-closure obstruction is being overlooked.

Fix the ample classh overk and let A/k be an abelian fourfold. Over an algebraic closure, choose a cycleΓ inCH²(A_bar×A_bar)_Q inducing the inverse ofL² onH⁶(3). Its finite defining data descend to a finite extensionK/k. Let

π:(A×A)_K→A×A

be the finite flat projection of degreed=[K:k], and putΓ_k=d^−1π_*Γ_K. After extending back to an algebraic closure, flat base change for cycles identifiesπ_*Γ_K with the sum of the conjugate cycles, counted with the inseparable multiplicity. IfK/k has separable degrees and inseparable degreee, this is e times the sum over thes embeddings of its maximal separable subextension, andd=es.

Every conjugate induces the same map onH⁶(3):L² is defined overk, is Galois-equivariant with the displayed twists, and its inverse is unique. Purely inseparable extension changes no geometric étale cohomology; its contribution to the cycle push–pull is the multiplicitye. Consequently the action ofd^−1π_*Γ_K is exactly(L²)^−1. Division byd is permitted with rational coefficients, including whenp dividesd. No claim thatΓ itself is unique in the Chow group is used; only the induced inverse on the specified cohomology group is unique.

## Full algebraic decomposition in degree four

This checks the exact use of the operator in the manuscript. Letα be the rational homological class of a codimension-two cycle on the fourfold, let h be the ample divisor class, and write∫ for the degree/trace onH⁸(4). Set

c=(∫αh²)/(∫h⁴),

α'=α−ch²,

β=(L²)^−1(Lα'),

γ=α'−Lβ.

The coefficientc is rational because its numerator and denominator are intersection numbers, and its denominator is the positive degree ofh⁴. The inverse correspondence acts on the cycleh·α', soβ is an algebraic divisor class. Henceγ is also algebraic. The construction is defined overk if the normalized transfer above is used, and geometrically suffices for the manuscript.

Since∫L²α'=0 andH⁸(4) has one-dimensional trace, L²α'=0. Therefore

L³β=L(L²β)=L²α'=0,

soβ belongs to the primitive part ofH²(1). AlsoLγ=Lα'−L²β=0, soγ belongs to the primitive part ofH⁴(2). Thus

α=ch²+Lβ+γ

is an algebraic Lefschetz decomposition. It is unique: pairing withh² recoversc; applyingL then recoversβ by injectivity ofL²; finallyγ is determined. Its three summands are orthogonal for the middle intersection pairing, becauseL³β=0 andLγ=0. This proves exactly the algebraic decomposition required by `prop:B1b-criterion`.

This argument supplies algebraicity and orthogonality. It does **not** replace the separate primitive positivity input in positive characteristic, and it does not convert positivity on numerical classes into definiteness on homological classes. The manuscript's Broe–Kahn finite-field equality plus Ancona positivity is still needed, as explicitly stated.

## The finite-field and spreading directions

For a finite-field fibreA0, a geometric cycle has finitely many coefficients and therefore descends to some finite extension of the residue field. If it is numerically trivial over the algebraic closure, it is numerically trivial over that finite extension by testing the cycles already defined there. Broe's theorem and the Kahn deduction apply over **every** finite field, so they can be applied at that extension. Geometric base-change invariance then gives its zero geometric cohomology class. This is not a general assertion thatD over one field automatically ascends to its algebraic closure.

For a fixed generic cycle, numerical triviality is preserved by extension via `lem:B-basechange-num`. Only finitely many cycles are used to construct its components and the needed correspondences. Their defining equations descend to an enlarged finitely generated field and, after shrinking, spread with the abelian scheme. Smooth proper base change preserves the cohomological Lefschetz equations and intersection pairings. Thus the fibre positivity is applied to the actual specialized primitive algebraic classes. No specialization of numerical triviality is assumed.

## Program and reading scope

Four original pages were rendered by a logged inline PyMuPDF command in **0.938050769000256seconds**. The exact executed code has been preserved afterward as `code/part_b_kleiman_dependency_render.py`; its original execution was the inline command, not a prior invocation of that filename. The complete output record is `code/part_b_kleiman_dependency_render_output.json`. All four images were actually viewed. No source was re-downloaded and no finite mathematical test was run for this audit. The proof above is algebraic, not inferred from a numerical experiment.
