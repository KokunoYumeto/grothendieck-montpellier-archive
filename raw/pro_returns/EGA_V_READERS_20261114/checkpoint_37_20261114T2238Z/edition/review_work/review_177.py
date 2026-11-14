import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\hand{$\widetilde{\phantom{d}}$}\!d',r'\overset{\hand{\sim}}{d}','Every tilde is drawn above its typed d; the revised encoding places it there without nested math delimiters.'),
(r'^{\unsure{\hand{2}}}',r'^{\unsure{2}}','The raised2 has a typed serif base and dark superposed strokes. Its precise retouch layer remains unresolved; it is not confidently assigned wholly to handwriting.'),
(r'\xout{\unsure{De plus, le discriminant corrigé d a ainsi introduit satisfait à}}',r"\xout{De plus, le ``discriminant corrigé'' $\overset{\hand{\sim}}{d}$ ainsi introduit satisfait à}",'The full cancelled line is legible, including the quotation marks and a pen tilde over d. There is no separate a between d and ainsi.'),
(r'\xout{\unsure{les conditions suivantes}}',r'\xout{\shortstack[l]{la\\conditions suivantes}}','The small cancelled upper group reads la, above a second cancelled baseline conditions suivantes. The draft les is not supported; the two levels are retained.'),
(r'propr\over{\illegible{1}}{\unsure{ié}}té',r'prop\unsure{r}\over{\illegible{2}}{\unsure{ié}}té','A pen stroke also crosses the r cell. The next two cells are heavily retouched; the proposed ié remains uncertain and the two older characters are unreadable.'),
(r'\inserted{sur $\underline{E}$}',r'\inserted[typed]{sur $\underline{E}$}','Sur and the underlined E are typed interlinearly; only the curved insertion leader is pen.'),
(r'\xout{Corollaire 16.7.}',r'\xout{\uline{Corollaire} 16.7.}','The cancelled word Corollaire still has its visible original underline.'),
(r'\unsure{Soinnt|Soient}',r'Soi\unsure{e|n}\unsure{n|e}t','The two cells after Soi each contain e/n overprinting; uncertainty is localized to those cells rather than selecting a normalized word.'),
(r'\oplus',r'\hand{\oplus}','The circled-plus signs in both displayed orthogonal-sum formulas are handwritten.'),
(r'\otimes 2',r'\hand{\otimes}2','Both tensor signs in determinant exponents are pen; their following2s are typed.'),
(r'\in \Gamma',r'\hand{\in}\hand{\Gamma}','Both membership signs and both gamma symbols in the theorem statements are handwritten.'),
(r'd\unsure{\over{s}{i}}scriminant',r'd\unsure{s|i}\unsure{s|i}criminant','Two successive cells after d each show s/i type overprinting. No separate pen replacement i is securely present, and the second altered cell must also remain visible.'),
(r'préschém-%','préschém','The right edge clips the end of the line immediately after the m; no hyphen is visible there and none is supplied.'),
(r'(i\xout{x}i bis)',r'(i\unsure{i|x}i bis)','The middle numeral occupies one overwritten i/x cell between the two other i characters; it is not a separate deleted x followed by an absent numeral.')
]
D={
5:'The top-right4 is handwritten.',
7:'The tilde lies above d in pen. A raised2 is visibly present after the closing parenthesis, but the serif type form and heavy retouch cannot be separated confidently; the exponent remains uncertain and is not removed for mathematical reasons.',
9:'The full cancelled line is recovered, with quotation marks around discriminant corrigé, a hand tilde over d, and ainsi directly after d.',
11:'The two cancelled levels read la above conditions suivantes; the visible la is retained literally despite agreement.',
13:'The r is crossed by an extra stroke and the following two cells are pen-retouched. The underlying letters are unreadable and ié remains a qualified reading.',
15:'Both commas after temps and avant are added in pen, distinct from the typed terminal comma.',
17:'Sur underlined E is typed, attached by a pen leader. The g is penned over the old p; the remaining visible ère is retained without adding u.',
23:'The x-cancelled Corollaire16.7 is fully legible, including the underline beneath Corollaire. The following tilde and tensor sign are pen.',
27:'The two e/n cells in the opening word are type overprints; Soi and final t are secure.',
32:'All three tildes and the circled plus are handwritten; the two right-hand factors have no extra separator supplied.',
35:'All three tildes, the circled plus and the explicit factor2 are pen; the digit2 is not a replacement inferred from the preceding formula.',
49:'The two consecutive s/i cells are typed overprints. The tilde, membership sign, gamma and tensor sign are hand drawn; modifié is retained literally.',
51:'The parenthesis Lorsque E est d e rang constant n is typed between the lines and led to condition (iii) by a pen curve; its extra final s is x-cancelled. The large S-prime/S gap contains no visible arrow.',
57:'The middle numeral cell is i/x overprint. The arrow from S-prime to S is pen and is clearly visible here.',
61:'The lower-left177 is handwritten.'
}
N=[
'A raised2 is present but its typed serif form and superposed dark strokes leave the exact layer unresolved. Every visible tilde, including the one in the cancelled line, is pen.',
'The cancelled first line is fully recovered with quotes and a tilde, and has no extra a before ainsi. The next cancelled material has la on an upper short baseline, then conditions suivantes below.',
'The r has an additional pen stroke; the following two altered cells retain uncertain ié and unreadable older characters.',
'The two cells after Soi contain e/n overprinting. Their uncertainty is retained separately.',
'Two cells after initial d show s/i overprinting, so both are marked rather than presenting one confident corrected letter.',
'The entire interlinear parenthesis is typed, its insertion curve is pen, and the extra s after constant is x-cancelled.',
'The gap S-prime then S in (iii) is blank. No arrow is inserted; the separate arrow in (iii bis) is visibly pen.',
'Both folios, upper4 and lower177, are handwritten and clear.',
'There is no long marginal handwriting. Every short insertion, retouched cell, formula sign and both outer margins were checked.'
]
extra=[
dict(line=19,before='isomorpphisme',image='isomorpphisme',decision='retained',reason='The doubled p is visible in the typed word.',category='literal-spelling'),
dict(line=25,before="s'appelera",image="s'appelera",decision='retained',reason='The word has one l in the scan; no spelling change is made.',category='literal-spelling'),
dict(line=49,before='modifié',image='modifié',decision='retained',reason='The scan uses modifié here although the earlier definition calls it corrigé.',category='literal-wording'),
dict(line=55,before='standart',image='standart',decision='retained',reason='The final typed letter is t.',category='literal-spelling'),
dict(line=43,before='préschém / ma',image='préschém / ma',decision='retained',reason='The m at the clipped right edge and the next-line ma are both preserved without repairing the duplicated letter.',category='line-boundary')
]
print(len(complete('ega25_25_177',R,D,N,extra)['decisions']))
