# Sweep 2 part 2, SA04 (cotes 93, 98, 161; Work-only cotes 69-102): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
DATE = '2026-11-18'
TITLE = 'SA04: crystals and the cote 93 strands; combinatorial geometry of cotes 69-89; descent and local cohomology of cotes 94-102'
INTRO = '''
The topic is "Géométrie et topologie combinatoire", part 2. It has three layers:
- **Cote 93, scans 47-91 and 219-236, with cote 161:** Barsotti-Tate crystals and p-adic representations, the Schwarzian and projective connections, periods, the Euler characteristic axioms and typed analysis exercises.
- **Cotes 69-89 (Work and Codex notes only):** graphs, polygons and polyhedra over rings, quadratic forms and orthogonal groups, triangle groups.
- **Cotes 94-102:** descent, including the draft "Pour EGA VI" of cote 102; local cohomology (dated 1958); Hilbert schemes; Chern classes.

Heavy notes: the Pro packages MPL_93_047-091, MPL_93_221-236+161-5, MPL_98 (GPT-6 Astra, ChatGPT Pro mode). Light notes: 102 Work folders and 98 Codex folders on cotes 69-102.

Pieces of sweep 2 part 2: `sweep2/REPORTS/cote93_scan052_exercise_22a.md` and `sweep2/REPORTS/cote102_pour_EGA_VI.md`.
'''
ORDER = [
 ('Crystals, p-adic representations and good reduction (cotes 93, 100, 161)', ['SA04-1', 'SA04-3', 'SA04-14', 'SA04-15', 'SA04-13', 'SA04-16', 'SA04-38']),
 ('Projective connections, the Schwarzian, uniformization and periods (cote 93)', ['SA04-7', 'SA04-8', 'SA04-9', 'SA04-11', 'SA04-12']),
 ('Topology and analysis on cote 93', ['SA04-4', 'SA04-6', 'SA04-2']),
 ('Combinatorial geometry: graphs, polygons and polyhedra (cotes 69-89)', ['SA04-20', 'SA04-21', 'SA04-22', 'SA04-23', 'SA04-24', 'SA04-26', 'SA04-27', 'SA04-28', 'SA04-31', 'SA04-32', 'SA04-33', 'SA04-34', 'SA04-35']),
 ('Quadratic forms and orthogonal groups over rings (cotes 77, 82)', ['SA04-25', 'SA04-30']),
 ('Algebraic geometry: descent, local cohomology, Hilbert schemes, Chern classes (cotes 94-102)', ['SA04-36', 'SA04-40', 'SA04-39', 'SA04-17', 'SA04-37']),
 ('Documentary and apparatus', ['SA04-5', 'SA04-18', 'SA04-29', 'SA04-41', 'SA04-10']),
]
DEPS = [
 ('SA04-3', 'SA04-1', 'our note', '93/55, 83: p-adic representations through the crystals of Barsotti-Tate groups'),
 ('SA04-15', 'SA04-1', 'his page', 'cote 161 sheets: filtered modules for Barsotti-Tate groups'),
 ('SA04-13', 'SA04-1', 'his page', '93/231-236: formal de Rham data toward the crystal construction'),
 ('SA04-38', 'SA04-1', 'his page', 'cote 100: good reduction of abelian varieties through their Barsotti-Tate groups'),
 ('SA04-14', 'SA04-3', 'our note', 'cote 161-5: the Hodge-Tate grading and Sen\'s theorem on the p-adic side'),
 ('SA04-8', 'SA04-7', 'his page', '93/36-86: the uniformization diagrams use the Schwarzian'),
 ('SA04-9', 'SA04-7', 'his page', '93/86-90: opers normalized by the Schwarzian'),
 ('SA04-11', 'SA04-9', 'our note', 'the notes\' Gauss-Manin and p-curvature comparisons for projective connections'),
 ('SA04-12', 'SA04-11', 'our note', '93/219-230: Picard-Fuchs from logarithmic differentials beside Gauss-Manin'),
 ('SA04-31', 'SA04-30', 'his page', 'cote 85 "Sous-groupes finis de GP(1)" after cote 82 "Dictionnaire lié à GP(1) = SO(3)"'),
 ('SA04-40', 'SGA 4 (sites, topos); EGA IV (étale, flat, henselian); SGA 1 VIII (fpqc descent)', 'his page', '102/3-14 (REPORTS/cote102_pour_EGA_VI.md)'),
 ('SA04-39', 'local cohomology, later SGA 2', 'our note', 'cote 101 notes, headed "Notes antiques" and 1958'),
 ('SA04-2', 'Cohen\'s factorization theorem (1959)', 'a proof (ours)', '93/052: 22 b) is the theorem, 22 a) its lemma (REPORTS/cote93_scan052_exercise_22a.md)'),
]
RELATED = [
 ('SA04-24', 'SA04-21', 'my inference', 'cellular maps and cartographic groups beside the regular polyhedra'),
 ('SA04-32', 'SA04-21', 'my inference', 'the course "Polyèdres réguliers" (cote 86) beside the n-polyhedra of cote 70'),
 ('SA04-21', 'SA04-26', 'my inference', 'regular polygons (cote 78) as the faces of regular polyhedra (cote 70)'),
 ('SA04-34', 'SA04-20', 'my inference', 'maps from root systems (cote 88) and E6 with the 27 lines (cote 69)'),
 ('SA04-40', 'SA04-36', 'a proof (ours)', 'the same programme of descent through representing functors (cotes 94, 102)'),
 ('SA04-25', 'SA02-1', 'our note', 'quadratic extensions and discriminants (cote 77) beside the quadratic algebras of cote 84'),
 ('SA04-28', 'SA11-8', 'our note', 'pseudoline systems (cote 80) and the relative-position surface (cote 154)'),
 ('SA04-21', 'SA01-1', 'our note', 'pinned regular realizations (cote 72; = H00W)'),
 ('SA04-1', 'SA03-16', 'our note', 'the crystal programme on scans 37-46 (= H024)'),
 ('SA04-7', 'SA01-32', 'our note', 'the Schwarzian and G_0 on scans 92-134 (= H03D)'),
 ('SA04-9', 'SA01-31', 'our note', 'projective connections on scans 92-134 (= H03F)'),
]
CLAIMS = [
 ['SA04-C1', 'the test value G_0(t, t^2) = dt^2/(2t)', '93/073', 'SA04-7', 'Hasse derivatives give dt^2/(4t^2) (sweep 1; Hua VI)', 'refutes his value', 'a proof (computation)', 'sweep1/SA04/CHECK_EVENTS.tsv'],
 ['SA04-C2', '"On présume que epsilon = (-1)^m": B^2 - epsilon Delta = 0 mod 4, for the generic determinant Delta with doubled diagonal and B the sum over perfect matchings (n = 2m)', '77/069', 'SA04-25', 'expansion of the determinant over permutations mod 4 (sweep 2 part 1)', 'proves', 'a proof (ours)', 'sweep2/SA04/CHECK_EVENTS.tsv'],
 ['SA04-C3', 'exercise 22 a) as typed (the lemma of Cohen\'s factorization theorem)', '93/052', 'SA04-2', 'my proof; both transcriptions misread ||yw - w|| as ||yw - u||', 'proves (as typed)', 'a proof (ours)', 'REPORTS/cote93_scan052_exercise_22a.md'],
 ['SA04-C4', 'his cocycle parametrization of extensions, with the cohomology of Gamma and pi, as stated', '93 (cote 161 sheets)', 'SA04-16', 'Hua\'s rank-one counterexample, verified by the Pro notes', 'refutes as stated (Hua credited)', 'our note', 'MPL_93_221-236+161-5 notes'],
 ['SA04-C5', 'uniqueness of the Euler characteristic under his axioms', '93/27-68', 'SA04-4', 'none', 'open (left open by him)', 'his page', 'MPL_93_047-091 notes'],
 ['SA04-C6', '"J\'ignore s\'il existe une structure de 2-polyèdre régulier ..."', '79/115-116', 'SA04-27', 'none', 'open (his question)', 'his page', 'codex:K79-08#1'],
 ['SA04-C7', 'the loop-space question: when the first class vanishes', '93/83', 'SA04-6', 'the notes give a model with a nonzero class', 'answers (the notes; not checked here)', 'our note', 'MPL_93_047-091 notes'],
]
CORR = [
 ['SA04-K1', 'SA04-7', '93/073', 'his slip (a test value)', 'G_0(t, t^2) = dt^2/(2t)', 'dt^2/(4t^2), up to sign', 'Hasse derivatives; Hua VI', 'computation'],
 ['SA04-K2', 'SA04-2', '93/052', 'misreading in the transcriptions', '||yw - u|| < epsilon', '||yw - w|| < epsilon', 'glyph comparison on the scan at 400 dpi', 'scan image'],
 ['SA04-K3', 'SA04-2', 'MPL_93_047-091 BT29-BT54', 'note label corrected', 'filed as Barsotti-Tate', 'typed exercises on pseudo-resolvents and Banach algebras (22 b) is Cohen\'s factorization theorem)', 'sweep 1 and the scan', 'our reading'],
 ['SA04-K4', 'SA04-40', 'cote 102', 'placement', 'combinatorial geometry (archive section 11)', 'descent and the EGA themes (Part III), with SA04-36', 'REPORTS/cote102_pour_EGA_VI.md', 'placement'],
 ['SA04-K5', 'SA04-41', 'reused sheets of cotes 69-80', 'dating', 'undated notes', 'terminus post quem about 1975-1981 from the reused sheets', 'Codex title-sheet entries', 'our reading'],
 ['SA04-K6', 'SA04-1', 'K93-07 (SA03), K93-13 and MPL_93_092-134 (SA01)', 'placement', 'filed under SA03 and SA01', 'cote 93 strands of SA04 (H02H, H00B, H00C, H03D, H03E, H03F, H0JE, H02J)', 'sweep 2 part 1', 'placement'],
]
CHECKS3 = [
 ['MPL_93_047-091 transcription, scan 52', 'transcription checked against the scan image (93.pdf p. 52, rotated, 400 dpi)', 'misreads: the type has ||yw - w||, the transcription ||yw - u||', '93.pdf page 52'],
 ['codex:K102-01#2', 'reading checked on the scan image (102.pdf p. 3)', 'agrees: typed "Pour EGA VI" above "Recollements d\'objets d\'un site."', '102.pdf page 3'],
 ['codex:K102-01#2', 'reading checked on the scan image (102.pdf p. 9, 200 dpi)', 'agrees: the underlined heading "Questions pour Artin"', '102.pdf page 9'],
]
