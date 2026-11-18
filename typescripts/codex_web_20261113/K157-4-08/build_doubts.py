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
s+='\n# Slips kept as written\n\nNo mathematical emendation is made here. The following are documentary alerts, not established corrections: scan 115 has unaccented `fut-ce`; scan 117 has two diagram labels read `p_1` beside prose `p_1,p_2`; scan 129 has two labels read `i_1(i_α(f))` and the phrase `limite projective`. Intended alternatives are not substituted for the visible writing. Any later discussion belongs to the mathematical notes after the freeze.\n\n'
s+='## Abbreviations met\n\nExpansions are editorial proposals and occur only here: `Cat.`, `Cat` and `ens.`, catégorie and ensemble; `cf`/`cf.`, confer / voir; `Cor`, corollaire; `def`, définition; `dég. de` (canceled, uncertain), degré de; `Fib`, fibrations; `Fl`, flèches; `h`, homotopiquement (explicit on scan 118); `hom.`/`hom`, homomorphisme; `ho.`, homotopique; `id`, identité; `ind.`, inductive; `iso.`/`isom`, isomorphisme; `Loc`, localisateur; `NB`, nota bene; `p.`, page; `p. ex`/`p. ex.`, par exemple; `p.-ê.` (alternative on scan 118), peut-être; `p.r.`, par rapport; `p.v.` (uncertain alternative), expansion unresolved; `s.` (uncertain reference suffix on scan 125), suivante(s); `sss`/`ssi`, si et seulement si; `syst.`, système; `Th.`/`th.`, théorème; `tt`, tout; `i.e.`, id est; `commut.`, commutation; `Génér.` (alternative on scan 126), généralités. The tiny Cat superscript `ens`/`et` remains unresolved; only `ens` admits the proposed expansion ensemble(s). These proposals do not resolve the source readings.\n\n'
s+='## Legibility\n\nThe typed sheet is substantially clearer than the mathematical working notes. The least secure readings are reduced word endings, crossed and overwritten letters, the title-cover contents references, and the successive old and replacement symbols in scans 127–131. Script capitals and the double stroke of Δ remain locally marked. No OCR or external transcription was used. The audit records each second-reading revision; a doubt mark represents retained uncertainty, not missing content.\n'
(OUT/f'{TASK}_doubts.md').write_text(s,encoding='utf-8')
print('Wrote doubts with',len(notation),'notation rows,',len(doubts),'detailed doubts and',len(rows),'current uncertainty markers')
