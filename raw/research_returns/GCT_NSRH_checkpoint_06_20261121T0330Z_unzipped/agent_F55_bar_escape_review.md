# F55 formal-bar one-place refinement: independent whole-proof review

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Run `GCT_NSRH_20261121`. Date: 2026-11-21 UTC.

Target: the entire `agent_fractional_bar_escape.md`, SHA256 `f99c7ff251a6437ef69a9ce4b35b104f1bac03fea117e6d2c030c895123ef725`.

**PASS.** I independently read and reconstructed every proof, exact scope statement and dictionary paragraph. I also reran exact symbolic checks of the bar identities, trace identities, base/collision values and determinant with SymPy1.14.0; all passed. Those computations do not replace the all-extension argument below. A generated-fragment match is separate.

## Invariant functions and fixed finite base

The lift `t -> t^-1`, fixing `sqrt(2)`, is an explicit involution of the coefficient field extending `v -> v^-1`. The Laurent function `g=4+2t+2t^-1` and the rational function `Delta(t^2)` are invariant. Hence so are `h,lambda,u`. The canceled expression for `h` is the previous expression divided by `t`; all displayed values at the base and negative collision follow. In particular the rank-eight base trace is `4+3sqrt(2)`, the last multiplicity eigenvalue is `1/sqrt(2)`, and the chosen collision values of `u,lambda` are units.

The stated finite localization is bar stable: the inherited denominator functions are invariant, `t-1` and `t^2+1` transform by explicit Laurent units, and the last two inverted functions are invariant. No additional place-by-place localization is hidden. All positive arithmetic points and their inverses survive.

For every `n>1`, monotonicity of `Delta(2^n)` gives `u>1`. For even `n`, the last eigenvalue is a rational number minus `sqrt(2)` and cannot vanish. For odd `n=2r+1`, its rational coefficient of1 is `2(eta/d_n-1)`, nonzero for `n>1`; independence of1 and `sqrt(2)` over `Q` then proves nonvanishing. The `n=1` value is checked separately. This establishes all-extension invertibility without an asymptotic sign assumption or finite sample. The collision still has the actual second-order contact because the cover has simple parameter vanishing at `t=-1`.

## Actual actions, bar and both traces

The determinant of the full operator is `2 u^20 lambda^2`, a unit. The last block acts only on the four-dimensional multiplicity factor, so it commutes with the actual right action, as do the other scalar blocks. The regular F43 comparison transports this to the original actual module.

Every adapted vector is fixed by the actual F43 tensor bar and every displayed operator entry is fixed by the chosen coefficient involution. Their semilinear commutation therefore holds on the actual module, including after transport. The involution takes the fiber at `t` to the fiber at `t^-1`; it does not make distinct arithmetic Frobenius eigenvalues isomorphic within one fixed fiber. The report correctly distinguishes that formal parameter involution from internal arithmetic duality, Verdier duality, or an unspecified prescribed lift in VIII.

The marked sector has trace `h`, the marked insertion has trace `eta g`, and the full ordinary trace is `56+g`. At the base, the marked spectrum has multiplicities `4,2,2` on `1,s,s^-1`; the full spectrum has multiplicities `60,2,2`. Thus powers of the base operator give exactly the two retuned trace functions at every positive extension degree. In the stated `q=4` normalization these are fractional mixed weights `0,+1/2,-1/2`, with no assertion of an integrally mixed geometric object.

## Stronger requirements still fail

The same actual left raising operator sends the multiplicity eigenvector of value`s` to one of value1, with commutator coefficient `1-s`. Ordinary left invariance is explicitly absent.

The generator trace formulas have factors `36+g-h/2` and `36+g/2`, respectively. For every `n>1`, the former is larger and its `D` factor is also strictly larger, proving the stated fixed-word failures. The square follows from the actual quadratic relation. The full spectral failure is unlabeled: base powers have60 eigenvalues equal to1, while the retuned family has at most42. No unproved correspondence between spectral labels is used.

The last coefficient eigenvalue and scalar-plus eigenvalue have poles at the positive collision. Their negative valuations rule out making this same operator regular there by changing a finite free lattice. The formal bar fixes each of the two collision points separately; it does not exchange them or supply all-places regularity. The scalar traces can remain regular through cancellation, but the marked residues are0 and8 at the two points. This is consistent with both the stronger all-places inserted-trace theorem and the separate positive continuous-branch theorem.

## Framework scope

An affine scheme involution with a semilinear involutive lift on a coherent module is explicit ordinary equivariance data. This makes the existing EGA affine-module and SGA3 action dictionary substantively applicable; it does not reinterpret the whole noncommutative GCT algebra as a group scheme. Cote90 scan17 remains a framework anchor, not an unpublished proof of these formulas. No new archive or exact primary theorem locator is needed for the new elementary identities.

The chosen lift on the algebraic coefficient field is stated, and no uniqueness or prescribed VIII globalization follows. The actual source bar compatibility comes from the already checked F43 basis, while the new rational functions supply the commuting operator. This proves a concrete formal-bar refinement without altering the existing left-action, global-form, or arithmetic comparison boundaries.

No main TeX or shared master logs were edited. No formal proof-kernel or compilation certificate is claimed.

## Entire generated-variant match

I independently read the entire `finding_F55_bar_variant.tex`, SHA256 `e1786cdbc0bb272407cbe94c5e81ef2019650602b96005213077730d71090fe1`, including every proof paragraph and the separate dictionary. **Full report-to-fragment match PASS.** The tildes correctly distinguish the variant from the original Part1 family, leaving its earlier formulas untouched. The new family retains every stated all-extension, bar and action property and every exact failure of a stronger comparison. The actual-bar lift is an explicit chosen extension, not a prescribed arithmetic duality or VIII globalization.
