"""Manually checked bibliography and exact scope of each opening.

No entry is marked verified on the strength of a search snippet. For two
publisher books only metadata was accessible; their scope says so explicitly.
"""
references=[]
def ref(key,author,title,year,url,locator,scope,first=None,publication=None,**more):
    references.append(dict(key=key,author=author,title=title,year=str(year),url=url,
        locator=locator,verification_scope=scope,note='verified',
        first_circulation=first or 'Not established separately in this run.',
        publication=publication or str(year),accessed='2026-11-19',**more))

ref('SGA5XV','Christian Houzel','Morphisme de Frobenius et rationalité des fonctions L (SGA5, Exposé XV)',1977,
 'https://wstein.org/sga/sga5/SGA5.pdf','§1 nos1–4, pp442–452; §2 no1 and Proposition1, pp452–454; zero-basedPDFpages453–465',
 'Original scan actually opened in memory, inspected visually and by OCR; title, author, absolute/relative Frobenius, module and projective formulas, and étale coefficient comparison read. Public-page images deleted after reading.',
 first='Seminar1965–1966; exact circulation date of this exposé not established.',
 publication='Lecture Notes in Mathematics589(1977), pp442–480.',doi='10.1007/BFb0096812')
ref('SGA3I','Michel Demazure','SGA3, Exposé I: Structures algébriques. Cohomologie des groupes',1970,
 'https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp1.pdf','§§4.5–4.7, especially Propositions4.6.2,4.6.4–6,4.7.2–3; §5.3; PDFpp18–25',
 'Original-text retyping opened; definitions of V/W, linear functor full faithfulness, coaction identities, and finite locally free End/Aut compared. Demazure is the exposé author; the series title does not justify classA.',
 first='SGA3 seminar1962–1964; exact date of the individual exposition not established.',publication='SGA3 I, LNM151(1970); opened retyping hosted by the SGA3 editor.')
ref('SGA3VI_A','Pierre Gabriel','SGA3, Exposé VI_A: Généralités sur les groupes algébriques',1970,
 'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp6A-13oct24.pdf','§1; §§2.3–2.5, especially Proposition2.4 and Corollary2.4.1',
 'Named-author exposition opened; locally finite-type connected components, flatness/image results, and imperfect-field reduced-group examples read. The2024 editorial file is not itself the original circulation date.',
 first='SGA3 seminar1962–1964.',publication='SGA3 I, LNM151(1970); revised edition2011; opened file dated13October2024.')
ref('SGA3VIIA','Pierre Gabriel','SGA3, Exposé VII_A: Schémas en groupes infinitésimaux',1970,
 'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp7A-13oct24.pdf','§§4.3.1–4.3.3; Theorem7.4 and Remark7.5; PDFpp28–29,49–51',
 'Frobenius/Verschiebung over flat bases, finite duality, and exact finite-flat restricted-Lie hypotheses read; the adjacent nonflat boundary was inspected.',
 first='SGA3 seminar1962–1964.',publication='SGA3 I, LNM151(1970); revised edition2011; opened file13October2024.')
ref('SGA3VIII','Alexander Grothendieck','SGA3, Exposé VIII: Groupes diagonalisables',1970,
 'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp8-8nov09.pdf','§§1–3; Theorem3.1; author linePDFp1',
 'The author line explicitly names Grothendieck. Biduality, diagonalizable groups, character duality and exactness read. Editorial additions in the2009 file are not silently assigned to the original manuscript.',
 first='SGA3 seminar1962–1964.',publication='SGA3 I, LNM151(1970); opened revised file8November2009.')
for key,title,locator,scope in [
 ('SGA1III','SGA1, Exposé III: Morphismes lisses, propriétés de prolongement','§5, Proposition5.8, Corollary5.9 and projective/Brauer–Severi paragraph, printedp63/PDF78',
  'Proper flat formal schemes over a complete local ring, H¹ tangent obstruction, and projective-space rigidity read. The following descent paragraph explicitly discusses a finite étale extension.'),
 ('SGA1V','SGA1, Exposé V: Le groupe fondamental, généralités','§§4–7; §5 Proposition5.2 atprintedp105/PDF120; Proposition5.8 atp107/PDF122',
  'Finite Galois-category equivalence and the explicit equivalence of pro-finite Galois sets with compact totally disconnected continuous-action spaces read; not confused with arbitrary locally pro-étale spaces.'),
 ('SGA1Torsors','SGA1: torsors and faithfully flat descent','Exposé III §4.1; Exposé VIII descent; compare MilneEC §11 for the exact cocycle/torsor calculation',
  'Torsor and descent framework opened. No claim that an exact theorem about the notebook’s f-rigidification was found under that name; its formula is reconstructed separately.')]:
    ref(key,'Alexander Grothendieck',title,1971,'https://arxiv.org/pdf/math/0206203',locator,scope,
        first='IHES seminar1960–1961.',publication='LNM224(1971); revised SMF edition2003, arXivv2 dated4January2004.')
ref('BrauerI1966','Alexander Grothendieck',"Le groupe de Brauer I: Algèbres d’Azumaya et interprétations diverses",1966,
 'https://www.numdam.org/article/SB_1964-1966__9__199_0.pdf','§§1.2–1.3; Theorem1.6(Serre), Corollary1.7, pp199–204; §2 general topoi',
 'Original published exposition opened; two independent split stabilizers, obstruction class, and finite-CW torsion realization read. Serre is explicitly credited for Theorem1.6.',
 first='Séminaire Bourbaki, exposé290, May1965.',publication='Séminaire Bourbaki9(1964–1966), published1966, pp199–219.')
ref('BrauerII1966','Alexander Grothendieck','Le groupe de Brauer II: Théorie cohomologique',1966,
 'https://www.numdam.org/item/SB_1964-1966__9__287_0.pdf','§0, pp288–289; §1.8 and Corollary1.10, p293',
 'Degree-one Brauer–Severi splitting and generic-injectivity statement read with the precise locally noetherian/regular or factorial hypotheses. No singular-base extension inferred.',
 first='Séminaire Bourbaki, exposé297, November1965.',publication='Séminaire Bourbaki9(1964–1966), published1966, pp287–307.')
ref('FGA236','Alexander Grothendieck','Technique de descente et théorèmes d’existence VI: Les schémas de Picard, propriétés générales',1962,
 'https://www.numdam.org/article/SB_1961-1962__7__221_0.pdf','§4, p242; Theorem4.1 and Corollary4.2, pp242–243; PDFpp22–23',
 'Original exposition opened; divisor-only numerical/torsion equality credited to Matsusaka, finiteness hypotheses, and distinction from higher-codimension cycles checked.',
 first='Séminaire Bourbaki, exposé236, May1962.',publication='Séminaire Bourbaki7(1961–1962), pp221–243.')
ref('Oda1969','Tadao Oda','The first de Rham cohomology group and Dieudonné modules',1969,
 'https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf','§5; Corollaries5.11–5.12, p131/PDF69; logarithmic comparison nearp126',
 'Both exact corollaries read:5.11 for abelian varieties over perfect fields;5.12 for proper smooth X over a perfect field explicitly assumes X(k) nonempty and has an iterated-Cartier-stable image. Pointwise Pic[p] is distinguished from group-scheme data.',
 first='Part of Harvard thesis, June1967 (authorial footnote).',publication='Annales scientifiques ENS, 4e série2(1969),63–135.',doi='10.24033/asens.1177')
ref('Cartier1958','Pierre Cartier','Questions de rationalité des diviseurs en géométrie algébrique',1958,
 'https://www.numdam.org/item/10.24033/bsmf.1503.pdf','Differential and logarithmic criterion, printedpp200–203; broader divisor discussion',
 'Original paper opened and the Cartier/logarithmic criterion inspected. Smooth/regular field hypotheses are retained; no claim that normal singular Kähler differentials satisfy the same criterion.',
 publication='Bulletin SMF86(1958),177–251.',doi='10.24033/bsmf.1503',zbl='0091.33501')
ref('Lang1956','Serge Lang','Algebraic groups over finite fields',1956,
 'https://wstein.org/papers/bib/Lang-Algebraic_Groups_Over_Finite_Fields.pdf','Theorems1–2, printedp555 onward; PDFpage1 visually inspected',
 'Primary scan opened and theorem page visually read. Connected finite-field Lang surjectivity is the exact comparator; the zero-differential arbitrary-base extension is reconstructed in this run.',
 first='Received9March1956.',publication='American Journal of Mathematics78(1956),555–563.',doi='10.2307/2372673')
ref('Perrin1976','Daniel Perrin','Schémas en groupes quasi-compacts sur un corps et groupes henséliens',1976,
 'https://www.numdam.org/item/10.24033/bsmf.1830.pdf','Theorem2.4.1; Theorems4.1.4 and4.2.1; Remark4.2.2',
 'Primary paper opened; quasi-compact approximation, quotient hypotheses and the infinite-product warning read. This is not an identification of the notebook’s illegible C,C′ and κ.',
 first='1975 prepublication, Publications Mathématiques d’Orsay165,75-46 (paper bibliography).',publication='Bulletin SMF104(1976),323–335.',doi='10.24033/bsmf.1830')
ref('Serre1960','Jean-Pierre Serre','Groupes proalgébriques',1960,
 'https://www.numdam.org/article/PMIHES_1960__7__5_0.pdf','Introduction and §§1–2',
 'Primary monograph opened; commutative pro-quasi-algebraic groups in the perfected category are explicitly distinguished from arbitrary pro-schemes/group objects.',
 first='Received2May1960.',publication='Publications Mathématiques IHES7(1960),5–67; archive publication28December1960, frontmatter legal-deposit1961.')
ref('MilneAG2017','James S. Milne','Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field',2017,
 'https://www.jmilne.org/math/Books/iAG2017.pdf','§2i; Theorem3.37, Example3.42(a), Lemma3.44, §§4.7–4.9; structure chapters',
 'Author-hosted full text opened. Exact finite-dimensional-algebra Hilbert90, smooth Shapiro H¹, finite subcomodule and faithful finite-dimensional representation statements read. The field/finite-type limits are explicit.',
 publication='Cambridge Studies in Advanced Mathematics170, Cambridge University Press,2017.')
ref('MilneCFT','James S. Milne','Class Field Theory',2020,
 'https://www.jmilne.org/math/CourseNotes/CFT.pdf','ChapterII, Proposition1.22, Corollary1.23, Proposition1.24; §4 Proposition4.2',
 'Author-hosted course notes opened; finite Galois Hilbert90, cyclic norm equation, additive vanishing and continuous-cohomology direct-limit proposition read.',
 first='First web version1996; course ancestry stated in the notes.',publication='Version4.03,6August2020.')
ref('MilneEC','James S. Milne','Lectures on Étale Cohomology',2013,
 'https://www.jmilne.org/math/CourseNotes/LEC.pdf','§§7–12; §11 Proposition11.1 and the preceding nonabelian six-term sequence, printedpp76–79',
 'Author-hosted text opened; sheaf/derived-image background and the actual cocycle–torsor construction read. It does not identify an unspecified gluing square in the manuscript.',
 first='Courses1989 and1998; first web version1998.',publication='Version2.21,22March2013.')
ref('SerreGC','Jean-Pierre Serre','Galois Cohomology',1997,
 'https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Serre%20-%20Galois%20cohomology.pdf','Opened9-page frontmatter and table of contents; I§5.3–5.5 locators are bibliographical only',
 'Metadata/frontmatter only: first-edition history and chapter titles checked. The full twisting chapter was not opened. Mathematical support in this dossier comes from opened Milne passages and the written cocycle calculations, not an alleged full-book read.',
 first='French first edition1964 based on1962–1963 course, as stated in the opened foreword.',publication='English translation1997; opened corrected printing2002.')
ref('Brion2014','Michel Brion','On algebraic semigroups and monoids',2014,
 'https://www-fourier.univ-grenoble-alpes.fr/~mbrion/asm_final.pdf','Conventionsp3; §2, especially Proposition1 and Proposition3(iii); matrix linearization discussion',
 'Author-hosted paper opened. Varieties are reduced separated finite type over an algebraically closed field; Proposition3(iii) gives the unique-idempotent group criterion. Nonreduced/arbitrary-base scheme extensions are not claimed from this source.',
 first='arXiv1208.0675,3August2012; revised20December2013.',publication='Algebraic Monoids, Group Embeddings, and Algebraic Combinatorics, Fields Institute Communications71(2014).')
ref('WisbauerCoalgebras','Tomasz Brzeziński and Robert Wisbauer','Corings and Comodules: Cairo lecture notes',2004,
 'https://www.math.uni-duesseldorf.de/~wisbauer/Cairo-Lec.pdf','§1.21; §7.6; Theorem7.12; §§8.4–8.7 and8.12',
 'Full lecture text opened; tensor-purity, flat finite intersections, locally projective duality and finite coefficient constructions inspected. Theorem7.12 says the flat comodule category is Grothendieck and directly checks intersections of two subcomodules; it is not cited as an underlying-set arbitrary-intersection theorem.',
 first='LecturesNovember–December2004.',publication='Cairo University Mathematics Department Technical Report1,2004; exact bibliographic authorship checked on frontmatter separately.')
ref('ModuleSchemes2009','Amelia Álvarez and Carlos Sancho and Pedro Sancho','Characterization of quasi-coherent modules that are module schemes',2009,
 'https://matematicas.unex.es/~sancho/articulos/Characterization.pdf','Theorem1.1 and Corollaries1.2–1.3, pp1–2',
 'Author-hosted2-page manuscript opened in full. It proves the module-scheme equivalence with finite projectivity; arbitrary scheme necessity is this run’s square-zero reconstruction. arXiv0709.3412 endpoint failed and is not substituted for this successful opening.',
 first='Manuscript datedJune2007; arXiv identifier0709.3412 found in search.',publication='Communications in Algebra37(2009); volume/year verified from metadata, page range not independently opened.')
ref('HornbostelSchroer2015','Jens Hornbostel and Stefan Schröer','Infinite CW-complexes, Brauer groups and phantom cohomology',2015,
 'https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/infinite_cw-complexes.pdf','Theorem1.6; Theorem3.1; §5',
 'Primary full text opened; compact-space equality, Br(K(Z/n,2))=0, and infinite elementary-abelian examples read. The compact/Hausdorff conventions and distinction from finite CW complexes are retained.',
 first='Opened manuscript dated2May2013.',publication='Israel Journal of Mathematics207(2015),77–101.',doi='10.1007/s11856-015-1172-x')
ref('AntieauWilliams2014','Benjamin Antieau and Ben Williams','The topological period-index problem over 6-complexes',2014,
 'https://arxiv.org/pdf/1208.4430','TheoremsA–B; TheoremB proofPDFp16; Proposition6.2',
 'Primary full text opened; finite connected6-dimensional CW example with periodn and index gcd(2,n)n², hence period2/index8, checked exactly. It refutes fixed degree while respecting arbitrary-degree finite-CW realization.',
 first='arXivv1,22August2012; v3,30August2013.',publication='Journal of Topology7(2014),617–640; online4November2013.',doi='10.1112/jtopol/jtt042')
ref('GiokasSingh2024','John Giokas and Anurag K. Singh','On an example of Nagarajan',2024,
 'https://www.math.utah.edu/~singh/publications/giokas_singh.pdf','Theorem2.1 and proof, PDFpp2–5; references to Nagata and Nagarajan',
 'Primary full text opened; cyclic-order-p action on a noetherian regular local power-series ring with nonnoetherian invariants read. Its historical references were followed as leads; older papers not opened are not certified.',
 first='Received29November2022; online16October2023.',publication='Journal of Algebra638(2024),931–936.',doi='10.1016/j.jalgebra.2023.09.038')
ref('MittagLeffler2026','Rankeya Datta and Neil Epstein and Kevin Tucker','Mittag-Leffler modules and intersection flatness',2026,
 'https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/mittagleffler-modules-and-intersection-flatness/EAE22B6C98269DA183E62520265AD1F2',
 'Definition4.2.2; Theorem4.3.1; Theorem4.3.12',
 'Full publisher HTML opened. Flat Mittag-Leffler iff intersection flat, including universal version, read. This is a module result, not an exact resolution of the flat-coalgebra intersection assertion.',
 publication='Forum of Mathematics, Sigma; published online3June2026.',doi='10.1017/fms.2026.10204')
ref('Narvaez2009','Luis Narváez Macarro','Hasse–Schmidt derivations, divided powers and differential smoothness',2009,
 'https://www.numdam.org/article/AIF_2009__59_7_2979_0.pdf','§1.3, equations(1.7)–(1.9), Proposition1.12, pp2991–2992/PDF13–14',
 'Original paper opened. The graded dual of Sym has divided powers and Γ(M∨)→(Sym M)∨ is an isomorphism with the stated finite-projectivity hypotheses. The Roby1963/1965 bibliography was read as a backward lead.',
 first='Received3February2009; accepted6March2009; arXiv0903.0246 identified.',publication='Annales de l’Institut Fourier59(2009),2979–3014.',doi='10.5802/aif.2513')
ref('Tarizadeh2026','Abolfazl Tarizadeh','Connected components of qcqs schemes and projective spaces',2026,
 'https://arxiv.org/pdf/2401.05185','Corollary3.4; Theorem3.13, PDFp7; Lemma3.19 and Corollary3.22',
 'Version6 full text opened; qcqs component/quasi-component theorem and inverse-image description via global functions read. No claim that the quasi-compact-only manuscript wording follows.',
 first='arXivv1,10January2024, under the earlier title Idempotents and connected components.',publication='arXivv6,16April2026; journal publication not established.')
ref('Humphreys1990','James E. Humphreys','Reflection Groups and Coxeter Groups',1990,
 'https://www.cambridge.org/core/books/reflection-groups-and-coxeter-groups/2910C1E00877D33A04A512791B6EDD72',
 'Publisher metadata; §3.16 pp74–76 is a locator found through secondary references, not opened text',
 'Publisher bibliographic page opened; theorem pages not obtained. Coxeter/forest mathematics is rechecked in proofs.md §12 and checks.py. Do not label this a full theorem-page verification.',
 publication='Cambridge Studies in Advanced Mathematics29,1990.')
ref('BourbakiUniform','Nicolas Bourbaki','General Topology, Chapters1–4',1995,
 'https://link.springer.com/book/10.1007/978-3-642-61701-0','ChapterII, Uniform Structures, pp169–218; chapter landing page also opened',
 'Publisher metadata and chapter locator opened; full chapter axioms not supplied by that page. The actual entourage implication is checked directly from the attached sheet and in proofs.md §9.',
 publication='Opened Springer edition copyright1995; softcover1998; eBook2013. Earlier edition chronology not independently certified here.',doi='10.1007/978-3-642-61701-0')
ref('GrothSerre1964CSG','Alexander Grothendieck','Lettre à J.-P. Serre,12.8.1964',2024,
 'https://csg.igrothendieck.org/wp-content/uploads/2024/04/L23d.pdf','ProvenancePDFp2; textPDFpp4–5',
 'Entire6-page edition opened, including provenance: derived from Montpellier cote44. It is another transcription of the same witness. Date and unproved positivity language read; scan reading is not certified.',
 first='Letter dated12August1964.',publication='Draft transcription edited by Mateo Carmona et al.,CSG,April2024.')
ref('SerreMotifs1991','Jean-Pierre Serre','Motifs',1991,
 'https://www.numdam.org/item/AST_1991__198-199-200__333_0.pdf','Annexe1, pp342–344, especiallyp343; PDFindices10–12',
 'Original publication opened. Extract explicitly dated16August1964; construction, half-Betti bound, and unresolved Hodge–Néron–Tate link read. The date is not inferred from nearby correspondence.',
 first='Luminy Journées arithmétiques17–21July1989; quoted letter16August1964.',publication='Astérisque198–199–200(1991),333–349.',zbl='0759.14002')
ref('GrothMumfordLetters','Alexander Grothendieck and David Mumford','Correspondence',2010,
 'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Letters/AGMumford.pdf','Letter24,31August1964,p89/PDF88; letter43,9August1968,p143/PDF142; letter44,4September1968,p145/PDF144',
 'Exact dated letters opened. The1964 limited-results admission and1968 reassessment were read. Editorial compilation date is not independently established and is not used to date the manuscript.',
 first='Letters dated1964 and1968 as above.',publication='Public edited correspondence PDF; compilation publication date not independently established.')

def st(key,tag,title,locator,scope):
    ref(key,'The Stacks Project Authors',title,2026,'https://stacks.math.columbia.edu/tag/'+tag,
        locator,scope,publication='Continuously revised electronic reference, opened19November2026.',tag=tag)
st('Stacks07Z6','07Z6','Fitting ideals','§15.8, Lemmas15.8.4 and15.8.8','Base change and local-freeness criterion read; finite-presentation input retained in the Frobenius-fixed-module proof.')
st('Stacks0EBU','0EBU','Frobenius action on modules and Kunz’s theorem','Kunz criterion in characteristicp','Noetherian regularity/flatness criterion opened; not used as if every Frobenius pullback were exact.')
st('Stacks025F','025F','Étale morphisms and open immersions','Theorem41.14.1 and relative-Frobenius Lemma41.14.3','Étale monomorphism/open immersion and the étale relative Frobenius implication read; full converse is checked in originalSGA5XV.')
st('Stacks0CC6','0CC6','Frobenii','§33.36','Absolute/relative Frobenius, twists and base-change properties read.')
st('Stacks03SL','03SL','Frobenii','§64.3, especially canonical coefficient comparison and cohomological identity','The coefficient map is part of the assertion; geometric Frobenius is not said to act trivially.')
st('Stacks04DE','04DE','Homeomorphism onto a closed subset','Lemma29.46.4','Exact lemma and local-affine proof read; no finite-presentation hypothesis inserted.')
st('Stacks01OA','01OA','Projective bundles','§27.21','Universal invertible quotient and O(1) convention read; monomorphism alone does not imply degree-one linearity.')
st('Stacks056P','056P','Relative effective Cartier divisors','§31.19, Lemma31.19.9','Fibrewise Cartier lifting under flatness and finite presentation read.')
st('Stacks062Y','062Y','Fibrewise Cartier criterion','Lemma31.19.9','Exact hypotheses and distinction between parts(1) and(2) read.')
st('Stacks047J','047J','Group schemes over fields','§39.7, Lemmas39.7.9–10 and Proposition39.7.11','General neutral component geometrically irreducible, quasi-compact, closed normal subgroup read, beyond locally finite type.')
st('Stacks035U','035U','Geometrically reduced schemes','§33.6','Field-extension and product criteria read with reducedness/perfectness hypotheses.')
st('Stacks0361','0361','Geometrically connected schemes','§33.7, especially Lemma33.7.12','Nonempty connected conventions, product/base-extension criteria and geometric-connected-source implication read.')
st('Stacks0364','0364','Geometrically irreducible schemes','§33.8','Nonempty irreducible product and separably closed field criteria read.')
st('Stacks0366','0366','Geometrically integral schemes','§33.9','Geometric integrality criteria and proper global function algebra read.')
st('StacksProperFunctions','0366','Global functions on a proper scheme over a field','Lemma33.9.3 and Lemma33.9.4','Proper reduced H⁰ is a product of finite field extensions; over a perfect field its units are p-divisible.')
st('StacksCompletion','0BNH','Completion of Noetherian rings','§10.97, Lemmas10.97.1–3','Finite-module exactness, flatness and faithful flatness hypotheses read; not transferred to arbitrary modules without justification.')
st('StacksInjective','05NU','Baer’s criterion','Lemma19.2.6','Ideal-extension criterion read and applied to principal ideals to prove divisible iff injective over aPID.')
st('Stacks0906','0906','Connected components of a spectral space','Lemma5.23.9','Profinite component-space conclusion read; spectral/qcqs hypotheses retained.')
st('StacksGeomRegular','038S','Geometrically regular schemes','§33.12','Finite purely inseparable testing and finite-type smoothness comparison read.')
st('StacksSmoothField','04QM','Schemes smooth over fields','§33.25','Reduced/perfect hypotheses and smooth locus criteria read; no claim that every nonreduced scheme has a dense smooth locus.')
st('StacksGroupSmooth','0BF6','Properties of algebraic group schemes','§39.8, Lemmas39.8.2,39.8.4 and Remark39.8.5','Characteristic-zero and perfect-field smoothness, and reduced imperfect-field counterexample read.')
st('StacksProjection','01E6','Projection formula','§20.54, Lemma20.54.2','Finite locally free projection formula read; it does not remove Picard representability/base-change hypotheses.')
st('Stacks04BU','04BU','Infinitesimal deformations of maps','Lemmas37.9.1–2,37.9.5','Square-zero difference of maps represented by Hom of pulled-back differentials read for arbitrary schemes, not only affines.')
st('Stacks0G8P','0G8P','Characterizing finitely presented modules','Lemma10.11.4','Hom(Q,−) preserves filtered colimits iff Q is finitely presented; exact lemma read and applied in the arbitrary-scheme representability proof.')

# Failed database openings are preserved honestly as search/access events,
# not as verified mathematical references.
for key,title,url in [
 ('ZblCartierAttempt','zbMATH Open record0091.33501, access attempt','https://zbmath.org/0091.33501'),
 ('ZblSerreMotifsAttempt','zbMATH Open record0759.14002, access attempt','https://zbmath.org/0759.14002'),
 ('ZblSerreProAttempt','zbMATH Open record0097.35901, access attempt','https://zbmath.org/0097.35901')]:
    references.append(dict(key=key,author='zbMATH Open',title=title,year='2026',url=url,
        locator='Access failed in this run.',verification_scope='Unverified database record; Numdam primary texts were opened separately.',note='unverified',first_circulation='Not applicable.',publication='Database access attempt19November2026.',accessed='2026-11-19'))
