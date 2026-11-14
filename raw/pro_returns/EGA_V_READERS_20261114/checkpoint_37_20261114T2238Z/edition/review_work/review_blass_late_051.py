import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete

R=[
(r'\underline{Y}^{1}',r'\underline{Y}1','The digit is full type size and lies at the body baseline in both occurrences; the scan does not show a raised exponent.'),
(r'g$_{1}$','g1','The full-size 1 follows g on the ordinary type line; no lowered index is supplied.'),
(r'g$^{-1}$','g-1','Each -1 is full type size at the ordinary baseline, as visible in both scan parts; retain the linear typing.'),
(r'\margin{* ASK AG}',r'\margin{\hand{* ASK AG}}','The star and all five capital letters are irregular pen strokes in the lower left margin. Preserve the note and explicitly encode its handwritten layer.')]
M={14:'The broad grey curved inclusion sign between W and U is handwritten and points open to the right; it is retained as subset.',27:'The second broad curved inclusion sign, after g-1(U), is handwritten in the typist’s blank and has the same form as the upper sign.',37:'The lower-left star and ASK AG are handwritten; the wording is complete and uncancelled. The typed [illegible]* above is a translator query, not an editorial replacement.'}
N=[
'The upper-right numeral 51 has a regular serif impression separate in face from the body typing; both digits are secure.',
'Contrary to the draft note, both Y1 and every g-1 group use full-size characters on the body baseline; g1 is likewise retained linearly. U1 is plainly baseline typing.',
'The brackets, word illegible, and following star are typed. The corresponding handwritten * ASK AG remains visible below. Checked cote25 site45, final assertions of8.8, has the revised Y superscript and handwritten clause “est défini par l’annulation d’une section D d’un Module inversible”; no words are inserted into Blass’s query.',
'Both broad subset signs are pen additions. Their positions and open-right shapes are visible in the upper paragraph and Remark8.10.',
'There is no long handwritten passage; the short * ASK AG footnote and two inclusion signs are the visible pen material.'
]
E=[
dict(line=19,before='[illegible]*',image='[illegible]*, typed literally',decision='retained_query_with_french_crossreference',reason='Checked cote25 site45, final assertions of8.8: the revised Y superscript is followed by the handwritten “est défini par l’annulation d’une section D d’un Module inversible”. Blass’s Ysing or Ysup sing [illegible]* is preserved without filling the query.',category='cote24-query'),
dict(line=37,before='* ASK AG',image='Handwritten * ASK AG',decision='retained_query_with_french_crossreference',reason='The starred note points to the typed [illegible]* in the paragraph corresponding to checked cote25 site45, final assertions of8.8 and the section D of an invertible Module.',category='cote24-query'),
dict(line=8,before='U1',image='U1',decision='comparison-recorded',reason='Blass prints baseline U1; checked cote25 site45 writes U′ in the corresponding “soit U′” passage. Each reading remains unchanged.',category='cote24-comparison'),
dict(line=9,before='we see immediately that g-1(U) → U is an open immersion',image='Same typed sentence',decision='comparison-recorded',reason='Checked cote25 site45 additionally states that g1 induces an isomorphism g-1(U) to U′ before the open-immersion sentence. That intervening clause is absent from this Blass page.',category='cote24-comparison'),
dict(line=16,before='dim Ysup sing = r - 2',image='The equality is typed and uncancelled.',decision='comparison-recorded',reason='Checked cote25 site45 has a pen replacement over the typed equality, recorded doubtfully as ≤. Blass’s visible equality is retained.',category='cote24-comparison'),
dict(line=24,before=r'\uline{Remark 8.10}',image='Remark 8.10 with a straight underline',decision='confirmed',reason='All heading characters and the underline are typed and plainly visible.',category='underline'),
dict(line='7–35',before='Body and formulas',image='All prose, punctuation, underlined variables, literal sing/sup sing, arrows, and indices compared.',decision='confirmed',reason='The printed “follows the”, “module.;”, dimension r followed by r-1, and baseline sing/sup sing are retained. Arrow shafts and heads are regular typed forms; the two subset signs alone have the pen layer described above.',category='full-text'),
dict(line='margins',before='Page edges',image='Blank upper and side margins apart from numeral51 and small isolated spots; lower handwritten note.',decision='confirmed',reason='Both image parts were read to all borders; no additional word or symbol is visible in the marginal spots.',category='layout')
]
rec=complete('ega24_24_051',R,M,N,E,visual_notes='Both supplied scan parts read completely, including their overlap, all prose lines, underlines, baseline math indices, arrows, and the lower handwritten query. Enlarged the upper text to verify full-size baseline digits. The literal translator query and footnote are retained with checked French site45 references.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
