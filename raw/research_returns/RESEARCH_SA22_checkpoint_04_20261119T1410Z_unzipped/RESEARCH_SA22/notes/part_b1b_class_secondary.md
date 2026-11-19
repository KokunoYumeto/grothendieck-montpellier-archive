# B1(b): exact argument domain and additional explicit geometric members

Date: 2026-11-19. Author: GPT-6 Astra (OpenAI, ChatGPT Pro mode; inherited effort not separately exposed), agent `part_c_algebra`.

## Interpretation audit

The literal prompt at `upload/PROMPT(20261119-110314).md:189` asks to determine the class of fourfolds to which “the same argument” applies. This does not itself ask for an exhaustive isomorphism classification of all fourfolds satisfying the standard conjectures.

The exact componentwise-definiteness method has two inputs: the Lefschetz projections preserve algebraic classes, and the signed primitive intersection pairing is positive definite on **homological algebraic classes**. This is a classical intrinsic cohomological/positivity condition, not an assumption of the desired numerical–homological equality. The existing `prop:B1b-criterion` proves that it suffices; its converse under numerical positivity describes exactly the additional radical issue. In that specified meaning, the conditional method-domain characterization is complete.

However, numerical positivity alone does not verify membership. Assuming numerical positivity, homological positivity is equivalent to absence of the homological radical, hence to the desired equality. Calling numerical positivity alone a completed verification would be circular. The manuscript explicitly does not do that. Ancona's Conjecture3.10, Proposition3.11 and Corollary3.12 confirm the distinction; his all-abelian-fourfold equality in2021 was only for infinitely many primes. The separate abelian theorem uses the opened2026 Broe/Kahn input for all primes and correctly identifies that dependency.

The method-domain criterion does not give an exhaustive geometric recognition algorithm or a list of every geometric family satisfying it. That stronger problem is not claimed to be solved, and the root has directed that it not be invented as a new mandatory isomorphism-classification task. The explicit families below are certified members, not a purported exhaustive list.

## New completed results

The fragment `sections/part_b1b_class.tex` gives three complete proofs.

### B1b-correspondence

If the identity on the fourth cohomology of a fourfold factors through finitely many fourfolds already satisfying D in codimension two by algebraic correspondences, then the target satisfies D. A numerical-zero cycle is sent to numerical-zero cycles by the correspondences because the transpose is adjoint for intersection. Equality on the sources kills all their cycle classes; the identity factorization kills the target class. A generically finite surjective morphism is the case of graph and transpose graph divided by its nonzero degree. No separability assumption is necessary with rational coefficients.

### B1b-blowup

For a smooth fourfold, D in codimension two is equivalent before and after blowing up any smooth closed center of positive codimension. A nontrivial center has dimension at most two, so its D statement in every codimension follows from the divisor theorem and degree for zero-cycles. The proof computes geometric cohomology while retaining cycles over the original field; it does not claim that the D property ascends solely from the numerical base-change lemma.

The proof does not just appeal to an abstract motive. With `j:E→W`, `q:E=P(N)→Z` and `ξ=c1(O_E(1))`, use

`H4(W)=f*H4(X) ⊕ Σ_{a=1}^{c−1} j*(ξ^{a−1}q*H^{4−2a}(Z))`.

For a numerical-zero class, pushforward kills the original component. The identities `j*j*=−ξ`, `q*ξ^{c−1}=1`, and `q*ξ^r=0` for `r<c−1` recover the exceptional components by descending induction. The recovering expressions are classes of numerical-zero cycles on the center, so they vanish by its D statement. The converse follows from degree-one push–pull. No factorization of arbitrary birational maps in positive characteristic is asserted.

For the specific codimension-two center used below, the exceptional pairing is minus the divisor intersection pairing on the center, as independently checked by the B agent.

### B1b-fermat

For every characteristic different from three and every invertible prime ℓ, the Fermat cubic fourfold satisfies numerical–ℓ-adic equality in every codimension. Geometric forms have the same property by the already-proved numerical base-change lemma.

Let `S` be the Fermat cubic surface, and `E` its plane cubic coordinate section. The seven displayed lines on `S` have a unimodular intersection matrix with determinant1. For fixed ℓ, smooth proper base change from `Z[1/(3ℓ)]`, weak Lefschetz and the Chern calculation `∫c2(S)=9` give `b2(S)=7`; thus all of the cohomology of `S`, hence of `S×S`, is algebraic. Poincaré duality gives D on `S×S`.

The exact Shioda–Katsura construction gives

`Bl_{E×E}(S×S) → {z0³+...+z5³=0}`

by

`([x],[y]) ↦ [x0y3:x1y3:x2y3:−x3y0:−x3y1:−x3y2]`.

The map's base ideal is locally `(x3,y3)`, so the blowup resolves it. A general inverse requires the three roots of `a³=−1/(z0³+z1³+z2³)`, so it is generically degree3, including in characteristic2. The source is smooth and projective, and properness makes the map surjective. The preceding blowup and correspondence results give D on the Fermat fourfold. Its other cohomology groups are generated by hyperplane powers, so all codimensions follow.

Ancona's actual PropositionA.9 proves numerical primitive positivity for this exact fourfold in every characteristic different from three. The algebraic Lefschetz splitting is explicit, because `H2` and `H6` each have rank1: subtract `deg(αh²)h²/3` from an algebraic middle class. D just proved identifies numerical with homological primitive positivity. Thus the Fermat fourfold is an additional independently verified seed for the same positivity/specialization argument.

## Explicit covered class

The stated certified class contains abelian fourfolds, Fermat cubic fourfolds, their geometric forms, and all finite constructions using smooth-center blowups or their inverses and algebraic-correspondence retractions as in the theorem. This includes generically finite images. Abelian and Fermat seeds also serve as good special fibres when there is an actual smooth projective specialization and the stated algebraic-Lefschetz hypothesis. An arbitrary fourfold is not silently allowed to specialize to a seed together with every algebraic cycle.

No equality conjecture about an arbitrary target is assumed in these geometric certificates. The intrinsic method-domain criterion is the complete conditional statement; recognizing all possible geometric members outside the proved families remains a separate, unclaimed problem. The smallest missing datum for any proposed additional member is a proof of the required homological primitive positivity (or a concrete correspondence/specialization certificate implying it), not another numerical-quotient positivity calculation.

## Exact primary-source locators

- Shioda–Katsura, *On Fermat varieties*, Tohoku Math.J.(2)31(1979),97–115, original full19-page J-STAGE PDF. `https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf/-char/ja`, opened as `turn441492256view0`, saved at `sources/shioda_katsura1979.pdf`, SHA256 `df45ac74b24700d8127f895fcb6439fe5d8ba8ea3785a28fb731fcdd9f5e8e1f`. Lemmas1.1–1.2, pp98–99, provide the rational map and its blowup resolution; Theorem1.7, pp101–102, summarizes the global construction; Lemmas2.1–2.3, p103, give the blowup and hypersurface cohomology formulas. The cubic map and degree are additionally checked explicitly above.
- Ancona2021, complete author source `sources/ancona/fourfolds_2020.tex:2035–2058` and original author HTML `https://arxiv.org/html/1806.03216v3`, opened as `turn441492256view1`, exact PropositionA.9 and RemarkA.10 reopened as `turn756125645view0`, `turn756125645view1` and `turn439859590view1`. A.9 gives numerical primitive positivity for the Fermat cubic fourfold; A.10 distinguishes this example and the rank-two method from a classification of all fourfolds.
- Kleiman1968 original p361 records Matsusaka's equality of numerical and τ-equivalence for divisors. The rational Chern class of an algebraically trivial line bundle vanishes, giving the divisor case of D needed on the center. Existing `sources/kleiman1968.pdf/.txt` were reopened at that passage.
- The general blowup and correspondence deductions are proved in full in this fragment; no finite-dimensional-motive theorem or unverified recent source is used for the Fermat addition.

## Programs actually run

| Script | Actual scope | Count | Runtime | Saved output |
|---|---|---:|---:|---|
| `code/part_c_cubic_surface_lines.py` | Exact F4 line-incidence calculation and rational Gram matrices |27 lines;351 unordered pairs;135 meeting pairs;216 disjoint pairs;each line meets10;Gram rank7;selected determinant1 |0.02672153499952401s |`part_c_cubic_surface_lines_output.json` and `.txt` |
| `code/part_c_sources_fetch3.py` | Two ordinary public HTTP requests, SK original and Gabriel public catalogue |2 successful requests after initial import correction |19.678302091997466s total;SK19.668251818999124s;catalogue8.502083743002004s |`part_c_sources_fetch3_output.json` and `.txt`; first import-error output separately retained |
| `code/part_c_fermat_source_extract.py` | Original-source text extraction and visual checking |1text extraction;3rendered pages98,99,103;all4commands exit0 |1.3725221739987319s |`part_c_fermat_source_extract_output.json` and `.txt` |

The finite-field calculation certifies the finite incidence data. It is not used as evidence that every characteristic behaves the same: the proof of characteristic independence is the even-cycle/difference-of-cube-roots argument written in the manuscript. Every integer determinant is exact, with no floating-point tolerance.
