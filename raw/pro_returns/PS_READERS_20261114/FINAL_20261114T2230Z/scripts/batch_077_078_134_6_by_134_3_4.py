import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-6_077'
sep=r'\ensuremath{\diagram{\begin{tikzpicture}[baseline=-.3ex,x=1em,y=1ex]\draw[color=blue,line width=.4pt] (0,-.7)--(.55,2.3);\end{tikzpicture}}}'
edits=[
 [r'\inserted{functors}',r'\inserted[typed]{functors}','Functors is regularly typed above the line; the pen curve places it before the machine-cancelled maps.'],
 [r"map\hand{s}''",r"map\over{s}{s}\unsure{''}",'The pen s overlies a visible regular typed s. The closing quotation strokes reach the clipped right edge and their complete pair remains uncertain.'],
 ['Thus, the',r'Thus, \over{t}{t}he','The t has a separate thick pen retracing over its typed form.'],
 [r'$A^{\wedge}$\hand{/}may',r'$A^{\wedge}$'+sep+' may','The long oblique pen stroke is a graphic separator, not a textual division slash; retain it inline.'],
 ['by adding',r'by \over[typed]{q}{a}dding','The a overlies a regular q-like lower bowl and descender.'],
 [r'\inserted{perchance} \deleted{already}',r'\inserted[typed]{perchance} already','Perchance is typed. The curve above already is continuous with its two placing hooks and does not independently cancel the live word.'],
 ['which by prop.3 can be',r'which by prop.3 \over[typed]{i}{c}an be','The c has an older typed i stem and dot beneath it.'],
 [r'\uline{presheaves} on A',r'\uline{presheaves} o\unsure{\over[typed]{f}{n}} A','The n has an overlapping tall f-like impression. Preserve the uncertain order under a scoped typed-layer doubt.'],
 [r'for the topos\inserted',r'for the topos \inserted','Preserve the word boundary before the separately inserted script A.'],
 ['may be viewed as a particular',r'\over{may}{may} be viewed as a particular','All three letters of may have thick pen retracing over visible typing.'],
 [r'\deleted{\xout{Corollary \illegible{1}}}',r'\deleted{\xout{Coroll\unsure{ary} \illegible{1}}}','The initial Coroll is recoverable beneath the machine row. The last three letters remain partly obscured by the pen scribble, and the following old label remains unreadable.']
]
save_review({'key':key,'edits':edits,'diffs':{
 8391:['may, typed interlinear perchance, live already, exist','The pen stroke above already joins the downturned left hook and upturned right hook of the insertion. There is no independent cancellation of already.','correct transcription; placing curve'],
 8394:[r'F\mapsto F\circ\varepsilon_A{}^o','The second F and composition circle are plainly typed and must not be omitted as in the witness.'],
 8405:[r'\deleted{\xout{Coroll\unsure{ary} \illegible{1}}}','Both the machine cancellation and the additional pen scribble are visible. The obscured ending and following label remain doubtful/unreadable.'],
 8389:['typed interlinear functors','The raised word has regular typewriter forms; its placing curve is handwritten.','correct provenance'],
 8390:['pen s over typed s; clipped closing quotation marks','A lower typed s survives to the right of the heavy pen s. The complete closing quote pair is clipped.','correct layers and retain doubt'],
 8392:['typed interlinear perchance','The word is typed and the curved pen stroke is only a placing mark.','correct provenance'],
 8401:[r'\over{the}{an}','The handwritten an overlies the typed the; the existing layer reading is supported by the enlarged patch.']
 },'illegible':[
 [r'\illegible{1}','The final old label after the crossed Corollary run is covered by the pen scribble and cannot be securely named.']
 ],'notes':[
 'The final s of maps is pen retracing over a visible typed s. The closing quote marks run into the clipped edge and remain tentative.',
 'Perchance is typed. Its placing curve is continuous across the tops of already and has no separate cancelling stroke; already remains live.',
 'The old Corollary run has both machine x marks and pen scribbling. Coroll is recoverable, ary remains tentative, and the following label is unreadable.',
 'Both the mapsto and the later right arrow in (38) are visibly pen-drawn, with thick irregular shafts and arrowheads. Their existing hand provenance is retained.',
 'The new an is written in pen over the typed the, as originally encoded.',
 'The pencil archive folio 77 is visible at lower left.'
 ],'evidence':'Both original halves and thirteen enlarged panels inspected. Functors and perchance are typed interlinear additions. The placing curve for perchance does not delete already; its two hooks and continuous middle stroke are distinguishable. The final maps s is penned over a typed s and the closing quotes are clipped. Thus the has a pen-retraced t, adding has typed a over q, and can has typed c over i. The on patch has overlapping n/f-like impressions whose order remains doubtful. May at the left margin is retraced in pen. The slash-like mark after A-hat is reconstructed as an inline pen graphic. The two arrows in38 are penned, while the second F and composition circle are typed and fully present. An over the is confirmed. The crossed heading at39 has machine and pen cancellation layers, with a partially doubtful word ending and an unreadable following label. The superscript circle and comma on the last B expression are handwritten as encoded. The literal interprete, semicolon and Than remain. The page identifies the free completion under direct limits, its dual inverse-limit version, and the resulting cosheaf/sheaf equivalence for M with both kinds of small limits.'})

key='ps_134-6_078'
edits=[
 [r'-valued \uline{sheaves}',r'-val\unsure{\over[typed]{a}{u}}\over[typed]{e}{e}d \uline{sheaves}','The u/e region has overlapping regular impressions: the old first cell is a-like but its order remains doubtful, and the following e has a repeated e impression.'],
 [r'\unsure{;|,}',r'\hand{,}','The separator is a single lower pen comma. There is no independent upper dot to make a semicolon.'],
 [r'\arrow[dr, "\hand{$\approx$}"]',r'\arrow[dr,color=blue, "\hand{$\approx$}"]','The left diagonal arrow is hand-drawn; only the arrow receives hand provenance, leaving the typed parts of its objects plain.'],
 [r'''\arrow[dl, "\hand{$\approx$}"']''',r'''\arrow[dl,color=blue, "\hand{$\approx$}"']''','The right diagonal arrow is hand-drawn; its topology and label are unchanged.'],
 [r'\diagram{\begin{tikzcd}', '% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+r'\diagram{\begin{tikzcd}','Record the diagram provenance comment and its line boundary as nonverbal metadata.'],
 [r'\uline{\unsure{Remark|Rgmark}.}',r'\uline{R\unsure{\over[typed]{g}{e}}mark.}','The e/g cell has a clear lower g loop and overlapping e shape. Preserve layer-order uncertainty in that cell rather than the entire heading.'],
 [r'\deleted{\hand{(\illegible{1}}}',r'\deleted{\hand{\unsure{$(\delta_{\illegible{1}}^{\mathcal M})^\circ$}}}','The crossed pen formula retains an opening parenthesis, a delta-like stem, raised M-like strokes and a right-hand circle. Its lower label remains unreadable and the whole reconstruction is tentative.'],
 [r"\hand{$(\delta^{\mathcal{M}}_{A})$}^{\unsure{\circ|'}}",r'\hand{$(\delta^{\mathcal{M}}_{A})^{\circ}$}','The raised mark is a small closed handwritten circle, not a prime; move its provenance inside the handwritten formula.'],
 [r'\text{Where }',r'\text{\over[typed]{w}{W}here }','A regular uppercase W lies above the lower lowercase w impression.'],
 [r'th\unsure{\over{i}{e}}s',r'th\unsure{\over[typed]{i}{e}}s','The i/e patch has regular typewriter forms. The order remains uncertain, so preserve the complete layered doubt.'],
 [r'\uline{canonically}',r'\uline{canonicall\unsure{\illegible{1}}y}','Both l cells are clear, followed by a separate fully blackened cell before y. No particular old character or independent cancelling stroke is recoverable; preserve the extra unreadable material rather than silently deleting it.'],
 [r'\xout{\illegible{1}}',r'\unsure{\illegible{1}}\xout{\illegible{1}}','Two separate cells follow equivalence: a dense left ink patch with no secure independent cancellation boundary, then a regular machine x over unreadable material. Preserve both with their different visible status.'],
 [r'equ\unsure{\xout{m}}ivalence',r'eq\unsure{\over[typed]{m}{u}}ivalence','The u/m impressions overlap within one type area and no independent x strike is visible. Retain uncertain typewriter layer order instead of a separately cancelled m.'],
 [r'\inserted{Case}\deleted{(}',r'\inserted{Case}','The apparent opening parenthesis is the left hook of one continuous placing curve under Case, not an independently typed character.'],
 [r'1\textsuperscript{o}).',r'\over{1}{1}\textsuperscript{\uline{o}}).','The 1 is retraced in pen over typing, and the small typed o has a separate underline.'],
 [r'\xout{(41)xas}',r'\xout{(41) as}','The x in the space between (41) and as is a machine cancellation impression, not a textual letter.'],
 [r'\unsure{formula|fbrmula}',r'f\unsure{\over[typed]{b}{o}}rmula','The affected cell has regular b/o impressions. Keep their order doubtful rather than supply a clean word.']
]
edits.append([r'\inserted{Case}',r'\inserted{\uline{Case}}','A separate short pen underline lies directly beneath Case, above the longer continuous placing curve; preserve both the underlining and insertion.'])
save_review({'key':key,'edits':edits,'diffs':{
 8411:[r'\hand{$(\delta_A^{\mathcal M})^\circ$}','The raised mark is a closed handwritten circle. The witness prime does not match the visible shape.','settled on image'],
 8421:['The two inner Hom arguments remain blank','The source has only the two blank slots and their separating comma. The witness supplied arguments are absent.'],
 8409:['Both diagonal arrows are handwritten','Both arrows have irregular pen shafts and heads. Their typed objects remain plain; the approximate-equivalence labels retain their hand provenance.','correct provenance'],
 8412:[r'\over[typed]{w}{W}here','The capital W overlies a regular lower w.','record typed layers'],
 8415:['Handwritten Case and continuous placing curve; no old opening parenthesis','The left hook and right arc are parts of a single curve. No separate opening parenthesis is visible to cancel.','correct placing mark']
 },'unsure':[
 [r'\hand{,}','A single low comma is visible and no separate upper dot is present.'],
 [r'R\unsure{\over[typed]{g}{e}}mark','Both e and lower g forms are visible, but their layer order is not secure.'],
 [r'\hand{\circ}','The small raised mark is a closed pen circle.'],
 [r'\unsure{\over[typed]{i}{e}}','Both impressions are regular typing; the i/e order remains doubtful.'],
 [r'\unsure{\over[typed]{m}{u}}','The u/m forms occupy the same type area and there is no separate machine x cancellation.'],
 [r'f\unsure{\over[typed]{b}{o}}rmula','The b/o overlap is visible but the final layer cannot be securely settled.']
 ],'illegible':[
 [r'\deleted{\hand{\unsure{$(\delta_{\illegible{1}}^{\mathcal M})^\circ$}}}','Some outer formula strokes become recoverable, but the lower label remains unreadable under the crossing strokes.'],
 [r'\unsure{\illegible{1}}\xout{\illegible{1}}','The enlarged run contains two cells with different visible ink status; neither underlying reading resolves.']
 ],'notes':[
 'The u/e region of valued is overprinted. The older first cell is a-like under u but remains uncertain; the e has a repeated regular impression.',
 'The Remark e/g cell has both a lower g loop and an overlapping e form. Its order remains doubtful.',
 'The right-hand diagram separator resolves as a pen comma, with no independent dot above it.',
 'The cancelled pen formula retains delta/M-like and circle strokes, but the lower label is unreadable; the entire proposed formula is kept tentative.',
 'The this/thes patch is a doubtful typed i/e overlap. Canonically contains a distinct unreadable extra cell after its two l cells, with no secure cancellation. The end-of-line run has a dense unreadable left cell and a separately machine-cancelled unreadable right cell.',
 'The supposed cancelled m is an overlapping u/m type impression occupying the same cell area. No independent x is visible; order remains doubtful.',
 'Formula has a regular b/o overprint whose order remains uncertain.',
 'The pencil archive folio 78 is visible at lower left.'
 ],'evidence':'Both original halves, thirteen enlarged panels and five supplemental panels inspected. The u/e region of valued is overprinted. Diagram40 has two handwritten arrows and handwritten definitional additions, with the typed parts of Hom objects left plain; its right separator is a pen comma. The Remark e/g patch remains an uncertain typed overlay. The crossed pen formula yields tentative delta, M and circle strokes but no readable lower label. The live duality superscript on39prime is a closed handwritten circle, and Where has typed W over w. The this/thes overlap is typed and its order remains doubtful. Two l cells in canonically are plainly present before an additional fully blackened cell; independent inspection confirms that a specific reading or cancellation cannot be established. The following end-of-line patch covers two cells, only the right showing a clear regular machine x. The u/m patch in equivalence has no independent x strike and remains a doubtful typed overprint. Case has a separate short underline and a longer continuous placing curve with no separate opening parenthesis, independently confirmed; the digit1 is pen-retraced and the small o is underlined. The extra x in cancelled (41) as occupies a blank. The final b/o patch stays doubtful, and both inner Hom arguments at the bottom are genuinely blank. No mathematical completion or grammatical normalization is introduced.'})

for key in ['ps_134-6_077','ps_134-6_078']:
 s=(OUT/'checked_pages'/f'{key}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);level=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  level+=1 if m.group()=='{' else -1
  assert level>=0,(key,m.start())
 assert level==0,(key,level)
