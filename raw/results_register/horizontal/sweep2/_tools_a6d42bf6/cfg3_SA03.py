# Sweep 2 part 2, SA03 (cotes 91, 93): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
DATE = '2026-11-18'
TITLE = 'SA03: deformations and representability (cote 91); characteristic p, connections and crystals (cote 93)'
INTRO = '''
The topic holds two cotes:
- **Cote 91, scans 19-143:** lifting of morphisms and their obstructions, representability of Hom, Isom and Aut, descent and the projective immersion, finite étale comparisons, functors of local nature, the constructible topology, the Greenberg functor and Néron spaces, and finite-order evaluation. Numbered typescripts are reused on the backs: exercise sheets on restricted Lie algebras and formal groups, and exterior algebras.
- **Cote 93, scans 2-60 and 135-220:** pointed genus-one curves in characteristic p, Hasse-Witt and the Cartier operation, connections and Gauss-Manin, the Schwarzian and p-curvature, and the Dieudonné-crystal programme (the Montreal notes, Ch. V). Also Wanderley's offprint on orientation, a typescript on operator semigroups, and reused administrative typescripts.

Cote 91 is split with SA02 (scans 2-18), and cote 93 with SA01 (scans 92-134) and SA04 (scans 47-91, 219-236).

Heavy notes: the Pro packages MPL_91_019-058, MPL_91_059-098, MPL_91_099-143, MPL_93_002-046 (GPT-6 Astra, ChatGPT Pro mode). Light notes: Work and Codex K91-02..10, K93-01..08.

Piece of sweep 2 part 2: `sweep2/REPORTS/cote93_scan052_exercise_22a.md`.
'''
ORDER = [
 ('Deformations, representability and descent (cote 91, scans 19-98)', ['SA03-1', 'SA03-2', 'SA03-3', 'SA03-4', 'SA03-6']),
 ('Constructible topology, Greenberg-Néron and jets (cote 91, scans 99-143)', ['SA03-7', 'SA03-9', 'SA03-10']),
 ('Characteristic p: curves, the Cartier operation and connections (cote 93)', ['SA03-11', 'SA03-12', 'SA03-18', 'SA03-14']),
 ('Crystals (cote 93, scans 37-60)', ['SA03-16', 'SA03-21', 'SA03-15']),
 ('Other mathematics on reused leaves', ['SA03-8', 'SA03-13', 'SA03-19']),
 ('Documentary and apparatus', ['SA03-20', 'SA03-5', 'SA03-17']),
]
DEPS = [
 ('SA03-2', 'SA03-1', 'his page', '91/19-34: representability of Hom, Isom and Aut uses the lifting and obstruction theory'),
 ('SA03-3', 'SA03-2', 'his page', '91/34-50: the projective immersion and descent serve representability'),
 ('SA03-6', 'SA03-4', 'his page', '91/59-98: the étale envelope uses the finite étale and infinitesimal comparisons'),
 ('SA03-9', 'SA03-7', 'his page', '91/118-136: the Greenberg functor uses constructible subsets, images and finite partitions'),
 ('SA03-9', 'SA03-10', 'his page', '91/131-142: finite-order evaluation gives the truncations of the Greenberg functor'),
 ('SA03-12', 'SA03-11', 'his page', '93/7-24: the Hasse invariant through the Cartier operation'),
 ('SA03-14', 'SA03-18', 'our note', '93/23-36: the Schwarzian and second-order equations through connections; p-curvature'),
 ('SA03-16', 'SA03-12', 'our note', '93/37-46: F and V on Dieudonné crystals beside the Cartier operation'),
 ('SA03-15', 'SA03-16', 'our note', 'the notes\' bridges to cotes 159 and 64 start from the crystal programme'),
 ('SA03-9', 'Greenberg (1961, 1963); Bosch-Lütkebohmert-Raynaud, Néron Models', 'our note', 'MPL_91_099-143 notes (literature named by the notes)'),
]
RELATED = [
 ('SA03-16', 'SA04-1', 'a proof (ours)', 'K93-07 re-reads MPL_93_047-091: Barsotti-Tate crystals (= H02H); Problem 4 follows Problems 1-3'),
 ('SA03-21', 'SA04-2', 'a proof (ours)', 'exercise 22 a) and b) on 93/052: the Banach-algebra exercises (= H02N)'),
 ('SA03-21', 'SA04-4', 'our note', 'the Euler characteristic of spheres by the hemisphere recurrence (93/58-60)'),
 ('SA03-14', 'SA04-7', 'our note', 'the Schwarzian on cote 93 (= H03D)'),
 ('SA03-14', 'SA01-32', 'our note', 'the Schwarzian and G_0 on scans 92-134'),
 ('SA03-18', 'SA04-11', 'our note', 'Gauss-Manin and Cartier across the cote (= H02J)'),
 ('SA03-2', 'SA02-12', 'our note', 'cote 91 split between SA02 and SA03'),
 ('SA03-9', 'SA04-40', 'our note', 'representability and gluing of functors (cote 102, "Pour EGA VI")'),
 ('SA03-6', 'SA04-40', 'our note', 'functors of local nature and the recollements of cote 102'),
 ('SA03-13', 'SA21-4', 'our note', 'orientation: Wanderley\'s axiomatic orientation and the orientation of networks in cote 156'),
]
RP = 'REPORTS/cote93_scan052_exercise_22a.md'
CLAIMS = [
 ['SA03-C1', 'D(s) = n D\'(s) (the set equation before the corollary on dimension nd)', '91/52', 'SA03-4', 'Hua VI p. 51 corrects it; Pro note C05 agrees with the page (sweep 1 passage read)', 'corrects (reversed as written)', 'our note (Hua credited)', 'sweep1/SA03/CHECK_EVENTS.tsv'],
 ['SA03-C2', 'exercise 22 a): ||u|| < C, ||uw - w|| < eta, 0 <= gamma <= 1/4C imply ||yw - w|| < epsilon, y = [(1 - gamma)e + gamma u]^-1', '93/052 (typed, struck)', 'SA03-21', 'my proof (||v^-1|| < 2, yw - w = -gamma v^-1 (uw - w)); the Work M52 refutes only the misreading ||yw - u||', 'proves (as typed)', 'a proof (ours)', RP],
 ['SA03-C3', 'Problem 4: the essential image of the restriction functor, a valuative criterion, a Zariski-open description in the Grassmannian', '93/49-51', 'SA03-16', 'none: an open question of his', 'open', 'his page', 'Work K93-07 #1; MPL_93_047-091 BT25-BT27'],
 ['SA03-C4', '"Pb à poser. Espaces de Néron!" in the six-item programme', '91/118', 'SA03-9', 'none: a programme item', 'open (programme)', 'his page', 'MPL_91_099-143 research lead #17'],
]
CORR = [
 ['SA03-K1', 'SA03-4', '91/52', 'his slip', 'D(s) = n D\'(s)', 'reversed (dimension nd, as his corollary has it)', 'Hua VI p. 51; Pro C05 (passage read in sweep 1)', 'passage read'],
 ['SA03-K2', 'SA03-21', '93/052', 'misreading in the transcriptions', '||yw - u|| < epsilon (Pro MPL_93_047-091 and Work K93-07)', '||yw - w|| < epsilon', 'glyph comparison on the scan at 400 dpi; the statement as typed proved', 'scan image and proof'],
 ['SA03-K3', 'SA03-21', 'work:K93-07#6 (M52)', 'note corrected', 'M52: the printed wording is refuted at u = 1, w = 0', 'M52 refutes the misreading only; S52\'s intended reading is the typed text', 'the scan', 'scan image'],
 ['SA03-K4', 'SA03-16', 'K93-07 (cote 93 scans 47-60)', 'placement', 'filed under SA03', 'a second reading of SA04\'s MPL_93_047-091 (H02H, H02N, SA04-4)', 'sweep 2 part 1', 'placement'],
]
CHECKS3 = [
 ['work:K93-07#6', 'reading checked on the scan image (93.pdf p. 52, rotated, 400 dpi; glyph comparison with "u" and "w" in the line above)', 'the typescript reads ||yw - w||: the Work transcription misreads w as u; S52 agrees with the ink; M52 refutes the misreading', '93.pdf page 52'],
 ['work:K93-07#6', 'claim checked by proof (exercise 22 a) as typed)', 'proved: ||v^-1|| < 2 and yw - w = -gamma v^-1 (uw - w), so ||yw - w|| < eta; eta = epsilon will do', RP],
]
