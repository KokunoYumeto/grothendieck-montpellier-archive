# Structure constants of VIII's E^opp(3) by word rewriting in nsH_3 (basis: alternating words of length <= 5 except yxyxy)
import os,sys,json,itertools
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
import sympy as sp
from classify import classify, v
q=v**2; D=(v+1/v)**2; A1=D; A2=(D-2)**2
WORDS=[(),(1,),(2,),(1,2),(2,1),(1,2,1),(2,1,2),(1,2,1,2),(2,1,2,1),(1,2,1,2,1)]
def reduce_word(w):
    """return dict word->sympy coeff, w a tuple over {1,2}"""
    out={}; stack=[(tuple(w),sp.Integer(1))]
    while stack:
        w,c=stack.pop()
        # adjacent repeats
        for i in range(len(w)-1):
            if w[i]==w[i+1]:
                stack.append((w[:i]+w[i+1:],c*D)); break
        else:
            if len(w)>=5:
                # find a length-5 alternating block starting with 2 (yxyxy) or any length-6
                if len(w)>=6 or w[0]==2:
                    # rewrite the first 5 letters if they are 2,1,2,1,2 ; else rewrite last 5 letters 2,1,2,1,2 occurring
                    for i in range(len(w)-4):
                        if w[i:i+5]==(2,1,2,1,2):
                            pre,post=w[:i],w[i+5:]
                            for ww,cc in (((1,2,1,2,1),1),((1,2,1),-(A1+A2)),((2,1,2),(A1+A2)),((1,),A1*A2),((2,),-A1*A2)):
                                stack.append((pre+ww+post,c*cc))
                            break
                    else:
                        # length>=6 starting with 1: 1,2,1,2,1,2 -> contains 2,1,2,1,2 at i=1
                        raise RuntimeError(w)
                    continue
            out[w]=sp.expand(out.get(w,0)+c)
    return {k:cc for k,cc in out.items() if sp.simplify(cc)!=0}
b1=-(q**2+1)**2/q**2; b2=-(q+1)**2/q
c1=(q**6+2*q**5+3*q**4+4*q**3+3*q**2+2*q+1)/q**3; c2=(q**4+q**3+4*q**2+q+1)/q**2
B={'Sigma':{(1,):c1,(1,2,1):-c2,(1,2,1,2,1):1},'mu':{():1}}
for i,b in ((1,b1),(2,b2)):
    B[f'g{i}_1']={(1,):b,(1,2,1):1}; B[f'g{i}_12']={(1,2):b,(1,2,1,2):1}
    B[f'g{i}_2']={(2,):b,(2,1,2):1}; B[f'g{i}_21']={(2,1):b,(2,1,2,1):1}
names=list(B)
M=sp.Matrix([[B[nm].get(w,0) for nm in names] for w in WORDS])
Minv=M.inv().applyfunc(sp.cancel)
def prod(x,y):
    out={}
    for w1,c1_ in B[x].items():
        for w2,c2_ in B[y].items():
            for w,c in reduce_word(w1+w2).items():
                out[w]=out.get(w,0)+c1_*c2_*c
    return sp.Matrix([sp.cancel(out.get(w,0)) for w in WORDS])
res=[]
for x in names:
    for y in names:
        sol=(Minv*prod(x,y)).applyfunc(sp.cancel)
        for k,c in zip(names,sol):
            if c!=0:
                r=classify(c); res.append({'b':x,'bp':y,'bpp':k,'c':str(sp.factor(c)),**{kk:(str(vv) if kk=='f' else vv) for kk,vv in r.items()}})
json.dump(res,open(os.path.join(here,'e3_constants.json'),'w'),indent=0,default=lambda o: int(o) if getattr(o,'is_Integer',False) else str(o))
print('nonzero constants',len(res))
