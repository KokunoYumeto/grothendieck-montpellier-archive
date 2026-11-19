from pathlib import Path
import re,json,csv
base=Path(__file__).resolve().parents[2]
out=base/'SA05/programs/outputs';out.mkdir(parents=True,exist_ok=True)
catalog=[]
for p in sorted((base/'sources').rglob('*')):
 if p.suffix not in ('.tex','.md'):continue
 lines=p.read_text().splitlines()
 row={'file':str(p.relative_to(base)),'lines':len(lines),'bytes':p.stat().st_size}
 row['scans']=[{'scan':m.group(1),'line':i+1} for i,s in enumerate(lines) if (m:=re.search(r'\\scanpage\{([^}]+)\}',s))]
 row['entries']=[{'entry':n+1,'line':i+1,'heading':s[4:]} for n,(i,s) in enumerate((i,s) for i,s in enumerate(lines) if s.startswith('### '))]
 catalog.append(row)
(out/'source_catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
for r in catalog:
 print(r['file'],r['lines'],'lines;',len(r['scans']),'scans;',len(r['entries']),'entries')
 if 'MPL_12_002-050_notes' in r['file']:
  print(json.dumps(r['entries'],ensure_ascii=False,indent=2))
