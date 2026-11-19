# Sweep 2, SA04 gap entries (196 Codex notes on the sheets, cotes 69-102; Work K70-02, K70-04, K70-06, K77-05): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
import re
DATE = '2026-11-18'
ITEMS2 = [
 ('SA04-41', 'documentary: title sheets, section headings, dates and reused sheets of cotes 69-102 (Codex notes on the sheets): course and draft titles, page counts, reused notices, letters and administrative sheets of 1975-1981',
  'documentary', 'documentary', 'documentary'),
]
COTE_ITEM = {'69': 'SA04-20', '70': 'SA04-21', '73': 'SA04-22', '74': 'SA04-23', '76': 'SA04-24', '77': 'SA04-25', '78': 'SA04-26', '79': 'SA04-27', '80': 'SA04-28',
             '82': 'SA04-30', '85': 'SA04-31', '86': 'SA04-32', '87': 'SA04-33', '88': 'SA04-34', '89': 'SA04-35', '94': 'SA04-36', '97': 'SA04-37', '101': 'SA04-39', '102': 'SA04-40'}
SHORT = {'SA04-20': 'cubic graphs, the 27 lines and E6, root systems', 'SA04-21': 'regular n-polyhedra in universal affine coordinates; the icosahedron', 'SA04-22': 'polygons in an affine plane over a base',
         'SA04-23': 'trialitarian graphs and cubic complexes: triads, hexagons', 'SA04-24': 'cellular maps, flags and cartographic groups; the cube', 'SA04-25': 'rank-two quadratic forms, quadratic extensions, discriminants, affine quadrics, orthogonal groups',
         'SA04-26': 'regular polygons over rings, star operations, cyclotomic polynomials', 'SA04-27': 'regular triangulated 2-polyhedra from rank-two modules over Z/nZ',
         'SA04-28': 'pseudoline systems and their classification', 'SA04-30': 'SO(3) = GP(1) over a base and rank-three Lie algebras', 'SA04-31': 'projective representations of triangle groups; finite subgroups of GP(1); Schwarz systems',
         'SA04-32': 'regular polyhedra (course)', 'SA04-33': 'convex polyhedra and the cube', 'SA04-34': 'maps associated with root systems', 'SA04-35': 'the 3-3 sets and the topological realization functor',
         'SA04-36': 'coherent modules and schemes by descent from their representing functor', 'SA04-37': 'Chern classes of the regular representation', 'SA04-39': 'local cohomology and the characterization of Cohen-Macaulay and Gorenstein modules',
         'SA04-40': 'recollements of objects of a site (for EGA VI)', 'SA04-41': 'documentary'}
QUOTE = re.compile(r'[“«"]([^”»"]{4,80})[”»"]')

def place(g):
    i = g['entry_id']; f = g['folder']; c = re.match(r'K(\d+)-', f).group(1)
    it = COTE_ITEM[c]; k = int(i.split('#')[1])
    if i.startswith('codex:'):
        if k == 2:
            q = [x.strip() for x in QUOTE.findall(g['body'])][:2]
            return dict(item='SA04-41', cote=c, kind='Codex notes on the sheets: title sheets, dates and page counts',
                        object=f'documentary of cote {c} ({f}): ' + ('; '.join(q) if q else 'pagination and headings'), his_term='; '.join(q)[:120],
                        basis='entry-read', note=f'compact read (dates, quoted titles); subject item {it}')
        return dict(item=it, cote=c, kind='Codex notes on the sheets: steps the pages mark as unverified', object=f'{SHORT[it]} ({f}): steps the pages mark as unverified',
                    basis='entry-read', note='opening read')
    return dict(item=it, cote=c, kind=f'Work math-notes unit: {g["heading"][:60]}', object=f'{SHORT[it]} ({f}): ' + g['heading'].lower(), basis='entry-read', note='opening read')

OVERRIDE = {
 'work:K77-05#3': dict(basis='passage-read', fidelity='agrees', note='77/069: n = 2m, B = sum over perfect matchings of the edge products, Delta the generic determinant with doubled diagonal; "Soit epsilon = +-1 ... B^2 - epsilon Delta = 0 (4)"; "On présume que epsilon = (-1)^m" (checked: true)'),
 'work:K77-05#6': dict(note='R1: the Work notes\' finite check on 8 vertices (105 matchings; multiplicities 2^r over alternating cycles)'),
 'codex:K102-01#2': dict(flag='a link across folders', note='"Recollements", "Pour EGA VI", "Recollements d\'objets d\'un site": a draft for EGA VI'),
 'codex:K101-02#2': dict(note='"Notes antiques", 1958, "Caractérisation des Coh. M., des Gorensteins etc": the cote 101 local-cohomology notes are dated 1958'),
}
CROSS2 = {'SA04-20': '= H02O', 'SA04-21': '= H02P', 'SA04-22': '= H02Q', 'SA04-23': '= H02R', 'SA04-24': '= H02S', 'SA04-25': '= H02T', 'SA04-26': '= H02U', 'SA04-27': '= H02V',
          'SA04-28': '= H02W', 'SA04-29': '= H02X', 'SA04-30': '= H02Z', 'SA04-31': '= H030', 'SA04-32': '= H031', 'SA04-33': '= H032', 'SA04-34': '= H033', 'SA04-35': '= H034',
          'SA04-36': '= H035', 'SA04-37': '= H036', 'SA04-39': '= H038', 'SA04-40': '= H03A; EGA VI (recollements, K102-01)', 'SA04-41': 'SA04-29 (= H02X); SA01-43 (thesis notices, cote 71)'}
ITEM_FLAGS2 = {'SA04-40': 'a link across folders (a draft for EGA VI)', 'SA04-25': 'his presumption epsilon = (-1)^m checked true (77/069)'}
FLAGS2 = [
 ['a link across folders', 'codex:K102-01#2 (cote 102)', 'The recollement notes of cote 102 are headed "Pour EGA VI": a draft for the unpublished EGA VI (descent), with "Recollements d\'objets d\'un site".', 'entry read'],
 ['a link across folders', 'codex:K101-02#2 (cote 101)', 'The local-cohomology notes of cote 101 carry "Notes antiques" and 1958, with "Caractérisation des Coh. M., des Gorensteins etc": an early date for SA04-39 (= H038).', 'entry read'],
 ['a link across folders', 'codex title-sheet entries of cotes 69-80 (K70-02, K70-08, K74-01, K74-03, K74-08, K77-05, K77-06, K78-07, K78-08, K79-03, K79-19, K80-02)', 'Reused and dated sheets bound the combinatorial-geometry notes of cotes 69-80 to about 1975-1981: 16 Nov 1975 (K78-08), the Bourbaki seminar of 19-21 June 1976 (K74-03), 17 June 1976 (K70-08), thesis notices and letters of 1977 (K74-01, K77-06, K78-07), December 1977 (K70-02, K77-05), 1980 (K79-19), 1981 (K79-03, K80-02). Dates of reused sheets give a terminus post quem only.', 'entries read (dates)'],
 ['a link across folders', 'codex steps entries of K69-03, K70-06, K74-06, K77-01, K79-05, K79-14, K82-03, K85-01, K85-03, K87-01', 'His own "faux" and "C\'est faux" marks beside statements on these leaves: self-corrections recorded by the Codex notes; the items\' status on the pages includes these corrections.', 'entries read'],
]
CHECKS2 = [
 ['work:K77-05#3', 'note checked against the transcription passage', 'agrees', 'K77-05_transcription.tex, scan 69'],
 ['work:K77-05#3', 'his presumption checked by computation (expansion of the determinant over permutations, mod 4, by hand)', 'agrees: B^2 - (-1)^m Delta = 0 mod 4 identically (for n = 2m); fixed points and cycles of length >= 3 contribute multiples of 4, perfect matchings and single alternating cycles cancel', 'K77-05_transcription.tex, scan 69'],
]
NOTES2 = '''
## Sweep 2, part 1: the gap entries (18 Nov 2026)

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. There were 220 gap entries; all are placed.

**What came in:**
- **Codex notes on the sheets for 98 folders of cotes 69-102 (196 entries).** Each folder has two entries:
  - the steps the pages mark as unverified, which go to the cote's item (SA04-20 to SA04-40);
  - title sheets, dates and page counts, which go to a new documentary item, SA04-41.
- **Work K70-02, K70-04 and K70-06** (cote 70, the regular polyhedra and the icosahedron) go to SA04-21.
- **Work K77-05** (cote 77, the discriminant of quadratic forms) goes to SA04-25.

**Findings:**
- **His presumption on 77/069 is true.** For n = 2m, B is the sum over perfect matchings and Delta is the generic determinant with doubled diagonal. He presumes that B^2 - epsilon Delta = 0 mod 4 with epsilon = (-1)^m. I checked this by expanding the determinant over permutations mod 4, and it holds identically.
- **Cote 102 is a draft for EGA VI.** The recollement notes there are headed "Pour EGA VI".
- **Cote 101 is early.** The local-cohomology notes carry "Notes antiques" and 1958.
- **The reused sheets date cotes 69-80.** Their dates run from 1975 to 1981 and give a terminus post quem for the combinatorial-geometry notes. The sheets include:
  - the Bourbaki seminar of June 1976;
  - Montpellier thesis notices of 1977;
  - letters of 1977;
  - a 1980 commission notice;
  - the "formulaire 1981".
- **His own "faux" marks** appear on ten leaves, recorded by the Codex notes.

**Basis:**
- 219 entry-read. The Codex entries were read in a compact view: the opening of the steps entries, and the dates and quoted titles of the title-sheet entries.
- 1 passage-read (77/069, agrees).

**Checks (2):** the note against the transcription, and his presumption by computation.

**What part 2 should take from here:**
- the 588 Work units and 196 Codex entries on cotes 69-102, which continue SA01's subjects and still have no Pro reading;
- the EGA VI draft of cote 102;
- the dating of cotes 69-80;
- the cote 77 discriminant result. It is classical in substance: the discriminant of an even-rank quadratic form is a square mod 4 up to the sign (-1)^m. Part 2 should cite it, not re-prove it.
'''
