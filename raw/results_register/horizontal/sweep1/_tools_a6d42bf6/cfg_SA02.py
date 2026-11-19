# SA02 Géométrie et topologie combinatoire (cotes 84, 90, 91): placement config (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
DATE = '2026-11-18'
A, B, N = 'MPL_84_097-145', 'MPL_84_146-193', 'MPL_90+91_002-018'
ITEMS = [
 ('SA02-1', 'the product of two quadratic algebras: u = 2u_1u_2 + b_2u_1 + b_1u_2, the rank-four tensor product and its quadratic subalgebra', 'construction/identity',
  'ours: for u_i^2 + b_iu_i + c_i = 0, u satisfies u^2 + b_1b_2u + b_1^2c_2 + b_2^2c_1 - 4c_1c_2 = 0 over any base ring, and the discriminant is multiplicative (classical product of quadratic algebras)', 'stated and calculated; identity correct (checked)'),
 ('SA02-2', 'relative trace and norm for quadratic algebras ("quasi-quadratic" algebras): definition, uniqueness, transitivity, base change, axioms', 'definition/proposition',
  'his: axioms for a norm and trace of A over a base k, possibly non-flat or non-faithful; ours: the five-axiom list and the earlier list differ (A20 counterexample)', 'stated; several steps under faithfulness only'),
 ('SA02-3', 'three quadratic algebras: the contracted triple product, the even subgroup of F_2^3, fixed ring vs scalar image, the étale case and the universal map', 'construction/conjecture',
  'his: a triple of quadratic algebras with product-one involutions and their contracted product; ours: fixed ring and scalar image differ in characteristic two', 'programme; partly proved, partly conjectured'),
 ('SA02-4', 'extensions of invertible modules with a chi-trivialisation: the product of extensions, splitting changes, cocycles and the "strange signs"', 'construction',
  'his: for extensions 0 -> L_i -> E_i -> M_i -> 0 with scalar chi, a product extension and comparison maps; ours: the canonicity needs choices compatible across splitting changes', 'worked over many sheets; conditional, with self-flagged questions'),
 ('SA02-5', 'the requested LM bridge B12: quaternion algebras, twisted P^1 and PGL_2, the LM2 congruence questions', 'research question put to the pages',
  'ours: whether these leaves construct the B12 object; the notes find no B12 construction and no route to LM2', 'not on the pages'),
 ('SA02-6', 'the reused autobiographical typescript on the backs of cote 84 (childhood, father, meditation from 1976, acceptance)', 'documentary (non-mathematical text)',
  'his typescript; dated sheets', 'documentary'),
 ('SA02-7', 'the yin-yang pairs of the same typescript: enumeration, later regrouping, cultural claims', 'documentary (non-mathematical text)', 'his typescript', 'documentary'),
 ('SA02-8', 'the notes\' apparatus for cote 84 (conventions, counts, coverage, limits, title sheets)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA02-9', 'a local chi-groupoid of rank-one modules: multiplication without division, invertibility, automorphisms when chi has an annihilator', 'notes\' proposal',
  'ours (the notes\'): a model for the product of SA02-4', 'not on the pages (notes\' proposal)'),
 ('SA02-10', 'KG(X) (cote 90): saturation over a Dedekind ring, the module criterion, finite dual algebras, projective covers, stable hulls', 'proposition',
  'his: criteria for saturated submodules and a stable-hull programme over a general base', 'stated; proofs deferred or marked for rewriting'),
 ('SA02-11', 'henselization, ordinary and strict, on the reused leaves of cote 90', 'proposition', 'his: parallel passages; questioned transitions', 'sketched; withdrawn parts'),
 ('SA02-12', 'Hom functors by non-projective methods (cote 91, around Greenberg-Néron): the relative product, condition R, flattening, the relative unramified Hom theorem', 'theorem (stated)',
  'his: representability of Hom and automorphism functors, with a flattening criterion and passage to the quotient', 'stated; proofs incomplete'),
 ('SA02-13', 'the notes\' apparatus for cotes 90-91 (citation key, plan, Hua findings, open register entries)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA02-14', 'a product with two parities on monoids R_0, R_1 (cote 84, scan 2)', 'construction', 'his: x wedge y on the disjoint union, by parity', 'not checked'),
 ('SA02-16', 'restricted enveloping algebras (cote 91, scan 129)', 'proposition', 'his: universal property of the restricted enveloping algebra', 'not checked'),
]
RANGES = [
 (A, 1, 1, 'SA02-8'), (A, 2, 2, 'SA02-4'), (A, 3, 7, 'SA02-1'), (A, 8, 9, 'SA02-2'), (A, 10, 10, 'SA02-1'), (A, 11, 21, 'SA02-2'), (A, 22, 24, 'SA02-3'),
 (A, 25, 28, 'SA02-2'), (A, 29, 41, 'SA02-3'), (A, 42, 67, 'SA02-4'), (A, 68, 68, 'SA02-5'), (A, 69, 69, 'SA02-1'), (A, 70, 72, 'SA02-5'), (A, 73, 99, 'SA02-6'),
 (A, 100, 111, 'SA02-8'), (A, 112, 112, 'SA02-4'),
 (B, 1, 2, 'SA02-8'), (B, 3, 40, 'SA02-4'), (B, 41, 79, 'SA02-1'), (B, 80, 135, 'SA02-6'), (B, 136, 197, 'SA02-7'), (B, 198, 201, 'SA02-5'), (B, 202, 205, 'SA02-1'),
 (B, 206, 207, 'SA02-5'), (B, 208, 210, 'SA02-9'), (B, 211, 221, 'SA02-8'), (B, 222, 222, 'SA02-1'), (B, 223, 223, 'SA02-4'), (B, 224, 224, 'SA02-9'),
 (N, 1, 1, 'SA02-13'), (N, 2, 16, 'SA02-10'), (N, 17, 22, 'SA02-11'), (N, 23, 44, 'SA02-12'), (N, 45, 45, 'SA02-10'), (N, 46, 46, 'SA02-13'), (N, 47, 50, 'SA02-12'),
 (N, 51, 53, 'SA02-13'),
]
HEADING_RULES = []
DEFAULT_ITEM = {'work': 'SA02-12', 'codex': 'SA02-12', '*': 'SA02-8'}
APPARATUS = {'SA02-8', 'SA02-13'}
HIS = {'SA02-1': 'u_1 * u_2; A_1 (x) A_2', 'SA02-2': 'algebre quasi-quadratique; norme relative, trace relative', 'SA02-3': 'produit contracte',
       'SA02-4': 'chi-trivialisation; "signe etrange"', 'SA02-6': 'Desir et meditation', 'SA02-7': 'yin, yang', 'SA02-10': 'KG(X); sature', 'SA02-12': 'foncteurs Hom (methodes non projectives); condition R'}
WORK_ITEM = {'K84-01': 'SA02-14', 'K84-02': 'SA02-1', 'K84-03': 'SA02-2', 'K84-04': 'SA02-1', 'K84-05': 'SA02-4', 'K84-06': 'SA02-4', 'K84-07': 'SA02-4',
             'K84-08': 'SA02-2', 'K84-09': 'SA02-4', 'K84-11': 'SA02-4', 'K84-12': 'SA02-1', 'K90-01': 'SA02-10', 'K91-10': 'SA02-16'}
for k in range(1, 10): WORK_ITEM[f'K91-0{k}'] = 'SA02-12'
WORK_OBJECT = {'K84-01': 'a product with two parities on monoids (scan 2)', 'K84-02': 'discriminants and the value line of a quadratic algebra (scan 19)',
               'K84-03': 'uniqueness of the conjugation in a quadratic algebra (scans 35, 39)', 'K84-04': 'the quadratic form 4N = T^2 - delta and the algebra (scan 51)',
               'K84-05': 'a lift of chi and its retraction (scans 67-68)', 'K84-06': 'trivialisations and involutions with 2 invertible (scan 82)',
               'K84-07': 'the sign in the extension diagram (scans 97-98)', 'K84-08': 'norm and base change on a tensor product (scan 113)',
               'K84-09': 'splitting coordinates for the product of extensions (scan 130)', 'K84-11': 'changing a projection (scan 162)',
               'K84-12': 'compatibilities and pairing for the product (scans 178-182)', 'K90-01': 'saturation over a Dedekind ring (cote 90, scan 2)',
               'K91-01': 'the programme: relative product, Hom functor, flattening, quotient (cote 91, scans 2-3)', 'K91-02': 'matching lifts and an Ext obstruction (scans 19-20)',
               'K91-03': 'an outline of the Hom chapter (scan 34)', 'K91-04': 'the open locus of freeness (scans 47-48)', 'K91-05': 'passage to an étale object (scan 59)',
               'K91-06': 'universal property and gluing (scans 73-74)', 'K91-07': 'atomic preschemes and functors on fields (scan 87)', 'K91-08': 'limits and Hom (scan 99)',
               'K91-09': 'constructible maps (scan 114)', 'K91-10': 'restricted enveloping algebras (scan 129)'}
WORK_SCANS = {'K84-01': '2', 'K84-02': '19', 'K84-03': '35,39', 'K84-04': '51', 'K84-05': '67-68', 'K84-06': '82', 'K84-07': '97-98', 'K84-08': '113', 'K84-09': '130',
              'K84-11': '162', 'K84-12': '178-182', 'K90-01': '2', 'K91-01': '2-3', 'K91-02': '19-20', 'K91-03': '34', 'K91-04': '47-48', 'K91-05': '59', 'K91-06': '73-74',
              'K91-07': '87', 'K91-08': '99', 'K91-09': '114', 'K91-10': '129'}
CODEX_ITEM = {}
CODEX_COTE = {'K84': '84', 'K90': '90', 'K91': '91'}
OVERRIDE = {
 B + '#41': dict(basis='entry-read', note='L172.1; identity rechecked by computation (Groebner reduction over Z[b_i,c_i]); discriminant (b_1^2-4c_1)(b_2^2-4c_2)'),
 B + '#73': dict(basis='passage-read', fidelity='agrees', flag='suspected misreading', note='L190.2; read 190 l. 10-12: frozen "-|+"; N(lambda u + mu) = lambda^2 c + mu^2 - lambda mu beta, so the mathematics says "-"'),
 B + '#50': dict(basis='entry-read', note='L176.1: the abstract product generator differs from u_1*u_2 by b_1b_2'),
 A + '#68': dict(flag='LM/Derivateurs lens'), A + '#70': dict(flag='LM/Derivateurs lens'), A + '#72': dict(flag='LM/Derivateurs lens'),
 B + '#198': dict(flag='LM/Derivateurs lens'), B + '#206': dict(flag='LM/Derivateurs lens'),
 A + '#73': dict(flag='a link across folders', note='C06: scan 143 supplies printed page 480, which the 146-193 notes listed as absent'),
 A + '#75': dict(flag='the same thing noted with different readings or statements', note='C08: a title reference ("Desir et meditation") has two reported section numbers'),
}
CROSS = {'SA02-1': 'SA01 (quadratic algebras K83-04..08; lambda-split extensions MPL_83 E01-E07; the trace identity with its -4cc\'c\'\' term)', 'SA02-4': 'SA01-17 (lambda-split extensions and the product *)',
         'SA02-5': 'La Longue Marche (research register B12, LM2)', 'SA02-6': 'other reused typescripts: SA01-24 (cote 83)', 'SA02-12': 'EGA/SGA material on Hom schemes (literature)'}
ITEM_FLAGS = {'SA02-5': 'LM/Derivateurs lens', 'SA02-1': 'a link across folders (Pro 84a, 84b and Work K84-02, -04, -12)'}
FLAGS = [
 ['LM/Derivateurs lens', 'MPL_84_097-145#68, #70, #72 (C01, C03, C05); MPL_84_146-193#198-201, #206-207 (R01-R04, R09-R10)', 'The requested questions read cote 84 through the La Longue Marche bridge B12 (quaternion algebras, twisted P^1, PGL_2) and the LM2 congruence rows; both packages\' notes find no B12 construction and no route to LM2 on these leaves.', 'headings C01-C05, R01-R10; MPL_84_146-193_notes.md L190.2 context paragraph'],
 ['suspected misreading', '84/190 l. 10-12 (MPL_84_146-193#73 = L190.2)', 'Frozen "lambda^2 c + mu^2 (-|+) lambda mu beta": for u^2 + beta u + c = 0 the norm of lambda u + mu is lambda^2 c + mu^2 - lambda mu beta, so the mathematics reads "-". Decide on the scan.', 'transcription scan 190; my computation; the note says the same'],
 ['a link across folders', 'MPL_84_097-145 A02-A10 (scans 98-105); MPL_84_146-193 L172-L192; work:K84-02, K84-04, K84-12', 'One object, the product of two quadratic algebras, runs through both packages and three Work folders. The identity u^2 + b_1b_2u + (b_1^2c_2 + b_2^2c_1 - 4c_1c_2) = 0 holds over Z[b_i, c_i] (checked), and its discriminant is (b_1^2 - 4c_1)(b_2^2 - 4c_2). Cross-topic: SA01 cote 83 (quadratic algebras, lambda-split extensions).', 'L172.1; my Groebner computation'],
 ['a link across folders', 'work:K84-07 (97-98), K84-08 (113), K84-09 (130), K84-11 (162), K84-12 (178-182), K90-01 (90/2), K91-01 (91/2-3)', 'Seven Work folders re-read pages of the Pro packages (A01 at 97; A24-A25 at 113; B09 at 130; E162 at 162; L178-L182; N90-01; the N91 programme): pairs of independent readings for sweep 2.', 'WORK_SCANS against the packages\' scan ranges'],
 ['the same thing noted with different readings or statements', 'MPL_84_097-145#75 (C08)', 'The typescript section "Desir et meditation" carries two reported section numbers (36 in this reading, another in the neighbouring report).', 'C08 heading; SA02 provisional dossier item SA02-075'],
 ['a link across folders', 'MPL_84_097-145#73 (C06) and MPL_84_146-193', 'The 146-193 notes list printed page 480 of the typescript as absent; scan 143 of 097-145 supplies it. Not a contradiction: different scan ranges.', 'C06 heading'],
 ['a link across folders', 'SA02 provisional dossier SA02_final (GPT-6 Astra, ChatGPT Pro mode)', 'The dossier makes one item per entry (389 items for 389 entries) and merges nothing; it cannot serve as an item list. Used here only to check headings.', 'SA02_items.json'],
]
CHECKS = [
 [B + '#41', 'claim checked by computation (Groebner reduction over Z[b_1,b_2,c_1,c_2])', 'agrees: u^2 + b_1b_2u + b_1^2c_2 + b_2^2c_1 - 4c_1c_2 = 0; discriminant multiplicative', 'MPL_84_146-193_notes.md L172.1'],
 [B + '#73', 'note checked against the page (scan 190, l. 10-12) and by computation', 'agrees: the frozen sign is "-|+"; the norm formula needs "-"', 'SA02/pro/MPL_84_146-193_transcription.tex scanpage 190'],
]
