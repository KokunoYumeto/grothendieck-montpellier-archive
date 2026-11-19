"""Read-only display of exact audit candidates and merged-problem sources."""
from pathlib import Path
import json,sys
P=Path(__file__).parent;R=P.parents[1]
if sys.argv[1]=='links':
    for n,x in enumerate(json.loads((P/'snapshot.json').read_text())['link_candidates_for_manual_review'],1):
        print(n,json.dumps(x,ensure_ascii=False))
elif sys.argv[1]=='merges':
    ids={'MP-SA21-6-09','MP-SA21-4-08','MP-SA21-7-08','MP-SA21-4-12','MP-SA21-8-07','MP-SA21-7-10','MP-SA21-9-08','MP-SA21-9-10'}
    for f in sorted((R/'parts').glob('*/problems.json')):
        for p in json.loads(f.read_text()):
            if p['id'] in ids:print(json.dumps(p,ensure_ascii=False,indent=2))
