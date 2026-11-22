INCOMPLETE

# D, G, J research record

Research by GPT-6 Astra (OpenAI), delegated task `/root/dgj`, 20 November 2026. No priority is claimed. Manuscript quotations were checked against the supplied diplomatic transcriptions; scans were not supplied in this task. This fragment is not a completed answer to the whole research prompt.

## Outcome table

| Requested item | Present state | Statements |
|---|---|---|
| D.1 both signs and variation | Proved | D1 |
| D.2 nonflat fixed group, nonflat Pic-tau, specialization incompatibility | Proved by explicit quotient families | D2, D3 |
| D.2 modular Igusa family | Complete: both ordinary and supersingular miniversal hulls, all-Artinian Pic-tau flatness, and an explicit modular trait with incompatible Picvar | D4-product, D4-modular-Picvar, D4-first-order, D4-gap, D4-versal |
| G.1 every polarization type over Z[1/2] | Proved: section exists exactly when at most one elementary divisor is odd | G1 |
| G.2 determinant section comparisons | Proved under the polarization hypotheses of Part G | G2a, G2b |
| G.3 Albanese sign and canonical theta class | Proved: c=-lambda_Theta; K=omega_C | G3 |
| J.1 all seven theorems | Incidence Th.1–3 existence/bounds known and exact family kernels proved; modern integral Th.3, raw Th.4, literal Th.5 and Th.7 refuted; all-regular existence and Th.6 unresolved | J0, J1-Th1 through J1-Th7 |
| J.2 canonical integral self-duality for every threefold | Refuted by the generic genus-three hyperelliptic Jacobian in characteristic five | J2a |
| J.2 positivity up to one overall sign | Refuted by E x P1 x P1 over Fbar3 | J2b |
| SA19 H5 | Broad classification refuted; corrected primitive and representability programme unresolved | J0, J2a, J2b |
| SA19 H6 | Complete negative audit of all 195 readable supplied transcriptions; variance inference refuted; no claim of historical absence | SA19-H6 |

## Main completed constructions

The quotient proof is relative in the fppf topology, for abelian schemes A and B with a constant finite group acting by automorphisms on A and by an embedded translation subgroup on B. It gives Pic-tau(X)=Y-dual x (A-dual)^Gamma. The norm identity proves that descended invariant algebraically trivial classes actually belong to Pic-tau. The character ambiguity is removed by the zero section and the dual isogeny kernel, including on nonreduced test schemes.

In characteristic two, shearing involutions attached to Frobenius and Verschiebung give both signs of the Hodge asymmetry. The family y^2+txy+y=x^3 over k[[t]] specializes from ordinary to supersingular. For the square of Frobenius, the finite intersection H=ker(F^2) intersect E[2] has exact algebra R[z]/(z^4,tz^2). Its length jumps from two to four. A Klein-four action produces a fixed group of lengths eight and sixteen and a nonflat relative Pic-tau. A cyclic action produces an image of an elliptic scheme whose kernel degree jumps, which excludes a closed abelian subscheme realizing all fibrewise Picard varieties.

For G the quadratic-refinement torsor gives the explicit section when the alternating pairing on A[2] has rank zero or two. Integral lattice transvections prove impossibility in every larger rank. This works over Z[1/2] without inverting odd divisors of the polarization degree. The determinant proof types its equivariance and tracks the inverse line bundle; canonical-square compatibility follows by choosing symmetric representatives locally. The remaining comparisons use absence of a natural universal two-torsion point and polarized lifting. The Jacobian minus sign was checked directly on the rendered Milne page because both web and local extracted text omit it.

The threefold X=E x P1 x P1, with E: y^2z=x^3-xz^2 over Fbar3, has algebraic representative E^2. The actual family of cycles specified in section_J.tex gives intersection matrix [[0,lambda_E],[lambda_E,0]]. It is an isomorphism, but its diagonal and antidiagonal restrictions are +2lambda_E and -2lambda_E. Neither overall sign is positive. This does not refute the primitive correction written in the manuscript margin.

## Corrections to prior readings

1. **R6, 57:286:** the full Picard product was quoted without the manuscript hypotheses A_Gamma=0 and trivial action on Pic-tau(B). A Poincare class on E x E refutes that unrestricted statement. The restricted Pic-tau formula used here is separately proved.
2. **59:13:** even Euler characteristic does not imply the polarization is twice a class. Type (1,2) is an explicit counterexample. The rank-two quadratic refinement is the correct replacement for the surface conclusion.
3. **59:13-14:** the torsor-power deduction uses a greatest common divisor, not the written least common multiple (ppcm). Several B subscripts on torsors of class delta must be A for the maps to type-check.
4. **59:23-25:** with lambda_L(a)=t_a^*L/L, the selected Albanese convention gives c=-lambda_Theta. The margin's correction has the correct sign.
5. **SA19 H5 and reading 44:8:** raw intersection positivity is false; one sign cannot replace primitive decomposition. The assertion that the modern codimension-two algebraic representative always has the stated integral Tate injection in positive characteristic is overstrong: ACMV explicitly impose the standard torsion assumption outside proved cases.
6. **44:2:** the ambiguous handwritten dual exponent is retained as ambiguous. The letter 44:8 explicitly supplies n+1-i. Existence of a modern algebraic representative alone does not identify the manuscript's Albanese equivalence relation.

## Computations and their scope

`code/check_dgj.py` and `code/check_dgj_output.json` contain the executed exact calculations. Final successful run time: 2.161108 seconds. Inputs are the symbolic Weierstrass coefficients a1=t, a3=1 in characteristic two; shearing matrices; finite F2 spaces of ranks 0,2,4,6; and the explicit elliptic cubic over F3. Outputs check discriminant 1+t^3, [2](z)=tz^2 modulo z^4, lengths 2/4 and 8/16, invariant-refinement counts 1/1/0/0, and the hyperbolic intersection diagonalization. The first run completed mathematical assertions but failed at JSON serialization of SymPy integers; this was corrected by conversion to ordinary integers and rerun successfully. The certificate does not claim to mechanize the geometric descent or algebraic-representative proofs.

`code/check_fermat.py` and its JSON output verify all three singular-ideal charts are empty, the specified rational point lies on the Fermat quartic, and its genus is three. Runtime 0.046760 seconds. Infinite order modulo algebraic equivalence is the cited published theorem, not a computed assertion.

A rendered source page, outputs/milne_jv_p23.png, verifies the sign in Milne's Lemma6.9. Initial rendering failed because the output directory did not exist; creating it and rerendering succeeded.

## Sources opened and access failures

The bibliography records exact source versions. In particular the final Poonen-Rains2011 text was opened from archive.intlpress.com; its numbering differs from the MIT preprint. Milne's 2021 Jacobian notes were downloaded after a first request returned HTTP406; a normal browser User-Agent succeeded. ACMV's 2025 diagonal paper, the 46-page author Bloch-map paper, and the 40-page functorial-regular-homomorphisms paper were opened. Oort's Theorem(8.3).1 on polarized lifting was opened at PDFp29.

Both Chai PDF versions, and an alternate UPenn host, returned HTTP403 via web and urllib. Subsequently the published Chai-Oort2017 section3.9(iv), p35, was opened through Utrecht and its universal first-order nonflatness assertion was located. A later audit found that the inspected indexed Chai v2 section2.4 p7 tangent inference does not prove nonflatness for nonsmooth torsors; the earlier Known classification has therefore been superseded by an unresolved verification gate. The annotated Grothendieck-Mumford letter9 p27 footnote1 was opened too; its auxiliary universal 2-torsion Chern-class assertion is overbroad, so not copied into a proof. Full versal calculation remains unresolved. The original Bloch1984 journal volume has been downloaded, after the web tool rejected its size; the definitions on printed94, the explicit Fermat-quartic statement on95, and Theorem(4.1) with proof on104 were visually read. The cycle over Qbar is now a completed refutation of Th7; products extend it to every intermediate codimension.

## Unresolved gates and attempts

- **Igusa modular family: closed.** Both ordinary and supersingular hulls are proved and algebraized, and all-Artinian Pic-tau flatness refutes the first-order nonflatness assertion. The earlier pending statements below are retained only as chronological audit history.
- **Earlier J.2 Kummer attempt, superseded by J2a:** the rationally chain connected and stably rational cases are covered by opened ACMV theorems. The E x Kummer(F x G) approach fails at identifying an integral lattice without the torsion standard assumption; it remains explicitly discarded as a proof. The independent generic hyperelliptic construction now refutes the universal integral assertion without that assumption.
- **J.1 Theorems1–3 and6:** Saito1979 settles incidence existence, the all-codimension Betti bound and complementary isogeny. J1i proves the family-kernel formulation. General all-regular existence and its identification with the manuscript quotient remain unresolved; the concrete smallest gate is codimension3 on fourfolds. Th6 remains open in its full form. The modern integral duality assertion is refuted by J2a.
- **J.1 Theorem5: literal statement refuted.** J5 chooses i=j=m=2 and both generic cycles zero, so neither the retained sign nor the unspecified equivalence causes ambiguity. Stronger admissibility or vertical-correction formulations are distinct.
- **SA19H6:** exact43:27 and43:30 locators establish the Abel map and Ext1 pullback injectivity; the sweep inference has reversed character variance. The full readable supplied corpus is now audited:184 files read by DGJ and all11 files43:56–66 certified by FHI. No rational-point-to-section injectivity proof was found. The195-file hashed manifest and complete scope discussion are saved; original scans, uncertain/illegible strings and13 absent labels do not support a stronger historical nonexistence claim.

No unresolved row is labelled finished.

## Completed generic-Jacobian refutation and search record

The complete J2a proof is now incorporated in `section_J.tex`; `attempt_J2a_generic.tex` is retained as its separately readable proof file, with the review-draft heading superseded. We choose the algebraic closure of the perfect closure of F5(a0,...,a6) and the Jacobian of y^2=x^7+a6 x^6+...+a0. Its universal algebraic representative descends over that perfect field. A miniversal family gives a rational Tate embedding; Sp6 monodromy and an ordinary-fibre Frobenius-polynomial argument bound its dimension by three. The translation family of the curve has intersection form exactly plus or minus twice the principal polarization. An integral compatible autoduality would therefore force a degree-eight isogeny over the field of definition. The generic S7 action on the six-dimensional A[2] is irreducible, excluding the required nonzero kernel subgroup. All maps, the finite Frobenius spreading, and transfer of monodromy through the pointed hyperelliptic stack are written explicitly. Root performed a separate targeted proof check of the rational quotient, primitive representation, eigenvalue argument, and final degree contradiction; the two requested spreading and coefficient-space details were then supplied.

`code/check_generic_jacobian.py` and its JSON output verify the exact integer exterior-intersection factor -2, the ordinary test curve y^2=x^7-x over F5, all 63 nonzero S7-module vectors, and primitive slope multiplicities. Runtime 0.039411 seconds. These finite checks do not mechanize descent, monodromy, or the universal property.

Before promoting this argument we searched for generic abelian-threefold algebraic representatives, intersection polarizations of degree two, hyperelliptic-Jacobian incidence polarizations, and the canonical autoduality statements of Achter--Casalaina-Martin--Vial. The opened ACMV papers provide descent, miniversal embeddings, and positive results under rational-connectedness hypotheses; Achter--Pries provides full hyperelliptic monodromy, and Achter--Howe supplies the correctly indexed Cartier/Manin congruence. We did not locate this exact positive-characteristic counterexample in those searches and make no priority claim. The counterexample excludes raw integral intersection autoduality, not rational pairings, an isogeny, an appropriately normalized primitive polarization, or an unrelated abstract isomorphism.

## Later proof-audit corrections before checkpoint 02

D4-first-order was earlier classified as Known after locating the statement in Chai-Oort2017. That classification is superseded: D4-gap proves that the tangent comparison in the inspected indexed extract of Chai v2 section2.4 p7 is insufficient, because a finite flat nonsmooth torsor can have exactly those differing absolute tangent dimensions and ranks. This is a gap in the inspected argument; no claim that the actual Igusa assertion is false is made. `check_flat_torsor.py` and its output certify the F2 algebra R[z]/(z²−e1), its free rank2 structure, tangent dimensions4/5 (5/6 after an elliptic factor), unit determinant of the torsor map, and absence of an R-valued section. Runtime0.005110 seconds.

Partsch2013's published text was opened and downloaded; its p95/p99/p100 counts give4 versus2+1 in the ordinary Igusa case, and the origin manipulation on p102 has an unjustified step. These are recorded source gaps, without importing or globally refuting the classification. The direct ordinary-cover deformation attempt is saved separately in attempt_D4_Igusa.md.

For J1-Th6, the Pro transcription reads isomorphisme and the Codex transcription reads isogénie at44:4. The difference is now stated explicitly; no scan-based resolution was available.

## Checkpoint03 addition: explicit modular Igusa degeneration

`section_D_modular.tex`, also incorporated in `section_D.tex`, gives a complete independent mixed-characteristic family. Both elliptics are Y²Z+XYZ=X³+XZ² over W(k), with discriminant−63 and nonzero étale two-torsion P=(0:0:1). The Hensel root 2w²−w+8=0, w≡0 mod2, gives another two-torsion section Q=(−2:1:w) which specializes to the origin. The commuting actions h(x,y)=(x+P_E,y+Q_F) and τ(x,y)=(−x,y+P_F) are free. Their quotient specializes to an ordinary Igusa surface. Its Pic-tau is a μ2-torsor over a fixed dual group, itself an Ebar-dual[2]-torsor over F-dual, hence finite flat of degree8 over F-dual. Nevertheless the Albanese map from F has degree4 generically and2 specially. Dualizing excludes a closed abelian subscheme with all fibrewise Picard varieties. This proves the desired specialization pathology inside a modular Igusa degeneration while keeping Pic-tau flat.

`check_igusa_trait.py` verifies the discriminant, the projective point and negation identities, and Hensel solutions modulo2^n through n=64; runtime0.042306sec. The numerical Albanese degrees in its output are the conclusion of the written universal-property proof, not a finite calculation.

The complete seven-page Chai v2 text has now been opened through web retrieval despite direct PDF403s. The proof gap is confirmed in the full Th2.4 pp6–7. A separate full ordinary calculation, `attempt_D4_ordinary.tex`, now supplies the R-point Serre–Tate coordinates, formal hull, origin quotient, algebraization, and two flat torsor sequences. Its conclusion is being independently audited before promotion; it is not used to prove the modular trait example.

Independent A3 checks for root are saved in `audit_A3_Raynaud.md` and `audit_A3_root_cover.md`. The latter proves the tame full-basis root-cover transfer, checks the characteristic-two globally generated Raynaud input, and verifies the explicit ninth power with556 sections. `check_root_cover_input.py` records the finite dimension arithmetic.

## Ordinary Igusa calculation promoted after independent audits

Root and fhi independently checked the complete ordinary proof, including the exact primary source statements, all-Artinian-point coordinates, dual extension, both finite flat torsor sequences, origin-forgetting hull argument, and algebraization. D4o is now incorporated in section_D.tex and D4-first-order is Refuted: Pic-tau is flat for every Artinian deformation of an ordinary Igusa surface, contradicting the literal Chai2008v2 Theorem2.4(iii) and its later restatement. Earlier unresolved classifications in this chronological record are superseded. The hull is W[[t,s,u,v]]/(s²+2s). A concrete first-order q12=1+epsilon direction and the explicit product curve y²+xy=x³+1+epsilon are included. The latter realizes the finite-flat, obstructed-section torsor directly in an Igusa family. The supersingular first-factor hull remains a separate active gate.

## Supersingular complete proof submitted for review, 16:21 UTC

`attempt_D4_supersingular.tex` now gives the complete candidate proof of the remaining case. The affine involution condition forces the canonical extension point into the multiplicative subgroup of the cover’s divisible group. An explicit pushout then gives the unique fixed ordinary elliptic subgroup, with finite flat levels proved directly. The cover is reconstructed as a graph quotient of E times F, parameterized by a formal point of E-dual[2]. The affine norm equation removes the ordinary F parameter. For E_t:y²+txy+y=x³, exact elimination gives the hull W[[t,s,u,v]]/(s⁴−ts²−2s), finite free of rank4 over W[[t,u,v]]. Flatness of Pic-tau for every supersingular Igusa deformation follows already from the subgroup construction and the same two fppf torsors as in the ordinary case. This is under independent audit and is not yet promoted.

`check_igusa_supersingular.py` and its saved JSON output verify the exact coordinate identities and the finite flat polynomial algebra, runtime2.278230sec. Initial assertions compared expanded and unexpanded symbolic expressions; they were replaced with difference-to-zero checks and the final run passed. The newly opened primary Tate1967 chapter supplies precise connected–étale and Cartier duality foundations, recorded in references.bib.

## Supersingular calculation promoted after two independent audits

Root and fhi independently checked the full seven-step supersingular proof. It is now incorporated into section_D.tex and saved separately as section_D_supersingular.tex. Both requested formal modular cases are determined explicitly: ordinary W[[t,s,u,v]]/(s²+2s), supersingular W[[t,s,u,v]]/(s⁴−ts²−2s). Both hull families algebraize. Every Artinian Igusa deformation has a canonical fixed ordinary elliptic subgroup of its abelian double cover; the dual fixed group is an elliptic-two-torsion torsor, and Pic-tau is a mu2 torsor over it. Hence Pic-tau is flat in every such deformation. The explicit modular trait still has incompatible fibrewise Picard varieties, as separately proved in D4m. D4 is complete within the stated Igusa family. All preceding draft and unresolved statements about the supersingular calculation are historical and superseded.

## Literal Theorem5 refuted by a split quadric fourfold

The full proof is incorporated in section_J.tex and separately saved as section_J5_quadric.tex. Root audited both exact44:4 transcriptions and the complete example. Over Fbar3, let X be x0*x3+x1*x4+x2*x5=0 and take the hyperplane pencil x2=t*x5. All fibres are geometrically integral; its base is a smooth quadric surface, and the two singular fibres are ordinary rank4 quadric cones. Four explicit planes give Z=alpha−beta and Zprime=alpha-prime−beta-prime. Both generic restrictions cancel as actual cycles, so every relevant Neron–Tate pairing is zero. The proper intersections on X are two transverse points and two empty pairs, giving degree2. This is the balanced case i=j=m=2, so the retained sign is unambiguous. It refutes the stated formula including the integral-fibre insertion, independently of the unspecified cycle-equivalence relation. The displayed planes meet the pencil base in excess dimension, which is not excluded in the literal statement; no stronger admissibility comparison is claimed refuted.

The exact criterion for an intersection form to descend through restriction is that the kernel be orthogonal to all classes. Restricting to its orthogonal complement gives a precise elementary corrected quotient. Geometric integrality of fibres alone does not impose this in codimension2. The finite certificate check_quadric_height.py checks all displayed equations and proper intersections, runtime0.074211sec.

## Exact incidence construction and regular-representability gate

The newly integrated section_J_incidence.tex replaces an overly broad unresolved description of Th1–3. Saito1979 Definition3.1 p108, Proposition3.4 pp109–110 and Theorem3.6 pp110–111 construct the incidence quotient in every codimension over every algebraically closed field and prove the half-Betti bound. The short family argument proves the common incidence kernel equals the kernel of its represented family map even as group schemes. Proposition4.4 p113 supplies complementary isogeny with miniversal-cycle integer factors, not the raw integral isomorphism.

Kleiman1971 ICM pp446–447 explicitly distinguishes Samuel abelian equivalence, defined using all regular homomorphisms, from Picard/incidence equivalence and attributes the boundedness observation to Grothendieck in1964. The full47MB primary volume was downloaded after the web opener refused its size, and exactly printed445–449 are extracted in sources/kleiman1971.pdf. These primary locators support the historical connection without asserting an identity of equivalence relations.

For all regular maps, the common family kernel gives a closed quotient individually; a uniform bound over all families is equivalent to existence of a universal regular homomorphism by Saito's Theorem2.2 pp103–106. Codimensions1,2,n are known; the codimension2 proof repair is Kahn2021, author versionpp2–4, and ACMV Proposition8.2 p31 explicitly limits its cohomology injection to these three indices. Kahn's Conjecture1 p5 asks nonexistence for A³ of a specified generic-abelian-threefold times nonisotrivial-elliptic fourfold. Infinite cycle torsion does not itself produce unbounded regular targets, and this remains an exact active gate.

A simple E×P1² family also shows why the self-kernel in the letter at44:9 cannot be silently used as the common kernel: Poincare*h1 has zero self-pairing but pairs by elliptic duality with Poincare*h2. Its self-kernel is E and its common incidence kernel is zero. The finite intersection matrix was already certified in check_dgj.py.

Two further transcription conflicts are retained: en substance versus ensemblistement in Th1, and Connu tel quel versus a form of Annulé/Cancelé tel quel beside Th4. No scan was supplied to resolve them.

## Explicit Artinian Picvar counterexample, independently audited

D4a is integrated into section_D.tex and saved separately as section_D_artin_picvar.tex. For R=Fbar2[epsilon]/epsilon² take E0=F0:y²+xy=x³+1, P=(0,1) on F0, and the actual ordinary Igusa deformation with q12=1+epsilon, all other qij=1. Its Pic-tau is flat by D4o, but no abelian R-scheme can map into it lifting the special Picvar inclusion. Such a map would pull back to f:B→A-dual. Its special map is (0,phi-dual):(F0/<P>)-dual→E0-dual×F0-dual. Since ker(phi-dual)=mu2, the étale Tate map is an isomorphism onto the F-dual factor, while the dual map kills the E factor. Katz's exact lifting criterion and transpose formula force1=q12=1+epsilon, a contradiction. This avoids every image-flatness assumption. The open neutral component argument ensures the pullback lands in A-dual.

Root and bce independently audited the full argument and exact Katz source. This refutes the Artinian compatible-abelian-subscheme interpretation of57:311. The source superscript00/infinity and the uncertain wordlocal remain explicit. Grothendieck's FGA VI Remark3.4 p238 already states a first-order Igusa failure of the canonical abelian subgroup; the present construction supplies fully specified dual-number coordinates and proof, without a priority claim. code/check_artin_picvar.py and its JSON output certify the finite ring arithmetic (runtime0.000005sec).

## Complete scoped SA19H6 corpus audit

The full195-file readable C43 corpus is now covered: DGJ read184 complete transcription files, and FHI expressly certified all eleven files43:56–66. No argument injecting rational points into sections of an arithmetic fundamental-group exact sequence was found. This is a scoped documentary finding, with no implication of absence from unresolved handwriting or other archival material. The detailed audit identifies misleading near matches and separates them from the actual Ext1 pullback injection at43:30. The stronger direction in the manuscript remains qualified by Il semble. The character-variance proof refutes the sweep's inference from that injection to fundamental-group injectivity.

The reproducible manifest outputs/c43_audit.tsv records full source paths, SHA256 hashes, readers, topics, and macro counts. build_c43_audit.py reports195 files,375496 bytes,2620 uncertainty macros,48 illegibility macros,13 absent scan labels; runtime0.015091sec. The code inventories the documentary evidence and does not purport to prove mathematical or historical absence. audit_SA19H6.md gives the complete scope and leaf-level distinctions.

## Conditional incidence Lefschetz theorem and a targeted cross-audit

J6L is integrated into section_J.tex and separately saved as section_J_lefschetz.tex after root's independent source-and-proof audit. In arbitrary characteristic, the relevant algebraic Lefschetz lowering operator onX gives an isogeny on incidence representatives in the stable range; the corresponding operator onY gives surjectivity in the high range. A complete cohomological detection lemma supplies the step from rational cohomology to the incidence homomorphism. The fixed-part clause, removal of algebraicity hypotheses, alternate integral-isomorphism reading, and all-regular identification remain unresolved. This is a strict stated reduction, not full closure ofTh6.

The separate audit_E4_tauclosed.md records a PASS for BCE's trait argument for tau-closedness without projectivity. The exact primary sources and complete matrix/Hodge-index/Galois-averaging/normalization/negativity chain were independently checked. Root is separately auditing the arbitrary-base approximation step.

## Codimension-two trace theorem and top-target Lefschetz case

J6P and J6Z are now integrated after root independently reopened the exact inputs and audited the complete proofs. For a smooth projective n-fold with n>=4 and a hyperplane pencil with smooth codimension-two axis, the image of Ab2(X) in the generic member’s Ab2 equals its K/k-trace image. The proof spreads a miniversal cycle over the blowup, uses the actual Ab2 blowup product, and absorbs the exceptional Picvar of the axis using degree-one weak Lefschetz and the projection formula. For n>=5, constant H3 and ACMV’s miniversal Tate injection give rationality of all prime-to-characteristic power torsion; Lang–Neron forces the trace to be surjective. Thus generic stable-range surjectivity is unconditional in every characteristic under the smooth-axis hypothesis.

The finite-kernel step is also proved, with its exact additional torsion-injectivity condition on the target universal map. That condition is known in characteristic zero and explicitly left open generally by ACMV Remark8.6; their Proposition8.2 alone does not imply it. This yields a characteristic-zero isogeny in the stable range and an isogeny onto the trace image in the middle case, still with smooth axis. No conclusion about singular pencil axes or the unspecified manuscript equivalence is hidden in these results.

Independently, J6Z proves surjectivity Pinc^(n-1)(X) to Alb(Y) for every smooth hyperplane section of every smooth projective n-fold, n>=3, in every characteristic. Intersecting Picvar(X) with H^(n-2) produces a map whose restriction is an isogeny onto Alb(Y), by weak and hard Lefschetz in degree one. It also proves the modern Ab2 assertion on arbitrary threefolds. The broad Th6 remains on the unresolved list.

Literature searches for universal regular homomorphism, nonexistence, Kahn Conjecture1, and codimension-three fourfolds found no newer primary resolution in the retrieved results. Kahn’s concrete conjecture and the general regular-representability gate remain unproved here; absence of a search result is not a proof of historical or mathematical open status.

## Literal middle Lefschetz clause refuted by an explicit cubic pencil

J6C is now integrated after independent complete-file audits by root and BCE. Over Fbar5, take the smooth cubic fourfold X: x0^3+x1^3+x2^3+x3^2*x4+x4^3+x5^3=0 and pencil x5=t*x4. Its axis is a cone over the constant Fermat elliptic curve E; every pencil member is geometrically integral, and the generic member is smooth. Both44:4 transcriptions require a generic member of an integral-fibre pencil, not a general pencil or a smooth axis. The optional cycle hypotheses hold with both cycles zero. Thus the literal quantifiers are met.

The ambient H3 vanishes, so both Ab2(X) and Pinc2(X) vanish. On the generic cubic threefold Y, blow up the cone vertex. Its strict transform S is a P1-bundle over E, with normal degree minus two on a ruling. The maps u=pi_* i_* q* and v=q_* i* pi* give v u=[-2] on Pic0(E). The point-blowup exceptional Z summand disappears precisely on algebraically trivial CH2. The constant elliptic image of u therefore survives in the K/k-trace, including for incidence equivalence because v is an actual Picard test. This contradicts the zero ambient image. The assertion is refuted without relying on disputed integral autoduality.

The independent audits checked all fibres, the regular-sequence blowup of the pencil, the multiplicity-three calculation, signs, regularity, and incidence detection. check_cubic_trace.py records exact characteristic-five polynomial certificates, runtime0.075394sec. BCE separately produced an exact certificate, runtime0.102263309sec. The smooth-axis correction J6P is unaffected; the full stable/high clauses, the positive-characteristic finite-kernel gate, and the alternative integral-isomorphism reading remain unresolved.

Existing-source searching found the relevant classical Eckardt-point geometry in Clemens–Griffiths1972 Lemma8.1 pp314–315 and Roulleau2009 Proposition10 p384, Lemma29 p398. Those sources were opened. Their complex-geometric context is not imported as a characteristic-five theorem; the proof above is algebraic and explicit. No novelty or priority claim is made for this construction.

## Igusa Albanese fibration lifting obstruction promoted

D4b is now integrated after root's independent audit of the full argument and the exact published Partsch2013 pp102–106. The actual ordinary Igusa deformation D4a over Fbar2[epsilon]/epsilon² cannot lift its special Albanese fibration to any smooth proper curve. A lift would give a homomorphism from an elliptic abelian Picard scheme into Pic-tau lifting the canonical special Picvar inclusion, which D4a rules out for every possible elliptic deformation. Its special fibration is Jacobian, so the literal assertions in Proposition6.6, Theorem6.7 and Proposition6.9 are refuted in their stated ordinary Igusa scope. This supplies a geometric contradiction beyond the previously observed tangent-count discrepancy.

The small map (Z/2)_R to mu2_R, 1 mapping to1+epsilon, is nonzero but specializes to zero. It separately diagnoses the p103 invocation of etale rigidity when only the source is etale; it is not substituted for the geometric example. check_partsch_etale_step.py and outputs/check_partsch_etale_step.json record the exact finite calculation, runtime0.000012sec. Grothendieck's FGA VI Remark3.4 p238 already records the first-order Picvar obstruction. A search of retrieved publisher/author records found no correction, which is only a limited search result. No priority claim is made.

## Precise Walker gate and fresh literature verification

section_J_walker.tex is integrated. For complex X, Walker universality among all regular homomorphisms is equivalent to the combined-image dimension test dim image(usual AJ,phi)=dim Ja for every regular test phi. The proof uses only the established isogeny-lift initiality and surjectivity. This condition has not been established or refuted for Kahn's proposed fourfold. Divisibility of the Abel–Jacobi kernel is not sufficient. The August5,2026 ACMV revision and Kahn's final published pp844–847 were checked, including the final Conjecture3.1 locator. General regular representability remains an explicit active gate.

## Focused main-question cross-check: leading Cartier obstruction

A2_cartier_leading.tex supplies A2V for root integration. The closed-form order argument was proposed by root and independently checked: a nonzero closed global form vanishing on a smooth ample divisor has order divisible byp. For a Cartier-fixed form of exact orderpa, the nonzero tangential leading term belongs to B1_Y tensor L^-a; it is therefore a nonzero element of the Frobenius kernel on H1(Y,L^-a). The ambient numerical condition h0Omega_X >= h0O_X(pY) and necessary nonnormality of the associated mu_p cover are proved. The local affine form dlog(1+t^p*x) has exact orderp and prevents a naive p² iteration. The exact finite certificate (p2,3,5,7;32 output coefficients each) passed in0.000361sec. This does not solve the global smooth very ample point-kernel question; realizing or excluding the leading Frobenius-kernel data globally is the remaining gate.

## Closed-forms exclusion for the main point-kernel question

A2_closed_forms.tex proves A2W: if every global regular one-form is closed, then H0(Omega1_X tensor L^-1)=0 for every very ample L on a smooth projective n-fold, n>=2. Multiplying a putative section by very ample coordinates gives forms whose differentials are the coordinate differentials wedged with the original form; the coordinate differentials span the function-field cotangent space, giving the contradiction. For n>=3 this excludes every point kernel using the finite p-group reduction. Root independently passed this proof. The same argument shows that any point-kernel example must have at least n-1 independent nonzero differentials of global one-forms. This is a strict searched-example restriction, not a universal closedness claim.

## Target-side Frobenius and W2 exclusions

A2_target_frobenius.tex proves the proposed A2Y criterion: for n>=3 a smooth very ample target Y cannot have a nonzero Picard point kernel if Frobenius on H1(Y,OY) is injective, or if Y itself has a smooth W2 lifting. In the first case the forced negative-twist H1 class injects into H1(OY) using a connected smooth Bertini divisor, and the Frobenius square gives a contradiction. In the second case Langer2011 Corollary11.2 p2116 kills the required H1 in total degree1, valid for every p and every dimY>=2. No lifting of X or of the polarization is used. This strictly narrows the remaining target-side gate; it does not solve the general point-kernel problem. Submitted for independent root audit.

### A2Y independent review (19:03 UTC)
The root independently checked the complete proof and opened Langer's published Section 11 and Corollary 11.2, p. 2116. PASS: the Bertini divisor is connected in target dimension at least two, scalar global sections give the required injection, and the Frobenius square uses multiplication by `s^p` on its right side. The lifting variant requires a smooth W2 lifting of Y alone. Main A2 remains unresolved.

### A2Z: the separable degree-p cover route is excluded
The full proof is in `A2_fierce_cover.tex`. If a finite flat generically separable degree-p map between smooth projective varieties has smooth ample full inverse image Y of a smooth divisor C, then Pic(C)[p](k) injects into Pic(Y)[p](k). A killed nontrivial class makes Y the normalization of its integral mu_p torsor. Finite duality gives an effective conductor D and relative canonical class -D. Ambient adjunction instead gives the restriction of the effective ramification divisor R, which contains Y. Intersecting yields 0=R.Y^(n-1)+D.(Y|Y)^(n-2)>0. This excludes the proposed fierce Artin–Schreier realization, including normalization of a nonnormal residue torsor; it does not settle A2 in general.

### A2S: surface-target classification and a bound on the leading order
For a threefold point-kernel example, A2V forces a negative H1 failure on the surface target Y. Martinez2024 Theorem1.1 (full primary PDF opened) excludes every birational class except general type and quasi-elliptic Kodaira dimension1; it also forces a²L²<=6C[Y] for the A2V integer a. `A2_target_surfaces.tex` contains the short deduction. Xie2011 has the same qualitative result in its official abstract, but its full PDF was inaccessible; no theorem number for that source is supplied. The HEP page's raw extracted retraction paragraph is an unpopulated hidden generic template (empty retractedArticleId), so it is not evidence of any retraction. Main A2 remains unresolved.

### A2Z independent review (19:41 UTC)
Root independently passed the full conductor/adjunction argument, including nonnormal torsors and the scheme-theoretic full inverse-image hypothesis. The precise finite-duality citation is Stacks Lemma 47.15.8. Owner row A2Z-cross is marked canonicalized by the root integrator.

### A2S reconciliation with A3s (19:48 UTC)
The earlier general-type-or-quasi-elliptic wording was weaker than the existing root A3s result. Since L^a is very ample, the quasi-elliptic case is already excluded by Zhang2022 Th3.1. The stable A2S now states general type, with the Terakawa numerical bound applied to a²L². Martinez supplies only an additional optional numerical bound. Read the root A3s argument and the complete local Terakawa Th1.6 / Zhang Th3.1 proofs; their scopes match this application.

### A2Gs: obstruction to the smooth surface torsor model
The complete submitted proof is in `attempt_A2_Gs_smooth_surface.tex`. A smooth projective surface cannot carry a line subbundle O(-D) of its tangent bundle tangent to a smooth ample D. Adjunction and Chern classes give K.D=0 and c2=-D²<0. Kodaira dimension zero is impossible; on a ruled model the explicit integer identity (2a²-4)(g-1)+sum[m_i(a-m_i)+1]=0 contradicts ampleness, including infinitely near blowups. A smooth G_s-torsor with smooth full inverse image differentiates to precisely such a subbundle. Opened Liedtke2013v4 Theorems4.4–4.5 and Section7 for surface classification. Exact symbolic intersection certificate is `code/check_Gs_ruled_identity.py` with `outputs/Gs_ruled_identity.json`. This is a construction exclusion only; singular normalizations remain unhandled. Submitted for root audit.

### A2 quasi-elliptic cusp route (19:58 UTC)
`attempt_A2_quasielliptic_cusp.md` records the numerical obstruction to making a smooth purely inseparable cusp multisection ample by passing to a non-Jacobian twist. With base genus g>=1 and degree r>=2, canonical adjunction and chi>=(1-g)/3 imply D²<=(2-5r/3)(g-1)<=0; at g0 there is no p-torsion from the base. This remains a route exclusion, submitted for review. Opened the exact Katsura–Saito2021 p1255 passage and Liedtke2013 Th5.6; Lang1979 Prop2.1 is p481.
