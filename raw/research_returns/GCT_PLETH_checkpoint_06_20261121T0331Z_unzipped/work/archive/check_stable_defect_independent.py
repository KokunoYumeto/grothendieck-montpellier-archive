"""Independent T047 stabilizer matrices, directional jets and literal polytopes."""
from pathlib import Path
from itertools import permutations,product
from functools import lru_cache
from math import comb
import sys,json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import character
sys.path.insert(0,str(HERE.parent/"theta"/"outer5"))
import stable_defect_correction as target

LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))

def cycle_type(perm):
    unseen=set(range(len(perm)));parts=[]
    while unseen:
        x=min(unseen);length=0
        while x in unseen:
            unseen.remove(x);length+=1;x=perm[x]
        parts.append(length)
    return tuple(sorted(parts,reverse=True))

def standard_matrix(perm):
    # Columns in the literal basis e_0-e_2,e_1-e_2.
    columns=[]
    for i in (0,1):
        vector=[0,0,0]
        vector[perm[i]]+=1
        vector[perm[2]]-=1
        assert sum(vector)==0
        columns.append(vector[:2])
    return tuple(tuple(columns[j][i] for j in (0,1)) for i in (0,1))

def trace_det(matrix):
    return matrix[0][0]+matrix[1][1],matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

@lru_cache(None)
def complete(n,tr,det):
    if n<0:return 0
    if n==0:return 1
    return tr*complete(n-1,tr,det)-det*complete(n-2,tr,det)

def schur2(a,b,tr,det):
    return complete(a,tr,det)*complete(b,tr,det)-complete(a+1,tr,det)*complete(b-1,tr,det)

GROUP=[]
for swapped in (0,1):
    p=((0,1),(1,0))[swapped]
    ptr,pdet=(2,1) if not swapped else (0,-1)
    for w in permutations(range(3)):
        wm=standard_matrix(w);wtr,wdet=trace_det(wm)
        perm=p+tuple(v+2 for v in w)
        GROUP.append((swapped,ptr,pdet,wtr,wdet,cycle_type(w),cycle_type(perm)))
assert len(GROUP)==12

restriction_checks=0
for label in LABELS:
    for sigma in (0,1):
        for rho in ((3,),(2,1),(1,1,1)):
            value=sum(character(label,cyc5)*(-1)**(swapped*sigma)*character(rho,cyc3)
                      for swapped,ptr,pdet,wtr,wdet,cyc3,cyc5 in GROUP)
            assert value%12==0
            assert value//12==int(target.strip(label,rho,bool(sigma)))
            restriction_checks+=1

@lru_cache(None)
def correction_trace(x,b,s,ptr,pdet,wtr,wdet):
    # Literal summands D.2; rank-two Schur characters use JT, not CG.
    answer=0
    for j in range(s-1):
        for u in range(min(x,s-2-j)+1):
            for v in range(min(b,s-2-j-u)+1):
                m=s-j-u-v-2
                answer+=pdet**(u+v+1)*complete(m,ptr,pdet)*complete(j,wtr,wdet)*schur2(b+x-u,b-v,wtr,wdet)
    return answer

coefficient_checks=0
for x,b,s in product(range(7),range(7),range(2,10)):
    for label in LABELS:
        numerator=sum(character(label,cyc5)*correction_trace(x,b,s,ptr,pdet,wtr,wdet)
                      for swapped,ptr,pdet,wtr,wdet,cyc3,cyc5 in GROUP)
        assert numerator%12==0
        expected=numerator//12
        assert expected>=0
        assert target.coefficient(x,b,s,label)==expected,(x,b,s,label)
        coefficient_checks+=1

matrix_checks=0;literal_points=0
for x,b,s in ((0,0,2),(1,0,3),(0,1,3),(2,1,4),(0,0,5),(3,2,3)):
    bounds=(s-2,min(x,s-2),min(b,s-2),min(s-2,x+b),s-2,
            (s-1)//2,(b+s-2)//2,(x+s-2)//2,(x+s-2)//3)
    for label in LABELS:
        found=set()
        for tag in target.tags(label):
            matrix=target.constraints(x,b,s,tag)
            tagkey=(tag["sigma"],tag["tau"],tag["rho"],tag["shift"])
            for point in product(*(range(n+1) for n in bounds)):
                if not all(sum(c*v for c,v in zip(row,point))==rhs
                           for row,rhs in zip(matrix["A_eq"],matrix["b_eq"])):continue
                if not all(sum(c*v for c,v in zip(row,point))<=rhs
                           for row,rhs in zip(matrix["A_ub"],matrix["b_ub"])):continue
                found.add((tagkey,point))
        yielded={((tag["sigma"],tag["tau"],tag["rho"],tag["shift"]),point)
                 for tag,point in target.witnesses(x,b,s,label)}
        assert found==yielded
        assert len(found)==target.coefficient(x,b,s,label)
        matrix_checks+=1;literal_points+=len(found)

def rank_mod(matrix,prime=1000003):
    a=[[v%prime for v in row] for row in matrix];pivot=0
    for col in range(len(a[0])):
        row=next((i for i in range(pivot,len(a)) if a[i][col]),None)
        if row is None:continue
        a[pivot],a[row]=a[row],a[pivot]
        inv=pow(a[pivot][col],-1,prime)
        a[pivot]=[(v*inv)%prime for v in a[pivot]]
        for i in range(pivot+1,len(a)):
            scale=a[i][col]
            if scale:
                a[i]=[(v-scale*w)%prime for v,w in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==len(a):break
    return pivot

jet_checks=[]
for r in range(1,9):
    for degree in (2*r-1,2*r):
        columns=[(i,j,degree-i-j) for i in range(degree+1) for j in range(degree-i+1)]
        matrix=[]
        for point,pivot in (((1,0,0),0),((0,1,0),1),((0,0,1),2),((1,1,1),2)):
            free=[i for i in range(3) if i!=pivot]
            for i in range(r):
                for j in range(r-i):
                    row=[]
                    for mon in columns:
                        e,f=(mon[q] for q in free)
                        value=(comb(e,i)*comb(f,j)*point[free[0]]**(e-i)*point[free[1]]**(f-j)
                               if e>=i and f>=j else 0)
                        row.append(value)
                    matrix.append(row)
        rank=rank_mod(matrix)
        expected=len(matrix) if degree==2*r else len(columns)
        assert rank==expected,(r,degree,rank,expected)
        # A full-size nonzero minor modulo the prime proves the Q rank.
        jet_checks.append(dict(r=r,degree=degree,rows=len(matrix),columns=len(columns),rank=rank))

receipt=dict(statement="T047 independent correction and directional-jet checks",status="PASS",
    restriction_character_checks=restriction_checks,
    correction_coefficient_checks=coefficient_checks,
    literal_matrix_cases=matrix_checks,literal_matrix_points=literal_points,
    tag_counts=[len(target.tags(label)) for label in LABELS],
    directional_jet_rank_checks=jet_checks,
    method="literal 12-element stabilizer matrices, MN restriction characters, 2x2 Jacobi-Trudi, Cartesian matrix enumeration; full minors modulo1000003")
(HERE/"STABLE_DEFECT_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({k:v for k,v in receipt.items() if k!="directional_jet_rank_checks"},indent=2))
