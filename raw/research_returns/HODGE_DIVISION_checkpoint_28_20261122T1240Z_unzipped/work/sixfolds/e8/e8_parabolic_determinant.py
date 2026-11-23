#!/usr/bin/env python3
"""Fresh exact parabolic quotient and invariant form for the E8.mu4 tuple.

This uses only candidate matrix data from e8_group_and_tuple.json.
It does not read the preprint's Gram matrix or numerical certificates.
No period-dominance or algebraic-cycle conclusion is made.
"""
from pathlib import Path
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'g29'))
from gaussian_linear import *
from g29_determinants import invariant,star,ser
import sympy as S

source=json.loads(Path(__file__).with_name('e8_group_and_tuple.json').read_text())
gs=[[[K(F(a),F(b)) for a,b in row] for row in M] for M in source['tuple']]
m=8;r=12
def quotient(gs):
 vs=[];bs=[];offs=[0]
 for g in gs:
  D=sub(eye(m),g);piv=rref(D)[1];V=cols(D,piv);J=rowbasis_inverse(V)
  beta=mul(J,D);assert mul(V,beta)==D
  vs.append(V);bs.append(beta);offs.append(offs[-1]+len(piv))
 total=offs[-1];P=eye(m);rel=[]
 for V,g in zip(vs,gs):rel.append(mul(P,V));P=mul(P,g)
 assert P==eye(m) and total==22
 C=hcat(*rel);Z=null(C);B=neg(sum(bs,[]))
 assert iszero(mul(C,B)) and rank(C)==rank(B)==8
 comb=hcat(B,Z);piv=rref(comb)[1];Q=cols(comb,piv[m:]);E=hcat(B,Q)
 PJ=rowbasis_inverse(E)[m:]
 assert len(Q[0])==6 and mul(PJ,Q)==eye(6) and iszero(mul(PJ,B))
 return C,Z,B,Q,PJ,vs,bs,offs

def returns(gs):
 C,Z,B,Q,PJ,vs,bs,offs=quotient(gs);logs=[];meta=[]
 for length in range(2,11):
  for left in range(r-length+1):
   right=left+length-1;c=eye(m);D=zero(m,22)
   for j in range(left,right+1):
    V=mul(c,vs[j])
    for x in range(m):
     for y in range(offs[j+1]-offs[j]):D[x][offs[j]+y]=V[x][y]
    c=mul(c,gs[j])
   cp=eye(m);avg=zero(m,m)
   for order in range(1,241):
    avg=add(avg,cp);cp=mul(cp,c)
    if cp==eye(m):break
   else:raise AssertionError('finite local order bound')
   Dk=mul(avg,D)
   if iszero(Dk):continue
   M=eye(22)
   for j in range(left,right+1):
    block=mul(bs[j],Dk)
    for k,row in enumerate(block):M[offs[j]+k]=[x+y for x,y in zip(M[offs[j]+k],row)]
   assert iszero(mul(C,mul(M,Z))) and mul(M,B)==B
   N=sub(mul(PJ,mul(M,Q)),eye(6))
   assert iszero(mul(N,N))
   if not iszero(N):logs.append(N);meta.append([left+1,right+1,order,rank(N)])
 return logs,meta,Q

def cup(gs,cochains):
 data=quotient(gs);vs,offs=data[5],data[7]
 n=len(cochains[0]);prefix=eye(m);Fprev=zero(m,n);result=zero(n,n)
 coeff=[[K(x) for x in row] for row in source['coefficient_hermitian']]
 for j,g in enumerate(gs):
  D=sub(eye(m),g);piv=rref(D)[1]
  A=zero(m,len(piv))
  for k,col in enumerate(piv):A[col][k]=o
  U=cochains[offs[j]:offs[j+1]];value=mul(vs[j],U)
  lifted=add(mul(inv(prefix),Fprev),mul(A,U))
  result=add(result,mul(star(lifted),mul(coeff,value)))
  Fprev=add(Fprev,mul(prefix,value));prefix=mul(prefix,g)
 assert iszero(Fprev) and prefix==eye(m)
 assert star(result)==neg(result)
 return [[w*x for x in row] for row in result]

def main(output_path=None, tuple_label='Appendix A candidate tuple'):
 t=time.time();logs,meta,Q=returns(gs)
 print('parabolic K dimension6; nonzero return logs',len(logs),flush=True)
 # Published simplicial cup formula, recomputed on the complete cocycle space.
 data=quotient(gs);full=cup(gs,data[1]);H=cup(gs,Q)
 assert rank(full)==6 and det(H) and star(H)==H
 assert all(iszero(add(mul(star(N),H),mul(H,N))) for N in logs)
 # Coboundaries pair to zero on both sides in the full cocycle basis.
 J=rowbasis_inverse(data[1]);Bc=mul(J,data[2])
 assert iszero(mul(full,Bc)) and iszero(mul(star(Bc),full))
 dh=det(H);assert dh.a and not dh.b
 val=-dh.a;fac={int(p):int(e) for p,e in S.factorint(abs(val.numerator)).items()}
 for p,e in S.factorint(val.denominator).items():fac[int(p)]=fac.get(int(p),0)-int(e)
 inert={str(p):e for p,e in fac.items() if p%4==3 and e%2}
 report={'statement':'E8 candidate parabolic Hermitian discriminant',
  'date':'2026-11-21','model':'GPT-6 Astra Pro; inherited effort',
  'tuple_label':tuple_label,
  'quotient_K_dimension':6,'full_cocycle_dimension':14,'full_cup_rank':6,
  'cup_formula':'sum_i h(P_i^-1 F_i+a_i,c_i); Hermitian form i times the skew cup form',
  'coboundaries_are_full_radical':True,
  'determinant':dh.pair(),'minus_determinant_factorization':{str(p):e for p,e in fac.items()},
  'odd_inert_valuations':inert,'invariant_hermitian_form':ser(H),
  'quotient_basis':ser(Q),'return_intervals_orders_ranks':meta,
  'logarithms':list(map(ser,logs)),'elapsed_seconds':time.time()-t,
  'scope':'Exact matrix result. Identification with the geometric cup form is proved separately; no dominance claim.'}
 (Path(output_path) if output_path else Path(__file__).with_suffix('.json')).write_text(json.dumps(report,indent=2)+'\n')
 print('determinant',dh,'odd inert valuations',inert,flush=True)
 return report
if __name__=='__main__':main()
