# Sweep 2, SA01 gap entries (139): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
import re
DATE = '2026-11-18'
P93 = 'MPL_93_092-134'
ITEMS2 = [
 ('SA01-30', 'the notes\' apparatus for the packages first placed in sweep 2 (MPL_93_092-134: context, conventions, reading list; MPL_83_178-222 records)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA01-31', 'projective connections on a relative curve (cote 93, scans 92-134): principal parts and transversality, the triple (P, sigma, c) and adjoint opers, the Riccati coordinate lambda and its poles, horizontal sections and frames, the torsor under omega^2, third jets',
  'construction', 'his: connexion projective; a P^1-bundle with a connection and a transverse section; locally 2 lambda\' + lambda^2 = mu (the normalization is the notes\')', 'sketched; formulas corrected later on the pages (factor 2, the Riccati equation); several steps self-flagged'),
 ('SA01-32', 'the Schwarzian G_t(s) = -2s\'\'\'/s\' + 3(s\'\'/s\')^2 as a cocycle of quadratic differentials: homography invariance, the developing equation G_t(s) = mu and its linearization, the integral invariant G_0 (G = 12 G_0) over any base, Frobenius constants and rigidity in characteristics 2 and 3',
  'definition/proposition', 'his: G(t,s), G_0; ours: G = -2S with S the classical Schwarzian (the notes\' convention)', 'stated ("on vérifie facilement"); the characteristic-zero kernel left "à vérifier !"; the characteristic-3 branch replaced on the page'),
 ('SA01-33', 'uniformization by the canonical projective connection: the three types, Möbius stabilizers and real forms, the canonical projective bundle from the universal cover, algebraicity of the uniformizing connection ("Sont-elles algébriques ?"), the thrice-punctured line, the affine and multiplicative cases',
  'programme/theorem (sketched)', 'his: fibré projectif canonique; uniformisation', 'sketched; open questions on the pages ("prouver (ou l\'infirmer !)", "mais pas l\'algéb. de c !")'),
 ('SA01-34', 'the notes\' arithmetic bridges for the cote 93 uniformization strand: Frobenius rigidity against p-curvature, Cartier descent, Gauss-Manin nilpotence (Katz), Kodaira-Spencer, the second fundamental form, the Legendre family, register item S20',
  'comparison (the notes\')', 'ours (the notes\'), not his claims', 'not his claim'),
 ('SA01-35', 'periods and the canonical connection in relative de Rham cohomology (cote 93, scans 221-236): operators on closed cochains, integrals between two sections, the Cartan formula, mu(a,b) computed algebraically',
  'construction', 'his: connexion canonique en cohomologie de De Rham; mu(a,b)', 'stated; (15) admitted ("l\'admettrons"); scope questions ("spécial à car. 0 ?", "steinien")'),
 ('SA01-36', 'extensions of invertible modules with a chi-trivialisation and their tensor product: changes b_i\' = b_i + chi u_i, the map Hom(M,L) (x) Hom(M\',L\') -> Hom(M (x) M\', L (x) L\') (cote 84, scans 146-160)',
  'calculation', 'his: b = b_1 b_2; T_1 (x) T_2', 'calculations; question marks on the table entries (154.06)'),
 ('SA01-37', 'documentary: the Récoltes et Semailles typescript leaves (pp. 475-478) under the mathematical leaves of cote 84 (K84-10)', 'documentary (non-mathematical text)', 'documentary', 'documentary'),
 ('SA01-38', 'KG(X) over a Dedekind ring: an affine group, the regular representation, stable quasi-coherent submodules of finite type, flat base change and direct limits (cote 90, scans 14-25)',
  'proposition', 'his: Lemme 1, Lemme 2; sous-modules stables', 'a cancelled proposition; the stable-submodule construction developed'),
 ('SA01-39', 'the EGA IV typescript reused in cote 90 (typed numbers IV-962; sections 17-18: henselization, strict localization) with pencil criticisms ("pas très clair", "Rédiger mieux")',
  'documentary/proposition (typescript)', 'EGA IV (18.5.10), (18.8.1), (18.8.5), (18.6.9)', 'typed; criticized in the margin'),
 ('SA01-40', 'plane polygons and the Jordan theorem: C. Contou-Carrère\'s manuscript on three good vertices of a polygon (cote 71, dated 15 July 1976), lemmas I-XXI, with marginal marks; simplicial realizations (|K|, |L|)',
  'theorem/proof (another author\'s manuscript)', 'Le théorème de Jordan et l\'existence de trois bons sommets pour un polygone de R^2', 'proved in the manuscript; marked "faux", "faux pour n = 3!", "so what" in the margins (hand not identified in the notes)'),
 ('SA01-41', 'the DEA course "Géométries combinatoires" (C4, 24 pp., cote 75): groups and homogeneous spaces, graphs and their topological and rectilinear realizations, the affine group of a group, small finite sets, classical groups, regular realizations, the vector envelope of a combinatorial polygon, orientation of a finite set',
  'course notes', 'his: Géométries Combinatoires; réalisation rectiligne', 'course notes; one step marked "il faut prouver que c\'est bien une réalisation rectiligne si n >= 3"'),
 ('SA01-42', 'documentary: EGA IV typescript leaves in cote 97 (pp. 17-23 with (4.43) left "au lecteur"; "IV-1102" with a note to move a passage to 21.2) and 1966 Collège de France and IHES letterheads (H97-01)',
  'documentary', 'documentary', 'documentary'),
 ('SA01-43', 'documentary: reused Montpellier thesis-defence notices of April 1977 (geology, chemistry) under cote 71', 'documentary', 'documentary', 'documentary'),
]
_SHORT = {i[0]: i[1].split(':')[0] for i in ITEMS2}
_SHORT.update({'SA01-29': 'immersions of the disc and of the circle (cote 81)', 'SA01-30': 'the notes\' apparatus for MPL_93_092-134'})
M93 = {}
for n in [1, 2, 90]: M93[n] = 'SA01-30'
for n in list(range(3, 14)) + [15, 16, 17, 19, 20, 22, 23, 24, 25, 26, 27, 36, 42, 45, 74, 75, 76, 77]: M93[n] = 'SA01-31'
for n in [18, 21, 28, 29, 30, 31, 37, 38, 39, 40, 41, 43] + list(range(46, 60)): M93[n] = 'SA01-32'
for n in [14, 32, 33, 34, 35, 44, 78, 79, 80, 85, 88] + list(range(60, 74)): M93[n] = 'SA01-33'
for n in [81, 82, 83, 84, 86, 87, 89]: M93[n] = 'SA01-34'
FOLDER = {'J71': 'SA01-40', 'J75': 'SA01-41', 'J81': 'SA01-29', 'H97': 'SA01-42', 'K93': 'SA01-35', 'K84': 'SA01-36', 'K90': 'SA01-38'}
COTE = {'J71': '71', 'J75': '75', 'J81': '81', 'H97': '97', 'K93': '93', 'K84': '84', 'K90': '90'}
UNIT = {'codex:J71-01#2': 'SA01-43', 'codex:J71-02#2': 'SA01-43', 'work:K84-10#4': 'SA01-37', 'work:K84-10#5': 'SA01-37', 'codex:K84-10#2': 'SA01-37',
        'work:K90-02#4': 'SA01-39', 'work:K90-02#5': 'SA01-39', 'codex:K90-02#1': 'SA01-39', 'codex:K90-02#2': 'SA01-39'}
HIS = {'SA01-31': 'connexion projective', 'SA01-32': 'G(t,s), G_0', 'SA01-33': 'uniformisation; fibré projectif canonique', 'SA01-35': 'connexion canonique en cohomologie de De Rham',
       'SA01-40': 'théorème de Jordan; bons sommets', 'SA01-41': 'Géométries Combinatoires', 'SA01-29': 'immersions du disque et de la circonférence'}

def place(g):
    i = g['entry_id']; d = {}
    if i.startswith(P93 + '#'):
        n = int(i.split('#')[1]); it = M93[n]
        m = re.search(r'Kind:\s*([^.]+)\.', g['body'].replace('*', ''))
        h = re.sub(r'^[A-F]\d\d\s*[—-]\s*', '', g['heading'])
        d = dict(item=it, cote='93', kind=(m.group(1) if m else 'apparatus'), object=_SHORT[it] + ': ' + (g['heading'][:3] + ' ' + h if re.match(r'[A-F]\d\d', g['heading']) else h),
                 basis='entry-read', note='entry opening read (source, kind, claim)')
    elif ':records:' in i:
        d = dict(item='SA01-30', cote='83', kind='records', object='the notes\' records for MPL_83_178-222: reading-led observations only', basis='entry-read')
    else:
        f = g['folder']; pre = f.split('-')[0]
        it = UNIT.get(i, FOLDER[pre])
        src = 'Codex notes on the sheets' if i.startswith('codex:') else 'Work math-notes unit'
        d = dict(item=it, cote=COTE[pre], kind=f'{src}: {g["heading"][:60]}', object=(_SHORT.get(it, '') + f' - {f}: ' + g['heading'].lower())[:200],
                 basis='entry-read', note='entry read (opening, or whole when short)')
    d['his_term'] = HIS.get(d['item'], '')
    return d

OVERRIDE = {
 P93 + '#5': dict(basis='passage-read', fidelity='agrees', note='A03 (095): the transcription has Omega^2 (x) omega ~ omega^{(x) 2|3} with the exponent unsure, as the note says; the torsor is later modeled on omega^2'),
 P93 + '#11': dict(basis='passage-read', fidelity='agrees', flag='suspected misreading', note='A09 (100): the transcription has D(f dt) = a df/dt + b, as the note says; a linear operator needs + b f (Hua\'s reading); misreading or his slip, for the scan'),
 P93 + '#28': dict(basis='passage-read', fidelity='agrees', flag='suspected misreading', note='B11 (113): the transcription has log s\' = -Lambda + c, then s\' = c exp Lambda(t), then s = c int exp -Lambda dt, as the note says; the middle exponent must be -Lambda'),
 P93 + '#39': dict(basis='passage-read', fidelity='agrees', flag='suspected misreading', note='C03 (117): the transcription has "mod. matrices diagonales", as the note says; the Möbius group is invertible matrices modulo scalars; his slip or a misreading'),
 P93 + '#14': dict(flag='the LM/Dérivateurs lens', note='A12 (101): the notes test a cancelled M_g diagram for a GT action or a Lego decomposition and find neither; the diagram is struck through'),
 'codex:J81-03#1': dict(note='empty ("none")'), 'codex:J81-03#2': dict(note='empty ("none")'),
}
CROSS2 = {'SA01-31': '= H03F (SA04-9); related: H03E (SA04-8), H04T (SA08-18), SA32-4', 'SA01-32': '= H03D (SA04-7); SA03-14 (the Schwarzian on cote 93 scans 2-46)',
          'SA01-33': '= H0JE (SA32-2); related: H03E (SA04-8)', 'SA01-34': '= H02J (SA04-11)', 'SA01-35': '= H00B (SA04-12); H00C (SA04-13)',
          'SA01-36': '= H01R (SA02-4); related: H01W (SA02-9), H00Z (SA01-17)', 'SA01-37': '= H01T (SA02-6)', 'SA01-38': '= H01J (SA02-10)', 'SA01-39': '= H01K (SA02-11); EGA IV sections 17-18',
          'SA01-41': 'related: H00W (SA01-1, pinned regular realizations); H02P (SA04-21, cote 70); SA04-22 (polygons, cote 73)', 'SA01-42': 'SA04-37 (cote 97); EGA IV section 21',
          'SA01-40': 'related: SA01-41 (cote 75, polygons and realizations)'}
ITEM_FLAGS2 = {'SA01-31': 'a link across folders', 'SA01-32': 'a link across folders; suspected misreadings at 93/113, 93/117', 'SA01-33': 'a link across folders', 'SA01-35': 'a link across folders',
               'SA01-36': 'a link across folders', 'SA01-38': 'a link across folders', 'SA01-39': 'a link across folders'}
FLAGS2 = [
 ['suspected misreading', P93 + '#11 (A09), 93/100', 'Transcription: D(f dt) = a df/dt + b. A linear differential operator needs + b f; Hua\'s reading has a f\' + b f. Decided on the scan in part 2: the ink has no f; his slip (REPORTS/cote93_scans100_113_117_slips.md).', 'passage read; scan image (part 2)'],
 ['suspected misreading', P93 + '#28 (B11), 93/113', 'Transcription: log s\' = -Lambda + c, then s\' = c exp Lambda(t), then s = c int exp(-Lambda) dt. The middle exponent must be -Lambda. Decided on the scan in part 2: the ink has no minus; his slip.', 'passage read; scan image (part 2)'],
 ['suspected misreading', P93 + '#39 (C03), 93/117', 'Transcription: the Möbius group as invertible matrices "mod. matrices diagonales"; it is modulo scalar matrices (diag(2,1) acts by t -> 2t). Decided on the scan in part 2: the ink says "diagonales"; his slip of wording.', 'passage read; scan image (part 2)'],
 ['suspected misreading', P93 + ' A03 (095), B01 (102), B02 (107), B04 (102), D06 (122), E04 (126), E17 (134)', 'Further reading questions of the package: the tensor exponent omega^{2|3}; D_{u_M(t)} = D_t, false for inversion; a missing factor 2; intermediate log coefficients; the divided-derivative orders; the invariant metric; the torsor "sur S" where X is meant. Listed by the notes in #90.', 'entries read; A03 passage read'],
 ['a link across folders', P93 + ' (90 entries, cote 93 scans 92-134)', 'Filed under SA01 but the continuation of SA04\'s cote-93 strands between MPL_93_047-091 and MPL_93_221-236: projective connections (= H03F, SA04-9), the Schwarzian and G_0 (= H03D, SA04-7), uniformization (= H0JE, SA32-2; H03E), the notes\' Gauss-Manin and Cartier bridges (= H02J, SA04-11). Merge with those items.', 'entries read'],
 ['a link across folders', 'work:K84-10, codex:K84-10 (cote 84); work:K90-02, codex:K90-02 (cote 90); work:K93-13, codex:K93-13 (cote 93 scans 221-236)', 'Filed under SA01 but SA02\'s and SA04\'s objects: chi-trivialised extensions (= H01R), the Récoltes et Semailles typescript (= H01T), KG(X) over a Dedekind ring (= H01J), the EGA IV henselization typescript (= H01K); periods and the canonical de Rham connection (= H00B, H00C).', 'entries read'],
 ['a link across folders', 'codex:K90-02#1 (scans 18, 21, 23, 24)', 'The pencil criticisms "pas très clair", "la forme hybride ici ne mérite pas le nom de ... universelle" and "Rédiger mieux ... début de la démonstration" stand on the typed EGA IV leaves (sections 17-18), not on the manuscript: comments on the EGA IV typescript.', 'entry read'],
 ['the LM/Dérivateurs lens', P93 + '#14 (A12), 93/101', 'The notes test a struck M_g diagram for a GT action, a Lego decomposition or a tower and find none: the LM reading is asked of the leaf, which does not support it.', 'entry read'],
 ['a link across folders', 'codex:J71-01..06 (cote 71); codex:J75-01..04 (cote 75)', 'Two subjects new to SA01: C. Contou-Carrère\'s manuscript on the Jordan theorem and three good vertices of a plane polygon (dated 15 July 1976), on the backs of April 1977 thesis notices; and the DEA course "Géométries combinatoires" (C4, 24 pp.), whose regular realizations continue SA01-1 (H00W) and cote 70 (H02P).', 'entries read'],
]
CHECKS2 = [
 [P93 + '#46', 'claim checked by computation (Hasse derivatives D1 = s\', D2 = s\'\'/2, D3 = s\'\'\'/6, by hand)', 'agrees: 12 G_0 = 3(s\'\'/s\')^2 - 2s\'\'\'/s\' = G', 'MPL_93_092-134_notes.md, D01'],
 [P93 + '#49', 'claim checked by computation (D^(k) t^n = C(n,k) t^(n-k) and Lucas\'s theorem)', 'agrees: common kernel A[t^p] for p > 3, A[t^4] for p = 2, A[t^9] for p = 3', 'MPL_93_092-134_notes.md, D04'],
 [P93 + '#29', 'claim checked by computation (by hand)', 'agrees: alpha = s\', lambda = -s\'\'/s\', and 2 lambda\' + lambda^2 = G_t(s)', 'MPL_93_092-134_notes.md, B12'],
 [P93 + '#30', 'claim checked by computation (by hand)', 'agrees: lambda = 2u\'/u gives 2 lambda\' + lambda^2 = 4u\'\'/u; for u\'\' = (mu/4)u the ratio of two solutions has S = -mu/2, so G = -2S = mu', 'MPL_93_092-134_notes.md, B13'],
 [P93 + '#35', 'claim checked against the classical formula {tau, z} = (z^2 - z + 1)/(2 z^2 (z-1)^2) for the thrice-punctured line', 'agrees: mu = -2S = -(z^2 - z + 1)/(z^2 (z-1)^2), leading coefficient -1 at each puncture', 'MPL_93_092-134_notes.md, B18'],
 [P93 + '#5', 'note checked against the transcription passage', 'agrees', 'MPL_93_092-134_transcription.tex, scan 95'],
 [P93 + '#11', 'note checked against the transcription passage', 'agrees (frozen D(f dt) = a df/dt + b)', 'MPL_93_092-134_transcription.tex, scan 100'],
 [P93 + '#28', 'note checked against the transcription passage', 'agrees (frozen s\' = c exp Lambda(t))', 'MPL_93_092-134_transcription.tex, scan 113'],
 [P93 + '#39', 'note checked against the transcription passage', 'agrees (frozen "mod. matrices diagonales")', 'MPL_93_092-134_transcription.tex, scan 117'],
]
NOTES2 = '''
## Sweep 2, part 1: the gap entries (18 Nov 2026)

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. There were 139 gap entries; all are placed, as 14 new items (SA01-30 to SA01-43) and two more entries in SA01-29.

**What came in:**
- **MPL_93_092-134, 90 Pro notes on cote 93, scans 92-134.** NOTES_INDEX had missed this package. It fills the gap between MPL_93_047-091 (SA04) and MPL_93_221-236 (SA04). Its strands:
  - projective connections on a relative curve (SA01-31, = H03F);
  - the Schwarzian G, its cocycle and the integral invariant G_0 with G = 12 G_0 in characteristics 2 and 3 (SA01-32, = H03D);
  - uniformization by the canonical projective bundle and the algebraicity questions (SA01-33, = H0JE);
  - the notes' own Gauss-Manin, Cartier and p-curvature bridges (SA01-34, = H02J).
- **Codex notes on the sheets for new cotes:**
  - cote 71: C. Contou-Carrère's manuscript on the Jordan theorem and three good vertices of a plane polygon (15 July 1976), on the backs of April 1977 thesis notices (SA01-40, SA01-43);
  - cote 75: the DEA course "Géométries combinatoires" (C4, 24 pp.; SA01-41);
  - cote 97: EGA IV typescript leaves and 1966 letterheads (SA01-42);
  - cote 81: J81-03, which is empty.
- **Work and Codex notes on folders whose objects are SA02's and SA04's:**
  - K84-10: chi-trivialised extensions (= H01R), with the Récoltes et Semailles typescript (= H01T);
  - K90-02: KG(X) over a Dedekind ring (= H01J), with the EGA IV henselization typescript and its pencil criticisms (= H01K);
  - K93-13: periods and the canonical de Rham connection (= H00B, H00C).

**Basis:**
- 135 entry-read. For the 90 Pro notes this means the opening of each entry (source, kind and claim); the Codex and Work entries were read in full when short.
- 4 passage-read, all agreeing with the frozen transcription: 93/095, 93/100, 93/113, 93/117.

**Checks (9):**
- Five of the notes' claims, checked by computation, all agree: G = 12 G_0 (D01); the Frobenius constants A[t^p], A[t^4], A[t^9] (D04); the developing-map system (B12); the linearization u'' = (mu/4)u (B13); the thrice-punctured-line coefficient (B18).
- Four notes checked against the transcription.

**Flags (9):**
- Three suspected misreadings or slips, passage-read:
  - 93/100: + b where + b f is needed;
  - 93/113: the sign of the exponent;
  - 93/117: "diagonales" for scalars.
- One further list of reading questions.
- Four links across folders.
- One LM-lens test, on 93/101.

**What part 2 should take from here:** the merge of SA01-31 to SA01-35 with SA04-7, -8, -9, -11, -12, -13 and SA03-14, which joins the cote 93 uniformization strand into one place; the three suspected misreadings; and the notes' own results in D07-D14 (rigidity with nilpotents, descent, the Picard hypothesis removed in odd characteristic), which are unchecked here.
'''
