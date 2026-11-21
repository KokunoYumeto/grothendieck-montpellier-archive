"""Independent MN, literal matrix, and lazy-witness audit of G026."""
from pathlib import Path
from itertools import combinations,islice
from math import comb
import csv,sys
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_two_row_bundle import schur_two

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'root'))
import first_power_zero_twist_positive as pos


def trace(cyc,x,b):
    answer=schur_two(cyc,b+x,b)
    for mask in range(1,1<<len(cyc)):
        chosen=[i for i in range(len(cyc)) if mask>>i&1]
        if sum(cyc[i] for i in chosen)>3:continue
        rest=tuple(cyc[i] for i in range(len(cyc)) if not(mask>>i&1))
        answer+=(-1)**len(chosen)*schur_two(rest,b+x,b)
    return answer


def expected(mu,x,b,d):
    value=sum((120//z(cyc))*character(mu,cyc)*(-1)**((5-len(cyc))*(d+b+x))*trace(cyc,x,b) for cyc in partitions(5))
    assert value%120==0 and value>=0
    return value//120


def feasible(poly,point):
    return (len(point)==len(poly['variables']) and
            all(sum(a*v for a,v in zip(row,point))==rhs for row,rhs in poly['equalities']) and
            all(sum(a*v for a,v in zip(row,point))<=rhs for row,rhs in poly['inequalities']))


def matrix_checks():
    notes=[];accepted=rejected=full=0
    for x,b,d,label in [(0,3,0,'5'),(1,3,0,'311'),(5,0,1,'5'),(7,0,0,'41'),(3,1,0,'5'),(2,2,1,'32'),(247,314,2,'311')]:
        polys=pos.polytopes(x,b,d,label)
        lookup={(tuple(p['residues']),tuple(p['order'])):p for p in polys}
        count=pos.coefficient(x,b,d,label)
        _,_,parameters,_=pos.validate(x,b,d,label)
        qq=tuple(v//60 for v in parameters)
        own_count=0
        for p in polys:
            own_count+=p['constant']*__import__('math').prod(comb(q,j) for q,j in zip(qq,p['order']))
            if any(q<j for q,j in zip(qq,p['order'])):continue
            for end in (False,True):
                chain=tuple(t for q,j in zip(qq,p['order']) for t in (range(q-j,q) if end else range(j)))
                point=qq+(p['constant']-1 if end else 0,)+chain
                assert feasible(p,point);accepted+=1
                bad=list(point);bad[len(qq)]=p['constant'];assert not feasible(p,bad);rejected+=1
                bad=list(point);bad[0]+=1;assert not feasible(p,bad);rejected+=1
                offset=len(qq)+1
                for q,j in zip(qq,p['order']):
                    if j:
                        bad=list(point);bad[offset+j-1]=q;assert not feasible(p,bad);rejected+=1
                    offset+=j
        assert count==own_count
        limit=count+1 if count<=200 else 17
        points=list(pos.witnesses(x,b,d,label,limit=limit))
        assert len(points)==min(limit,count)
        assert len({(tuple(p['order']),tuple(p['coordinates'])) for p in points})==len(points)
        for w in points:assert feasible(lookup[(tuple(w['residues']),tuple(w['order']))],w['coordinates']);accepted+=1
        if count<=200:full+=len(points)
        notes.append(f'PASS literal matrices x={x},b={b},d={d},outer={label}; tags={len(polys)}; returned={len(points)}')
    huge=10**250
    for x,b,d,label in [(60*huge,3+60*huge,1,'5'),(5+60*huge,0,1,'5')]:
        polys=pos.polytopes(x,b,d,label);lookup={(tuple(p['residues']),tuple(p['order'])):p for p in polys}
        it=pos.witnesses(x,b,d,label,limit=3)
        assert iter(it) is it
        points=list(it);assert len(points)==3
        assert any(sum(p['order'])>0 for p in points)
        for w in points:assert feasible(lookup[(tuple(w['residues']),tuple(w['order']))],w['coordinates']);accepted+=1
        assert pos.coefficient(x,b,d,label)>0
        notes.append(f'PASS 251-digit quotient lazy iterator; branch={points[0]["branch"]};3 witnesses including a nonempty chain')
    allp=pos.polytopes(7,0,0,'41',all_residues=True)
    for p in allp:
        rhs=p['equalities'][0][1]
        assert (rhs%60==0)==(p['residues']==(2,))
    assert not list(pos.witnesses(7,0,0,'41',limit=0))
    notes.append(f'PASS all-residue boundary export tags={len(allp)}; accepted={accepted}; rejected violations={rejected}; exhaustive small witnesses={full}')
    (HERE/'FIRST_POWER_ZERO_TWIST_MATRIX_WITNESS_CHECK.txt').write_text('\n'.join(notes)+'\n')
    print('\n'.join(notes),flush=True)


def main():
    rows=[]
    for n in range(7):
        for b in range(n+2):
            for x in range(n+2-b):
                d=n+1-b-x
                if 2*b+x<5:continue
                lam=(d+3*b+2*x-5,d+b+x,d+b+x,d+x,d)
                assert sum(lam)==5*n and tuple(sorted(lam,reverse=True))==lam and min(lam)>=0
                for mu in partitions(5):
                    a=actual(mu,n,lam);e=expected(mu,x,b,d);p=pos.coefficient(x,b,d,mu)
                    assert a==e==p,(n,x,b,d,mu,lam,a,e,p)
                    rows.append(dict(n=n,x=x,b=b,d=d,outer=','.join(map(str,mu)),output=','.join(map(str,lam)),actual_MN=a,arrangement_trace=e,positive_evaluator=p,status='PASS'))
        print('completed n',n,'cases',len(rows),flush=True)
    with (HERE/'FIRST_POWER_ZERO_TWIST_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    matrix_checks();print('PASS actual MN',len(rows),flush=True)


if __name__=='__main__':main()
