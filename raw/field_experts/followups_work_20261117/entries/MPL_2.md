### L01 — The geometric family is part of the input

**Cote/scans:** 2/021, lines 4, 9, 45; 028, lines 6–45; 029, lines 28–32. **Kind:** unpursued implication. **Context:** bears on both Hua IDs; qualifies the formulation of the first and is essential to the second.

The phrase “plus la famille des $E_s$ est grande … plus $CK$ devient petit” on scan 029 makes the chosen family part of the universal problem. Closure under the indicated positive operations must be distinguished from replacement by every element that is algebraically geometric in $K$: the warning on scan 029 and the added $nL-1$ on scan 022 give a concrete difference. Consequently write $C(K,S)$ in a modern restatement, even though the manuscript usually abbreviates this to $CK$.


### L02 — The displayed relations do not by themselves enforce lambda compatibility

**Cote/scans:** 2/028, lines 33–35; 029, lines 6–13. **Kind:** own idea / counterexample to an overbroad restatement. **Context:** bears on **2-chern-ring-gamma-comparison**; contradicts a literal exhaustive reading of that entry's abbreviated relation list. **Confidence:** high, because the explicit countermodel is verified in Appendix A of `records/research_lambda.md`.

Scan 028 explicitly requires an “hom de $\lambda$-anneaux”, whereas the displayed list on scan 029 contains only unit, Whitney, product, and selected rank bounds. Those displayed relations alone admit an augmented ring map from $\mathbb Z[x,y,y^{-1}]$, with $\lambda^2x=y$, to the Chern ring of $\mathbb Z[\epsilon]/\epsilon^2$ sending $x\mapsto[2,1]$ and $y\mapsto[1,1+\epsilon]$, which is not a lambda homomorphism. The intended universal problem must retain lambda compatibility; the explicit gamma-compatibility relations in SGA 6, V, 6.14, p. 358, confirm the distinction (Berthelot, 1971).


### L04 — Precise comparison, including the degree-zero exception

**Cote/scans:** 2/021–022; 029, lines 21–28; 030, lines 8–15. **Kind:** unpursued implication / narrowed claim. **Context:** **2-chern-ring-gamma-comparison**, supported with qualifications.

The corollary “Son noyau est un groupe de Torsion” follows degreewise from the two composites being $d_i\operatorname{id}$, where $d_i=(-1)^{i-1}(i-1)!$ and $i\geq1$. More precisely, for the intended lambda-theoretic universal ring, $\phi_i:C^i(K,S)\twoheadrightarrow\operatorname{gr}^i_\gamma K$ has kernel annihilated by $(i-1)!$, hence is an isomorphism for $i=1,2$ and after rationalization in every positive degree. Degree zero must be treated separately: for the stated $\mathbb Z$-augmentation and the universal graded ring generated in positive degrees it is $\mathbb Z\to\mathbb Z$, not an instance of a formula containing $(-1)!$.


### L05 — The return map lands in a ring with a different product

**Cote/scan:** 2/030, lines 8–10 and 15. **Kind:** unpursued implication. **Context:** qualifies the “map $\psi$ back” in **2-chern-ring-gamma-comparison**; no exact `A!` or `A^!` match occurs in the supplied context.

The marginal restriction “additivement … en degrés $\ne0$” is essential: the coefficient identification of $\operatorname{gr}_{\deg}\widetilde A$ with $A$ does not preserve the ordinary product. For $a\in A^i,b\in A^j$, $i,j>0$, its product is $a\star b=-\frac{(i+j-1)!}{(i-1)!(j-1)!}ab$, so $\psi$ is multiplicative into this modified ring and only a graded additive map when its target is identified with ordinary $A$. Appendix C of `records/research_lambda.md` checks the formula and the factorial composites; the formula is also SGA 6, V, (6.5.3), p. 349 (Berthelot, 1971).


### L08 — The projective-space noninjectivity has a precise homogeneous witness

**Cote/scan:** 2/022, lines 41–56. **Kind:** own idea — verification of the manuscript's counterexample. **Context:** **2-chern-ring-not-injective-pn**, supported and sharpened. **Confidence:** high, from the explicit universal calculation in Appendix B of `records/research_lambda.md`.

The answer “Non” to “Est-ce que $\varphi_K$ est tjrs bijectif ???” is justified for $K=\mathbb Z[L]/(L-1)^n$, with only the family generated geometrically by $L$, when $n\geq3$. The complete relation is coefficientwise $P_n(\xi)=1$, where $P_n(z)=\prod_{j=0}^{n}(1+jz)^{(-1)^{n-j}\binom nj}$, and its first relation gives $C^n(K,\{L\})\cong\mathbb Z/(n-1)!$, whereas $\operatorname{gr}_\gamma K=\mathbb Z[\bar y]/\bar y^n$. In particular, for $n=3$, the exact ring is $\mathbb Z[\xi]/(2\xi^3,\xi^4)$, so the nonzero class $\xi^3$ is an explicit element of the kernel.


### L09 — Adjoining the tangent-class element really changes the chosen family

**Cote/scans:** 2/022, line 58; 029, lines 28–32. **Kind:** own idea — verification / unpursued implication. **Context:** adds to **2-chern-ring-not-injective-pn** and qualifies **2-chern-ring-gamma-comparison**. **Confidence:** high, by the rank and coefficient arguments in Appendix B of `records/research_lambda.md`.

The margin “si on adjoint … $nL-1$” imposes $c^n(nL-1)=\xi^n=0$, because $c(nL-1)=(1+\xi)^n$, giving $C(K,\{L,nL-1\})=\mathbb Z[\xi]/\xi^n$. For $n\geq3$, $nL-1$ is geometric but is not generated from $L$ by the stated positive operations and inverses of rank-one elements; thus this is a genuine enlargement of the family. This also furnishes the example promised by scan 029: an admissible Chern theory for the smaller family can have a nonzero high Chern component on another geometric element.


### L11 — The next-degree torsion criterion can be checked in a genuinely truncated ring

**Cote/scan:** 2/025, lines 12–16. **Kind:** own idea — verification with a hypothesis clarification. **Context:** no exact context match for the truncated criterion; it bears on the torsion mechanism in **2-chern-ring-not-injective-pn**. **Confidence:** high under the explicit truncation stated here.

The assertion “il faut et il suffit … $n!x^{n+1}=0$” is valid for a graded ring with all components above $n+1$ zero, as the finite-difference calculation in Appendix E of `records/research_lambda.md` shows. Interpret the manuscript's $A^{n+2}=0$ as a degree-cutoff/filtration condition for this verification; vanishing of just one homogeneous component would be a weaker statement and is not substituted silently. The calculation isolates the first degree in which torsion can let a geometric element have a Chern coefficient above its rank.


### L15 — The first possible prime obstruction follows from the comparison

**Cote/scans:** 2/022, lines 37–58. **Kind:** own idea / unpursued implication. **Context:** bears on both Hua IDs; the precise prime-by-degree bound has no matching context entry. **Confidence:** high, from the factorial annihilator and Appendix B of `records/research_lambda.md`.

The factorial comparison implies that the $p$-primary part of the kernel is zero in degrees $i\leq p$. The smaller-family example with $n=p+1$ has a nonzero $p$-primary kernel in degree $p+1$, since $C^{p+1}\cong\mathbb Z/p!$. This is a useful sharpness test for the degree bound in this family-dependent setting, not a claim of a new theorem.


### S03 — Cote 2, scan 033 — Conditional reconstruction of the full-faithfulness claim

**Kind:** own idea — conditional proof.

**Anchor:** $\operatorname{Lim}_nD^\bullet_{\mathrm{parf}}(i_n)\to D_Z(X)$.

For $X=\operatorname{Spec}A$ with $A$ Noetherian and $Z=V(I)$, our reconstruction gives $\varinjlim_n\operatorname{Ext}^q_{A/I^n}(M,N)\simeq\operatorname{Ext}^q_A(M,N)$ for finite modules killed by powers of $I$, and consequently the expected filtered categorical comparison after restricting to complexes perfect over $A$. The proof uses the equivalence between derived $I$-power torsion modules and complexes with torsion cohomology (The Stacks Project Authors, n.d., Tags 0955 and 06UP), together with finiteness of the data in bounded complexes and roofs; Appendix B of `records/research_supports.md` records the actual argument. Confidence is high for this stated affine Noetherian version, but the page's unrestricted “préschéma” formulation, the precise meaning of its categorical limit, and the target notation $D_Z(X)$ require additional conventions before this argument supplies a proof. Context search S03 found no corresponding own entry; the torsion hit **Hua, findings register, 2-chern-ring-not-injective-pn** concerns scan 022 and a different Chern-ring problem, so does not settle this statement.


### S07 — Cote 2, scan 035 — Pseudo-ring; the unit issue is substantive

**Kind:** unpursued implication.

**Anchor:** “pseudoanneau (pas néc d'élément 1).”

Derived tensor product preserves supported perfect complexes, and the ambient perfect-complex ring acts on their Grothendieck group, while the ambient unit $[\mathcal O_X]$ is unavailable when the allowed supports do not contain $X$. Thus the qualified nonunital language fits the construction and should not be silently replaced by “ring with 1”; the modern localized Chern character also has an explicitly multiplicative supported formulation (The Stacks Project Authors, n.d., Tag 0FET). Context search S07 found no relevant supported-ring entry in either context file; confidence in this structural explanation is high, without excluding accidental units for special supports such as an open-and-closed component.


### S08 — Cote 2, scan 035 — Construction ambiguity; rational equivalence with supports

**Kind:** own idea.

**Anchor:** “en prenant tjrs des cycles sur $X$ à support … $\Phi$.”

The phrase leaves a consequential choice between rational-equivalence data that stay inside the allowed supports and the image of supported cycles in the ordinary Chow group. In our test $X=\mathbb A^1_k$, $Z=\{0\}$, the former gives $CH_0(Z)=\mathbb Z$, whereas the class of $0$ maps to zero in $CH_0(X)$ because it is the divisor of $t$ on $X$. This high-confidence calculation shows that forgetting supports can lose information and that the proposed $A^\bullet_\Phi(X)$ is not determined merely as a subobject of $A^\bullet(X)$; context search S08 found no matching result or ID in the two supplied files.


### S12 — Cote 2, scan 037 — Proposed covariance; why “sans plus” is plausible

**Kind:** unpursued implication.

**Anchor:** “propreté sur supports (sans plus)” and the displayed equality commuting with $g_*$.

Relative perfection can make proper covariance stronger than covariance of absolute $K^0$: for a proper $g:X\to Y$ between Noetherian schemes over a Noetherian base $S$, $Rg_*$ preserves complexes perfect relative to $S$, without requiring $g$ itself to have finite Tor-dimension (Alonso Tarrío et al., 2023, Proposition 3.5). A later realized analogue is the proper-covariant rational transformation $G_0(X)\to CH_*(X)_{\mathbb Q}$ for quasi-projective schemes, with its module property and smooth Todd normalization (Baum et al., 1975, §0 and Chapter II). This comparison explains the force of the proposal but does not prove every relative, support-indexed assertion in the unfinished sheet; the uncertain word “bivification|homification” remains a reading uncertainty. Search S12 matches only the general Riemann–Roch subject in **context/README.md**, no same-object result ID; confidence is high in the cited mathematics and moderate in identifying the exact intended formalism.


### S13 — Cote 2, scan 037 — Unfinished canonical-element proposal

**Kind:** own idea.

**Anchor:** “un élément canonique explicitable”.

One rigorous candidate for the formal map $K^0(X)\to K^0(X\to S)$, when $X\to S$ is locally of finite type between Noetherian schemes and has finite Tor-dimension, is multiplication by the relative orientation $[\mathcal O_X]$ (Alonso Tarrío et al., 2023, §6.9). The Riemann–Roch image of the structure sheaf is a Todd homology class, and in singular situations that class need not come from an ordinary cohomology class capped with the fundamental class (Baum et al., 1975, §0.2 and IV §6). This supplies a candidate interpretation rather than an identification of the unfinished “canonical element,” and does not establish an integral $K^0$-preimage of any desired Todd factor; confidence is high for the formal distinction and low-to-medium for its identification with this fragment. Context search S13 found no relevant entry in either supplied context file.


### S15 — Cote 2, scan 038 — Coherent dévissage; stronger than the written surjectivity label

**Kind:** own idea — conditional strengthening.

**Anchor:** $K_\bullet(X_0)\to\varinjlim K_\bullet(X_n)$, “surj. si $X'$ rég.”.

If the lower groups are coherent Grothendieck groups and $X'$ is Noetherian, nilpotent dévissage makes each thickening pushforward $G_0(X_0)\to G_0(X_n)$ an isomorphism, and also identifies $G_0(X_0)$ with the coherent group supported on $X$ inside $X'$; ambient regularity is unnecessary for this lower-row statement (Quillen, 1973, §5, Theorem 4, and §7.3, Propositions 3.1–3.2). The finite ideal-adic filtration supplies the dévissage, while regularity is needed for the passage to the upper perfect groups, not for the filtration itself. Search S15 found only the unrelated “surjectivity” in **Hua, findings register, 2-chern-ring-gamma-comparison** (scans 021,022,029,030; unchecked), not a matching own result. Confidence is high under the explicit Noetherian/coherent interpretation; this is a conditional strengthening, not a transcription correction.


### S17 — Cote 2, scan 038 — Supported Riemann–Roch expression

**Kind:** unpursued implication.

**Anchor:** $\operatorname{ch}(i_!x)\operatorname{Todd}(X'/S)$.

For an embedding into a smooth ambient variety, the later singular Riemann–Roch construction combines the localized Chern character of an ambient resolution with the ambient Todd class to obtain a class on the support, and proves independence and proper covariance (Baum et al., 1975, I §6 and II §3). This makes the displayed expression a precise research lead, but the ordinary ambient Chern character alone can lose the supported class, as S08 and S16 demonstrate; a localized character supplies the missing supported target (The Stacks Project Authors, n.d., Tags 0FB0 and 0FET). Confidence is high in this comparison under its smooth-ambient, field, and rational-coefficient hypotheses, but it does not establish the sheet's unrestricted relative formulation. Context search S17 found no same-object result or ID in either context file.


### S20 — Cote 2, scan 036 — Nontrivial warning; group schemes versus inverse-image sheaves

**Kind:** unpursued implication / own idea.

**Anchor:** “n'est pas un cas particulier”; “au sens du changement de base pour les préschémas”.

The warning is mathematically substantive because base change of a group scheme and inverse image of its associated sheaf on the small étale site need not coincide. Our example takes algebraically closed $k$, $K=k(t)$, and $\mathbb G_m$: the small étale sheaf over $k$ is the constant sheaf $k^\times$, whose inverse image to connected $\operatorname{Spec}K$ still has global sections $k^\times$, whereas the base-changed group scheme has sections $K^\times$. Confidence is high in this explicit distinction, so the printed warning should be retained even where theorem numbers are in revision. Context search S20 found no corresponding result or ID in the supplied files.
