# Implications of DP_MULT

Run: **DP_MULT_20261121**, 21 November 2026, Europe/Berlin. This document distinguishes what is proved here, what was already a theorem, what proposed inference is false, and what remains to be constructed. The local questions are decided. The literal substitution into the existing theta construction is refuted; the existence of a different construction with fewer lifts remains an explicit open gate.

## 1. The principal mathematical change

Fable run **20261120, suggestion 2** can be replaced by a checked theorem, DP1–DP4. Over `W(k)`, the one-dimensional height condition suffices; the proof does not require a Lubin–Tate normal form. At finite height h the optimal universal affine slope is `c_h=1/(p−1)−1/(p^h−1)` and the optimal constant loss at that slope is **h−1**. The additional exact floor sum omits the indices divisible by h. Both estimates are coefficientwise and therefore propagate through mixed derivatives on integral product factors.

The adjective “optimal” has a precise scope. The slope is forced by the derivative orders `(p^h)^r` of the coordinate itself. The affine intercept is forced by `n=p^h−1` and `f=t^n` for every fixed normalized group. No exact minimum at every remaining derivative order is claimed. At infinite height the exact universal lower bound is `v_p(n!)`; its digit error is unbounded.

The Fable proof's unsupported normal-form step is removed. Its assertion that one may use total height for a multidimensional summand is false (DP8). A one-dimensional factor only in the special fibre does not by itself give the integral lifted map and tangent lattice used by DP7.

DP19 gives the precise extension over a ramified base: a full integral action of the unramified degree-h local CM order, with its specified tangent character, restores both bounds. The proof uses a Teichmüller-equivariant coordinate and integer ideal containments; it never rounds a fractional valuation as though the base were unramified. DP20 shows that this is a real hypothesis. For every h≥2 and e>p a genuine Lubin–Tate deformation has the same residue height but exact witness valuations `(p^s−1)/(e(p−1))`. The resulting deficit is linear, so even an O(log n) error cannot repair the height-only assertion over arbitrary ramified bases.

## 2. Alpöge step 2 and the theta chain

The scalar coefficient in **Remark, p.3, step2** is exactly `c_2=p/(p²−1)`. For an integral formal function and the normalized invariant derivative, DP6 gives affine loss1. This identifies the local formal-group mechanism; applying it to a normalized analytic theta expression requires an actual integral expansion, period comparison and denominator control. Katz's **Main Theorem3.11(I), p.672**, is stronger on a special trace-zero subspace. Its trace hypothesis cannot be dropped.

The initial source-identification gate is closed. The expanded inventory contains526 targeted modules recovered from a pinned mirror or directly from the author archive. Every local copy was compared byte for byte with the original fourteen-part archive; all matched. Extraction and byte comparison are distinguished from reading the source proof. The exact interfaces include `ProductZerothFirstParts.Loc.AdmB` and B0–B4, `GaussJetBounds.oneLog`, `IsSys7.caseB`, `IsExpansion`, `valuation_of_entry_bounds`, the local `adm2` period comparison, and `CartierLocalBounds.vLe`/`vGe`. Their declarations and paths are recorded in the paper and manifests. B0–B4 do not by themselves construct the independent global path data. The local lower valuation bound also does not provide controlled nonvanishing: DP24 gives an explicit counterexample. No Lean compilation is claimed by this source comparison.

For **Remark, p.4, steps8–10**, DP7 supplies a higher-height *directional derivative* gain. DP9 refutes its automatic conversion to geometric vanishing: an integral unit already satisfies the local theorem, and multiplication by a scalar changes valuations without changing the generic-fibre divisor. This does not prove that a specially constructed shorter chain is impossible. A claim that one has been constructed requires the actual height-h replacements of the named local inputs and their global rank, level, norm and covolume costs.

The CM height/dimension identities put a further constraint on the proposal. A self-conjugate one-dimensional factor at an unramified CM prime has height2. A factor of height h>2 brings a distinct conjugate factor of dimension h−1; its ambient dimension is at least h. A numerical local gain therefore cannot be treated as free of geometric cost.

The existence of a suitable local CM direction is no longer hypothetical: DP22 constructs one in `Jac(y²=x⁷−1)` over `W(F_11³)`. Its integral factors have heights3 and dimensions2 and1, with slopes2/3 and1/3; the line gives `c3/c2=144/133`. The FGA Picard and Tate formal-group references identify it as an actual integral formal direct factor. This closes the local realization gate, but does not construct its theta kernel or global chain.

Several precise replacement attempts are refuted. DP21 shows that the old scalar logarithm, whose degree-p² coefficient is1/p, cannot be the logarithm of a height≥3 group in an integral unit-normalized coordinate. DP23 shows that adjoining the Cartier dual, taking products, or making an unramified restriction of scalars does not recover the old rank-one alternating blocks. Their Newton slopes remain different from1/2.

DP17 and DP18 determine what can be concluded from the numerical improvement alone. At fixed ramp weights the change is at most `A/(p²−1)` per prime, and the log-p-weighted change is O(A). Thus it does not change an existing leading A log X coefficient. The recovered normalized error allowance is at least `2x/m+4m`, so a bounded coefficient improvement cannot make that unchanged allowance certify a polynomially shorter chain. These are bounds on a certificate and an allowance. They do not bound the actual best gain or actual error of a new construction, nor exclude every finite saving.

## 3. Divided powers and crystals

**DP5** places the result in the distribution algebra of a smooth formal group. Its order-associated graded is the divided-power algebra on its Lie module. The original invariant operators `D^n/n!` are not all integral at finite height; the failure occurs already at order `p^h`. Nor does the original ideal `(t)` admit divided powers. After a ramified contraction with `pi^(p^h−1)=p`, the contracted formal group has an integral logarithm and integral invariant divided powers.

This distinction matters for **cote54, scans3,5–7**, and **cote4, scan3**. The inequality is a statement about an integral operator lattice. A crystal additionally needs the appropriate compatible PD-stratification, or an integrable topologically quasi-nilpotent connection in the setting of **Stacks60.17.4, tag07JH**. Restricted nilpotence of a vector field is not the same assertion as zero p-curvature of a connection.

## 4. Cote54: an old question with a precise classical answer

The box in **cote54, scan7** concerns `t_A^vee`, the additive vector kernel of the universal extension. Its restricted p-operation is zero for every abelian variety, including ordinary ones. It is not the assertion that `Lie(A)` is p-nilpotent. This interpretive correction is DP10; the boxed words themselves should not be changed in the transcription.

The Cartier sequence is `0→A[F]→A[p]→D(B[F])→0`, with `B=A^vee`. **Oda, Corollary5.11, p.131**, canonically identifies the contravariant Dieudonné module of `A[p]` with the filtered Frobenius–Verschiebung module `H^1_dR(A)`. The short Čech calculation in DP10 verifies that its Frobenius is the actual restricted operation on the universal extension. Thus the Hodge restricted-Lie extension is recoverable from `A[p]` over a perfect field. This was already a theorem in1969, independently of RH.

Five mathematical emendation candidates are recorded separately. The complete official cotes47 and54 PDFs were subsequently retrieved and the three target pages visually checked. Four disputed readings are clearly present in the autograph itself; the fifth general exponent remains faint but compatible with the supplied reading. These are not five confirmed transcription errors. Preserve the diplomatic text and add the mathematical corrections as editorial notes. In particular, no Tate twist is inserted into a statement only about the underlying de Rham vector spaces; the twist belongs to the Frobenius or étale realization.

## 5. Cote4 and the SGA/weight setting

The integral base-change sequence in **cote4, scan3, (8.1.1)–(8.1.2)** retains `Tor_1(H_crys^(i+1),k)`. Its derived comparison is classical crystalline cohomology; see **BerthelotV.3.6**, with the historical discussion in **Illusie§3.2 and§4.2(iv)**. The local derivative estimate does not remove that torsion term.

The Frobenius-stable-part arguments in **scans5–6**, local systems in **scans7–10**, and monodromy question in **scan12,8.6** are not solved by DP1. No statement about all later solutions to these historical questions is inferred from this limited scope.

For an abelian scheme, **SGA4 XII5.1–5.2, XV2.1 and XVI2.1** supply smooth proper base change; **SGA5 VI§1.4.2, Definition1.4.3** supplies the rational l-adic coefficient formalism. **WeilI(1.6)** and **WeilII(3.3.9)** give weight1 on fibrewise H1. These facts place the objects in the requested framework, but complex purity does not determine the integral p-adic derivative lattice. No new weight or purity theorem follows from the calculation.

## 6. Cotes16 and47, and H8

For **cote16, scan14,§7**, and run **20261112, H8**, DP15 verifies the exterior divided powers by a subset expansion. The dimension3 test gives the direct Lefschetz block `J−I` with cokernel `Z/2`, so the integral divided powers do not imply integral hard Lefschetz. **H8(iv)**, concerning an integral order/index, is not proved here. No theorem identifies these Lefschetz strings with the theta-lift chain.

For **cote47, scan9**, DP16 computes the coefficients conditional on its displayed total-Chern formula. The three recorded expansions lack a power of chi in the denominator. The final unsigned integrality expression is `(-1)^k chi c_k`, so it may be a deliberately weaker consequence and is not listed as a forced correction. The generating formula in integral Chow or K-theory remains outside what this coefficient check proves.

## 7. Fable suggestion9 and the homotopy side

Under torsion-freeness, identity Frobenius lifts at every prime are equivalent to binomial operations and to the stated special lambda structure. This is an established theorem, with the exact form and its functorial consequences recorded as DP11. DP12 gives a precise integral-calculus bridge: finite differences preserve numerical polynomials, and their degree-associated graded is the divided-power Hopf algebra. Ordinary differentiation fails even on `binom(x,2)`.

**Horel, Theorems3.7 and5.4**, yields the exact positive homotopy statement in DP13: derived cosimplicial binomial cochains recover connected nilpotent spaces of finite type, with the correct derived mapping spaces. **Theorem6.1** gives Z-completion without the nilpotence hypothesis. Neither an ordinary cohomology ring nor an ordinary commutative cochain algebra may silently replace that derived binomial structure.

DP14 refutes the immediate identification of the formal-disc ring with a binomial ring having identity Frobenius. A more elaborate comparison could be a separate research problem, but none is specified or proved by the suggestion. The precise prior-run **B7** comparison was not supplied. A public-source follow-up now locates the binomial polynomials and product/composition formulas in **cote153, PDFp3/archivep2**, and the rational-homotopy, integration-denominator and extra-PD-base discussion in **cote136, PDFpp4–6/archivepp3–5**. On the last page Grothendieck explicitly replaces the inadmissible PD relation sumX_i=1 by sumX_i=t over a coefficient ring with t in its PD ideal. The official catalog dates cote153 from1982, so these four cotes cannot all be called 1976 notes. Only twelve specified pages were read. The particular passage in133 and relevant theorem in137 remain unlocated; no homotopy-to-theta comparison is inferred from historical proximity.

## 8. Dependence on the cited2026 results

As instructed, **Alpöge's RH and Dirichlet-GRH declarations are accepted as cited theorems**. Their Lean compilation is not re-audited here. Every local formal-group, divided-power, Cartier and binomial result proved or used above is independent of those hypotheses. Consequently this report does **not** newly discharge a named conditional theorem in the literature by invoking RH or Dirichlet-GRH.

No Masullo draft, numbered statement, or exact conditional premise appears in the attachments. No result is labelled “conditional on Masullo” without such a statement. The other parallel programme prompts are not treated as secretly completed by the present calculation.


## 9. Further reductions of the higher-height construction gate

**DP25** proves a stronger obstruction in the actual source: its basic CM types are induced from a fixed imaginary quadratic field. Enlarging the ambient CM field preserves slope1/2 at the relevant inert primes. The height3 Jacobian has a different type; at11 the quadratic subfield is split. Even its balanced product cannot satisfy the old equal-dimensional surjective comparison, because the source is ordinary there and the target has slopes1/3 and2/3. A new mixed-type correspondence is required before the old theta-frame input is reached.

**DP26–DP27** separate numerical and geometric shortening. Bare ramps permit an exact finite saving, even with both lift counts even:24 height3 contributions equal26 height2 contributions in the displayed p11 example. The actual Ranks structure requires even m, and literal truncation changes terminal rank, auxiliary signature and period-map domain. Rebracketing composed kernels retains the product of denominator factors and does not create a new less expensive geometric lift. No general impossibility of a new construction follows.

**DP28–DP29** resolve a concrete analytic test of the proposed replacement. The q-typical logarithm and inverse estimates exist, but the original proof's height2 weight quantization does not generalize. A fully admissible scalar correction violates the substituted intermediate LemmaS. Nevertheless a valid final estimate survives, and an explicit nonzero correction realizes the sharp c_h slope.

**DP31** closes this scalar analytic gate over W(k), h>2. Zink's formal biextension injection, together with an explicit reduction-rigidity and unique-splitting argument, forces the correction to be an integral unit. The final factorial-weighted coefficients therefore have the full c_h slope. The theorem uses the slope mismatch between two copies of G_h and its dual; it cannot be applied to the true pair G_h by G_h^D, whose classification target is End(G_h).

**DP30** computes a real limitation in that true dual. Its restricted p-operation is a single nilpotent chain of length h−1, with image dimension h−2. For h>2 some primitive integral dual direction has a unit p-th derivative on an integral coordinate. Thus the line's positive order-p divisibility cannot be assigned to every accompanying dual direction. This does not yet identify a required theta entry or quantify the complete global cost.

At that stage the remaining local gate was the actual dual model and its kernel. DP32–DP34, below, now close the model and directional-bound part of that gate. The prescribed theta/minor/period interfaces and the net geometric cost remain to be supplied.


## 10. The actual dual model and its sharp affine bounds

**DP32** gives an explicit integral model of the actual Cartier dual of the Honda line in every finite height h≥2. This is not an isocrystal-only identification: the proof constructs a finite-free p-series, dualizes its special-fibre Frobenius identity over F_p, and applies the exact integral Lubin–Tate uniqueness theorem after W(F_(p^h)). The transported coordinates are integral and the invariant tangent basis is primitive.

Its h−1 directions have sharp asymptotic slopes **p^i/(p^h−1)**, i=1,…,h−1. The exact q-power coefficient witnesses establish optimality, and the slopes sum to the line's c_h. Thus DP30's unit p-th derivative does not mean that all asymptotic divisibility on the dual vanishes. For the equal list of coordinate directions on the line times its dual, the mean2c_h/h is strictly below c2 at h>2. This is a statement about that weighting, not the source's actual automorphic cost.

**DP33–DP34** remove the digit error for the dual as well. Every direction in the explicit model has the optimal uniform affine error **1**, for every h≥2. The proof uses whole-ring translation operators and integer p-ideal recurrences. A single monomial, with exponents p−1 except p²−1 on the last coordinate, attains the intercept in every direction at n=p^h−1. Mixed exponents add. The ideal containments persist under integral base change, without unjustified rounding in a ramified valuation ring.

This closes the actual-dual existence and directional-asymptotic gates. The later primitive-class and frame-normalization results are recorded next. An ordinary integral section in an algebraic frame does not automatically give the normalized expression used by the source: the exact ExpTie formula includes an explicit exponential gauge.

## 11. The primitive kernel and the exact harmonic transfer

**DP35** proves that a compatible rational splitting with an integral first addition coboundary is integral whenever its denominators are bounded. Any nonintegral splitting therefore has a positive linear denominator rate. An integral unit or an integral multiplier with primitive first homogeneous part cannot clear those denominators. This is a statement about a compatible splitting, not every arbitrary exponential gauge or every selected jet.

**DP36–DP37** now realize a genuine local primitive Poincare kernel satisfying the stated weighted estimate. Tate's exact Hodge–Tate sequence determines the missing torus character, so the true dual action has precisely the exponents required for the weighted quantization. An invariant integral frame and unique invariant rational logarithmic splitting follow. On the specified last-dual path the sufficient residual is rho_h. This is not an upper bound on the best possible geometric gain.

**DP38** replaces an abstract denominator objection with explicit coefficients: +1/p and −1/p in total degree p+1, giving unit mixed derivatives where integral formal functions give p-divisible values. For the invariant normalization, h>2 and odd p, every integral local-unit multiplier still has a unit (p+1)st jet on the specified last-dual logarithmic path. The numerical denominator rate is at least1/(p+1) in the stated group coordinates; no asymptotic assertion for every prescribed algebraic path is inferred.

The actual source expression is P(D)(f exp(k hL))(0). Its conjugated connection is proved integral, and its canonical-gauge independence and J^e ordered-column bounds are supplied theorems, with exact files and declarations in the paper's connection subsection. Thus basic connection/gauge existence is not an unfilled source gate. The J^e theorem controls its stated denominator budget and does not itself add the positive height-h slope.

**DP39** decides both tempting simplifications. Full-series nonintegrality can be entirely invisible to harmonic values. But the source's summed contractions, row invariance, fixed row degrees and integral coefficients also admit a polynomial giving a unit on two copies of the primitive kernel while giving p-divisible values on every integral function. Those conditions alone do not transfer the bare formal-function bound. This does not refute the source's actual theorem or instantiate a new mixed-type global datum.

The remaining positive transfer must use the prescribed mixed-type theta section, its actual connection lattice and corrections, selected polynomial/minor module and geometric path, followed by the new global correspondence and a complete cost comparison. No shorter chain follows from a scalar slope ratio, and no general impossibility of a new chain has been proved.
