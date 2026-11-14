import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\inserted[typed]{multiple de 2.}'+'\n','','The typed interlinear replacement belongs above the cancelled end of Prouvons; its place is represented there below.'),
(r'\xout{de la forme 2\deleted{$^r$}\illegible{1}}',r'\xout{de la forme 2^{\deleted{r}}, r\illegible{1}\unsure{1}}\inserted[typed]{multiple de 2.}','De la forme, 2 and its raised r are legible under cancellation; after the comma a further r and a final1-like cell survive, but the intervening material is unreadable. The raised r has an additional pen cancellation. No relation sign is inferred. Multiple de2. is typed above this cancelled span.'),
(r'\deleted{\xout{\illegible{1}}}',r'\deleted{\xout{\unsure{(2)}}}','The short doubly cancelled group has a visible2 and final parenthesis; the proposed opening parenthesis and full group remain uncertain.'),
(r'\xout{la}un',r'\unsure{l|u}\unsure{a|n}','Two overprinted type cells precede corps: l/u then a/n. There are not two spatially separate words with a cancelled la followed by un.'),
(r'Z/\over{p}{2}Z',r'\underline{Z}\hand{/}\unsure{2|p}\underline{Z}','Each Z has its own underline and the slash is pen. The central2/p cell is overprinted; no separate secure pen replacement layer can be isolated.'),
(r'p\neq 2',r'p\hand{\neq}2','The inequality strokes inside the cancelled avec clause are handwritten.'),
(r'ce qui \xout{xxx}',r'ce qui \xout{est}','The cancelled word is legibly est beneath the typed x marks.'),
(r'imp\over{q}{a}ir',r'imp\unsure{a|q}ir','The a/q forms overlap in one type cell; the visible ink does not support a separate handwritten replacement a.'),
(r'fai\unsure{r}e',r'fai\unsure{r|t}e','The cell combines a rightward r shoulder and a tall t-like stroke; both type-overprint candidates remain visible.'),
(r'\inserted{de la forme}',r'\inserted[typed]{de la forme}','The interlinear words are typed and their curved insertion leader is pen.'),
(r'\xout{\unsure{On en conclut immédiatement}}',r'\xout{On en conclut immédiatement}','Every letter of the cancelled phrase is recoverable under the x cancellation.'),
(r'\[ \overset{\hand{\sim}}{d}\xout{*}',r'\[ \overset{\hand{\sim}}{d}^{\deleted{*}}','The old asterisk sits at the upper right of d and is cancelled in pen; the new tilde is pen above d.'),
(r'\deleted{\xout{Q}}\inserted{q}de',r'\deleted{\xout{Q}}\inserted[typed]{q} de','The lower-case replacement q is a typed interlinear character; the capital Q carries both typed and pen cancellation, and de begins the next word.'),
(r'\overset{\hand{\sim}}{d}\xout{*}',r'\overset{\hand{\sim}}{d}^{\deleted{\unsure{*}}}','In the inline occurrence, the pen tilde overlaps the old upper-right mark. An old asterisk is plausible but its form is partly concealed.'),
(r'\unsure{\hand{``}}',r'\unsure{``|*}','The blot before discrimihant contains crossed dark strokes compatible with quotation marks or an asterisk; its glyph and exact layer remain unresolved.'),
(r'\inserted{et}',r'\inserted[typed]{et}','Et is typed above the baseline with a pen insertion curve.'),
(r'Q \in \unsure{\Gamma}',r'Q \hand{\in}\over{\illegible{1}}{\Gamma}','The membership sign and overlaid gamma are pen. The earlier type cell under gamma is not securely recoverable and is not assigned an inferred letter.'),
(r'\otimes 2',r'\hand{\otimes}2','The tensor sign in the determinant exponent is filled in by hand; its following2 is typed.'),
(r'(\xout{1}a)',r'(\unsure{a|1})','The label consists of one overwritten a/1 type cell inside the parentheses, rather than separate cancelled1 and live a.'),
(r'base\hand{, et',r'base,\hand{ et','The comma after base has the same typed form as the other baseline commas; the addition beginning et is pen.')
]
D={
5:'The upper-right folio has two closed handwritten loops and reads8; no sequence-based change to3 is made.',
9:'Multiple de2. is typed above and attached to the cancelled end of Prouvons; its placement has been moved to that span.',
10:'Cela is legible under typed x cancellation. The old terminal phrase preserves its readable de la forme2, raised r, comma, another r and uncertain final1-like cell; the missing relation is not guessed.',
11:'The short group after que has typed and pen cancellation; a candidate (2) remains uncertain as a whole.',
12:'The two cells before corps are type overprints l/u and a/n. Both Zs are underlined, the slash is pen, and the middle2/p remains ambiguous. The added closing parenthesis is pen. Avec p-not-equal2 is pen-cancelled, the inequality itself is pen, the typed n-apostrophe is x-cancelled, and est at the line end is readable beneath x marks.',
13:'The q/a cell in impair is a same-cell type overprint, without a securely separable pen a.',
15:'The inserted c and its V-shaped leader are pen. The r/t cell in faire remains uncertain.',
16:'De la forme is a typed interlinear addition with a pen leader. Standart and the following degree n are unchanged.',
20:'On en conclut immédiatement is fully legible beneath typed cancellation.',
21:'The tilde is hand drawn; the old asterisk lies at the upper right and has a separate pen strike.',
24:'The capital Q is cancelled by both layers; the lower-case q above it is typed. The final accented character of degré is clipped and remains uncertain.',
25:'The second tilde is pen, with a partly concealed old raised asterisk. The isolated black mark before discrimihant remains quote/asterisk uncertain with unresolved layer. The word itself visibly has h in discrimihant.',
27:'The extra e in de-une is visibly cancelled by type x; the apostrophe remains live.',
32:'The inserted et is typed with a pen leader; the extra final e of toute is x-cancelled. The literal associéer is retained.',
33:'The d before e is x-cancelled exactly as typed. The short qu. addition at the right end is handwritten and is not expanded.',
34:'The membership sign, gamma replacement, tilde and tensor sign are handwritten. The earlier character under gamma is illegible; no contextual reconstruction is supplied.',
37:'The label contains a single a/1 overprinted cell. The comma after base is typed; et fonctorialité pour isomorphismes en underlined E and its final period are handwritten.',
39:'The tilde over d is pen; the formula and the parenthetical ou d(Q) are otherwise retained literally.',
42:'The lower-left176 is a handwritten archive folio.'
}
N=[
'The cancelled end is partially recovered as de la forme2 with a raised r, then comma and r and an uncertain final1-like cell. The intervening mark remains illegible; multiple de2. is typed interlinearly and attached to this span.',
'The middle2/p cell is an unresolved type overprint, not a securely isolated handwritten2. Both Zs have underlines. The slash, closing parenthesis, inequality and cancellation of avec are pen; n-apostrophe is cancelled by type x.',
'The disputed cell in faire visibly combines r/t forms and retains both candidates.',
'On en conclut immédiatement is fully readable beneath the cancellation and no longer needs a word-level uncertainty.',
'All four tildes are pen. The old marks in the first two occurrences sit at the upper right of d; the display asterisk is secure, while the inline one is partly covered by the tilde.',
'The black mark before discrimihant is retained as quote/asterisk uncertainty; neither its precise shape nor its layer is settled.',
'A pen gamma is visible over an unreadable older type cell. The pen membership sign is recorded separately.',
'The last character of degré remains clipped and uncertain. Essentielle ends at the edge; no unobserved hyphen is supplied before ment.',
'Upper-right8 and lower-left176 are handwriting; the8 is retained despite the surrounding folio sequence.',
'The empty source-note field supplies no separate concern; the full margins were nevertheless inspected.',
'No long marginal addition occurs. The full short handwritten addition to condition (a), all pen signs, insertion leaders and cancellations were read.'
]
extra=[
dict(line=14,before='à un discriminant nul',image='à un discriminant nul',decision='retained',reason='The typed accent and wording are visible; no grammatical substitution a is made.',category='literal-spelling'),
dict(line=25,before='On appela',image='On appela',decision='retained',reason='The scan has appela without an extra l or final e.',category='literal-spelling'),
dict(line=26,before='indétérminée',image='indétérminée',decision='retained',reason='The visible accents are retained as typed.',category='literal-spelling'),
dict(line=39,before='ou d(Q)',image='ou d(Q)',decision='retained',reason='No grave accent is supplied to the visible unaccented ou.',category='literal-spelling')
]
print(len(complete('ega25_25_176',R,D,N,extra)['decisions']))
