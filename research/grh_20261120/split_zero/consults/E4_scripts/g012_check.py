# Independent check of NEG_NIGHT NN-G012 from our own e3_constants.json (Table A, b2=-(q+1)^2/q), at v = i (q=-1, D=0)
import os,json,itertools
import sympy as sp
here=os.path.dirname(os.path.abspath(__file__))
v=sp.symbols('v'); I=sp.I
R=json.load(open(os.path.join(here,'e3_constants.json')))
C={}
for r in R: C[(r['b'],r['bp'],r['bpp'])]=sp.nsimplify(sp.sympify(r['c']).subs(v,I))
names=['Sigma','mu','g1_1','g1_12','g1_2','g1_21','g2_1','g2_12','g2_2','g2_21']
def prod(x,y):  # x,y dict name->coef ; returns dict
    out={}
    for a,ca in x.items():
        for b,cb in y.items():
            for z in names:
                c=C.get((a,b,z),0)
                if c!=0: out[z]=sp.simplify(out.get(z,0)+ca*cb*c)
    return {k:val for k,val in out.items() if val!=0}
q4=sp.Rational(1,4)
beta={'1':{'g2_1':1,'Sigma':q4},'2':{'g2_2':1,'Sigma':q4},'12':{'g2_12':1},'21':{'g2_21':1}}
E={'1':(0,1,8),'2':(1,0,8),'12':(0,0,16),'21':(1,1,16)}   # beta_x -> scale * E_{ij}  (0-based i,j)
ok=True
for x,y in itertools.product(beta,beta):
    lhs=prod(beta[x],beta[y])
    i,j,s=E[x]; k,l,t=E[y]
    rhs={}
    if j==k:
        # find z with E_{il}
        for z,(a,b,u) in E.items():
            if (a,b)==(i,l):
                for kk,val in beta[z].items(): rhs[kk]=sp.simplify(rhs.get(kk,0)+val*sp.Rational(s*t,u))
    if {k_:sp.simplify(v_) for k_,v_ in lhs.items()}!={k_:v_ for k_,v_ in rhs.items() if v_!=0}:
        ok=False; print('mismatch',x,y,lhs,rhs)
print('NN-G012 matrix-unit identification holds at v=i:',ok)
print('Sigma^2 =',prod({'Sigma':1},{'Sigma':1}),'  Sigma*beta_12 =',prod({'Sigma':1},beta['12']))
