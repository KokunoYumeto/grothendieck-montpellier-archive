# Sweep 2 part 2, SA21 (cote 156): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
DATE = '2026-11-18'
TITLE = 'SA21: Vers une géométrie des formes (cote 156)'
INTRO = '''
The topic is cote 156, in nine parts:
- **156-1 and 156-2 (Pro package MPL_156-1+156-2):** forms, one-dimensional models and their axioms F1-F6, networks, ficelles, cuttings, rives and mailles.
- **156-3 to 156-9:** the dated 1986 series marked GF (or CF) III to IX bis, from 8 June to 15 July 1986:
  - 156-3: networks via cuttings;
  - 156-4: "Analysis situs (première mouture)", with the contrées;
  - 156-5: "Sorite ensembliste";
  - 156-6: "Analysis situs (deuxième mouture)", with the ateliers;
  - 156-7: "Analysis Situs (troisième mouture)" (Chap VII);
  - 156-8: magasins and oriented multistrata;
  - 156-9: morphisms of ateliers.

The 1986 series is read so far only by the Codex notes on the sheets: the steps marked unverified, and the title sheets. Reused Récoltes et Semailles typescript leaves (1985 and May 1986) lie in 156-8 and 156-9.
'''
ORDER = [
 ('Forms and one-dimensional models (156-1)', ['SA21-1', 'SA21-2', 'SA21-3', 'SA21-4']),
 ('Ficelles, cuttings, rives and mailles (156-2)', ['SA21-5', 'SA21-6', 'SA21-7']),
 ('The 1986 series: from networks to ateliers and magasins (156-3 to 156-9)', ['SA21-12', 'SA21-13', 'SA21-14', 'SA21-10', 'SA21-15']),
 ('The programme questions put to the pages (the notes\')', ['SA21-8']),
 ('Documentary and apparatus', ['SA21-11', 'SA21-9']),
]
DEPS = [
 ('SA21-2', 'SA21-1', 'his page', '156-1: one-dimensional models as the first case beyond dimension zero'),
 ('SA21-3', 'SA21-2', 'his page', '156-1/013-022: the filtering axiom F6 on segments and branches'),
 ('SA21-4', 'SA21-2', 'his page', '156-1: networks built from segments; divisible and reduced cases'),
 ('SA21-4', 'SA21-3', 'his page', '156-1: the order reconstruction uses the filtering axioms'),
 ('SA21-5', 'SA21-4', 'his page', '156-2: ficelles realize one-dimensional models by regular immersions'),
 ('SA21-6', 'SA21-5', 'his page', '156-2/007-019: cuttings along separating lieux of ficelles'),
 ('SA21-7', 'SA21-6', 'his page', '156-2/015-019: rives as germs of the sides of a cut; mailles'),
 ('SA21-12', 'SA21-6', 'his page', '156-3 (sheet III, 8 June 1986): "Réseaux ... via découpages"'),
 ('SA21-13', 'SA21-12', 'our note', '156-4 (sheet IV): Analysis situs, première mouture, after sheet III'),
 ('SA21-10', 'SA21-13', 'our note', '156-6 and 156-7: the deuxième and troisième moutures replace the contrées by ateliers'),
 ('SA21-15', 'SA21-10', 'our note', '156-8 (CF VIII): homomorphisms of magasins and ateliers; polyhedral ateliers'),
 ('SA21-15', 'SA21-6', 'our note', '156-8: "Axiomes pour les Lieux", "Recollement des raffinements"'),
]
RELATED = [
 ('SA21-8', 'SA21-1', 'our note', 'P01: the README conjecture is not on these pages'),
 ('SA21-10', 'SA10-2', 'our note', '"multiombre" and "ombres": the requested question on tubulure and ombre (H05G)'),
 ('SA21-12', 'SA11-3', 'our note', '"Partie fermée modérée": the tame line of cotes 120-121'),
 ('SA21-5', 'SA10-7', 'our note', 'conical neighbourhoods and collars (MPL_150_001-043 Q1b)'),
 ('SA21-11', 'SA02-6', 'our note', 'the Récoltes et Semailles typescript, also reused in cote 84 (= H01T)'),
 ('SA21-4', 'SA03-13', 'our note', 'orientation: the orientation theorem of 156-1 and Wanderley\'s offprint'),
]
CLAIMS = [
 ['SA21-C1', 'arbitrary restriction of a segment structure (asserted, not proved; his own warning on 008: "on n\'affirme pas égalité!")', '156-1/010', 'SA21-2', 'MPL_156-1+156-2#28 (A12): a counterexample of the notes; #29 (A13): a repair by closure under required gluings', 'refutes (the notes; not checked here); refines', 'our note', 'MPL_156-1+156-2_notes.md A12, A13'],
 ['SA21-C2', 'the passage from local to global filtering', '156-1/021-022', 'SA21-3', 'withdrawn by him; #38 (A22): a branching-order counterexample confirming the withdrawal', 'withdrawn (his); confirmed by the notes', 'his page', 'MPL_156-1+156-2_notes.md A21, A22'],
 ['SA21-C3', 'the orientation theorem for networks', '156-1/018', 'SA21-4', 'none: explicitly unverified by him', 'open (his own flag)', 'his page', 'MPL_156-1+156-2_notes.md A17'],
 ['SA21-C4', 'endpoint enlargement of ficelles; the universal equivalence of oriented structures', '156-2/011', 'SA21-5', 'withdrawn by him; #72 (B27): a tripod explains the obstruction', 'withdrawn (his)', 'his page', 'MPL_156-1+156-2_notes.md B26-B28'],
 ['SA21-C5', 'the local strict inequality on 019 ("si x <= y,z" ... "x < u < y,z")', '156-1/019', 'SA21-3', 'none; inconsistent as written for x = y; the strict version at 013', 'suspected misreading or his slip (open)', 'our note', 'MPL_156-1+156-2_notes.md A20'],
 ['SA21-C6', 'W\'_t = X - V_t, with V_t in X/A', '156-2/003', 'SA21-5', 'none; W_t would be type-correct', 'suspected misreading or his slip (open)', 'our note', 'MPL_156-1+156-2_notes.md B04'],
 ['SA21-C7', 'the end of the proof of the first three ficelle conditions: "X - {c} ne serait pas connexe"', '156-2/006', 'SA21-5', 'none; the target is X - {a}', 'suspected misreading or his slip (open)', 'our note', 'MPL_156-1+156-2_notes.md B10'],
]
CORR = [
 ['SA21-K1', 'SA21-3', '156-1/019', 'suspected misreading or his slip (open)', 'si x <= y,z ... x < u < y,z', 'the strict antecedent of 013', 'A20', 'not decided (scan not viewed)'],
 ['SA21-K2', 'SA21-5', '156-2/003', 'suspected misreading or his slip (open)', 'W\'_t = X - V_t', 'W\'_t = X - W_t', 'B04', 'not decided (scan not viewed)'],
 ['SA21-K3', 'SA21-5', '156-2/006', 'suspected misreading or his slip (open)', 'X - {c} ne serait pas connexe', 'X - {a}', 'B10', 'not decided (scan not viewed)'],
 ['SA21-K4', 'SA21-10', 'MPL_156-1+156-2 D16', 'note answered by later pages', 'no definition of an atelier on 156-1 and 156-2', 'ateliers are defined and used in 156-6, 156-7 and 156-9 (Codex notes)', 'sweep 1 and sweep 2 part 1', 'our reading'],
 ['SA21-K5', 'SA21-11', 'cote 156 series', 'dating', 'the GF series dated 8 June to 12 July 1986 (sweep 1)', 'to 15 July 1986 (GF IX, J156-9-01); third mouture 23 June (H156-01)', 'Codex title-sheet entries', 'our reading'],
 ['SA21-K6', 'SA21-8', 'MPL_156-1+156-2 P01', 'framing', 'the README reads a form as a tame space recovered from a pro-object of finite posets or categories', 'not on these pages (our framing): finite chains of cuts, no category of refinements, no reconstruction theorem', 'P01', 'our note'],
]
CHECKS3 = []
