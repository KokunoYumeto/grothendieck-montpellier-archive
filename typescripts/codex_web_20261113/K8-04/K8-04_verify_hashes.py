"""Check both hash sets and reconstruct the pre-witness text by reversing only logged spans."""
from pathlib import Path
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parent
LOG = (ROOT / 'progress.log').read_text()
def snapshot(start, end):
    part = LOG.split(start,1)[1].split(end,1)[0]
    return {name:value for value,name in re.findall(r'^([0-9a-f]{64})  (.+)$',part,re.M)}
def sha(data):
    return hashlib.sha256(data).hexdigest()

if __name__ == '__main__':
    frozen = snapshot('SHA-256 before witness comparison', 'transcription frozen ')
    final = snapshot('SHA-256 after witness comparison', 'witness check done ')
    assert len(frozen)==16 and final.keys()==frozen.keys()
    with (ROOT/'K8-04_witness.tsv').open(newline='') as f:
        ledger=list(csv.DictReader(f,delimiter='\t'))
    assembled_name='K8-04_transcription.tex'
    pieces=[];original=[];covered=0
    for filename in sorted(n for n in final if n.startswith('pages/')):
        raw=(ROOT/filename).read_bytes()
        assert sha(raw)==final[filename], filename
        txt=raw.decode('utf8');n=int(Path(filename).stem[-3:])
        rows=[r for r in ledger if int(r['scan'])==n]
        parts=[];i=0;offset=0
        for r in rows:
            j=int(r['final_offset']);v=r['final_span'];old=r['frozen_span']
            assert i<=j and txt[j:j+len(v)]==v, (n,r['id'])
            assert j+offset==int(r['frozen_offset']), (n,r['id'],'frozen offset')
            assert old.startswith((r'\unsure{',r'\illegible{'))
            assert (old!=v)==(r['result'] in ('changed','alternative added'))
            parts.extend([txt[i:j],old]);i=j+len(v);offset+=len(old)-len(v)
        parts.append(txt[i:])
        before=''.join(parts)
        count=len(re.findall(r'\\(?:unsure|illegible)\{',before))
        assert count==len(rows), (filename,count,len(rows))
        assert sha(before.encode())==frozen[filename],filename
        covered+=len(rows);pieces.append(raw);original.append(before.encode())
    assert covered==len(ledger)
    assert b''.join(pieces)==(ROOT/assembled_name).read_bytes()
    assert sha(b''.join(pieces))==final[assembled_name]
    assert sha(b''.join(original))==frozen[assembled_name]
    print(f'PASS: all 16 final SHA-256 digests match. Reversing the {covered} marked spans reconstructs all 16 freeze digests.')
