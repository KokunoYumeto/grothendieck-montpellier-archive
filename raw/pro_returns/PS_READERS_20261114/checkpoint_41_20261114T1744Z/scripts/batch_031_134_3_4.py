import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_031';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');edits=[]
def e(a,b,r):edits.append([a,b,r])
for no in [8,11,17,20,33,50]:
 a=s.splitlines()[no-1];b=a.replace(r'\subset',r'\hand{\subset}').replace(r'\to',r'\hand{\to}').replace(r'\mapsto',r'\hand{\mapsto}').replace(r'A^{\wedge}',r'A^{\hand{\wedge}}')
 e(a,b,'The subset/arrow and hat strokes in this line are handwritten additions to typed formula characters; their topology and direction are retained.')
e(r'\inserted{$F$:}',r'\inserted[typed]{$F$:}','The F and colon above the functor line are typed, with a pen placement curve.')
e(r'\xout{\unsure{model}}',r'\xout{``model}','The enlarged cancellation resolves model and also shows its earlier opening double quotation marks under the first x.')
e(r'\xout{with the}',r'\deleted{\xout{with the}}','A horizontal pen stroke crosses the already machine-cancelled with the.')
for sym in [r'\Delta',r'\square']:
 a='\\margin{$'+sym+r'^\wedge$ (circled)}'
 b='\\margin{\\diagram{\\begin{tikzpicture}[baseline=(n.base)]\\node[draw,ellipse,inner sep=3pt] (n) {$'+sym+r'^\wedge$};\end{tikzpicture}}}'
 e(a,b,'The margin contains the hatted symbol inside a drawn oval; replace the editorial word circled with the actual oval diagram.')
# Both diagrams mix typed objects and handwritten connectors.
a=s[s.index(r'\diagram{\begin{tikzcd}'):s.index(r'\end{tikzcd}}')+len(r'\end{tikzcd}}')]
b=a.replace(r'\arrow[',r'\arrow[color=blue, ')
e(a,'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+b,'All three arrows of the triangle are handwritten, whereas M, M prime, F and Hot are typed.')
start=s.index(r'\diagram{\begin{tikzcd}',s.index(r'\end{tikzcd}}')+1);end=s.index(r'\end{tikzcd}}',start)+len(r'\end{tikzcd}}');a=s[start:end];b=a.replace(r'\arrow[',r'\arrow[color=blue, ')
e(a,'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+b,'All six connectors of the modelizer diagram are handwritten, including both inclusion hooks; labels already marked hand remain so, typed category names stay plain.')
conf=dict(key=key,edits=edits,diffs={
1962:['sinply','The enlarged right-edge word has n, not m; retain the typescript spelling.'],
1963:[r"\hand{(28')}",'Only the call28-prime is handwritten after the localization functor in a); the witness explanatory footnote is not on the page.'],
1965:[r'\inserted[typed]{$F$:}','The inserted F colon is typewritten, with a pen placement stroke.','correct provenance'],
1966:['either of the two following equivalent conditions','The typed two is present before following.'],
1970:[r'so far\hand{,}','A dark comma-like pen mark appears after far, before the note29 call.'],
1971:[r'\hand{(29)}','Only the call29 is present; no text of the witness footnote occurs in this margin.'],
1976:[r'\hand{$\square$}','The body cubical symbol is a heavy square; its separate hatted spelling is drawn in the margin. No additional distinct hat is supplied to the body from the witness.'],
1978:['Two oval-enclosed hatted symbols, Delta and square','The margin shows actual circled or oval-enclosed symbols, now drawn as such instead of described by the word circled.','correct transcription']},
unsure=[[u[0][0],'The o area in Mod has an additional upper arc and possible retouch; its original/overwritten character remains uncertain.'],['model','The enlarged cancelled letters resolve model; an earlier opening quote is also visible.']],
illegible=[],notes=[
'The Mod o area was enlarged; an extra upper arc makes its overwritten state uncertain, so the existing doubt is retained.',
'The initial s in satisfying and h of the/the diagram are visibly retouched or overtyped, but the words are legible and unchanged.',
'The enlarged cancelled group resolves an opening quote and model; the uncertainty is removed on the image.',
'The M in simply M is a bold pen form; the existing handwriting markup is retained.',
'The comma and call29 are penned; with the has both machine x strokes and an additional pen cancellation, now recorded.',
'Both inclusion hooks and the four following arrows of the large diagram are pen; all six receive handwritten-arrow coloring. The two margin ovals are reconstructed.'],
evidence='Both halves inspected, plus enlarged sinply, Mod, cancelled model and the upper diagram symbol. The spelling sinply is definite. The Mod letter remains uncertain because an upper arc overlaps the round o. The old quoted model is recoverable beneath x strokes. The F colon insertion is typed, whereas subset signs, ordinary formula arrows, all three triangle arrows and all six modelizer-diagram connectors are hand drawn. The upper branch has a hatted Delta, the lower a heavy square, and the margin contains separate oval-enclosed hatted symbols; those ovals now replace editorial prose placeholders. Simply M is pen, and with the has a pen stroke over its typewriter cancellation. Calls28-prime and29 occur without their expanded witness notes.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
