# SA21 Vers une géométrie des formes (cote 156): placement config (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
import os, re, sys
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
from notes_extract import blocks
DATE = '2026-11-18'
P = 'MPL_156-1+156-2'
ITEMS = [
 ('SA21-1', 'the notion of form ("forme"): a complete definition only in dimension zero (156-1, 156-2)', 'definition', 'his: forme', 'complete only in dimension zero (D01)'),
 ('SA21-2', 'one-dimensional models: segments, endpoints and branches; the axioms F1-F5 and their revisions; restriction', 'axiomatics',
  'his: segments, extremites, branches; F1-F6', 'revised on the pages; several claims withdrawn or unproved; the notes give a counterexample to arbitrary restriction (A12) and a repair (A13)'),
 ('SA21-3', 'filtering: the axiom F6 and its two formulations; local against global filtering; singular endpoints', 'axiomatics',
  'his: filtrant; F6', 'the passage from local to global filtering is retracted on the page (A21); F6 has two formulations'),
 ('SA21-4', 'networks (reseaux) and segment models: divisible and reduced cases; reconstruction of the order, the components and the orientation', 'construction',
  'his: reseau; reseau divisible, reduit', 'order reconstruction conditional; the orientation theorem self-flagged as unverified; topology not reconstructed'),
 ('SA21-5', 'ficelles and regular immersions: contraction quotients, cone bases, sides, connectivity, existence and uniqueness, the interval classification', 'construction',
  'his: ficelle; immersion reguliere', 'asserted separately; endpoint enlargement and universal equivalence withdrawn'),
 ('SA21-6', 'cuttings (decoupages): separating lieux, cone gluing, tubular boundaries, gluing homeomorphisms, the exchange lemma, ordered cuts and finite chains, partial cuts', 'construction',
  'his: decoupage; lieu separant; raccordement', 'lemmas stated; the cone-gluing lemma lacks a covering hypothesis; regular immersion of the cut boundary unproved'),
 ('SA21-7', 'rives, birives and mailles: germs of clopen sets, the Boolean algebra Comp, the sheaf spectrum and Stone spaces, links', 'definition/proposition',
  'his: rives, birives, mailles', 'definitions; the link identification plausible, unproved'),
 ('SA21-8', 'the requested programme questions P01-P16: pro-objects of finite posets or categories, finite T0 spaces, simple homotopy, exit paths, the Esquisse comparison', 'comparison (requested)',
  'ours (the notes\'): not his claims', 'P01: the README conjecture (a form as a tame space recovered from a pro-object of finite posets or categories) is not confirmed on these pages'),
 ('SA21-9', 'the notes\' apparatus for SA21 (scope, standing questions, register relations, sources, limits)', 'apparatus', 'apparatus', 'apparatus'),
 ('SA21-10', 'ateliers (workshops): not defined in 156-1, 156-2 (D16); defined and used in 156-6, 156-7, 156-9: sub-ateliers, the axioms At, saturation, spatial ateliers, multiombre and ombres, quasi-correspondences, morphisms of ateliers', 'definition/construction',
  'his: atelier, sous-atelier; axiomes At; multiombre; Morphismes d\'ateliers', 'read only by Codex stage-A notes: self-flagged steps and dates'),
 ('SA21-11', 'documentary: covers, title sheets, dates and pagination of cote 156; the 1986 series marked GF (or CF) III to IX bis, 8 June to 12 July 1986', 'documentary', 'documentary', 'documentary'),
 ('SA21-12', '156-3, "Reseaux ... via decoupages" (8 June 1986, sheet III): troncons and sous-troncons, closed tame parts', 'construction', 'his: reseaux via decoupages; troncons; partie fermee moderee', 'read only by Codex stage-A notes: self-flagged steps and dates'),
 ('SA21-13', '156-4, "Analysis situs (premiere mouture)" (10-13 June 1986, sheet IV): contrees and their axioms Cont 1-5, figures, a presumed Boolean algebra', 'axiomatics', 'his: Analysis situs; contrees; Cont 1-5', 'read only by Codex stage-A notes: self-flagged steps and dates'),
 ('SA21-14', '156-5, "Sorite ensembliste" (15-18 June 1986): set-theoretic sorites, the order relations and their comparison', 'proposition', 'his: sorite ensembliste', 'read only by Codex stage-A notes: self-flagged steps and dates'),
 ('SA21-15', '156-8 (27 June - 2 July 1986): the symmetric point of view; the magma associated with an ordered set; elementary figures', 'construction', 'his: point de vue symetrique; magma associe a un ensemble ordonne; figures elementaires', 'read only by Codex stage-A notes: self-flagged steps and dates'),
]
RANGES = [
 (P, 1, 1, 'SA21-1'), (P, 2, 7, 'SA21-2'), (P, 8, 8, 'SA21-3'), (P, 9, 10, 'SA21-4'), (P, 11, 12, 'SA21-5'), (P, 13, 13, 'SA21-6'), (P, 14, 15, 'SA21-7'), (P, 16, 16, 'SA21-10'),
 (P, 17, 30, 'SA21-2'), (P, 31, 34, 'SA21-4'), (P, 35, 43, 'SA21-3'), (P, 44, 45, 'SA21-4'),
 (P, 46, 56, 'SA21-5'), (P, 57, 66, 'SA21-6'), (P, 67, 73, 'SA21-5'), (P, 74, 78, 'SA21-6'), (P, 79, 89, 'SA21-7'), (P, 90, 93, 'SA21-6'), (P, 94, 94, 'SA21-7'),
 (P, 95, 95, 'SA21-6'), (P, 96, 96, 'SA21-7'), (P, 97, 98, 'SA21-5'),
 (P, 99, 114, 'SA21-8'), (P, 115, 116, 'SA21-9'), (P, 117, 117, 'SA21-11'), (P, 118, 122, 'SA21-9'),
]
HEADING_RULES = []
DEFAULT_ITEM = {'*': 'SA21-9', 'codex': 'SA21-10'}
APPARATUS = {'SA21-9'}
HIS = {it[0]: it[3].replace('his: ', '') for it in ITEMS if it[3].startswith('his: ')}
WORK_ITEM = {}; WORK_OBJECT = {}; WORK_SCANS = {}
# Codex stage-A notes on cote 156 parts 3-9: one item per part; title-sheet units to the documentary item; scan ranges from the units
_PART = {'3': 'SA21-12', '4': 'SA21-13', '5': 'SA21-14', '6': 'SA21-10', '7': 'SA21-10', '8': 'SA21-15', '9': 'SA21-10'}
CODEX_ITEM = {}; CODEX_COTE = {}; OVERRIDE = {}
_cdir = os.path.join(os.path.dirname(os.path.dirname(_here)), 'inputs', 'SA21', 'codex')
for _f in sorted(os.listdir(_cdir)):
    if not _f.endswith('_notes.md'): continue
    _fo = _f[:-9]; _m = re.match(r'J156-(\d+)-', _fo)
    if not _m: continue
    CODEX_ITEM[_fo] = _PART.get(_m.group(1), 'SA21-10'); CODEX_COTE[_fo] = '156-' + _m.group(1)
    _bs = [b for b in blocks(os.path.join(_cdir, _f)) if b[0] == 2]
    _nums = []
    for _k, _b in enumerate(_bs, 1):
        _t = re.sub(r'\s+', ' ', _b[3]).strip()
        if _t.lower() in ('none', 'none.', ''): continue
        if _b[1].lower().startswith('tit'):
            OVERRIDE['codex:%s#%d' % (_fo, _k)] = dict(item='SA21-11')
            _nums += [int(x) for x in re.findall(r'(?m)^\|\s*0*(\d{1,3})\s*\|', _b[3])]
            _nums += [int(x) for x in re.findall(r'[Ss]cans?\s+0*(\d{1,3})', _b[3])]
    _nums = [x for x in _nums if 0 < x < 400]
    if _nums: WORK_SCANS[_fo] = '%d-%d' % (min(_nums), max(_nums))
_ER = dict(basis='entry-read', fidelity='not checked')
def _ov(i, **kw):
    d = OVERRIDE.setdefault(i, {}); d.update(_ER); d.update(kw)
_ov(P + '#36', flag='suspected misreading', note='A20 (156-1/019): the frozen "si x<=y,z" with "x<u<y,z" is impossible for x=y; the clear strict version is at 013; kept frozen; the scan decides (misreading or his slip)')
_ov(P + '#49', flag='suspected misreading', note='B04 (156-2/003): the frozen W\'_t = X - V_t mixes X and X/A (V_t lies in X/A); W_t would be type-correct; kept frozen; the scan decides')
_ov(P + '#55', flag='suspected misreading', note='B10 (156-2/006): the proof ends with "X minus {c} ne serait pas connexe" where X minus {a} is the target; kept frozen; the scan decides')
_ov(P + '#28', note='A12: the notes\' own counterexample to arbitrary restriction (test of 156-1/010; his warning at 008 "on n\'affirme pas egalite!"), confidence high in the notes, memo records/segment_counterexamples_memo.md; not checked in this sweep')
_ov(P + '#99', note='P01: the notes find that the README conjecture (a form as a tame space recovered from a pro-object of finite posets or categories) is not on these pages: segment and lieu data, cutting and gluing, rives and mailles; finite chains of cuts, but no category of refinements and no reconstruction theorem')
_ov(P + '#117', note='T01, T02: institutional covers (IMAG) of 156-1 and 156-2, no subject title or date; compare MPL_148_029-072 T01')
OVERRIDE.setdefault(P + '#16', {}).update(flag='a link across folders', note='D16: no definition of atelier in 156-1, 156-2; ateliers are defined and used in 156-6, 156-7, 156-9 (Codex stage-A notes)')
for _i, _n in [('codex:J156-6-03#1', '156-6 scan 20: "Je veux que cette multiombre soit une figure ensembliste"'),
               ('codex:J156-7-05#1', '156-7 scan 42: the reasoning needs the equality of the ombres (after Lemme A\')'),
               ('codex:J156-6-06#1', '156-6 scan 42: whether a sub-atelier arises when F is an atelier'),
               ('codex:J156-6-10#1', '156-6 scan 74: "J\'ai envie de renforcer At 11\'"; "Proposition (?)"'),
               ('codex:J156-6-11#1', '156-6 scan 81: to be recovered at the saturation of the atelier'),
               ('codex:J156-9-07#1', '156-9 scan 54: "et meme (je presume) un atelier spatial"'),
               ('codex:J156-6-02#1', '156-6 scan 10: "au moins dans le cas modere"'),
               ('codex:J156-3-03#2', '156-3 scan 18: "Partie fermee moderee de I"'),
               ('codex:J156-9-17#2', '156-9 scan 130: "Morphismes d\'ateliers", "CF IX bis", 12.7.86')]:
    _ov(_i, note=_n)
CROSS = {'SA21-1': 'SA11-3, SA10-4 (tame topology, cotes 120-121)', 'SA21-8': 'SA10-8 (exit paths, stratified homotopy); SA11-4; the homotopy line (finite posets as models)',
         'SA21-5': 'SA10 (conical neighbourhoods and collars, MPL_150_001-043 Q1b); SA11-1 (tubulure)', 'SA21-6': 'SA10 (MPL_150_001-043 Q1b, 150/012-015, 022-023; 147/140-142)',
         'SA21-7': 'SA10 (pro-neighbourhoods of strata, MPL_150_044-084)', 'SA21-10': 'SA10-2, SA11-1 (ombre: multiombre in 156-6, ombres in 156-7)',
         'SA21-12': 'SA11-3 (tame axiomatics, cote 121); SA10-19 (cote 120)', 'SA21-13': 'SA11-3; SA10-19', 'SA21-11': 'MPL_148_029-072 T01 (covers)'}
ITEM_FLAGS = {'SA21-10': 'a link across folders', 'SA21-8': 'requested questions; the notes\' work'}
FLAGS = [
 ['suspected misreading', P + '#36 (A20), 156-1/019', 'Frozen "si x<=y,z" with conclusion "x<u<y,z": impossible when x=y; the strict version is clear at 013. Misreading or his slip; the scan decides.', 'entry A20'],
 ['suspected misreading', P + '#49 (B04), 156-2/003', 'Frozen W\'_t = X - V_t, with V_t in X/A: a type mismatch; W_t would be type-correct. The scan decides.', 'entry B04'],
 ['suspected misreading', P + '#55 (B10), 156-2/006', 'The proof of the first three ficelle conditions ends with X minus {c} where X minus {a} is the target. The scan decides.', 'entry B10'],
 ['a link across folders', P + '#16 (D16); codex J156-6-06, -6-10, -6-11, -9-07, -9-17', 'D16 finds no definition of atelier in 156-1 and 156-2; ateliers are defined and used in 156-6, 156-7 and 156-9 (sub-ateliers, the axioms At, saturation, spatial ateliers, "Morphismes d\'ateliers", CF IX bis, 12.7.86). The Pro package saw only parts 1 and 2.', 'Codex stage-A notes'],
 ['a link across folders', 'codex J156-6-03 (scan 20), J156-7-05 (scan 42); J156-3-03 (scan 18), J156-6-02 (scan 10)', '"multiombre" and "ombres" occur in 156-6 and 156-7 (June 1986): attestations for the requested question on tubulure and ombre (SA10-2, SA11-1). "moderee"/"modere" in 156-3 and 156-6: the tame line (SA11-3, SA10-4, cotes 120-121).', 'Codex stage-A notes'],
 ['a link across folders', P + '#49 (B04); #117 (T01)', 'The neighbourhood notation of 156-2 links to MPL_150_001-043 Q1b (SA10; 150/012-015, 022-023; 147/140-142); the covers to MPL_148_029-072 T01.', 'entries B04, T01'],
]
CHECKS = []  # entry-reads only; no passage read or computation for SA21
