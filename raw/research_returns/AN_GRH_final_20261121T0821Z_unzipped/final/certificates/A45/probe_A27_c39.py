#!/usr/bin/env python3
"""Exact degree39 character tables for A27 and its F4 quadratic twist.

This imports the already checked linear-interpolation implementation; it is
not an independent reimplementation of Jacobian arithmetic.
"""
from pathlib import Path
import hashlib
import importlib.util
import itertools
import json
from sympy import Matrix, Poly, symbols, cyclotomic_poly, ZZ
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT/'verify_A27_character13_linear.py'
spec = importlib.util.spec_from_file_location('retained_A32_linear', SOURCE)
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)


def frobenius4(D):
    return tuple(tuple(ar.M[ar.M[c][c]][ar.M[c][c]] for c in pol) for pol in D)


def v2(n):
    return (abs(int(n)) & -abs(int(n))).bit_length()-1 if n else None


def l_value_data(counts, conductor, q=256):
    X = symbols('X')
    phi = Poly(cyclotomic_poly(conductor, X), X, domain=ZZ)
    coeff = list(counts)
    coeff[0] += 1+q
    value = Poly(sum(c*X**i for i,c in enumerate(coeff)), X, domain=ZZ).rem(phi)
    degree = phi.degree()
    columns = []
    for j in range(degree):
        col = (value*Poly(X**j, X)).rem(phi)
        columns.append([int(col.nth(i)) for i in range(degree)])
    matrix = Matrix(degree, degree, lambda i,j:columns[j][i])
    diagonal = smith_normal_form(matrix, domain=ZZ)
    vals = [v2(diagonal[i,i]) for i in range(degree)]
    assert all(v is not None for v in vals)
    return {'L_value_ascending':[int(value.nth(i)) for i in range(degree)],
            'smith_diagonal':[int(diagonal[i,i]) for i in range(degree)],
            'two_adic_valuations': vals, 'max_valuation': max(vals)}


def main():
    raw = json.loads((ROOT/'A32_ALL_POINT_IMAGES.json').read_text())
    Ds = [ar.IDENTITY if r['point'] is None else
          ((r['point'][0],1),(r['point'][1],) if r['point'][1] else ()) for r in raw]
    projected = [ar.scalar(D,7280) for D in Ds]
    values = list(dict.fromkeys(projected))
    print('distinct3projections',len(values),flush=True)
    nonzero = [D for D in values if D != ar.IDENTITY]
    orders = [next(n for n in (3,9) if ar.scalar(D,n)==ar.IDENTITY) for D in nonzero]
    print('orders',orders,flush=True)
    if max(orders)==9:
        basis = [next(D for D,n in zip(nonzero,orders) if n==9)]
        span = {ar.scalar(basis[0],i):[i] for i in range(9)}
    else:
        basis = [nonzero[0]]
        span = {ar.scalar(basis[0],i):[i] for i in range(3)}
    if any(D not in span for D in values):
        basis.append(next(D for D in values if D not in span))
        span = {ar.add_divisors(ar.scalar(basis[0],i),ar.scalar(basis[1],j)):[i,j]
                for i in range(3) for j in range(3)}
    assert len(span)==9 and all(D in span for D in projected)
    Fmatrix=[span[frobenius4(D)] for D in basis]
    print('Frobenius4_columns',Fmatrix,flush=True)
    assert Fmatrix == [[8]]
    delta13 = tuple(tuple(a) for a in next(r['projected_Mumford'] for r in raw if r['image_in_Z13']==1))
    assert frobenius4(delta13) == ar.scalar(delta13,5)
    twist_root = next(c for c in range(256) if ar.M[c][c]^c == ar.u)
    assert ar.M[ar.M[twist_root][twist_root]][ar.M[twist_root][twist_root]]^twist_root == 1
    counts13=[0]*13
    for r in raw: counts13[r['image_in_Z13']]+=1
    candidates=[]
    for line in itertools.product(range(3),repeat=len(basis)):
        if not any(line) or next(x for x in line if x)!=1:
            continue
        if any(sum(line[i]*Fmatrix[j][i] for i in range(len(basis)))%3 != 2*line[j]%3 for j in range(len(basis))):
            continue
        counts=[0]*39
        counts3=[0]*3
        twist_counts3_F4=[0]*3
        twist_F4_points=[]
        images=[]
        for r,D in zip(raw,projected):
            a3=sum(x*y for x,y in zip(line,span[D]))%3
            a13=r['image_in_Z13']
            a39=next(i for i in range(39) if i%3==a3 and i%13==a13)
            counts[a39]+=1; counts3[a3]+=1
            images.append({'point':r['point'],'a3':a3,'a13':a13,'a39':a39})
            if r['point'] is None:
                twist_counts3_F4[a3]+=1
                twist_F4_points.append({'point':None,'a3':a3})
            else:
                x,y=r['point']; yt=y^ar.M[twist_root][ar.M[x][x]]
                if all(ar.M[ar.M[c][c]][ar.M[c][c]]==c for c in (x,yt)):
                    twist_counts3_F4[a3]+=1
                    twist_F4_points.append({'point':[x,yt],'original_point':[x,y],'a3':a3})
        assert twist_counts3_F4==[2,1,1]
        X=symbols('X')
        phi39=Poly(cyclotomic_poly(39,X),X,domain=ZZ)
        L39=l_value_data(counts,39)
        assert all(c%2==0 for c in L39['L_value_ascending'])
        half_binary=sum(((c//2)%2)<<i for i,c in enumerate(L39['L_value_ascending']))
        phi_binary=sum((int(phi39.nth(i))%2)<<i for i in range(phi39.degree()+1))
        gcd,bezout_left,bezout_right=ar.f2bezout(half_binary,phi_binary)
        assert gcd==1
        assert ar.f2product(half_binary,bezout_left)^ar.f2product(phi_binary,bezout_right)==1
        result={'functional':line,'counts':counts,'counts3':counts3,
                'twist_conductor3_counts_F4':twist_counts3_F4,
                'twist_F4_points':twist_F4_points,
                'twist_conductor3_over_F4':l_value_data(twist_counts3_F4,3,4),
                'conductor3_over_F256':l_value_data(counts3,3),
                'conductor13_over_F256':l_value_data(counts13,13),
                'conductor39_over_F256':L39,
                'Phi39_binary':phi_binary,'L39_half_mod2_binary':half_binary,
                'L39_half_Bezout_binary':[bezout_left,bezout_right],
                'all_point_images':images}
        candidates.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!='all_point_images'}),flush=True)
    result={'status':'PASS','scope':'exploratory exact tables; imports retained A32 Jacobian arithmetic',
            'arithmetic_source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'basis3':basis,'frobenius4_columns':Fmatrix,
            'delta13':delta13,'frobenius4_on_delta13':5,
            'quadratic_twist_coefficient':ar.u,'twist_root_in_F256':twist_root,
            'twisted_deck_Frobenius_exponent_C39':34,'minimal_deck_constant_degree':4,
            'candidates':candidates,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
