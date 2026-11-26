#!/usr/bin/env python3
"""Independent finite checks; finite posets here test the relaxed lemma, NOT density."""
from itertools import combinations, product
from pathlib import Path

def bounded_orders(n):
    middle=list(range(1,n-1)); pairs=list(combinations(middle,2))
    for bits in range(1<<len(pairs)):
        r={(i,i) for i in range(n)}|{(0,i) for i in range(n)}|{(i,n-1) for i in range(n)}
        r|={p for k,p in enumerate(pairs) if bits>>k&1}
        if all((i,k) in r for i,j in r for jj,k in r if j==jj): yield r

def check_orders():
    total=anchors=triples=0
    for n in range(2,8):
        count=0
        for r in bounded_orders(n):
            count+=1; total+=1
            N=lambda x,y,z: ((x,y) in r and (y,z) in r) or ((z,y) in r and (y,x) in r)
            B=lambda x,y,z: len({x,y,z})==3 and N(x,y,z)
            for a,b in r:
                if a==b: continue
                anchors+=1
                ds=[x for x in range(n) if x==a or B(x,a,b)]
                us=[y for y in range(n) if y==b or B(a,b,y)]
                for u,v in product(range(n),repeat=2):
                    q=any(N(x,u,y) and N(x,v,y) and N(x,u,v) for x,y in product(ds,us))
                    assert q==((u,v) in r),(n,r,a,b,u,v)
            for x,y,u,v in product(range(n),repeat=4):
                if x==y or (x,y) not in r:continue
                if N(x,u,y) and N(x,v,y) and (N(x,u,v) or N(u,v,y)):
                    triples+=1;assert (x,u) in r and (u,v) in r and (v,y) in r
        print(f'relaxed reconstruction: n={n}, naturally labelled bounded posets={count}, PASS')
    print(f'total posets={total}; oriented anchors={anchors}; satisfied four-point antecedents={triples}')

def check_boolean():
    for n in range(1,9):
        full=(1<<n)-1
        for x,y in product(range(full+1),repeat=2):
            add=(x|y)&(full^(x&y))
            assert add==x^y
            assert x|y == add^(x&y)
            assert ((x&y)==x)==((x|y)==y)
            assert full^(x&y)==(full^x)|(full^y)
        print(f'Boolean ring and De Morgan identities: {n} atoms, PASS')
    # Five real-line cells and one generator [0,1].
    full=31;x=0b01110
    generated={0,full,x,full^x}
    atoms=[a for a in generated if a and not any(0<b<a and (b&a)==b for b in generated)]
    print(f'one generator [0,1]: generated algebra={len(generated)} elements, atoms={sorted(atoms)}; full five-cell algebra=32 elements')
    assert len(atoms)==2

def check_horizontal_sum():
    # 0,1,a,a*,b,b*; two 4-element Boolean blocks.
    elems=range(6); blocks=[{0,1,2,3},{0,1,4,5}]; comp={0:1,1:0,2:3,3:2,4:5,5:4}
    le=lambda x,y: x==0 or y==1 or x==y
    compatible=lambda x,y:any({x,y}<=b for b in blocks)
    def meet(x,y):return x if le(x,y) else y if le(y,x) else 0
    def join(x,y):return y if le(x,y) else x if le(y,x) else 1
    for x,y in product(elems,repeat=2):
        assert not le(x,y) or compatible(x,y)
        assert comp[comp[x]]==x
        assert le(x,y)==le(comp[y],comp[x])
        assert compatible(x,y)==compatible(x,comp[y])
        if compatible(x,y):
            assert comp[meet(x,y)]==join(comp[x],comp[y])
            assert comp[join(x,y)]==meet(comp[x],comp[y])
        zero_candidates=[z for z in elems if compatible(x,z) and meet(x,z)==0]
        assert all(le(z,comp[x]) for z in zero_candidates)
        assert [z for z in zero_candidates if join(x,z)==1]==[comp[x]]
    for bits in range(64):
        family={i for i in elems if bits>>i&1}
        if all(compatible(x,y) for x,y in product(family,repeat=2)):
            assert any(family<=block for block in blocks)
    assert not compatible(2,4)
    print('horizontal sum: axioms 1–7 with identity closure and finite compatible-block condition PASS; all six elements clopen; a,b incompatible')

if __name__=='__main__':
    print('Scope: finite certificates supplement, never replace, the infinite-model proofs.')
    check_orders(); check_boolean(); check_horizontal_sum()
