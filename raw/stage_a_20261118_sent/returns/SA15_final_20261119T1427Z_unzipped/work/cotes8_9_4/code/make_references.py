"""Serialize only opened references, with explicit limits on what was read."""
from pathlib import Path
import json
W=Path(__file__).resolve().parents[1]
refs=[]
def r(key,typ,fields,locator,result,scope,ref,status='text read at stated locator',dates=''):
    fields['note']='verified'
    refs.append(dict(key=key,type=typ,fields=fields,locator=locator,result=result,scope=scope,web_ref=ref,read_status=status,dates=dates,checked='2026-11-19'))
r('BerghRydh2019','misc',dict(author='Daniel Bergh and David Rydh',title='Functorial destackification and weak factorization of orbifolds',year='2019',url='https://davidrydh.se/papers/destackification20190502.pdf'),
 'AppendixB, PropositionB.4, printed33–34; B.6–B.7, printed34–35',
 'Derived character formula for co-Lie complex; proof uses arbitrary locally constant character sheaves. Equal elementary divisors permit equivariantTor0/Tor1 identification; mixed divisors can fail.',
 'Matches cote8 formula. The manuscript locally freeZ/n case satisfies the relevant equality restriction. Author version used; publication metadata not asserted.','turn494048218view2',dates='Author PDF2May2019.')
r('Illusie1972','incollection',dict(author='Luc Illusie',title='Cotangent complex and deformations of torsors and group schemes',booktitle='Toposes, Algebraic Geometry and Logic',series='Lecture Notes in Mathematics',volume='274',pages='159--189',year='1972',publisher='Springer',url='https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/ce/24/ce243c31-2953-498e-92cb-c8b2e70d207d/i_illusie-64.pdf'),
 'Propositions1.3.3,1.5.1; Theorem1.7; §§3–4',
 'Cotangent deformation classes in Ext; co-Lie and torsor framework.',
 'Broad obstruction framework, not a read proof of every module-lifting identification in LNM239.','turn780286101view2',dates='HalifaxlectureJanuary1971; thesisdefense21May1971; prefacedOctober1972 and published1972.')
r('IllusiePisa2015','incollection',dict(author='Luc Illusie',title='Grothendieck at Pisa: crystals and Barsotti--Tate groups',booktitle='Colloquium De Giorgi 2013 and 2014',editor='Umberto Zannier',pages='79--107',year='2015',publisher='Edizioni della Normale',url='https://www.imo.universite-paris-saclay.fr/~luc.illusie/Illusie-Pisa5.pdf'),
 '§2.3.1; §3.2; §4.2.1; discussion of letter6.7 atPDFp15',
 'Tate full faithfulness, equal-characteristic extension, formally smooth BT deformations, and historical route to crystalline Dieudonné theory.',
 'Historical exposition by a participant; exact references distinguished from proofs. Says extension-deformation part of Grothendieck’s letter was not discussed in two later accounts, not why it was abandoned.','turn447878462view0',dates='Book2015; exact historical dates given only where checked.')
r('Singla2010','phdthesis',dict(author='Pooja Singla',title='Representations and Conjugacy Classes of General Linear Groups over Principal Ideal Local Rings of Length Two',school='Homi Bhabha National Institute',year='2010',month='January',url='https://www.imsc.res.in/xmlui/bitstream/handle/123456789/198/HBNI%20Th21PoojaSingla.pdf?isAllowed=y&sequence=1'),
 'Introduction printedp3/PDFp16; bibliography Sah and Ginosar',
 'Records the complete splitting exception list forGL_d(Z/p²)→GL_d(Fp).',
 'Exact theorem statement read; classification proof cited backwards, not independently read in the original Sah article.','turn674268119view3',dates='January2010.')
r('Ginosar2001','article',dict(author='Yuval Ginosar',title='On splitting of the canonical map: mod(p): GL(n,(p)) to GL(n,p)',journal='Communications in Algebra',volume='29',number='12',pages='5879--5881',year='2001',doi='10.1081/AGB-100107963',url='https://cris.haifa.ac.il/en/publications/on-splitting-of-the-canonical-map-modp-gln-p-gln-p/'),
 'Institutional publication record', 'Bibliographic identity and DOI verified.',
 'Publisher full text returned403. Mathematical classification used through Singla, not this metadata record.','turn240213277view2',status='metadata only')
r('Oda1969','article',dict(author='Tadao Oda',title='The first de Rham cohomology group and Dieudonn\'e modules',journal='Annales scientifiques de l\'École Normale Supérieure',series='4',volume='2',number='1',pages='63--135',year='1969',doi='10.24033/asens.1175',url='https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf'),
 'Theorem1.1; Proposition3.18 and Theorem3.19, p89; Corollary5.11,p131',
 'Cartier/Dieudonné duality and H¹deRham realization preserving F,V and the Hodge subspace.',
 'Does not resolve manuscript truncation indices, cancellation marks or its later determinant normalization.','turn619807611view1',dates='Based on Harvard dissertationJune1967; published1969.')
r('BerthelotMessing1979','incollection',dict(author='Pierre Berthelot and William Messing',title='Théorie de Dieudonné cristalline I',booktitle='Journées de géométrie algébrique de Rennes',series='Astérisque',volume='63',pages='17--38',year='1979',url='https://www.numdam.org/item/AST_1979__63__17_0.pdf'),
 '§2, Theorem2; §5.1 formulas(5.1)–(5.3); §5.2,Theorem5 andCorollary2',
 'Crystalline Dieudonné formalism over more general bases.',
 'Locally free crystalline realization and duality results were read; they do not resolve the manuscript’s finite truncation index or cancellation discrepancy.','turn331030471view0',dates='Rennes1978meeting; publication1979.')
r('Katz1981','incollection',dict(author='Nicholas M. Katz',title='Serre--Tate local moduli',booktitle='Surfaces algébriques',series='Lecture Notes in Mathematics',volume='868',pages='138--202',year='1981',publisher='Springer',url='https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf'),
 'Theorem1.2.1,pp143–144; Theorem2.1,pp148–149; §§3.7,4.3,6',
 'Deformation equivalence with p-divisible groups and ordinary bilinear formal multiplicative parameters.',
 'Exact local ordinary extension question answered. Global arbitrary-base classification and manuscript determinant normalization are not asserted here.','turn941980207view1',dates='Published1981; earlier Serre–Tate history is stated in the introduction, with no precise first manuscript date certified here.')
r('DembeleFreitasVoight2025','misc',dict(author='Lassina Dembélé and Nuno Freitas and John Voight',title='On Galois inertial types of elliptic curves over Qp',year='2025',url='https://jvoight.github.io/articles/inertial-types-042325.pdf'),
 '§3.2; Lemma3.2.1; Proposition4.2.1 and Table1',
 'Finite potentially-good elliptic inertia and its cyclic types forp≥5.',
 'Corroborates order3 monodromy and distinguishes finite inertial type. Does not contain the specific constant-E[5] counterexample proved in this run.','turn221955421view0',dates='Author version23April2025; publication date not asserted.')
r('Caraiani2017','misc',dict(author='Ana Caraiani',title='Perfectoid Shimura varieties',year='2017',url='https://www.ma.imperial.ac.uk/~acaraian/papers/arizona_notes.pdf'),
 '§4.1, Definition4.1.5 and Lemma4.1.7,pp28–29',
 'The Hasse determinant is invertible exactly on the ordinary locus; geometric points enter the definition.',
 'General abelian-scheme Hasse invariant statement, despite the larger Shimura-variety subject.','turn898518145view5',dates='Expanded2017ArizonaWinterSchool notes; later revision date not specified.')
r('Milne2008','misc',dict(author='James S. Milne',title='Abelian Varieties, version2.00',year='2008',url='https://www.jmilne.org/math/CourseNotes/AV.pdf'),
 'I§10, Proposition10.13; Theorem11.1; §13; Proposition14.2 and Theorem14.3',
 'Polynomial degree, square degree of a line-bundle homomorphism, duality and Rosati positivity.',
 'Standard ingredients only. This source does not prove the exact unpolarized ordinary determinant normalization sought in cote9.','turn494048218view1',dates='Version2March2008; first webversionJuly1998.')
r('Illusie1976','incollection',dict(author='Luc Illusie',title='Cohomologie cristalline [d\'après P. Berthelot]',booktitle='Séminaire Bourbaki 1974/1975',number='456',series='Lecture Notes in Mathematics',volume='514',pages='53--60',year='1976',url='https://www.numdam.org/item/SB_1974-1975__17__53_0.pdf'),
 '§§2.1–2.6, printedpp55–56; especially2.2 and2.5',
 'Universal coefficients, Poincaré/Gysin formalism, and Katz–Messing comparison for smooth projective varieties over finite fields.',
 'Primary contemporaneous exposition without proofs. Scope in2.5 is projective; no broader smooth-proper extension is inferred from it.','turn485449693view0',dates='LectureNovember1974; published1976.')
r('BMS2016','misc',dict(author='Bhargav Bhatt and Matthew Morrow and Peter Scholze',title='Integral p-adic Hodge theory',year='2016',eprint='1602.03148',archivePrefix='arXiv',url='https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/BMS16.pdf'),
 'Theorem1.1; §2.3, Theorem2.10; Lemma2.12,printedp17',
 'Torsion-length comparison can be strict; sufficiently high ample powers satisfy integral weak Lefschetz.',
 'Does not give arbitrary-degree integral saturation, equality of torsion groups, or the exact stable-F lifting criterion.','turn780286101view0',dates='FirstarXiv9February2016 verified at https://arxiv.org/abs/1602.03148; published2018 (parent has full journal verification).')
r('KatzMessing1974','article',dict(author='Nicholas M. Katz and William Messing',title='Some consequences of the Riemann hypothesis for varieties over finite fields',journal='Inventiones mathematicae',volume='23',pages='73--77',year='1974',doi='10.1007/BF01405203',url='https://web.math.princeton.edu/~nmk/old/katzmessing.pdf'),
 'Bibliographic cover; theorem checked through Illusie1976§2.5',
 'Identity and publication metadata verified.',
 'PDF was image-only after repository cover. Screenshot tool produced no inspectable image content. No original proof claimed read.','turn240213277view0',status='metadata only; result checked in a separate primary exposition')
r('KatzSGA7XXI','incollection',dict(author='Nicholas M. Katz',title='Le niveau de la cohomologie des intersections complètes',booktitle='Groupes de monodromie en géométrie algébrique, SGA7II',series='Lecture Notes in Mathematics',volume='340',pages='363--400',year='1973',publisher='Springer',doi='10.1007/BFb0060517',url='https://web.math.princeton.edu/~nmk/old/niveaucoho.pdf'),
 'Theorem1.4,pp374–376; Corollary2.2,p378; Theorem4.2,p383',
 'Eventual generic nonnilpotence for projective equidimensional Cohen–MacaulayX; coniveau divisibility; complete-intersection maximal-level result.',
 'The first theorem matches arbitraryX positivity. The later complete-intersection result does not certify the general converse motivic-level equivalence.','turn960295759view0',dates='SGA7IIpublished1973; exact firstcirculation date not verified.')
r('KatzSGA7XXII','incollection',dict(author='Nicholas M. Katz',title='Une formule de congruence pour la fonction zêta',booktitle='Groupes de monodromie en géométrie algébrique, SGA7II',series='Lecture Notes in Mathematics',volume='340',pages='401--438',year='1973',publisher='Springer',doi='10.1007/BFb0060518',url='https://web.math.princeton.edu/~nmk/old/congzeta.pdf'),
 '§1; Corollary3.2,pp410–411; Theorem3.3,formula(3.3.4),p411',
 'Stable Frobenius formalism, coherent mod-p trace congruence and stable deRham augmentation.',
 'Exact matches to cote4:5–6 and the trace-formula part of its final programme; supplies no all-X monodromy result.','turn297288399view1',dates='Published1973.')
r('Koblitz1975','article',dict(author='Neal Koblitz',title='p-adic variation of the zeta-function over families of varieties defined over finite fields',journal='Compositio Mathematica',volume='31',number='2',pages='119--218',year='1975',url='https://www.numdam.org/item/CM_1975__31_2_119_0.pdf'),
 'I§2,Lemma4,p132; I§5Theorems1–2,pp139–141; I§6Theorem3,p142; II§§2–3',
 'Theorem1 states leading stable-rank term Dd^n/n!; Lemma4 transfers the estimate to the generic Cohen–Macaulay section. Also proves generic complete-intersection invertibility.',
 'Displayed defect bounds are missing in OCR, but the explicit prose leading-term statement and generic-transfer lemma suffice for unboundedness. No all-X full invertibility or monodromy theorem is inferred.','turn892992999view0',dates='Princetonthesis1974 recorded in Illusie bibliography; publication1975.')
r('AchterPries2008','article',dict(author='Jeffrey D. Achter and Rachel Pries',title='Monodromy of the p-rank strata of the moduli space of curves',journal='International Mathematics Research Notices',year='2008',number='15',pages='rnn053',doi='10.1093/imrn/rnn053',eprint='0707.2110',archivePrefix='arXiv',url='https://www.math.colostate.edu/~achter/math/prm0508.pdf'),
 'Proposition4.8,PDFp15; arXiv https://arxiv.org/abs/0707.2110',
 'FullGL_f(Fp) andGL_f(Zp) monodromy for components of curve p-rank strata, g≥2,1≤f≤g.',
 'Universal moduli family, not the fixed-X hypersurface linear system in the manuscript.','turn240213277view1',dates='FirstarXiv13July2007; revised28May2008; published2008.')
r('StienstraPutMarel1991','article',dict(author='Jan Stienstra and Marius van der Put and Bernard van der Marel',title='On p-adic monodromy',journal='Mathematische Zeitschrift',volume='208',pages='309--325',year='1991',url='https://pure.rug.nl/ws/files/3346605/1991MathZStienstra.pdf'),
 'Introduction and stated family hypotheses',
 'Studies specified unit-root monodromy families.',
 'No theorem matching all fixed-X hypersurface families was found in the inspected scope.','turn892992999view1',dates='Received21March1990; revised1February1991; published1991.')
r('BerthelotEsnaultRulling2012','article',dict(author='Pierre Berthelot and Hélène Esnault and Kay Rülling',title='Rational points over finite fields for regular models of algebraic varieties of Hodge type at least1',journal='Annals of Mathematics',volume='176',year='2012',pages='413--508',doi='10.4007/annals.2012.176.1.8',url='https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n1-p08-p.pdf'),
 'Remarks9.2(i),printedp478/PDFp65',
 'Verifies the historical Serre freeZ/p quotient mechanism and its nonzeroH¹(O) via Artin–Schreier.',
 'The later paper’s own explicit high-dimensional construction is not substituted for the manuscript surface. Further H¹crystalline facts are independently derived in proofs.md.','turn485449693view2',dates='Published2012.')
r('Serre1958metadata','misc',dict(author='Jean-Pierre Serre',title='Sur la topologie des variétés algébriques en caractéristique p',year='1958',howpublished='Symposium internacional de topología algebraica, Mexico, pp24--53',url='https://csg.igrothendieck.org/articles-and-books/'),
 'Bibliography metadata, and citation[Ser58,Prop16] in Berthelot–Esnault–Rülling§9.2',
 'Historical work identified; original17.7MB scan failed reader limit.',
 'Metadata only. No original pages or proof claimed read; all result use is attributed to the separately opened2012source.','turn331030471view2',status='metadata only',dates='Mexico1956meeting; publication1958.')
r('Illusie1979metadata','article',dict(author='Luc Illusie',title='Complexe de de Rham--Witt et cohomologie cristalline',journal='Annales scientifiques de l\'École Normale Supérieure',series='4',volume='12',number='4',pages='501--661',year='1979',doi='10.24033/asens.1374',url='https://www.numdam.org/item/ASENS_1979_4_12_4_501_0/'),
 'Numdam bibliographic record and bibliography',
 'Metadata and backwards references verified, including Berthelot1973weakLefschetz.',
 'Full14.4MB PDF could not be read; no numbered result from it is claimed checked. zbMATHrecord0436.14007 returned403.','turn445140460view0',status='metadata only')

b=[]
for x in refs:
    fields=',\n'.join('  '+k+' = {'+str(v)+'}' for k,v in x['fields'].items())
    b.append('@'+x['type']+'{'+x['key']+',\n'+fields+'\n}')
(W/'references.bib').write_text('\n\n'.join(b)+'\n')
(W/'reference_evidence.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(refs),'opened references with exact read-status limitations.')
