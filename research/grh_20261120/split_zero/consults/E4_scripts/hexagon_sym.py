# All permutations of E^opp(3) (fixing Sigma, mu; permuting within or swapping the two 4-element cells) that preserve
# the structure-constant table as automorphisms c(px,py;pz)=c(x,y;z) or anti-automorphisms c(py,px;pz)=c(x,y;z)
import os,sys,json,itertools
here=os.path.dirname(os.path.abspath(__file__))
R=json.load(open(os.path.join(here,'e3_constants.json')))
C={(r['b'],r['bp'],r['bpp']):r['c'] for r in R}
c1=['g1_1','g1_12','g1_21','g1_2']; c2=['g2_1','g2_12','g2_21','g2_2']
def perms():
    for p1 in itertools.permutations(c1):
        for p2 in itertools.permutations(c2):
            for swap in (False,True):
                m={'Sigma':'Sigma','mu':'mu'}
                if not swap: m.update(zip(c1,p1)); m.update(zip(c2,p2))
                else: m.update(zip(c1,p2)); m.update(zip(c2,p1))
                yield m
def is_auto(m,anti):
    for (x,y,z),c in C.items():
        k=(m[y],m[x],m[z]) if anti else (m[x],m[y],m[z])
        if C.get(k)!=c: return False
    return len(C)==len({((m[y],m[x],m[z]) if anti else (m[x],m[y],m[z])) for (x,y,z) in C})
autos=[(m,a) for m in perms() for a in (False,True) if is_auto(m,a)]
print('symmetries found (auto/anti):',[(a,{k:v for k,v in m.items() if k!=v}) for m,a in autos])
fail=[(r['b'],r['bp'],r['bpp']) for r in R if not r['unimodal']]
def act(t,m,a):
    x,y,z=t; return (m[y],m[x],m[z]) if a else (m[x],m[y],m[z])
orbits=[]; seen=set()
for t in fail:
    if t in seen: continue
    orb={t}; frontier=[t]
    while frontier:
        s=frontier.pop()
        for m,a in autos:
            u=act(s,m,a)
            if u not in orb: orb.add(u); frontier.append(u)
    seen|=orb; orbits.append(sorted(orb))
print('group order',len(autos),' orbits of the six failing triples:',[len(o) for o in orbits]); [print(o) for o in orbits]
