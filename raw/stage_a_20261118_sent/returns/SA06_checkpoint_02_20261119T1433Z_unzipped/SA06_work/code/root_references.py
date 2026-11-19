#!/usr/bin/env python3
"""Bibliographic records authored from sources opened in this run."""
from pathlib import Path
import json
R=[]
def ref(key,author,title,year,url,locators,first,**kw):
 R.append(dict(key=key,author=author,title=title,year=str(year),url=url,locators=locators,first_circulation=first,note='verified',checked_date='2026-11-19',**kw))
ref('Oda1969','Oda, Tadao','The first de Rham cohomology group and Dieudonné modules',1969,'https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf',
 ['Definition3.1; Propositions3.22–3.24, pp99–101; Corollary5.11 and its remark, p131; bibliography[15], p134. Original p131 visually inspected.'],
 'Modified Harvard dissertation submitted June1967, stated in introduction; publication1969.',journal='Annales scientifiques de l’École Normale Supérieure',volume='2',number='1',pages='63--135',doi='10.24033/asens.1175',limitations='Perfect base field; the abelian-variety comparison identifies M(X[p]) with H1_dR. It does not compute the manuscript’s particular determinant-orientation class.')
ref('GrothBrauerII1966','Grothendieck, Alexander','Le groupe de Brauer: II. Théories cohomologiques',1966,'https://www.numdam.org/article/SB_1964-1966__9__287_0.pdf',
 ['Lemma1.1, Corollaries1.2–1.3, Proposition1.4, pp290–291; original formula pages visually inspected.'],
 'Bourbaki exposé297; seminar1965/66, volume1966. Exact lecture month not yet independently read.',series='Séminaire Bourbaki',number='297',pages='287--307',limitations='Cor1.3 assumes noetherian without embedded associated primes, or reduced qcqs with finitely many components. Prop1.4 additionally assumes strict henselian local factoriality; Hq(Gm) torsion only forq≥2.')
ref('Lang1956','Lang, Serge','Algebraic groups over finite fields',1956,'https://wstein.org/papers/bib/Lang-Algebraic_Groups_Over_Finite_Fields.pdf',
 ['Theorem1 and corollary; Theorem2, pp557–558, visually inspected; introductionp555.'],
 'Received1956-03-09, printed first page; publication1956. Earlier public circulation not established.',journal='American Journal of Mathematics',volume='78',number='3',pages='555--563',doi='10.2307/2372673',limitations='Connected algebraic groups over finite fields; gives existence/isomorphism classes of torsors, not a preferred point. Smooth henselian lifting and inverse limits are additional arguments.')
ref('Deuring1941','Deuring, Max','Die Typen der Multiplikatorenringe elliptischer Funktionenkörper',1941,'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1941.Deuring.pdf',
 ['Introduction§§2–3, pp198–200; quaternionic maximal-order and j-invariant classification.'],
 'Publication1941; earlier public circulation not established.',journal='Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg',volume='14',pages='197--272',limitations='Classical supersingular/maximal-order results, not an exact norm-rigidified gerbe construction matching every manuscript coherence datum.')
ref('Voight2021','Voight, John','Quaternion algebras',2021,'https://link.springer.com/chapter/10.1007/978-3-030-56694-4_18',
 ['Chapter18, Theorem18.3.4, Cor18.3.5, Eq18.3.8, Lemma18.4.4, Eq18.4.6/18.4.9, §18.4.7, Prop18.5.3 and Remark18.5.9.',
  'Chapter42, Theorem42.1.9; §42.2.4; Proposition42.4.8 and Corollary42.4.12.'],
 'Book2021; chapter first online2021-06-29. Earlier book drafts not used to claim priority.',publisher='Springer',doi='10.1007/978-3-030-56694-4',additional_urls=['https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42'],limitations='Exact quaternion/maximal-order hypotheses retained; abstract bimodule groups and principal one-sided ideal classes are distinguished.')
ref('Silverman2009','Silverman, Joseph H.','The arithmetic of elliptic curves',2009,'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/silverman.pdf',
 ['III Theorem10.1 and Corollary10.2, pp103–104; V§3 for supersingularity.'],
 'First edition1986; second edition2009; consulted PDF corrected second printing2016.',publisher='Springer',series='Graduate Texts in Mathematics',volume='106',doi='10.1007/978-0-387-09494-6',limitations='Automorphism orders4and6 are for characteristic≠2,3 over an algebraic closure.')
ref('StacksKummer','The Stacks Project Authors','Kummer theory, Lemma59.28.3, Tag040N',2026,'https://stacks.math.columbia.edu/tag/040N',
 ['Exact fppf Kummer sequence for every positive integern; checked current tag.'],
 'Continuously updated project; accessed2026-11-19. No priority date inferred.')
ref('StacksSmoothLift','The Stacks Project Authors','Lifting, Lemma15.9.14, Tag07M7',2026,'https://stacks.math.columbia.edu/tag/07M7',
 ['Lifts a point of a smooth A-algebra after an étale base change preserving A/I.'],
 'Continuously updated project; accessed2026-11-19.')
ref('StacksHenselian','The Stacks Project Authors','Henselian local rings, Lemma10.153.3, Tag04GE',2026,'https://stacks.math.columbia.edu/tag/04GE',
 ['Equivalent henselian conditions, especially(7)–(8) retractions of étale neighbourhoods with identical residue field.'],
 'Continuously updated project; accessed2026-11-19.')
ref('MilneCM2020','Milne, James S.','Complex multiplication',2020,'https://www.jmilne.org/math/CourseNotes/CM.pdf',
 ['Propositions1.36–1.39, pp20–21 in the file’s printed numbering: positive involutions and real/CM factor classification; §4.17–4.18 Serre condition.'],
 'v0.00 first posted2006-04-07; consulted v0.10 dated2020-07-14.',version='0.10',limitations='Positive involution allows totally real identity-involution factors as well as CM factors. A connected torus hypothesis is separate.')
ref('MilneAG2015','Milne, James S.','Algebraic groups: The theory of group schemes of finite type over a field',2015,'https://www.jmilne.org/math/CourseNotes/iAG200.pdf',
 ['Corollary14.42 p239: rational points of a torus over an infinite field are Zariski dense.',
 'Corollary27.56 p488: H1(k,G)=1 for connected group varieties over finite fields.',
 'Chapters12–14: character/diagonalizable-group dictionary; chapter25: split reductive groups and root data.'],
 'v1.00 posted2014-07-31; consulted v2.00 dated2015-12-20.',version='2.00',limitations='Density does not extend to arbitrary disconnected multiplicative-type groups; these are finite-type statements.')
ref('MilneCM1981','Milne, James S.','Abelian varieties with complex multiplication (for pedestrians)',1981,'https://www.jmilne.org/math/articles/1981dT.pdf',
 ['§4, pp9–12, Serre group character lattice and Lemma4.2 norm relation.'],
 'Disseminated September1981; author’s corrected and expanded text dated1998-06-07, explicitly stated on first page.',limitations='Provides a later comparison method, not an identification of the manuscript’s particular torus with the universal Serre group.')
ref('MilneGerbes2003','Milne, James S.','Gerbes and abelian motives',2003,'https://jmilne.org/math/articles/2003b.pdf',
 ['§6.1 conditional motivic interpretation; Theorem6.3 and Remark6.4, pp36–37, existence/uniqueness of pseudomotivic gerbe systems and weight-zero variant.'],
 'Consulted author version1.1 dated2003-02-21; original public circulation date not established.',journal='Moscow Mathematical Journal',volume='3',number='1',pages='125--157',limitations='The pseudomotivic gerbe theorem is unconditional as a specified gerbe problem; identifying it with all geometric motives retains Tate/Hodge hypotheses. It is not the exact integral Deuring orientation problem.')
ref('GrothDeRham1966','Grothendieck, Alexander','On the de Rham cohomology of algebraic varieties',1966,'https://www.numdam.org/article/PMIHES_1966__29__95_0.pdf',
 ['Theorem1 and variant1′, pp95–96; p102 discussion of p-kernel and Hodge exact sequences; footnote10 period relations; p103 footnotes12–13. Original pp102–103 visually inspected.'],
 'Letter to Atiyah dated1963-10-14; most editorial remarks November1963; received1965-07-05; footnote13 added July1965; publication1966. These dates were read on the original first and last pages.',journal='Publications Mathématiques de l’IHÉS',volume='29',pages='95--103',limitations='The period-conjecture footnote is distinct from the p-kernel comparison proved by Oda. Footnote12 retracts naive characteristic-p dimension/base-change hopes.')
ref('SGA4VII1972','Grothendieck, Alexander','Site et topos étales d’un schéma (Exposé VII)',1972,'https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/originaux/SGA4-VIIo.pdf',
 ['§4 Proposition4.1, original exposé pp11–12 (folio352–353): fully faithful small-to-big étale pullback and cohomology comparison.'],
 'Seminar1963–1964; SGA4 tome2 publication1972. Original draft numbering differs from the later edited references.',booktitle='Théorie des topos et cohomologie étale des schémas',series='Lecture Notes in Mathematics',volume='270',publisher='Springer',limitations='Both sites carry the étale topology. This is not a blanket comparison of étale with fppf/fpqc cohomology.')
ref('SGA4XVIII1973','Deligne, Pierre, d’après Alexander Grothendieck','La formule de dualité globale (Exposé XVIII)',1973,'https://publications.ias.edu/deligne/paper/350',
 ['§1.4.11 two-term complex construction; Lemma1.4.13 and Proposition1.4.15 Picard-stack/derived-complex equivalence; §1.4.21 torsors.'],
 'SGA4 seminar1963–1964; tome3 publication1973; exact circulation date of this edited exposé not established.',booktitle='Théorie des topos et cohomologie étale des schémas',series='Lecture Notes in Mathematics',volume='305',pages='481--587',publisher='Springer',additional_urls=['https://publications.ias.edu/sites/default/files/Number4.pdf','https://grothendiecksga.com/read/sga4/fr/XVIII-1.html'],limitations='Strictly commutative Picard stacks and additive functors; a monoidal functor need not preserve a chosen symmetry unless required.')
ref('Humphreys1990','Humphreys, James E.','Reflection groups and Coxeter groups',1990,'https://sites.math.washington.edu/~billey/classes/reflection.groups/references/Humphreys.ReflectionGroupsAndCoxeterGroups.pdf',
 ['§2.12 exceptional Weyl groups; §2.11 orders; §2.5 Cartan determinants.'],
 'Publication1990; historical references there to Bourbaki VI exercises pp228–229 and the classical finite groups.',publisher='Cambridge University Press',series='Cambridge Studies in Advanced Mathematics',volume='29',limitations='Group-symbol conventions differ: the simple order25920 group is the derived/spinor kernel, not the full order51840 determinant-one orthogonal group in the manuscript convention.')
ref('GrothBibliography','Grothendieck Circle','Bibliographie d’Alexander Grothendieck','n.d.','https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG-bibliotex.pdf',
 ['Entries for BrauerII, deRham1966, standard conjectures1969 and Hodge general conjecture1969.'],
 'Accessed2026-11-19; no creation date asserted.',limitations='Used only to trace publications backward, not as proof of any mathematical claim.')

ref('GrothHodge1969','Grothendieck, Alexander',"Hodge’s general conjecture is false for trivial reasons",1969,'https://matematicas.unex.es/~navarro/res/articles/Hodge%27s%20Conjecture%20is%20False.pdf',
 ['§1 pp299–300 cubic elliptic-period counterexample; §2 pp300–301 corrected maximal rational sub-Hodge structure and motivic effectivity; §3 special cases.'],
 'Received27October1968; additionApril1969; publication1969. No earlier circulation date established.',journal='Topology',volume='8',pages='299--303',doi='10.1016/0040-9383(69)90016-0',limitations='Refutes the naive generalized Hodge filtration equality, not the usual rational Hodge conjecture. The real-base restriction-of-scalars variant is this run’s reconstruction.')
ref('BostCharles2016','Bost, Jean-Benoît and Charles, François','Some remarks concerning the Grothendieck period conjecture',2016,'https://www.math.ens.psl.eu/~charles/crelle-periods.pdf',
 ['§1.1 comparison and cycle classes; §2.1 integral/rational deRham–Betti categories; Conjecture2.12 and Proposition2.13 distinguish period torsor and cycle fullness.'],
 'arXiv1307.1045 first3July2013, revised9April2014; publisher online30April2014; volume714 publication2016.',journal='Journal für die reine und angewandte Mathematik',volume='714',pages='175--208',doi='10.1515/crelle-2014-0025',limitations='The integral Betti component of the defined category is finite free. General integral cohomology may contain torsion. The full transcendence statement is conjectural; special GPC results are not its general proof.')
ref('SGA1V1971','Grothendieck, Alexander','Le groupe fondamental: généralités (SGA1, ExposéV)',1971,'https://arxiv.org/pdf/math/0206203',
 ['Theorem4.1; Proposition5.6 and Corollary5.7; §7 geometric points and paths; reedition pp104,106–107,115–116 (original marginal pp126–130,140–142).'],
 'Seminar1960–1961, mimeographed distribution described in introduction; LNM224 publication1971; recomposed SMF edition2003, arXiv first20June2002, v2 4January2004.',booktitle='Revêtements étales et groupe fondamental',publisher='Springer / Société mathématique de France',limitations='The consulted §7 assumes a connected locally noetherian scheme. Fibre functors are isomorphic noncanonically; their isomorphisms form a groupoid/path torsor.')
ref('SGA4XVI1973','Artin, Michael','Théorème de changement de base par un morphisme lisse, et applications (SGA4, ExposéXVI)',1973,'https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf',
 ['Theorem4.1, original pp232–233, reedition p149/PDF156, finite-type complex schemes and torsion comparison; proper morphism or constructible coefficient condition.'],
 'Seminar1963–1964; original LNM305 publication1973; consulted electronic recomposition retains original marginal page numbers.',booktitle='Théorie des topos et cohomologie étale des schémas, tome3',series='Lecture Notes in Mathematics',volume='305',publisher='Springer',limitations='The theorem is stated for torsion coefficients; integral ℓ-adic comparison requires the compatible inverse system, not an assertion that all integral cohomology is free.')
ref('Humphreys1972','Humphreys, James E.','Introduction to Lie algebras and representation theory',1972,'https://www.math.uci.edu/~brusso/humphreys.pdf',
 ['§6.3 p28 Weyl complete reducibility; §7.2 pp32–33 divided-power recurrence; §§8.1–8.5 pp35–40 root/Killing properties; §§15.1–15.4 pp78–81 generalized weights and Cartan subalgebras; §16.2–16.4 pp82–85 conjugacy. Selected published pages rendered and OCR read.'],
 'Book copyright1972; Springer print release23January1973. Classical results predate this modern exposition; no precise earliest historical attribution is inferred here.',publisher='Springer',series='Graduate Texts in Mathematics',volume='9',doi='10.1007/978-1-4612-6398-2',limitations='Generally algebraically closed characteristic0; §15 explicitly allows arbitrary characteristic for specified existence/Engel statements. The manuscript’s missing draft-relative hypotheses are not reconstructed from this book.')
ref('BourbakiLie1975','Bourbaki, Nicolas','Groupes et algèbres de Lie, chapitres7 et8',1975,'https://link.springer.com/book/10.1007/978-3-540-33977-9',
 ['Publisher metadata verifies originalMasson1975 and later reprint; opened English contents givesVII§§1–3 andVIII§§1–3,11–12 subject locations. Full theorem bodies were not accessible here; mathematical checks instead use Humphreys1972 and explicit proofs.'],
 'OriginalFrench chaptersVII–VIII published1975; French reprint2006/ebook2007. EnglishVII–IX contents is a later translation, not evidence of a manuscript date.',publisher='Masson',additional_urls=['https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Bourbaki%20-%20Lie%20groups%20and%20Lie%20algebras.%20Chapters%207-9.pdf'],limitations='Verified only as publication/contents comparison. Never used as an independently checked theorem text or identification of the manuscript’s editorial numbers.')

if __name__=='__main__':
 d=Path(__file__).resolve().parents[1]/'parts/root';(d/'references.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n');print({'verified_reference_records':len(R)})
