#!/usr/bin/env python3
"""Independent rational/symbolic reconstruction of D-UNW and D-LNW constants.

No author checker is imported.  Published character theorems are source inputs;
the universal two-regime and normalizer arguments are separately proof-read.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import sympy as s
import hashlib,json,re,time

HERE=Path(__file__).resolve().parent
OTHER=HERE.parent.parent/'imprimitive/unitary_nonweil'

def main():
    start=time.perf_counter()
    C=16384*10**12
    root=isqrt(9*C)
    assert root*root==9*C
    sigma=min(Q(1,241*root**3),Q(1,8192*10**12*82))
    assert sigma==Q(1,6507*2097152*10**18)
    small=Q(1,10**29); J=10**30; N=10**61
    assert sigma>7*small and N>2*J
    assert N-J*J-J-8>0 and N-2*J*J-9>0
    exponent=small*J/4
    assert exponent==Q(5,2)
    # Positive squaring verifies 2^(-5/2)<1/4 exactly.
    assert Q(1,2**5)<Q(1,4**2)

    x,n,j,u,d=s.symbols('x n j u d')
    def coefficients_nonnegative(p,var):
        return all(c>=0 for c in s.Poly(s.expand(p),var).all_coeffs())
    # The degree-denominator bounds hold for all q=x+2, x>=0.
    assert coefficients_nonnegative((x+2)**3-2*(x+3),x)
    assert coefficients_nonnegative((x+2)**2-(x+3),x)
    # The low/high degree regimes, by exact decompositions used in the proof.
    assert s.expand(j*(n-j)-3-n*j/4-(j*(n/2-j)+(n*j/4-3)))==0
    assert coefficients_nonnegative(((x+8)**2/s.Integer(4)-4)-(x+8)**2/s.Integer(8),x)
    assert s.expand(j*(n-j)-2*(n-2)-(j-2)*(n-j-2))==0
    assert coefficients_nonnegative((x+8)**2/s.Integer(4)-4-(x+8),x)
    # Both square-root tail bounds, valid for all j>=2.
    assert s.expand(2*j*j-(j*j+j-1)-((j-1)**2+j))==0
    assert s.expand(2*j*j-(j*j+j)-j*(j-1))==0
    assert Q(413,25)<25 and 8<9

    # Independently normalize every exponent in the two exact source displays.
    middle=s.expand(j*j+(n-1)*(j-1)+1-n*j)
    assert middle==j*j-n-j+2
    assert s.expand(2*j*j+n*(j-2)-n*j)==2*j*j-2*n
    assert s.expand(2*j*j+n*(j-1)-n*j)==2*j*j-n
    assert s.expand((j*j-n)-middle)==j-2
    assert s.expand((2*j*j-n)-(j*j-n))==j*j

    # Error functions are increasing on their stated positive ranges.
    unit_error=2*u+10*u*u
    assert s.diff(unit_error,u)==2+20*u
    ratio=(s.Rational(1,4)+d)/(1-d)
    assert s.simplify(s.diff(ratio,d)-s.Rational(5,4)/(1-d)**2)==0
    du=2*Q(1,256)+10*Q(1,256)**2
    assert du==Q(261,32768)<Q(1,100)
    exact_unit_ratio=(Q(1,4)+du)/(1-du)
    relaxed_unit_ratio=(Q(1,4)+Q(1,100))/(1-Q(1,100))
    dl=4*Q(1,512)
    linear_ratio=(Q(1,4)+dl)/(1-dl)
    assert linear_ratio==Q(33,127)<relaxed_unit_ratio==Q(26,99)<Q(4,15)
    assert exact_unit_ratio<relaxed_unit_ratio
    support=(1-Q(4,15))/4
    assert support==Q(11,60)<Q(1,4)
    assert 6/(12*support-2)==30

    proofs={}
    for name in ('unitary_nonweil_section.tex','linear_nonweil_section.tex'):
        p=OTHER/name; text=p.read_text()
        assert text.count('\\[')==text.count('\\]')
        stack=[]
        for typ,env in re.findall(r'\\(begin|end)\{([^}]+)\}',text):
            if typ=='begin':stack.append(env)
            else:assert stack and stack.pop()==env
        assert not stack
        proofs[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    sources={name:hashlib.sha256((OTHER/'cache'/name).read_bytes()).hexdigest()
             for name in ('LT2024_author.pdf','GLT2020_published.pdf')}
    assert sources['LT2024_author.pdf']=='70d2546d2a0f01f8e701aa718201216f2b334b6cd074c12b41c2c59e0b7cdd4f'
    assert sources['GLT2020_published.pdf']=='0726271e666bd5eb736ff91ea031ef83bb072f2e10f27b664c217d7702926c32'
    out={'result':'PASS','proofs':proofs,'sources':sources,'published_sigma':str(sigma),
         'chosen_sigma':str(small),'level_split':str(J),'natural_dimension_cutoff':str(N),
         'unitary_exact_error':str(du),'unitary_exact_ratio':str(exact_unit_ratio),
         'unitary_relaxed_ratio':str(relaxed_unit_ratio),'linear_error':str(dl),
         'linear_ratio':str(linear_ratio),'common_ratio':'4/15',
         'normalizer_support':str(support),'total_degree_ceiling':30,
         'runtime_seconds':time.perf_counter()-start,
         'scope':'Independent exact constants and universal polynomial decompositions; no author arithmetic, character-table scan, or enumeration of the enormous remaining rank range. TeX delimiters/environments checked, not compiled.'}
    (HERE/'audit_nonweil_cutoffs.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
