# Independent whole-proof audit: D-BI-23a/b/23

**Outcome: PASS.** Reviewer `/root/imprimitive`, GPT-6 Astra Pro,
reasoning effort inherited/not exposed, HODGE_DIVISION,
21 November 2026, approximately 17:42–17:48 UTC.

Audited proof SHA-256: `d893f75031482ed88f5df7bb9ffe738887a1019a0e8c2b7a825094d71387c9a0`.

## Scope actually checked

I read the complete `linear_weil_section.tex`, its bibliography,
`linear_weil/export_and_scan.g`, and `check_linear_weil.py`.
I independently reconstructed the mathematical argument, including
the following points.

1. **Restriction to the special linear group.** The independent-pair
   orbit is transitive for `n≥3`, because a third basis vector corrects
   the determinant. There are exactly `q+3` ordered-pair orbits. The
   displayed decomposition reaches the minimal squared-character norm
   `4+1+(q−2)`, proving both irreducibility and inequivalence of the
   stated restrictions. The two actual trivial summands cause no gap.
2. **Character estimates.** The scalar projector gives the displayed
   fixed-eigenspace sum. With `sum dα≤n` and `dα≤n−1`, moving units to
   the largest part yields the bound `q^(n−1)+q−2`. The deleted
   permutation character lies between `−1` and `B−1`. The separate
   `q=2` formula is `2^d−2`, giving the sharper bound needed there.
   The projective-kernel argument is valid for all the stated simple
   `PSL_n(q)` cases; the exceptional isomorphisms do not invalidate it.
3. **Actual full normalizers.** The triple cover of `L3(4)` is the
   characteristic quotient of the universal cover by its prime-to-three
   center. Automorphisms lift uniquely because the cover is perfect.
   `D12` has precisely the listed conjugacy types of cyclic subgroups.
   Replacing the core representation by an automorphic conjugate keeps
   it among the two degree-21 rows. The scalar correction to `T^d`
   supplies an honest representation of the chosen fixed extension;
   no splitting of that extension is assumed. The inner factor is still
   an element of the same extension, whose entire table was scanned.
4. **All-rank branch inequalities.** I checked the sign and monotonicity
   in `A−3B`, including its exact value `q²−2q−6` at `n=3`. The
   displayed endpoint inequalities for `q=2,3,4` are exact. The unique
   symmetric-form line is present in every real factor case and survives
   transitive tensor products. An imaginary quadratic subfield of the
   inducing character field forces a nontrivial multiplier; at least
   two generating product-one inertias have that property. Thus the
   use of the stronger `e(3−5c)≤12` inequality is justified. No
   convolution claim about nonreal eigenspaces is used.
5. **Geometric scope.** The Euler identity and finite intermediate
   Hurwitz factorization apply to the actual inducing variation, even
   with larger inducing field. The proof derives a necessary obstruction,
   never dominance from parameter dimension. The `q=2` exceptional
   endpoints use the already established all-normalizer spectral lemmas
   D-BI-21c and HD-ALT-02a(3); I reread the latter lemma and proof. Their
   spectral assertions themselves do not require a nonsplit determinant.

No mathematical defect was found. The theorem's transitive-core and
linear-Weil scope is explicit; it makes no claim about arbitrary
non-Weil or unitary characters.

## Primary sources freshly read

- Gérardin, *Weil representations associated to finite fields*,
  Journal of Algebra 46 (1977), 54–101: Proposition 4.2 and its
  **complete proof**, printed pp.82–83, together with the function model
  in Proposition/Corollary 1.4, pp.59–60. I opened and read the original
  published article text through
  <https://www.academia.edu/126991842/Weil_representations_associated_to_finite_fields>.
  This is the published article, not an AI summary or another paper's
  paraphrase. The GL decomposition is a published input; the additional
  SL restriction argument was checked directly.
- Official ATLAS `L3(4)` page:
  <https://brauer.maths.qmul.ac.uk/Atlas/lin/L34/>.
  I read the order, multiplier `3×4×4`, outer group `2×S3`, descriptions
  of the cyclic outer types, and the natural triple-cover model. The
  webpage's general work-in-progress notice is not used to infer any
  undocumented matrices; the complete numerical table inputs are the
  independently retained published ATLAS records of CTblLib.
- All six retained table source strings and the actual fusion metadata
  were checked. The table correctness remains an explicit mathematical
  input, not a conclusion from orthogonality alone.

## Independent exact reconstruction actually executed

`independent_check.py` imports **none of the author's checker, selected
rows, or scan output**. It uses this reviewer's previously authored and
reviewed integer-polynomial cyclotomic Fourier helper from D-SPOR.
It selects rows anew by normalized-trace restriction **inner products**,
rather than the author's pointwise selection. It verifies identity
kernels, orders, normal-class unions, all prime power-map compatibilities,
and cyclic quotient witnesses from the retained linear characters.

The fresh execution passed in **0.182 seconds**:

| Table | Selected rows | Nonscalar spectra |
|---|---:|---:|
| `3.L3(4)` | 2 | 50 |
| `3.L3(4).2_1` | 4 | 140 |
| `3.L3(4).2_2` | 0 | 0 |
| `3.L3(4).2_3` | 0 | 0 |
| `3.L3(4).3` | 6 | 342 |
| `3.L3(4).6` | 12 | 756 |
| **Total** | **24** | **1,288** |

Every spectrum has nonnegative integral multiplicities summing to 21;
every selected row has minimum moving rank exactly eight. All minimizing
spectra are retained in `independent_check.json`.

Input SHA-256:
`12becae3b988a84d6820b658da1ac3dcba4a2a83ff3be85c1342e6cd9bed5e76`.
This is an independent arithmetic implementation of the consequences
of the same published mathematical table data, not a new construction
of those character tables. I did not rerun the GAP exporter as part of
this audit, and make no such claim.
