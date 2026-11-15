from review_root import review
from pathlib import Path
import json,csv

P=Path(__file__).resolve().parents[1]
def arrows(key,changes):
 s=(P.parent/'inputs/text/transcription/ps_pages'/(key+'.tex')).read_text()
 for a,b,_ in changes:s=s.replace(a,b,1)
 for line in s.splitlines():
  new=line
  for macro in [r'\longrightarrow',r'\Longrightarrow',r'\Rightarrow',r'\to']:
   new=new.replace(macro,r'\hand{'+macro+'}')
  if new!=line:changes.append((line,new,'The source arrow shafts and heads are continuous pen strokes; the labels remain typed.'))
 return changes

oldmargin="\\margin{I call them now ``open sub-objects'' of $C$, as they correspond to \\unsure{open sets} of $\\mathrm{Top}(C)$ \\unsure{$= C^\\wedge$}}"
newmargin="\\margin{I call them now ``open sub-objects'' of $C$, as they correspond to open subtopoi of $\\mathrm{Top}(C)=C^\\wedge$}"
move_anchor=r'met,\hand{\tikz[baseline=-.2ex]{\fill[blue!65!black] (0,0)--(.08,.18)--(.12,0)--cycle;}}'
move_box=r'\hand{\fbox{\textcolor{black}{for \xout{\unsure{effecting|affecting}} checking contractibility}}}'
c=[
 (r'\over{\unsure{0}}{1}',r'\over{0}{1}','The older typed 0 has a closed oval visible beneath the pen 1 and its lower foot.'),
 ('b) The objects',r'b) T\unsure{\ensuremath{\underset{\mathrm h}{\overset{\perp\perp}{\mathrm h}}}}e objects','The h carries paired raised bars and a lower h-like trace. Preserve this recurrent graphic without asserting pen provenance.'),
 (r'\unsure{hontractible|contractible}',r'\unsure{\over[typed]{c}{h}}ontractible','The initial cell has an h-like tall stem over a rounded c-like body; both are regular impressions, but their final order remains doubtful.'),
 (r'\unsure{hamotopy|homotopy}',r'h\unsure{\over[typed]{a}{o}}motopy','The second cell contains regular a/o impressions. The final vowel order remains doubtful rather than normalized from the mathematical term.'),
 (r'$A^{\hand{\wedge}}$ associated',r'$A^{\wedge}$\hand{/} associated','The raised caret has the same regular symmetric shape as neighbouring typed carets. A separate long oblique pen stroke after it is restored.'),
 ('met, we even',move_anchor+' we even','A pen arrowhead at the gap after met marks the destination of the circled phrase below; preserve its destination separately so the move can be recorded in the master.'),
 (r'interval \xout{\illegible{1}}',r'interval \xout{for}','The old f stem, o bowl and r shoulder are legible under the regular cancellation x impressions.'),
 (r'for \xout{\unsure{effecting}} checking contractibility',move_box,'The whole phrase is enclosed by a pen line and moved to the gap after met. The cancelled word has readable ffecting, but its first vowel remains doubtful.'),
 ('namely we got',r'\over[typed]{\unsure{f}}{n}amely we got','The initial n contains an older tall curved impression, plausibly f, but the base is partly blackened.'),
 (r'\xout{\unsure{Ixxa}}',r'\xout{is to}','The enlarged old run has an i dot, an s, a t ascender and a final o; the intervening x impressions cancel is to.'),
 (r'\xout{$\underline{W}$\illegible{1}}',r'\xout{$\underline{W}_A$\unsure{-}}','The old underlined W and its subscript A are legible. The short terminal impression is probably a hyphen but remains doubtful under its x strike.'),
 (r'conditions \xout{\illegible{1}} which',r'conditions \xout{on $\underline{W}$} which','The old o, n and underlined W remain readable under the regular typewriter cancellation.'),
 (r'introduce\xout{x}',r'introduce\xout{\illegible{1}}','Only the cancelling x is readable after introduce; it does not establish that the old character was itself x.'),
 (r'Let C be in \hand{(}(Cat)',r'Let C be in \over{(}{(}Cat)','The scan has one opening parenthesis with a pen retracing, not two successive opening parentheses.'),
 ('and if b $',r'and if \over{b}{b} $','The b has a heavy irregular pen retracing over its typed stem and bowl.'),
 (r'\cup',r'\hand{\cup}','The union sign is a continuous handwritten curve.'),
 (r'\cap',r'\hand{\cap}','The intersection is a rounded handwritten arch, not a typed caret.'),
 (oldmargin,newmargin,'After rotation the note clearly says open subtopoi, not open sets, and ends Top(C)=C-caret. No doubt remains in these words.'),
 ('such cohomologically',r'such \over[typed]{$\underline{W}$}{c}ohomologically','A typed underlined W remains beneath the initial c; the source correction is restored without altering the live word.'),
 ('which looks very',r'which lo\over[typed]{b}{o}ks very','The second o has an older b stem and upper bowl, both regular typewriter impressions.')
]
review('ps_134-4_084',owner='134_4_tail',changes=arrows('ps_134-4_084',c),doubts={'unsure':[
 ('0','doubt resolved','A complete older oval identifies typed 0 beneath the pen 1.'),
 (r'\unsure{\over[typed]{c}{h}}ontractible','doubt narrowed','The initial regular c/h layers are restored, but their final order remains uncertain.'),
 (r'h\unsure{\over[typed]{a}{o}}motopy','doubt narrowed','The doubt is localized to the regular a/o overprint in the second cell.'),
 (r'\unsure{effecting|affecting}','doubt retained','The cancelled ffecting is readable; the first vowel remains obscured by a regular x.'),
 ('is to','doubt resolved with corrected reading','The old dotted i and the following s, t and o are visible under the x strikes.'),
 ('open subtopoi','doubt resolved with corrected reading','The rotated handwriting has the consecutive letters subtopoi, not sets.'),
 (r'$=C^\wedge$','doubt resolved','The equality, C and raised caret are all visible at the end of the note.')
 ],'illegible':[
 ('for','doubt resolved','The three old letters for can be read through the x cancellation before the typed I-equals insertion.'),
 (r'$_A$\unsure{-}','doubt narrowed','The old subscript A is clear; the following short struck impression remains a doubtful hyphen.'),
 (r'on $\underline{W}$','doubt resolved','The o, n and underlined W are legible beneath the regular cancellation.')
 ]},notes=[
 'The original page number is 170, corrected by pen to 171; the older 0 is now resolved.',
 'The cancelled word before I-equals is for. I-equals is typed. The later cancelled word has clear ffecting but an obscured first vowel, so effecting/affecting remains doubtful.',
 'The box around for checking contractibility and its arrowhead after met are restored. Two linked explicit master variants execute the move without adding punctuation or rewriting the surrounding sentence.',
 'The first struck run is is to; the second contains underlined W with subscript A and a doubtful terminal hyphen.',
 'The rotated marginal note reads open subtopoi of Top(C)=C-caret. Its two draft doubts are resolved.',
 'The intersection is an irregular rounded pen arch, and the union is also hand-drawn.',
 'The lower-left 84 is handwritten archive foliation.'
 ],summary='Both halves, fifteen enlarged details and the rotated marginal note inspected. Resolved old folio0, cancelled for/is-to/on-W and the margin open subtopoi/Top(C)=C-caret; preserved doubts in c/h, a/o, the cancelled first vowel, and the terminal old hyphen. Restored the circled phrase move, typed/pen distinctions and visible letter overprints. The recurrent h graphic remains of uncertain provenance. The Mayer-Vietoris axiom and its full crible/open-subtopos note are retained, as are the author spellings do-nt, standart and is-nt.',differences={
 4667:('Mayer-Vietoris argument','the typescript reads as our transcription','The source spells Vietoris without the additional e found in the witness.'),
 4679:(r'$W_{(\mathrm{Cat})}$','the typescript reads as our transcription','The source index contains parentheses around Cat.'),
 4682:(newmargin,'our transcription corrected','The omitted marginal note explicitly calls cribles open sub-objects corresponding to open subtopoi, not open sets. The two uncertain readings are resolved by the rotated scan.'),
 4685:(r'\margin{$\times$}','the typescript reads as our transcription','A handwritten marginal cross stands beside the question about L1 through L4.')
 })
# A local shape substitution, also retained as a mechanical decision on replay.
rp=P/'records/CHECK_DECISIONS_134_4_tail.tsv'
rows=list(csv.DictReader(rp.open(),delimiter='\t'));fields=list(rows[0])
sid='MECH:ps_134-4_084:arrowhead_glyph'
rows=[r for r in rows if r['source_id']!=sid]
rows.append(dict(key='ps_134-4_084',cote='134-4',site='84',line='14',transcription_reading=r'\hand{\ensuremath{\blacktriangle}}',image_reading=move_anchor[4:],arxiv_reading='',decision='mechanical typesetting repair',reason='The math-font U+25B4 glyph was missing in the diplomatic and apparatus proofs. A local filled TikZ triangle preserves the visible pen arrowhead and its anchor without depending on that glyph.',source_id=sid))
with rp.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
tp=P/'records/TYPESETTING_FIXES_MANUAL.tsv';rr=list(csv.DictReader(tp.open(),delimiter='\t'));ff=list(rr[0])
rr=[r for r in rr if not (r['page_key']=='ps_134-4_084' and 'U+25B4' in r['what_was_wrong'])]
rr.append(dict(reader='all',page_key='ps_134-4_084',source_line='14',what_was_wrong='The inserted arrowhead used a missing U+25B4 math-font glyph.',what_was_done='Draw the local filled triangular pen shape with TikZ; preserve the original anchor and author-transposition variant.'))
with tp.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=ff,delimiter='\t');w.writeheader();w.writerows(rr)
vp=P/'records/MASTER_VARIANTS_134_4_tail.json';vv=json.loads(vp.read_text())
vv=[v for v in vv if not v['source_id'].startswith('NOTE:ps_134-4_084:3:')]
for before,after,suffix in [(move_anchor,'met, for checking contractibility','destination'),(move_box,'','origin')]:
 vv.append(dict(key='ps_134-4_084',before=before,after=after,kind='author transposition',reason='The pen enclosure and arrow move for checking contractibility from after the interval to immediately after met. The cancelled effecting/affecting remains only in the diplomatic origin. Both origin and destination are explicitly represented; no punctuation is supplied.',source_id='NOTE:ps_134-4_084:3:'+suffix))
vp.write_text(json.dumps(vv,indent=2)+'\n')

oldmargin="\\margin{\\unsure{(ii) W str. saturated} i.e. \\unsure{($f_A$ : $\\mathrm{Hot}_W \\to \\mathrm{Hot}_W$} ``exists'' and transf. final object to final object}"
newmargin="\\margin{(if $\\underline{W}$ str. saturated i.e. ($f_A : \\uline{\\mathrm{Hot}}_W \\to \\uline{\\mathrm{Hot}}_W$ ``exists'' and \\unsure{transf.|transforms} final object into final object}"
oldformula="\\inserted{= \\unsure{``$A^{**}A$''}}"
newformula="\\inserted{= \\unsure{``$A$''$A^{*}$}}"
c=[
 (r'Definition} 2.  T\over{H}{h}e',r'Definition} 2.  T\over[typed]{h}{\unsure{H|h}}e','The raised H-like impression is regular typing over h; the final H/h status is uncertain, not a demonstrable pen correction.'),
 (r'b)  T\over{H}{h}e',r'b)  T\over[typed]{h}{\unsure{H|h}}e','The same regular raised H/h impression occurs in this line and is kept doubtful.'),
 (r'$i_A^*$ : (Cat)',r'$i_A^*$ : \over{A}{(}Cat)','The opening parenthesis is penned over a visible typed A, not a plain unaltered parenthesis.'),
 (r'\hand{(}i_A^*\hand{)}',r'\overset{\hand{\frown}}{i_A^*}','Only a single curved pen arch over the functor is present; the draft supplied two enclosing parentheses.'),
 (r'Proposition} 2.  T\over{H}{h}e',r'Proposition} 2.  T\unsure{\ensuremath{\overset{\perp\perp}{\mathrm h}}}e','The paired short upper bars over h are retained graphically, without a definite pen/typing attribution.'),
 (r'\hand{\textcircled{\normalfont ii}}',r'\hand{\textcircled{\textcolor{black}{\normalfont ii}}}','The two i letters are typed; only the circle is handwritten.'),
 (r'T\unsure{\over{H}{h}}e functors',r'T\unsure{\ensuremath{\underset{\mathrm h}{\mathrm h}}}e functors','The h has an extra lower h-like trace, not a clearly legible capital H replaced by pen h.'),
 (r'\begin{tikzcd} (\mathrm{Hot}',r'\begin{tikzcd}[every arrow/.append style={draw=blue!65!black}] (\mathrm{Hot}','Both curved arrows are continuous pen strokes; their typed objects remain black.'),
 (r'in ($\mathrm{Hot}_A$)',r'in ($\mathrm{H}\unsure{\overset{\smile}{\mathrm o}}\mathrm{t}_A$)','A detached cup-shaped mark above o is restored without guessing its origin or intended replacement.'),
 ('deduced from the adjunction morphisms',r'deduced from the ad\unsure{\over[typed]{h}{j}}unction morphisms','The j contains a regular h-like upper impression. Its precise overwrite order remains doubtful.'),
 (oldmargin,newmargin,'The halves were rejoined and rotated. Independent inspection confirms the opening if, not a numbered ii. The Hot-to-Hot map is legible; the abbreviated/full verb after and remains doubtful.'),
 (r'(iii)  T\over{H}{h}e',r'(iii)  T\over[typed]{h}{\unsure{H|h}}e','The initial h has a regular raised H-like overprint, whose final status remains uncertain.'),
 (r'\over{\xout{\illegible{1}}}{\textcircled{\normalfont iv}}',r'\over[typed]{\xout{\illegible{1}}}{\hand{\textcircled{\textcolor{black}{\normalfont iv}}}}','The raised iv is typed over an unreadable cancelled label; its surrounding circle is pen.'),
 (r'A_{/i_A^*(C)}',r'A_{/i_A^{\hand{*}}(C)}','The asterisk has irregular radiating pen strokes, unlike the regular typed stars in the preceding formulas.'),
 (r'T\over{H}{h}e obvious',r'T\over{h}{h}e obvious','The h has a long heavy continuous pen stem and lower retracing over the typed h.'),
 (r'\xout{xx} A',r'\xout{an} A','The old a and n remain readable beneath their regular x cancellation.'),
 (r'\unsure{\over{t}{f}}he\hand{$_A$}',r'\over{t}{f}he$_A$','The pen f clearly replaces t; the remaining he is not cancelled. The lowered A is typed, not handwriting, and is retained where the source places it.'),
 (oldformula,newformula,'The note has two separate capital As, a pair of quote-like marks around the first, and a raised star-like mark over the second. The whole expression remains doubtful; the draft two stars between the As is not visually supported.'),
 ('weaker than  being',r'weaker th\over[typed]{\unsure{q}}{a}n  being','The a contains an older descending q-like impression; its base is retained as doubtful.')
]
review('ps_134-4_085',owner='134_4_tail',changes=arrows('ps_134-4_085',c),doubts={'unsure':[
 (r'\ensuremath{\underset{\mathrm h}{\mathrm h}}','doubt revised','The extra lower h-shaped trace is visible, but the draft H-to-h replacement is not established.'),
 ('(if W str. saturated','doubt resolved with corrected reading','The rejoined and rotated note has i followed by a taller crossed f before W; an independent reader agrees it says if, not ii.'),
 (r'($f_A:\uline{\mathrm{Hot}}_W\hand{\to}\uline{\mathrm{Hot}}_W$','doubt resolved','The f with subscript A, colon, both Hot_W labels and their connecting arrow are legible after rotation.'),
 (r'\over{t}{f}','doubt resolved','The continuous pen f and the underlying regular t are clearly separable.'),
 (r"\unsure{``$A$''$A^{*}$}",'doubt revised','The two As and surrounding raised/quote-like marks are preserved in a revised but still doubtful rendering; no mathematical interpretation is supplied.')
 ],'illegible':[
 (r'\illegible{1}','doubt retained','The original label beneath the regular x strikes and heavy pen circle cannot be securely read.')
 ]},notes=[
 'The first, b) and iii) h cells have regular raised H-like overprints with uncertain final case. Proposition2 and ii) have raised/lowered graphic traces now represented neutrally. The obvious has a clear long pen retracing of h.',
 'The opening parenthesis before Cat is penned over a visible typed A.',
 'Both curved arrows in the displayed pair are handwritten; the object labels remain typed.',
 'After rejoining the halves and rotation, the margin begins if W str. saturated, confirmed independently. The f_A map and final-object condition are clear, with a scoped doubt only on the abbreviated/full verb.',
 'The old iv label remains unreadable; its raised replacement iv is typed and circled in pen. The star in the slice-category expression is handwritten.',
 'The pen f over t is clear, while he remains live and the lowered A is typed. The later equality has two As and uncertain surrounding quote/star marks; its entire formula remains doubtful.',
 'The detached cup above Hot_A and the h/j overprint in the second adjunction are restored. The dark mark above which belongs to the W subscript on the preceding line. Than has an older q-like descender beneath a, now marked doubtful.',
 'The lower-left 85 is handwritten archive foliation.'
 ],summary='Both halves, fifteen details, an enlarged formula and the completely rejoined/rotated marginal note inspected. Corrected multiple pen/typing attributions, restored the arch over i_A-star and old A under the Cat parenthesis, and distinguished typed circled labels from their pen circles. The margin opens if W str. saturated, independently confirmed, rather than numbered ii. Retained the unfinished fhe_A correction and the doubtful two-A formula literally. Recovered cancelled an and marked the other crowded letter/graphic layers without silently regularizing them. Weak-test-category equivalences and all author qualifications remain intact.',differences={
 4693:(r'\hand{\textcircled{\textcolor{black}{\normalfont ii}}}','our transcription corrected','The label ii is typed and its surrounding circle is pen; the witness omits the circle.'),
 4695:(r'\uline{both}','the typescript reads as our transcription','A continuous pen underline emphasizes both.'),
 4696:(r'in (\uline{$\mathrm{Hot}_{\underline{W}}$})','the typescript reads as our transcription','The source underlines Hot_W and retains its surrounding parentheses.'),
 4697:(r'\inserted{(the latter being in $W$ and $W_A$)}','the typescript reads as our transcription','The long handwritten qualification is present after the adjoint-functor pair and absent from the witness.'),
 4698:(newmargin,'our transcription corrected','The omitted marginal condition begins if, not ii, and describes existence of the induced Hot_W endomorphism and preservation of a final object. One abbreviated/full-verb doubt remains.'),
 4703:(newformula,'our transcription corrected','The omitted handwritten equality is revised to match the two visible As and surrounding raised marks, while retaining a doubt on the whole expression.'),
 4704:(r'final object\deleted{s}\hand{,} -','the typescript reads as our transcription','The source cancels s and adds a comma; the witness does not preserve the comma.')
 })
