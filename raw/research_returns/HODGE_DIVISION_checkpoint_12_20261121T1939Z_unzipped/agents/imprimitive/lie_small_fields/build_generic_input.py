#!/usr/bin/env python3
"""Extract only the original mathematical entries from frozen official tables.

No Julia code is executed.  The complete third-party source is kept only in
cache; this produces an offline, compact mathematical input with provenance.
"""
from pathlib import Path
import hashlib,json,re,urllib.request
from parse_generic_bounds import matching,rows,split_top

BASE=Path(__file__).resolve().parent
CONDITIONS={
 'G2.01.jl':'q even, q = 1 mod 3',
 'G2.02.jl':'q even, q = 2 mod 3',
 'G2.101.jl':'q a power of 3, q = 1 mod 4',
 'G2.103.jl':'q a power of 3, q = 3 mod 4',
 'G2.111.jl':'q odd, q = 1 mod 3, q = 1 mod 4',
 'G2.113.jl':'q odd, q = 1 mod 3, q = 3 mod 4',
 'G2.121.jl':'q odd, q = 2 mod 3, q = 1 mod 4',
 'G2.123.jl':'q odd, q = 2 mod 3, q = 3 mod 4',
 '3D4.0.jl':'q even',
 '3D4.11.jl':'q odd, q = 1 mod 4',
 '3D4.13.jl':'q odd, q = 3 mod 4',
}

def array(text,name):
    m=re.search(r'^'+name+r'\s*=\s*R\.\(\[',text,re.M)
    assert m,name
    pos=text.index('[',m.start());end=matching(text,pos,'[',']')
    return split_top(text[pos+1:end])

def compact(s):return re.sub(r'\s+',' ',s).strip()

def main():
    manifest=json.loads((BASE/'generic_table_retrieval.json').read_text())
    assert manifest['commit']=='87231738271ed548f62e7f1c98ff2bbfc1ed30d3'
    assert {Path(f['path']).name for f in manifest['files']}==set(CONDITIONS)
    out={'format':'original generic character entries, mathematical data only',
         'upstream_commit':manifest['commit'],'tables':[]}
    for f in manifest['files']:
        name=Path(f['path']).name;p=BASE/'cache'/name
        if not p.exists():
            p.parent.mkdir(exist_ok=True)
            p.write_bytes(urllib.request.urlopen(f['url'],timeout=60).read())
        raw=p.read_bytes();assert len(raw)==f['bytes']
        assert hashlib.sha256(raw).hexdigest()==f['sha256']
        text=raw.decode()
        assert 'CharTable(order, permutedims(table), classinfo, classlength, charinfo, chardegree,' in text
        item={'name':name,'condition':CONDITIONS[name],'source':f,
              'threshold':3 if name.startswith('3D4.') else 5,
              'entries':[[compact(e) for e in r] for r in rows(text)],
              'declared_degrees':[compact(e) for e in array(text,'chardegree')],
              'declared_class_lengths':[compact(e) for e in array(text,'classlength')]}
        assert len(item['entries'])==len(item['declared_degrees'])
        assert len(item['entries'][0])==len(item['declared_class_lengths'])
        out['tables'].append(item)
    dest=BASE/'generic_character_entries.json'
    dest.write_text(json.dumps(out,separators=(',',':'))+'\n')
    raw=dest.read_bytes()
    print(json.dumps({'tables':len(out['tables']),'bytes':len(raw),
                      'sha256':hashlib.sha256(raw).hexdigest()}))

if __name__=='__main__':main()
