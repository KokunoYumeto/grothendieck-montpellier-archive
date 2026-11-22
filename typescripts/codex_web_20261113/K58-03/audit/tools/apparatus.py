import csv,re,sys
from pathlib import Path
sys.path.insert(0,'out')
from tex_elements import arguments, page_path
root=Path('out');p=root/'K58-03_doubts.md'
notation=p.read_text().split('\n## Local doubts')[0].rstrip()
notation=notation.replace('In the cancelled/inserted functor clause the capital of F′ and the short map stroke are less clear.', 'In the insertion, the two arms identify F′; the shaft terminates without a separate head.').replace('The last argument is', 'The last argument is')
extra='''| 30–35, boundaries of cohomology maps | Headless horizontal strokes, asymmetric pen thickenings, deliberate triangular heads, sometimes with a separate tilde | Compared 30, line above équivalence; 31 (i); 33 (∗) and degree zero; 34, test-family comparison; and both rows on 35. Ordinary dash or an alternative to an arrow where the head is indistinct. |
| 32, items 3 and 5; 33, title | Initial F, abbreviated joined middle and detached mark before a final s | Fermés. Clear on 33, compatible with the amended plan on 32. |
| 35, last diagram column | Separate roof over a round open coefficient whose bottom lacks the prominent inflection in the G above | A local C/G question in the bottom-right argument. |'''
if extra.splitlines()[0] not in notation:notation+='\n'+extra
rr=list(csv.DictReader((root/'audit/frozen_places.tsv').open(),delimiter='\t'))
def esc(t):return t.replace('|',r'\|').replace('\n',' ')
def code(t):return chr(96)+esc(t)+chr(96)
text=[notation,'','## Local doubts','',
'The table records the reading at the freeze. The last table records what changed when the other transcription and the image were compared. Letter case, an empty contact between strokes and the position of a pen mark can be more significant than the grammatical or mathematical fit. The files named here can be regenerated from the supplied scans using the crop coordinate table.','',
'| Scan and place | Approximate location | Reading | Other readings allowed by the ink | Confidence | Crop and distinguishing stroke | Preference from context |','|---|---|---|---|---|---|---|']
for r in rr:
 vals=r['frozen reading'].split('|')
 text.append('| '+' | '.join([r['id'],esc(r['place']),code(vals[0]),', '.join(code(v) for v in vals[1:]) or '—',r['confidence'],code(r['crop'])+'. '+esc(r['stroke']),esc(r['context'])])+' |')
text+=['','## Slips and anomalous forms retained','','| Scan and place | Visible form | Possible intended form and grounds |','|---|---|---|',
'| 20, second line of text | A colon between the barred f-prime and lambda inverse | A composition sign would give the application being discussed. The crop shows two vertically separated dots. The colon is certain; the proposed intention is editorial. |',
'| 25, diagonal note at the local spectrum | A closing parenthesis followed by a prime, with no comparably clear opening parenthesis before Spec | The punctured-spectrum notation elsewhere on 21 encloses the spectrum. The unmatched visible parenthesis is kept. |',
'| 35, opening of case b | A v-like glyph in the degree equation | The degree cases above use i. The shape remains marked, so an authorial slip cannot be distinguished from handwriting. |',
'', 'Unaccented capitals in the typewritten headings and the form procèdera on 24 follow the page. An uncertain ending in the handwritten notes has not been classified as a spelling error.','',
'## Abbreviations and their possible expansions','',
'| Form | Likely expansion | Form | Likely expansion |','|---|---|---|---|',
'| Ass | associés, ensemble des idéaux ou points associés | prop. | proposition |',
'| C.Q.F.D., CQFD, cqfd | ce qu’il fallait démontrer | cor., Cor. | corollaire |',
'| th., thé., th | théorème (sometimes théorie in running text) | Déf | définition |',
'| tt, tte | tout, toute | pt | point |',
'| dim | dimension | loc. | localement, local, locaux, according to the noun |',
'| noeth, noeths | noethérien, noethériens | gén. | générique or général, according to the line |',
'| géom., géométriquemt | géométrique, géométriquement | universellt, univ. | universellement |',
'| formellt | formellement | équidim. | équidimensionnel |',
'| resp | respectivement | par. | paragraphe |',
'| Nᵒ, nᵒ | numéro | cf, cf. | confer, comparer |',
'| coh. | cohérent, cohérents | imm. | immersion |',
'| p. ex., p.ex. | par exemple | i.e. | id est |',
'| mod., Mod. | module, modules | ple. fid. | pleinement fidèle |',
'| prof | profondeur | ext. | extension |',
'| isom | isomorphisme | mono | monomorphisme |',
'| inj, surj | injectif, surjectif | hom | homomorphisme |',
'| hyp. | hypothèse | réc. | récurrence |',
'| tq | tel que | ens | ensemble |',
'| N.B. | nota bene | Ex | exemple |',
'| EGA | Éléments de géométrie algébrique | Pic | Picard |',
'| LG | Lefschetz-Grauert | π₁ | groupe fondamental in the outlined applications |','',
'## Legibility','',
'The typescript body and the large manuscript headings are legible throughout. Some symbols on typed sheets are pen additions, and the copy clips one word on scan 22. The hardest places are the superimposed revisions and left insertion of 30, the deeply cancelled observations and the end of (ii) on 31, the small boxed and diagonal notes on 33–34, and the distinction between a headless shaft and a slight terminal accumulation of ink on 35. Scan 27’s last bound and scan 35’s last diagram object retain a conflict between their letterforms and their expected roles.']
p.write_text('\n'.join(text)+'\n')
