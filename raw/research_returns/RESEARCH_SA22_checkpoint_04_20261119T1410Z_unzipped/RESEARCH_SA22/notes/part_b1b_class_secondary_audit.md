# Independent audit of the added B.1(b) fourfold class

Reviewer: GPT-6 Astra (OpenAI), agent `part_b_cycles`, independent of the author `part_c_algebra`. Audit completed 2026-11-19, integration at13:45UTC. No new mathematical gate remains in the three added statements after the four precision edits below.

## Files and exact sources read

- The complete fragment `sections/part_b1b_class.tex`, its four-row results table, author's notes `notes/part_b1b_class_secondary.md`, and the full finite-field script and saved output were read.
- The complete original Shioda–Katsura PDF is available at `sources/shioda_katsura1979.pdf`. Lemmas1.1–1.2, originalpp98–99, and Theorem1.7, pp101–102, were read for the map and its resolution; Lemmas2.1–2.3 onp103 were read for the blowup decomposition and nonmiddle hypersurface cohomology. Original pages98 and103 were also rendered to `qa/part_b_audit_shioda_p98.png` and `qa/part_b_audit_shioda_p103.png`; the latter was visually inspected in this audit. Public original URL: https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf/-char/ja . The author's successful web opening is `turn441492256view0`; this reviewer's separate web request `turn695520050view0` timed out, but the actual complete local original was opened and read. The two facts must not be conflated.
- Ancona Appendix PropositionA.9 and RemarkA.10 were previously reopened in the original author source, `sources/ancona/fourfolds_2020.tex:2036–2058`, and at https://arxiv.org/html/1806.03216v3 (`turn130022901view0`, `turn130022901view1`). They give numerical primitive positivity for the exact Fermat cubic fourfold and the limits of the rank-two strategy, not an all-fourfold numerical–homological theorem.
- Kleiman1968 originalp361 supplies the divisor numerical–tau input. The base-change lemma used elsewhere was reread to ensure it was not incorrectly promoted to ascent of the D property.

## Independent proof checks

| Statement | Checks performed | Conclusion |
|---|---|---|
| `B1b-correspondence` | All cycles have the asserted codimensions; transposed correspondence is adjoint for the numerical intersection pairing; the identity factorization kills the target class; graph/transpose directions give pullback then pushforward; the nonzero degree is invertible in Q_l even for an inseparable map. | Correct. |
| `B1b-blowup` | Exceptional summands have cohomological degree4 and twist2; f_* kills them; j^*j_* is multiplication by −xi; q_*xi^(c−1)=1 and lower powers vanish. For descending b, the extraction expression has codimension2−b on Z and equals beta_b plus already killed higher terms. The extraction is an algebraic numerically trivial cycle defined over k. D for centers of dimension at most2 follows from the divisor theorem and degree. Converse is degree-one push–pull. | Correct over arbitrary k with cycles kept over k. |
| `B1b-fermat` | Line equations and within/cross-family incidence equations solved directly; distinct cube roots stay distinct in all characteristics other than3. Meeting lines are transverse on a smooth surface, and adjunction gives self-intersection−1. The displayed seven-line matrix matches the saved determinant1 certificate. Euler characteristic9 and b2=7 follow from weak Lefschetz and c2=3H². Smooth proper base change is applied only where l is invertible. Cubic identity, base ideal, exceptional resolution, generic inverse, degree3 and proper surjectivity all verified. Outside middle degree the cited hypersurface formula applies. Numerical base change is used only to descend geometric D to k/forms. | Correct, including characteristic2 and every invertible l. |

For the map, on x3=y3=1 the output is [x0:x1:x2:−y0:−y1:−y2]. If z is a general target representative, a preimage has x_i=a z_i and y_i=−a z_(i+3). The two surface equations become the same equation a³=−1/(z0³+z1³+z2³), which has three distinct roots when3 is invertible. Along E×E at least one x0,x1,x2 and at least one y0,y1,y2 are local units, so the coordinate ideal is exactly (x3,y3). This proves the degree and resolution without an unstated inseparability argument.

## Precision changes made before integration

1. The blowup center is explicitly of **positive codimension on every component**. Allowing Z=X would produce the empty blowup and would falsify the unrestricted statement.
2. The blowup proof now computes geometric cohomology while retaining cycles and cycle operations **over k**. The numerical-triviality base-change lemma concerns a fixed cycle; it does not on its own show that an assumed D property on k-cycles ascends to all cycles over an algebraic closure. No ascent is needed: the exceptional extraction expressions are cycles over k and the argument applies directly to them.
3. The smooth proper family used for a fixed l is explicitly over **Z[1/(3l)]**, ensuring l is invertible on the base for the base-change theorem.
4. The finite incidence program is explicitly described as a computation over **F4**. The all-characteristic conclusion is proved by the separate cube-root calculation, not extrapolated from that computation.

The author agreed with each refinement. These are source/scope precision changes and a repaired overly broad reduction sentence; they do not rely on modifying the mathematical hypothesis to assume the desired equality.

## Computation and scope

`code/part_c_cubic_surface_lines.py` was independently read; its existing output was inspected, not rerun merely to duplicate a check. The saved output records27 lines,351 unordered pairs,135 meeting pairs,216 disjoint pairs,10 neighbours for each line, rational Gram rank7, and determinant1 for the displayed7×7 submatrix. Original runtime:0.02672153499952401seconds. Finite-field incidence and exact rational determinant arithmetic are the actual scope. There is no measured runtime for the mathematical proof audit itself and none is invented.

The phrase “the class the same argument covers” is answered by the exact conditional method domain in `prop:B1b-criterion`, together with the newly certified geometric families and transfer rules. The audit does not introduce an extra requirement to classify all geometric fourfolds. Numerical positivity alone still cannot certify the homological positivity hypothesis. The Fermat example closes that distinction by first proving D independently and only then using AnconaA.9. Abelian all-prime statements continue to carry their explicitly identified Broe2026 preprint dependency.

## Integration

The fragment is included once by `\input{sections/part_b1b_class.tex}` in `sections/part_b.tex`, before B.1(c). The old overlapping paragraph that speculated about an exhaustive-classification requirement was removed. The author's three numbered statements keep their original labels and dedicated result/event records. The owned PartB main-fragment audit counts51 statements; including this fragment gives54 in the combined PartB material. The parent assembles the bibliography including `ShiodaKatsura1979C` from `sources/part_c.bib` and performs the full recursive compilation/audit.
