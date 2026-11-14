import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_032';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');ill=occurrences(s,'illegible');edits=[]
def e(a,b,r):edits.append([a,b,r])
a=s.splitlines()[10];b=a.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'A^\wedge',r'A^{\hand{\wedge}}').replace(r'\mapsto',r'\hand{\mapsto}').replace(r'\in',r'\hand{\in}')
e(a,b,'The j_A formula has hand-drawn arrow, hat, mapping arrow and membership sign among typed letters; the clipped end is retained without inventing a complete outer delimiter.')
for no in [14,17]:
 a=s.splitlines()[no-1];b=a.replace(r'\ar[',r'\ar[color=blue, ').replace(r'^\wedge',r'^{\hand{\wedge}}')
 e(a,'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+b,'Both arrows in this small diagram are hand drawn; the visible presheaf hats are hand strokes. The diagram itself is retained, including the one absent from the witness.')
e(r'\inserted{the vertices of}',r'\inserted[typed]{the vertices of}','The vertices of is typed above the line; the placement curve passes above this graph without deleting it.')
e(r'$A \subset A^\wedge$',r'$A \hand{\subset} A^{\hand{\wedge}}$','The subset sign and hat are handwritten.')
e(r'\[ n \mapsto \hand{\Delta}/\hand{\Delta}_n \]',r'\[ n \hand{\mapsto} \hand{\Delta}\hand{/}\hand{\Delta}_n \]','The mapping arrow and slash are penned; the slash remains on the baseline rather than moved to a subscript.')
e(r'\hand{$\Delta$}$^\wedge$ and \hand{$\square$}$^\wedge$',r'\hand{$\Delta^\wedge$} and \hand{$\square^\wedge$}','Both hats in the modelizer sentence are handwritten as are the underlying symbols.')
e(u[0][0],'ize','The enlarged overwritten word resolves handwritten i, z and e over ato, yielding modelizers.')
e(r'\inserted{each one}',r'\inserted[typed]{each one}','Each one is typed interlinear text.')
e(u[1][0],"it's",'The enlarged possessive shows a short raised apostrophe immediately after t; retain the source usage it\'s.')
e(r'\inserted{right}',r'\inserted[typed]{right}','Right is typewritten above adjoint, with a handwritten placement curve.')
e(u[2][0],r'\Delta','The second product factor is unmistakably triangular in the enlarged crop; retain Delta despite the cubical interpretation in the prose.')
e(r'\hand{\unsure{$\wedge$}}',r'\deleted{\unsure{x}}','The mark after the presheaf symbol is a crossed dark x-like character, not a separate hat. Its exact cancelled glyph remains uncertain.')
e(r'$T^\wedge_{p,q}$',r'$T^{\hand{\wedge}}_{p,q}$','The actual hat attached to T is handwritten and remains distinct from the following crossed mark.')
e(r'\[ T_{p,q} \longrightarrow',r'\[ T_{p,q} \hand{\longrightarrow}','The arrow into Ord is hand drawn.')
e(r'\deleted{\illegible{1}} : \text{(Cat)} \longrightarrow T^{\wedge}_{p,q}',r'\deleted{\hand{\illegible{1}$_{p,q}$}} : \text{(Cat)} \hand{\longrightarrow} T^{\hand{\wedge}}_{p,q}','The canceled handwritten symbol has a still-legible p,q subscript; its head remains illegible. The final arrow and T hat are penned.')
conf=dict(key=key,edits=edits,diffs={
1988:['Inline Cat-to-two-presheaf-categories diagram retained','The upper half visibly contains this two-branch diagram before which appear; it cannot be omitted with the witness.'],
1991:['or to every multioriented cube','The typed words are every and multioriented, not each and multiordered.'],
1992:[r'\inserted[typed]{the vertices of}','The insertion is typewritten and the original this graph remains live.','correct provenance'],
1994:[r'\hand{\Delta}\hand{/}\hand{\Delta}_n','The slash lies between the two Delta symbols on the line, not as a lowered /Delta_n subscript.'],
1997:[r'model\over{ato}{ize}rs','The enlarged pen correction resolves ize, producing modelizers where the witness retains modelators.','correct transcription'],
1998:[r'\inserted[typed]{each one}','The letters are typewritten above embodied.','correct provenance'],
1999:["all it's facettes",'The crop shows a raised apostrophe after t; retain the source spelling and possessive.','correct transcription'],
2003:[r'\inserted[typed]{right}','Right is typed interlinear text.','correct provenance'],
2007:[r'(\hand{\Delta})^p \hand{\times} (\hand{\Delta})^q','The two symbols are triangles; the second is not silently changed to a square even though the prose says q times cubical.','correct transcription'],
2010:[r'\deleted{\unsure{x}}','The following mark is a crossed x-like character, not an independent hat; the cancelled glyph remains doubtful.','correct transcription']},
unsure=[['ize','Enlargement resolves the handwritten replacement letters i,z,e.'],["it's",'The raised mark after t is an apostrophe.'],[r'\Delta','The second factor is a closed triangle with sloping sides.'],[r'\deleted{\unsure{x}}','The old mark looks x-like under cancellation, rather than like a hat; exact character remains uncertain.']],
illegible=[[ill[0][0],'The crossed head of the old final symbol is unreadable; its attached p,q subscript can be retained separately.']],
notes=['At the clipped right edge, the Cat closing parenthesis is visible and there is a small lower stroke; no secure complete extra outer delimiter can be reconstructed.','This graph is not struck: the insertion curve runs above it, and the typed addition the vertices of precedes it.','The pen letters over ato resolve to ize, giving modelizers.','The enlarged word has a raised apostrophe after t: it\'s.','The second product symbol is a triangle, not the square suggested by the prose; this authorial mismatch will be discussed in the guide.','The actual T hat is clear; the following mark is crossed and x-like, left doubtful. The last canceled symbol retains readable p,q but an illegible head.'],
evidence='Both halves inspected, with crops of modelizers, it\'s, the mixed-product formula and crossed mark, the final overwritten alpha area, and the clipped top-right line. The source says every multioriented cube; the slash in Delta/Delta_n is on the baseline. The vertices of, each one and right are typed additions, while (i.e. “are” not) is handwritten. This graph remains live. The corrected modelizers and apostrophe in it\'s are now resolved. Both product factors are visibly Delta, despite q times cubical in the prose. The presheaf hat over T is separate from a following canceled x-like mark, whose exact character remains doubtful. The final canceled symbol retains a readable p,q subscript but an illegible head. Both small diagrams and their arrows have been retained and their hand-drawn provenance marked.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
