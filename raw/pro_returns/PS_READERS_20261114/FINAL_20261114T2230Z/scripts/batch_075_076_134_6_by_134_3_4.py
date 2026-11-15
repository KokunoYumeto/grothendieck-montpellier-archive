import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-6_075'
ringstar=r'\ensuremath{\diagram{\begin{tikzpicture}[baseline=(s.base)]\node[inner sep=0pt] (s) {$*$};\draw[color=blue,line width=.5pt] (s.center) circle (.42em);\end{tikzpicture}}}'
edits=[
 [r'\mathcal{A}^{\mathcal{M}} \unsure{\cong|\approxeq}',r'\mathcal{A}^{\mathcal{M}} \approxeq','The first sign in (**) has two wavy strokes over one straight bar, so approxeq resolves.'],
 [r'\mathcal{B}_{\mathcal{M}} \unsure{\cong|\approxeq}',r'\mathcal{B}_{\mathcal{M}} \approxeq','The second sign in (**) also has two wavy strokes and one lower straight bar.'],
 [r'\mathcal{B}}_{\mathrm{ab}}',r'\mathcal{B}}_{\overset{\hand{\unsure{\illegible{1}}}}{\mathrm{ab}}}','Preserve the separate blackened mark immediately right of B and above the typed ab. Its identity and any cancellation chronology cannot be recovered.'],
 [r'\xout{the}\inserted{a} final',r'\xout{the}\inserted[typed]{a} final','The raised a is regularly typed above the machine-cancelled the.'],
 [r'\xout{(Ab) and Hom(}',r'\xout{\unsure{(Ab) and Hom(}}','The cancelled run has two offset rows of typing and x/w strikes. The candidate (Ab) and Hom( is plausible, but the whole lower sequence does not resolve securely.'],
 [r'\inserted{(we hope !)}',r'\inserted[typed]{(we hope !)}','The entire parenthetical phrase is typed above the line; its surrounding long curve is a pen placing mark.'],
 [r'\hand{$\cong$} (Ab)',r'\hand{$\approxeq$} (Ab)','The later isomorphism sign repeats two waves over a straight lower bar.'],
 [r'using this identification',r'using th\over[typed]{\unsure{a}}{i}s identification','The i in this overlies a rounded older a-like type impression. The live i is clear; retain doubt on the older cell.'],
 [r'between the categories',r'between the categor\over[typed]{j}{i}es','The i cell has a regular lower j descender and overlapping i impression.'],
 [r'\xout{more}\inserted{\unsure{a}}',r'\deleted{more}\inserted{a}','The old more is crossed by irregular pen strokes, not a machine x row. The small raised a has a distinct loop and trailing stroke and resolves.'],
 [r'defi\xout{n}',r'defi\xout{\unsure{n}}','The final machine-cancelled cell is clipped at the right edge. The n-like lower reading remains tentative.'],
 [r'\inserted{exterior}',r'\inserted[typed]{exterior}','Exterior is typed between the hooks of a pen placing curve. Neither hook is a textual parenthesis.'],
 [r'F \hand{$\circledast$} L',r'F '+ringstar+' L','The inline star has regular typewriter bars, while the enclosing ring is drawn in pen. Preserve the mixed provenance without changing the symbol.'],
 [r'notations introduced here',r'notations int\unsure{\over[typed]{o}{r}}\over[typed]{o}{o}duced here','The first crowded cell has rounded o and r-like impressions whose order remains doubtful; the following o has a repeated regular o impression.']
]
save_review({'key':key,'edits':edits,'diffs':{
 8380:[r'\margin{$*$}, \margin{$\circledast$}, \margin{$*$}','All three separate handwritten signs are present in the left margin and retained.'],
 8367:['Two handwritten approxeq signs; unreadable mark above typed ab','Both signs have two waves and a lower bar. The separate blackened mark after the last B is preserved instead of omitted.','correct transcription'],
 8368:['typed interlinear a','The a has the regular typewriter form and is raised above the cancelled the.','correct provenance'],
 8370:['typed interlinear (we hope !)','The phrase is typed; only its placing curve is pen-drawn.','correct provenance'],
 8373:[r'\hand{$\approxeq$}','The sign has two wavy strokes above a straight lower bar.','correct transcription'],
 8374:['pen-cancelled more and clear handwritten a','The raised a resolves; the deletion of more is an irregular pen crossing.','correct provenance'],
 8377:['typed interlinear exterior','The word is typed within a pen placing curve.','correct provenance'],
 8379:['typed star enclosed by a handwritten circle','The central star has regular horizontal typewriter bars; the ring is penned.','correct provenance']
 },'unsure':[
 [r'\approxeq','Two separate wavy strokes and a straight lower bar resolve the first sign.'],
 [r'\approxeq','The same three-stroke form resolves the second sign.'],
 ['a','The enlarged raised mark has a closed lower loop and a rightward trailing stroke, resolving as a.']
 ],'notes':[
 'The main page number 393 has pen forms; the archive folio 75 is pencilled at lower left. Both are present and the structural page identifiers remain numeric.',
 'Both signs in (**) resolve as approxeq. A separate blackened mark immediately right of the last B and above ab is unreadable; it is retained under a doubt without an asserted cancellation boundary.',
 'The cancelled run has vertically offset repeated typing and regular x/w strikes. Its candidate (Ab) and Hom( is retained doubtfully; the image does not justify fabricating a second complete verbal sequence.',
 'The i of this has an older a-like typed layer, retained doubtfully. Categories has typed i over j. The two crowded cells in introduced are recorded as a doubtful o/r layer and a repeated o.',
 'The solid o in underlined Hom and the solid o in of circling retain their readable circular forms; no independent correction stroke can be distinguished from filled typewriter ink.',
 'The small hand-added a above more resolves, and more has pen cancellation strokes.',
 'The n-like cancelled cell after defi is clipped and remains doubtful. The final g of associating is clipped at the right edge, but its two joined left-hand curves remain sufficient to read g.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-6_075:tensor_glyph','before':r'L\otimes F','after':r'L\otimes F','decision':'retain','reason':'The circle and internal cross have regular thin impressions, unlike the thick freehand arrows. The composite tensor symbol is clear and is retained as typed.'},
 {'source_id':'OBS:ps_134-6_075:compatibility','before':'I did\'nt work it out myself','after':'I did\'nt work it out myself','decision':'retain source claim; guide handoff','reason':'The source explicitly leaves the compatibility for literal A=A^o unchecked. Do not promote that suggestion to an established equivalence in the guide.'}
 ],'evidence':'Both original halves reopened after restoration, in addition to the actual pre-interruption inspection; thirteen enlarged panels and four supplemental panels were inspected. The signs in (**) and after Hom! have two waves over a straight bar. A distinct blackened mark beside the last B is unreadable and preserved above the typed ab. The a replacing the, the phrase (we hope !), and exterior are typed interlinear additions with pen placing marks. The old long cancellation has offset x/w rows and does not securely reveal its whole candidate wording. The i of this retains an older a-like type layer; categories has i over j; introduced has an uncertain o/r cell and a repeated o. More is cancelled in pen and the raised a resolves; the clipped n after defi stays doubtful. The right edge clips associating, but the left portions of the final g remain identifiable. The filled o cells have no separately recoverable correction stroke. The inline circled star is reconstructed with a typed star and pen ring, while the three marginal signs and the other inline star are handwritten. The page finishes section104 by identifying the two tensor actions in the Sets/Ab case and expressly leaving the wider A=A^o compatibility unchecked.'})

key='ps_134-6_076'
edits=[
 [r'1\unsure{2}.8.',r'1\over{\unsure{2}}{2}.8.','The live 2 is penned over a partly obscured earlier 2-like typed digit. Retain doubt only on that lower digit.'],
 [r'(3\over{2}{3})',r'(3\over[typed]{2}{3})','The second digit has regular typewriter 3 impressions over the flat lower stroke of 2; comparison with the later plain (33) confirms the regular type form.'],
 ['As I am at a loss',r'\over[typed]{I}{A}s I am at a loss','The initial A has a distinct straight central I impression with regular serifs beneath it.'],
 [r'\xout{i\unsure{x}}',r'\xout{i}','The i is recoverable under the first machine x. The further x is a cancellation impression in the adjoining space, with no independently visible older character; it is not a textual x. The separate lower hand ! remains live.'],
 [r'\hand{$\varinjlim$}_{a \text{ in } A_{/F}}',r'\mathop{\underset{\hand{\longrightarrow}}{\mathrm{lim}}}\limits_{a \text{ in } A_{/F}}','The letters lim are plainly typed and only the arrow beneath them is handwritten. Preserve the same limit operation with mixed provenance and valid math scope.'],
 [r'\underline{\mathrm{Hom}}_{\hand{$!$}}(A^{\wedge},\hand{$\mathcal{M}$})',r'\underline{\mathrm{Hom}}_{\hand{$!$}}(\underset{\hand{\unsure{\illegible{1}}}}{A^{\wedge}},\hand{$\mathcal{M}$})','The clear A-hat has a separate heavily blackened lower glyph. Its identity is unrecoverable; retain it as a doubtful lower mark.'],
 [r'\inserted{(}\inserted[typed]{prop.3 above and}\inserted{by\}}',r'\inserted[typed]{prop.3 above and} \inserted{by}','The apparent opening parenthesis and closing brace are the continuous hooks of the pen placing curve. The typed interlinear phrase and appended handwritten by are live words, with a boundary between them.'],
 [r'coro\unsure{l}lary',r'coro\deleted{\unsure{a|t}}llary','An extra blackened cell follows coro, and two clear typed l cells follow it. Two oblique heavy pen passes cancel the extra cell; its lower bowl favors a, but a/t remains uncertain. Independent inspection supports the cancellation and the two live l cells.']
]
save_review({'key':key,'edits':edits,'diffs':{
 8382:['105. followed directly by the review sentence','The comparison witness section title is absent. The page begins with the number and the ordinary review sentence, then heading D.'],
 8387:['pseudocotopos','The source clearly types the additional co syllable. Preserve pseudocotopos rather than the witness pseudotopos.'],
 8388:['typed prop.3 above and, followed by handwritten by','The two hook ends belong to a single placing curve. They are not textual parenthesis/brace characters.','correct placement punctuation'],
 8385:['handwritten epsilon, arrows, script M and exclamation marks; typed lim','The arrow under lim is pen-drawn while its three letters are typed. Other listed handwritten symbols retain their provenance.','correct provenance']
 },'unsure':[
 [r'\over{\unsure{2}}{2}','The live handwritten 2 is clear. The underlying typed digit remains partly covered and only tentatively 2.'],
 ['No independent second older character','The second x is itself a regular cancellation impression in the adjacent space. It does not establish a textual old x.'],
 [r'\deleted{\unsure{a|t}}','The draft missed an extra cancelled cell before the two live l cells. Its lower bowl survives but its identity remains uncertain.']
 ],'notes':[
 'The date has a live pen 2 over a doubtful lower typed 2-like digit. The additional and 13.8. is handwritten.',
 'The display label (33) uses regular typewriter 3 over 2; a second crop compares it with the later plain typed reference (33).',
 'The first cancelled cell resolves as i. The further x is a strike in the adjacent space, not a recoverable older letter; the hand ! below is independently visible and unstruck.',
 'Corollary has an extra cancelled a/t-like cell after coro and two clear following l cells. The cancellation is independently confirmed by two heavy oblique pen passes.',
 'All three stars on i in (36) and (37) have the same regular typewriter bars and diagonal arms. No independent pen retouching can be separated; retain them as typed stars.',
 'A separate unreadable blackened lower glyph beneath the clear A-hat is retained as a doubtful mark; it is not silently discarded.',
 'The pencil archive folio 76 is visible at lower left.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-6_076:variance37','before':r'\underline{\mathrm{Hom}}(A,\mathcal M)\longrightarrow\underline{\mathrm{Hom}}^!(\mathcal M,A^\wedge)','after':'Formula (37) retained without adding an opposite','decision':'retain source; guide qualification','reason':'With ordinary natural transformations, i mapped to i-star reverses arrows. The earlier page385 explicitly uses opposite functor categories to express this variance, as independently checked by the section reviewer. The missing opposite is a mathematical caution for the guide, not a source correction.'}
 ],'evidence':'Both original halves reopened after restoration, in addition to the pre-interruption inspection; nine detail panels and five supplemental panels inspected. The live date 2 is penned over a doubtful older type digit. The corrected display number is regular typed 3 over 2, and the initial As has typed A over I. The cancelled inline i is visible, with a further machine x in the next space and a separate live pen ! below; no old textual x is supplied. Formula35 has typed lim and only its lower arrow is handwritten. The A-hat after36 remains clear above an unreadable lower inked glyph. The Remark visibly types pseudocotopos. Its insertion has typed prop.3 above and plus handwritten by, and the long continuous placing curve supplies no textual parentheses or brace. Corollary has a cancelled extra a/t-like cell before two live typed l cells, independently confirmed. The three raised stars are regular typewriter glyphs. The source contains no witness-added section title and no opposite on formula37; the variance issue is handed to the guide author rather than amended in the reader.'})

for key in ['ps_134-6_075','ps_134-6_076']:
 s=(OUT/'checked_pages'/f'{key}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);level=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  level+=1 if m.group()=='{' else -1
  assert level>=0,(key,m.start())
 assert level==0,(key,level)
