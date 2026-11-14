import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\mspage{8}',r'\mspage{\hand{8}}','The upper8 is handwritten.'),
(r'\margin{181}',r'\mspage{\hand{181}}','The lower181 is handwritten archive numbering.'),
(r'\oplus',r'\tikz[baseline=(sum.base)]{\node[draw,circle,handwritten,text=black,inner sep=0pt] (sum) {$\unsure{+}$};}','The circle is certainly penned around a plus. The plus itself may be typed or retouched, so its layer remains qualified while the known pen circle is represented separately.'),
('de rang 1 et $Q_2$',r'de rang 1 \unsure{e|a}t $Q_2$','The first letter of et has an e/a type overprint with a raised upper trace.'),
(r'\neq',r'\hand{\neq}','Both not-equal signs are drawn in pen.'),
(r'ramené à prouver dans ce cas \deleted{\unsure{que}} \inserted[typed]{Lemme 16.11.2.} Q lisse \hand{$\Longleftrightarrow$} Q standart.',r'ramené à prouver dans ce cas \tikz[baseline=(lemma.base)]{\node[draw,ellipse,handwritten,text=black,inner sep=2pt] (lemma) {\shortstack[l]{\inserted{le} \inserted[typed]{\uline{Lemme} 16.11.2.}\\\deleted{\unsure{que}} Q lisse \hand{$\Longleftrightarrow$} Q standart.}};}'+'\n% NOTE: The pen oval encloses the lemma title and its formula; its upper edge crosses the preceding typed line without cancelling that line.','The missing pen le is legible before the typed interlinear, underlined Lemme16.11.2. The cancelled que remains obscured. A single pen oval encloses the two levels and crosses the preceding line as its upper boundary; the words on that preceding line remain live.'),
(r'\xout{\unsure{On sait déjà que (ii) implique que}}',r'\deleted{\xout{On sait déjà que (ii) implique que}}'+'\n% NOTE: Tiny dark specks above the initial On and a small n-like remnant below it have no secure added-word or symbol reading.\n','The cancelled sentence is legible throughout. A continuous pen strike is present in addition to the typed x cancellation. The tiny displaced marks around On do not form a secure additional word.'),
(r'\xout{\illegible{3}}',r'\xout{\unsure{on pourrait}}','The crossed span permits the tentative two-word reading on pourrait, but multiple letters remain obscured; the entire candidate stays uncertain rather than being asserted as a recovery.'),
(r"\inserted{D'autre part,}",r"\inserted[typed]{D'autre part}",'D-autre part is typed interlinearly; no terminal comma is visible on that upper line.'),
(r'\xout{\unsure{(ii) $\Rightarrow$ (i). Or}}',r'\deleted{\xout{(ii) \unsure{$\Rightarrow$} (i). Or}}','The two parenthesized labels and Or are legible, while the relation sign is concealed by cancellation. The heavy pen strike supplements the typed x marks.'),
(r'\inserted{Q lisse}',r'\inserted[typed]{Q lisse}','Q lisse is typed above the pen-cancelled (ii).'),
(r'\inserted{signifie}',r'\inserted[typed]{signifie}','Signifie is typed above the x-cancelled implique.'),
(r'standar\over{t}{d}\hand{/}',r'standar\unsure{d|t}\hand{/}.','The final d/t is a same-cell type overprint, not a securely separate handwritten d. A pen slash and a distinct typed period both follow it.'),
(r'a-t\hand{\unsure{-}}il',r'a-t\unsure{-}il','The short horizontal stroke between t and i is visible, but its separate-hyphen status and pen/type layer cannot be confidently distinguished from the adjoining type strokes.'),
(r'\over{n}{c}orrigé',r'\unsure{n|c}o\unsure{d|r}rigé','The first cell has n/c overprinting and the third has d/r overprinting; no distinct pen c can be isolated. The underline beneath the whole word is pen.'),
('étaient connus',r'étai\unsure{e|t}nt connus','The cell after étai contains overlapping e/t forms and is retained as uncertain.'),
('16.2. ou 16.3. ( qui',r'16.2. ou 16.3. \hand{(} qui','The opening parenthesis is a thick curved pen mark; the closing parenthesis later in the line is typed.')
]
D={
15:'Et on est is typed above the cancelled d-autre part. The oval crosses the earlier spectre/corps words but does not independently cancel them.',
16:'The omitted handwritten le is added. Lemme16.11.2 is typed and Lemme has an underline. The old que remains uncertain under pen cancellation. The equivalence arrow is pen and the full lemma passage is enclosed by a pen oval.',
18:'On sait déjà que (ii) implique que is readable beneath both type x marks and a continuous pen strike. Lorsque above it is typed. Tiny marks around On remain without a secure added-word reading.',
19:'The cancelled phrase is only tentatively on pourrait; no definite reconstruction is claimed.',
20:'The check accent over the source E and the rightward arrow are pen. The typed target Ev is retained literally.',
21:'The cancelled donc is clearly legible.',
22:'D-autre part and Q lisse are typed insertions; the former has no visible added comma. The old parenthesized labels and Or are readable, but their relation sign remains uncertain. The old (ii) beneath Q lisse is pen-cancelled. Le noyau is x-cancelled and legible.',
24:'Signifie is typed, replacing the x-cancelled implique. The not-equal sign is pen.',
26:'The final d/t of standard is a type overprint. The slash is pen and a separate period follows it. Prouve16.11.2.et is typed with a pen brace-shaped insertion leader.',
33:'The short stroke at a-t-il remains uncertain as a separate hyphen and in its layer.',
34:'The first and third cells of the underlined word remain n/c and d/r type-overprint uncertainties. The underline is pen; mérité is retained with its visible accent.',
39:'The lower181 is handwritten archive numbering.'
}
N=[
'The oval encloses the typed lemma title and formula and crosses the preceding line only as its upper boundary. The small omitted word before Lemme is a clear handwritten le. The old que remains uncertain under cancellation.',
'Lemme16.11.2, et on est, Lorsque, prouve16.11.2.et, D-autre part, Q lisse and signifie are typed insertions. Their leaders and enclosing oval are pen.',
'The long On-sait sentence is fully legible and has both typed and pen cancellation. The parenthesized labels and Or in the later crossed group are legible but its arrow remains uncertain. The middle cancelled phrase remains the tentative candidate on pourrait.',
'The dual/check mark above source E and the arrow are pen. Ev at the target is typed and is not repaired.',
'The hyphen-like stroke at a-t-il has unresolved layer/status. The word below has n/c and d/r type overprints, rather than a confidently penned c; its underline is pen.',
'The circle around the plus is definitely pen, while the plus itself has unresolved typed/retouched layer and is marked separately as uncertain.',
'Upper8 and lower181 are handwritten and clearly legible.',
'Both complete halves and all pale background areas were inspected. The pale traces do not yield a separately secure additional passage on this face; no background text was silently promoted into the front body.',
'All short handwritten material, the enclosing oval, every cancellation and all margins were read; no additional long marginal passage is securely present.'
]
extra=[
dict(line=23,before='quenle',image='quenle',decision='retained',reason='The extra n is visibly typed between que and le.',category='literal-spelling'),
dict(line=28,before='pû',image='pû',decision='retained',reason='The circumflex is visible and is not normalized away.',category='literal-spelling'),
dict(line=34,before='mérité',image='mérité',decision='retained',reason='The word has an acute on the final e as typed.',category='literal-spelling')
]
print(len(complete('ega25_25_181',R,D,N,extra)['decisions']))
