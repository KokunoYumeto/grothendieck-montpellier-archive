import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review

save_review({
 'key':'ps_134-3_051',
 'edits':[
  [r'\inserted{$(i\hand{\geq}1)$,}',r'\inserted[typed]{$(i\hand{\geq}1)$}', 'The parentheses, i and 1 above the first line have typewriter serifs; only the inequality is drawn in pen. The curved placement line ends in an upturn, not a comma.'],
  [r'\deleted{any}\inserted{for}',r'\inserted{for} any','The enlarged top-right crop shows intact typed any below the insertion curve; for is inserted before it, not substituted for it.'],
  [r'\xout{\unsure{of}} U',r'\xout{of} U','The o bowl and tall f remain readable under cancellation before U.'],
  [r'objects \inserted{U}',r'objects \inserted[typed]{U}','U has the same serif typeface as the base line and sits above the placement stroke.'],
  [r'\xout{The \unsure{notion of}}',r'\xout{The notion o}','The enlarged machine cancellation ends with a round o; no following f is present before the blank preceding Clearly. Preserve the incomplete cancelled phrase.'],
  [r'\inserted{$A\hat{}$}',r'\inserted[typed]{$A^{\hand{\wedge}}$}','The inserted A is typed; the small raised caret is handwritten.'],
  [r'the\xout{\unsure{ir}} case',r'the\xout{ir} case','Both the narrow i and final r are visible under the machine cancellation in their.'],
  [r'$\hand{\mathcal{A}} = A\hand{\hat{}}$',r'$\hand{\mathcal{A}} = A^{\hand{\wedge}}\deleted{\illegible{1}}$','A has a raised pen caret and a separate dense crossed-out character at its right on the base line. Restore that visible unresolved cancellation; use a proper raised caret.']
 ],
 'diffs':{
  2357:[r'cohomology \xout{groups} $H^i(X,G)$','The word groups is machine-cancelled across all its letters; the later witness does not govern the diplomatic layer.'],
  2358:[r'\inserted[typed]{$(i\hand{\geq}1)$}','Typed interlinear condition with handwritten inequality; there is no independent comma after it.','correct transcription'],
  2359:[r'namely \inserted{for} any','Insertion stroke passes above any without cancelling its letters. The image retains any, absent from the witness.','correct transcription'],
  2360:['0-connexity','The page clearly types connexity; retain the author’s word.'],
  2363:[r'objects \inserted[typed]{U} of','Serif U above the line is typed; only its placement stroke is drawn.','correct transcription'],
  2366:[r'\hand{*}\uline{locally aspheric} ... \margin{* loc. modelizing (cf § 39)}','The dark asterisk before locally aspheric corresponds to the paler margin note with loc. modelizing and the reference to §39.'],
  2367:[r'\uline{locally aspheric} .','The underline and separated period are present; no quotation marks enclose the term.'],
  2369:[r'\inserted[typed]{$A^{\hand{\wedge}}$}','Typed A, handwritten caret and a placement curve are distinguishable in the insertion after topoi.','correct transcription']
 },
 'unsure':[
  ['of','Enlarged cancellation retains recognizable o and f.'],
  ['notion o','The machine-cancelled phrase has no final f; it stops after the round o.'],
  ['ir','The two cancelled letters of their are separately visible.'],
  [r'\unsure{s}','The old character above the handwritten replacement i is covered by a solid blot; s remains only a tentative reading.']
 ],
 'illegible':[
  [r'\illegible{1}','Small mixed machine and pen cancellation after aspheric is too dense to recover its underlying character.'],
  [r'\illegible{1}','The separate vertically scribbled deletion after equivalent and its colon has no reliable underlying letter.']
 ],
 'notes':[
  'All arrows on the page, both inequalities, membership sign and script A forms are drawn in pen; the bases of the formulas are typed.',
  'The curve introduces for before the untouched any. Corrected both placement and deletion status.',
  'Both occurrences of generating are typed above the line; the curved line before full positions the word and does not cancel full.',
  'The l of well and t of Let show superposed typed impressions. Their final letters are clear, but the underlying impressions do not support a distinct recoverable earlier word.',
  'Both small cancellations were enlarged; neither yields a safe old character. The dense separate mark beside the final A caret is also now retained as an unresolved deletion.',
  'The final i of topoi is a handwritten replacement; the underlying old character is still uncertain.'
 ],
 'evidence':'Both complete scan halves inspected, followed by enlarged first-line, cancellation, replacement and final-A details. The first line has mixed typed/pen (i>=1), an intact any with handwritten for inserted before it, and cancelled groups. U and A in the interlinear insertions are typed; A’s caret is pen. The cancelled fragment after arrows ends The notion o, not notion of. The margin reads * loc. modelizing (cf §39), associated with the asterisk before locally aspheric. The bottom assertion that the product conditions imply T1 remains exactly as written; page 52 supplies the nonemptiness qualification. Unreadable old characters after aspheric, after equivalent and under the final A caret remain explicit; no witness-based completion was used.'
})

save_review({
 'key':'ps_134-3_052',
 'edits':[
  [r'for any \xout{\illegible{1}}',r'for any \xout{\unsure{coeffi}}','The machine cancellation at the right end of the line retains o/e/f/f/i shapes, suggesting the unfinished coeffi; retain uncertainty over the initial character.'],
  [r'\inserted{two,}',r'\inserted{two}','The apparent comma is the upturned end of the placement curve; there is no independent punctuation after the handwritten two.'],
  [r'\inserted{not empty and}',r'\inserted[typed]{not empty and}','The interlinear phrase is in serif type, with a hand-drawn placement line; the base words not the remain uncancelled.'],
  [r'\unsure{31|3)}',r'31','The enlarged reference distinctly shows 3 followed by a vertical 1; the nearby curved stroke belongs to the old parenthesis below.']
 ],
 'diffs':{
  2377:[r'if it \xout{satisfiesxthe} is','The typed it is present before the cancelled original predicate.'],
  2378:[r'is \inserted{[``non empty'',]} locally aspheric','The bracketed handwritten phrase is linked by a placement curve immediately before locally; it supplies an explicit nonemptiness qualification.'],
  2379:['satisfies moreover the','The last words of line 1 and the start of line 2 clearly give satisfies moreover the.'],
  2380:[r'\margin{\unsure{Anal. p.\ 351, Cor.\ 1} \unsure{hay mon Rep?}}','Rotated and enlarged the upper-left note. The p.351/Cor.1 portion is plausible, but the rest is crossed by broad slanting pencil strokes and does not support a secure expansion. Retain both doubts; cancellation status itself is uncertain.'],
  2382:[r'any \inserted{two} non-empty','The insertion reads two without a comma; the curve ends in an upward hook.','correct transcription'],
  2384:[r'\inserted[typed]{not empty and} not the union','The added words are typed above the line; the placement curve is handwritten and does not delete not the.','correct transcription'],
  2387:['Hausdorf, this means also','The page includes this at the right end of the line, followed by means also on the next.'],
  2392:[r'\inserted{section 31} \deleted{p. 39-40}','The handwritten section number is 31; the old page reference remains legible beneath a horizontal pen cancellation.','correct transcription']
 },
 'unsure':[
  [r'\unsure{Anal. p.\ 351, Cor.\ 1}','The rotated margin has recognizable page and corollary numerals, but the opening abbreviation and connector cannot be settled through the crossing strokes.'],
  [r'\unsure{hay mon Rep?}','Upper part of the rotated marginal note remains too faint and heavily crossed to establish its wording or cancellation status.'],
  [r'\unsure{l}','A narrow upright survives under the x after topological; it could be l but cannot be identified securely.'],
  ['31','The enlarged lower reference has a clear 3 and an upright 1.']
 ],
 'illegible':[
  [r'\unsure{coeffi}','The enlarged machine strike supports an unfinished coeffi but not all strokes securely; replace total illegibility with an explicitly tentative reading.'],
  [r'\illegible{1}','The double cancellation immediately after object obscures its underlying character(s).']
 ],
 'notes':[
  'Inspected the full margin and three rotated enlargements. Keep both uncertain readings and do not promote the possible note to a secure source reference; broad crossing strokes may cancel it.',
  'The bracketed handwritten non empty is inserted before locally, after is. Its brackets, quotation marks and internal comma are visible.',
  'not empty and is typed above the base line. Its placement curve crosses above not the without cancelling those letters.',
  'clearly is a typed insertion above the machine-cancelled that, as already encoded.',
  'The handwritten reference reads section 31; p.39-40 is cancelled by a single horizontal pen stroke.',
  'Both háčeks above Cech and the membership sign are handwritten; the surrounding letters and indices are typed.',
  'above contains a crowded typed b/f impression but a readable final b; the cancelled o before for is clear. The extra character after topological and the cancellation after object remain uncertain. The cancelled fragment before constant coefficients tentatively reads coeffi.',
  'The dot above the final typed i in topoi is reinforced by pen. The readable word remains topoi; no different underlying letter can be established.'
 ],
 'evidence':'Both complete halves opened and read with the page text; enlarged and rotated marginal writing and eight correction details. The opening explicitly adds ["non empty",] before locally aspheric. Corollary 2 retains Hausdorf and this. In Proposition 2 the hypothesis totally aspheric is machine-cancelled, and both parenthetical equivalents are cancelled, leaving aspheric over the final object as the condition for an arbitrary topos. The interval sections and the empty-set signs, mapsto and implication are pen additions; Conversely is handwritten. The lower reference securely reads section 31 and the final two-line proposed constant-map phrase is cancelled by hand. The top-left marginal note and two old characters remain uncertain.'
})
