import json,re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT

def commit(c):
 (OUT/'review_notes'/f"{c['key']}.json").write_text(json.dumps(c,ensure_ascii=False,indent=2))
 save_review(c)

key='ps_134-3_049';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=re.sub(r'(?<!\\hand\{)\\(to|in|leq|geq)(?![A-Za-z])',lambda m:r'\hand{'+m[0]+'}',l)
 a=a.replace(r'A\^{}',r'$A^{\hand{\wedge}}$')
 if a!=l:edits.append([l,a,f'Source line {n}: the arrows, membership/inequality signs and specified caret are penned; the variable letters and product x are typed.'])
edits += [
 [r'$(K_n)_{n \hand{\geq} 0}$',r'$(\inserted[typed]{K}_{\xout{\illegible{1}}n})_{n \hand{\geq} 0}$','The live K is retyped above an old machine-cancelled character at the level of n. Preserve that unreadable lower layer rather than flattening the two levels to one K.'],
 [r'\hand{$\cap$}[0,n]',r'\hand{$\cap$}\hand{[}0,n\hand{]}','The intersection sign and both surrounding square brackets have heavy hand-drawn strokes; the numerals, comma and n are typed.'],
 [r'\hand{$\tilde{\Delta}$}\^{}',r'\hand{$\tilde{\Delta}^{\wedge}$}','The extra presheaf caret is handwritten just above/right of the hand Delta-tilde, and is mathematically present on the scan.'],
 [r'\uline{affine simplices}',r'\uline{affine} \uline{simplices}','Two separate underline strokes emphasize affine and simplices, with a gap between the words.']
]
commit(dict(key=key,edits=edits,diffs={
2311:[r"in the $\underline R^n$'s",'The source has the article, pluralizing apostrophe-s, and no semicolon at the end of the line. The high mark is an apostrophe.'],
2315:['handwritten membership sign and braces','The membership sign as well as the braces is penned before the typed 0,1.','correct layer attribution'],
2322:['N cap [0,n], with hand cap and brackets','The enlarged cap and square brackets have irregular thick pen strokes, distinct from the typing.'],
2323:[r'\hand{$\tilde{\Delta}^{\wedge}$}','The presheaf caret really is present and is a pen addition. The witness omits the caret and the comparison description wrongly called it typed.','retain formula; correct layer attribution']
},unsure=[],illegible=[],notes=[
'The high mark after n is an apostrophe belonging to the pluralizing s; the full source wording is retained.',
'The mark after pr_i has the curve of an old opening parenthesis under a crossing cancellation; the existing cancellation reading is retained.',
'The live K is typed above a lower cancelled character, which remains unreadable. That lower layer is now explicitly retained.',
'The small cap and both square brackets around 0,n are handwritten.',
'The small mark under The is an overtyped/retraced part of h, not an independent caret symbol.',
'The ly is typed above the line, and its curve places it after corresponding; more is not deleted.',
'The braces, squares and Deltas are penned, as are the inequality and membership signs. The extra presheaf caret after Delta-tilde is also handwritten.'
],evidence='Both halves inspected, with crops of the R^n apostrophe, cancelled parenthesis, displaced K, N-intersection interval and Delta-tilde caret. The comparison of cubical variants explicitly retains diagonals and symmetry operations, and the repeated source spelling is standart. The lower cancelled character under K is retained as unreadable, with the live K typed above. The second category really has the presheaf caret; the witness omission is not followed. The affine/simplices underlines are separate. The section reference is the hand replacement section 31 over pages 39-40, and the final two-line condition statement is entirely cancelled.'))

key='ps_134-3_050';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=l.replace(r'A^\wedge',r'A^{\hand{\wedge}}')
 # All initially plain arrows on this page are penned. Avoid the one already within the hand insertion only by retaining that insertion's outer layer.
 if r'\to' in a and n!=17:a=a.replace(r'\to',r'\hand{\to}')
 if n==17:a=a.replace(r'c_a : e\to a',r'c_a : e\hand{\to} a')
 if a!=l:edits.append([l,a,f'Source line {n}: the arrows and the small A carets are drawn in pen, whereas their letters and indices remain typed.'])
edits += [
 [r'\inserted{-test}',r'\inserted[typed]{\hand{-}test}','The word test is interlinear typing; its preceding hyphen and the placing bracket are handwritten.'],
 [r'\uline{Condition} \xout{\illegible{1}}',r'\uline{Condition} \xout{H}','The cancelled capital is H, visible through its overstrike before the new T H label.'],
 [r'\xout{\unsure{the}}',r'\xout{the}','The cancelled t-h-e can be read beneath the e= insertion stroke.'],
 [r'\mathrm{id}\xout{\illegible{1}}_a',r'\mathrm{id}\xout{e}_a','The old extra letter after id has the round bowl and middle bar of e under the cancelling x.'],
 [r'\inserted{homotopy}',r'\inserted[typed]{homotopy}','The added homotopy is typed above argument, with a handwritten placement curve.'],
 [r'that \xout{\illegible{1}}',r'that \xout{\unsure{Fxe}$_I$}','The old group has a visible subscript I and a tentative F-x-e base; the base remains explicitly uncertain.'],
 [r'$F\mathrm{x}I\hand{\to} F$ \xout{xxx}',r'$F\mathrm{x}I\hand{\to} F$ \xout{are}','The cancelled old predicate is are, beneath the three overstrikes before is.'],
 [r'A\unsure{?|.}',r'A?','The end of line clearly has a question mark with a curved head and separate lower dot.'],
 [r'topos\inserted{X}',r'topos\inserted[typed]{X}','The small interlinear X is typed, placed by a pen curve.'],
 [r'\xout{xxxxx}\inserted[typed]{whose}',r'\xout{\illegible{1}}\inserted[typed]{whose}','The crossed old group under whose is not five literal x letters; its old wording remains unreadable.'],
 [r'\over{foo}{\unsure{for}}',r'fo\over{o}{r}','The live correction is for: only the last o is overwritten with a pen r, while the first fo remain typed.']
]
commit(dict(key=key,edits=edits,diffs={
2330:[r'\inserted[typed]{\hand{-}test}','Test is typed, while the leading short hyphen is penned.','correct layer attribution'],
2331:['Condition, cancelled H, then T H :','The old H is legible; the live label T H has no surrounding parentheses.'],
2335:[r'u_a=p_a c_a, with hand :a to a','The scan puts p_a before c_a and inserts the stated source/target a to a. Preserve this order as written, although it conflicts with the right-to-left composition convention used in the following homotopy equation.'],
2339:[r'\inserted[typed]{homotopy}','The interlinear word is typed, unlike the neighboring cursive for proving asphericity of F.','correct layer attribution'],
2341:['F','The terminal letter in the handwritten insertion is a capital F.'],
2344:[r'A? \over{x}{(}This','The question mark at the end of the first line is clear; the next line has a hand opening parenthesis over x.'],
2350:[r'topos\inserted[typed]{X}','The X is typed above the line.','correct layer attribution'],
2356:[r'fo\over{o}{r}','Only the final o receives a pen r; the live reading for is clear.','settled and corrected scope']
},unsure=[
['the','The cancelled word is readable through the crossing strokes.'],
['?','The final mark is a definite question mark.'],
['for','The final o is corrected to r; the live word is for.']
],illegible=[
['H','The capital H remains visible under the machine cancellation.'],
['e','The cancelled extra character after id is e.'],
[r'\unsure{Fxe}$_I$','The lower I is readable; the upper Fxe-like group remains tentative under mixed overstrikes.']
],notes=[
'The extra character in retract is machine-cancelled as recorded; the live word is retract.',
'The old condition letter is H and the crossed word before e_A is the; both are recovered.',
'The extra cancelled character after id is e.',
'The cancelled group after that has a visible subscript I and a tentative Fxe-like base; that base remains doubtful.',
'The line ends in a question mark. The next-line opening parenthesis is a pen correction over x, retained without adding an inferred matching parenthesis.',
'The live for is clear; only the final o of foo is overwritten with r.'
],evidence='Both halves inspected with eleven enlarged details of the test insertion, old H, old the, axists, extra e, cancelled formula group, are, question mark, for, whose base and inserted X. The literal source readings axists, oddurs and consequance are confirmed and retained. The author explicitly catches the circularity of using T2 to prove T2 and adds the separate asphericity of a x I. Test, homotopy and X are typed interlinear additions; the hyphen before test and the longer explanatory insertion are handwritten. The formula u_a=p_a c_a is visibly in that order and is preserved as an apparent authorial composition-order slip. The question mark and live for are settled; the old group under whose and part of the earlier cancelled formula remain unreadable or doubtful.'))
