# Sweep 2 part 2, SA01 (cotes 71-72, 75, 81, 83, 84, 90, 93, 97; cote 154 scans 46-76): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
DATE = '2026-11-18'
TITLE = 'SA01: regular polyhedra over rings, 2x2 matrices and traces, plane topology, and the cote 93 uniformization notes'
INTRO = '''
The topic is "Géométrie et topologie combinatoire", part 1. Its subjects, by cote:
- **Cote 72:** pinned regular realizations of the regular polyhedra over rings.
- **Cote 83:** 2x2 matrices, traces and quadratic algebras: the trace identity for triples, the trace cube and its determinants, Azumaya algebras.
- **Cote 81 and cote 154, scans 46-76:** immersions of the disc and pseudoline arrangements. The shared package belongs to SA11.
- **Cotes 71 and 75:** plane polygons, C. Contou-Carrère's Jordan-theorem manuscript and the DEA course "Géométries combinatoires".
- **Cote 93, scans 92-134 (from sweep 2):** projective connections, the Schwarzian and uniformization; with K93-13, periods and the canonical de Rham connection.

Several folders filed here belong with SA02 or SA04 by object: K84-10, K90-02, K93-13 and MPL_93_092-134. Their items carry the global tags of those objects.

Heavy notes: the Pro packages MPL_72, MPL_81_038-055+154_046-076, MPL_83_*, MPL_93_092-134 (GPT-6 Astra, ChatGPT Pro mode). Light notes: Work and Codex K72, K83, K84-10, K90-02, K93-13, J71, J75, J81, H97.

Piece of sweep 2 part 2: `sweep2/REPORTS/cote93_scans100_113_117_slips.md`.
'''
ORDER = [
 ('Regular polyhedra and their realizations over rings (cotes 72, 75, 83)', ['SA01-1', 'SA01-3', 'SA01-4', 'SA01-6', 'SA01-27', 'SA01-16', 'SA01-41']),
 ('Quadratic algebras, traces and 2x2 matrices (cotes 83, 84, 90)', ['SA01-28', 'SA01-17', 'SA01-36', 'SA01-18', 'SA01-23', 'SA01-19', 'SA01-20', 'SA01-21', 'SA01-22', 'SA01-38']),
 ('Plane topology, pseudolines and immersions (cotes 71, 81, 154)', ['SA01-40', 'SA01-9', 'SA01-10', 'SA01-11', 'SA01-12', 'SA01-29']),
 ('Projective connections, the Schwarzian and uniformization (cote 93)', ['SA01-31', 'SA01-32', 'SA01-33', 'SA01-34', 'SA01-35']),
 ('The requested LM bridge (a question the notes put to the pages)', ['SA01-2']),
 ('Typescripts and documentary', ['SA01-39', 'SA01-42', 'SA01-37', 'SA01-24', 'SA01-7', 'SA01-15', 'SA01-26', 'SA01-43']),
 ('Reading questions and apparatus', ['SA01-5', 'SA01-8', 'SA01-30']),
]
DEPS = [
 ('SA01-3', 'SA01-1', 'his page', '72: the invariant quadratic form of the reflection realization of the pinned polyhedron'),
 ('SA01-4', 'SA01-3', 'our note', '72/45-57: determinants and recurrences of the realization\'s matrices (MPL_72 notes)'),
 ('SA01-6', 'SA01-3', 'his page', '72/35-36: alpha_i = 4cos^2 theta_i from the invariant form'),
 ('SA01-16', 'SA01-27', 'our note', '83/63-64, 571: bi-icosahedra from the icosahedral group over Z/5'),
 ('SA01-41', 'SA01-1', 'our note', 'cote 75: the course treats regular realizations of combinatorial polygons (Codex J75 notes)'),
 ('SA01-17', 'SA01-28', 'his page', '83/178-180: lambda-split extensions of quadratic algebras and their product'),
 ('SA01-18', 'SA01-28', 'his page', '83/245: the trace form of a quadratic algebra in characteristic two'),
 ('SA01-23', 'SA01-18', 'his page', '83/245-258: Azumaya algebras recovered from traces, compared with P^1-bundles'),
 ('SA01-20', 'SA01-19', 'his page', '83/183-190: the trace identity is a relation among the invariants of triples'),
 ('SA01-21', 'SA01-20', 'his page', '83/194-219: the trace cube of four matrix variables'),
 ('SA01-22', 'SA01-21', 'his page', '83/211, 219: the determinants of the trace-cube systems'),
 ('SA01-10', 'SA01-9', 'his page', '154/46-76: the local gluing of the relative-position surface'),
 ('SA01-11', 'SA01-10', 'his page', '154/65: polygon transport along edges and its dihedral monodromy'),
 ('SA01-12', 'SA01-9', 'his page', '154/69: the natural-map schemes on the surface'),
 ('SA01-32', 'SA01-31', 'his page', '93/97-114: the Riccati coordinate lambda of a projective connection gives the Schwarzian equation G_t(s) = mu'),
 ('SA01-33', 'SA01-31', 'his page', '93/126-134: the canonical projective bundle with connection and transverse section'),
 ('SA01-33', 'SA01-32', 'his page', '93/114-115: the uniformizing equation G_t(s) = mu'),
 ('SA01-34', 'SA01-32', 'our note', 'MPL_93_092-134 F02-F05: Frobenius rigidity of G_0 against p-curvature'),
 ('SA01-34', 'SA01-33', 'our note', 'MPL_93_092-134 F07-F10: the Legendre family and Gauss-Manin'),
 ('SA01-31', 'EGA IV 16 (principal parts)', 'our note', 'the principal-parts sequence of 93/093-095 (MPL_93_092-134 A02, E15)'),
 ('SA01-33', 'GAGA; Deligne, Équations différentielles à points singuliers réguliers, II.5.9', 'our note', 'MPL_93_092-134 B15-B17, E12 (algebraization)'),
 ('SA01-39', 'EGA IV sections 17-18', 'his page', 'cote 90 typed references'),
 ('SA01-2', 'SA01-1', 'our note', 'MPL_72 B5: the bridge asks for level-n regular maps through pinned realizations; the leaves do not supply it'),
]
RELATED = [
 ('SA01-36', 'SA01-17', 'our note', 'the chi-trivialised extensions of cote 84 (= H01R) beside the lambda-split extensions of cote 83 (= H00Z)'),
 ('SA01-12', 'SA01-29', 'our note', 'immersions of the disc (cote 81) and the immersion schemes of cote 154'),
 ('SA01-40', 'SA01-41', 'our note', 'plane polygons in cote 71 and the course of cote 75'),
 ('SA01-35', 'SA01-31', 'our note', 'periods and Gauss-Manin beside projective connections on cote 93'),
]
P = 'MPL_93_092-134#'; RPT = 'REPORTS/cote93_scans100_113_117_slips.md'
CLAIMS = [
 ['SA01-C1', 'the determinant of the trace-cube system on 219 is 27^2 - 1 = 728', '83/219', 'SA01-22', 'Pro C19, Work K83-14 and Hua XIII: 512 (with -1 in the corner; +1 gives 384 = 2^7 x 3, against his "premier à 3")', 'refutes his value', 'a proof (computation)', 'sweep1/SA01/CHECK_EVENTS.tsv'],
 ['SA01-C2', 'tr(xyz) tr(xzy) as he writes it, without the term -4cc\'c\'\'', '83/183-186', 'SA01-19', 'the identity with -4cc\'c\'\' checked on 300 random integer triples (sweep 1)', 'refines (adds the missing term)', 'a proof (computation)', 'sweep1/SA01/CHECK_EVENTS.tsv'],
 ['SA01-C3', '2(2cos^2 theta_i + 1) = 4cos 2theta_i as transcribed', '72/036', 'SA01-6', 'false as transcribed; "+1" against "-1" (Pro A15, Work S36)', 'suspected misreading, open (scan not viewed)', 'our note', 'sweep1/SA01/FLAGS.tsv'],
 ['SA01-C4', 'D(f dt) = a df/dt + b', '93/100', 'SA01-31', 'ink read on the scan: no f; a linear operator needs + b f', 'corrects his slip', 'scan image', RPT],
 ['SA01-C5', 's\' = c exp Lambda(t), between log s\' = -Lambda + c and s = c int exp(-Lambda)', '93/113', 'SA01-32', 'ink read on the scan: no minus', 'corrects his slip', 'scan image', RPT],
 ['SA01-C6', 'H = GP(1,C) as invertible matrices "mod. matrices diagonales"', '93/117', 'SA01-32', 'ink read on the scan; the Möbius group is modulo scalars', 'corrects his slip', 'scan image', RPT],
 ['SA01-C7', 'G(t,s) = 12 G_0(t,s), the integral invariant defined without dividing by 12', '93/121-122', 'SA01-32', P + '46 (D01), checked by hand with Hasse derivatives (sweep 2 part 1)', 'proves', 'a proof (computation)', 'sweep2/SA01/CHECK_EVENTS.tsv'],
 ['SA01-C8', 'the constants of D(1), D(2), D(3) in small characteristic', '93/122', 'SA01-32', P + '49 (D04): A[t^p], A[t^4], A[t^9], checked by Lucas\'s theorem', 'proves', 'a proof (computation)', 'sweep2/SA01/CHECK_EVENTS.tsv'],
 ['SA01-C9', 'Pic(A) = 0 gives a matrix with ad - bc = 1', '93/122', 'SA01-32', P + '54 (D09): Hua\'s counterexample s = 2t in A[t]/t^5 over F_5; ' + P + '59 (D14): in odd characteristic the Picard hypothesis can be removed in this model', 'refutes; refines', 'our note (Hua credited)', 'MPL_93_092-134_notes.md D09, D14'],
 ['SA01-C10', 'Theorem 1: a homogeneous simply connected Riemann surface is of the three uniformization types, as written ("homogène")', '93/126', 'SA01-33', P + '60 (E01): C* is homogeneous but neither simply connected nor of the three types', 'refutes the wording; refines', 'our note', 'MPL_93_092-134_notes.md E01'],
 ['SA01-C11', 'PGL_2(R) = SL_2(R)/{+-1} for the disc stabilizer', '93/126-127', 'SA01-33', P + '61 (E02): false on real points; the stabilizer is the identity component', 'refutes; refines', 'our note', 'MPL_93_092-134_notes.md E02'],
 ['SA01-C12', 'H \\ P_{P^1} is "le faisceau final"', '93/119', 'SA01-32', P + '40 (C04): t and t^2 on G_m are both local coordinates; the local sheaf is not final', 'refutes', 'our note', 'MPL_93_092-134_notes.md C04'],
 ['SA01-C13', '"Sont-elles algébriques ?": algebraicity of the uniformizing connection', '93/115', 'SA01-33', P + '34 (B17): yes for a fixed finite-type complex curve (cusp uniformization, GAGA); ' + P + '33 (B16), ' + P + '85 (F06): not holomorphic in families', 'answers (the notes; not checked here)', 'our note', 'MPL_93_092-134_notes.md B16, B17, F06'],
 ['SA01-C14', 'G(t,s) = 0 implies s = g o t ("lisse/S ??", "à vérifier !")', '93/121', 'SA01-32', P + '43 (C07): holds over a characteristic-zero field; the relative hypotheses stay open', 'proves in part (the notes)', 'our note', 'MPL_93_092-134_notes.md C07'],
 ['SA01-C15', '"prouver (ou l\'infirmer !)": the formal data determine an algebraic realization', '93/130-132', 'SA01-33', P + '70 (E11): x exp(w) has algebraic coefficients and a transcendental realization', 'refutes the naive form (the notes)', 'our note', 'MPL_93_092-134_notes.md E11'],
 ['SA01-C16', 'the developing equations lambda = -s\'\'/s\', G_t(s) = mu and the linearization', '93/114', 'SA01-32', P + '29 (B12) and ' + P + '30 (B13), checked by hand', 'proves', 'a proof (computation)', 'sweep2/SA01/CHECK_EVENTS.tsv'],
 ['SA01-C17', 'the uniformizing coefficient of P^1 minus three points', '93/115', 'SA01-33', P + '35 (B18): mu = -(z^2 - z + 1)/(z^2 (z-1)^2), checked against the classical formula', 'proves', 'a proof (computation)', 'sweep2/SA01/CHECK_EVENTS.tsv'],
]
CORR = [
 ['SA01-K1', 'SA01-31', '93/100', 'his slip', 'D(f dt) = a df/dt + b', 'D(f dt) = a df/dt + b f', 'ink read on the scan (300 dpi); A09; Hua VIIb', 'scan image'],
 ['SA01-K2', 'SA01-32', '93/113', 'his slip', 's\' = c exp Lambda(t)', 's\' = c exp(-Lambda(t))', 'ink read on the scan (300 dpi); B11; scan 114', 'scan image'],
 ['SA01-K3', 'SA01-32', '93/117', 'his slip of wording', 'mod. matrices diagonales', 'mod. matrices scalaires (H = PGL_2(C))', 'ink read on the scan (300 dpi); C03', 'scan image'],
 ['SA01-K4', 'SA01-22', '83/219', 'his arithmetic', '27^2 - 1 = 728', '512 (first reading -1 in the corner)', 'Pro C19, Work K83-14, Hua XIII', 'computation (three witnesses)'],
 ['SA01-K5', 'SA01-19', '83/183-186', 'his omission', 'tr(xyz) tr(xzy) without -4cc\'c\'\'', 'Pi - 4cc\'c\'\'', '300 random integer triples (sweep 1)', 'computation'],
 ['SA01-K6', 'SA01-6', '72/036', 'suspected misreading (open)', '2(2cos^2 theta_i + 1) = 4cos 2theta_i', 'with -1 the identity holds', 'Pro A15, Work S36', 'not decided: the scan was not viewed'],
 ['SA01-K7', 'SA01-32', '93/102', 'his statement corrected (the notes)', 'D_{u_M(t)} = D_t', 'c_{D_s} = c_{D_t} (the affine connections differ under inversion)', P + '18 (B01)', 'our note'],
 ['SA01-K8', 'SA01-31', '93/107', 'his slip (the notes)', 'the change of reference connection without a factor 2', 'with the factor 2: F changes by 2 eta eta-bar', P + '19 (B02)', 'our note'],
 ['SA01-K9', 'SA01-32', '93/114', 'refinement (the notes)', 'the pure-weight coordinate-change formula for G', 'with the inhomogeneous term G_t(t~)', P + '31 (B14)', 'our note'],
 ['SA01-K10', 'SA01-32', '93/122', 'refinement (the notes, Hua credited)', 'Pic(A) = 0 gives ad - bc = 1', 'false (s = 2t over F_5); in odd characteristic the Picard hypothesis can be dropped in this model', P + '54, ' + P + '59', 'our note'],
 ['SA01-K11', 'SA01-33', '93/126-127', 'refinement (the notes)', 'the homogeneity theorem and PGL_2(R) = SL_2(R)/{+-1}', 'simply connected; the identity component', P + '60, ' + P + '61', 'our note'],
 ['SA01-K12', 'SA01-31', 'MPL_93_092-134, K84-10, K90-02, K93-13', 'placement', 'filed under SA01', 'objects of SA04 (H03D, H03E, H03F, H0JE, H02J, H00B, H00C) and SA02 (H01R, H01T, H01J, H01K)', 'sweep 2 part 1', 'placement'],
 ['SA01-K13', 'SA01-9', 'MPL_81_038-055+154_046-076', 'placement', 'indexed under SA01 and SA11', 'cote 154, scans 46-76: SA11', 'sweep 1', 'placement'],
]
CHECKS3 = [
 [P + '11', 'reading checked on the scan image (93.pdf p. 100, 300 dpi)', 'agrees with the frozen reading: D(f dt) = a df/dt + b, no f; his slip', '93.pdf page 100'],
 [P + '28', 'reading checked on the scan image (93.pdf p. 113, 300 dpi)', 'agrees with the frozen reading: s\' = cte exp Lambda(t), no minus; his slip', '93.pdf page 113'],
 [P + '39', 'reading checked on the scan image (93.pdf p. 117, 300 dpi)', 'agrees with the frozen reading: "mod. matrices diagonales"; his slip of wording', '93.pdf page 117'],
]
