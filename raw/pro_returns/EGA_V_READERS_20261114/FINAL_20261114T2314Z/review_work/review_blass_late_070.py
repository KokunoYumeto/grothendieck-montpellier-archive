import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[
 (r'${}^{\mathrm{V}}$N',r'${}^{\mathrm{v}}$N','Enlargement shows a small typed lowercase v raised before the full-height N; preserve the letter and its raised position.'),
 (r'\margin{* Ask Grothendieck}',r'\margin{\hand{* Ask Grothendieck}}','The entire lower-left starred Ask Grothendieck is pen, including the star. No secure punctuation follows the name.')
]
M={37:'The star and Ask Grothendieck are handwritten. The two relevant body stars are typed; the footer does not identify just one of them.'}
N=[
 'The enlarged mark before N is a small raised typed v. Its top and bottom are above the corresponding N positions; the raised placement is retained and the letter encoded lowercase.',
 'The first P, in the opening P^1, has a short straight typed underline. The later P^1 occurrences are ununderlined.',
 'The lower-left starred Ask Grothendieck is pen. It remains a footer, with the two starred body comments recorded separately rather than an invented exclusive attachment.',
 'The isolated spots at the upper-left edge have no readable textual form. All page margins were inspected.',
 'No long handwritten passage occurs; only the short starred footer is penned.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d(13,'just [58]','Literal bracketed 58 after just','retained_query_with_french_crossreference','Checked cote25 site60, final explanation after10.2, has tout juste abordée à l’heure actuelle in a parenthesis. Blass prints the bracketed number58 and a later close parenthesis without the corresponding opening one; no text is inserted.','cote24-query')
d(15,'in a certain measure (to some extent)','Both typed renderings remain','retained_query_with_french_crossreference','Checked cote25 site60 reads dans une certaine mesure. Blass’s parenthetical alternative is preserved.','cote24-query')
d(23,'raised v N° added regular immersions.*','Literal raised v, N°, quoted phrase and typed star','retained_query_with_french_crossreference','Checked cote25 site61 opens with the proposal for un nº en rabiot aux immersions régulières. The English notation and starred query remain without interpreting the raised v.','cote24-query')
d('24–25','Proposition 10.3 is crossed out. Ask AG if that is his intention.*','Typed statement and question by the translator','retained_query_with_french_crossreference','Checked cote25 site61 contains Proposition10.3, its formulas, the following explanatory paragraph, and the dimension≤1 transition. Blass omits these and prints this question about cancellation. The question is preserved as his observation, without making it the edition’s determination of the French cancellation.','cote24-query')
d(37,'* Ask Grothendieck','Handwritten footer query','retained_query_with_french_crossreference','Both preceding typed stars relate to checked cote25 site61: the proposed regular-immersion section and Blass’s question about Proposition10.3. The scan does not assign the footer exclusively to one.','cote24-query')
d('24–27','Transition directly from cancellation comment to Corollary10.4','No intervening English theorem body or dimension≤1 paragraph','comparison-recorded','Checked cote25 site61 retains the Proposition10.3 body, the explanatory exercise paragraph, and the S=Spec k, dimension≤1 paragraph before the corollary. The omission is recorded; no translation is supplied inside Blass’s text.','cote24-comparison')
d('8–9','all the fibers are ... smooth except at most a finite number','Literal English except','comparison-recorded','Checked cote25 site60 has the literal repeated wording toutes les fibres sont lisses sont au plus un nombre fini after the insertion about geometrically integral fibres. Blass’s English is retained independently.','cote24-comparison')
d('7,27,34','First P underline, Corollary10.4 underline, or underline','All are straight typed underlines with the visible scopes','confirmed','The first underline covers P alone, the heading underline ends after10.4, and the final one covers or only.')
d('7–37','All continuation prose, comment, corollary and footer','Every word, sign, index, underline, quote, bracket and margin read','confirmed','Both supplied scans and their overlap were read completely. The raised v was enlarged; P exponents, lowered s, k primes and k(s) are clear. The missing opening parenthesis before just, literal [58], and n- forms spacing remain.','full-text')
rec=complete('ega24_24_070',R,M,N,E,visual_notes='Both supplied scan parts read completely, from the fibration continuation through the unfinished corollary sentence and handwritten footer. The small raised v before N was enlarged and preserved. Blass’s omission of Proposition10.3 and its surrounding French paragraphs is recorded as an omission with his question retained; all translation alternatives and starred queries have exact checked French60–61 links.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
