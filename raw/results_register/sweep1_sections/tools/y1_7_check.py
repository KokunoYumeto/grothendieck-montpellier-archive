from fractions import Fraction as F
a1,a2,a3,a4,a6=F(-1),F(-4),F(-4),F(0),F(0)
b2=a1*a1+4*a2; b4=2*a4+a1*a3; b6=a3*a3+4*a6; b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
D=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
print("discriminant",D)
def on(P):
    x,y=P; return y*y+a1*x*y+a3*y-(x**3+a2*x*x+a4*x+a6)==0
def neg(P):
    x,y=P; return (x,-y-a1*x-a3)
def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    (x1,y1),(x2,y2)=P,Q
    if x1==x2 and y1+y2+a1*x2+a3==0: return None
    if x1==x2:
        l=(3*x1*x1+2*a2*x1+a4-a1*y1)/(2*y1+a1*x1+a3); nu=(-x1**3+a4*x1+2*a6-a3*y1)/(2*y1+a1*x1+a3)
    else:
        l=(y2-y1)/(x2-x1); nu=(y1*x2-y2*x1)/(x2-x1)
    x3=l*l+a1*l-a2-x1-x2; y3=-(l+a1)*x3-nu-a3
    return (x3,y3)
P=(F(0),F(0)); print("on curve",on(P))
Q=None
for n in range(1,9):
    Q=add(Q,P); print(n,Q)
    if Q is None: print("order",n); break
