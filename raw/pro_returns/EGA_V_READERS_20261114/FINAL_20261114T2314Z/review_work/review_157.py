import sys,re,csv
from pathlib import Path
sys.path.insert(0,'edition/scripts')
from audit_record import save,source_path
from audit_late_helpers import MACROS,group
k='ega25_25_157'
original=source_path(k).read_text()
head='\n'.join(original.splitlines()[:4])+'\n'
body=Path('edition/review_work/157_restored_body.tex').read_text()
s=head+body
reasons={
2:'The pale cursive marginal heading allows nouveau EGA V; all its letters remain doubtful.',
3:'The heading, crossed old heading and interlinear cursive replacement were individually inspected; Formes lisses and the proposed replacement remain faint and tentative. The crossing strokes are visible.',
4:'Pale long curved traces at the upper left follow the sheet edge. Their material or writing origin remains unresolved; they are recorded as an image observation without assigning a textual bracket.',
5:'The full opening baseline was followed; NB, Je viens de m’apercevoir and the following terminology clause remain readable only tentatively.',
6:'The pale typed baseline and interlinear SUP were inspected; the lengthy final words remain doubtful, and no certainty is borrowed from the neighbouring source.',
7:'The baseline concerning terminologie reçue was traced; the final a/s cancellation remains tentative.',
8:'The repeated t-like mark and the entire definition1 correction clause were examined; the repeated letter and the words remain tentative.',
9:'The non dégénérée quotation and following dimension-paire line are visible in the contrast views but remain faint throughout.',
10:'The cancellation, appended s and equation were examined separately; the undertext and phi are tentative, while their positions are retained.',
11:'This complete baseline about an ambient odd dimension was traced in the original and contrast views; the wording remains tentative.',
12:'The cancelled short group and opening handwritten quotation mark were examined; the erased group remains a candidate reading.',
13:'The overprinted d area, closing quote, ordinary-quadratic phrase and phi were traced; all weak readings remain marked.',
14:'The two quotation marks and the complete following clause were examined; the accent/layer on dû is too weak to classify confidently, so only a doubtful word is supplied.',
15:'The full odd-number-of-variables baseline is visible but remains tentative.',
16:'The full cone-origin baseline was inspected; no clean certainty is asserted from the adjacent page.',
17:'The equation x²+yz=0 and ensuing clause were followed symbol by symbol; the faint equation and words remain tentative.',
18:'The beginning of this line overlaps the two image parts; it is transcribed once. The small cancelled f and the lisse/ordinaire words remain tentative.',
19:'The parenthetical Module baseline was followed across the page; its reading remains tentative.',
20:'The broad hand-drawn implication sign, its two surrounding terms and the rank-pair clause were inspected; all are retained as faint readings.',
21:'The underline, base-S clause and handwritten comparison sign were inspected; the sign and its 2 remain tentative.',
22:'The complete supersingulière terminology baseline was traced, with its weak letters left doubtful.',
23:'The struck group is visible but its beginning remains unreadable; only the tentative ending de mon texte is recovered before de SUP.',
24:'The non dégénérée line and a faint f/r overprint were inspected; both layers remain tentative.',
25:'The point-supersingulier baseline was traced; its abbreviation and words remain doubtful.',
26:'The geometric-supersingularity baseline was traced in full and remains tentative.',
27:'The whole displayed-in-text comparison map was inspected, including both M/m letters, exponent2, gr subscript and long arrow; every faint symbol remains doubtful.',
28:'The kernel clause was traced from its left edge to the right edge and retained as a tentative reading.',
29:'The full line beginning non dégénérée and ending zéro singulier was followed; its letters remain tentative.',
30:'The final baseline and the appended final e were inspected; the clipped continuation ends at zéro and is not completed.',
31:'The archive folio157 is dark, handwritten and unambiguous.'}
d=[]
for i,line in enumerate(body.splitlines(),1):
 if i==1: continue
 d.append(dict(line=i+4,before='Omitted in source transcription (except folio)',image=line,decision='observed' if line.startswith('%') else 'restored',reason=reasons[i],category='material-mark' if line.startswith('%') else 'faint-page-line'))
 for m in MACROS.finditer(line):
  j=group(line,m.end())
  if m.group(1)=='over':j=group(line,j)
  d.append(dict(line=i+4,before='Omitted visible layer',image=line[m.start():j],decision='retained-uncertain' if m.group(1) in ('unsure','illegible') else 'restored',reason=reasons[i],category=m.group(1)))
notes=next(r['notes'] for r in csv.DictReader(open('source/transcription/ega_v_cote25/NOTES.tsv'),delimiter='\t') if r['key']==k).split(' | ')
answers=['Both original images and contrast-adjusted channel views show a complete forward-reading text with heading revisions and marginal marks. Its physical origin remains unresolved, but omission as blank is unjustified. Each visible baseline is restored with extensive uncertainty; the adjacent source transcription supplied comparison proposals only, never certainty.','The lower157 is dark and unambiguous handwriting.','The pale handwritten heading, insertions, overwrites, quotation marks, symbols and curved edge traces were inspected along with every typed baseline.']
for i,(before,why) in enumerate(zip(notes,answers),1):d.append(dict(line=f'NOTES {i}',before=before,image=why,decision='reviewed',reason=why,category='source-note'))
for m in MACROS.finditer(original):
 line=original[:m.start()].count('\n')+1
 d.append(dict(line=line,before=original[m.start():group(original,m.end())],image=r'\hand{157}',decision='confirmed',reason='The original source’s only transcribed handwritten content,157, is clearly present at the foot.',category=m.group(1)))
x=save(k,s,d,0,'Both original scan parts inspected completely, then green-channel and background-adjusted views and six enlarged bands compared line by line. All visible baselines and margins were read as far as the faint image permits; unresolved characters remain explicitly doubtful or unreadable. No claim is made that the pale physical impression is a carbon rather than show-through.');print(k,len(d))
