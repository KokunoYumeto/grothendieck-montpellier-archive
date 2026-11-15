from review_root import review

oldmargin=r'\margin{\unsure{this plus the fact that L5+L3\'} +L1 \unsure{implies} \unsure{W=W$^0$} ! \unsure{If this not known, we need L5* + this condition} \illegible{2} \unsure{cf p. 30} \illegible{1} \unsure{or}}'
# Apostrophes are literal TeX text, not escaped characters.
oldmargin=oldmargin.replace("\\'", "'")
newmargin=r"\margin{this plus the fact that $L5+L3'+L1$ implies $W=W^o$! If this not known, we need $L5+$ \unsure{dual axiom} (\unsure{cofibrations} \ldots{} or}"
review('ps_134-4_077',owner='134_4_tail',changes=[
 (r'F\unsure{l}((Cat))',r'F\over{l}{\ensuremath{\ell}}((Cat))','The typed l is clear beneath the added diagonal pen stroke.'),
 (r'\inserted{with values in (Cat)}',r'\inserted[typed]{with values in (Cat)}','The interlinear phrase has regular typewriter letters and a handwritten placement curve.'),
 ('definition above',r'definition a\over{b}{b}ove','The b is a pen retracing over a visible typed b.'),
 (r'$A \longrightarrow$',r'$A \hand{\longrightarrow}$','The arrow has a continuous hand-drawn shaft and uneven pen head.'),
 (oldmargin,newmargin,'The complete oblique note was rotated and independently read. It gives W=W^o and asks for L5 plus a dual axiom (cofibrations), not L5-star plus this condition or a reference to p.30. The body-overlapped words remain doubtful, and the trailing dots and detached or are retained.'),
 (r'\deleted{statements}\inserted{facts}',r'\over{state}{facts}\deleted{ments}','Facts is written directly over the first five typed letters of statements; the remaining ments is cancelled separately.'),
 (r'\deleted{\illegible{2}}',r'\deleted{\unsure{The most basic are}}','The crossed pen phrase has readable outer letters supporting The most basic are. Its crowded middle remains doubtful, so it is not adopted as a settled reading.')
 ],doubts={'unsure':[
 (r'\over{l}{\ensuremath{\ell}}','doubt resolved','The typed l and its separate diagonal pen stroke are both visible.'),
 (r'\unsure{(}','doubt retained','The blackened regular overstrike after axiom conceals its base; an opening parenthesis remains plausible.'),
 (r'\hand{\unsure{$\vee$}}','doubt retained','The visible V-shaped mark keys the oblique note, but its precise shape/function remains doubtful.'),
 (r"this plus the fact that $L5+L3'$",'doubt resolved','Rotation reveals the complete introductory phrase and both axiom labels.'),
 ('implies','doubt resolved','The connected pen strokes spell implies; the final s crosses pale body type but remains separable.'),
 (r'$W=W^o$','doubt resolved','The two W letters, equality and small raised circular o are visible.'),
 (r'If this not known, we need $L5+$ \unsure{dual axiom}','doubt narrowed with corrected reading','The opening clause is legible. The ordinary plus and the phrase dual axiom replace the unsupported star and this condition; the latter phrase remains doubtful under body type.'),
 (r'\unsure{cofibrations}','doubt revised','The long word begins cofibra- and is independently read as cofibrations; there is no page-reference sequence. Its overlapped ending remains doubtful.'),
 ('or','doubt resolved','The detached lower-left pen word reads or.'),
 (r'\unsure{f}','doubt retained','The first old letter of localizer remains largely covered by pen l; an f-like crossbar is visible but not decisive.'),
 (r'\unsure{f}','doubt retained','The second old first letter is again obscured by pen l; the f reading remains uncertain.')
 ],'illegible':[
 (r'\unsure{dual axiom}','doubt narrowed','The old two-word lacuna belongs to the dual-axiom clause. That clause is now readable as a tentative phrase, with its crossing type still marked.'),
 (r'\ldots{}','doubt resolved as graphic','The small separated trailing pen marks are dots, not an unreadable word.'),
 (r'\unsure{The most basic are}','doubt narrowed','The cancelled phrase has recoverable letters, but the middle remains crossed and uncertain.')
 ]},notes=[
 'The second character of Fl is a typed l with a diagonal pen addition, now resolved.',
 'The b of above is visibly retraced by pen over the old b, now represented.',
 'The blackened old glyph after fibration axiom remains a doubtful opening parenthesis.',
 'Both first letters of localizer have pen l over an obscured f-like typed base; both old-letter doubts remain.',
 'The complete margin was rotated and independently read. It says W=W^o and L5 plus a dual axiom, with cofibrations and trailing dots; it does not cite p.30. The body-overlapped words remain doubtful.',
 'The cancelled pen phrase is tentatively The most basic are; its doubt is retained.',
 'The V-shaped mark before W is the visible anchor adjacent to the long margin note; its uncertain graphic is preserved.',
 'The lower-left 77 is handwritten archive foliation.'
 ],summary='Both halves, eight enlarged details and the rotated long margin note inspected; the latter also independently read. Corrected the typed with-values insertion, above retracing and facts-over-statements layering. Resolved Fl and much of the margin; retained uncertainty in its body-overlapped dual-axiom/cofibrations clause and in the two old localizer letters. The note asks for a dual fibration axiom if W=W^o is not known, not the draft page-30 reference. The final cancelled phrase is now a doubtful reading rather than an unparsed two-word lacuna. The basic-localizer definition and conditional role of L5 are preserved.',differences={
 4544:('page 79 - 88','the typescript reads as our transcription','The typed noun is singular page.'),
 4546:(r'objects\hand{,} \hand{(}which','the typescript reads as our transcription','Both pen comma and opening parenthesis are visible after objects.'),
 4552:(newmargin,'our transcription corrected','Rotation and independent inspection recover W=W^o, an ordinary plus after L5, and dual axiom/cofibrations. The witness omits the whole note, which qualifies the implication from fibration to localization.'),
 4554:(r'functor ...)\hand{*}.','the typescript reads as our transcription','The small handwritten asterisk after the parenthesis is visible and retained.')
 })

review('ps_134-4_078',owner='134_4_tail',changes=[
 (r're\unsure{s\xout{p}}pect',r're\over[typed]{p}{s}pect','The old p descender and new s occupy the same cell. This is a regular typewriter overprint, not an additional cancelled p after s.'),
 (r'H\unsure{o}wever',r'H\unsure{\ensuremath{\underset{\cap}{\mathrm o}}}wever','The main o is clear, with a separate lower arch beneath it. Preserve that uncertain composite instead of suppressing the lower mark when reading o.'),
 (r'\unsure{\xout{in}to|to}',r'\unsure{\over[typed]{in}{to}}','Both cells contain regular overlapping impressions; no row of cancellation x marks is visible. The proposed in-to layering remains uncertain.'),
 (r'\unsure{\over{m}{t}ake|make}',r'\over{make}{turn}','The pen writes all four letters t,u,r,n over make. The last n and the r over the old k are clear; it does not merely change m to t.'),
 (r'exc\unsure{e}pt',r'exc\over[typed]{p}{e}pt','A complete old p descender remains below the final regularly typed e in the disputed cell.'),
 (r'B\unsure{u}t',r'B\unsure{\ensuremath{\underset{\mathrm n}{\mathrm u}}}t','The live u is clear and a lower n-like impression is visible below it. Preserve the uncertain displaced composite.'),
 (r'it\deleted{s}',r'\over{it}{it}\deleted{s}','The pen i and t retrace both typed letters before the cancelled s.'),
 (r'X \rightrightarrows Y',r'X \hand{\rightrightarrows} Y','Both parallel arrows are drawn by hand.'),
 (r'(Cat)$\longrightarrow',r'(Cat)$\hand{\longrightarrow}','The localization arrow is a continuous pen stroke.')
 ],doubts={'unsure':[
 (r'\over[typed]{p}{s}','doubt resolved with layering corrected','The old p descender and the final s are both visible in one cell.'),
 (r'\unsure{\ensuremath{\underset{\cap}{\mathrm o}}}','doubt retained as graphic','The main o is clear; the lower arch remains uninterpreted and is retained graphically.'),
 (r'\unsure{\over[typed]{in}{to}}','doubt retained with mechanism corrected','The two letter cells are overprinted, not x-cancelled; the sequence of old and final impressions is not secure.'),
 (r'\over{make}{turn}','doubt resolved with corrected reading','The pen letters spell turn, including a distinct r and final n over k and e.'),
 (r'\unsure{2}','doubt retained','The old numeral is largely concealed by the pen 1; a 2 remains plausible but not fully exposed.'),
 (r'\unsure{a|e}','doubt retained','The a/e cell is densely overprinted; its final case cannot be securely separated.'),
 (r'\over[typed]{p}{e}','doubt resolved','The old p descender is visible below the complete new e.'),
 (r'\unsure{\ensuremath{\underset{\mathrm n}{\mathrm u}}}','doubt retained as graphic','The live u and lower n-like mark are preserved without asserting why the second impression is present.')
 ]},notes=[
 'The respect cell is a regular p-to-s overprint; the old descender and final s are legible.',
 'However has a clear o with a lower arch beneath it. The uncertain graphic is now represented, not silently omitted.',
 'The word after indeed has two regularly overprinted cells; the proposed in-to sequence remains doubtful.',
 'The pen replacement reads turn, not take or make; all four letters are rewritten over make.',
 'The underline under nal curves slightly into the margin. Its emphasis is preserved as the existing underline; no separate word or symbol is present.',
 'The old digit under L1 and the a/e in than remain uncertain. The old p beneath the e of except is clear and is now recorded.',
 'The lower-left 78 is handwritten archive foliation.'
 ],summary='Both halves and nine correctly located enlarged details inspected (an earlier nine-panel crop sampled nearby text and was not used to settle the readings). Corrected turn over make, respect and except overprints, pen retracing of it, and the arrows. Preserved displaced lower marks in However and But as doubtful composites, and retained the old numeral and than doubts. The source proposition is unchanged. A mathematical caution independently checked for the guide: the emptiness-preserving localizer satisfies L1 and L2 and has discrete-two-point W-aspheric intervals, but its localization is [1], not terminal; equality of all parallel arrows does not imply a terminal localization.',differences={
 4569:(r'$\underline{Hom}(X,Y)$) have','the typescript reads as our transcription','The closing parenthesis after the Hom expression is visible and closes i.e.'),
 4570:('have same image in the localization','the typescript reads as our transcription','No article the occurs before same.'),
 4575:(r'to \over{make}{turn} C into','our transcription corrected','The image shows a complete four-letter pen turn over the typed make, not just a possible t over m. The witness retains make.'),
 4576:('have same image in (Hot','the typescript reads as our transcription','The second occurrence likewise has no article the before same.'),
 4581:('when (Hot) is equivalent to the final category','the typescript reads as our transcription','The source includes the verb is in the proposition; its mathematical assertion remains uncorrected in the readers.')
 })
