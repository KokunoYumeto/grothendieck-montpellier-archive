#!/usr/bin/env python3
"""Audit citations and numeric ID ranges in the finished SA08 prose.

No prose is edited. This mechanical identifier check does not assess the
mathematics; the separately authored review records the latter's scope.
"""
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs'
INT = ROOT / 'work/integration'
aliases = {r['original_id']:r['canonical_id'] for r in csv.DictReader((OUT/'SA08_id_aliases.tsv').open(),delimiter='\t')}
refalias = json.loads((INT/'reference_aliases.json').read_text())
known = set()
for fn in ['SA08_items.json','SA08_claims.json','SA08_problems.json']:
    known.update(r['id'] for r in json.loads((OUT/fn).read_text()))

def mkid(prefix,n):
    if prefix=='SA08-C':
        return prefix+f'{n:03d}'
    if prefix=='MP-SA08-':
        return prefix+f'{n:02d}'
    return prefix+str(n)

range_re = re.compile(r'(MP-SA08-|SA08-C|SA08-)(\d+)\s*[–—-]\s*(?:(?:MP-SA08-|SA08-C|SA08-|C))?(\d+)')
single_re = re.compile(r'(?:MP-SA08-\d+|SA08-C\d+|SA08-\d+)')
records, refs = [], []
for fn in ['SA08_dossier.md','SA08_directions.md']:
    for num,line in enumerate((OUT/fn).read_text().splitlines(),1):
        ids=set(single_re.findall(line))
        for m in range_re.finditer(line):
            prefix,low,high=m.group(1),int(m.group(2)),int(m.group(3))
            assert low<=high and high-low<500, m.group()
            ids.update(mkid(prefix,x) for x in range(low,high+1))
        for key in sorted(ids):
            target=aliases.get(key,key)
            while target in aliases and aliases[target]!=target:
                target=aliases[target]
            records.append({'file':fn,'line':num,'original_id':key,'canonical_id':target,'exists':target in known,'retired':target!=key})
        for key in re.findall(r'@([A-Za-z][A-Za-z0-9_:-]*)',line):
            refs.append({'file':fn,'line':num,'key':key,'canonical':refalias.get(key),'exists':key in refalias})

result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'counts':{'identifier_occurrences':len(records),'reference_occurrences':len(refs),
                  'retired_identifier_occurrences':sum(r['retired'] for r in records)},
        'unresolved_ids':[r for r in records if not r['exists']],
        'unresolved_refs':[r for r in refs if not r['exists']],
        'retired_ids':[r for r in records if r['retired']],
        'identifiers':records,'references':refs}
(INT/'prose_id_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['utc','counts','unresolved_ids','unresolved_refs','retired_ids']},ensure_ascii=False,indent=2))
