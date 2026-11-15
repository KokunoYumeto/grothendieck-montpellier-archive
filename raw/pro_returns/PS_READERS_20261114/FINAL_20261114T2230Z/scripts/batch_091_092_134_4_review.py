import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_091'
oldnote=r'\inserted{and this implies that \deleted{\unsure{implies}} $i_A^*:\mathrm{Cat}_{/A}\to A^\wedge$, is model-preserving}\margin{to check}'
newnote=r'\inserted{\fbox{\parbox{.72\linewidth}{and this implies that \deleted{\unsure{implies|equally}} $i_A^{\unsure{\prime}*}:\mathrm{Cat}_{/A}\to A^\wedge$, \unsure{\over{a}{i}}s model-preserving}}}\margin{to check $\rightarrow$}'
edits=[
 [oldnote,newnote,'Preserve the boxed note, its to-check arrow, the separate doubtful raised prime, and the uncertain crossed word. The initial is has an unresolved a/i pen layer. The box and its text are all handwritten.'],
 [r'$i_{/a} : A_{/a}\to(\mathrm{Cat})$',r'$i_{/a} : A_{/a}\hand{\to}(\mathrm{Cat})$','The slice-functor arrow is handwritten.'],
 [r'$A^\wedge$ \xout{xxx}',r'$A^\wedge$ \xout{\unsure{are}}','The lower run beneath the x row is compatible with are, but its last cell is obscured; retain it tentatively.'],
 [r'\xout{E)} F)',r'\xout{\unsure{E|e})} \over{F}{F})','The older cancelled heading letter is partly obscured. The new F has a pen retracing over its typed form.'],
 [r'\uline{\xout{Strictx}}x',r'\uline{\xout{Strict}}','Strict is readable beneath the machine row. The further x impressions occupy its following space and are cancellation marks, not live textual x letters.'],
 [r'\uline{functors}\xout{x}\inserted',r'\uline{functors}\xout{\illegible{1}} \inserted','The extra cancelled cell after functors has no secure lower reading. Preserve a boundary before the inserted functor domain.'],
 [r'i:\ A\longrightarrow(\mathrm{Cat})',r'i:\ A\hand{\longrightarrow}(\mathrm{Cat})','The displayed functor arrow is penned.'],
 ['i is a test functor iff',r'i is a \over[typed]{\unsure{l|t}}{t}est functor iff','The t has a lower tall type impression, tentatively l or repeated t.'],
 [r'a local\inserted{$\underline{W}$-} test',r'a local \inserted{$\underline{W}$-}test','The inserted W-hyphen qualifies test; put the word boundary before the inserted prefix and join its hyphen to test.'],
 ['prop.2 (with',r'prop.\unsure{\over[typed]{3|2}{2}} (with','The live 2 is clear, but its older overlapping digit remains 3/2.'],
 [r'i be a weak $\underline{W}$-test functor',r'i be a weak $\underline{W}$-\over{\unsure{l|t}}{t}est functor','The t is penned over a tall lower typed impression, retained tentatively.'],
 [r'$A^\wedge$\hand{/}totally',r'$A^\wedge$\diagram{\begin{tikzpicture}[baseline=-.4ex,x=1em,y=1ex]\draw[color=blue,line width=.45pt] (0,-.5)--(.45,2.8);\end{tikzpicture}} totally','The long oblique separator is a pen graphic rather than a textual division slash.'],
 [r'$i:\ A\to(\mathrm{Cat})$',r'$i:\ A\hand{\to}(\mathrm{Cat})$','The theorem functor arrow is penned.'],
 [r'$(\mathrm{Cat})\to A^\wedge$',r'$(\mathrm{Cat})\hand{\to} A^\wedge$','The arrow after the cancelled phrase is hand-drawn.'],
 [r'\overline{i^*}',r'\overset{\hand{\rule{1em}{.6pt}}}{i^{\over{*}{*}}}','The bar is a broad pen stroke and the star is pen-retraced, while the i remains typed.'],
 [r'(\mathrm{Hot}_{\underline{W}})\longrightarrow(\mathrm{Hot}_A)',r'(\mathrm{Hot}_{\underline{W}})\hand{\longrightarrow}(\mathrm{Hot}_A)','The displayed localization arrow is penned.'],
 [r'\xout{if} f',r'\deleted{\xout{if}} f','The older if has an additional irregular pen crossing over its machine cancellation.'],
 [r'\inserted[typed]{implies}\hand{,}',r'\inserted[typed]{implies}','The apparent following comma is the continuous downturned end of the placing curve; no independent comma is visible.'],
 [r'$C\to e$',r'$C\hand{\to} e$','The arrow in the explanatory final-object map is penned.']
]
edits.append([newnote,r'\par\noindent '+newnote+r'\par\noindent ',
 'Local typesetting repair after the rendered cote proof: set the boxed author insertion on its own line at the same attachment point; its former inline placement overflowed by 48.552 pt. No wording or layer changes.'])
oldsep=r'$A^\wedge$\diagram{\begin{tikzpicture}[baseline=-.4ex,x=1em,y=1ex]\draw[color=blue,line width=.45pt] (0,-.5)--(.45,2.8);\end{tikzpicture}} totally'
newsep=r'$A^\wedge$\ensuremath{\diagram{\begin{tikzpicture}[baseline=-.4ex,x=1em,y=1ex]\draw[color=blue,line width=.45pt] (0,-.5)--(.45,2.8);\end{tikzpicture}}} totally'
edits.append([oldsep,newsep,'Keep the small pen separator in inline math so the diagram wrapper does not create a detached display and interrupt the sentence. Its strokes and wording are unchanged.'])
save_review({'key':key,'edits':edits,'diffs':{
 4794:['from (Cat) to the presheaf category','To is visibly typed, not an arrow.'],
 4796:['W-aspheric over e_Ahat','The first W has no subscript A on the page.'],
 4798:[newnote,'The complete boxed addition and to-check arrow are present. The raised prime-like mark is real but uncertain in interpretation; the old crossed word remains doubtful.'],
 4799:['to be a even a W-test functor','The source includes a even a; preserve it literally.'],
 4800:[r'\inserted{and $i_A^*$}','The addition is written in the left margin with a matching placement mark after i-star.'],
 4797:['a times i-star of Delta with no subscript','The product formula visibly has a bare triangle. The preceding and later interval symbols do have typed subscript 1.']
 },'unsure':[[r'\unsure{implies|equally}','The lower crossed handwriting is not securely implies. Equally is visually plausible; independent inspection agrees to retain uncertainty.']],
 'notes':[
 'The boxed note is reconstructed as a box. A distinct raised prime-like stroke between i and star is preserved under a doubt, independently confirmed. The crossed word has competing implies/equally readings, and the initial is has an a/i layer doubt.',
 'The old heading letter remains E/e beneath cancellation. F is pen-retraced. Strict is readable, and the extra x impressions after it are cancellation strokes in blank space, not live letters.',
 'Both test t patches retain an older l/t doubt; the first is typed overprinting, the second pen retracing. The prop.2 lower digit remains uncertain.',
 'The display bar and star are pen strokes over the typed i-star; the i stays typed. The comma after the parenthesis in ii is independently visible pen punctuation. After implies the apparent comma is only a placing hook.',
 'The pencil folio 91 is visible at lower left.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_091:WA_objects','before':'W_A-objects','after':'W_A-objects','decision':'retain source wording; discuss in guide','reason':'Condition iv visibly omits aspheric before objects, although its explanatory parenthesis describes the asphericity test. Do not silently complete the source phrase.'}],
 'evidence':'Both original halves and ten detail panels inspected. The upper-right note is enclosed by a pen box and has a separate to-check arrow. A distinct raised prime-like mark survives between i and star; it is retained doubtfully. The crossed word is not securely implies, with equally another candidate. The note initial is has an uncertain older a-like layer. The first corollary W lacks subscript A, its later product uses Delta without subscript 1, and the source says a even a. The margin and i_A-star addition is legible. Strict is cancelled, with further x impressions extending into the blank, and the extra cell after functors is unreadable. The two test t patches and prop.2 retain older-layer doubts. The pen separator after A-hat is graphic. All observed arrows, the localization bar and the star retracing have pen provenance. The comma after implies is a placing hook and is removed as textual punctuation; the comma in ii is real. The literal W_A-objects omission remains in the source.'})

key='ps_134-4_092'
oldgraph=r'\[ (i)\Rightarrow(ii)\Rightarrow(iii)\Rightarrow(iv)\Rightarrow \text{\deleted{\unsure{(v)}}}\,(vi)\,\text{\deleted{\unsure{(vi)}}} < \hand{\Longleftarrow}\ \text{\inserted{(v)}\deleted{\illegible{1}}} \quad , \]'
newgraph=r'''\[ (i)\hand{\Rightarrow}(ii)\hand{\Rightarrow}(iii)\hand{\Rightarrow}(iv)\hand{\Rightarrow}
\underset{\text{\deleted{\unsure{(vi)}}}}{\overset{\substack{\text{\deleted{\xout{\unsure{(v)}}}}\\\text{\deleted{\hand{\unsure{(vi)}}}}}}{(vi)}}
\hand{\Longleftarrow}\ \underset{\text{\deleted{\illegible{1}}}}{\text{\inserted[typed]{(v)}}}\quad , \]'''
edits=[
 [r'\inserted{defi-%}',r'\inserted{defi-}%', 'Mechanical repair: move the closing insertion brace before the comment marker, so it is not swallowed by the TeX comment.'],
 ['(vi) The functor',r'(vi) T\over[typed]{h}{H}e functor','The capital H is a regular typed impression over the lower h.'],
 [r'\xout{\unsure{element} of \underline{W}}',r'\xout{element of $\underline{W}$}','Element resolves beneath the regular x row. Put the underlined mathematical W into valid inline math scope.'],
 [r'projection $\Delta_1 \to e$',r'projection $\hand{\Delta}_1 \hand{\to} e$','The triangle and projection arrow are hand-drawn; the subscript 1 is typed.'],
 [r'$i^{*}(\Delta_1)$'+'\nis',r'$i^{*}(\hand{\Delta}_1)$'+'\nis','The interval triangle in the first asphericity condition is handwritten.'],
 [oldgraph,newgraph,'Reconstruct the revised implication display with its four pen right-arrows, pen left-arrow, typed raised v, and three distinct cancelled clusters around vi. The extra textual less-than sign in the draft is not an independent symbol. Preserve the unresolved cancelled material in its vertical positions.'],
 [r'(v)$\Rightarrow$(vi)',r'(v)$\hand{\Rightarrow}$(vi)','The implication sign in the prose is hand-drawn.'],
 [r'$\Delta_1$ as a generating',r'$\hand{\Delta}_1$ as a generating','The generating-contractor triangle is penned.'],
 [r'$i^{*}(\Delta_1)$'+'\n'+r'$\underline{W}$',r'$i^{*}(\hand{\Delta}_1)$'+'\n'+r'$\underline{W}$','The later interval triangle is penned.'],
 [r'\inserted{over $e_{A^{\wedge}}$}',r'\inserted[typed]{over $e_{A^{\wedge}}$}','Over e_Ahat is typed above the line, with a continuous pen placing curve.'],
 [r'\inserted{``weak homotopy}',r'\inserted[typed]{``weak homotopy}','The opening quote and weak homotopy are typed interlinearly, with a pen placing curve.'],
 [r"intervals''which",r"intervals'' which",'Restore the boundary between the closing quotation and the following word.'],
 [r'(vi)$\Rightarrow$(i)',r'(vi)$\hand{\Rightarrow}$(i)','The later implication sign in the prose is penned.']
]
joinbefore=r'\inserted{defi-}%'+'\n'+r'\inserted{nition on}'
extras=[{'source_id':'OBS:ps_134-4_092:definition_join','before':joinbefore,'after':r'\inserted{definition on}','decision':'apply physical continuation in corrected forms','reason':'The handwritten word is split across the page line and left margin; remove its physical line-end hyphen only in corrected forms.'}]
for j,pair in enumerate(['i to ii','ii to iii','iii to iv','iv to vi'],1):extras.append({'source_id':f'GRAPH:ps_134-4_092:arrow{j}','before':pair+' plain arrow','after':pair+' pen arrow','decision':'provenance correction','reason':'The enlarged display shows an irregular pen double shaft and pen arrowhead for this implication, without an independently recoverable typed arrow layer.'})
extras.extend([
 {'source_id':'GRAPH:ps_134-4_092:extra_above_vi','before':'One cancelled label above vi in the draft','after':'Two separately cancelled clusters above vi','decision':'correct transcription','reason':'The scan has a top typed v-like cluster with machine and pen strikes, and a second rounded hand vi-like cluster below it; preserve both under doubt.'},
 {'source_id':'GRAPH:ps_134-4_092:raised_v','before':'Handwritten inserted v','after':'Typed interlinear inserted v','decision':'provenance correction','reason':'The raised right-hand v and its parentheses have regular typewriter forms.'},
 {'source_id':'GRAPH:ps_134-4_092:less_than','before':'Extra less-than sign before the left-arrow','after':'No separate less-than sign','decision':'correct transcription','reason':'The apparent sign belongs to the left-arrow head, not an independent relation.'}])
save_review({'key':key,'edits':edits,'diffs':{
 4814:[r'\hand{(}theorem 1\inserted{, (ii) $\Rightarrow$ (i))}.','The handwritten opening parenthesis, comma, numbered implication and final closing parenthesis are visible; retain the punctuation dropped by the witness.']
 },'unsure':[
 ['element','All seven lower letters are recoverable beneath the machine x row.'],
 [r'\unsure{(v)}','The uppermost crossed label remains v-like but is too overlaid to settle.'],
 [r'\unsure{(vi)}','The lower cancelled label retains visible parentheses and i-like stem, but the full vi remains tentative.']
 ],'illegible':[
 [r'\illegible{1}','The blackened old label beneath the live raised v remains unreadable.'],
 [r'\illegible{1}','The short old run under weak homotopy is covered by machine cancellation and a heavy pen patch.']
 ],'notes':[
 'The has a regular typed capital H over h.',
 'The cancelled element of W resolves. The first line ends with a cancelled n after a, as encoded.',
 'The four forward implication arrows are pen-drawn, as are the backward arrow and the two prose implication signs. The display is reconstructed with two cancelled clusters above vi, one below it, and an unreadable old label below the typed interlinear v. No independent less-than sign exists.',
 'The second supplied half is blank except for the pencil archive folio 92 at lower left; it was separately opened and inspected.'
 ],'extra_records':extras,
 'evidence':'Both original halves and eight enlarged panels inspected. The second half is blank except for the pencil folio. The definition-on insertion is handwritten across the line boundary and left margin; its comment-hidden closing brace is repaired mechanically. The The patch is typed H over h. Element of W resolves under the machine row. All four Delta triangles and the map to e are handwritten. The implication display contains four pen right-arrows, a pen left-arrow, two distinct cancelled clusters above the live vi, another cancelled label below it, and a typed interlinear v over a fully blackened old label. These layers are reconstructed without the draft spurious less-than sign. The lower cancelled word beneath weak homotopy remains unreadable. Both over e_Ahat and weak homotopy are typed interlinear additions. The final parenthetical theorem reference and in the end are handwritten, and after all is pen-cancelled.'})
v={'key':key,'before':joinbefore,'after':r'\inserted{definition on}','kind':'author word join','reason':'Join the physical handwritten defi-/nition continuation in corrected forms.','source_id':'OBS:ps_134-4_092:definition_join'}
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());old=[x for x in old if x['source_id']!=v['source_id']];old.append(v);p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
for k in ['ps_134-4_091','ps_134-4_092']:
 s=(OUT/'checked_pages'/f'{k}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  n+=1 if m.group()=='{' else -1
  assert n>=0,(k,m.start())
 assert n==0,(k,n)
