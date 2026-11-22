"""Exact finite checks for the baseline-free crossed-module realization theorem.
No external packages. We enumerate all normalized cochains in the stated small
families, and verify group laws, centres and derived subgroups independently.
"""
from itertools import product
from pathlib import Path
import json,time,datetime
START=time.perf_counter()
OUT={"run_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}

def generated(elements, op, inv, ident):
    s={ident}; todo=list(elements)
    while todo:
        x=todo.pop()
        if x in s: continue
        old=list(s);s.add(x);todo.append(inv(x))
        for y in old:todo.extend((op(x,y),op(y,x)))
    return s

def check_group(elements,op,ident,do_assoc=True):
    eset=set(elements);inv={}
    for a in elements:
        assert op(ident,a)==op(a,ident)==a
        for b in elements:assert op(a,b) in eset
        both=[b for b in elements if op(a,b)==ident and op(b,a)==ident]
        assert len(both)==1
        inv[a]=both[0]
    triples=0
    if do_assoc:
        for a,b,c in product(elements,repeat=3):
            assert op(op(a,b),c)==op(a,op(b,c));triples+=1
    centre={a for a in elements if all(op(a,b)==op(b,a) for b in elements)}
    comm=[op(op(op(a,b),inv[a]),inv[b]) for a,b in product(elements,repeat=2)]
    derived=generated(comm,op,lambda a:inv[a],ident)
    return centre,derived,triples

# Nonzero H^3 obstruction: N=K=Z/4, d=2, odd K acts by inversion.
N=range(4);Q=range(2);C=(0,2)
act=lambda l,n: ((-1)**l*n)%4
d=lambda n:2*n%4
crosschecks=0
for l,n in product(N,repeat=2):
    assert d(act(l,n))==d(n);crosschecks+=1
for n,m in product(N,repeat=2):
    assert act(d(n),m)==m;crosschecks+=1
f=lambda x,y:int(x==y==1)
a=lambda x,y,z:(act(x,f(y,z))+f(x,(y+z)%2)-f((x+y)%2,z)-f(x,y))%4
for vals in product(Q,repeat=3):assert a(*vals) in C
for x,y,z,w in product(Q,repeat=4):
    assert (a(y,z,w)-a((x+y)%2,z,w)+a(x,(y+z)%2,w)-a(x,y,(z+w)%2)+a(x,y,z))%4==0
solutions=[]
for v in C:
    t=lambda x,y:v if x==y==1 else 0
    if all((t(y,z)+t(x,(y+z)%2)-t((x+y)%2,z)-t(x,y)+a(x,y,z))%4==0 for x,y,z in product(Q,repeat=3)):
        solutions.append(v)
assert a(1,1,1)==2 and not solutions
OUT['nonzero_obstruction']={'crossed_module_identities_checked':crosschecks,'three_cocycle_quadruples':16,'normalized_two_cochains':2,'trivializations':solutions,'o_111_in_Z4':2}

# All normalized cochains Q^2->C2 for Q=C2^2.
Q=range(4);pairs=list(product(range(1,4),repeat=2));els=list(product(range(2),Q))
valid=admissible=assoc=0;classes=set();goodclasses=set();signatures=[]
# coboundaries of all 1-cochains Q->C2 normalized at 0
cob=[]
for vals in product(range(2),repeat=3):
    u=(0,)+vals
    cob.append(tuple(u[x]^u[y]^u[x^y] for x,y in pairs))
for bits in product(range(2),repeat=9):
    table=dict(zip(pairs,bits))
    c=lambda x,y:table.get((x,y),0)
    if not all((c(y,z)^c(x,y^z)^c(x^y,z)^c(x,y))==0 for x,y,z in product(Q,repeat=3)):continue
    valid+=1
    op=lambda a,b:(a[0]^b[0]^c(a[1],b[1]),a[1]^b[1])
    Z,D,num=check_group(els,op,(0,0));assoc+=num
    pairing=lambda x,y:c(x,y)^c(y,x)
    rad={x for x in Q if all(pairing(x,y)==0 for y in Q)}
    image={pairing(x,y) for x,y in product(Q,repeat=2)}
    criterion=(rad=={0} and image=={0,1})
    brute=(Z=={(0,0),(1,0)} and D=={(0,0),(1,0)})
    assert criterion==brute
    equiv=min(tuple(a^b for a,b in zip(bits,db)) for db in cob)
    classes.add(equiv)
    if brute:admissible+=1;goodclasses.add(equiv)
    signatures.append({'cochain_bits':''.join(map(str,bits)),'centre_order':len(Z),'derived_order':len(D),'criterion':criterion})
assert (valid,admissible,len(classes),len(goodclasses))==(16,8,8,4)
OUT['all_C2_squared_cochains']={'candidates':512,'cocycles':valid,'marked_extension_classes':len(classes),'admissible_cocycles':admissible,'admissible_marked_classes':len(goodclasses),'associativity_triples':assoc,'signatures':signatures}

# Nonabelian derived subgroup: H=Heis(F3), G=H semidirect C2.
H=list(product(range(3),repeat=3))
def hm(u,v):
    a,b,z=u;c,d,w=v
    return ((a+c)%3,(b+d)%3,(z+w+2*(a*d-b*c))%3)
def ha(t,u):
    a,b,z=u
    return (((-1)**t*a)%3,((-1)**t*b)%3,z)
E=list(product(H,range(2)))
def op(u,v):return (hm(u[0],ha(u[1],v[0])),u[1]^v[1])
Z,D,num=check_group(E,op,((0,0,0),0))
expectedZ={((0,0,z),0) for z in range(3)}
expectedD={(h,0) for h in H}
assert Z==expectedZ and D==expectedD
assert any(hm(u,v)!=hm(v,u) for u,v in product(H,repeat=2))
OUT['nonabelian_derived_example']={'group_order':54,'kernel_N_order':27,'N_nonabelian':True,'centre_order':len(Z),'derived_order':len(D),'associativity_triples':num,'centre_equals_Z':True,'derived_equals_N':True}
OUT['elapsed_seconds']=time.perf_counter()-START
out=Path(__file__).resolve().parents[1]/'logs/C4_finish_realization_certificate.json'
out.write_text(json.dumps(OUT,indent=2)+'\n')
print(json.dumps(OUT,indent=2))
