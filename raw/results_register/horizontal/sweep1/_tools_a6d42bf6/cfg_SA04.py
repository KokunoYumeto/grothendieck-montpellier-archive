# SA04 (cotes 93, 98, 100, 161 and the Work-only cotes 69-102): placement config (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
DATE = '2026-11-18'
A, B, H = 'MPL_93_047-091', 'MPL_93_221-236+161-5', 'MPL_98'
ITEMS = [
 ('SA04-1', 'Barsotti-Tate groups and their crystals: the crystalline comparison for abelian schemes, deformations (Serre-Tate, Messing), canonical filtration, the isogeny category', 'programme/theorem (stated)',
  'his: the BT crystal by two constructions and its comparison with the abelian crystal; deformation theories equal', 'stated; several steps deferred or self-flagged'),
 ('SA04-2', 'pseudo-resolvents and resolvent estimates (typed analysis exercises: Liouville, little-o growth, perturbation)', 'exercise/proposition (others\' text?)',
  'typed exercises on pseudo-resolvents; the notes find the stated radius and the perturbation target false as written', 'stated with literal errors (notes)'),
 ('SA04-3', 'p-adic representations and crystals: Tate\'s theorem, Hodge-Tate condition, full faithfulness on an admissible category, a quasi-inverse, F-crystals', 'programme/conjecture',
  'his: a crystalline description of p-adic representations, assuming Problem 1', 'programme; later proved results cited by the notes'),
 ('SA04-4', 'axioms for the Euler characteristic of locally compact spaces (ordinary and compact support): additivity, Mayer-Vietoris, conical class, end-link defect, triangulability in low dimensions', 'axiomatics',
  'his: axioms (a)-(h) and a uniqueness question; triangulation claims in dimensions 1-4', 'stated; uniqueness left open by him'),
 ('SA04-5', 'documentary: reused administrative sheets (research policy, a 1976 budget) in cote 93', 'documentary', 'administrative typescript', 'documentary'),
 ('SA04-6', 'loop spaces and deloopings: when the first class vanishes', 'question', 'his: a question on a loop-space leaf', 'question; the notes give a model with a nonzero class after one delooping'),
 ('SA04-7', 'the Schwarzian derivative as a projective invariant over any base: cocycle, invariance, rigidity, normalization G = 12G_0, characteristics 2 and 3', 'theorem (stated)/calculation',
  'his: an integral invariant G of projective structure, identically zero in characteristics 2 and 3; ours: G_0 = D3/D1 - (D2/D1)^2 in Hasse derivatives', 'stated; a test value on 73 wrong as printed (Hua VI)'),
 ('SA04-8', 'logarithmic and n-differentials, frames of line bundles, uniformization diagrams and rank-two splittings', 'construction',
  'his: affine and projective structures through logarithmic differentials and their powers', 'worked; several questioned maps'),
 ('SA04-9', 'projective connections and opers: rank-two bundles, PGL_2 and Borel reductions, Killing forms, the bad characteristic two', 'construction',
  'his: projective connections as connections on a P^1-bundle with a flag; ours: opers', 'worked; some boxed factors checked by the notes'),
 ('SA04-10', 'the notes\' apparatus and synthesis for cote 93 (strands, sources, the strand comparisons S20, X01-X07)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA04-11', 'Gauss-Manin, Picard-Fuchs, the Cartier operation and p-curvature: the notes\' comparisons across the cote', 'comparison', 'notes\' comparisons', 'not on these pages as a proof'),
 ('SA04-12', 'periods and the Picard-Fuchs construction from logarithmic differentials (cote 93, scans 221-236)', 'construction',
  'his: integrals of closed differentials, cocycle identity, an explicit Picard-Fuchs construction', 'constructed; identification open'),
 ('SA04-13', 'formal de Rham data and derived Hom toward the crystal construction (formally exact, formal Poincaré, torsor extension)', 'construction',
  'his: a torsor extension and a boxed isomorphism with derived Hom', 'stated; the notes supply a roof proof (own idea)'),
 ('SA04-14', 'p-adic Galois representations: Hodge-Tate grading, the algebraic envelope, openness of inertia, Sen\'s theorem (cote 161 offprints and notes)', 'theorem (stated)/comparison',
  'offprints and his notes; the notes identify later answers (Sen)', 'printed results and notes'),
 ('SA04-15', 'filtered modules for Barsotti-Tate groups: fibre functors, Tate twists, descent with Frobenius (cote 161 sheets)', 'construction', 'his: the fibre in Omega and its descent', 'worked; reading questions'),
 ('SA04-16', 'cocycle parametrization of extensions and the cohomology of Gamma and pi (Hua\'s rank-one counterexample)', 'proposition', 'his: restriction fibres as cocycle quotients', 'stated; notes verify Hua\'s example'),
 ('SA04-17', 'Hilbert schemes and norms (cote 98): norms, symmetric powers, descent, bounded families, Tor and Ext', 'proposition', 'his: norms of coherent modules and symmetric powers', 'not checked'),
 ('SA04-18', 'documentary: offprints, covers and year labels of cotes 93 and 161', 'documentary', 'documentary', 'documentary'),
 ('SA04-20', 'cubic graphs: the 27-vertex criterion, roots from pairs of vertices, configurations and stabilizers (cote 69)', 'combinatorics', 'his: graphe cubique', 'Work notes only'),
 ('SA04-21', 'geometric realizations of regular polyhedra: the group G_n generated by involutions, affine realizations of the pinned icosahedron (cote 70)', 'construction', 'his: realisations geometriques; icosaedre epingle', 'Work notes only'),
 ('SA04-22', 'polygons in an affine plane over a base (cote 73)', 'construction', 'his: polygones', 'Work notes only'),
 ('SA04-23', 'cubic complexes: graphs from group data, triads, hexagons and their coverings (cote 74)', 'combinatorics', 'his: complexes cubiques', 'Work notes only'),
 ('SA04-24', 'n-cellular maps: faces, incidence, flags, quasi-simplicial sets, cube symmetries (cote 76)', 'combinatorics', 'his: n-cartes cellulaires', 'Work notes only'),
 ('SA04-25', 'affine quadrics and quadratic extensions: rank-two forms, alpha^2 - 4, mu_2 actions, the Arf scheme (cote 77)', 'algebra', 'his: quadriques affines, extensions quadratiques', 'Work notes only'),
 ('SA04-26', 'regular polygons and cyclotomic polynomials: pinned regular n-gons over rings, unimodularity, orientations (cote 78)', 'construction', 'his: polygones reguliers', 'Work notes only'),
 ('SA04-27', 'regular triangulated 2-polyhedra from free rank-two modules over Z/nZ and Z: repères, edge types, automorphisms, torsors (cote 79)', 'construction',
  'his: 2-polyedres reguliers triangules et modules libres de rang 2 sur Z/nZ', 'Work notes only'),
 ('SA04-28', 'pseudoline systems: configurations, a distinguished line, orientation and the canonical functor (cote 80)', 'combinatorics', 'his: systemes de pseudo-droites', 'Work notes only'),
 ('SA04-29', 'documentary: autobiographical and administrative typescripts among cotes 69-102 (cote 80 scans 22-30; cote 94 report on local fields)', 'documentary', 'typescript', 'documentary'),
 ('SA04-30', 'SO(3) = GP(1) over a base: rank-three quadratic modules, the sl_2 action, the stabilizer of a section of P^1 (cote 82)', 'algebra', 'his: SO(3) = GP(1)', 'Work notes only'),
 ('SA04-31', '2-polyhedra and 1-polygons: dihedral and triangle-group representations, traces and orders (cote 85)', 'group theory', 'his: 2-polyedres et 1-polygones', 'Work notes only'),
 ('SA04-32', 'regular polyhedra: incidence data, antipodism, the fifteen directions and trihedra (cote 86)', 'combinatorics', 'his: polyedres reguliers', 'Work notes only'),
 ('SA04-33', 'convex polyhedra: convex hulls, faces and relative interiors (cote 87)', 'geometry', 'his: polyedres convexes', 'Work notes only'),
 ('SA04-34', 'the root-system functor (cote 88, "Cartes standards")', 'algebra', 'his: systeme de racines', 'Work notes only'),
 ('SA04-35', 'the combinatorial hexagon and 3-3 sets: orientations, torsors and partitions (cote 89)', 'combinatorics', 'his: hexagone combinatoire', 'Work notes only'),
 ('SA04-36', 'coherent modules from a functor and prorepresentability (cote 94)', 'algebra', 'his: construction de faisceaux de modules', 'Work notes only'),
 ('SA04-37', 'Chern classes of representations: the regular representation of a cyclic group (cote 97)', 'algebra', 'his: classes de Chern des representations', 'Work notes only'),
 ('SA04-38', 'good reduction of abelian varieties via Barsotti-Tate groups over any base (cote 100)', 'theorem (stated)', 'his: bonne reduction via T_p(A)', 'Work notes only'),
 ('SA04-39', 'local cohomology: cones, twists, topologies on H^0, change of rings and duality (cote 101)', 'algebra', 'his: cohomologie locale', 'Work notes only'),
 ('SA04-40', 'functors (Sch)^op -> (Ens): recollements along a class of covers (cote 102)', 'construction', 'his: recollements', 'Work notes only'),
]
RANGES = [
 (A, 1, 6, 'SA04-10'), (A, 7, 34, 'SA04-1'), (A, 35, 43, 'SA04-2'), (A, 44, 50, 'SA04-1'), (A, 51, 60, 'SA04-2'), (A, 61, 75, 'SA04-3'),
 (A, 76, 117, 'SA04-4'), (A, 118, 121, 'SA04-5'), (A, 122, 129, 'SA04-6'), (A, 130, 135, 'SA04-4'), (A, 136, 175, 'SA04-7'), (A, 176, 234, 'SA04-8'),
 (A, 235, 253, 'SA04-7'), (A, 254, 302, 'SA04-9'), (A, 303, 307, 'SA04-10'), (A, 308, 321, 'SA04-11'), (A, 322, 325, 'SA04-10'),
 (B, 1, 5, 'SA04-18'), (B, 6, 19, 'SA04-12'), (B, 20, 35, 'SA04-13'), (B, 36, 58, 'SA04-14'), (B, 59, 80, 'SA04-15'), (B, 81, 92, 'SA04-16'), (B, 93, 99, 'SA04-10'),
 (H, 1, 3, 'SA04-17'), (H, 4, 6, 'SA04-17'), (H, 7, 7, 'SA04-17'), (H, 8, 8, 'SA04-17'),
]
HEADING_RULES = []
DEFAULT_ITEM = {'work': 'SA04-10', 'codex': 'SA04-10', '*': 'SA04-10'}
APPARATUS = {'SA04-10'}
HIS = {'SA04-1': 'cristal de Barsotti-Tate', 'SA04-4': 'caracteristique d\'Euler-Poincare a supports compacts', 'SA04-7': 'G = 12 G_0; "identiquement nulle en car. 2 et 3"',
       'SA04-9': 'connexion projective', 'SA04-12': 'equation de Picard-Fuchs'}
PREF = {'K69': 'SA04-20', 'K70': 'SA04-21', 'K73': 'SA04-22', 'K74': 'SA04-23', 'K76': 'SA04-24', 'K77': 'SA04-25', 'K78': 'SA04-26', 'K79': 'SA04-27', 'K80': 'SA04-28',
        'K82': 'SA04-30', 'K85': 'SA04-31', 'K86': 'SA04-32', 'K87': 'SA04-33', 'K88': 'SA04-34', 'K89': 'SA04-35', 'K94': 'SA04-36', 'K97': 'SA04-37', 'K100': 'SA04-38',
        'K101': 'SA04-39', 'K102': 'SA04-40', 'K93': 'SA04-11'}
import csv as _csv
WORK_ITEM = {}
for _r in _csv.DictReader(open('C:/Users/user/Documents/results_register/horizontal/inputs/WORK_MATHNOTES_BY_TOPIC.tsv', encoding='utf-8'), delimiter='\t'):
    if _r['topic'] == 'SA04':
        WORK_ITEM[_r['folder']] = PREF.get(_r['folder'].split('-')[0], 'SA04-10')
for _k in range(1, 13): WORK_ITEM[f'K93-{_k:02d}'] = 'SA04-11'
for _k in range(1, 5): WORK_ITEM[f'K100-0{_k}'] = 'SA04-38'
WORK_ITEM['K80-02'] = 'SA04-29'; WORK_ITEM['K94-02'] = 'SA04-29'
WORK_OBJECT = {}
WORK_SCANS = {}
CODEX_ITEM = {}
CODEX_COTE = {'K93': '93', 'K10': '100'}
OVERRIDE = {
 A + '#158': dict(basis='entry-read', note='SC23: frozen test value dt^2/(2t); Hasse differentiation gives dt^2/(4t^2) (up to the sign convention); credit Hua VI; checked by computation'),
 A + '#155': dict(basis='entry-read', note='SC20: "identiquement nulle en car. 2 et 3" follows from G = 12G_0'),
 A + '#120': dict(basis='entry-read', note='EC45: 275 + 79 = 354, agreeing with the inserted digit'),
 A + '#118': dict(basis='index-row', note='EC43: six interleaved administrative research-policy sheets'),
}
CROSS = {'SA04-1': 'SA03-16 (the crystal programme, cote 93 scans 37-46); SA04-38 (cote 100)', 'SA04-3': 'SA03-16; p-adic Hodge theory (literature)', 'SA04-4': 'SA21 (Vers une geometrie des formes; tame topology)',
         'SA04-7': 'SA03-14 (the Schwarzian on cote 93 scans 2-46)', 'SA04-9': 'SA04-30 (SO(3) = GP(1), cote 82)', 'SA04-21': 'SA01-1 (pinned realizations, cote 72)', 'SA04-26': 'SA01-1',
         'SA04-27': 'SA01-2 (level-n regular maps); SA01-1', 'SA04-28': 'SA01-9 and SA11 (cote 154 pseudolines)', 'SA04-25': 'SA02-1 (quadratic algebras, cote 84); SA01-28',
         'SA04-31': 'SA01-27 (icosahedral matrices); SA01-2', 'SA04-38': 'SA04-1; SA03-16', 'SA04-11': 'SA03-12, SA03-18 (Cartier, Gauss-Manin)'}
ITEM_FLAGS = {'SA04-2': 'note overstates or misreads the page? (typed exercise source unidentified)', 'SA04-7': 'suspected misreading (test value on 73)'}
FLAGS = [
 ['suspected misreading', '93/073 (MPL_93_047-091#158 = SC23)', 'The final frozen test value G_0(t, t^2) = dt^2/(2t) is not homogeneous of the right weight; Hasse differentiation (G_0 = D3/D1 - (D2/D1)^2 for f = t^2: D1 = 2t, D2 = 1, D3 = 0) gives dt^2/(4t^2) up to sign. Hua VI makes the same correction. A slip of his or a misreading of "4t^2" as "2t": decide on the scan.', 'SC23 entry; my computation'],
 ['a link across folders', 'MPL_93_047-091 (BT, HC, S20) and SA03 MPL_93_002-046 (C01-C35)', 'Cote 93 is split between SA03 (scans 2-46) and SA04 (47-91, 221-236): the crystal programme (SA03-16) continues as SA04-1 and SA04-3, the Schwarzian (SA03-14) as SA04-7, Cartier and Gauss-Manin (SA03-12, -18) as SA04-11. One cote, two topics.', 'package ranges; headings'],
 ['a link across folders', 'Work K69-K102 (102 files) and SA01', 'The Work-only cotes 69-102 are the "other part" cotes of SA01\'s list (cubic graphs, polygons, regular polyhedra, cotes 79-80, SO(3) = GP(1), ...). They continue SA01\'s subjects: pinned realizations (SA01-1) in cotes 70, 78, 79; pseudolines (SA01-9, SA11) in cote 80; quadratic algebras (SA01-28, SA02-1) in cote 77; icosahedral groups (SA01-27) in cote 85.', 'WORK_MATHNOTES_BY_TOPIC.tsv; SA01/TOPIC.md'],
 ['note overstates or misreads the page', 'MPL_93_047-091#35-43, #51-60 (BT29-BT37, BT45-BT54)', 'Twenty entries in the BT series concern pseudo-resolvents, Fourier coefficients and perturbation estimates (typed analysis exercises), not Barsotti-Tate groups. Their "BT" label places them in the wrong cluster; their source is not identified (compare SA03-19, the operator-semigroup typescript of the same cote).', 'headings BT29-BT54'],
 ['a link across folders', 'MPL_93_221-236+161-5 (S01-S23, B01-B22)', 'The package includes cote 161 (offprints on p-adic representations, Sen\'s theorem, the algebraic envelope). It belongs with the p-adic material, which the topic list does not name.', 'package name; S-entry headings'],
 ['a link across folders', 'Work K100-01..04 (cote 100) and SA04-1, SA03-16', 'Good reduction of abelian varieties via Barsotti-Tate groups (cote 100) is the same programme as the BT crystals of cote 93.', 'K100 summaries'],
]
CHECKS = [
 [A + '#158', 'claim checked by computation (Hasse derivatives of f = t^2)', 'agrees: G_0(t, t^2) = 1/(4t^2) dt^2 up to sign, not dt^2/(2t)', 'MPL_93_047-091_notes.md:1223'],
 [A + '#120', 'claim checked by computation', 'agrees: 275 + 79 = 354', 'MPL_93_047-091_notes.md:889'],
]

# global tags from the broad agent's inbox (build_global.py, 15:08 UTC), added 18 Nov 2026
def _addx(k, s):
    CROSS[k] = (CROSS[k] + '; ' + s) if CROSS.get(k) else s
for _k, _s in [('SA04-12', '= H00B (SA23-43)'), ('SA04-13', '= H00C (SA23-44); related: SA23-38 (H0DR, Quillen tapis, cote 162-5)'), ('SA04-15', '= H00D (SA23-36)'),
               ('SA04-18', '= H00E (SA23-45)'), ('SA04-14', 'related: SA23-34 (H0DO, Serre 1967, cote 161-5)'), ('SA04-11', 'related: SA23-24 (H0DD, connections, cote 23)'),
               ('SA04-8', 'related: SA32-2 (H0JE, uniformization by projective connections)'), ('SA04-9', 'related: SA32-2 (H0JE)')]:
    _addx(_k, _s)
