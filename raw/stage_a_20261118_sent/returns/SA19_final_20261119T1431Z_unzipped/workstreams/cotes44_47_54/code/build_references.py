"""Hand-checked bibliography. 'verified' concerns an opened URL, not a proof."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
R=[]
def ref(key,typ,author,title,year,url,locator,**kw):
    row=dict(key=key,type=typ,author=author,title=title,year=str(year),url=url,
             note=kw.pop('note','verified'),annote=locator,urldate='2026-11-19')
    row.update(kw);R.append(row)

ref('Mukai1981','article','Mukai, Shigeru','Duality between D(X) and D(X-hat) with its application to Picard sheaves',1981,
 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf',
 'Primary full article opened. Theorem2.2; formulas3.1,3.4,3.7,3.8; Proposition3.11. Receipt9October1979 is documented; no earlier public circulation inferred.',
 journal='Nagoya Mathematical Journal',volume='81',pages='153--175',doi='10.1017/S002776300001922X')
ref('Laumon1996','misc','Laumon, Gérard','Transformation de Fourier généralisée',1996,
 'https://arxiv.org/abs/alg-geom/9603004',
 'Primary PDF opened. Based on IHES preprintSeptember1985; arXiv5March1996. Lemmas1.1.3,1.2.5; Theorem1.2.4; Propositions1.3.1,1.3.4; Corollary1.3.3; section2.2. Locally noetherian base retained.',
 eprint='alg-geom/9603004',archivePrefix='arXiv')
ref('Mumford1970','book','Mumford, David','Abelian varieties',1970,
 'https://djvu.online/file/2tC7xp3dbqGCh',
 'Primary book reproduction opened and section8(vii), p76 checked. Book first publication1970; the accessible reproduction edition is not inferred from its URL. The source manuscript explicitly admits and attributes the vanishing lemma.',
 publisher='Oxford University Press for the Tata Institute of Fundamental Research')
ref('Beauville1983','incollection','Beauville, Arnaud','Quelques remarques sur la transformation de Fourier dans l’anneau de Chow d’une variété abélienne',1983,
 'https://math.univ-cotedazur.fr/u/beauvill/pubs/fourier.pdf',
 'Author-hosted full text opened. Proposition3,p243 and Proposition3-prime,p245. ConferenceTokyo/Kyoto1982, publication1983. Opened text works with complex abelian varieties.',
 booktitle='Algebraic geometry, Tokyo/Kyoto1982',series='Lecture Notes in Mathematics',volume='1016',pages='238--260',doi='10.1007/BFb0099965',publisher='Springer')
ref('Kleiman1968','incollection','Kleiman, Steven L.','Algebraic cycles and the Weil conjectures',1968,
 'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf',
 'Primary scan opened. Lemma2A12 and Remark2A13,pp377--378. The first product direction has no sign; the alleged erroneous converse formula was not found there.',
 booktitle='Dix exposés sur la cohomologie des schémas',pages='359--386',publisher='North-Holland and Masson')
ref('Moonen2026','article','Moonen, Ben','A remark on the paper of Deninger and Murre',2026,
 'https://www.math.ru.nl/~bmoonen/Papers/RPDM.pdf',
 'Author-hosted full text and arXiv2407.05837 opened. First8July2024, online2024, final volumeJanuary2026. Corollary2.7(1) proves Todd(H1dR)=1 under section2.1 hypotheses; polarization assumption belongs to the stronger Chern-class conclusion.',
 journal='Indagationes Mathematicae',volume='37',number='1',pages='149--157',doi='10.1016/j.indag.2024.07.010')
ref('HasanEtAl2025','article','Hasan, Junaid and Hassan, Hazem and Lin, Milton and Manivel, Marcella and McBeath, Lily and Moonen, Ben','Integral aspects of Fourier duality for abelian varieties',2025,
 'https://arxiv.org/abs/2407.06184',
 'Primary PDF and author publication list opened. First8July2024. Section3.2 retains smooth quasi-projective base and characteristic-zero/liftability/base-change hypotheses; section5 uses coefficients Z[1/(2g+d+1)!].',
 journal='Manuscripta Mathematica',volume='176',pages='article64',doi='10.1007/s00229-025-01662-7')
ref('BeckmannDeGaay2023','article','Beckmann, Thorsten and de Gaay Fortman, Olivier','Integral Fourier transforms and the integral Hodge conjecture for one-cycles on abelian varieties',2023,
 'https://arxiv.org/abs/2202.05230',
 'Primary PDF opened. First10February2022; revised8February2023. Theorem3.8 and Question3.9, with principally polarized/symmetric ample representative restrictions for the stronger equivalences.',
 journal='Compositio Mathematica',volume='159',number='6',pages='1188--1213',doi='10.1112/S0010437X23007133')
ref('Coleman1998','article','Coleman, Robert F.','Duality for the de Rham cohomology of an abelian scheme',1998,
 'https://www.numdam.org/item/10.5802/aif.1659.pdf',
 'Primary full text opened. Theorem1.1, Theorem2.2(i), section4. Reduced or Z-flat base assumption retained; V(M)=SpecSymM is contravariant.',
 journal='Annales de l’Institut Fourier',volume='48',number='5',pages='1379--1393',doi='10.5802/aif.1659')
ref('Oda1969','article','Oda, Tadao','The first de Rham cohomology group and Dieudonné modules',1969,
 'https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf',
 'Primary full text opened. Harvard dissertationJune1967 noted onp63. Definition3.5,p82; Proposition3.13,p86; Theorem3.19,p89; Corollary5.11,p131. Semilinear F/V and perfect-field hypotheses preserved. Corollary5.2 is degeneration for curves, not by itself the full Jacobian de Rham pullback theorem.',
 journal='Annales scientifiques de l’École Normale Supérieure',series='4',volume='2',number='1',pages='63--135',doi='10.24033/asens.1175')
ref('Gabriel1970','incollection','Gabriel, Pierre','Étude infinitésimale des schémas en groupes. B) Groupes formels',1970,
 'https://wstein.org/sga/SGA3/Exp7B-20jan2010.pdf',
 'Opened recomposition20January2010 of SGA3 ExposéVIIB. Theorem4.4 and Corollary4.4.1, original marginpp548--549, recomposedp493. Original publication1970; no date assigned to the reused manuscript.',
 booktitle='Schémas en groupes I, SGA3',editor='Demazure, Michel and Grothendieck, Alexander',series='Lecture Notes in Mathematics',volume='151',publisher='Springer')
ref('SGA3XXI','incollection','Demazure, Michel','Données radicielles',1970,
 'https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExpo21.pdf',
 'Primary ExposéXXI opened. Definition1.1.1, Lemma1.1.9, Corollary1.1.11, section1.2 and section3. Integral perfect duality in the standard datum is stronger than rational perfect pairing on the canceled source sheet.',
 booktitle='Schémas en groupes III, SGA3',series='Lecture Notes in Mathematics',volume='153',publisher='Springer')
ref('EGAIV2','article','Grothendieck, Alexander','Éléments de géométrie algébrique IV. Étude locale des schémas et des morphismes de schémas, seconde partie',1965,
 'https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf',
 'Complete primary PDF downloaded after web parser size limit, parsed with pdftotext; hash retained in research/EGAIV2_extract.json. Theorem6.9.1 and Lemma6.9.2,pp153--154, read. Domain/noetherian generic freeness is a predecessor, not the exact nonreduced corollary.',
 journal='Publications Mathématiques de l’IHÉS',volume='24',pages='5--231',doi='10.1007/BF02684322')
ref('EGAIV3','article','Grothendieck, Alexander','Éléments de géométrie algébrique IV. Étude locale des schémas et des morphismes de schémas, troisième partie',1966,
 'https://www.numdam.org/item/PMIHES_1966__28__5_0/',
 'Primary full PDF downloaded and exact statements/proofs read; hashes and selected extraction in research. Lemma8.9.4.1,p35; Theorem11.4.1,pp143--145; Corollary11.4.4,pp145--146; Proposition11.4.5,pp146--147; Corollary11.4.6,p147; Proposition11.4.7,p147. Numdam receipt15November1964; publication1966. No date inferred for the manuscript sheet.',
 journal='Publications Mathématiques de l’IHÉS',volume='28',pages='5--255',doi='10.1007/BF02684343')
ref('Grothendieck1962Picard','incollection','Grothendieck, Alexander','Technique de descente et théorèmes d’existence en géométrie algébrique. VI. Les schémas de Picard: propriétés générales',1962,
 'https://www.numdam.org/item/SB_1961-1962__7__221_0.pdf',
 'Primary text opened. FGA VI, section4,p242 records Matsusaka’s numerical-versus-torsion algebraic criterion for divisors. Exposé236,May1962.',
 booktitle='Séminaire Bourbaki1961--1962',number='236',pages='221--243')
ref('Grothendieck1964Letter','misc','Grothendieck, Alexander','Letter to Jean-Pierre Serre, Bures,12August1964',1964,
 'https://csg.igrothendieck.org/wp-content/uploads/2024/04/L23d.pdf',
 'External transcription published by the Cercle Sofia Kovalevskaïa in April2024 opened. The letter itself is unpublished1964 correspondence. Confirms date and n+1-i complement; not a substitute for the absent archive scan.',
 howpublished='Correspondence transcription, Cercle Sofia Kovalevskaïa')
ref('Saito1979','article','Saito, Hiroshi','Abelian varieties attached to cycles of intermediate dimension',1979,
 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8BE754AE13330E3050F3588FCD123D87/S0027763000024855a.pdf/abelian_varieties_attached_to_cycles_of_intermediate_dimension.pdf',
 'Primary full article opened. Definition3.1,pp108--109; Proposition3.4,p110 explicitly credits Grothendieck; Theorem3.6,pp110--111; Proposition4.4,pp112--113; Propositions5.2--5.3,pp115--116. Receipt17July1978, publicationSeptember1979. Picard/incidence quotient differs from arbitrary universal regular representative.',
 journal='Nagoya Mathematical Journal',volume='75',pages='95--119',doi='10.1017/S0027763000024855')
ref('Kleiman1971ICM','incollection','Kleiman, Steven L.','Finiteness theorems for algebraic cycles',1971,
 'https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.1/ICM1970.1.ocr.pdf',
 'Primary ICM volume downloaded and articlepp445--449 read. Pp446--447 explicitly mention an unrecorded1964 observation of Grothendieck; footnotes5--6 specify isogeny duality and torsion equivalence. Conference1970, printed1971. Bibliography misdates Lieberman Higher Picard varieties as1969; not propagated.',
 booktitle='Actes du Congrès International des Mathématiciens, Nice1970',volume='1',pages='445--449')
ref('ACMV2023','article','Achter, Jeffrey D. and Casalaina-Martin, Sebastian and Vial, Charles','A functorial approach to regular homomorphisms',2023,
 'https://api.algebraicgeometry.nl/Article/19846/2023-1-003.pdf',
 'Primary full article and arXiv1911.09911 opened. First22November2019, revised12October2022. Example1.14; Theorem8.1; Proposition8.2,p120, including i=1,2,d, excluded primes and target modulo torsion.',
 journal='Algebraic Geometry',volume='10',number='1',pages='87--129',doi='10.14231/AG-2023-003')
ref('ACMV2026Twist','misc','Achter, Jeffrey D. and Casalaina-Martin, Sebastian and Vial, Charles','Regular homomorphisms, with a twist',2026,
 'https://arxiv.org/abs/2506.17033',
 'Bibliographic and abstract scope verified, not a full theorem proof. First20June2025, revised5August2026; to appear in La Matematica as recorded there. Torsor attached to a given regular homomorphism does not supply arbitrary-codimension universal existence.',
 eprint='2506.17033',archivePrefix='arXiv')
ref('Kahn2021','article','Kahn, Bruno','On the universal regular homomorphism in codimension2',2021,
 'https://www.numdam.org/item/10.5802/aif.3408.pdf',
 'Primary full article and arXiv2007.07592 opened. Based on letter to Murre5December2018, firstarXiv15July2020, publication2021. Theorem0.1 and the exact gap in the codimension-two regular-representative argument checked.',
 journal='Annales de l’Institut Fourier',volume='71',number='2',pages='843--848',doi='10.5802/aif.3408')
ref('OttemSuzuki2020','article','Ottem, John Christian and Suzuki, Fumiaki','A pencil of Enriques surfaces with non-algebraic integral Hodge classes',2020,
 'https://arxiv.org/abs/1906.08994',
 'Primary PDF opened. First21June2019, revised19February2020. Corollary4.2: codimension-three Abel–Jacobi nonuniversality on a specific complex fourfold; not failure of existence of every algebraic representative.',
 journal='Mathematische Annalen',volume='377',pages='183--197',doi='10.1007/s00208-020-01969-8')
ref('Peters2026','misc','Peters, Chris','Incidence equivalence, a survey',2026,
 'https://arxiv.org/abs/2607.22233',
 'Primary PDF opened. First24July2026. Lemma5.4(2), Theorem5.8, Criterion7.3, Corollaries7.8--7.9. Conditional primitive-algebraicity comparisons; no universal integral positivity theorem. Its discussion of a Murre incidence proof gap is distinct from Kahn’s regular-representative gap.',
 eprint='2607.22233',archivePrefix='arXiv')
ref('CaibarClemensWithdrawn','misc','Caibar, Mirel and Clemens, C. Herbert','Incidence and Abel–Jacobi equivalence',2013,
 'https://arxiv.org/abs/1109.2932',
 'Withdrawal metadata verified. First13September2011; finalv9withdrawn19February2013 because of an error in the last theorem’s statement. Not treated as an established solution.',
 eprint='1109.2932',archivePrefix='arXiv')
ref('HernandezPelaez2026','article','Hernández, Iván and Pelaez, Pablo','Regular homomorphisms and mixed motives',2026,
 'https://arxiv.org/abs/2509.15920',
 'Primary PDF opened. First19September2025. Theorems3.2.28 and4.1.13 describe kernels of given regular homomorphisms and Samuel abelian equivalence using motives. They do not construct universal abelian representatives in every codimension.',
 journal='Algebra i Analiz',volume='38',number='1',pages='247--268')
ref('Kunnemann2001','article','Künnemann, Klaus','Height pairings for algebraic cycles on abelian varieties',2001,
 'https://www.numdam.org/article/ASENS_2001_4_34_4_503_0.pdf',
 'Primary full article opened. Theorem1.6 provides the model input; Corollary1.7 gives canonical higher-cycle heights for abelian varieties over number fields. This is not the manuscript’s arbitrary generic-pencil theorem.',
 journal='Annales scientifiques de l’École Normale Supérieure',series='4',volume='34',number='4',pages='503--523',doi='10.1016/S0012-9593(01)01068-0')
ref('Ulmer2014','incollection','Ulmer, Douglas','Curves and Jacobians over function fields',2014,
 'https://arxiv.org/abs/1203.5573',
 'Primary PDF, author bibliography and author errata opened. First26March2012; revised28October2012; publication2014. Section4.3,Proposition4.3.1 in preprint. Geometric negative intersection of corrected lifts; finite-field arithmetic factorlogq. Printed startpage281 follows errata; author list alternatively says283.',
 booktitle='Arithmetic geometry over global function fields',pages='281--337',publisher='Birkhäuser')
ref('UlmerErrata','misc','Ulmer, Douglas','Errata to Curves and Jacobians over function fields','n.d.',
 'https://dlulmer.github.io/research/papers/2014b-correction.pdf',
 'Author-posted correction opened. General-ground-field finite-cokernel claim not proved as originally stated; finitely generated or algebraically closed cases retained. No uncorrected arbitrary-field assertion is used.')
ref('Clemens1983','article','Clemens, C. Herbert','Homological equivalence, modulo algebraic equivalence, is not finitely generated',1983,
 'https://www.numdam.org/item/PMIHES_1983__58__19_0.pdf',
 'Primary full article opened. Theorem0.2 and formula0.1 for a very general smooth complex quintic threefold. This is used as a theorem input, not independently re-proved; implication to numerical versus torsion-algebraic equivalence checked separately.',
 journal='Publications Mathématiques de l’IHÉS',volume='58',pages='19--38',doi='10.1007/BF02953771')
ref('Matsusaka1957','article','Matsusaka, Teruhisa','The criteria for algebraic equivalence and the torsion group',1957,
 'https://www.jstor.org/stable/i316383',
 'Bibliographic verification only: opened primary journal issue lists title,author,pp53--66 and DOI. The article page does not expose theorem text. The exact divisor result is instead checked in Grothendieck1962Picard section4,p242.',
 journal='American Journal of Mathematics',volume='79',number='1',pages='53--66',doi='10.2307/2372383')
ref('Lieberman1972','incollection','Lieberman, David I.','Intermediate Jacobians',1972,
 'https://zbmath.org/?q=an:0249.14015',
 'Unverified original: direct zbMATH opening failed; bibliographic identity is corroborated by opened Saito1979 and Peters2026 references and primary-paper backward citations. No theorem is claimed checked in the original chapter. Oslo conference1970, publication1972.',
 booktitle='Algebraic geometry, Oslo1970',editor='Oort, Frans',pages='125--139',publisher='Wolters-Noordhoff',note='unverified')
ref('MoonenAVDuality','misc','van der Geer, Gerard and Moonen, Ben','Abelian varieties, preliminary version: ChapterVII, Duality','n.d.',
 'https://www.math.ru.nl/~bmoonen/BookAV/DualAV2.pdf',
 'Primary chapter opened; section7.18 and Exercise7.5 checked. FrontMatter.pdf separately opened and confirms these two named authors; later project history is not used to change this titlepage. Chapter is a draft, not assigned a publication year.')

tags={
 '0DJT':'Lemma36.35.10: perfect pushforward and arbitrary base change',
 '0FYP':'Section57.8: Fourier–Mukai functors',
 '0G99':'Recognizing perfect complexes by fibres',
 '0621':'Koszul complexes',
 '02UM':'Chern character',
 '02UN':'Todd classes',
 '02UO':'Grothendieck–Riemann–Roch',
 '0BRT':'Smooth proper duality',
 '051R':'Lemma10.118.1: generic freeness over a noetherian domain',
 '05P7':'Definition38.21.3: flattening stratification',
 '00MB':'Lemma10.97.2: completion for noetherian rings',
 '00MC':'Lemma10.97.3: faithful completion and the Jacobson radical'}
for tag,title in tags.items():
    ref('Stacks'+tag,'misc','{The Stacks Project Authors}',title,2026,
        'https://stacks.math.columbia.edu/tag/'+tag,
        'Official tag opened and hypotheses checked. Dynamic numbering is reported at access19November2026. Tag05P7 is only a definition and is not used as an existence theorem.' if tag=='05P7' else
        'Official tag opened; exact hypothesis and role recorded in the claim audit. Access19November2026; current statement not backdated to the manuscript.')

def bibvalue(x):
    return str(x).replace('{','\\{').replace('}','\\}') if x!='{The Stacks Project Authors}' else x
lines=[]
for r in R:
    lines.append('@'+r['type']+'{'+r['key']+',')
    for k,v in r.items():
        if k in ('key','type'):continue
        lines.append('  '+k+' = {'+bibvalue(v)+'},')
    lines.append('}\n')
(ROOT/'references.bib').write_text('\n'.join(lines),encoding='utf-8')
(ROOT/'research/reference_audit.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print('References:',len(R))
print('Verified URL records:',sum(r['note']=='verified' for r in R))
print('Unverified originals:',[r['key'] for r in R if r['note']!='verified'])
print('Verification level is explicit in every annote; an opened metadata page is not a theorem proof.')
