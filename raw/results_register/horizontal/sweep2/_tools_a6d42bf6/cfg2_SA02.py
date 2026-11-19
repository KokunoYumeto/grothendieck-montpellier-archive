# Sweep 2, SA02 gap entries (49 research leads of MPL_84_097-145): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
import re
DATE = '2026-11-18'
RL = 'MPL_84_097-145:records:research_leads'
ITEMS2 = []
_OBJ = {'SA02-1': 'the product of two quadratic algebras (A1*A2, the reduced tensor kernel, the trace pushout)', 'SA02-2': 'relative trace and norm for quadratic algebras ("quasi-quadratic")',
        'SA02-3': 'three quadratic algebras: the contracted triple product, the even subgroup of F_2^3, the étale case', 'SA02-4': 'chi-trivialised extensions of invertible modules: splitting changes, the product of extensions, the "signe étrange"',
        'SA02-6': 'the reused Récoltes et Semailles typescript on the backs of cote 84 (typed pp. 465-474, 480)', 'SA02-8': 'the notes\' apparatus for cote 84'}
HIS = {'SA02-1': 'A1*A2', 'SA02-2': 'quasi-quadratique; trace, norme', 'SA02-3': 'X1 ^ X2 ^ X3; produit contracté', 'SA02-4': 'chi-scindages; signe étrange', 'SA02-6': 'Récoltes et Semailles (typed)'}

def place(g):
    n = int(g['entry_id'].split('#')[1])
    sc = int(g['scans'].split(',')[0]) if g['scans'] else 0
    if n == 49: it = 'SA02-8'
    elif 97 <= sc <= 102: it = 'SA02-1'
    elif 103 <= sc <= 110: it = 'SA02-2'
    elif 111 <= sc <= 124: it = 'SA02-3'
    elif sc in (125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145): it = 'SA02-6'
    else: it = 'SA02-4'
    return dict(item=it, cote='84', kind='Pro records: research lead (per scan)', object=f'{_OBJ[it]}: lead on scan {g["scans"] or "all"}',
                his_term=HIS.get(it, ''), basis='entry-read', note='entry opening read')

OVERRIDE = {
 RL + '#24': dict(basis='passage-read', fidelity='agrees', flag='suspected misreading', note='84/120: the transcription has b) k -> Gamma(X_J, O_X_J) (~ k^J) injective, with X_J marked unsure, as the lead says; the proof needs the sections of the subscheme; the lemma says "sous-schéma", the proof uses a closed one'),
 RL + '#25': dict(basis='entry-read', note='84/121: the same possibly mistaken target X_J; "J\'ai envie de vérifier" the biquadratic structure; "Ceci doit généraliser" left as a programme'),
 RL + '#49': dict(basis='entry-read', flag='the same thing noted with different readings or statements', note='second audit from the scans: 102 "supposant" not "supprimant"; 129 marker 106 then 1; Hom with exclamation exponent on 134, 136; typed 474 present (145), so 475-479 are missing here'),
 RL + '#6': dict(flag='the same thing noted with different readings or statements', note='superseded on 102 by #49 ("supposant", not "supprimant")'),
 RL + '#46': dict(flag='the same thing noted with different readings or statements', note='its absent-pages statement (474-479) is superseded by #48 and #49: typed 474 is on scan 145; 475-478 are in K84-10'),
}
CROSS2 = {'SA02-6': 'typed pp. 475-478 are in K84-10, scans 146-160 (SA01-37, = H01T)', 'SA02-4': 'K84-10 (SA01-36, = H01R)'}
ITEM_FLAGS2 = {'SA02-3': 'suspected misreading at 84/120 (X_J)', 'SA02-6': 'a link across folders (pp. 475-478 in K84-10)'}
FLAGS2 = [
 ['suspected misreading', RL + '#24, #25 (84/120-121)', 'Lemma hypothesis b): "k -> Gamma(X_J, O_X_J) (~ k^J) injectif", with X_J marked unsure. With X_J the hypothesis says nothing (k -> k^J is injective for J nonempty); the proof needs the sections of the subscheme. The lemma also says "sous-schéma" where the proof uses a closed one. Decided on the scan in part 2: the ink reads X_J; his slip; the lemma as written is false and the corrected form holds (REPORTS/cote84_scan120_lemma_hypothesis.md).', 'passage read; scan image (part 2)'],
 ['the same thing noted with different readings or statements', RL + '#6, #32, #37, #39, #46 against #49', 'The second audit (#49), made from the scans, supersedes earlier leads: 102 "supposant", not "supprimant"; the note marker on 129; Hom with an exclamation exponent on 134 and 136; typed 474 is present, so 475-479 are the missing run.', 'entries read'],
 ['a link across folders', RL + '#28-#48 (odd scans 125-145); K84-10 (SA01-37)', 'The Récoltes et Semailles typescript of cote 84: typed pp. 465-474 and 480 on the backs of MPL_84_097-145; typed pp. 475-478 on the backs of K84-10 (scans 146-160), filed under SA01. The run the leads call missing is in the next folder.', 'entries read; codex:K84-10#2'],
]
CHECKS2 = [[RL + '#24', 'note checked against the transcription passage', 'agrees (frozen X_J marked unsure in hypothesis b)', 'MPL_84_097-145_transcription.tex, scan 120']]
NOTES2 = '''
## Sweep 2, part 1: the gap entries (18 Nov 2026)

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. There were 49 gap entries, the research leads of MPL_84_097-145: one lead per scan from 97 to 145, plus the second audit (#49). All are placed in existing items and no new item was needed:

| Scans | Item |
|---|---|
| 97-102 | SA02-1 |
| 103-110 | SA02-2 |
| 111-124 | SA02-3 |
| Even scans 126-144 | SA02-4 |
| Odd scans 125-145 (the typed pages) | SA02-6 |
| #49 | SA02-8 |

**Basis:** 48 entry-read and 1 passage-read (84/120, agrees).

**Flags (3):**
- A suspected misreading at 84/120. In the lemma's hypothesis b), X_J is marked unsure, and the proof needs the subscheme instead.
- The second audit supersedes earlier leads on 102, 129, 134, 136 and 143.
- The typed Récoltes et Semailles pages 475-478, which the leads call missing, are in K84-10. That folder is filed under SA01 (SA01-37).

**What part 2 should take from here:**
- the X_J reading;
- his own "signe étrange" worksheets (134, 136) and the unharmonized signs on 132 and 140, which belong to SA02-4 and need one sign convention;
- the triple-product proposition (119-121), whose hypotheses the leads question.
'''
