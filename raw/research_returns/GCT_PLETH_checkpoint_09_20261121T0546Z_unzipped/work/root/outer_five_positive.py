"""G036 complete positive formula for every outer-five Schur plethysm coefficient."""
from pathlib import Path
import sys,argparse,json
HERE=Path(__file__).resolve().parent
sys.path.append(str(HERE.parent/'theta'/'outer5'/'variable_wall'))
import five_point_two_row_positive as bulk
import normalized_below_positive as below
import generic_high_twist_positive as high
from generic_twist_upper_positive import LABELS,transpose

def normalized_route(x,b,k,c,d,mu):
 if any(type(z)is not int or z<0 for z in (x,b,k,c,d)):raise ValueError('parameters must be nonnegative integers')
 mu=tuple(mu)
 if mu not in LABELS:raise ValueError('outer must partition five')
 if b+c<2*k or 2*b+x+3*c<5*k:raise ValueError('parameters must satisfy both normalization and partition inequalities')
 if c>=2*k:return 'bulk',(x,b,k,c-2*k,d,mu)
 if c>=k:return 'high',(x,b,k,c,d,mu)
 return 'below',(x,b,k,c,d,mu)
PROVIDERS={'bulk':bulk,'high':high,'below':below}

def partition_route(lam,mu=(5,)):
 lam=tuple(lam);mu=tuple(mu)
 if mu not in LABELS:raise ValueError('outer must partition five')
 if any(type(z)is not int or z<0 for z in lam) or any(lam[i]<lam[i+1] for i in range(len(lam)-1)):raise ValueError('output must be a nonnegative partition')
 while lam and not lam[-1]:lam=lam[:-1]
 if sum(lam)%5:raise ValueError('partition size must be divisible by five')
 n=sum(lam)//5
 if len(lam)>5:return {'original':lam,'inner':n,'zero':'more than five rows'}
 lam=lam+(0,)*(5-len(lam));original=lam;original_n=n;original_mu=mu
 k=lam[1]-n;b=lam[2]-lam[3];c=lam[1]-lam[2]
 complemented=False;H=None
 if k>0 and b+c-k<k:
  H=lam[0];lam=tuple(H-z for z in reversed(lam));n=H-n
  if H%2:mu=transpose(mu)
  complemented=True
 e=max(0,n-lam[1]);n0=n-e;normalized=(lam[0]-5*e,)+lam[1:]
 d=lam[4];x=lam[3]-lam[4];b=lam[2]-lam[3];c=lam[1]-lam[2];k=lam[1]-n0
 assert k>=0 and b+c>=2*k
 assert normalized==(d+3*b+2*x+4*c-5*k,d+b+x+c,d+b+x,d+x,d)
 assert 2*b+x+3*c>=5*k and n0==d+b+x+c-k
 selected=normalized_route(x,b,k,c,d,mu)
 route={'original':original,'inner':original_n,'outer':original_mu,'complement':complemented,'complement_height':H,'stable_power':e,'normalized':normalized,'normalized_inner':n0,'parameters':(x,b,k,c,d,mu),'selected':selected}
 if selected[0]=='below':route['below_selected']=below.route(*selected[1])
 return route

def coefficient_partition(lam,mu=(5,)):
 r=partition_route(lam,mu)
 if 'zero' in r:return 0
 name,args=r['selected'];return PROVIDERS[name].coefficient(*args)

def partition_polytopes(lam,mu=(5,)):
 r=partition_route(lam,mu)
 if 'zero' in r:return {'route':r,'polytopes':[]}
 name,args=r['selected'];return {'route':r,'formula':PROVIDERS[name].polytopes(*args)}

def coefficient(x,b,k,c,d=0,mu=(5,)):
 if any(type(z)is not int or z<0 for z in (x,b,k,c,d)) or 2*b+x+3*c<5*k:raise ValueError('invalid nonnegative chart parameters')
 lam=(d+3*b+2*x+4*c-5*k,d+b+x+c,d+b+x,d+x,d)
 return coefficient_partition(lam,mu)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--partition',type=int,nargs='*',required=True);p.add_argument('--outer',default='5');p.add_argument('--polytopes',action='store_true')
 v=p.parse_args();mu=tuple(map(int,v.outer.split(',')));r={'coefficient':coefficient_partition(v.partition,mu),'route':partition_route(v.partition,mu)}
 if v.polytopes:r['positive_formula']=partition_polytopes(v.partition,mu)
 print(json.dumps(r,indent=2))
if __name__=='__main__':main()
