import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_012';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line
 for sym in [r'\to',r'\sim']:
  new=new.replace('\\hand{$'+sym+'$}',r'\hand{\ensuremath{'+sym+'}}')
 if new!=line:edits.append([line,new,'Use ensuremath for handwritten arrows and tildes already occurring within math mode; this is a mechanical repair with no reading change.'])
diag=r'\[ I \ = \ \diagram{\begin{tikzcd}[row sep=small, column sep=small] e_0 \arrow[dr] & \\ & e_2 \\ e_1 \arrow[ur] & \end{tikzcd}} \qquad , \]'
newdiag='% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+r'$I = $ \diagram{\begin{tikzcd}[row sep=small, column sep=small] e_0 \arrow[dr,color=blue] & \\ & e_2 \\ e_1 \arrow[ur,color=blue] & \end{tikzcd}} $\qquad ,$'
edits += [
 [r'\xout{withxxixx}',r'\xout{with it\illegible{1}}','The old letters with it are visible under the x row; the last cancelled cell cannot be read.'],
 [diag,newdiag,'The two arrows are penned, the three objects typed. Remove the redundant outer math environment around the diagram wrapper while preserving the displayed relation and topology.'],
 [r'\xout{fx}',r'\xout{fi\illegible{1}}','The first two old letters f and dotted i survive at the clipped edge; the continuation is not recoverable.'],
 [r'Hom(\deleted{\illegible{1}}X,Y)$_{\underline{I}}$',r'$\mathrm{Hom}_{\deleted{\illegible{1}}}(\over[typed]{X}{X},Y)_{\underline{I}}$','The cancelled mark is a subscript beneath Hom, not text inside the parenthesis. Two vertically displaced typed X impressions survive beside it.'],
 ['category $M_I$ having',r'category $M_{\underline{I}}$ having','This first subscript I is visibly underlined.'],
 ['object of $M_I$),',r'object of $M_{\underline{I}}$),','The subscript here bears a separate pen underline.'],
 ['final object of $M_I$ .',r'final object of $M_{\underline{I}}$ .','The next subscript also has a separate underline.'],
 [r'\unsure{isomorphims|isomorphisms}','isomorphims','The handwritten ending reads i-m-s after h; no s is present between i and m. Preserve the spelling diplomatically.'],
 [r'\xout{thexcompx}',r'\xout{the compo}','The cancelled letters read the compo, including the last rounded o.'],
 [r'\xout{thisx}',r'\deleted{\xout{\unsure{this}\illegible{1}}}','Both machine x strikes and a pen stroke cross the old fragment. This is tentative, and the final old cell is unreadable.'],
 [r'\xout{MxxxHx}',r'\deleted{\xout{$M\ \illegible{1}\ H\illegible{1}$}}','The old M and H are readable, but the intervening and following cells are not. The fragment has both machine and pen cancellation.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3338:['Paragraph break before Returning to general M','The new paragraph is distinct on the scan.'],
 3341:['their compositions with','The plural s is present.'],
 3342:['having same objects as M','The source has no article the.']
 },'unsure':[['isomorphims','The pen ending is i-m-s; the extra s of normal isomorphisms is absent.']],
 'illegible':[[r'\illegible{1}','The first subscript is hidden beneath a dense pen blot; its underline survives but its letter is not securely recoverable.'],[r'\illegible{1}','The second subscript is similarly covered. It precedes the parenthesis and is distinct from the two typed X impressions.']],
 'notes':[
 'Both old Hom subscripts are pen-cancelled beyond secure identification. The second is repositioned below Hom, and the displaced old X is separately retained.',
 'The handwritten word reads isomorphims. Its spelling is retained in every form; the allowance for isolated typing slips does not apply to this pen insertion.',
 'All formula arrows and tildes are penned. Their nested math delimiters are repaired mechanically; the two diagram arrows receive the shared blue style.',
 'The first M_I and the two final-object occurrences have visible separate underlines. The two intervening occurrences in the object-isomorphism sentence do not visibly have one and remain plain.',
 'The cancellations now distinguish recoverable with it, fi and the compo from unreadable cells. This is tentative beneath both machine and pen strokes; M and H are clear in the final cancelled fragment, but the other cells remain unreadable.',
 'The lower-left 12 is handwritten.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_012:isomorphims','before':'isomorphims','after':'isomorphims','line':33,'decision':'retain handwritten spelling','reason':'This is a pen insertion, so the permitted correction of isolated typing slips does not apply. The earlier proposed master correction is withdrawn; literal isomorphims remains in every form.'}],
 'evidence':'Both original halves and eight enlarged panels inspected. The interval diagram has typed e-nodes and two handwritten arrows. Formula arrows and tildes are penned; nested math is repaired. The two old Hom subscripts remain unreadable under pen blots; the second is below Hom and has an adjacent vertically repeated typed X. Underlining of M_I is preserved occurrence by occurrence. The pen insertion explicitly reads isomorphims. The cancellation fragments retain only recoverable letters, with unreadable cells marked, and distinguish machine strikes from later pen cancellation. The source paragraph break and plural compositions are retained.'})

key='ps_134-4_013';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\rightrightarrows',r'\hand{\rightrightarrows}').replace(r'\to',r'\hand{\to}').replace(r'\subset',r'\hand{\subset}').replace(r'\in',r'\hand{\in}')
 # Restore macro names beginning with in; only the relation is a token.
 new=new.replace(r'\hand{\in}serted',r'\inserted')
 new=new.replace(r'\xrightarrow{\ \sim\ }',r'\hand{\xrightarrow{\ \sim\ }}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows, membership signs, inclusion and isomorphism arrow are drawn in pen.'])
BRACKET=r'\margin{\diagram{\begin{tikzpicture}[x=1ex,y=1ex]\draw (0,0) .. controls (.5,-.1) and (.55,.4) .. (.65,1.3)--(.8,2.3) .. controls (1.3,2.2) and (1.8,2.2) .. (2.1,2.35);\end{tikzpicture}}}'
edits += [
 [r'\unsure{\mathrm{Fl}}',r'\mathrm F\over{\mathrm l}{l}','The second typed letter is l, with a long slanting pen retracing; no literal slash is substituted for the letter.'],
 [r'\unsure{of}',r'\over[typed]{i}{o}\over[typed]{n}{f}','The old i dot and n arch survive beneath typed o and f.'],
 [r'\margin{\unsure{$\ulcorner$}}',BRACKET,'Replace the tentative corner glyph by the actual long pencil bracket with curved lower end and short upper arm.'],
 [r'\unsure{Stride|stride}',r'\over[typed]{S}{s}tri\over[typed]{\unsure{l}}{d}\over{e}{e}','The initial S/s type overlap is clear; d has an older tall impression tentatively l, and e is traced in pen.'],
 [r'\inserted{saturation}',r'\inserted[typed]{saturation}','Saturation is typed above condition; the placing curve and following comma are penned.'],
 [r'\xout{xx}',r'\xout{we}','The old two letters w and e are readable beneath the x strikes.'],
 [r'\inserted{still more,}',r'\inserted{still more}','The apparent final comma is the upward end of the continuous insertion curve; no independent punctuation follows more.'],
 [r'\over{gf}{fg}',r'\over{gf}{gf}','The live handwritten letters are g then f: a closed loop with descender followed by the tall f stem and crossbar. Independent image review confirms this. Preserve the repeated gf despite the earlier correct statement gf and fg.'],
 [r'Y=Y_1\mathrm{x}Y_2 \quad ,',r'Y=Y_1\mathrm{x}Y_2 \quad \unsure{\mathrm n},','A very faint n-like impression appears before the comma. Its status as source text or offset trace is uncertain, so retain it doubtfully.'],
 [r'\xout{xxy}',r'\xout{any}','The old letters a-n-y, including the final descender, are readable.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3351:[r'\inserted{still more}','The apparent comma belongs to the insertion hook, not the words. The witness does not omit an independent comma here.','correct transcription'],
 3354:['if it satisfies','The source has a single f.'],
 3356:[r'gf,\over{gf}{gf}\in W','The live penned second composite is gf, not fg. The earlier version of c-prime on this page has gf and fg. Independent image reading confirms the repeated gf.','retain authorial formula slip'],
 3357:[r'\unsure{?} Thus','The mark has a separate dot and a dark angular upper body. It resembles a question mark, but possible overprinting prevents a secure reading.']
 },'unsure':[
 ['F with pen-retraced l','The typed l is visible under the long oblique pen stroke.'],
 ['of typed over in','The older i dot and n shoulder are visible.'],
 ['Reconstructed long pencil bracket','Its long sloping stem, lower turn and upper arm are visible.'],
 [r'\over[typed]{S}{s}tri\over[typed]{\unsure{l}}{d}\over{e}{e}','The live word is stride; the older d-cell impression remains uncertain.'],
 [r'\unsure{accasionally|occasionally}','The first rounded cell is heavily retouched; a versus o and the order of the layers cannot be securely separated.'],
 [r'\unsure{?}','The dark upper body is angular and layered; the independent lower dot is clear, but a clean colon or question mark is not securely established.']
 ],'notes':[
 'The second letter in Fl is a typed l with a slanting pen retracing, rather than a literal slash.',
 'The first word reads of typed over in, retaining both old letters.',
 'Stride has S/s overlap, a doubtful older tall cell under d, and pen retracing of e.',
 'The long pencil bracket is reconstructed graphically, with no editorial wording added to the manuscript.',
 'All is penned over the typed word and underlined; there is no separate deletion of the whole word.',
 'The mark after the quotient functor remains doubtful between question-mark-like and overprinted punctuation.',
 'The very faint n-like trace before the display comma is retained with doubt because its status cannot be established.',
 'The short horizontal stroke near The analoguous is the top bar of the product sign on the line below, not an independent word or annotation.',
 'The lower-left 13 is handwritten. The restriction to a finite indexing set is enforced by the pen cancellation of not necessarily.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_013:gf','before':r'gf,\over{gf}{gf}\in W','after':'Source repeated gf retained; compare earlier gf and fg on this page.','line':42,'decision':'retain mathematical slip for guide','reason':'The image confirms g followed by f in the handwritten second composite. The intended symmetric condition is stated correctly earlier, but the repeated version is not silently repaired.'}],
 'evidence':'Both original halves and twelve enlarged panels inspected. Fl has a pen-retraced l and of is typed over in. The pencil margin bracket is reconstructed. Stride has a clear live reading but uncertain older d-cell; the first letter of accasionally/occasionally remains unresolved. Saturation is typed interlinearly. The apparent comma after still more is only the placement hook. All is live pen retracing over type. Crucially, the second composite in the repeated c-prime condition is handwritten gf, independently confirmed; the source repetition is preserved despite the earlier correct gf/fg pair. The punctuation after the quotient functor and faint n-like trace before the display comma remain doubtful. The product-bar issue and final pen cancellation restricting to finite products are accounted for.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
