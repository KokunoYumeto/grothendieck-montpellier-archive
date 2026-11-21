"""Non-coordinate A10->A9 Koszul exploration of determinant ten-plane gates."""
from pathlib import Path
import json,math,time
import numpy as np
from coordinate_koszul import slices,koszul,modular_rank
from verify_det7_global import detmod

HERE=Path(__file__).resolve().parent

def main():
    source=json.loads((HERE.parent/'pencil/det10_A_koszul.json').read_text())['records']
    candidates=[q for q in source if 'certificates' in q and q['bound']<18]
    out=[];start=time.time();rng=np.random.default_rng(202611210419)
    for i,rec in enumerate(candidates):
        S=rec['subset'];support,mats=slices(S,-1)
        v=rng.integers(1,12,size=9,dtype=np.int64)
        projected=[mats[a]+int(v[a])*mats[9] for a in range(9)]
        M=koszul(projected,4);rank=modular_rank(M);bound=(rank['rank_mod_p']+69)//70
        record={'subset':S,'support':support,'last_slice_coefficients':list(map(int,v)),'rank_mod_p':rank['rank_mod_p'],'cost':70,'bound':bound}
        if bound>=18:
            n=17*70+1;rows=rank['rows'][:n];cols=rank['cols'][:n]
            value=detmod(M[np.ix_(rows,cols)],1000003);assert value
            record['certificate']={'rows':rows,'cols':cols,'order':n,'determinant_mod_p':value}
        out.append(record)
        (HERE/'det10_generic_A9_results.json').write_text(json.dumps({'status':'EXPLORATION','records':out,'seconds':time.time()-start},separators=(',',':'))+'\n')
        print(i+1,'of',len(candidates),S,'m',len(support),'rank',rank['rank_mod_p'],'bound',bound,'seconds',round(time.time()-start,2),flush=True)
    print('DONE',time.time()-start,flush=True)

if __name__=='__main__':main()
