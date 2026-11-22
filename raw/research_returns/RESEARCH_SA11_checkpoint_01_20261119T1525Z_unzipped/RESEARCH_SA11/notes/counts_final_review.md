# Final independent review of T1–T3 and the treatment of L4

**Date:** 19 November 2026. **Reviewer:** GPT-6 Astra (OpenAI), inherited effort, subrun `/root/counts`. **Type:** targeted proof check. No priority is claimed.

## T1–T3: verdict

The proof in `sections/surface.tex` has a coherent complete route to the asserted surface, with arbitrary old vertex multiplicities allowed. I found no counterexample or remaining substantive gap in its local four-cycle or exceptional collar construction. The coordinate normalization is correct: a nonzero localization coordinate outside a changed zero set fixes the orientation of the new element, and the normal sign near an old line is fixed using an old vertex off that line. Rank three guarantees the needed off-line vertex and at least two distinct vertices on every old line.

The lens lemma properly uses a rank-three oriented-matroid program rather than assuming that an arbitrary drawing is metrically monotone. On its chosen sector, the horizon/objective pair supplies exactly the stated directions, and no strand there is objective-parallel. A source yields the full concurrent fan, so the proof does not silently specialize to double intersections.

The corrected packet convention is now stated accurately. The selected packet reverses its extreme labels; the reflection exchanges those labels and preserves the two spatial sides. The newly interior apex blocks an additional fan on the tracked side. Disjoint vertex supports make the two resolutions commute, and their zero sets make the four face labels distinct.

The exceptional completion is likewise valid for a multiple vertex. Its two stable positions are distinguished by the virtual crossing in an old edge, and the two semi-stable ones by the two local normal choices. Ordinary resolution concerns the whole concurrent fan. The old vertex–edge flag identifies the endpoint of either sort of sweep. The argument excluding two different walls from one stable inertia gap is the right exhaustion argument: two such walls would contain the same two distinct old vertices, contradicting the unique-intersection hypothesis.

The rank-two circle identification and `kappa_+(rho)→kappa_+(-rho)` give the actual antipodal pairing of the free boundary circle. Thus the resulting Möbius collar proves non-orientability directly. This part no longer depends on extrapolating the finite examples or on trusting the manuscript monodromy assertion.

The no-zigzag statement is also correctly separated into two stages. Before filling inertia circuits, pairwise disjoint closed transition intervals give equivalence classes of size at most two along the intervals. In the normalized closed-cell model, the four distinct face labels in every vertex orbit exclude all same-face corner identifications. The local links then prove the manifold property independently of the embedding argument.

### Recommended precision edits

These are clarification edits, not changes of theorem.

1. **T2 after both resolutions.** Replace or supplement “the reverse fans likewise block the tracked sides” with the exact combinatorial reason: a stable exceptional interval inserted into the tracked SS gap would have to have an old wall containing both its boundary apices `v,w`. Those apices belong to disjoint old-line sets, so no old wall contains both. After only one resolution, the newly exposed apex lies inside the tracked lens and blocks the potential empty corridor. This makes the exclusion fully explicit at both stages.
2. **T3 uncapped boundary argument.** State that the maximum-of-`nu` argument for uncapped circuits is applied *before inserting exceptional intervals*, to the ordinary inertia circuits. Once E intervals have been inserted but left free, a boundary walk has constant-height free portions; the earlier argument still describes it after collapsing those portions, but saying which version is used prevents an unnecessary ambiguity.
3. **Positive boundary degree.** If desired, note explicitly that a stable position has an ordinary incident transition: the ordinary extension face-incidence graph is connected (the connectedness proof later in T3 is independent of the surface proof), and it has more than one vertex. No isolated zero-transition disk is therefore missed by the corner-germ permutation. The four-cycle argument itself excludes a one-edge closed face. Alternatively, the standard Levi triangle bound supplies a stronger familiar statement if its source has been opened.
4. **Labelled homeomorphisms.** If the final “labelled cellular homeomorphism” is intended to preserve the interior chord graph as well as the surface cellulation, extend the boundary map over the fixed chord graph and then over its complementary disks. Coning an arbitrary whole-disk boundary map suffices for the surface cellulation, but does not by itself promise preservation of all interior chord labels.

## L4: original scans inspected

I visually inspected:

- `figures/156-4_scan032_cords.png`;
- the complete `figures/156-4_scan032.png`;
- `figures/156-4_scan045.png`;
- the preceding `figures/156-4_scan031.png` for context.

On /032, in the paragraph dated 12 June, the text describes interior “lieux” in `D−∂D`, compact/contractible subsets subject to conditions, and an additional equivalence-class datum of “cordes” joining them to `∂D`. The interior-to-boundary endpoint type is visible in the source. It is not a reading supplied solely by an AI transcription or by Michel Hua's project.

The /045 sentence concerning two disjoint interior lieux does have the recorded reading problem: the visible affirmative clause concerning a subdivision sits uneasily with the following conclusion. Keeping both possibilities is justified. Neither version changes /032's endpoint type, so no inference about chord endpoints depends on supplying the doubtful negation.

## L4: what is legitimately refuted

The **literal identification** of these added arc data with the proper chords of 154/035 is false. Every proper chord has two endpoints on the ambient boundary. An arc joining an interior lieu to the boundary has an interior endpoint and a boundary endpoint. A homeomorphism of ambient pairs preserves that distinction. This is a universal type obstruction, independent of whatever additional compatibility axioms the unfinished 1986 discussion may impose.

The square, singleton, and segment in T4 give a complete finite example of this endpoint-type obstruction. However, their role must remain exactly that: a counterexample to identifying the **two typed kinds of arc datum**, not a purported model of all the unspecified 1986 axioms. The current section already disclaims a complete 1986 axiom system, but its line “therefore supplies the boundary-joining arc datum under discussion” would be maximally precise as:

> It supplies an embedded instance of the stated interior-to-boundary arc type; we do not assert that this example completes the unspecified 1986 axioms.

The universal endpoint obstruction, not an unverified claim about those extra axioms, is what refutes the literal L4 identification. The report should likewise mark L4 as “literal identification refuted,” and should not claim to have settled every possible historical influence or a correspondence obtained after adding markings, collapsing lieux, or doubling arcs. Those are different assertions that L4 did not formulate.

This is a legitimate refutation of L4 as literally stated. If the intended lead were instead “the two topics may be related after a construction,” it would not be a precise proposition and the endpoint example would not refute that broader possibility. The paper correctly gives a concrete relationship instead of claiming historical intent.

## The corrected arc correspondence

The marked proper-chord correspondence is exact in the explicitly stated category of embedded arc data:

- An unoriented proper chord with a marked interior point determines an **unordered pair** of embedded tethers with that common interior endpoint, disjoint interiors, and distinct boundary endpoints.
- The union of such an unordered pair recovers the marked proper chord.
- If an ordered pair of tethers is intended, an orientation of the chord must also be retained.

The two operations are inverse on embedded subsets; on parametrized intervals they are inverse up to endpoint-preserving reparametrization. The paragraph's “up to homeomorphism” should keep this small ambiguity explicit.

A second precision issue concerns the last completion example. The completions ending at `(-1,0)` and `(0,1)` have different **geometric boundary endpoint data**, as the text says. After forgetting those boundary markings and quotienting by all homeomorphisms of the disk that fix the original tether, they can become equivalent. Thus the example proves that a single tether does not specify a particular second boundary endpoint or geometric completion. It should not be used to claim nonuniqueness in every possible unspecified equivalence relation on the 1986 “cordes.” A suitable precise sentence is:

> An individual tether does not specify a second boundary endpoint or a particular embedded completion; those data require choosing a second tether.

The family-level qualification is correct and important: joining paired tethers does not enforce at-most-one crossing or the parallel-class conditions. They remain additional hypotheses. Nothing in T4 should claim an equivalence between all possible 1986 pseudo-disks and all 1983 relative-position disk models.

## Overall recommendation

The general surface theorem can be retained as proved after the stated precision edits. T4 can be retained as a refutation of the literal arc identification, with its exact marked-arc replacement. Preserve the distinction between that proved endpoint statement and the unformalized full 1986 theory; the original scans support the former, not an assertion that every missing axiom has been reconstructed.

## Additional final audit: P4's nonuniform chirotope test

I opened `sources/polygons_richtergebert_ziegler.txt`, §7.2.3, printed p. 10 (lines 417–462 in the text extraction), and its matroid definition in §7.1.1, pp. 1–2. The source states exactly:

- (CHI1): the unsigned support `|chi|` is a matroid;
- (CHI2): every three-term Grassmann–Plücker sign set contains both signs or is `{0}`.

It expressly presents these as a chirotope axiom system, including zeros. Therefore P4's combination of unsigned basis exchange and the three-term relations is sufficient in the nonuniform case. The old rank-three chirotope supplies at least one nonzero triple, so the support is nonempty and has rank three. All its nonzero sets have cardinality three by construction. No missing uniformity assumption is present.

The source quantifies over `lambda` and four other entries, allowing repeated entries among the four. P4 checks five distinct labels. This reduction is valid: if two of the four entries coincide, alternation makes one term zero and the other two opposite, or makes all three zero. Thus the repeated-entry relations hold automatically. A repeated entry with `lambda` is excluded in the source and would likewise force the relevant terms to vanish. The test therefore checks every nonautomatic rank-three relation.

The zero-row exclusion is also correctly typed. In a rank-three matroid, if no basis contains the pair `{i,d}`, that pair has rank at most one. Since `i` is an old nonloop, `d` is either a loop or parallel to `i`. Conversely either condition gives the zero row. Deletion remains the fixed rank-three `M`, so the new element cannot be a coloop. Once the combined map is a valid chirotope and the zero rows are excluded, contraction by `d` has rank two and no loops, as required by the expansion.

## Additional final audit: P3's signed expansion

The expansion formula is correct with the stated positive-endpoint calibration:

`epsilon i precedes eta j` iff `-eta chi_M(i,j,k) q(i,k)=+1`.

There is one prose normalization ambiguity to repair. The *original* vectors need not satisfy a positive proportionality `w_j=lambda w_i`; only the *signed* vectors `epsilon w_i`, `eta w_j` lie on the same positive ray. Write instead

`w_j=lambda w_i`, with `lambda≠0` and `sgn(lambda)=epsilon eta`.

The determinant identity in P3 remains valid for this arbitrary nonzero `lambda`:

`det(a_i,a_j,a_k)=-(z_j-lambda z_i) det(w_i,w_k)`.

The two signed boundary directions have first-order angular offsets

`delta_i=epsilon z_i/(R||w_i||)`,

`delta_j=eta z_j/(R||w_j||)=epsilon z_j/(R lambda ||w_i||)`.

Therefore

`sgn(delta_j-delta_i)=sgn[eta (z_j-lambda z_i)]`

`= -eta chi_M(i,j,k) q(i,k)`.

This proves exactly the displayed precedence sign; changing the chart or using the opposite packet gives the required reversed order. Choosing `k` outside the parallel class makes both determinant signs nonzero. The whole pencil together with one transverse line is straightenable, so a common choice of `k` yields a total packet order; its intrinsic geometric description proves independence of `k`. No realizability of the whole arrangement is assumed.

This audit agrees with the earlier independent boundary certificates for every position in the five finite inputs, but the source-axiom and sign derivations above are the reason the general statements pass.
