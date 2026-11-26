import math
c=1/math.sqrt(2)
d=1.25-1/(2*math.sqrt(2))/math.tan(c)
f0=lambda v: math.cos(math.sqrt(2)*v)/(math.sqrt(2)*math.sin(c)) if abs(v)<=0.5 else 0.0
n=4000
h=1.0/n
xs=[-0.5+(i+0.5)*h for i in range(n)]
I1=sum(f0(x) for x in xs)*h
A=sum(f0(x)**2 for x in xs)*h
# w(v)=int f0(y)f0(y-v)dy ; B=int |v| w(v) dv = E|X-Y| under f0 x f0
B=0.0
vals=[f0(x) for x in xs]
for i in range(0,n,4):
  for j in range(0,n,4):
    B+=vals[i]*vals[j]*abs(xs[i]-xs[j])
B*=(4*h)**2
print('d',d,'1/d',1/d,'int f0',I1,'A',A,'B',B,'A+B',A+B,'1/2+c cot c',0.5+c/math.tan(c),'3-2d',3-2*d)
print('A<=51/50',A<=1.02,'B<=1/3',B<=1/3,'5/6<d<=7/8',5/6<d<=7/8)
