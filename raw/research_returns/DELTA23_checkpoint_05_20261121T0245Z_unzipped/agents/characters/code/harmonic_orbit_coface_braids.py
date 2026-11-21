#!/usr/bin/env python3
"""Numerical discovery of quadratic harmonic orbit-replacement coface braid words.
The discovered words require independent exact topology/Artin verification.
"""
from pathlib import Path
import numpy as np,json,sys
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE.parent/'five_level_six'))
from cyclic12_cover import braid,red,wi
zeta=-1;angle=.173;rot=np.exp(1j*angle)
base=(.2,.8);ep=.01;small=ep**(1/2);close=(1+ep)**(1/2)

def segment_rot(start,end,n=2501):
 zz=np.linspace(start,end,n)
 return np.stack([base[0]*np.exp(1j*zz),np.full(n,base[1],complex)],axis=1)
def lollipop(zfixed,zmoving,n=2501):
 A=zfixed**2;B=zmoving**2;r=.1*A
 path=np.concatenate([np.linspace(B,A+r,n),A+r*np.exp(2j*np.pi*np.linspace(0,1,2*n)),np.linspace(A+r,B,n)])
 return np.power(path.astype(complex),1/2)
def source(word):
 if word=='u':return segment_rot(0,2*np.pi/2)
 if word=='U':return segment_rot(0,2*np.pi)
 j=int(word[1:]);yy=lollipop(*base)
 middle=np.stack([np.full(len(yy),base[0]*np.exp(2j*np.pi*j/2),complex),yy],axis=1)
 return np.concatenate([segment_rot(0,2*np.pi*j/2),middle,segment_rot(2*np.pi*j/2,0)])
def orbital(coords):
 z1,z2,z3=coords.T
 return np.stack([-z1,np.zeros(len(z1),complex),z1,z2,z3],axis=1)
def target(face,word):
 if face==0:
  coords=np.tile(np.array([.2,.8,1.5],complex),(10004,1))
  if word=='x':yy=lollipop(.2,.8);coords=np.tile([.2,.8,1.5],(len(yy),1)).astype(complex);coords[:,1]=yy
  else:yy=lollipop(.8,1.5);coords=np.tile([.2,.8,1.5],(len(yy),1)).astype(complex);coords[:,2]=yy
 else:
  ss=source(word);u,v=ss.T
  if face==1:coords=np.stack([small*u,u,v],axis=1)
  elif face==2:coords=np.stack([u,close*u,v],axis=1)
  elif face==3:coords=np.stack([u,v,close*v],axis=1)
  elif face==4:coords=np.stack([u,v,np.full(len(u),1.5)],axis=1)
  else:raise ValueError(face)
 pp=orbital(coords)
 # Holomorphic normalization sends labelled fifth point to infinity.
 out=1/(pp[:,:4]-pp[:,4,None])
 return out

def track(pp):
 pp=pp*rot;re=pp.real;im=pp.imag
 order=list(np.argsort(re[0]));expected=order.copy();crossings=[]
 for a in range(4):
  for b in range(a+1,4):
   diff=re[:,a]-re[:,b]
   at=np.flatnonzero(diff[:-1]*diff[1:]<0)
   for k in at:
    t=float(-diff[k]/(diff[k+1]-diff[k]));y=(1-t)*(im[k,a]-im[k,b])+t*(im[k+1,a]-im[k+1,b]);der=diff[k+1]-diff[k]
    sign=-1 if der*y>0 else 1
    crossings.append((k+t,a,b,sign))
 word=[];margin=1
 for time,a,b,sign in sorted(crossings):
  ia,ib=order.index(a),order.index(b)
  assert abs(ia-ib)==1,(time,a,b,order)
  gen=min(ia,ib)+1;word.append(sign*gen);order[ia],order[ib]=order[ib],order[ia]
 assert order==list(np.argsort(re[-1])),(order,list(np.argsort(re[-1])))
 # Initial real order after Mobius normalization is old labels4,3,2,1.
 assert expected==[3,2,1,0],expected
 word=[(4-abs(j))*(1 if j>0 else -1) for j in word]
 return list(red(word)),len(crossings)

def equal_mod_center(w,v):
 diff=sum(1 if j>0 else -1 for j in w)-sum(1 if j>0 else -1 for j in v)
 if diff%12:return False,None
 k=diff//12;central=(1,2,3)*4
 correction=central*(-k) if k<0 else wi(central)*k
 return braid(tuple(w)+tuple(correction))==braid(tuple(v)),k

out={}
for face in range(5):
 words=['x','y'] if face==0 else (['u','Y0'] if face==4 else ['U','Y0','Y1'])
 row={}
 for word in words:
  ww,ncross=track(target(face,word));row[word]={'braid_word':ww,'crossing_count':ncross}
  print(face,word,ww,flush=True)
 out[str(face)]=row
# Expected first tests in our proposed marking.
checks={
'face0x':equal_mod_center(out['0']['x']['braid_word'],[3,3]),
'face0y':equal_mod_center(out['0']['y']['braid_word'],[1,2]*3),
'face4u':equal_mod_center(out['4']['u']['braid_word'],[1,2,1]),
'face4Y0':equal_mod_center(out['4']['Y0']['braid_word'],[3,3]),
'face3U':equal_mod_center(out['3']['U']['braid_word'],[1,2]*3),
}
print(json.dumps(checks,indent=2));out['checks']=checks
(HERE/'records/harmonic_orbit_coface_braids_discovery.json').write_text(json.dumps(out,indent=2)+'\n')
