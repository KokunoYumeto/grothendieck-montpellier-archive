import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_058'
separator=r'\diagram{\begin{tikzpicture}[baseline=-.4ex,x=1em,y=1ex]\draw[color=blue,line width=.35pt] (0,2.4)..controls(0,1)and(-.05,-.5)..(.2,-1.4);\end{tikzpicture}}'
marks=r'\unsure{T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\underset{\hand{\scriptscriptstyle,}}{\mathrm h}}$e}'
edits=[
 [r'which\inserted{category}',r'which \inserted{category}','Restore a word boundary before the handwritten category insertion.'],
 [r'fro\hand{m}(Cat)',r'fro\hand{m} (Cat)','The m is hand-drawn as encoded; preserve the boundary before the category name.'],
 [r'Th\uline{is}',r'Th\uline{i}\over[typed]{s}{s}','The short rule falls beneath i alone. The final s has repeated regular typed impressions.'],
 [r'$W_{\text{(Cat)}} = W$',r'$W_{\text{(Cat}\over{p}{)}} \over[typed]{\unsure{,}}{=} W$','The subscript closing parenthesis is penned over a typed p. The equality has a displaced comma-like lower impression, retained tentatively.'],
 [r'\xout{ly}',r'\deleted{\xout{ly}}','The regular machine-x cancellation of ly also carries an irregular pen crossing.'],
 [r'\uline{localization}',r'\uline{localiz\over{at}{at}\over[typed]{i}{i}on}','The a and t have pen retracings; the i has repeated typed impressions.'],
 [r'homotopi\unsure{sms}\hand{|}only',r'homotopi\unsure{\over{sms}{sms}}'+separator+' only','The terminal sms has dense ink and uncertain lower layering. The following pencil stroke is a slightly curved graphic separator, not a textual vertical-bar symbol.'],
 ['getting this factorization',r'getting this factori\over[typed]{s}{z}ation','The z has a rounded s-like lower type impression.'],
 [r"\unsure{is'nt|isn't}","is'nt",'The raised apostrophe follows the s in the handwritten margin note.'],
 ['Quillen\'s closed',r"Quillen's clo\unsure{\over{s}{s}}ed",'The s has a curved dark pen layer, but the older form and exact stroke scope remain uncertain.'],
 [r'focus\xout{x}',r'focus\xout{\illegible{1}}','The regular x impression cancels an unrecoverable extra cell; it is not evidence for an old textual x.'],
 ['59. Before',r'5\over{\unsure{8}}{9}. \over[typed]{B}{B}efore','The 9 is a pen replacement over a doubtful older digit; Before has repeated regular capital B impressions.'],
 ['sets, which is true',r'set\unsure{\over{s}{s|)}}, which is true','The terminal s has a curved pen layer resembling a parenthesis; retain uncertainty rather than silently choosing its letter form.'],
 ['connected spaces. The point','connected spaces. '+marks+' point','The repeated paired upper marks and lower comma-like spot around h are preserved, but their pen-versus-mechanical provenance is doubtful.']
]
# Repair each nested math delimiter without changing a visible symbol.
for before,after,why in [
 (r'\text{(Cat)} \hand{$\longrightarrow$} \overline',r'\text{(Cat)} \hand{\ensuremath{\longrightarrow}} \overline','first localization arrow'),
 (r'\overline{\text{(Cat)}} \hand{$\longrightarrow$} \text{(Hot)}',r'\overline{\text{(Cat)}} \hand{\ensuremath{\longrightarrow}} \text{(Hot)}','second localization arrow'),
 (r'$W_h \hand{$\subset$} W$',r'$W_h \hand{\ensuremath{\subset}} W$','inclusion sign'),
 (r'$f \hand{$\in$} W$',r'$f \hand{\ensuremath{\in}} W$','membership sign'),
 (r'$\hand{$\pi$}_0(f)$',r'$\hand{\ensuremath{\pi}}_0(f)$','component functor'),
 (r'$C\mathrm{x}\hand{$\Delta$}_1 \hand{$\longrightarrow$} C$',r'$C\mathrm{x}\hand{\ensuremath{\Delta}}_1 \hand{\ensuremath{\longrightarrow}} C$','projection formula')]:
 edits.append([before,after,'Mechanical math-mode repair for the '+why+': replace nested dollar delimiters by ensuremath; symbol and provenance unchanged.'])
save_review({'key':key,'edits':edits,'diffs':{
 4199:['59. with its digit overwritten; no title','The source has a numbered paragraph without the witness descriptive section heading.']
 },'unsure':[
 [r'\unsure{\over{sms}{sms}}','The ending is heavily overlaid; sms is strongest, but its lower letters and layer order remain doubtful.'],
 ["is'nt",'The apostrophe is visibly after s in the dated handwritten note.']
 ],'notes':[
 'The short horizontal rule is under i alone; the final s has repeated type impressions.',
 'The terminal sms remains doubtful in its layers. The following pencil separator is curved and is reproduced as a graphic, with a real boundary before only.',
 'The closing parenthesis is penned over typed p, the equality has a doubtful comma-like lower cell, ly has both machine and pen cancellation, and localization has pen at and repeated typed i.',
 'The m of from is wholly handwritten, as encoded; there is no additional readable lower letter.',
 'The z of factorization is typed over an s-like lower impression.',
 'The closed s has a dense curved pen layer, retained under a doubt.',
 'The extra cell after focus is machine-cancelled and its old content remains unreadable.',
 'The heading has pen 9 over a doubtful older digit and repeated typed B in Before. The terminal s of sets has a doubtful curved pen layer. The recurring upper/lower h marks of The have uncertain mechanical-versus-pen provenance.',
 'The bars over Cat and W are straight rules whose precise typing-versus-drawing provenance is not secure; their notation is retained without inventing corrections.',
 'The pencil folio 58 is visible at lower left.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_058:ususal','before':'ususal','after':'usual','decision':'isolated typing slip corrected only in corrected forms','reason':'The extra su is visibly typed, while usual is correctly typed in reviewed 134-4/057 and elsewhere. Preserve ususal diplomatically.'}],
 'evidence':'Both original halves and twelve enlarged panels inspected. Category is a handwritten insertion requiring a word boundary. The m of from is handwritten. The short underline in This covers i, while s is repeated typing. A typed p is visible under the pen closing parenthesis of W-sub-Cat; the equality lower comma-like impression remains doubtful. The ly cancellation has both machine and pen strokes. Localization has pen at retracing and repeated i. The terminal sms layers and the curved s of closed remain doubtful, and the pencil separator after homotopisms is reconstructed graphically. Factorization has z over s. The dated 6.4 margin visibly writes is-apostrophe-nt and retracts the pi-zero condition. The extra cancelled cell after focus is unreadable. The heading and Before have distinct overwritten layers, and sets and the recurring The marks retain uncertainty. All nested math dollars were repaired mechanically without changing the penned signs.'})

key='ps_134-4_059';edits=[
 [r'direction\hand{,} associating',r'direction\hand{,} as\over[typed]{s}{S}ociating','The second s is overtyped by a regular capital S; retain that visible capital rather than normalize the word.'],
 ['we should have to restrict',r'we \over{sh}{sh}ould have to restrict','The sh of should is retraced in pen over its typed letters.'],
 ['matter  visibly',r'matter  \unsure{\over[typed]{v}{v}}isibly','The v has dense repeated impressions whose provenance and order remain uncertain.'],
 ['introducing as an',r'int\over{ro}{ro}ducing as an','The r and o have irregular dark pen retracings over type.'],
 ['The first which comes',''+marks+r' first which c\over{\unsure{a|o}}{o}mes','The recurring upper/lower h marks have uncertain provenance. The o of comes is penned over an older rounded cell, whose a/o reading remains doubtful.'],
 [r'\pi}_0-functor',r'\pi}_0-fun\over{c}{c}tor','The c of functor is retraced in pen.'],
 ['through the localized',r'through the \unsure{\over[typed]{r}{l}}ocalized','The initial cell has a small r-like upper blob beside the live l stem; retain the typed-layer doubt.'],
 ['(maybe we should',r'(may\over[typed]{\unsure{o|b}}{b}e we should','The b has an older rounded impression; o or repeated b remains uncertain.'],
 [r':\xout{x}(Hot)',r':\xout{\illegible{1}}(Hot)','The cancelled extra cell after the colon has no recoverable older reading.']
]
# All seven arrows are hand-drawn, including those left plain by the draft.
arrow_edits=[
 (r'(Spaces) \longrightarrow (Sets)',r'(Spaces) \hand{\longrightarrow} (Sets)'),
 (r'M \rightarrow (Sets)',r'M \hand{\rightarrow} (Sets)'),
 (r'M \longrightarrow (Hot)',r'M \hand{\longrightarrow} (Hot)'),
 (r'M \rightarrow (Hot) \longrightarrow (Sets)',r'M \hand{\rightarrow} (Hot) \hand{\longrightarrow} (Sets)'),
 (r'(Hot) \longrightarrow (Sets)',r'(Hot) \hand{\longrightarrow} (Sets)'),
 (r'(Cat) $\longrightarrow$ (Sets)',r'(Cat) $\hand{\longrightarrow}$ (Sets)'),
 (r'M $\rightarrow$ (Hot)',r'M $\hand{\rightarrow}$ (Hot)')]
for a,b in arrow_edits:edits.append([a,b,'The corresponding arrow has an irregular pen shaft and pointed pen head; restore its handwritten provenance.'])
# Give every previously bare inline pi-subscript expression valid math scope.
for a,b in [
 (r'that \hand{\pi}_0 commutes',r'that $\hand{\pi}_0$ commutes'),
 (r'commutation of \hand{\pi}_0 to',r'commutation of $\hand{\pi}_0$ to'),
 (r'natural functor \hand{\pi}_0 indeed',r'natural functor $\hand{\pi}_0$ indeed'),
 (r'the \hand{\pi}_0-fun',r'the $\hand{\pi}_0$-fun'),
 (r'natural functor \hand{\pi}_0 around',r'natural functor $\hand{\pi}_0$ around'),
 (r'given \hand{\pi}_0 )',r'given $\hand{\pi}_0$ )'),
 (r'just \hand{\pi}_0 ,',r'just $\hand{\pi}_0$ ,'),
 (r'functor \hand{\pi}_0 .',r'functor $\hand{\pi}_0$ .')]:edits.append([a,b,'Mechanical repair: place the inline pi-with-subscript in math mode; no reading or provenance change.'])
save_review({'key':key,'edits':edits,'diffs':{
 4208:['an adjunction formula','Formula is plainly typed and is omitted by the witness.'],
 4212:['Thus followed immediately by the opening quotation','No comma is visible after Thus.'],
 4213:[r'modelizer\unsure{,}','The right edge clips the punctuation; preserve the tentative comma instead of silently removing it.'],
 4226:['59','The handwritten archive folio is visible and remains included.']
 },'unsure':[
 [r'\unsure{s}','The extra old cell after extra is crossed by regular x strokes; s remains only a tentative lower reading.'],
 [r'\unsure{,}','A small dark projection survives at the clipped edge, but punctuation identity remains uncertain.']
 ],'notes':[
 'Pathwise is typed interlinearly. Its continuous placing curve points before locally and does not independently cancel locally; both words remain live in the indicated order.',
 'The capital S over s of associating, pen sh of should, and pen ro of introducing are recorded. Visibly, the repeated h marks, comes, localized and maybe retain uncertainty where the old layer or provenance is not secure; functor has a pen c retracing.',
 'The extra final cell after extra is clearly machine-cancelled but only tentatively s. The cell after the displayed colon is unreadable beneath its cancellation.',
 'The physical canoni/cal and some/thing continuations remain joined. The added i at the edge after canon has both a visible dot and a short pen stem. The punctuation after modelizer remains clipped and doubtful.',
 'The pencil folio 59 is visible at lower left.',
 'The pi signs are penned; their typed round subscripts retain the draft zero convention. Each displayed or inline arrow is independently visible as pen-drawn.'
 ],'evidence':'Both original halves and fourteen detail panels inspected. Pathwise is typed above the line, and its placing curve leaves locally live. The second s of associating has a regular capital S overprint. Should has pen sh retracings, introducing pen ro, functor a pen c, and comes a penned o over a doubtful old rounded cell. Visibly, localized and maybe have uncertain older layers; the recurring top/bottom marks around The h are also marked doubtful in provenance. The extra cell after extra remains tentatively s under cancellation, while the cancelled cell after the displayed colon is unreadable. The edge-added i of canonical is visible, but the punctuation after modelizer remains clipped. All arrows are hand-drawn, including those incorrectly left plain in the initial text. Eight bare inline pi expressions were put into valid math mode. Formula and the absence of a comma after Thus are preserved against the witness.'})
for k in ['ps_134-4_058','ps_134-4_059']:
 s=(OUT/'checked_pages'/f'{k}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  n+=1 if m.group()=='{' else -1
  assert n>=0,(k,m.start())
 assert n==0,(k,n)
v={'key':'ps_134-4_058','before':'ususal','after':'usual','kind':'slip corrected','reason':'Isolated duplicated su; usual is correctly typed in reviewed 134-4/057 and elsewhere.','source_id':'OBS:ps_134-4_058:ususal'}
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());old=[x for x in old if x['source_id']!=v['source_id']];old.append(v);p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
