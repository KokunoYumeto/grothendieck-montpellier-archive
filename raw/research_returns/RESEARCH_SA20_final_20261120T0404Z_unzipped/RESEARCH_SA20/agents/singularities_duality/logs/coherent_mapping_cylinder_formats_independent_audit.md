# Bounded independent audit: coherent approximation and scalar mapping cylinders

20 November 2026, completed before the 04:04 UTC review. This audit concerns the complete criterion and proof pasted by `/root/maximal_locus2` in the collaboration thread. At the time of this read there was no saved complete authored candidate, so this is an argument audit, not a hash-tied literal-file audit. The already promoted A5.16.1 was freshly read in `agents/maximal_locus/part_A5_surface_method.tex`.

**Verdict: PASS for the explicitly coherent approximation property.** This is not an angular bundle theorem and supplies no qualifying movement of that remaining gate.

## Property being tested

For a continuous definable surjection `q:F->G` between nonempty compact definable sets, positivity means that there is **one** jointly continuous definable family of homeomorphisms `h_s:F->G`, for `0<s<=epsilon`, whose uniform distance from `q` tends to zero as `s` tends to zero.

This must be distinguished from the weaker external statement that, for every positive tolerance, there exists some definable homeomorphism in a possibly unrelated formula format. The proof audited here neither assumes nor proves that this weaker assertion gives a coherent definable family.

## Necessity over every real closed field

The proposed scalar mapping cylinder is

`C(q)={(s,sx,q(x)):x in F,0<s<=1} union {(0,0,y):y in G}`.

After decreasing the original parameter interval to have `epsilon<=1` and extending the homeomorphism family constantly above `epsilon`, the proposed map from `G×[0,1]` sends `(y,s)`, for `s>0`, to `(s,s h_s^{-1}(y),q(h_s^{-1}(y)))`, and sends `(y,0)` to `(0,0,y)`.

This is a bijection preserving the actual scalar height. The identity

`sup_y |q(h_s^{-1}(y))-y| = sup_x |q(x)-h_s(x)|`

and boundedness of `F` prove continuity at the bottom. On positive compact parameter bands the total inverse of the homeomorphism family is continuous by the compact-definable continuous-bijection theorem; these bands cover the positive interval. The full cylinder map is a continuous definable bijection between compact definable sets, hence a definable homeomorphism over any real closed field. No ordinary countable sequence or real compactness is used.

Exact scalar triangulation makes the height a nonnegative PL function and the bottom its zero subcomplex. Relative definable Hauptvermutung applied to the compact product pair then implies that this zero subcomplex has a PL collar. This step only claims a collar; it does not claim that the Hauptvermutung homeomorphism itself preserves height.

## Sufficiency and uniformity of the scalar construction

A5.16.1 applies to a compact polyhedron with a nonnegative PL function whose zero subcomplex is PL-collared. It supplies a collar that preserves the **specified height**. Pulling back by the scalar triangulation and dividing the compressed source coordinate by the positive height gives homeomorphisms `k_s:G->F`. Uniform continuity of the resulting map on `G×[0,delta]` shows that `q k_s` tends uniformly to the identity. Their inverses are a jointly continuous definable family on the positive interval and approximate `q` uniformly.

Thus the criterion is equivalent to PL-collaredness of the bottom in any exact scalar triangulation of this mapping cylinder, with the pair transported by the indicated definable maps.

## Finite formula extraction

In every model of the fixed complete o-minimal theory, an individual cylinder has a finite exact scalar triangulation. Each actual finite abstract pair `(K,L)` and actual formula for its triangulation, with its coefficients and vertex heights as variables, gives a first-order certificate. The certificates range over ordinary finite formats. Compactness gives finitely many formats covering all relevant parameters in all models: failure of every finite subcover would produce a model and parameter with no scalar triangulation.

The label that `(K,L)` admits a PL collar is field-independent. An existing collar has an actual finite semilinear format; its embedding, inverse-continuity, bottom-identity and relative-open-neighbourhood conditions are first-order over the real algebraic field. Existence therefore reflects to that field. Conversely a fixed real-algebraic PL collar is interpreted in every real closed field.

Fix one such collar for every positive label. A fixed common refinement makes that collar, the domain height and every moving target height `g_v` linear on their relevant finite cells. Choose the small height below the positive vertex heights and below the minimum of `g_v` on the **fixed compact complement of an open half-collar**. This minimum is positive because that complement misses the zero set. It can be taken over a fixed finite vertex list after refinement.

For a mixed simplex with `l` positive vertices, give positive vertex `p` weight `epsilon/(l v_p)`; distribute the remaining weight equally over the `k` zero vertices. If `epsilon` is smaller than every positive height, these are all positive, sum to one, and have weighted height exactly `epsilon`. The analogous fixed-domain construction gives the paired stellar subdivisions of A5.16.1. These are finitely many rational operations and finite PL extensions in one format for each certificate. No increasingly fine mesh is required.

Definable choice can select certificate coefficients and an error cutoff. It supplies finite formats for the coherent approximants and for homeomorphisms within a specified error. The proof does not assert continuity of the chosen coefficients or homeomorphisms in the external family parameter.

## Exact remaining distinction

Nothing in this scalar argument preserves the continuum of angular equations `Theta_t A_t=pr_Sigma`. Ordinary closeness of a homeomorphism and finite compatibility with marked subsets do not impose that equation. The finite pool therefore does not presently supply the controlled angular anchors needed for A5.019. A proof of that additional implication would require new projection-preserving input; it is not included in this PASS.


## Literal-file and original-source addendum

At 2026-11-20T04:02:59Z, the complete saved candidate `agents/maximal_locus/notes/coherent_near_homeomorphism_pool_0400.tex` had been literally read. Its final SHA256 is `149bd3f708eb81050f76913b382d88798ed70d1609dd8888a1dc97a84992c225`. **Full authored-text PASS.** The only requested clarification was subsequently read back: the conditional source family `r_t` in Section 4 is explicitly jointly continuous and definable. The final delta consists only of that hypothesis. The principal criterion and finite-format proof were unchanged.

The added matcher estimate is a direct triangle inequality after substituting `y=a_s(x)`. Positivity of the limit is correctly conditional on an already supplied genuine bundle chart; that chart is not manufactured by the scalar pool. The final paragraph explicitly retains both the exact angular projection constraint and the coherence of varying-source/target anchors.

Fresh original-source check: Walsberg, arXiv:1510.07291v2, <https://arxiv.org/pdf/1510.07291>, Lemma 2.8 and Corollary 2.9, printed pp.5–6, concern definable families of pointwise/uniform limits along definable parameter paths over arbitrary o-minimal fields. The sequential identification has the explicit real-field hypothesis. Fact 6.1 and Proposition 6.2, pp.13–14, give definable completeness and completion, not ordinary completeness over an arbitrary field. The saved note preserves these distinctions. Reader references: `turn317472377view0`, `turn890805150view0`, `turn890805150view1`.
