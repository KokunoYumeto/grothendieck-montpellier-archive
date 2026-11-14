import sys,re,csv
from pathlib import Path
sys.path.insert(0,'edition/scripts')
from audit_record import save,source_path
from audit_late_helpers import MACROS,group
k='ega25_25_165';original=source_path(k).read_text();body=Path('edition/review_work/165_restored_body.tex').read_text();s='\n'.join(original.splitlines()[:4])+'\n'+body
reasons={
2:'The pale upper cursive heading allows nouveau EGA V; the two oblique margin strokes are weak and remain doubtful.',
3:'The second heading has EGA IV par and a question-mark-like ending; all are faint and retained tentatively.',
4:'The underlined title allows Ensemble singulier et supersingulier, not the previous draft title; the entire faint title remains uncertain.',
5:'The curving edge traces and upper-right spot were inspected; neither yields a secure additional bracket or folio numeral.',
6:'The entire first baseline was followed, including14,15 and the proposed replacement of S by Y; every pale reading remains doubtful.',
7:'The second baseline has15 ligne10, the short i.e. with two quote-like pen marks, and abusif; mot and absurde from the draft are unsupported. The whole faint line remains uncertain.',
8:'The line ends with an on en a-like group; the draft on songe is not supported. The entire baseline remains tentative.',
9:'The proposition number7 and page16 are the visible candidates on this full baseline; they and the text remain faint and uncertain.',
10:'The continuation starts et17 and describes the diagram; all words were followed across the line and remain tentative.',
11:'The reference reads page4 tentatively; its terminal colon is faint.',
12:'The complete diagram was followed in both overlapping images. The row, central column and two diagonals are visible; weak endpoints and labels are explicitly qualified.',
14:'A very pale zero-like trace stands above the upper differential object; it remains doubtful.',
15:'The upper object is over the central column, not over N. Its Omega, exponent1, X/Y index, tensor sign and coefficient with V1-like index were examined; all are faint. A short upward connector is retained with its weak head noted.',
16:'Every cell of the horizontal row was traced. The left and right endpoints are zero-like; N has a V1/X-like index, the central Omega has X/S-like index and a coefficient, and the right Omega has V1/S-like index. The arrows point right, with a rising diagonal from N and an upward central connector. The diagonal mu-like label remains uncertain.',
17:'The lower object belongs to the same central column and permits Omega1 Y/S tensor O V1; its upper connector and rising diagonal are visible. The small diagonal wr-like label remains doubtful.',
18:'A very faint lower zero-like endpoint and its upward connector can be followed at the top of the second image; its glyph remains doubtful.',
20:'The full line reads tentatively où N désigne le faisceau conormal and the following all-sheaves clause; the former illegible blocks are replaced only by doubtful readings.',
21:'The next baseline, its faint interlinear sur V1 and the lemma reference7 were followed. The M formula has Omega1 X/S, tensor and O V1-like traces; every weak symbol and the insertion layer remain tentative.',
22:'The complete two-sub-Modules baseline and its final Avec were examined and retained tentatively.',
23:'The line begins les notations, rather than the draft les conditions, and ends section a; its full text remains faint and doubtful.',
24:'The small crossed initial a, Hom(L,P), both interlinear mu labels and the two displayed-in-text maps were each examined. The target has X/Y-like and V1-like indices. All local readings and the insertion layers remain tentative.',
25:'The line contains a small interlinear pré, V(a), and a mu-like handwritten mark before strictement; its text and these additions remain uncertain.',
26:'A faint less-than sign precedes d, followed by rang M/Q, V(a)=V(D), and the definition-of-D clause. Every sign and letter remains tentative.',
27:'The first digit of the page15 reference has overlapping strokes; both layers are tentatively1. The rest reads inclusions de SS-préschémas lisses, retained as faint.',
28:'Two nearly parallel vertical margin strokes are visible beside the lower block; their pen classification and exact shape remain faint and tentative.',
29:'The displayed chain has V with exponent1, V with a small round exponent, and X, joined by two inclusion-like signs; the o exponent and all weak glyphs remain doubtful.',
30:'The line permits donnent une suite exacte (réf ?); the parenthetical reference request remains tentative.',
31:'The entire five-object exact row was inspected symbol by symbol. Its three internal terms begin with N-like letters, not the draft Hom; their V1/Vo/X indices, the first coefficient, all tensor/arrow signs and endpoints remain uncertain.',
32:'The full line d’autre part on a des isomorphismes canoniques was traced and retained tentatively.',
33:'Both isomorphism groups were traced. The first has N Vo/X, E and an O V1 coefficient; the second has N V1/Vo and Hom(W,K)-like letters. The two isomorphism signs and tensor sign are weak and remain doubtful.',
34:'The final baseline permits où W,K sont définis (page15) comme noyau et conoyau de; all words remain faint, and the sentence is not completed beyond the page.',
35:'The lower archive number165 is dark and unambiguous handwriting.'}
d=[]
for i,line in enumerate(body.splitlines(),1):
 if i in (1,13,19):continue
 why=reasons[i]
 d.append(dict(line=i+4,before='Draft passage re-read against this faint page',image=line,decision='observed' if line.startswith('%') else 'revised-with-uncertainty',reason=why,category='material-mark' if line.startswith('%') else 'faint-page-line'))
 for m in MACROS.finditer(line):
  j=group(line,m.end())
  if m.group(1)=='over':j=group(line,j)
  d.append(dict(line=i+4,before='New or revised local reading',image=line[m.start():j],decision='confirmed' if i==35 else 'retained-uncertain',reason=why,category=m.group(1)))
old_reasons={6:reasons[2],8:reasons[3],10:reasons[4],12:reasons[6],13:reasons[7],16:reasons[9],18:reasons[11],21:reasons[15],22:reasons[16],23:reasons[17],26:reasons[20],27:reasons[21],28:reasons[22],29:reasons[23],30:reasons[24],31:reasons[25],32:reasons[26],33:reasons[27],34:reasons[29],35:reasons[30]+' '+reasons[28],36:reasons[31],37:reasons[32],38:reasons[33],39:reasons[34],41:reasons[35]}
for m in MACROS.finditer(original):
 ln=original[:m.start()].count('\n')+1;j=group(original,m.end())
 if m.group(1)=='over':j=group(original,j)
 d.append(dict(line=ln,before=original[m.start():j],image=old_reasons[ln],decision='reviewed',reason=old_reasons[ln],category=m.group(1)))
notes=next(r['notes'] for r in csv.DictReader(open('source/transcription/ega_v_cote25/NOTES.tsv'),delimiter='\t') if r['key']==k).split(' | ')
answers=['Both originals and red, green and blue contrast-separated views were inspected, followed by enlarged bands covering every text baseline and diagram. The full faint forward-reading impression remains explicit; its physical origin is unresolved and every weak reading remains doubtful. The source text of166 provided comparison proposals only.','The two headings permit nouveau EGA V and EGA IV par ?, while the underlined title permits Ensemble singulier et supersingulier. All remain uncertain, replacing the unsupported draft title.','The diagram has a central differential column, a five-object horizontal row and two rising diagonals. Each object, index, endpoint, arrow and label was inspected; weak readings remain doubtful, and the former displaced column and missing nodes are corrected.','The two close vertical margin strokes are visible beside the lower sequence/isomorphism block; their faintness is retained.','The archive number165 is dark and clearly handwritten.','There is no long handwritten prose passage; all short marginal and interlinear pen-like traces were inspected, with their faint layer classifications kept tentative.']
assert len(notes)==len(answers)
for i,(before,why) in enumerate(zip(notes,answers),1):d.append(dict(line=f'NOTES {i}',before=before,image=why,decision='reviewed',reason=why,category='source-note'))
x=save(k,s,d,0,'Both complete original scan parts inspected, then red/green/blue separated background-adjusted views, eight enlarged text bands and three local diagram/heading crops. Every visible baseline, formula, node, arrow, index and margin was followed as far as the faint impression permits. Remaining uncertainty and unreadability are explicit; no certainty was imported from the neighbouring source.');print(k,len(d))
