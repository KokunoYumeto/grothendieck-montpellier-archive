import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_063';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=new.replace(r'A^\wedge',r'A^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The presheaf carets are separate pen marks. Repair nested math delimiters with ensuremath without changing the typed base letters or the mathematical reading.'])
edits += [
 [r'\mspage{63}',r'\mspage{\hand{63}}','The folio is handwritten.'],
 [r'\inserted{get}',r'\inserted[typed]{get}','The added get has typewriter letterforms above a pen placement curve.'],
 [r'I had to stop',r'I had \over[typed]{s}{t}o stop','The t is typed over an old s at the same position; the lower s curve remains visible.'],
 [r'T\hand{h}e main',r'T\over[typed]{h}{h}e main','Both h impressions have typewriter serifs, the second displaced downward; this is typed overprinting rather than a handwritten h.'],
 [r'of A,\inserted{plus asphericity',r'of $A^{\hand{\wedge}}$,\inserted{plus asphericity','The enlarged scan shows a small independent raised caret above and to the right of A. It is separate from the later insertion curve and cannot be omitted.'],
 [r'\unsure{prousin}',r'\unsure{promise}','The quoted cursive word begins pro and has medial strokes compatible with promise, but the last letters remain too compressed to settle; retain a tentative reading.'],
 [r'\hand{\unsure{;|:}}',r'\hand{;}','The lower dot has a distinct descending leftward tail; this is a handwritten semicolon.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2609:[r'\inserted[typed]{get}','The insertion itself is typed; only its placement curve is pen.','correct transcription'],
 2610:['giving heaps','The line ends giving, with no final s; the next line begins heaps.'],
 2614:[r'of $A^{\hand{\wedge}}$,','A distinct pen caret stands above the A before the comma. The insertion begins farther right. This agrees with the mathematical reading in the witness, while correcting the transcription’s omission.','correct transcription'],
 2616:['that the two do','The typed article the is plainly present between that and two.'],
 2618:[r'\hand{(44)}','The handwritten call after mind reads 44.'],
 2619:[r'\margin{X}','A separate X is drawn in the left margin beside pect, however.'],
 2620:[r'\margin{cf 65 E,F (after ``\unsure{promise}'' 47)}','The page number 65, capitals E,F and final 47 are clear. The quoted cursive word remains doubtful after rotation and enlargement.','correct transcription'],
 2622:[r'F \hand{\to} A_{/F}','The arrow after F has no tail bar; the a-to-A/a arrow above it does have a bar.']
 },'unsure':[[r'\unsure{promise}','The word is still not secure; the tentative reading better fits the visible pro and medial strokes than prousin.'],[';','The enlarged lower dot has a comma tail, settling the separator as a semicolon.']],
 'illegible':[[r'\illegible{1}','The crossed small item after functor has overlapping angular and rounded strokes, with no safely separable complete character.']],
 'notes':[
 'The t in had to is typed over s; the old s is recoverable and has been represented.',
 'The h has two displaced serif type impressions. The o of point is ink-heavy, but no distinct substituted letter is recoverable; the legible word point is retained.',
 'The corrected i over a has a sloping ink stroke and dot, unlike the clean typeset i elsewhere; the existing handwritten overprint is retained.',
 'The separator is a handwritten semicolon, settled by the tail on its lower dot.',
 'The marginal cf 65 E,F and 47 are clear; the quoted word remains tentative as promise.',
 'The short cancelled item after functor remains illegible; no reading is supplied from context alone.'
 ],'evidence':'Both original halves inspected, followed by eight enlarged local details and a renewed view of each full half. The crucial A after unit element really has its own small pen caret, separate from the insertion plus asphericity of the latter. The insertion get is typed, and The has a displaced typed h over h. The section retains Lets, two kind, localised and définition. The canonical a-to-slice arrow has a mapsto tail, whereas F-to-A/F is plain. The marginal word after after remains doubtful, and the crossed item following functor is unresolved. The semicolon in the i_A display is settled by its lower tail.'})

key='ps_134-3_064';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=new.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'A\hat{u}',r'A\overset{\hand{\wedge}}{u}')
 for macro in ('longrightarrow','to','subset','simeq','phi'):
  new=re.sub(r'\\'+macro+r'(?![A-Za-z])',r'\\hand{\\'+macro+'}',new)
 if new!=line:edits.append([line,new,'The scan shows pen carets, phi symbols, arrows and inclusion/isomorphism signs on this line. Preserve the typed letters, including the stray u under the Corollary 2 caret, and repair nested math delimiters.'])
edits += [
 [r'\mspage{64}',r'\mspage{\hand{64}}','The folio is handwritten.'],
 [r'\over{\unsure{W}}{L}',r'\over{W}{L}','The old letter under the pen L has the two diagonals and upper serif of a typed W.'],
 [r'Then we get :',r'T\over{h}{\unsure{h}}en we get :','A small dense pen correction lies above the typed h. It is h-like but not fully separable, so retain the observed overprint with a doubtful reading.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2627:[r'b\uline{e}','Only the e of be is underlined by the short separate stroke.'],
 2630:[r'see prop. \hand{in} \deleted{p.}\inserted{section} 30','The handwritten in and section replace the typed page-reference wording; 30 stays typed.'],
 2631:[r'\hand{(}and also \deleted{\illegible{1}}\inserted{section 29)}, for equivalent formulations\deleted{)})','The opening pen parenthesis and replacement section 29) are readable. The old reference is densely struck, and the earlier closing parenthesis after formulations has a cancellation.'],
 2633:[r'\margin{25.3. or rather, than the set of conditions T1 to T3}','The oblique margin is dated 25.3. and revises the comparison to the set T1 through T3; retain it as marginal wording.'],
 2637:[r'\over{W}{L}et again','The lower letter is visibly a typed W beneath the hand L.','correct transcription'],
 2639:[r'\hand{\phi}(C) =','A typed equals sign follows the hand phi(C), not a comma.']
 },'unsure':[[r'\unsure{va}','The right-edge cancelled letters remain clipped and overtyped; va is plausible but not fully visible.'],['W','The old typed W remains distinguishable beneath the pen L.']],
 'illegible':[[r'\illegible{1}','The old character after wide sense is obscured by looped cancellation; a parenthesis-like trace is insufficient for a secure reading.'],[r'\illegible{1}','The old reference under section 29) is crossed densely enough that its full literal text cannot be recovered.']],
 'notes':[
 'The right edge shows fi followed by the machine-cancelled na fragment; its continuation nal begins on the next line.',
 'The first old p. is clear. The second old reference remains illegible. A short old closing parenthesis after formulations is cancelled before the surviving parenthesis and period.',
 'The cancelled terminal va remains uncertain because the right edge clips it. The old W beneath Let is settled.',
 'The subscript really has a typed u with a pen caret above it, after A. Preserve this irregularity instead of normalizing it to A-hat. The extra l before the hyphen is machine-cancelled.',
 'Every displayed phi, plain arrow, the hook arrow, the isomorphism sign and the subset sign is handwritten; the displayed equals sign after phi(C) is typed.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_064:1','before':'for a in J','after':'for a in J','decision':'retain apparent authorial slip','reason':'The scan plainly types J, although a indexes values J(a) and is consequently an object of A in the construction. Preserve the visible J.','line':31}],
 'evidence':'Both original halves read and nine enlarged details inspected. Corollary 1 retains the underlined e of be, the replacement references to sections 30 and 29, and the dated margin strengthening the comparison from T2 to all T1–T3. The interval-to-Lawvere map is described through cribles; phi(C) has a typed equals sign, and its arrows/subset/isomorphism glyphs are pen. The sentence for a in J is literally typed that way and is preserved as an apparent indexing slip. Corollary 2 retains the stray typed u under a pen caret in its final-object subscript. The two old cancelled items and the clipped va remain unresolved; the old W is recovered. A small h-like overprint above the final Then is newly retained with uncertainty.'})
