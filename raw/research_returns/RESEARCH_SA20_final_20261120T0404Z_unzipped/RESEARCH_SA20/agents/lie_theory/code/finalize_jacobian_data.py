from pathlib import Path
import json,re,ast
base=Path(__file__).resolve().parents[1]
records=json.loads((base/'logs/all_exceptional_jacobians.json').read_text())['results']
rows=[{k:r[k] for k in ['type','orbit','diagram','orbit_dimension']} for r in records]
(base/'code/exceptional_orbits.json').write_text(json.dumps(rows,indent=2))
raw=(base.parents[2]/'source_external/lie_theory/sla_nilporb.gi').read_text()
# Compare all nonzero characteristics with the author's SLA orbit lists.
for kind in ['G2','F4','E6','E7','E8']:
 p=raw.index('type = "'+kind+'"');p=raw.index('list:=',p)+6;start=raw.index('[',p);level=0
 for i in range(start,len(raw)):
  level+=(raw[i]=='[')-(raw[i]==']')
  if level==0:arr=ast.literal_eval(raw[start:i+1]);break
 if kind=='G2':arr=[x[::-1] for x in arr]
 assert {tuple(r['diagram']) for r in rows if r['type']==kind and any(r['diagram'])}=={tuple(x) for x in arr}
 print(kind,'all characteristics match SLA list; G2 order reversed;',len(arr),'nonzero orbits')
def tex(name):
 name=name.replace('"',"^{\\prime\\prime}").replace("'","^{\\prime}")
 name=re.sub(r'([A-G])(\d+)',r'\1_{\2}',name)
 name=re.sub(r'([ab])(\d+)',r'\1_{\2}',name)
 name=name.replace('A_{1}s',r'\widetilde A_1').replace('A_{2}s',r'\widetilde A_2')
 return name
lines=[r'\begin{longtable}{@{}lp{29mm}p{91mm}@{}}',r'\toprule Type&Nonzero exponents&Nilpotent orbit labels\\\midrule\endhead']
for kind in ['G2','F4','E6','E7','E8']:
 groups={}
 for r in records:
  if r['type']!=kind:continue
  ex=tuple(r['nonzero_exponents'])
  if len(ex)>=2:groups.setdefault(ex,[]).append(r['orbit'])
 for ex,names in sorted(groups.items(),key=lambda a:(len(a[0]),a[0])):
  # Split long name lists so every row is modest in width/height.
  for first in range(0,len(names),5):
   ns=names[first:first+5]
   lines.append('$'+tex(kind)+'$&$'+r',\allowbreak '.join(map(str,ex))+'$&$'+r',\allowbreak\;'.join(map(tex,ns))+r'$\\')
lines += [r'\bottomrule',r'\end{longtable}']
(base/'jacobian_exceptional_table.tex').write_text('\n'.join(lines)+'\n')
