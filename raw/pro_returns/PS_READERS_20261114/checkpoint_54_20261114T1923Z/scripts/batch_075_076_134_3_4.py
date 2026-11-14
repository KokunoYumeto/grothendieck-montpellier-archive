import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review

save_review({'key':'ps_134-3_075','edits':[
 ["Now let's come",'Now lets come','No separate apostrophe is visible between the t and s in the opening line.'],
 ['for a little',r'for \over[typed]{a}{a} little','The a has two slightly displaced type impressions.'],
 ['Not speaking',r'N\hand{\ensuremath{\overset{\smile}{\textcolor{black}{o}}}}t speaking','A short pen cup stands above the typed o; it is retained graphically rather than interpreted as an accent correction.'],
 ['The smaller,',r'The s\unsure{\over[typed]{\illegible{2}}{ma}}ller,','The two cells after s are multiply overtyped. The live word reads smaller, but the earlier characters and exact layering remain uncertain.'],
 [r'i: $\hand{\Delta} \hand{\longrightarrow}$ (Cat)',r'i: $\hand{\Delta} \hand{\longrightarrow}$ (\over[typed]{\unsure{U}}{C}at)','The C has an older U-like typed bowl under it; preserve uncertainty on the lower letter.'],
 [r'\unsure{moreover}','moreover','The individual letters of moreover remain distinguishable below the x strikes.'],
 [r'\unsure{Also, the stan-}','Also, the stan-','The upper remnants and word spaces recover Also, the stan- within the large cancelled passage.'],
 [r'\unsure{dard criterion}','dard criterion','The lower continuation reads dard criterion beneath the typewriter x row.'],
 [r'\unsure{amounts to the same}','amounts to the same','The lower baseline letters and spaces recover amounts to the same.'],
 [r'\inserted{is enough}',r'\inserted[typed]{is enough}','Is enough is an interlinear typewritten replacement, with the same monospaced serifs as the main text.'],
 ['as this category',r'as \over[typed]{A}{t}his category','The t is typed over an earlier capital A whose legs remain visible.'],
 ['objects. This',r'objects. T\over[typed]{h}{h}is','The h has a displaced upper type impression.'],
 [r'\hand{\widetilde{\Delta}^{\unsure{\wedge}}}',r'\hand{\widetilde{\Delta}}\hand{\unsure{\ensuremath{{}^{\sim}}}}','The disputed mark is a low wavy pen stroke immediately to the upper right of an already tilded Delta. It is not a clear caret; retain a doubtful second tilde-shaped stroke without assigning a presheaf meaning.']
 ],'diffs':{
 2819:[r'\over{\unsure{p. 67}}{\S. 39}','The handwritten final reference is section 39; the covered typed page number is not independently recoverable.'],
 2824:['such homotopy','No article stands between such and homotopy.'],
 2825:['but this leads','This, with initial t, is legible before leads.'],
 2826:[r'the fact that $\hand{\Delta}$ is a strict test category','There is no tilde over this Delta, in contrast with the clear tildes in the surrounding occurrences. Preserve the apparent omitted tilde.'],
 2827:['(factoring in fact through (Ord), as does','The parenthesis before factoring is typed and belongs to the two-line parenthetical.'],
 2828:['the corollary 3 to','The numeral 3 is typed explicitly.'],
 2829:[r'(\over{\unsure{p.66}}{\S.38})','The final pen reference reads section 38; the lower typed page number is obscured.']
 },'unsure':[
 ['moreover','The x row leaves the full letter sequence legible.'],
 ['Also, the stan-','The raised fragments and spaces distinguish the cancelled words.'],
 ['dard criterion','The cancelled continuation is readable.'],
 [r'\unsure{p. 67}','The typed layer under the heavy section reference cannot be recovered without the witness.'],
 ['amounts to the same','The word sequence is visible under the x strikes.'],
 [r'\unsure{\ensuremath{{}^{\sim}}}','The additional stroke is wavy rather than a definite caret; its intended function remains uncertain.'],
 [r'\unsure{p.66}','The earlier reference is too covered to settle independently.']
 ],'illegible':[[r'\illegible{1}','The single crossed type cell before it cannot be separated securely into an earlier letter.']],
 'notes':[
 'The last letters of standard are clipped at the right border; retain the existing lexical reading without supplying further marginal content.',
 'The drawn outline and diagonal strokes cancel the whole passage, including provided we check that. The three previously doubtful cancelled word groups are now recovered from surviving letter parts.',
 'The live references are section 39 and section 38. Both lower page references remain uncertain.',
 'The crossed cell before it remains illegible. Amounts to the same is recoverable, and its replacement is enough is typed above the line.',
 'The Delta in the fact that Delta is a strict test category has no tilde. This apparent symbol omission is preserved.',
 'The displayed domain has a clear tilde over Delta plus a further wavy stroke to its right. No definite hat is visible; the second stroke remains doubtful.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_075:1','before':r'the fact that $\hand{\Delta}$ is a strict test','after':r'the fact that $\hand{\Delta}$ is a strict test','decision':'retain apparent authorial symbol slip','reason':'The paragraph is about the unordered simplex category, but this single handwritten Delta has no tilde. The source form is retained and the guide identifies its context.','line':38}],
 'evidence':'Both original image halves and twelve detail crops inspected. The large boxed and diagonal cancellation includes the typed conditional insertion. Moreover, Also the stan- / dard criterion and amounts to the same are recoverable under machine strikes; the isolated pre-it cell is not. Is enough is typed interlinearly. The two pen section references are 39 and 38, with obscured earlier page numerals. The ordered-simplex argument has no article before such homotopy. In the unordered example, the singled-out Delta in the strict-test conclusion lacks a tilde. The later displayed domain instead shows one normal tilde and a second doubtful wavy stroke, not a secure presheaf caret. The final two-arrow subset diagram is entirely penned, including its braces and numerals. Source comm-monly and the clipped right-edge standard are retained.'})

save_review({'key':'ps_134-3_076','edits':[
 ['We map this',r'\over{W}{W}e map this','The opening W is retraced with a tall pen stroke extending above the type line.'],
 ['morphism compatible',r'morphism \unsure{\over[typed]{oc}{co}}mpatible','The first two type cells contain overlapping rounded and c-shaped impressions. Compatible is the apparent final reading, but their original order remains uncertain.'],
 ['denote still',r'denote \over[typed]{s}{s}till','The s has two displaced typed impressions.'],
 ['there was an',r'there \over[typed]{\unsure{a}}{w}as an','The w overlays a rounded a-like typed impression; the older letter is not wholly secure.'],
 [r'\unsure{poin}','poin','The right-edge struck letters read poin before the next line restarts points.'],
 [r'\diagram{\begin{tikzcd}',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\diagram{\begin{tikzcd}','All four arrows in the comparison square are hand drawn; retain the typed Ord objects and bar label.'],
 [r'\ar[r,"\hand{}"]',r'\ar[r,color=blue]','The top arrow has no label and is penned.'],
 [r'\ar[d,swap,"\hand{i}"]',r'\ar[d,swap,"\hand{i}",color=blue]','The left arrow and its i label are penned.'],
 [r'\ar[d,"\hand{\tilde{i}}"]',r'\ar[d,"\hand{\tilde{i}}",color=blue]','The right arrow and its tilde-i label are penned.'],
 [r'\ar[r,"\text{bar}"]',r'\ar[r,"\text{bar}",color=blue]','The lower arrow is penned, while its bar label is typewritten.'],
 ['These '+r'\uline{are}',r'T\over{h}{h}ese \uline{are}','A small pen h is written below and against the typed h; preserve it as a handwritten retracing.'],
 [r'\unsure{despite the fact that we kept using}','despite the fact that we kept using','The complete cancelled phrase is recoverable from the baseline forms beneath the x row.'],
 [r'\text{\unsure{\deleted{a}} discrete category',r'\text{\over{\unsure{a}}{d}iscrete category','The pen mark is a d written in the first cell of discrete. No separate preceding article or interword gap is visible; an older a remains plausible but uncertain.'],
 [r'\xout{xx}\inserted{and}',r'\xout{xx} \inserted[typed]{and}','And is typed interlinearly above the two x cells; its placing curve is handwritten. Supply the word boundary explicitly.']
 ],'diffs':{
 2833:[r"\inserted{[namely satisfies the conditions of the ``key theorem''].}", 'The bracketed addition after test functor continues by hand onto the next line and is not cancelled.'],
 2842:['as soon as trying to check','The live line says as trying; no we is present.'],
 2843:[r'a \inserted{strict} test category','Strict is written by hand with its placing curve before test.'],
 2845:[r'n \hand{>} 0','The inequality uses the typed numeral zero, not one.']
 },'unsure':[
 ['poin','The four underlying letters are readable below their x strikes.'],
 ['despite the fact that we kept using','Surviving ascenders, bowls and spaces recover the complete phrase.'],
 [r'\over{\unsure{a}}{d}','A handwritten d replaces or retraces the first character of discrete. The possible old a remains doubtful; there is no separate deleted article.'],
 [r'\unsure{any more at most}','The first two words are clear, but the heavily crossed final cells do not securely recover every letter of at most. Retain the proposed reading as uncertain.']
 ],'notes':[
 'The right-edge cancelled letters are poin; the next line begins points again.',
 'Despite the fact that we kept using is recoverable beneath the x row and is retained as cancelled typing.',
 'Any more is readable, but the remaining cancelled cells are too overlapped to settle the whole proposed at most.',
 'The mark occupies the first cell of discrete and forms a pen d. The lower a-like letter remains uncertain; remove the spurious separate article and space.',
 'The small marginal x is visible to the left of the product display.',
 'Delta, tildes, K subscripts and prime, the four comparison arrows and their i labels are pen. The Ord objects and bar are typed. The interlinear and is also typed.'
 ],'evidence':'Both original halves and ten enlarged details inspected. The opening W is penned over type; the comparison square has four pen arrows with typed Ord objects and bar. The added explanation of test functor is a live bracketed hand note. The source explicitly writes n greater than zero, as trying, does\'nt and would\'nt. The disputed display starts with a pen d over a possibly typed a in discrete, not a separately deleted article. The long cancelled degeneracy sentence is recoverable; the shorter cancellation after much use remains partly doubtful. The insertion and is typed with a pen placement curve. The pen h below These and the small marginal x are retained.'})
