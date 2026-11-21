#!/usr/bin/env python3
"""Independent exact crossing certificate for the quadratic orbital cofaces."""
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(Path(__file__).resolve().parent))
import certify_orbital_paths as c

def source(word):
    if word in ('u','U'):
        n=6 if word=='u' else 12
        return [(v,c.base[1]) for v in c.vertices[:n+1]]
    j=int(word[1:]);turn=c.vertices[:6*j+1]
    out=[(v,c.base[1]) for v in turn]
    out.extend((turn[-1],v) for v in c.lollipop(1,4)[1:])
    out.extend((v,c.base[1]) for v in turn[-2::-1])
    return out

def target(face,word):
    coords=[]
    if face==0:
        for v in c.lollipop(1 if word=='x' else 4,4 if word=='x' else c.q(15,2)):
            coords.append((c.base[0],v,c.complex_pair(c.q(15,2))) if word=='x' else (c.base[0],c.base[1],v))
    else:
        for u,v in source(word):
            if face==1:w=(c.scale(c.small,u),u,v)
            elif face==2:w=(u,c.scale(c.close,u),v)
            elif face==3:w=(u,v,c.scale(c.close,v))
            else:w=(u,v,c.complex_pair(c.q(15,2)))
            coords.append(w)
    return [(c.scale(-1,u),c.complex_pair(0),u,v,w) for u,v,w in coords]

c.source=source;c.target=target
started=time.monotonic();out={}
old=json.loads((ROOT/'work/agents/characters/records/harmonic_orbit_coface_braids_discovery.json').read_text())
for face in range(5):
    words=['x','y'] if face==0 else (['u','Y0'] if face==4 else ['U','Y0','Y1'])
    for w in words:
        result=c.track(face,w)
        result['equals_discovery_in_B4']=c.braid(tuple(result['word']))==c.braid(tuple(old[str(face)][w]['braid_word']))
        assert result['equals_discovery_in_B4'],(face,w,result['word'],old[str(face)][w]['braid_word'])
        out[f'{face}:{w}']=result
        print(face,w,result['word'],'PASS',flush=True)
        (ROOT/'work/records/harmonic_orbital_paths_exact.json').write_text(json.dumps({'scope':'Exact algebraic-polygonal crossing audit for the quadratic orbital cofaces, literal B4, no central quotient.','completed':out,'elapsed_seconds':time.monotonic()-started},indent=2)+'\n')
print('PASS all13 harmonic coface paths with exact rational crossing isolation',flush=True)
