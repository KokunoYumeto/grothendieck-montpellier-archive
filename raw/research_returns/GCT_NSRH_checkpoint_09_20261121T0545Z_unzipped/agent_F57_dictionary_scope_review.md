# F57: source scope, effective-cone dictionary and parity audit

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

Report read in full for scope: `agent_rank4_negative_trace.md`, final inspected SHA256 `d22b8faf7f5616686c736e26bd28b320766ad7b823574e0a4693cf0a2d465778`.

**Scope/parity/source-context PASS.** This reviewer inspected the complete report and independently checked the listed primary TeX contexts and parity consequence. Theta is assigned the separate whole-proof, original-PDF figure and exact word-product review. This record does not claim to replace that review or to have rerun the entire length-eleven matrix certificate.

## Primary source scope independently checked

I read the supplied primary IV TeX, SHA256 `5c5b990306c3b817d822df9f5088fdd42dda146fc3449155a0b2f6202d2ed49e`, in the following complete pertinent contexts: Proposition11.6 and its elementary proof; the definitions of the ordinary and Theta-opposite contragredients; Propositions11.11 and11.12; the trace/symmetric splitting and its displayed generic denominator; Remark11.19; the full rank-four simple list and dimension114; Theorem13.4's two-row list; Example19.3's modified forms, coefficient statements and Figure22 TeX graph/caption; the following distinction between the already constructed tensor basis and the unresolved algebra cellular basis.

The source explicitly makes Theta send `P_i` to `Q_i`, while the sharp contragredient uses the anti-involution. Therefore the dual matrices are transposes and the reversed word is required for the displayed trace identity. The report preserves that order correctly.

The extra five-dimensional sharp-dual is in the full generic simple list and is omitted from the two-row quotient. The source's tensor contragredient formulas place it in the stated `M_(2,1,1) tensor M_(3,1)` restriction. The generic splitting is explicitly over the field, so no integral splitting is silently claimed. Its quantum tensor occurrence for dimensions at least3 and2 follows from those ordinary polynomial partitions. These are source classification inputs and a scoped occurrence deduction, not a new proof of all source representation theory.

I matched the three displayed Q matrices to the source's Figure22 TeX nodes, descent labels and directed edges, including the `-2`, negative delta and negative `a2` edges. The source graph is a named Q action on the trace-free symmetric simple. Its necessary algebra-relation checks do not become a full rank-four presentation, which the source explicitly says is unavailable there. This is a primary source-code inspection; I did not newly render the PDF figure in this review.

The report correctly distinguishes source signed/factored positivity from strict nonnegative Laurent matrices. The already known rank-four tensor basis, modified global/local forms and the two-row restriction are not refuted by this result. A whole-tensor effective-kernel conclusion requires the extra effectiveness of the specified summand projector. That premise is stated, not inferred from abstract semisimplicity.

## Parity and Tate-shift consequence

Given the proved word polynomial, its highest Laurent coefficients are `-1` at powers plus/minus18. Its constant Laurent coefficient is668. I independently expanded the displayed polynomial in `D=(v+v^-1)^2` with exact SymPy arithmetic and checked all coefficients:

`c0=668`, and for `j=1,...,9`, the coefficients at both `v^(2j)` and `v^(-2j)` are `657,476,297,176,67,36,4,2,-1`.

Under `v=q^(n/2)` with `q>1`, these are distinct nonzero exponential roots `q^j`. Finite-power Vandermonde independence fixes their coefficients uniquely, even for an eventual equality. A genuine finite power trace has nonnegative integer coefficients after eigenvalues are grouped; arithmetic Jordan blocks do not change its power trace. Since the polynomial has both positive and negative coefficients, neither it nor its negative is such a trace. Therefore an overall cohomological parity shift cannot repair it. More generally, a bounded complex with all nonzero cohomology in one fixed parity has only one coefficient sign and is excluded under the same comparison. A fixed Tate twist rescales every distinct root by the same nonzero scalar and preserves all coefficient signs. This is exactly the added consequence in the report.

The opposite-parity possibility is concrete. With geometric Frobenius on `E(-j)` equal to `q^j`, put

\[
 E_+=E^{\oplus668}\oplus
 \bigoplus_{j=1}^{8}\bigl(E(-j)\oplus E(j)\bigr)^{\oplus c_j},
 \qquad E_-=E(-9)\oplus E(9),
\]

where `(c1,...,c8)=(657,476,297,176,67,36,4,2)`. Then the bounded coefficient complex `E_+ direct-sum E_-[-1]` has the displayed polynomial as its Euler trace. The exact dimension check gives `dim E_+=4098`, `dim E_-=2`, and Euler dimension4096, also equal to `p(4)`. All twists are integral because the word polynomial has only even quantum exponents. This constructs a trace-only bounded Tate witness; it does not retain the word operators, source simple labels, or coherent operations. It confirms the deliberate scope of the obstruction.

## Proposed exact Grothendieck translation

The actual generic simple and named matrices are finite locally free module/action data in EGA I, Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90–92. SGA3 I4.7.2–3 and cote90 scan17 supply the existing action framework, not a new group-scheme realization of the noncommutative algebra.

Effective graded coefficient spaces are split-torus representations with characters in `N[v,v^-1]`. The obstruction concerns this actual effective cone. SGA6 V sections2–3 and cote133 scan18 supply coefficient representation/lambda/sigma language; they do not assert a lambda-ring structure on the noncommutative word algebra. The bounded Tate coefficient complex is in the perfect-complex framework of SGA6 I, Definition4.7 pp121–122 and Example4.8 p122, and its Euler class is virtual. A one-parity effective coefficient object and an effective summand projector are not supplied by such a virtual trace witness.

The grading-to-Frobenius law and the larger-module effective projector remain explicit extra comparison hypotheses. No new archive positivity, purity or Lefschetz theorem is used, and no general nonstandard positivity program is refuted by this specified-simple trace. A final generated dictionary can use these already audited anchors without inventing a new manuscript locator.

No main TeX or shared master log was edited. A later complete generated-fragment match remains separate.

## Generated scope and added Tate-witness match

The final generated fragment `finding_F57.tex`, SHA256 `d96f71bfefb7e38e1d6a3b638cb42856476ac0edb9caca21667c4440d63e267e`, was freshly read in its full Laurent-expansion, effective-kernel, finite-power/parity/Tate-witness, final-scope and separate-dictionary passages. They match the proof and distinctions above. The added complex has the stated dimension4098 in even degree and dimension2 in odd degree, the correct geometric-Frobenius twists and the correct negative Euler contribution from `E_-[-1]`. The generated dictionary correctly labels Frobenius as additional coefficient data and retains the extra projector/comparison hypotheses. **Scoped final-fragment match PASS.** Theta owns the separate complete fragment/word-product proof match; this record does not claim a new complete product certificate or a final main-paper insertion check.
