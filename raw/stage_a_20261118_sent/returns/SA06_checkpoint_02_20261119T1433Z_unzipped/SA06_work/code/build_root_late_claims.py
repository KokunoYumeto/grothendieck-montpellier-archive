#!/usr/bin/env python3
"""Individually authored claims on the late realisation and reused leaves."""
import build_root_claims as b
claim=b.claim
fibre=b.fibre+'; root_search_014/015/023, GrothHodge1969 and BostCharles2016'
lie='root_search_006/023/024; Humphreys1990, Humphreys1972, BourbakiLie1975; the exact editorial draft number is not inferred from the printed theorem'

claim(800,[802],
 'The agenda proposes a relation between odd motives and abelian varieties, without specifying a universal quantifier or the required Tate twist and Hodge level.',
 'open on the pages','F',
 'A precise theorem cannot be identified from this heading. Polarizable rational Hodge structures of weight1 are realized by abelian varieties; for higher odd cohomology the level1/coniveau question is the corrected generalized Hodge conjecture. Grothendieck1969 §2 states this connection explicitly, but does not prove that every odd motive is an abelian h1 with a twist.',
 ['GrothHodge1969','DeligneMilne1982'],fibre,confidence='medium')
claim(801,[803],
 'The agenda asks for positivity under blowups, induction and Lefschetz pencils, without an explicit bilinear form or a complete stability statement.',
 'open on the pages','F',
 'These are identifiable methods in the standard-conjecture programme, but this line does not determine one theorem. The published standard conjectures and the abelian-scheme Lefschetz construction give precise comparison statements; neither permits an unqualified positivity theorem for all blowups or all cycle equivalence relations.',
 ['GrothHodge1969','Kunnemann1993'],fibre,confidence='medium')
claim(802,[804],
 'The agenda proposes compatible integral lattices for the different realisations and a theory recovering rational structures from them.',
 'open on the pages','C',
 'Finite-rank integral Betti realisations and rational comparison torsors are established in their geometric settings. The full mixed integral motivic fibre-functor programme, with all integral and filtered comparisons demanded by the later pages, is stronger than the rational Nori reconstruction theorem. The agenda contains no exact general existence theorem to mark solved.',
 ['HuberMuellerStach2017','ChoudhuryGallauer2017','GrothDeRham1966','BostCharles2016'],fibre,confidence='medium')
claim(803,[805,806],
 'The headings on class field theory, L-functions, topology over SpecZ, Riemann-hypothesis methods and the doubtful extension noun specify research subjects, not complete mathematical assertions.',
 'open on the pages','F',
 'The class-field/CM search finds exact Serre-group constructions, and the realization search finds precise comparison theorems, but no unique theorem is recoverable from these headings alone. The unreadable noun is retained as a scan question; no Ext or motivic-homotopy statement is supplied as his words.',
 ['MilneCM1981','MilneGerbes2003','GrothDeRham1966'],fibre,confidence='low')
claim(804,[807],
 'For a quasi-compact quasi-separated schemeX and a point inclusioni:Specκ(x)→X, the positive-degree direct images of an étale abelian sheaf from the point, and Hq(X,i_*F), are torsion in the stated range.',
 'corrected by himself later on the same scan: a deleted Leray route is replaced by the live rational-function/divisor sequence','A',
 'Grothendieck, BrauerII, Lemma1.1 and Corollary1.2, pp290–291, give the exact generic-point and rational-function-unit torsion results. The manuscript deletion is recorded; the deleted argument is not counted as an extant proof.',
 ['GrothBrauerII1966'],fibre,words='the deleted Leray paragraph at15/179, followed by the surviving divisor sequence',
 proof='For the residue-field étale site, positive Galois cohomology is torsion: a continuous cocycle is represented on a finite quotient after passage to a suitable open subgroup. The direct-image stalks satisfy the same assertion; the Leray spectral sequence then compares Hq(X,i_*F) with the field cohomology modulo torsion, under the hypotheses of Lemma1.1. The statement for a finite collection of generic points follows by the finite product decomposition of rational-function units.')
claim(805,[807],
 'For X noetherian without embedded associated primes, the exact étale sheaf sequence0→Gm→R_X^*→Div_X→0 induces Hi(X,Div_X)→Hi+1(X,Gm) as an isomorphism modulo torsion fori≥1.',
 'proof sketched','A',
 'This is exactly BrauerII, Corollary1.3, p291, with the generic-point torsion assertion from Corollary1.2. The source also permits a reduced qcqs scheme with finitely many irreducible components. No torsion-free or integral isomorphism is asserted.',
 ['GrothBrauerII1966'],fibre,
 proof='In the long exact sequence, the kernel of the connecting map is the image of Hi(X,R_X^*) and its cokernel embeds in Hi+1(X,R_X^*). Both groups are torsion fori≥1 by the generic-point lemma. Thus the connecting morphism becomes an isomorphism after tensoring withQ; neither adjacent group is asserted zero integrally.')
claim(806,[808],
 'The strictly henselian factorial paragraph onscan179 ends after a colon, so the intended following assertion is absent from the supplied text.',
 'open on the pages','F',
 'BrauerII Proposition1.4, p291, proves Hq(X,Gm) torsion forq≥2 whenX is the spectrum of a strictly henselian noetherian factorial local ring. This is an exact contextual continuation candidate, not words supplied to the missing manuscript clause.',
 ['GrothBrauerII1966'],fibre,confidence='medium')
claim(807,[809],
 'For a suitably polarizable pure Tate category with even degrees, a real fibre functor can be chosen; the page then works relative to such a choice. Passing to the even part is proposed for certain distribution questions only.',
 'stated without proof; its domain is explicitly narrowed by the insertion onscan183','C',
 'The real Tate-triple/polarization formalism supplies precise neutrality criteria (Deligne–Milne §5). The page has not specified all of those axioms for its integral category overS, so existence for that entire category is conditional. Its correction from most to certain distribution questions must be respected.',
 ['DeligneMilne1982','MilneGerbes2003'],fibre,confidence='medium')
claim(808,[811],
 'After fixing a real fibre functor and its Artin/Tate identifications, the comparison fibre functor attached to(s,i) determines an Isom tensor torsor inH1(R,G00), whereG00=ker(ε:G0→Gm).',
 'stated without proof','B',
 'The Tannakian Isom-torsor construction is established (Deligne–Milne Proposition2.8 and Theorem3.2). Reduction of its structure group toG00 requires the stated connected/Artin and Tate identifications; it is not automatic for two arbitrary fibre functors.',
 ['DeligneMilne1982'],fibre,
 proof='For two tensor fibre functorsω,η, Isom⊗(ω,η) is a torsor underAut⊗ω. Requiring the chosen isomorphism to be the fixed one on the Artin quotient and the Tate object cuts the structure group to the intersection of their stabilizers, namelyker(ε|G0). Descent of this torsor classifies the relative fibre functor. This proves the classification after, not before, specifying those identifications.')
claim(809,[811],
 'The homomorphism attached to a fibre over a closed point takes values in the inner formG^ξ of the chosen real group and is defined up to the statedG00(R)-conjugacy.',
 'stated without proof','B',
 'Tannakian functoriality and torsor twisting establish the construction after the relative fibre functors and their comparison torsor are supplied. Conjugating a choice of comparison changes the displayed homomorphism without changing its intrinsic morphism between tensor automorphism groups.',
 ['DeligneMilne1982'],fibre,
 proof='Transport Aut⊗η along the Isom torsorP by the conjugation action ofG to obtainP×^G G=G^ξ. A tensor functor induces the corresponding map of automorphism groups. Two trivializations ofP differ by an element of its structure group, so the concrete homomorphisms are conjugate. Restricting to comparisons preserving Artin and Tate data givesG00-conjugacy.')
claim(810,[812],
 'For a complex algebraic torusT of rankr, Hom(μ2,T) has2^r elements. The unqualified literal set of such homomorphisms into a noncommutative real group need not be finite.',
 'open on the pages: fini, if commutative at least, followed by a question mark','C',
 'The finite torus statement is proved by the character lattice. Literal homomorphisms inGL2 already form an infinite conjugacy orbit of involutions; this does not refute finiteness of conjugacy classes or finiteness of admissible polarization classes. Those are separate assertions, and the source deletes the words classes de.',
 ['MilneAG2015','DeligneMilne1982'],fibre,comp=['torus_mu2','involutions_GL2'],
 proof='The restriction map identifies Hom(μ2,T) withHom(X*(T),Z/2)≅(Z/2)^r. InGL2, A_t=[[1,−2t],[0,−1]] squares toI for every realt, and distinctt give distinct homomorphismsμ2→GL2, all conjugate todiag(1,−1). Only the literal-homomorphism reading is refuted by this example.')
claim(811,[810,813],
 'A cocharacter’s restriction toμ2 determines its class modulo2, but does not determine its oriented ray inX_*(T)⊗R or the effectivity cone generated by such rays.',
 'stated without proof through the passage fromv(s′) to rays onscan187','C',
 'The character-lattice calculation exposes a missing datum:μ and−μ have the same restriction toμ2 and opposite rays. A correct cone construction must retain the full preferred cocharactersi(s′), including their orientation and normalization. It cannot be read solely from the displayed involutionsv(s′).',
 ['MilneAG2015','GrothHodge1969'],fibre,comp=['torus_mu2'],
 proof='ForT=Gm the cocharactersn↦(z↦z^n) restrict toμ2 according tonmod2. The cocharacters1and−1 agree there, but span the positive and negative rays inR. Their associated inequalities on a character have opposite signs. No rule using only the common restriction can recover both.')
claim(812,[813],
 'Frobenius eigenvalues are algebraic integers on effective geometric objects; the words in every representation cannot hold on an unrestricted rigid category containing Tate objects and their duals.',
 'false as stated if every representation includes the rigid Tate category','C',
 'ForGm and a Frobenius elementq>1, the standard character has eigenvalueq but its dual hasq^−1, which is not an algebraic integer. The refined assertion restricts to an effective subcategory/monoid. Recovering that subcategory from all Frobenius conditions remains a stronger conjectural assertion.',
 ['GrothHodge1969','DeligneMilne1982','HuberMuellerStach2017'],fibre,comp=['effectivity_dual_test'],
 proof='A rational number is an algebraic integer iff it is an integer. For an integerq>1, q^−1 is not integral. In a rigid tensor category a one-dimensional representation with eigenvalueq has a dual with eigenvalueq^−1. Thus integrality for every object forces the relevant eigenvalues to be units, while effective Tate objects already violate that stronger requirement.')
claim(813,[814],
 'The distribution heading and the polarization/twisting restrictions do not yet define a measure, ordering of closed points or equidistribution theorem.',
 'open on the pages','F',
 'The supplied text identifies a distribution programme but no quantified analytic assertion. Modern motivic-group and period results do not supply the missing measure and averaging procedure. The earlier run’s Sato–Tate comparison is preserved as its research lead, not an author theorem.',
 ['MilneGerbes2003','DeligneMilne1982'],fibre,confidence='high')
claim(814,[816,824],
 'The existence obstruction for a banded motivic gerbe belongs in degree2; after a fibre functor is fixed, comparison objects are classified by degree1 torsors, with degree0 automorphisms.',
 'stated without proof; H2|H1 is explicitly doubtful in the transcription','B',
 'The gerbe/torsor distinction is established in Tannakian theory. It supplies a mathematical reading alarm, not a decision between the uncertain superscripts onscans191and193. The real quaternion example shows that having local realisations need not give a rational fibre functor.',
 ['DeligneMilne1982','MilneGerbes2003','SGA4XVIII1973'],fibre,
 proof='A neutralization of a gerbe is an object, whose obstruction is the gerbe class. Once an objectω exists, the sheafIsom(ω,η) is a torsor; its class measures comparison withη. Its automorphisms formAutω. These are categorically different degrees, so moving from existence to comparison changes the cohomology group.')
claim(815,[817,900],
 'The asserted ℓ-adic or Witt realisation may descend to a henselian or strictly henselian coefficient ring, but the margin says probably and does not specify an integral model proving the descent.',
 'open on the pages','C',
 'Smooth points lift over henselian local rings under the Stacks hypotheses, and finite-type torsors can then be compared. These results do not manufacture an integral motivic model, nor descend arbitrary p-adic comparison data to the unnamed henselisation. The exact all-motive assertion remains unmatched in this bounded search.',
 ['StacksSmoothLift','StacksHenselian','Lang1956','Oda1969'],fibre,confidence='medium')
claim(816,[818,900],
 'For an abelian variety over a perfect field of characteristicp, its degree-one de Rham cohomology identifies with the Dieudonné module of its p-kernel, with Hodge subspaceVM=kerF; the manuscript’s broader diagram asks for a derived filtered replacement.',
 'open on the pages for the general diagram; stated extra F,V structure','B',
 'Oda Corollary5.11, p131, proves precisely the degree-one p-kernel/de Rham comparison, including the Hodge exact sequence. His introduction dates the underlying dissertation toJune1967; publication1969. It does not establish a rigid integral tensor fibre functor on all motives with the same degree-oneF,V relation.',
 ['Oda1969','GrothDeRham1966'],fibre,
 proof='The cited Oda corollary is read together with its exact sequence: M(X[p])→H1_dR(X) carriesVM=kerF toH0(X,Ω1), and the quotient toH1(X,O_X). This checks the actual claimed range, perfectness and degree. The filtration and its extension class are additional data, so a bare vector space is insufficient for the later manuscript programme.')
claim(817,[818],
 'If two modules haveFV=p, their unmodified tensor-product operators satisfy(F⊗F)(V⊗V)=p², notp. General cohomological degree requires weight-dependent normalizations or an isocrystal/filtered-derived formulation.',
 'false as stated if the boxed relation is imposed unchanged on all tensor products','C',
 'The degree-one relation is correct in Dieudonné theory. The exact tensor calculation refutes its unrestricted extension; the page itself warns that the de Rham–Hodge realisation should be derived and filtered.',
 ['Oda1969','GrothDeRham1966'],fibre,comp=['slope_half_rank2'],
 proof='Using the usual semilinear tensor operators over the common base, composition is componentwise: (F_M⊗F_N)(V_M⊗V_N)=(F_MV_M)⊗(F_NV_N)=p²id. The semilinearity cancels in eachFV and does not remove the extra factorp. A Tate/weight correction is genuinely extra structure.')
claim(818,[819],
 'LetR be henselian local with finite residue fieldk, andG/R a smooth affine group scheme of finite type with connected special fibre. Then everyG-torsor overR is trivial; its points are not canonically chosen.',
 'open on the pages: sans doute, th. de Lang','C',
 'Lang1956 proves H1(k,Gk)=1 for connected algebraic groups. Smooth lifting and henselian retractions prove the refined integral statement. The manuscript has not established these hypotheses for its pro-motivic band or all integral models, so its blanket uniqueness inference is not a theorem of Lang alone.',
 ['Lang1956','MilneAG2015','StacksSmoothLift','StacksHenselian'],fibre,
 proof='A torsorP under smoothG is smooth overR. Lang givesPk(k)≠∅ becauseGk is connected. A k-point of a smoothR-scheme lifts after an étale neighbourhood preservingk; henselianity retracts that neighbourhood, henceP(R)≠∅. Choosing a point trivializesP. Different points differ byG(R), which explains uniqueness up to isomorphism rather than a unique isomorphism.')
claim(819,[820],
 'The proposed extension from finite fields to perfect fields of dim ch1 is explicitly tentative and its dimension convention is uncertain.',
 'open on the pages','F',
 'The finite-field Lang theorem and the smooth henselian lifting argument do not identify this assertion for all perfect fields of a suggested cohomological dimension. The prime, cohomology theory, connectedness, integral ring and torsor band must first be specified. No general theorem is attributed to the doubtful phrase.',
 ['Lang1956','StacksHenselian','MilneGerbes2003'],fibre,confidence='low')
claim(820,[821],
 'A compatible inverse system of motivic comparison groupoids might have only one isomorphism class even when individual levels have several.',
 'open on the pages','C',
 'This is an inverse-limit existence/uniqueness question; neither Lang nor ordinary Tannakian reconstruction proves it. The page supplies no hypotheses eliminating incompatibility or derived-limit obstructions. The constant system with a fixed nontrivialH1 already shows that inverse limits do not automatically force uniqueness, but is not claimed as a counterexample to the unspecified motivic system.',
 ['DeligneMilne1982','MilneGerbes2003'],fibre,confidence='medium',
 proof='IfTα=T and all transition maps are identities, the inverse limit isT. Hence any nontrivial torsor-class set remains nontrivial. An argument for the author’s particular system must therefore use properties of its transition functors beyond the existence of an inverse system.')
claim(821,[822],
 'On a connected locally noetherian scheme, changing a geometric basepoint gives isomorphic ℓ-adic fibre functors noncanonically; choices form a path torsor, and the fundamental group acts on a chosen fibre.',
 'stated without proof, with non uniq. emphasized','E',
 'This is the standard fibre-functor formalism of the étale fundamental group. The small/big étale-site comparison does not turn these paths into a canonical choice. The source’s explicit nonuniqueness is retained.',
 ['SGA1V1971','DeligneMilne1982'],fibre+'; root_search_031; SGA1 V Corollary5.7 and §7, reedition pp107,115–116',
 proof='For locally constant finite sheaves, a geometric point defines an exact fibre functor. Tensor/natural isomorphisms between two such functors form a torsor under the automorphism group of either; its points are étale paths. Passing to compatible finite quotients gives the profinite group and toℓ-adic systems its continuous actions. Connectedness is needed to compare the basepoints.')
claim(822,[823,901],
 'Perfect-field-valued points over different underlying points need not give canonically isomorphic p-adic realisations. For two embeddings of the same residue field into an algebraically closedk, an automorphism ofk conjugates the scalar-extended objects; stabilizing automorphisms act semilinearly.',
 'stated without proof; the absence of general isomorphisms is expressed as a doubt','B',
 'Scalar extension and the extension theorem for embeddings establish the conjugacy assertion for the same residue field and compatible functorial realisations. Automorphisms not fixing the embedding can change the point. This does not preclude monodromy theories for families ofF-isocrystals; it says the specific fibre in this model has not been given the sameπ1 action as its étale counterpart.',
 ['Oda1969','GrothDeRham1966'],fibre,
 proof='Given two embeddingsL→k withk algebraically closed, their induced isomorphism of the subfields extends to an isomorphism of algebraic closures, and then over corresponding transcendence bases to an automorphism ofk. Functorial scalar extension transports the realisation by that automorphism; Witt vectors are functorial. FixingL produces semilinear descent operators on a fixed point. These statements do not compare distinct residue fields or provide a linear canonical isomorphism.')
claim(823,[901],
 'Two rational fibre functors on the same Tannakian category become objects whose isomorphisms are measured byH1, whereas the obstruction to any rational fibre functor is a gerbeH2 class; the scan197 phraseH2 for each rational point is ambiguous.',
 'stated without proof; degree is not resolved by the text','B',
 'The categorical degree distinction is settled, but the intended datum onscan197 is not identified sufficiently to change the superscript. Both theQℓ-object and its integral extension problem must be specified before giving anH1 classification.',
 ['DeligneMilne1982','MilneGerbes2003'],fibre,confidence='medium')
claim(824,[902],
 'For smooth proper geometric realisations in characteristic0 and a complex embedding, Betti cohomology supplies an integral lattice and the usual complex de Rham andℓ-adic comparison maps, after the appropriate torsion or derived conventions.',
 'stated without proof','B',
 'Grothendieck1966 proves algebraic de Rham comparison overC. The rational motivic formalism packages compatible Betti and de Rham fibre functors and their torsor. Integral cohomology can have torsion and is not automatically a finite free lattice on every object; the broader integral category of the pages requires that restriction or a derived formulation.',
 ['GrothDeRham1966','SGA4XVI1973','BostCharles2016','HuberMuellerStach2017'],fibre+'; root_search_032–034; SGA4 XVI Theorem4.1',
 proof='A finite CW model for a smooth proper complex variety gives finitely generated integral cohomology; quotienting its torsion gives a lattice in rational cohomology. Tensoring withC and the algebraic de Rham comparison gives the second realization. Compatibility on tensor constructions is part of the geometric comparison formalism; it does not by itself construct an abelian category of all integral motives.')
claim(825,[902,903],
 'Complex conjugation identifies the Betti lattices of conjugate complex points; for a real point it induces a linear involution on the Betti lattice, distinct from coefficientwise semilinear conjugation on de Rham realisation.',
 'stated without proof','B',
 'The topological conjugation map and real de Rham comparison give these involutions. The source correctly distinguishes an action attached to the real place from an asserted action of the whole arithmetic fundamental group on one Betti lattice.',
 ['GrothDeRham1966','BostCharles2016','DeligneMilne1982'],fibre,
 proof='Conjugating complex points is a homeomorphism of the associated analytic spaces, hence gives an integral cohomology isomorphism whose square isidentity. At a real point it is an endomorphism. Coefficient conjugation is conjugate-linear on complex vector spaces and fixes a chosen real form; these two operations have different scalar linearity and cannot be identified before using the comparison map.')
claim(826,[904],
 'Under the real equivariant de Rham–Betti comparison, the two conjugate-linear involutionscB,c_dR commute and their product is the complex-linear real Frobeniusf∞; its action agrees with complex conjugation in theℓ-adic realisation.',
 'open on the pages: both products and the final Frobenius comparison marked à vérifier','B',
 'The comparison formalism verifies the identity in its geometric domain. The Tate object supplies a sign check: onQ(1), the Betti generator2πi has real Frobenius−1. None of this constructs an action of allπ1 on the integral Betti fibre.',
 ['GrothDeRham1966','BostCharles2016','DeligneMilne1982'],fibre,comp=['real_comparison_involutions'],
 proof='Transport coefficient conjugation on the real de Rham form to the Betti complexification. Real equivariance statesc_dR=f∞cB. Sincef∞ preserves the Betti real lattice, it commutes withcB and has square1. ThuscBc_dR=c_dRcB=f∞. The same geometric conjugation acts on finite étale comparisons, yielding itsℓ-adic action. These equalities use real equivariance, not just the existence of two arbitrary real forms.')
claim(827,[905],
 'The motivic/coniveau level is predicted by Hodge position; the literal rational intersection of Hodge subspaces must be replaced, in general, by its largest rational sub-Hodge structure.',
 'open on the pages as a conjecture; false as stated for the literal rational-intersection equality, corrected in the author’s later publication','A',
 'Grothendieck1969 §§1–2, pp299–301, explicitly refutes the naive general filtration formula and gives the corrected largest-sub-Hodge-structure formulation. He also explains its equivalence, in the motivic yoga, to Hodge effectivity detecting motivic effectivity. This is a correction of the generalized formulation, not a disproof of the usual rational Hodge conjecture. The source date isreceived27October1968, publication1969.',
 ['GrothHodge1969'],fibre,
 proof='Takeτ to be the upper-half-plane root ofT³−2 andE=C/(Z+τZ). In V=H1(E,Q)⊗3⊂H3(E³,Q), the map toH^{0,3} has coefficients1,τ,τ²,τ³ andQ-rank3. Its rational kernelK has dimension8−3=5. For a rational vector vanishing of its(0,3)-part forces vanishing of its conjugate(3,0)-part; hence this is the naive rational level1 intersection. A rational Hodge structure of odd weight has even dimension, because its H^{p,q} summands pair withH^{q,p}. ThereforeK is not a sub-Hodge structure. For the real base use the smooth projective abelian varietyX=Res_C/R(E³), of dimension6. InsideH3(X_C,Q), W=V⊕Vbar is an f∞-stable rational Hodge direct summand, and the naive intersection onW isK⊕Kbar. Its dimension10 is not itself a parity contradiction. If the full naive intersection were a sub-Hodge structure, its intersection withW and then its rational Hodge projection toV would makeK a sub-Hodge structure, contradiction. Thus the maximal sub-Hodge structure is the correct necessary target. This exact restriction-and-projection step was independently checked by cote15_middle; the rational rank certificate is parts/cote15_middle/audit/peer_review_C827.json.')
claim(828,[831],
 'For an effective Cartier divisorD∼E, the sequence0→O_V((n−1)E)→O_V(nE)→O_D(nE)→0 is exact; stabilization ofh1 and the indicated vanishing onD imply surjectivity of restriction of sections and then base-point-freeness as used on the reused folios.',
 'proof sketched across folios70,72,73 and the separately supplied folio74; folio71 is not supplied','E',
 'The sheaf exact sequence and long-exact-sequence argument are valid under their Cartier and vanishing hypotheses. Equality of dimensions alone is not sufficient: one also uses surjectivity of theH1 map, from the adjacent vanishing. The missing folio prevents certification of a continuous proof of the entire projectivity criterion or exact provenance.',
 ['SerreFAC1955'],fibre+'; root_search_028–029; FAC §47 Theorem5 Corollary2 and §66 Theorem2',
 proof='Tensor0→O(−D)→O→O_D→0 by the invertible sheafO(nE). IfH1(D,O_D(nE))=0, the inducedH1(O((n−1)E))→H1(O(nE)) is surjective. Equality of their finite dimensions makes it an isomorphism, forcing the preceding connecting map fromH0(D,O_D(nE)) to vanish. Hence restrictionH0(V,O(nE))→H0(D,O_D(nE)) is surjective. A section definingD hasnth power nonzero offD; lifted generating sections onD eliminate the remaining basepoints.')
claim(829,[832],
 'TheE6 andE7 root-lattice quotients and Weyl actions in the exercise sheet yield the finite orthogonal/symplectic groups, with the manuscript’s determinant-one and spinor-kernel conventions distinguished.',
 'stated as exercise instructions, with outlined constructions','E',
 'The computations verify detCartanE6=3 anddetCartanE7=2, quotient dimensions5overF3and6overF2, and the group orders. Humphreys1990 §2.12 gives the exact classical identifications: |W(E6)|=51840, the simple spinor/derived subgroup hasorder25920, andW(E7)≅C2×Sp6(F2) withorders2903040 and1451520. Equality of orders alone is not used as proof of the isomorphisms.',
 ['Humphreys1990'],lie,comp=['exceptional_root_lattices'])
claim(830,[825,906],
 'For a split semisimple Lie algebra in characteristic0, the root-space decomposition has one-dimensional root spaces, sl2 root triples and the usual opposite-root/Killing pairings; a subalgebra containing the split Cartan is determined by a closed set of roots.',
 'stated as editorial additions and corrections in reused Lie-algebra leaves','E',
 'The precise root-space assertions are classical; Humphreys §8, pp35–40, was read for the root-space and Killing-pairing statements. Bourbaki VIII§§1–3 was located in the publisher contents only, not used as a checked proof. A symmetric closed root subset yields a reductive regular subalgebra. Calling an abstract subalgebra reductive without specifying its embedding or toral action is stronger than this criterion; the source’s ambient context is essential.',
 ['Humphreys1972','BourbakiLie1975'],lie,
 proof='Ifh acts diagonally, a subalgebra containingh decomposes intoh-weight spaces, hence chooses root spacesgα. Closure under brackets forcesα+β whenever it is a root and[gα,gβ]≠0. In characteristic0 that bracket is nonzero in the root-string range. Stability underα↦−α supplies the opposite root triples and a reductive derived part. The Killing pairing has B(gα,gβ)=0unlessα+β=0, byh-invariance.')
claim(831,[825],
 'For the standard positive nilpotent subalgebran+ of a characteristic0 semisimple Lie algebra, its Killing orthogonal isn+⊕h=b+, not the opposite Borelb−.',
 'corrected by himself later on the same line: the opposite-Borel expression is struck out','E',
 'The surviving root/Killing calculation and the explicitsl2 matrix check give the corrected identity. The struck-out false expression is not retained as an author assertion. The earlier notes chiefly treated this as editorial material; the exact sign error is recorded in the reading table.',
 ['Humphreys1972','BourbakiLie1975'],lie,comp=['sl2_orthogonals'],
 proof='The Killing form pairsgα perfectly withg−α, andh orthogonally to every root space. Orthogonality to all positive root spaces excludes precisely the negative root components, leavingh⊕n+=b+. Forsl2, B(e,f)=4,B(h,h)=8, soeperp=span(e,h).')
claim(832,[907],
 'In characteristic0 the finite-dimensional simplesl2 module of highest weightm≥0 has divided-power basisv_n=f^n v_0/n!, weightsm−2n, and the usual recurrence; finite-dimensional modules are completely reducible.',
 'stated as editorial corrections, including insertion of finite-dimensional hypotheses','E',
 'Humphreys §6.3 p28 and §7.2 pp32–33 give the complete-reducibility statement and divided-power recurrence; these passages were read. Bourbaki VIII§1 was located in its contents, without access to its theorem text. The finite-dimensional and characteristic0 qualifications are indispensable. The draft’s requests for a canonical normalization and binomial operators are more precise than merely listing all weights.',
 ['Humphreys1972','BourbakiLie1975'],lie,
 proof='From[h,e]=2e,[h,f]=−2f,[e,f]=h, induction givese f^n v_0=n(m−n+1)f^{n−1}v_0. Division byn! yieldse v_n=(m−n+1)v_{n−1}, f v_n=(n+1)v_{n+1}, h v_n=(m−2n)v_n. If the string terminates atq, applying e to f^{q+1}v_0 forcesm=q in characteristic0. The basis is linearly independent because its weights are distinct. Complete reducibility is the separate characteristic0 theorem, not a consequence of this string calculation alone.')
claim(833,[908,909],
 'The reused editorial text invokes existence and conjugacy of Cartan subalgebras, regular-element/Fitting-nullspace criteria and passage through intermediate subalgebras, with hypotheses inherited from a missing draft.',
 'stated without complete surrounding hypotheses in the supplied editorial excerpt','C',
 'Humphreys §15.3 p80 gives Cartan existence over an algebraically closed field; §§16.2–16.4 pp82–85 state the characteristic0 conjugacy results. These statements and their hypotheses were read, but the complete conjugacy proof continues beyond the selected excerpt. Bourbaki VII§§2–3 was checked only at contents level. Some characteristic-p conclusions are explicitly deleted in the source. The unrestricted draft-relative assertions, including scalar restriction over arbitrary fields, cannot be certified without the missing hypotheses; they are indexed separately as provenance/reading questions rather than exported as universal motivic facts.',
 ['Humphreys1972','BourbakiLie1975'],lie,confidence='medium')
claim(834,[909],
 'In characteristic2, sl2 is nilpotent, so the characteristic0 regularity example cannot be retained verbatim.',
 'stated with an explicit warning onscan202','E',
 'The displayed characteristic2 warning is correct. In the basisI,e,f one has[e,f]=I central, so the lower central series hasdimensions3,1,0. It is a mathematical correction of the reused Lie text, unrelated to semisimplicity of motivic categories.',
 ['BourbakiLie1975','Humphreys1972'],lie,comp=['sl2_char2'])
claim(835,[910],
 'An equivariant bilinear map sends simultaneous generalized weight spaces to weightλ+μ for Lie actions and to weightλμ for multiplicative actions, under the stated intertwining identity.',
 'stated with a proposed editorial formula onscan204','E',
 'Humphreys §15.1, pp78–79, proves the generalized-weight bracket formula, with its binomial expansion. The same proof gives the stated equivariant bilinear variant below. The Bourbaki contents place the corresponding subject inVII§1, but that book’s full theorem text was not accessed in this run. For generalized weights the nilpotent orders must be combined; plain eigenvector substitution only proves the nongeneralized special case.',
 ['Humphreys1972','BourbakiLie1975'],lie,
 proof='For an additive actionD, the defectD_W−(λ+μ) onB(v,w) equalsB((D_V−λ)v,w)+B(v,(D_{V′}−μ)w). These two induced operators commute; if their nilpotence indices areabyb, their sum is nilpotent ofindex at mosta+b−1 by the binomial theorem. For multiplicative commuting actions the same argument expands(λI+N)⊗(μI+M)−λμI into commuting nilpotent terms. Thus the generalized weights add or multiply as claimed.')
claim(836,[911],
 'The final reused sheet proposes a new split-Lie-algebra title, infinite highest-weight modules, Harish–Chandra formulae, Jacobson–Morozov, triality and integral forms; missing numbered propositions are editorial instructions rather than recoverable theorem statements.',
 'open on the pages as an editorial work programme','F',
 'Bourbaki VIII develops the identifiable subjects, but the source’s Tribu/draft numbers do not identify one exact published proposition for every requested addition. The assignment to Cartier is a documentary statement, not a proof of an integral-form theorem. No claim about motives is inferred from this reused text.',
 ['BourbakiLie1975','Humphreys1972'],lie,confidence='medium')

for c in b.C:
 if c['id']=='C-SA06-827':
  c['computation']['certificate']='parts/cote15_middle/code/peer_review_C827.py'
  c['computation']['output']='parts/cote15_middle/audit/peer_review_C827.json'
  c['computation']['independent_review']='parts/cote15_middle/peer_review_C827.md'
if __name__=='__main__':b.save()
