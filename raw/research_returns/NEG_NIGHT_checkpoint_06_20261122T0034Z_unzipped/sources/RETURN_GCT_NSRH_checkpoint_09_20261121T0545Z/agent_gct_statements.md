# Exact-source audit: GCT IV, VI, VII, VIII

Date: 2026-11-21 (Europe/Berlin). Run: `/root/gct_statements`. Model: GPT-6 Astra Pro, inherited effort (not independently exposed). This memo records source reading and mathematical interpretation. It does not record independent proofs of the cited research papers.

## 1. Main answer to the source-identification question

**None of the four attached versions formulates a nonstandard Riemann hypothesis with a category, finite-field objects, Frobenius operators, and specified weights.** GCT VI and VIII explicitly propose extending the methods surrounding finite-field RH and perverse sheaves, with conjectural canonical-basis properties as the intended consequence. GCT VII constructs quantum algebraic objects and points to the missing perverse-sheaf interpretations. The revised attached GCT IV develops substantial algebra and a two-row combinatorial result, but contains no occurrence of “Riemann”, “purity”, or “perverse” in the mathematical text. It points to the flip/positivity program via references to GCT VI and related articles.

Accordingly, a paper should not put a fabricated formula into quotation marks and call it “Mulmuley's nonstandard RH.” It can give an explicitly labeled **sufficient prospective realization/purity package**, then name its missing hypotheses.

### Versions checked

- **IV**: attached `LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex`, Blasiak–Mulmuley–Sohoni, matching arXiv **cs/0703110v4**, 6 June 2013, 145 pages. This is materially newer than the 2007 IV cited in VII/VIII. It proves Kronecker Schur–Weyl duality; do not inherit the conjectural status of VII for this case.
- **VI**: attached `LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex`, matching arXiv **0704.0229v4**, 22 January 2009, 139 PDF pages; title *The flip via saturated and positive integer programming in representation theory and algebraic geometry*. It already contains the relaxation after strict saturation failed.
- **VII**: attached `LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/main.tex`, arXiv **0709.0749v2**, 1 September 2008, 59 pages.
- **VIII**: attached `LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex`, arXiv **0709.0751v2**, 1 September 2008, 71 pages.

The displayed October/November 2018 dates on some arXiv rendered title pages arise from the sources' undated `\maketitle`; use arXiv version dates to identify versions. Numbered statements below were checked against the arXiv PDF text as well as the local source context. PDF page indices from web extraction start at 0; ordinary printed pages are specified when unambiguous.

### Exact RH/program locators

| Work | Locator in attached version | What is actually asserted |
|---|---|---|
| IV | §1.1, Problem **1.1** (`pintrokronecker`); §1.2–1.5; §19 | Positive combinatorial rule and stronger basis problem; construction program. No finite-field RH statement. |
| VI | Chapter 1 introduction, printed pp. 4–6, **Figure 1.1** | The proposed link to finite-field RH and extensions is marked by question marks. |
| VI | **§1.7**, Observation **1.7.1 (PH0)** (`obslusztig`), Figure **1.2** (`fbasicapp`) and last paragraph of §1.7 | Positive canonical bases motivate PH0, then PH1/SH; verification of the nonstandard conjectures is said to seem to need substantial extension of work around finite-field RH. |
| VI | **§4.2**, Proposition **4.2.1 (PH0)** (`plusztigkashi`); **§4.2.2**, Question **4.2.6 (PH0??)** (`queph0main`); **§4.3** (`squantumgroup`) | Standard canonical rings are quantized; asks for analogous compatible canonical bases and positivity for general structural constants. These are questions, not purity theorems. |
| VII | **§1**, after Conjectures **1.3–1.4**, source lines 335–364 | Missing interpretations of coefficients analogous to perverse-sheaf interpretations of KL/canonical constants prevent proving algorithm correctness. |
| VII | **§4.1**, equations **(9)–(10)** (`eqmult`, `eqcomult`), Theorem **4.4** (`tlaplace`); **§4.2**, Theorem **4.5** (`tlaplace2`) | Signed positive structural data would give nonstandard Laplace expansions; the needed interpretations are absent. No independently formulated RH. |
| VIII | **§1**, printed pp. 2–3, source lines 215–259 | An extension of perverse sheaves and underlying finite-field RH “seems necessary” for explicit minors and bases. |
| VIII | **§2.3**, following Conjecture **2.5**, printed pp. 13–14, source lines 980–1023 | Explicit interpretation of Laplace coefficients is the “basic core problem” behind correct efficient globalization. |
| VIII | **§2.4.2**, following Conjecture **2.7**, printed pp. 15–16, source lines 1111–1128 | Topological interpretation and Hard Lefschetz are suggested; a nonstandard extension dealing with nonflat, noncommutative algebras “may be needed.” |
| VIII | **§2.4.3**, after Conjecture **2.9**, printed pp. 17–18, source lines 1219–1240 | Speculates that nonflatness contributes a small correction, and an extension handling the Kronecker case may open the general case. |

## 2. The actual quantum objects and the actual positivity statements

Use a separate letter, e.g. **v**, for the quantum parameter in the new paper, and **Q** for a finite-field cardinality. All source occurrences of q below mean the quantum parameter unless explicitly stated otherwise. Substituting a prime power for this q is not a construction of Frobenius or a Weil sheaf.

### Objects

VII **Problem 1.1** and **Theorem 1.2**: (H\) is a complex connected classical reductive group, (X=V_\mu(H)\), (G=GL(X)\), and \(\rho:H\to G\) is the representation homomorphism. The plethysm constant is

\[
a_{\lambda,\mu}^{\pi}=\dim\operatorname{Hom}_H(V_\pi,\operatorname{Res}_\rho V_\lambda(G)).
\]

The standard quantum group is \(H_q\). The possibly singular nonstandard quantum object \(G_q^H\) is described through its matrix-coordinate bialgebra \(S=\mathcal O(M_q^H(X))\); see VII **§2**, equations **(4)–(6)** (`eqide`, `eqnonstd1`, `eqnonstd2`). Its defining generators \(u_j^i\) satisfy

\[
P^{+,H}_{X,X}(\mathbf u\otimes\mathbf u)=(\mathbf u\otimes\mathbf u)P^{+,H}_{X,X},
\]

where the projector separates the signs of the eigenvalues of the braiding of \(X_q\otimes X_q\). This is a relation in a noncommutative algebra over a field containing \(\mathbb Q(q)\), not a finite-field trace relation. The determinant can vanish, so VII explicitly says “quantum semigroup” would be the strict term (Theorem 1.2 discussion; §2). Finite-dimensional polynomial representations are comodules of S. Theorem **2.1** (`tnonstdformal`) supplies complete reducibility and Peter–Weyl statements. The dual algebra of its degree-r piece is the nonstandard q-Schur algebra \(\mathcal A_r^H\), VII **§3**, Theorem **3.1** (`tnonstdformalschur`). The dual nonstandard symmetric-group deformation is \(\mathcal B_r^H(q)\), VII **§5** (`sbr`).

For Kronecker, \(H=GL(V)\times GL(W)\), \(X=V\otimes W\). Revised IV constructs \(\mathcal O(M_q(\check X))\), its determinant localization and compact real form, and \(\check{\mathscr H}_r\subset\mathscr H_r\otimes\mathscr H_r\). Theorems **1.4/10.7** (source `t intro cmqg`/`tcmqg`) concern compactness; **1.5/12.1** (`t nonstandard schur-weyl duality`) gives actual Schur–Weyl duality. Its decomposition identity \(g_{\lambda\mu\nu}=\sum_\alpha n_{\lambda,\mu}^{\alpha}m_{\alpha\nu}\) appears in **§1.4, equation (11)** (`e ns Kronecker decomposition`).

No such object comes equipped in these texts with a scheme over \(\mathbb F_Q\), an étale site, an intersection complex, a geometric Frobenius, a middle degree, or a Tate-weight normalization. **Nonflat** is not in itself an obstruction to standard algebraic geometry: commutative nonflat schemes have étale sheaves. Here the immediate obstruction to directly writing \(\operatorname{Spec}S\) as an ordinary scheme is **noncommutativity**; nonflatness adds a separate specialization/reciprocity problem.

### VIII's basis existence/globalization prerequisites

- **Conjecture 2.2**, `clocalcrystalb`: embedding-independent local crystal basis \((L_\alpha,B_\alpha)\) compatible with Kashiwara operators for \(H_q\), with disjoint monomial supports.
- **Question 2.3**, `cbalance`: standard balanced triple. The text immediately says this fails in general, with examples in §5.3. Ordinary canonical-basis globalization cannot simply be copied.
- **Conjecture 2.5**, `cuniquemindegleft`: unique lift of minimum degree complexity. This is a construction/uniqueness conjecture, separate from positivity.
- **Conjecture 2.6**, `ccelldecompleft`: refined Peter–Weyl/cell property of \(CB(S)\), \(CB(\mathcal A)\), including restricted \(H_q\)-subcells.
- **Conjectures 3.1–3.2**, `cunimindegright`, `cunimindegright2`: minimum-degree globalization of the bases \(E(r)\), \(E^{opp}(r)\) on the dual side.
- **Conjecture 3.3**, `ccelldecompright`: cell decomposition giving irreducible modules.
- **Conjecture 3.7**, `coppquasicell`: the **opposite** basis has quasi-subcells whose specialization gives composition factors/Specht modules, with KL basis after normalization. The text explicitly warns that this property need not hold for E(r) itself.

VIII **Proposition 2.4** (`eta` embedding statement, unlabeled proposition in source) has the printed proof “The proof is easy. (To be filled in).” It is a cited assertion with omitted proof, not a proof checked in this run. Its lattice conclusion assumes Conjecture 2.2. This should not be recorded as independently re-proved.

### Precise Kronecker positivity (VIII 2.7 and 3.4)

**Conjecture 2.7**, `cposkroneckerleft`, says that every coefficient g(q) of a canonical-basis element of \(\mathcal A_r^H\) in the external canonical basis \(CB(Z)\), \(Z=\operatorname{End}(X_q^{\otimes r})\), is a polynomial with **nonnegative rational coefficients**. The relevant expansion is **equation (9)**, `eqyincanZ`. Its multiplicative/comultiplicative structural constants have the form

\[
\pm(q-q^{-1})^a f(q),\quad a\in\mathbb Z_{\ge0},
\]

where f is bar-invariant, coefficientwise nonnegative rational, and unimodal in the displayed sequence of Laurent exponents. The same statement is asserted for \(CB(S)\).

**Conjecture 3.4**, `cposkroneckerright`, applies to structural constants and external expansion coefficients of E(r), and likewise Eopp(r). They have the form

\[
\pm(q^{1/2}-q^{-1/2})^a f(q),
\]

with nonnegative rational, bar-invariant, unimodal Laurent f in \(q^{1/2}\). Relevant external expansion: **equation (13)**, `eqexpincanZright`.

Thus even “Kronecker positivity” here is not the assertion that all raw multiplication constants have nonnegative coefficients. A raw constant can have a minus sign and a vanishing factor. A prospective geometric interpretation must explain the normalization/factors and rational denominators. A dimension of one graded vector space is an integer, whereas a normalized dimension divided by a specified positive integer can be rational.

### General plethysm positivity (VIII 2.8–2.9 and 3.5–3.6)

The external coefficients can be algebraic over \(\mathbb Q(q)\). VIII discusses the coefficients of their minimal polynomials. On the coordinate side **Conjecture 2.8** (`cnonstdposleft0`) asks for positivity at q=1 of the normalized data; multiplicative/comultiplicative polynomial coefficients are written as

\[
(-1)^e(q-q^{-1})^{e'}c(q) \quad\text{(equation (10), `eqbexpli2`)},
\]

with c saturated, meaning \(c(1)>0\) for nonzero c, after a prescribed sign normalization. **Conjecture 2.9**, `cnonstdposleft1`, asks for \(c=c^0+c^1\) with dominant nonnegative unimodal c0 and small correction c1, including

\[
\|c^1\|_2/\|c^0\|_2\le1/\operatorname{poly}(\langle\mu\rangle,\langle\pi\rangle,\langle r\rangle),\qquad c^0(1)\gg|c^1(1)|.
\]

This is not a complete uniform quantitative assertion: the polynomial and the asymptotic “much greater” must be fixed before it can be a precise theorem target.

On the dual side **Conjecture 3.5**, `cnonstdposright`, uses

\[
s(q)=(-1)^e(q^{1/2}-q^{-1/2})^{e'}g(q) \quad\text{(equation (14), `eqbexpli3`)},
\]

and **Conjecture 3.6**, `cnonstdposright1`, is explicitly titled “Nonstandard Positivity, informal,” with the same dominant-positive-plus-small-correction pattern.

The motivation is real negative coefficients, not only absence of a proof. VIII **§5.4.1**, **Figure 30** (`fmult7_3`), gives the normalized vector for \(c(v_5^1,v_5^1;v_5^1)\), with final entries

\[
-68,-101,-90,-64,-38,-18,-6,-1.
\]

The paper describes positive rescaling factors used before this positivity study; these conventions must accompany any claimed counterexample. We read the displayed computation, but did not recompute the entire 21-dimensional algebra. Its status is **carried as background without fault found**, with targeted reading of the sign entries; it is not a formal certificate generated in this run.

**Normalization caveat, not a refutation of the intended program.** Conjecture 2.8's first sentence literally requires every coefficient of a minimal polynomial to be saturated. With the ordinary monic convention f1(T)=T−1, this fails for the coefficient −1. However §5.4.1 calls both trace and norm coefficients of the minimal polynomial, suppressing the conventional minus on trace. This makes a signed-elementary-symmetric convention plausible. The proper conclusion is that a precise target must specify those signs; do not use this editorial ambiguity as a claimed disproof of the intended positivity conjecture.

Also, “Frobenius automorphisms” in VIII §5.4.1 source line 2375 means conjugations of an algebraic extension K/\(\mathbb Q(q)\) used to form trace/norm. It supplies **no** arithmetic Frobenius over a finite field and no Weil-weight statement.

## 3. Deduction chain, with all independent gates named

This is a reconstruction of the proposed program, not a theorem claimed by the source.

1. **Realization gate.** Construct spaces/categories over finite fields (or a rigorously defined replacement) realizing the nonstandard algebras and the designated bases. Identify the quantum variable with a grading/Tate normalization, not with field size by notation alone.
2. **Weight gate.** Specify actual Weil complexes and their cohomology groups, integer/rational weights, and Frobenius actions. Prove weight purity. A proposed trace-bound lemma can address this gate only after the complexes and trace formula have been supplied.
3. **Positive-multiplicity gate.** Identify the basis constants with coefficients of decompositions into simple objects, or actual graded dimensions. A pure trace need not be a positive dimension. Parity/Tate information, semisimplicity/decomposition, and normalization have separate jobs.
4. **Duality/self-duality and Lefschetz gate.** Explain bar invariance and unimodality. Hard Lefschetz-type injections, or an \(\mathfrak{sl}_2\)-action, are extra to purity. Explain signed \((q-q^{-1})^a\) or half-power factors and rational normalizations.
5. **Basis gate.** Prove local crystals, uniqueness of minimum-degree globalization, and identification of any geometric basis with VIII's designated algebraic bases (Conjectures 2.2, 2.5, 3.1–3.2). An arbitrary positive basis does not prove positivity of the specified basis.
6. **Cell gate.** Establish VIII 2.6, 3.3, 3.7 and the specialized Specht/quasi-subcell descriptions. Positivity of constants alone does not establish the required cell irreducibility or specialization.
7. **Plethysm comparison gate.** General VII **Conjectures 1.3–1.4**, refined **Conjecture 6.1**, give
   \(a_{\lambda,\mu}^\pi=\sum_\alpha m_\lambda^\alpha n_\pi^\alpha\), where n counts Hq constituents and m counts Specht constituents after q=1. In revised IV the Kronecker decomposition and duality are established, so that part of this gate is already removed in that case.
8. **Effective-label gate.** VIII **§6** (`scomplexity`), printed p. 68, explicitly calls for *additional* complexity-theoretic properties of basis labels and crystal/cell operations, “to be described in the full version.” A basis indexed by an unboundedly difficult set does not give a #P formula. Need polynomial-length witnesses and polynomial-time verification (with the specified encoding).
9. **Polyhedral gate.** A #P counting formula is weaker than VI **Hypothesis 1.6.4 (PH1)**: a rational polytope with exact Ehrhart stretching function, polynomial ambient dimension/entry bitlength, and polynomial separation/membership oracle. PH1 requires more than canonical positivity or an abstract count.
10. **Saturation/index gate.** VI **Hypothesis 1.6.5 (SH)** asks for polynomially bounded saturation index and asymptotic generic saturation; **1.6.6 (PH2)** for polynomially bounded positivity index; **1.6.7 (PH3)** for polynomial modular index of a positive Hilbert-series form. Literal strict saturation is not assumed in the attached revised VI. **Theorem 1.6.8** gives relaxed PHflip from PH1+SH, with the hypotheses retained.
11. **Obstruction/existence gate.** Efficiently testing positivity does not itself construct a multiplicity inequality between the determinant and permanent orbit closures. The strict inequality and an effective family of such obstructions remain additional. The standard “flip” isn't the implication “finite-field RH implies P≠NP.”

### Stretching-convention discrepancy in VI

VI **§1.6**, source lines 1169–1178, defines the stretching function as \(\widetilde a(n)=a_{n\lambda,\mu}^{n\pi}\), expressly holding \(\mu\) fixed. PH1 Hypothesis 1.6.4 uses that stretching. Yet **Theorem 1.6.8(a)** prints \(a_{b\lambda,b\mu}^{b\pi}\), and its proof applies fixed-\(\mu\) PH1. The direct consequence of the displayed hypotheses is the **fixed-\(\mu\)** version \(a_{b\lambda,\mu}^{b\pi}\). Preserve this source discrepancy rather than silently changing which weights are stretched. Merely reporting the relaxed-decision implication avoids propagating the typo, but a fully exact reconstruction should name it.

VI **Proposition 4.2.1** is slightly more nuanced than the compressed introduction: it gives compatible canonical bases for the standard canonical rings, and the following paragraph calls positivity of their structural constants conjectural. Its citation is to Lusztig *Introduction to Quantum Groups*, **Chapter 27**, and Kashiwara *Global crystal bases of quantum groups*, **Theorem 2**. The standard Uq− canonical-basis positivity should not silently be conflated with every coordinate-ring normalization in that paragraph.

## 4. Template dictionary suitable for the parent paper

| Standard ingredient | Actual role | Nonstandard replacement supplied | Missing ingredient |
|---|---|---|---|
| Split reductive group/flag variety G/B and Schubert varieties Xw over finite fields | Algebraic geometric source of IC complexes and Hecke convolution | Hq and noncommutative FRT bialgebra S; external Hecke tensor-product ambient algebra Z | A space or categorical replacement whose strata correspond to the designated nonstandard basis |
| ICw with prescribed shifts/Tate normalization | Distinguished simple/pure objects yielding KL basis | Candidate minimum-degree bases CB(S), CB(A), E(r), Eopp(r) | IC objects and proof that their classes equal these candidates |
| Weil Frobenius | Defines weights through eigenvalues at all closed points | None; bar q↦q−1 is algebraic involution, not Frobenius | Arithmetic models, Weil structures and trace functions |
| Purity of IC and weight stability under proper maps | Prevents unsuitable weight mixing; input to semisimplicity | No corresponding finite-field assertion | Precise purity theorem; bound alone is insufficient without degree support/no-cancellation |
| Proper convolution maps and decomposition theorem | Express product as sum of shifted simple perverse objects with nonnegative multiplicities | Multiplication/comultiplication in S and A/B | Geometric/categorical convolution and properness/semisimple decomposition |
| Parity/Tate stalks and normalized character map | Identifies trace expressions with graded nonnegative dimensions | Signed rational Laurent forms conjectured in VIII | Parity, Tate eigenvalue phases, denominators/signs, character identification |
| Verdier duality | Bar symmetry | Algebraic bar involution | Compatibility with a geometric duality |
| Relative Hard Lefschetz | Unimodality of normalized graded multiplicities | f(q) unimodality conjectured | Projective correspondence and Lefschetz operator/\(\mathfrak{sl}_2\)-module |
| Crystal/path/tableau models | Effective labels and counting highest weights | Conjectural cells; two-row IV actual tableaux | Effective labels/operations for general n, r |
| Lusztig quiver/flag constructions for quantum groups | Standard positive canonical bases beyond direct Schubert Hecke case | Nonstandard minors/canonical coordinate algebras | Realization of the actual nonstandard coefficients |

Do not write that every standard quantum-group canonical basis is obtained directly from a single Schubert variety. The KL Hecke case is the useful prototype; the analogous quantum-group constructions use additional geometric machinery (e.g. Lusztig's quiver/flag settings).

## 5. Known positive cases already available, independent of Alpöge's step 5

Revised IV **Theorem 1.6** (`t intro main theorem advertisement`), sharpened as **Theorem 15.21**, especially (vii) and (viii), gives

\[
g_{\lambda\mu\nu}=\#\{T\in{}^+\mathrm{HNSTC}(\nu): T\text{ highest weight of weight }(\lambda,\mu)\}
\]

for \(\ell(\lambda),\ell(\mu)\le2\); \(\nu\) has at most four parts in the GL4 setting. It also gives symmetric/exterior counts by the eigenvalue of the swap \(\tau\). These are **cited existing results**, not findings of this run and not consequences newly obtained from the sign argument. IV **§18** supplies explicit positive formulas; IV **Theorem 17.7** (`t positivity`) gives the stated action-coefficient property. The basis of \(\check X_\nu\) constructed there is not automatically a proof of VIII's full coordinate/dual canonical-basis conjectures for arbitrary rank and r.

This special case includes rectangular partitions with two rows when those are the two Kronecker factors, but not arbitrary n-row rectangles in the asymptotic determinant/permanent regime. The other agent should state the exact Ikenmeyer–Panova/Bürgisser–Ikenmeyer–Panova hypotheses.

## 6. Candidate check events for the root audit trail

The following events describe what happened, not more:

- SRC-GCT-PROGRAM: **used and rechecked in this run** — read full relevant introductory/positivity sections in VI/VII/VIII, searched all four attached source files for RH/purity/Frobenius, checked numbered locators against matching arXiv PDFs. Outcome: no formal nonstandard finite-field RH statement; programmatic proposed extension confirmed.
- SRC-VIII-2.7-3.4: **used and rechecked in this run** — read entire conjectures and preceding/following definitions. Outcome: signed factors, rational coefficients and unimodality included; raw coefficientwise positivity would misstate them.
- SRC-VIII-GENERAL: **used and rechecked in this run** — read 2.8–2.9, 3.5–3.6, §5.4.1 and figure data. Outcome: corrections and negative entries confirmed; normalization ambiguity recorded. Full experimental algebra not recomputed.
- SRC-VII-1.3-1.4-6.1: **used and rechecked in this run** — read exact conjectures and multiplicity identity. Outcome: general comparison remains conjectural in this source.
- SRC-IV-12.1: **carried as background without fault found** — exact theorem statement and use in §1.4 read; proof of whole research theorem not independently reproved.
- SRC-IV-15.21: **carried as background without fault found** — exact theorem statement, introductory explanation and scope read; long proof not independently rechecked in full.
- SRC-VI-PH: **used and rechecked in this run** — exact PH1/SH/PH2/PH3 statements and adjacent deduction read; no new proof claimed.
- SRC-VIII-COMPLEXITY: **used and rechecked in this run** — entire §6 read. Outcome: effective-label properties are explicitly additional and not fully specified.

## 7. Primary web retrieval IDs (root must open before citing in chat)

- IV: https://arxiv.org/pdf/cs/0703110 — `turn128831581view2`; selected duality locator `turn720157863view1`.
- VI: https://arxiv.org/pdf/0704.0229 — `turn535935867view0`; PH locators `turn778071149view0`; PH0 Question4.2.6 `turn778071149view2`.
- VII: https://arxiv.org/pdf/0709.0749 — `turn128831581view1`; refined reciprocity `turn711787842view1`.
- VIII: https://arxiv.org/pdf/0709.0751 — `turn128831581view0`; 2.7–2.9 `turn764193458view0`; 3.3–3.7 `turn764193458view1`; Figure30 `turn720157863view0`.

All substantial content in this memo was read from the user-provided LaTeX. Web PDFs were used mainly to verify numbering and version information, not to substitute snippets for source reading.
