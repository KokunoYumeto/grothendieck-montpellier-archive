import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[
 ('% typescript. Draft compared: none.','% handwritten note with mirrored typed show-through. Draft compared: none.','The direct-facing text is the three-line pen note, its interlinear addition and the pen folio. The pale typescript is reversed show-through.'),
 (r'\hand{activités \inserted{\uline{importantes}} à la fois, une mathématique,}',r'\hand{activités \inserted{\uline{importantes}} à la fois, une mathématique,}'+'\n% NOTE: The interlinear importantes is linked to the gap after activités by a large bent pen leader; its right arm runs under importantes. The leader crosses the end of activités without a separate secure cancellation stroke.','The large bent stroke points at the gap after activités, and its right arm underlines importantes. There is no independent stroke securely cancelling activités.'),
 (r'\mspage{\hand{75}}',r'\mspage{\hand{75}}'+'\n% NOTE: A separate short grey curved mark lies to the right of folio75. Its origin and function are uncertain; no additional punctuation or word is assigned.','Both folio digits are hand. Enlargement also shows a separate short grey curved mark farther right, with uncertain origin and function.')
]
M={
 7:'The first word remains the doubtful candidate Idem: its tall initial stroke and compressed following letters do not establish every letter. The short word before Groth. remains the doubtful candidate aussi; its compact crossed/linked strokes do not securely settle the reading. The remainder cf ... Groth. pour avoir plusieurs is handwritten and retained as visible.',
 8:'The line reads activités ... à la fois, une mathématique, with handwritten importantes above it. The bent insertion leader points after activités and continues beneath importantes; it does not securely establish cancellation of the crossed activity-word ending.',
 9:'The full pen line une autre non math. mais valable. is visible. The abbreviation period after math and the final period, visible also at the overlap of the second scan, are retained.',
 11:'The folio75 is handwritten near the lower-left edge; both digits are clear. The separate grey mark to its right is described without assigning it a letter or punctuation role.'
}
N=[
 'Both Idem and aussi remain doubtful after enlargement. The other words on the first line were inspected individually; no context-driven expansion replaces either candidate.',
 'Importantes is interlinear and underlined by the right arm of a bent leader. The point reaches the gap after activités, so the insertion is retained there, before à la fois.',
 'Both digits of the lower-left75 are hand. A separate short grey curved mark farther right has uncertain origin and function and is noted separately.',
 'The pale typed lines are reversed relative to the pen note, with mirrored letters. They are inspected as show-through and are not duplicated as direct-facing text. The sheet edges, folds, tears and spots are distinguished from handwriting.',
 'The three-line note and its interlinear addition are entirely handwritten; both scan parts, all margins and the folio region were inspected.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d(7,'Idem','Compressed pen candidate remains uncertain','retained-uncertainty','The initial tall slanted stroke and following small loops permit the inherited candidate, but do not establish its whole spelling. No outside source is used.','unsure')
d(7,'aussi','Short word before Groth. remains uncertain','retained-uncertainty','The linked low strokes and small vertical at the right do not securely distinguish the whole candidate. The uncertainty remains visible.','unsure')
d('7–9','French handwritten note','Preserved in its archive position','comparison-recorded','No paired line in the reviewed cote25 mathematical text is used to expand this note or resolve its two doubtful words. It remains the separate handwritten note present at cote24 site75.','cote24-comparison')
d('5–11','All direct-facing text, interlinear layer, folio and margins','Every pen word and visible mark inspected in both scans','confirmed','Enlargements checked the first line, the bent insertion leader, the remaining two lines and the folio. The second scan contains the overlapping final period, reversed show-through, and folio75; no additional direct-facing sentence is visible.','full-text')
rec=complete('ega24_24_075',R,M,N,E,visual_notes='Both supplied scan parts read completely. Enlargements checked every word of the pen note, the two retained doubtful candidates, the interlinear importantes with its bent leader, and the folio75. The pale mirrored typescript is identified by its reversed letter orientation and not duplicated as this side’s text. The separate grey mark near75 is recorded with uncertain function/origin.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
