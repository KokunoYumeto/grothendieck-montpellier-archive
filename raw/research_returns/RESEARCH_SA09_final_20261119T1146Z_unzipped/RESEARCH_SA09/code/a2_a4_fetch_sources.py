#!/usr/bin/env python3
"""Retrieve the exact primary sources used by the A.2/A.4 agent.

Downloads are not mathematical checks.  The retrieval log records which
URLs succeeded.  Existing successful downloads are reused.
"""
from pathlib import Path
import urllib.request
import time
import json

root=Path(__file__).resolve().parents[1]
sources=root/'sources'
tasks=[
 ('https://arxiv.org/src/0811.1480','buehler_0811.1480_source'),
 ('https://webhomes.maths.ed.ac.uk/~v1ranick/papers/doldpupp.pdf','dold_puppe_1961.pdf'),
 ('https://stacks.math.columbia.edu/tag/066Z','stacks_066Z.html'),
 ('https://stacks.math.columbia.edu/tag/0G99','stacks_0G99.html'),
]
results=[]
for url,name in tasks:
    p=sources/name
    t=time.perf_counter()
    if p.exists():
        results.append({'url':url,'file':str(p.relative_to(root)),'status':'reused','bytes':p.stat().st_size})
        continue
    try:
        with urllib.request.urlopen(url,timeout=40) as response:
            p.write_bytes(response.read())
        results.append({'url':url,'file':str(p.relative_to(root)),'status':'downloaded','bytes':p.stat().st_size,'seconds':time.perf_counter()-t})
    except Exception as exc:
        results.append({'url':url,'status':'failed','error':str(exc),'seconds':time.perf_counter()-t})
print(json.dumps(results,indent=2))
