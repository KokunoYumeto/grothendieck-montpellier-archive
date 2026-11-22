#!/usr/bin/env python3
"""QC-012: fresh stdlib certificate for three nonic HW restrictions.

Reconstructs the explicit bracket polynomials, all coefficient sums, three
actual 9x9 block determinant specializations, and the ambient multiplicity.
No stored matrix, pickle cache, original-run checker, NumPy, or SymPy is used.
The selected restriction minor is46 modulo101, so all three copies survive.
"""
import argparse
from collections import Counter, defaultdict
from itertools import permutations, combinations_with_replacement
from math import factorial, prod
from pathlib import Path
import json
import time

P=101
BITS=5
ROWBITS=4*BITS
ROWMASK=(1<<ROWBITS)-1
GUARD=sum(16<<(BITS*i) for i in range(4))
PERM4=list(permutations(range(4)))
SYMBOLS=[
 [((0,1,2,3),4),((0,1,4,5),4),((2,3,4,5),4),((0,2,4),1),((1,3,5),1)],
 [((2,3,4,5),4),((0,1,4,5),3),((0,1,2,3),3),((0,1,3,5),2),((0,2,4),1),((1,2,4),1)],
 [((2,3,4,5),3),((0,1,4,5),3),((0,1,2,3),2),((1,3,4,5),2),((0,2,3,5),1),((0,2,3,4),1),((0,1,2),2)]
]
A=(2,2,2,3)
B=(4,2,2,1)
C=(2,4,2,1)
D=(2,2,4,1)
E=(3,3,3,0)
PATTERNS=[('A3BCD',(A,A,A,B,C,D),(0,1,2)),
          ('A4E2',(A,A,A,A,E,E),(0,1,2)),
          ('A4CD_probe0',(A,A,A,A,C,D),(1,2,3))]



def parity(pi):
 return (-1)**sum(pi[i]>pi[j] for i in range(len(pi)) for j in range(i+1,len(pi)))

def row_code(a):
 return sum(v<<(BITS*i) for i,v in enumerate(a))

def det_power(power):
 terms=[(sum(1<<(ROWBITS*r+BITS*pi[r]) for r in range(4)),parity(pi)) for pi in PERM4]
 out={0:1}
 for _ in range(power):
  nxt=defaultdict(int)
  for a,va in out.items():
   for b,vb in terms:nxt[a+b]+=va*vb
  out={a:v%P for a,v in nxt.items() if v%P}
 return out

def automorphisms(symbol):
 ref=Counter({tuple(a):p for a,p in symbol})
 result=[]
 for pi in permutations(range(6)):
  image=Counter();sign=1
  for a,p in symbol:
   aa=tuple(pi[i] for i in a)
   image[tuple(sorted(aa))]+=p;sign*=parity(aa)**p
  if image==ref:
   assert sign==1, 'A negative automorphism would symmetrize to zero.'
   result.append(pi)
 return result

def small_terms(symbol,axes):
 out={0:1}
 for bracket,power in symbol:
  if bracket in [(0,1,2,3),(0,1,4,5),(2,3,4,5)]:continue
  colors=tuple(range(4)) if len(bracket)==4 else axes
  terms=[]
  for pi in permutations(range(len(colors))):
   key=sum(1<<(ROWBITS*v+BITS*colors[pi[r]]) for r,v in enumerate(bracket))
   terms.append((key,parity(pi)))
  for _ in range(power):
   nxt=defaultdict(int)
   for a,va in out.items():
    for b,vb in terms:nxt[a+b]+=va*vb
   out={a:v%P for a,v in nxt.items() if v%P}
 return [(tuple((key>>(ROWBITS*i))&ROWMASK for i in range(6)),v)
         for key,v in out.items()]

def tables(symbol,axes,dp):
 powers=dict(symbol)
 pa=powers[(0,1,4,5)];pb=powers[(0,1,2,3)]
 aa=[];bb=defaultdict(list)
 for key,v in dp[pa].items():
  aa.append((tuple((key>>(ROWBITS*i))&ROWMASK for i in range(4)),v))
 for key,v in dp[pb].items():
  rr=tuple((key>>(ROWBITS*i))&ROWMASK for i in range(4))
  bb[rr[:2]].append((rr[2],rr[3],v))
 return aa,bb,small_terms(symbol,axes),dp[powers[(2,3,4,5)]]

def coefficient(target,tab):
 aa,bb,small,cc=tab
 tt=list(map(row_code,target));answer=0;joins=0
 guard=GUARD
 for ss,sval in small:
  t0,t1,t2,t3,t4,t5=(guard+t-s for t,s in zip(tt,ss))
  # Guard bits detect every negative coordinate without cross-digit borrow.
  if any((t&guard)!=guard for t in (t0,t1,t2,t3,t4,t5)):continue
  for (a0,a1,a4,a5),aval in aa:
   n0=t0-a0;n1=t1-a1;r4=t4-a4;r5=t5-a5
   if (n0&guard)!=guard or (n1&guard)!=guard or (r4&guard)!=guard or (r5&guard)!=guard:continue
   pair=(n0-guard,n1-guard)
   tail=((r4-guard)<<(2*ROWBITS))+((r5-guard)<<(3*ROWBITS))
   partial=0
   for b2,b3,bval in bb.get(pair,()):
    r2=t2-b2;r3=t3-b3
    if (r2&guard)!=guard or (r3&guard)!=guard:continue
    key=(r2-guard)+((r3-guard)<<ROWBITS)+tail
    cval=cc.get(key,0)
    if cval:partial+=bval*cval;joins+=1
   answer+=sval*aval*partial
 return answer%P,joins

def grouped_targets(pattern,axes,auts):
 coordinate_perms=[]
 for perm in permutations(axes):
  pi=list(range(4))
  for i,j in zip(axes,perm):pi[i]=j
  coordinate_perms.append(pi)
 grouped=Counter()
 for target in set(permutations(pattern)):
  variants=[]
  for pi in coordinate_perms:
   renamed=tuple(tuple(a[pi[k]] for k in range(4)) for a in target)
   variants.extend(tuple(renamed[i] for i in aut) for aut in auts)
  grouped[min(variants)]+=1
 return sorted(grouped.items())


def product_groups(tab):
 aa,bb,small,cc=tab
 pairs=[(rows[0],rows[1],r2,r3,v) for rows,values in bb.items() for r2,r3,v in values]
 groups=defaultdict(lambda:defaultdict(int))
 for (a0,a1,a4,a5),av in aa:
  tail=(a4<<(2*ROWBITS))+(a5<<(3*ROWBITS))
  for b0,b1,b2,b3,bv in pairs:
   groups[(a0+b0,a1+b1)][b2+(b3<<ROWBITS)+tail]+=av*bv
 result={pair:[(tuple((key>>(ROWBITS*i))&ROWMASK for i in range(4)),v%P)
                for key,v in terms.items() if v%P] for pair,terms in groups.items()}
 return result

def coefficient_join(target,tab,groups):
 _,_,small,cc=tab
 tt=list(map(row_code,target));total=0;joins=0;tested=0;g=GUARD
 for ss,sv in small:
  r=[g+t-s for t,s in zip(tt,ss)]
  if any((x&g)!=g for x in r):continue
  terms=groups.get((r[0]-g,r[1]-g),())
  t2,t3,t4,t5=r[2:]
  sub=0
  for (a2,a3,a4,a5),v in terms:
   z2=t2-a2;z3=t3-a3;z4=t4-a4;z5=t5-a5
   if (z2&g)!=g or (z3&g)!=g or (z4&g)!=g or (z5&g)!=g:continue
   key=(z2-g)+((z3-g)<<ROWBITS)+((z4-g)<<(2*ROWBITS))+((z5-g)<<(3*ROWBITS))
   cv=cc.get(key,0)
   if cv:sub+=v*cv;joins+=1
   tested+=1
  total+=sv*sub
 return total%P,joins,tested


def weight_table(n, d, caps):
    bmax, cmax, emax = caps
    ne = emax+1
    nc = (cmax+1)*ne
    nb = (bmax+1)*nc
    a = [0]*((d+1)*nb)
    # The zero-tail monomial fills any remaining coefficient degree.
    for k in range(d+1):
        a[k*nb] = 1
    for b in range(min(n, bmax)+1):
        for c in range(min(n-b, cmax)+1):
            for e in range(min(n-b-c, emax)+1):
                if not b+c+e:
                    continue
                offset = nb+b*nc+c*ne+e
                for k in range(1, d+1):
                    for i in range(b, bmax+1):
                        for j in range(c, cmax+1):
                            base = k*nb+i*nc+j*ne
                            for h in range(e, emax+1):
                                index = base+h
                                a[index] += a[index-offset]
    return a, (ne,nc,nb)

def multiplicity(n, d, lam, table=None):
    assert len(lam) == 4 and sum(lam) == n*d
    if table is None:
        caps = tuple(lam[j]+3-j for j in range(1, 4))
        table = weight_table(n,d,caps)
    a,(ne,nc,nb)=table
    terms = []
    for sig in permutations(range(4)):
        alpha = tuple(lam[j]+sig[j]-j for j in range(4))
        parity = (-1)**sum(sig[i] > sig[j] for i in range(4) for j in range(i+1,4))
        if min(alpha) < 0:
            value = 0
        else:
            value = a[d*nb+alpha[1]*nc+alpha[2]*ne+alpha[3]]
        terms.append(dict(permutation=sig, weight=alpha, sign=parity, count=value))
    return dict(n=n, d=d, partition=lam,
                multiplicity=sum(t['sign']*t['count'] for t in terms),
                weyl_terms=terms)




def poly_product(a,b):
 out=defaultdict(int)
 for u,x in a.items():
  for v,y in b.items():out[tuple(i+j for i,j in zip(u,v))]+=x*y
 return {u:x for u,x in out.items() if x}

def determinant3(matrix):
 out=defaultdict(int)
 for pi in permutations(range(3)):
  term={(0,0,0,0):parity(pi)}
  for row,column in enumerate(pi):term=poly_product(term,matrix[row][column])
  for alpha,value in term.items():out[alpha]+=value
 return {a:x for a,x in out.items() if x}

def actual_determinants():
 x=[]
 for i in range(4):
  alpha=tuple(int(j==i) for j in range(4));x.append({alpha:1})
 zero={};minus_x1={a:-v for a,v in x[1].items()}
 matrices=[[[x[3],x[0],x[1]],[x[0],x[3],x[2]],[minus_x1,x[2],x[3]]],
           [[x[3],x[0],zero],[zero,x[3],x[1]],[x[2],zero,x[3]]]]
 first=[{tuple(a+b for a,b in zip(alpha,(2,2,2,0))):value
         for alpha,value in determinant3(m).items()} for m in matrices]
 assert first[0]=={A:1,B:-1,C:1,D:-1}
 assert first[1]=={A:1,E:1}
 swap=lambda a:(a[3],a[1],a[2],a[0])
 first.append({swap(a):v for a,v in first[0].items()})
 # Every six-fold monomial product contributing to weight lambda is listed.
 expected=[sorted(PATTERNS[0][1]),sorted(PATTERNS[1][1]),
           sorted(swap(a)for a in PATTERNS[2][1])]
 for polynomial,wanted in zip(first,expected):
  good=[list(ms) for ms in combinations_with_replacement(sorted(polynomial),6)
        if tuple(sum(a[i]for a in ms)for i in range(4))==(14,14,14,12)]
  assert good==[wanted]
 return [[dict(exponent=a,coefficient=v)for a,v in sorted(polynomial.items())]
         for polynomial in first]

def check():
 start=time.monotonic()
 actual=actual_determinants()
 ambient=multiplicity(9,6,(14,14,14,12))
 assert ambient['multiplicity']==3
 dp={power:det_power(power)for power in (2,3,4)}
 assert [len(dp[i])for i in (2,3,4)]==[282,1848,10147]
 matrix=[];all_records=[]
 for index,symbol in enumerate(SYMBOLS):
  assert [sum(power for bracket,power in symbol if i in bracket)for i in range(6)]==[9]*6
  assert [sum(power for bracket,power in symbol if j<len(bracket))for j in range(4)]==[14,14,14,12]
  assert all(0<=j<6 for bracket,_ in symbol for j in bracket)
  auts=automorphisms(symbol);tabcache={};outercache={};values=[]
  for label,pattern,axes in PATTERNS:
   if axes not in tabcache:
    tabcache[axes]=tables(symbol,axes,dp)
    if index==2:outercache[axes]=product_groups(tabcache[axes])
   tab=tabcache[axes];groups=grouped_targets(pattern,axes,auts)
   total=0;records=[]
   for number,(target,count)in enumerate(groups):
    if index==2:
     value,joins,tested=coefficient_join(target,tab,outercache[axes])
    else:
     value,joins=coefficient(target,tab);tested=None
    total=(total+count*value)%P
    records.append(dict(target=target,multiplicity=count,coefficient=value,joins=joins,tested=tested))
    print(json.dumps(dict(symbol=index,pattern=label,group=number+1,total_groups=len(groups))),flush=True)
   factor=prod(factorial(a)for monomial in pattern for a in monomial)%P
   signed=total*factor*(1 if label!='A4CD_probe0'else -1)%P
   values.append(signed)
   all_records.append(dict(symbol=index,pattern=label,coefficient_sum=total,
                           derivative_factor=factor,signed_value=signed,groups=records))
  matrix.append(values)
 expected=[[81,5,15],[22,95,1],[27,2,72]]
 assert matrix==expected,(matrix,expected)
 minor=sum(parity(pi)*prod(matrix[i][pi[i]]for i in range(3))for pi in permutations(range(3)))%P
 assert minor==46
 return dict(status='PASS',prime=P,degree=6,partition=[14,14,14,12],
             ambient_multiplicity=3,actual_determinant_multiplicity=3,
             padded_multiplicity_by_QC011=3,matrix=matrix,minor=minor,
             symbols=SYMBOLS,actual_polynomials=actual,ambient_weyl_terms=ambient['weyl_terms'],
             coefficient_records=all_records,seconds=round(time.monotonic()-start,3))

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,default=Path('work/quaternary/results/three_nonic_restrictions.json'))
 args=ap.parse_args();result=check()
 temporary=args.output.with_suffix('.json.tmp')
 temporary.write_text(json.dumps(result,indent=2)+'\n');temporary.replace(args.output)
 print(json.dumps({k:v for k,v in result.items()if k not in ('coefficient_records','ambient_weyl_terms','actual_polynomials','symbols')}),flush=True)
