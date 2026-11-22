#!/usr/bin/env python3
"""Independent P-15 enumeration in Q or F_p, standard-library only.
Every exact zero-pattern stratum of quotient lines/planes is enumerated;
there is no random sampling and no input certificate.
"""
import argparse,json,time
from collections import defaultdict,Counter
from itertools import combinations,product
from functools import lru_cache
from br_linear import setup,rank,rowspace,nullspace,Space,NONUNIT_PIVOTS
from check_higher_prolongation import arrangements


def apply(cols,v,p):
 out=defaultdict(int)
 for j,x in v.items():
  for i,y in cols[j].items():out[i]+=x*y
 if not p:
  for x in out.values():
   if x and hasattr(x,'numerator'):NONUNIT_PIVOTS.update(z for z in (abs(x.numerator),x.denominator) if z>1)
 return {i:(x%p if p else x) for i,x in out.items() if (x%p if p else x)}


def conditions(cols,p):
 rows=defaultdict(dict)
 for j,v in enumerate(cols):
  for i,x in v.items():rows[i][j]=x
 return rowspace([tuple(v.items()) for v in rows.values()],p)


def build_components(D):
 p=D['prime'];comps={};idx={}
 for o in ('A','B'):
  idx[o]={w:i for i,w in enumerate(sorted({w for maps in D['maps'][o] for w,cs,eq in maps}))}
 for i,(w,params) in enumerate(D['blocks']):
  d=len(params);raw=D['maps']['A'][i]+D['maps']['B'][i]
  for mult in range(1,min(2,d)+1):
   eqs=[];base=[];drop=[]
   if mult==d:
    states=[{'K':None,'E':[{j:1} for j in range(d)],'ranks':[rank(cols,p) for t,cols,eq in raw]}]
   else:
    for t,cols,eq in raw:
     r=len(eq)
     if mult==1:eqs.append(eq);base.append(int(r>0));drop.append(int(r>0))
     elif r==0:eqs.append(());base.append(0);drop.append(0)
     elif r==3:eqs.append(tuple((((j,1),)) for j in range(3)));base.append(2);drop.append(0)
     else:
      # The normal of a plane must annihilate ker(Q) for a rank drop.
      eqs.append(tuple(tuple(v.items()) for v in nullspace(eq,d,p)))
      base.append(r);drop.append(1)
    states=[]
    for eq,zeros in arrangements(eqs,d,p):
     K=nullspace(eq,d,p);st={'K':K,'zero':zeros,'ranks':[b-int(j in zeros)*v for j,(b,v) in enumerate(zip(base,drop))]}
     if len(K)==1:st['E']=K if mult==1 else nullspace([tuple(K[0].items())],d,p)
     states.append(st)
   for st in states:
    for o,offset,n in (('A',0,7),('B',7,9)):
     st[o]=tuple(sum(1<<idx[o][raw[offset+j][0]] for j in range(n) if st['ranks'][offset+j]>=level) for level in (1,2))
   comps[i,mult]=states
 return comps


def saturation_tables(D):
 tables={};p=D['prime']
 for o in ('A','B'):
  groups=defaultdict(lambda:defaultdict(list))
  for i,maps in enumerate(D['maps'][o]):
   for w,cols,eq in maps:groups[w][i]+=cols
  lookup=[]
  for w,byowner in groups.items():
   owners=list(byowner);mask=sum(1<<i for i in owners);tab={0:0}
   for q in range(1,min(4,len(owners))+1):
    for chosen in combinations(owners,q):tab[sum(1<<i for i in chosen)]=rank([v for i in chosen for v in byowner[i]],p)
   lookup.append((mask,tab))
  tables[o]=lookup
 return tables


def fixed_spaces(D,chosen):
 p=D['prime'];spaces={o:defaultdict(lambda:Space(p)) for o in ('A','B')}
 for i,st in chosen:
  if 'E' not in st:continue
  for o in ('A','B'):
   for w,cols,eq in D['maps'][o][i]:
    for v in st['E']:spaces[o][w].append(apply(cols,v,p))
 return spaces,{o:sum(s.rank() for s in spaces[o].values()) for o in ('A','B')}


def refined(D,i,st,spaces):
 p=D['prime'];K=st['K'];raw=[];eqs=[];oldcols=[]
 for o in ('A','B'):
  for w,cols,eq in D['maps'][o][i]:
   full=[apply(cols,v,p) for v in K];oldcols.append(full)
   newer=[spaces[o][w].reduce(v) for v in full]
   eqs.append(conditions(newer,p));raw.append((o,w))
 out=[]
 for eq,zeros in arrangements(eqs,len(K),p):
  L=nullspace(eq,len(K),p)
  if any(j not in st['zero'] and not any(apply(cols,v,p) for v in L) for j,cols in enumerate(oldcols)):continue
  active={o:set() for o in ('A','B')}
  for j,(o,w) in enumerate(raw):
   if j not in zeros:active[o].add(w)
  out.append(active)
 return out


def check_case(label,p):
 S=[0,1,3,6,7,9,18] if label!='perB' else [0,1,3,6,7,18,21]
 sign=-1 if label=='det' else 1
 D=setup(S,sign,p);assert len(D['support'])==9
 limits={o:(D['factor_dims'][o]-1)*13-D['base_ranks'][o] for o in ('A','B')}
 start=time.time();dims=[len(c) for w,c in D['blocks']];C=build_components(D);tables=saturation_tables(D);counts=Counter();survivors=[]
 for q in range(1,5):
  for inds in combinations(range(len(dims)),q):
   ds=sum(dims[i] for i in inds)
   if ds<4:continue
   counts['supports_tested']+=1;mask=sum(1<<i for i in inds)
   nullity={o:D['factor_dims'][o]*(9+ds)-D['base_ranks'][o]-sum(tab[mask&bits] for bits,tab in tables[o]) for o in ('A','B')}
   if min(nullity.values())<13:counts['saturation_excluded']+=1;continue
   counts['supports_surviving_'+str(q)]+=1
   if q not in (3,4):survivors.append({'support':inds,'reason':'one or two weights survived'});continue
   if q==3:
    for doubled in inds:
     if (doubled,2) not in C:continue
     for states in product(*(C[i,2 if i==doubled else 1] for i in inds)):
      counts['three_states']+=1
      bounds={o:sum((states[0][o][level]|states[1][o][level]|states[2][o][level]).bit_count() for level in (0,1)) for o in ('A','B')}
      if not any(bounds[o]>limits[o] for o in ('A','B')):survivors.append({'support':inds,'reason':'double-plane stratum survived','bounds':bounds})
    continue
   minima={o:sum(min(st[o][0].bit_count() for st in C[i,1]) for i in inds) for o in ('A','B')}
   overlap={o:len(inds)*D['factor_dims'][o]-len({w for i in inds for w,cols,eq in D['maps'][o][i]}) for o in ('A','B')}
   if any(minima[o]-overlap[o]>limits[o] for o in ('A','B')):counts['four_min_overlap']+=1;continue
   hit=False
   for states in product(*(C[i,1] for i in inds)):
    if any((states[0][o][0]|states[1][o][0]|states[2][o][0]|states[3][o][0]).bit_count()>limits[o] for o in ('A','B')):continue
    hit=True;counts['four_joint_states']+=1
    chosen=list(zip(inds,states));spaces,inc=fixed_spaces(D,chosen)
    if any(inc[o]>limits[o] for o in ('A','B')):counts['four_fixed_excluded']+=1;continue
    free=[(i,st) for i,st in chosen if 'E' not in st]
    if len(free) not in (1,2):survivors.append({'support':inds,'reason':'fixed extension or at least three free lines survived'});continue
    counts['four_free_'+str(len(free))]+=1
    options=[refined(D,i,st,spaces) for i,st in free]
    for opts in product(*options):
     counts['refined_states']+=1
     if not any(len(set.union(*(st[o] for st in opts)))+inc[o]>limits[o] for o in ('A','B')):
      survivors.append({'support':inds,'reason':'refined parameter stratum survived'})
   if not hit:counts['four_joint_union']+=1
 result={'case':label,'subset':S,'sign':sign,'prime':p,'base_ranks':D['base_ranks'],'limits':limits,'counts':dict(counts),
         'survivors':survivors,'status':'PASS' if not survivors else 'OPEN','nonunit_pivots':sorted(NONUNIT_PIVOTS),
         'seconds':round(time.time()-start,3)}
 print(json.dumps(result),flush=True);return result


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=0);ap.add_argument('--case',choices=['det','perA','perB','all'],default='all');ap.add_argument('--output');args=ap.parse_args()
 if args.prime:assert args.prime>=2 and all(args.prime%d for d in range(2,int(args.prime**.5)+1))
 result=[check_case(c,args.prime) for c in ['det','perA','perB'] if args.case in (c,'all')]
 if args.output:
  with open(args.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
if __name__=='__main__':main()
