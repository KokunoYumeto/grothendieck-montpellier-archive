#!/usr/bin/env python3
"""AM-K047 exact Q(i,sqrt(-7)) identities and actual displacement bounds."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from math import gcd
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def ck(name, statement):
    if not statement:
        raise AssertionError(name)
    CHECKS.append(name)


def K(x):
    return x if isinstance(x, tuple) else (F(x), F(0), F(0), F(0))


def add(x, y):
    return tuple(a+b for a,b in zip(K(x), K(y)))


def neg(x):
    return tuple(-a for a in K(x))


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    # Basis indices are 1, i, delta, i*delta; i^2=-1, delta^2=-7.
    z = [F(0)]*4
    for a, ca in enumerate(K(x)):
        for b, cb in enumerate(K(y)):
            factor = (-1 if a & b & 1 else 1)*(-7 if a & b & 2 else 1)
            z[a ^ b] += factor*ca*cb
    return tuple(z)


def bar(x):
    return tuple(c*(-1 if j.bit_count() % 2 else 1) for j,c in enumerate(K(x)))


def mat(rows):
    return [[K(x) for x in row] for row in rows]


def mm(A, B):
    return [[sumk(mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def sumk(xs):
    out = K(0)
    for x in xs:
        out = add(out,x)
    return out


def star(A):
    return [[bar(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def det2(A):
    return sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]))


def ma(A,B):
    return [[add(x,y) for x,y in zip(ar,br)] for ar,br in zip(A,B)]


def scale(x,A):
    return [[mul(x,y) for y in row] for row in A]


def main():
    ii = (F(0),F(1),F(0),F(0)); delta = (F(0),F(0),F(1),F(0))
    ck('exact field relations and CM conjugation',mul(ii,ii)==K(-1)
       and mul(delta,delta)==K(-7) and bar(ii)==neg(ii) and bar(delta)==neg(delta))
    I=mat([[1,0],[0,1]]);J=mat([[1,0],[0,-1]])
    v=mat([[1],[1]]);N=mm(mm(v,star(v)),J)
    ck('isotropic rank-one nilpotent',mm(mm(star(v),J),v)==mat([[0]])
       and mm(N,N)==mat([[0,0],[0,0]]) and N!=mat([[0,0],[0,0]]))
    inp=ROOT/'work/agents/definite_oscillator_large_t_certificate.json'
    data=json.loads(inp.read_text());reports=[]
    ck('carried deterministic prime certificate',data['status']=='DETERMINISTIC_CERTIFICATE_PASS')
    for row in data['rows']:
        name=row['host'];a=row['a'];D=int(row['D']);T=int(row['T'])
        Q=row['g0']*row['g1'];A=(T+1)//2;B=(T-1)//2
        pi=add(1+2*D,mul(D,delta));cp=bar(pi)
        invpi=mul(F(1,T),cp);invcp=mul(F(1,T),pi)
        ck(name+' actual norm generator and rational prime formula',
           mul(pi,cp)==K(T) and T==11*D*D+4*D+1 and T%2==1)
        ck(name+' exact generator inverses',mul(pi,invpi)==K(1) and mul(cp,invcp)==K(1))
        g=mat([[mul(A,invpi),mul(B,invcp)],[mul(B,invpi),mul(A,invcp)]])
        gi=mm(mm(J,star(g)),J)
        ck(name+' global special-unitary matrix',mm(mm(star(g),J),g)==J and det2(g)==K(1))
        ck(name+' actual rational inverse',mm(g,gi)==I and mm(gi,g)==I)
        tau=mat([[1,0],[mul(cp,invpi),1]])
        k=mat([[mul(A,invcp),neg(mul(B,invcp))],[neg(cp),cp]])
        ck(name+' selected finite factorization and determinant',mm(tau,k)==gi and det2(k)==K(1))
        ck(name+' coprime norm halves',gcd(T,2*(1+2*D))==1)
        ck(name+' unchanged principal G congruence',D%(Q*Q)==0 and
           (T-1)%(Q*Q)==0 and (A-1)%(Q*Q)==0 and B%(Q*Q)==0)
        # Numerators of g-I over the denominator T. All coefficients are integral.
        numer=ma(scale(T,g),scale(-T,I))
        ck(name+' every G-congruence numerator coefficient',
           all(c.denominator==1 and c.numerator%(Q*Q)==0 for rr in numer for x in rr for c in x)
           and gcd(T,Q)==1)
        tt=mul(Q,ii);u0=ma(I,scale(tt,N))
        ck(name+' integral principal unipotent',mm(mm(star(u0),J),u0)==J and det2(u0)==K(1)
           and mm(u0,ma(I,scale(neg(tt),N)))==I and u0!=I)
        w=mm(gi,v);expected_w=mat([[invcp],[invpi]])
        ck(name+' exact contracted isotropic vector',w==expected_w and mm(mm(star(w),J),w)==mat([[0]]))
        gam=mm(mm(gi,u0),g)
        expected=ma(I,scale(tt,mm(mm(w,star(w)),J)))
        explicit=ma(I,scale(tt,mat([[F(1,T),neg(mul(invcp,invcp))],
                                  [mul(invpi,invpi),F(-1,T)]])))
        ck(name+' rational conjugate and explicit entries',gam==expected==explicit and gam!=I)
        ck(name+' conjugate special-unitary and nontrivial nilpotent',
           mm(mm(star(gam),J),gam)==J and det2(gam)==K(1)
           and mm(ma(gam,scale(-1,I)),ma(gam,scale(-1,I)))==mat([[0,0],[0,0]]))
        ck(name+' exact all-embedding Euclidean vector norm',mm(star(w),w)==mat([[F(2,T)]]))
        bound=953 if name=='J14' else 923
        ck(name+' exact tiny Cartan displacement bound',2*Q*(2**bound)<T and 2*Q<T)
        ck(name+' advertised bit lengths',
           (row['g0'].bit_length(),row['g1'].bit_length(),T.bit_length())==
           ((23,23,1001) if name=='J14' else (35,36,996)))
        # At each selected T component pi=0, so cp=2(1+2D) in F_T.
        c_res=2*(1+2*D)%T;inv_c=pow(c_res,-1,T)
        u=[pow(2,j,T) for j in range(a)]
        first=[inv_c*x%T for x in u]
        ck(name+' actual local covector transport',all(c_res*x%T==y for x,y in zip(first,u))
           and first[0]==inv_c and inv_c!=0)
        # The triangular matrix has first row u/c, later rows standard.
        # Its inverse has first row (c,-u_2,...,-u_a), later rows standard.
        ck(name+' triangular transport inverse and unit determinant',
           first[0]*c_res%T==1 and all((-first[0]*u[j]+first[j])%T==0 for j in range(1,a)))
        reports.append(dict(host=name,a=a,Q=Q,T_bits=T.bit_length(),bound=f'Cartan u<2^-{bound}',
            displacement_numerator=2*Q,displacement_denominator=str(T),
            selected_c_residue=str(c_res),local_transport_determinant_residue=str(inv_c)))
    inputs=[inp,ROOT/'work/research/standard_bottom_finite_level_adapter.md',
            ROOT/'work/agents/primitive_negative_line_and_bottom_pin.md',
            ROOT/'work/agents/bottom_dat0_translation_detector.md']
    result=dict(finding='AM-K047',status='PASS',utc=datetime.now(timezone.utc).isoformat(),
        grouped_checks=len(CHECKS),checks=CHECKS,actual=reports,
        scope='Exact rational CM-field matrix/form checks, G congruences, both actual finite-covector transports and displacement bounds. Carries prior deterministic T primality. No lattice enumeration, global cusp vanishing, projected period or Lean build.',
        input_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',utc=result['utc'],checks=len(CHECKS),output=str(dest))))


if __name__=='__main__':
    main()
