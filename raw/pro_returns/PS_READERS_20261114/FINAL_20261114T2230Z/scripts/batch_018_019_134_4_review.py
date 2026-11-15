import sys,re,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT

key='ps_134-4_018';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m[1]+'}}',line)
 new=new.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}').replace(r'\underset{W}{\sim}',r'\underset{W}{\hand{\sim}}').replace(r'\emptyset_M',r'\hand{\varnothing}_M')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows, relation tildes and initial-object circle are penned. Nested math delimiters in handwritten symbols are repaired mechanically.'])
edits += [
 [r'\overline{W}',r'\overset{\hand{\rule{0.65em}{0.4pt}}}{W}','The bar is penned above typed W.'],
 [r'$M\hand{\to} M_W$ commutes',r'$M\hand{\to} M_{\over[typed]{\illegible{1}}{W}}$ commutes','The W has a displaced older typed impression whose letter is not securely readable.'],
 ['taking products with',r'taking products \over{w}{w}\over{\unsure{i|j}}{i}\over{t}{t}h','The w, i and t are retraced in pen; the older middle cell has a descender-like trace and remains doubtful.'],
 [r'\inserted{any}',r'\inserted[typed]{any}','Any is typed above the pen-cancelled a.'],
 [r'\deleted{The same',r'\deleted{T\over{h}{h}e same','The h in the cancelled block is retraced in pen, with its tall upper stroke still visible.'],
 [r'\unsure{infinite|intinite}','infinite','The upper hook and crossbar identify f beneath the block strike.'],
 [r'interval\inserted{$\underline{I}_o$}',r'interval \inserted[typed]{$\underline{I}_o$}','The interval name is typed interlinearly and is a separate mathematical token.'],
 [r'\xout{xxxxxx}',r'\xout{result}','The six surviving letter shapes read result beneath the machine strikes.'],
 [r'\inserted{homotopy equivalence or}',r'\inserted{\uline{homotopy equivalence} or}','The two handwritten words homotopy equivalence have their own underline; or does not.'],
 [r'\xout{xxxxxxxxxxxxxxxxsimpl}',r'\xout{When X\illegible{1}simpl}\hand{\ensuremath{\unsure{\lozenge}}}','When X and final simpl are readable; the intervening cancelled cells remain uncertain. A small angular loop below the row is retained as an explicitly doubtful graphic.'],
 [r'objects of $M_W$',r'objects of $M_{\over{W}{W}}$','A low pen W retraces the typed subscript.'],
 [r'\inserted{W-}',r'\inserted[typed]{W-}','W and its hyphen are typed above the line, with a pen placing hook.'],
 [r'\xout{ixxxrdxx}',r'\xout{in order}','In order is readable under the machine x row.'],
 [r'\inserted{Remark.}',r'\inserted{\uline{Remark.}}','The handwritten Remark has a separate underline.'],
 [r'interval\over{.}{!}',r'interval\over{\unsure{.}}{!}','The live pen exclamation is clear; its heavily covered older punctuation cannot be independently established.'],
 ['THe only',r'T\over[typed]{H}{h}e only','The H/h overlap consists of offset typewriter impressions.'],
 [r'notion\deleted{s}',r'notion\unsure{s}','The final s is densely retraced but has no securely separable cancellation stroke; retain the letter with doubt rather than delete it.'],
 [r'a\xout{xxobjxxxx}',r'a\xout{n object}','The cancelled n object is recoverable; the preceding a remains live.'],
 [r'condition\xout{xxa)xxand(x)xofxpagexx59}',r'condition \xout{a) and (\illegible{1}) of page 59}','The cancelled condition reference has readable a), and, of page 59, with an obscured parenthesized letter.'],
 [r'\over{If}{In} \inserted{case}',r'I\over[typed]{f}{n} \inserted[typed]{case}','The f/n correction and the raised case are typed; the curve under case places the insertion.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3437:['a homotopy equivalence or homotopism','The added handwritten phrase has no second a. Only homotopy equivalence is underlined within it.'],
 3438:['This implies f and g are weak equivalences.','The interlinear sentence is typed and contains no that.'],
 3446:['It occurs to me','The verb begins It; the witness If is not the scan reading.'],
 3450:[r'(\underline I,\delta_o,\delta_1)','The tuple begins with an underlined I and has no preceding I equals sign.'],
 3455:['as when using only actual homotopy intervals','The next line clearly begins as when; as must not be omitted.']
 },'unsure':[['infinite','The f has an upper hook and crossbar despite the superposed block cancellation.']],
 'notes':[
 'No hyphen is visible at the clipped end weak equivalen. The following ce is joined mechanically by the existing percent continuation, without inventing a hyphen.',
 'The cancelled word resolves to infinite. The whole block is crossed out, including its uncompleted displays; no missing equals sign is supplied.',
 'The first M_W has an unreadable older typed impression under W. The later objects of M_W has a pen W below and over the typed W.',
 'Cancelled result, in order and n object are recovered. When X and simpl are recoverable around an obscured middle span; the condition reference has one unreadable parenthesized letter.',
 'The appended equals e period is handwritten. The live exclamation is penned, but the older punctuation beneath it remains doubtful.',
 'Both tildes in the homotopism display are smoothly drawn pen curves.',
 'The small angular loop below the cancelled row is retained as a doubtful graphic; it is not used to invent a letter or a mathematical relation.',
 'The lower-left 18 is handwritten. Any, W- and case are typed interlinear additions. Actual and the underlined Remark are pen additions.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_018:contactible','before':r'\uline{contactible}','after':r'\uline{contractible}','line':30,'decision':'master slip variant','reason':'The omitted r is a one-off keystroke omission, settled by the correctly spelled contractible in the same sentence.'}
 ],'evidence':'Both original halves, fifteen detail panels and an additional cancelled-text enlargement inspected. The first overwritten W has an unreadable typed lower layer; the later W is pen-retraced. With has three pen retracings with a doubtful older i/j cell. Any, the inserted interval name, W- and case are typed additions. Infinite and the cancelled result, in order and n object are recovered; other cancelled cells remain explicit lacunae. The whole infinite-product block is cancelled and its blank formula spaces remain blank. The handwritten homotopy equivalence and Remark are underlined. The old punctuation under the exclamation and the cancellation status of the final s in notions remain doubtful. Required readings no second a, no that, It occurs, the literal underlined-I tuple and as when are all visible on the scans.'})

key='ps_134-4_019';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\rightrightarrows',r'\hand{\rightrightarrows}').replace(r'\to',r'\hand{\to}').replace(r'\underset{\underline{I}}{\sim}',r'\underset{\underline{I}}{\hand{\sim}}').replace(r'\emptyset_M',r'\hand{\varnothing}_M')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows, homotopy tilde and initial-object circle are handwritten.'])
edits += [
 ['The question',r'T\over[typed]{\unsure{H}}{h}e question','The h has displaced type fragments above and below it; the older capital-H reading is plausible but incomplete.'],
 [r'\margin{$\lfloor$}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\draw[gray] (0,1.8)--(.1,.1)--(2.4,0);\end{tikzpicture}}}','The marginal pencil mark has a long vertical and a rightward lower horizontal; retain it as a graphic rather than a mathematical floor sign.'],
 [r'\margin{$\lceil$}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\draw[gray] (0,-1)--(0,0)--(2.5,.3);\end{tikzpicture}}}','The second marginal pencil bracket has a downward left stroke and slanted upper horizontal.'],
 ['contractib\nle element','contractib%\nle element','The word is split at the supplied right edge. Join the two visible parts mechanically without inserting a space or an unobserved hyphen.'],
 [r'section $e_o$',r'section $c_o$','The section name is typed c with an open right side, not e.'],
 [r'c = p_X e_o',r'c = p_X c_o','The displayed factor after p_X is c_o, matching the section label; preserve the printed factor order.'],
 ['If $X$ is contractible',r'\over{I}{I}f $X$ is contractible','The initial capital I is retraced in pen over its typed impression.'],
 [r'\inserted{one would expect it} \deleted{to be}',r'\inserted[typed]{one would expect it} to be','The insertion is typed. Its single continuous placing curve is not a cancellation of to be; an independent visual review agrees.'],
 [r'\xout{xxxxx}, \deleted{an} \inserted{that px is}',r'\xout{\illegible{1}}, \inserted[typed]{that px is} a\over{n}{n}','The typed insertion is placed before live an. The n is independently pen-retraced; the curve does not delete either letter. The older machine-cancelled cells are unreadable.'],
 [r'$A\hat{}$',r'$A^{\hand{\wedge}}$','The presheaf caret is penned above A; repair the empty-hat macro while preserving its position.'],
 ['The natu-',r'T\over[typed]{H}{h}e natu-','The H/h pair is a type overlap.'],
 [r'$S\hand{\to} e$',r'$S\hand{\to} \over{e}{e}$','The final e is retraced in pen over a visible typed e.'],
 ['gically asphericity',r'\over[typed]{f}{g}ically asphericity','The g of gically is typed over an older f whose upper stem and crossbar remain visible.'],
 ['(The condition',r'(\over[typed]{T}{T}he condition','The capital T has displaced repeated typed bars.'],
 [r'$M$ = (Ss sets)',r'$\over[typed]{M}{M}$ = (Ss sets)','M has two displaced type impressions.'],
 ['usual notions',r'usual notio\over{n}{n}\over{s}{s}','The final n and s are retraced in pen over their typed counterparts.'],
 [r't\over{\unsure{q}}{a}king',r't\over[typed]{\unsure{q}}{a}king','The live a has regular typewriter form; the older descender-like cell remains doubtful.'],
 ['The same examples',r'T\over{H}{h}e same examples','The h is penned over a typed capital H; its looped ascender accounts for the extra upper mark.'],
 [r'homot\over{a}{o}py',r'homot\over{\unsure{a}}{o}py','The live pen o is clear, but the old rounded cell is mostly covered and does not securely establish a.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3460:["it has'nt got a homotopy interval",'The source has got with g, not the witness hot.'],
 3461:['However for the time being','No comma follows However.'],
 3468:['one would expect it to be even universally so','The scan insertion is typed and to be remains live. The witness added is arises from the initial false deletion.','correct insertion and cancellation'],
 3471:[r'elementary modelizers $A^{\wedge}$','The word modelizers is present immediately before the presheaf symbol.']
 },'unsure':[
 [r"\unsure{is'nt|isn't}",'The apostrophe overlaps the n stem. Its exact order relative to that letter remains insecure, so the two source possibilities stay explicit.'],
 [r'\unsure{q}','The older typed cell has a descender-like trace beneath the live a but is not sufficiently distinct to settle q.']
 ],'illegible':[[r'\illegible{1}','The old cell beneath the pen a of Spaces remains largely covered.']],
 'notes':[
 'The apostrophe/n cluster in is not retains the original doubt; the neighbouring is\'nt forms do not settle its exact visible order.',
 '(I recall) is typed above the line, and its placing curve leaves means live.',
 'X_S equals is typed above projection with a pen placing hook, as initially encoded.',
 'Both marginal marks are reconstructed as their actual pencil bracket shapes, not floor and ceiling operators.',
 'Spaces keeps an unreadable older cell under pen a; taking has typed a over a doubtful q-like cell; homotopy has pen o over an uncertain older rounded cell.',
 'The lower-left 19 is handwritten. Both newly checked interlinear clauses are typed and leave to be and an live; the n of an is pen-retraced.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_019:composition','before':r'c=p_Xc_o:X\to e\to X','after':'Source order p_X c_o retained, with c_o the section e to X.','line':17,'decision':'retain source formula slip for guide','reason':'The scan clearly names the section c_o and prints p_X first. Under the surrounding right-to-left composition convention the indicated endomorphism of X would be c_o p_X, as in the analogous earlier reversal on p.50.'},
 {'source_id':'OBS:ps_134-4_019:singular','before':'aspheric spaces (in the sense of singular cohomology)','after':'Literal cohomological formulation retained and distinguished in the guide from weak contractibility.','line':46,'decision':'retain source qualification for guide','reason':'Ordinary acyclicity alone does not ensure trivial fundamental group. The example is part of the author\'s discussion of weak equivalences and must not be expanded into an unqualified converse.'}
 ],'evidence':'Both original halves, seventeen detail panels and an enlarged constant-map formula inspected. The section and displayed factor are c_o, not e_o; the printed composition order is preserved and flagged. The two typed interlinear clauses leave to be and an live, as independently confirmed; an has a pen-retraced n. The double pencil brackets are reconstructed, and the clipped contractible line break is mechanically joined. There are typed H/h overlaps, a repeated typed T and M, a typed f/g correction, and pen retracings of initial I, final e and notions n/s. The is\'nt/isn\'t cluster, the old letters in Spaces and taking, and the old homotopy vowel retain explicit doubts. Every required difference, the typed (I recall) and X_S insertion, and the literal modelizers wording were checked on the scans.'})

p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());v={'key':'ps_134-4_018','before':r'\uline{contactible}','after':r'\uline{contractible}','kind':'slip corrected','reason':'One-off omitted r, with contractible correctly typed in the same sentence.','source_id':'OBS:ps_134-4_018:contactible'};p.write_text(json.dumps([x for x in old if x['source_id']!=v['source_id']]+[v],ensure_ascii=False,indent=2)+'\n')
