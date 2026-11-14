import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\mspage{7}',r'\mspage{\hand{7}}','The upper-right 7 is pencil handwriting.'),
(r'l\unsure{e}',r'l\unsure{e|r}','The final cell of le has overlapping e/r forms; the l is clear.'),
(r'\unsure{ensembhes|ensembles}',r'ensemb\unsure{h|l}es','The overlap is localized to the h/l cell after ensemb.'),
(r'\unsure{supersinguliers}',r'supersingulier\unsure{s}','The preceding letters are clear; the final s lies at the clipped edge and is overprinted.'),
(r'\unsure{du}',r'd\unsure{a|u}','The first letter is d; the second shows an a-like bowl and right stem, with u still possible beneath the overlap.'),
(r'\deleted{la}',r'\deleted{\xout{la}}','The visible la is covered by type overstrikes and pen cancellation.'),
(r'\inserted{sous-préschéma $E_{o}$ de $E$}',r'\inserted[typed]{sous-préschéma $E_{o}$ de $E$}','The interlinear phrase is typed; its long enclosing insertion curve is handwritten. Section nulle remains uncancelled.'),
(r'x\in V(u)',r'x\hand{\in} V(u)','The membership sign is handwritten.'),
(r'\inserted{pour u}',r'\inserted[typed]{pour u}','Pour u is typed above the line, with a pen insertion curve.'),
(r'\unsure{rel.}',r'\deleted{f}rel.','The letters rel. are readable and preceded by a separately cancelled f-like type letter, crossed in pen.'),
(r'\xout{\unsure{dx}}',r'\xout{d\unsure{e|u}}','A d and a second obscured e/u cell lie beneath the two type cancellation cells.'),
(r'\inserted[typed]{\unsure{On} suppos\xout{ant} E et $E_{o}$ lisses sur X en les points de $v(X)$.}',r'\inserted[typed]{\over{\unsure{O|e}}{e}n suppos\over{\unsure{ant}}{ant} E et $E_{o}$ lisses sur X en les points de $v(X)$.}','The interlinear sentence begins en: e is retraced in pen over an uncertain O/e cell. The ending ant is pen retraced over obscured typing, not visibly deleted. The rest is typed and the leader places it after par u.'),
(r'\unsure{seul}',r'\unsure{s|g}eul','Only the first cell is overprinted, with s and a descending g shape; eul is clear and no final e is supplied.'),
(r'\xout{\illegible{1}} \inserted{de non transversalité à $E_{o}$}',r'\xout{singulier} \inserted[typed]{de non transversalité à $E_{o}$}','The deleted type word is singulier; the replacement phrase above it is also typed.'),
(r'\deleted{\illegible{1}} \inserted{x}',r'\inserted[typed]{$x$} \deleted{$\illegible{1}_{oy}$} \inserted{$x$}','Two uncancelled replacements are visible: a typed x above-left, and a pen x above-right of the struck old expression. The old lower o and y remain legible; its base letter is obscured. Both surviving x marks are retained without deciding their editorial precedence.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','Both arrows in the closing conormal discussion are hand drawn.'),
(r'\inserted{\unsure{un immers.|une immers.}}',r'\inserted{un imm.}','The pen insertion reads un imm., with a final period. The longer immers. expands beyond the visible letters.'),
(r'régulier\xout{e}',r'régulièr\xout{e}','The grave accent over the penultimate e remains visible although the final e is cancelled; it is not removed to regularize the resulting word.'),
(r'\otimes',r'\hand{\otimes}','The tensor sign between the separately underlined E and O is drawn in pen.'),
(r'v_{o}^{*}',r'v_{o}^{\hand{*}}','The pullback star is a filled-in pen glyph.'),
('travailler ensemble',r'travailler \unsure{e|t}nsem\unsure{b|v}le','The first and sixth type cells of ensemble have overlaps/overstrikes, localized as e/t and b/v.'),
(r'\margin{172}',r'\margin{\hand{172}}','Lower-left archive folio 172 is handwritten.')
]
D={
11:'A typed x cancels the final s of les; the line-end le has an overlapping e/r cell.',
12:'The ensemble word has a localized h/l overlap; supersingulier is clear before its damaged/clipped last s.',
16:'The d is secure and second vowel a/u uncertain. Cancelled la is visible under both type and pen. The interlinear sous-préschéma phrase is typed, supported by a pen curve; section nulle remains live.',
17:'Pour u is a typed insertion with a pen leader. Before rel. there is a separately pen-cancelled f; the live rel. is secure. The underline under transversal is pen.',
23:'The two crossed type cells are d plus uncertain e/u.',
24:'Interlinear en supposant has typed text with a pen e and pen ant retouches; the ending is not an independent deletion. Seul has only an initial s/g overlap.',
29:'Cancelled singulier and its interlinear replacement are typed. At the right, both a typed interlinear x and a pen x survive beside the cancelled expression, whose lower oy is readable; both additions are preserved.',
32:'The pen abbreviation is un imm., with no visible ers. The original grave accent in régulièr remains before the cancelled final e. The arrow is pen.',
37:'The full bottom handwriting reads Je vais t’envoyer des notes succintes ces jours-ci.; Je vais begins at the preceding line’s far right, and the remainder continues along the foot. Literal succintes is retained.',
38:'The archive folio 172 is clear handwriting.'
}
N=[
'Upper 7 and lower 172 are clear handwritten folios.',
'The s after le is type-cancelled. The final word has l plus an overprinted e/r cell.',
'The damaged h/l cell is localized in ensembles; the last s of supersinguliers remains uncertain at the right edge.',
'The second vowel after d remains a/u uncertain. The sous-préschéma phrase is typed with a pen insertion curve, and section nulle has no cancellation.',
'A separately cancelled f precedes the clear rel.; the earlier typed rel. à S is retained literally.',
'Two cancelled cells read d plus an uncertain e/u.',
'The interlinear sentence is en supposant, with pen retouches on e and ant. Its stated v(X) has no lower o and is retained.',
'Seul has a same-cell s/g overlap; the remaining eul is clear, with no feminine ending supplied.',
'Singulier is recovered under x strokes; the replacement phrase is typed. Two surviving x additions, one typed and one pen, are separately retained around the cancelled base with lower oy.',
'The exact pen abbreviation is un imm., not an expanded immers. reading.',
'E and O have separate underlines; the tensor symbol is pen. The v and u subscripts/arguments are retained exactly as written.',
'The entire added closing sentence is legible, including the literal spelling succintes.',
'Both image halves, their overlap and all margins were read. No additional marginal paragraph is present.'
]
extra=[dict(line=18,before='dondition',image='dondition',decision='retained',reason='The initial d is visibly typed; it is not corrected to c.',category='literal-spelling'),dict(line=31,before='dodimension',image='dodimension',decision='retained',reason='The tall stem in the initial d is visible.',category='literal-spelling'),dict(line=24,before='v(X)',image='v(X)',decision='retained',reason='The interlinear X has no lower o, unlike the later v(X_o).',category='literal-notation'),dict(line=29,before='single x replacement',image='typed x above-left plus pen x above-right',decision='corrected',reason='Both marks are uncancelled in the scan; their relative editorial authority cannot be established from the ink, so both are retained.',category='layer-layout')]
print(len(complete('ega25_25_172',R,D,N,extra)['decisions']))
