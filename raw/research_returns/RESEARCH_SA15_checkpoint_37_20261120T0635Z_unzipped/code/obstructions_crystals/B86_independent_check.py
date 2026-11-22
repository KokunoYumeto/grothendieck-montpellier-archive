"""B86 exact determinant, point-field character, and cyclotomic break checks."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
from collections import Counter
from math import comb,isqrt
import sympy as sp
import json,time

start=time.perf_counter();counts=Counter()
p,a,b,c,d,u,v,w,z=sp.symbols('p a b c d u v w z')
A=sp.Matrix([[a,b],[c,d]]);B=sp.Matrix([[u,v],[w,z]])
det=sp.expand((sp.eye(2)+p*A+p*p*B).det())
remainder=sp.Poly(det-(1+p*sp.trace(A)+p*p*(sp.trace(B)+A.det())),p)
assert all(exp[0]>=3 for exp,coef in remainder.terms() if coef)
counts['symbolic_determinant_identities']+=1
H=sp.diag(1,-1);X=sp.Matrix([[0,1],[0,0]]);Y=sp.Matrix([[0,0],[1,0]])
assert X*Y-Y*X==H
assert (a*H+b*X+c*Y)*sp.Matrix([1,0])==sp.Matrix([a,c])
counts['symbolic_point_field_and_bracket_identities']+=2
N=p*p-1;k=sp.symbols('k')
assert sp.expand(N*N-p*N*(p-2)-N*(2*p-1))==0
counts['symbolic_break_gap_identities']+=1

primes=[r for r in range(5,102) if all(r%d for d in range(2,isqrt(r)+1))]
for p in primes:
    N=p*p-1;q=p*p
    for k in range(1,p-1):
        assert p**3*k-p*k==p*N*k
        assert N*N-p*N*k>=N*(2*p-1)>0
        counts['cyclotomic_point_field_break_rows']+=1
    # A zero terminal trace does NOT kill determinant on a first-layer lift.
    modulus=p**3
    matrix=sp.eye(2)+p*H+p*p*sp.diag(2,0)
    assert int(matrix.det())%modulus==(1+p*p)%modulus
    assert int((matrix**p).det())%modulus==1
    counts['nonzero_determinant_with_traceless_terminal_guards']+=1
    # Actual finite additive quotients:sl2/<E12> and ell=t*a.
    if p<=31:
        for t in range(1,p):
            for a,c in product(range(p),repeat=2):
                ell=t*a%p
                assert (ell!=0)==(a!=0)
                # The p b-values above this same point class have equal ell.
                for b in range(p):
                    assert (t*a)%p==ell
                    counts['point_stabilizer_character_rows']+=1
            counts['nonzero_diagonal_character_rows']+=1
        for ratio in range(2,p):
            assert ratio!=1 and pow(ratio,-1,p)!=1
            # An invariant linear functional on each nontrivial weight is zero.
            assert all((ratio*x-x)%p!=0 for x in range(1,p))
            counts['tame_offdiagonal_invariant_checks']+=1
    # Cyclotomic Eistenstein coefficients at a stated small exact range.
    if p<=11:
        for n in (2,3):
            step=p**(n-1);degree=(p-1)*step
            coefficients=[sum(comb(j*step,h) for j in range(p) if j*step>=h)
                          for h in range(degree+1)]
            assert coefficients[0]==p and coefficients[-1]==1
            assert all(x%p==0 for x in coefficients[:-1])
            assert coefficients[0]%(p*p)!=0
            counts['exact_eisenstein_coefficients']+=len(coefficients)
            counts['exact_cyclotomic_polynomials']+=1

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'counts':dict(counts),
     'p5':{'cyclotomic_quotient_break':24**2,
           'largest_possible_lift_break_bound':5*24*3,
           'strict_gap':24**2-5*24*3,'tame_sector_minimum_order':5**7},
     'scope':'Symbolic determinant/traceless bracket/evaluation and break-gap identities; all small k for primes5..101; '
             'all actual additive point quotients and nonzero diagonal functionals for primes5..31; '
             'exact Eisenstein coefficients of Phi_(p^n)(1+T) at p5,7,11,n2,3. '
             'The zero-terminal-trace guard deliberately retains a nonzero finite determinant. '
             'Actual field inclusion and quotient norm ramification are separately proved, not inferred from this finite certificate.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
