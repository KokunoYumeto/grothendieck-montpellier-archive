import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
N=['The top-right56 is in the regular separate serif face, with no pen alteration.','The sign after Z is a tall narrow left angle with two straight strokes. Retain the literal angle bracket, without interpreting it as a subset sign.','Both v letters after underlinedP are physically raised, typed lowercase v. Each occurrence was checked separately.','All words, arrows, inequalities, Greek symbols, underlines and the angle bracket have regular typed impressions; no secure handwriting is visible in either part.','No handwritten passage appears, long or short.']
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d(11,'only eliminate a set of codimention and such that','Literal codimention followed directly by and','comparison-recorded','Checked cote25 site49,8.15 continuation, reads “condition n’éliminant qu’un ens de codim≥2”. The bound≥2 and the opening parenthesis have no printed counterpart at this Blass position; no gap is silently filled.','cote24-comparison')
d(13,r'Z\langle\underline{P}^{v}','Z followed by a narrow left angle and underlinedP with raisedv','comparison-recorded','Checked cote25 site49 uses handwritten subset in “l’ensemble exceptionnel Z⊂P∨”. The visible Blass angle is preserved as an angle.','cote24-comparison')
d(20,'codimension ≥ K + 1','Typed capital K','comparison-recorded','Checked cote25 site50 Remords has a disputed overprinted R|2|k before+1. Blass’s unambiguous capitalK is retained but does not resolve the French ink.','cote24-comparison')
d(17,'Remorse:','Plain typed heading with colon','confirmed','No underline or hand layer is present; the surrounding paragraph starts directly after8.15.','heading')
d(21,'Proposition 8.16','Typed heading underlined','confirmed','All heading characters and its straight underline are clear in the lower image.','underline')
d('10–33','All formula indices and signs','Lowered xi and k(xi), raised v, lowered k and1, typed arrows and inequalities retained.','confirmed','Every attached Greek group was compared with standalone xi on the same page. The underlined Y is present except in the first x∈Y_xi; no underline is supplied there.','formula')
d('7–33','Body and page borders','Every prose line, reference and punctuation mark agrees with the scan.','confirmed','Retain the literal only eliminate, where complement, they should be unramified, repeated perhaps, and capitalK. Both parts and the blank lower margin were read to their edges; only isolated small stains appear.','full-text')
rec=complete('ega24_24_056',[],{},N,E,visual_notes='Both supplied images read completely, including overlap, all indices and symbols, the complete Remorse paragraph,8.16 and the start of its proof, and all blank margins. No text-reading correction was needed. The missing dimension bound, literal angle and capitalK are recorded against checked French49–50 without substitution.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
