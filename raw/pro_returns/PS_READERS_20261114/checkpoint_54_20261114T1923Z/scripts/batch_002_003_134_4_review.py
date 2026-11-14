import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-4_002';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'i_!',r'i_{\hand{!}}').replace(r'\simeq',r'\hand{\simeq}')
 if new!=line:edits.append([line,new,'All these arrows, hats, the left-adjoint exclamation subscript and the localization comparison sign are drawn in pen; the adjacent letters are typed.'])
edits += [
 [r'anywhere\hand{,}to',r'anywhere\hand{,} to','The comma is followed by the separate word to.'],
 [r'\over{\unsure{t}}{t}est',r'\over{t}{t}est','The older serifed typed t remains visible under the taller pen t.'],
 ['There is also',r'T\over[typed]{H}{h}ere is also','The H and h share a typewriter cell.'],
 [r'compare\inserted{directly} \deleted{an}',r'compare \inserted[typed]{directly} \unsure{an}','Directly is typed above the line. Its placing curve crosses an, but no independent deletion stroke is separable; retain an with explicit uncertainty instead of deleting it outright.'],
 [r'\deleted{\unsure{to}}',r'\deleted{to}','The old t stem and rounded o are visible beneath the diagonal pen hatching.'],
 [r'neither\inserted{to}',r'neither \inserted{to}','The inserted to is a separate word.'],
 [r"isn\hand{'}t",r"is\hand{'}n\over{t}{t}",'The added apostrophe is placed before n, and the final t is pen-retraced over a typed t. Retain the visible is\'nt order.'],
 [r'functors\inserted{(3)}',r'functors \inserted{(3)}','The inserted formula reference is separated from functors.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3157:['be mapped into anywhere','The typed past participle is mapped.'],
 3159:[r'modelizers\xout{\unsure{,}}','A machine x strikes the punctuation cell; its underlying comma remains doubtful.'],
 3161:[r'canonical functor $i_A$','The source does not add a restriction-to-A sign.'],
 3163:[r'thus $i_A$ is','The word is thus, not this.'],
 3165:[r'\unsure{an} arbitrary','The only clear line crossing an is the placement curve for directly. Cancellation cannot be established securely, so the word remains in doubt.','retain uncertain cancellation'],
 3168:[r'nor\hand{ to} inverse limits','The handwritten to is present after nor at the right edge.'],
 3169:[r"is\hand{'}n\over{t}{t}",'The apostrophe lies before n, with pen retracing of the final t.','correct transcription'],
 3172:[r'\margin{also to fibered products $\times$}','The faint pencil note is legible in the margin, including its final cross.']
 },'unsure':[
 [r'\unsure{,}','The machine x obscures the lower punctuation cell.'],
 ['t','The typed t survives under the pen replacement.'],
 ['to','Both lower letters can be distinguished through the pen hatching.']
 ],'notes':[
 'The spectra parenthetical is typed. The little terminal hook belongs to its placing line and supplies no comma.',
 'The cancelled punctuation after modelizers remains doubtful as a comma.',
 'The underlying typed t is visible beneath the pen t.',
 'The crossed word before neither is to.',
 'The right-edge addition reads to after nor.',
 'The apostrophe is before n, and t is pen-retraced; the source order is is\'nt.',
 'The pencil note reads also to fibered products, followed by a cross.',
 'The lower-left handwritten 2 is preserved as a marginal foliation.'
 ],'evidence':'Both original halves, five enlarged inline details and a rotated view of the pencil margin inspected. The source says mapped, thus, and canonical i_A without the witness restriction. All arrows and hats are penned. Directly is a typed interlinear addition; its curve crosses an but does not independently establish deletion, so an remains explicitly doubtful. The old to is recovered under dense pen hatching. The handwritten nor to is present, and the apostrophe in is\'nt is visibly before n. The pencil margin adds also to fibered products and a cross. The first spectra insertion has no independent terminal comma.'})

key='ps_134-4_003';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A^\wedge',r'A^{\hand{\wedge}}').replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'A \to',r'A \hand{\to}').replace(r'\phi',r'\hand{\phi}').replace(r'\psi',r'\hand{\psi}')
 if new!=line:edits.append([line,new,'The arrows, presheaf carets and phi/psi symbols are handwritten; preserve the typed surrounding letters.'])
edits += [
 ['except\n',r'ex\over[typed]{c}{c}\over[typed]{e}{e}pt'+'\n','The c and e have repeated type impressions.'],
 ['in this case',r'in this ca\over[typed]{s}{s}e','The s has displaced typed impressions.'],
 [r'we get \xout{\illegible{1}}',r'we get \xout{of course}','The old words of course are readable under the x row.'],
 [r'\longrightarrow} A^{\hand{\wedge}} \]',r'\longrightarrow} \over[typed]{A}{A}^{\hand{\wedge}} \]','The A in formula (4) has repeated typed impressions.'],
 ['More specifically',r'M\over[typed]{o}{o}re specifically','The o has a second lower type impression.'],
 [r'\xout{xxxx}\inserted{modelizers}',r'\xout{ones} \inserted[typed]{modelizers}','The old word ones is recoverable; modelizers is typed above the line.'],
 ['in due cour-',r'in due \over{\unsure{c}}{c}our-','The c is penned over a partly visible older rounded type cell.'],
 ['There is  one',r'T\over[typed]{h}{h}ere is  one','The h has displaced regular type impressions.'],
 [r'\xout{\illegible{1}} \inserted[typed]{avators}',r'\xout{species} \inserted[typed]{avators}','The old species is legible under the x row; retain the literal typed replacement avators.'],
 [r'\xout{xxxx} ``highly',r'\xout{case} ``highly','The four cancelled letters read case.'],
 ['THe situation',r'T\over[typed]{H}{h}e situation','The H and h occupy the same typed cell.'],
 ['\nry modelizer','\n'+r'r\over[typed]{u}{y} modelizer','The typed u remains visible under the replacement y.'],
 ['considered  as',r'consid\over[typed]{\illegible{1}}{e}red  as','The e-cell has overlapping type impressions; the older letter cannot be identified securely.'],
 [r"it's\hand{``}next best\hand{''}substitute",r"\over[typed]{it}{it}'s \hand{``}next best\hand{''} substitu\over[typed]{e}{t}e",'The it has repeated type impressions, and the final t of substitute overlies e. The added quotation marks enclose next best with word boundaries.'],
 [r'r_{\hand{!}} i^* : (\mathrm{Cat}) \hand{\longrightarrow} (\mathrm{Spaces})',r'r_{\hand{!}} i^* : (\mathrm{Cat}) \hand{\longrightarrow} (\over[typed]{\mathrm{Spa}}{\mathrm{Spa}}\over{\mathrm{c}}{\mathrm{c}}\mathrm{es})','In formula (6), S/p/a have overlapping typed impressions and c is retraced in pen.'],
 [r'\ar[r, shift left,',r'\ar[r, shift left,color=blue,','The upper adjunction arrow is drawn in pen.'],
 [r'\ar[l, shift left,',r'\ar[l, shift left,color=blue,','The lower adjunction arrow is drawn in pen.'],
 [r'\[ (5) \qquad \diagram{',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\noindent $(5)\qquad$ \diagram{','Keep the mixed diagram outside the outer math display to avoid nested math mode. Its number remains mathematical and both pen arrows retain their directions.'],
 [r'\end{tikzcd}} \]',r'\end{tikzcd}}','Close the now-inline diagram without the obsolete display delimiter.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3175:['in M depending','There is no comma after M at the line end.'],
 3180:['presumably...). There','The typed period after the closing parenthesis is visible.'],
 3183:[r'\xout{(5)}','The old (5) is machine-cancelled; no live three-star label is supplied by the page.'],
 3190:[r'r_{\hand{!}} i^* : (\mathrm{Cat}) \hand{\longrightarrow} (\mathrm{Spaces})','The second functor is visibly i*, not r*. This is the composite with the Cat-to-presheaves functor (4).'],
 3193:[r"\hand{``}next best\hand{''}",'The quotation marks are handwritten and enclose next best.']
 },'unsure':[
 [r'\unsure{r}','The right edge cuts the terminal cell; its top stroke is visible but its complete form remains unconfirmed.'],
 [r'\unsure{.}','The edge after limits does not establish a complete final period.']
 ],'illegible':[
 ['of course','The cancelled lower letters are recoverable beneath their x row.'],
 ['species','The old seven letters remain readable below avators.']
 ],'notes':[
 'The last r of particular remains clipped and doubtful; no full handwritten replacement is asserted.',
 'The cancelled phrases are of course and species, both recovered from the enlarged image.',
 'The final punctuation after limits remains uncertain at the cut edge.',
 'The hand and has only a placing hook after it; no extra comma is supplied.',
 'W is hand-corrected over w. The cancelled word is ones, with typed modelizers above it.',
 'The lower-left handwritten 3 is preserved as a marginal foliation.',
 'The listed sites contain typewriter overlap: repeated c/e in except, repeated s in case, u/y in ry, unresolved older e-cell in considered, repeated it, e/t in substitute, and repeated Spa in Spaces; its c is pen-retraced.'
 ],'evidence':'Both original halves and fourteen enlarged details inspected. Of course, ones, species and case are recovered under machine x strikes. Modelizers and avators are typed replacements, with the latter spelling retained. The diagrams and all inline arrows have pen strokes; phi/psi and hats are also handwritten. Formula (6) clearly has r_! i*, preserving the source against the witness r_! r*. The old display label (5) is cancelled without a replacement three-star label. There are repeated type impressions in several words, a clipped final r and uncertain right-edge period. The typed H-to-h correction in The and the handwritten quotation marks around next best are retained.'})
