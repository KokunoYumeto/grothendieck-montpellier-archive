"""Exact Q[D] word-order closure, with Flint polynomial arithmetic.

This accelerates the same unsaturated module problem as
polynomial_order_rank4.py.  In addition to Euclidean row insertion it
reduces all entries above each pivot, to control coefficient growth.
Every operation is tracked by a compact straight-line program starting
from actual accepted P-words; expanded polynomial word coefficients
are intentionally not stored.
Requires python-flint; all arithmetic is exact.
"""
from pathlib import Path
from collections import Counter
import sys,json,gzip,time
from flint import fmpq, fmpq_poly
import polynomial_order_rank4 as source

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([])
ONE=fmpq_poly([1])


def convert(p):
    if not p:return ZERO
    return fmpq_poly([fmpq(str(p.get((i,),0))) for i in range(p.degree()+1)])


OPS=[[{j:convert(p) for j,p in row.items()} for row in op]
     for op in source.OPS]


def axpy(x,y,c):
    if not c:return
    for j,a in y.items():
        b=x.get(j,ZERO)+c*a
        if b:x[j]=b
        else:x.pop(j,None)


def combination(x,a,y,b):
    z={j:c*a for j,c in x.items() if c*a}
    axpy(z,y,b)
    return z


def step(x,si):
    z={}
    for j,p in x.items():axpy(z,OPS[si][j],p)
    return z


class StraightLineProgram:
    def __init__(self):self.nodes=[]

    def word(self,i):
        self.nodes.append(("word",i))
        return len(self.nodes)-1

    def combine(self,i,a,j=None,b=ZERO):
        if not b and a==ONE:return i
        self.nodes.append(("combine",i,a,j,b))
        return len(self.nodes)-1

    def compact(self,finals):
        needed=set(finals);todo=list(finals)
        while todo:
            node=self.nodes[todo.pop()]
            if node[0]=="word":continue
            for i in [node[1],node[3]]:
                if i is not None and i not in needed:
                    needed.add(i);todo.append(i)
        ordered=sorted(needed);mapping={n:i for i,n in enumerate(ordered)}
        nodes=[]
        for k in ordered:
            node=self.nodes[k]
            if node[0]=="word":nodes.append(node)
            else:nodes.append(("combine",mapping[node[1]],node[2],
                               None if node[3] is None else mapping[node[3]],node[4]))
        return nodes,[mapping[n] for n in finals]


class Module:
    def __init__(self):
        self.rows={}
        self.expressions={}
        self.slp=StraightLineProgram()
        self.updates=0

    def contains(self,x):
        x=dict(x)
        while x:
            j=min(x)
            if j not in self.rows:return False
            q,r=divmod(x[j],self.rows[j][j])
            if r:return False
            axpy(x,self.rows[j],-q)
        return True

    def reduce_above(self):
        pivots=sorted(self.rows)
        for j in reversed(pivots):
            x,e=self.rows[j],self.expressions[j]
            for k in pivots:
                if k<=j or k not in x:continue
                q,r=divmod(x[k],self.rows[k][k])
                if q:
                    axpy(x,self.rows[k],-q)
                    e=self.slp.combine(e,ONE,self.expressions[k],-q)
                assert x.get(k,ZERO)==r
            self.expressions[j]=e

    def add(self,x,expr):
        x,e=dict(x),expr
        changed=False
        while x:
            j=min(x)
            if j not in self.rows:
                scale=1/x[j].leading_coefficient()
                self.rows[j]={k:p*scale for k,p in x.items()}
                self.expressions[j]=self.slp.combine(e,fmpq_poly([scale]))
                self.updates+=1
                changed=True
                break
            b,f=self.rows[j],self.expressions[j]
            a,p=x[j],b[j]
            q,r=divmod(a,p)
            if not r:
                axpy(x,b,-q);e=self.slp.combine(e,ONE,f,-q)
                continue
            g,ss,tt=p.xgcd(a)
            assert ss*p+tt*a==g
            pp,pr=divmod(p,g);aa,ar=divmod(a,g)
            assert not pr and not ar
            new=combination(b,ss,x,tt)
            newexpr=self.slp.combine(f,ss,e,tt)
            side=combination(x,pp,b,-aa)
            sideexpr=self.slp.combine(e,pp,f,-aa)
            assert new[j]==g and j not in side and g.leading_coefficient()==1
            self.rows[j],self.expressions[j]=new,newexpr
            self.updates+=1
            changed=True
            x,e=side,sideexpr
        if changed:self.reduce_above()
        return changed


def sp(p):
    return {str(i):str(c) for i,c in enumerate(p.coeffs()) if c}


def sv(v):
    return {str(j):sp(p) for j,p in sorted(v.items())}


def main():
    started=time.time()
    one={source.index[source.h.e,source.h.e]:ONE}
    M=Module();M.add(one,M.slp.word(0))
    words=[()];vectors=[one];head=0
    while head<len(words):
        for si in range(3):
            x=step(vectors[head],si)
            if M.contains(x):continue
            idx=len(words)
            words.append(words[head]+(si+1,));vectors.append(x)
            assert M.add(x,M.slp.word(idx))
            if len(words)%10==0:
                print(json.dumps({"accepted":len(words),"rank":len(M.rows),
                                  "pivot_updates":M.updates,"max_length":max(map(len,words)),
                                  "maximum_row_degree":max(p.degree() for b in M.rows.values() for p in b.values()),
                                  "seconds":time.time()-started}),flush=True)
            if len(words)>=1000:raise RuntimeError("bounded exploratory stop at 1000 accepted words")
        head+=1
    assert len(M.rows)==114
    pivots=sorted(M.rows)
    nodes,finals=M.slp.compact([M.expressions[j] for j in pivots])
    uses=Counter(finals)
    for node in nodes:
        if node[0]=="combine":
            uses[node[1]]+=1
            if node[3] is not None:uses[node[3]]+=1
    cache={}
    for i,node in enumerate(nodes):
        if node[0]=="word":cache[i]=vectors[node[1]]
        else:
            _,a,p,b,q=node
            cache[i]=combination(cache[a],p,{} if b is None else cache[b],q)
            for k in [a,b]:
                if k is None:continue
                uses[k]-=1
                if not uses[k]:del cache[k]
    for j,idx in zip(pivots,finals):
        b=M.rows[j]
        assert cache[idx]==b
        assert min(b)==j and b[j].leading_coefficient()==1
    for x in vectors:
        assert M.contains(x)
        for si in range(3):assert M.contains(step(x,si))
    rows=[{"pivot":j,"vector":sv(M.rows[j]),"slp_node":idx}
          for j,idx in zip(pivots,finals)]
    serialized_nodes=[]
    for node in nodes:
        if node[0]=="word":serialized_nodes.append({"word":node[1]})
        else:
            _,a,p,b,q=node
            serialized_nodes.append({"a":a,"p":sp(p),"b":b,"q":sp(q)})
    record={"status":"PASS","rank":114,"ambient_rank":300,
            "accepted_words":[list(w) for w in words],"accepted_count":len(words),
            "maximum_word_length":max(map(len,words)),"pivot_updates":M.updates,
            "pivot_degree_counts":dict(Counter(M.rows[j][j].degree() for j in M.rows)),
            "maximum_row_degree":max(p.degree() for b in M.rows.values() for p in b.values()),
            "straight_line_nodes":len(nodes),
            "seconds":time.time()-started,
            "scope":"actual Q[D] word order, not integral Z[v±] order or saturation"}
    (HERE/"polynomial_order_rank4_verified.json").write_text(json.dumps(record,indent=2)+"\n")
    with gzip.open(HERE/"polynomial_order_rank4_rows.json.gz","wt") as f:
        json.dump({"coordinates":[[a,b] for a,b in source.keys],"rows":rows,
                   "straight_line_program":serialized_nodes},f)
    print(json.dumps({k:v for k,v in record.items() if k!="accepted_words"},indent=2),flush=True)


if __name__=="__main__":main()
