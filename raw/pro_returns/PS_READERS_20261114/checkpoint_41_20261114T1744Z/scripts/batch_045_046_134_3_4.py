import json,re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT

def commit(c):
 (OUT/'review_notes'/f"{c['key']}.json").write_text(json.dumps(c,ensure_ascii=False,indent=2))
 save_review(c)

key='ps_134-3_045';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=l.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'A^{\wedge}',r'A^{\hand{\wedge}}').replace(r'\hand{\Delta}^{\wedge}',r'\hand{\Delta}^{\hand{\wedge}}')
 a=a.replace(r'\xrightarrow{\ iA\ }',r'\overset{i_A}{\hand{\longrightarrow}}')
 if a!=l:edits.append([l,a,f'Source line {n}: the arrows and presheaf carets are penned; the i_A label over the comparison arrow is typed with a lowered A.'])
edits += [
 [r'\xout{\unsure{finite}}',r'\xout{finite}','All six old letters are readable below the cancelling x characters.'],
 [r'\xout{\unsure{this}}',r'\xout{this}','The cancelled word is this, below the typed whether.'],
 [r'\inserted{to these,}',r'\inserted{to these}','The apparent comma is the turned-up end of the continuous insertion curve, not a separate punctuation mark.'],
 [r'\inserted{provisionally,}',r'\inserted{provisionally}','The curve after provisionally continues the insertion bracket below the word; no independent comma is visible.'],
 [r'\xout{\illegible{2}}',r'\xout{boils down to}','The underlying phrase is recoverable as boils down to beneath the row of x cancellations.'],
 [r'\inserted{and,}',r'\inserted{and}','The stroke after and is the right end of its insertion curve, not a comma.'],
 [r'\inserted{moreover,}',r'\inserted{moreover}','The long line under moreover curves up at its right end; that curve is not separate comma punctuation.']
]
commit(dict(key=key,edits=edits,diffs={
2243:[r'\inserted{to these}','The pen words read to these; the trailing curved stroke belongs to placement.','correct punctuation attribution'],
2245:[r'\inserted{provisionally}','The word has a placement curve rather than a distinct following comma.','correct punctuation attribution'],
2246:[r'\hand{(\unsure{35})}','The call starts with 3; the following open digit is insufficiently clear to decide between the proposed 5 and a possible 6. No footnote prose occurs here.'],
2247:['reasonable','The word ends e; it is not the witness reasonably.'],
2256:[r'\inserted{and}','The final upturn belongs to the placement mark, not comma punctuation.','correct punctuation attribution'],
2257:[r'\inserted{moreover}','The same continuous placement curve accounts for the apparent comma.','correct punctuation attribution']
},unsure=[
['finite','The cancelled six-letter word is legible.'],
['this','The cancelled four-letter word is legible.'],
[r'\unsure{35}','The first digit is 3, but the second is an open hooked form compatible with 5 or 6; retain uncertainty.']
],illegible=[
['boils down to','The three old words can be distinguished beneath the x-overstrikes.']
],notes=[
'The old word before sums is finite, recovered from the scan.',
'The old this is recovered. Whether is typed and the latter is handwritten, as the source already distinguishes.',
'The call begins 3 and has a doubtful second digit; no confident resolution is made.',
'The crossed phrase is boils down to, below the typed replacement (*) just means.',
'The overtyped letters in indeed, this, sums, operations and namely leave the source final readings legible; no spelling normalization is introduced.'
],evidence='Both halves inspected with crops of finite, this, the call, boils down to and the four interlinear insertion ends. The cancellation boils down to is readable, and (*) just means is typed above it. To these, provisionally, and and moreover have continuous pen placement curves whose upturned ends were mistakenly treated as commas; those added punctuation characters are removed. The comparison-arrow label is typed i with a lowered A, not baseline iA. The weak-equivalence criterion displays preserve literal typed x products. The uncertain note call is retained without importing its witness footnote.'))

key='ps_134-3_046';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=l.replace(r'A\char`\^',r'A^{\hand{\wedge}}')
 a=a.replace(r'\hand{$\xrightarrow{i_A}$}',r'\overset{i_A}{\hand{\longrightarrow}}')
 if a!=l:edits.append([l,a,f'Source line {n}: the A carets are pen additions; the first display has a typed i_A label over a hand arrow, so its lettering remains plain.'])
edits += [
 ['Theorem: Let',r'\uline{Theorem}: Let','The word Theorem is underlined on the scan, while the colon follows the underline.'],
 [r'\inserted{sed}',r'\inserted[typed]{sed}','The replacement sed above the cancelled end of composition is typed, with a pen placement curve.'],
 [r'\margin{9.4. Presumably}',r'\margin{\unsure{9.4. Presumably}}','The readable dated heading belongs to the left marginal note crossed by broad pencil hatching; uncertainty concerns cancellation status rather than the letters.'],
 [r'\unsure{cf remark 3 p.174}',r'cf remark 3 p.174','The right note clearly reads cf remark 3 p.174.'],
 [r"\margin{we'll have to add that $j_A = i_A^*$ is model preserving, cf remark 3 on p. 174}",r"\margin{\unsure{we'll have to add that $j_A = i_A^*$ is model preserving, cf remark 3 on p. 174}}",'The rotated left note is readable, but broad pencil strokes across it leave its cancellation status uncertain; preserve the full wording with that uncertainty.'],
 [r'\deleted{def}',r'\deleted{\xout{def}}','The old def is machine-cancelled by x characters and then crossed with a continuous pen stroke.'],
 [r'the functor $m_A$ commutes with finite products.',r'\inserted[typed]{the functor $m_A$ commutes with finite products.}','This complete sentence continuation is typed between the base lines, with a curved placement mark leading after Moreover.'],
 [r'semi-simpli\unsure{-}',r'semi-simpli\xout{\illegible{1}}','At the clipped edge a typewriter cancellation obscures an old character; it is not a securely read hyphen.'],
 [r'pro\xout{du}',r'pro\deleted{\xout{du}}\hand{-}','The terminal du is machine-cancelled and pen-struck; a short separate pen dash is added above the cancelled group before the next-line ducts.'],
 [r'\inserted{in (i) and (ii)}',r'\inserted[typed]{in (i) and (ii)}','The phrase above ducts being replaced is typed, with a hand placement curve.']
]
commit(dict(key=key,edits=edits,diffs={
2260:[r'compo\xout{si}\inserted[typed]{sed} \xout{tion}','The new sed is interlinear typing rather than handwriting.','correct layer attribution'],
2263:[r'\hand{(*37)}','The star and 37 are clearly penned after by i_A.'],
2264:[r'9.4. Presumably ... cf remark 3 p.174 -- is not strong enough ... we\'ll have to add that j_A=i_A^* is model preserving, cf remark 3 on p.174','The scan says model preserving, not the witness equally modelizing. The right reference is legible; broad pencil strokes make the left note\'s cancellation status uncertain.'],
2269:["But I'll still refrain",'The adverb still is plainly typed and remains in the text.'],
2271:[r'\inserted[typed]{in (i) and (ii)}','The phrase is typed above the line rather than written in cursive.','correct layer attribution']
},unsure=[
['cf remark 3 p.174','The full reference is legible in the enlarged right-margin note.'],
[r'\xout{\illegible{1}}','The right-edge mark is a cancelled old character; the old glyph is not recoverable and should not be asserted as a hyphen.']
],illegible=[],notes=[
'The live first-line word category is readable through its overtyping.',
'The right note reads cf remark 3 p.174 -- is not strong enough. The left note dated 9.4 adds j_A=i_A^* model preserving and repeats the page reference; broad pencil hatching leaves its cancellation status uncertain.',
'The semi-simpli edge contains an unreadable machine-cancelled character. The pro/ducts break has cancelled du plus an added pen dash. Made remains a legible live word despite retouching.',
'The live The in both numbered conditions is readable through the typewriter overprints.'
],evidence='Both halves inspected, with a rotated crop of the entire left note and enlarged right-note, def, line endings and interlinear product sentence. The theorem heading is underlined. Sed, the finite-product sentence following Moreover, and in (i) and (ii) are interlinear typing marked by pen curves. The first displayed arrow has a typed i_A label; its shaft and all carets are penned. The right note explicitly refers to remark 3 p.174 and says condition (i) is not strong enough. The dated left continuation says to add that j_A=i_A^* is model preserving, but its pencil hatching makes cancellation uncertain. The call (*37) is clear. The two clipped line ends retain their actual cancellations and do not acquire inferred characters.'))
