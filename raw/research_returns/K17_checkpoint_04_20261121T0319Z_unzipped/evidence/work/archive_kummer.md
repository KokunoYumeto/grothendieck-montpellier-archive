# K17 archive review: cote 149, scans 79–85

Agent: `/root/archive_kummer`; model: GPT-6 Astra Pro; reasoning-effort setting: not exposed to this agent. Date: 2026-11-21 (Europe/Berlin). This is a research contribution for incorporation into the root package, not a final delivery. The seven supplied TeX transcriptions were read in full. The manuscript images are not attached, so no palaeographic claim below is image-verified.

## 1. Exact object of the archive passage

Write `D` for the finite étale boundary of the relative curve, to avoid the manuscript's reuse of `T` for the Tate module. In scan 79, `X/S` is smooth proper, `U=X\D`, and `g_i:S→D` is a boundary section. Subject to the stated homotopy exactness and inertia-injectivity hypotheses, `L_i` is the corresponding geometric inertia subgroup. Scans 80–81 consider

\[
1\longrightarrow T\longrightarrow N(L_i)\longrightarrow E_S\longrightarrow1,
\qquad T=\varprojlim_n\mu_n=\widehat{\mathbf Z}(1),
\]

with class `c_i` in `H²(E_S,T)`. The proposed geometric interpretation is the Kummer first Chern class of the normal or conormal line at the cusp. The author expressly leaves the sign/convention open in scan 81, line 13. A normal/conormal sign cannot honestly be entered as a transcription error.

Scans 82 and 85 separate two torsors, after existence of a splitting:

* bases of the conormal line form a torsor under `Γ(S,O_S)^×`;
* conjugacy classes of splittings form a torsor under `H¹(S,T)`.

The word “conjugacy” is essential: actual splittings of a fixed split extension are described by continuous `Z¹`; quotient by conjugation under `T` gives `H¹`. Scan 79 already works with a conjugacy class of inertia subgroups, so this is a mathematical clarification, not an emendation.

The problem at the end of scan 85 is to characterize the geometric sub-torsor in the profinite description. It is not merely to show that the obstruction `c_i` vanishes, nor to count cuspidal packets. The supplied war-game table repeats an uncertain wedge when describing the group acting on geometric splittings; that repetition does not validate it.

### Primary locators checked

1. **SGA 4, Exposé IX, Théorie de Kummer 3.2; Théorème 3.3.** The first gives the étale exact sequence when `n` is invertible; the second identifies `H¹(G_m)` with `Pic`. Primary text (retypeset French edition maintained by Fabrice Orgogozo): <https://www.normalesup.org/~forgogozo/SGA4/tomes/tome3.pdf>. PDF indices 19–20; printed retypeset pages 14–15. Search references: `turn696412794view0`, `turn866964894view1`, `turn636145465view1`.
2. **Jannsen, Continuous Étale Cohomology, Math. Ann. 280 (1988), (3.1), p.216; (3.27), p.222.** The first supplies the derived inverse-limit exact sequence; the second treats inverse-system Kummer sequences. Primary author/institutional repository: <https://epub.uni-regensburg.de/26684/1/jannsen12.pdf>. References `turn794738992view1`, `turn435555193view3`, `turn435555193view4`, `turn636145465view2`.
3. **SGA 1, Exposé XIII, Proposition 5.2 and Corollaire 5.3**, printed reedition pp.315–316 (original marginal pp.428–430): the local tame Kummer cover classification and its inertia module. The relative versions are Proposition 5.5 and Corollaire 5.6. Primary reedition: <https://arxiv.org/pdf/math/0206203>. References `turn447264653view0`, `turn600754779view0`, `turn636145465view0`. Exposé X, Lemme 3.6 is the DVR form of Abhyankar's lemma.
4. **Stix, On cuspidal sections of algebraic fundamental groups**, author PDF dated 24 February 2012, Proposition 11 (§3.3, p.7); Proposition 16 (§3.5, p.8); Theorem 17 and Corollary 19 (§4, pp.8–9). These give the local packet torsor, normalizers, and packet injectivity/abundance with stated hypotheses. Primary URL: <https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf>. References `turn794738992view0`, `turn342517261view1`, `turn435555193view0`, `turn435555193view2`. Do not turn the all-cuspidal-packet characterization in Corollary 32 into a characterization of the geometric tangent-vector subset.

## 2. F149-KUM: the exact inverse-limit Kummer calculation

**Statement.** Let `S` be a connected normal noetherian scheme, let `l` be invertible on `S`, and put `U=Γ(S,O_S)^×`, `P=Pic(S)`. Write `U_l^∧=lim_r U/U^{l^r}`, `P_l^∧=lim_r P/l^rP`, and `T_lP=lim_r P[l^r]`, where the torsion transition is multiplication by `l`. Then

\[
0\to U_l^\wedge\to\varprojlim_r H^1(S,\mu_{l^r})\to T_lP\to0,
\]
\[
0\to P_l^\wedge\to\varprojlim_r H^2(S,\mu_{l^r})
\to T_l H^2(S,\mathbf G_m)\to0.
\]

If `P[l^∞]` has bounded exponent (in particular if `P` is finitely generated), then `T_lP=0`, and `H¹(S,μ_{l^r})` is Mittag-Leffler. Consequently the degree-two continuous cohomology equals the displayed inverse limit. Since `H⁰(S,μ_{l^r})` is finite, degree-one continuous cohomology equals its inverse limit without that Picard hypothesis. Thus in the finite-generation setting

\[
H^1_{\rm cont}(S,\mathbf Z_l(1))\simeq U_l^\wedge.
\]

For a scheme over `Q`, replace the `l`-powers by all `n`, indexed by divisibility (or by the cofinal sequence `n=r!`), to obtain the full-Tate-module formulas used in scans 80–82. This completion is the **pro-N completion** `lim U/U^n`; if `U/U^n` is infinite it need not be a compact profinite completion of `U`.

**Proof of the form needed here.** Kummer 3.2 and Hilbert 90 3.3 give

\[
0\to U/U^{l^r}\to H^1(S,\mu_{l^r})\to P[l^r]\to0,
\]
\[
0\to P/l^rP\to H^2(S,\mu_{l^r})\to H^2(S,\mathbf G_m)[l^r]\to0.
\]

The transition on each left term is the quotient map, hence surjective. Its `lim¹` is therefore zero, so taking inverse limits proves both short exact sequences, including surjectivity on the right. If `l^e` annihilates `P[l^∞]`, then for `m≥r+e` the transition `P[l^m]→P[l^r]` is zero. Thus the image of `H¹(S,μ_{l^m})` in `H¹(S,μ_{l^r})` is contained in the unit term. It contains that entire unit term because `U/U^{l^m}→U/U^{l^r}` is surjective. These stabilized images prove Mittag-Leffler and `T_lP=0`. Jannsen (3.1) now removes the degree-two `lim¹` term. For degree one, the missing term is `lim¹H⁰(S,μ_{l^r})`, which vanishes because these groups are finite. The full-`n` proof is the same on the cofinal factorial sequence; finite torsion exponent annihilates sufficiently long torsion transitions. ∎

**Consequence for transcription.** In scan 82, formula (21), the uncertain final arrow is mathematically `→0`, with the usual transition maps. Scan 80, formula (17), can likewise be completed by `→0` if its middle term is the naïve inverse limit, or continuous cohomology under the preceding hypotheses. Its missing terminal zero is not a false formula. The `K(π,1)` assertion in scan 80 does not by itself dispose of every inverse-limit issue; the finite-generation arithmetic hypotheses do so in the application. No unverified universal identification of continuous cohomology with ordinary cohomology of the inverse-limit étale sheaf is used.

**Proof check.** Entire proof reread after writing. Checked coefficient transition diagram: roots map by `l^{m-r}`, first `G_m` by that power, second `G_m` by identity; therefore quotient transitions are reduction and Picard/Brauer torsion transitions are multiplication. Checked both `lim¹` uses and the distinction between degrees one and two. Pass; no formal certificate.

## 3. F149-UNIT: explicit nongeometric Kummer classes on the integer scheme

**Statement.** For every prime `l`, let `S_l=Spec Z[1/l]`. Then

\[
H^1_{\rm cont}(S_l,\mathbf Z_l(1))\cong
\begin{cases}
\mathbf Z_l,& l\text{ odd},\\
\mathbf Z/2\mathbf Z\oplus\mathbf Z_2,&l=2.
\end{cases}
\]

Under this identification, the valuation coordinate of every Kummer class of an actual global unit is an integer. The compatible Kummer class with valuation

\[
\alpha=\frac{1}{1-l^2}\in\mathbf Z_l\setminus\mathbf Z
\]

is therefore not geometric. This occurs despite `Pic(S_l)=0` and despite the triviality of the normal line of the standard tripod cusp. It is an example of a nongeometric *local splitting class*, not a proof that no richer anabelian description can recognize the geometric subset.

**Proof.** The localization `Z[1/l]` is a PID, so its Picard group vanishes; its units are exactly `±l^a` with `a∈Z`, by unique factorization in `Z`. F149-KUM gives `H¹_cont=lim_r U/U^{l^r}`. For odd `l`, exponentiation by `l^r` is an automorphism of `{±1}`, so the sign factor vanishes in every quotient and the valuation factor is `Z/l^r`. For `l=2`, the sign factor remains `Z/2` with identity transitions, and the valuation factor is `Z/2^r`. This proves the formula. Since `1-l²` is a unit of `Z_l`, `α` belongs to `Z_l`; it is not an integer because its reduced rational denominator is `l²-1>1`. For each `r`, choose `a_r∈Z` congruent to `α mod l^r`. The classes of `l^{a_r}` in `U/U^{l^r}` form a compatible system, independent of the choices. If this system came from `±l^a`, then `a=α` in `Z_l`, impossible for `a∈Z`. For the cusp with a chosen parameter, a fixed tangential splitting identifies local splitting classes with the Kummer `H¹`; changing the global tangent parameter by a unit acts by that unit's Kummer class. Thus the displayed class is outside the geometric parameter image. ∎

**Full versus one-prime warning.** The injection in scan 85 is a full-completion statement. It cannot be projected to an injectivity assertion for every `l`: for every odd `l`, `-1` is an `l^r`-th power of `-1` for all `r`, hence maps to zero in the `l`-adic Kummer completion. This explicit counterexample requires no conjecture.

**Proof check.** Entire proof reread after writing. Checked the `l=2` torsion factor (it is `Z/2`, not zero), coherence of the exponent classes, PID/Picard calculation, and the restricted interpretation as local splitting classes. Pass.

## 4. F149-TORSOR: correction of the uncertain completion mark

**Statement.** In scan 85, line 8, the group of changes between geometric bases of a trivial conormal line is `G_m(S)`, not `G_m(S)^∧`. The map of geometric bases to splitting classes is equivariant for the Kummer map `G_m(S)→H¹(S,T)`. When that Kummer map is injective, the geometric bases form the claimed sub-torsor under the *uncompleted* group.

**Proof.** If `L≅O_S` and `b,b'` are two bases, the unique scalar `u` with `b'=ub` is an invertible global regular function. Conversely every such function changes a basis. Thus the basis set is a simply transitive `G_m(S)`-set. In a local parameter model, replacing `t` by `ut` changes the compatible root towers by roots of `u`; their descent cocycles are exactly the Kummer cocycles. This gives equivariance. The class from F149-UNIT cannot come from such a basis, proving concretely that replacing the acting group by its completion changes the statement. ∎

This is a mathematically compelled resolution of the `\unsure{\wedge}` flag, not visual confirmation of the handwritten glyph. Scan 82, line 4 already gives the correct uncompleted group explicitly. A standalone correction of the repeated wedge in the war-game intake should point to the archive source rather than treat the intake as a second source.

**Proof check.** Entire proof reread. Checked ordinary bases versus formal parameters: higher-order changes `t↦ut+O(t²)` act on tame root towers through the leading unit because `1+tA[[t]]` is uniquely `n`-divisible when `n` is invertible. In the displayed arithmetic `l`-power situation, the same Hensel argument applies. Pass.

## 5. The line-bundle obstruction: what is proved and what remains in this review

The finite-level expected identity is `c_i mod n=±δ_n(L_i)`, where `δ_n:Pic(S)/n→H²(S,μ_n)` is Kummer and `L_i=J_i/J_i²` is conormal. A local coordinate check is transparent: choose parameters `t_a`; their leading transitions `u_ab` are the line-bundle cocycle. On refinements choose `n`-th roots `v_ab` of `u_ab`. The failure of the lifted root coordinates to satisfy the triple-overlap condition is `v_ab v_bc v_ca∈μ_n`, the usual Kummer boundary. Higher-order coordinate terms have unique `n`-th roots in the formal unit subgroup and do not change this class. SGA 1 XIII 5.2–5.3 supplies the local tame cover calculation needed to recognize these root towers.

This checks the **finite-level local obstruction formula** and its sign change under dualizing the line. It does **not**, by itself, establish the full relative identification of the formal-tube extension with `N(L_i)` in every generality suggested by scan 79. That comparison requires the homotopy hypotheses, inertia embedding, and descent of the formal tube. The archive itself marks part of the setup “à vérifier”. Do not label a global proof of this comparison as complete on the strength of the above two paragraphs. Over a field the local extension and its torsor are already covered by Stix Proposition 11; over a trivial normal line the geometric root tower directly supplies a splitting.

The finite-generation hypothesis in scan 81 ensures `Pic(S)→lim_n Pic(S)/n` is injective: for any finitely generated abelian group `A`, structure theory gives `∩_n nA=0`. Therefore **once the extension-class comparison is supplied**, splitting is equivalent to triviality of the line in that arithmetic setting. This is an obstruction calculation, still distinct from the final recognition problem.

## 6. The two additional editorial flags

* **Scan 83, line 5: `x_i de X` should refer to `x_i de S`.** Irreducible divisors of `S` are in bijection with codimension-one generic points of `S`. The same sentence normalizes `S` in its function field and chooses points above `x`. A codimension-one point of the relative curve `X` need not be a point of `S` and cannot serve as the stated normalization point. This is high-confidence mathematical correction, but no image was available.
* **Scan 80, line 2: surjectivity does not imply splitting.** A literal unconditional reading of “on trouve donc des scindages” contradicts the subsequent obstruction calculation. The exact sequence `0→Z_l --l→ Z_l → Z/l→0` is a concrete nonsplit continuous extension: a section would send a nonzero finite-order element into the torsion-free group `Z_l`. Surjectivity of a normalizer proves the extension exists, not that it splits. The correct intended word cannot be reconstructed from mathematics; record this as a return-to-image flag with a logical requirement, not an invented French transcription.

Possible but **not compelled**: scan 83, line 3, invokes `S' normal` in a Hartogs argument across a codimension-two complement. The needed condition is normality (or appropriate `S_2`) of `S`. Since `S` is already smooth in the surrounding setup, the proof is not refuted; `S'` may be a scribal/transcription slip or an unnecessary remark. It should be a low-priority image-check candidate, not a claimed correction. A precise published locator for the extension principle is EGA IV_2, Théorème 5.10.5, pp.115–116, together with the normality criterion 5.8.6. The original Numdam edition is <https://archive.numdam.org/item/PMIHES_1965__24__5_0/>. Update: the primary EGA IV2 PDF was subsequently downloaded from the Grothendieck Circle mirror, https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EGA/EGAIV.2.pdf . Theorem5.8.6 p108, Proposition5.9.8 and Definition5.9.9 pp111–112, and Theorem5.10.5 with its proof pp115–116 have now been directly read; the printed pages108 and115 were also visually inspected. Normality gives S2, hence depth at least2 along the codimension-at-least2 complement; Theorem5.10.5 and Proposition5.9.8 give O_S = j_* O_(S prime). Exact primary locators are now verified.

## 7. Relation to K17 and SA06

1. The archive's Kummer calculations have Tate twist one and integral Tate-module coefficients. The obstruction is a first Chern class of a line bundle, and the splitting ambiguity is the completion of units. In algebraic K-theory language these belong to the determinant/first gamma-filtration layer of `K_0` and to units in `K_1`; writing `Pic` as an additive subgroup of `K_0` would generally be incorrect. They do not identify `H¹(O_E[1/l],Q_l/Z_l(-e))` with `H¹(S,Z_l(1))`. The rational Tate sheaf `Q_l(1)` has weight `-2` at finite-field fibres, not weight one.
2. A Tate twist changes the cyclotomic Galois action. Even if a duality converts a negative-twist group into a positive-twist obstruction, its cohomological degree and local conditions must be given. No such duality map or class-to-line-bundle comparison is specified by step 17.
3. Vanishing of higher `K_{4k}(Z)⊗Z_l` would therefore not, merely by the Kummer sequences, select the uncompleted units inside their completion. F149-UNIT demonstrates the residual distinction on `Spec Z[1/l]` with zero Picard group for every prime.
4. The supplied SA06 intake E.4a–p consists principally of status summaries; its table expressly says these statements were not read in full by that intake author. It is not a supplied proof or full all-twist cohomology table. This subtask does not import those statuses as established lemmas. In particular E.4m's “negative-twist wild local Galois-cohomology correction” cannot be eliminated without its full statement and comparison maps.
5. The war-game row **S24**, not B3 itself, is the precise programme location for scan 85's recognition problem. The elementary Kummer results and Stix's packet results clarify it; they do not close it. There is no result here requiring Masullo's draft. Crystals, divided powers, and characteristic-prime comparison do not enter these prime-invertible Kummer proofs; inventing such a bridge would overstate the result.

## 8. Recommended status for task 5

* Exact reading of the questions in scans 79–85: checked.
* Inverse-limit Kummer formulas in the arithmetic finite-generation setting: proved in the needed form (F149-KUM).
* Distinction between geometric parameters and all local splitting classes, including explicit nongeometric classes for every prime: proved (F149-UNIT, F149-TORSOR).
* Full global relative normalizer/formal-tube comparison: gate remains; local finite-level computation checked, no universal global proof claimed here.
* Profinitary intrinsic recognition of geometric tangent vectors: remains a gate, untouched by a merely unspecified weakening of Vandiver.
* Transcription amendments: mathematics-based candidates only; no original image verification.
