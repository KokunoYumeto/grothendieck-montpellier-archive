"""Read-only source audit: inventory and exact duplicate candidates.

Only this agent's audit files are written. Other agents' bibliographies,
the consolidated bibliography and the manuscript are not modified.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, unicodedata

here = Path(__file__).resolve().parent
root = here.parent

def group(text,start):
    depth=1
    i=start+1
    while i<len(text):
        if text[i]=='\\':
            i+=2
            continue
        if text[i]=='{': depth+=1
        elif text[i]=='}':
            depth-=1
            if not depth: return text[start+1:i],i+1
        i+=1
    raise ValueError('unclosed group')

def entries(path):
    text=path.read_text()
    result=[]
    for m in re.finditer(r'@([A-Za-z]+)\s*\{',text):
        body,end=group(text,text.index('{',m.start()))
        key,rest=body.split(',',1)
        fields={}
        p=0
        while p<len(rest):
            f=re.search(r'(\w+)\s*=\s*',rest[p:])
            if not f: break
            name=f.group(1).lower()
            a=p+f.end()
            if rest[a]=='{':
                value,p=group(rest,a)
            elif rest[a]=='"':
                p=rest.index('"',a+1)+1
                value=rest[a+1:p-1]
            else:
                p=rest.find(',',a)
                if p<0:p=len(rest)
                value=rest[a:p].strip()
            fields[name]=value
        result.append({'key':key.strip(),'type':m.group(1),'file':str(path.relative_to(root)),**fields})
    return result

def normal(s):
    s=unicodedata.normalize('NFKD',s.lower())
    return ''.join(c for c in s if c.isalnum())

consolidated=entries(root/'RESEARCH_SA05_references.bib')
fragments=[]
for path in sorted(root.glob('part_*/*.bib')):
    fragments.extend(entries(path))

bytitle={}
byurl={}
for entry in consolidated:
    bytitle.setdefault(normal(entry.get('title','')),[]).append(entry['key'])
    if entry.get('url'):byurl.setdefault(entry['url'].replace('http://','https://'),[]).append(entry['key'])

def expand(path):
    text=path.read_text()
    result=[(str(path.relative_to(root)),text)]
    for m in re.finditer(r'\\input\{([^}]+)\}',text):
        child=root/m.group(1)
        if not child.suffix:child=child.with_suffix('.tex')
        result.extend(expand(child))
    return result

cites={}
for name,text in expand(root/'RESEARCH_SA05_paper.tex'):
    for m in re.finditer(r'\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}',text):
        for key in m.group(1).split(','):
            cites.setdefault(key.strip(),[]).append(name)

keys={e['key'] for e in consolidated}
fragment_keys={e['key'] for e in fragments}
result={
 'created_utc':datetime.now(timezone.utc).isoformat(),
 'scope':'Read-only audit against the current consolidated snapshot; owner files may change afterwards.',
 'consolidated_entries':len(consolidated),
 'entries_without_explicit_opened_or_not_obtained_mark':[
     {'key':e['key'],'note':e.get('note','')} for e in consolidated
     if not re.search(r'\b(opened|not obtained|not opened|retrieved)\b',e.get('note',''),re.I)],
 'same_normalized_title_candidates':{k:v for k,v in bytitle.items() if len(v)>1},
 'same_url_candidates':{k:v for k,v in byurl.items() if len(v)>1},
 'fragment_keys_absent_from_consolidation':sorted(fragment_keys-keys),
 'undefined_main_manuscript_citations':{k:v for k,v in cites.items() if k not in keys},
 'main_cited_keys':sorted(cites),
 'consolidated_inventory':consolidated,
}
(here/'audit_bibliography_output.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
with (here/'bibliography_inventory.tsv').open('w',newline='') as stream:
    fields=['key','title','author','year','url','note']
    writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',extrasaction='ignore')
    writer.writeheader();writer.writerows(consolidated)
small={k:v for k,v in result.items() if k not in ['consolidated_inventory','main_cited_keys']}
print(json.dumps(small,indent=2,ensure_ascii=False))
