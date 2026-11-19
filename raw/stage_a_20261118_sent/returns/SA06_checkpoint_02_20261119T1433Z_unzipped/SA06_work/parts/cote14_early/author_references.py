#!/usr/bin/env python3
"""Manually curated primary-source metadata; emit mergeable JSON and BibTeX."""
import json
from pathlib import Path
O=Path(__file__).resolve().parent
R=[]
def ref(key, author, title, year, url, locators, **kw):
    R.append(dict(key=key,author=author,title=title,year=year,url=url,note='verified',
                  checked_date='2026-11-19',locators=locators,**kw))

ref('DeligneMilne1982','Deligne, Pierre and Milne, James S.','Tannakian Categories','1982',
    'https://www.jmilne.org/math/xnotes/tc2018.pdf',
    ['Proposition 2.23: characteristic-zero connected affine group is pro-reductive iff its finite-dimensional representation category is semisimple.',
     'Theorem 3.2: tensor isomorphism scheme of fibre functors is an affine faithfully flat torsor; converse by contracted products.',
     'Lemma 4.24 and Propositions 4.22–4.23: Hodge elements and compact inner real forms.',
     'Theorem 5.16 and Remark 5.17, corrected PDF p.53: polarizable Tate triples and compact kernel of the Tate character; neutralness has a further parity-square condition.',
     'Propositions 5.18–5.19, corrected PDF p.53: Hodge-element description of polarizations; positive real fibre functor under w(-1)=1.'],
    booktitle='Hodge Cycles, Motives, and Shimura Varieties',series='Lecture Notes in Mathematics',volume='900',pages='101--228',publisher='Springer',
    first_circulation='Not established in this search; publication 1982.',version='Author-corrected text, 2018-11-04; locators use this text.',
    opened_refs=['turn280700554view0','turn264799867view3'],limitations='Not an identification of the missing manuscript axioms 3° or I(G).')
ref('ChoudhuryGallauer2017','Choudhury, Utsav and Gallauer Alves de Souza, Martin','An isomorphism of motivic Galois groups','2017',
    'https://arxiv.org/pdf/1410.6104',
    ['Theorem 9.1, arXiv v3 p.41: the two comparison maps are inverse isomorphisms of Hopf algebras over a principal ideal domain.',
     'Introduction pp.1–3: Ayoub group uses H_0 of the Betti-derived Hopf algebra; the theorem does not identify a motivic t-structure.'],
    journal='Advances in Mathematics',volume='313',pages='470--536',doi='10.1016/j.aim.2017.04.006',
    first_circulation='2014-10-22 (arXiv v1); v3 2017-05-18; journal issue 2017-06-20.',
    opened_refs=['turn654440830view0','turn300877855view0','turn981018233view4'],
    additional_urls=['https://arxiv.org/abs/1410.6104'],
    limitations='Base field has a chosen embedding into C; group is the degree-zero stable group, not the full derived Hopf object. Publisher page returned403; bibliographic DOI and journal metadata independently exposed by arXiv record.')
ref('Arapura2013','Arapura, Donu','An Abelian Category of Motivic Sheaves','2013',
    'https://arxiv.org/pdf/0801.0261',
    ['Theorem 6.4.1, arXiv v4 p.60: for smooth S the pure Nori-type category M_pure(S,Q) is equivalent to the category M_A(S) of André motives; proof displayed for Spec(k).',
     'Proposition 6.3.8 and Corollary 6.3.9, p.59: exact tensor associated-graded functor and induced semidirect-product statement.'],
    journal='Advances in Mathematics',volume='233',pages='135--195',
    first_circulation='2008-01-01 (arXiv v1); v4 2012-10-09; journal 2013.',
    opened_refs=['turn654440830view1','turn264799867view4','turn981018233view5'],
    additional_urls=['https://arxiv.org/abs/0801.0261'],
    limitations='Schemes are over a subfield of C. The theorem concerns motivated correspondences; it does not assert every motivated cycle is algebraic.')
ref('HuberMuellerStach2017','Huber, Annette and Müller-Stach, Stefan','Periods and Nori Motives','2017',
    'https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-errata/buch-errata.pdf',
    ['Theorem 9.1.16, printed p.213 (PDF p.235), proof §9.5: rational Nori motivic Galois exact sequence over k with algebraic closure embedded in C.',
     'Remark 9.5.7, printed p.239 (PDF p.261): connectedness of the geometric motivic group is open and follows from the period conjecture.',
     'Theorem 10.2.7, printed p.247 (PDF p.269): pure rational Nori motives and André motives are equivalent semisimple abelian categories.',
     'Theorem 10.2.8, printed p.249 (PDF p.271): kernel of the quotient to the pure group is pro-unipotent; the pure group is pro-reductive; arithmetic base-change sequence is compatible.',
     'Theorem 13.1.4, printed p.284 (PDF p.306): formal-period spectrum is the Betti–de Rham comparison torsor.',
     '§14.1, printed pp.301–302 (PDF pp.323–324), equation(14.1): relative H^1(G_m,{1,alpha}) period matrix with entries1,log(alpha),2pi i.'],
    publisher='Springer',series='Ergebnisse der Mathematik und ihrer Grenzgebiete',volume='65',
    first_circulation='First circulation not established; original book2017. Consulted annotated file dated2025-07-01, including2024 corrections to §9.5.',
    opened_refs=['turn654440830view2','turn300877855view2','turn300877855view3','turn300877855view4','turn264799867view1','turn557706848view2','turn557706848view3'],
    limitations='Exact sequence does not prove geometric connectedness. Semisimplicity applies to pure motives; the mixed category contains nontrivial extensions.')
ref('Kahn2025Descent','Kahn, Bruno','Galois descent for motivic theories','2025',
    'https://webusers.imj-prg.fr/~bruno.kahn/preprints/stacks-TAC.pdf',
    ['Theorem 1.1: rational pure motives for an adequate relation form an étale stack.',
     'Theorem 5.10, printed p.606 (PDF p.19): exact sequence1→H→G→Pi→1 under Theorem2.17(b) for every finite Galois object.',
     'Theorem 10.2 and Remark 10.3, PDF p.24: Nori motives with coefficients in a Q-algebra form an étale stack; Theorem5.10 recovers HMS Theorem9.1.16.'],
    journal='Theory and Applications of Categories',volume='44',number='20',pages='588--616',
    first_circulation='Received2024-05-30; final form2025-05-29; published2025-06-25, as printed in consulted file. First public preprint date not established.',
    opened_refs=['turn654440830view3','turn300877855view5','turn300877855view6','turn264799867view2'],
    limitations='A descent proof of exactness; it is not a connectedness theorem for the geometric kernel.')
ref('Kunnemann1993','Künnemann, Klaus','A Lefschetz decomposition for Chow motives of abelian schemes','1993',
    'https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0011.pdf',
    ['Introduction equations(2)–(4), pp.85–86: hard Lefschetz and primitive decomposition for rational Chow motives of abelian varieties, and the commutator identity.',
     '§1 p.87: relative category over a smooth quasi-projective connected base S over a field; rational coefficients.'],
    journal='Inventiones Mathematicae',volume='113',pages='85--102',doi='10.1007/BF01244303',
    first_circulation='Received1992-04-23; publication1993. Earlier public circulation not established.',
    opened_refs=['turn981018233view1'],
    limitations='Special to abelian schemes; does not settle the standard conjectures or motivic sl2 construction for every smooth projective variety.')
ref('Jannsen1992','Jannsen, Uwe','Motives, numerical equivalence, and semi-simplicity','1992',
    'https://epub.uni-regensburg.de/26642/1/jannsen10.pdf',
    ['Theorem1, pp.448–449: for an adequate equivalence relation on cycles with coefficients in a characteristic-zero field, the category of pure motives is semisimple abelian iff the relation is numerical equivalence.',
     'Corollary2, pp.450–451: under algebraicity of Künneth components, modify symmetry by the grading sign to obtain a Tannakian category.'],
    journal='Inventiones Mathematicae',volume='107',number='3',pages='447--452',doi='10.1007/BF01231898',
    first_circulation='Received1991-07-12; publication1992; earlier circulation not established.',
    opened_refs=['turn981018233view2'],
    limitations='The theorem alone does not cause the action on an arbitrary finer cycle quotient to factor through numerical equivalence.')
ref('Clemens1983','Clemens, Herbert','Homological equivalence, modulo algebraic equivalence, is not finitely generated','1983',
    'https://www.numdam.org/article/PMIHES_1983__58__19_0.pdf',
    ['Introduction Theorem0.2 and Corollary0.3, pp.19–20: for a very general quintic threefold, the Abel–Jacobi image of homologically trivial cycles has infinite rational dimension and the Griffiths group is not finitely generated.'],
    journal='Publications Mathématiques de l’IHÉS',volume='58',pages='19--38',
    first_circulation='Publication1983; first public circulation not established.',opened_refs=['turn280700554view1'],
    limitations='The countable-union genericity qualifier is retained; this supplies nonzero rational Griffiths classes, not a statement for every quintic.')
ref('Mumford1969','Mumford, David','Rational equivalence of 0-cycles on surfaces','1969',
    'https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969e--0-cycles-Euclid.pdf',
    ['Introduction pp.195–196 and theorem p.200: holomorphic2forms obstruct finite-dimensional parametrization of rational-equivalence classes of0cycles; hence pg>0 surfaces have nonrepresentable CH0 in the stated sense.'],
    journal='Journal of Mathematics of Kyoto University',volume='9',number='2',pages='195--204',
    first_circulation='Communicated1968-11-28; publication1969.',opened_refs=['turn280700554view2','turn557706848view8'],
    limitations='Web extractor attached an unrelated metadata title; PDF first-page title and author were checked. Application to E×E uses its nonzero holomorphic2form.')
ref('Voisin2025Universal0','Voisin, Claire','Varieties with representable CH_0-group and a question of Colliot-Thélène','2025',
    'https://api.algebraicgeometry.nl/Article/21296/2025-6-027.pdf',
    ['Definition1.1: integral universal0cycle on Alb(X)×X.',
     'Theorem1.4: smooth projective threefold with representableCH0 and no integral universal0cycle.'],
    journal='Algebraic Geometry',volume='12',number='6',pages='888--901',doi='10.14231/AG-2025-027',
    eprint='2508.02331',archiveprefix='arXiv',first_circulation='Received 2025-06-16; arXiv v1 2025-08-04; accepted 2025-10-10; arXiv v2 2025-10-15; journal issue 2025.',
    additional_urls=['https://arxiv.org/abs/2508.02331','https://arxiv.org/html/2508.02331v2'],opened_refs=['turn280700554view3','turn981018233view6','turn593062726view0','turn244379444view4','turn947032895view3'],
    limitations='Separates integral universalcycles from rational/miniversalcycles. It does not deny existence after multiplication by a nonzero integer.')
ref('AchterCasalainaMartinVial2023','Achter, Jeffrey D. and Casalaina-Martin, Sebastian and Vial, Charles','A functorial approach to regular homomorphisms','2023',
    'https://api.algebraicgeometry.nl/Article/19846/2023-1-003.pdf',
    ['Definition4.2 and Lemma4.7: miniversal cycles; regular-homomorphism image is an abelian subscheme and has a positive-degree miniversalcycle.',
     'Proposition5.3: Saito dimension-bound criterion for existence of an algebraic representative.',
     '§7.1, Theorem7.1 and Remark7.2: codimension1 algebraic representative is reduced Picard variety, with stated relative hypotheses.',
     '§7.2 and Remark7.10: top-degree Albanese map and torsion comparison; not generally an isomorphism on all0cycles.'],
    journal='Algebraic Geometry',volume='10',number='1',pages='87--129',doi='10.14231/AG-2023-003',
    first_circulation='Received2020-10-04; accepted2022-06-19; published2023. arXiv first date still to check.',
    opened_refs=['turn482488260view1','turn557706848view4','turn557706848view5','turn694517553view1','turn694517553view2'],
    limitations='Algebraic representatives are universal regular quotients; they are not automatically isomorphic to Grothendieck’s quotient by correspondence-generated Albanese kernels.')
ref('Kahn2021Regular','Kahn, Bruno','On the universal regular homomorphism in codimension 2','2021',
    'https://www.numdam.org/item/10.5802/aif.3408.pdf',
    ['Theorem0.1: existence of the universal regular homomorphism in codimension2 for a smooth projective variety over an algebraically closed field.',
     'Introduction and Lemma1.1: repair of the gap in Murre’s torsion argument; curve/Jacobian reduction.'],
    journal='Annales de l’Institut Fourier',volume='71',number='2',pages='843--848',doi='10.5802/aif.3408',
    first_circulation='Paper originated from letter to Murre2018-12-05; received2019-06-21; arXiv2007.07592 first2020-07-15; published2021-12-08.',
    opened_refs=['turn482488260view2'],limitations='Codimension2 existence does not establish existence in arbitrary codimension, nor equality with the manuscript quotient.')
ref('AchterCasalainaMartinVial2025','Achter, Jeffrey D. and Casalaina-Martin, Sebastian and Vial, Charles','Decomposition of the diagonal, intermediate Jacobians, and universal codimension-2 cycles in positive characteristic','2025',
    'https://www.math.uni-bielefeld.de/~vial/diagonal.pdf',
    ['Theorem1, Theorem4.4 and Theorem12.12: under the respective decomposition-of-diagonal hypotheses, distinguished symmetric autoduality/isogeny on the codimension2 algebraic representative.',
     'Conjecture5.1: canonical symmetric isomorphism for universally CH0-trivial smooth projective threefolds over perfect fields is conjecturally a principal polarization.',
     'Remark12.13 and Corollary13.3 distinguish autoduality from positivity in characteristicp.'],
    series='Astérisque',volume='455',publisher='Société Mathématique de France',doi='10.24033/ast.1244',
    first_circulation='AuthorPDF dated2025-03-19; published2025; earlier public preprint date still to check.',
    additional_urls=['https://smf.emath.fr/publications/decomposition-de-la-diagonale-jacobiennes-intermediaires-et-cycles-universels-de?language=en'],
    opened_refs=['turn482488260view3','turn694517553view3','turn694517553view4','turn981018233view3'],
    limitations='Cited theorem locators refer to the83-page authorPDF, not a presumed identical pagination of the printed volume.')
ref('Tate1966','Tate, John','Endomorphisms of abelian varieties over finite fields','1966',
    'https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf',
    ['Main Theorem, p.134: for finitek and l≠char(k), Hom(A,B)⊗Z_l→Hom_Gk(T_l A,T_l B) is bijective.',
     'First page: elliptic-curve case follows from Deuring, as pointed out by Mumford four years earlier.'],
    journal='Inventiones Mathematicae',volume='2',pages='134--144',
    first_circulation='Publication1966; first public circulation not established; source recalls Mumford observation about1962.',
    opened_refs=['turn224049452view2','turn694517553view5'])
ref('Milne2001Tate','Milne, James S.','The Tate conjecture for certain abelian varieties over finite fields','2001',
    'https://www.jmilne.org/math/articles/2001aP.pdf',
    ['AppendixA, TheoremA.3 and following Example, pp.14–15 of authorPDF: P(A)⊂M(A)⊂L(A), and absence of exotic Tate classes on powers of an elliptic curve.',
     'Example followingA.3: all Tate classes on powers of an elliptic curve are generated by Lefschetz classes.'],
    first_circulation='Authorfile dates1999-08-01; minor changes2001-02-11; publication2001.',
    opened_refs=['turn224049452view3','turn694517553view6'],limitations='Does not establish generation by divisorclasses for all abelian varieties; exterior invariants can be exotic.')

ref('Milne2004Shimura','Milne, James S.','Introduction to Shimura Varieties','2004',
 'https://www.jmilne.org/math/xnotes/svi2004.pdf',
 ['Proposition15.6, p122: representations of a torus are semisimple, and simple objects correspond to Galois orbits of characters.',
  'p19 and pp121–122: character gradings and their descent compatibility; p124: protori and continuous actions on infinite lattices.'],
 first_circulation='Consulted author text dated2004-10-23; earlier circulation not established.',
 opened_refs=['turn331942763view0','turn302622132view3','turn167079478view4'],limitations='Used for torus representation structure; the elementary cone and invariant-ring proofs are supplied independently, not attributed as theorem statements in this text.')
ref('Grothendieck1962Picard','Grothendieck, Alexander','Technique de descente et théorèmes d’existence en géométrie algébrique. VI. Les schémas de Picard: propriétés générales','1962',
 'https://www.numdam.org/article/SB_1961-1962__7__221_0.pdf',
 ['§3, Theorem3.3(iii), pp237–238: canonical relative Albanese torsor when the canonical abelian subscheme of Picard exists; compatibility with base change.',
  'Corollary3.2 and Remark3.4: existence over a field and failure of the analogous abelian subscheme for some infinitesimal bases.'],
 journal='Séminaire Bourbaki',number='236',volume='7',pages='221--243',
 first_circulation='Bourbaki exposé236, 1961–1962 session; published1962. Exact oral day not verified.',
 opened_refs=['turn776996946view2','turn167079478view2','turn408103069view2'])
ref('Grothendieck1969Standard','Grothendieck, Alexander','Standard conjectures on algebraic cycles','1969',
 'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1968.Grothendieck.StandardConjs.pdf',
 ['§2 pp194–195: algebraic Künneth projectors, trace argument, integrality and the same-cycle condition for l-independence.',
  '§3 pp196–197: algebraic-cohomology LefschetzA; B(X)⇒A(X), A(X×X)⇒B(X), and B⇒KünnethC.',
  '§4 pp197–199: primitive Hodge positivity, Weil consequences and numerical/homological cycle comparisons.'],
 booktitle='Algebraic Geometry, Bombay1968',publisher='Oxford University Press',pages='193--199',
 first_circulation='Presented at Bombay colloquium1968; published1969. Introduction says Bombieri and Grothendieck independently worked out the ideas about three years earlier.',
 opened_refs=['turn981018233view7','turn224049452view0'],
 inspection='All seven printed pages193–199 visually read from local renderings groth-1.png throughgroth-7.png; original tool PDF is image-only.',
 limitations='Its C^i means algebraic cohomology classes, unlike the1965 letter’s cycles modulo algebraic equivalence tensorQ.')
ref('Kleiman1968','Kleiman, Steven L.','Algebraic cycles and the Weil conjectures','1968',
 'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf',
 ['§1: cycle and correspondence formalism; Proposition1.3.6 is the trace formula.',
  'Theorem2.9 p371: B(X) equivalent to Künneth algebraicity together with algebraic inverse isomorphisms.',
  '§2 Appendix, Lemma2A5 p375: curve and Jacobian H1 comparison.',
  'Proposition3.5–3.6 pp378–379: numerical finiteness and comparison with homological equivalence.',
  'Corollary3.12 and Lemma3.13 p381: semisimplicity from positive involution under the stated Lefschetz/Hodge hypotheses.'],
 booktitle='Dix exposés sur la cohomologie des schémas',publisher='North-Holland',pages='359--386',
 first_circulation='Notes concern the1966 seminar; published1968. Exact first public version not established.',
 opened_refs=['turn224049452view1','turn173779276view2','turn260045725view2','turn260045725view3'])
ref('Deligne1974Weil','Deligne, Pierre','La conjecture de Weil. I','1974',
 'https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf',
 ['Theorem1.6, p276: for smooth projectiveX/F_q, Frobenius characteristic polynomials are integral and independent ofl≠p, with eigenvalue absolute valuesq^(i/2).',
  'Introduction p273: text follows six Cambridge lectures inJuly1973.'],
 journal='Publications Mathématiques de l’IHÉS',volume='43',pages='273--307',doi='10.1007/BF02684373',
 first_circulation='Cambridge lecturesJuly1973; received1973-09-20; publication1974-12-28.',
 opened_refs=['turn776996946view0','turn302622132view1','turn932258685view5'])
ref('Deligne1980Weil','Deligne, Pierre','La conjecture de Weil. II','1980',
 'https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf',
 ['Theorem4.1.1: hard Lefschetz for smooth projectiveX over an algebraically closed field, with ample class and l invertible.',
  '§4.1.6: weak Lefschetz/affine dimension input is cited toSGA4XIV3.2.'],
 journal='Publications Mathématiques de l’IHÉS',volume='52',pages='137--252',doi='10.1007/BF02684780',
 first_circulation='Received1979-06-01; publication1980-12-28; earlier public preprint not established.',
 opened_refs=['turn776996946view1','turn173779276view0','turn167079478view3','turn408103069view3'],
 limitations='Full PDF initially opened successfully; a later repeat exceeded tool size limit. Metadata rechecked at the primary Numdam article page.')
ref('SGA4XIV1973','Artin, Michael','Théorème de finitude pour un morphisme propre; dimension cohomologique des schémas algébriques affines','1973',
 'https://www.normalesup.org/~forgogozo/SGA4/14/14.pdf',
 ['ExposéXIV Corollary3.2, original p160, retyped PDFp9: affine finite-type scheme over separably closedk has torsion étale cohomological dimension at mostdimX.',
  'Corollary3.3, pp160–161: hyperplane/Gysin consequence; prime-to-characteristic local-constant purity identifies the usual weak Lefschetz statement.'],
 booktitle='SGA4, Théorie des topos et cohomologie étale des schémas, Tome3',series='Lecture Notes in Mathematics',volume='305',publisher='Springer',
 first_circulation='Seminar1963–1964; published1973. Consulted scholarly French retyping dated2024-07-30, with editorial annotations distinguished from the original.',
 opened_refs=['turn907701243view0','turn932258685view3'])
ref('SGA6XIII1971','Kleiman, Steven L.','Les théorèmes de finitude pour le foncteur de Picard','1971',
 'https://wstein.org/sga/sga/pdf/sga6.pdf',
 ['ExposéXIII Theorem4.6, printed645–647 (PDF648–650): for properX over algebraically closedk, numerical triviality of a line bundle is equivalent to tau-triviality.',
  'Theorem5.1, printed650 (PDF653): finite generation and bounded ranks/torsion orders of geometric-fibre Néron–Severi groups for properX over noetherianS.',
  'Proposition5.2, printed651 (PDF654): numerical codimension-p cycles are free of rank at mostb_(2p), for smooth properX over algebraically closedk.',
  'Theorem5.4, printed652 (PDF655): finitely many curves test bounded subsets ofPicard.'],
 booktitle='SGA6, Théorie des intersections et théorème de Riemann–Roch',series='Lecture Notes in Mathematics',volume='225',publisher='Springer',
 first_circulation='Seminar1966–1967; publication1971. Earlier versions of the statements were announced inFGA, according to the text.',
 opened_refs=['turn167079478view0','turn547131675view0','turn547131675view1'],
 inspection='Web PDF size limit; original54,325,694-byte PDF downloaded byroot and relevant pages visually inspected in this part. Numbering offset3 verified from printed pages.',
 limitations='Only the stated theorem loci and adjoining proofs were read, not the entire702-page volume.')
ref('Samuel1960Equivalence','Samuel, Pierre','Relations d’équivalence en géométrie algébrique','1960',
 'https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf',
 ['§2.5 pp477–479: abelian cycles are the common kernel of rational homomorphisms to abelian varieties; propositions10–11 compare algebraic and square equivalence.',
  '§2.6 p479: pseudo-equivalence means equality after a nonzero integral multiple.',
  'p480: divisor endpoint and Néron–Severi/numerical facts.'],
 booktitle='Proceedings of the International Congress of Mathematicians, Edinburgh1958',publisher='Cambridge University Press',pages='470--487',
 first_circulation='Congress1958-08-14 through1958-08-21; title/copyright pages establish publication1960.',
 opened_refs=['turn260045725view0'],inspection='Full originalPDF downloaded locally after web size-limit error; §2.5–2.6 and title/copyright pages read in OCR with mathematical formulas checked against context.',
 limitations='This kernel definition is not silently equated with the archive’s subgroup generated by images of Albanese kernels.')
ref('Kleiman1971Finiteness','Kleiman, Steven L.','Finiteness theorems for algebraic cycles','1971',
 'https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.1/ICM1970.1.ocr.pdf',
 ['pp445–447: universal regular quotients, miniversal isogeny families, distinction of abelian, Picard and Weil equivalence.',
  'p446 bottom–p447 andfootnote5: attributes a Picard-equivalence quotient construction to an unrecorded1964 observation ofGrothendieck; states cohomological dimension bound and dual isogeny.',
  'p449 references: identifies Samuel, Lieberman andSGA6 sources.'],
 booktitle='Actes du Congrès International des Mathématiciens, Nice1970',volume='1',publisher='Gauthier-Villars',pages='445--449',
 first_circulation='CongressSeptember1970; title/copyright pages establish publication1971.',
 opened_refs=['turn260045725view1'],inspection='Full originalPDF downloaded locally after web size-limit error; complete pp445–449 andtitle/copyright pages read.',
 limitations='The historical attribution is a source statement, not proof that the unidentified archive sheets were written in1964.')
ref('HernandezPelaez2025','Hernandez, Ivan and Pelaez, Pablo','Regular homomorphisms and mixed motives','2025',
 'https://arxiv.org/html/2509.15920v1',
 ['§4.1: Samuel abelian equivalence is the intersection of kernels of all regular homomorphisms.',
  'Theorem3.2.28: motivic image description of the kernel of a specified regular homomorphism.',
  'Theorem4.1.13: analogous construction for Samuel’s abelian-equivalence subgroup.'],
 eprint='2509.15920',archiveprefix='arXiv',first_circulation='2025-09-19; no later version or journal publication verified.',
 additional_urls=['https://arxiv.org/abs/2509.15920'],opened_refs=['turn184690913view0','turn411682971view0','turn411682971view1','turn797786326view0'],
 limitations='These statements do not assert algebraic representability in every codimension or equality with the archive quotient.')
ref('PelaezReyes2025','Pelaez, Pablo and Reyes, Araceli','Incidence equivalence and the Bloch–Beilinson filtration','2025',
 'https://arxiv.org/html/2501.19147v1',
 ['Theorem3.3.1: top-degree rational incidence subgroup equals the second orthogonal-filtration step; over algebraically closedk this is the rational Albanese kernel.',
  'Theorem3.3.2: exterior and intersection products of algebraically trivial cycles lie inF2.',
  'Theorem3.3.3: further all-codimension statements over finite fields or their algebraic closures.'],
 eprint='2501.19147',archiveprefix='arXiv',first_circulation='2025-01-31; journal publication not verified.',
 additional_urls=['https://arxiv.org/abs/2501.19147'],opened_refs=['turn184690913view1','turn411682971view2','turn797786326view1'],
 limitations='Rational incidence equivalence is not automatically the manuscript’s integral Albanese equivalence.')
ref('StacksMoving2026','The Stacks Project Authors','Chow Homology and Chow Groups: Moving Lemma','2026',
 'https://stacks.math.columbia.edu/tag/0B0D',
 ['§43.24, Lemma43.24.3: on a nonsingular projective variety, rationally equivalent representatives can be chosen to meet finite prescribed cycle lists properly.'],
 first_circulation='Continuously updated reference; consulted2026-11-19. Historical priority not assigned from this source.',
 opened_refs=['turn263247143view0'])
ref('StacksBrauer2026','The Stacks Project Authors','Étale Cohomology: The Brauer group of a scheme','2026',
 'https://stacks.math.columbia.edu/tag/0A2J',
 ['§59.62: Azumaya algebras and stabilized Brauer equivalence.',
  'Lemma59.62.1: an isomorphism of endomorphism algebras gives a line-bundle twist; proof uses the Morita evaluation map.'],
 first_circulation='Continuously updated reference; consulted2026-11-19. No historical priority claim.',opened_refs=['turn331942763view1'])
ref('Bass1967KTheory','Bass, Hyman','Lectures on Topics in Algebraic K-Theory','1967',
 'https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr41.pdf',
 ['Chapter2 Theorem4.4: Morita equivalence and evaluation maps for faithfully projective generators.',
  'Chapter3 Theorem4.1 pp81–83: equivalent Azumaya criteria.',
  'Chapter3 Corollary4.3 p84: double-centralizer multiplicationA⊗B^A≃B.',
  'Chapter3 Proposition4.10 pp85–86: stable Brauer equivalence and Morita equivalence.'],
 publisher='Tata Institute of Fundamental Research',number='41',
 first_circulation='LecturesDecember1965–February1966; notes byAmitRoy; publication1967, as stated inpreface.',
 opened_refs=['turn907701243view2','turn932258685view4','turn661638085view3'],
 limitations='Ring statements are used stalkwise for the supplied sheaf arguments. The book does not identify the author of the reused English draft.')
ref('BourbakiLie4562007','Bourbaki, Nicolas','Groupes et algèbres de Lie, chapitres4,5et6','2007',
 'https://link.springer.com/book/10.1007/978-3-540-34491-9',
 ['ChapterV, Groupes engendrés par des réflexions, pp57–141 (publisher contents).'],
 publisher='Springer',doi='10.1007/978-3-540-34491-9',
 first_circulation='Publisher explicitly identifies this as a reprint ofHermann1968 edition; eBook2007-05-26.',
 opened_refs=['turn167079478view1','turn408103069view1','turn547131675view2'],
 limitations='Publisher metadata and chapter scope checked; full subscription chapter not obtained. No exact published proposition number or identification of draftn°391 is asserted. Chamber facts are independently re-proved from supplied text.')
ref('Grothendieck1964LetterSerre','Grothendieck, Alexander','Letter to Jean-Pierre Serre,12August1964','1964',
 'https://csg.igrothendieck.org/wp-content/uploads/2024/04/L23d.pdf',
 ['Opening/intermediate-Jacobian paragraph: Albanese equivalence, duality of abelian cycle-parameter varieties and their Tate-module cohomological subquotients.',
  'Finalparagraph: positivity question for the induced pairing.'],
 first_circulation='Private letter dated1964-08-12; consulted modern transcription hosted2024. First public publication not verified.',
 opened_refs=['turn101449938view0'],
 limitations='External transcription of a different letter, not the27August1965 letter continued inCodex45–47.')
ref('Alexandrou2026Universal0','Alexandrou, Theodosis','A surface with representable CH_0-group but no universal zero-cycle','2026',
 'https://arxiv.org/pdf/2602.13435',
 ['Theorem1.3 p2: for specified ellipticAlbaneseE (includingEnd(E)=Z), a smooth projective complex surface with representableCH0 has no integral universal0cycle.',
  'Theorem5.1 and proof ofTheorem1.3 pp22–23: degeneration obstruction and passage tocomplex surfaces.'],
 eprint='2602.13435',archiveprefix='arXiv',doi='10.48550/arXiv.2602.13435',
 first_circulation='v1 submitted2026-02-13; v2 submitted2026-03-08; PDF internally dated2026-03-10. Journal publication not verified.',
 additional_urls=['https://arxiv.org/abs/2602.13435'],opened_refs=['turn663972476view0','turn663972476view1','turn494779915view0','turn494779915view1'],
 limitations='Recorded as a checked preprint theorem and its checked application. Main degeneration theorem not independently re-proved here. Index2 of the Albanese fibration alone is explicitly insufficient.')
ref('OpenAI2026CMHodge','OpenAI','The rational Hodge conjecture for CM abelian varieties','2026',
 'https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/README.md',
 ['Theorem1.1 p1 claims rationalHodge for allcomplexCMabelianvarieties.',
  'Corollary8.3 p49 claims rationalTate for allfinite-fieldabelianvarieties;Corollary8.4 p50 claims homological=numerical andHodgestandard for allabelianvarieties.',
  'The main argument depends onTheorem2.5 and thetheta/CM-source construction in§§4–7; §8 citesMilne implications.'],
 first_circulation='Previousedition2026-09-30 linked by theprimaryREADME; revisedcitation edition2026-10-06. Journal publication/referee status not verified.',
 additional_urls=['https://mathcommunity.github.io/oai-math-revised/papers/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf'],
 opened_refs=['turn374761499view2','turn374761499view3','turn431241942view0','turn431241942view1','turn431241942view2'],
 limitations='Existence and exact theorem statements/argument outline/consequence proofs checked. Main53-page theta construction NOT independently verified. This is carried as a source claim, not promoted to an established resolution of every standard-conjecture question.')
R.append(dict(key='Auslander1966RingedSpace',author='Auslander, Bernice',title='The Brauer group of a ringed space',year='1966',journal='Journal of Algebra',volume='4',pages='220--273',doi='10.1016/0021-8693(66)90040-8',url='https://doi.org/10.1016/0021-8693(66)90040-8',note='unverified',checked_date='2026-11-19',first_circulation='Publication1966 suggested by secondary bibliographies; primary publisher retrieval failed.',locators=[],opened_refs=['turn269780978view0'],limitations='Candidate for the reused English sheets only; no exact collation or authorship determination. Do not cite as a checked theorem source.'))
R.append(dict(key='Broe2026TateFourfolds',author='Broe, Matt',title='The Tate conjecture for abelian fourfolds over finite fields',year='2026',eprint='2608.28651',archiveprefix='arXiv',url='https://arxiv.org/abs/2608.28651',note='unverified',checked_date='2026-11-19',first_circulation='Search metadata says2026-08-19; primary abstract/PDF/HTML returnedDisabledError.',locators=[],opened_refs=['turn663972476view2','turn663972476view3','turn374761499view0','turn374761499view1'],limitations='Relevant lead only, no theorem locator or proof/application checked. Not used to upgrade a manuscript claim.'))

ref('Grothendieck1968LetterMumford','Grothendieck, Alexander','Letter to David Mumford, 20 November 1968','1968',
 'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Letters/AGMumford.pdf',
 ['Letter 46, p. 151: explicitly deduces failure of Samuel’s box-cycle question on a product of two elliptic curves from Mumford’s result.',
  'Letter 45, pp. 149–150, 10 October 1968: discusses Griffiths’s examples and distinguishes function-field examples from the finite-field speculation.'],
 first_circulation='Private letters dated 1968-10-10 and 1968-11-20; later public edition date not established by this PDF.',
 opened_refs=['turn175653707view0','turn175653707view1','turn947032895view4'],
 limitations='The direct negative answer for box cycles is documentary evidence; it is not evidence that the archive sheet itself was corrected or dated in 1968.')
ref('AchterCasalainaMartinVial2019','Achter, Jeffrey D. and Casalaina-Martin, Sebastian and Vial, Charles','Parameter spaces for algebraic equivalence','2019',
 'https://arxiv.org/pdf/1610.06586',
 ['Theorem 1 and Proposition 3.14, arXiv pp. 1, 9–10: over a perfect field, algebraic triviality can be exhibited by a smooth projective curve or an abelian variety.',
  'Introduction cites Weil 1954, Lemma 9 for the algebraically closed case; Theorem 4.11 separates descent and tau-triviality.'],
 journal='International Mathematics Research Notices',number='6',pages='1863--1893',doi='10.1093/imrn/rnx178',eprint='1610.06586',archiveprefix='arXiv',
 first_circulation='arXiv v1 2016-10-20; accepted 2017-07-11; first online publication 2017-08-13; issue March 2019; consulted arXiv v3 2019-10-16, internally dated 17 October.',
 additional_urls=['https://academic.oup.com/imrn/article/2019/6/1863/4082263'],
 opened_refs=['turn949400221search3','turn593062726view1','turn244379444view3','turn947032895view2'],
 limitations='Algebraically closed fields are perfect. No extension to arbitrary imperfect fields with integral coefficients is inferred.')
ref('Saito1979Intermediate','Saito, Hiroshi','Abelian varieties attached to cycles of intermediate dimension','1979',
 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8BE754AE13330E3050F3588FCD123D87/S0027763000024855a.pdf/abelian_varieties_attached_to_cycles_of_intermediate_dimension.pdf',
 ['Theorem 3.6, p. 111: incidence quotient of algebraically trivial cycles is an abelian variety, with correspondence functoriality.',
  'Theorem 4.4 and Corollary 4.5, p. 113: isogeny duality and transposition independence for incidence correspondences.',
  'Theorem 4.6, pp. 113–114: the correspondence-to-Hom map becomes an isomorphism over Q; a fixed positive integer clears denominators.',
  'Section 5, pp. 115–117: comparison with the complex algebraic Abel–Jacobi image; the unrestricted isogeny claim is explicitly left dependent on Griffiths’s announcement.'],
 journal='Nagoya Mathematical Journal',volume='75',pages='95--119',doi='10.1017/S0027763000024855',
 first_circulation='Received 1978-07-17; issue September 1979. Publisher online digitization 2016-01-22 is not the first publication.',
 opened_refs=['turn871099360search0','turn474940744view0','turn302317142view0','turn302317142view2','turn302317142view3','turn947032895view0','turn947032895view1'],
 limitations='Base field algebraically closed, arbitrary characteristic unless specified. The common-kernel incidence relation is not identified with the archive’s subgroup generated by images of Albanese kernels.')
ref('Peters2026Incidence','Peters, Chris','Incidence equivalence, a survey','2026',
 'https://arxiv.org/pdf/2607.22233',
 ['Definition 3.2 p. 6: common-kernel incidence equivalence; Theorem 5.8 p. 12 points back to Lieberman and Saito for duality.',
  'Corollary 7.8 p. 16: the stated Lefschetz-component condition implies the rational incidence/Abel–Jacobi comparison.'],
 eprint='2607.22233',archiveprefix='arXiv',
 first_circulation='arXiv v1 2026-07-24; PDF internally dated 2026-07-27. Journal publication not established.',
 opened_refs=['turn593062726view2','turn244379444view0','turn244379444view1','turn244379444view2','turn474940744view1','turn474940744view2'],
 limitations='Used as a backward-reference guide. The manuscript quotient is different. This survey’s whole argument is not independently certified; primary Saito passages, rather than the survey alone, support the recorded later theorem.')

ref('StacksLocalization2026','The Stacks Project Authors','Localization','2026',
 'https://stacks.math.columbia.edu/tag/00CM',
 ['Section 10.9, Definition 10.9.6 and the preceding construction: m/1=0 in S^-1 M exactly when sm=0 for some s in S.',
  'Lemma 10.9.7: universal property of module localization.'],
 first_circulation='Continuously maintained reference; precise original date of this elementary result not investigated. Consulted 2026-11-19.',
 opened_refs=['turn191591263search0','turn108393566view0'],limitations='Used only for the elementary localization criterion; not a theorem about motivic realizations.')

for q in R:
 if q['key']=='AchterCasalainaMartinVial2023':
  q['first_circulation']='arXivv1 2019-11-22; v2 2022-10-12; received2020-10-04, accepted2022-06-19, journal2023.'
  q['additional_urls']=['https://arxiv.org/abs/1911.09911']; q['opened_refs']+=['turn797786326view2','turn167079478view5']
  q['locators']+=['Proposition 8.2, pp. 119–120: for a surjective regular homomorphism and miniversal cycle of degree r, the induced Tate-module map is injective for i=1,2,dim X and primes l coprime to pr; it is an isomorphism in the endpoint cases if the quotient is the algebraic representative.']
  q['opened_refs']+=['turn898774666view1','turn191591263view0','turn191591263view1']
 if q['key']=='Kahn2021Regular': q['opened_refs']+=['turn797786326view3']
 if q['key']=='Voisin2025Universal0':
  q['locators']+=['§2 beforeLemma2.1: integral inverse AlbaneseH1 component is equivalent to an integral universal0cycle, with torsion-free homology conventions.', 'Lemma2.1 andfollowingparagraph: rational universal0cycle via a Jacobian splitting up to an integer; Proposition2.2 adds the torsion-free integral Künneth condition.']
  q['opened_refs']+=['turn302622132view0','turn661638085view2']
 if q['key']=='AchterCasalainaMartinVial2025':
  q['first_circulation']='arXiv v1 submitted 2020-07-15; author draft dated 2020-07-14; v2 submitted 2025-03-20; consulted author PDF dated 2025-03-19; published Astérisque 455 (2025).'
  q['additional_urls']=q.get('additional_urls',[])+['https://arxiv.org/abs/2007.07470']
  q['locators']+=['Theorem12.12, p53–54: precise threefold hypotheses and pure-inseparability/isomorphism conclusions; positivity is separatelyConjecture5.1.']
  q['opened_refs']+=['turn260045725view4','turn191591263view2']
 if q['key']=='Bass1967KTheory':
  q['locators']+=['Chapter 3, Corollary 2.12, p. 74: tensor product of finite-projective endomorphism algebras.', 'Chapter 3, Proposition 2.13, p. 75: End_k(P) is separable for finite projective P, with center k/ann(P); explicit matrix-unit separability element.']
  q['opened_refs']+=['turn898774666view0','turn172192899view0']
 if q['key']=='Milne2004Shimura': q['opened_refs']+=['turn898774666view2','turn172192899view2']
 if q['key']=='HuberMuellerStach2017':
  q['locators']+=['Conjecture 13.2.1 and Remark 13.2.2, printed p. 288: evaluation on formal periods is conjecturally injective over an algebraic extension of Q; Corollary 13.2.7, p. 289, gives conditional geometric connectedness.']
  q['opened_refs']+=['turn898774666view3','turn172192899view3','turn608916113view4']

(O/'references.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
fields=['author','title','year','journal','booktitle','series','volume','number','pages','publisher','doi','url','eprint','archiveprefix','note']
out=[]
for r in R:
    typ='article' if 'journal' in r else ('book' if r['key']=='HuberMuellerStach2017' else 'misc')
    out.append('@'+typ+'{'+r['key']+',\n'+',\n'.join('  '+k+' = {'+str(r[k]).replace('&','\\&')+'}' for k in fields if k in r)+'\n}')
(O/'references.bib').write_text('\n\n'.join(out)+'\n')
print(f'{len(R)} manually checked references written')
