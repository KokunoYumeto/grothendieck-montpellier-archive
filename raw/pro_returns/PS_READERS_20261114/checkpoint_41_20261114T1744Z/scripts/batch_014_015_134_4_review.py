import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_014';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m[1]+'}}',line)
 for sym in [r'\coprod',r'\rightrightarrows',r'\to',r'\amalg',r'\simeq']:
  new=new.replace(sym,r'\hand{'+sym+'}')
 new=new.replace(r'\underline{I}\vee\underline{J}',r'\underline{I}\hand{\vee}\underline{J}').replace(r'}\vee\overset',r'}\hand{\vee}\overset')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The coproduct/amalgamation signs, arrows and comparison sign are penned; nested math delimiters inside handwritten symbols are repaired mechanically.'])
edits += [
 [r'T\over{\illegible{1}}{h}e dual',r'T\over{H}{h}e dual','The capital H remains visible behind the penned lowercase h.'],
 [r'\xout{xxxx}',r'\xout{\illegible{}}','The four cancellation x marks obscure their older letters; do not transcribe the cancellation glyphs as the old text.'],
 [r'\hand{only}',r'\over{only}{only}','Only is written in pen over the typed word, whose round o and remaining letter bodies remain visible.'],
 [r'vals\inserted{$\underline{K}$}',r'vals \inserted[typed]{$\underline{K}$}','K is typed interlinearly, with an added underline and placing hook; it is a separate formula.'],
 [r'\inserted{homotopy}',r'\inserted[typed]{homotopy}','Homotopy is typed above intervals. Its pen placing curve does not delete intervals.'],
 [r'\xout{fxx}',r'\xout{for}','The old f, o and r are readable beneath the machine strikes.'],
 [r'gamated\xout{x}',r'gamat\over{e}{e}\over{d}{d}\xout{\illegible{}}','The final e and d are retraced in pen; the following machine-cancelled cell has no recoverable older letter.'],
 [r'\inserted{the}',r'\inserted[typed]{the}','The is typed above sections, with a pen placing curve.'],
 [r'\inserted{for K}',r' \inserted[typed]{for $\underline{K}$}','For K is typed above the line; K has a separate underline and the phrase has its own word boundary.'],
 [r'\unsure{J}','J','The final superscript has the upper bar, right stem and leftward foot of J despite heavy retracing.'],
 [r'\xout{bxx}',r'\xout{by\illegible{}}','By is legible, but the final cancelled cell is not recoverable.'],
 [r'T\over{\illegible{1}}{h}e operation',r'T\over[typed]{H}{h}e operation','This is a displaced capital-H/lowercase-h type overlap, rather than a pen h.'],
 [r'e_0 \wedge e_1 = \emptyset_M',r'e_0 \hand{\cap} e_1 = \hand{\varnothing}_M','The intersection sign is rounded and penned, as is the slashed-circle initial-object symbol.'],
 [r'\over{\illegible{1}}{J}',r'\over[typed]{\unsure{U}}{J}','The correction is typed J, with a rounded older U-like impression whose identification remains doubtful.'],
 [r'\over{\illegible{1}}{t}',r'\over[typed]{t}{t}','The first t of the has offset repeated type impressions.'],
 [r'M\over{\illegible{1}}{o}re',r'M$\overset{\hand{\smile}}{\mathrm o}$re','The mark is a clear cup-shaped pen stroke above typed o, not an overwritten old letter.'],
 [r'b\over{\illegible{1}}{y}',r'b\over{y}{y}','The old typed y is visible beneath the large pen y.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3376:[r'\underline I\vee\underline J','The source uses a handwritten vee between the interval letters, not the witness\'s broken lor text.'],
 3377:[r'\delta_1^J:e\to J','The superscript of the right-hand endpoint is clearly J.'],
 3379:['up to canonical isomorphism','No article a occurs before canonical.']
 },'unsure':[
 [r'\unsure{a}','The older rounded cell beneath penned b is largely covered and cannot be independently settled.'],
 [r'\unsure{b}','The older cell beneath penned c is similarly obscured; its ascender is not secure.'],
 ['J','The live J is recoverable from its upper bar, right stem and bottom hook; the dense retracing does not change its letter.']
 ],'illegible':[
 ['H','The upper-right bar and vertical of the old capital H remain visible beneath pen h.'],
 ['H','The old upper H and lower h have regular typewriter serifs.'],
 [r'\unsure{U}','The old rounded impression beneath typed J is U-like but not secure.'],
 [r'\illegible{1}','The old letter beneath the heavy pen d of reduced remains covered.'],
 ['t','The old and new t impressions are offset but recognizable.'],
 ['No old letter: cup above o','The mark is a separate pen cup above the typed o.'],
 ['y','The old type y branches remain visible under the larger pen y.']
 ],'notes':[
 'The first The has pen h over typed H; the second has typed H/h overlap. Their provenance is distinguished.',
 'Only is written over the typed word, not wholly new blank-space writing. With is a separate pen insertion.',
 'Homotopy is typed above intervals, with a placing curve that leaves intervals live.',
 'The amended superscript is readable as J. The initial K is struck through, and the endpoint superscripts on the right are I and J.',
 'The live labels are b and c; the older underlying a/b readings remain doubtful.',
 'The lower-left 14 is handwritten. All three finite restrictions and the cancelled arbitrary passages are retained; the inserted K, the and for K are typed.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_014:opposite','before':r'(\underline I\vee\underline J)^\vee\simeq\check I\vee\check J','after':'Source order I then J retained; reversing endpoints normally reverses the order of the two intervals.','line':39,'decision':'retain mathematical slip for guide','reason':'The chosen amalgamation identifies the last endpoint of I with the first of J. Reversing its endpoints gives the order opposite J then opposite I. The scan nevertheless prints I before J.'},
 {'source_id':'OBS:ps_134-4_014:or','before':r'$\hand{\ensuremath{\delta}}_0$ of $\hand{\ensuremath{\delta}}_1$','after':r'$\hand{\ensuremath{\delta}}_0$ or $\hand{\ensuremath{\delta}}_1$','line':26,'decision':'master slip variant','reason':'The isolated of in the either/or alternatives is a wrong final keystroke; or is correctly attested elsewhere on this same page.'}
 ],'evidence':'Both original halves and fourteen enlarged panels inspected. The first The is pen h over H; the second is a type overlap. Only is pen rewriting over the typed word. The interlinear K, homotopy, the and for K are typed and their placing curves do not delete the underlying text. The final e/d of amalgamated are pen-retraced. Cancelled for and by are recovered, while other struck cells remain unreadable. The superscript J is clear after enlargement; older labels beneath b/c remain doubtful. The bottom J has typed correction with a doubtful older U-like layer; reduced retains an unreadable old cell, the has repeated typed t, More has a pen cup, and by has pen y over type y. The displayed reversal formula visibly retains I then J and is flagged mathematically without correction.'})
variants.append({'key':key,'before':r'$\hand{\ensuremath{\delta}}_0$ of $\hand{\ensuremath{\delta}}_1$','after':r'$\hand{\ensuremath{\delta}}_0$ or $\hand{\ensuremath{\delta}}_1$','kind':'slip corrected','reason':'The isolated of in either/or alternatives is settled by context and same-page or.','source_id':'OBS:ps_134-4_014:or'})

key='ps_134-4_015';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\to',r'\hand{\to}').replace(r'\in ',r'\hand{\in} ').replace(r'\underset{\underline{I}}{\sim}',r'\underset{\underline{I}}{\hand{\sim}}').replace(r'C^{\wedge}',r'C^{\hand{\wedge}}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows, membership sign, comparison tilde and presheaf caret are handwritten.'])
edits += [
 [r'\over{\unsure{n}}{c}opies',r'\over{\underline{I}}{c}opies','The older cell is a capital I with underline, not n; the live c is written over it.'],
 [r'\over{\unsure{m}}{n}',r'\over[typed]{i}{n}','A dotted typed i is visible beneath the typed n.'],
 [r'\xout{fxxxd}',r'\deleted{\xout{f and}}','The old fragment reads f and beneath both the typed x row and a later continuous pen strike.'],
 ['Remark} THe',r'Remark} T\over[typed]{H}{h}e','The H/h type overlap is visible.'],
 [r'\xout{xx}',r'\xout{\unsure{we}}','The two old cells are plausibly we but remain partly hidden beneath the x strikes.'],
 [r'$A^{\wedge}$\hand{$\hat{}$}',r'$A^{\hand{\overset{\wedge}{\wedge}}}$','Two distinct pen carets are stacked above A. Preserve both and repair the empty-hat macro and its placement.'],
 [r'\inserted{too}',r'\inserted[typed]{too}','Too is typed above the line. Its pen curve places it before the still-live to.'],
 [r'\xout{\unsure{s}}seems',r'\deleted{\unsure{s}}seems','The extra old cell is covered by a heavy pen stroke; its tentative s remains doubtful.'],
 ['definitely reasonabl\n',r'definitely reasonabl\unsure{e}'+'\n','The final letter lies beyond the supplied right edge; mark the contextual completion e as conjectural rather than silently complete or omit it.'],
 ['lemma on page )',r'lemma on page \hspace{2em})','Preserve the conspicuous blank left for the unfinished page reference.'],
 [r'\hspace{2em}). The'+'\n',r'\hspace{2em}). T$\underset{\hand{\unsure{\wedge}}}{\mathrm h}$e'+'\n','A small angular pen mark sits below h in this The; its function is uncertain, so retain it as a graphic doubt.'],
 [r'amal\over{\unsure{ja}}{g}amation',r'amal\over{\unsure{j|g}}{g}\over{a}{a}mation','The first old cell is partly hidden and may be j or g. The following a is a separate live pen retracing over typed a; it must not be absorbed into a two-letter deletion.'],
 [r'M\over{\unsure{e}}{o}re',r'M$\overset{\hand{\smile}}{\mathrm o}$re','The mark is a cup above the typed o, not an e-to-o replacement.'],
 [r'an\xout{category}',r'an \deleted{\xout{category}}','The old category has both a machine-x row and a continuous pen strike; the preceding an is a separate word.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3380:['be the set of all homotopy intervals','The defining verb is be.'],
 3381:["the condition c')",'The prime is visibly present. In context this refers to the earlier amalgamation hypothesis c), not the distinct saturation axiom c-prime; preserve and flag the source reference.'],
 3385:[r'cf. lemma on page \hspace{2em})','A blank of several type spaces is left before the closing parenthesis. No page number is supplied.']
 },'unsure':[
 ['Underlined I','The old letter has full capital-I top and bottom bars with a separate underline.'],
 ['i','The old dot and vertical stem of typed i are visible under n.'],
 [r'\unsure{s}','The heavy pen cancellation hides most of the old letter.'],
 [r'\unsure{j|g}','The older first cell is too obscured to distinguish j from g; the following a is separate and live.'],
 ['Cup above typed o','The pen stroke is a separate upper cup, not an older e.']
 ],'notes':[
 'The first large tilde and the later f~g tilde are both penned; the second is thinner but has the same smooth hand-drawn curve.',
 'Too is typed above the line, and the placing curve leaves the typed to live.',
 'Mayer-Vietoris type is correctly classified as a typed insertion. The continuous pen placing bracket does not cancel statement about.',
 'A has two stacked angular pen carets. Both are preserved in one superscript, with no empty-hat macro.',
 'The last e of reasonable is outside the supplied edge and is added only as an explicitly doubtful contextual completion.',
 'The first The is typed H/h. The extra cell before seems is pen-cancelled and uncertain; the old t after referring is visibly machine-cancelled. Membership in Comp is penned.',
 'The cancelled fragment reads f and, beneath both machine strikes and a later pen stroke.',
 'The lower-left 15 is handwritten. The unfinished reference remains a blank; More has an upper pen cup, and the last The has a small uncertain mark below h.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_015:cprime','before':"the condition c')",'after':'Source prime retained; the surrounding argument concerns amalgamation condition c).','line':25,'decision':'retain source cross-reference slip for guide','reason':'The sentence refers to stability under amalgamation of aspheric objects, which is c) on p.102. The distinct saturation condition c-prime concerns composites gf and fg.'}],
 'evidence':'Both original halves and thirteen enlarged panels inspected. Copies is written over an underlined I, and n=2 has typed n over dotted i. The f and fragment is doubly cancelled. Both tildes and the membership sign are penned. The presheaf A has two stacked carets; too is a typed insertion whose hook leaves to live. The final e of reasonable is clipped and retained only as a conjecture. The blank page reference is explicit. The extra cell before seems remains pen-obscured; the marked t after referring is machine-cancelled. Amalgamation contains a doubtful older j/g under the live g and a separate pen-retraced a. More has a cup above o, and the later The retains an uncertain small angular mark below h. The literal primed c reference is preserved with its contextual inconsistency noted.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
