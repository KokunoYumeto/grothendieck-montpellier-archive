import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_006';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'\to',r'\hand{\to}').replace(r'\Longrightarrow',r'\hand{\Longrightarrow}').replace(r'A_{/i^*(x)}',r'A_{\hand{/}i^*(x)}')
 if new!=line:edits.append([line,new,'The arrows, presheaf carets and category-of-elements slash are drawn in pen.'])
JOIN=r'implic\hand{\ensuremath{\smile}}ation'
DOUBLE=r'\margin{\diagram{\begin{tikzpicture}[x=1ex,y=1ex]\draw (0,0)--(.2,9);\draw (.5,0)--(.45,9);\end{tikzpicture}}}'
edits += [
 [r'implic\hand{\unsure{$\smile$}}ation',JOIN,'A clear shallow pen joining curve runs from the c toward the a. Preserve its graphic; the master variant applies the join.'],
 [r'\xout{\unsure{condition a(iv}}',r'\xout{condition a(iv)}','The old line is readable as condition a(iv), including its inner closing parenthesis, beneath the machine x row. The outer closing parenthesis remains separate.'],
 [r'The proof',r'T\over[typed]{H}{h}e proof','The H and h share the same type cell.'],
 [r'setting\hand{\unsure{,}}',r'setting\xout{\unsure{,}}','The extra character after setting is a regular typed x, cancelling an uncertain earlier punctuation mark; it is not a handwritten comma.'],
 [r'\margin{||}',DOUBLE,'Replace two text bars by the two long slightly slanted pen lines beside the paragraph.'],
 [r'\uline{existence}',r'\uline{existen\over{c}{c}e}','The c is traced again with pen above the underlining.'],
 [r'demanded\inserted{beforehand!}',r'demanded \inserted{beforehand!}','Beforehand is a separate inserted word.'],
 [r'T\hand{h}e question',r'T\over{h}{h}e question','The handwritten h lies over an identifiable typed h.'],
 [r'\hand{\unsure{$\smile$}}comes',r'\hand{\unsure{.}}comes','Only a small low speck and faint attachment at the c are discernible; a full joining arc cannot be established. Preserve the mark as doubtful.'],
 [r'\hand{or}\inserted{be}',r'\hand{or} \inserted{be}','The interlinear be follows the separate handwritten word or.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3231:[r"``interesting extra feature'' \unsure{a}",'A dark a-shaped type impression follows the closing quote. Its layers remain unclear; no full stop is supplied.'],
 3232:['transforms weak equivalences into weak equivalences','Both occurrences visibly have plural s.'],
 3235:[r'W_M = i^{*\,-1}(W_{A^{\hand{\wedge}}})','The source uses the literal star-minus-one superscript, without added parentheses.'],
 3237:['the usual asphericity criterion','The page has these words, not a numbered or linked reference.'],
 3240:['the functor is modelizing','The source verb is is, with final s.'],
 3243:['assumptions M = (Cat)','The typed noun is plural.'],
 3244:['needs be elementary','The typed word is be.'],
 3246:['or be (Cat) itself:','The inserted word has a clear e, and the entire concluding addition is handwritten.'],
 3247:['Two long pen lines beside the paragraph','Both strokes are present from there at any rate to valence of categories; they are reconstructed graphically.']
 },'unsure':[
 [r'\unsure{a}','The dark final a-shaped impression does not securely disclose any earlier punctuation layer.'],
 [r'\unsure{H_A = W_A^{-1}A\hat{}}','The old formula has both typed x cancellation and diagonal pen strokes. H_A, equality, W_A and the inverse exponent are plausible, but the whole old formula remains doubtful.'],
 [r'\unsure{.}','The end mark has a vertical stem and two dark lobes, possibly a bracket or overwritten punctuation. A full-stop reading remains doubtful.'],
 [r'\ensuremath{\smile}','The shallow pen joining curve from c to a is distinct.'],
 ['condition a(iv)','The letters and the inner closing parenthesis can be distinguished beneath the x row.'],
 [r'\unsure{,}','The upper layer is a typed x; the earlier punctuation beneath it is still uncertain.'],
 [r'\unsure{.}','A small low speck before c is visible, but no complete smile-shaped arc can be traced.']
 ],'notes':[
 'The first line ends in a dark a-shaped type impression, without enough evidence to resolve its layered history as a colon.',
 'The cancelled formula retains doubt because both machine x strikes and diagonal pen strokes obscure its letters. The following end mark remains uncertain between punctuation and a bracket-like stroke.',
 'The old condition a(iv) is legible; the replacement (a iv) and (a ii) are typed above the line, with a handwritten implication arrow.',
 'The mark after setting is a typed x over an uncertain earlier punctuation impression.',
 'The implication join is a clear shallow pen curve. The tiny low mark before comes is not a securely recoverable joining arc and remains doubtful.',
 'Existence has a pen-retraced c; The proof has typed H/h overlap, while The question has a penned h over typed h. The clipped final part of modelizers is dark and overprinted, with no securely separable older reading.',
 'The lower-left 6 is handwritten. The two long marginal strokes and the handwritten merely, beforehand and final or/be addition are retained.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_006:join','before':JOIN,'after':'implication','line':21,'decision':'authorial join for master','reason':'The pen curve joins the two parts of implication; corrected forms apply the instruction rather than print the curve as a mathematical symbol.'}],
 'evidence':'Both original halves and nine enlarged detail panels inspected. The opening a remains a doubtful layered impression. The old formula and its final dark mark are not resolved. The cancelled reference reads condition a(iv), with typed replacement clauses above it and a penned implication arrow. A typed x, not a pen comma, follows setting. The c of existence is pen-retraced; The proof has a typed H/h overprint and The question a pen h over the original h. The clear joining curve in implication is represented and given a master join; the much smaller mark before comes remains doubtful. The double margin lines, pen additions merely and beforehand, and final or/be addition are present. Literal fastiduously and dependant are retained.'})
variants.append({'key':key,'before':JOIN,'after':'implication','kind':'authorial word join','reason':'The shallow pen curve joins the c and a of implication.','source_id':'OBS:ps_134-4_006:join'})

key='ps_134-4_007';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'A^{\wedge}',r'A^{\hand{\wedge}}').replace(r'B^{\wedge}',r'B^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'All arrows and presheaf carets on the page are drawn in pen.'])
STROKE=r'\margin{\diagram{\begin{tikzpicture}[x=1ex,y=1ex]\draw (0,0)--(.12,5)--(.1,10)--(.2,14);\end{tikzpicture}}}'
edits += [
 [r'M\xout{*}',r'M^{\unsure{*}}','The raised mark is heavily blackened and asterisk-like. Neither a separate regular machine-x row nor a secure cancellation boundary can be established, so retain the whole mark doubtfully instead of deleting it.'],
 [r"\margin{vertical stroke in the left margin from this line down to ``categories.''}",STROKE,'The margin contains a single long pen stroke, not this editorial description.'],
 ['as for that',r'as f\over[typed]{a}{o}r that','An a-shaped lower type impression is visible beneath the o.'],
 ['some mild extra',r'some \over[typed]{m}{m}\over[typed]{i}{i}ld extra','The m and i have repeated type impressions.'],
 ['Maybe',r'May\over[typed]{v}{b}e','The b is typed over a v-shaped lower impression.'],
 ['The very first',r'T\over{h}{h}e very first','A long pen h is superimposed on a typed h.'],
 ['means looking',r'means lo\over[typed]{v}{o}king','The second o is typed over a v-shaped lower letter.'],
 [r'$A^{\hand{\wedge}}$is',r'$A^{\hand{\wedge}}$ is','Preserve the boundary between the formula and the following word.'],
 [r'that\hand{,} in',r'that\hand{\unsure{,}} in','The mark has an unusually dark upper body and a short lower stroke. A comma is plausible but its graphic layer is not securely resolved.'],
 [r'$A^{\hand{\wedge}}$\hand{/}is',r'$A^{\hand{\wedge}}$\hand{/} is','The oblique pen separation mark precedes the separate word is.'],
 [r'\inserted{rather}',r'\inserted[typed]{rather}','Rather is typed above the line; the long placing curve below it is handwritten.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3248:['when A is a strict test category, namely','The words test category are clearly typed and remain live.'],
 3253:[r'that\hand{\unsure{,}} in the case at least','The added dark pen mark is present, although the comma interpretation is retained with doubt.','retain doubtful mark'],
 3254:['Long single pen line beside the Question paragraph','The line extends beside the whole paragraph, and is reconstructed without the draft editorial description.']
 },'unsure':[
 [r'\unsure{or}','The o and r are cramped and overprinted at the clipped edge; the probable reading remains doubtful.'],
 [r'\unsure{-}','The end of the line is heavily overprinted and clipped; a hyphen cannot be recovered cleanly.'],
 [r'\unsure{a}','The a-shaped lower cell is covered by the insertion curve and heavy retracing. Its survival is probable but not secure enough to remove doubt.'],
 [r'\unsure{-}','The last line-end mark is blotted and cut by the supplied image edge.']
 ],'notes':[
 'The raised asterisk-like mark after M is heavily blotted. Its cancellation status is not secure; it is retained as a doubtful marked superscript.',
 'For has typed a/o, mild repeated m/i impressions, Maybe v/b, looking v/o, and The a long pen h over the original typed h.',
 'The clipped or of functor and both dark line-end hyphen positions remain doubtful after enlargement.',
 'The interlinear rather is typed, with a handwritten placing curve; the old a remains visible only beneath heavy retracing and is retained doubtfully.',
 'The oblique stroke between the presheaf formula and is is handwritten. The following word boundary is explicit in the checked TeX.',
 'The lower-left 7 is handwritten; the date 30.3 and section number 47 are typed. The two clear earlier additions a priori and quite are handwritten.'
 ],'evidence':'Both original halves and ten enlarged detail panels inspected. The long single margin line is reconstructed. The raised mark after M is too blotted to support a secure deletion. Type overprints are separately recorded in for, mild, Maybe and looking; The has a pen h. The a priori and quite insertions are penned, whereas rather is typed above the line with a penned placing hook. The old a beneath that hook remains doubtful. The mark after that is dark and not a secure clean comma; it is now explicitly doubtful. The right-edge or and both line-end hyphen positions remain uncertain. Strict test category is fully present, contrary to the witness omission.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
