"""Construct N-024's Laurent-parameter family and exact minimizers.

Sympy constructs the entire table.  The separate verifier uses Laurent
dictionaries, direct source expressions and matrix products.  The optimum
claim is for the precise family in the accompanying proof, not all tables.
"""
from pathlib import Path
from itertools import product
import json,sympy as s
q=s.Symbol('q');D=q+2+1/q;u=q+1/q;a=(D-1)*u
WORDS=('1','12','2','21');NAMES=['mu','Sigma']+[f'g{i}_{x}' for i in (1,2) for x in WORDS]

def laurent(p):
    result={}
    for term in s.Add.make_args(s.expand(p)):
        c,e=term.as_coeff_exponent(q)
        assert c.is_Integer and e.is_Integer,(p,term)
        result[int(e)]=result.get(int(e),0)+int(c)
    return {e:c for e,c in result.items() if c}

def reduce_word(x):
    alpha=beta=0
    while True:
        for k in range(len(x)-1):
            if x[k]==x[k+1]:x=x[:k]+x[k+1:];alpha+=1;break
        else:
            if len(x)<3:return x,alpha,beta
            x=x[2:];beta+=1

def table(W,L):
    G={1:2*W*a,2:W*a};K={1:u,2:D};S=2*W*a*a
    ans={}
    for b in NAMES:ans['mu',b,b]=ans[b,'mu',b]=1
    ans['Sigma','Sigma','Sigma']=S
    for i,x in product((1,2),WORDS):
        b=f'g{i}_{x}';ans['Sigma',b,'Sigma']=ans[b,'Sigma','Sigma']=K[i]**(len(x)-1)*G[i]
    for i,j,x,y in product((1,2),(1,2),WORDS,WORDS):
        b,c=f'g{i}_{x}',f'g{j}_{y}'
        if i!=j:ans[b,c,'Sigma']=W*K[i]**(len(x)-1)*K[j]**(len(y)-1);continue
        z,al,be=reduce_word(x+y)
        ans[b,c,f'g{i}_{z}']=a*D**al*(u if i==1 else L)**be
        if i==1:ans[b,c,'Sigma']=2*W*u**(len(x)+len(y)-2)-D**al*u**(be+len(z)-1)
        else:ans[b,c,'Sigma']=D**(len(z)+al-2+be)*((D*W-L)/2 if be else (W-D)/2)
    return {key:laurent(p) for key,p in ans.items() if s.expand(p)!=0}

def main():
    F=q**-1+q**3
    L=4*q**4-4*q**3-q**2+6*q-2-2/q+3/q**2
    cases=[('general',F,L,3898),('general_reversed',F.subs(q,1/q),L.subs(q,1/q),3898),
           ('bar',u,3*D**2-10*D,4046),('bar_alternative',u,3*D**2-14*D+16,4046)]
    out=[]
    for name,F,L,score in cases:
        W=3*D+4*F;t=table(W,L)
        out.append({'name':name,'F':laurent(F),'W':laurent(W),'Lambda':laurent(L),
                    'expected_score':score,'table':[{'inputs':[x,y],'output':z,'q_coefficients':p} for (x,y,z),p in sorted(t.items())]})
    target=(q**4+q**-4)+(q**3+q**-3)+2*(q**2+q**-2)+3*(q+q**-1)+2
    Cmin=target+2*(q**4+q**-4)
    proof={'absolute_cell_trace':laurent(target),'Cmin':laurent(Cmin),
           'Cmin_mass':int(Cmin.subs(q,1)),'Cmin_at_i':str(s.expand(Cmin.subs(q,s.I))),
           'Cmin_mod_q2_q_plus_1':str(s.rem(s.expand(Cmin*q**4),q**2+q+1,q)),
           'general_minimum_in_family':3898,'bar_minimum_in_family':4046,
           'unrestricted_all_tables_minimum':'NOT_COMPUTED'}
    path=Path(__file__).with_name('dimension_scale_family_certificate.json')
    path.write_text(json.dumps({'status':'CONSTRUCTED_PENDING_SEPARATE_REPLAY','cases':out,'proof_data':proof},indent=2)+'\n')
    print('saved four full tables; family minima3898 and4046; all-table optimum open')

if __name__=='__main__':main()
