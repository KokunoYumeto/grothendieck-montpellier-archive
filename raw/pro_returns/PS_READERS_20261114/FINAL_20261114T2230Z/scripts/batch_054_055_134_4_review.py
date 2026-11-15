import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
key='ps_134-4_054';edits=[
 [r'\inserted{assume M,}',r'\inserted{assume M}','The apparent final comma is the upturned end of the continuous placing curve beneath assume M; no separate comma is present.'],
 [r'\inserted{a)}b)c)e)',r'\inserted{a)} b)c)e)','Keep an actual boundary between the inserted label a) and the following typed label.'],
 [r'W$\hand{\subset}$F$\hand{\ell}$(M)',r'W$\hand{\subset}$F$\over{l}{\ell}$(M)','The l is typed, with a separate pen slash converting its appearance to ell.'],
 [r'\xout{xxxM}',r'\xout{on }\unsure{M}','The crossed lower letters on resolve. The final M remains visible, but an independent cancellation through that cell is not secure.'],
 [r'F$\hand{\ell}$(M) consists',r'F$\over{l}{\ell}$(M) consists','The second Fl likewise retains a typed l underneath its pen slash.'],
 ['b) For any connected',r'\over{b}{b}) For any connected','The label b has a pen retracing over its typed stem and loop.'],
 [r'by \deleted{a} \inserted{finite} chain',r'by a \inserted[typed]{finite} chain','Finite is typed above the line. Its continuous placing curve runs under the word and points before chain; the baseline a is live, not cancelled.'],
 [r'\xout{\unsure{of M asph}}',r'\xout{of M asph}','All lower letters of of M asph are recoverable beneath the regular x row.'],
 ['THe condition',r'T\over[typed]{h}{H}e condition','A regular capital H is superimposed on the lower h-shaped impression.'],
 [r'\xout{\unsure{at any rate}}',r'\xout{at any rate}','The full old phrase is readable beneath the regular typewriter cancellation.'],
 [r'T\over{\unsure{h}}{\unsure{h}}e conditions',r'T$\overset{\hand{\scriptscriptstyle\circ}}{\over{\mathrm h}{\mathrm h}}$e conditions','The baseline h is retraced in pen and has a separate small closed pen loop above it. Preserve the upper graphic as well as the live letter.'],
 [r'statement\xout{s}',r'statement\unsure{s}','The terminal s is densely inked, but the patch does not establish cancellation rather than retracing. Keep the live-letter possibility.'],
 [r'\margin{$+$}',r'\margin{$\times$}','The pencil margin cross has two oblique strokes, not a horizontal and vertical plus.'],
 [r'co\over{\unsure{w}}{n}versely',r'co\over{w}{n}versely','The lower typed w and the superimposed pen n can be separated in the enlarged panel.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4125:['W be','Be is clearly typed, with an e rather than the witness y.'],
 4132:['(*) Compare with p. 135.','The complete handwritten margin note and its matching call after paragraph are visible.'],
 4127:[r'$s_i = \hand{\delta}_o$','The first subscript is visibly i. Preserve this apparent endpoint-index slip, rather than the witness correction to zero.']
 },'unsure':[
 ['of M asph','The old letters are all readable beneath the regular typewriter row.'],
 [r'\unsure{W}','The live pen W is clear, but its small lower impression remains uncertain.'],
 ['at any rate','The entire phrase resolves beneath the machine cancellation.'],
 [r'\unsure{Certain}','The middle and final cells are too heavily superimposed to settle Certain; retain the candidate.'],
 ['h','The lower typed h is visible beneath the retracing.'],
 ['h with an upper pen loop','The pen h is live; the separate raised loop is preserved graphically.'],
 ['w','The lower typed w is distinguishable from the pen n.']
 ],'illegible':[[r'\illegible{1}','The dense oval scribble after h_W hides the old run completely.']],
 'notes':[
 'The inclusion signs, pi, deltas, membership signs, comparisons and arrows are penned. Both Fl occurrences retain typed l under a pen slash. The finite insertion is typed, and its curve does not delete a.',
 'Of M asph and at any rate resolve; Certain remains doubtful. The earlier old on resolves while the final M cancellation remains uncertain.',
 'The conditions has a lower h retracing and separate raised closed pen loop. The prime in a-prime is handwritten and visible.',
 'The old typed w and the replacement pen n in conversely are distinguishable.',
 'The blacked-out run after h_W remains illegible beneath the oval pen scribble.',
 'The margin sign is an oblique pencil cross, and the archive folio 54 is visible at the foot.'
 ],'evidence':'Both original halves and eleven enlarged panels inspected. Assume M has no independent final comma: the apparent punctuation is the placing hook. The a-label is handwritten; both Fl letters are typed l with pen slashes. The old on before h_M resolves, but cancellation of the final M is not secure and remains doubtful. The b label is pen-retraced. Finite is typed interlinearly, and the placing curve leaves the baseline a live. Of M asph and at any rate resolve beneath machine x rows; Certain remains tentative. THe has a typed H over h. The later The has a pen h retracing and raised loop. The W lower layer and the dense erased word after h_W remain uncertain or illegible. The final s of statements remains live under a doubt because deletion is not secure. The margin cross is oblique. Conversely has a pen n over typed w. The source be, s_i=delta_o and singular two section are retained; the margin reference to p.135 is fully legible.'})

key='ps_134-4_055'
move=r'\margin{\diagram{\begin{tikzpicture}[baseline=0ex,x=1em,y=1ex]\draw[color=blue,line width=.6pt] (1,-4.2)--(.2,-4.2)..controls(0,-4.2)and(0,-4)..(0,-3.8)--(0,-1.2)..controls(0,-1)and(.2,-1)..(.4,-1)--(1,-1);\draw[->,color=blue,line width=.6pt] (-.2,-2.3)..controls(-1.1,-.8)and(-.8,2)..(1,3.6);\end{tikzpicture}}}'
group=r'\margin{\diagram{\begin{tikzpicture}[baseline=0ex,x=1em,y=1ex]\draw[color=blue,line width=.45pt] (.15,1.5)..controls(-.1,0)and(-.1,-3)..(.15,-4.7);\end{tikzpicture}}}'
edits=[
 [r'\xout{\unsure{axp}}',r'\xout{a\unsure{s|x}p}','The first a and final p resolve. The middle letter is mixed with the regular x strike and may be s or x.'],
 ["% NOTE: a handwritten bracket with an arrow in the left margin links the four lines a''), a'''), a), a') below (re-ordering mark)",'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+move,'Reconstruct the bracket around the lower two conditions and the curved arrow carrying them before the first condition; do not turn the graphic instruction into manuscript prose.'],
 [r"\over{a)}{\unsure{a'')}}",r"\over{a)}{a'')}",'The handwritten first label has two distinct prime strokes before its parenthesis.'],
 [r"\over{a')}{\unsure{a''')}}",r"\over{a')}{a''')}",'The next handwritten label has three primes before its parenthesis.'],
 [r"\hand{b''')}same",r"\hand{b''')} same",'Keep an actual word boundary between the inserted fourth label and same.'],
 ["% NOTE: a handwritten bracket in the left margin groups the lines c), c'), c'')",group,'Reconstruct the separate light pen grouping curve beside the three c-conditions.'],
 [r'ret\unsure{ra}ct',r'ret\unsure{\over[typed]{ra}{ra}}ct','The live ra is the strongest reading of the dense repeated impressions, but the older letters and exact layering remain doubtful.'],
 [r'\inserted{on M}',r'\inserted[typed]{on M}','The interlinear on M has regular typewriter letterforms; only its placing curve is penned.'],
 ['above i.e. W is geometric',r'above i.e. \unsure{\over{W}{W}} is geometric','The live W is secure, but the dense added strokes do not securely distinguish pen retracing from repeated typing. Mark the layered reading as doubtful.'],
 [r'\unsure{chedk|check}',r'che\unsure{\over[typed]{c}{d}}k','The fourth cell has a tall d-like type impression and a rounded lower layer. Preserve the c/d layering doubt instead of adopting the witness check.'],
 [r'modeliz\unsure{er}',r'modelize\unsure{r}','The e is visible before the right edge; the final r remains clipped.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4143:[r"is W-aspheric\inserted{, i.e. is ``universally in W''.}",'The complete handwritten universal qualification is visible after c-prime and must remain.'],
 4150:[r'functors, \xout{and} which was','And is crossed by the regular typewriter x row; the witness prints cancelled text.']
 },'unsure':[
 [r'a\unsure{s|x}p','The outer a and p are legible, while the middle cell is entangled with its typewriter cancellation.'],
 ["a'')",'Two prime strokes are visible in the first live handwritten label.'],
 ["a''')",'Three prime strokes are visible in the second live handwritten label.'],
 [r"\unsure{a'')}",'The lower typed third label is partly hidden by the broad pen a and cannot be recovered independently in full.'],
 [r'\unsure{\over[typed]{ra}{ra}}','The ra reading is strongest, but the dense overlap does not secure the old letters and exact repeated layer.'],
 [r'che\unsure{\over[typed]{c}{d}}k','The fourth cell has a tall d-like stem; the lower rounded impression remains uncertain.'],
 [r'e\unsure{r}','The e resolves, but the final r is cut by the scan edge.']
 ],'notes':[
 'The first two new labels resolve as a-double-prime and a-triple-prime. The older third label remains doubtful beneath the handwritten a.',
 'Both margin graphics are reconstructed: the lower a-pair is bracketed and moved upward by the curved arrow, and the three c-clauses have a separate light grouping curve. The reordered reading is specified separately as a complete balanced span.',
 'The live ra of retract is strongest, but the repeated lower impressions remain doubtful and are explicitly marked.',
 'The live W is secure. The dense strokes leave its pen-versus-type layering uncertain, which is marked rather than silently resolved.',
 'Main and somewhat are typed interlinear words with hand placing curves, as encoded. On M is also typed above the line.',
 'The e of modelizer is visible, but the final r reaches the cropped right edge and remains doubtful.',
 'The pencil folio 55 is visible at lower left.'
 ],'extra_records':[{'source_id':'MECH:ps_134-4_055:margin_braces','before':'Both reconstructed margin graphics closed only one enclosing macro','after':'Both margin and diagram macros closed','decision':'mechanical correction','reason':'Add the missing outer margin brace to both graphics; no manuscript reading or topology changes.'},{'source_id':'OBS:ps_134-4_055:condition_order','before':'Physical order a-double-prime, a-triple-prime, a, a-prime','after':'Corrected order a, a-prime, a-double-prime, a-triple-prime','decision':'apply author instruction in corrected forms','line':14,'reason':'The continuous bracket encloses the lower pair and its curved arrow carries that pair before the first two conditions. The complete balanced before/after span is recorded in MASTER_VARIANTS_134_3_4.json.'}],
 'evidence':'Both original halves and seven enlarged panels inspected. The first two rewritten labels are a-double-prime and a-triple-prime; the third old typed label remains obscured under a. The lower a and added a-prime are enclosed together and moved upward by a clear curved arrow. That instruction is preserved graphically in diplomatic order and applied only in the explicit reordered variant. The c-clause grouping curve and all handwritten universal-asphericity additions remain. The If moreover X has a section addition is fully legible; its qualification is essential for d and d-prime. The ra of retract has dense repeated impressions with retained layering doubt. On M, main and somewhat are typed above the line. The Example W has uncertain dense layering. And is machine-cancelled. The final paragraph retains developped, the c/d overprint doubt in chedk/check, the legible e and clipped r of modelizer, and the visible hat over A.'})
# Apply only the author-directed condition transposition, using a whole balanced span.
p=OUT/'checked_pages'/f'{key}.tex';s=p.read_text();start=s.index(move);end=s.index("b)b')b'')",start)
before=s[start:end]
lines=before.splitlines();conditions=[l for l in lines if l.startswith('\\over') or l.startswith('\\inserted')]
assert len(conditions)==4,conditions
after='\n'.join(conditions[2:]+conditions[:2])+'\n'
v={'key':key,'before':before,'after':after,'kind':'author condition transposition','reason':'The bracket encloses the third typed and newly added fourth conditions, and its curved arrow moves that pair before the first two conditions. Preserve the physical order in the diplomatic source.','source_id':'OBS:ps_134-4_055:condition_order'}
f=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(f.read_text());old=[x for x in old if x['source_id']!=v['source_id']];old.append(v);f.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
