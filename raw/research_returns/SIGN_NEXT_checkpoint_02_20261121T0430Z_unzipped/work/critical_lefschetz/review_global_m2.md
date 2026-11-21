# Independent review: actual global (m=2) specialization

Reviewer: GPT-6 Astra Pro, effort not exposed, `/root/critical_lefschetz`.
Review date: 2026-11-21. This report records human source and proof checks; it does not claim a Lean build.

## SF-Q6-01: numerical `numBig` is not an actual global record

**Verdict: approved.** The complete proof in `../singular_fibres/arithmetic_review/no_global_numBig.tex` was read and independently reconstructed, including its final wording that `Delta` and `h0` are nonnegative integers. Checked SHA256: `ba1975eb5fdad5f4f97f4ed1851fb60906907ea1278f0f92e79244270525da21`.

The relevant source definitions give `R0.k=8`, `R0.m=2`, `R0.t=15`, `R0.r=9`, `R0.f=8`. The numerical `hostEx` has `q=11`, `d=7`; both `numEx` and `numBig` use this host, and `numBig` copies the ranks of `numEx`. In contrast, an actual `D7` has `D.host : Host D.R`; `Host.qd_big` requires both `4*R.t*R.r+1<q` and the analogous inequality with `d`. Thus the claimed equality of ranks and host would give (541<11) and (541<7), each impossible. The source definition `ofRecord` copies `D.R` and `D.host.toHostAx`, so altering size, `Delta`, or `h0` cannot affect this contradiction.

I also checked the constructive scope paragraph: `Examples₂.H0` in `ExampleLayerExistsGenerators.lean` is a full `Host R0`, has `(q,d)=(571,599)`, and explicitly provides the required inequalities. This repairs the host obstruction only; the paper correctly does not assert that it constructs a composed nonzero theta period or full divisibility input.

Source checks used the supplied archive copies of `DataHost.lean`, `RhoDetPrimeEqMuTildeMulChiPow.lean` (the `D7` definition), `NumbersLemmas.lean`, `NumbersLink.lean`, `ExampleRanksRankComplement.lean`, and `ExampleLayerExistsGenerators.lean`. The proof's exact locators are accurate. No substantive fault remains.

## Actual two-step theta-chain bridge: interim source findings

The complete proof of `FamilyLinkOnto.linkOnto_of_ontoAll` was read. It has no hypothesis `1 ≤ rS`. Its only use of the length is the equation (2n+2=m); for (m=2), (n=0). Its `Reach` witness consists of `reach_dn` at stage one (one actual `stepY`) followed by `stepX` at stage zero. `PkHyp W`, `FamCh.RowOK`, and `OntoAll D` supply the actual Weil data, validity statements, and surjectivity. Therefore it is incorrect to say that this theorem itself excludes the two-step case.

`OntoAll D` has `NodeGap D` as an antecedent. The theorem feeds it `PkHyp.gap`. The source theorem `ontoAll_of_classicalTheorems_and_hecke` constructs `OntoAll` from eleven named published theorem propositions, with no separate `rS≥1` gate. This is a theorem about a supplied valid global datum; it does not construct that datum or its coefficient and size records.

The complete `TrueGeometryFamilyRowData.famAllQ_of_allTrue` proof places `1≤rS` precisely in its initial call to `exists_central_bottom_datum`. That lemma constructs one central pin shared by all words and families. Its proof invokes `matching_translates_bottom` and `placed_bessel_compatibility`, both with this hypothesis. The remaining geometric family, row, column, `LinkDown`, and `LinkOnto` calls do not use it directly. Consequently the supplied uniform star-product route cannot simply be applied at `R0.rS=0`; this observation does not by itself rule out an ordinary nonzero period for one fixed word.

The complete `RelOfLinks.rel_of_links` proof and `JointOfFamilyAndService.joint_of_famAllQ` proof were also read. `LinkOnto` is used to lift an already specified bottom vector (T) to a top vector (G_0); it does not prove that any bottom period functional is nonzero. The complete `JointStarProductNonvanishing` proof separately uses `PuNZ`, a nonzero bottom anchor, and the common pin to construct the nonzero terminal functional. Thus replacing these hypotheses by surjectivity alone would be an unsupported inference.

Further single-family bridge tracing is in progress; the preceding source-scope statements are established, not a proof of general impossibility.

## SF-Q6-02: genuine rational jets and the displayed size obstruction

**Verdict: approved.** I read the entire `actual_m2_jets_scope.tex` proof and scope discussion, checked the complete `ExistsHypJetsAll.lean`, `ExistsNatBoundPre.lean`, `HarishChandraParameterFormula.lean`, `JetsInIffStepField.lean`, and `DegreeEqTotDeg.lean` files, and checked the relevant `HostFam`, `DataParams₂`, `D7.eTau`, `tau1P`, and `ThDistC` definitions. Checked contribution SHA256: `758fc0213eeeeb0ff050b7e04b099bf763ecabbe7cd137bc1e026f29b81a3ded`.

The parameter calculation is correct. `Rt 0` gives `(k,m,t,f)=(8,2,15,8)` and `N_i=8+16i`. The selected all-true word gives `v=(24,20,16,12,8,4,0)`, `u=(49,45,37,29,21,13,5,-1)/2`, `b=(1,37)`, and `e=(19,55)`. Restriction to the selected word uses `Word := Unit` and changes `duStar` and `Dstar`, preserving the host, weights, and the nonempty top set. These equalities describe the witness selected in this proof; they are not universal assertions about every witness of the existential theorem. The contribution states this distinction explicitly.

For the obstruction itself, choose a top index `t` and set `tau = D.eTau.symm (tau1P D.R.toFrame t)`. The `top_u` equality applies because `eTau` is an equivalence and `tau1P` has underlying group coordinate `R.tau1 t`. With `k=8` and final coordinate `-1/2`, the second equality gives `-1/2=-bT(t)-7/2`, hence `bT(t)=-3`. But `bT_ge` implies `bT(t)≥sc.b'`; `x>1` and positivity of both real exponentials imply `sc.b'>0`. This is a strict contradiction. It is independent of all unexamined gain and error fields.

The coefficient rationality statement is also accurately scoped. `jetC` is the product of the prescribed `cD` powers with an ordinary iterated derivative, without factorial division. `JetsIn` gives algebraicity only in the used multidegrees, with the `chiF` normalization. `JetEx.exists_replace` replaces the ambient datum by `amb0` and resets the two index exponents to `m`; it preserves `C`, `S`, and the range of `xi`, as claimed. Finite generation and coefficient-field enlargement supply the rational jets. This is stronger than an arbitrarily assigned coefficient table but is neither an all-degree `Amb.JetsRat` claim nor a full `SizeData₂` construction.

I did not independently re-prove every deeper imported arithmetic or theta theorem, and did not run Lean. The source-level constructor and obstruction checks support the exact claim made in SF-Q6-02. No substantive correction is needed.

## SF-Q6-03: the asymptotic rank constructor excludes the fixed ranks

**Verdict: approved.** I read the complete asymptotic_rank_scope.tex proof, the defining RankVal clauses and integer-valued TOv,nWv, the full NodeGap.le_m proof, the full exists_sizeData_explicit constructor, and the relevant SizeParametersNonempty construction. Checked contribution SHA256: ba2d7fddcc839a0b33b6e910326779fb53b47c16d9720d68770b108d1e48096d.

Independently, the rank equality gives \(r+t=8fr+4+\mathrm{TOv}(s)\mathrm{nWv}(R,s)\). The last product is a nonnegative integer. Substitution of \((r,t,f)=(9,15,8)\) gives \(24\ge580\), impossible. For arbitrary \(m=2\), the rank lower bound gives \(x^{(1-\varepsilon/8)/2}\le2\). Since \(x>1\) and \(0<\varepsilon<1/52\), its left side is at least \(x^{1/4}\); hence \(x\ge81\) is impossible. This reproduces the cited NodeGap.le_m implication with \(M=3\). The source's exact constructor and Ctx.ok.rank calls justify the stated scope. The abstract SizeData₂ record does not include RankVal; the contribution correctly does not generalize this obstruction to all direct size constructions.

## A single-family route without a common central pin

There is a precise, useful source-level refinement of the earlier gate analysis. Retain every base, TC, size, extra, and RealPack hypothesis in famAllQ_of_allTrue, and its named published theorem assumptions, AllTrue W, and OntoAll D, but omit 1≤rS. For each fixed word \(u\), the same proof constructs \(f,d\) with f.RowOK, LawsX f.t, LinkZero f d, LinkTail f, LinkDown f, LinkOnto f, LinkComm f, and RatioQ f. No claim of d.Pin z for a common central \(z\) is made.

To check this assertion, follow all_true_family_datum, exists_consistent_row_choices, true_geometry_family_invariance, and true_geometry_family_column_data exactly as in that proof. Set f := a.fam row col and **take d := a.d**, instead of calling the common-pin theorem. GeoAll.Is.bot in IsStdFr.lean supplies both
\[
 \forall h_0,\quad a.d.B.lev=f.c.B\,0\,rS\,h_0,
 \qquad a.d.b=f.g.b\,0.
\]
These are exactly the two extra hypotheses of linkZero_of_chartZero. The other four links and the ratio statement are already returned or obtained by the same unmodified calls. The only discarded construction is the common Pin. This derivation was independently checked against the complete displayed proofs and exact GeoAll.Is.bot definition; it is a human derivation from supplied source theorems, not a newly compiled Lean theorem.

With such a family at \(m=2\), a separately supplied nonzero bottom value \(d.\mathrm{per}(\phi,T;y,v)\), \(T\in\mathrm{ThetaLiftSpaceZero}\), yields a nonzero **complex terminal tail value** as follows. LinkOnto lifts \(T\) to \(G\). Apply MainX with \(n=0\), singleton index set, base family member, and coefficient one. If the terminal tail on up 1 (col0 phi) vanished, MainX and LinkZero would force \(c_{\rm Bot}\,d.\mathrm{per}(\phi,T;y,v)=0\). Each factor defining \(c_{\rm Bot}\) is nonzero by LawsX.tup, so this contradicts the assumed bottom value. LinkComm then transfers nonvanishing to the composed column operator, because its scalar is nonzero and its source change is an invertible linear map. This establishes the conditional complex tail implication. To obtain a number-field input and the specified perCol on coefficient coordinates, one must also verify the rational spanning/base-change and topOf identifications; these are not supplied merely by LinkOnto.

### The proposed finite-support bottom anchor

For freely chosen compatible neat levels on a totally definite \(G/H\) pair, identity-supported modular forms and a nonzero branching functional can indeed produce a nonzero finite period; its exact value depends on the fixed Haar and stabilizer normalization. This observation does **not** by itself construct the source's anchor. Here D.eMu identifies the allowed column space with
\[
 M_{\rm ram}=M_0\cap\bigcap_v\ker N_v,\qquad
 N_v=\sum_{c\in\mathbf F_v^\times}\rho_T(v,c),
\]
as defined in DataKernels.lean. ScaledRamifiedLattice.lean identifies these with the actual diamond norm kernels. An identity-supported vector on a free diamond orbit has a nonzero orbit sum and therefore does not itself lie in this intersection. One may form differences or apply a rational projection onto the norm kernels, but must then prove that the desired bottom period survives the prescribed row level rJ, its character, the Bessel embedding, and the translate d.b. Refining levels also requires rebuilding the corresponding actual family and its validity hypotheses.

The other remaining distinction is scalar field: FamilyLinkOnto is a complex-linear surjectivity statement. A rational matrix whose complexification is surjective is already surjective over its number field, but using that fact here requires the actual rational-form/base-change identification. Clearing denominators may then give integral inputs with nonzero output; it does not preserve a unit output. These are concrete compatibility gates, not a proof that all two-step global periods vanish.

## SF-Q6-04: actual stabilizer support and conditional full local bound

**Approved.** Complete proof read at SHA256 `aaa5a1cad63f883c4e7121b3ae3c560ddea839fca4c16cd38e45730191060c10`. Independently, an order-p element of a finite subgroup of GL_n(E) has a nontrivial primitive p-th eigenvalue, so restriction of scalars gives p-1≤[E:Q]n. The actual finite LCM defining DGam therefore has prime support at most [E:Q]N_m+1=641. The proof uses the actual source autOrd/gamRanks/DGam and rank bounds, not an arbitrarily selected stabilizer constant.

The complete displayed F and E branches give, under the stated actual FDef/EDef/ParametersFill hypotheses, sg=(96M+3456)/(p²-1)-76800 log_p(a). I independently checked the sum of all e-values, the two error contributions, the ramification exclusion and the positive numerical lower bound at p=863. Exact rational arithmetic verifies the lower-bound floor 5676959810847744. This is a conditional local calculation, not an actual complete global row record. In particular the illustrative constant consecutive b-gap 36 fails the separate NodeGap condition: its least permissible N is 40 and its required gap is 128016. The local computation does not use NodeGap and remains valid as stated.

## SF-Q6-07: constant untwisted completion cannot supply the positive gain

**Approved.** Complete proof read at SHA256 `b4e7c6c4dac8a9b527c1dbb486314e8050ce6a5bdc173dad7ce283b3e4c969b7`. The model and assembly preserve muAt=Cmu everywhere, so the SizeData untwisted clause forces every indicated F-value to be zero. At the specified inert hP0 place, FDef gives the strictly positive number (k-1) times the positive sum of e-values divided by p²-1. The two conclusions contradict each other. The exact model, assembly, untwisted and FDef source clauses were checked. This excludes the named constant-twist completion only; an actual finite-prime twist governed by MuIs.on is not excluded.

## Final SF-Q6-05/06 proof scope

The complete SF-Q6-05 proof was reread after the root's layout-only gathered-display change. Its current SHA256 is `456d5da169cdf36ee14ef285926032f818822179b6777636a176b801d94248f8`. The complete SF-Q6-06 proof and the final ambient-signature correction have been read; current SHA256 is `6258ac6323d211108c38e28208bf9c22851db267fae0751aa583732aa1431887`.

SF-Q6-06(c) assumes compact real groups. The actual m=2 Hida ambient is U(k,1), not compact: the supplied card_epsS_false computation gives rS+1 negative directions. Thus the refined-level compact-group interpolation theorem does not directly provide the actual bottom anchor, even before the independent fixed-K2 restriction. Parts (a) and (b), the finite Fourier criterion and exact translated-period identity, retain their stated actual scope. An actual analytic Poincare nonvanishing argument is still required.

## SF-Q6-08: pointwise inert valuation theorem

**Approved after full proof and exact source comparison.** Checked SHA256 `57bb57abe360a54a5a6e31e0864ac492017331dc2bbf89e705c6ae37c5069de9`. I read the whole contribution, the complete one-letter bound wrapper and thmOne_of proof, the exact Loc1 assumptions, the orbit-sum definitions and entC_of proof, KForm, the composition and terminal-pairing proofs, and the entire fixed-prime adapted-kernel proof. These checks confirm that rankA is unused in this branch and that the split-bound premise there is used to obtain p≥5, which the pointwise statement supplies directly. The theta expansion, actual KForm, twist preservation and PairInt remain genuine hypotheses.

The first KForm step loses zero DGam valuation at sp=1; the remaining m-1 steps lose one each; period_ge loses one further copy. This gives exactly m*d_w, with v_w/e_w on the left. The zero-output case is retained. The coefficient field and actual terminal period identification come from PairInt and the source perCol ties, not from a generic local matrix.

I independently substituted srcPar and nuRow using rational arithmetic, obtaining both displayed partitions and sizes. Their nonnegativity and monotonicity hold for M≥0,G≥16. The total numerator is 128M+192G-208 and the rank error coefficient is 9216. The difference R_G-sg_G has exactly the stated positive coefficients; G≥16 already makes its rational numerator nonnegative, and log_p(a)≥1 makes the error difference positive. The proposed G=10^9 satisfies the exact existential NodeGap with N=40. The numerical assertions remain conditional on all stated actual arithmetic and global input ties, and the theorem asserts divisibility including zero, not nonvanishing. No Lean compilation or reproof of every imported analytic prerequisite is claimed.
