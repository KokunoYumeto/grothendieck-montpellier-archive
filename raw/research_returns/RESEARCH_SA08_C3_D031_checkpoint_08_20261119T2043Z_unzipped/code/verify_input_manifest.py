#!/usr/bin/env python3
"""Verify only the supplied input manifest; do not alter the inputs."""
import csv, hashlib, json, pathlib, time
root=pathlib.Path(__file__).resolve().parents[2]
start=time.monotonic(); checks=[]
with (root/'inputs/MANIFEST.tsv').open(newline='') as f:
    for row in csv.DictReader(f,delimiter='\t'):
        file=root/'inputs'/row['path']
        actual=hashlib.sha256(file.read_bytes()).hexdigest()
        checks.append({'path':row['path'],'sha256':actual,'passed':actual==row['sha256']})
result={'scope':'All files listed by the supplied MANIFEST.tsv',
        'checks':len(checks),'passed':all(x['passed'] for x in checks),
        'elapsed_seconds':time.monotonic()-start,'files':checks}
(root/'deliverable/logs/input_manifest_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))
assert result['passed']
