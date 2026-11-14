import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-4_048';cur=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
def E(a,b,r):
 global cur
 assert cur.count(a)==1,(a,cur.count(a));cur=cur.replace(a,b,1);edits.append([a,b,r])
E('that the asphericity',r'that \over[typed]{the}{the} asphericity','The three letters the have displaced regular type impressions, with the same live reading.')
E('conditi\\xout{\\illegible{1}}\non on', 'conditi'+r'\xout{\unsure{o}}'+'%\non on','The cancelled edge cell has an o-like lower loop but is clipped. Join the physical continuation conditi/on mechanically; the following on is the separate preposition.')
E(r'$i^*(\hand{\Delta})$',r'$i^{\hand{*}}(\hand{\Delta})$','The superscript asterisk as well as Delta is pen-written.')
E(r'provided only \xout{\illegible{1}} the',r'provided only \xout{\illegible{1}}\unsure{M} the','The preceding short run is machine-cancelled. The terminal M is visible, but its diagonal strokes cannot securely establish an independent x cancellation; retain the M with doubt.')
E('as well deno-',r'as we\over{ll}{ll} deno-','Both final l letters of well are retraced in pen over type.')
E('we think of',r'we thin\over{k}{k} of','The k is retraced in pen over its typed impression.')
E(r'the \xout{\illegible{1}}saturated',r'the \xout{\unsure{sub}}saturated','The cancelled prefix offers sub as a plausible lower reading, especially the final b, but the first two letters remain heavily crossed.')
E('full small homotopy-generatin%\nsubcategory',r'full \over{sma}{sma}ll homotopy-generatin\unsure{g}'+'\nsubcategory','The first three letters of small are pen-retraced. The terminal g of generating is clipped and retained with doubt; restore the word boundary before subcategory instead of joining two words with a TeX comment.')
E(r'\xout{\unsure{possible}}\inserted[typed]{reasonable}',r'\xout{possible} \inserted[typed]{reasonable}','Possible resolves beneath the x row. Reasonable is typed above it, with a separate word boundary in the linearized diplomatic text.')
E(r'\subset F\ell(M)',r'\hand{\subset} F\over{l}{\ell}(M)','The inclusion is penned, and the Fl has a typed l crossed by a pen slash.')
E('modeli\\xout{\\illegible{1}}\nsers', 'modeli'+r'\deleted{\xout{\unsure{ze}}}'+'%\nsers','The two old cells suggest ze but are heavily crossed by both typing and pen. Preserve the doubt, and mechanically join the physical word continuation modeli/sers.')
for line in list(cur.splitlines()):
 if r'A\hat{}' in line:
  E(line,line.replace(r'A\hat{}',r'A^{\hand{\wedge}}'),'The raised hat above A is a separate pen-drawn angle, not plain typing.')
E(r'i^{\hand{*}}\colon M \hand{\longrightarrow}',r'i^{\hand{*}}\colon \over[typed]{M}{M} \hand{\longrightarrow}','The M in the display has repeated regular type impressions; the arrow is already marked as handwritten.')
save_review({'key':key,'edits':edits,'diffs':{
 4023:['i^*(Delta)','The argument is a hand-drawn triangle Delta, not an underlined I.'],
 4025:['for any Delta in M_c^o','The second symbol is another handwritten Delta.'],
 4027:['as we did assume indeed','The source places indeed after assume.'],
 4037:['handwritten folio 48','The pencil number is clearly present at lower left.']
 },'unsure':[['possible','All old letters are visible beneath the row of typewriter crosses.']],
 'illegible':[
 [r'\unsure{o}','The clipped cancelled edge cell has an o-like lower loop, but the whole cell cannot be certified.'],
 [r'\illegible{1}\unsure{M}','The short first run remains unreadable. The following M can be read, but whether it has a separate cancellation is uncertain, so it is not silently removed.'],
 [r'\unsure{sub}','The old prefix suggests sub, but its first cells remain crossed.'],
 [r'\unsure{ze}','The two lower cells suggest ze; machine strikes and pen ink prevent certainty.']
 ],'notes':[
 'The last cancelled cell after conditi is clipped and only tentatively o. The next-line on continues the word; the next on is the preposition.',
 'Provide is readable at the edge. The short cancelled run after only remains unreadable, and the terminal visible M has uncertain cancellation scope; it is preserved with doubt.',
 'Contrac runs to the clipped edge without a visible hyphen. The generating ending has a clipped g candidate, now marked, and the next subcategory begins a new word.',
 'Possible is readable beneath its x row; reasonable is clearly typed above it.',
 'The tiny marks above conversely are two isolated specks with a faint slant, without a recoverable letter or authorial instruction; they are recorded as nontextual ink evidence.',
 'Both initial Deltas, both final Deltas, the two relevant asterisks, arrows, raised hats and folio are handwritten. Additional pen retracing in well, think and small and the display inclusion/Fl slash are now recorded.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_048:faithful','before':'nor embeddable faithfully in modelisers such as (Spaces)','after':'nor embeddable faithfully in modelisers such as (Spaces)','line':43,'decision':'retain author wording','reason':'Faithfully is the visible underlined word, with no fully. For ordinary topological spaces the standard simplex functor is faithful, so the guide qualifies this statement rather than changing the source.'}
 ],'evidence':'Both original halves and ten detail panels inspected. The top the and displayed M have repeated typing. The top cancelled edge cell is tentatively o, and the terminal cancelled cells near modelisers are tentatively ze; both physical word continuations are joined mechanically. The M after the old short cancelled run is visible but not securely independently cancelled, so it remains doubtful and live. Possible resolves below its x row and reasonable is typed above. The first star, four Deltas, arrows, inclusion, all A-hats and folio are penned; well, think and small have additional pen retracing. The generating ending is clipped and retains a doubtful g, with a corrected word boundary before subcategory. The faint marks above conversely form no recoverable textual sign. The last sentence literally says faithfully, with no fully; it is preserved for a guide qualification.'})

key='ps_134-4_049';edits=[
 [r'\xout{xxxxxxx}\inserted[typed]{carefully}',r'\xout{suitably} \inserted[typed]{carefully}','The cancelled word suitably is legible beneath the typed carefully.'],
 [r'\xout{xxxxx} lately',r'\xout{there} lately','The old t-h-e-r-e cells resolve beneath the regular crosses.'],
 [r'ob\over{\unsure{g}}{j}ects',r'o\over{b}{b}\over{\unsure{g}}{j}ects','The b is also pen-retraced. The lower g candidate under j remains obscured and doubtful.'],
 [r'notion of \inserted{a}',r'notion o\over{\unsure{f|a}}{f} \inserted{a}','The f is penned amid a visible raised typed a/f layer. Its old-cell interpretation remains doubtful; the independent following a is a clear handwritten insertion.'],
 [r'categor\over{ies}{y}',r'categor\over{\unsure{i}}{y}\deleted{\xout{\unsure{es}}}','The pen y occupies the first terminal cell, whose old i-like layer is doubtful. The following two cells are independently crossed by typing and pen, with es only tentative.'],
 [r'\xout{xxxxx}\inserted[typed]{outline}',r'\xout{notes} \inserted[typed]{outline}','The old n-o-t-e-s sequence is visible beneath the interlinear typed outline.'],
 ['The two ``expectations',r'T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\over{\mathrm h}{\mathrm h}}$e two ``expectations','Two separate small upper pen marks stand above h, which also has pen retracing below the typed shoulder.'],
 ['The situation',r'T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\mathrm h}$e situation','The h carries two small upper pen marks with horizontal feet and upright stems; preserve them graphically.'],
 [r'$\hand{$\pi$}_{o}$',r'$\hand{\ensuremath{\pi}}_{o}$','The pi is penned; remove the redundant nested math delimiters.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4039:['digressions ...) The two','No separate period appears after the closing parenthesis.'],
 4045:['weak homotopy interval structures too','The second too is explicitly typed and remains live.'],
 4048:['The situation','The visible word is The, with small pen marks around h; not This.'],
 4050:['this seemed by then','The verb ends in the clearly typed ed.'],
 4051:[r'\deleted{indeed}','A continuous pen strike crosses indeed, while the following comma is outside it.']
 },'unsure':[
 [r'\unsure{would}','The pen should covers the first and middle old letters; would remains plausible but not independently fully legible.'],
 [r'\unsure{\circ|0}','The small raised round impression does not securely distinguish a letter o/circle from a zero.'],
 [r'\unsure{g}','The lower round letter and descender are largely covered by pen j; g remains tentative.']
 ],'notes':[
 'Would remains a plausible lower word under should, but several cells are hidden; the doubt is retained.',
 'Deter reaches the clipped edge without a visible hyphen, and the earlier in also touches the edge; no unseen punctuation is supplied.',
 'The M superscript is a small round typed glyph whose o/zero interpretation remains doubtful.',
 'The cancelled the (unique is visibly readable through the typewriter row, including the opening parenthesis.',
 'The b is pen-retraced as well as j; the old g-like lower cell under j remains uncertain.',
 'There is a raised typed a/f layer at the preposition and a pen f, followed by a separately inserted pen a. At the end of category, the pen y covers the first terminal cell and the following two are independently cancelled; lower i/es readings remain doubtful.',
 'Both The words have paired upper pen marks. The first also has a lower pen h-shaped retracing; these are now represented instead of omitted.',
 'The pencil folio 49 is present at lower left.'
 ],'evidence':'Both original halves and nine enlarged panels inspected. Suitably, there and notes resolve through typewriter cancellation; carefully and outline are typed interlinear replacements. Should is pen-written over a still-doubtful would, and the round superscript of M remains o/zero ambiguous. Objects has pen retracing of b and a pen j over a doubtful g. The preposition before the added a has a raised typed a/f layer and penned f; the lower reading remains uncertain. Category has a pen y over the first old terminal cell and separate combined strikes through the remaining two, whose es reading stays doubtful. Both The patches have separate paired upper pen strokes, the first also a lower h retracing. Indeed is definitely pen-cancelled, and no period follows the earlier closing parenthesis. The literal second too, seemed, and The remain as typed. Nested math in pi is repaired.'})
