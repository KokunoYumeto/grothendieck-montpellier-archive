"""Floating discovery of rank10 cofaces with one last-coordinate-two vector.
No mathematical assertion without a separate exact certificate.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np

base=Path(__file__).parent
source=json.loads((base/'k12_survivor_certificate.json').read_text())
q=np.array(source['integer_gram'],dtype=float)/36
mins=np.array(source['vectors'],dtype=int)
u=np.array([z for z in product((-1,0,1),repeat=9) if any(z) and next(x for x in z if x)>0],dtype=int)
values=np.einsum('ij,jk,ik->i',u,q,u)
alpha=(values+3)/(4*values)
cross=np.max(np.abs(u@q@mins.T),axis=1)*alpha
eligible=np.flatnonzero((values>3.05)&(values<5.2)&(cross<.499999))
eligible=sorted(eligible,key=lambda i:(cross[i],abs(values[i]-4)))
out=[]
attempts=0
for idx in eligible:
    attempts+=1
    vec=u[idx];ell=-alpha[idx]*(q@vec)
    gram=np.zeros((10,10));gram[:9,:9]=q;gram[9,:9]=ell;gram[:9,9]=ell;gram[9,9]=1
    upper=np.linalg.cholesky(gram).T
    z=np.zeros(10,dtype=int);found=[];nodes=[0]
    def visit(i,partial):
        nodes[0]+=1
        if nodes[0]>20000:raise RuntimeError('node cap')
        if i<0:
            if any(z):found.append(tuple(int(x) for x in z))
            return
        rem=1.00000001-partial
        if rem<0:return
        shift=float(upper[i,i+1:]@z[i+1:]);rad=np.sqrt(rem)/upper[i,i];center=-shift/upper[i,i]
        for x in range(int(np.ceil(center-rad-1e-8)),int(np.floor(center+rad+1e-8))+1):
            z[i]=x;visit(i-1,partial+(upper[i,i]*x+shift)**2)
    try:visit(9,0.0)
    except RuntimeError:continue
    target=[tuple(v)+ (0,) for v in mins]+[(0,)*9+(1,),tuple(int(x) for x in vec)+(2,)]
    signed=set(target)|{tuple(-x for x in v) for v in target}
    if set(found)!=signed:continue
    out.append({'u':vec.tolist(),'q_u':float(values[idx]),'alpha':float(alpha[idx]),'float_enumeration_nodes':nodes[0],'signed_minimum_count':len(found)})
    if len(out)>=5:break
result={'scope':'Floating discovery only, exact verification required','eligible_u_count':len(eligible),'attempts':attempts,'candidates':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
