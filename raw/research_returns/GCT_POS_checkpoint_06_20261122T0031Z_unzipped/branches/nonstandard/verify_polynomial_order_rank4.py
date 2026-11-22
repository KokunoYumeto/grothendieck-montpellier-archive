"""Independent replay of the actual Q[D]-order certificate.

Does not import either polynomial-order search script.  Reconstructs the
opposite KL basis in the standard T basis, derives right multiplication
by T_s, and uses the expanded standard-T formula for P_s.  The recorded
straight-line program then proves actual word membership of every row.
Triangular division, all basis-generator products, and the identity prove
full algebra equality; no degree cutoff or generic-rank input is assumed.
Requires python-flint and the unchanged supplied e4lib arithmetic.
"""
from pathlib import Path
from collections import Counter
from math import comb
import sys,json,gzip,time
from flint import fmpq,fmpq_poly

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'dependencies'))
import e4lib as h
ZERO=fmpq_poly([]);ONE=fmpq_poly([1])
DELTA={1:1,-1:1};VMV={1:1,-1:-1};SCALAR={2:1,-2:1}


def axpy(x,y,c):
    for j,a in y.items():
        b=x.get(j,ZERO)+c*a
        if b:x[j]=b
        else:x.pop(j,None)


def combination(x,a,y,b):
    z={j:c*a for j,c in x.items() if c*a}
    axpy(z,y,b)
    return z


def polynomial(p):
    if not p:return ZERO
    return fmpq_poly([fmpq(p.get(str(i),'0')) for i in range(max(map(int,p))+1)])


def vector(v):return {int(j):polynomial(p) for j,p in v.items()}


def factor_delta(p,epsilon):
    """Recover p(v)=delta^epsilon f(D), verifying every Laurent term."""
    p=dict(p);ans={}
    assert all(p.get(-e,0)==c for e,c in p.items())
    while p:
        e=max(p);c=p[e]
        assert e>=epsilon and (e-epsilon)%2==0
        ans[(e-epsilon)//2]=c
        power={e-2*j:comb(e,j) for j in range(e+1)}
        p=h.padd(p,{k:c*a for k,a in power.items()},-1)
    return fmpq_poly([ans.get(i,0) for i in range(max(ans,default=-1)+1)])


def make_operators(keys):
    # v -> v^-1, T_i -> -T_i is semilinear and preserves the Hecke relation.
    # It sends C'_w to (-1)^length(w) C_w; this reconstructs the opposite
    # KL basis itself, rather than inferring word coordinates by a sign.
    C={w:{x:{-e:(-1)**(h.length(w)-h.length(x))*a for e,a in p.items()}
          for x,p in co.items()} for w,co in h.Cp.items()}

    def coordinates(x):
        x=dict(x);out={}
        while x:
            w=max(x,key=h.length);p=x[w];out[w]=p
            x=h.hadd(x,h.hscale(C[w],p),-1)
        return out

    rightT={(w,i):coordinates(h.mulTs(C[w],s))
            for w in h.G for i,s in enumerate(h.S)}
    index={k:j for j,k in enumerate(keys)}
    operators=[]
    for i in range(3):
        op=[]
        for a,b in keys:
            eps=(h.length(a)+h.length(b))%2
            gauge=DELTA if eps else {0:1}
            out={}

            def put(c,d,p):
                if c>d:return
                j=index[c,d]
                out[j]=h.padd(out.get(j,{}),h.pmul(gauge,p))
                if not out[j]:del out[j]

            for x,y in [(a,b)] if a==b else [(a,b),(b,a)]:
                put(x,y,SCALAR)
                for c,p in rightT[x,i].items():
                    put(c,y,{e:-z for e,z in h.pmul(VMV,p).items()})
                for d,q in rightT[y,i].items():
                    put(x,d,{e:-z for e,z in h.pmul(VMV,q).items()})
                for c,p in rightT[x,i].items():
                    for d,q in rightT[y,i].items():
                        put(c,d,{e:2*z for e,z in h.pmul(p,q).items()})
            op.append({j:factor_delta(p,(h.length(keys[j][0])+h.length(keys[j][1]))%2)
                       for j,p in out.items()})
        operators.append(op)
    return operators


def step(x,op):
    ans={}
    for j,p in x.items():axpy(ans,op[j],p)
    return ans


def main():
    started=time.time()
    metadata=json.loads((HERE/'polynomial_order_rank4_verified.json').read_text())
    with gzip.open(HERE/'polynomial_order_rank4_rows.json.gz','rt') as f:data=json.load(f)
    keys=[(tuple(a),tuple(b)) for a,b in data['coordinates']]
    assert keys==[(a,b) for a in h.G for b in h.G if a<=b]
    ops=make_operators(keys)
    one={keys.index((h.e,h.e)):ONE}
    words=[tuple(w) for w in metadata['accepted_words']]
    word_vectors={():one}
    vectors=[]
    for w in words:
        if w:word_vectors[w]=step(word_vectors[w[:-1]],ops[w[-1]-1])
        vectors.append(word_vectors[w])
    rows={r['pivot']:vector(r['vector']) for r in data['rows']}
    assert len(rows)==len(data['rows'])==114
    for j,b in rows.items():
        assert min(b)==j and b[j].leading_coefficient()==1

    nodes=data['straight_line_program']
    finals=[r['slp_node'] for r in data['rows']]
    uses=Counter(finals)
    for node in nodes:
        if 'word' not in node:
            uses[node['a']]+=1
            if node['b'] is not None:uses[node['b']]+=1
    cache={}
    for i,node in enumerate(nodes):
        if 'word' in node:
            assert 0<=node['word']<len(vectors)
            cache[i]=vectors[node['word']]
        else:
            a,b=node['a'],node['b']
            assert 0<=a<i and (b is None or 0<=b<i)
            cache[i]=combination(cache[a],polynomial(node['p']),
                                 {} if b is None else cache[b],polynomial(node['q']))
            for k in [a,b]:
                if k is None:continue
                uses[k]-=1
                if not uses[k]:del cache[k]
    for rec in data['rows']:assert cache[rec['slp_node']]==rows[rec['pivot']]

    def contains(x):
        x=dict(x)
        while x:
            j=min(x)
            if j not in rows:return False
            q,r=divmod(x[j],rows[j][j])
            if r:return False
            axpy(x,rows[j],-q)
        return True

    assert contains(one)
    assert all(contains(x) for x in vectors)
    assert all(contains(step(row,op)) for row in rows.values() for op in ops)
    result={'status':'PASS','coefficient_ring':'Q[D]','rank':len(rows),
            'word_count':len(words),'maximum_word_length':max(map(len,words)),
            'exact_operator_columns':len(keys)*3,
            'exact_basis_generator_products':len(rows)*3,
            'straight_line_nodes_replayed':len(nodes),
            'actual_unsaturated_word_order':True,
            'inherited_generic_dimension_used':False,
            'seconds':time.time()-started,
            'scope':'Independent arithmetic/certificate path, same author; not an independent whole-proof review.'}
    (HERE/'polynomial_order_rank4_independent_arithmetic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
