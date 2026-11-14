import sys,json
from pathlib import Path
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-3_077';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'^{\wedge}',r'^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The presheaf carets are filled in by pen above the type line.'])
join=r'\begin{tikzpicture}[baseline=(word.base)]\node[inner sep=0pt] (word) {canonic al};\draw[color=blue,line width=.45pt] ([xshift=-.8em,yshift=.15ex]word.south) to[bend right=18] ([xshift=.25em,yshift=.5ex]word.south);\end{tikzpicture}'
edits += [
 [r"$\hand{\Delta}_m$'s",r"$\hand{\Delta}_m$\hand{'}s",'The raised apostrophe after the first Delta is written in pen.'],
 [r'\hand{\Delta^{f}}',r'\hand{\Delta}^{\over{f}{f}}','The first superscript f has a typed f beneath a heavy pen retracing.'],
 [r'\hand{\Delta^{f}}',r'\hand{\Delta}^{\over{f}{f}}','The second superscript f likewise has both typed and pen layers.'],
 [r"definitely isn't",r"definitely is'nt",'The apostrophe stands before n, matching the later is\'nt.'],
 ['Indeed $A',r'I\over{n}{n}deed $A','A small pen n is supplied below the typed n in Indeed.'],
 ['canonical',join,'The typed canonic al has a joining pen curve across its internal blank. Preserve that graphic instruction in the diplomatic text.'],
 ['Thus the topos',r'Thus \over[typed]{A}{t}he topos','The t is typed over a still visible capital A.'],
 [r'\xout{xxx}\inserted[typed]{in}',r'\xout{\unsure{seg}}\inserted[typed]{in}','The earlier first syllable is plausibly seg, but is too heavily crossed to settle; retain the partial recovery as doubtful.'],
 [r'\xout{xxxx}\inserted[typed]{terval}',r'\xout{\unsure{ment}}\inserted[typed]{terval}','The next-line struck letters plausibly continue ment, with uncertainty retained under the x row.'],
 [r'\uline{the wide sense}\inserted{[or weak test category]}',r'\uline{the wide sense} \inserted{[or \uline{weak} test category]}','Weak has its own pen underline in the bracketed insertion; separate the inserted words from sense.'],
 ['(ordered) category',r'(ordered\over{)}{)} category','The closing parenthesis after ordered is reinforced by a straight pen stroke.'],
 [r'\inserted{into C,}',r'\inserted{into C}','The hand reads into C. The rising stroke to its right is the insertion curve, not a comma.'],
 [r'$e_{A^{\hand{\wedge}}}$ !',r'$e_{A^{\hand{\wedge}}}$ \hand{!}','The emphatic exclamation before the closing parenthesis is written in pen.'],
 [r'then\unsure{\hand{,}}',r'then\xout{x}','The mark after then is plainly a typed x, with crossing diagonals and baseline serifs.'],
 [r'\xout{xxxxx} ordered',r'\xout{subse} ordered','The cancelled five-letter fragment has readable s-u-b-s-e, including the b ascender; it is not merely five literal x characters.']
]
# The same Delta-f substring occurs twice; replace the full line as a single operation.
edits=[e for e in edits if e[0]!=r'\hand{\Delta^{f}}']
line=next(l for l in src.splitlines() if 'ding a homotopy interval' in l)
line=line.replace(r'^{\wedge}',r'^{\hand{\wedge}}')
edits.append([line,line.replace(r'\hand{\Delta^{f}}',r'\hand{\Delta}^{\over{f}{f}}'),'Both initial superscript f letters have typed f forms beneath pen retracing; the Delta outlines are wholly hand drawn.'])
save_review({'key':key,'edits':edits,'diffs':{
 2860:[r'\inserted{[or \uline{weak} test category]}','The addition uses square brackets and underlines weak; preserve both.'],
 2862:[r'\inserted{into C}','The live insertion belongs before the closing parenthesis after the slice notation. No independent comma follows C.','correct transcription']
 },'unsure':[[r'\xout{x}','The isolated mark is a typed x rather than a pen comma.']],
 'notes':[
 'The first definitely is\'nt has its apostrophe before n, as does the later is\'nt locally; retain the visible author spelling.',
 'The word is typed canonic al with a small pen joining curve. Its graphic form is reconstructed; the applied form joins canonical.',
 'The ordered closing parenthesis is retraced in pen. Into C is placed before the later closing parenthesis after the category notation; its right-hand curve is not a comma.',
 'The mark after then is a typed x. The right-edge proposi remains clipped at the border.',
 'The first two f superscripts are pen retracings over typed f; the other f letters in the displayed and subsequent notation are typed. The Delta outlines, carets and arrows are pen.',
 'The isolated brown dot is unlike the black writing ink and has no recoverable textual function. It is not promoted to a manuscript punctuation mark.',
 'The small mark beneath the n in Indeed is an n-shaped pen retracing and is now represented.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_077:join','before':'canonic al','after':'canonical','decision':'apply authorial joining instruction','reason':'The pen joining curve closes the typed internal blank; diplomatic preserves the graph and applied reading joins the word.','line':21}], 'evidence':'Both original halves and nine enlarged details inspected. The first apostrophe is before n. Both initial Delta-f superscripts have two layers, while the later f letters are typed. The joining curve in canonic al is retained graphically, with an applied join variant. The original homotopy word may have been seg-ment, but those crossed syllables remain uncertain. The bracketed weak-test addition has an underlined weak. Into C has no comma: its curved right stroke places the insertion. A pen exclamation follows the final-object expression. The isolated after-then character is a typed x, and the final cancelled fragment reads subse. The brown margin speck is not treated as an intentional annotation.'})
vp=Path('PS_READERS_WORK/records/MASTER_VARIANTS_134_3_4.json');v=json.loads(vp.read_text());v=[x for x in v if x.get('source_id')!='OBS:ps_134-3_077:join'];v.append({'key':key,'before':join,'after':'canonical','kind':'authorial word join','reason':'A pen joining curve closes the typed internal blank in canonic al.','source_id':'OBS:ps_134-3_077:join'});vp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

key='ps_134-3_078';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\hand{$\Delta$}',r'\hand{\ensuremath{\Delta}}').replace(r'\hand{$\longrightarrow$}',r'\hand{\ensuremath{\longrightarrow}}').replace(r'\hand{$\leqslant$}',r'\hand{\ensuremath{\leqslant}}').replace(r'\hand{$\subset$}',r'\hand{\ensuremath{\subset}}').replace(r'\hand{$\cap$}',r'\hand{\ensuremath{\cap}}')
 if new!=line:edits.append([line,new,'Use ensuremath for the scan-confirmed handwritten symbols so the source does not open nested math mode inside a display.'])
edits += [
 [r'\deleted{(namely a simplicial maquette)}\inserted',r'\deleted{(namely a simplicial maquette)} \inserted','Keep the replacement parenthetical separated at the word boundary.'],
 [r'\unsure{-|t}',r'\over[typed]{t}{-}','The line-end t has a typed hyphen struck across it before the continuation ty.'],
 [r'$A$\hand{$_{/\Delta}$}$_{\infty}$',r'$A_{\hand{/\Delta}_{\mathrm{oo}}}$','The slash and Delta are penned; the index consists of two separate typed round o forms, not a joined handwritten infinity. Keep it within the slice index.'],
 [r'\hand{\ensuremath{\Delta}}$_\infty$',r'\hand{\ensuremath{\Delta}}$_{\mathrm{oo}}$','The second inline index likewise consists of two separate round typed o letters.'],
 [r'\xout{of} in A\^{}',r'\xout{of} in A\hand{\ensuremath{^{\wedge}}}','The presheaf caret is penned above A.'],
 [r'\hand{\ensuremath{\Delta}}_\infty',r'\hand{\ensuremath{\Delta}}_{\hand{\infty}}','In the display the infinity is a connected, heavy pen figure, unlike the two inline typed oo indices.'],
 [r')\hat{}',r')^{\hand{\wedge}}','The display presheaf caret is hand drawn; replace the empty accent command by the actual raised mark.'],
 [r'T\inserted{h}e Lawvere',r'T\over[typed]{h}{h}e Lawvere','The two vertically shifted h forms have typewriter serifs. This is typed overprinting, not a hand insertion.'],
 [r'A\hand{\^{}}is',r'A\hand{\ensuremath{^{\wedge}}} is','Represent the raised pen caret without an empty accent and restore the visible gap before is.'],
 [r'\unsure{J}',r'\over[typed]{I}{J}','The old capital I has broad horizontal serifs; the final typed J adds a curved left foot.'],
 [r'\inserted{(absolute)}',r'\inserted[typed]{(absolute)}','Absolute and both parentheses are typewritten interlinearly; their placing curve is pen.'],
 [r'\xout{\illegible{1}}'+'\n'+r'\xout{\illegible{1}}',r'\xout{of}'+'\n'+r'\xout{all}','The crossed final word of the line reads of, and the next-line continuation reads all.'],
 [r'F in A\^{}',r'F in A\hand{\ensuremath{^{\wedge}}}','The last presheaf caret is penned.'],
 [r'\unsure{(K,}',r'(K)','The last crossed character has the curved right boundary of a closing parenthesis, not a comma.']
]
save_review({'key':key,'edits':edits,'diffs':{2873:['one stemming','The hand clearly writes one, ending with e, before stemming.']},
 'unsure':[
 [r'\over[typed]{t}{-}','The overstruck t and horizontal hyphen are both visible at the right edge.'],
 [r'\unsure{inex}','The first i and remaining crossed cells are visible, but the complete old four-letter sequence cannot be securely separated.'],
 [r'\over[typed]{I}{J}','The earlier I and final J are distinguishable by their lower serifs and curved foot.'],
 ['(K)','The old expression has a closing curved parenthesis before the fully rewritten pair.']
 ],'illegible':[['of','The o bowl and f ascender survive the x strikes.'],['all','The a and two l ascenders survive in the next line.']],
 'notes':[
 'A typed hyphen is struck across the final t in non-empt before the next-line ty.',
 'The letter is typed J over a clear capital I; preserve both layers.',
 'The two words are of / all across the line break, and the later discarded expression is (K). All are now recovered as machine cancellations.',
 'The proposed inex remains uncertain because the heavy x row merges with the middle and final cells.'
 ],'evidence':'Both original halves and eleven enlarged details inspected. The parenthetical replacement is hand written and reads one stemming. The right-edge t is overtyped by a hyphen. The first two infinity-like indices are separate typed round o letters; the displayed infinity is a joined pen figure. All Delta outlines, the final order and intersection signs, and the presheaf carets are penned. The Lawvere The is a doubled typed h, and (absolute) is an interlinear typewritten insertion. J is typed over I. The earlier line-broken cancellation is of / all, and the discarded pair is (K). The short crossed fragment before category remains uncertain. The source retains insure, the cancelled binary-products/intersection sentence, and the explicit observation that one-point slices obstruct local testness.'})
