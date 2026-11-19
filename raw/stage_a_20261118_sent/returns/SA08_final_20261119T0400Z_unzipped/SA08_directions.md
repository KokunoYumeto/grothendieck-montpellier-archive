# SA08 — ranked research directions

**Scope and date:** cote 136, this supplied part only; assessment as of 19 November 2026. These are task specifications, not developments of the proposed research. The elementary proofs and counterexamples in the dossier check existing assertions; they are not presented as new research. Canonical IDs below refer to the consolidated tables. Retired packet IDs are resolved in `SA08_id_aliases.tsv`.

The rank weighs mathematical interest first and the chance of obtaining a decisive, reviewable result in one run of a few hours second. A feasible first step can be a precise obstruction or a hypothesis comparison; it need not settle the entire programme.

| Rank | Direction | Interest | What one run could realistically deliver |
|---:|---|---|---|
|1|Multiplicative recovery from weighted shadows|Very high|An exact tensor-compatibility statement and the first unresolved coherence diagram|
|2|Choice independence of admissible PD theories|Very high|A hypothesis-by-hypothesis comparison with a precise uniqueness theorem|
|3|The correct infinite shadow quotient|High|A theorem/counterexample separating the literal and repaired negligible classes under a specified finiteness condition|
|4|The half-differential-algebra product obstruction|High|The first actual extension-class calculation for a small bidegree|
|5|Universal divided-power convolution data|High|A complete axiom table and a decisive low-rank existence/uniqueness test|
|6|Filtered and completed coefficient comparison|High|A clean associated-graded lemma and a list of genuinely required completion hypotheses|
|7|Test embeddings and relative coefficient comparison|High|One exact slice/relative criterion, with a proof or counterexample|
|8|Natural splittings of the simplex sequences|Medium–high|An integral obstruction in the first relevant weight and its localization behaviour|
|9|Natural operation complexes and coherence across arities|High|A correct small-arity formulation separating naturality, freeness and operadic composition|
|10|The unfinished additive-group Ext induction|Medium–high|A line-by-line match of one edge-map lemma with the later published construction|
|11|The curve bundle and Euler normalization|Medium|A definitive list of the geometric hypotheses and the bundle actually required|
|12|The divided-power versus exterior-power normalization question|Medium|A scan-resolved statement and a small, integral derived-functor table|

## 1. Multiplicative recovery from weighted shadows

**Origins:** items SA08-16, SA08-58, SA08-438; claims SA08-C013, SA08-C015, SA08-C226; problem MP-SA08-04.

**Target.** Specify whether the recovered object carries only the ordinary cohomological pairing, a derived tensor comparison, or a coherently multiplicative structure, and prove the strongest of these that the chosen shadow category supports. This would identify the precise extra information still missing after linear recovery.

**Known boundary.** Cartan's weight-dependent product is already published: weightsr, s contribute the factor \(\binom{r+s}{r}\), and sufficiently large compatible weights recover the ordinary cup pairing because these factors generate the unit ideal. The finite nonnegative derived recovery is also checked in this dossier. Neither statement alone makes the recovery functor strongly monoidal or supplies all higher operations. Cenkl–Porter's DASH/bar construction and higher products offer precise comparisons with their own structures and coefficient ranges. [@Cartan1976, §7 p. 271; @CenklPorter1982, Theorems 1–2]

**First concrete step.** Write the binary tensor comparison and its associativity square in one explicitly chosen finite-cutoff category, retaining both gradings and the binomial coefficient. Determine whether the square can even be formulated before passing to the proposed infinite quotient. Do not replace this by a claim about an unweighted integral PD cohomology ring.

## 2. Choice independence of admissible PD theories

**Origins:** items SA08-98, SA08-201, SA08-212, SA08-234, SA08-309; claims SA08-C064, SA08-C114, SA08-C115, SA08-C188; problems MP-SA08-26, MP-SA08-34, MP-SA08-35.

**Target.** State and prove a comparison theorem for the actual category of admissible generalized PD theories: connectedness, simple connectedness of the localization groupoid, or a stronger uniqueness result, with those three targets kept distinct.

**Known boundary.** A morphism compatible with two established comparison isomorphisms is already a quasi-isomorphism by two-out-of-three. That formal observation does not prove the existence of common refinements or the Ore/equalization conditions. Mandell's *Cochain Multiplications* gives a precise uniqueness theorem for an enhanced cochain theory satisfying explicit axioms. No equivalence between that target and this historical PD/\(\tau_\infty\) category was located. [@Mandell2002, Main Theorempp 548–549 and Uniqueness Theorem] Guillén–Navarro–Pascual–Roig provide a closer monoidal acyclic-model comparison, but require a PID base, free bidegree modules, simplexwise cochain homotopy equivalence and degreewise simplicial contractibility. [@GuillenNavarroPascualRoig2008, Theorem 9.2 and Corollary 9.3]

**First concrete step.** Make a two-column axiom comparison, including augmentation, weak equivalences, coefficient behaviour and allowed morphisms. Select one missing common-refinement or equalization condition and formulate it as an independently testable lemma. A successful result should say exactly which localization it concerns.

## 3. The correct infinite shadow quotient

**Origins:** items SA08-50, SA08-51, SA08-469; claims SA08-C033, SA08-C034, SA08-C217–C 219, SA08-C223, SA08-C287; problem MP-SA08-17.

**Target.** Determine when the different proposed negligible classes agree, and which one supports the desired section functor and derived recovery.

**Known boundary.** The literal elementwise eventual-tail-annihilation class is not extension-closed over \(\Gamma_{\mathbf F_p}(T)\). Uniform boundedness is extension-closed but not closed under arbitrary coproducts. The localizing Serre closure of bounded nonnegative modules is a legitimate replacement, and its stated induced-module recovery is checked in the proof memorandum. This replacement must not be relabelled as the author's original class. Later divided-power module results impose their own finite-presentation and base-completeness hypotheses. [@Gabriel1962; @NagpalSnowden2017]

**First concrete step.** Choose one explicit finiteness condition on the graded module category, and compare all three classes under that condition. Start with the already recorded \(I/I^2\),\(S/I^2\),\(S/I\) sequence to see exactly which object the condition excludes. The result sought is a precise equivalence or counterexample, not a general claim that all torsion notions coincide.

## 4. The half-differential-algebra product obstruction

**Origins:** Codex item SA08-905; claims SA08-C918–SA08-C920; problem MP-SA08-100. The surrounding simplex extension is also recorded in SA08-96.

**Target.** Decide existence of the first partial product \(C^i\otimes Z^j\to C^{i+j}\) for the specified universal model, before imposing all associativity, symmetry and naturality conditions.

**Known boundary.** Under tensor exactness, with source extension \(e\), target extension \(e'\), cycle product \(a\) and boundary product \(c\), the obstruction is \(a_*e-c^*e'\) in the indicated \(\operatorname{Ext}^1\). If it vanishes, choices form the Hom torsor written on the page. This is a precise obstruction framework, not a computation of its value in the full model. Cartan and Cenkl treat different multiplicative structures. [@Cartan1976; @Cenkl1989]

**First concrete step.** Specify the source and target exact sequences for the smallest nontrivial pair \((i,j)\), identify both products \(a,c\), and calculate their extension classes in the actual sheaf/simplicial category. A cycle-only lift would test the wrong problem.

## 5. Universal divided-power convolution data

**Origins:** items SA08-489, SA08-520; claims SA08-C255, SA08-C257, SA08-C259, SA08-C285; problems MP-SA08-77, MP-SA08-78.

**Target.** Compare the proposed packages of natural power data and identify the exact hypotheses for existence and uniqueness on convolution ideals.

**Known boundary.** For a flat counital cocommutative coalgebra \(A\), the convolution PD structure on \(\operatorname{Hom}(A,J)\) is checked here using \(\Gamma^nA\simeq\operatorname{TS}^nA\);\(J\) need not be flat. There is a fully specified nonflat counterexample. Positive-index composition and binomial identities alone do not force uniqueness; allowing index 0 or full additive naturality changes that question. [@SGA4XVII, XVII 5.5.2.4–5; @Roby1963; @Roby1968]

**First concrete step.** Write all six proposed data packages with their exact index ranges, counit conditions and test-algebra naturality. Test one proposed implication on the rank-one characteristic-two example before attempting a general equivalence theorem.

## 6. Filtered and completed coefficient comparison

**Origins:** items SA08-403–SA08-407; claims SA08-C201–SA08-C208; problems MP-SA08-60, MP-SA08-61.

**Target.** Determine when the filtered/complete simplex construction has the promised associated graded and cohomological comparison, distinguishing a completed algebraic presentation from exactness of completion.

**Known boundary.** Cartan's graded universal theorem does not automatically supply the arbitrary completed-coefficient version. The later filtered statement retains a graded-free hypothesis. The \(p\)-adic valuation calculations are checked, including the exceptional behaviour at 2; cofinality of filtration levels does not mean the associated graded is the free PD algebra. The transcribed \(\Gamma^p\Psi\)/\(K(k,p)\) identification also needs a notation or hypothesis correction. [@Cartan1976, §7; @GarvinEtAl1998, Theorem 4.2]

**First concrete step.** Fix one complete coefficient ring, specify the topology on every homogeneous piece, and compare the ordinary and completed associated-graded sequence. Record which exactness statement is assumed, proved or false before invoking a spectral sequence.

## 7. Test embeddings and relative coefficient comparison

**Origins:** items SA08-87, SA08-95–SA08-100, SA08-207; claims SA08-C053, SA08-C061–SA08-C065, SA08-C103–SA08-C104; problems MP-SA08-21, MP-SA08-24, MP-SA08-25, MP-SA08-27, MP-SA08-30.

**Target.** Give an exact sufficient criterion for the internal or relative de Rham comparison, with the coefficient category and all slices specified.

**Known boundary.** An actual simplicial contraction survives application of the relevant functors. Flatness plus acyclicity is weaker. Absolute section-acyclicity does not imply \(f_*\)-acyclicity or the needed slice condition. The arbitrary-presheaf comparison on the simplicial circle has an explicit counterexample, while the locally constant comparison survives. [@Cartan1976, Theorems 2–3; @BMT2016, Proposition 6.6]

**First concrete step.** Select one relative map \(f\) and write the exact resolution whose terms must be \(f_*\)-acyclic after coefficient extension. Prove that criterion in a useful example or produce a counterexample to the weakest proposed version. Do not infer \(\Gamma_k(T)\)-flatness from \(k\)-flatness.

## 8. Natural splittings of the simplex sequences

**Origins:** items SA08-94 and the Codex occurrence of SA08-C917; claims SA08-C060, SA08-C917; problem MP-SA08-23.

**Target.** Decide whether the displayed sequences admit a natural integral splitting and identify the precise obstruction when the weight is not invertible.

**Known boundary.** The derivative-style return map on 346 composes to multiplication by the weight \(p\). It is a splitting after inverting \(p\), and it is not an integral right inverse as written. Projective existence of some splitting is different from a canonical simplicial choice. [@BMT2016, the PD/Koszul comparisons; @Roby1963]

**First concrete step.** Express the sequence in the normalized simplicial category for the first relevant weight, calculate its extension class, and check compatibility with degeneracies. The factor \(p\) supplies a diagnostic, not a proof that every other natural splitting is impossible.

## 9. Natural operation complexes and coherence across arities

**Origins:** Codex items SA08-906–SA08-907 and item SA08-478; claims SA08-C926–SA08-C928, SA08-C290; problems MP-SA08-101, MP-SA08-102.

**Target.** Formulate the actual operation complex needed for the manuscript's higher products and identify what must be added to obtain coherent composition across arities.

**Known boundary.** Dold's theorem uses independently varying inputs and a separately chosen free group-ring resolution. The diagonal-only natural-Hom reading has at least four independent degree-zero classes when the arity is 2. A single arity resolution does not itself give all operadic compositions. The blank sign in the displayed power operation remains an ink question. [@DoldSteenrod1961, Theorem 1.6 and §§1.7–1.12; @SteenrodEpstein1962]

**First concrete step.** State the source functor category and the two-variable naturality condition explicitly. Compare one binary/ternary composition square with the chosen resolution maps; keep the missing sign outside any claimed verified formula.

## 10. The unfinished additive-group Ext induction

**Origins:** Codex items SA08-910–SA08-911; claims SA08-C952–SA08-C957; problems MP-SA08-111–MP-SA08-116.

**Target.** Determine which of the handwritten spectral-sequence and power-operation steps can be matched to the later complete proof, and which require an independent argument.

**Known boundary.** Breen gives the exact \(\mathbf F_p\)-linear higher Ext calculation and the exponent \(v_p(i)+1\). Perfect-site higher vanishing is a separate theorem. The Witt extension is not an extension in \(\mathbf F_p\)-module sheaves. Neither the final group formula nor perfect-site vanishing proves the particular handwritten edge map is zero, and the second lemma is only calculated for \(P^0\) on the leaf. [@Breen1978, Theorem 1.3 and §§IV, VII; @Mathew2022, AppendixA]

**First concrete step.** Type every sheaf category and coefficient action in the first edge-map square, then compare it with the corresponding map in Breen's spectral sequence. A useful result is an exact commuting diagram or a precise missing compatibility, not a rediscovery of the already established Ext groups.

## 11. The curve bundle and Euler normalization

**Origins:** items SA08-500 and SA08-901; claims SA08-C264, SA08-C901; problems MP-SA08-80, MP-SA08-90.

**Target.** Recover the intended geometric example with the correct bundle, lift and Euler convention.

**Known boundary.** The literal split bundle \(\mathbf P(\Omega^{-1}\oplus\Omega)\) on a compact curve with \(\deg\Omega\ne0\) does not have the claimed holomorphic projective connection. The oper comparison uses a nonsplit jet extension. The defining \(\mathrm{SL}_2\) circle and the projective \(\mathrm{PSL}_2\) boundary circle differ by a factor of 2 in the Euler generator. Uniformization does not automatically supply an algebraic splitting in families. [@BHR2021; @Atiyah1957]

**First concrete step.** Inspect the original scans for the meanings of \(\Omega\),\(E''\), and the projectivization, then write the exact extension and the represented circle. If the split bundle really is intended, retain the counterexample rather than replacing it silently by the jet bundle.

## 12. The divided-power versus exterior-power normalization question

**Origins:** item SA08-267, item SA08-405, and the Codex query at 346; claims SA08-C168–SA08-C169, SA08-C205, SA08-C958; problems MP-SA08-50, MP-SA08-51, MP-SA08-60.

**Target.** Establish an editorially reliable statement of the queried \(\Gamma^s\Psi\) object and its intended relation to the exterior and symmetric variants.

**Known boundary.**\(N\Lambda^r\Psi\) has the expected term in degreer. By contrast, over \(\mathbf Z\),\(N\Gamma^2\Psi\) has differential \(\pm2\) between degrees 2 and 1, whereas \(N\operatorname{Sym}^2\Psi\) has a unit differential. Over \(\mathbf Q\) the quadratic divided-power complex is acyclic. The derived décalage theorem supplies a framework but does not turn every nonlinear functor into a quasi-isomorphism-preserving termwise construction. [@DoldPuppe1961; @BMT2016, Proposition 3.5]

**First concrete step.** Decide the \(\Pi_*\)/\(K_*\),\(\Gamma\)/\(\Lambda\), variance and shift readings from the ink, then compute the next small integral weight in the precisely identified object. Its principal value is preventing a false general theorem from entering the future commentary.

## Work deliberately kept outside this list

The other-project links remain provenance leads in their own table. They have not been used to rank these directions or to supply mathematical hypotheses. Published-source errata and the remaining sign/index alarms are prioritized in the readings register; resolving them requires scans and is not treated as speculative theorem development. The already proved nonnegative tail recovery, quadratic normalization, binomial gcd and flat convolution case should be used as checked inputs, not assigned again as open discoveries.
