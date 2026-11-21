# DP44 — smaller rank records, generic spaces, and the exact remaining lift comparison

Date of this pass: 2026-11-21 UTC. Researcher: GPT-6 Astra Pro; effort is not exposed. This is a source-application and mathematical comparison memo, not a Lean execution or an audit of Alpoge's accepted theorems. Alpoge's theorems are accepted as stated. This memo distinguishes definitions, supplied constructors, and quantitative hypotheses. Original-author archive provenance for the newly recovered modules is recorded in `dp44_added_sources.json`.

## 1. Result and scope

The conditions in the recovered `Ranks`, `HCParam`, `Host`, and `Spaces` interfaces do **not** force the chosen lift count beyond the universal lower bound two and the stated upper constraints. At the same frame and the same $k,t$, every smaller even value $2\le M'\le M$ gives valid rank and Harish–Chandra parameter records; the old host transports, and the actual generic source constructor builds the required new Hermitian spaces from the same norm element.

This is a reconstruction of the numerical and Hermitian-space inputs, not literal truncation with the same endpoint. The new terminal positive rank is $k+M'(t+1)$, the auxiliary signatures change, and the period field in the nonzero-row constructor has a different domain. Neither this reconstruction nor the local higher-height theorems supply a comparison of the full selected determinant gains and costs of two complete global families.

The distinction refines DP25 and DP27. DP25 excludes a height-greater-than-two substitution inside the old induced CM type. DP27 excludes stopping the old chain early while retaining its old endpoint data. Neither result proves that every other chain with a smaller even count is impossible.

## 2. DP44(a): restriction of the rank and HC records

Let $R$ be a source `Ranks` record, write $M=R.m$, and let $M'$ be even with $2\le M'\le M$. Keep `R.toFrame`, $k$, and $t$, and replace $M$ by $M'$. Then the resulting data satisfy all the `Ranks` requirements. Every `HCParam R` restricts to an `HCParam R'` by keeping $u,v$ and restricting $b,e$ to the first $M'$ indices.

**Proof.** The parity conditions on $k,t$ are unchanged and the new parity condition on $M'$ is assumed. The inequalities

\[
M'+3\le k,\qquad k+M'-1+5\le t,\qquad 3M'<t,\qquad M'\le2\operatorname{ord}
\]

follow respectively from the old inequalities and $M'\le M$. The frame and the condition $2\operatorname{ord}\le k$ are unchanged. For the only apparently nonlinear condition, $3M<t$ gives $M'\le t+1$, so

\[
(M')^2\le M'(t+1)\le k+M'(t+1).
\]

This proves every field of `Ranks`.

For `HCParam`, the two interlacing conditions on $u,v$ are unchanged. The inequality involving the final $u$ and the first $b$ is unchanged because $M'\ge2$. Each $e_j-b_j\ge(t+3)/2$ is an old inequality. Each retained adjacent inequality $b_{j+1}-e_j\ge(t+3)/2$ is also an old inequality because $j+1<M'\le M$. All integrality and half-integrality conditions restrict. This proves the assertion. \(\square\)

The same construction works pointwise for the source's word-indexed families of HC parameters. Conditions fixing $v$, the first and last entries of $u$, the common $b,e$, and the prescribed interior relations between $u,v$ remain true after restriction; the interior entries of $u$ may vary across words. No claim is made that a terminal representation at $M$ equals one at $M'$.

**Exact source locators.** `Formalism/LocalRingCardinality/Params.lean`: `Ranks` 6–22, derived ranks and signatures 28–46, `HCParam` 50–69. The word-family conditions used by the generic nonzero-row constructor appear in `SpanPowerMembership/NZRowAsm.lean` 15–29.

## 3. DP44(b): host transport and an actual generic Spaces constructor

Let $H:\mathrm{Host}(R)$. With the same frame and $k,t$, the record in part (a) admits the same host fields, with only the proof of `qd_big` replaced by its weaker inequality. If the old data include a prime $T$ and an element $z\in H.E$ with $z\overline z=T$, the source's `hostSpacesOfNorm` constructs `Spaces R' H.F H.E` from the same $T,z$.

**Proof.** Inspection of the entire `Host` structure shows that its only dependence on the changing $m$, apart from the common frame, is

\[
4t(k+m-1)+1<q,d.
\]

Since $k+M'-1\le k+M-1$, both inequalities weaken. Every other field uses the same frame, host fields, fixed $k,t$, or data independent of $m$. Thus the host transports.

The actual generic constructor is

```
hostSpacesOfNorm (T) [Fact T.Prime] (pz : H.E)
  (hpz : pz * H.conj pz = T) : Spaces R H.F H.E.
```

It calls `spacesOfRanks`, with `star_isIntegral`, `cmData H`, the given norm equation, and `exists_adelic_neg_one H ...`. These hypotheses remain supplied by the transported host and the same $T,z$. This proves existence of the new `Spaces`, not merely consistency of their dimensions. \(\square\)

**Exact source locators.** `DataHost.lean` 39–109 is the full structure; `qd_big` is at 54. `SpanPowerMembership/RankRecordRowDimensionZero.lean` 137–142 is the generic `hostSpacesOfNorm`. Its implementation calls the general declaration in `SpanPowerMembership/BaseFormAnisotropicOrthogonalSingle.lean`: inputs 200–205, `spacesOfRanks` 325–386, and `spacesOfRanks_T` 388.

The generic constructor is explicit. Its $X_j$ is the positive standard space of rank $k+j(t+1)$ (329–332); $Y_j$ has rank $k+M'-1+jt$ and negative index $\lfloor(M'-j)/2\rfloor$ (341–346); $W_j$ has rank $k+M'-1$ and signature $(k+j-1,M'-j)$ (368–376). The terminal complement and the distinguished vectors are constructed at 333–367. The adelic isometry field is actually filled at 376. Thus the associated abstract Hermitian spaces are not the first missing datum for a smaller even $m$.

The containing file also has a `rankRecord`, but its `chain2` has empty class sets (25–44) and its `period2` has zero evaluation and period (77–83). Its name or type must not be used as evidence that a nonzero shorter theta chain with the needed estimates has been constructed.

## 4. DP44(c): what is preserved and what changes

At fixed $k,t$, the positive spaces $X_j$ of the generic construction have the same rank and standard form for every retained $j\le M'$. Thus there is no ambient-dimension obstruction to reusing class lattices on these retained $X_j$'s. The auxiliary $Y_j,W_j$, the terminal $X_{M'}$, and the endpoint period are different data.

The rank difference is exact:

\[
N_M-N_{M'}=(M-M')(t+1)>0\quad(M'<M).
\]

In the old chain, $W_{M'}$ has signature

\[
(k+M'-1,M-M'),
\]

whereas the new chain ends with $W'_{M'}$ of signature $(k+M'-1,0)$. The new spaces therefore cannot be obtained by merely relabeling the old endpoint while retaining all auxiliary data. This recovers the exact unchanged-endpoint qualification in DP27.

There is also a useful numerical qualification. Even fixing the *terminal positive dimension* does not force $M$ if $t$ is allowed to change. For even $2\le M'<M$, choose any even $k\ge M+3$, a frame with $M\le2\operatorname{ord}\le k$, and a sufficiently large integer $c$. Put

\[
t+1=2M'c,\qquad t'+1=2Mc.
\]

Both $t,t'$ are odd, all rank inequalities hold for sufficiently large $c$, and

\[
k+M(t+1)=k+M'(t'+1).
\]

This is only a numerical example, conditional on the displayed common frame. It does not transport the host size bounds, HC gaps, auxiliary ranks, periods, or analytic estimates from one tuple to the other. In particular it does not establish a shorter chain with the same representation-theoretic endpoint.

## 5. The first nonautomatic fields of a shorter complete construction

The recovered generic nonzero-row constructor is `SpanPowerMembership/NZRowE.lean:194`, `hostLevelRecord`. It accepts arbitrary admissible ranks, host, HC data, class packages and the remaining stated inputs. Its `sp` field is exactly the generic `hostSpacesOfNorm` (198). This supplies a concrete construction interface; one need not treat all of D7 as a mysterious unknown.

However, its hypotheses 165–189 include actual class lattices, a level window, norm elements and congruences, signature weight arrays, a local gap datum, a local $G$-package, and a period of type

\[
\mathrm{per}_u:\mathrm{FK}(\mathrm{cls}_u(M))
\longrightarrow \mathrm{En}(d)\longrightarrow\mathbf C.
\]

The period is an explicit input at 185, enters `memC` at 159–163 and `hostLevelRecord` at 211, and is used in the terminal period comparison at 245. After restriction to $M'$, the new input has domain $\mathrm{FK}(\mathrm{cls}_u(M'))$. The old terminal period is not of this type. Composing it with the discarded transition kernels produces a linear map on the earlier space, but still uses precisely those discarded kernels; no theorem identified in this pass turns that composite into a single cheaper geometric theta operation with the same integral normalizations.

Even a supplied D7 does not by itself supply the source's quantitative hypotheses. `SpanPowerMembership/NZRowAsm.lean:61–86` defines the additional `ExtraNZIn` inputs. They include the level-error data, lattice comparison and lattice definitions, actual `LocalToGlobal₂` kernels, entropy and entry ties, the `KapI` and `Kap` definitions, orbit-filling and unserved-orbit data, the error definition, a choice and tie of the relevant $N$, the `NMj` condition, the `FDef`, normalized dimension parameters, and `GaugeExists`. The constructor `extraNZ` at 91–123 assembles the final `Extra` once these inputs are given; it does not erase them.

For the global family comparison, the precise top-level inputs are `GlobalTheoremInputs.lean:158–160`:

\[
\mathrm{LinkG}\wedge\mathrm{LinkS}\wedge\mathrm{LinkIRR}
\wedge\mathrm{LinkDIV}\wedge\mathrm{LinkMu}.
\]

Their existence for Alpoge's accepted family is not in question here. A new shorter family, or a new mixed CM host, requires these interfaces to be instantiated for that new family. This source reading does not certify such an instantiation.

## 6. DP44(d): exact gain and main-term bookkeeping

The relevant source functional is explicitly indexed by the lift set \(\{1,\ldots,m\}\). For a fixed member $u$, define

\[
\begin{aligned}
g_j&=\sum_{w\in\mathrm{supp}}\mathrm{sz}_w(\mathrm{gainD}_{j,w}),\\
e_j&=\sum_{w\in\mathrm{supp}}\mathrm{sz}_w(E_{u,j,w}),\\
T_\tau&=\sum_{w\in\mathrm{supp}}\mathrm{sz}_w(\tau_w),\\
H&=\sum_{t\in\mathrm{TT}}\bigl(\mathrm{phF}(A_t)-A_t\log\Omega\bigr),\\
K_u&=\sum_{t\in\mathrm{TT}}A_t\log T_u.
\end{aligned}
\]

Since `sz` is a fixed scalar multiple, the definitions give

\[
\mathrm{Ga}_m=\sum_{j=1}^m g_j-T_\tau,
\quad
\mathrm{Ee}_m(u)=\sum_{j=1}^m e_j,
\quad
\mathrm{MAIN}_m(u)=mH-K_u.
\tag{DP44.1}
\]

These are exact identities. In particular, if the other displayed data are held fixed,

\[
\mathrm{MAIN}_{M}-\mathrm{MAIN}_{M'}=(M-M')H.
\tag{DP44.2}
\]

There is no justification for silently assuming $H>0$. For the signed comparison quantity

\[
Q_m=\mathrm{Ga}_m-\mathrm{Ee}_m-\mathrm{MAIN}_m,
\]

the same frozen-data comparison yields

\[
Q_{M'}-Q_M
=-\sum_{j=M'+1}^{M}(g_j-e_j-H).
\tag{DP44.3}
\]

If an additional numerical allowance $B_m$ is subtracted, its effect is exactly an additional $B_M-B_{M'}$ on the right. For two genuinely rebuilt families all the changed $g_j,e_j,\tau,A_t,\log\Omega,T_u$ must also be included; (DP44.3) is then not a license to freeze them. The algebra proves that merely counting fewer terms does not decide the comparison. It does not assert that $Q_m$, by itself, is the complete global theorem hypothesis.

**Exact source locators.** `DataParams₂.lean`: `sz` 203–206, `lifts` 208, `gainD` 212–213, `sg` 215–216, `Fo/Ga/Ee` 218–222, `logOm` 224, `B0/Nc` 228–230, `MAIN` 232–234. The source uses both local slope and global cost quantities: `LocalQuadraticParts.lean:677–680` gives the stated `Conclusion4` slope comparison involving `Ga + Fo − Ee`, whereas `GlobalTheoremInputs.lean:77–89` gives `LinkDIV_at`, including its explicit upper bound involving `MAIN`, `m(B0+Nc)`, and the other costs. These references identify the input/output statement interfaces; they do not themselves assert that a new family satisfies them.

Other parameters visibly change with $m$. The gamma normalization is `DataParams₂.lean:176`, \(\log\Gamma=C_\Gamma m^5 fL\); the level condition is `TuGe`, 252, \(b^{m/2}\le T\). `GlobalTheoremInputs.lean:100–102` has the terminal rank squared in `flG`; `loG` 109–120 has further rank, orbit, and scale terms. Thus “same cost per lift” is an additional proposed comparison hypothesis, not a property already proved by the old formulas.

## 7. Why DP40 and DP42 do not yet evaluate the complete global comparison

The source's `LinkG_at` at 122–136 has, at inert/signal places, the lower certificate

\[
\sum_{j=1}^{m}\sum_{t\in\mathrm{TT}_w}
\bigl(R_{2,j,t,p}-\operatorname{loG}\bigr)
-m\operatorname{flG}
\le \sum_{j=1}^{m}\mathrm{gain}_{j,w}-\tau_w.
\tag{DP44.4}
\]

Here `R₂` is precisely the finite odd-level ramp sum `vonMangoldtClassSum`, `DataParams₂.lean:240–242`, with weights at least one (180). The cutoff is `Nat.log p (aT.toNat) + 2`, and only odd indices contribute. Equation (DP44.4) is a **lower certificate** for the source gain. It cannot be reversed into an upper bound on the true gain.

DP40 proves an equal-direction sum bound for cyclic CM-type formal-group slopes, with equality at the alternating type. It is not a componentwise bound and it does not identify the source's weighted harmonic selections, paths, or minors with that equal-direction sum. DP42 proves the exact radius and factorial-slope limit on every primitive mixed line of the actual higher-height line–dual pair, under its explicit primitive-frame identification and nonzero bounded-prefactor restriction. Its best such mixed-line slope is the height-two value. It does not identify every source selected harmonic polynomial or determinant entry with a primitive mixed line.

Consequently these results eliminate two concrete free-gain routes—equal treatment of all CM directions and improved primitive mixed-line kernels—without proving that every alternative weighted selection or shorter global theta construction is impossible. DP26's finite ramp arithmetic remains a numerical non-exclusion under fictitiously identical costs; it is not a geometric construction. DP18's unchanged-budget comparison controls the specified asymptotic exponent and is not a minimum theorem for actual lift counts.

## 8. The strongest presently justified reduction

For a smaller even number of lifts in the existing host, rank/HC/host compatibility and the generic Hermitian spaces can be rebuilt as in parts (a)–(b). To claim the desired saving with a specified endpoint, one must first give the new endpoint period and its integral/representation-theoretic ties. One must then instantiate the selected local kernel and lattice data of `ExtraNZIn` and the global links for the new family, and compare their actual gain and cost terms. If all those data and comparison constants are supplied, the lift-count question reduces to those explicit finite or asymptotic inequalities; no further rank-record obstacle remains.

For a genuinely mixed CM host, the first old-host identity already changes: the induced type and its typeP/typeM input cannot be retained (DP25). The actual new selected theta normalization and path/minor estimates must then be supplied. DP40 and DP42 sharply constrain particular proposed replacements but are not a substitute for this construction.

No conclusion in this memo says that Alpoge's chosen lift count is globally minimal, that all shorter proofs are impossible, or that a successful shorter family has already been built.

## 9. Check and provenance boundary

The new mathematical assertions in DP44(a)–(d) were proved directly above. The fresh source reading inspected all `Ranks`, `HCParam`, and `Host` fields; the whole generic `spacesOfRanks` constructor block with its hypotheses; the exact `hostSpacesOfNorm` wrapper; the nonzero-row constructor's relevant parameter and assembly blocks; the whole `ExtraNZIn` interface and assembly; and the cited gain/main-term definitions and global-link inequalities. It did not execute Lean, rebuild the entire source dependency tree, or re-prove the accepted global theorem. The source archive inventory contains additional files recovered for locating these declarations; the manifest records the actual reading scope separately from byte provenance.
