"""Bounded exploratory LC/pivot search, not a minimum-edge certificate."""
from pathlib import Path
import hashlib,json,math,random,time

W=Path(__file__).resolve().parents[1]
ip=W/'inputs/sh_lu_preparation_lc_search.json';cfg=json.loads(ip.read_text())
g=json.loads((W/cfg['graph_input']).read_text())['systematic_css'];n=27
initial=[0]*n
for i,j in g['source_graph_edges_one_based']:
    initial[i-1]|=1<<(j-1);initial[j-1]|=1<<(i-1)

def lc(a,v):
    b=a[:];mask=a[v]
    for i in range(n):
        if mask>>i&1:b[i]^=mask^(1<<i)
    return b

def cost(a):return sum(x.bit_count()for x in a)//2

rng=random.Random(cfg['seed']);records=[];best=(cost(initial),initial[:],[])
start=time.time()
for phase in cfg['phases']:
    phase_best=cost(initial)
    for restart in range(phase['restarts']):
        a=initial[:];c=cost(a);seq=[]
        for t in range(phase['steps']):
            u=rng.randrange(n)
            if phase['move']=='lc':move=[u]
            else:
                neigh=[v for v in range(n)if a[u]>>v&1]
                if not neigh:continue
                v=rng.choice(neigh);move=[u,v,u]
            b=a
            for v in move:b=lc(b,v)
            cc=cost(b)
            temperature=phase['floor_temperature']+phase['temperature']*(1-t/phase['steps'])**2
            if cc<=c or rng.random()<math.exp((c-cc)/temperature):
                a=b;c=cc;seq.extend(v+1 for v in move)
            phase_best=min(phase_best,c)
            if c<best[0]:
                best=(c,a[:],seq[:]);records.append({'move':phase['move'],'restart':restart,'step':t,'edges':c})
                print('best',records[-1],flush=True)
    records.append({'phase':phase['move'],'phase_best':phase_best})
replay=initial[:]
for v in best[2]:replay=lc(replay,v-1)
assert replay==best[1] and cost(replay)==best[0]
out={'status':'BOUNDED EXPLORATION ONLY; no optimality or conversion advantage claimed',
     'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),'seconds':time.time()-start,
     'best_edge_count':best[0],'best_edges_one_based':[[i+1,j+1]for i in range(n)for j in range(i+1,n)if best[1][i]>>j&1],
     'local_complementation_sequence_one_based':best[2],'records':records}
p=W/cfg['output'];tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(p)
print(json.dumps({k:v for k,v in out.items()if k not in('best_edges_one_based','local_complementation_sequence_one_based','records')},indent=2))
