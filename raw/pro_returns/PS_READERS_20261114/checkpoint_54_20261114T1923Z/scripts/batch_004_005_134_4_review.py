import sys,re,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
JOIN_DEFINED=r'\begin{tikzpicture}[baseline=(w.base)]\node[inner sep=0pt] (w) {def ined};\draw[color=blue,line width=.45pt] ([xshift=-.5em,yshift=.65ex]w.south) to[bend left=20] ([xshift=.2em,yshift=.65ex]w.south);\end{tikzpicture}'
PARA=r'\begin{tikzpicture}[baseline=-.2ex]\draw[color=blue] (0,0)--(.45,0)--(.45,.4)--(.82,.4);\draw[color=blue] (.49,.02)--(.49,.42);\end{tikzpicture}'
key='ps_134-4_004';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\mapsto',r'\hand{\mapsto}').replace(r'A_{/a}',r'A_{\hand{/}a}')
 if new!=line:edits.append([line,new,'The hats, arrows and category-of-elements slash are drawn in pen.'])
edits += [
 [r'\deleted{\unsure{(92)}}',r'\xout{(92)}','The old folio (92) is legible and crossed by a regular row of typed x marks.'],
 ['One drawback',r'O\over[typed]{N}{n}e drawback','The capital N and lowercase n share a type cell.'],
 ['More seriously',r'M$\overset{\hand{\smile}}{\mathrm{o}}$re seriously','A small cup-shaped pen stroke is placed above the typed o.'],
 ['which can be',r'which \over[typed]{i}{c}\over[typed]{a}{a}n be','The first cell has a dotted typed i under c; a has repeated type impressions.'],
 ['the canonical pair',r'the \over[typed]{p}{c}anonical pair','The old p descender remains visible beneath c.'],
 ['still less does',r'still \over{t}{l}\over{e}{e}ss \over[typed]{d}{d}oes','The l is penned over typed t, e is pen-retraced, and d has repeated type impressions.'],
 [r"it\hand{\unsure{'}}s",r"it\hand{'}s",'The small pen apostrophe above the t/s boundary is clear.'],
 [r'\deleted{upon}\inserted{about}',r'\deleted{upon} \inserted{about}','About is a separate replacement word.'],
 ['The first one',r'T\over[typed]{H}{h}e first one','The H and h occupy one typed cell.'],
 [r'def\hand{\unsure{-}}ined',JOIN_DEFINED,'The typescript has an internal blank, with a curved pen join from f to i; it is not a lexical hyphen. Preserve the graphic and typed gap diplomatically.'],
 [r'\unsure{xixx}','ties','The old letters t-i-e-s are readable under the four machine x strikes; their spelling is preserved.'],
 [r'\margin{\unsure{new-paragraph sign (bracket)}}',PARA,'Replace the editorial description by the visible stepped pen paragraph mark, including its reinforced vertical stroke.'],
 [r'Th\over{e}{is}',r'T\over[typed]{H}{h}\over{e}{is}','The h also has H/h type overlap; the later is is written over typed e in pen.'],
 [r'test-notion\unsure{s}','test-notions','The final s is visible at the edge, but no final period is supplied.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3199:['viewed as part','The typed past participle ends ed.'],
 3202:[r"it\hand{'}s variants",'The pen apostrophe is visible and retained.'],
 3206:['test functor (still to be defined !) of a test category into an arbitrary modelizer M','The whole intervening phrase is on the page; the internal gap of defined bears an authorial joining stroke.'],
 3207:['Stepped paragraph mark before This','The large stepped pen mark calls for a new paragraph before the handwritten correction This; the master variant applies that instruction.','record author paragraph instruction'],
 3209:['test-notions','The plural s is visible at the edge; no final full stop is visible.'],
 3210:[r'\margin{4}','The lower-left pencil 4 is present.']
 },'unsure':[
 ['(92)','All four characters are readable beneath machine x strikes.'],
 ["'",'The apostrophe-like stroke is a clear pen apostrophe.'],
 [r'\unsure{e}','The extra cell after class is obscured by a thick pen deletion.'],
 ['Reconstructed join over def ined','The line arches across an internal blank and joins the two typed portions; it is not a textual hyphen.'],
 ['ties','The original four lower letters are readable.'],
 ['Reconstructed stepped paragraph sign','The step and reinforced vertical are visible; no editorial wording is retained as manuscript content.'],
 ['s','The final s is recognizable at the right edge.']
 ],'notes':[
 'The earlier folio (92) is machine-cancelled, not crossed by a single pen stroke.',
 'One has capital N and lowercase n in the same typed cell.',
 'The small pen cup above o is reconstructed explicitly.',
 'Can has typed i/c and repeated a impressions; the lower word is not supplied as the speculative has.',
 'The l of less is penned over t, e is retraced, and the d of does is retyped.',
 'The extra letter after class remains unreadable under its pen blot, with the tentative e retained.',
 'The first The and the final This both have H/h type overlap.',
 'The curved joining mark bridges the blank in def ined; a master variant joins it in corrected forms.',
 'The stepped mark is placed before This and is applied as a paragraph break only in the corrected forms.',
 'The final plural s is visible, while the final punctuation remains absent from the supplied edge.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_004:join','before':JOIN_DEFINED,'after':'defined','line':33,'decision':'authorial join for master','reason':'The pen curve closes the typed internal gap in def ined; diplomatic retains both the gap and the mark.'}],
 'evidence':'Both original halves and details of can, less/does, def ined, the cancelled ties, This and the class blot inspected. The earlier (92) is machine-cancelled. Can and One contain typed overprints; More bears a pen cup. The apostrophe in its is a live pen addition. The curved mark in def ined joins a typed gap and is represented graphically, with a master join. The large stepped mark before This supplies an authorial paragraph break, replacing the draft editorial description. The last s of test-notions is readable, with no visible final period. The extra class cell remains doubtful.'})
variants += [{'key':key,'before':JOIN_DEFINED,'after':'defined','kind':'authorial word join','reason':'The pen curve joins the typed def and ined across their internal blank.','source_id':'OBS:ps_134-4_004:join'},{'key':key,'before':PARA,'after':'\n\n','kind':'authorial paragraph break','reason':'The stepped pen mark before This calls for a new paragraph.','source_id':'DIFF:3207'}]

JOIN_TECHNICAL=r'\begin{tikzpicture}[baseline=(w.base)]\node[inner sep=0pt] (w) {technic al};\draw[color=blue,line width=.45pt] ([xshift=.65em,yshift=.3ex]w.south) to[bend right=15] ([xshift=1.35em,yshift=.3ex]w.south);\end{tikzpicture}'
key='ps_134-4_005';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A^\wedge',r'A^{\hand{\wedge}}').replace(r'\longrightarrow',r'\hand{\longrightarrow}')
 if new!=line:edits.append([line,new,'The arrows and presheaf carets are drawn in pen.'])
edits += [
 [r'F\unsure{i}rst',r'F\unsure{\over[typed]{!}{i}}rst','The live i is clear; extra marks above and below resemble an older exclamation impression, but this layer interpretation remains doubtful.'],
 [r'test-func\unsure{g|t}or',r'test-func\over[typed]{g}{t}or','The old g loop and descender remain distinct beneath the typed t.'],
 [r'A^{\unsure{*}}',r'A^{\unsure{\overset{\hand{/}}{\mathrm{x}}}}','The superscript has a raised x-like type impression and an oblique pen stroke above it. Neither an earlier hat nor a definite cancellation boundary can be established, so the whole mark remains doubtful.'],
 [r'\xout{t}Thus',r'\deleted{t}Thus','The old lowercase t before the separate typed Thus is crossed in pen.'],
 [r'\unsure{famil}','famil','The five old letters f-a-m-i-l are readable under the machine x row.'],
 [r'\mathrm{F}\unsure{l}(M)',r'\mathrm{F}\unsure{\over{l}{l}}(M)','The typed l has a long oblique pen stroke through it; whether this is a retracing of l remains uncertain.'],
 [r'technic\hand{\unsure{$\smile$}}al',JOIN_TECHNICAL,'The typescript has an internal blank in technic al; the pen curve joins the two portions. Preserve the literal gap and its graphic diplomatically.'],
 [r'\unsure{b|r}educe','beduce','The visible first typed letter is b; no secure r correction is visible. Record reduce as a contextual one-off slip variant, leaving beduce in the diplomatic source.'],
 ['THe very first',r'T\over[typed]{H}{h}e very first','The H and h share a typed cell.'],
 [r'\unsure{\mathrm{x}}',r'\mathrm{x}','The superscript after modelizing is a regular typed x.'],
 [r'(\unsure{W_{A^{\hand{\wedge}}}|W_A})',r'(W_A\over{)}{)}','The target is W_A. The nearby dark stroke belongs to the retraced closing parenthesis; no independent hat over A is visible.'],
 ['THere is',r'T\over[typed]{H}{h}ere is','The H and h are typed in the same cell.'],
 [r'\xout{w}We',r'\deleted{w}We','The old lowercase w before the separate typed We is pen-cancelled.'],
 [r'\inserted{$= H_M$}',r'\inserted[typed]{$= H_M$}','The equals sign and H_M are typed above the line, placed by a pen curve.'],
 [r'\inserted{if}',r'\inserted[typed]{if}','The inserted if is typewritten, with a separate placing hook.'],
 [r'saturated\hand{,}namely',r'saturated\hand{,} namely','The comma precedes a separate word.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3211:[r'i : A^{\unsure{\overset{\hand{/}}{\mathrm{x}}}} \hand{\longrightarrow} M','The extra superscript is visibly marked but its layers and cancellation status remain uncertain. An independent review agreed that a cancelled hat is not secure.','retain doubtful marked superscript'],
 3217:[r'modelizing;$^{\mathrm{x}}$','A typed superscript x follows the semicolon.'],
 3218:[r'W_M=i^{*\,-1}(W_A\over{)}{)}','The exponent is literally star followed by minus-one. The target is W_A; the apparent extra hat is the reinforced bottom of the closing parenthesis.','correct transcription'],
 3223:["that it's image",'There is no the between the source its-form and image.'],
 3227:['provided we assume','The source clearly reads we.']
 },'unsure':[
 [r'\unsure{\over[typed]{!}{i}}','The final i is clear, but the extra upper and lower marks do not securely settle the older impression or its order.'],
 ['g corrected to t by typing','The lower g loop and the upper t crossbar are separately visible.'],
 [r'\unsure{\overset{\hand{/}}{\mathrm{x}}}','A raised x-like type mark and upper pen slash are visible; their semantic status remains uncertain.'],
 ['famil','The five cancelled letters are readable.'],
 [r'\unsure{\over{l}{l}}','The extra pen slash through l cannot be identified securely as correction or retracing.'],
 ['Reconstructed joining curve in technic al','The curve bridges the literal internal blank; it is not a smile symbol in the word.'],
 ['b','The first letter is b; the corrected-form reduce is separately justified by context and the same word on checked 134-3/16.'],
 [r'\mathrm{x}','The raised x is a regular typed character.'],
 [r'W_A\over{)}{)}','The A has no independent hat; the adjacent black mark is part of the closing parenthesis.']
 ],'notes':[
 'The extra upper and lower marks around i are preserved as a doubtful layered interpretation; the live i itself is recognizable.',
 'The cell has typed t over g, with the old descender exposed.',
 'The superscript is represented as a wholly doubtful x-like mark with upper pen stroke, without resolving it to a cancelled hat.',
 'The old t and w are separately pen-cancelled before the typed capitals. Famil is recoverable. The l has a distinct oblique pen stroke of uncertain function.',
 'The cancelled of and the literal i?e. are retained; the latter has an explicit master slip variant to i.e. with same-abbreviation evidence.',
 'The joining stroke across the blank in technic al is reconstructed and applied by a master word-join variant.',
 'The target is W_A; the dark lower portion belongs to the closing parenthesis, not a presheaf hat.',
 'The superscript x after modelizing is typed and clear.',
 'The lower-right 5 is handwritten. The dated 29.3 marginal note is fully retained, including inserted be and its comma.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_005:join','before':JOIN_TECHNICAL,'after':'technical','line':16,'decision':'authorial join for master','reason':'The pen curve joins technic and al across their typed blank.'},
 {'source_id':'OBS:ps_134-4_005:beduce','before':'beduce to the ones','after':'reduce to the ones','line':22,'decision':'master slip variant','reason':'The wrong initial b is a one-off typing slip settled by context; the same word reduce is correctly typed on checked 134-3/16.'},
 {'source_id':'OBS:ps_134-4_005:ie','before':'i?e. a notion','after':'i.e. a notion','line':9,'decision':'master slip variant','reason':'The isolated question mark replaces the normal period in the abbreviation i.e., repeatedly attested in checked pages, including 134-3/87. Diplomatic preserves i?e.'}
 ],'evidence':'Both original halves, the general details panel, nine further enlarged panels and a separate functor-cell crop inspected. Test-functor has typed t over g. The raised domain mark has an x-like type impression plus a pen slash, but no secure cancelled hat; uncertainty is retained after independent review. Famil is recovered, while the pen stroke through l remains uncertain. The First i has extra upper and lower impressions of uncertain identity. Beduce is the literal source and gets an explicit corrected-form slip variant. The joining curve in technic al is reconstructed. Formula a) has W_A with a reinforced closing parenthesis, not a separate hat. H_M and if are typed insertions; the dated marginal note is handwritten and fully retained.'})
variants += [{'key':key,'before':JOIN_TECHNICAL,'after':'technical','kind':'authorial word join','reason':'The pen curve joins the typed technic and al across their blank.','source_id':'OBS:ps_134-4_005:join'},{'key':key,'before':'beduce to the ones','after':'reduce to the ones','kind':'slip corrected','reason':'The wrong initial b is settled by context and the same word reduce on checked 134-3/16.','source_id':'OBS:ps_134-4_005:beduce'},{'key':key,'before':'i?e. a notion','after':'i.e. a notion','kind':'slip corrected','reason':'The question mark is an isolated wrong keystroke in i.e., whose normal form is repeatedly attested in checked pages including 134-3/87.','source_id':'OBS:ps_134-4_005:ie'}]
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
