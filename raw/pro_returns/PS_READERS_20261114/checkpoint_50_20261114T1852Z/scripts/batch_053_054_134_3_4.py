import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-3_053'
src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\(to|neq|subset|emptyset|cap|mapsto)(?![A-Za-z])',r'\\hand{\\\1}',line)
 if new!=line:edits.append([line,new,'The arrows, inclusion/intersection signs, empty-set signs and inequality strokes on this line are handwritten; retain the typed letters and formula structure.'])
edits += [
 [r'\unsure{aspheric}',r'aspheric','The word is readable in the first paragraph despite a heavier typed impression at r.'],
 [r'\xout{\unsure{are}}is',r'\xout{a}\over[typed]{re}{is}','The old a is machine-cancelled; typed i and s are superposed on r and e. This is a typed correction rather than a separate uncancelled is after the whole old word.'],
 [r'th\over{e}{\unsure{is}}',r'th\over{e}{is}','The enlarged handwritten replacement has a dotted i followed by an s over the old e.'],
 [r'to\hand{t}ally',r'\hand{t}o\hand{t}ally','Both t stems of totally are reinforced/replaced in pen; the initial t was omitted from the handwritten marking.'],
 [r'\xout{If however $V_o \hand{\neq} \hand{\emptyset}$ and $U_o \hand{\neq} \hand{\emptyset}$}',r'\xout{If however $V_o = \hand{\emptyset}$ and $U_o = \hand{\emptyset}$}','In the enlarged cancelled line both old relations are equals signs; the oblique marks belong to the adjacent empty-set symbols, not to the equalities.'],
 [r"\[ L'(U,\hand{\emptyset})",r"\[ \over{U}{L}'(U,\hand{\emptyset})",'First displayed L has a visibly typed U beneath a thick handwritten L.'],
 [r"\qquad L'(V,V_o) = V \hand{\cap} L'(U,U_o)",r"\qquad \over{U}{L}'(V,V_o) = V \hand{\cap} \over{U}{L}'(U,U_o)",'Both L letters in the (*) display are pen replacements of typed U; the old right-hand U strokes remain visible.'],
 [r"$L'(U,U_o)$  \xout{a}",r"$\over[typed]{U}{L}'(U,U_o)$  \xout{a}",'The L after the cancelled the sets is a serif typed overprint on U, unlike the preceding pen replacements.'],
 [r"we know  $L'(X,U_o)$",r"we know  $\over[typed]{U}{L}'(X,U_o)$",'At the right end of the same line, the serif L overprints a typed U.'],
 [r"\[ L'(U,U_o) = U \hand{\cap}",r"\[ \over[typed]{U}{L}'(U,U_o) = U \hand{\cap}",'The following display retains the old U beneath a serif L replacement; the other L in this display is cleanly typed.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2394:[r'\xout{under} by localisation ... $\hand{\mathcal{A}}$','The first word under is machine-cancelled; by localisation is the live continuation and A is inserted in pen.'],
  2398:[r'Assume $X$ \unsure{*is*} a topological space','The two dark signs stand above either side of the slightly lowered typed is. They may be cancelled old letters rather than intentional asterisks; retain the uncertain literal representation instead of treating them as emphasis.'],
  2401:[r'if \deleted{for}\inserted{to} any open','for is clearly crossed by a horizontal pen stroke.'],
  2402:[r'\inserted{to}','The two handwritten letters above the cancelled for read to.'],
  2406:[r'th\over{e}{is}','The pen replacement is securely is, yielding this; the witness retains the earlier the.','correct transcription'],
  2409:[r'empty\hand{;} in other words','The lower dot and descending stroke form an added handwritten semicolon.'],
  2411:[r'\hand{t}o\hand{t}ally','Both t letters carry handwritten strokes, visible in the enlarged word.','correct transcription']
 },
 'unsure':[
  ['aspheric','The full word is clear, including the heavy r.'],
  [r'\unsure{*is*}','The flanking marks remain ambiguous between asterisk-like signs and cancelled former letters; is itself is typed and clear.'],
  ['are','The old a/r/e shapes and the superposed typed i/s are distinguishable in the enlargement.'],
  ['is','The added dotted i and s are legible.']
 ],'illegible':[],
 'notes':[
  'Enlarged the two marks beside is. Their irregular crossed shapes do not establish purposeful asterisks or a safe old word; uncertainty is retained.',
  'Three formula letters are handwritten L over typed U, and three later L forms are typed over U. These layers are now encoded individually; the remaining L letters are plainly typed.',
  'aspheric, functorial and the corollary references are readable despite heavy/doubled type. Corollay in the first heading is the page’s actual misspelling and remains unchanged.',
  'The handwritten is over e is clear in the enlarged crop, so the uncertainty has been removed.',
  'The cancelled a followed by typed i/s over r/e is now represented as a typed correction of are to is.',
  'The arrow in U to L, the first two arrows on the page, the mapsto and the set-theoretic signs are handwritten; all have now been marked accordingly.'
 ],
 'evidence':'Both scan halves read in full, followed by enlarged is/are/this/totally and six L-prime details. The upper proof localizes the interval condition without assuming local asphericity. The corollary proof uses a direct summand L-prime and contains actual U-to-L corrections in two different media. The cancelled intermediate sentence has V_o=emptyset and U_o=emptyset, not inequalities. The handwritten transition is this association, both t letters in totally are pen strokes, and the final correction is local to total. The signs flanking typed is remain unresolved; author spellings independant and Corollay, and letter-o subscripts, are preserved.'
})

save_review({
 'key':'ps_134-3_054',
 'edits':[
  [r'\margin{$^*$ \unsure{cf} (39)}',r'\margin{$^*$ cf (34)}','The enlarged first margin note has a clear cursive cf and a final angular 4, unlike the 9 in the adjacent body call (39). Preserve the discrepancy.'],
  [r'\xout{\unsure{for any}}',r'\xout{for any}','The letters of for any remain legible beneath the machine x cancellation.'],
  [r'Hau\unsure{s}dorf',r'Hausdorf','The crowded type shows a readable s before d; the final f remains a separate pen addition.'],
  [r'\xout{\unsure{an aspheric}}',r'\xout{an aspheric}','The whole old phrase is readable through the machine cancellation.'],
  [r'\over{\unsure{S}}{s}eems',r'\over{S}{s}eems','The capital S underneath the pen lowercase s is visible.'],
  [r'A\^{}',r'$A^{\hand{\wedge}}$','The A is typed and its raised caret is handwritten; replace the malformed free accent with the corresponding mathematical notation.'],
  [r'\deleted{under the}\inserted{pinpointing by} name',r'\deleted{under}\inserted{pinpointing by} the name','The cancellation crosses under only; the curved placement line descends before an intact the. The final reading includes the.'],
  [r'W $\hand{$\subset$}$ F\hand{l}(\hand{$\mathcal{A}$})',r'$W \hand{\subset} F\over{l}{l}(\hand{\mathcal{A}})$','The l in Fl is typed and retraced diagonally by pen. Keep both layers and remove the nested math delimiters around the subset sign.'],
  [r'\[ \hand{$\mathcal{A}$} \hand{$\longrightarrow$} (\mathrm{Hot}) \]',r'\[ \hand{\mathcal{A}} \hand{\longrightarrow} (\mathrm{Hot}) \]','Mechanical repair: remove inner dollar delimiters inside the displayed formula; the script A and arrow are visibly handwritten.'],
  [r'ca\unsure{t}egories',r'categories','The final typed t is legible despite a heavier earlier impression; no alternative word is supported.']
 ],
 'diffs':{
  2416:[r'\inserted{[, or any irreducible space]}','The addition has square brackets and its initial comma; retain these rather than the witness parentheses.'],
  2417:[r'totally aspheric\hand{(39)}.The positive','The raised handwritten body reference reads (39) and is part of the source.'],
  2418:[r'\margin{$^*$ cf (34)}','The enlarged marginal numeral ends with an angular 4; the adjacent body call ends in 9. Preserve both as written.','correct transcription'],
  2419:[r'are\hand{``}sufficiently far away\hand{\'\'}','Handwritten double quotation strokes stand before sufficiently and after away.'],
  2426:[r'pos\textquotedbl\hand{(39)}.For','A second handwritten (39) follows the modelizing-topos expression.'],
  2427:[r'\margin{$^*$ \unsure{strictly} (\unsure{comp.} p.39) \unsure{save few exceptions\dots}}','The lower note was enlarged and rotated. The first word may be strictly, the middle has a clear 39 and a comp.-like abbreviation, but the lower lines do not yield a secure reading. Retain the existing doubts rather than a conjectural expansion.'],
  2429:[r'\deleted{under}\inserted{pinpointing by} the name','The base the is intact; only under is struck. The witness final reading agrees, but the decision comes from the placement/cancellation strokes in the image.','correct transcription'],
  2430:['to be the weak equivalences','The typed article the is present before weak equivalences.'],
  2435:[r'W$^{-1}$\hand{$\mathcal{A}$}','Comparison with the capital W in taking W and the lowercase w in we shows the localization symbol is capital W on the page.'],
  2437:['W saturated namely','There is no comma after saturated on the scan.']
 },
 'unsure':[
  ['cf','The cursive cf is distinguishable in the upper margin enlargement.'],
  [r'\unsure{s}','The underlying letter of the final satisfied correction is covered by the pen d; s remains tentative.'],
  ['for any','All letters can be followed under the typewriter cancellation.'],
  ['s','The final s of Haus is readable despite the superposed impressions.'],
  [r'\unsure{*}','The dark mark before existence may be a cancellation rather than an asterisk; its exact nature remains unresolved.'],
  ['an aspheric','The phrase is legible under the x strokes.'],
  ['S','The upper and lower curves of the old capital S survive around the pen s.'],
  [r'\unsure{n}','The old character in an is almost entirely blackened by the new n; retain doubt.'],
  [r'\unsure{strictly}','The first marginal word resembles strictly, but the central letters are faint and contracted.'],
  [r'\unsure{comp.}','The abbreviation is compatible with comp. but does not securely resolve at the supplied image quality.'],
  [r'\unsure{save few exceptions\dots}','The final two marginal lines remain unresolved after rotation and enlargement; do not present the tentative transcription as established.'],
  [r'\unsure{t}','The old typed letter under the handwritten n of One cannot be securely separated.'],
  [r'\unsure{e}','The pen y of my covers the old character; e is not independently confirmed.'],
  ['t','The final readable letter is t; the overtyped shape does not justify uncertainty about categories.']
 ],'illegible':[],
 'notes':[
  'The listed heavy type impressions were checked in both halves. Their final readings are visible; categories is now settled. Underlying prior characters are not reconstructed without evidence.',
  'Upper margin reads cf (34), while both body calls read (39). Lower note remains doubtful after rotation; preserve the discrepancy and the unresolved wording.',
  'The mark before existence is densely crossed and cannot securely be called an intentional star; the existing doubt is retained.',
  'The cancelled phrases for any and an aspheric are readable in enlarged crops and have been resolved.',
  'The small strokes above the cancelled The do not yield an independent word. The cancellation itself is clear; no conjectural marginal/interlinear wording has been added.'
 ],
 'evidence':'Both complete halves inspected and fourteen correction details enlarged, including a separately rotated larger view of the lower marginal note and a capital-W comparison. Body references (39) are distinct from the margin cf (34). The insertion pinpointing by replaces only under, leaving the typed the alive. The cancelled for any and an aspheric, the final s of Hausdorf and t of categories are readable. The strictness-related lower margin and old characters under several pen replacements remain uncertain. The page proposes exactness/localization and Verdier–Artin–Mazur expectations for modelizing topoi rather than proving them; the source’s monomorphisme and non separated remain unchanged.'
})
