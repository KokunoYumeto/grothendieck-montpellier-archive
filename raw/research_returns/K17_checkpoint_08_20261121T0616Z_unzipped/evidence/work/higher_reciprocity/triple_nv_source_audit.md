# Source audit for the actual cubic companion obstruction

Author/reviewer: `/root/tripod_integral`, GPT-6 Astra Pro. Date: 21 November 2026.

## Outcome and exact scope

The papers checked below supply an exact formal description of generalized Bockstein maps by **specified proper defining systems**. They also identify a full Bockstein cokernel with an augmentation-graded Iwasawa cohomology module. They do **not**, in the results checked here, prove the rootwise nonvanishing of the actual cubic companion used in `odd_torsion_cubic_section.tex`.

There is a useful precise reduction: the missing arithmetic assertion is a support statement for the image of a specified universal three-input family, after localization away from the proper pair factors. It is not the statement that some ordinary triple Massey product contains a nonzero value. The actual-extension comparison has now been written by `/root/archive_kummer` and independently whole-audited here; the final checked comparison and its exact scope are recorded below.

Two tempting substitutions fail. First, a theorem giving eventual nonzero higher Bocksteins does not force the degree-two Bockstein. Second, a norm-compatible cyclotomic-unit family has coherently **zero** obstructions in the repeated *cyclotomic* direction. That direction differs from the three independent free-quotient directions in the cubic criterion.

## The target being tested

Let \(M=H^{\mathrm{ab}}\), let \(T\) be its Iwasawa torsion, and put \(Q=M/T\). In the assigned-degree filtration, the actual odd companion belongs to the extension

\[
0\longrightarrow W_3\longrightarrow E_3\longrightarrow T_a\longrightarrow0,
\qquad W_3=L_3(Q)\oplus[Q,T^+].
\]

The direct sum describes rational coordinates. The action of \(\Gamma\) mixes the second term into the first through the already fixed even companions. If \(q_a\) is the odd companion polynomial and \(z_i=1+T_i\), the actual target coefficient satisfies

\[
q_a(z_1z_2z_3)B_a=\mathcal C_a.
\]

Here \(\mathcal C_a\) is meromorphic only along the proper adjacent-pair divisors. For every root \(\alpha\) of \(q_a\), Triple-NV requires a matching ordered odd-character triple whose numerator is nonzero on \(z_1z_2z_3=\alpha\). Repeated roots are retained; testing only a simple-root quotient of a different extension is insufficient.

The expected dual root is \(u^3/\alpha\), with character \(\omega^{3-a}\). This twist and the actual proper defining system must occur in any source comparison. No statement below identifies them merely by comparing characteristic polynomials.

## Primary-source ledger

### A. Lam–Liu–Sharifi–Wake–Wang, generalized Bocksteins (2023)

Primary: [author PDF](https://www.math.ucla.edu/~sharifi/augmentation.pdf); [publisher](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/generalized-bockstein-maps-and-massey-products/303B92F7CDE917179CC9253AAEBF2A6A). Retrieval refs: `turn393332360search9`, `turn947254061view0`. Published as *Forum of Mathematics, Sigma* 11 (2023), e5, DOI 10.1017/fms.2022.103.

Read in full: author-version §§2.1–2.2, §§3.1–4.1, §4.6, and §5, including all proofs in those sections. Important locators: Theorem2.2.4 pp15–16; Remark2.2.5 p17; Definitions3.1.3/3.2.1/3.2.2 pp21–23; Theorem4.1.2 pp28–29; Theorem4.6.3 p39; Corollary4.6.4 p40; Example5.2.7 pp45–46. The general defining-system definition allows all matrix-entry coefficient twists. The single-twisted-module restriction begins only after Definition3.2.2 and applies to the later specialized Bockstein comparison.

Theorem4.1.2 identifies the image of a generalized Bockstein under a fixed coefficient map with the proper Massey value attached to its input cocycle. Theorem2.2.4 identifies the full cokernel with \(I^nH^d_{\rm Iw}/I^{n+1}H^d_{\rm Iw}\). Neither asserts this module vanishes. The Heisenberg calculation gives four proper triples for \(\Psi^{(2)}\); \(\Psi^{(3)}\) instead gives fourfold products. The arithmetic applications impose Vandiver/cyclic-class hypotheses and yield class-group lower bounds. Example5.2.7 has a zero degree-two Bockstein for its specified quotient. This is not a counterexample to our different Triple-NV assertion.

### B. Qi: the current author revision, not only arXiv2024

Primary: [arXiv2402.06028](https://arxiv.org/abs/2402.06028); [author research page](https://peikaiqi.github.io/math/index.html); [author PDF dated18October2026](https://peikaiqi.github.io/math/Iwasawa%20lambda%20invariant%20and%20Massey%20product.pdf). Retrieval refs: `turn947254061view1`, `turn803369376view0`, `turn336034329view0`.

Read complete relevant proofs in both versions. Current locators: Lemma10, Theorems11–13 pp13–15; Theorems14–16 pp15–18; Theorem35 p35. The 2024 numbering is different.

Theorems12–13 say that norm-compatible unit classes lift to full Iwasawa coefficients, hence admit a coherent sequence of vanishing proper products in the repeated cyclotomic direction. Theorems14/16 detect the first nonzero Bockstein, under explicit cohomology-dimension and no-finite-submodule hypotheses; they do not bound that first degree by two. Theorem35 treats odd class-group characters, not the remaining reflected even class-group support of our odd torsion. The new revision also corrects the local corestriction discussion and replaces an imprecise torsion condition by the appropriate finite-submodule condition. This audit uses the current proof.

### C. Sharifi, restricted ramification (2022)

Primary: [arXiv1609.03616v3](https://arxiv.org/abs/1609.03616). Retrieval ref: `turn947254061view2`. Published in *Transactions of the AMS* 375 (2022),5361–5392.

Read complete §§3.1–3.2 and §4. Locators: Theorem3.1.4 pp21–22; Corollary3.1.6 p23; Theorem3.2.1 p25; Theorem4.1.2 and proof pp27–29; Theorem4.2.2 pp30–31.

The first results compare degree-one reciprocity maps and impose an antisymmetry relation on cup values. The higher theorem gives the augmentation-graded cokernel equivariantly. Its completed-tensor formulation explicitly allows a quotient group that is not finitely generated. The six-term sequence in §4.2 assumes that the extension group is \(\mathbb Z_p\); its additional class-group and local-reciprocity terms are genuine obstructions. These results can organize a proposed cubic calculation, but do not establish its nonvanishing.

### D. Sharifi, extension of the Fukaya–Kato method (2026)

Primary: [author PDF](https://www.math.ucla.edu/~sharifi/publ/fkmethod.pdf); [journal](https://ems.press/journals/jems/articles/14298089). Retrieval refs: `turn356380275view2`, `turn858079670search0`. *JEMS*28 (2026),2877–2943; DOI10.4171/JEMS/1519.

Read §§5.4–5.5, including Theorems5.21/5.25 and the surrounding proofs, and all of §6. Locators in the author PDF: pp56–63 and64–72; Questions5.26/6.15; Propositions6.14/6.18.

The intermediate-zeta-map existence statement is equivalent to a Sharifi conjecture in the indicated setting. The stronger compatibility is posed as a question. In the test case, the extra norm relation is obtained under vanishing of the relevant completely split Iwasawa component; absent that vanishing, a splitting of another exact sequence remains required. The test case also has tame-level and character restrictions. It cannot be used to remove our remaining even class-group support without supplying the missing hypothesis.

### E. Sharifi, through the lens of the Eisenstein ideal (October2026)

Primary: [author PDF](https://www.math.ucla.edu/~sharifi/publ/program.pdf), arXiv2610.04943. Retrieval refs: `turn219348183view0`, `turn281558917academia6`. The author PDF has25pages.

Read the complete relevant constructions and all displayed proof outlines on pp8–23: the map \(\Upsilon\), Theorem8, Euler-system Steps1–6, Theorem10, and Remark11. The paper expressly defers some full construction details to work in preparation; this audit does not label those outlines full proofs.

The geometric construction yields an actual cyclotomic-unit extension, norm relations, and character-wise nontriviality. Theorem1's Eisenstein factorization does not imply surjectivity. Isomorphism and inverse-map assertions remain Conjectures2/6/7. Remark11 is a universal cup-symbol reciprocity map. Remark9 corrects earlier sign/factor-two conventions; these are units for odd primes and do not alter our unit/nonvanishing gates. The construction does not identify a class-three companion or prove a three-input residue nonzero.

### F. Ray–Sujatha, fine Selmer groups (2026 revision)

Primary: [arXiv2508.17156v2](https://arxiv.org/abs/2508.17156). Retrieval ref: `turn356380275view0`. Local PDF dated8September2026.

Read complete Theorems6.2/6.9/6.10, Corollary6.11, and Theorems7.1/7.3 with their proofs, pp19–28. Theorem7.1 says that a fine-Selmer \(\mu=0\) condition is equivalent to spanning by proper repeated-cyclotomic products at **some** order. It has neither a fixed cubic bound nor restriction to our chosen universal family. The first-layer argument in Theorem7.3 needs an additional justification at orders at least \(p\); see the explicit caution below. No result of this audit depends on that theorem.

### G. Older arithmetic formulas and current finite formulas

Sharifi, [*Massey products and ideal class groups*](https://www.math.ucla.edu/~sharifi/publ/massey.pdf), author version26July2006, published2007. Retrieval ref `turn540069763view1`. Read all of §6 and §7, including Theorem6.3, Corollary6.4, Propositions6.5–6.6 and7.2–7.5. These describe repeated Kummer-direction products through augmentation-graded class modules. Universal norms form the intersection of their vanishing stages. They do not give a uniform cubic stage. Proposition7.4 explicitly permits a surviving second augmentation piece with the corresponding triples zero.

Ahlqvist–Carlson, [arXiv2207.06353v7](https://arxiv.org/abs/2207.06353), published *Crelle*823 (2025),61–112. Retrieval ref `turn540069763view0`. Read Lemma4.11 and Theorem4.12 with their entire proofs, pp28–31, and Remark4.14. The ideal/norm formula computes a finite repeated-input triple modulo its indeterminacy. A compatible universal defining-system comparison and a rootwise arithmetic nonvanishing argument would still be needed here.

## Three elementary checks that prevent invalid inferences

### 1. A full coefficient lift kills its own connecting obstructions

Let \(\Omega\) have augmentation ideal \(I\), and suppose \(f\in H^1(G,T\widehat\otimes\Omega)\). Write \(f_n\) for its reduction modulo \(I^n\). In the cohomology sequence of

\[
0\to T\otimes I^n/I^{n+1}\to T\otimes\Omega/I^{n+1}
\to T\otimes\Omega/I^n\to0,
\]

the class \(f_n\) lies in the image of \(f_{n+1}\). Exactness gives \(\Psi^{(n)}(f_n)=0\) for every \(n\). This proves the relevant implication directly, with no choice-of-defining-system shortcut. It says nothing about a different quotient or different family of partial lifts. In particular it does not make the actual three-free-direction obstruction zero.

### 2. Eventual augmentation termination gives no cubic bound

Take \(X=\mathbb Z_p[[x]]/(x^r)\), with arbitrary \(r>2\). It is finite free of rank \(r\) over \(\mathbb Z_p\), has \(\mu=0\), and has no nonzero finite submodule. Its reduction \(A=X/pX=\mathbb F_p[[x]]/(x^r)\) is finite, but

\[
x^2A/x^3A\ne0,\qquad x^rA=0.
\]

Consequently a cokernel formula of the form in LLSWW is compatible with a nonsurjective degree-two map and eventual surjectivity. This is a formal module counterexample to an inference, not an arithmetic counterexample to Triple-NV. Additional arithmetic information must bound or annihilate the relevant degree-two quotient.

### 3. Residual first-layer data do not fix all proper binomial systems

For \(G=\mathbb Z_p^2\), take continuous surjections \(\kappa(s,t)=s\) and \(\kappa'(s,t)=s+pt\). They agree modulo \(p\). At \(g=(0,1)\), however,

\[
\binom{\kappa(g)}p=0,\qquad
\binom{\kappa'(g)}p=1\pmod p.
\]

Thus the standard proper upper-triangular block at order at least \(p\) remembers more than the first layer. This identifies the exact missing justification in the quoted first-layer argument; it does not disprove its final arithmetic theorem. It also explains why an eventual-order criterion cannot automatically be transported using only a residual character.

## A precise conditional bridge to the cubic gate

Write \(\mathscr A\) for the bounded-denominator three-variable ring after inverting the actual proper pair factors. Fix an odd companion root \(\alpha\), and let \(K_\alpha\) be the fraction field after imposing \(z_1z_2z_3=\alpha\). All of these rings must be formed in the bounded-denominator category; replacing \(\mathbb Z_p[[T]][1/p]\) by unrestricted \(\mathbb Q_p[[T]]\) is not permitted.

An application of the source theorems needs the following four concrete steps.

1. **Actual coefficient sequence.** Construct the upper-triangular partial system from the actual class-two companions, with its compatible topology and coefficient action. Identify its connecting class with the pushout of the actual \(E_3\). In particular, the \(XY\) and \(YX\) contributions cannot be discarded when fixing the defining system.

2. **Root quotient and duality.** Identify the relevant quotient of the Bockstein target with the dual \(u^3/\alpha\), \(\omega^{3-a}\) component. For a repeated root, use the cyclic module's socle and dual root quotient, not an unsupported generic-character specialization. Verify localization and completed-tensor base change before passing to \(K_\alpha\).

3. **Specified input family.** Let \(\mathscr S_{\rm cyc}\) be the cocycles obtained from the norm-compatible cyclotomic families using these actual partial systems. Prove that their projected obstruction map

   \[
   \mathscr S_{\rm cyc}\longrightarrow K_\alpha
   \]

   is the collection of the restrictions \(\mathcal C_{a;b,c,d}|_{z_1z_2z_3=\alpha}\), up to nonzero factors. Nonzero one-variable cyclotomic multipliers alone suffice to remove those factors on the generic divisor; they do not prove the resulting obstruction is nonzero.

4. **Arithmetic image support.** Prove that this projected map is nonzero for each root. Since the target is a field line, this is equivalent to spanning it. This last assertion is not supplied by the checked source theorems.

For the **full** Bockstein source, the formal exact sequence identifies its cokernel with an augmentation-graded Iwasawa cohomology module. After a legitimate flat base change and a surjection to the desired root line, vanishing of that cokernel is a sufficient full-source condition. To restrict to \(\mathscr S_{\rm cyc}\), one must also prove that this family generates the projected image. Neither condition follows just from the existence of the cokernel identification.

This formulation separates two possible future arithmetic approaches. One may prove the rootwise image statement directly for the universal family, or prove vanishing of the corresponding augmentation quotient together with the image-generation statement. The checked papers give tools for computing those objects, but the required computation remains open in this run.

## What has and has not been exhausted

The direct routes through the stated LLSWW, Qi, and Sharifi2022 results have been checked against their entire relevant proofs. Two newer2026 sources, the2026 author revision of Qi, and the2007/2025 finite formulas were also checked. None proves the current gate by the proposed substitutions. This is a statement about those precise routes, not a claim that no theorem anywhere can imply Triple-NV.

The next arithmetic step is to prove nonvanishing of the explicit class in the checked comparison below, or to identify it with a specified image for which a rootwise support theorem is available. No full kernel theorem, new Greenberg case, or unconditional cubic nonvanishing is promoted by this note.

## Subsequent completed actual-class comparison

The complete `work/cubic_twisted_obstruction_section.tex`, final reviewed SHA-256 `46013fd13c4f54c9969ce5dae1774452a342330b311af422d71d4634af9f1994`, has now passed an independent whole-proof audit. The detailed review is in `work/cubic_uppertriangular_tripod_audit.md`; check event TC107 records the actual review.

It constructs the actual partial triangular system from the class-two companions, clears the proper-pair denominators compatibly, and defines the twisted central cocycle

\[
c=x_1\cup B_{23}+B_{12}\cup x_3.
\]

A specified rank-four coefficient extension has connecting class exactly c. Its class in the algebraic localization of the continuous A-valued cochain complex is nonzero if and only if the actual cubic residue is nonzero. The proof retains each complete cyclic companion, so repeated roots cause no additional hypothesis. It supplies bounded lifts in both directions rather than identifying this localized complex with all function-field-valued continuous cochains. The actual norm-compatible cyclotomic inputs differ from the abstract rank-one inputs by nonzero generic-divisor multipliers; a single scalar coboundary also identifies their localized global H1 classes, while the actual pair defining system remains fixed.

Thus the actual extension, compatible coefficient topology, defining system, repeated-root test, and input normalization are now explicit. What is still missing is an arithmetic nonzero image in this **specific** coefficient extension for each required root. The comparison does not turn the rank-four coefficient extension into the augmentation sequence in LLSWW by assertion, and it supplies no vanishing of that sequence's cokernel. The source mismatch and the arithmetic image-support gap remain exactly as described above.

## Local source files and reproducibility

All PDFs and extracted texts are under `work/higher_reciprocity/`. The accompanying `triple_nv_source_manifest.json` records their hashes. Reads are recorded separately in `work/tripod_checks.tsv`. Downloaded source statements and author proof sketches are distinguished above from independently supplied elementary arguments.
