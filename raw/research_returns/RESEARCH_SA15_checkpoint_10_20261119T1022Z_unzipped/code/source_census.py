"""One inspectable row per bibliographic source, preserving access limitations."""
from pathlib import Path
import csv,re,json
w=Path(__file__).resolve().parents[1]
def field(text,key):
 m=re.search(r'\b'+key+r'\s*=\s*\{',text,re.I)
 if not m:return ''
 start=m.end();depth=1;i=start
 while i<len(text) and depth:
  if text[i]=='{' and (i==0 or text[i-1]!='\\'):depth+=1
  if text[i]=='}' and (i==0 or text[i-1]!='\\'):depth-=1
  i+=1
 return ' '.join(text[start:i-1].split())
rows=[]
for entry in re.split(r'(?=^@)',(w/'RESEARCH_SA15_references.bib').read_text(),flags=re.M):
 m=re.match(r'@\w+\{([^,]+)',entry)
 if not m:continue
 note=field(entry,'note'); low=note.lower()
 if 'not obtained' in low or 'not opened' in low or 'not accessible' in low:
  access='Original full text not obtained; see precise note'
 elif 'unavailable' in low or 'preview' in low:
  access='Specified passage opened; full-work access limited'
 elif 'transcription' in low and 'original scan not obtained' in low:
  access='Transcription opened; original scan not obtained'
 else:access='Opened at the specified locators'
 rows.append(dict(key=m[1],author=field(entry,'author'),year=field(entry,'year'),title=field(entry,'title'),access=access,locators_and_limits=note,url=field(entry,'url') or ('https://doi.org/'+field(entry,'doi') if field(entry,'doi') else 'Supplied source or exact location in agent source log')))
rows.append(dict(key='MichelHuaWitness',author="Michel Hua's project",year='',title='Modernised reading of cote 9 in supplied archive',access='Not used',locators_and_limits='No remark from this witness is used in the paper; no source claim or fresh scan reading is attributed to it.',url='Supplied archive hua_project/'))
fields=list(rows[0])
with (w/'notes/SOURCE_CENSUS.tsv').open('w') as f:
 out=csv.DictWriter(f,fieldnames=fields,delimiter='\t');out.writeheader();out.writerows(rows)
md='# F.2: source census\n\nAccess is passage-specific. An opened publisher landing page does not count as an opened theorem. Historical failed attempts in the agent logs are superseded only when the current row records actual primary-text access.\n\n| Source key | Source | Access | Exact checked locators and limitations |\n|---|---|---|---|\n'
for r in rows:
 vals=[r['key'],f"{r['author']} ({r['year']}). {r['title']}",r['access'],r['locators_and_limits']]
 md+='| '+' | '.join(x.replace('|','\\|') for x in vals)+' |\n'
(w/'notes/SOURCE_CENSUS.md').write_text(md)
print(len(rows),'source census records written.')
