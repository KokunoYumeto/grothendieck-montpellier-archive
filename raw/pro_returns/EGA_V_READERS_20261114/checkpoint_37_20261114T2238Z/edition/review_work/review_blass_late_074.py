import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[
 (r'N$^{o1}$s',r'N$^{\circ}$\raisebox{0.5ex}{1}s'+'\n% NOTE: The printed degree circle and digit1 have separate levels: 1 is raised partway above N/s, while the circle is higher. The local raisebox records that physical displacement without interpreting the extra digit.\n','Enlargement shows a floating circle, then a full-height digit1 raised partway above the N/s baseline. The circle is higher than the digit’s baseline; preserve the two positions rather than making o and1 one superscript string.'),
 (r'\margin{* Ask AG or Deligne about the best word.}',r'\margin{\hand{* Ask AG or Deligne about the best word.}}','The entire starred footer is handwritten, including its final small period. The wording and names are clear.')
]
M={35:'The star, Ask AG or Deligne about the best word, and final period are penned. The matching star after [sorites Fr] is typed.'}
N=[
 'The sign between the two P expressions is an ordinary typed capital C, with no arrow shaft, equality or extra stroke. It remains literal C.',
 'Both P_S{}^1 and L_S{}^1 have lowered capital S followed by a clearly raised digit1. The final E_S1 has lowered capital S but its digit1 returns to the E baseline; enlargement confirms that difference.',
 'The handwritten starred footer is clear and matches the single typed star after [sorites Fr]. Its whole layer is now explicitly marked as hand.',
 'Only the short starred footer is pen. The body queries, alternative letters, brackets, underlines and all formula signs are typed.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d(7,'again','Typed underline over again alone','retained_query_with_french_crossreference','Checked cote25 site65 has appelés encore hyperplans de P. Blass’s underlined again remains.','cote24-query')
d(11,'[by which of course we mean]','Literal typed square-bracketed phrase','retained_query_with_french_crossreference','Checked cote25 site65 has the parenthetical par quoi bien sûr on entend. The English bracket choice and placement remain.','cote24-query')
d(15,'G or Q [illegible]','Typed letter alternatives and explicit gap','retained_query_with_french_crossreference','Checked cote25 site65 retains a doubtful underlined G in quotient loc libre G de E dont il provient. Blass’s G-or-Q alternatives and gap remain unfilled and do not settle the French letter.','cote24-query')
d(22,'[sorites Fr]*','Typed French word label and single star','retained_query_with_french_crossreference','Checked cote25 site65 reads Voici un minimum de sorites dont on devra disposer. Blass’s untranslated word and star remain.','cote24-query')
d('23–24','(only when) until','Both typed alternatives','retained_query_with_french_crossreference','Checked cote25 site65 says ne pourra ... être fixée qu’une fois que. Both English renderings remain.','cote24-query')
d(27,'[commode Fr]','Typed French-word bracket','retained_query_with_french_crossreference','Checked cote25 site65 begins its handwritten addition Il me semble commode d’introduire. The English bracket is preserved.','cote24-query')
d(29,'[illegible ask AG]','Literal typed gap/query after E_S1','retained_query_with_french_crossreference','Checked cote25 site65’s handwritten addition defines the functor by quotients loc libres de rang non précisé of E over S′ and continues Alors ... représentable par. Blass places this query at that transition; no text is inferred into it.','cote24-query')
d(33,'[slightly illegible confirm with AG]','Literal typed query after not connected','retained_query_with_french_crossreference','Checked cote25 site65’s final handwritten NB reads le rang i.e. la dim relative peut varier si S non connexe, with its own unmatched bracket/parenthesis. Blass’s confirmation request remains, as does his unclosed NB opening bracket.','cote24-query')
d(35,'* Ask AG or Deligne about the best word.','Handwritten footnote','retained_query_with_french_crossreference','Its star refers to [sorites Fr] above, corresponding to checked cote25 site65’s minimum de sorites sentence. No replacement word is proposed.','cote24-query')
d(12,'points of L','L has no raised zero or circle here','comparison-recorded','Checked cote25 site65 has points de L^o. Blass retains the raised0 in his first L occurrence but omits it in this points phrase.','cote24-comparison')
d('12–20,28–29','Raised1 and baseline1 forms','Digits retain their observed positions','comparison-recorded','Checked cote25 site65 uses S′ and G′. Blass has raised1 after S/P_S/L_S and after G in five occurrences, while the final E_S1 has a baseline1. These are preserved separately.','cote24-comparison')
d('17–18','Capital C and in so far as ... G1 is majorized','Literal English link and wording','comparison-recorded','Checked cote25 site65 uses a handwritten hook arrow and then ssi before G′ est majoré. Blass prints capital C and has no explicit if-and-only-if wording at that position. No logical connective is inserted.','cote24-comparison')
d('28–32','Grass without star/bullet; n≥0 Grass_n(E)','No coproduct sign appears','comparison-recorded','Checked cote25 site65’s handwritten addition has doubtful star/bullet indices and an explicit coproduct sign over n≥0. Blass omits those functor indices and the coproduct sign, leaving the literal baseline n≥0 Grass_n(E).','cote24-comparison')
d('7–35','Entire section ending and footer','All words, alternatives, indices, signs, brackets, underlines and margins read','confirmed','Both supplied scans were read completely. Enlargements establish the distinct levels in N-circle-1-s and E_S1. The footer is clear; occured, the capital C, unmatched NB bracket, and all translator queries remain.','full-text')
rec=complete('ega24_24_074',R,M,N,E,visual_notes='Both supplied scan parts read completely, including the section-ending functor addition and handwritten footer. Every printed query/alternative has a separate checked French65 cross-reference. The raised1 and baseline1 occurrences were checked independently; the N-circle-1-s group was enlarged and its two raised levels retained. Section11 ends on this page.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
