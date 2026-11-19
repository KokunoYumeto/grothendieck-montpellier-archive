#!/usr/bin/env python3
"""Serialize the manually verified bibliography and its reading scope."""
from pathlib import Path
import runpy,json
base=Path('/workspace/scratch/c38eb4e8f07f/SA18_work/parts/agent46')
refs=runpy.run_path(str(base/'data/references_data.py'))['references']
assert len({r['key'] for r in refs})==len(refs)
def esc(s):
    return str(s).replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('_','\\_')
parts=[]
for r in refs:
    fields={k:r[k] for k in ['author','title','year','url','doi','zbl'] if k in r}
    fields['note']=r['note']
    fields['annote']='Opened '+r['accessed']+'. Locator: '+r['locator']+'. Scope: '+r['verification_scope']
    fields['addendum']='First circulation: '+r['first_circulation']+' Publication: '+r['publication']
    parts.append('@misc{'+r['key']+',\n'+',\n'.join('  '+k+' = {'+(v if k in ['url','doi'] else esc(v))+'}' for k,v in fields.items())+'\n}')
(base/'references.bib').write_text('\n\n'.join(parts)+'\n')
(base/'data/references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
out={'references':len(refs),'verified':sum(r['note']=='verified' for r in refs),'unverified':sum(r['note']=='unverified' for r in refs),'metadata_only':[r['key'] for r in refs if 'metadata' in r['verification_scope'].lower() or 'frontmatter only' in r['verification_scope'].lower()]}
(base/'outputs/reference_build.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
