import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
GLOBE=r'\mathord{\begin{tikzpicture}[x=1ex,y=1ex,baseline=-.5ex]\draw (0,0) ellipse (.72 and .95);\draw (0,-.95) .. controls (-.75,-.15) and (-.2,.65) .. (0,.95);\end{tikzpicture}}'
key='ps_134-3_089';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m.group(1)+'}}',line)
 new=new.replace(r'\bigcirc',GLOBE).replace(r'$^\wedge$',r'\hand{\ensuremath{^{\wedge}}}')
 if new!=line:edits.append([line,new,'The handwritten hemisphere symbol has a closed outline and an inner curved arc, not a plain circle; reconstruct both strokes. Its hat is also penned. Use ensuremath to avoid nested math delimiters.'])
edits += [
 ['rehabilitating',r'rehab\over[typed]{\unsure{o}}{i}litating','The i after rehab is overtyped on a rounded older impression, tentatively o.'],
 [r'\unsure{,|.}',',','The final mark has a downward tail and is a comma.'],
 [r'\hand{i}ndependently',r'\over{u}{i}ndependently','The handwritten i overwrites the old typed u, whose lower bowl remains visible.'],
 [r'primit\deleted{\unsure{i}}\inserted{ve}',r'prim\over[typed]{a}{i}\over{t}{t}\over{\unsure{j}}{i}\inserted[typed]{ve}','The first corrected i is typed over a; t is pen-retraced. The final i is live pen correction over a j-like lower layer, not a deletion. Ve is typed above the line and placed after it by a curved stroke.'],
 [r'he\hand{mi}spheres',r'he\over{mi}{mi}spheres','The pen mi retraces typed letters; parts of the old bases remain visible.'],
 [r'\inserted{on}triangles',r'\inserted{on} triangles','On is a separate inserted word.'],
 [r'stric\hand{t}',r'stric\over{\unsure{t}}{t}','The final t is penned over a dark older cell, probably typed t; retain uncertainty on the lower layer.'],
 [r'\margin{\unsure{\S}}',r'\margin{\diagram{\begin{tikzpicture}[x=.8em,y=.7ex]\draw (.6,3)--(0,2.6) .. controls (-.3,1.4) and (.9,1.7) .. (.55,.8)--(0,.2)--(.2,-.5);\draw (.05,2.2)--(.65,2.4);\end{tikzpicture}}}','The final pen sign is an angular continuation-like flourish, not a securely readable section symbol. Preserve its visible strokes as a graphic.'],
 [r'\mspage{89}',r'\mspage{\hand{89}}','The lower-left foliation 89 is written by hand.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3067:[r'inaccurate \xout{desi} name','The type clearly reads inaccurate, not accurate; the cancelled desi is distinct.'],
 3072:[r"(or \hand{``}h.''sets'')",'The h is followed by a period and quotation marks; the hand opening mark is visible.'],
 3073:['comes in very naturally','The adverb naturally ends in ly on the page.'],
 3075:[r'$k_i$ $(i \hand{\ensuremath{\geq}} 0)$','The degeneracy lower bound is visibly zero, unlike the preceding face-operation bound one.'],
 3082:['Handwritten angular terminal flourish','The sign exists at the right end of the last line. Its strokes are reconstructed without asserting that it is a section sign.','replace speculative character by graphic']
 },'unsure':[
 [',','The terminal mark after cubes has a visible downward comma tail.'],
 [r'\over{\unsure{j}}{i}','There is no separate cancellation through this cell. The live i is penned over a lower j-like descender, which remains doubtful. An independent view agreed on retaining this live correction.'],
 ['Reconstructed angular pen flourish','The shape is visible, but assigning it the textual value section sign is unsupported; retain the graphic itself.']
 ],'notes':[
 'The i after rehab has a rounded older impression beneath it, retained as a doubtful o.',
 'The first I in the upper foliation and the second I of Chapter II are reinforced by pen; the original hand scopes are retained.',
 'The lower typed u and the live handwritten i of independently are distinguishable.',
 'The word contains typed a-to-i correction, a retraced t, and a live penned i over an uncertain j-like cell. The raised ve is typed; deleting the last i would misrepresent the visible layers.',
 'The t of strict is a pen correction over an obscured older cell, retained as a doubtful t.',
 'Each hemisphere symbol has an inner arc; the reconstruction preserves it instead of substituting a plain circle.',
 'The terminal flourish is reproduced graphically without deciding its semantic function.',
 'The last punctuation after cubes is a comma.'
 ],'evidence':'Both original halves and detail panels for rehabilitating, independently, primitive, hemispheres, strict and the last flourish inspected. The first corrected i of primitive is typed over a; the last is live handwritten i over a j-like old cell, with typed ve inserted after it. The draft cancellation of that last i is rejected. Independently has pen i over typed u. Cubes ends with a comma. The hemisphere symbols have a separate internal arc, and their presheaf hat is penned. Inaccurate, naturally, and the degeneracy index zero are clear against the witness. The last marginal flourish is reconstructed graphically, and the lower foliation is marked handwritten.'})

key='ps_134-3_090';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m.group(1)+'}}',line)
 new=new.replace(r'\bigcirc',GLOBE).replace(r'$\hat{}$',r'\hand{\ensuremath{^{\wedge}}}')
 if new!=line:edits.append([line,new,'Preserve the handwritten hemisphere outline and inner arc; mark the pen hat and avoid nested math delimiters.'])
edits += [
 [r"test-functors\hand{''}which",r"test-functors\hand{''} which",'The quoted term and which are separate words.'],
 [r'\xout{\unsure{f}}dwelled',r'\deleted{\unsure{f}} dwelled','The dark mark over the old f-like character is drawn in pen, not made by machine x strikes. The underlying character remains doubtful.'],
 [r'\inserted{(I believe),}',r'\inserted[typed]{(I believe)}','The entire parenthetical is typed above the line. Its terminal hooked placing stroke is not a textual comma.'],
 [r'(            ),',r'(\hspace{5em}),','The typed reference parentheses enclose a visible blank. Preserve that space instead of letting TeX collapse it.'],
 [r'\unsure{to the}','to the','The cancelled words to the are legible under the machine x row.'],
 [r'(\over{\illegible{1}}{$^8$})',r'(\hand{\unsure{!}}$^8$)','The 8 has regular typewriter loops. The separate heavy mark to its left and below resembles a handwritten exclamation sign; its exact identity remains doubtful. It is not a secure handwritten 8 over an unreadable typed digit.'],
 [r'\inserted{tentative ,}',r'\inserted[typed]{tentative}','Tentative is typed above the line. The apparent comma is the continuous hooked insertion stroke.'],
 ['ject by a',r'je\over[typed]{d}{c}t by a','A tall old d is overlapped by the corrected c in the same typed cell.'],
 ['Fritsch and Latch',r'Fri\over[typed]{j}{t}sch and Latch','The old j descender remains visible under the retyped t.'],
 ['Dispite this',r'Dispite th\over[typed]{i}{i}s','The i has displaced repeated type impressions.'],
 ['are being forgotten',r'are being forg\over[typed]{t}{o}tten','The first o after g overlaps an old typed t.'],
 ['on this topic',r'on th\over[typed]{e}{i}\over[typed]{s}{s} topic','The i overwrites e and the s has repeated type impressions.'],
 [r'\mspage{90}',r'\mspage{\hand{90}}','The lower-left foliation is handwritten.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3084:['settled yet','The typed word includes the final d.'],
 3088:[r'(\hspace{5em}),','The blank reference between typed parentheses is present and remains unfilled.'],
 3089:[r'\margin{X}','A large thin pen X marks the missing reference in the left margin.'],
 3094:[r'\inserted[typed]{tentative}','The insertion is typewritten and has no independent final comma; the curved hook belongs to its placing mark.','correct transcription']
 },'unsure':[
 [r'\unsure{f}','The old character is thickly overwritten in pen; f remains plausible but not secure.'],
 [r'\unsure{that}','The machine x row prevents secure recovery of all four lower letters.'],
 ['to the','Both cancelled words are recoverable.']
 ],'illegible':[[r'\hand{\unsure{!}}$^8$','The 8 is typed; the separate heavy pen mark resembles an exclamation sign but remains doubtful.']],
 'notes':[
 'II ii is typed at the top, whereas 90 is penned at the lower left.',
 'The quotation marks enclosing test-functors are thin pen strokes.',
 'The separating slash after and is handwritten. The hemisphere symbol is reconstructed with its internal arc.',
 'The f-like mark is crossed or overwritten in pen; the lower character remains doubtful.',
 'That remains uncertain under the x row; to the is clearly recoverable.',
 'The 8 has regular typed loops; the nearby heavy pen mark is separate and remains doubtful.',
 'The typed d/c in ject, j/t in Fritsch, t/o in forgotten, repeated i in the first this, and e/i plus repeated s in this topic are represented as overprinting.',
 'Notes 5, 6, 10 and 11 are fully present on the page and are retained, including the literal Dispite and the cancelled rather than and still.'
 ],'evidence':'Both original halves and enlarged panels of dwelled, cancelled that and to the, label 8, ject, Fritsch, forgotten and this inspected. The interlinear I believe and tentative are typed additions; their apparent terminal commas are placing hooks. The unfilled Bourbaki reference remains a visible blank with a pen X in the margin. The word settled includes its final d. To the is recovered; that and the f-like pen-overwritten mark remain doubtful. The regular typed 8 is distinguished from the separate dark pen mark beside it. Five sites of typed overprinting are recorded, and the handwritten hemisphere symbol keeps its inner arc.'})
