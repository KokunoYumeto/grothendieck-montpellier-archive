# SA03 (cotes 91, 93): placement config (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
DATE = '2026-11-18'
A, B, C, D = 'MPL_91_019-058', 'MPL_91_059-098', 'MPL_91_099-143', 'MPL_93_002-046'
ITEMS = [
 ('SA03-1', 'lifting of morphisms and its Ext obstruction classes; rigidity and rigidification (Murre\'s criterion)', 'proposition',
  'his: an element with two prescribed images exists iff an Ext class vanishes; rigidity conditions for Hom', 'stated; naturality and compatibility left as obligations'),
 ('SA03-2', 'representability of Hom, Isom and Aut functors by schemes (quasi-projectivity, separatedness, finite type of components, étale covers, descent of Aut and Isom)', 'theorem (stated)',
  'his: Hom(X,Y) is a scheme under quasi-projectivity hypotheses; Aut/Isom descend', 'stated; scope and proof status qualified by the notes'),
 ('SA03-3', 'descent, norms and the projective immersion: very ampleness, determinants, Nagata\'s example, the orbit lemma, finite type', 'proposition',
  'his: a two-stage construction of a projective immersion with determinant and norm line bundles', 'stated with revisions; "fermé" deleted'),
 ('SA03-4', 'infinitesimal and finite étale comparisons: smoothness, étale repair, sections, the n^nu bound, dimension under Weil restriction, homogeneity', 'proposition',
  'his: dimensions and smoothness are preserved under the restriction f_*; the set equation on 91/52 is written D(s) = nD\'(s)', 'stated; one equation reversed (Hua VI)'),
 ('SA03-5', 'the notes\' apparatus for cote 91 (keys, scan summaries, comparisons, plans)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA03-6', 'functors on rings of local nature: the étale envelope, the equivalence criterion, partial right adjoints, gluing with triple intersections', 'proposition',
  'his: criteria for a functor to be of local nature and to glue', 'stated; one corollary withdrawn'),
 ('SA03-7', 'constructible sets and the constructible topology: atomic points, piecewise isomorphism, noetherian topology vs scheme, finite type vs presentation, limits', 'proposition',
  'his: constructible images, universal factorization for constructible subsets', 'stated; several reading questions'),
 ('SA03-8', 'the printed exercise sheets with editorial requests (polarization, restricted Lie identities, tensor reciprocity, restricted enveloping algebras, formal groups)', 'documentary/exercise',
  'printed exercises with requests ("montrer que", a less cursory proof)', 'printed; exercises'),
 ('SA03-9', 'the Greenberg functor and Néron spaces: the six-part programme, ind objects, valuation-ring points, the Greenberg promorphism, Laurent-unit stages', 'programme/theorem (stated)',
  'his: "Pb a poser. Espaces de Neron!"; compact and locally compact preschemes, flasque rings, quasi-schematic spaces', 'programme; stated theorems'),
 ('SA03-10', 'finite-order evaluation, jets and the affine-space rows; exterior-algebra components', 'calculation', 'his: translation/composition calculations', 'unfinished calculations'),
 ('SA03-11', 'pointed genus-one curves in characteristic p: the formulary (Hasse invariant, Legendre polynomial, Tate cusp, j = 1728, wild automorphisms in characteristics 2 and 3)', 'calculation',
  'his: a typescript formulary for curves of genus 1 with reference requests', 'stated; two reference requests'),
 ('SA03-12', 'Hasse-Witt, the Cartier operation on differentials and Cartier descent', 'proposition', 'his: Cartier operation', 'stated'),
 ('SA03-13', 'Wanderley\'s offprint "Théorie axiomatique de l\'orientation des variétés topologiques à bord" and his handwritten orientation sheets', 'documentary/definition',
  'printed offprint (M. Wanderley) and his sheets on orientation through a sheaf', 'offprint and definitions'),
 ('SA03-14', 'the Schwarzian, second-order equations and p-curvature', 'calculation', 'his: Schwarzian derivative and its normalization', 'calculated; coefficient corrected on the page'),
 ('SA03-15', 'the notes\' proposed bridges to cotes 159 and 64 (arithmetic routes)', 'notes\' proposal', 'notes\' proposal', 'not on the pages'),
 ('SA03-16', 'the Dieudonné-crystal programme (Montreal notes, Ch. V): Problems 1-3, F-V exactness, Barsotti-Tate groups and their deformations, abelian crystals and de Rham', 'programme/conjecture',
  'his: full faithfulness and essential image of the crystal functor; finite groups to Barsotti-Tate groups; deformation theorems announced', 'programme; theorems announced, not proved here'),
 ('SA03-17', 'the notes\' apparatus for cote 93', 'apparatus', 'apparatus', 'apparatus'),
 ('SA03-18', 'connections: principal parts, Gauss-Manin, logarithmic connections, stratifications on torsors, Picard functors with connection (cote 93 typescript)', 'construction',
  'his: Gauss-Manin connection in the Leray spectral sequence; P^c_{X/S} and curvature', 'typescript (Work notes)'),
 ('SA03-19', 'a typescript on operator semigroups and the Yosida-Hewitt decomposition (cote 93, typed pp. 5-6)', 'documentary (others\' mathematics)',
  'a typescript; the notes suggest R. E. Huff\'s paper as a lead only', 'documentary'),
 ('SA03-20', 'a reused typescript report on university research (cote 93, scans 61-67)', 'documentary', 'typescript', 'documentary'),
]
RANGES = [
 (A, 1, 2, 'SA03-5'), (A, 3, 17, 'SA03-1'), (A, 18, 38, 'SA03-2'), (A, 39, 40, 'SA03-5'), (A, 41, 73, 'SA03-3'), (A, 74, 99, 'SA03-4'), (A, 100, 108, 'SA03-5'),
 (B, 1, 1, 'SA03-5'), (B, 2, 31, 'SA03-6'), (B, 32, 53, 'SA03-7'), (B, 54, 62, 'SA03-8'), (B, 63, 67, 'SA03-9'), (B, 68, 70, 'SA03-5'),
 (C, 1, 1, 'SA03-5'), (C, 2, 20, 'SA03-7'), (C, 21, 32, 'SA03-9'), (C, 33, 33, 'SA03-7'), (C, 34, 40, 'SA03-9'), (C, 41, 49, 'SA03-10'), (C, 50, 56, 'SA03-8'),
 (C, 57, 57, 'SA03-9'), (C, 58, 60, 'SA03-5'),
 (D, 1, 1, 'SA03-17'), (D, 2, 26, 'SA03-11'), (D, 27, 27, 'SA03-12'), (D, 28, 28, 'SA03-11'), (D, 29, 35, 'SA03-13'), (D, 36, 39, 'SA03-19'), (D, 40, 45, 'SA03-14'),
 (D, 46, 48, 'SA03-15'), (D, 49, 83, 'SA03-16'),
]
HEADING_RULES = []
DEFAULT_ITEM = {'work': 'SA03-18', 'codex': 'SA03-18', '*': 'SA03-5'}
APPARATUS = {'SA03-5', 'SA03-17'}
HIS = {'SA03-2': 'schemas Hom; Aut, Isom', 'SA03-4': 'D(s) = nD\'(s); f_*', 'SA03-7': 'constructible; points atomiques', 'SA03-9': 'foncteur de Greenberg; espaces de Neron',
       'SA03-11': 'courbe de genre 1; invariant de Hasse', 'SA03-12': 'operation de Cartier', 'SA03-16': 'cristaux de Dieudonne; groupes de Barsotti-Tate', 'SA03-18': 'connexion de Gauss-Manin'}
WORK_ITEM = {'K93-01': 'SA03-18', 'K93-02': 'SA03-18', 'K93-03': 'SA03-18', 'K93-04': 'SA03-12', 'K93-05': 'SA03-18', 'K93-06': 'SA03-18', 'K93-07': 'SA03-18',
             'K93-08': 'SA03-20', 'K93-09': 'SA03-18', 'K93-10': 'SA03-11', 'K93-11': 'SA03-11', 'K93-12': 'SA03-19'}
WORK_OBJECT = {'K93-01': 'a first-principal-parts extension on omega (scans 135-136)', 'K93-02': 'a stratification on a torsor (scan 151)',
               'K93-03': 'de Rham cohomology and the Gauss-Manin connection in the Leray spectral sequence (scan 165)', 'K93-04': 'residues and the relative Cartier operation (scan 179)',
               'K93-05': 'connections on O_X and logarithmic differentials (scan 193)', 'K93-06': 'curvature and the Picard functors with connection (scan 207)',
               'K93-08': 'a typescript report on university research (scans 61-67)', 'K93-09': 'from a local basis to a connection (scans 76-77)',
               'K93-10': 'pointed genus-one curves (typescript, scan 3)', 'K93-11': 'normal forms and the invariant j (scans 17, 19)', 'K93-12': 'fixed points and the weak-operator closure (typed pp. 5-6, scans 32, 34)'}
WORK_SCANS = {'K93-01': '135-136', 'K93-02': '151', 'K93-03': '165', 'K93-04': '179', 'K93-05': '193', 'K93-06': '207', 'K93-08': '61-67', 'K93-09': '76-77',
              'K93-10': '3', 'K93-11': '17,19', 'K93-12': '32,34'}
CODEX_ITEM = {}
CODEX_COTE = {'K91': '91', 'K93': '93'}
OVERRIDE = {
 A + '#78': dict(basis='passage-read', fidelity='agrees', note='C05; read 91/52 l. 21-23: "D(s) = nD\'(s)" against "dimension nd"; Weil restriction multiplies dimension by n, so D\' = nD; credit Hua VI p. 51'),
 A + '#79': dict(basis='entry-read', note='C06; mixed dimensions: restriction of A^1 u A^2 over two points has dimensions 2, 3, 4; credited to Hua'),
 D + '#29': dict(basis='entry-read', note='O01: offprint by Marcus Wanderley on axiomatic orientation of topological manifolds with boundary'),
 D + '#49': dict(basis='entry-read', note='C01: the sequence parallels Ch. V "Programme" of the Montreal notes (1970 course, published 1974)'),
 D + '#36': dict(basis='entry-read', note='A01: a bibliographic lead (Huff, Yosida-Hewitt), medium confidence, insufficient for attribution'),
 C + '#21': dict(basis='entry-read', note='RN118-01: "Pb a poser. Espaces de Neron!"'),
 B + '#55': dict(basis='entry-read', note='N085-01: printed exercise on (ad x)^p y = (ad x^p) y'),
}
CROSS = {'SA03-2': 'SA02-12 (cote 91 scans 2-18, MPL_90+91_002-018); EGA/SGA Hom schemes', 'SA03-9': 'SA02-12; Greenberg, Néron models (literature)', 'SA03-16': 'crystalline Dieudonné theory (Montreal notes); cotes 100 (Barsotti-Tate, SA01 list) and 159',
         'SA03-13': 'SA21 (Vers une géométrie des formes) and the tame topology / pseudoline material (SA11)', 'SA03-11': 'any topic with the Legendre family or Hasse invariants (SA10?)', 'SA03-8': 'SA02-16 (restricted enveloping algebras, K91-10)'}
ITEM_FLAGS = {'SA03-15': 'a link across folders (bridges to cotes 159, 64)', 'SA03-2': 'a link across folders (SA02 Work K91 folders re-read these pages)'}
FLAGS = [
 ['a link across folders', 'work:K91-02..K91-10 (listed under SA02) and MPL_91_019-058, 059-098, 099-143', 'The cote 91 Work folders are filed under SA02 but re-read SA03\'s Pro pages: K91-02 (19-20, the Ext obstruction) with A01-A06; K91-03 (34) with B01; K91-04 (47-48) with B27-B28; K91-05 (59) with N059; K91-06 (73-74) with N073-N074; K91-07 (87) with N087; K91-08 (99) with RN099; K91-09 (114) with RN114; K91-10 (129) with RN129. Pairs of independent readings for sweep 2, across the SA02/SA03 boundary.', 'SA02 WORK_SCANS; SA03 index scans'],
 ['a link across folders', 'SA02 MPL_90+91_002-018 (cote 91, scans 2-18) and SA03 MPL_91_019-143', 'Cote 91 is split between SA02 (scans 2-18) and SA03 (19-143); the Hom-functor items SA02-12 and SA03-2 are one subject.', 'TOPIC.md of SA02 and SA03'],
 ['a link across folders', 'MPL_93_002-046#49-83 (C01-C35)', 'The crystal programme pages parallel Chapter V "Programme" of the Montreal notes (1970 course, published 1974), by the notes\' comparison with the French edition; the notes do not date the sheets.', 'C01 entry'],
 ['a link across folders', 'MPL_93_002-046#29-35 (O01-O07)', 'Cote 93 holds an offprint by Marcus Wanderley ("Théorie axiomatique de l\'orientation des variétés topologiques à bord") with handwritten orientation sheets; a link to the topology topics (SA21, SA11), not to Gauss-Manin.', 'O01 entry'],
 ['a link across folders', 'MPL_93_002-046#46-48 (P07-P09)', 'The notes propose bridges to cotes 159 and 64; they are proposals, not on the pages.', 'P07-P09 headings'],
]
CHECKS = [
 [A + '#78', 'note checked against the page (91/52, l. 21-23)', 'agrees: the set equation is written D(s) = nD\'(s) while the corollary says "dimension nd"; restriction along degree n multiplies dimension by n, so D\' = nD (Hua VI p. 51 has the correction)', 'SA03/pro/MPL_91_019-058_transcription.tex scanpage 52'],
 [A + '#79', 'claim checked by computation (dimension count)', 'agrees: (A^1 u A^2) x (A^1 u A^2) has components of dimension 2, 3, 4, and 2{1,2} = {2,4} misses 3', 'MPL_91_019-058_notes.md C06'],
]
