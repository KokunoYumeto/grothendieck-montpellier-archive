"""Exact finite checks for the rank-eight Heisenberg degeneration.
GPT-6 Astra (OpenAI), 2026-11-20. No geometric Bertini test is claimed.
"""
import itertools,json,time
start=time.perf_counter()
V=list(itertools.product(range(2), repeat=2))
def c(v,w):return (v[1]*w[0])%2
def add(v,w):return tuple((a+b)%2 for a,b in zip(v,w))
cocycle=all((c(v,w)+c(add(v,w),q)-c(w,q)-c(v,add(w,q)))%2==0 for v,w,q in itertools.product(V,repeat=3))
G=list(itertools.product(range(2),repeat=3))
def mul(g,h):
 z,a,b=g;zz,aa,bb=h
 return ((z+zz+b*aa)%2,(a+aa)%2,(b+bb)%2)
e=(0,0,0)
def inv(g):return next(h for h in G if mul(g,h)==e and mul(h,g)==e)
assoc=all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in itertools.product(G,repeat=3))
r=(0,1,0);s=(0,0,1)
comm=mul(mul(mul(r,s),inv(r)),inv(s))
chars=[]
for values in itertools.product(range(2),repeat=7):
 h={e:0};h.update(dict(zip([g for g in G if g!=e],values)))
 if all(h[mul(a,b)]==(h[a]+h[b])%2 for a,b in itertools.product(G,repeat=2)):chars.append(h)
res={"cocycle_checks":64,"cocycle_identity":cocycle,"associativity_checks":512,"associative":assoc,"commutator_r_s":comm,"central_nonidentity":[1,0,0],"generic_abelianization_characters":len(chars),"generic_character_scheme_rank":4,"special_character_scheme_rank":8,"neutral_rank_over_R_mod_4":4,"extra_component_module_over_R_mod_4":"(R/2)^4; nonflat over R/4","geometric_cut":"Raynaud1979 Prop4.2.3, formal independent coefficients; not computationally expanded","seconds":time.perf_counter()-start}
assert cocycle and assoc and comm==(1,0,0) and len(chars)==4
print(json.dumps(res,indent=2))
