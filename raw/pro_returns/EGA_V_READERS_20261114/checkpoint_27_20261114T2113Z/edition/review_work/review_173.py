import sys,re,csv
from pathlib import Path
sys.path.insert(0,'edition/scripts')
from audit_record import save,source_path
from audit_late_helpers import MACROS,group
k='ega25_25_173';original=source_path(k).read_text();body=Path('edition/review_work/173_restored_body.tex').read_text();s='\n'.join(original.splitlines()[:4])+'\n'+body
R={
1:'The pale text is forward-reading in both original images; its physical origin remains unresolved. It is not omitted as a presumed blank sheet.',
2:'The upper cursive group permits nouveau EGA V. The tall left strokes permit IV or two slashes; both the reading and pen classification remain doubtful.',
3:'The heading permits17.16 and Formes quadratiques lisses, with an underline. The earlier draft16.2/Formes quadratiques libres is unsupported; all pale characters remain doubtful.',
4:'The entire upper-right area and all outer margins were inspected. No additional author folio or marginal wording can be securely recovered.',
5:'The full opening baseline was followed through Q, Sym with exponent2, both underlined E symbols, and the finite-rank parenthesis. All are faint and explicitly doubtful.',
6:'The complete baseline permits de sorte que Q and the interpretation phrase; the crossed word allows définit but remains uncertain.',
7:'The dual mark over E is a faint vee-like pen trace. The cancelled middle phrase remains illegible except for a tentative section; the live continuation ends forme biliné-.',
8:'The whole baseline was traced through B, two dual E symbols, the rightward arrow, and et passant aux. Each dual mark and the arrow remains tentatively classified as pen.',
9:'The determinant baseline contains a dual E-to-E arrow and the concluding une section; all letters, dual mark and arrow remain doubtful.',
10:'The display was examined symbol by symbol: d(Q), membership, Gamma, determinant(E), and a tensor-like exponent followed by2. The whole expression and pen classifications remain uncertain.',
11:'The complete baseline permits appelée (sauf erreur), the underlined discriminant phrase and Q. Lorsque; its faintness is preserved.',
12:'The opening formula permits E=O_S with a raised n-like pen stroke. The full matrix-description line and second O_S were followed and remain doubtful.',
13:'The line gives n lignes, n colonnes, Gamma O_S, and qui exprime Q. Notons tout; all are retained tentatively.',
14:'The short continuation de suite: is visible but faint.',
15:'The proposition heading and number16.2, s-membership-S, car k(s), not-equals2 and underlined ou were individually traced. All weak readings and pen classifications remain uncertain.',
16:'The full rank/parity baseline contains E tensor k(s), pair and the lisse criterion wording; no missing condition is supplied.',
17:'The full baseline permits non dégénérée, d(Q) soit inversible and D’ailleurs la condition est. An added opening parenthesis is faint and tentatively pen.',
18:'The continuation sans restriction sur S ni E and the closing added parenthesis are faint but visible; the whole line remains uncertain.',
19:'The full explanatory baseline begins La dernière assertion and ends des référen-; it was read through without borrowing certainty from the neighbouring page.',
20:'The continuation ces éventuelles through dans la première is visible but faint and remains doubtful.',
21:'The complete hypothesis line was followed, including non dégénérée, implique en effet and the final underlined E/rank phrase; all remain doubtful.',
22:'The baseline contains pair en tout point, car est2, and the beginning of the direct-proof phrase. Its faint reading remains qualified.',
23:'The continuation through caractéristique and the parenthetical se plaçant sur un corps was followed in full and retained tentatively.',
24:'A faint interlinear alg clos-like addition is visible. The derivative fraction, both partial signs, X_i index and two final cancelled s cells were examined individually; all remain doubtful.',
25:'The complete non-trivial-zero baseline was examined; the small pronoun permits ils but remains locally doubtful in addition to the overall faintness.',
26:'The characteristic-not-two baseline and its entire introductory formula phrase were followed; the inequality sign is tentatively pen.',
27:'The full display has2Q, equals, a sum-like pen sign, X_i and the derivative fraction. Its symbols, index and layer classifications remain uncertain.',
28:'The final derivative numerator has a Q/E-like trace, not a secure Q. Both partial signs, X_i and the rest of the full baseline were followed and remain doubtful.',
29:'The bottom baseline permits car k=2, a cancelled si E est de rang pair, and alors la forme bilinéaire B. The cancelled phrase and complete faint line remain doubtful; nothing beyond the page is completed.',
30:'The dark archive folio173 at the lower left is unambiguous handwriting.'}
d=[]
for i,line in enumerate(body.splitlines(),1):
 why=R[i]
 d.append(dict(line=i+4,before='Draft omitted faint page text',image=line,decision='observed' if line.startswith('%') else 'revised-with-uncertainty',reason=why,category='material-observation' if line.startswith('%') else 'faint-page-line'))
 for m in MACROS.finditer(line):
  j=group(line,m.end())
  if m.group(1)=='over':j=group(line,j)
  d.append(dict(line=i+4,before='Newly recovered local reading',image=line[m.start():j],decision='confirmed' if i==30 else 'retained-uncertain',reason=why,category=m.group(1)))
d.append(dict(line=6,before=r'\hand{173}',image=r'\hand{173}',decision='confirmed',reason=R[30],category='hand'))
notes=next(r['notes'] for r in csv.DictReader(open('source/transcription/ega_v_cote25/NOTES.tsv'),delimiter='\t') if r['key']==k).split(' | ')
answers=['The original scan is extremely faint, but enhanced views reveal a complete forward-reading body as well as the clear folio173. It is not recorded as blank.','Both originals and separately background-adjusted red, green and blue channels were inspected. Green preserves the text best. Eight enlarged bands cover every baseline. The physical origin of the impression cannot be established, and the neighbouring174 source supplied comparison proposals only; every recovered reading and weak pen layer remains explicitly doubtful.','There is no long marginal handwritten prose. The short upper heading, dual signs, arrows, algebraic symbols and insertion traces were each inspected and qualified for faintness.']
assert len(notes)==len(answers)
for i,(before,why) in enumerate(zip(notes,answers),1):d.append(dict(line=f'NOTES {i}',before=before,image=why,decision='reviewed',reason=why,category='source-note'))
r=save(k,s,d,0,'Both complete original image halves, all six separated-channel contrast views, and eight enlarged bands inspected. Every faint text baseline, formula, exponent, index, cancellation, interlinear trace and margin was followed to the limits of visibility. All pale readings remain uncertain; only the dark archive folio is confirmed without qualification.');print(k,len(d))
