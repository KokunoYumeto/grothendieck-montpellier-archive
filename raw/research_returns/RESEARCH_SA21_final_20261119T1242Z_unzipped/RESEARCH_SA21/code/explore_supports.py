"""Reproducible finite exploration; witness verification is independent of counts."""
import argparse, json, time
from itertools import combinations
from supports_core import Orthoset, natural_posets, comparability, magasin, figures, supp1_witness

p=argparse.ArgumentParser()
p.add_argument('mode',choices=['graphs','orders','magasins'])
p.add_argument('--maxn',type=int,default=5)
args=p.parse_args()
t=time.perf_counter()
counts={}; witnesses={}
for n in range(args.maxn+1):
    stats={}
    if args.mode=='graphs':
        pairs=list(combinations(range(n),2))
        data=((None,Orthoset(list(range(n)),[e for k,e in enumerate(pairs) if mask>>k&1]))
              for mask in range(1<<len(pairs)))
    else:
        data=((lt,(comparability if args.mode=='orders' else magasin)(n,lt)) for lt in natural_posets(n))
    for lt,g in data:
        om=g.om_witness() is None
        su=g.sumner_witness() is None
        bo=g.boolean_witness() is None if om else False
        key=f'OML={om},Sumner={su},Boolean={bo}'
        stats[key]=stats.get(key,0)+1
        if not om and su and 'sumner_not_om' not in witnesses:
            witnesses['sumner_not_om']=dict(n=n,lt=sorted(lt) if lt is not None else None,
                **g.describe(),om_witness=[g.decode(x) for x in g.om_witness()],
                dacey_witness=[g.decode(x) for x in g.dacey_witness()])
        if args.mode=='magasins' and not om and 'magasin_not_om' not in witnesses:
            fs=figures(g)
            witnesses['magasin_not_om']=dict(n=n,lt=sorted(lt),**g.describe(),
                om_witness=[g.decode(x) for x in g.om_witness()],figures=len(fs),
                supp1_witness=supp1_witness(g,fs))
        if args.mode=='magasins' and not bo and 'magasin_not_boolean' not in witnesses:
            witnesses['magasin_not_boolean']=dict(n=n,lt=sorted(lt),**g.describe())
    counts[n]=stats
    print(json.dumps(dict(mode=args.mode,n=n,counts=stats,seconds=time.perf_counter()-t)),flush=True)
print(json.dumps(dict(witnesses=witnesses,total_seconds=time.perf_counter()-t),indent=2),flush=True)
