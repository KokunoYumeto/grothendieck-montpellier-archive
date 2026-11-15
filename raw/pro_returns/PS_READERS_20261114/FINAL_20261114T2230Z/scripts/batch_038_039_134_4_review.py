import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

def hmarks(tail='e'):
 return r'T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\underset{\hand{\scriptscriptstyle,\frown}}{\mathrm h}}$'+tail
key='ps_134-4_038';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[
 [r'\hand{(}it will',r'\hand{(}i\over{t}{t} w\over{ill}{ill}','The parenthesis is penned, and t in it and ill in will are retraced over the typed letters.'],
 [r'\inserted{M-}isomorphic',r'\inserted[typed]{M-}isomorphic','M- is typed above isomorphic, with a pen placing hook.'],
 [r'\inserted{M-}equivalent',r'\inserted[typed]{M-}equivalent','This M- is likewise a typed interlinear prefix.'],
 [r'w\hand{h}ether',r'w\over{\unsure{h}}{h}\over{e}{e}ther','Both h and e have pen retracing. The lower h-like impression is obscured, while the old e remains recognizable.'],
 [r'T\hand{h}e first',hmarks()+' first','The h is typed and legible; the pen adds paired upper and lower marks rather than replacing the letter.'],
 [r'\inserted[typed]{injective on objects,}\hand{,}',r'\inserted[typed]{injective on ob\over{j}{j}ects\hand{,}}','The phrase is typed, its j is pen-retraced and its comma is penned. The second apparent comma is the continuous placing-hook end, not separate punctuation.'],
 [r'\over{f}{F}or definin',r'\over{\unsure{f}}{F}or defining','The live F is penned over a partly obscured old letter; the final g of defining is visibly present at the clipped right edge.'],
 [r'\over{\illegible{1}}{W}',r'\over{\unsure{W}}{W}','A W-like older type impression is visible inside the pen W, but its lower strokes remain obscured.'],
 [r'R\inserted{in Q}',r'R \inserted[typed]{in Q}','In Q is typed above the line, and the whole phrase requires its visible separating space.'],
 [r'\hand{$\alpha=\alpha_{R}$}',r'\hand{\ensuremath{\alpha=\alpha_{R}}}','Remove nested dollar delimiters inside the display without changing the handwritten formula.'],
 ['order relatio\n','order relatio'+r'\unsure{n}'+'\n','The last n has only a clipped edge fragment; preserve that partial reading with doubt.'],
 [r'(\over{\unsure{*}}{1})',r'(\over{\unsure{*}}{2})','The live pen numeral has a curved top and broad lower horizontal foot: it is 2, not 1. Its old star-like layer remains doubtful.'],
 [r'\xout{\illegible{1}} objects',r'\xout{arrows} objects','Arrows is readable beneath the machine x row before the replacement objects.'],
 [r'sur\hand{j}ective',r'surjective','The j in this occurrence is a regular typed impression, without a separate pen replacement.'],
 ['\\uline{injectiv\non arrows}',r'\uline{injectiv\hand{e}'+'\non arrows}','The terminal e is written in pen at the clipped right edge.']
]
for old in [r'\mathrm{Fl}$(M)',r'\mathrm{Fl}(M)']:
 # Record each visible occurrence separately.
 for i,line in enumerate(src.splitlines(),1):
  if old in line:
   # Other edits do not touch these lines except the order-relation line.
   before=line;after=line.replace(old,r'F\over{l}{\ell}$(M)' if '$' in old else r'F\over{l}{\ell}(M)')
   edits.append(['\n'+before+'\n','\n'+after+'\n','The typed l has an added oblique pen stroke; preserve the typed lower layer and handwritten ell form.'])
# The first diagram has typed objects and labels with hand-drawn curved arrows.
edits.append([r'\hand{(1)} \diagram{\begin{tikzcd} Q \arrow[r, bend left, "r"] & L \arrow[l, bend left, "s"] \end{tikzcd}}',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\hand{(1)} \diagram{\begin{tikzcd} Q \arrow[r, bend left, "r", color=blue] & L \arrow[l, bend left, "s", color=blue] \end{tikzcd}}','Both curved arrows are drawn in pen. The Q, L and r, s labels are typed; topology is unchanged.'])
save_review({'key':key,'edits':edits,'diffs':{
 3826:['having same objects','There is no typed the between having and same.'],
 3827:['let Q(M)=Q the set','There is no be after the equality.'],
 3828:['iff u(f) is invertible','The typed variable is u, not i, and iff has two f letters. Retain the source variable slip.'],
 3830:['for simplicity I write','I is the ordinary typed pronoun.']
 },'unsure':[
 [r'\over{\unsure{*}}{2}','The live numeral is 2; the obscured old star-like sign remains doubtful.'],
 [r'\unsure{\'s}','The pen zigzag clearly cancels material after Q, but its lower apostrophe/s reading remains obscured.']
 ],'illegible':[
 [r'\unsure{W}','A W-like lower impression is visible but not sufficiently separated from the pen strokes for a settled reading.'],
 [r'\illegible{1}','The machine-cancelled and pen-scribbled formula/word before alpha cannot be read securely.'],
 ['arrows','The old arrows is readable beneath the x row.']
 ],'notes':[
 'The first a-item has a typed capital H beneath the pen h, as encoded.',
 'The parenthesis, t in it and ill in will are penned or retraced. The final t of not is also visibly handwritten.',
 'Whether has pen h/e retracing; such retains its pen s; The first has upper/lower h marks. The later surjective j is typed.',
 'The lower cell in s(W) suggests W but remains doubtful under its pen retracing.',
 'The material before alpha is covered by both machine strikes and pen scribbling; its illegibility remains.',
 'The mark after Q has a clear cancellation zigzag, with the older apostrophe/s still doubtful.',
 'Now start with is an independently typed and machine-cancelled half-line between the two surrounding lines.',
 'The printed l in Fl is crossed by an oblique pen stroke. Each occurrence is now represented with both layers.',
 'Defining retains a visible final g at the edge; relation has only a doubtful final n fragment; injective ends in a clear penned e. Sam and the following me, and clear/ly, are kept as visible.',
 'The archive folio 38 is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_038:variable','before':'i: M to M-prime; iff u(f) is invertible','after':'i: M to M-prime; iff u(f) is invertible','line':22,'decision':'retain author notation','reason':'The defined functor is i but the later invertibility condition visibly uses u. Preserve this mathematical variable slip and flag it in the guide.'},
 {'source_id':'OBS:ps_134-4_038:cross_reference','before':'In terms of (1)','after':'In terms of (2)','line':39,'decision':'correct transcription','reason':'The scan numeral is 2, referring to the displayed comparison functor. A separate earlier reference still literally reads (*).'}
 ],'evidence':'Both original halves, sixteen enlarged panels and four additional edge/insertion panels inspected. The M- prefixes and in Q are typed above the line. It will and whether have pen retracing; The first has the recurrent upper/lower h marks. Injective on objects has a penned j and comma, while its supposed second comma is a continuous hook end. All Fl occurrences retain typed l with an added oblique pen stroke. The old W-like cell and the scribbled material before alpha remain doubtful/unreadable. Arrows resolves beneath machine cancellation. The live reference numeral in In terms of is 2, not 1. The scan retains u(f), the absent article and absent be. Defining has a visible edge g; relation has only a partial n; injective ends with a penned e. Both curved diagram arrows are handwritten, with typed labels. The nested math delimiters in alpha are repaired mechanically.'})

key='ps_134-4_039';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[
 [r'\unsure{f}',r'\unsure{\over{f}{f}}','The clipped extra cell has a typed f-like impression with heavier superposed ink. No secure independent cancellation removes it.'],
 [r'In \unsure{this}',r'In th\over[typed]{\unsure{e}}{i}s','The live word is this, with typed i over a doubtful earlier e-shaped cell.'],
 [r'L\deleted{\unsure{$_0$}} int',r'L\deleted{$_0$} int\hand{\unsure{o}}','The cancelled subscript is a visible round zero. At the clipped edge, a penned rounded stroke suggests the final o of into but is only partly visible.'],
 [r'general,\deleted{\illegible{1}}',r'general,\deleted{f}','The old f is visible beneath a diagonal pen cancellation.'],
 [r'\over{\illegible{1}}{$G\'$}',r'\over{\unsure{G}}{$G\'$}','A G-like lower type impression survives, but its exact form remains uncertain under the new G-prime.'],
 [r'\xout{\illegible{1}} map',r'\xout{canonical} map','Canonical is legible beneath the machine x row.'],
 [r'\over{\illegible{1}}{G\'}',r'\over{\unsure{G}}{G\'}','The old lower capital resembles G but is too heavily overwritten for certainty.'],
 ['We may describe $Q_0$ and $L_0$',r'We may describe $\over{Q}{Q}_0$ and $\over[typed]{L}{L}_0$','Q is pen-retraced; L has repeated typed impressions.'],
 ['definitionsof $Q_0$',r'definitionsof $\over{Q}{Q}_0$','The Q in the parenthetical is retraced in pen.']
]
edits=[[(v.replace("\\'","'") if isinstance(v,str) else v) for v in e] for e in edits]
# Preserve each ell provenance separately by complete original line.
for line in src.splitlines():
 if r'F\ell(M)' in line:edits.append(['\n'+line+'\n','\n'+line.replace(r'F\ell(M)',r'F\over{l}{\ell}(M)')+'\n','Each typed l has an oblique pen addition forming ell; preserve that lower layer.'])
save_review({'key':key,'edits':edits,'diffs':{
 3850:['isomorphism','The noun is singular, with no final s.'],
 3856:['In this general','The live typed word is this; its i has an older doubtful e-like layer.'],
 3859:['W = r(R)','The variable is a clearly typed r.'],
 3861:['general, followed by a pen-cancelled f','The extra old f is visible under the pen slash, and is retained as a deletion.'],
 3862:['with just one object','The source types with, not which.'],
 3865:['we may take, with may underlined','The pen underline lies beneath may and is retained.'],
 3870:['need not be surjective','The final t of not is visibly typed.']
 },'unsure':[
 [r'\unsure{\over{f}{f}}','The clipped extra f-like cell has superposed dark ink; neither a secure live replacement nor a full cancellation is established.'],
 [r'\unsure{sur}','The lower cells beneath inj remain partly obscured; sur stays tentative.'],
 [r'th\over[typed]{\unsure{e}}{i}s','The live word this resolves, while the earlier cell under i remains doubtful.'],
 ['$_0$','The round subscript under the diagonal cancellation is visible.'],
 [r'\unsure{s}','The last s is clipped by the page edge.'],
 [r'\unsure{sur}','The lower three-cell run is partly hidden by pen rewriting; the candidate sur remains tentative.']
 ],'illegible':[
 ['f','The old cell has the f stem and crossbar beneath the diagonal strike.'],
 [r'\unsure{G}','A G-shaped old impression is plausible but not securely separable from the handwritten G-prime.'],
 ['canonical','The complete old canonical can be followed through the x strikes.'],
 [r'\unsure{G}','The overwritten old capital has a G-like outline, retained with doubt.'],
 [r'\illegible{1}','The small cancelled run after then is densely overtyped and scribbled, leaving no secure reading.']
 ],'notes':[
 'The clipped extra f-like cell has dark overlaid ink. Its reading/layer uncertainty remains; no deletion is imposed.',
 'Both old sur candidates beneath pen corrections remain doubtful; the live inj/in readings are clear.',
 'This is legible with a typed i over a doubtful old cell. The cancelled L subscript resolves as round zero; into has a clipped pen o, and Thus ends with a clipped doubtful s.',
 'The pen-cancelled extra f after general resolves. The small run after then remains illegible.',
 'The lower-left 39 is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_039:monoid_tests','before':'The stated monoid examples and comparison tests','after':'The stated monoid examples and comparison tests','line':31,'decision':'retain author argument','reason':'Failure of injectivity of the comparison M_W to M_R tests whether R is in Q_0; failure of surjectivity of M_R to M_W tests whether W is in L_0. The prose applies these observations to differently named preceding claims. The guide qualifies the examples without changing the manuscript.'},
 {'source_id':'OBS:ps_134-4_039:map_letter','before':'r maps Q into L_0 or L into Q_0','after':'r maps Q into L_0 or L into Q_0','line':28,'decision':'retain author notation','reason':'The second direction would involve s, not r, but no separate s is typed in the source sentence. The visible wording is retained.'}
 ],'evidence':'Both original scan halves and ten enlarged panels inspected. The extra f-like right-edge cell remains doubtful with its ink layer. The corrected inj and in are clear but their old sur candidates remain obscured. This resolves as the live word with a typed overprint at i. The cancelled round subscript resolves, while the edge o of into and s of Thus remain partial. The cancelled f after general and the old canonical under machine strikes resolve. Both old G-like layers remain uncertain, and the short cancelled run after then is unreadable. The formulas visibly use r(R), the noun is singular isomorphism, and the source has with and not. The manuscript monoid arguments and the r/s direction wording are preserved and specifically flagged for guide qualification.'})
