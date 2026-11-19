"""Verify an existing archive's CRC, embedded file hashes and duplicate-name bytes."""
from pathlib import Path
import argparse,csv,hashlib,io,json,time,zipfile,collections
p=argparse.ArgumentParser();p.add_argument('archive');p.add_argument('--output',required=True);a=p.parse_args()
start=time.perf_counter();archive=Path(a.archive)
with zipfile.ZipFile(archive) as z:
    bad=z.testzip();assert bad is None,bad
    names=z.namelist();duplicates={n:c for n,c in collections.Counter(names).items() if c>1}
    duplicate_equal={}
    for name in duplicates:
        hashes={hashlib.sha256(z.read(info)).hexdigest() for info in z.infolist() if info.filename==name}
        duplicate_equal[name]=len(hashes)==1
    manifests=[n for n in names if n.startswith('CHECKPOINT_') and n.endswith('_FILES.tsv')]
    if 'DELIVERY_MANIFEST.tsv' in names: current='DELIVERY_MANIFEST.tsv'
    else: current=sorted(manifests)[-1]
    mismatches=[];checked=0
    for row in csv.DictReader(io.StringIO(z.read(current).decode()),delimiter='\t'):
        name=row['path']
        if name not in names: mismatches.append([name,'missing']);continue
        actual=hashlib.sha256(z.read(name)).hexdigest();checked+=1
        if actual!=row['sha256']:mismatches.append([name,'hash differs'])
    data={'archive':archive.name,'bytes':archive.stat().st_size,'entries':len(names),
          'manifest':current,'hashes_checked':checked,'hash_mismatches':mismatches,
          'duplicate_names':duplicates,'duplicate_bytes_identical':duplicate_equal,
          'nested_zip':[n for n in names if n.lower().endswith('.zip')],
          'crc':'PASS','runtime_seconds':time.perf_counter()-start}
    assert not mismatches,mismatches
    assert all(duplicate_equal.values()),duplicate_equal
    assert not data['nested_zip']
    if current=='DELIVERY_MANIFEST.tsv':assert not duplicates,duplicates
Path(a.output).write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
