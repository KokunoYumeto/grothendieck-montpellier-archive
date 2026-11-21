# Whole-proof independent audit: D-BI-22a, D-BI-22b, D-BI-22

**Outcome: PASS.** Reviewer `/root/imprimitive`, GPT-6 Astra Pro, reasoning effort inherited/not exposed, run HODGE_DIVISION, 2026-11-21, completed about 17:15 UTC.

Reviewed the complete `twisted_lie_section.tex`, SHA-256 `58fcc2b26bfd785b14b01bd254e17bc853e6138787e8ce9238342cdd5cd7ca43`, the complete GAP exporter/scanner and the complete Python checker. No changes were made to the author's files.

## Mathematical verification

I checked the coverage of all nonlinear irreducible representations of the universal Suzuki cover with noncyclic center, rather than incorrectly restricting to faithful representations. For its cyclic outer group, the specified actual extension suffices: a lifted normalizer intertwiner can be rescaled to satisfy the extension's power relation, including when that extension is nonsplit. The selected extension rows are precisely those restricting irreducibly to the universal core. A central kernel not preserved by an automorphism cannot create a missed compatible intertwiner.

For the three remaining small simple groups I checked the distinction between a bound on core traces and a bound on arbitrary normalizing operators. D-BI-18's complex commutator argument supplies the latter with the factor of one fourth, including its separately handled nonidentity scalar commutator. No unavailable outer-extension table is being assumed. The coefficient L1 estimate on each retained cyclotomic value is an upper bound in every complex embedding, so it is sufficient without numerical approximation or cancellation assumptions.

For every remaining field size, the precise DHP character bound gives `c(q) <= 9/32` at `q >= 32`; the normalizer moving fraction is consequently at least `23/128`. The three smallest-degree formulas have the correct conversion from Lübeck's square-root field parameter. Their first admissible large fields are 32,243,32 and the minima are 124,58807,134090748. All are increasing thereafter.

I checked the full tensor argument, including the intrinsic simple-factor decomposition, factor-preserving intertwiners, finite-order weighted tensor cycles and the constant-word count. The same fraction survives tensoring with other cycles. The actual intermediate-cover period factorization gives genus zero and at least twelve genuine branch points; this is not a sufficiency inference from parameter dimension. The resulting inequality is `12 ceil(23e/128) <= 2e+6`, hence `e <= 192/5`. Two factors already have degree at least 196; one large-field factor has degree at least 124. The sharper small-group fractions leave bounds 6 and24, below their minima14 and26. The treatment of the nonsimple `2G2(3)` endpoint is correctly separated.

## Independent finite reconstruction

Executed the new reviewer-owned `independent_check.py`, importing only this reviewer's earlier integer-polynomial cyclotomic arithmetic. It imports neither of the author's checkers, and selects extension rows by pointwise equality with a complete core character row rather than by the author's normalized-trace norm computation.

Result: PASS in 0.188 seconds. Input SHA-256 `10dd43bccf28471f0c8725086666385aba1dc9970fe9d53bd1478e9ad6a1637b`.

| Table | Selected rows | Nonscalar entries | Independently recovered bound |
|---|---:|---:|---:|
| `2^2.Sz(8)` |34|1054|minimum `nu/a = 3/7`|
| `2^2.Sz(8).3` |12|276|minimum `nu/a = 3/7`|
| `R(27)` |34|1156|maximum coefficient L1 ratio `26/703`|
| `2F4(2)'` |21|441|maximum coefficient L1 ratio `3/13`|
| `2F4(8)` |112|12544|maximum coefficient L1 ratio `449/32319`|

Thus all213 rows, all1330 Suzuki Fourier spectra and all14141 remaining trace bounds were reconstructed. The Fourier method reduces integer polynomials modulo cyclotomic polynomials and independently checks nonnegative integral multiplicities and their degree sum. Exact output is `independent_check.json`.

## Published-input checks and limitations

Freshly opened the published Duyan–Halasi–Podoski PDF, Theorem4.1(2), p141, including its full stated proof/attribution. The ordinary complex character bound has no finite-field representation hypothesis; its use here is through the already proved complex commutator lemma.

Freshly read Hiss–Husen–Magaard Chapter5, Table1 and preceding paragraph, numbered p35, confirming the sole exceptional multiplier among the three series is `Sz(8)`; the same passage explicitly treats `PSp4(3)` as ordinary in characteristic3. Freshly read §10.2, numbered pp130–131, especially the complete-character-table statement immediately before Proposition10.4. This supports the distinction between Malle's published unipotent calculation and the complete CHEVIE table: no claim that the unipotent paper alone contains every character was made.

Read Lübeck's complete Theorem2.1 statement and its surrounding computational-input explanation on numbered p4, and all relevant first-degree tables on numbered pp9,14–15. Its web server returned the unsupported MIME type `application/x-pdf`, so these pages were read from the author's already downloaded full PDF/text in the sibling source cache. The theorem and the identified character tables are accepted published mathematical inputs; this audit is not a new proof of their classification or construction.

Sources read:

- DHP: https://www.degruyterbrill.com/document/doi/10.1515/jgth-2019-0043/pdf — retrieved refs `turn626113053view1`, `turn952401152view0`.
- HHM author full text: https://www.math.rwth-aachen.de/~Gerhard.Hiss/Preprints/ImIrrMod.pdf — refs `turn267577393view0`, `turn626113053view3`, `turn411133210view0`, `turn952401152view1`.
- Lübeck author full text: https://www.math.rwth-aachen.de/~Frank.Luebeck/preprints/smdegexc.pdf — local full text `../g34_eightfolds/bireflection/sources/Luebeck_smallest_exceptional.txt`.

The finite exact input is a representation-theoretic source, not a construction of the groups from axioms. Orthogonality is a consistency check, not by itself proof of the groups' identities. This distinction is explicit in the audited proof.
