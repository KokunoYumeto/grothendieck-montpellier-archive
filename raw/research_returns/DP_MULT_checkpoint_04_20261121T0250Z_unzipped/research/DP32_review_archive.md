# Independent whole-proof review of DP32

Reviewer: `/root/archive_binomial`, GPT-6 Astra Pro, inherited model; reasoning effort not exposed by the runtime. Date: 2026-11-21 UTC. Event: **ABA-CE27**. Review began at **01:16:17 UTC** and was closed at **01:19:59 UTC**. This is an independent-agent manual whole-proof challenge of the supplied draft, not a formal verification or a claim to have independently audited the complete proofs of the cited classical theorems.

## Result and exact scope

**PASS. No substantive mathematical gap or counterexample was found.** I read the complete statement, every paragraph of proof sections 1--4, and the complete numerical consequence in section 5 of `actual_dual_all_heights_DP32.md`. I then re-read the exact saved snapshot in full. The actual-dual identification, integral coordinate construction, mixed coefficientwise bound, individual sharpness, and the qualified equally weighted comparison are valid as stated, including the boundary cases $p=2$ and $h=2$.

This record concerns the draft named above. It does not automatically certify a later integrated or edited version of the main paper. No main-paper edits were made by this reviewer.

## 1. Functional-equation construction

I directly read Hazewinkel's **Functional Equation Lemma 2.3**, including hypotheses (2.2), equations (2.4), conclusions (2.5)--(2.7), and congruence equivalence (2.8), in the primary PDF's printed pp. 74--75. I also read the corresponding page images. With $B=\mathbf Z_p$, $L=\mathbf Q_p$, ideal (pB), and coefficient endomorphism equal to the identity, all stated matrix entries (0,1/p) satisfy the required ideal condition. No commutativity condition on the two matrices is missing from the cited lemma.

The component functional equations follow from the monomial iterates. The case $d=1$ correctly has only the $p^2$ arrow. Multiplying the functional equation by $p$ supplies the second input needed for conclusion (2.6), so the asserted integral $p$-series follows. The exact identity (L(M)=p(L-X)) then makes the difference of logarithms precisely (pX); applying (2.8) is legitimate and gives the claimed special-fibre $p$-series.

## 2. Finite freeness and the actual dual

The monomial basis modulo $p$ is a basis over the **power-series** subring, with exactly $p^{d-1}p^2=p^h$ elements. The direct integral lifting argument is sound. Both power-series rings are complete and separated for the $p$-adic topology, even though their maximal-ideal topology is finer in a different direction. Coefficientwise reduction/lifting gives surjectivity, and $p$-torsion-freeness plus separation gives injectivity. The substitution homomorphism is $p$-adically continuous, so the lifted sums retain the required module identity. This establishes finite freeness rather than assuming it from the special fibre.

The resulting formal group has a connected height-$h$ $p$-divisible group. Tate's formal-group correspondence and dual dimension formula apply: the base is complete noetherian local, and the dual has dimension $h-d=1$. I directly read the primary extracted statements of **Tate 1967, §2.2 Proposition 1, pp. 162--164**, and **§2.3 Proposition 3, p. 166**, including the surrounding Frobenius/Verschiebung and duality discussion. The cited classical proofs are used as sources, not re-proved here.

On the special fibre over **\(\mathbf F_p\)**, all Frobenius twists are canonically the same group. A full cycle of $M$ raises each coordinate to $p^h$. Duality therefore gives $V_G^h=[p]^{h-1}$, and composing with $F_G^h$ and cancelling the surjective multiplication-by-$p^{h-1}$ map gives $F_G^h=[p]$. This is a legitimate cancellation in the category of $p$-divisible fppf sheaves. It does not divide by $p$ in a torsion object.

The identity also gives (G[p^n]=\ker(F_G^{hn})). These special-fibre kernels are connected. Their finite integral lifts are local because the base is complete local and their special fibres are local. Consequently the integral dual is connected and Tate's equivalence indeed supplies a one-dimensional formal group over $\mathbf Z_p$.

I directly read the primary statement of the **Lubin--Tate uniqueness and strict-isomorphism theorem in Hazewinkel 1979, §5, printed pp. 76--77**, and viewed the printed p. 77 image. In any integral coordinate on this one-dimensional group, the $p$-series has linear term (pT), and its reduction is $T^q$. After extension to (\mathcal O=W(\mathbf F_q)), these are exactly the hypotheses (5.1), with uniformizer $p$ and residue cardinality $q$. The existing group law already makes that series an endomorphism, so uniqueness identifies it with the law in the theorem. The Honda logarithm gives another law in the same class by (5.2)--(5.4); strict integral isomorphism follows.

**No prior \(\mathcal O\)-action on the candidate dual was assumed or is needed.** The theorem supplies the group identification, and the action may then be transported. Dualizing the resulting isomorphism gives an integral coordinate model of the actual Honda dual. Its dual isomorphism need not be strict for the argument: transporting coordinates still gives an integral tangent basis and the stated normalized primitive derivations.

## 3. Contraction and exact coefficients

The weights (r_i=1/(p-1)-p^i/$p^h-1$) are positive for every indicated $i$. The arrow relations $p^{e_i}r_j-r_i=1$ hold also at the wrap-around $p^2$ arrow and when $d=1$. Choosing the common ramified parameter makes each first nonlinear coefficient **exactly one**, not merely a unit. Every later term has positive valuation by the displayed geometric-sum formula, including when $p=2$.

The reduction of the inverse is consequently the convergent formal geometric series in the additive map $M$. In characteristic $p$, the signs commute with all powers used here; in characteristic two both signs coincide. There is no convergence issue, because degrees strictly increase. In the $i$-th component restricted to the $i$-th coordinate axis, precisely the iterates with step number divisible by $d$ survive. Their degrees are $q^r$, with nonzero coefficient ((-1)^{dr}). There are no distinct iterates at the same degree to cancel.

The inverse scaling formula uses both the input and output scale. It gives exactly

\[
v_p([t^{q^r}]E_i(te_i))=-$q^r-1$r_i.
\]

This is consistent with the coefficient lying in the original rational field: ($q^r-1$r_i) is an integer. The ramified extension is a proof device for detecting its exact valuation.

## 4. Coefficientwise derivatives and optimality

The integral formal law supplies integral commuting invariant derivations with tangent basis (D_iX_j(0)=\delta_{ij}). The logarithm has identity linear term, so these become the ordinary coordinate partial derivatives. The displayed factorial coefficient identity is therefore correctly normalized.

The weighted bound on each component of $E$ passes to every integral (f(E)): each fixed monomial coefficient uses only finitely many terms, and every contributing product has at least the stated weight. Legendre's formula gives the proposed bound at the identity; integrality of the derivations supplies the additional lower bound zero.

The passage to **every coefficient** is valid. The translated function (f(F_H(X,Y))) belongs to $\mathcal O[[X,Y]]$. Treating $X$ as coefficient variables preserves the weighted estimates in $Y$ coefficient by coefficient, and translation invariance identifies the resulting derivative at $Y=0$ with (D^a f(X)). Thus the argument does not confuse an evaluation bound with a coefficientwise bound.

For the witnesses $f=X_i$ and $n=q^r$, the previously computed exact coefficient and (s_p(n)=1) give (v_p(D_i^nX_i(0))=(n-1)c_i). These witnesses exclude any larger asymptotic slope with sublinear error in the **specified primitive direction**. Transport along the integral group isomorphism and extension to (W(k)\supset\mathcal O) preserve all the assertions.

## 5. Scope of the numerical consequence

The finite geometric sum is exactly \(\sum_i c_i=c_h\). Hence the displayed line-plus-dual basis has mean slope $2c_h/h$. For $h>2$, $c_h/c_2<1+1/p$, and (2(1+1/p)/h\leq1); the strict first inequality covers the boundary $p=2,h=3$, where the latter inequality is an equality.

This is an equally weighted comparison for the **displayed basis**. The proof does not identify these coordinate functions with theta entries, prescribe geometric weights, estimate the costs of a mixed-variable kernel, or prove an automorphic chain lower bound. Its explicit scope limit is necessary and already present. DP30's unit derivative at order $p$ is compatible with these positive asymptotic slopes; it does not contradict the theorem.

## Exact version record

The complete reviewed file is preserved as `late_proof_snapshots/DP32_draft_checked.md`.

| Scope | SHA-256 |
|---|---|
| Entire file, exact original bytes | `f239e38a268218ea5909db06ef36483ab2fe3792144cce647d4a139bdbeeb325` |
| Statement, from `## Statement` to immediately before `## 1. Integral construction` | `407c8ea2ecf18371d57970dd871304ec07559b03524393f7c20729af0516b00f` |
| Complete proof and consequence, from `## 1. Integral construction` to immediately before `## Check status` | `3742d0d6b29a7935b017ad33f967543ecb72519abf4ec1429d58df09a586dfa5` |

The section hashes preserve all intervening original whitespace. The whole file has 10,154 bytes. The check is recorded as **ABA-CE27** in both reviewer TSV logs. No requested future check is counted as completed.
