# Step 17 direct unit-trace interface

**Finding K17-S17-UNIT.** Date 2026-11-21 UTC. Author/checker `/root/vandiver_k`; model GPT-6 Astra Pro; effort not exposed. This is a deduction from the recovered source theorem, with its actual admissibility predicates retained. It is not a deduction from the weaker existential polynomial bound alone. This note contains the entire source-interface argument; the separate finite Hecke calculation and the rank-two conductor calculation remain independent inputs.

All Lean locators below refer to commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of `CocoSgt/riemann-hypothesis-lean`. Paths are relative to `src/Development/AutomorphicArithmetic/AutomorphicVarieties/`, except the explicitly named Foundations paths. Newly retrieved copies and SHA256 manifests are in `work/hecke_coverage/interface/`.

## 1. The exact source theorem that is needed

`ModularityArgument/ThresholdArguments/DenseThresholdCases/NumberU3US.lean`, definition `OneCharU_s`, lines 49–59, states the following. Suppose the source datum `GD Ω K ℓ e ψ` holds. For any coefficient embedding \(\iota:\overline{\mathbf Q}_\ell\simeq\mathbf C\), any \(s\in G_K\), and the prescribed Eisenstein trace
\[
t=\Psi(s)+1+\Psi(s)^{-1},
\]
assume that every representation satisfying
\[
\operatorname{Adm3U\_s}(\iota,e,N,\rho)
\quad\text{or}\quad
\operatorname{Adm2A}(\iota,e,N|d_K|,\rho)
\tag{1}
\]
has \(\operatorname{tr}\rho(s)\ne t\). Then the Selmer length `Vlen` is finite, and there exists a finite set \(X\) of representations satisfying (1), pairwise nonisomorphic, with
\[
 V_n\le 2\sum_{\rho\in X}v_\ell\bigl(\operatorname{tr}\rho(s)-t\bigr).
\tag{2}
\]
Here `vl` is \(-\log_\ell|\cdot|_\ell\), and `Vn = Chr.nrm ℓ c.O Vlen`. The exact normalization is
\[
\operatorname{nrm}(a)=a.\operatorname{toNat}/e(O/\mathbf Z_\ell),
\]
for a finite coefficient DVR; the definition is `CharacterLevelBounds/ShaFamMono.lean`, line 71. Finiteness is essential because `toNat` sends infinity to zero.

The actual theorem proving this is `FOneCharU.lean`, `oneCharU_of_katoTwoW_rig_admI_automorphy`, lines 75–95, with its complete preceding private proof `oneChar_unramU`, lines 19–74. The proof constructs an actual universal deformation datum, local ring, and model; applies `model_upper`; and sends the resulting finite set of points satisfying `TwoPt` into rank-three representations. Its `hadm` step treats Type I using `AdmI_s` and Type II using `adm2B_rhoK_of_typeII_of_modular_extensions`, whose output is the literal `Adm2A` predicate. The final theorem removes the coefficient-unramified restriction by `exists_unram` and `coefIndep`. Thus (2) applies to arbitrary coefficient DVRs in the source, not just to the unramified choice.

This theorem is **closed with the same source inputs as step 17**. Specifically, `SmallClassNumbers/CorGKOf.lean`, lines 10–18, applies precisely this theorem, supplying its cohomology, algebra, Kato, rigidity, admissibility, and automorphy arguments. Lines 20–27 supply the closed `litN` and `published_hypotheses_from_patching_alt` input used in `corGK`. One can retain that inner theorem value rather than pass it to `propGK_of_numberU3U_of_oneCharU`. No new statement about those source inputs is postulated here. The cited source proof is used as stipulated background; this reading does not claim a new kernel verification of the entire repository.

### Direct unit criterion

Under the same GD hypotheses, if every difference in (1) is an \(\ell\)-adic unit, then
\[
 V_{\mathrm{len}}=0.
\tag{3}
\]
Indeed a unit is nonzero, so `OneCharU_s` gives finite length and (2). Every summand on its right is zero. Since a finite module length divided by a positive finite ramification index is nonnegative, (2) forces that length to be zero.

This proof does **not** require a smaller `TrData`, injective assignment of representations to Hecke eigenvalues, or a divisibility relation between an earlier oversized polynomial and a new characteristic product. Repeated eigenvalues and arbitrary multiplicities do not affect it. The only coverage requirement is that each actual admitted trace be one of the traces certified to have unit difference.

## 2. Literal rank-three admissibility and the retained hypotheses

The actual predicate, `NumberU3US.lean`, lines 27–29, is
\[
\operatorname{Adm3U\_s}=\operatorname{Adm3Alt}\ +\ \operatorname{Th.Unl}.
\]
`AfStmt.lean`, lines 29–33, defines `Adm3Alt` by irreducibility of \(\rho\),
\[
 \operatorname{IsAutCsdA}(\iota,r),\qquad
 r=\rho\chi_\ell^{-1},
\]
and the literal condition
\[
 \operatorname{Level}(\ell,N,(e,0,-e),\rho).
\tag{4}
\]
`IsAutCsdA.lean`, lines 11–12, says
\[
 \operatorname{AutCsd0}(\iota,r)\ \wedge\
 (r\text{ continuous}\Rightarrow\operatorname{WitA}(\iota,r)).
\tag{5}
\]
The definition `AutCsd0` in Foundations/GaloisRepresentations/AdmissibleResidues/IsAutomorphicOverImagQuad.lean, lines 35–36, is exactly the existence of a regular algebraic, conjugate-self-dual **cuspidal** \(\Pi\) of \(\mathrm{GL}_3(\mathbf A_K)\) with `AttC ι r Π`. Thus no isobaric or noncuspidal representation is silently included in this branch. The extra `WitA` assertion in (5) is retained, rather than discarded as an irrelevant strengthening.

## 3. Strengthening level two to level one

By `BlochKatoSelmerVanishes.lean`, lines 66–67,
\[
 \operatorname{KillsMu}(M,\chi)
 \iff \forall g,\quad
 [g\text{ fixes every }M\text{-th root of unity}]\Rightarrow\chi(g)=1.
\]
Every characteristic-zero field automorphism fixes the two roots of unity \(\{1,-1\}\). Hence `KillsMu 2 χ` forces \(\chi=1\). Conversely the trivial character satisfies `KillsMu 1`.

Consequently every witness in the away and above-prime clauses of (4), with \(N=2\), is also a witness with \(N=1\). In the above-prime clause the flag, its diagonal characters, their nonadjacency/potential-crystallinity disjunction, and continuity are unchanged. Thus
\[
 \operatorname{Level}(\ell,2,(6,0,-6),\rho)
 \Longrightarrow
 \operatorname{Level}(\ell,1,(6,0,-6),\rho).
\tag{6}
\]
The exact Level definitions are `BlochKatoSelmerVanishes.lean`, lines 89–115.

The complete proved lemma `BuildingsResidueChars/LevelTwistCyclotomicPow.lean`, `UpperTheory.level_twist_cyclotomic_pow`, lines 20–60, transports (6) through \(r=\rho\chi_\ell^{-1}\) and shifts each exponent by \(-1\):
\[
 \operatorname{Level}(\ell,1,(5,-1,-7),r).
\tag{7}
\]
In particular \(r\) is continuous, so (5) gives `WitA ι r`.

There is also the independent local input `Adm3U_s.unl`. The complete theorem `AutomorphyLifting/AdmissibleLevelRestriction/UnlAllOf.lean`, `unlAll_of`, lines 36–39, turns this into `Unl1 ρ w` at every \(w\mid\ell\). `Unl1` means an ordinary flag whose diagonal characters \(\kappa_i\) satisfy \(\kappa_i\ne\kappa_j\chi_\ell\) for every \(i,j\); see `AutomorphyLifting/WeakOfAtt.lean`, lines 19–21. Multiplying every \(\kappa_i\) by the same character \(\chi_\ell^{-1}\) preserves those inequalities and transports the flag. Thus `Unl1 r w` holds at every \(w\mid\ell\). This supplies the above-prime hypothesis of the source level theorem. We do not infer zero monodromy from the LevelAt disjunction alone.

## 4. Apply the source's actual full-level theorem

Use `ThresholdArguments/DenseThresholdCases/KeepLevel.lean`, theorem `Keep.levelCore_alt`, lines 31–83, or its CSD specialization `Keep.levelKA_alt`, lines 95–102. Its inputs are:

* the same published `Hypotheses'` supplied by the closed step-17 source;
* \(K=E=\mathbf Q(\sqrt{-3})\), rank three, \(\ell\ne2\);
* \(M=1\), the exponent vector \(m'=(5,-1,-7)\), and (7);
* the above-prime `Unl1` condition just established;
* the actual `WitA ι r` from (5);
* the regular algebraic CSD cusp representation \(\Pi\) and attachment from `AutCsd0`.

The CSD specialization supplies the required polarization by the quadratic character to the third power. The conclusion is
\[
 \Pi_f^{K\mathrm{Lev}(E,3,1)}\ne0,
 \qquad \operatorname{InfChar}_\tau(\Pi)=\operatorname{infOf}(5,-1,-7),
\tag{8}
\]
and, **at every** \(w\nmid\ell\), exact `FrobEig ι r w (algSat 3 q B)` for its Satake multiset \(B\), where \(q=Nw\). This is not merely cofinite compatibility from the definition of `AttC`.

`KLev` is the principal congruence kernel inside integral finite adelic matrices (`BlochKatoSelmerVanishes.lean`, lines 47–51). At modulus one its congruence condition is vacuous, so it is exactly \(\prod_w\mathrm{GL}_3(O_{E_w})\). This can also be checked directly from `AutomorphicForms/KLevTop.lean`, `mem_KLev`, lines 17–51: with \(M=1\), the difference \(g-I\) is integral whenever \(g\) and \(g^{-1}\) are integral. Hence (8) says that \(\Pi\) is unramified at every finite place, including those above \(\ell\).

The source infinitesimal-character convention is
\[
 \operatorname{infOf}(m')=\{(n-1)/2+m'_i\}_i.
\]
For rank three this yields \((6,0,-6)\). In unitary, regular cohomological normalization the infinity parameter is therefore
\[
 \operatorname{diag}\bigl((z/\bar z)^6,1,(z/\bar z)^{-6}\bigr),
\]
and the compact coefficient highest weight is \((6,0,-6)-(1,0,-1)=(5,0,-5)\). Equivalently the source Hodge–Tate weights of \(r\) are \((-5,1,7)\), and the relation used in `levelCore_alt` is \(\mathrm{HT}=1-\operatorname{InfChar}\). This records both shifts explicitly.

Thus every actual rank-three admissible representation is covered by **K17-U3-COVERAGE**, with no omitted `WitA`, `Unl`, local \(\ell\)-condition, or Tate twist.

## 5. Exact trace normalization and the unit test

Take a split auxiliary rational prime \(p\ne\ell\), a place \(w\mid p\), and arithmetic Frobenius \(\sigma\). The source convention is \(\chi_\ell(\sigma)=p\), and `FrobEig` describes the eigenvalues of **\(r(\sigma^{-1})\)**. Since
\[
 r(\sigma^{-1})=p\rho(\sigma^{-1}),
\]
and `algSat 3 p B` multiplies unitary Satake roots by \(p^{(3-1)/2}=p\), the two factors cancel. Thus
\[
 \iota\operatorname{tr}\rho(\sigma^{-1})=\sum_{\beta\in B}\beta.
\tag{9}
\]
The exact local Hecke normalization is a separate input of the finite certificate. With the certificate's notation \(A_p\), it says \(\sum\beta=A_p/p^6\). The source comparison trace for \(\psi=1,e=6\), at \(s=\sigma^{-1}\), is
\[
 t=p^{-6}+1+p^6.
\]
Therefore every rank-three admitted difference equals
\[
 \frac{A_p-(1+p^6+p^{12})}{p^6}.
\tag{10}
\]
There is no eigenvalue-multiplicity assumption in (9) or (10): coverage in a fully computed one-dimensional Hecke space forces its Hecke eigenvalue.

For the rank-two branch, its literal predicate `AutNewformW.lean`, `Adm2A`, lines 14–21, adds `WitAQ` to the original newform/Level/block conditions; the newform has weight \(2e+1\), and the block is \(1\oplus W|_{G_E}\). The parent is separately checking that, for \(e=6,N|d_E|=6\), every such branch is represented by a normalized eigenform in \(S_{13}(\Gamma_0(3),\chi_{-3})\) and has trace \(1+a_p/p^6\). Under that independent coverage assertion, its difference is
\[
 \frac{a_p-(1+p^{12})}{p^6}.
\tag{11}
\]
Let \(Q_p(X)=\det(XI-T_p)\) on the entire three-dimensional space, with its full characteristic multiplicities. Since every \(a_p\) is algebraic integral and \(Q_p\in\mathbf Z[X]\), if
\[
 \ell\nmid (1+p^6+p^{12}-A_p)\,Q_p(1+p^{12})
 \quad\text{and}\quad \ell\ne p,
\tag{12}
\]
then all differences (10) and (11) are units at **every** prime above \(\ell\). Indeed the product of all integral conjugate factors of the characteristic polynomial is an \(\ell\)-adic unit, while each factor has nonnegative valuation; every factor consequently has valuation zero. This remains true with repeated characteristic roots. Applying the direct unit criterion (3) gives \(V_{\mathrm{len}}=0\).

No earlier congruence integer is used. In particular (12) does not assert that the oversized old characteristic product divides this smaller one. This is a new unit test applied directly to the source theorem, not a divisibility inference between unrelated products.

## 6. Scope and actual checks

The entire generic `TrData` norm-bound proof was also read and does permit arbitrary replacement classifying data, but that stronger construction is unnecessary here. The present argument uses only pointwise trace coverage and therefore avoids all multiplicity and same-eigenvalue/global-isomorphism issues.

Actual full reads in this task: `NumberU3US.lean`; `FOneCharU.lean` including both proofs; the earlier `OneCharU.lean`; `SmallClassNumbers/CorGKOf.lean`; `FPropGKU.lean`; `AfStmt.lean`; `IsAutCsdA.lean`; `AutNewformW.lean`; the definitions and relevant proof in `IsAutomorphicOverImagQuad.lean`/`WitApi.lean`; `KeepLevel.lean` including its complete core proof and specializations; the entire cyclotomic-twist proof; the complete `unlAll_of` proof and `Unl1`/`WitA` definitions; and `KLevTop.lean` including the entire `mem_KLev` proof. The foundational source theorems they invoke are treated as cited source inputs. A complete independent Lean build was not run.
