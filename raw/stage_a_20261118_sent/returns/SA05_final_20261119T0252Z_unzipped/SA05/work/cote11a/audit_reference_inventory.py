"""Read all four scopes' bibliography records; identity decisions are authored separately."""
import pathlib,re,json,csv,collections,hashlib
R=pathlib.Path('SA05/work');out=R/'cote11a'
def braced(s,i):
 assert s[i]=='{';depth=1;j=i+1
 while j<len(s):
  if s[j]=='\\':j+=2;continue
  if s[j]=='{':depth+=1
  elif s[j]=='}':
   depth-=1
   if depth==0:return s[i+1:j],j+1
  j+=1
 raise ValueError('unclosed brace')
def parse_bib(path):
 s=path.read_text();rows=[];i=0
 while m:=re.search(r'@(\w+)\s*\{([^,]+),',s[i:]):
  start=i+m.start();pos=i+m.end();_,end=braced(s,s.index('{',start));body=s[pos:end-1];row={'key':m.group(2).strip(),'bib_type':m.group(1).lower()};p=0
  while fm:=re.search(r'([A-Za-z_][A-Za-z_0-9-]*)\s*=\s*',body[p:]):
   k=fm.group(1);a=p+fm.end()
   if body[a]=='{':v,b=braced(body,a)
   elif body[a]=='"':b=body.index('"',a+1)+1;v=body[a+1:b-1]
   else:
    b=body.find(',',a);b=len(body) if b<0 else b;v=body[a:b].strip()
   row[k]=v;p=b
  rows.append(row);i=end
 return rows
allrows=[];snapshots=[]
jsonnames={'root':'references.json','cote11a':'references_metadata.json','cote12c':'reference_records.json'}
tsvnames={'root':'reference_ledger.tsv','cote11a':'reference_checks.tsv','cote11b':'reference_checks.tsv','cote12c':'reference_ledger.tsv'}
for scope in ['root','cote11a','cote11b','cote12c']:
 path=R/scope/'references.bib';rows=parse_bib(path)
 extra={}
 if scope in jsonnames:
  jp=R/scope/jsonnames[scope];j=json.loads(jp.read_text());extra={r['key']:r for r in j};snapshots.append({'file':str(jp),'sha256':hashlib.sha256(jp.read_bytes()).hexdigest()})
 tp=R/scope/tsvnames[scope];ledger=list(csv.DictReader(tp.open(),delimiter='\t'));ledg={r.get('key',r.get('reference_key',r.get('ref_key'))):r for r in ledger}
 for row in rows:
  row={'scope':scope,'source_bib':str(path),**row,'metadata':extra.get(row['key'],{}),'verification_record':ledg.get(row['key'],{})};allrows.append(row)
 snapshots.append({'file':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'entries':len(rows)})
 print(scope,len(rows))
(out/'reference_audit_inventory.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2)+'\n')
(out/'reference_audit_snapshot.json').write_text(json.dumps(snapshots,ensure_ascii=False,indent=2)+'\n')
print('Total records',len(allrows))
for key,group in sorted(collections.defaultdict(list).items()):pass
d=collections.defaultdict(list)
for r in allrows:d[r['key']].append(r)
print('Repeated keys:',{k:[r['scope'] for r in v] for k,v in d.items() if len(v)>1})
print('All records read from supplied workspace bibliography/ledger files; no external library access.')
