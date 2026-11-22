"""Certificate-only verification of the actual rank-four sign fibre (N020).

No sign-fibre constructor is imported.  Inputs are the certified actual
Hermite order, N019's full table, its faithful generic GT models, and the
two stored finite certificates.  Inherited KL arithmetic is used only to
evaluate the ambient symmetrizing functional.  All ranks are over Q.
"""
from pathlib import Path
import gzip,json,sys,time
import sympy as sp
from flint import fmpq,fmpq_poly,fmpq_mat

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'dependencies'))
import e4lib as hecke
D=sp.Symbol('D');ZERO=fmpq_poly([])


def read(name):
    with gzip.open(HERE/name,'rt') as f:return json.load(f)


def polynomial(p):
    return fmpq_poly([fmpq(p.get(str(i),'0')) for i in range(max(map(int,p),default=-1)+1)])


def rational_vector(v):return {int(k):fmpq(c) for k,c in v.items()}


def length(w):return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))


def main():
    started=time.time()
    order=read('polynomial_order_gt_hermite.json.gz')
    original=read('gt_hermite_multiplication_table.json.gz')
    abstract=read('sign_fibre_abstract_certificate.json.gz')
    quotient=read('sign_fibre_quotient_certificate.json.gz')
    models=json.loads((HERE/'rational_gt_rank4_verified.json').read_text())['GT_data']
    table=[[rational_vector(v) for v in row] for row in abstract['specialized_products']]
    assert len(table)==114 and all(len(row)==114 for row in table)
    for i in range(114):
        for j in range(114):
            expected={int(k):fmpq(p['0']) for k,p in original['multiplication'][i][j].items() if p.get('0','0')!='0'}
            assert table[i][j]==expected
        assert table[0][i]==table[i][0]=={i:fmpq(1)}

    def product(x,y):
        z={}
        for i,a in x.items():
            for j,b in y.items():
                for k,c in table[i][j].items():z[k]=z.get(k,fmpq(0))+a*b*c
        return {k:c for k,c in z.items() if c}

    def linear(x,y,scale=fmpq(1)):
        z=dict(x)
        for k,c in y.items():z[k]=z.get(k,fmpq(0))+scale*c
        return {k:c for k,c in z.items() if c}

    def dense(x):return [x.get(k,fmpq(0)) for k in range(114)]

    # Check generator coordinates before specialization in the faithful
    # generic GT model, by an equality rather than triangular division.
    raw=[{int(k):polynomial(p) for k,p in row['gt_numerators'].items()} for row in order['rows']]
    denominators=[polynomial(p) for p in order['coordinate_denominators']]
    generators=[rational_vector(v) for v in quotient['generators']]
    for si,co in enumerate(quotient['generator_polynomials']):
        poly={int(k):polynomial(p) for k,p in co.items()}
        assert generators[si]=={k:p[0] for k,p in poly.items() if p[0]}
        for z,label in enumerate(order['coordinate_labels']):
            lhs=sum((p*raw[k].get(z,ZERO) for k,p in poly.items()),ZERO)
            text=models[label['module']]['generator_matrices'][si][label['matrix_row']][label['matrix_column']]
            value=sp.cancel(sp.sympify(text,locals={'D':D})*sum(sp.Rational(str(denominators[z][i]))*D**i for i in range(denominators[z].degree()+1)))
            value=sp.Poly(value,D)
            rhs=fmpq_poly([fmpq(str(value.nth(i))) for i in range(value.degree()+1)]) if value else ZERO
            assert lhs==rhs

    def word(w):
        x={0:fmpq(1)}
        for si in w:x=product(x,generators[si-1])
        return x

    # Independent trace evaluation: at v=i the T_identity coefficient
    # of C_w equals that of C'_w.  The parity of every contributing
    # exponent proves this from the opposite-KL transformation.
    roots=[(1,0),(0,1),(-1,0),(0,-1)]
    traces={}
    for w in hecke.G:
        re=im=0
        for exponent,c in hecke.Cp[w].get(hecke.e,{}).items():
            assert (exponent-length(w))%2==0
            x,y=roots[exponent%4];re+=c*x;im+=c*y
        traces[w]=(re,im)
    coordinates=[(tuple(a),tuple(b)) for a,b in order['ambient_coordinates']]
    ambient=[];trace_weights=[]
    for a,b in coordinates:
        x,y=traces[a];z,t=traces[b]
        trace_weights.append((1 if a==b else 2)*(x*z-y*t))
    for row in order['rows']:
        ambient.append([fmpq(row['ambient_coordinates'].get(str(z),{}).get('0','0'))
                        if (length(a)+length(b))%2==0 else fmpq(0)
                        for z,(a,b) in enumerate(coordinates)])
    assert ambient==[[fmpq(c) for c in row] for row in abstract['ambient_image']]
    assert fmpq_mat(ambient).rank()==55
    tau=[sum((c*t for c,t in zip(row,trace_weights)),fmpq(0)) for row in ambient]
    reg=[sum((table[i][j].get(j,fmpq(0)) for j in range(114)),fmpq(0)) for i in range(114)]
    assert tau==[fmpq(c) for c in abstract['canonical_trace']]
    assert reg==[fmpq(c) for c in abstract['regular_trace']]
    assert tau[0]==1 and reg[0]==114
    def trace(x,functional=tau):return sum((c*functional[k] for k,c in x.items()),fmpq(0))
    Grams=[]
    for functional,name,rank in [(tau,'canonical_Gram',42),(reg,'regular_Gram',5)]:
        gram=[[trace(table[i][j],functional) for j in range(114)] for i in range(114)]
        assert gram==[[fmpq(c) for c in row] for row in abstract[name]]
        assert gram==list(map(list,zip(*gram))) and fmpq_mat(gram).rank()==rank
        Grams.append(gram)

    # The stored quotient is verified on every product, and its values
    # on all actual generators determine the desired homomorphism.
    images=[[fmpq(c) for c in row] for row in quotient['projection']]
    def image(x):return [sum((c*images[k][j] for k,c in x.items()),fmpq(0)) for j in range(5)]
    def matrix_product(x,y):
        value=[x[0]*y[0]]
        value += [sum((x[1+2*i+k]*y[1+2*k+j] for k in range(2)),fmpq(0)) for i in range(2) for j in range(2)]
        return value
    assert images[0]==[1,1,0,0,1]
    assert [image(g) for g in generators]==[[0,0,1,0,0],[0,0,0,4,0],[0,0,1,0,0]]
    for i in range(114):
        for j in range(114):assert image(table[i][j])==matrix_product(images[i],images[j])
    assert fmpq_mat(images).rank()==5
    assert fmpq_mat([a+b for a,b in zip(ambient,images)]).rank()==55
    assert all(t==78*p[0]+18*(p[1]+p[4]) for t,p in zip(reg,images))

    expected_words=[[],[1],[2],[1,2],[2,1],[1,2,1],[2,1,2],[1,2,1,2],[2,1,2,1],[1,2,1,2,1]]
    # All-degree rank-three spanning relations, checked in every block
    # of the already faithful generic rank-four representation.
    u=D+(D-2)**2;w=D*(D-2)**2
    for model in models.values():
        aa,bb=[sp.Matrix([[sp.sympify(v,locals={'D':D}) for v in row] for row in model['generator_matrices'][i]]) for i in range(2)]
        for a,b in [(aa,bb),(bb,aa)]:
            ab=a*b;aba=ab*a;ababa=aba*b*a;bab=b*a*b
            assert all(sp.cancel(x)==0 for x in ababa-b*a*b*a*b-u*(aba-bab)+w*(a-b))
            assert all(sp.cancel(x)==0 for x in ab**3-D*ababa-u*ab**2+D*u*aba+w*ab-D*w*a)
    assert quotient['parabolic_basis_words']==expected_words
    parab=[word(w) for w in expected_words];parab_rows=[dense(x) for x in parab]
    assert fmpq_mat(parab_rows).rank()==10
    for x in parab:
        for g in generators[:2]:assert fmpq_mat(parab_rows+[dense(product(x,g))]).rank()==10
    def ambient_image(x):return [sum((c*ambient[k][j] for k,c in x.items()),fmpq(0)) for j in range(300)]
    assert fmpq_mat([ambient_image(x) for x in parab]).rank()==7
    assert fmpq_mat([[trace(product(x,y)) for y in parab] for x in parab]).rank()==6

    gamma=[word(w) for w in [(1,2,1),(1,2,1,2),(2,1,2,1),(2,1,2)]]
    sigma=linear(word((1,2,1,2,1)),gamma[0],fmpq(-4))
    assert sigma==rational_vector(quotient['Sigma']) and sigma
    assert sigma==linear(word((2,1,2,1,2)),gamma[3],fmpq(-4))
    assert not product(sigma,sigma) and not any(ambient_image(sigma))
    assert all(not product(x,sigma) and not product(sigma,x) for x in gamma)
    corrected=[linear(gamma[0],sigma,fmpq(1,4)),gamma[1],gamma[2],linear(gamma[3],sigma,fmpq(1,4))]
    assert corrected==[rational_vector(v) for v in quotient['corrected_cell_vectors']]
    assert fmpq_mat([dense(x) for x in corrected]).rank()==4
    expected_images=[[0,0,4,0,0],[0,16,0,0,0],[0,0,0,0,16],[0,0,0,16,0]]
    assert [image(x) for x in corrected]==expected_images
    cell=[[rational_vector(v) for v in row] for row in quotient['corrected_cell_table']]
    for i in range(4):
        for j in range(4):
            rhs={}
            for k,c in cell[i][j].items():rhs=linear(rhs,corrected[k],c)
            assert product(corrected[i],corrected[j])==rhs
    e={k:c/16 for k,c in linear(corrected[1],corrected[2]).items()}
    f=linear({0:fmpq(1)},e,fmpq(-1))
    assert e==rational_vector(quotient['corrected_cell_local_unit'])
    assert product(e,e)==e and product(f,f)==f
    assert all(product(e,x)==x==product(x,e) and not product(f,x) and not product(x,f) for x in corrected)
    assert image(e)==[0,1,0,0,1] and image(f)==[1,0,0,0,0]
    assert trace(e)==2 and trace(f)==-1
    expected_gram=[[0,0,0,64],[0,256,0,0],[0,0,256,0],[64,0,0,0]]
    assert [[trace(product(x,y)) for y in corrected] for x in corrected]==expected_gram
    pi=[3,1,2,0];weights=[64,256,256,64];swap=[3,2,1,0];transpose=[0,2,1,3]
    triples=[(i,j,k) for i in range(4) for j in range(4) for k in range(4)]
    def weighted(t):
        i,j,k=t;return cell[i][j].get(k,fmpq(0))*weights[k]
    def rotation(t):i,j,k=t;return j,pi[k],pi[i]
    def dynkin(t):return tuple(swap[i] for i in t)
    def reflection(t):i,j,k=t;return transpose[j],transpose[i],transpose[k]
    for t in triples:
        assert weighted(t)==weighted(rotation(t))==weighted(dynkin(t))==weighted(reflection(t))
        assert rotation(rotation(rotation(t)))==t
        assert dynkin(rotation(t))==rotation(dynkin(t))
        assert reflection(rotation(reflection(t)))==rotation(rotation(t))
    def group_order(actions):
        identity=tuple(triples);seen={identity};todo=[identity]
        for p in todo:
            for action in actions:
                new=tuple(action(t) for t in p)
                if new not in seen:seen.add(new);todo.append(new)
        return len(seen)
    assert [group_order([rotation]),group_order([rotation,dynkin]),group_order([rotation,reflection])]==[3,6,6]
    # The full-label obstruction uses this exact fixed-pairing idempotent.
    assert product(corrected[1],corrected[1])=={k:16*c for k,c in corrected[1].items()}
    assert product({0:fmpq(1)},corrected[1])==corrected[1]

    result={'status':'PASS_EXACT_CERTIFICATE','scope':'Certificate-only path by branch author; independent agent proof/code review tracked separately.',
            'abstract_dimension':114,'ambient_image_dimension':55,'ambient_kernel_dimension':59,
            'ambient_Gram_rank':42,'regular_Gram_rank':5,'quotient_dimension':5,
            'regular_character':[78,18],'parabolic_abstract_dimension':10,'parabolic_ambient_dimension':7,
            'parabolic_ambient_Gram_rank':6,'Sigma_nonzero_abstract_zero_ambient':True,
            'quotient_product_identities':12996,'cell_products':16,'weighted_triples':64,
            'slot_group_orders':[3,6,6],'seconds':time.time()-started}
    (HERE/'sign_fibre_independent_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
