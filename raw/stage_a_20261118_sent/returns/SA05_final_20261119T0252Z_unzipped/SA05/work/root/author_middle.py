#!/usr/bin/env python3
"""Manually authored middle-cote12 records, following complete source reading."""
import json
from author_items import items,add,P,MP

add(61,[],'reading question',[51],'Pro middle4–31; K12-03 5–26','H^i_!(X)∈M_n',
 'Two geometric filtrations are used. The literal membership of every compactly supported cohomology group of a smooth n-fold in the weight≤n category fails for X=P1, i=2: H2=Q(-1) has weight2.',
 'Both witnesses retain the offending n. Replacing the weight filtration by the dimension filtration, or changing the index with the cohomological degree, are distinct possible repairs; neither is adopted without the scan.',
 'understates','The earlier note separates the filtrations but does not isolate this elementary counterexample.',middle=[1])
add(62,[],'conjecture',[51,73,76],'Pro middle27–31,454–481,550–567; K12-05 52–83','M motif ct tordu de poids ρ; −2≤ρ≤1',
 'The bounds are valid in their usual smooth constant-coefficient setting, but the sharper displayed ordinary-cohomology bound cannot hold for every lisse geometric coefficient of weightρ. For the Legendre family over F5, H1 of its weight-one rank-two sheaf has weight4.',
 'After twist(2), the coefficient has weight−3 and absolute H1 is nonzero. This uses geometric monodromy, duality and the exact Legendre trace formula. The separately printed interval[-2,1] is weaker than[-2,0], not false merely because it is weaker. Weight zero alone does not mean eigenvalue1.',
 'agrees','The notes correctly distinguish restricted constant coefficients, arbitrary lisse coefficients, and the logical status of the loose endpoint.',middle=[2,30,31,64])
add(63,[],'conjecture',[53],'Pro middle64–79; K12-03 52–67','car il résulte des conjectures de Tate',
 'The proposed bijection from a Grothendieck ring of motives to its realized image uses the Tate conjecture to distinguish nonisomorphic simple motives and identify morphisms. Faithfulness of realization alone does not prove the claimed injectivity on K0.',
 'The domain, equivalence relation on cycles and semisimplicity must be fixed before formulating a theorem. No unconditional numerical-motive realization is supplied.',
 'agrees','The Tate condition is explicit on the page and must remain in the assertion.',middle=[5])
add(64,[],'conjecture',[54],'Pro middle87–98; K12-03 74–85','à coefficients entiers',
 'Effectivity is conjecturally characterized by integrality of Frobenius characteristic coefficients in the appropriate arithmetic convention; the proposed dimension filtration adds corresponding Tate-scaled integrality tests.',
 'Geometric Frobenius and its inverse have opposite integrality behavior. The direct integrality theorem for actual geometric objects and the converse effectivity conjecture are different statements.',
 'agrees','The margin invokes Tate; the notes correctly do not replace the converse by a theorem about weights.',middle=[7])
add(65,[],'unproved claim',[54,55],'Pro middle116–134; K12-03 96–113','Ce sont des racines de l’unité; quotient fini',
 'For an effective weight-zero object with the stated integrality conditions, Kronecker gives root-of-unity eigenvalues. A finite monodromy conclusion additionally needs the semisimplicity/rationality and bounded-order input used by the argument.',
 'A nontrivial unipotent representation has all eigenvalues1 and infinite image. This refutes the inference from eigenvalues alone, not the conditional assertion with the required semisimplicity.',
 'agrees','The note identifies the extra input without falsely attributing an unconditional realization-semisimplicity theorem to the page.',middle=[8])
add(66,[],'self-flagged step',[55],'Pro middle134–140; K12-03 113–119','ne se généralise guère via filtration de π1',
 'The author rejects a naive extension of the dimension-type filtration through a filtration of the ordinary fundamental group and asks for a better Galois description.',
 'A Tannakian group of a specified tensor category is a plausible replacement, but is not the construction made on this page.',
 'agrees','This is a surviving warning and question, not a proved filtration theorem.',middle=[9])
add(67,[],'unproved claim',[56,57],'Pro middle147–188; K12-03 126–162','commutant; Q_l-espaces engendrés',
 'Under the stated semisimplicity and correspondence-identification hypotheses, the double-centralizer theorem identifies the image associative algebra from its commutant. The recovered cycle data are Q_l-linear spans, not distinguished individual algebraic cycles.',
 'Finite-dimensional semisimple modules are required for the bicommutant step. Identifying the commutant with algebraic correspondences is the Tate input, not a consequence of linear algebra.',
 'agrees','The notes preserve both the conditional theorem and its explicitly limited conclusion.',middle=[10,11])
add(68,[],'unproved claim',[57],'Pro middle170–183; K12-03 147–158','extensions finies de K; algèbre de Lie',
 'For a continuous finite-dimensional representation of a compact l-adic analytic Galois image, the union of invariant spaces over finite extensions equals the invariant space of the analytic Lie algebra.',
 'An invariant vector for the Lie algebra is fixed by an open subgroup; compactness and finite dimension are part of this argument. The analytic Lie algebra is not automatically the Lie algebra of the Zariski closure.',
 'agrees','The note correctly interprets the Gothic Lie algebra and the change of invariants.',middle=[12])
add(69,[],'idea of the earlier run',[57],'Pro middle184–188; K12-03 159–162','seulement l’algèbre enveloppante',
 'Equality of associative envelopes does not identify algebraic subgroups: SL2 and GL2 in their standard characteristic-zero representations both span M2 and have the same scalar commutant.',
 'The explicit example is the earlier run’s elucidation, independently recomputed here. It does not purport to be a counterexample to an assertion of group equality by Grothendieck.',
 'agrees','The manuscript itself limits the conclusion to the envelope.',middle=[13])
add(70,[],'conjecture',[57,59],'Pro middle227–235; K12-04 203–211','On pense que l’image provient d’un motif',
 'The author proposes an l-independent motivic Lie object giving the Galois-image Lie algebras. The proposal needs a choice between analytic image Lie algebras and algebraic monodromy Lie algebras.',
 'For finite-field Frobenius with polynomial T2−T+5, the compact procyclic l-adic image has analytic dimension1 whereas its Zariski closure can be a two-dimensional torus. This prevents an unqualified identification of the two targets.',
 'agrees','The notes flag an inference gap in a modern interpretation, not a theorem already established on the page.',middle=[15,16])
add(71,[],'conjecture',[60,62,63,64,71],'Pro middle242–255,273–340,397–438','Cohomologie absolue; On veut',
 'Absolute cohomology is specified by desired derived functors, transitivity, continuity, H0=Hom(1,M), arithmetic l-adic comparison and finite-dimensional rational groups. These axioms do not construct the theory.',
 'The finite-field even/odd pattern suggests a Weil-group comparison, but the whole proposal is neither ordinary rational étale cohomology nor any later motivic cohomology theory without qualification.',
 'agrees','The notes correctly separate desiderata and later analogies.',middle=[18,21,23,62])
add(72,[],'other',[61],'Pro middle266–269; K12-04 242–244','par le changement de base',
 'A cancelled reused typescript fragment about base change interrupts the manuscript. It is documentary evidence of reuse, not an additional motivic axiom.',
 'An exact published EGA identification requires more context than these two surviving lines. It is kept separate from the more identifiable reused fragment at scan72/66.',
 'agrees','The note correctly retains the reused face without assimilating its subject to the live manuscript.',middle=[19])
add(73,[],'self-flagged step',[62,63],'Pro middle283–322; K12-04 259–292','on espère que Ext¹; je doute',
 'The author hopes that degree-one absolute extensions coincide with Yoneda extensions, then doubts higher effaceability and considers Ind-motives as a possible enlargement.',
 'Ext1 in an abelian category has its usual Yoneda meaning. Identifying a proposed cohomology theory with derived Ext requires a construction and effaceability; it is not supplied by the notation.',
 'agrees','The change from hope to doubt is preserved, including the proposed rather than proved Ind-category remedy.',middle=[20,22])
add(74,[],'reading question',[64,65,71],'Pro middle327–368,397–438; K12-04 299–330','correspondances rationnelles; H^i=0',
 'The cycle target is rational algebraic cycles modulo the selected equivalence relation, not all Q_l-linear classes. The draft vanishing of higher absolute cohomology after algebraic closure conflicts with the later odd unit calculation under the written restriction maps.',
 'For H1(Fq,Q)=Q and restriction multiplication by extension degree, the direct limit over finite fields is Q, not0. Index variants Ri/R2i and j+1/2j+1 must be checked on ink.',
 'agrees','The note identifies a genuine conflict of axioms and comparison conventions, not a harmless change from rational to l-adic coefficients.',middle=[24,25])
add(75,[],'self-flagged step',[67,69],'Pro middle380–388; B12-01 32–55','Q(n)[2n+1]; à développer',
 'Arithmetic duality is proposed with shift2n+1 for schemes proper over SpecZ; the reused continuation at scan69 analyzes the finite-field cyclic case with H1(Fp,Q)=Q and pairings in complementary degrees summing to1.',
 'The extra arithmetic degree is compatible with a Weil-group model, not the continuous cohomology of the profinite group with discrete Q. The cup products are expressly left to develop. Geometric purity has a different shift.',
 'understates','B12-01 supplies an attached continuation omitted from the Pro page selection; its exact extra hypotheses and unfinished product construction are now included.',middle=[26])
add(76,[],'unproved claim',[71],'Pro middle397–438; K12-05 7–45','conj. de Tate + semi-simplicité',
 'The Hochschild–Serre two-term complex gives even-degree invariants and odd-degree coinvariants. Tate identifies the cycle part; semisimplicity at eigenvalue1 is needed to identify invariants with coinvariants through their natural map.',
 'The unipotent Jordan block has equal invariant and coinvariant dimensions but zero natural map between them. Odd-degree identifications need a generator/normalization of the arithmetic direction.',
 'agrees','The note correctly retains the separate Tate and semisimplicity inputs and the noncanonical odd-degree normalization.',middle=[27,28])
add(77,[],'reading question',[66,72],'Pro middle444–449; B12-01 13–17; K12-05 scan72','B_h ... A_h-module libre',
 'The same reused EGA algebra fragment has incompatible scan labels: Pro/K12-05 assign72, B12-01 assigns66. Its displayed localization/freeness statement appears to lose a prime or a base-ring label.',
 'The proof tensors A′/pA′ over A/p with B and chooses h in B, supporting B′_h free over B_h rather than B_h free over A_h. This remains a reading alarm, not an emendation.',
 'understates','The note noticed difficult algebra but did not compare the conflicting attached page labels.',middle=[29])
add(78,[],'reading question',[74,76],'Pro middle503–516,550–555; K12-05 92–110','pur de poids1; poids1−1=0',
 'An abelian variety over a finitely generated field is spread to an abelian scheme over a regular model. Its rational Tate module is identified motivically with R1f_*Q of the dual abelian scheme, twisted(1), hence has weight−1 in the manuscript’s conventions.',
 'The printed weight+1 conflicts with both this expression and the later weight1−1 calculation. Extending K-points to sections uses regularity and the extension theorem for maps to abelian schemes, not properness alone.',
 'agrees','The proposed sign correction is supported by both formulas but remains pending the scan.',middle=[32])
add(79,[],'conjecture',[75,76,80],'Pro middle520–567,635–641; K12-05 113–157,241–248','raisons heuristiques convaincantes; essentiellement équivalente',
 'The Kummer exact sequence identifies the rational-points contribution inside H1(S,V_l A), with remaining term V_l H1(S,A). Its vanishing, and under finite-cotype hypotheses finiteness of the l-primary torsor group, is a substantive Sha-type conjecture. The rank comparison is qualified as essentially BSD.',
 'Weight zero does not eliminate this term. A rank equality is weaker than the full leading-term BSD formula. The precise global-function-field implication of Kato–Trihan does not settle all finitely generated bases or all number fields.',
 'agrees','The notes preserve the finiteness hypothesis and the limited BSD comparison.',middle=[33,34,40])
add(80,[],'withdrawn in the same text',[76,77,79],'Pro middle550–590,610–617; K12-05 143–181,211–222','(M⊗Q/Z)^π; surj. à noyau fini',
 'For a discrete lattice M with profinite action, H1 is the invariant Q/Z quotient divided by the image of rational invariants. A comparison initially called bijective is later weakened to surjective with finite kernel. At degree zero, rationalizing the section lattice likewise only recovers sections modulo finite groups.',
 'For trivial M=Z, H1_cont(Zhat,Z)=0 while (Q/Z)^Zhat=Q/Z. For a nontrivial finite A(Fq), the rational section lattice is zero but the section group is not. These examples check the omitted quotient and finite-error conventions.',
 'understates','The note catches the H1 quotient and later finite-kernel correction; the degree-zero finite torsion issue is added here.',middle=[35,36])
add(81,[],'unproved claim',[78,82],'Pro middle597–606,645–673; K12-05 187–206,251–278','qui est non nul; H^i(C,A)=0 si i≥2',
 'For a positive-genus proper smooth curve C/Fq and its constant Jacobian J, the rational l-adic degree-two term is End_{Fq}(J)⊗Q_l and is nonzero. Inverse Kummer also gives a nonzero V_l H2(C,J×C), so the later literal vanishing contradicts this worked example.',
 'The endomorphism tensor must contain a dual (or the corresponding polarization twist). The later local/global deductions cannot use the uncorrected vanishing. No cancellation of the later sentence is visible in the supplied witnesses.',
 'agrees','The contradiction is between two surviving places, unlike the explicitly cancelled drafts.',middle=[37,41])
add(82,[],'self-flagged step',[79],'Pro middle621–625; K12-05 224–231','surjectif mod groupes finis ??',
 'The author asks whether a Sha-type finiteness assertion is approximately equivalent, via Jacobians, to surjectivity modulo finite groups of a Brauer comparison for a fibration.',
 'A precise theorem must specify the base and total space, relative Picard/Jacobian, period-index corrections and the relevant Leray differentials. A theorem about a surface over a finite field is not the unrestricted formulation.',
 'agrees','The double question mark and approximate equivalence remain part of the statement.',middle=[38])
add(83,[],'conjecture',[79],'Pro middle628; K12-05 234–236','fini aussi pour i≥3',
 'Higher l-primary cohomology H^i(S,A), i≥3, is expected to be finite for the abelian scheme under discussion.',
 'The dimension, regularity, arithmetic type of S and finite-cotype inputs are not fully stated on the line. Vanishing of a rational Tate module alone need not imply finiteness without them.',
 'agrees','The note rightly requires a restricted modern formulation and does not treat the margin as a general theorem.',middle=[39])
add(84,[],'unproved claim',[82],'Pro middle665–673; K12-05 270–278','essentiellement un p-groupe, modulo groupe fini',
 'Over a nonarchimedean local field of residue characteristic p with finite residue field, local duality makes the prime-to-p primary parts of the Weil–Châtelet group finite, with a potentially large p-primary part.',
 'The statement is qualified modulo finite groups. It does not say all torsors are p-primary or imply vanishing of the global degree-two group.',
 'agrees','The qualification is already on the page; the note is right to restore it when comparing abbreviated modern prose.',middle=[42])
add(85,[],'unproved claim',[84],'Pro middle681–724; K12-05 283–323','coBrauer; Q_l(1)',
 'Kummer sequences distinguish the l-adic completion of units, Picard contributions and the Tate module of the Brauer group in H1 and H2 with Q_l(1) coefficients.',
 'The prime l must be invertible on the base, and inverse-limit/exactness or finiteness hypotheses must be stated. The manuscript’s p-adic ambiguity is not resolved by silently applying étale Kummer at p.',
 'agrees','The note correctly keeps the three sources of cohomology distinct.',middle=[43])
add(86,[],'idea of the earlier run',[84],'Pro middle721–724; K12-05 320–323','le rang ... augmente d’autant',
 'For a smooth proper geometrically connected curve over a finite field, removing r≥1 closed points gives l-primary Brauer corank r−1, not r: the normalized local invariants satisfy one global sum relation.',
 'For r=1 the prime-to-p Brauer group remains zero. This is a correction to the literal point-count increment, under the stated curve hypotheses.',
 'agrees','The earlier run proposed this correction; the residue calculation is independently checked here.',middle=[44])
add(87,[],'idea of the earlier run',[84],'Pro middle703–714; K12-05 302–313','H^i(X,Q_l(1))=0 ... si i≥4 ??',
 'The unrestricted proper-scheme vanishing question has a negative answer. Let D be the union of four coordinate planes in P3/Fq and X=D×P1. For l≠char(Fq), the SNC spectral sequence and arithmetic Hochschild–Serre give dim H4(X,Q_l(1))=4.',
 'X is proper but singular. This does not refute the analogous proper smooth weight argument. The earlier run supplied the example; all strata, differential ranks and Frobenius weights are recomputed here.',
 'agrees','The note labels the example as its own and checks the missing smoothness hypothesis.',middle=[45])
add(88,[],'unproved claim',[86,87],'Pro middle731–794; K12-05 329–379','symétriques ... alternées; un cône convexe fermé',
 'Positive forms on pure weightρ objects take values in Q(-ρ), with symmetry sign(-1)^ρ. The proposed cones, products and duality are axioms in a category already assumed semisimple.',
 'Closedness, interior and convexity require real scalar extension of the finite-dimensional space of forms. Invariance of a real form alone does not make it positive.',
 'agrees','The notes preserve parity, topology and the logical direction of the assumptions.',middle=[46,47])
add(89,[],'reading question',[86,87],'Pro middle736,756–768; K12-05 334,351–364','B(M′,M′′) ... Q(ρ)',
 'The cross-term target Q(ρ) conflicts with the defining pairing target Q(-ρ). Tensor weight2ρ requires Q(-ρ) in the adopted convention.',
 'Both supplied transcriptions retain the opposite-sign target, so a mathematical alarm does not establish which symbol is in the ink.',
 'agrees','The earlier correction is justified as a proposal only.',middle=[48])
add(90,[],'unpursued implication',[87,88],'Pro middle794–798; K12-05 376–382','N=M⊕M^⊥',
 'If the restriction of a positive nondegenerate form to every subobject remains nondegenerate, each subobject splits orthogonally. This is a conditional semisimplicity mechanism.',
 'It neither constructs the motive category nor proves the positivity conjecture that would provide the forms. The page had already assumed semisimplicity.',
 'agrees','The note keeps this implication separate from the premise of the section.',middle=[49])
add(91,[],'idea of the earlier run',[88],'Pro middle807–810; K12-05 388–391','Si ρ=0, de sorte que ... un vectoriel',
 'A general pure weight-zero motive need not belong to the trivial vector-space subcategory. For an elliptic curve E/C, h1(E)^∨⊗h1(E) has weight zero and nonzero Hodge types(1,−1),(−1,1).',
 'A trivial/Artin or effective level-zero restriction could support a narrower statement. Weight zero alone does not.',
 'agrees','The earlier run’s counterexample is verified with its Hodge numbers and the distinction from effective level zero retained.',middle=[50])
add(92,[],'unpursued implication',[89],'Pro middle821–849; K12-05 400–427','composantes isotypiques; corps gauche',
 'Nonempty positive cones on simple objects provide the twisted self-duality needed for isotypic orthogonality. Schur’s lemma then reduces forms to Hermitian linear algebra over the simple object’s division endomorphism algebra.',
 'The division algebra need not be commutative. Product decomposition of cones uses these self-duality and orthogonality hypotheses, not semisimplicity by itself.',
 'agrees','The note correctly repairs an overly broad modern interpretation while retaining what the cone axioms can supply.',middle=[51])
add(93,[],'reading question',[90],'Pro middle861–890; K12-06 early lines','Soit k un ... anneau; longueur finie; proj.',
 'The category of finite-dimensional endomorphisms over a field admits the stated simple-object description. Replacing the field by a ring requires a choice of exact category, typically endomorphisms of finite projective modules, not all finite-length modules.',
 'Over Z, the projective module Z has infinite length, while Z/p has finite length and is not projective. The monoid of endomorphisms and the group of automorphisms also have different zero-eigenvalue behavior.',
 'agrees','The note catches a change of category, not merely a notational substitution.',middle=[52])
add(94,[],'unproved claim',[91],'Pro middle897–922; K12-06 endomorphism section','Lorsque k est un corps ... injectif',
 'The determinant series L(V,u)=det(1−tu)^−1 is not injective on K0 of all finite-dimensional endomorphisms over a field: [(k,0)] has nonzero rank but L=1. Its kernel is exactly the integer span of this zero-eigenvalue simple class.',
 'After quotienting by this class, or restricting to automorphisms, factorization into irreducible reciprocal polynomials gives injectivity. This repair is distinct from the trace-ghost issue in characteristic p.',
 'agrees','The earlier run identified the nilpotent kernel; the exact kernel and counterexample are proved here.',middle=[53])
add(95,[],'reading question',[91],'Pro middle903–941; K12-06 endomorphism section','φ(t)↦1/φ(t); L=∏Q^{c_P}',
 'With λ_t from exterior powers, the symmetric-power series is σ_t=1/λ_{−t}. For the adopted reciprocal determinant convention, simple reciprocal factors occur with negative multiplicities. The logarithmic derivative records power traces.',
 'The missing minus sign and reciprocal exponent are independent transcription alarms. One can choose a different λ convention, but it must be stated consistently.',
 'agrees','The note correctly tests the formulas on a one-dimensional scalar operator.',middle=[54])
add(96,[],'unpursued implication',[92],'Pro middle945–948; K12-06 endomorphism section','n’est ... pas injectif',
 'In characteristic p, ghost traces do not determine the determinant series even for invertible operators: p copies of the identity have L=(1−t^p)^−1≠1 but every power trace is zero.',
 'The class has rank p in the integer-valued Grothendieck group. Reduction of traces modulo p, not nilpotence, loses the information.',
 'agrees','The page states the failure; the explicit calculation is credited to the earlier run and redone here.',middle=[55])
add(97,[],'reading question',[92,93],'Pro middle952–981; K12-06 L-functions section','l’opération du Frobénius dedans; h^i=H^{i−ρ}_!',
 'A determinant series recovers a virtual semisimplified Frobenius class, not Jordan blocks. For pure coefficient weightρ on a proper smooth variety, regrouping by weight i instead of cohomological degree i−ρ changes the Euler sign by(-1)^ρ.',
 'Identity2 and a nontrivial unipotent Jordan block have the same determinant series and power traces. Semisimplicity is a separate hypothesis. The parity correction is forced by the written indexing.',
 'agrees','The notes correctly separate K0 information, actual Frobenius structure, and the sign convention.',middle=[56,57])
add(98,[],'unproved claim',[93,94],'Pro middle999–1039; K12-06 L-functions section','poids≤2n−2+ρ; l’Albanèse',
 'For smooth proper n-folds with the stated pure coefficient setting, quotienting the virtual Frobenius invariant by weights≤2n−2+ρ makes it insensitive to lower-dimensional modifications in the indicated range. For constant coefficients, the two surviving top pieces encode geometric components and the Albanese up to isogeny.',
 'Tate’s theorem for abelian varieties over finite fields supplies the Albanese isogeny conclusion. The cutoffρ must be retained for general coefficients, and this coarse invariant does not reconstruct the variety.',
 'agrees','The notes preserve the limited top-degree content and the conditional general-coefficient setting.',middle=[58,59])
add(99,[],'self-flagged step',[93,95],'Pro middle983–997,1044–1061; K12-06 final middle section','Dans quelle mesure faut-il faire les hypothèses ... ??',
 'A relative L-function programme seeks invariants of a generic fibre modulo factors supported over proper closed subsets of the base, and asks which smoothness/properness assumptions are necessary.',
 'A cancelled first draft and the later surviving question are distinct. Pro and Codex differ in the exact final adjective list. No single established relative invariant with precisely these quotient rules is identified by the bounded literature search.',
 'agrees','The final question is not answered by general rationality or trace formula theorems.',middle=[60])
add(100,[],'other',[52,58,77,79,82,93,95],'Pro middle37–55,192–223,583–617,645–673,983–1061','bijective; surj. à noyau fini',
 'Visible deletions, surviving contradictory drafts, uncertain readings and genuine questions have different documentary status. The scan77/79 finite-kernel revision is explicit; the scan78/82 degree-two conflict is not visibly withdrawn.',
 'This is editorial classification, not an additional mathematical claim. It prevents a contradiction from being labelled as the author’s correction without evidence.',
 'agrees','Both metadata notes are supported by the retained deletion markup and the parallel witnesses.')
items[-1]['sources']=[f'{MP}#77',f'{MP}#78']

if __name__=='__main__':
    (P/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    covered={x for y in items for x in y['subnotes'] if x.startswith(MP)}
    print(json.dumps({'items':len(items),'middle_subnotes':len(covered),'source_entries':len({x for y in items for x in y['sources']})}))
