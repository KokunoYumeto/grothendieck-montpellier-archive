#!/usr/bin/env python3
"""Check E2/E3/E6 against the complete finite gluing certificates.

Scope: the five simple bases enumerated by the counts branch, n=3,4,5,6,6.
The program independently reconstructs cubical incidence diamonds, the
rank-two boundary circles of parallel cells, and their Mobius-band fibers.
It does not prove general oriented-matroid axioms or the general surface
theorem. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-19.
"""
from pathlib import Path
from itertools import combinations, product
from math import comb
import json, time

ROOT = Path(__file__).resolve().parents[1]

def canonical(signs):
    first = next(s for s in signs if s)
    return tuple(first*s for s in signs)

def compatible(lower, upper):
    return any(all(a == 0 or a == eps*b for a,b in zip(lower,upper))
               for eps in (1,-1))

def run(name):
    started = time.perf_counter()
    data = json.loads((ROOT/f'audit/counts_{name}_input.json').read_text())
    n = data['n']; pairs = [tuple(p) for p in data['pairs']]
    base = {tuple(row[:3]):row[3] for row in data['base_chirotope']}
    def chi(a,b,c):
        if len({a,b,c}) < 3: return 0
        seq = (a,b,c)
        return (-1)**sum(seq[i] > seq[j] for i in range(3) for j in range(i+1,3))*base[tuple(sorted(seq))]
    positions = [tuple(map(int,line.split())) for line in
                 (ROOT/f'audit/counts_{name}_positions.txt').read_text().splitlines()]
    lookup = {s:i for i,s in enumerate(positions)}
    nu = [s.count(0) for s in positions]
    c = [nu.count(j) for j in range(max(nu)+1)]
    cert = json.loads((ROOT/f'audit/counts_{name}_gluing_certificate.json').read_text())
    covers = set(); diamonds = set()
    for u,s in enumerate(positions):
        zeros = [k for k,a in enumerate(s) if not a]
        all_resolutions = set()
        for choices in product((-1,0,1), repeat=len(zeros)):
            t = list(s)
            for k,a in zip(zeros,choices): t[k]=a
            all_resolutions.add(lookup[canonical(t)])
        assert len(all_resolutions) == 3**len(zeros)
        for k in zeros:
            for eps in (-1,1):
                t=list(s);t[k]=eps;v=lookup[canonical(t)]
                covers.add(tuple(sorted((u,v))))
        for k,l in combinations(zeros,2):
            for eps,eta in product((-1,1), repeat=2):
                t=list(s);t[k]=eps;v=lookup[canonical(t)]
                t=list(s);t[l]=eta;w=lookup[canonical(t)]
                t[k]=eps;x=lookup[canonical(t)]
                assert len({u,v,w,x})==4
                diamonds.add(tuple(sorted((u,v,w,x))))
    # The fixed-vertex Euler identity is checked at every old vertex.
    vertex_euler = [sum((-1)**(nu[u]-1) for u,s in enumerate(positions) if s[k]==0)
                    for k in range(len(pairs))]
    assert set(vertex_euler)=={2}
    observed_ordinary_edges=set(); observed_extra={i:set() for i in range(n)}
    for f,j,g,k,*endmap in cert['edge_pairing']:
        arc=cert['faces'][f][j]
        edge=tuple(sorted((f,g)))
        if arc['kind']=='E': observed_extra[arc['line']].add(edge)
        else: observed_ordinary_edges.add(edge)
    assert observed_ordinary_edges==covers
    band_squares=set(); band_counts=[]
    for i in range(n):
        parallel=tuple(chi(a,b,i) for a,b in pairs)
        near={u for u,s in enumerate(positions) if compatible(parallel,s)}
        assert len(near)==4*(n-1)
        boundary={e for e in covers if set(e)<=near}
        degree={u:sum(u in e for e in boundary) for u in near}
        assert set(degree.values())=={2}
        seen=set();todo=[next(iter(near))]
        while todo:
            u=todo.pop()
            if u in seen:continue
            seen.add(u)
            todo.extend(v for e in boundary if u in e for v in e if v!=u)
        assert seen==near
        antipode={u:lookup[canonical(tuple(-a if i in pair else a
                         for a,pair in zip(positions[u],pairs)))] for u in near}
        assert all(v in near and antipode[v]==u and v!=u for u,v in antipode.items())
        fibers={tuple(sorted((u,v))) for u,v in antipode.items()}
        assert fibers==observed_extra[i] and len(fibers)==2*(n-1)
        squares={tuple(sorted((u,v,antipode[u],antipode[v]))) for u,v in boundary}
        assert len(squares)==2*(n-1) and all(len(set(q))==4 for q in squares)
        assert not (band_squares&squares)
        band_squares |= squares
        band_counts.append(dict(line=i,boundary_vertices=len(near),
                                boundary_edges=len(boundary),fiber_edges=len(fibers),
                                rectangles=len(squares)))
    observed_squares=[tuple(sorted(f for f,j in orbit)) for orbit in cert['vertex_orbits']]
    assert len(observed_squares)==len(set(observed_squares))
    selected=set(observed_squares)-band_squares
    assert band_squares<=set(observed_squares) and selected<=diamonds
    assert not (band_squares&diamonds)
    # Each selected ordinary square has its unique gen-gen corner at max nu.
    for orbit in cert['vertex_orbits']:
        labels=tuple(sorted(f for f,j in orbit))
        if labels not in selected:continue
        high=max(nu[f] for f,j in orbit)
        top=[(f,j) for f,j in orbit if nu[f]==high]
        assert len(top)==1
        f,j=top[0];arcs=cert['faces'][f]
        assert arcs[j]['kind']=='G' and arcs[(j+1)%len(arcs)]['kind']=='G'
    small_cells=[2**k*sum(comb(j,k)*c[j] for j in range(k,len(c)))
                 for k in range(len(c))]
    b=n*(n-1)
    b_cells=small_cells+[0]*max(0,3-len(small_cells))
    b_cells[1]+=2*b;b_cells[2]+=2*b
    assert sum((-1)**k*z for k,z in enumerate(b_cells))==1-n
    missing=len(diamonds-selected)
    assert missing==small_cells[2]-len(selected) if len(small_cells)>2 else missing==0
    if max(nu)<3: assert missing==0
    result=dict(case=name,n=n,ordinary_counts=c,principal_cube_intervals_checked=len(positions),
                fixed_vertex_euler_values=vertex_euler,all_one_skeleton_edges=len(covers)+sum(map(len,observed_extra.values())),
                ordinary_diamonds=len(diamonds),selected_diamonds=len(selected),
                missing_diamonds=missing,band_rectangles=len(band_squares),
                blowup_cell_counts=b_cells,relative_cells_dimension_two_and_higher=[missing,*small_cells[3:]],
                bands=band_counts,runtime_s=time.perf_counter()-started)
    if name=='n6_three_pair':
        # Exact added dual point p=(0,0,1); det(a,b,p)=a_x*b_y-a_y*b_x.
        vecs=data['base_vectors']
        dets=[vecs[a][0]*vecs[b][1]-vecs[a][1]*vecs[b][0] for a,b in pairs]
        signs=canonical(tuple((a>0)-(a<0) for a in dets))
        assert signs.count(0)==3 and signs in lookup
        zeros=[k for k,s in enumerate(signs) if s==0]
        stable=[]
        for eps in product((-1,1), repeat=3):
            t=list(signs)
            for k,e in zip(zeros,eps):t[k]=e
            t=canonical(t);assert t in lookup and 0 not in t
            stable.append(dict(resolutions=eps,position_id=lookup[t],localization=t))
        assert len({x['position_id'] for x in stable})==8
        result['L2_counterexample']=dict(added_dual_vector=[0,0,1],
            localization=signs,position_id=lookup[signs],zero_pairs=[pairs[k] for k in zeros],
            stable_generizations=stable)
    return result

if __name__=='__main__':
    started=time.perf_counter()
    results=[run(name) for name in ('n3','n4','n5','n6_convex','n6_three_pair')]
    output=dict(scope='finite certificates only; independent cellular-comparison checks',
                results=results,total_runtime_s=time.perf_counter()-started)
    (ROOT/'audit/extension_compare_cells_output.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
