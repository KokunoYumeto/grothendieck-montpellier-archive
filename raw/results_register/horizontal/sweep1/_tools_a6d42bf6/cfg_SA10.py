# SA10 Espaces stratifiés (cotes 150, 151, 152, 120-121): placement config (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notes_extract import entries, H
DATE = '2026-11-18'
A, B, C, D, E_ = 'MPL_150_001-043', 'MPL_150_044-084', 'MPL_150_085-099+151_001-031', 'MPL_151_032-075', 'MPL_152+120'
ITEMS = [
 ('SA10-1', 'the notes\' apparatus for the stratified-spaces packages (evidence, statuses, sources, research tasks)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA10-2', 'his terms "tubulure" and "ombre": where the tubular pro-neighbourhood and the shadow are introduced (cotes 150, 151, 147, 149, 136, 67)', 'reading question (requested)',
  'his: tubulure, ombre; ours: the tubular pro-neighbourhood of a stratum and its shadow; the attestations are uses, not definitions', 'used, not defined, on these pages'),
 ('SA10-3', 'the "Remords": his reconsideration of the realization and its date (December 1981)', 'his claim / history', 'his: Remords', 'stated; the date is a source question'),
 ('SA10-4', 'comparison of his tame-topology axioms (cotes 120-121, M1-M11) with o-minimal structures', 'comparison (requested)',
  'ours: the axioms are not literally the o-minimal axiom list; explicit models and dictionaries given by the notes', 'not his claim; the notes\' comparison'),
 ('SA10-5', 'comparison with Shiota\'s Hauptvermutung for definable sets and its isotopy refinements', 'comparison (requested)',
  'ours: his stated comparison is stronger than object-level Hauptvermutung; Shiota\'s compact case is a partial match', 'not his claim; the notes\' comparison'),
 ('SA10-6', 'stratifications: partitions, preorders, faithful and smallest stratifications, local stratifications and descent', 'definition',
  'his: stratification of a space with an ordered index set', 'defined; several claims conditional'),
 ('SA10-7', 'conical neighbourhoods, collars, strict and cylindrical structures, equisingularity, and the reconstruction of a stratified space from its strata and gluing data', 'definition/theorem (stated)',
  'his: voisinage conique (absolu), collier, voisinage cylindrique, conique strict; the reconstruction theorem by inductive pushout', 'stated; self-flagged revisions (F01-F14)'),
 ('SA10-8', 'stratified homotopy types: exit paths, gerbes and homotopy amalgams; the stratified homotopy hypothesis (comparisons with Treumann and modern repairs)', 'comparison/conjecture',
  'his: protopos of a stratified space; ours: exit-path categories', 'his sketches; the notes\' comparisons'),
 ('SA10-9', 'documentary: covers, title sheets, dates, numbering and page counts of cotes 150-152 and 120', 'documentary', 'documentary', 'documentary'),
 ('SA10-10', 'reading questions and index slips in the three-stratum induction (cote 150, scans 1-43)', 'reading question', 'reading questions', 'reading questions'),
 ('SA10-11', 'lexical findings: paths, fundamental groupoids, homotopy vocabulary, protopos', 'lexical', 'his vocabulary', 'lexical'),
 ('SA10-12', 'pro-neighbourhoods of strata and their restrictions: bands, flags, gluing formulas, strict flags, the band lemma, the spectral sequence (cote 150, scans 44-84)', 'construction',
  'his: bandes, drapeaux, raccord; the band lemma', 'constructed; several claims conditional or self-flagged'),
 ('SA10-13', 'reading questions of cote 150, scans 44-99 and cote 151, scans 1-31', 'reading question', 'reading questions', 'reading questions'),
 ('SA10-14', 'the last section of cote 150 (scans 85-99): conditions Strat 1-5, "non dense", metrizability', 'definition/theorem (stated)', 'his: Strat 1-5', 'stated; one sentence dropped by the second pass'),
 ('SA10-15', 'the stratified topos (cote 151, 1981), scans 1-31: hypotheses, phi_!, finite diagrams, left exactness', 'construction', 'his: topos stratifie', 'constructed; questioned implications'),
 ('SA10-16', 'the stratified topos, scans 32-58: tubes, flags, local triviality, (1)-(25)', 'construction', 'his: topos stratifie', 'worked; conjectures and withdrawals'),
 ('SA10-17', 'the theorem on 151/069 and its continuation (scans 59-75): cylinder and cone descriptions, tube base change, subsection C', 'theorem (stated)', 'his: theorem on 069', 'stated; proof paragraph cancelled'),
 ('SA10-18', 'the category of word types and plane trees (cote 152): operations, admissibility, orientation torsor, contours, nonpenetration, stable-tree indexing', 'construction',
  'his: categorie des types de mots; arbres plans', 'constructed; revisions'),
 ('SA10-19', 'cote 120 tame-geometry axioms M1-M11 and the graph calculus (amalgams, scalar extension, compact graphs, countability)', 'axiomatics', 'his: geometrie moderee; axiomes M1-M11', 'stated; the notes realize them'),
]
RANGES = [
 (A, 1, 4, 'SA10-1'), (A, 5, 8, 'SA10-2'), (A, 9, 10, 'SA10-3'), (A, 11, 15, 'SA10-4'), (A, 16, 20, 'SA10-5'), (A, 21, 28, 'SA10-6'), (A, 29, 68, 'SA10-7'),
 (A, 69, 71, 'SA10-8'), (A, 72, 89, 'SA10-7'), (A, 90, 98, 'SA10-9'), (A, 99, 103, 'SA10-10'), (A, 104, 109, 'SA10-1'),
 (B, 1, 1, 'SA10-2'), (B, 2, 2, 'SA10-3'), (B, 3, 4, 'SA10-9'), (B, 5, 5, 'SA10-11'), (B, 6, 6, 'SA10-9'), (B, 7, 7, 'SA10-7'), (B, 8, 8, 'SA10-8'), (B, 9, 9, 'SA10-4'),
 (B, 10, 11, 'SA10-9'), (B, 12, 14, 'SA10-11'), (B, 15, 30, 'SA10-12'), (B, 31, 33, 'SA10-9'), (B, 34, 81, 'SA10-12'), (B, 82, 88, 'SA10-8'), (B, 89, 89, 'SA10-9'),
 (B, 90, 93, 'SA10-4'), (B, 94, 98, 'SA10-5'), (B, 99, 99, 'SA10-1'), (B, 100, 111, 'SA10-13'), (B, 112, 113, 'SA10-1'),
 (C, 1, 18, 'SA10-14'), (C, 19, 48, 'SA10-15'), (C, 49, 53, 'SA10-13'), (C, 54, 60, 'SA10-9'), (C, 61, 66, 'SA10-2'), (C, 67, 75, 'SA10-8'), (C, 76, 85, 'SA10-4'), (C, 86, 93, 'SA10-5'),
 (D, 1, 1, 'SA10-2'), (D, 2, 2, 'SA10-3'), (D, 3, 3, 'SA10-4'), (D, 4, 4, 'SA10-5'), (D, 5, 27, 'SA10-16'), (D, 28, 57, 'SA10-16'), (D, 58, 103, 'SA10-17'), (D, 104, 104, 'SA10-8'),
 (D, 105, 106, 'SA10-17'), (D, 107, 109, 'SA10-1'),
 (E_, 1, 1, 'SA10-1'), (E_, 2, 17, 'SA10-18'), (E_, 18, 18, 'SA10-9'), (E_, 19, 19, 'SA10-18'), (E_, 20, 26, 'SA10-2'), (E_, 27, 27, 'SA10-1'), (E_, 28, 35, 'SA10-3'), (E_, 36, 37, 'SA10-1'),
 (E_, 38, 56, 'SA10-4'), (E_, 57, 57, 'SA10-1'), (E_, 58, 82, 'SA10-19'), (E_, 83, 83, 'SA10-1'), (E_, 84, 98, 'SA10-5'), (E_, 99, 106, 'SA10-19'), (E_, 107, 107, 'SA10-18'), (E_, 108, 113, 'SA10-9'),
]
HEADING_RULES = []
DEFAULT_ITEM = {'work': 'SA10-1', 'codex': 'SA10-1', '*': 'SA10-1'}
APPARATUS = {'SA10-1'}
HIS = {'SA10-2': 'tubulure; ombre', 'SA10-3': 'Remords', 'SA10-7': 'voisinage conique; collier; equisingularite', 'SA10-8': 'protopos', 'SA10-12': 'bande; drapeau; raccord',
       'SA10-15': 'topos stratifie', 'SA10-18': 'types de mots; arbres plans', 'SA10-19': 'espace modere; M1-M11'}
WORK_ITEM = {}; WORK_OBJECT = {}; WORK_SCANS = {}; CODEX_ITEM = {}; CODEX_COTE = {}
CROSS = {'SA10-2': 'cotes 147, 149, 136, 67 (other topics: SA11? SA12?)', 'SA10-4': 'SA21 (Vers une geometrie des formes); SA04-4 (Euler characteristic axioms)',
         'SA10-19': 'SA21; SA04-4', 'SA10-8': 'Pursuing Stacks / exit paths (Part II of the handbook outline); cote 147', 'SA10-15': 'SGA 4 recollement (literature)',
         'SA10-18': 'SA01 (planar maps, cote 88 "Cartes standards"); dessins (SA03?)'}
ITEM_FLAGS = {'SA10-4': 'requested comparison; the notes\' work, not his', 'SA10-5': 'requested comparison; the notes\' work, not his'}
# second-pass verdicts (Claude Opus 5.5 at effort max, 17 Nov 2026) attached by label
OVERRIDE = {}; FLAGS = []; CHECKS = []
SP = os.path.join(H, 'SA10', 'second_pass')
lab = collections.defaultdict(dict)
for e in entries('SA10'):
    m = re.match(r'^([A-Z]{0,4}\d[\w.-]*|\d{3}-\d{2}|[A-Z]\d+[a-z]?)\s+[—-]', e['heading'])
    if m: lab[e['pkg']].setdefault(m.group(1), e['id'])
verdicts = collections.Counter(); drops = []
for pkg in os.listdir(SP):
    for f in os.listdir(os.path.join(SP, pkg)):
        if not f.endswith('_notes_checked.md'): continue
        for k, line in enumerate(open(os.path.join(SP, pkg, f), encoding='utf-8'), 1):
            if not line.startswith('|'): continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            mm = re.match(r'([A-Z]{0,4}\d[\w.-]*|\d{3}-\d{2})\b', cells[0]) if cells else None
            if not mm or mm.group(1) not in lab.get(pkg, {}): continue
            eid = lab[pkg][mm.group(1)]
            vi = next((i for i in (1, 2) if i < len(cells) and re.match(r'(keep|correct|drop|confirm|withdraw|kept)', cells[i].lower())), None)
            v = cells[vi].lower()[:40] if vi else 'see row'
            why = re.sub(r'\s+', ' ', ' | '.join(cells[(vi or 1) + 1:]))[:150]
            verdicts[re.match(r'[a-z]+', v).group(0) if re.match(r'[a-z]+', v) else v] += 1
            o = OVERRIDE.setdefault(eid, {})
            o['note'] = f'second pass 17 Nov (Claude Opus 5.5 at effort max): {v}: {why}'
            if v.startswith('drop') or 'overstat' in why.lower() or 'not on the page' in why.lower():
                o['flag'] = 'note overstates or misreads the page'
                drops.append((eid, v, why, f'SA10/second_pass/{pkg}/{f}:{k}'))
for eid, v, why, where in drops:
    FLAGS.append(['note overstates or misreads the page', eid, f'second pass verdict "{v}": {why}', where])
FLAGS += [
 ['a link across folders', 'SA10 MPL_150_001-043 Q1-Q4, MPL_150_044-084 Q1-Q9, MPL_151_032-075 1.1-1.4, MPL_152+120 Q1-Q4', 'Four requested questions (tubulure and ombre; the Remords and its date; cotes 120-121 against o-minimality; Shiota\'s Hauptvermutung) are answered in all five packages; the answers are the notes\' research, merged here into SA10-2 to SA10-5.', 'headings'],
 ['a link across folders', 'MPL_152+120 (A120-01..24, Q3-01..11, U01-U09)', 'Cote 120 (tame geometry axioms M1-M11) sits in SA10 through the package MPL_152+120 but is the subject of SA21 (Vers une geometrie des formes).', 'package name; SA21 topic'],
 ['the same thing noted with different readings or statements', 'second pass of all five packages', f'The second pass (Claude Opus 5.5 at effort max, 17 Nov) changed many first-pass readings; its verdicts on the notes, matched here by label: {dict(verdicts)}. Where it changed a reading, its reading is current.', 'SA10/second_pass/*/..._notes_checked.md, _changes.md'],
]

# global tags from the broad agent's inbox (build_global.py, 15:08 UTC), added 18 Nov 2026
def _addx(k, s):
    CROSS[k] = (CROSS[k] + '; ' + s) if CROSS.get(k) else s
for _k, _s in [('SA10-18', '= H00J (SA20-7)'), ('SA10-19', '= H00K (SA20-12)'), ('SA10-3', '= H00L (SA20-9)')]:
    _addx(_k, _s)
