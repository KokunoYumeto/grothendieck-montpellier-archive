# Sweep 2, SA03 gap entries (38 research leads of MPL_91_099-143; Work and Codex K93-07): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
DATE = '2026-11-18'
RL = 'MPL_91_099-143:records:research_leads'
ITEMS2 = [
 ('SA03-21', 'Work K93-07\'s remarks on cote 93 scans 52-60: the typed Banach-algebra exercise 22 a) (the lemma of Cohen\'s factorization theorem), the Euler characteristic of spheres by the hemisphere recurrence, the local-system cell lemma',
  'remarks (the Work notes\')', 'ours (the Work notes\')', 'decided on the scan (part 2): the type reads ||yw - w||, both transcriptions misread it as ||yw - u||; M52 refutes only the misreading and the exercise as typed is true; the recurrence agrees on dimensions 0-8'),
]
_OBJ = {'SA03-7': 'the constructible topology and the category of constructible models (Cons, Ind(Cons Aff), compact schemes)', 'SA03-8': 'the reused numbered typescripts (exercise sheets: restricted enveloping algebras, formal groups)',
        'SA03-9': 'the Greenberg functor and Néron spaces: the programme, épais points, Laurent-unit stages, pro-preschemes', 'SA03-10': 'finite-order evaluation and automorphisms of augmented algebras; the exterior-algebra typescript',
        'SA03-16': 'Barsotti-Tate groups and their crystals on cote 93 scans 47-51 (K93-07): vector extensions, the crystalline comparison, the canonical filtration, isogroups, Problem 4', 'SA03-21': 'K93-07 remarks on scans 52-60'}
HIS = {'SA03-7': 'topologie constructible; Cons', 'SA03-9': 'Greenberg - Néron; point épais', 'SA03-16': 'cristaux de Dieudonné; groupes de BT; Problème 4'}
SCAN_ITEM = {99: 'SA03-7', 100: 'SA03-10', 101: 'SA03-7', 102: 'SA03-7', 118: 'SA03-9', 119: 'SA03-10', 120: 'SA03-9', 121: 'SA03-10', 122: 'SA03-9', 123: 'SA03-10', 124: 'SA03-9',
             126: 'SA03-9', 127: 'SA03-8', 128: 'SA03-9', 129: 'SA03-8', 131: 'SA03-9', 132: 'SA03-9', 134: 'SA03-9', 135: 'SA03-9', 136: 'SA03-9', 138: 'SA03-10', 139: 'SA03-8',
             140: 'SA03-10', 141: 'SA03-8', 142: 'SA03-10', 143: 'SA03-8'}
TYPED = {100: 'n° 285, p. 12', 102: 'n° 285, p. 10', 119: 'n° 371, p. 90', 121: 'n° 371, p. 93', 123: 'n° 371, p. 92', 127: 'n° 316, p. 145', 129: 'n° 316, p. 135', 139: 'n° 316, p. 132', 141: 'n° 316, p. 129', 143: 'n° 316, p. 130'}

def place(g):
    i = g['entry_id']
    if i.startswith(RL):
        sc = int(g['scans'].split(',')[0])
        it = SCAN_ITEM.get(sc, 'SA03-7' if 104 <= sc <= 116 else 'SA03-9')
        obj = f'{_OBJ[it]}: lead on scan {sc}' + (f' (reused typescript {TYPED[sc]})' if sc in TYPED else '')
        return dict(item=it, cote='91', kind='Pro records: research lead (per scan)', object=obj, his_term=HIS.get(it, ''), basis='entry-read', note='entry opening read')
    it = 'SA03-21' if i == 'work:K93-07#6' else 'SA03-16'
    src = 'Codex notes on the sheets' if i.startswith('codex:') else 'Work math-notes unit'
    return dict(item=it, cote='93', scans='47-60', kind=f'{src}: {g["heading"][:60]}', object=(f'{_OBJ[it]} - K93-07: ' + g['heading'].lower())[:200], his_term=HIS.get(it, ''),
                basis='entry-read', note='entry read (opening, or whole when short); the folder also covers scans 52-60 (pseudo-resolvent exercise, Euler characteristic)')

OVERRIDE = {
 'work:K93-07#6': dict(flag='suspected misreading', note='M52 refutes the misreading ||yw - u|| of exercise 22 a); the type reads ||yw - w|| (scan, part 2) and the exercise is true. M58: 2,0,2,... agrees with the sphere formula for dimensions 0-8'),
 RL + '#8': dict(note='a recurring coined-looking term read "antifique/antifini" (107); reading open'),
 RL + '#23': dict(note='title sheet "Greenberg - Néron" (124)'),
}
CROSS2 = {'SA03-16': '= H024; K93-07 re-reads SA04\'s MPL_93_047-091 (= H02H, SA04-1), Problem 4 continues Problems 1-3', 'SA03-21': '= H02N (SA04-2, the pseudo-resolvent exercises); SA04-4 (Euler characteristic axioms)',
          'SA03-8': 'the numbered typescripts n° 285, 316, 371 (possibly Bourbaki rédactions: my inference from the numbering, not checked)'}
ITEM_FLAGS2 = {'SA03-16': 'a link across folders (K93-07 re-reads SA04 pages)', 'SA03-21': 'suspected misreading or an error of the typed exercise (scan 52)'}
FLAGS2 = [
 ['a link across folders', 'work:K93-07, codex:K93-07 (cote 93 scans 47-60)', 'Filed under SA03 but a second reading of SA04\'s MPL_93_047-091 pages: Barsotti-Tate crystals and the crystalline comparison (= H02H, SA04-1), whose Problem 4 continues the Problems 1-3 of SA03-16 (= H024); the pseudo-resolvent exercise (= H02N); the Euler characteristic axioms (SA04-4). A Pro/Work reading pair for part 2.', 'entries read'],
 ['suspected misreading', 'work:K93-07#6 (M52), 93/052', 'The Work notes refute the wording of exercise 22 a) at u=1, w=0, C=2, gamma=0, epsilon=1/2. Decided on the scan in part 2: the type reads ||yw - w||, and both transcriptions (Pro and Work) misread it as ||yw - u||; the exercise as typed is true (REPORTS/cote93_scan052_exercise_22a.md).', 'entry read; scan image (part 2)'],
 ['a link across folders', RL + ' (typed scans 100, 102, 119, 121, 123, 127, 129, 139, 141, 143)', 'The reused typescripts of cote 91 carry series numbers n° 285 (topological groups, projective systems), n° 316 (formal groups, restricted Lie algebras: exercises) and n° 371 (exterior algebras). The numbering suggests Bourbaki rédactions (my inference, not checked); SA03-8 and SA03-10 hold them.', 'entries read'],
]
CHECKS2 = []
NOTES2 = '''
## Sweep 2, part 1: the gap entries (18 Nov 2026)

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. There were 46 gap entries; all are placed.

**The research leads of MPL_91_099-143 (38 entries, one per scan)** fall into the sweep-1 items by scan:

| Item | Subject | Scans |
|---|---|---|
| SA03-7 | Constructible topology | 99-116 |
| SA03-9 | Greenberg-Néron | 118, 120, 122, 124-136 |
| SA03-10 | Finite-order evaluation; the exterior-algebra typescript | 100, 119-123, 138-142 |
| SA03-8 | The numbered typed exercise sheets | 127, 129, 139-143 |

The typed leaves carry the series numbers n° 285, 316 and 371. Reading these as Bourbaki rédactions is my inference from the numbering; I have not checked it.

**Work and Codex K93-07 (8 entries)** cover cote 93, scans 47-60:
- Barsotti-Tate crystals and the crystalline comparison, with Problem 4 (SA03-16). These pages are SA04's MPL_93_047-091, so the folder gives a reading pair for part 2.
- One model remark, which went to a new item, SA03-21. It says the typed pseudo-resolvent exercise 22 a) is false as worded at given values.

**Basis:** 46 entry-read (the opening of each lead, which is the whole lead when it is short).

**Flags (3):**
- K93-07 is a second reading of SA04's pages.
- The exercise 22 a) wording, which the Work notes refute.
- The numbered typescripts.

**Checks:** none of my own.

**What part 2 should take from here:**
- the Pro/Work reading pair on 93/47-60;
- the exercise 22 a);
- the merge of SA03-16 (= H024) with SA04-1 (= H02H).
'''
