import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_099'
edits=[
 ['now look upon',r'now l\unsure{\^o}ok upon','A small roof-like impression lies over the first o; preserve its graphic form under a provenance doubt.'],
 [r'\xout{xxx}',r'\xout{has}','The old h, a and s are separately recoverable beneath the regular x row.'],
 [r'\hand{$\check{\ }$}Cech',r'$\overset{\hand{\scriptscriptstyle\vee}}{\mathrm C}$ech','Place the handwritten caron above the plain typed C, rather than above an empty cell.'],
 [r'ech-type\inserted{W-}',r'ech-type \inserted[typed]{W-}','The raised W- is regular typing; preserve the word boundary before its inserted prefix.'],
 [r'\xout{\unsure{modelizer}}',r'\xout{modelizer}','All letters of modelizer resolve beneath the machine cancellation.'],
 [r'\over{\unsure{4}}{$\Delta$}$_1$',r'\xout{\unsure{4}}\hand{$\Delta$}$_1$','The old crossed cell is to the left of the new handwritten Delta, rather than beneath it; its 4-like reading remains tentative.'],
 ['was looking at',r'was l\unsure{\^o}oking at','The first o repeats the small raised roof-like impression; retain graphic/provenance doubt.'],
 [r'Hot$_{\hand{$\underline{W}$}}$',r'Hot$_{\underline{W}}$','The subscript W is typed, not penned. The correction also removes nested dollar delimiters.'],
 [r'\[ \hand{$\pi$}_o',r'\[ \hand{\ensuremath{\pi}}_o','Mechanical repair: retain the handwritten pi in valid display-math scope.'],
 [r'\hand{$\longrightarrow$} (\mathrm{Sets})',r'\hand{\ensuremath{\longrightarrow}} (\mathrm{Sets})','Mechanical repair: retain the handwritten arrow in valid display-math scope.'],
 [r'\xout{xx}',r'\xout{i\unsure{s}}','The first cancelled letter is i; the obscured following s remains tentative.'],
 ['in terms of 0-connected',r'in terms of \unsure{\over[typed]{O}{0}}-connected','The rounded cell has overlapping regular impressions. Keep the tentative capital-O/zero layer order rather than silently normalizing it.'],
 [r'T\over{\unsure{n}}{h}e situation',r'T\over[typed]{h}{H}e situation','The live capital H and older lowercase h are regular typed impressions, not a handwritten h over n.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4947:['I forgot to clear up','The source visibly types forgot, not the witness forget.'],
 4950:['typed interlinear W- and handwritten caron','The raised W and hyphen have regular typewriter forms; only the caron and placing curve are penned.','correct provenance'],
 4954:[r'\xout{\unsure{4}}\hand{$\Delta$}$_1$','The cancelled 4-like cell is spatially left of the new Delta; preserve its unresolved reading and separate position.','correct layer placement'],
 4957:[r'Hot$_{\underline{W}}$','The subscript W has a regular typed form.','correct provenance'],
 4958:[r'T\over[typed]{h}{H}e situation','The cell contains regular uppercase H over lowercase h, as in the recurring typewriter patch.','correct provenance'],
 4959:[r'\margin{$\times$}','The separate pencil cross in the left margin is visible and retained.']
 },'unsure':[
 ['modelizer','The lower letters resolve through the regular cancellation row.'],
 [r'\unsure{4}','The crossed old cell has a 4-like angular lower shape but remains partly covered.'],
 [r'\over[typed]{h}{H}','The two regular type impressions resolve as lowercase h and capital H.']
 ],'notes':[
 'Both look and looking have a small roof-like mark over the first o. Their graphic form is retained doubtfully without asserting pen provenance.',
 'The first cancelled word resolves as has and modelizer is recoverable. The later cancelled run reads i followed by a tentative s.',
 'The old 4-like cell is crossed and placed to the left of the new Delta, rather than directly under it. Its reading remains doubtful.',
 'The final The has regular typed uppercase H over lowercase h; the original n/hand-h reading is corrected.',
 'The pencil archive folio 99 is visible at lower left.'
 ],'evidence':'Both original halves and ten enlarged panels inspected before the workspace interruption. The first o in look and looking has a recurring small roof-like mark, preserved as graphic/provenance doubt. Has and modelizer resolve under the regular x rows; the later is retains doubt on its second letter. The caron is penned, but the interlinear W- is typed. The crossed old 4-like cell is left of the handwritten Delta, so the source is separated into cancellation and addition instead of an overlay. The subscript W of Hot is typed, and nested math delimiters are repaired without changing its reading. The O/zero patch in 0-connected remains an explicitly doubtful typed overlay. The final The has regular H over h impressions. The left-margin pencil cross and handwritten pi, arrows, Delta symbols, braces and quotation marks remain. The literal singular equivalence, missing it after that, apostrophes and standart are preserved. L6 is now added as the connectedness axiom, and the dated final paragraph begins the revision of weak-interval terminology.'})

key='ps_134-4_100'
edits=[
 [r'\inserted{from now on}',r'\inserted[typed]{from now on}','The interlinear phrase is regularly typed, with a separate pen placing curve.'],
 [r'\xout{an}',r'a\xout{n}','Only the n is machine-cancelled. The preceding a remains live.'],
 ["``\\uline{homotopy}",r'\xout{``}\uline{homotopy}','Regular typewriter x strokes independently cancel the opening quotation marks.'],
 [r"\uline{interval}''(with",r"\uline{interval}\xout{''}(with",'The closing quotation marks are also independently machine-cancelled.'],
 [r're\over{\unsure{p}}{s}pect',r're\over{p}{s}\over{p}{p}ect','The old p beneath the handwritten s resolves. The following p has separate pen retracing over its typed form.'],
 [r'\inserted{page 132}',r'\inserted[typed]{page 132}','The raised reference is typed. Its placing curve passes through earlier without an independent cancellation of that word.'],
 [r'\inserted{till this very minute}',r'\inserted[typed]{till this very minute}','The interlinear phrase is typed and its pen bracket is a placing mark.'],
 [r'\emptyset_M$ ;',r'\hand{\emptyset}_M$ ;','The complete empty-set glyph is hand-drawn; the M subscript is typed.'],
 [r'we have (independe\unsure{nt}ly',r'we have \hand{(}independe\unsure{\over{nt}{nt}}ly','The opening parenthesis is handwritten. The middle nt cells have dense pen retracing over lower typing, whose precise layers remain doubtful.'],
 [r'\emptyset_M$ (initial',r'\hand{\emptyset}_M$ (initial','The second complete empty-set glyph is handwritten, with a plain typed M subscript.'],
 [r're\unsure{sp}ect',r're\unsure{\over[typed]{p}{s}}\over[typed]{p}{p}ect','The first cell has crowded regular p/s impressions with uncertain order; the following p has a clear repeated regular p impression.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4960:['typed from now on, followed by live a and cancelled n','The interlinear phrase is typed; the x cancellation falls on n alone.','correct provenance and cancellation span'],
 4962:[r'a\xout{n} \xout{``}\uline{homotopy} \uline{interval}\xout{\'\'}','The a remains live and the n is cancelled. Both pairs of quotation marks show their own regular machine x strikes.','correct cancellation spans'],
 4965:['earlier, then typed interlinear page 132','The word earlier remains live beneath the continuous placing curve. The insertion is typed and no extra comma is visible.','correct provenance'],
 4966:['typed till this very minute','The raised phrase has regular typewriter forms; its pen curve places the words.','correct provenance']
 },'unsure':[
 [r'\over{p}{s}','The lower p resolves beneath the penned s.'],
 [r'\unsure{scarcely}','The first and second c-like patches remain crowded; the word is plausible but its affected layers do not resolve securely.'],
 [r'\unsure{\over{nt}{nt}}','The middle letters are densely retraced; preserve the tentative nt layers under a whole doubt.'],
 [r'\unsure{\over[typed]{p}{s}}\over[typed]{p}{p}','The first p/s cell retains layer-order doubt, while the following repeated p is clear.']
 ],'notes':[
 'The a is live; only n and the independently marked opening and closing quotation marks are machine-cancelled.',
 'Page 132 is typed above the line. The long curve is a placing mark and earlier remains live. Scarcely retains its unresolved letter-layer doubt.',
 'The first respect has a resolved handwritten s over p and a pen-retraced following p. The second has a doubtful typed p/s layer and a repeated typed p.',
 'The opening parenthesis before independently is penned, and nt remains a doubtful dense retracing over typed letters.',
 'The a above the cancelled the is typed, as already encoded.',
 'The pencil archive folio 100 is visible at lower left on the second half.'
 ],'evidence':'Both original halves and nine enlarged panels inspected before the workspace interruption. The lower half contains only the final three body lines and the pencil archive folio. From now on, page 132 and till this very minute are typed interlinear additions with pen placing curves. The first a is live and the following n is machine-cancelled. Independent regular x impressions cross both quotation pairs around homotopy interval. Earlier remains live: the nearby stroke belongs to the placement of page 132. The first respect has a resolved p-to-s pen correction followed by pen retracing of p; the final respect retains p/s type-layer uncertainty and a separate repeated p. Scarcely and the retraced nt of independently remain doubtful; the preceding parenthesis is handwritten. All delta and empty-set glyphs are penned while their subscripts remain typed. The raised a above the cancelled the is correctly marked typed. The literal caracterization is retained. The page broadens homotopy interval to the former weak notion and replaces separated interval by separating interval; the source mathematical claims are not silently amended.'})
for key in ['ps_134-4_099','ps_134-4_100']:
 s=(OUT/'checked_pages'/f'{key}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  n+=1 if m.group()=='{' else -1
  assert n>=0,(key,m.start())
 assert n==0,(key,n)
