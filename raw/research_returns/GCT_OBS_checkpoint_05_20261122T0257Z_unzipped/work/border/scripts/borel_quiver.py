"""Exact Borel module quotients and finite flag enumeration (exploratory)."""
from collections import defaultdict,Counter
from br_linear import Space,rowspace,nullspace,rank,add,tensor,RECTS


def linear_apply(v,action):
 out=defaultdict(int)
 for i,x in v.items():
  for j,y in action(i).items():out[j]+=x*y
 return {i:x for i,x in out.items() if x}


def module(U,R,weight,root_actions):
 uspaces=defaultdict(Space);rspaces=defaultdict(Space)
 for v in U:
  w=weight(next(iter(v)));assert all(weight(i)==w for i in v)
  uspaces[w].append(v)
 for v in R:
  w=weight(next(iter(v)));assert all(weight(i)==w for i in v)
  rspaces[w].append(uspaces[w].reduce(v))
 blocks=[];index={}
 for w,s in rspaces.items():
  vectors=[dict(r) for r in s.canonical()]
  if vectors:index[w]=len(blocks);blocks.append((w,vectors))
 arrows=[]
 for w,vectors in blocks:
  maps=[]
  for action in root_actions:
   images=[linear_apply(v,action) for v in vectors]
   targets={weight(i) for v in images for i in v}
   assert len(targets)<=1
   if not targets:continue
   target=next(iter(targets));images=[uspaces[target].reduce(v) for v in images]
   if not any(images):continue
   j=index[target];bas=blocks[j][1];piv=[min(v) for v in bas];cols=[]
   for v in images:
    co={h:v.get(t,0) for h,t in enumerate(piv) if v.get(t,0)}
    assert linear_combination(bas,co)==v,('R is not root stable',w,target)
    cols.append(co)
   maps.append((j,cols))
  arrows.append(maps)
 return {'U':U,'blocks':blocks,'arrows':arrows}


def linear_combination(basis,v):
 out=defaultdict(int)
 for j,x in v.items():
  for i,y in basis[j].items():out[i]+=x*y
 return {i:x for i,x in out.items() if x}


def successors(M,F):
 spaces=[];free=[]
 for (w,basis),eq in zip(M['blocks'],F):
  s=Space()
  for row in eq:s.append(dict(row))
  spaces.append(s);free.append([i for i in range(len(basis)) if i not in s.rows])
 rigid=[];families=[]
 for i,indices in enumerate(free):
  if not indices:continue
  rows=[]
  for j,cols in M['arrows'][i]:
   mat=defaultdict(dict)
   for h,z in enumerate(indices):
    v=spaces[j].reduce(cols[z])
    for k,x in v.items():mat[k][h]=x
   rows.extend(tuple(r.items()) for r in mat.values())
  K=nullspace(rows,len(indices))
  if not K:continue
  vectors=[{indices[j]:x for j,x in v.items()} for v in K]
  if len(K)>1:families.append((i,vectors));continue
  G=list(F);G[i]=rowspace(F[i]+(tuple(vectors[0].items()),));rigid.append(tuple(G))
 return rigid,families


def extension_vectors(M,F):
 return [linear_combination(basis,dict(v)) for (w,basis),rows in zip(M['blocks'],F) for v in rows]


def variable_roots(support):
 index={v:i for i,v in enumerate(support)};roots=[]
 for axis in (0,1):
  for lo in range(3):
   def action(i,axis=axis,lo=lo):
    r,c=divmod(support[i],4);rc=[r,c]
    if rc[axis]!=lo+1:return {}
    rc[axis]=lo;return {index[4*rc[0]+rc[1]]:1}
   roots.append(action)
 return roots


def ab_module(S):
 support,U,aw,bw,blocks=tensor(S,-1);a=len(S);b=len(support)
 varroots=variable_roots(support);sp={q:i for i,q in enumerate(S)};rp={v:i for i,v in enumerate(RECTS)}
 actions=[]
 for axis in (0,1):
  for lo in range(3):
   dual=defaultdict(dict)
   for h,q in enumerate(S):
    pair=RECTS[q][axis]
    if lo+1 not in pair or lo in pair:continue
    new=tuple(lo if v==lo+1 else v for v in pair);sgn=1 if new[0]<new[1] else -1
    rect=list(RECTS[q]);rect[axis]=tuple(sorted(new));target=sp[rp[tuple(rect)]]
    dual[target][h]=-sgn
   vr=varroots[axis*3+lo]
   def act(coord,dual=dual,vr=vr):
    h,v=coord;out={(z,v):x for z,x in dual[h].items()}
    for z,x in vr(v).items():out[h,z]=out.get((h,z),0)+x
    return out
   actions.append(act)
 weight=lambda x:add(aw[x[0]],bw[x[1]])
 R=[{(h,v):1} for h in range(a) for v in range(b)]
 M=module(U,R,weight,actions);M.update({'subset':S,'support':support,'aw':aw,'bw':bw,'actions':actions})
 return M
