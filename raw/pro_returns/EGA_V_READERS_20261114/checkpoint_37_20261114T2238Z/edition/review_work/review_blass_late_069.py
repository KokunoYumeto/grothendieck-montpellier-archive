import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[(r'\margin{* Ask AG}',r'\margin{\hand{* Ask AG}}','The star and Ask AG at the lower left are handwritten, with no securely attached periods after the initials.')]
M={38:'The complete footer is a penned star followed by Ask AG. Its matching body stars are typed. No extra punctuation is supplied.'}
N=[
 'The upper-right 69 is in a different serif face and remains the page number.',
 'The star after the mystery parenthesis and the star after the literal [illegible] are typed. The separate lower-left star and Ask AG are pen and now explicitly marked as such.',
 'The sign is the typed phi glyph; the following xi is visibly lowered. The standalone xi before membership has its ordinary text-level placement. These clear English letters do not resolve the French uncertainties.',
 'Only the short starred footer is handwritten. All body lines, formula letters, underlines, and both margins were inspected.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d(16,'catching up indicated in No. 1','Typed underlined phrase, ending in digit 1','retained_query_with_french_crossreference','Checked cote25 site60 has the parenthetical rattrappages signalés with handwritten nº12 and a cancelled suivant. Blass’s underlined wording and literal No.1 remain.','cote24-query')
d(18,'above five lines a mystery).*','Typed comment, underlined inside its parentheses, followed by typed star','retained_query_with_french_crossreference','This comments on the preceding translation of checked cote25 site60, from Pour comprendre through the opening construction of bons pinceaux linéaires. The comment and the repeated following translation are preserved.','cote24-query')
d(19,'indicated or anticipated','Both typed alternatives remain in the repeated sentence','retained_query_with_french_crossreference','Checked cote25 site60 reads signalés in the preceding parenthesis and indiquées in the following pencil construction. Blass retains the alternatives at this repeated transition; no single wording is selected.','cote24-query')
d(20,'[illegible]* 5.3.','Literal typed gap label and star before 5.3','retained_query_with_french_crossreference','Checked cote25 site60 has a handwritten insertion retained as notamment pour S.3.|notamment pour 5.3. in the catching-up parenthesis. Blass’s explicit gap remains unfilled.','cote24-query')
d(38,'* Ask AG','Handwritten shared footer query','retained_query_with_french_crossreference','The two typed stars refer to the translation difficulty in checked cote25 site60’s opening paragraph and its inserted reference. Each starred body query has its own record.','cote24-query')
d('13–22','Two overlapping versions of the opening explanation','All repeated clauses are typed and live','comparison-recorded','Checked cote25 site60 has one continuous opening paragraph. Blass prints the first five-line attempt, its mystery comment, and a repeated transition/construction. All are retained.','cote24-comparison')
d(15,'L in P','No dual mark over or after this P','comparison-recorded','Checked cote25 site60 supplies a handwritten dual mark at the corresponding P. Blass’s ordinary P is retained.','cote24-comparison')
d('24–25','xi, phi_xi, X_k(xi)','Clear typed xi and phi, with the attached indices visibly lowered','comparison-recorded','Checked cote25 site60 retains xi|zeta and phi|emptyset uncertainties in these occurrences. The clear English type is recorded independently and does not settle the French ink.','cote24-comparison')
d(28,'is used only','Literal only','comparison-recorded','Checked cote25 site60 says utilisé surtout. Blass’s only remains as typed.','cote24-comparison')
d(30,'which according to 10.2','Literal English wording','comparison-recorded','Checked cote25 site60 reads qu’après 10.2 in its ordering of the reformulation. The English phrase is not rewritten.','cote24-comparison')
d(36,'codimension two','Clear word two without an inequality sign','comparison-recorded','Checked cote25 site60 has 2 preceded by a doubtful cancellation/greater-or-equal mark. English two is preserved without resolving that French layer.','cote24-comparison')
d('7–38','Entire theorem, explanation and footer','All words, punctuation, indices, arrows, quote marks, underlines and margins read','confirmed','Both scan parts were inspected fully, including the overlap, the typed No.1, both 5.3 references, the repeated construction sentences, X-isomorphism wording without an inserted hyphen, and the lower handwritten query.','full-text')
rec=complete('ega24_24_069',R,M,N,E,visual_notes='Both supplied scan parts read completely. The theorem statement, repeated translation attempt, underlined mystery comment, explicit [illegible] gap, all Greek letters and their levels, and the handwritten starred footer were checked individually. Each query has a checked French60 context; the theorem itself corresponds to the end of French59.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
