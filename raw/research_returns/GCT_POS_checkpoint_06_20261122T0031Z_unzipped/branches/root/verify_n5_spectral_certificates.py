#!/usr/bin/env python3
"""Independent integer replay of five-dimensional spectral certificates.

Rational certificates are cleared to integers. Farkas inequalities are
then checked on ALL 125 coordinate triples (including multiplicities),
which differs from the generator's compressed eigenvalue-row check.
Coverage of the spectral enumeration is a separate induction/proof.
"""
import argparse, collections, fractions, itertools, json, math, pathlib, time
ap=argparse.ArgumentParser();ap.add_argument('--target',type=int,default=2)
ap.add_argument('--primitive',action='store_true');args=ap.parse_args()
source=pathlib.Path(__file__).resolve().parents[1]/'kronecker'
prefix='recursive_n5' if args.primitive else f'character_n5_t{args.target}'
summary=[];start=time.time()
for result_path in sorted(source.glob(prefix+'_m*_result.json'),key=lambda p:json.loads(p.read_text())['M']):
    report=json.loads(result_path.read_text());M=report['M'];target=(1 if args.primitive else args.target)%M
    counts=collections.Counter();old=None;positive=[]
    spectrum_path=source/f'{prefix}_m{M}_spectra.txt'
    spectra=spectrum_path.open() if spectrum_path.exists() else None
    for line in (source/f'{prefix}_m{M}_certificates.jsonl').open():
        row=json.loads(line);w=row['W'];key=tuple(tuple(a) for a in w)
        assert old is None or old<key;old=key
        assert len(w)==3 and all(len(a)==5 and a[0]==0 and a==sorted(a) for a in w)
        assert w==sorted(w) and all(0<=x<M for a in w for x in a)
        assert sum(map(sum,w))%M==target
        if spectra:assert list(map(int,next(spectra).split()))==sum(w,[])
        vals=[sorted(set(a)) for a in w]
        coords=[(a,x) for a in range(3) for x in vals[a]]
        if 'y' in row:
            q=list(map(fractions.Fraction,row['y']));assert len(q)==len(coords)
            denominator=math.lcm(*(x.denominator for x in q))
            y=dict(zip(coords,(int(x*denominator) for x in q)))
            expanded=[[y[a,x] for x in w[a]] for a in range(3)]
            assert sum(map(sum,expanded))<0
            for i,j,k in itertools.product(range(5),repeat=3):
                if (w[0][i]+w[1][j]+w[2][k])%M==0:
                    assert expanded[0][i]+expanded[1][j]+expanded[2][k]>=0
            counts['infeasible']+=1
        else:
            edges=[e for e in itertools.product(*vals) if sum(e)%M==0]
            assert row['E']==list(map(list,edges))
            q=list(map(fractions.Fraction,row['x']));assert len(q)==len(edges)
            denominator=math.lcm(*(x.denominator for x in q))
            x=[int(a*denominator) for a in q]
            assert all(a>=0 for a in x)
            for a,v in coords:
                assert sum(c for c,e in zip(x,edges) if e[a]==v)==denominator*w[a].count(v)
            assert row['strict']==all(a>0 for a in x)
            positive.append(row);counts['feasible']+=1
    if spectra:assert next(spectra,None) is None;spectra.close()
    assert sum(counts.values())==report['orbits'] and dict(counts)==report['counts']
    assert positive==report['feasible']
    data={'modulus':M,'target_exponent':target,'counts':dict(counts),'certificates':sum(counts.values())}
    summary.append(data);print('PASS',data,flush=True)
out={'status':'PASS','method':'denominator-cleared integer checks on all125 coordinate triples',
     'prefix':prefix,'levels':summary,'total':sum(r['certificates'] for r in summary),
     'seconds':time.time()-start,'scope':'Arithmetic and candidate-list coverage; recursive orbit coverage is separately proved.'}
dest=pathlib.Path(__file__).resolve().parents[2]/'reviews'/f'{prefix}_independent_certificates.json'
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
