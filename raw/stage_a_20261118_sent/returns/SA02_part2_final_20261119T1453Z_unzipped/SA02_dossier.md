# SA02 — Géométrie et topologie combinatoire

## Scope, sources, and how to use this dossier

**Completed consolidation of part 2; assessment date: 19 November 2026.** This dossier covers the supplied packages of Montpellier cotes 84, 90, and 91. It gives a read verdict for every one of the 389 entries in this part’s `NOTES_INDEX.tsv`, and extends the mathematical claim and problem registers to the supplied transcription passages outside those Pro notes. In particular, the early cote-84 and later cote-91 Codex material is included. Codex notes are leads to the text, not additional indexed entries.

The authoritative source is the attached archive, extracted once. No scans and no second-pass corrections are present. The transcriptions have not been altered. A mathematical inconsistency is evidence for an ink review, not permission to replace a diplomatic reading. `SA02_readings.tsv` therefore retains both the transmitted reading and the proposed alternative, with the mathematical stakes stated explicitly.

The source inventory records 56 files and 343 distinct supplied scan markers: 190 in cote 84, 24 in cote 90, and 129 in cote 91. These are counts of the supplied witnesses, not the catalogue’s page totals. The absent K84-10 Codex witness does not remove scans 146–161 from coverage: the Pro transcription supplies them. Cote 84 has no supplied markers 8 or 123; cote 91 likewise has gaps listed in the inventory. No claim is made to have read an absent face. `SA02_scope.tsv` accounts for all 30 cotes listed in `TOPIC.md`; the other 27 belong to the other parts and receive scope records, not invented substantive assessments.

The main registers are deliberately distinct. `SA02_entries.tsv` accounts for each input entry exactly once. `SA02_items.json` consolidates notes about the same object, assertion, question, or reading. `SA02_claims.json` records mathematical assertions, including computations and withdrawals. Its nine explicitly labelled auxiliary records are coefficient completions, repairs, or comparisons from this or the earlier runs, not nine additional assertions attributed to Grothendieck. `SA02_problems.json` includes questions that were later answered locally as well as genuinely unresolved steps. An open mark on the page does not imply an open problem in 2026. The essay questions in the reused typescript are labelled nonmathematical.

Source locators use the original archive’s `SA02_texts/pro/…` and `SA02_texts/codex/…` paths and physical line numbers. The archive itself remains the prerequisite for those paths; it is not duplicated in this ZIP. Proof files, programs, and outputs cited in the registers are included. Bibliographic keys in brackets refer to `SA02_references.bib`, where links, dates, checked locators, and access limits are given. “Verified” means that the recorded link or source was opened to the stated extent; it does not turn a publisher abstract into a checked full proof.

The class letters describe the located literature, not just mathematical truth. A identifies an exact counterpart in Grothendieck’s own published work; B an established development by others; C a partial counterpart, restricted theorem, or repaired scope; D a bounded search that did not locate the exact development; E established background; F a statement that cannot be identified precisely from the surviving text. Where sheets are undated, A does not establish that the printed work was historically later than this particular draft. D is not a claim of historical absence. A class-C assertion may already have a complete independent proof here while its exact publication history remains unidentified.

## 1. Cote 84: quadratic structures, their products, and the limits of tensor realizations

### 1.1 The opening graded construction and binary forms

The early sheets begin with two sorts of quadratic data and a parity-dependent product. The positive factor four in the odd–odd case is part of the displayed construction. Its associativity reduces to eight parity patterns, all checked symbolically in `programs/root_computations.py`. The later Arf-type and monoidal questions are less complete. These statements should not be identified wholesale with a modern graded discriminant algebra merely because the even quadratic product agrees. In Loos’s actual odd–odd formula the discriminant is **minus** four times the product and the symmetry has a Koszul sign. Changing the sign of both odd parameters does not remove the discrepancy. The real example with two unit-square odd factors distinguishes the constructions. The exact even comparison survives. See CL-SA02-700–702, 733; MP-SA02-300–301, 308; [Loos1997, §§2.8–2.10] and `parts/cote84_second/Loos_graded_comparison.md`.

The next development relates a primitive binary quadratic form to an endomorphism algebra and its distinguished quadratic subalgebra. The alternating expression $x\wedge u(x)$ gives the map from endomorphisms modulo scalars to line-valued binary forms. The sign changes if the order of the wedge is reversed. The coordinate checks were performed over the integer polynomial ring, with characteristic two retained. Primitivity means that the form is nonzero on every reduced fibre; it is not nondegeneracy of the polar form. Under that condition the associated module is invertible over its quadratic algebra. Wood’s correspondence supplies a precise later framework, including the distinction between traceable modules and the primitive/invertible specialization. It does not justify discarding the determinant line or the chosen algebra identification. See CL-SA02-704–712; [Wood2011, Theorems 1.4–1.6 and §§2–3; Wood2009, Chapter 2].

The norm-one torsor discussion has a consequential topology error under the literal unrestricted reading. For a finite locally free quadratic algebra $A$, the norm sequence is exact for the fppf topology: adjoining a square root of a unit proves local surjectivity. With the associated algebra identified with $A$, primitive scalar-valued norm forms are described by torsors under its norm-one group. The parenthetical identification of fppf and étale torsors fails for non-smooth groups. Over $k=\mathbf F_2(t)$, take $A=k[\epsilon]/(\epsilon^2)$ and $q=t x^2$. This is primitive, but the norm-one-frame equation $x^2=t^{-1}$ has no point after a separable algebraic extension. The corrected fppf statement and the failed étale parenthesis therefore have separate records, CL-SA02-714 and 713. [StacksKummer] supplies the relevant topology distinction; the counterexample and all its hypotheses are in `evidence/root_proofs.md`, P03.

### 1.2 A retraction, reflections, and parity over a base with 2-torsion

On scans 29–32 the author tries to recover $E$ from $\operatorname{End}(E)/A$, then explicitly rejects the proposed recovery. For a finite locally free quadratic algebra $A$ and an invertible $A$-module $E$, the surviving formula is a tensor square:

$$
\operatorname{End}_{\mathcal O}(E)/A
\simeq E\otimes_A E\otimes_{\mathcal O}(\det_{\mathcal O}E)^\vee.
$$

This is an isomorphism for the left $A$-action; the right action is conjugate. The dossier gives a full descent proof, including nonétale algebras, by checking both a change of $A$-frame of $E$ and a change of generator of $A$. The distinction from $E$ itself is genuine: on $\mathbf P^1$, with $A=\mathcal O\times\mathcal O$ and $E=\mathcal O\oplus\mathcal O(1)$, the quotient is $\mathcal O(-1)\oplus\mathcal O(1)$, which is not a base-line twist of $E$. This confirms the author’s withdrawal rather than treating an abandoned idea as his final theorem. See CL-SA02-717–718, MP-SA02-304, and P04. Wood’s dual-module discussion is a comparator, not an identified publication of this exact quotient formula.

The ensuing intertwiner and reflection calculations are valid when their pairings and actions are specified. The operator $\theta\mapsto u\theta-\theta\bar u$ is skew-adjoint for the reduced-norm polar pairing $\operatorname{Tr}(\theta\bar\theta')$, not for an arbitrary trace pairing. For $Q$e$=1$, the reflection $x\mapsto B(e,x)e-x$ works integrally without division by two. Conversely, action by $-1$ on $A/\mathcal O$ does not characterize conjugation in characteristic two: identity and swap on $\mathbf F_2\times\mathbf F_2$ have the same quotient action. The ink may contain an additional nonidentity qualification; the present run cannot decide it. See CL-SA02-719–724, MP-SA02-305–306, and the corresponding reading alarms.

The discriminant and parity sheets require equal care with division. In trace coordinates the norm is $(b^2-r^2\delta)/4$, on the appropriate parity lattice, rather than a formula valid on all pairs over any base. Dallaporta supplies an exact modern treatment when 2 is regular, including discriminant and parity data; that hypothesis must travel with the comparison. On test schemes with 2-torsion, the naïve root functor need not be the quadratic cover. The congruence subgroup functor $\lambda^2=1,\ \lambda\equiv1\pmod2$ is in fact nonrepresentable when the base has a local ring in which 2 is nonzero and noninvertible: its tangent functor $M\mapsto2M\cap M[2]$ fails left exactness. This is independently proved here, not left as an unresolved conjecture merely because an exact published formulation was not found. See CL-SA02-725–732, MP-SA02-307; [Dallaporta2025, Proposition 2.23, Theorem 2.25, Examples 2.29–2.30] and P06–P08.

### 1.3 The integral quadratic product

The product formula reappears several times and is one genuine consolidation, rather than several purported discoveries. For a commutative ring $R$, let

$$
A_i=R[u_i]/(u_i^2+b_i u_i+c_i),
$$

the abstract product is

$$
A=R[U]/(U^2+b_1b_2U+C),\qquad
C=b_1^2c_2+b_2^2c_1-4c_1c_2.
$$

Its canonical tensor map takes $U$ to $2u_1u_2+b_2u_1+b_1u_2$, and its discriminant is $(b_1^2-4c_1)(b_2^2-4c_2)$. All these are integral polynomial identities. They match the established even product after explicit generator changes: the relevant Voight generator is $U+b_1b_2$, while the corresponding Loos presentation realizes $-U$. The independent source occurrences on scans 63–65, 104, 172, and 192 are preserved under CL-SA02-005. [Loos1997, §§2.8–2.10; Voight2016, Construction 3.14 and Lemma 3.23].

Three stronger assertions must remain separate: existence of this abstract rank-two algebra; injectivity of its map to $A_1\otimes A_2$; and equality with the diagonal invariant algebra. Coefficient comparison gives the exact local kernel

$$
\ker(A\longrightarrow A_1\otimes A_2)
=\operatorname{Ann}_R(2,b_1,b_2)\,U.
$$

Injectivity split as an $R$-module map is equivalent to $(2,b_1,b_2)=R$. Over $\mathbf Z/4\mathbf Z$, with $b_i=c_i=0$, the nonzero element $2U$ is killed. The field-only characteristic-two slogan is therefore not a sufficient statement over general rings. CL-SA02-006, 217, 748, and 749 retain the different invariant and coinvariant questions. Voight’s tensor-image warning [Voight2016, Remark 3.17] is an exact relevant comparison; it does not erase these distinctions. The special statement that dual numbers absorb the product is used only in the free based context of [Voight2016, Lemma 3.16], not silently promoted to arbitrary determinant lines.

The relative trace $q:A_1\otimes A_2\to A$ takes the basis $1,u_1,u_2,u_1u_2$ to $2,-b_1,-b_2,U+b_1b_2$. Its composites satisfy $iq=1+\sigma_1\otimes\sigma_2$ and $qi=2\operatorname{id}_A$; the symmetrizer squares to twice itself. Scan 176 replaces a provisional coefficient 2 by 1 in the last trace value. This is an actual authorial correction, retained in CL-SA02-007. The product is étale exactly when both factors are étale. If one is étale, it instead gives an étale-local twist of the other. The map from the tensor cover to the product fails to be flat at simultaneous nonétaleness even in characteristic zero; the source itself cancels a characteristic-two-only qualification. See CL-SA02-216, 753.

The coinvariant criterion in the earlier extension language has a further rank-zero edge case. For positive-rank finite locally free kernels, the characteristic-two generation test works. With $L_1=0,L_2=k$ and both distinguished sections zero over $k=\mathbf F_2$, the written “one section generates” condition is vacuously satisfied on the first side, yet the dimensions differ. The corrected all-ranks criterion and the ring-level proof are in P11. This is a narrowly specified literal counterexample, not a rejection of the quadratic line-kernel case.

### 1.4 Relative norms and quasi-biquadratic systems

Scans 97–124 develop a relative norm, quasi-quadratic algebras, and systems of three quadratic subalgebras. The genuine quadratic-input relative norm has been checked through its full coefficient identities: homogeneity, polarization, multiplicativity, and transitivity. Its validity is not contingent on the tensor algebra being finite locally free over the contracted product. However, that does not validate every broader proposed norm construction on nonflat or nilpotent inverse images. EGA II §6.5 distinguishes its finite locally free case from a reduced, generically free case with specific restrictions on the norm and on base change. Ferrand and Biesel likewise cannot be cited with their finite locally free hypotheses removed. CL-SA02-008–010, 029, 051; MP-SA02-03, 05, 11; [EGAII, §§6.5.1–6.5.9; Ferrand1998; Biesel2024].

The five-axiom quasi-quadratic recap omits the earlier multiplicativity requirement. The omission matters even when “quadratic” is interpreted as a polynomial law: an explicit $\mathbf Z/4\mathbf Z$ example satisfies the weak axioms and violates multiplicativity. Scalar faithfulness restores the relevant implication. The weak and strong notions therefore have separate records rather than a silent repair. The strong version has a precise degree-two Cayley–Hamilton comparison with Chenevier, whose hypotheses are recorded. CL-SA02-011–017, 019, 052; MP-SA02-06–09; [Roby1963, Proposition II.1; Chenevier2014].

For the three-subalgebra system, scalar image of a contracted triple product is weaker than equality of the whole invariant ring with the scalars. A characteristic-two example separates them. The results have different scopes: CL-SA02-024 identifies the triple product with tensor invariants where 2 is invertible or at least two inputs are étale; CL-SA02-026 proves the scalar-invariant assertion for the compatible system when 2 is invertible; and CL-SA02-027 treats the all-three-étale parity-fibre case under its additional hypotheses. The generalized scalar-image question is not proved merely by assuming two inputs étale. Similarly, a finite surjective inverse-image construction is not thereby flat. The lemma on scan 120 requires careful attention both to the ambient ring of functions and to closedness of the subscheme. These are distinct issues, preserved in CL-SA02-018–029 and MP-SA02-08–11, not repaired by a single broad appeal to étale covering theory.

### 1.5 χ-trivialized extensions, strict comparison, and duality

The later mathematical sequence returns repeatedly to extensions equipped with a χ-retraction. The earlier pushout construction on scans 67–80 has a genuine integral local law and coherence calculations. Its universal property must retain the boundary coefficient map; when χ is zero or acts nonfaithfully, that map cannot be recovered by division. The later fragments cannot be used to erase this positive construction. CL-SA02-734–737, 739–745, 747, 750–751 and P09–P10 give the exact scope.

A different question asks for a comparison fixing both endpoints between pushout and pullback presentations. The local tensor calculation leaves residuals $(2-\gamma\chi)\tau_1$, $(2-\gamma\chi)\tau_2$, and $\chi(\gamma\chi-2)$. The condition $\gamma\chi=2$ is sufficient; it is not equivalent to invertibility of χ. At χ=2 the explicitly chosen γ=1 recovers the familiar symmetrizer. For a 2-retraction, $\sigma=1-a\pi$ is an involution integrally, and invertibility of 2 on the kernel alone gives the splitting. These occurrences are merged in CL-SA02-043–044 while their withdrawals and restorations remain visible.

The unrestricted strict comparison is false under the displayed identity-endpoint convention. On an elliptic curve in characteristic zero, take a nonzero extension class $e\in H^1(\mathcal O)$, one split factor, χ=0, and the specified trivialization maps. All the required local identities and universal injectivity conditions hold, but the two products have classes $e$ and $-e$. Since $2e\ne0$, no endpoint-fixing comparison exists. This refutes that precise reading, not either product construction or a comparison allowing an endpoint sign. The uncertain labels on scans 168–170 remain ink questions. CL-SA02-207, 211–214; MP-SA02-100, 103, 105; `parts/cote84_second/proof_checks.md`, §2.

Finally, ordinary finite locally free duality does not prove the particular product duality. The four-block χ=2 quadratic pairing has been independently checked on both relation submodules, and its descended matrix in the abstract product bases is the identity. It is perfect without inverting 2. The ordinary tensor pairing restricts to twice this pairing, so degeneration of that restriction does not disprove abstract perfectness. The general product-duality problem and this successful specialization remain separate: CL-SA02-210, 224–227, 234; MP-SA02-104, 110. Pirashvili’s relation $pq+2=0$ is a useful comparator after $p=-\chi,q=\gamma$, but the unit condition, torsor data, and arrows must also be matched. [Pirashvili2019, §§3.1, 4.2].

## 2. The reused Récoltes et Semailles leaves

The mathematical sheets in the latter part of cote 84 alternate with reused typed prose. Taken together, the two Pro packages supply 35 such leaves: original folios 465–500 except 481 and 485, together with 475bis. Scan order and folio order differ; folio 480 occurs in the earlier packet. Every supplied typed leaf was compared with its public counterpart, and the exact permutation is in the checked links. Internal cross-references were followed to their public targets. The reference to section 39 for *Désir et méditation*, whose actual heading is section 36, is inherited by the public text. It is not evidence of a new transcription error. [GrothendieckRS].

These pages concern personal change, acceptance, curiosity, paired qualities, yin and yang, and autobiographical interpretation. “Group” in their semantic classifications does not mean an algebraic group. Fourteen pairs are counted as 6+6+2; later qualifications and a public continuation to twenty-one groups have their own locations and are not substituted into the supplied earlier account. The question marks belong in the problem index but not in a list of mathematical conjectures. Health, psychological, cultural, and historical assertions remain attributed authorial statements; a textual concordance does not verify their empirical truth. The essay dates point to October 1984 and later annotations, without dating the reused mathematical faces.

The mathematical recollections are treated separately. Deligne’s Weil result is matched to its actual theorem, with the July 1973 lectures and September 1973 receipt distinguished from 1974 publication; a first written-preprint circulation date is not established. The standard conjectures are not made consequences of that proof. The located later advances include the specified abelian-variety cases of Agugliaro, Cossart–Piltant’s resolution for reduced separated Noetherian quasi-excellent schemes of dimension at most three, and de Jong’s alterations. Alterations are not birational resolutions. The general standard-conjecture and positive-characteristic resolution programmes remain open in the precise generality recorded here; the November 2026 searches did not locate an established general solution. Recent partial papers and unsupported broad search claims were not promoted into a settlement. CL-SA02-048–050; MP-SA02-19–20; [Grothendieck1969; Deligne1974; Agugliaro2025; Agugliaro2026; CossartPiltant2019; deJong1996; Berczi2026].

## 3. Cote 90: representations over Dedekind bases and henselian drafts

Two threads alternate through cote 90. One studies flat modules, coalgebras, representations, stable submodules, and equivariant generation over a Dedekind base. The other rewrites henselization, strict henselization, geometric branches, and connectedness arguments that have exact published EGA counterparts.

The opening Dedekind lemma overstates an equivalence. Let

$$
M=\sum_{p\ \mathrm{prime}}\mathbf Z\cdot(1/p)\subset\mathbf Q.
$$

This is countably generated and torsion-free, hence flat over $\mathbf Z$. At each prime $p$, $M_{(p)}=p^{-1}\mathbf Z_{(p)}$, so the indicated divisible-submodule obstruction is absent. Nevertheless the saturation of the finite submodule $\mathbf Z\subset M$ is all of $M$, which is not finitely generated. Thus the local exclusion condition does not imply the required finite-saturation condition. The valid implications, the countable projectivity conclusion under the stronger hypothesis, and the finite-coalgebra consequences are separated in CL-SA02-500–506 and `parts/cotes90_91/verification.md`, V01. [DuongHai2018, §3.1; SGA3VIB1970; SGA3VIB2024].

A stable finite projective generating submodule gives a faithful representation of an affine group under the stated finite-generation hypotheses. It does not make that group faithfully flat onto the entire automorphism group; the author crosses out that stronger proposition. The distinction is preserved in CL-SA02-503 and 508. Subsequent finite equivariant generation statements need the available finite coalgebra stages and the relevant projectivity or resolution hypothesis. An arbitrary quasi-coherent module cannot be a quotient of a finite locally free module merely because finite-type modules admit such covers. CL-SA02-509–515 retain the successive versions rather than treating them as one unconditional theorem.

The ample-line-bundle argument uses graded sections and sheafification to transport these questions. EGA II §4.6.3 supplies the exact ample open immersion and the recovery of a quasi-coherent sheaf from its graded sections; §§3.3.2–3.3.5 supply the unit/counit formalism under their hypotheses. This verifies the adjunction step. It does not independently establish existence of an equivariant stable hull without the preceding coalgebra assumptions. [EGAII].

The henselian thread has a much closer exact published fate. EGA IV, §§18.6–18.9, supplies the local universal properties, semilocal conditions, integral base change, reducedness and normality, strict variants, and connectedness results. The original primary text was read at these locations. The manuscript’s cancelled semilocal homomorphism category and later local repair remain separate. One parenthetical confusion is substantial: universal catenarity is not the formal-fibre separability condition needed in that application; the final EGA statement uses the appropriate Japanese-type hypothesis. An incomplete cancelled characteristic-zero remark is class F, not a theorem reconstructed from a likely destination. CL-SA02-516–533, 628–629; [EGAIV4, §§18.6.6–18.6.12, 18.8.10–18.8.17, 18.9.1–18.9.11].

## 4. Cote 91: representability, restriction of scalars, and constructible geometry

### 4.1 Equality functors, pseudo-torsors, and relative Hom

The opening sheets explore representability through equality subfunctors, adic conditions, rigidity conditions, centralizers, transporters, and flattening. The exact finiteness and separatedness assumptions change between versions. The draft’s unconditional closedness of a centralizer is cancelled; the live version separates representability from closedness under a separatedness assumption. The general nonnoetherian variants remain questions, with partial comparisons to the opened SGA, Murre, Raynaud, and later algebraic-space literature. CL-SA02-534–546; [Murre1966; SGA3VIII2009; SGA3XI2008; Raynaud1972].

The pseudo-torsor corollary needs flatness. Taken by itself, the pseudo-torsor identity is not enough. The additive group $G=\operatorname{Spec}\mathbf Z[x]/(2x,x^2)$, acting on $P=G$, is finitely presented and satisfies that identity but is not flat. Its identity section forces the proposed base monomorphism to be an isomorphism, contradicting the asserted faithfully flat torsor conclusion. Flatness may have been intended as an inherited assumption; the source uncertainty is retained. CL-SA02-545 records the literal counterexample, and auxiliary CL-SA02-630 states the precise repair rather than adding words to the transcription.

The relative Hom programme continues beyond the initially indexed leaves. Finite modules corepresent the relevant linear Hom functors; surjectivity of the induced module map defines an open condition. The deformation argument then uses square-zero extensions, pseudo-torsors, and compatibility diagrams. Several compatibilities are explicitly admitted on scans 20–21. The corrected obstruction construction must use the kernel of the combined compatibility map, not separate kernels or the wrong whole-domain cokernel. These proof obligations are not discharged by citing representability in the abstract. CL-SA02-547–553 and 625 retain each stage.

The letter to Anantharaman, dated 11 September 1967, was checked against its public two-page transcription. It is a separate dated witness to the claimed Hom theorem and the warning that the relevant functor need not be a scheme. It does not retroactively supply proofs for every marginal extension in the drafts. Proper flat finitely presented sources, a separated target locally of finite presentation, and the scheme/algebraic-space distinction all matter. Claims about section schemes likewise require target separatedness when separatedness is concluded. The question whether their connected components are of finite type has a negative answer under the merely locally-finite-presentation target hypothesis: over a field, an infinite connected separated chain of projective lines supplies a non-quasi-compact component. CL-SA02-549, 552, 554, 627, 635–638; [GrothendieckLetter1967; MatsumuraOort1967; Murre1966].

### 4.2 Restriction of scalars and Greenberg-type constructions

The restriction-of-scalars sheets contain a substantial positive theory. The adjunction and finite-limit identities are formal. For a finite locally free base, an affine target is represented by coefficient equations in a local basis; the schemes glue when the stated affine-neighbourhood condition on finite fibres is available. Radicial finite locally free bases make the locality argument especially effective. These are exact constructions, not merely anticipations of a later general theorem. The preserved properties are recorded with their individual hypotheses in CL-SA02-556–576. [Stacks05Y8; Rydh2011; BertapelleGonzalez2018; Greenberg1961; Greenberg1963].

Properness, finiteness, degree, and dimension need separate scrutiny. Ramified restriction of scalars does not preserve every property preserved by finite étale restriction. Deleting finiteness from a finite-étale degree argument invalidates it; the dimension formula on scan 52 also has a reversed reading to check. A blanket properness-descent assertion along a merely faithfully flat map needs an additional covering or finiteness hypothesis. A counterexample over $S=\operatorname{Spec}\mathbf Z$ uses the square-zero algebra $B=\mathbf Z\oplus\bigoplus_p\mathbf Z/p$. The map $Y=\operatorname{Spec}B\to S$ is not of finite type. After the faithfully flat, non-quasi-compact cover $\coprod_p\operatorname{Spec}\mathbf Z_{(p)}\to S$, it is finite on every component and hence proper. This refutes the self-contained unrestricted statement even with a noetherian base. Actual fpqc properness descent is the valid repair, CL-SA02-639. CL-SA02-561, 566, 568–572, 633; [Stacks02YJ; Stacks01WG].

The later ring-scheme and Greenberg constructions have positive affine equations and gluing arguments, while their abstract categorical explanation is less secure. In particular, a left-exact **set-valued** functor on a suitably small category and a left-exact endofunctor of a geometric category are different assertions. The former has a precise pro-representability statement; the latter cannot be obtained merely by dropping the target category from the notation. CL-SA02-573–576, 631; [Stacks00YB; Stacks0G2X; Stramaccia1985, §1.2].

The compactness lemma on scans 76–77 also survives its strongest global formulation: for a quasi-compact space $X$, if an open family contains every subset with at most $n$ points, quasi-compactness of the ordinary topological product gives a finite subfamily with that property. The draft uses a relative fibre power, which proves the fibrewise version; that proof mismatch does not refute the stronger true statement. CL-SA02-577 and MP-SA02-228 preserve the distinction. [Stacks08ZU.]

### 4.3 Cons, Ind/Pro systems, Laurent units, and jets

The constructible geometry sheets distinguish actual schemes, atomic preschemes, finite constructible stratifications, and objects of an Ind/Pro enlargement. An atomic prescheme is a disjoint union of spectra of fields. Passing to piecewise morphisms preserves more than a bare set of points: residue-field maps remain part of the data. The finite-stratification definitions and elementary equivalences have been compared with the absolutely flat reflection in Olivier’s primary paper. CL-SA02-577–594; [Olivier1968, Proposition 5; Stacks0CKV; Stacks0901].

Two shortcuts are false in the literal broad reading. First, an ordinary noetherian scheme can be isomorphic in Cons to a nonnoetherian one. A rank-one valuation ring with value group $\mathbf Q$ has two points; stratifying into its generic and closed points identifies its Cons object with the disjoint union of the fraction and residue fields, which is noetherian. The marginal definition in terms of possessing a noetherian constructible model can be consistent, but it is a different notion. Second, arbitrary inverse limits need not commute with a colimit over **finite** stratifications. Infinitely many point-indicator coordinates on $\mathbf A^1$ are individually constructible yet admit no common finite constructible partition. CL-SA02-585 and 632 keep these distinctions explicit.

The Ind/Pro formula $\operatorname{Hom}_{\mathrm{Pro}}((X_i),(Y_j))=\lim_j\operatorname*{colim}_i\operatorname{Hom}(X_i,Y_j)$ is standard for appropriately small cofiltered index categories and a locally small base category. Geometric finite-presentation and quasi-compact/quasi-separated hypotheses enter the comparison with actual scheme limits. The categorical formula does not automatically prove the draft’s entire adjunction diagram or every eventually-pointwise equivalence. The Laurent-unit construction, by contrast, has explicit affine stages bounding both a series and its inverse, with coefficient equations that can be checked directly. The nilpotent substitution and jet sheets also require their exact test category and ideal-stability condition: an arbitrary substitution with a nilpotent constant term need not descend to every proposed truncated polynomial quotient. CL-SA02-595–603; [Stacks0G2X; ContouCarrere1994; KapranovVasserot2004].

### 4.4 Reused mathematical typescript

Cote 91 also contains typed exercises and proof fragments on Lie algebras, formal groups, topological groups, and exterior algebras. They are included in source coverage, but are not established as original Grothendieck claims. Their hypotheses sometimes begin on an absent preceding page. The all-degree Lie-cohomology exercise is therefore not silently assigned a standard theorem whose assumptions cannot be recovered.

The positive checks include the restricted PBW construction over a commutative ring of prime characteristic when the Lie algebra is free; Schauenburg’s Theorem 3.2 was read with its proof for this exact scope. Formal-group examples show that a noncommutative group in characteristic $p$ can have abelian tangent Lie algebra. The exterior-algebra direct-sum formula uses the graded tensor product and retains its signs. Inverse-limit surjectivity for topological groups keeps the stated countability or quotient hypotheses. Conversely, a typed submodule/submodule reciprocity assertion for simple modules is false without an appropriate semisimplicity or quotient correction; the supplied two-dimensional affine-Lie example checks the failure. CL-SA02-605–624, 626; [Schauenburg2015, Theorem 3.2; MilneLie2013; the scoped Bourbaki records].

## 5. What consolidation changes, and what remains to do

The earlier notes often correctly identify unfinished calculations, cancellations, and local hypotheses. Their recurrent weaknesses are promotion of a local calculation into a global comparison, promotion of a conditional statement into an unrestricted one, and conflation of objects that share a rank or formula. The consolidation corrects those without discarding the useful local observations. It also merges genuine repetitions across the two cote-84 packages while preserving different assertions about duality, injectivity, invariants, norms, and strict comparison. `SA02_aliases.tsv` records retired identifiers; occurrence-level statements, source status, and check evidence remain attached to the canonical claim.

The checked links table contains only links whose archive or published endpoints were read. Earlier-run references to La Longue Marche, Les Dérivateurs, B12/B5, S6, and named research runs are preserved in `SA02_project_leads.tsv` with their note provenance. Their external context packets are absent, so they are explicitly unverified leads and are not counted as checked links or established mathematical connections. This is the concrete limit of Stage 5 for the supplied material, not an invitation to infer project identifications from shared vocabulary.

The ranked future tasks in `SA02_directions.md` are narrower than the broad historical programmes. The strongest immediate candidates are the exact χ-comparison conventions, a basis-free nonflat relative norm theorem, the weak/strong quasi-quadratic distinction, the scalar image of the triple product, and a global statement of the verified χ=2 pairing. Cotes 90–91 supply corresponding finite-saturation, representability, and finite-stratification tasks. Each direction cites its originating records and separates mathematical interest from what a few-hour run could achieve. No new direction is developed here beyond the proof checks and counterexamples necessary to assess the supplied claims.

## 6. Counts and verification record

<!-- COUNTS_BEGIN -->
| Register | Count |
|---|---:|
| Indexed source entries | 389 |
| Canonical Stage 1 items | 336 |
| Assertion records in the claims register | 274 |
| Source-associated assertion records | 265 |
| Auxiliary repairs, completions, and comparisons | 9 |
| Reused typed source assertions (included in source-associated count) | 21 |
| Problem records, including locally resolved questions | 101 |
| Explicitly nonmathematical essay questions (included above) | 10 |
| Undecided reading alarms | 197 |
| Checked links with both endpoints inspected | 158 |
| Separate unverified external-project leads | 15 |
| Ranked future directions | 16 |
| Bibliographic records with scoped access notes | 88 |
| Check events | 1084 |
| Distinct supplied scan markers | 343 |
| Catalogue cotes accounted for in the scope table | 30 |

### Entry verdicts

| Verdict | Count |
|---|---:|
| kept | 306 |
| merged | 53 |
| corrected | 22 |
| withdrawn | 8 |
| rests on a misreading | 0 |

Zero in the last row does not mean there are no reading alarms: the notes often already flag the uncertainty correctly, and corrected or withdrawn verdicts preserve the particular reason.

### Item kinds

| Kind | Count |
|---|---:|
| conjecture | 2 |
| idea of the earlier run | 22 |
| other | 134 |
| reading question | 36 |
| self-flagged step | 28 |
| title, date or page count | 24 |
| unproved claim | 43 |
| unpursued implication | 20 |
| withdrawn in the same text | 27 |

### Claims by literature class

| Class | Count |
|---|---:|
| A | 28 |
| B | 65 |
| C | 95 |
| D | 6 |
| E | 66 |
| F | 14 |

### Status categories

| Category | All assertion records | Source-associated records only |
|---|---:|---:|
| proved there | 51 | 51 |
| proof sketched | 78 | 78 |
| stated without proof | 71 | 62 |
| corrected by himself later | 15 | 15 |
| false as stated | 30 | 30 |
| open on the pages | 29 | 29 |

The exact categories were assigned by the passage readers, not inferred from keywords. Rich occurrence-level descriptions remain in the JSON. In particular, “false as stated” can be conditional on a literal reading or a missing inherited hypothesis; it does not decide the ink. The nine auxiliary records are explicitly attributed and excluded from the source-only column.
<!-- COUNTS_END -->

The source-reading work was divided among four readers, all GPT-6 Astra Pro; the effort setting is not exposed in this environment. `CHECK_EVENTS.tsv` describes the actual scope of each event. A textual comparison is labelled textual and is not counted as an independent proof. A finite-ring example is a counterexample or diagnostic, not a universal theorem. Polynomial certificates are distinguished from geometric arguments, and literature statements read without re-proving them have their own event scope.

The main independent arguments are in `evidence/root_proofs.md`, `parts/cote84_first/proofs.md`, `parts/cote84_second/proof_checks.md`, and `parts/cotes90_91/verification.md`. The code and authored computational outputs accompany them. Full external publications and raw retrieval excerpts are not redistributed; the concise query ledgers, access notes, URL metadata, and packaging exclusions preserve the audit trail. The source inventory, search-to-claim audit, reference access audit, local validation reports, integration decisions, final structural report, and archive manifest make the coverage and limitations inspectable. The structural checks confirm identifiers, source assignment, schemas, references, locators, and saved evidence; they do not replace the passage reading or mathematical reasoning.

First circulation, receipt, online publication, printed publication, and later corrected versions are separated wherever the sources supply those dates. No priority claim is inferred from an undated mathematical sheet. No historical explanation for abandoning a question is invented where the sources give none. The remaining scan questions and bounded literature-identification limits are substantive results of the consolidation and remain visible in the finished registers.
