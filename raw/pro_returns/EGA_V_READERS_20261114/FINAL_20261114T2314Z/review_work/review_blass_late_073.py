import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[(r'^{\vee}',r'^{\mathrm{v}}','This occurrence is a raised typed letter v. Each E/G/P occurrence was inspected at its own position; the source wedge is replaced only by the visible letter, retaining its level.')]
M={}
N=[
 'All ten dual marks are raised typed v letters. Both isomorphism signs have a typed tilde above a straight stroke, as represented by simeq; no arrowhead or pen layer occurs.',
 'The 1 after lowered S in P_S{}^1 and the later S^1 are clear raised digits, not prime strokes. The first P alone is underlined.',
 'The isolated top-left marks are specks with no letter structure. The remaining margins and lower blank area were inspected.',
 'Every body word, formula sign and underline is typed; no handwritten material is discernible.',
 'No long handwritten passage occurs.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d(9,'(i.e., to say)','Typed parenthetical wording','retained_query_with_french_crossreference','Checked cote25 site64 reads savoir P(G) at this point. The English parenthetical rendering remains literal.','cote24-query')
d(10,'imposing','Typed underline over this word alone','retained_query_with_french_crossreference','Checked cote25 site64 inserts mais sans imposer le rang de G. Blass’s underlined verb remains without choosing another translation.','cote24-query')
d(32,'as follows','Typed underline over both words','retained_query_with_french_crossreference','Checked cote25 site64 ends the corresponding geometric-visualization sentence with ainsi. The English emphasis is retained.','cote24-query')
d('19–21','relative dimension m and that are of projective degree one','No intervening characterization clause is printed','comparison-recorded','Checked cote25 site64 includes ce sont les sous-préschémas fermés de P, lisses sur S et partout de dimension relative m between the two corresponding English phrases. Blass omits this entire clause; it is recorded here without filling the text.','cote24-comparison')
d(13,'and empty is n = 0','Literal is','comparison-recorded','Checked cote25 site64 reads et vide si n=0. The printed English is remains.','cote24-comparison')
d(17,'P_S{}^1 and S^1','Raised digit1 at both occurrences','comparison-recorded','Checked cote25 site64 has P with S′ in its subscript and then S′. The two English digit1 forms and their actual levels are preserved.','cote24-comparison')
d(24,'let E^v be its dual','Clear raised v after this E','comparison-recorded','Checked cote25 site64 literally has soit E son dual without a visible dual mark at that first definition, while later French occurrences carry marks. The English raised v is retained independently.','cote24-comparison')
d('7–34','Local letter underlines','Underlining varies by occurrence','confirmed','The first part has underlined Grass but ununderlined E/G; the later quotient letters E/G and final E are underlined, as is P in the last displayed isomorphism. These local scopes match the scan and are not extended.')
d('7–34','Complete body through let us','Every word, formula, raised letter, index, quote, underline and margin read','confirmed','Both supplied scans and their overlap were read fully. Retain isomophism, empty is, the line-break join in (r-1), all parentheses, the two tilde-plus-line signs, and the unfinished parenthetical at the foot.','full-text')
rec=complete('ega24_24_073',R,M,N,E,visual_notes='Both supplied scan parts read completely. Each of the ten raised v letters was checked individually along with both typed isomorphism signs, the two raised1 glyphs and all underline scopes. The omitted intrinsic-characterization clause is recorded against checked French64; Blass’s text remains unchanged at that omission.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
