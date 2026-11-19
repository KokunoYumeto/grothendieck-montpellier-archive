"""Manually formulated open-step index; no headings or keyword classification."""
from pathlib import Path
import json
P=Path('/workspace/scratch/a5176e5b5d45/SA06_work/parts/cote15_middle')
Q=[]
def p(n,title,occ,as_he_states,plausible_today,state,why,worth,refs):
    Q.append(dict(id=f'MP-SA06-{n}',title=title,occurrences=occ,as_he_states=as_he_states,plausible_today=plausible_today,state_of_art='As of 2026-11-19: '+state,why_open=why,worth=worth,refs=refs))
p(200,'Realization of integral Weil numbers', ['15/100 Pro244–282; SA06-408; C-SA06-406'],
  'The strong conjecture asks whether the stated integrality and absolute-value conditions suffice for an algebraic number to occur as a Frobenius eigenvalue of the indicated degree over the finite field.',
  'For q a prime power, every algebraic integer whose conjugates have modulus q^(i/2), with i>0, occurs in H^i of a smooth projective variety over F_q; weight0 is realized by finite étale schemes, and negative integral weight has no nonzero algebraic-integer examples.',
  'Tate’s Honda exposition, Theorem1(a),(c),(d), pp95–96, supplies weight-one realization. Taking an i-th root, applying Honda–Tate, and using the H^1 tensor power and Künneth gives the stated eigenvalue conclusion; P3 proves the reduction. This does not prove the full Tate conjecture or identify an entire motive category.',
  'The page calls it a strong conjecture; the opened sources do not explain his later abandonment or continuation of this exact draft.',
  'Useful for a precise historical annotation, but the numerical eigenvalue existence problem itself is settled.', ['TateHonda1968','MilneFiniteFields1994'])
p(201,'The weak finite-field band description', ['15/106 Pro428–440; SA06-410; C-SA06-407'],
  'He proposes the displayed multiplicative-type group and says the weak conjecture probably follows from a form of the Taniyama–Shimura complex-multiplication theory.',
  'The character group of a specified numerical motive category over F_q is compared with the correct Weil-number group; integral eigenvalue realization and equality of the whole band must be distinguished, as must q and the characteristic p.',
  'Honda–Tate settles the numerical realization input. Milne, Motives over finite fields, Proposition2.6 and Remark2.7 pp14–15 and §§2.25–2.29 pp22–24, give the modern comparison with explicit Tate-conjecture and equivalence-relation premises. The unspecified manuscript category is not thereby identified.',
  'The page supplies the prospective CM route, but no exact theorem or hypothesis package for M.',
  'Worth one bounded run to align each character lattice and category premise, not to treat the broad conjecture as unconditionally solved.', ['TateHonda1968','MilneFiniteFields1994'])
p(202,'Saturation after finite-field extension', ['15/102 Pro314–338;15/104 Pro368–391;15/106 Pro428–438; SA06-411,412; C-SA06-408,409'],
  'He asks whether the displayed weights/eigenvalues fill all allowed integers, then deletes part of the argument and moves to a direct-limit description.',
  'For the full Weil-number character groups, power maps have the stated torsion kernel and bounded-torsion cokernel; the geometric direct limit rationalizes the valuation lattice. A finite-stage integral lattice need not be saturated.',
  'Milne §§2.25–2.29 supply P(q) and its direct limit. P4 proves the exact power-map sequence and explains why the integral finite-index defect disappears only after the appropriate limit.',
  'The deletions show revision on these sheets; no source establishes the author’s later reason for dropping this formulation.',
  'Worth checking finite-stage kernels when reconstructing the intended band; the rationalized calculation is established.', ['MilneFiniteFields1994','MilneCM2020'])
p(203,'A class group not killed by two', ['15/96 Pro188–198;15/98 Pro221–225;15/114 Pro615–617; SA06-404,415,427; C-SA06-410,416'],
  'He asks whether the integral obstruction can be nontrivial and writes that Serre could be asked for an imaginary quadratic field whose ideal class group is not killed by2.',
  'The prime above2 in Q(sqrt(-23)) has exact class order3. Its norm-one p-unit divisor lattice has finite index3 in the ambient anti-invariant lattice.',
  'Milne ANT Theorems4.3–4.4 and Proposition8.10 provide class-group and decomposition-group background. P5 and exact_checks.py independently prove the specific ideal order, norm obstruction, valuation matrix and Smith form; no general saturation assertion survives.',
  'The manuscript explicitly postpones the example to a question for Serre; it does not give a reason beyond that.',
  'The example is complete and useful as a permanent audit case for integral versus rational character lattices.', ['MilneANT2020'])
p(204,'Lifting the normalized Frobenius through an isogeny', ['15/112 Pro580–596;15/114 Pro615–617; SA06-416,417; C-SA06-414,415'],
  'He constructs a norm-one torus isogeny and asserts that the normalized Frobenius lifts only when the isogeny is an isomorphism; the displayed f0 normalization does not itself have weight zero.',
  'After fixing f0, a rational lift through 1→K→S→T→1 exists exactly when its connecting class in H^1(Q,K) vanishes. The special Frobenius point may detect the integral lattice defect only after an additional explicit calculation.',
  'The general obstruction is the standard torsor boundary; Deligne–Milne Theorem3.2 supplies the torsor interpretation and Milne §§2.25–2.29 the finite-field lattice. P7 isolates the missing implication and computes the normalization error. A generic isogeny does have rational points lifting without being an isomorphism.',
  'The page gives no proof of the special lift criterion and follows it with the class-group question.',
  'High priority: a short run can formulate and test the exact special-point claim without making a false assertion about arbitrary isogenies.', ['DeligneMilne1982','MilneFiniteFields1994'])
p(205,'A prescribed norm in a fixed CM field', ['15/132 Pro953–957;15/133 Pro961; SA06-418,419; C-SA06-417,418'],
  'The assertion for a preassigned CM field is struck out; the surviving text instead allows a CM extension containing the chosen totally real field.',
  'The fixed-field norm condition can fail. Allowing a finite CM enlargement realizes the desired positive rational norm by a root-taking construction, while retaining the chosen real subfield.',
  'Milne CM Proposition1.4, Corollary1.5 and Remarks1.6–1.7 provide the CM structure used in P6. Exact norm obstructions in Q(i) and Q(sqrt(-23)) distinguish rational and integral failures; the enlarged-field construction is proved independently.',
  'The manuscript itself withdraws the overly strong fixed-field statement; it does not state the counterexample that prompted the deletion.',
  'The corrected result is settled; further work should classify minimal extension degree or norm obstructions only if separately requested.', ['MilneCM2020','MilneANT2020'])
p(206,'Real fibre functors in the primitive Tate case', ['15/117 Pro650–682;15/119 Pro699–714; SA06-431,432,433,435; C-SA06-423,424,425'],
  'He distinguishes the primitive and square cases for epsilon, uses compactness, and invokes a fundamental alternating form and a rank-two object in odd degree.',
  'For a polarized real Tate category with the inherited positivity and descent axioms, the obstruction and parity are controlled by the real Tate gerbe. Statements about arbitrary tori and a character alone are weaker data and do not imply his criterion.',
  'Deligne–Milne Lemma4.24 and Propositions5.13,5.15–5.19 give the precise compact real-form and polarization context. P9 computes H^1 and H^2 for the compact real torus and the quaternionic rank-two model. The broad neutral-G_m objection of the earlier notes does not refute the contextual assertion.',
  'The source sketches the criterion and relies on inherited category axioms; it does not isolate all of them on these two pages.',
  'Worth a focused reconstruction of the exact axioms and the square/primitive dichotomy, with no extrapolation to arbitrary bands.', ['DeligneMilne1982'])
p(207,'The polarization and fibre-functor torsor comparison', ['15/119 Pro706–714;15/121 Pro730–740; SA06-436,437; C-SA06-426'],
  'He asserts that the indicated fibre-functor and polarization data determine one another, finishing with equivariance and simple transitivity; the printed domain of i1 is inconsistent with the cocharacter formulas.',
  'Once both nonempty parameter sets are torsors for the same group and the construction is equivariant, the map is a bijection. The construction and nonemptiness require the stated polarized Tate-category hypotheses.',
  'Deligne–Milne Theorem3.2 and Propositions5.15–5.19 give exact torsor and polarization comparisons. P9 re-proves the equivariant torsor argument; it does not infer the nonempty torsor premise from the final sentence alone.',
  'The page leaves parts of the construction implicit; the original ink is needed to decide the mu2/G_m domain alarm.',
  'Worth a short annotation that makes the construction and its domain precise before using the torsor bijection elsewhere.', ['DeligneMilne1982'])
p(208,'Automorphism orbits of polarization data', ['15/121 Pro732;15/123 Pro788–802; SA06-438; C-SA06-428'],
  'He asks separately whether real, rational, and full arithmetic automorphism groups act transitively on the relevant polarization/effectivity data.',
  'For a fixed torus or band, a specified integral cocharacter lattice and a specified packet, formulate each group action separately and compute its orbit set. Torsor simple transitivity under a different group does not answer this question.',
  'Deligne–Milne Theorem3.2 classifies fibre functors by torsors, but does not state the manuscript’s three orbit assertions. The exact unrestricted orbit problem is not identifiable without the missing packet and automorphism conditions; the search found no theorem with all these quantifiers.',
  'The source says À voir and then calls part of the subsequent packet question secondary; no further historical explanation is supplied.',
  'Worth pursuing only after fixing a finite CM quotient where orbit calculations can be completely specified.', ['DeligneMilne1982','MilneFiniteFields1994'])
p(209,'Integrality of the valuation cocharacter', ['15/110 Pro534–555;15/121 Pro744–758; SA06-426,439; C-SA06-412,429'],
  'He warns that the valuation functional is not always integer-valued, while using it as a cocharacter.',
  'Normalize the valuation on the exact integral character lattice; a rational functional gives an integral cocharacter only when its value on every lattice generator is integral. Galois conjugate valuations may span only a finite-index sublattice.',
  'Milne §§2.25–2.29 retain the rational/integral distinction. P5 and P7 compute the Q(sqrt(-23)) lattice and its index; P10 separates additive valuation identities from the transcribed false multiplicative formula.',
  'The page explicitly records the nonintegrality obstacle; it gives no universal normalization resolving it.',
  'High priority as a finite calculation needed by several later claims about effectivity and parity.', ['MilneFiniteFields1994','MilneANT2020'])
p(210,'Finite-index differences of splittings', ['15/121 Pro740;15/123 Pro794; SA06-440; C-SA06-431'],
  'He asserts finite index for the group generated by differences of the cocharacters under consideration.',
  'All such differences have epsilon-weight zero, so finite index can only be asserted in the correct weight-zero lattice; it is impossible in the entire positive-rank cocharacter lattice containing the weight direction.',
  'Character duality in Milne CM §4 and the Weil lattice in Milne §§2.25–2.29 give the precise framework. P10 proves the rank obstruction and identifies the possible corrected target. The exact corrected finite-index claim still depends on which splittings are allowed.',
  'The manuscript gives no proof here, and the earlier notes carried an overly large target.',
  'Worth resolving alongside the valuation-lattice run because the target correction is indispensable and explicit.', ['MilneCM2020','MilneFiniteFields1994'])
p(211,'The mod-two packet of cocharacters', ['15/123 Pro794–802; SA06-441; C-SA06-432'],
  'He states that the preceding information gives no indication about the resulting mod-two packet and calls this question secondary.',
  'For a specified integral lattice and a specified Galois family of weight splittings, compute the image of their differences modulo2 and its automorphism orbits.',
  'Milne’s integral Weil lattices provide the input but no universal packet theorem. P10 and real_descent computations show that finite index alone is inadequate: 2Z and3Z have different reductions modulo2.',
  'The source itself explicitly labels this question secondary; no reason for that ranking is supplied.',
  'Worth a bounded finite-lattice computation after the manuscript’s cocharacter normalization is fixed.', ['MilneFiniteFields1994','DeligneMilne1982'])
p(212,'Effectivity from one valuation and its conjugates', ['15/121 Pro742–758;15/123 Pro788; SA06-442; C-SA06-430,514'],
  'He says the effectivity structure is determined by i and its conjugates and that a rational automorphism respecting i is the identity.',
  'In the full Weil-number lattice, nonnegative values of all conjugate p-adic valuations characterize integrality. A Q-automorphism is forced to be the identity if the conjugates of i span the rational cocharacter space. Identifying the integrality cone with actual effective motives remains a categorical premise.',
  'Milne §§2.25–2.29 describe the exact Weil-number lattice and its Frobenius. P10 proves the spanning and integrality implications, while preserving the extra effective-category assumption.',
  'The source treats the valuation description as inherited and explicitly notes the separate integrality issue.',
  'Worth clarifying in the commentary; a new theorem would require a fixed motive category and an exact effectivity assertion.', ['MilneFiniteFields1994','MilneCM2020'])
p(213,'Lifting the CM involution from the band to the gerbe', ['15/123 Pro806–810;15/125 Pro834; SA06-443; C-SA06-433'],
  'He constructs a canonical involution of the commutative band and questions whether it lifts to the gerbe; the ne/me reading reverses his stated expectation.',
  'A band automorphism can lift only if it preserves the gerbe class in H^2; a lift with a coherent order-two structure imposes an additional descent condition. Inversion on a weight-zero torus sends its class to its negative.',
  'Deligne–Milne Proposition5.8 describes Tate reduction; Milne Lemma3.15 p37 identifies character pushouts with Brauer classes. P11 gives a fully specified order-three test obstructing inversion in a standard finite-field realization. The literal M of the manuscript remains unidentified.',
  'The page explicitly doubts the lift. No source consulted establishes his later decision, and the uncertain negation is left to the scan.',
  'High priority: finite-dimensional quotient gerbes can turn the broad lifting question into a precise Brauer obstruction.', ['DeligneMilne1982','MilneFiniteFields1994','TateHonda1968'])
p(214,'Is the global gerbe class killed by two?', ['15/125 Pro834; SA06-444; C-SA06-434'],
  'He replaces exact order2 by order dividing2 for h in H^2(Q,U).',
  'For a specified Tate-reduced commutative-band category, inspect every character-orbit pushout to a Brauer group. The broad assertion is false in a standard category containing the F8 simple threefold with Frobenius1+sqrt(-7) and its usual endomorphism algebra.',
  'TateHonda Theorem1(c),(d) and Milne Theorem2.19 yield local invariants1/3 and2/3; Milne Lemma3.15 maps the gerbe class to that Brauer class. P11 verifies the absolute simplicity, all invariants, the character-field restriction, and preservation of the obstruction under Tate reduction. This is a conditional modern test, not an unconditional identification/refutation of the undefined manuscript M.',
  'The deletion records weakening on the page. The opened literature does not explain why he first expected order2 globally; the real-place calculation alone cannot justify it.',
  'Highest mathematical interest: determine exactly which category and reduction his h denotes before deciding how the order-three example bears on the text.', ['TateHonda1968','MilneFiniteFields1994','DeligneMilne1982'])
p(215,'Tate-rigidified fibre gerbe and the Giraud question', ['15/135 Pro978–992; SA06-445; C-SA06-435'],
  'He restricts fibre functors by a chosen trivialization of the Tate object and writes Giraud? alongside the gerbe construction.',
  'The two-fibre product of the fibre gerbe with a chosen point of the Tate-subcategory gerbe has band ker(epsilon), under the stated Tate-subcategory hypothesis. It need not be neutral.',
  'Deligne–Milne Proposition5.8 p51 states the precise reduction and cites Giraud IV3.2.1. The Deligne–Milne result is opened and checked; Giraud’s original theorem remains marked unverified because only its publisher metadata was accessible.',
  'The source flags the formalism as a reference question, not a claim that reduction is impossible.',
  'Useful as a short formal annotation; the construction is established and must be separated from neutralization.', ['DeligneMilne1982','Giraud1971'])
p(216,'Finite objects, Artin motives, and the component quotient', ['15/135 Pro995–1005;15/137 Pro1010–1013; SA06-446,447,449; C-SA06-436,438'],
  'He constructs the finite-object subcategory and relates it to finite étale vector objects and the component quotient.',
  'For a specified Tannakian category, finite objects give a profinite quotient. Equality with the Artin subcategory and identification of its kernel with the connected component must be established in that category; a geometric point chooses the Artin fibre functor.',
  'Deligne–Milne Proposition2.20 treats finite Tannakian groups. HMS Theorem9.1.16 gives the Nori arithmetic exact sequence, while Remark 9.5.7 in the checked2025 version leaves geometric connectedness open. Thus the exact sequence alone cannot prove the stronger component identification.',
  'The page takes M as given and does not prove the required category-specific comparison.',
  'Worth an exact comparison table by motive theory, because conflating geometric kernel with connected component changes the claim.', ['DeligneMilne1982','HuberMuellerStach2017'])
p(217,'The Artin–Tate decomposition and its chosen fibre functor', ['15/137 Pro1010–1041; SA06-448,449,455; C-SA06-437,439'],
  'He writes objects as finite sums of V_i(i), keeps track of duals, and warns that the geometric-point fibre choice is particular.',
  'In the Artin–Tate subcategory with independent Tate weights, objects are finite graded Artin representations, the dual has the negative twist, and the tensor group splits after the stated choice.',
  'Deligne–Milne finite-object and torsor results and HMS §9.4 support the framework. P12 gives a complete permutation-module and Maschke proof for finite-image rational representations, including the choice-dependence.',
  'The author explicitly notes the special choice. There is no evidence here for a canonical neutral fibre on all motives.',
  'This is settled at the stated scope and useful for correcting the earlier notes’ stronger canonical-splitting language.', ['DeligneMilne1982','HuberMuellerStach2017'])
p(218,'Extending the regular normal form', ['15/97 Pro205;15/99 Pro234–238; SA06-472; C-SA06-461'],
  'The reused text asks about extending the regular normal form N to wider classes of groups or elements.',
  'Specify whether the desired object is a section of the adjoint quotient, a rational section, or representatives for every conjugacy class; these are different problems.',
  'Steinberg Theorems1.4–1.7 treat the simply connected regular setting. Popov Theorem1.2 and Corollary1.4 give exact cross-section criteria; Theorem1.6 provides a rational adjoint-quotient section over an algebraically closed field. None classifies every conjugacy class merely by quotient fibres.',
  'The fragment states the problem but gives no finer quantifiers. Popov’s epigraph points to a1969 letter, which is a bibliographic lead rather than an independently checked archive endpoint here.',
  'Worth a narrowly formulated historical comparison; a broad claim that normal forms are solved would be inaccurate.', ['Steinberg1965','Popov2011'])
p(219,'Removing perfectness in the reused Steinberg assertions', ['15/97 Pro207–215; SA06-473; C-SA06-462'],
  'The fragment says perfectness is unnecessary for most assertions but does not enumerate which assertions.',
  'Match each numbered theorem separately, retaining rationality, quasi-splitness, simple connectedness and component-type conditions until an exact replacement theorem is established.',
  'The opened Steinberg pp50–52 state the perfect-field context. Popov’s algebraically closed-field results do not by themselves remove perfectness in all rational-point statements. The manuscript’s word most is not a uniquely identifiable theorem.',
  'The source supplies no list or proof, so its exact scope cannot be reconstructed without further source context.',
  'Worth a finite theorem-by-theorem reference audit; no blanket generalization should be recorded.', ['Steinberg1965','Popov2011'])
p(220,'The semisimple-automorphism centralizer extension', ['15/109 Pro511–521; SA06-471; C-SA06-463'],
  'The reused source lists centralizer structure and connectedness statements and defers the final semisimple-automorphism extension.',
  'Use the exact hypotheses of Steinberg2.7–2.10, including the source’s fundamental-group condition; arbitrary fixed-point groups of semisimple automorphisms need not satisfy an unconditional connectedness assertion.',
  'The checked primary source has precisely these numbered statements and deferred-proof wording at p53. The ordinary simply connected centralizer theorem is distinguished from the broader automorphism extension.',
  'The source explicitly postpones the proof; no additional historical motive is given.',
  'A useful annotation of recycled source material, but not a new motive-theoretic research problem.', ['Steinberg1965'])
p(221,'The deferred étale descent cases', ['15/91 Pro75–81;15/93 Pro112–122; SA06-470; C-SA06-455'],
  'The draft says certain proper and ground-field cases will be seen later, after a formal equalizer argument.',
  'Retain the morphism hypotheses of SGA4 VIII9.4.1–9.4.4, including the final text’s distinct field formulation; derive the formal descent statement only once the necessary base-change comparison is supplied.',
  'SGA4 VIII9.4, original pp410–412, is the exact later published passage; its proper case cites XII5.1(i) and its field case XVI1.4–1.5. The equalizer argument was independently checked, but this part did not re-prove those entire base-change theorems.',
  'The source expressly says the requisite results occur later in the exposition.',
  'The open step is resolved by the published continuation and should be annotated as classA, not retained as an open conjecture.', ['SGA4II'])
p(222,'The cancelled multiplicative-type immersion refinement', ['15/118 Pro685–696; SA06-478; C-SA06-456'],
  'A paragraph refining an immersion assertion is cancelled; the surrounding text discusses failures involving group-scheme hypotheses.',
  'Use SGA3 VIII7.13(b),(c) with its separation/connected-source conditions; do not infer that cancellation disproves the eventual theorem.',
  'The exact refinement is published at SGA3 VIII7.13(b),(c), and Remark7.10 describes the Raynaud counterexamples. The checked edition’s historical footnote distinguishes the1965 SGAD state from the1970 LNM edition.',
  'The page shows deletion but no reason. Its later publication demonstrates only that the mathematical statement, with its final hypotheses, survived.',
  'Worth annotating the draft/final difference; there is no remaining open theorem at the published scope.', ['SGA3VIII'])
p(223,'The anonymous reflexive-extension theorem', ['15/87 Pro5–15; SA06-467,468; C-SA06-452,453'],
  'The reused theorem extends a finite module satisfying local conditions to a reflexive module and invokes VI.1; P and the topology on Y are not defined in the fragment.',
  'For an open subset of a normal noetherian scheme whose complement has codimension at least2, reflexive coherent sheaves extend uniquely in the usual form. An arbitrary subset Y requires the missing original hypotheses.',
  'Stacks Lemmas31.13.12–14 and15.24.19 provide the exact normal/open and height-one comparisons. They do not identify the anonymous VI.5 theorem. The literal opening is tautological if f is already an isomorphism, suggesting a reading alarm but not making the literal implication false.',
  'The relevant definitions and previous theorem are absent from the supplied recycled page.',
  'Worth one source-identification run; until the missing definitions are found, the general theorem must remain classF.', ['StacksReflexive2026','StacksHull2026'])
p(224,'The full proof behind the projectivity fragments', ['15/101 Pro289–308;15/105–126 Pro398–849; B15-01/188; SA06-474,475,476; C-SA06-464–468'],
  'The recycled English chapter develops a numerical projectivity criterion through linear-series, cohomology and divisor arguments; isolated lemmas rely on an induction whose full context is discontinuous.',
  'The Nakai–Moishezon ampleness criterion is established. Each local inference in these fragments is valid under its stated common-twist, vanishing and generation assumptions; the entire proof must be read in its continuous original source before being certified as this exact draft.',
  'Cartier1966 Theorem1 p351 supplies the numerical criterion and bibliography[6] points to a Moishezon English mimeograph. The official Moishezon1964 record gives pp179–224 and receipt4June1963. Serre FAC §66 Theorem2 p259 supplies eventual generation/vanishing on a projective support; P14 checks the local long-exact-sequence implications.',
  'The archive supplies reused, discontinuous sheets. It does not identify the exact English edition or translator.',
  'Worth a source-collation task, especially to decide whether the common-twist mismatch is a transcription error or a draft typo.', ['Cartier1966','Moishezon1964','SerreFAC1955'])
p(225,'Distribution spaces as Lusin spaces', ['15/138 Pro1062; SA06-481; C-SA06-472'],
  'He writes that one can show D′(Ω) and E′(Ω), with their natural topologies, are Lusin spaces.',
  'The specific strong dual topologies on distributions and compactly supported distributions over the indicated finite-dimensional domain yield the stated Lusin property; no assertion is made for every strong dual of every Fréchet space.',
  'Bourbaki Topological Vector Spaces III§6 no2, Theorem2, its corollary and Example2 ppIII35–36 give the specific checked comparison. The ambiguous OCR wording of the general countability premise was not used to broaden it.',
  'The page omits the proof; the checked source supplies the specific example without explaining any archival chronology.',
  'Useful for source attribution, with low research priority once the exact topology is named.', ['BourbakiTVS1987'])
p(226,'The converse for strict generators and jolie categories', ['B15-01/59 lines7–35;Pro15/61 lines481–507;B15-01/63 lines56–68; C-SA06-473–476'],
  'He asks et inversement? and claims a jolie category is a filtered union of full strictly monogenic subcategories.',
  'An additive Karoubian A-linear category with a chosen strict generator is equivalent to finite projective modules over its endomorphism ring. For weaker jolie axioms, the filtered-union claim needs a common strict generator for each finite collection; this is not supplied by the displayed definition alone.',
  'Stacks Lemma12.4.2, Lemma10.78.2 and Lemma10.78.9 give the exact idempotent and finite-projective ingredients; P15 gives the independent corner-matrix proof. Searches for the exact jolie terminology did not identify a theorem fixing the weaker axioms.',
  'The Pro61 sentence continues on Codex63, so the definition is not missing merely because of a package boundary. The actual common-generator issue remains a mathematical hypothesis question.',
  'Worth a short axiomatic analysis that either derives directedness from his exact definition or supplies a counterexample.', ['StacksKaroubi2026','StacksProjective2026','StacksYoneda2026'])
p(227,'Localizability over Spec(R)', ['B15-01/81 lines85–107;B15-01/82 lines111–127; C-SA06-477–482'],
  'He proves that objects with an R-action form a stack on the small site of Spec(A), then explicitly says the argument does not prove localizability on Spec(R).',
  'Descent of objects and their action maps holds on the specified Spec(A) site; restriction to affine opens preserves localizability. A change to the Spec(R) site requires additional hypotheses and a specified base-change construction.',
  'Stacks Theorem59.16.2 and Proposition10.83.3 establish effective descent of quasi-coherent and finite-projective modules in the precise module setting. P15 proves the manuscript’s local rank-one and idempotent descriptions; neither result fills the stronger arbitrary-category Spec(R) gap.',
  'The author explicitly identifies the limit of his proof.',
  'Worth one focused run on the minimal hypotheses for this change of base site, without confusing it with ordinary descent of R-actions.', ['StacksDescent2026','StacksProjectiveDescent2026','StacksProjective2026'])
p(228,'An unfinished abstract continuation principle', ['B15-02/27 lines10–12; C-SA06-490'],
  'He proposes a general continuation principle and breaks off in the last hypothesis after enfin, si.',
  'A sheaf of local analytic solutions with unique continuation and existence along every relevant path admits the usual monodromy conclusion on a simply connected domain; the incomplete fragment does not fix which general sheaf or differential-equation assumptions he intended.',
  'Bourbaki Variétés §9.3.3 and the closed-form framework verify the concrete continuation results surrounding the fragment. They do not supply the missing final hypothesis of the proposed abstract statement.',
  'The paragraph is literally incomplete in the supplied source.',
  'Worth recovering adjacent sheets or the exact draft source; formulating a new general theorem would exceed the textual evidence.', ['BourbakiVarietes1967'])
p(229,'The C¹ extension of the closed-form argument', ['B15-02/31 lines40–46; C-SA06-487,488'],
  'He asks whether it is worthwhile to state the same Cauchy/homotopy result for continuously differentiable functions.',
  'A closed C¹ real one-form on a simply connected open subset of R^n has a global C² primitive; endpoint-fixed homotopy preserves its path integrals.',
  'Cristoferi §11.6 Lemma11.15 p125 is an opened author source for the closed-form exactness statement. P16 independently proves the local-to-global argument, including the Banach-valued analytic version needed by the surrounding pages.',
  'The question is explicitly about editorial usefulness, not an assertion that the C¹ theorem is unknown.',
  'The mathematics is settled; record the editorial question without promoting it to a contemporary open problem.', ['Cristoferi2016','BourbakiVarietes1967'])
p(230,'Holomorphic dependence from a vanishing Jacobian', ['B15-02/47 line211; C-SA06-498'],
  'A marginal question requests a dependence theorem for holomorphic functions whose Jacobian is identically zero, without fixing its local or germ quantifiers.',
  'The holomorphic constant-rank theorem gives local relations near a point of constant rank. The unrestricted implication to a nonzero relation in the target analytic germ ring at a singular image point is false.',
  'Belotto da Silva–Curmi–Rond2021 Example1.16 p1339 records Osgood’s example. P18 independently proves that (u,uv,uv exp(v)) has Jacobian rank2 but no nonzero formal or analytic relation; the polynomial-exponential independence argument is included. The1916 original remains unverified because its PDF was inaccessible.',
  'The manuscript provides only the question. No evidence identifies which stronger or weaker formulation he meant.',
  'High interest for annotation: the exact quantifier distinction prevents a false theorem, and the full counterexample is already checked.', ['BelottoCurmiRond2021','Osgood1916','BourbakiVarietes1967'])
p(231,'Local inversion versus global injectivity', ['B15-02/47 lines202–209; C-SA06-496,497'],
  'He contrasts real one-variable monotonicity with a complex power-map example and writes n sufficiently large.',
  'On the real interval a continuous nonzero derivative has constant sign. On |z−1|<1/2, the function z^13 has no critical point but fails injectivity; analytic inverse theorems remain local.',
  'Bourbaki Variétés §§3.2.1,3.2.7–9 state the local theorems and Glöckner Theorems7.3–7.4 give strict-differentiability variants. The exact_checks.py inequality for exp(±pi i/13) certifies the explicit complex example.',
  'The page asks only for a sufficiently large exponent, with no unsolved global criterion stated.',
  'Low priority after the explicit n=13 certificate; the local/global distinction belongs in the annotation.', ['BourbakiVarietes1967','Glockner2003'])
p(232,'Analytic ODE and Frobenius formula repairs', ['B15-02/39 lines95–132;B15-02/43–45 lines148–197; C-SA06-493,495'],
  'He proves local existence through an analytic ODE/majorant recursion, but the transcribed Frobenius compatibility and product indices fail the chain rule.',
  'Use the correct component U_ih in the final Frobenius summand and products of h_j in the ODE expansion. The local analytic germ theorem over a complete valued field of characteristic0 follows with those indices.',
  'Bourbaki Variétés §11.2.3 supplies the analytic Frobenius comparison; §§9.1 and9.3 supply local analytic expansions. P18 derives the compatibility equation, and exact_checks.py verifies a compatible system that the printed formula incorrectly excludes and a two-component ODE that exposes the product index.',
  'No source establishes whether the errors belong to transcription, manuscript or an earlier draft. The scans are required before any reading change.',
  'High priority for the next scan run because these indices reverse the validity of displayed formulas.', ['BourbakiVarietes1967'])
p(233,'Convergence at the boundary after coefficient division', ['B15-03/51 lines39–62;B15-03/53 lines67–82; C-SA06-501–505'],
  'He bounds reciprocal integers by polynomial growth and says weighted coefficient sums converge at the same time; the strict-differentiability estimate also loses r^(−2).',
  'Polynomial weighting preserves the open domain of convergence after shrinking the polyradius, not arbitrary convergence at its boundary. The strict-differentiability bound must retain the radius factor from the definition of M.',
  'Bourbaki Variétés §§9.1.1,9.1.7–8,9.3.3 and Glöckner Theorems7.3–7.4 support the corrected analytic-germ statements. P17 and exact_checks.py give explicit scalar counterexamples to the printed boundary and estimate claims.',
  'The source does not distinguish the boundary from the open domain in that sentence; no scan is available to decide the exact wording.',
  'Worth correcting in the mathematical annotation while leaving the diplomatic reading unchanged.', ['BourbakiVarietes1967','Glockner2003'])
p(234,'The Lusin binary-expansion normalization', ['15/138 Pro1048–1060; SA06-479,480; C-SA06-470,471'],
  'The copied argument maps binary sequences using a sum starting at n=0 and calls the target I, without defining I on this isolated sheet.',
  'The displayed map has range [0,2]; mapping to [0,1] requires starting at n=1 or using2^(−n−1). Countable sums, products and inverse limits retain the Lusin property under the specified Hausdorff convention.',
  'Bourbaki Topologie générale IX§6 no4 Proposition11, proof and corollary, ppIX62–63, defines I=[0,1] and visibly prints the same n=0 formula. The source witness therefore shares the normalization issue; it does not settle what the manuscript ink says.',
  'No explicit doubt appears beside the copied formula; this is a mathematically detected source/reading issue rather than an author-announced conjecture.',
  'Useful to the scan check because a printed-source agreement is not evidence that the formula is mathematically correct.', ['BourbakiTopology2007'])
p(235,'Identifying the motive category and limiting modern comparisons', ['15/135 Pro965–991;15/137 Pro1015–1041; SA06-450–456,466; C-SA06-438,441,448–450'],
  'He takes the category of semisimple (iso)-motives M as given; these pages do not construct it from a specified cycle-equivalence relation.',
  'Identify M from its actual inherited axioms before importing numerical, homological, motivated, Nori or Ayoub results. The comparisons in the earlier notes are modern analyses, not statements made on the pages.',
  'Jannsen Theorem1 gives numerical semisimplicity; HMS Theorem10.2.7 gives the pure Nori/André comparison in its characteristic-zero setting; Choudhury–Gallauer Theorem9.1 identifies Nori and Ayoub Hopf algebras over a PID. These exact theorems do not by themselves identify the archival M.',
  'The absence of a construction is a limit of the supplied sheets, not evidence of why the author left the general theory incomplete.',
  'Highest interpretive priority because a precise choice of category changes the truth and scope of the gerbe and component assertions.', ['Jannsen1992','HuberMuellerStach2017','ChoudhuryGallauer2017'])
p(236,'Separating Lefschetz operators from a tensor subgroup', ['15/90 Pro49–65;15/135 Pro978–986;15/137 Pro1015–1025; SA06-458–460; C-SA06-442–444'],
  'No sl2 construction occurs on these specific pages; the earlier notes propose comparisons using the weight grading and Tate twists.',
  'A Lefschetz sl2 action on a graded realization or Chow motive is compatible with a separate Tate action and need not arise from a subgroup of the motivic tensor group. General Chow hard Lefschetz requires the correct shifted grading and additional hypotheses.',
  'Künnemann Theorems5.1–5.2 p96 give rational Chow-motivic Lefschetz decomposition for an abelian scheme over smooth quasiprojective connected S. Beauville Theorem3.3 and Propositions5.5,5.11 give the SL2 correspondence action and shifted Chow conclusions. P13 verifies the universal string identities and their rational denominators.',
  'This is an earlier-run proposed bridge, not an open question explicitly left by the author in the assigned passage.',
  'Useful as a separate modern comparison task, with the tensor and correspondence actions kept distinct.', ['Kunnemann1993','Beauville2008','DeligneMilne1982'])
p(237,'The proposed singular-hypersurface standard-conjecture link', ['15/101–126 projectivity fragments; supplied cote14 smooth/local Lefschetz passages; SA06-461–463; C-SA06-445'],
  'No singular-hypersurface standard-conjecture formulation occurs in the assigned pages. The proposed connection and A–D lettering come from earlier-run context.',
  'Compare only the explicitly smooth/global and regular punctured-local Lefschetz statements present in cote14, and the independent complete-variety projectivity criterion in cote15. An absent cote16 endpoint cannot be supplied by inference.',
  'The checked abelian-motive Lefschetz sources and Cartier’s numerical ampleness theorem concern distinct statements. Cross-package source checks show smooth affine/hyperplane continuations and a local programme with both punctured spaces regular; they do not establish the claimed singular endpoint.',
  'The missing endpoint belongs to another part of the archive and is not attached here; this is a bounded source finding, not a claim that no such programme exists anywhere.',
  'Worth a later archive-to-archive comparison only when the exact missing endpoint is supplied.', ['Beauville2008','Kunnemann1993','Cartier1966'])
p(238,'Maximal single-valued analytic continuation', ['B15-01/62 lines40–52;B15-01/64 lines75–79; C-SA06-483–486'],
  'He uses gluing and Zorn for maximal extensions and illustrates failure of uniqueness across disconnected overlaps with square-root branches.',
  'An extension is unique on a fixed connected domain; maximal single-valued domains need not be unique. Equality on a nonempty open subset of each connected overlap suffices for gluing, while disconnected overlaps require componentwise agreement.',
  'Bourbaki Variétés §9.3.3 provides analytic uniqueness. P16 proves the chain-union/Zorn argument and the precise overlap conditions; the H/H′ label in the square-root sentence is a separate scan alarm.',
  'The source’s maximality construction is complete at the fixed-domain scope; no unresolved universal maximal-domain uniqueness theorem is claimed.',
  'Useful to prevent the notes from strengthening a germ or fixed-domain statement into false global uniqueness.', ['BourbakiVarietes1967'])
p(239,'Identity of the recycled analytic source', ['B15-01/62,64;B15-02/27–47;B15-03/49–57; C-SA06-483–510'],
  'These analytic sheets give numbered formulas, theorem fragments and editorial questions, but no complete bibliographic identity.',
  'Match statement numbering, typography and pagination to a specific draft or edition before assigning authorship, chronology or a claimed later publication of this exact text.',
  'The opened Bourbaki Variétés fascicles1967/1971, unchanged2007 reprint, provide close mathematical comparisons but explicitly give results without proofs. They therefore do not by themselves identify these proof-bearing recycled sheets. Glöckner’s backwards references to Bourbaki and Cartan are leads, not proof of identity.',
  'The title and continuous source pages are missing from the fragments; no historical reason for the recycling is established.',
  'Worth a focused bibliographic collation, while retaining established mathematical claims separately from classF provenance.', ['BourbakiVarietes1967','Glockner2003'])
(P/'problems.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'problems':len(Q),'first':Q[0]['id'],'last':Q[-1]['id']},indent=2))
