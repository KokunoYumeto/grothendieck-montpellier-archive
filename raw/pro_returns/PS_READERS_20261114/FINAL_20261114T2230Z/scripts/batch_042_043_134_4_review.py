import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_042';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[
 ['\n53.\\quad','\n'+r'\hand{53.}\quad','The section numeral and point are handwritten.'],
 [r'\xout{\unsure{a reflection}}',r'\xout{a reflection}','The earlier words a reflection are legible beneath the x row.'],
 [r'\unsure{is} a final',r'\over{is}{is}\deleted{\illegible{1}} a final','Is is retraced in pen, and a separate following old run is densely pen-cancelled. The initial transcription omitted that cancelled material.'],
 [r'\inserted{(NB.}It',r'\inserted{(NB.} It','The inserted NB and following It have a visible word space.'],
 [r'\xout{\unsure{elemen}}',r'\xout{elemen}','The old elemen sequence can be read through the machine cancellation.'],
 [r'\inserted{(trivially)}(ii\')',r'\inserted{(trivially)} (ii\')','Restore the word space after the parenthetical insertion. Its actual parentheses are independent of the outer placing curve.'],
 [r"(i\unsure{'})",r"(i\unsure{\over{'}{'}})",'The prime has superposed irregular pen ink; its layer is not securely cancelled or replaced by a different sign. Preserve the doubtful prime layers.'],
 [r'\uline{moreover} \ the functor',r'\uline{moreover}\textsuperscript{\hand{\unsure{*}}} \ the functor','A separate star-like ink mark is visible above moreover; retain its doubtful graphic reading. Nearby faint dots do not form recoverable text.'],
 [r'\unsure{$*$}\hand{,}',r'\hand{\unsure{\ensuremath{*|1}}}\hand{,}','The compact mark after the lower diagram node lacks clear star arms and also resembles 1. Preserve both candidates with handwritten provenance.'],
 [r'\unsure{on|in}',r'\over[typed]{o}{i}\over[typed]{n}{n}','The live word is in: i is typed over o and the n has repeated type impressions.'],
 ['it is valid',r'it \over[typed]{is}{is} valid','The is has displaced type impressions, with the same live reading.']
]
edits=[[(v.replace("\\'","'") if isinstance(v,str) else v) for v in e] for e in edits]
old=src[src.index(r'\diagram{'):src.index(r'\end{tikzcd}')+len(r'\end{tikzcd}')]
new=old.replace(r'\ar[',r'\ar[color=blue, ').replace(r'\hand{$\mathrm{Hom}_3$}',r'\hand{\ensuremath{\mathrm{Hom}_3}}').replace(r'\hand{$\mathrm{Hom}_4$}',r'\hand{\ensuremath{\mathrm{Hom}_4}}').replace(r'\hand{$*$}',r'\hand{\ensuremath{*}}')
edits.append([old,'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+new,'All diagram arrows and their Hom/star annotations are handwritten; the four condition labels are typed. Preserve topology and remove nested math delimiters in labels.'])
save_review({'key':key,'edits':edits,'diffs':{
 3913:['(f;g) in R_h','The raised typed pair has a semicolon, including its lower curved point, not a comma.'],
 3916:['u(f) is an isomorphism','No then is present in condition ii.'],
 3918:['u(X) is a final object','No then is present in condition ii-prime.'],
 3924:["Contractibility gives (ii-prime) implies (i-prime); weak intervals and finite-product preservation give (i-prime) implies (i)",'The complete two-hypothesis sentence is visible; the witness omits its middle line.'],
 3925:['Doubtful star/1-like mark after the lower right diagram node','A compact dark mark is present and must not be omitted, but its exact graphic is uncertain.'],
 3927:['Pencil asterisk in the left margin','The separate pencil star at diagram height is clearly present.']
 },'unsure':[
 ['a reflection','The old phrase is readable beneath the x impressions.'],
 [r'\over{is}{is}\deleted{\illegible{1}}','The live is resolves as pen retracing, while the following cancelled old run remains unreadable.'],
 ['elemen','The letters elemen remain visible below the machine strike.'],
 [r"\unsure{\over{'}{'}}",'Irregular pen ink overlies the prime, but its exact alteration remains uncertain.'],
 [r'\hand{\unsure{\ensuremath{*|1}}}','The mark has no unambiguous star arms and could be 1-shaped; it remains doubtful.'],
 [r'\over[typed]{o}{i}\over[typed]{n}{n}','The overlaid o/i and repeated n impressions resolve the live in reading.']
 ],'notes':[
 'A reflection is legible beneath machine cancellation.',
 'Is is penned over its typed form. A further old run after it is heavily pen-cancelled and now recorded as illegible.',
 'The old elemen is readable through its x row.',
 'The tilde has a smooth thick pen curve and is handwritten, as encoded.',
 'The prime has a dark overlaid pen layer; the uncertainty is preserved instead of silently removing it.',
 'A star-like mark above moreover is retained with doubt. The faint spots under tion do not give a recoverable textual sign.',
 'Both prose Hom3 subscripts are penned. The final preposition is in, with typed i over o and repeated n.',
 'The is in it is valid has repeated typed impressions, now marked.',
 'The folio 42 at lower left is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_042:requirement','before':'requitement','after':'requirement','line':31,'decision':'master slip variant','reason':'The isolated t for r is settled by the correctly typed requirement in reviewed 134-4/007, line 28.'}
 ],'evidence':'Both original halves and nine enlarged panels inspected. The section number is penned. A reflection and elemen resolve below their machine strikes. The condition-ii-prime is is pen-retraced and followed by an omitted unreadable pen-cancelled run. The semicolon in the typed interlinear pair f;g is clear. The tilde is penned. The parenthetical trivially has its own two parentheses inside a larger placing curve, while the later prime remains ink-layer doubtful. A star-like upper mark and a compact star/1-like diagram mark retain uncertainty. The preposition in and repeated is type impressions resolve. The witness omission removes a complete implication line, preserved here with the matching diagram. All diagram arrows and Hom/star labels are handwritten; condition labels are typed. Whole-word insertion spacing and nested label math are repaired.'})
variants.append({'key':key,'before':'requitement','after':'requirement','kind':'slip corrected','reason':'Isolated t for r, settled by correctly typed requirement in reviewed 134-4/007.','source_id':'OBS:ps_134-4_042:requirement'})

key='ps_134-4_043';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[
 [r'\unsure{impbrtant|important}','important','The word has a regular round o with no b ascender; important is secure.'],
 [r'\xout{\unsure{in W.} \illegible{1}}',r'\xout{in W. \illegible{1}}','The initial in W. is visible through the cancellation, but the following old run remains unreadable.'],
 [r'compa-tibility','compa-%\ntibility','The hyphen is at the handwritten physical line break, not an internal spelling hyphen. Preserve that break explicitly.'],
 [r'or (as we\'ll say) W-\uline{aspheric}.\hand{\unsure{,|)}}'+'\n'+r'\hand{(}Indeed,',r'\inserted[typed]{or (as we\'ll say) W-\uline{aspheric}.}'+'\nIndeed,','The phrase is typed interlinearly, and one continuous placing curve has the two hooks misread as extra punctuation. Neither hook is a separate comma or parenthesis.'],
 [r'\hand{e}\xout{\unsure{I}xxx}',r'\inserted{e}\xout{\unsure{I}\illegible{1}}','The e is penned above the machine-cancelled run; only an I-like initial fragment is tentatively recoverable, and the rest is unreadable.'],
 [r'\over{t}{w}here',r'\over{t}{w}\over{h}{h}ere','The h as well as the new w is pen-retraced; its upper loop is independent of the old typed ascender.'],
 ['Then W is',r'T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\mathrm h}$en W is','A pair of small upper pen marks stands over the h of Then.'],
 ['are strictly\ncompatible',r'are \over{st}{st}rictly'+'\ncompatible','The initial st of strictly is retraced in pen, while the following letters remain typed.']
]
edits=[[(v.replace("\\'","'") if isinstance(v,str) else v) for v in e] for e in edits]
for line in src.splitlines():
 if r'\mathrm{Fl}' in line:
  new=line.replace(r'\mathrm{Fl}',r'F\over{l}{\ell}')
  for before,after,_ in edits:
   if before in line:line=line.replace(before,after);new=new.replace(before,after)
  edits.append(['\n'+line+'\n','\n'+new+'\n','The typed l has a slanting pen overstroke; retain both layers of the Fl notation.'])
step=r'\diagram{\begin{tikzpicture}[baseline=-.4ex,x=1em,y=1ex]\draw[color=blue,line width=.5pt] (0,0)--(.7,0)--(.9,1.7)--(2.1,1.7);\draw[color=blue,line width=.5pt] (.6,0)--(.8,1.7);\end{tikzpicture}}'
edits.append([r'\hand{$\Vert$}',step,'The manuscript has a doubled stepped paragraph sign, joining rules below in W and above If we; it is not a textual double vertical bar.'])
save_review({'key':key,'edits':edits,'diffs':{
 3928:['if it satisfies','The typed verb ends in s, not d.'],
 3935:['X to E','The first target is a clearly typed capital E. Later projections use lowercase e.'],
 3938:[r'\inserted[typed]{or (as we\'ll say) W-\uline{aspheric}.} Then plain Indeed'.replace("\\'","'"),'The old apparent comma/closing parenthesis and opening parenthesis are the two ends of one continuous insertion curve. The actual interlinear sentence is typed.']
 },'unsure':[
 ['important','The o is round and has no b ascender.'],
 [r'\unsure{sub}','The three old cells are heavily struck; sub is plausible but the lower letters cannot all be separated.'],
 [r'\unsure{sm}','The penned S-shaped first letter is clear, but the cramped final m-like strokes are clipped and remain doubtful.'],
 [r'\unsure{h}','The new h covers the lower cell almost completely; an old h remains plausible but not secure.'],
 ['in W.','The in W. segment is readable through the strike.'],
 ['placing-hook end, no independent punctuation','The right hook is continuous with the rule beneath the interlinear or ... W-aspheric phrase; the matching left hook descends before Indeed.'],
 [r'\unsure{I}','Only an I-like initial fragment survives beneath the x row; it remains doubtful.']
 ],'illegible':[
 [r'\illegible{1}','The cancelled run after W_h subset W remains densely crossed and partly overlapped by the following handwriting; no settled reading is imposed.'],
 [r'\illegible{1}','The old run following in W. cannot be fully recovered through the overlapping machine and pen strokes.']
 ],'notes':[
 'Important resolves with an ordinary round o; the suspected b is not present.',
 'Each Fl has typed l with a slanting pen overstroke, now represented explicitly.',
 'The arrows and inclusion signs are handwritten, as encoded.',
 'The terminal sm remains doubtful at the clipped edge, with a clear S-like pen first letter.',
 'The old h remains obscured beneath the pen h.',
 'The doubled stepped rule is an authorial paragraph instruction before If we, retained graphically and applied in the corrected forms.',
 'The old word after W_h subset W remains unreadable. In W. resolves before a still-unreadable further run. The handwritten compatibility is divided only by its physical line break.',
 'Both apparent extra parentheses are the hooks of one continuous curve placing the typed interlinear or ... W-aspheric sentence. They are removed as false textual punctuation.',
 'The lower-left 43 is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_043:paragraph','before':step,'after':r'\par','line':26,'decision':'master author instruction','reason':'The doubled stepped rule directs a new paragraph before If we.'},
 {'source_id':'OBS:ps_134-4_043:it_is','before':'is is sufficient','after':'it is sufficient','line':25,'decision':'master slip variant','reason':'The first is is a clear typed slip for it in the impersonal construction. It is is correctly typed elsewhere in the reviewed discussion, including 134-4/039.'},
 {'source_id':'OBS:ps_134-4_043:localization_letter','before':'N = W^{-1}M is a localisation of N','after':'N = W^{-1}M is a localisation of N','line':16,'decision':'retain author notation','reason':'The localized source should be M in this definition, but the manuscript types N; preserve the variable slip and flag it in the guide.'}
 ],'evidence':'Both original halves, seven detail panels and eight additional enlarged panels inspected. Important resolves, while sub, the final sm and the old h remain doubtful. The first projection target is capital E, and the localization sentence literally says of N. The doubled stepped sign directs a paragraph. In the rewritten strict-compatibility passage, in W. resolves but the following old run and the cancelled word after W_h subset W remain unreadable. The interlinear or ... W-aspheric sentence is typed; its continuous placing curve supplies both hooks initially misread as punctuation around Indeed. The insertion e sits above an unreadable machine-struck run with a tentative I-like first fragment. The h of where and initial st of strictly are pen-retraced, and Then has paired upper h marks. All Fl occurrences retain their typed-l and pen-slash layers.'})
variants += [
 {'key':key,'before':step,'after':r'\par','kind':'author paragraph instruction','reason':'Apply the new paragraph before If we directed by the doubled stepped pen sign.','source_id':'OBS:ps_134-4_043:paragraph'},
 {'key':key,'before':'is is sufficient','after':'it is sufficient','kind':'slip corrected','reason':'Isolated s for t in it is; the impersonal construction and correctly typed it is elsewhere in the reviewed discussion settle the slip.','source_id':'OBS:ps_134-4_043:it_is'}]
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
