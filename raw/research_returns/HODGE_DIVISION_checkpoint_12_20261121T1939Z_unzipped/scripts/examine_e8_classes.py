"""Exact exploratory E8 class arithmetic from the author's CHEVIE class words.

This script does not prove class-list completeness independently. Carter's
classification and the CHEVIE author's documented class representatives are
the explicit source for that list. Every matrix and polynomial below is
recomputed. The retained JSON contains mathematical witness data, not the
third-party library code. No period-rank or cycle claim is made.
"""
from pathlib import Path
import ast, hashlib, json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'research/sources/chevie/weyle8.g'
txt=source.read_text() if source.exists() else ''
def bracket_after(token):
    start=txt.index('[',txt.index(token))
    depth=0; quoted=False; escape=False
    for j in range(start,len(txt)):
        c=txt[j]
        if quoted:
            if escape: escape=False
            elif c=='\\': escape=True
            elif c=='"': quoted=False
            continue
        if c=='"': quoted=True
        elif c=='[':depth+=1
        elif c==']':
            depth-=1
            if depth==0:return ast.literal_eval(txt[start:j+1])
    raise ValueError(token)

if source.exists():
    words0=bracket_after('CHEVIE.AddData("WordsClassRepresentatives"')
    names=bracket_after('CHEVIE.AddData("ClassNames"')
    orders=bracket_after('orders:=')
    sizes=bracket_after('classes:=')
    source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
else:
    # Checkpoint reproduction needs only the retained mathematical witnesses.
    old=json.loads((ROOT/'research/e8_class_exploration.json').read_text())
    words0=[r['word'] for r in old['classes']]
    names=[r['name'] for r in old['classes']]
    orders=[r['order'] for r in old['classes']]
    sizes=[r['class_size'] for r in old['classes']]
    source_hash=old['source_sha256']
assert len(words0)==len(names)==len(orders)==len(sizes)==112
assert sum(sizes)==696729600
roots=[S.Matrix([1,-1,-1,-1,-1,-1,-1,1])/2,
       S.Matrix([1,1,0,0,0,0,0,0]),S.Matrix([-1,1,0,0,0,0,0,0]),
       S.Matrix([0,-1,1,0,0,0,0,0]),S.Matrix([0,0,-1,1,0,0,0,0]),
       S.Matrix([0,0,0,-1,1,0,0,0]),S.Matrix([0,0,0,0,-1,1,0,0]),
       S.Matrix([0,0,0,0,0,-1,1,0])]
B=S.Matrix.hstack(*roots);H=B.T*B;assert H.det()==1
I=S.eye(8)
gens=[I-I[:,j]*H[j,:] for j in range(8)]
assert all(g*g==I and g.T*H*g==H for g in gens)
x=S.Symbol('x');desired=S.Poly(S.cyclotomic_poly(12,x)*S.cyclotomic_poly(3,x)*S.cyclotomic_poly(6,x),x)
rows=[]
for index,(name,word0,order,size) in enumerate(zip(names,words0,orders,sizes),1):
    word=[k for a in word0 for k in (range(1,9) if a==0 else [a])]
    w=I
    for j in word:w=w*gens[j-1]
    assert w.T*H*w==H and w**order==I
    assert all(w**(order//p)!=I for p in S.factorint(order))
    cp=w.charpoly(x).as_poly();factors=[(str(a.as_expr()),int(b)) for a,b in S.factor_list(cp)[1]]
    value=S.expand(cp.as_expr().subs(x,-S.I))
    row={'index':index,'name':name,'class_size':size,'order':order,'word':word,
         'characteristic_polynomial':str(cp.as_expr()),'factors':factors,
         'det_one_minus_iw':str(value),'candidate':cp==desired,
         'matrix':[[int(a) for a in w.row(j)] for j in range(8)]}
    rows.append(row)
out={'status':'PASS','source_url':'https://raw.githubusercontent.com/jmichel7/gap3-jm/master/pkg/chevie/tbl/weyle8.g',
     'source_sha256':source_hash,
     'source_scope':'CHEVIE complete class representatives; independently recomputed matrices, orders, orthogonality and characteristic polynomials',
     'cartan':[[int(a) for a in H.row(j)] for j in range(8)],'classes':rows,
     'candidate_indices':[r['index'] for r in rows if r['candidate']]}
p=ROOT/'research/e8_class_exploration.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','class_count':len(rows),'candidate_indices':out['candidate_indices'],
                  'candidate_names':[r['name'] for r in rows if r['candidate']],
                  'nonsquare_odd_det_examples':[(r['index'],r['name'],r['det_one_minus_iw']) for r in rows if r['det_one_minus_iw'] in ['3','-3','3*I','-3*I']]}))
