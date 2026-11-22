"""Split semisimple quotient and inherited sign-cell data in the actual D=0 fibre.

The two-dimensional polynomial representation is obtained from the
verified Sprime22 GT block by Q=[[1,1],[0,-D]].  Its generators are
[[D,1],[0,0]], [[0,0],[(D-2)^2,D]], and the first matrix again.
The script checks actual integral-in-D extension, the full specialized
algebra homomorphism, the ambient-kernel containment, and the parabolic
rank-three cell elements in the abstract fibre.
"""
from pathlib import Path
import gzip,json,time
import sympy as s
from flint import fmpq,fmpq_poly,fmpq_mat

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=fmpq_poly([0,1]);Ds=s.Symbol('D')


def parse(p):return fmpq_poly([fmpq(p.get(str(i),'0')) for i in range(max(map(int,p),default=-1)+1)])
def vector(v):return {int(j):parse(p) for j,p in v.items()}
def exact(p,q):
    a,r=divmod(p,q);assert not r
    return a
def fp(expr):
    p=s.Poly(expr,Ds)
    return fmpq_poly([fmpq(str(p.nth(i))) for i in range(p.degree()+1)]) if p else ZERO


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    with gzip.open(HERE/'sign_fibre_abstract_certificate.json.gz','rt') as f:cert=json.load(f)
    models=json.loads((HERE/'rational_gt_rank4_verified.json').read_text())['GT_data']
    table=[[{int(k):fmpq(c) for k,c in row.items()} for row in block] for block in cert['specialized_products']]
    raw=[vector(row['gt_numerators']) for row in data['rows']]
    den=[parse(p) for p in data['coordinate_denominators']]
    labels=data['coordinate_labels'];Delta=ONE
    for p in den:Delta=exact(Delta*p,Delta.gcd(p))
    Delta/=Delta.leading_coefficient()
    rows=[{j:p*exact(Delta,den[j]) for j,p in row.items()} for row in raw]
    def divide(row):
        row=dict(row);out={}
        while row:
            j=min(row);q=exact(row[j],rows[j][j]);out[j]=q
            for k,p in rows[j].items():
                x=row.get(k,ZERO)-q*p
                if x:row[k]=x
                else:row.pop(k,None)
        return out
    generators=[];generator_polynomials=[]
    for si in range(3):
        image={}
        for z,label in enumerate(labels):
            text=models[label['module']]['generator_matrices'][si][label['matrix_row']][label['matrix_column']]
            p,q=s.fraction(s.cancel(s.sympify(text,locals={'D':Ds})))
            value=exact(fp(p)*Delta,fp(q))
            if value:image[z]=value
        co=divide(image);generator_polynomials.append(co)
        generators.append({k:p[0] for k,p in co.items() if p[0]})
    def multiply(x,y):
        z={}
        for i,a in x.items():
            for j,b in y.items():
                for k,c in table[i][j].items():
                    q=z.get(k,fmpq(0))+a*b*c
                    if q:z[k]=q
                    else:z.pop(k,None)
        return z
    def word(w):
        y={0:fmpq(1)}
        for i in w:y=multiply(y,generators[i-1])
        return y
    # Explicit polynomial descent of the Sprime22 representation.
    ids={(label['matrix_row'],label['matrix_column']):z for z,label in enumerate(labels) if label['module']=='Sprime22'}
    assert all(den[z]==D for z in ids.values())
    character=next(z for z,label in enumerate(labels) if label['module']=='eps-')
    projection=[]
    for row in raw:
        a,b,c,d=[row.get(ids[i,j],ZERO) for i,j in [(0,0),(0,1),(1,0),(1,1)]]
        # Q G Q^-1, where G has common denominator D.
        matrix=[exact(a+c,D),exact(a-b+c-d,D**2),-c,exact(d-c,D)]
        chi=exact(row.get(character,ZERO),den[character])
        projection.append([chi[0]]+[p[0] for p in matrix])
    def projected(x):return [sum((c*projection[k][i] for k,c in x.items()),fmpq(0)) for i in range(5)]
    def product5(x,y):
        a,b,c,d=x[1:];e,f,g,h=y[1:]
        return [x[0]*y[0],a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h]
    assert projection[0]==[1,1,0,0,1]
    assert [projected(g) for g in generators]==[[0,0,1,0,0],[0,0,0,4,0],[0,0,1,0,0]]
    for i in range(114):
        for j in range(114):assert projected(table[i][j])==product5(projection[i],projection[j])
    assert fmpq_mat(projection).rank()==5
    ambient=[[fmpq(c) for c in row] for row in cert['ambient_image']]
    assert fmpq_mat([x+y for x,y in zip(ambient,projection)]).rank()==55
    regular=[fmpq(c) for c in cert['regular_trace']]
    assert all(t==78*p[0]+18*(p[1]+p[4]) for t,p in zip(regular,projection))
    # The whole parabolic image, generated inside the abstract rank-four fibre.
    basis=[];accepted=[];mat=[]
    def accept(x,w):
        row=[x.get(k,fmpq(0)) for k in range(114)]
        if fmpq_mat(mat+[row]).rank()>len(mat):
            mat.append(row);basis.append(x);accepted.append(w);return True
        return False
    accept({0:fmpq(1)},[]);head=0
    while head<len(basis):
        for i in range(2):accept(multiply(basis[head],generators[i]),accepted[head]+[i+1])
        head+=1
    cell=[word(w) for w in [(1,2,1),(1,2,1,2),(2,1,2,1),(2,1,2)]]
    sigma=word((1,2,1,2,1))
    for k,c in word((1,2,1)).items():
        v=sigma.get(k,fmpq(0))-4*c
        if v:sigma[k]=v
        else:sigma.pop(k,None)
    cell_rank=fmpq_mat([[x.get(k,fmpq(0)) for k in range(114)] for x in cell]).rank()
    canonical=[fmpq(c) for c in cert['canonical_trace']]
    tau=lambda x:sum((c*canonical[k] for k,c in x.items()),fmpq(0))
    gram=[[tau(multiply(x,y)) for y in cell] for x in cell]
    expected=[[0,0,0,64],[0,256,0,0],[0,0,256,0],[64,0,0,0]]
    assert gram==expected and cell_rank==4
    e=cell[1];assert multiply(e,e)=={k:16*c for k,c in e.items()}
    # The uncorrected four-vector span is not a subalgebra: some
    # products have a nonzero Sigma component.  The following correction
    # produces an actual matrix subalgebra in the abstract fibre.
    assert sigma and not multiply(sigma,sigma)
    assert all(not multiply(sigma,x) and not multiply(x,sigma) for x in cell)
    def add(x,y,factor=fmpq(1)):
        z=dict(x)
        for k,c in y.items():
            v=z.get(k,fmpq(0))+factor*c
            if v:z[k]=v
            else:z.pop(k,None)
        return z
    corrected=[add(cell[0],sigma,fmpq(1,4)),cell[1],cell[2],add(cell[3],sigma,fmpq(1,4))]
    expected_projection=[[0,0,4,0,0],[0,16,0,0,0],[0,0,0,0,16],[0,0,0,16,0]]
    assert [projected(x) for x in corrected]==expected_projection
    # h1=4E12, h12=16E11, h21=16E22, h2=16E21.
    units=[(0,1),(0,0),(1,1),(1,0)];scales=[4,16,16,16]
    local_table=[]
    for i,x in enumerate(corrected):
        line=[]
        for j,y in enumerate(corrected):
            if units[i][1]!=units[j][0]:co={};actual={}
            else:
                k=units.index((units[i][0],units[j][1]))
                value=fmpq(scales[i]*scales[j],scales[k])
                co={k:value};actual={z:value*c for z,c in corrected[k].items()}
            assert multiply(x,y)==actual
            line.append(co)
        local_table.append(line)
    local_unit={k:c/16 for k,c in add(corrected[1],corrected[2]).items()}
    assert multiply(local_unit,local_unit)==local_unit
    assert all(multiply(local_unit,x)==x==multiply(x,local_unit) for x in corrected)
    scalar_unit=add({0:fmpq(1)},local_unit,fmpq(-1))
    assert multiply(scalar_unit,scalar_unit)==scalar_unit
    assert all(not multiply(scalar_unit,x) and not multiply(x,scalar_unit) for x in corrected)
    assert projected(scalar_unit)==[1,0,0,0,0]
    assert projected(local_unit)==[0,1,0,0,1]
    parabolic_image=[[sum((c*ambient[k][z] for k,c in x.items()),fmpq(0)) for z in range(300)] for x in basis]
    parabolic_gram=[[tau(multiply(x,y)) for y in basis] for x in basis]
    assert fmpq_mat(parabolic_image).rank()==7
    assert fmpq_mat(parabolic_gram).rank()==6
    assert [[tau(multiply(x,y)) for y in corrected] for x in corrected]==expected
    pi=[3,1,2,0];dynkin=[3,2,1,0];transpose=[0,2,1,3];weights=[64,256,256,64]
    def coefficient(i,j,k):return local_table[i][j].get(k,fmpq(0))*weights[k]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                value=coefficient(i,j,k)
                assert value==coefficient(j,pi[k],pi[i])
                assert value==coefficient(dynkin[i],dynkin[j],dynkin[k])
                assert value==coefficient(transpose[j],transpose[i],transpose[k])
    triples=[(i,j,k) for i in range(4) for j in range(4) for k in range(4)]
    permutation=lambda action:tuple(triples.index(action(*t)) for t in triples)
    rotation=permutation(lambda i,j,k:(j,pi[k],pi[i]))
    swap=permutation(lambda i,j,k:(dynkin[i],dynkin[j],dynkin[k]))
    reflection=permutation(lambda i,j,k:(transpose[j],transpose[i],transpose[k]))
    def group_size(gens):
        identity=tuple(range(64));seen={identity};todo=[identity]
        for p in todo:
            for g in gens:
                new=tuple(p[g[k]] for k in range(64))
                if new not in seen:seen.add(new);todo.append(new)
        return len(seen)
    assert group_size([rotation])==3
    assert group_size([rotation,swap])==6
    assert group_size([rotation,reflection])==6
    result={'status':'COMPUTED_PENDING_PROOF_REVIEW','scope':'Actual rational-order sign fibre and its parabolic cell; not an E(4) label table.',
            'quotient':'Q direct_sum Mat2(Q)','quotient_dimension':5,
            'regular_character_multiplicities':{'zero_character':78,'two_dimensional_simple':18},
            'all_specialized_product_homomorphisms_checked':12996,
            'ambient_kernel_is_in_quotient_kernel':True,
            'parabolic_generated_dimension':len(basis),
            'inert_four_vector_rank':cell_rank,'Sigma_specialization_zero_in_abstract_rank4':not sigma,
            'inert_cell_Gram':expected,'inert_idempotent_relation':'gamma12^2=16 gamma12',
            'corrected_cell':'h1=gamma1+Sigma/4; h12=gamma12; h21=gamma21; h2=gamma2+Sigma/4',
            'corrected_cell_is_actual_Mat2_subalgebra':True,
            'explicit_semisimple_complement':'Q(1-e) direct_sum corrected_cell, e=(gamma12+gamma21)/16',
            'canonical_trace_of_Sigma':str(tau(sigma)),
            'canonical_trace_on_complement':{'scalar_character':str(tau(scalar_unit)),'matrix_trace_multiplier':'1'},
            'parabolic_ambient_image_dimension':7,'parabolic_ambient_trace_rank':6,
            'corrected_cell_all_products_checked':16,
            'corrected_cell_weighted_symmetry_checks':64,
            'slot_group_orders':{'rotation_C3':3,'with_parabolic_Dynkin_C6':6,'with_word_reversal_D3':6},
            'seconds':time.time()-started}
    (HERE/'sign_fibre_quotient_verified.json').write_text(json.dumps(result,indent=2)+'\n')
    extra={'projection':[[str(x) for x in row] for row in projection],
           'generators':[{str(k):str(c) for k,c in g.items()} for g in generators],
           'generator_polynomials':[{str(k):{str(i):str(p[i]) for i in range(p.degree()+1) if p[i]} for k,p in g.items()} for g in generator_polynomials],
           'parabolic_basis_words':accepted,
           'inert_cell_vectors':[{str(k):str(c) for k,c in x.items()} for x in cell],
           'Sigma':{str(k):str(c) for k,c in sigma.items()},
           'corrected_cell_vectors':[{str(k):str(c) for k,c in x.items()} for x in corrected],
           'corrected_cell_table':[[{str(k):str(c) for k,c in co.items()} for co in row] for row in local_table],
           'corrected_cell_local_unit':{str(k):str(c) for k,c in local_unit.items()},
           'pairing_permutation':pi,'pairing_weights':weights,'parabolic_Dynkin':dynkin,'word_reversal':transpose}
    with gzip.open(HERE/'sign_fibre_quotient_certificate.json.gz','wt') as f:json.dump(extra,f)
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
