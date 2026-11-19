# SA11 Espaces stratifiés (cotes 121, 153, 154, 155): placement config (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
import os, sys, importlib.util
DATE = '2026-11-18'
R, A, B, C, P81 = 'MPL_121_049-073+153+155', 'MPL_154_001-045', 'MPL_154_077-126', 'MPL_154_127-176', 'MPL_81_038-055+154_046-076'
ITEMS = [
 ('SA11-1', 'his terms "tubulure" and "ombre": germs around an immersion (cotes 121, 149)', 'reading question (requested)', 'his: tubulure, ombre; germes', 'used, not defined, on these pages'),
 ('SA11-2', 'the "Remords" and his own repair; its date', 'his claim / history', 'his: Remords', 'repair attested; date not established'),
 ('SA11-3', 'the axiomatics of moderate (tame) spaces in cote 121: adapted partitions, graphs, conservativity, effective epimorphisms, function language, triangulation', 'axiomatics',
  'his: espaces moderes; partitions adaptees; graphes', 'stated; several axioms unfinished or self-flagged'),
 ('SA11-4', 'comparison of the cote 121 axiomatics with o-minimal structures, analytic-geometric categories, Nash categories and Shiota\'s Hauptvermutung', 'comparison (requested)',
  'ours (the notes\'): dictionaries and benchmarks', 'not his claim'),
 ('SA11-5', 'analysers (cote 153): binomial and lambda operations, plethories, divided powers, coaddition and comultiplication', 'definition/proposition',
  'his: analyseurs; ours: close to plethories (not literally, under the written axioms)', 'stated; existence questions self-flagged'),
 ('SA11-6', 'rigidity of tensor categories and reconstruction (cote 155): exactness and faithfulness after diagonal tensoring, descent data, bialgebroids', 'question/construction',
  'his: rigidite de categories tensorielles; reconstruction of the equivalence', 'question; unfinished'),
 ('SA11-7', 'the notes\' apparatus for SA11 (keys, method, inventories, register matches)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA11-8', 'the combinatorial surface of relative positions of an added projective pseudoline (Esquisse §8): scope, tame topology, oriented-matroid comparisons', 'construction (programme)',
  'ours: the space of positions of one more pseudoline relative to an arrangement; the notes compare the extension space of an oriented matroid', 'constructed in part; open'),
 ('SA11-9', 'deployments: valences, sweeps of weight two, blow-up and antipodal identification, Möbius band, dihedral covers', 'construction', 'his: deploiement; balayages', 'sketched; self-flagged'),
 ('SA11-10', 'specialization and generization: weights, polygon invariants and the conjectured injectivity, reconstruction of the weighted graph', 'proposition/conjecture',
  'his: specialisation, generisation; the polygon invariant is expected injective', 'conjectured'),
 ('SA11-11', 'local gluing of the cellular surface: polygon disks, edge transport, facewise maps, critical points and arcs, flag permutations', 'construction',
  'his: transport le long des aretes; points critiques', 'sketched; several claims unproved or withdrawn'),
 ('SA11-12', 'the disk model: chord conditions, inertia arcs, corridors and faces, exceptional cells', 'construction', 'his: cordes; arcs d\'inertie; couloirs', 'sketched; revised definitions'),
 ('SA11-13', 'the deployment by two cellular graphs K and L: exceptional edges forming circles, bands, weighted face totals 2n', 'construction', 'his: graphes K, L; bandes', 'declared; sufficiency not verified'),
 ('SA11-14', 'dihedral monodromy of polygon transport and the parity (sign) character', 'proposition/conjecture', 'his: caractere de parite', 'calculated in part; conjectured'),
 ('SA11-15', 'reading questions of cote 154 (scans 1-45 and 127-176)', 'reading question', 'reading questions', 'reading questions'),
 ('SA11-16', 'the cartographic dictionary: circuits, involutions, duality signs, cyclic words and the quartic count', 'construction', 'his: involutions cartographiques', 'worked; comparisons by the notes'),
 ('SA11-17', 'the sweeps sigma_0, sigma_1, the joint quotient and the endpoint construction; move systems and innermost triangles (scans 127-176)', 'construction', 'his: sigma_0, sigma_1', 'self-flagged; unfinished'),
 ('SA11-18', 'documentary: dates, marginal pagination, printer paper and titles of cote 154', 'documentary', 'documentary', 'documentary'),
 ('SA11-19', 'pencils (fuseaux) of pseudolines: isotopy classes, the cube of indices, one-element extensions, allowable sequences', 'proposition', 'his: fuseaux', 'stated with qualifications'),
 ('SA11-20', 'the natural-map schemes A1, A2, B1, B2: immersions, folding and circuit tests', 'construction/test', 'his: schemas A1, A2, B1, B2; pliage', 'tested; self-flagged failures'),
]
RANGES = [
 (R, 1, 6, 'SA11-1'), (R, 7, 12, 'SA11-2'), (R, 13, 53, 'SA11-3'), (R, 54, 73, 'SA11-4'), (R, 74, 99, 'SA11-5'), (R, 100, 124, 'SA11-6'), (R, 125, 129, 'SA11-7'),
 (A, 1, 2, 'SA11-7'), (A, 3, 6, 'SA11-8'), (A, 7, 19, 'SA11-9'), (A, 20, 44, 'SA11-10'), (A, 45, 51, 'SA11-11'), (A, 52, 70, 'SA11-12'), (A, 71, 82, 'SA11-13'),
 (A, 83, 84, 'SA11-10'), (A, 85, 85, 'SA11-11'), (A, 86, 86, 'SA11-14'), (A, 87, 88, 'SA11-13'), (A, 89, 89, 'SA11-11'), (A, 90, 90, 'SA11-8'), (A, 91, 91, 'SA11-12'),
 (A, 92, 92, 'SA11-10'), (A, 93, 116, 'SA11-15'), (A, 117, 122, 'SA11-7'),
 (B, 1, 1, 'SA11-8'), (B, 2, 3, 'SA11-14'), (B, 4, 4, 'SA11-13'), (B, 5, 5, 'SA11-16'), (B, 6, 6, 'SA11-10'), (B, 7, 7, 'SA11-18'),
 (C, 1, 5, 'SA11-8'), (C, 6, 12, 'SA11-17'), (C, 13, 16, 'SA11-18'), (C, 17, 26, 'SA11-19'), (C, 27, 32, 'SA11-16'), (C, 33, 33, 'SA11-17'), (C, 34, 36, 'SA11-11'),
 (C, 37, 42, 'SA11-17'), (C, 43, 45, 'SA11-8'), (C, 46, 53, 'SA11-13'), (C, 54, 65, 'SA11-17'), (C, 66, 75, 'SA11-15'), (C, 76, 77, 'SA11-7'),
]
# the shared package: reuse SA01's ranges, translated to SA11 items
_spec = importlib.util.spec_from_file_location('c1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cfg_SA01.py'))
_c1 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_c1)
_T = {'SA01-9': 'SA11-8', 'SA01-10': 'SA11-11', 'SA01-11': 'SA11-14', 'SA01-12': 'SA11-20', 'SA01-15': 'SA11-18'}
RANGES += [(p, lo, hi, _T[it]) for (p, lo, hi, it) in _c1.RANGES if p == P81]
HEADING_RULES = []
DEFAULT_ITEM = {'work': 'SA11-20', 'codex': 'SA11-14', '*': 'SA11-7'}
APPARATUS = {'SA11-7'}
HIS = {'SA11-3': 'espaces moderes', 'SA11-5': 'analyseurs', 'SA11-6': 'categories tensorielles rigides', 'SA11-8': 'pseudo-droites; positions relatives', 'SA11-14': 'caractere de parite',
       'SA11-19': 'fuseaux', 'SA11-20': 'application naturelle; pliage, double pliage'}
WORK_ITEM = {'K154-01_3': 'SA11-20', 'K154-02': 'SA11-14'}
WORK_OBJECT = {'K154-01_3': 'the structural map of the surface by faces, edges and vertices; folding and double folding (scan 46)',
               'K154-02': 'transport of orientation data and signs along faces and pseudolines (scans 62-63)'}
WORK_SCANS = {'K154-01_3': '46', 'K154-02': '62-63'}
CODEX_ITEM = {'K154-02': 'SA11-14'}; CODEX_COTE = {'K15': '154'}
OVERRIDE = {
 A + '#99': dict(basis='entry-read', fidelity='not checked', flag='the same thing noted with different readings or statements', note='Q07 (scan 032 l. 51-64): the frozen reading has rho_som rho_f = sigma_2 sigma_0 = sigma; Hua 154.modern.tex:935-956 reads the left side as rho_f alone and corrects that label from a later page; the normalized products agree; the scan decides the first factor'),
 A + '#105': dict(basis='entry-read', fidelity='not checked', flag='the same thing noted with different readings or statements', note='Q13 (scan 044 l. 46-60): the 0/1 definition of epsilon(s) is struck, while epsilon stays in the marginal count; Hua 154.modern.tex:1192-1202 restores it editorially from its recurrence on scan 171; a difference of editorial status, not of reading'),
 A + '#96': dict(note='Q04: a reported Lean statement (Hua\'s project) needs translation to the polygon data'),
 R + '#39': dict(note='R121-27: a Chern-class calculation inside the tame-topology leaves, a distinct fragment'),
}
for _e in range(1, 117):
    OVERRIDE.setdefault(P81 + f'#{_e}', {})['note'] = 'shared with SA01 (same package, same entry); cote 154 scans 46-76'
CROSS = {'SA11-8': 'SA01-9 (same package under SA01); SA04-28 (cote 80 Work); Esquisse §8 (cote 119)', 'SA11-1': 'SA10-2', 'SA11-2': 'SA10-3', 'SA11-3': 'SA10-19 (cote 120); SA21',
         'SA11-4': 'SA10-4, SA10-5', 'SA11-14': 'SA01-11', 'SA11-20': 'SA01-12; SA01-29 (immersions of the disc, cote 81)', 'SA11-6': 'Tannakian categories (literature); Deligne', 'SA11-5': 'lambda-rings, plethories (literature)'}
ITEM_FLAGS = {'SA11-8': 'a link across folders', 'SA11-4': 'requested comparison; the notes\' work'}
FLAGS = [
 ['a link across folders', 'MPL_81_038-055+154_046-076 (116 entries)', 'The same package and the same 116 entries are indexed in SA01 and here; it is cote 154 (scans 46-76) and belongs here. Items translated: SA01-9 = SA11-8, SA01-10 = SA11-11, SA01-11 = SA11-14, SA01-12 = SA11-20, SA01-15 = SA11-18.', 'NOTES_INDEX of SA01 and SA11'],
 ['a link across folders', 'work:K154-01_3 (scan 46), work:K154-02 (62-63)', 'Both Work folders re-read pages of the shared Pro package (154/46-76): pairs of independent readings for sweep 2.', 'WORK_SCANS'],
 ['the same thing noted with different readings or statements', 'MPL_154_001-045#99 (Q07), #105 (Q13)', 'Q07: the frozen reading has rho_som rho_f = sigma_2 sigma_0 = sigma on scan 032 (l. 51-64); Hua\'s modernization reads the left side as rho_f alone and corrects it from a later page; the normalized products agree, so only the first factor is in question, for the scan. Q13: the 0/1 definition of epsilon(s) is struck on scan 044 but epsilon stays in the marginal count; Hua restores it editorially from scan 171: a question of editorial status, not of reading.', 'Q07, Q13 headings'],
 ['a link across folders', 'MPL_121_049-073+153+155 (H01-H12, TC01-TC20)', 'The requested questions of SA10 (tubulure and ombre; the Remords; o-minimality; Shiota) recur here; merge SA11-1, -2, -4 with SA10-2, -3, -4, -5 in the global tag space.', 'headings'],
 ['a link across folders', 'MPL_121_049-073+153+155 (A01-A26, T01-T25)', 'Cotes 153 (analysers) and 155 (rigidity of tensor categories) are algebra, not stratified spaces; they sit in SA11 by catalogue order.', 'SA11/TOPIC.md rows 153, 155'],
]
CHECKS = []

# global tags from the broad agent's inbox (build_global.py, 15:08 UTC), added 18 Nov 2026
def _addx(k, s):
    CROSS[k] = (CROSS[k] + '; ' + s) if CROSS.get(k) else s
for _k, _s in [('SA11-3', '= H00M (SA20-15)'), ('SA11-5', '= H00N (SA20-16)'), ('SA11-6', '= H00O (SA20-17)'), ('SA11-2', 'H00L (SA10-3, SA20-9)'), ('SA11-1', 'related: SA10-2')]:
    _addx(_k, _s)
