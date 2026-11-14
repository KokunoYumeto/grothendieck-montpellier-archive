import json,re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT

def commit(c):
 (OUT/'review_notes'/f"{c['key']}.json").write_text(json.dumps(c,ensure_ascii=False,indent=2))
 save_review(c)

key='ps_134-3_047';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=l.replace(r'A\^{}',r'$A^{\hand{\wedge}}$').replace(r'F\hand{$\ell$}',r'F\over{l}{l}').replace(r'A\hat{}',r'A^{\hand{\wedge}}')
 if a!=l:edits.append([l,a,f'Source line {n}: the presheaf caret is a pen addition. Where Fl occurs, the l is typed and retraced by an oblique pen stroke, rather than a freestanding handwritten script ell.'])
edits += [
 [r'namely\inserted{of}',r'namely\inserted[typed]{of}','The interlinear of has typewriter forms; only its placing slash is handwritten.'],
 [r'limits\hand{.}',r'limits\hand{\unsure{.}}','The heavy blot after limits does not securely resolve into a clean period; retain the likely punctuation with explicit doubt.'],
 [r'\unsure{\hand{.}}','.','The separate dot after the closing SGA reference parenthesis is a clearly typed period.'],
 [r'\margin{$\uparrow$}',r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.7,0)--(.2,0) .. controls (0,0) and (0,.2) .. (0,.4)--(0,1.2);\end{tikzpicture}}}','The marginal mark is a long bent upward arrow embracing the end of the paragraph, not a short isolated up-arrow character.'],
 [r'\margin{$\downarrow$}',r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.8,1.2)--(.2,1.2) .. controls (0,1.2) and (0,1.1) .. (0,.9)--(0,0);\end{tikzpicture}}}','The second mark is a long bent downward arrow beside the opening of section 34.'],
 [r'\inserted{I=}',r'\inserted[typed]{I=}','The upper I and equals sign are typed, with a hand insertion curve crossing below them.'],
 [r'\hand{$\emptyset$}_{A^{\hand{\wedge}}}',r'\emptyset_{A^{\hand{\wedge}}}','The initial-element symbol is a thin typed slashed o; the cap and A-caret are penned.']
]
commit(dict(key=key,edits=edits,diffs={
2272:[r'above\hand{(38)}','The call reads 38 and is placed around the original punctuation; no witness footnote prose appears.'],
2274:[r'namely\inserted[typed]{of}','Of is an interlinear typed insertion, not cursive.','correct layer attribution'],
2275:['with a small A,','The article and adjective precede the hand A and comma.'],
2276:['which amounts to saying','The s of amounts is plainly typed.'],
2283:[r'\inserted[typed]{I=}I_A','The upper I= is in the typewriter face and positioned by a curved hand stroke.','correct layer attribution']
},unsure=[
['.','The period after the SGA reference parenthesis is typed and distinct.'],
[r'\unsure{\xout{x}}','A small machine overstrike sits below/right of the caret; the old character cannot be distinguished from the cancelling x.'],
[r'\unsure{es}','The end of consequences is cut by the right image boundary; the final completion remains doubtful.']
],illegible=[
[r'\illegible{1}','The old group after e_A is covered by dense pen hatching and is unreadable.']
],notes=[
'The call is (38), penned around the existing punctuation after above.',
'The two long strokes separate nearby words/expressions; they are not extra letters or a division operation.',
'The limits blot remains doubtful as a period. The separate dot after 7.5.) is a clear typed period.',
'The small overstrike beneath the hat is retained as uncertain; no old parenthesis or letter is inferred.',
'The two opposite long bent margin arrows are reconstructed graphically, with their original upward/downward orientations.',
'The consequences ending remains clipped and uncertain.',
'The cancelled group after e_A remains unreadable.'
],evidence='Both halves inspected with crops of the limits/reference punctuation, Fl, the mark beneath A-hat, the clipped consequences, the e_A cancellation and the I= insertion. The first two occurrences of Fl contain typed l characters retraced in pen. Of and I= are interlinear typing. The cap in the endpoint condition is handwritten, while the slashed-o empty symbol is typed. Two long bent margin arrows bracket the end of the modelizing-topos paragraph and the start of section 34; they have been reconstructed as graphics. The source retains O-connected as a letter O, and the uncertain edge/cancellation marks remain explicit.'))

key='ps_134-3_048';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=l.replace(r'\geqslant',r'\hand{\geqslant}').replace(r'\leqslant',r'\hand{\leqslant}')
 # Only the two plain arrows require provenance; the ordered-set arrow is already hand-wrapped.
 if n in [37,38]:a=a.replace(r'\rightarrow',r'\hand{\rightarrow}')
 if a!=l:edits.append([l,a,f'Source line {n}: the inequality signs have uneven hand-drawn angled strokes and underbars; the unmarked arrows are also penned, while the adjacent letters and numbers are typed.'])
mark=r'\margin{\diagram{\begin{tikzpicture}\draw (0,0)--(.55,0)--(.66,.42)--(1.15,.42);\end{tikzpicture}}}'
edits += [
 [r'\mspage{48}',r'\mspage{\hand{48}}','The folio number is written by hand.'],
 [r'\inserted{C}\inserted[typed]{with}',r'\inserted[typed]{C}\inserted[typed]{with}','The interlinear C has the same typewriter face as with, unlike the later large pen C in the body.'],
 [r'subcategory \inserted{A}',r'subcategory \inserted[typed]{A}','The small upper A is typed and placed by a hand curve.'],
 [r'\hand{m}ind',r'\over{\illegible{1}}{m}ind','A typewriter base is visible beneath the pen m, but the old character cannot be securely read; preserve that overwritten layer.'],
 [r'Ta\hand{k}e',r'Ta\over{\unsure{k}}{k}e','The correcting k is penned over a typewriter character resembling k; the old base remains tentative.'],
 [r'\margin{$\lceil$}',mark,'The paragraph instruction is a long stepped corner spanning the sentence boundary, not a single ceiling glyph.'],
 [r'\inserted{m} components',r'\inserted[typed]{m} components','The upper m is typed, with a curved pen placement mark.'],
 [r'\xout{\unsure{s}}',r'\xout{s}','The old final s after The is legible beneath the cancelling x.'],
 [r'\unsure{i.e,}',r'\unsure{i.e,|i.e;}','The last punctuation is heavily overprinted and may be comma or semicolon; retain the two visually plausible readings.']
]
commit(dict(key=key,edits=edits,diffs={
2296:[r'\inserted[typed]{C}\inserted[typed]{with}','Both C and with are typed above the cancelled stable under; the later C in the following line is handwritten.','correct layer attribution'],
2299:[r'Ta\over{\unsure{k}}{k}e ... \inserted[typed]{A}','The k is penned over an uncertain typewriter base; the small inserted A is typed.','correct layer attribution'],
2300:[r'I and \hand{\Delta}_o, \hand{\Delta}_1','The source really uses triangular capital-delta forms here. They are not silently changed into the endpoint-map small deltas.'],
2301:['stepped paragraph mark before The simplest choice','The visible stepped pen mark requests a new paragraph. It is reconstructed in the diplomatic page; an exact master variant applies the paragraph break.','reconstruct instruction'],
2302:['is to take','The source has is, not the witness it.'],
2303:[r'whose \inserted[typed]{m} components','The body word is whose. The m is typed above the line.'],
2304:[r'\inserted[typed]{m}','The interlinear m matches the typewriter letters, not handwriting.','correct layer attribution']
},unsure=[
['s','The cancelled s after The is visible.'],
[r'\unsure{.}','The old punctuation under the heavy replacement after cubes remains doubtful.'],
[r'\unsure{:}','The upper and lower ink lobes suggest a colon but are connected/overlapped enough to leave the exact live punctuation uncertain.'],
[r'\unsure{i.e,|i.e;}','The last mark has a heavy descending stroke and may be comma or semicolon; no confident choice.']
],illegible=[],notes=[
'The enlarged inequality signs have hand-drawn angled strokes and underbars; all three n inequalities and the paired i bounds are marked as pen additions.',
'The A after provided it is in is heavily handwritten over the typewriter A, as recorded.',
'The old base under the pen m in mind is unreadable. The old k in Take is tentative; the pen e retracing in here remains as recorded.',
'The cancelled s after The is readable; the doubt is removed.',
'The cubes punctuation remains doubtful, and no missing right-edge periods are invented. The terminal c of instanc is machine-cancelled before the next-line ce.'
],evidence='Both supplied halves inspected with a twelve-detail sheet of the inequalities, m/k corrections, The-s, cubes punctuation, i.e punctuation and the C/A/m insertions. The page number is handwritten. The inserted C, A and m are typed, whereas the body C and endpoint/map symbols are penned. The literal capital Deltas after containing I are preserved despite the surrounding discussion of endpoint maps. The two displayed/plain arrows and all inequality signs are handwritten. The stepped paragraph mark is reconstructed and supplied as a master-only paragraph-break variant. The old m base, old k base and altered punctuation remain uncertain.'))

variant=dict(key=key,before='Then A is a test category. '+mark+' The simplest choi-',after='Then A is a test category.\n\nThe simplest choi-',kind='author paragraph break',reason='The stepped hand mark at this boundary instructs a new paragraph; the diplomatic page retains its graphic and typed order.',source_id='DIFF:2301')
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text()) if p.exists() else [];old=[v for v in old if not(v['key']==key and v['source_id']==variant['source_id'])];p.write_text(json.dumps(old+[variant],ensure_ascii=False,indent=2)+'\n')
