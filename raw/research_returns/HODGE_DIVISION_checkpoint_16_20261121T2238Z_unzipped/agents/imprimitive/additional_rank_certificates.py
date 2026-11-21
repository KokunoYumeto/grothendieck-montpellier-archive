#!/usr/bin/env python3
"""Exact minor certificates for two auxiliary cyclic Prym calculations.

Outputs (a) genus4, unramified, gluing exponents0,1,1,1;
        (b) genus5, branch exponents e,d-e at0,infinity, e|d and e<d.
The accompanying proof file must be consulted for the geometric meaning.
"""
import json
import nodal_rank as nr

P=nr.P

def cert_from_columns(columns, row_count):
    rows=[[c[k] if k<len(c) else 0 for c in columns] for k in range(row_count)]
    rank,cids=nr.rank_pivots(rows)
    selected=[[row[j] for j in cids] for row in rows]
    _,rids=nr.rank_pivots(list(map(list,zip(*selected))))
    minor=[[rows[i][j] for j in cids] for i in rids]
    det=nr.determinant(minor)
    assert det!=0
    return {"rank_mod_prime":rank,"column_ids_zero_based":cids,
            "row_ids_zero_based":rids,"minor_determinant_mod_prime":det,
            "minor":minor}

def unramified_genus4(d):
    g=4
    z=nr.primitive_root_of_order(d)
    pts=list(range(1,2*g+1))
    par={x:nr.poly_without(pts,x) for x in pts}
    def forms(q):
        a=[nr.add(par[2*j+1],par[2*j+2],-(1 if j==0 else q)) for j in range(g)]
        return [a[0]]+[nr.add(a[j],a[-1],-1) for j in range(1,g-1)]
    f,h=forms(z),forms(pow(z,-1,P))
    result=cert_from_columns([nr.mul(a,b) for a in f for b in h],4*g-3)
    result.update({"d":d,"g":g,"prime":P,"zeta_mod_prime":z,
                   "node_pairs":[[2*j+1,2*j+2] for j in range(g)],
                   "gluing_exponents":[0,1,1,1],"construction":"unramified"})
    assert result["rank_mod_prime"]==9
    return result

def ramified_genus5(d,e):
    g=5
    z=nr.primitive_root_of_order(d)
    pairs_integer=[[(2*j)*(2*j+1)**d,2*j] for j in range(1,g+1)]
    pairs=[(a%P,b%P) for a,b in pairs_integer]
    pts=[x for pair in pairs for x in pair]
    assert len(set(pts))==2*g and 0 not in pts
    par={x:nr.poly_without(pts,x) for x in pts}
    f,h=[],[]
    for j,(a,b) in enumerate(pairs,1):
        q=pow(2*j+1,-e,P)*z%P
        qinv=b*pow(a,-1,P)*pow(q,-1,P)%P
        assert pow(q,d,P)==pow(b*pow(a,-1,P),e,P)
        assert pow(qinv,d,P)==pow(b*pow(a,-1,P),d-e,P)
        f.append(nr.add(par[a],par[b],-q))
        h.append(nr.add(par[a],par[b],-qinv))
    result=cert_from_columns([nr.mul(a,b) for a in f for b in h],4*g-1)
    result.update({"d":d,"e":e,"g":g,"prime":P,"zeta_mod_prime":z,
                   "node_pairs_integer":pairs_integer,"node_pairs_mod_prime":pairs,
                   "construction":"two_branch_points","branch_exponents":[e,d-e],
                   "branch_points":[0,"infinity"],
                   "gluing_formula":"q_j=zeta_d/(2*j+1)^e; qprime_j=(b_j/a_j)/q_j"})
    assert result["rank_mod_prime"]==14
    return result

if __name__=="__main__":
    result=[unramified_genus4(d) for d in [3,4,6]]
    result.extend(ramified_genus5(d,e) for d in [3,4,6] for e in range(1,d) if d%e==0)
    print(json.dumps(result,indent=2))
