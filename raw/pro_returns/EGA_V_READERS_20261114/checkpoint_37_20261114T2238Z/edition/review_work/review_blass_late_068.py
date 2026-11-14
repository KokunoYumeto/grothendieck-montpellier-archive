import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[
 (r'P^{\vee}',r'P^{\mathrm{v}}','The raised mark after P is a typed letter v. Its letter strokes and raised placement are visible in both scans.'),
 (r'\underline{E}^{\vee}',r'\underline{E}^{\mathrm{v}}','The raised letter after underlined E is typed v, retained at its observed level.'),
 (r'X \times_{P} L^{\circ}',r'X \mathrm{x}_{P} L^{\circ}','The product is typed with the ordinary lowercase x, with P visibly lowered after it.'),
 (r'$O_{X}(-1)$)',r'$0_{X}(-1)$)','The enlarged twisting expression has the narrow, tall zero glyph; the adjacent display has a visibly wider round O. Preserve this occurrence as zero.'),
 (r'then its image in $O_{X}$ forms an $O_{X}$ - regular sequence',r'then its image in $0_{X}$ forms an $0_{X}$ - regular sequence','Both ovals on this line are the narrow, tall zero type. Each was compared with the wider O in the display and tensor expression, without restoring mathematical notation.')
]
M={}
N=[
 'The upper-right 68 has a different serif face from the body and is retained as the page number. The scan alone does not establish the printing process.',
 'Enlarged comparison resolves the twisting expression and both regular-sequence expressions to narrow digit 0. The two displayed targets, the tensor quotient, and the target after G have the round O form. The decisions are occurrence-specific.',
 'Both closing square brackets, after situation and immersions, are present, while only the NB opening bracket is visible. Retain this bracket sequence.',
 'The two isolated top-left spots have no readable letter structure and are outside the text.',
 'The page body, formulas, heading underline and punctuation are typed; no handwritten addition is discernible in either scan.',
 'No long handwritten passage occurs. Both margins and the lower blank area were inspected.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d(7,'10.2','Typed heading with a straight typed underline','confirmed','All four characters and the underline are visible; no correction layer occurs.')
d(15,r'O_{X}(1)','Round typed O followed by lowered X and baseline (1)','confirmed','The first display has the wider O form; its letter and index placement remain unchanged.')
d(20,r'O_{X}','Round typed O with lowered X','confirmed','The enlarged target has the round O form, distinct in shape from the narrow zero in the preceding twisting line.')
d(26,r'O_{X}/J','Round typed O in the tensor quotient','confirmed','The oval in this occurrence is round and wide. The tensor sign, slash, arrow and raised 2 are typed and clear.')
d(29,r'G → O_{X}','Round typed O in the final NB homomorphism','confirmed','This target uses the round O form. There is no underline under G or O in the English scan.')
d('27–30','pull out of find out ... situation] ... immersions]','Literal wording and both closing brackets','retained_query_with_french_crossreference','Checked cote25 site59, §10.2, has the NB beginning “il faudrait quelque part dégager la situation générale avec un hom” and ending with the regular-immersion section. Blass types “of”, both alternative verbs, and two closing brackets; none is silently repaired.','cote24-query')
d('15–29','Ununderlined F, E, O/0, J and G in formulas','English symbols retain their local underlining and glyph forms','comparison-recorded','Checked cote25 site59 underlines the corresponding sheaf letters. Blass underlines E and F in the opening prose but leaves these display and later formula letters ununderlined, with three literal zero glyphs.','cote24-comparison')
d('9–30','Complete body and both formula displays','All words, formula signs, indices, punctuation, underlines and margins read','confirmed','The two supplied images overlap at the second display; every baseline was checked against the source, including the lowercase product x, raised v letters, colon before the second display, “announced”, “of find out”, and unmatched bracket sequence.','full-text')
rec=complete('ega24_24_068',R,M,N,E,visual_notes='Both supplied scan parts read completely, including the heading, two formula displays, overlapping display, NB, margins and blank lower area. Three enlarged O/0 crops establish occurrence-specific zero glyphs. The typed v letters, lowercase product x, all lowered indices and literal NB wording remain tied to their physical placement; the NB has an individual checked French59 cross-reference.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
