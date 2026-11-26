import cmath, math
z=cmath.exp(2j*math.pi/8)
rows=[((0,1,2,4),(0,2,4,7),(0,2,4,7)),((0,1,4,6),(0,1,4,6),(0,1,4,6)),((0,1,2,4),(0,2,3,4),(0,2,3,4)),((0,1,2,5),(0,1,5,6),(0,2,5,6))]
Cs=[]
for A,B,C in rows:
    assert (sum(A)+sum(B)+sum(C))%8==1, (A,B,C)
    num=1
    for X in (A,B,C):
        for a in X:
            for b in X:
                if a!=b: num*= (1-z**(a-b))
    den=1; fixed=0
    for a in A:
        for b in B:
            for c in C:
                if (a+b+c)%8==0: fixed+=1
                else: den*=(1-z**(a+b+c))
    Cs.append(num/den); print('fixed support size',fixed,'C=',num/den)
r2=math.sqrt(2)
print('claimed', [1/256,(1+r2)/128,(3-2*r2)/256,-r2/256])
tot=3*Cs[0]+Cs[1]+3*Cs[2]+6*Cs[3]
print('sum',tot,'claimed',(14-10*r2)/256)
