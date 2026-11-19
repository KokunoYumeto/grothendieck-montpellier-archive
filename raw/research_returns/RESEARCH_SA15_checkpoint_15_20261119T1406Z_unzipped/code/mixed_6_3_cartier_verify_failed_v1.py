"""Independent symbolic construction and polynomial determinant of the (6,3) seed."""
from pathlib import Path
import json, time, traceback
import sympy as sp
from sympy.polys.matrices import DomainMatrix

started=time.perf_counter()
root=Path(__file__).resolve().parents[1]
dest=root/'outputs/mixed_6_3_cartier_verify.json'
assert not dest.exists()
out={'status':'RUNNING','scope':'Exact p-basis identities, full Cartier matrix, two kernel sections and one16minor over GF(2)[c]. Geometry is proved separately.'}
try:
    x,y,t,c=sp.symbols('x y t c')
    ring=sp.GF(2).poly_ring(x,t)
    equation=sp.Poly(y*y+x*y+x**3+t*t,y,domain=ring)
    def curve_zero(expr):
        numerator,denominator=sp.fraction(sp.cancel(expr))
        assert sp.Poly(numerator,y,domain=ring).rem(equation).is_zero
        assert denominator!=0
    basis=[1,x,y,x*x,x*y,x**3]
    A=[1,0,x,x,y+t,0]
    B=[0,1,(y+t)/x,0,x,x]
    for f,a,b in zip(basis,A,B):curve_zero(f-a*a-x*b*b)
    source=json.loads((root/'outputs/mixed_6_3_cartier_search.json').read_text())
    encoded=source['squared_ordinary_pairing']
    pairing=[]
    for i in range(6):
        row=[]
        for j in range(6):
            expected=sum((1 if coefficient==1 else t)*basis[int(k)]
                         for k,coefficient in encoded[i][j].items())
            curve_zero(A[i]*A[j]+x*B[i]*B[j]-expected)
            row.append(str(expected))
        pairing.append(row)
    chosen=next(rec for rec in source['trials'] if rec.get('minor_polynomial_bits')==32)
    coefficients=chosen['coefficients']
    derivative=[0]*18
    # D(1)=0,Dx=x,Dy=x^2+y,Dx^2=0,Dxy=x^3,Dx^3=x^3.
    d_basis=[{}, {1:1}, {2:1,3:1}, {}, {5:1}, {5:1}]
    for i in range(6):
        for j in range(3):
            if coefficients[3*i+j]:
                for k in d_basis[i]:derivative[3*k+j]^=1
    # Derive every entry from the independently checked tensor pairing.
    E2=[[{int(k):1 if coefficient==1 else c for k,coefficient in v.items()}
         for v in row] for row in encoded]
    ss=[[None,0,1],[0,None,2],[1,2,None]]
    T=[[sp.S.Zero]*18 for _ in range(18)]
    for i in range(6):
        for j in range(3):
            for a in range(6):
                for b in range(3):
                    z=ss[j][b]
                    if coefficients[3*i+j] and z is not None:
                        for k,v in E2[i][a].items():T[3*k+z][3*a+b]+=v
    def red(e):return sp.Poly(e,c,modulus=2).as_expr()
    T=sp.Matrix([[red(v) for v in row] for row in T])
    assert all(red(v)==0 for v in T*sp.Matrix(coefficients))
    assert all(red(v)==0 for v in T*sp.Matrix(derivative))
    assert coefficients[0]==1 and derivative[0]==0 and derivative[3]==1
    M=T.T
    MM=M*M.applyfunc(lambda e:e.subs(c,c*c))
    MM=MM.applyfunc(red)
    assert [[int(sp.Poly(v,c,modulus=2).nth(i)) for i in range(4)]
            for v in MM]==[[int(bits>>i&1) for i in range(4)]
                           for row in chosen['two_iterate_matrix'] for bits in row]
    R=sp.GF(2).poly_ring(c)
    rows,cols=chosen['minor_rows'],chosen['minor_columns']
    exact_minor=DomainMatrix([[R.from_sympy(MM[i,j]) for j in cols] for i in rows],(16,16),R)
    determinant=exact_minor.det()
    assert determinant==R.from_sympy(c**5)
    out.update({'status':'PASS','p_basis_identities':6,'ordinary_pairing_identities':36,
                'ordinary_pairing':pairing,'section_coefficients':coefficients,
                'ordinary_derivative_coefficients':derivative,
                'minor_rows_zero_based':rows,'minor_columns_zero_based':cols,
                'minor_determinant':str(determinant),
                'matrix_orientation':'M=(T_s^[2])^t; Frobenius2=M M^[2]',
                'squared_cartier_matrix':[[str(v) for v in row] for row in T.tolist()]})
except Exception:
    out['status']='FAIL';out['traceback']=traceback.format_exc()
finally:
    out['elapsed_seconds']=time.perf_counter()-started
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('ordinary_pairing','squared_cartier_matrix')},indent=2))
