"""Certified Koszul lower bounds on all Borel-fixed determinant residuals."""
import sys,json,math,time,argparse
from pathlib import Path
import numpy as np
from coordinate_koszul import slices,koszul,modular_rank

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--lo',type=int,default=7)
    pa.add_argument('--hi',type=int,default=12)
    pa.add_argument('--out',type=Path,required=True)
    pa.add_argument('--target',type=int,default=0,help='Stop each case once total substituted bound reaches this.')
    args=pa.parse_args()
    data=json.loads(Path('work/root/borel_ideals.json').read_text())
    out=[];start=time.time()
    for j in range(args.lo,args.hi+1):
        recs=[]
        for mask in data[str(j)]:
            s=[i for i in range(36) if mask>>i&1]
            support,mats=slices(s,-1);ten=np.array(mats)
            lower=max(j,len(support));certs=[]
            rng=np.random.default_rng(mask+20261121)
            if not(args.target and 36-j+lower>=args.target):
                jobs=[]
                if j<=8:
                    for p in range(1,min((j-1)//2,3)+1):jobs.append((j,p,None))
                for a in [3,5,7]:
                    if a<j:
                        for k in range(2):jobs.append((a,(a-1)//2,rng.integers(-3,4,size=(a,j))))
                for a,p,proj in jobs:
                    mm=ten if proj is None else np.einsum('ai,ijk->ajk',proj,ten)
                    mat=koszul(mm,p);c=modular_rank(mat)
                    cost=math.comb(a-1,p)
                    c.update({'p':p,'wedge_dimension':a,'pure_cost':cost,'shape':list(mat.shape),'projection':None if proj is None else proj.tolist(),'bound':(c['rank_mod_p']+cost-1)//cost})
                    lower=max(lower,c['bound']);certs.append(c)
                    if args.target and 36-j+lower>=args.target:break
            recs.append({'subset':s,'mask':mask,'support':support,'lower_bound':lower,'substitution_bound':36-j+lower,'certificates':certs})
        result={'j':j,'number_of_ideals':len(recs),'minimum_certified':min(r['lower_bound'] for r in recs),'records':recs}
        result['substitution_bound']=36-j+result['minimum_certified']
        out.append(result)
        print(j,len(recs),result['minimum_certified'],result['substitution_bound'],'minimizers',[(r['subset'],len(r['support'])) for r in recs if r['lower_bound']==result['minimum_certified']],flush=True)
        args.out.write_text(json.dumps({'seconds':time.time()-start,'results':out},indent=2)+'\n')

if __name__=='__main__':main()
