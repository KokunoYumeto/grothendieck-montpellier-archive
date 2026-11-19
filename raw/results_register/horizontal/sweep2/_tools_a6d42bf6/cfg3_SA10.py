# Sweep 2 part 2, SA10 (cotes 150, 151, 152, 120): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
import re
DATE = '2026-11-18'
TITLE = 'SA10: stratified spaces (cotes 150, 151, 152, 120)'
INTRO = '''
The topic is "Espaces stratifiés", part 1. It holds:
- **Cote 150:** stratifications, conical neighbourhoods and collars, the reconstruction of a stratified space, pro-neighbourhoods of strata with their bands and flags.
- **Cote 151 (1981):** the stratified topos.
- **Cote 152:** word types and plane trees.
- **Cote 120:** his tame-geometry axioms M1-M11.

Four requested questions recur in every package: tubulure and ombre, the Remords, o-minimality, Shiota. They are the notes' research.

Heavy notes: five Pro packages (GPT-6 Astra, ChatGPT Pro mode). The second pass of 17 Nov (Claude Opus 5.5 at effort max) checked them against the scans; its 282 verdicts are now check events, and its corrections are in CORRECTIONS.tsv. There are no Work or Codex notes.

One research run reads these pages: EXIT_TOWER, on cote 150, folios 9 and 15-16.
'''
ORDER = [
 ('Stratifications and their neighbourhoods (cote 150)', ['SA10-6', 'SA10-7', 'SA10-12', 'SA10-14', 'SA10-2', 'SA10-3']),
 ('The stratified topos (cote 151, 1981)', ['SA10-15', 'SA10-16', 'SA10-17']),
 ('Stratified homotopy types', ['SA10-8']),
 ('Word types and plane trees (cote 152)', ['SA10-18']),
 ('Tame geometry: his axioms (cote 120) and the notes\' comparisons', ['SA10-19', 'SA10-4', 'SA10-5']),
 ('Reading questions, lexical findings, documentary and apparatus', ['SA10-10', 'SA10-13', 'SA10-11', 'SA10-9', 'SA10-1']),
]
DEPS = [
 ('SA10-7', 'SA10-6', 'his page', '150: conical neighbourhoods and collars are defined for a stratification'),
 ('SA10-12', 'SA10-7', 'his page', '150/44-84: pro-neighbourhoods of strata restrict the conical structures to bands and flags'),
 ('SA10-14', 'SA10-6', 'his page', '150/85-99: the conditions Strat 1-5'),
 ('SA10-15', 'SA10-12', 'his page', '151/1-31: the stratified topos from tubes and pro-neighbourhoods'),
 ('SA10-16', 'SA10-15', 'his page', '151/32-58: tubes, flags and local triviality in the topos'),
 ('SA10-17', 'SA10-16', 'his page', '151/59-75: the theorem on 069 uses the tubes and flags'),
 ('SA10-8', 'SA10-15', 'our note', 'exit paths and the stratified homotopy type, read from the stratified topos'),
 ('SA10-7', 'SA10-2', 'our note', 'the tubulure as the tubular pro-neighbourhood of a stratum (his term, used and not defined)'),
 ('SA10-4', 'SA10-19', 'our note', 'the comparison with o-minimal structures starts from M1-M11'),
 ('SA10-5', 'SA10-19', 'our note', 'Shiota\'s Hauptvermutung for definable sets, against the cote 120 axioms'),
]
RELATED = [
 ('SA10-19', 'SA11-3', 'our note', 'the later drafts of cote 121 (= H00M); cote 120 itself is H00K'),
 ('SA10-2', 'SA11-1', 'our note', 'the same requested question (= H05G)'),
 ('SA10-3', 'SA11-2', 'our note', 'the Remords (= H00L)'),
 ('SA10-4', 'SA11-4', 'our note', 'the o-minimality and Nash comparisons'),
 ('SA10-2', 'SA21-10', 'our note', '"multiombre" (156-6, scan 20) and "ombres" (156-7, scan 42)'),
 ('SA10-19', 'SA21-12', 'our note', '"Partie fermée modérée" (156-3): the tame line'),
 ('SA10-8', 'SA21-8', 'our note', 'exit paths and finite models among the notes\' programme questions'),
 ('SA10-18', 'SA01-9', 'my inference', 'plane trees and maps beside pseudoline arrangements'),
]
CLAIMS = [
 ['SA10-C1', 'the stratification of the moduli of stable curves on folio 9: its intervals and intersections of strata', '150/28-30', 'SA10-7', 'EXIT_TOWER:A.1, A.2, A.3 (Proved): every interval of the poset of stable graphs G_{g,n} is Boolean; pairs with a common lower bound have an infimum exactly for g = 0, n >= 3; g = 1, 1 <= n <= 3; (g,n) = (2,0); X_G meets X_G\' in the union of the X_H below both', 'proves (research run)', 'research run', 'results_register/REGISTER.tsv'],
 ['SA10-C2', 'the face and flag assertions of folios 15-16 (the run\'s Part A(e), formulated from these folios)', '150/39-42', 'SA10-7', 'EXIT_TOWER:A.11 (Refuted): raw oriented faces fail (ii) and (iv); EXIT_TOWER:A.13 (Refuted): an unpinned flag need not give the cartesian square, at type (3,0); EXIT_TOWER:A.12 (Proved): local triviality of the deployed family and its lattice monodromy', 'refutes in part; proves in part (research run)', 'research run', 'results_register/REGISTER.tsv'],
 ['SA10-C3', 'the reconstruction of a stratified space from its strata and links: the reconstruction (19), the theorem on 035, the flag presentation 039-042', '150/33-42', 'SA10-7', 'the second pass (17 Nov) keeps the notes against the scans; no proof is checked', 'his claim (stated)', 'his page', 'inputs/SA10/second_pass/MPL_150_001-043'],
 ['SA10-C4', 'the theorem on 151/069: cylinder and cone descriptions, base change of tubes', '151/69-75', 'SA10-17', 'none: its proof paragraph is cancelled on the page', 'his claim (proof cancelled)', 'his page', 'MPL_151_032-075 notes'],
 ['SA10-C5', 'the band lemma and the gluing formulas of pro-neighbourhoods', '150/44-84', 'SA10-12', 'none; several steps conditional or self-flagged', 'his claim', 'his page', 'MPL_150_044-084 notes'],
]
CORR = []
SPWHO = 'Claude Opus 5.5 at effort max, second pass of 17 Nov 2026 (recorded by a6d42bf6fe2b0d8a8)'
DROP_WHO = [SPWHO]
_V = re.compile(r'second pass 17 Nov \(Claude Opus 5\.5 at effort max\):\s*(keep|correct|drop|confirm|withdraw|kept|[a-z]+)\s*:?\s*(.*)', re.I)
def corr_auto(P):
    out = []; n = 0
    for r in P:
        m = _V.search(r['note'])
        if not m: continue
        v = m.group(1).lower()
        if v in ('correct', 'drop', 'withdraw'):
            n += 1
            out.append([f'SA10-SP{n}', r['item'], f'{r["entry_id"]} (scans {r["scans"]})', 'note corrected by the second pass' if v != 'drop' else 'note dropped by the second pass',
                        r['object'][:160], (v + ': ' + m.group(2))[:300], 'second pass against the scans, 17 Nov 2026', 'Claude Opus 5.5 at effort max (second pass)'])
    return out
def checks_auto(P):
    out = []
    for r in P:
        m = _V.search(r['note'])
        if not m: continue
        pkg = r['entry_id'].split('#')[0]
        out.append([r['entry_id'], '2026-11-17', SPWHO, 'note checked against the scans (second pass)', (m.group(1).lower() + ': ' + m.group(2))[:240], f'inputs/SA10/second_pass/{pkg}/'])
    return out
CHECKS3 = []
