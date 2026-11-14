import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[
 (r'\binom{\hand{$r$}}{n}',r'\overset{\hand{r}}{\textstyle(n)}','At each occurrence the pen r is above an ordinary typed (n); the parentheses surround n alone. Preserve that physical arrangement rather than enlarging the parentheses around both lines.'),
 (r"(s) $0 \to E' \to E \to$",r"(s) $O \to E' \to E \to$",'The first exact-sequence endpoint uses the round wide capital O glyph. It was compared with the narrow digit0 below Hom on the same page.'),
 (r"$E'' \to 0$",r"$E'' \to O$",'The second endpoint also has the round wide capital O form, matching the first endpoint and differing from the narrow zero below Hom.'),
 (r'\underline{Hom}_{O_S}',r'\underline{Hom}_{0\mathrm{s}}','The enlargement shows narrow digit0 followed by lowercase s at the same lowered baseline. The source’s round O and doubly lowered capital S are not the printed forms.')
]
M={
 17:'The first numerator r is handwritten above the typed (n), with no pen change to either parenthesis or to n. The parentheses enclose only the lower typed n.',
 20:'The second r is likewise handwritten above the ordinary typed (n). Its long upright and short shoulder are clear; no other part of this coefficient is pen.'
}
N=[
 'Both r letters are pen; both typed pairs of parentheses surround n alone. The checked encoding now preserves that arrangement explicitly.',
 'Each index after E is a lowered capital S, compared with the smaller lowercase s elsewhere. Its following prime is raised back to the prime level; the first expression in the composed map also has a separate prime immediately after E.',
 'The Hom subscript is narrow0 followed by lowercase s on one common lowered level. Neither glyph is underlined. Both sequence endpoints instead use round capital O.',
 'The two complete representable-by-open-immersion lines are indeed typed twice. Both stay, including the repeated on the other hand.',
 'After sub-functor, the first Grass is underlined and its lower index is excluded; the second Grass is ununderlined and only its E is underlined. Retain both scopes.',
 'The upper-left dots and edge specks have no letter structure and are not added to the text.',
 'Only the two short pen r additions occur; all other body text, arrows, signs and underlines are typed.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d('26–27','Repeated representability sentence','Both identical typed lines are live','comparison-recorded','Checked cote25 site63 has the corresponding representability and d’autre part clause once. Blass’s repeated line remains.','cote24-comparison')
d('25,28','Grass_n(S)','Capital S in both parenthesized arguments','comparison-recorded','Checked cote25 site63 has lowercase s in the corresponding subfunctor argument. The English capital S is retained at both occurrences.','cote24-comparison')
d(17,'recovered from','Literal English words','comparison-recorded','Checked cote25 site63 reads peut être recouvert par. Blass’s recovered from remains; it is not silently rewritten as a different English verb.','cote24-comparison')
d(28,'fiber bundle','Literal English phrase','comparison-recorded','Checked cote25 site63 calls the same displayed object fibré vectoriel. Blass’s phrase contains no word vector; no word is supplied.','cote24-comparison')
d('20–21','O → E′ → E → E″ → O','Typed round O endpoints and four full arrows','comparison-recorded','Checked cote25 site63 records numerical0 endpoints and horizontal strokes without arrowheads at the two middle positions. Blass has four typed arrowheads and round O forms, retained as printed.','cote24-comparison')
d('23–24','E_S prime and E′_S prime','Lowered capital S with separately raised primes','comparison-recorded','Checked cote25 site63 places the base prime with S in the corresponding subscripted expressions. Blass’s prime strokes sit at the raised prime level and remain encoded at that observed position.','cote24-comparison')
d(28,'Hom lower0s','Narrow zero and lowercase s sharing a lowered baseline','comparison-recorded','Checked cote25 site63 uses underlined O with a lowered capital S. The English zero, lowercase s, common baseline and lack of underline are recorded literally.','cote24-comparison')
d('7–35','Complete prose and all formulas','Every word, index, arrow, prime, underline and margin read','confirmed','Both scans and the overlap were inspected completely. Enlarged crops checked both O endpoints, all three E indices, the Hom subscript, and the local baseline relationships. The repeated sentence, period after sub-functor and all underline exceptions remain.','full-text')
rec=complete('ega24_24_072',R,M,N,E,visual_notes='Both supplied scan parts read completely. Enlargements establish round O sequence endpoints, narrow0 plus lowercase s on a common lowered Hom-subscript baseline, and capital S with separately raised primes after E. The two handwritten r letters sit above typed (n), and each has its own layer decision. The duplicate representability line and all local underline differences remain.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
