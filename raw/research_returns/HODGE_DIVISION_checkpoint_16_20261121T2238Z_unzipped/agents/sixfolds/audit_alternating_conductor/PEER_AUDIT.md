# Independent whole-proof audit: HD-AST-04–06

**Verdict: PASS in the stated ordinary standard-tensor and actual-source scope.**

Reviewer: GPT-6 Astra Pro, `/root/sixfolds`; inherited reasoning effort is not exposed. This is an independent mathematical reconstruction, complete reading of the submitted proof and author checker, fresh primary-source verification, and a separately authored exact supplement. No author code was imported.

## 1. Frozen material and actual scope of this review

The entire `research/alternating_standard_conductor_section.tex` was read, including the scope and framework paragraphs. Its reviewed SHA-256 is

`051bdda5eccbb84c61c2e197aaec3588f8cd42427f34029736a1694bd0896777`.

The full adjacent bibliography, `research/check_alternating_standard_conductor.py`, and `research/alternating_standard_conductor_checked.json` were also read. The complete dependency `agents/imprimitive/lie_small_fields/alternating_standard_tensor_section.tex`, D-AST-01–03, was reread. In particular this review reconstructed the tensor-wreath trace and normalizer arguments, rather than applying their conclusions to an unrelated scalar twist.

The actual intermediate-cover/source and period-factorization interface in D-AST-03 remains an explicitly identified previously reviewed input. The new proof does not replace that interface by group dimension or conjectural dominance. The archival framework references in the final paragraph were read as scope metadata; their scans were not reopened in this audit. No fresh full proof of upstream class-field reciprocity or existence is claimed.

## 2. Scalar uniqueness and field inclusion

Let `a=n−1`, `e=a^t`, and let `R` be the rational orthogonal tensor-wreath image. A scalar in `R` centralizes each represented simple factor. Since the factors are faithful, centerless, distinct represented subgroups, a nontrivial factor permutation cannot do this. Each remaining standard permutation operator centralizes its `A_n` factor. The centralizer of `A_n` in `S_n` is trivial in the stated range: commuting with every three-cycle preserves each three-element support, and intersecting all such supports containing one letter isolates that letter. Thus `R∩C*I={I}`.

Consequently the scalar coordinate of `g=λT` is unique, multiplicative, and has finite cyclic image `μ_M`. Since each `T` is rational, every actual character value belongs to `Q(ζ_M)`. This proves only the needed inclusion

`K ⊂ F ⊂ Q(ζ_M)`.

The original imaginary quadratic field and the inducing character field are never identified. The direction of the inclusion is correct.

If `K` is not Eisenstein, the quotient `μ_M/(μ_M∩μ_6)` is nontrivial. Images of a generating product-one tuple generate this quotient and have product one, so at least two are nonidentity. For a prime `p|M`, the quotient `μ_M/μ_(M/p)` similarly supplies two exponents not divisible by `p`; their scalar orders contain the entire `p`-part of `M`. This proves the claimed odd-prime and eight-divisibility marks after the quadratic-conductor input. No converse or existence of a marked source is inferred.

## 3. Fresh primary-source check

The author-hosted primary source was opened at

<https://www.jmilne.org/math/CourseNotes/CFT.pdf>.

The front matter identifies **J. S. Milne, Class Field Theory, version 4.03, August 6, 2020**. This is an author course-note source, not a refereed journal article. The following complete invoked passages were read in text and visually checked on PDF pages 165–167, which carry printed pages 157–159:

- Chapter V, Example 3.2, printed p. 157: the cyclotomic Galois group and its action. This supports equal multiplicities for primitive roots in the rational characteristic polynomial.
- Chapter V, Remark 3.8, printed p. 158: conductor divisibility characterizes containment in the relevant ray class field.
- Chapter V, Examples 3.10–3.11, printed p. 159: the rational cyclotomic ray class field and the quadratic conductor, including the three squarefree congruence cases giving conductor `|Δ_K|` in the finite part.

The `M≡2 mod 4` adjustment is legitimate: `Q(ζ_M)=Q(ζ_(M/2))`, so conductor divisibility for the reduced modulus also implies divisibility by the original `M`. The passages support exactly the use `K⊂Q(ζ_M) ⇒ |Δ_K| divides M`. They do not require identifying `K` with the full character field.

Retrieval references from this audit: full PDF `turn939303323view0`; exact text `turn202862188view0`, `turn202862188view1`, `turn202862188view2`; page images `turn839781926view0`, `turn839781926view1`, `turn839781926view2`. These are retrieval identifiers, not a substitute for the bibliographic locators above.

## 4. Rational eigenspaces and support estimates

For the actual finite-order rational operator `T`, primitive roots of a fixed order have equal multiplicities, hence `φ(d)m≤e`. For a root outside `μ_6`, either `d=4` or `φ(d)≥4`. In the latter case the desired estimate is immediate.

For `d=4`, the `i` and `−i` spaces have equal dimension `m`. Their contribution to `tr(T²)` is `−2m`; all other eigenvalues contribute real part at most `e−2m`. The complete D-AST-01 trace argument gives `tr(T²)≥−e/a`. Indeed, the trace on any tensor-wreath element is a product of deleted-permutation traces in `{−1,0,…,a}`, indexed by permutation cycles. A negative product is at least `−a^(c−1)≥−a^(t−1)`, and every power remains in the same rational group. Therefore

`−e/a ≤ tr(T²) ≤ e−4m`,

so `m≤(a+1)e/(4a)`. This argument is made before scalar multiplication, as required. The fixed space of `λT` is the `λ⁻¹` eigenspace of that very operator `T`; it is not estimated by an unjustified scalar-invariance principle.

An order divisible by an odd prime `p` has totient at least `p−1`; an order divisible by eight has totient at least four. If the relevant eigenvalue is absent, the stated lower moving-rank bound is still valid.

## 5. Actual-source budgets and all endpoint arithmetic

The previously reviewed source interface supplies genus zero, at least twelve genuine inertias, and total moving rank `2e+6`. Here `e≥a²≥196`; the higher-genus and genus-one exclusions used in D-AST-03 remain valid. Every one of the other genuine inertias has moving rank at least `e/a`, including factor permutations and scalars.

Two non-Eisenstein marks give

`2e+6 ≥ ((3a+19)/(2a))e`.

For `14≤a≤18`, this means `e≤12a/(19−a)`. The inequality `e≥a²` contradicts this because the minimum of `a(19−a)` over that interval is 18, larger than 12.

Two eight-divisible marks give

`2e+6 ≥ (3/2+10/a)e`.

For `14≤a≤19`, this means `e≤12a/(20−a)`, contradicted by the minimum 19 of `a(20−a)`.

For an odd prime `p≥7`, set `h=p−1≥6`. The budget becomes

`2e+6 ≥ (2−2/h+10/a)e`, hence `e≤3ah/(5h−a)` when `a<5h`.

On `14≤a≤5h−1`, the concave difference `a(5h−a)−3h` has positive endpoint values `67h−196` and `2h−1`. This proves precisely the advertised range `15≤n≤5(p−1)`.

The listed discriminants and remaining lower cutoffs `20,21,31,51,91,211,331,811` follow. At `n=15,t=2`, the old numerical budgets allow the label while the new non-Eisenstein budget requires `427≤398`. This certifies strict strengthening of a necessary gate, not existence of a source satisfying the old gate.

## 6. Independently authored exact supplement

Files in this directory:

- `independent_check.py`
- `independent_checked.json`

The complete independent program and resulting JSON were read after execution. The actual run completed **2026-11-21 22:23:30.156191 UTC**, internal runtime **0.18113369900675025 s**, with status **PASS**. Its script SHA-256 is

`46db70e4d03d6c9089dd80a27cf86ec013726fc116983b7ac2a7eb147a0c6211`.

The checker uses integer cyclic group-ring convolution and three-letter rotation orbits. It does not use the author's phase-counter/two-factor-swap code. In particular it reconstructs weighted three-factor permutation cycles: constant basis words are treated separately, while all remaining ordered words form length-three orbits whose eigenvalues are cube roots of the product phase. It checks rational multiplicities, the square-trace lower bound, and each arithmetic eigenspace estimate.

Actual finite counts were:

- 132 selected deleted-permutation spectra for `8≤n≤24`;
- 132 one-active-factor operators inside three tensor factors;
- 132 three-active-factor tensor spectra;
- 132 weighted three-factor cycles;
- 83,608 generating scalar quadruples for moduli `4,8,12,20,28,40`;
- 1,436 prime-cutoff integer comparisons.

The fourth-root estimate is attained at the tested all-four-cycle labels `n=8,12,16,20,24`. This supplement tests different tensor and tuple cases from the author checker. It is not a computational proof of the universal normalizer statement, conductor criterion, or existence of any curve or period map.

The root output was also read in full. Its separately reported first run was PASS at `2026-11-21T22:19:22.643061+00:00`, runtime `0.5899758599989582 s`, with 2,206 single-active partitions, 1,056 selected two-active tensors, 176 swaps, and 28,524 generating scalar triples. This is recorded as a read author result, not as a reviewer rerun.

## 7. Conclusion and limits

No mathematical repair is requested. The new field-dependent restrictions are valid for the explicitly stated ordinary standard tensor cores and actual rank-nine sixfold-source setting. They do not assert a result for arbitrary long partition shapes, projective cores, arbitrary finite groups, or existence in any remaining range. The conductor source and inherited actual-source interface remain precisely identified.

Audit record finalized: **2026-11-21 22:27 UTC**. Exact file hashes and event times accompany the separate manifest and check register.
