import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-3_059';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 if new!=line:edits.append([line,new,'Mechanical repair of nested math delimiters in hand macros; ensuremath preserves each visible mathematical symbol in text or display.'])
arrow=r'\diagram{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0.3,0.85)--(0,0);\draw (0.055,0.17) to[out=-5,in=130] (0.18,0.02);\end{tikzpicture}}'
edits += [
 [r'\unsure{L} $(^{42})$',arrow+r' $(^{42})$','The L-like margin mark is an oblique stroke with a short branch near its lower end. Reconstruct the observed graphic instead of assigning it a letter.'],
 [r'\inserted{here}',r'\inserted[typed]{here}','The interlinear here is typed. Its pen placement curve passes above the intact base word is.'],
 [r'\xout{seg}interval',r'\over[typed]{seg}{int}erval','The old seg occupies the same three positions as the typed replacement int; it is not a separately cancelled word before interval.'],
 [r'\uline{homotopy \over[typed]{seg}{int}erval in}',r'\uline{homotopy} \uline{\over[typed]{seg}{int}erval} \uline{in}','The scan has three separate underline strokes under homotopy, interval and in.'],
 [r'\unsure{provisional}',r'provisional','The rotated marginal word is legible as provisional, above the underlined separating.'],
 [r'\xout{\illegible{1}} final objects',r'\xout{unit} final objects','The cancelled word retains the bowls/stems of u, n, i and t beneath the four typed x strikes.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2518:[arrow+r' $(^{42})$','The (42) is clear; the adjacent mark is a branched oblique graphic, not a securely readable L.','correct transcription'],
  2525:[r'\inserted[typed]{here} is','here is typed above a hand placement line; is remains intact.','correct transcription'],
  2526:[r'hold \hand{\ensuremath{(^{43})}}','The source has the note call (43) without a preceding colon.'],
  2527:[r'\hand{\ensuremath{(^{43})}}','The handwritten call follows hold and is retained without invented note text.'],
  2528:[r'\margin{* provisional \uline{separating} W-homotopy interval}','The rotated pencil note reads provisional, separating (underlined), W-homotopy interval.','correct transcription']
 },
 'unsure':[
  [arrow,'The enlarged mark is drawn as a sloping branched stroke; no alphabetic reading is assigned.'],
  [r'\unsure{,}','An x-shaped machine strike is clear after interval, but an underlying comma cannot be confirmed.'],
  ['provisional','The rotated enlargement makes the entire word readable.']
 ],
 'illegible':[['unit','The original unit is legible through the machine cancellation.']],
 'notes':[
  'Reconstructed the oblique branched mark as a graphic beside the clear call (42). Its function is not inferred.',
  'The first word is provisional; separating is underlined, followed by W-homotopy interval.',
  'The cancellation after the first interval covers its old punctuation; retain uncertainty.',
  'The cancelled word in condition a) reads unit and has been recovered.',
  'here is a typed insertion; is is not struck. The placing line curves above it.'
 ],
 'evidence':'Both full halves inspected and six details enlarged, including a rotated view of the terminology note. The opening explicitly retracts the preceding corollary because functoriality of C_u in u still has to be assumed. The three W conditions include a retraction condition stronger than the previously stated mild saturation. The margin qualifies the new term as provisional separating W-homotopy interval. Typed here is an insertion, seg is overtyped by int, and the cancelled unit before final objects is readable. The source’s debote remains; the old punctuation after interval is still doubtful.'
})

key='ps_134-3_060';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=new.replace(r'\phi',r'\hand{\phi}')
 if new!=line:edits.append([line,new,'The phi symbols on this line are handwritten. Also repair any nested dollars inside hand macros using ensuremath, without changing the visible mathematical notation.'])
edits += [
 [r'\mspage{60}',r'\mspage{\hand{60}}','The folio 60 is handwritten.'],
 [r'$e_o \wedge e_1 = \emptyset_{\hand{\mathcal{A}}}$',r'$e_o \hand{\cap} e_1 = \hand{\emptyset}_{\hand{\mathcal{A}}}$','The first relation has a rounded handwritten intersection cap, not a wedge; the empty-set sign is also pen.'],
 [r'\xout{\illegible{4}}',r'\xout{property however will be used in}','The long machine-cancelled phrase is recoverable in the enlarged strip: property however will be used in.'],
 [r'\delta}_i^L \colon e \to L',r'\delta}_i^L \colon e \hand{\to} L','The arrow after e in the definition of the two sections is drawn by hand.'],
 [r'e_{\over{\unsure{o}}{1}}^{\hand{a}} \wedge x = x \ , \ e_{\over{\unsure{1}}{0}}^{\hand{a}} \wedge x \ = e_{\over{\unsure{1}}{0}}^{\hand{a}}',r'\hand{e}_{\over{\unsure{o}}{1}}^{\hand{a}} \hand{\wedge} x = x \ , \ \hand{e}_{\over{\unsure{1}}{0}}^{\hand{a}} \hand{\wedge} x \ = \hand{e}_{\over{\unsure{1}}{0}}^{\hand{a}}','The three e letters and both angular multiplication wedges in the display are handwritten. The old subscripts remain doubtful under their corrections.'],
 [r'\over{\illegible{1}}{a} \hand{\to} \over{\illegible{1}}{I}',r'\over[typed]{\illegible{1}}{a} \hand{\to} \over[typed]{\illegible{1}}{I}','The final a and I have typewriter serifs and overprint earlier characters; only the arrow is handwritten. Earlier characters remain unresolved.'],
 [r'$x\colon \over{\illegible{1}}{a}',r'$x\colon \over[typed]{\illegible{1}}{a}','The final a in the second map is a typed overprint, with its old character still unreadable.'],
 [r'h(\over{\illegible{1}}{x},\over{\illegible{1}}{u})',r'h(\over[typed]{\illegible{1}}{x},\over[typed]{\illegible{1}}{u})','The x and u in the displayed h(x,u) are serif typed overprints rather than pen letters; their old layers cannot be safely read.'],
 [r'\unsure{initial|initiab}',r'initia\over[typed]{\unsure{b}}{l}','The final l is visible as an upright serif over a rounded old form resembling b. Resolve the live word initial while retaining doubt about the old character.'],
 [r'\xout{for} any',r'\deleted{\xout{for}} any','The machine-cancelled for also carries a thick horizontal pen deletion.'],
 [r'$e_o^L \hand{\cap} e_1^L = \emptyset$ ).',r'$e_o^L \hand{\cap} e_1^L = \hand{\emptyset}$ ).','The empty-set sign at the end of the comparison lemma is handwritten.'],
 [r'$e_o^L \hand{\cap} e_1^L = \emptyset$ \ .',r'$e_o^L \hand{\cap} e_1^L = \hand{\emptyset}$ \ .','The empty-set sign in the corollary’s endpoint equation is handwritten.'],
 [r'$\emptyset_{\hand{\mathcal{A}}}$, i.e.',r'$\hand{\emptyset}_{\hand{\mathcal{A}}}$, i.e.','The empty-set sign naming the strict initial object is pen, as is its script-A index.'],
 [r'$a \hand{\to} \emptyset_{\hand{\mathcal{A}}}$',r'$\underset{\text{\begin{tikzpicture}[x=1cm,y=1cm,baseline]\draw[color=blue] (0,0.05)--(0.3,0.05) to[out=-10,in=180] (0.65,-0.04) to[out=0,in=190] (0.95,0.08)--(1.5,0.04);\end{tikzpicture}}}{a \hand{\to} \hand{\emptyset}_{\hand{\mathcal{A}}}}$','A separate wavering pen stroke runs under the map to the strict initial object and toward is. Preserve the visible line beneath the formula without assigning it a textual meaning; also mark the empty-set sign as pen.']
]
draft=src
for before,after,reason in edits:
 if draft.count(before)!=1:raise ValueError((before,draft.count(before)))
 draft=draft.replace(before,after,1)
for line in draft.splitlines():
 if r'\hand{a}' in line:
  edits.append([line,line.replace(r'\hand{a}',r'\over[typed]{\illegible{1}}{a}'),'The small two-storey a letters on this line have typewriter serifs and overprint earlier characters. Preserve those unread old layers rather than misclassifying the replacement letters as handwriting.'])

save_review({
 'key':key,'edits':edits,
 'diffs':{
  2536:[r'\inserted[typed]{still the case for} \xout{property however will be used in}','The added line is typed, and the old machine-cancelled phrase remains readable in the enlargement.'],
  2541:['a left unit and a zero element','The source includes the second article a at the end of the line before zero element.'],
  2543:[r'$e_1^a\wedge x=x,\quad e_0^a\wedge x=e_0^a$','The pen revises the subscripts to 1 for the unit and 0 for the zero element. The earlier subscripts are not securely legible beneath the thick replacements; retain those doubts in the diplomatic text.'],
  2545:[r'$c_{\hand{\unsure{0|a}}}$ ... $\hand{\delta}^L_{\hand{\unsure{0|a}}}$','Both small subscripts are closed, thick loop-and-stem forms. They are compatible with zero over an old a, but the supplied scan does not establish that layering securely; retain the visual ambiguity despite the formula’s expected zero endpoint.'],
  2551:[r'$e_{\hand{1}}$, $\hand{\phi}(u)=\hand{e}^a_{\hand{1}}$','The revised first endpoint and resulting value both have handwritten 1.'],
  2552:[r'$e_{\hand{0}}$, $\hand{\phi}(u)=\hand{e}^a_{\hand{0}}$, $h(x,u)=\hand{e}^a_{\hand{0}}$','The revised second endpoint and both values have handwritten zero.'],
  2557:[r'$\hand{\delta}^L_{\hand{1}}$ and $\hand{\delta}^L_{\hand{0}}$','The source orders the full subobject first with subscript 1 and the empty subobject second with subscript 0.'],
  2558:[r'$e_o^L\hand{\cap}e_1^L=\hand{\emptyset}$','The second factor is clearly e_1^L, not the repeated e_0^L in the witness. The intersection and empty-set signs are pen.']
 },
 'unsure':[
  [r'\unsure{o}','The thick replacement 1 covers the old subscript; a curved remnant is compatible with o but not conclusive.'],
  [r'\unsure{1}','The old subscript is covered by the zero loop; the proposed 1 cannot independently be verified.'],
  [r'\unsure{1}','The right-hand zero likewise obscures the earlier subscript.'],
  [r'\unsure{0|a}','The c subscript has an oval and a rightward foot/stem, leaving zero versus a or an overprint unresolved.'],
  [r'\unsure{0|a}','The delta subscript has the same ambiguity; do not settle it solely from the zero-element argument.'],
  [r'initia\over[typed]{\unsure{b}}{l}','The final typed l is legible; the rounded underlying form may be b and remains explicitly doubtful.'],
  [r'\unsure{interval}','The extra dense t/r-area impression prevents a secure account of the correction. The intended final word is plausible but the doubt is retained.']
 ],
 'illegible':[
  ['property however will be used in','The entire machine-cancelled phrase can be read in the enlarged horizontal strip.'],
  [r'\illegible{1}','The cancellation before L is a dense mixture of pen and typed strokes; no safe old character is recovered.'],
  [r'\illegible{1}','The old character beneath the typed a in u:a remains unreadable.'],
  [r'\illegible{1}','The old character beneath the serif I remains unreadable.'],
  [r'\illegible{1}','The old character beneath the second typed a remains unreadable.'],
  [r'\illegible{1}','The first argument of h is a typed x over an unresolved earlier character.'],
  [r'\illegible{1}','The second argument is typed u over an unresolved earlier character.']
 ],
 'notes':[
  'The cancelled ix before c=ir and the final cancelled i after and are visible; the latter is heavily blackened but its original upright serif remains.',
  'The new subscripts 1,0,0 are clear. The old o/1/1 readings remain doubtful and are not supplied from the witness.',
  'Both c and delta subscripts were enlarged; zero/a remains ambiguous in the ink shape, despite the logical zero-endpoint role.',
  'The new letters in u:a-to-I, x:a-to-L and h(x,u) are typed overprints. Their earlier characters remain unreadable.',
  'The last letter of initial is a typed l over a rounded old form, tentatively b. The live word is now settled, while its old layer stays uncertain.',
  'The wavy pen stroke under the strict-initial-object map is retained graphically beneath that formula; its purpose remains uninterpreted.',
  'The final interval has a dense extra impression near its t/r sequence; the existing uncertainty remains.',
  'The initial th of the is retouched/heavier but the final word is clear. No safe earlier word is reconstructed.'
 ],
 'evidence':'Both complete halves inspected and thirteen detailed crops plus a full-width cancelled-phrase enlargement examined. The first endpoint relation uses intersection, while multiplication uses angular wedges. The old phrase property however will be used in is readable under the inserted still the case for. The equations and endpoint checks consistently revise the unit to 1 and zero to 0, but the earlier respectively wording remains untouched. The c/delta subscripts and several old overprinted characters remain uncertain. In the corollary, delta_1 is the full subobject and delta_0 the empty one; the product equation has e_1 as its second factor. The source’s a factors, set ob and necessay remain unchanged, and the unexplained wavy stroke is retained as a graphic.'
})
