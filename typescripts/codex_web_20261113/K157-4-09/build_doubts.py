from pathlib import Path
import csv,re
OUT=Path(__file__).resolve().parent
TASK=OUT.parent.name

def cell(s):
 return str(s).replace('&','&amp;').replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
 return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)
def readrows(name):
 with (OUT/name).open(encoding='utf-8') as f:return list(csv.reader(f,delimiter='\t'))[1:]
def macros(s,name):
 pat=re.compile(r'\\'+name+r'\{')
 for m in pat.finditer(s):
  j=m.end();depth=1;k=j
  while k<len(s) and depth:
   if s[k]=='{' and (k==0 or s[k-1]!='\\'):depth+=1
   elif s[k]=='}' and (k==0 or s[k-1]!='\\'):depth-=1
   k+=1
  yield m.start(),s[j:k-1]
notation=readrows('notation_entries.tsv');doubts=readrows('reading_doubts.tsv')
s='# Notation table\n\nBuilt from the supplied images. Entries made during the second reading explicitly supersede the corresponding earlier reading where indicated; the audit preserves the change history. A font or letter candidate is a reading of the strokes, not a mathematical identification.\n\n'
s+=table(['Scan','Position','LaTeX / reading','Visible strokes and comparison'],notation)
s+='\n# Doubts\n\nThe following entries describe the individual image readings. Alternatives remain explicit in the transcription. Where surrounding text favours a candidate, that preference is recorded separately from the ink.\n\n'
s+=table(['Scan','Approximate location','Reading','Alternatives','Confidence','Ink and contextual preference'],doubts)
s+='\n## Complete current uncertainty-marker register\n\nThis register is generated from the current page files to ensure that no marked reading is omitted from the apparatus. TeX line numbers locate the deliverable, not an inferred manuscript line. The detailed entries above give the image position and confidence when separately assessed. For an additional marker not separately assessed above, confidence is conservatively low and no contextual preference is asserted. Repeated ambiguous glyphs are marked at their first occurrence on each page; their later occurrences follow that candidate.\n\n'
rows=[]
for p in sorted((OUT/'pages').glob('*.tex')):
 text=p.read_text();scan=re.search(r'scan(\d+)',p.name).group(1)
 for i,(at,value) in enumerate(macros(text,'unsure'),1):
  context=' '.join(text[max(0,at-55):min(len(text),at+len(value)+75)].split())
  rows.append([scan,f'TeX line {text.count(chr(10),0,at)+1}; marker {i}',value,context])
s+=table(['Scan','Location','All candidates in the marker','Immediate transcription context'],rows)
s+='\n# Slips kept as written\n\nNo emendation is made. Documentary alerts currently include the reworked indices and class names on scans 134, 137 and 142; the occurrence of `p_1(f)` beside a reference to 1.20 on scan 136; repeated numbering (1.23) on scans 135 and 137; the reference 1.25 on scan 137; the revised 3.8/3.9 labels on scan 145; the right-facing ≥ in card A on scan 146; and the missing card before one Hom bound and the lower j∈I on scan 146. These are retained readings, not mathematical error findings. The word on scan 143 is now marked fixé/fixe after the second reading; no claim of an unaccented spelling is established. All uncertain word endings and the deletion state of the last est on scan 147 remain reading questions.\n\n'
s+='## Abbreviations met\n\nEditorial expansions proposed only in this apparatus: `am.`, amalgamée(s); `catégorie` is sometimes prefixed by a universe symbol; `cf`/`cf.`, confer / voir; `cochgt`/`cochgt.`, cochangement; `comm.`/`comm,`, commutatif (terminal punctuation uncertain on scan 144); `cor.`/`Corollaire`, corollaire; `dép.`/`dep.`, dépendance; `Dém`/`Dèm`, démonstration; `ens.`/`ens`, ensemble; `Fl`, flèches; `fonct.`/`fonctlle`, fonctorielle; `hom.`, homomorphisme; `id`, identité; `i.e.`, id est; `c.à.d.` (uncertain alternative), c’est-à-dire; `loc cit.`, loco citato; `NB`, nota bene; `p.`, page; `p.e.`/`p.ex.`, par exemple; `p.a.` is an unresolved alternative on scan 138; `pet.`, petites; `p.r.`, par rapport; `p.v.`/`p.r.` on scan 142, unresolved (the first candidate follows that page’s own strokes); `th.`, théorème; `trans`/`trans.`, transition; `tt`, tout/toute; `acc.`, accessible; `coquar.`/`coquar`, coquarrable. `str.`, strictement; `isom.`/`isom`, isomorphisme; `syst.`, système; `cl.`/`cl`, classe; `élém.`/`élémts`, éléments (the competing reading élus remains unresolved); `à val.`, à valeurs; `lim.` (alternative to hom.), limite; `Ob`, objets; `Sup`, supremum; `card`/`Card`, cardinal. `Filt` is retained as a symbolic filtration name. Expansions do not settle disputed ink.\n\n'
s+='## Legibility\n\nThese are handwritten mathematical working pages. Reduced medial letters and endings, interlinear insertions, slanted cancelled notes and reworked indices require particular caution. Scans 134, 137, 138, 142, 145 and 147 contain especially dense overlapping correction layers; the cancelled slanted NB on 134, the rewritten indices on 142, and the bottom revision on 147 are among the least secure readings. All readings come from the supplied images; no OCR or external transcription is used. The completed audit records the full second reading and revisions, including the scan 134 preread-saving execution incident and the supplementary reading time for scan 137. These procedural details are retained rather than concealed.\n'
(OUT/f'{TASK}_doubts.md').write_text(s,encoding='utf-8')
print('Wrote doubts with',len(notation),'notation rows,',len(doubts),'detailed doubts and',len(rows),'current uncertainty markers')
