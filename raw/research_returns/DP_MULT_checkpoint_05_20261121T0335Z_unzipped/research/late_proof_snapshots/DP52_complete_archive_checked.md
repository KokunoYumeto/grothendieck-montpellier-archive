# DP52 — Shorter endpoint parameters, period construction, and the exact field-type prerequisite

**Author/checker:** GPT-6 Astra Pro. **Reasoning effort:** not exposed. **Date:** 2026-11-21 UTC. This memo concerns the requested lift-count interface. It does not reconsider Alpoge's accepted theorems, and it does not claim a new shorter global proof. All Lean quotations below refer to byte-exact members of the author's original split archive; recovery manifests and source-reading events are separate from mathematical proof checks. No Lean execution is claimed.

## 1. Precise conclusion

The existing endpoint and period framework is uniform in the admissible even integer \(m\). Reducing \(m\) and rebuilding the endpoint does not, by itself, destroy the complex interlacing and noncompact-gap hypotheses or the ability to define the endpoint period. There is one explicit remaining numerical condition in the source's `Hyp3`, namely

\[
             1801\le k+m'-1+t.                         \tag{EP1}
\]

The formal nonzero-period induction also works for every such \(m'\), provided the same six named theta-correspondence statements (`AdmS`) hold for the rebuilt theta family. We give the complete induction below; no unknown minimum number of induction steps occurs in it.

The unchanged column-period wrapper, however, does not accept an arbitrary CM type. Its first field input `Fields.Ok.quad` requires a common quadratic subfield for all selected embeddings. For the genus-three Jacobian \(y^2=x^7-1\), with its actual CM type \(\{1,2,3\}\) on \(\mathbf Q(\zeta_7)\), that common subfield is exactly \(\mathbf Q\). Thus the unchanged construction cannot even form this field certificate, independently of \(m\). This is a direct obstruction in the period constructor's own input, in addition to the previously established `CMObj.typeP/typeM` obstruction.

The sharper positive result is that this quadratic input can be removed from the endpoint-period layer. The actual source goodness proof uses only compatibility with complex conjugation; those weaker assumptions hold for the genus-three type. We explicitly construct its row/point goodness certificates and endpoint period below. What remains is to identify these periods and local theta germs with the prescribed iterated theta image, selected kernel operators and quantitative estimates for one global family.

## 2. Truncation of the exact complex parameter package

### Statement DP52(a)

Let \(D,D'\) be records with the same \(k\), the same set of complex places (identified explicitly), and respectively even chain lengths \(M\) and \(M'\), with \(2\le M'\le M\). Put

\[
 r=k+M-1,\qquad r'=k+M'-1.
\]

This assertion assumes the smaller rank record and its spaces have been rebuilt as in DP44; it does not assert that the old terminal space remains unchanged. Let \(P\) be the source's `TPar D`, whose parameter we denote by \(t=P.t\), to distinguish it from a rank-record field when necessary. Define \(P'\) by retaining \(t,u,v,\eta\) and restricting the arrays \(b,e\) to their first \(M'\) entries. Then:

1. \(P'\) is a `TPar D'`.
2. Interlacing, half-integral/integral parity, and `Centred` pass from \(P\) to \(P'\).
3. For every \(0\le j\le M'\) and complex place \(\tau\),
   \[
   X_{P'}(j,\tau)=X_P(j,\tau),\qquad
   D_{P'}(j,\tau)\subseteq D_P(j,\tau).                \tag{EP2}
   \]
   Here \(X_P,D_P\) denote the source's finite sets `Xpar`, `Dpar`, including their Boolean signs.
4. `NCGaps P` implies `NCGaps P'`.
5. For any theta packages \(X,X'\) on these records,
   \[
   \operatorname{Hyp3}(X,P)\ \text{and}\ (EP1)
       \quad\Longrightarrow\quad \operatorname{Hyp3}(X',P'). \tag{EP3}
   \]
   The numerical requirement (EP1) follows, for example, from
   \[
             r+t\ge1801+(M-M').                       \tag{EP4}
   \]

**Exact source:** `Formalism/LocalRingCardinality/DataTheta.lean`, `TPar` 501–511, `Interlace` 529–533, `block` 535–536, `Dpar` 538–543, `Xpar` 545–548, and `Centred` 550–554. The parity, gap and `Hyp3` definitions are in `Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean` 106–118.

### Proof

The source's `TPar` requires \(t\) odd and \(r+5\le t\), in addition to the listed arrays and the condition \(\eta_\tau\in\{1/2,-1/2\}\). Since \(r'\le r\), every requirement remains valid after the indicated restriction. This proves (1).

Interlacing retains the identical inequalities between adjacent \(u,v\), the identical inequality involving \(b_0\), and only a subset of the old inequalities \(b_j<e_j<b_{j+1}\). Parity merely removes entries from the integral arrays. Every quantified condition in `Centred` either retains \(u,v,t\) or restricts an index of \(b,e\); its block length remains \(t\). All these conditions therefore pass to \(P'\).

For clarity, the finite set `Dpar` before its last translation is the union of

\[
 \{(v_i,\mathrm{true})\}_{i<k-1},
 \quad
 \{(-b_i,\ [i\le j\ \text{or}\ i-j\text{ even}])\}_{i<M},
 \quad
 \bigcup_{i<j}\{(x,\mathrm{true}):x\in\operatorname{block}(-e_i,t)\}.
                                                               \tag{EP5}
\]

The source uses natural subtraction in the parity expression. That does not cause a problem: for every retained pair \(i,j\), both records use the same natural numbers and the same Boolean test. If \(j\le M'\), the first set in (EP5) is unchanged, the second loses precisely the entries with \(i\ge M'\), and the third is unchanged because every \(i<j\) satisfies \(i<M'\). Both sets then receive the same translation by \(\eta_\tau\) when \(j\) is odd. This proves the `Dpar` inclusion, with signs retained. Likewise `Xpar` consists of the unchanged \(u\)-set together with the unchanged blocks of length \(t+1\) indexed by \(i<j\); this gives the equality in (EP2).

The old `NCGaps` says that the distance between any two elements of `Dpar` of different signs exceeds \((r+Mt)^3\). Every pair in the smaller set occurs in the old one. Moreover all quantities are nonnegative and

\[
 r'+M't\le r+Mt,
 \qquad (r'+M't)^3\le(r+Mt)^3.
\]

Thus every required strict gap inequality remains true. Finally, `Hyp3` is exactly the conjunction of this gap condition, interlacing, parity, centredness, the `etaT` infinity-type identity, and \(1801\le r+t\). The infinity-type condition also transports automatically: every source `ThetaX` has `etaT_pos`, requiring its `etaT` infinity type to equal \(1/2\) at each place. Thus the old condition already says \(\eta_\tau=-1/2\), and the new package has the same right-hand side. The other four conditions have just been transported; the numerical condition is precisely (EP1) for the new record. Since \(r'=r-(M-M')\), (EP4) implies (EP1). This proves every assertion. \(\square\)

**Limit.** This is a theorem about rebuilding a shorter record. It does not identify \(Y'_{M'}\) with the old \(Y_{M'}\), nor does it transport an already chosen theta family, lattice, kernel, or cost certificate. In particular, equal `Xpar` sets for retained \(j\) do not imply equality of all indefinite spaces or their periods.

## 3. The finite nonzero-period induction has no additional lower bound on the length

### Statement DP52(b)

For any source record \(D\), theta package \(X:\mathrm{ThetaX}(D)\), and parameter \(P\), the source's six explicit statements `AdmS D X` and `Hyp3 X P` imply its `PointsLemma` conclusion at \(P\). Consequently, whenever a rebuilt shorter package \(X'\) satisfies those same six statements, DP52(a) supplies the full parameter hypothesis apart from the one displayed size condition (EP1), and the same induction gives a nonzero period through \(M'\) downward lifts.

This is a proof of the implication whose *proposition* is named `TowerRallisLemma` in the source. That name at `CayleySignature.lean` 204 is a definition, not by itself an executed proof or a theorem declaration. We prove the implication here directly from the six statements; the source's accepted geometric statements are not being audited.

**Exact inputs:** `CayleySignature.lean`, `PointsLemma` 138–148; `PerNZ` 150–152; `RallisSiegelWeilFormula` 154–161; `LiftParameterConditions` 163–166; `ThetaUnfoldingFreeData` 168–175; `ThetaStablePeriodVanishing` 177–184; `RealThetaLiftDiscreteSeries` 186–194; `RealConstantNonvanishing` 196–199; and `AdmS` 201–202. Additivity, conjugation, group-stability and odd-codimension period identities are fields of `ThetaX` in `DataTheta.lean` 573–694, especially `etaT_pos` 614 and `Bper_odd` 663.

### Proof

Write \(M=D.R.m\ge2\). The first input, `RallisSiegelWeilFormula`, supplies the character sequence \(\mu\), irreducible nonzero representations \(\pi_j\) of the definite groups for all \(0\le j\le M\), their prescribed types, and the assertion that every vector of \(\pi_{j+1}\) is a finite sum of upward theta lifts of vectors of \(\pi_j\), using factorizable finite-type Schwartz data.

At the terminal index \(M\), `LiftParameterConditions` supplies a vector \(\phi_M\in\pi_M\) and a cuspidal vector \(F_M\) of the required discrete-series type such that `PerNZ` holds. At this index it is the top period, rather than a lower Bessel period.

Suppose now that \(j<M\), and that \(\phi_{j+1}\in\pi_{j+1}\), \(F_{j+1}\) have been chosen with the required type, cuspidality and nonzero period. Express \(\phi_{j+1}\) as the finite sum of upward theta lifts given by the first input. Periods are additive in this vector; the conjugation appearing in `bB` is also additive. The nonzero sum therefore has a nonzero summand. Choose its vector \(\phi_j\in\pi_j\) and upward Schwartz datum \(\Phi'_j\). Then the period of the upward lift of \(\phi_j\), paired with \(F_{j+1}\), is nonzero.

`ThetaUnfoldingFreeData` supplies a downward Schwartz datum \(\Phi_j\), factorizable and finite-type, such that the downward lift of \(F_{j+1}\) has nonzero `PerNZ` against \(\phi_j\), as soon as that lift is regarded as a cuspidal vector. Here is why the source's other inputs supply precisely that cuspidality and its type.

Let \(W_{j+1}\) be the complex subspace of the automorphic space consisting of cuspidal vectors \(F\) for which `IsDv` holds, i.e. the conjugate of \(F\) lies in the designated type submodule. It is a complex subspace: `conjAF` is additive and conjugate-linear, and inverse images of complex subspaces under such a map are complex subspaces. It is stable under the finite and real group actions by `RealConstantNonvanishing`, together with the cusp-stability fields of `ThetaX`. The lower-tower vanishings needed by `ThetaStablePeriodVanishing` hold on every vector of this subspace by the second clause of `RealThetaLiftDiscreteSeries`. The vanishing input therefore implies that the downward lift

\[
             F_j=v\theta_j(\Phi_j,F_{j+1})           \tag{EP6}
\]

is cuspidal. Since \(\Phi_j\) is finite-type, the first clause of `RealThetaLiftDiscreteSeries` says that \(F_j\) has `IsDv`. The unfolding input now gives its nonzero period with \(\phi_j\). This completes the induction step.

Descending finitely from \(M\) to \(0\) constructs all the required \(F_j,\Phi_j,\phi_j\). Values outside this finite interval can be extended by zero, as the conclusion constrains only \(j<M\). The character sequence and representation \(\pi_0\) came from the first input, and every stated type and lift identity is preserved during the induction.

At \(j=0\), `PerNZ` cannot be its terminal alternative because \(M\ge2\). Thus there are position and Fourier–Jacobi data with nonzero initial Bessel period. The rank difference is

\[
 \operatorname{rank}Y_0-\operatorname{rank}X_0
       =(k+M-1)-k=M-1,
\]

which is odd because \(M\) is even. The `ThetaX.Bper_odd` identity consequently replaces the Fourier–Jacobi datum by zero without changing the value. This is exactly the zero-datum nonvanishing required by `PointsLemma`. \(\square\)

### What has and has not been constructed

The proof constructs the finite chain and its nonzero period from *all six specified theta identities*. It does not infer these identities from a formal-group height, a local theta germ, or a generic nonzero bilinear form. For the new mixed CM type, a concrete geometric \(X'\) with these identities remains required. The induction itself imposes no further minimum \(M'\), and its nonvanishing conclusion does not by itself imply the quantitative global inequality needed in the main argument.

There is also an abstract source realization for every `D7`: `ThetaFamilyAdmissibleThree.lean` constructs `thetaG` (71–153), proves its six statements (215–274), and concludes `thetaG_exists` (277–280). Its automorphic spaces are a common auxiliary Hilbert space, its group actions are identity, and its periods are inner products. It is a genuine realization of the stated abstract interface; it does not identify that realization with the mixed-type algebraic theta germs or with the required local kernels. We do not use it as such an identification.

## 4. The actual endpoint period map is uniform in ranks

### Statement DP52(c)

The construction `Formalism.L2.Col.periodC` and the resulting `recPer` accept arbitrary `Ranks R`. Their endpoint dimension is \(N_R(m)-1\). Given their listed field, weight, level, and row-space inputs at a smaller rank record, they define the rebuilt endpoint period without a new \(m\)-specific existence assumption. The inner-product formula is a proved theorem for those inputs. This statement concerns construction of the map; it does not assert that its restriction to a specified theta-lift image is nonzero.

**Exact source locators:**

- `Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`: `Wts` 443–449; `Wts.Ok` 455–460; the endpoint weights `sgW`, `sgTrue` 472–476.
- `Formalism/LocalToGlobal/Columns/Record.lean`: generic parameters and `rowGSD`, `ptGSD` 1434–1442; `ptOk` 1444–1448; `lowC` 1558–1560 and `lowC_ev` 1562–1564; `periodC` 1568–1571; `jMC` 1575–1578; `periodC_eq_ipCl` 1580–1590; `recPer` 1603–1610.
- `Formalism/LocalToGlobal/Columns/RecordInst.lean`: `ptEv_gram_unit` 47–58 and `periodC_eq_ipCl'` 60–64.

### Construction and verification

Fix the source field package \(X\), its good-field proof \(h_X:X.\mathrm{Ok}\), a rank record \(R\), weight data \(W\), endpoint level \(\Lambda_M\), and the specified proof that the endpoint row datum is good. The row invariant space has a chosen basis \(\{h_a\}\). For each point-class representative \(c\), pairing against \(h_a(c)\) gives a scalar-valued linear functional on the endpoint coefficient representation. The source's evaluation map has linearly independent images of its basis (`GSD.Ev.li`); `extend` extends any such functional to its ambient complex function space and `extend_ev` proves agreement on evaluated coefficient vectors (`Record.lean` 154–205).

`periodC` is then the finite class sum of these extended functionals, paired with the coordinates of a row vector and weighted by the reciprocals of finite stabilizer orders. The positive Gram matrix of the endpoint coefficient representation is invertible; this is the theorem `ptEv_gram_unit`. Consequently each extended functional is represented by a vector for the classwise inner product, and `periodC_eq_ipCl'` identifies the entire period with the corresponding classwise inner product against `jMCL`.

Finally, `recPer` combines this period with evaluation at the terminal classes and the branching map `lowC` from dimension \(N_R(m)\) to dimension \(N_R(m)-1\). Each definition is parameterized by \(R\), rather than a fixed numerical value of \(m\). Replacing \(R\) by the rebuilt \(R'\) and supplying those same kinds of data produces the required map at \(N_{R'}(m')-1\), with the same proved inner-product identity. This verifies the assertion. \(\square\)

### Minimal weakening of this endpoint construction

The preceding package obstruction is not intrinsic to the linear-algebra period map. Inspection of the definition at `Record.lean` 1568–1571 shows that `hX : X.Ok` is used there only through `ptOk W ΛM hX`. Therefore one can define the same map directly from

\[
 h_{\mathrm{pt}}:(\mathrm{ptGSD}\,W\,\Lambda_M).\mathrm{Ok},
 \qquad
 h_{\mathrm{row}}:(\mathrm{rowGSD}\,W\,\Lambda_M).\mathrm{Ok}.
                                                               \tag{EP9}
\]

Replace `ptOk W ΛM hX` in that displayed definition by \(h_{\mathrm{pt}}\), leaving its classwise functionals and its row basis unchanged. The proof of `periodC_eq_ipCl` is then the same finite class-sum identity. Its Gram invertibility input is still available: `ptEv_gram_unit` in `RecordInst.lean` 47–58 has **no** `X.Ok` argument. This gives an explicit weakened endpoint-period constructor and its inner-product formula, without assuming `Fields.Ok.quad`.

### The goodness certificates are constructible for the actual mixed type

There is no need to leave (EP9) as an unspecified hypothesis. The full proof of `formGSD_ok` in `Columns/ColFormsLemmas.lean` 83–119 uses exactly the following two field properties:

\[
\begin{aligned}
 &\phi(\bar x)=\overline{\phi(x)}
       &&(\phi:E\hookrightarrow\mathbf C),\\
 &\sigma_0(\bar y)=\overline{\sigma_0(y)}
       &&(y\in K)
\end{aligned}                                                   \tag{EP10}
\]

for one coefficient-field embedding \(\sigma_0\), together with the explicitly supplied coefficient equivariance `C.Eqv`. For the row and point coefficient data, equivariance in turn uses only

\[
       \operatorname{emb}_\tau(\bar x)
          =\overline{\operatorname{emb}_\tau(x)}.        \tag{EP11}
\]

Here are all five components of the weakened goodness proof.

1. The first identity in (EP10) makes the standard hermitian form positive at every infinite place. The theorem `DecoSet.finite_reps`, invoked in the source at 85, gives finitely many representatives of the decorated lattice orbits. Each orbit for the subgroup `FormG` is represented by one of them: the representative move is an isometry paired with the identity level element, so it already lies in `FormG`. This proves `fin_orb` exactly as in 84–93.
2. The theorem `DecoSet.finite_stabilizer`, invoked at 96 with the same positivity hypothesis, gives finite decorated-lattice stabilizers. The inclusion `FormG.incl` is injective, so its stabilizers are finite as well (94–101).
3. Any value of the finite level character is a root of unity, as `LevFam.chr_root` proves at 77–81. Multiplication by such a scalar preserves an integral lattice: the scalar and its inverse are algebraic integers. Combining this fact with the two lattice-equivariance identities in `C.Eqv` proves `nab_smul` and `del_smul` (102–109).
4. The second identity in (EP10) shows that a root of unity \(c\) has \(\bar c c=1\): after the injection \(\sigma_0\), its complex norm is one. The invariant hermitian pairing of `C.Eqv` is therefore still invariant after the finite-character scalar twist. This is the final `inv` field, at 110–119.
5. No other field of `X.Ok` occurs in this construction. Thus these steps prove the same goodness conclusion directly from (EP10) and `C.Eqv`, without assembling a false `X.Ok` record.

For the point datum, `Record.ptOk` 1444–1448 supplies `C.Eqv` using the round coefficient lattice identities and `roundPk_inv`, whose only field input there is `emb_star`. For the row datum, `RowFormsLemmas.rowVal_eqv` 20–23 uses the row lattice identities and `squarePk_inv` with exactly the same `emb_star` input. Consequently (EP10)–(EP11) construct both certificates in (EP9).

Now take \(E=K=\mathbf Q(\zeta_7)\), \(F=E^+\), conjugation \(\zeta_7\mapsto\zeta_7^{-1}\), and the selected embeddings \(\sigma_1,\sigma_2,\sigma_3\). Complex conjugation is canonical on this CM field, and its Galois group is abelian, so (EP10) and (EP11) hold. For every admissible rank record, every specified dominant weight package and endpoint level, the preceding construction therefore supplies the actual row and point finite-class goodness data. The weakened `periodC` construction then supplies their endpoint period and its inner-product identity. This is an explicit mixed-type endpoint-period construction, rather than an assumption that the failed `quad` field somehow holds.

The full original `recPer` is attached to `recChain hX ...`, and a new global construction must still rebuild the relevant class kernels and their compatibility with its theta correspondence. The result just proved does not claim that the endpoint period is nonzero on a prescribed iterated lift image, or that the required level, lattice and quantitative bounds remain unchanged. It proves that the common-subfield mismatch is removable from this entire row/point period-map layer.

The simpler `NZColC.periodN` at 160–167 accepts an arbitrary bilinear form `per` on the terminal class-function space and inserts identity evaluation/lowering maps. `NZRowE.hostLevelRecord` uses this package. Its existence should therefore not be confused with a theorem identifying an actual geometric period: that identification, its nonzero restriction, and its quantitative bounds are additional inputs.

For comparison, the source does prove nontriviality of the initial ramified column lattice uniformly in \(R\): `Columns/NonDeg.lean`, `MramL_ne_bot` 522–525 and `finrank_MramV_pos_of_sizes` 900–902. The displayed size input there is \(2f k<g_0-1\), which is unchanged when only \(m\) decreases. This is useful initial nontriviality; it is not a statement that every chain of kernels has a nonzero terminal period.

## 5. Exact common-subfield obstruction for the actual genus-three CM type

### Statement DP52(d)

Let \(E=\mathbf Q(\zeta_7)\), let \(F=E^+\), and let a coefficient field contain \(E\) via an injection \(\iota\). Use the actual Jacobian CM type

\[
       \Phi=\{\iota\sigma_1,\iota\sigma_2,\iota\sigma_3\},
       \qquad \sigma_a(\zeta_7)=\zeta_7^a.
\]

The common subfield specified by `Fields.Kq` is

\[
 E_\Phi=\{z\in E:\sigma_1(z)=\sigma_2(z)=\sigma_3(z)\}
             =\mathbf Q.                              \tag{EP7}
\]

It therefore cannot satisfy the source field input

\[
           [\mathrm{Fields.Kq}:\mathbf Q]=2.            \tag{EP8}
\]

The same conclusion holds after simultaneously composing the type with an embedding or field automorphism, taking its conjugate type, or enlarging the coefficient field through an injective embedding. It is independent of the chain length.

**Exact source:** `Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`, `Fields.Kq` 59–78, especially its carrier at 60; `Fields.Ok` 80–108, especially `quad` at **108**. The weaker-looking `Fields.Core` also retains `quad` (the same file, 144–157). The assumptions `hX : X.Ok` appear explicitly in `Record.periodC` 1568 and `recPer` 1603. DP22 and DP49 establish the actual Jacobian character type \(\{1,2,3\}\).

### Proof

The group \((\mathbf Z/7\mathbf Z)^\times\) has order six. The successive powers of \(3\) are

\[
              3,2,6,4,5,1\pmod7,
\]

so \(\sigma_3\) generates \(\operatorname{Gal}(E/\mathbf Q)\). If \(z\in E_\Phi\), comparison of the embeddings with labels \(1\) and \(3\), followed by cancellation of the coefficient-field injection, gives \(z=\sigma_3(z)\). It follows that every element of the Galois group fixes \(z\), hence \(z\in\mathbf Q\). Conversely every rational element is fixed by all embeddings, proving (EP7). Its rational degree is one, contradicting (EP8).

An injective enlargement of the coefficient field leaves every equality between these embeddings unchanged. Simultaneously composing all embeddings by an injective map likewise preserves equality. Applying an automorphism to the type replaces the subgroup of relative automorphisms by a conjugate; here the group is abelian, and in any event the fixed field remains \(\mathbf Q\). Complex conjugation is one such automorphism. No chain parameter occurs in this argument. \(\square\)

### Why this is exactly a type condition

More generally, let \(E/\mathbf Q\) be a Galois CM field of degree \(2g\), with CM type \(\Phi\) of size \(g\). Its common subfield \(L\) is defined by equality of all selected embeddings. If \([L:\mathbf Q]=2\), all \(g\) selected embeddings restrict to the same embedding of \(L\). There are exactly \([E:L]=g\) extensions of that embedding to \(E\), so the selected embeddings are *all* of those extensions. Moreover \(L\) must be imaginary quadratic: if it were real, every conjugate of a selected embedding would have the same restriction, giving \(2g\) distinct extensions of one embedding of a degree-two subfield, which is impossible. Thus `quad` forces the type to be induced from one embedding of an imaginary quadratic field. Conversely such an induced type has that imaginary quadratic field as its common subfield: the relative automorphisms between its embeddings fill \(\operatorname{Gal}(E/L)\), whose fixed field is \(L\).

For \(E=\mathbf Q(\zeta_7)\), the different type \(\{1,2,4\}\) does have common field \(\mathbf Q(\sqrt{-7})\): its relative automorphisms form the order-three subgroup. Explicitly, \(z=\zeta_7+\zeta_7^2+\zeta_7^4\) is fixed by that subgroup, satisfies \(\bar z=-1-z\) and \(z\bar z=2\), hence \(z^2+z+2=0\). Its degree-two field is therefore \(\mathbf Q(\sqrt{-7})\), the subgroup's full fixed field. That replacement changes the CM type of the abelian input. It is not a relabeling of the Jacobian type \(\{1,2,3\}\), and it cannot be used to transport the actual mixed-height local calculations while leaving the global field package unchanged.

## 6. Exact remaining boundary

DP44 plus DP52(a) removes a possible rank/parameter objection to a smaller even \(m'\), subject to the explicit residual bound (EP1). DP52(b) removes an additional formal-induction objection once the six theta identities have been supplied at the rebuilt endpoint. DP52(c), including its weakened goodness proof, constructs the actual mixed-type endpoint row/point spaces and period map uniformly in \(m'\). DP52(d) identifies why the unchanged global field record still cannot be used verbatim; it is not an intrinsic obstruction to the endpoint period just constructed.

Accordingly, a precise next construction problem is:

> Replace the quadratic-induced field/type package by a mixed-type package containing the actual CM embeddings; construct its weights, row/column spaces and theta family; identify the algebraic theta germs with the selected kernel/period operators; and prove the six `AdmS` identities and the selected local/global quantitative conditions for that same family.

The first failed field in the unchanged wrapper is `Fields.Ok.quad`, and the explicit weakened construction above bypasses it at the endpoint period-map layer. The remaining meaningful global input is the identification with the intended iterated theta image and its selected local/global certificates, not mere existence of an endpoint period or an unknown minimum induction length. It also gives no upper bound on the true selected gains and no claim that every shorter chain is impossible. The numerical global deficit from DP44 must still be evaluated on the actual rebuilt family; ordinary-path rates or equal-direction averages cannot be substituted for that calculation.

## 7. Source provenance and check status

Original archive URL pattern: `https://alpo.ge/lean.tar.gz.partNN`, parts 01–14. Each recovered module was read directly from its `lean/src/...` archive member. The manifests `endpoint_period_source_scan.json` and `endpoint_period_sources_pass2.json` through `endpoint_period_sources_pass9.json` preserve member names, byte counts, SHA256, extraction times and whether a file was new. Some modules were recovered only because a declaration-name search matched; such recovery does not constitute a source read or a proof check. The consolidated manifest and the separate actual source/proof events accompany this memo. Later targeted recovery manifests continue the same numbered series.
