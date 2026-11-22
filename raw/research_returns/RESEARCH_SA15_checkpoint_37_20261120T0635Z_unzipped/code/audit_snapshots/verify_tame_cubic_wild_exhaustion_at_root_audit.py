"""Exact B57 first-term/ramification supplement; no BT model is constructed."""
from pathlib import Path
import datetime,json,math,time,itertools
started=time.perf_counter()
first_term_cases=0;anti_pair_cases=0;cartan_anti_cases=0
patterns={}
for p in [5,7,11,13,17,19]:
    q,N=p*p,p*p-1;A=p*(p-1);b0=N*(p-1);limit=(q-1)*A
    def signature(kind,b):
        if b==b0:return None
        j=A+(p-1)*b if b<b0 else q*A-b
        if not(A<j<q*A and j%p):return False
        return j,('linear' if b<b0 or kind=='Cartan' else 'Frobenius')
    antis=[b for b in range(N//2,limit,N)]
    cartans=list(range(N,limit,N))
    sigs={b:signature('anti',b) for b in antis}
    for b,sig in sigs.items():
        first_term_cases+=1
        assert b!=b0
        if sig:
            j,kind=sig
            if b<b0:
                assert j==A+(p-1)*b and kind=='linear' and b%p
            else:assert j==q*A-b and kind=='Frobenius'
    valid=[(b,sig) for b,sig in sigs.items() if sig]
    for ix,(b,sig) in enumerate(valid):
        for c,other in valid[ix+1:]:
            anti_pair_cases+=1
            assert sig!=other
    allowed=[]
    for b,sig in valid:
        for c in cartans:
            cartan_anti_cases+=1
            if c==b0:
                compatible=sig[0]>=q*A-b0
            else:
                cs=signature('Cartan',c)
                compatible=bool(cs) and cs==sig
            expected=(b<b0 and b%p and c==p*b0-(p-1)*b)
            assert compatible==bool(expected),(p,b,c,sig)
            if compatible:allowed.append([b,c])
    assert len(allowed)==p-2
    assert all(b%p and b<b0<c and b%(N)==N//2 and c%N==0 for b,c in allowed)
    patterns[str(p)]=allowed
assert patterns['5']==[[12,432],[36,336],[84,144]]
# Actual Fp² multiplication/Frobenius and scalar impossibility on the Cartan plane.
scalar_cases=0;cartan_conjugacy_cases=0
for p in [5,7,11,13]:
    ns=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    def mul(x,y):return ((x[0]*y[0]+ns*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def power(x,n):
        out=(1,0)
        while n:
            if n&1:out=mul(out,x)
            x=mul(x,x);n//=2
        return out
    def sig(x):return x[0],-x[1]%p
    els=[(a,b) for a in range(p) for b in range(p)]
    for a in els[1:]:
        ai=power(a,p*p-2)
        for beta in els:
            for z in [(1,0),(0,1)]:
                x=mul(sig(ai),sig(z))
                x=mul(beta,x)
                x=mul(a,sig(x))
                assert x==mul(sig(beta),z)
            cartan_conjugacy_cases+=1
    for k in els:
        witness=(1,0) if k!=(1,0) else (0,1)
        assert mul(k,witness)!=sig(witness)
        scalar_cases+=1
# Enumerate every projective dual row, hence every hyperplane, over F5.
p=5
def normalized(row):
    first=next((x for x in row if x),None)
    if first is None:return None
    inv=pow(first,-1,p)
    return tuple(inv*x%p for x in row)
rows={normalized(row) for row in itertools.product(range(p),repeat=4)}-{None}
assert len(rows)==156
fixed=[]
for row in sorted(rows):
    transformed=normalized((row[0],row[1],-row[2]%p,-row[3]%p))
    if transformed==row:
        z_support=any(row[:2]);u_support=any(row[2:])
        assert z_support!=u_support
        fixed.append({'dual_row':row,'cartan_dimension':1 if z_support else 2,'anti_dimension':2 if z_support else 1})
assert len(fixed)==12
assert sum(r['cartan_dimension']==1 for r in fixed)==6
assert sum(r['cartan_dimension']==2 for r in fixed)==6
r={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'scope':'Exact first-prime-degree compatibility, lower-break patterns and finite Cartan conjugacy only; no formal-group or pair-existence inference.',
   'first_term_cases':first_term_cases,'anti_two_break_comparisons':anti_pair_cases,'Cartan_anti_break_comparisons':cartan_anti_cases,
   'Cartan_conjugacy_cases':cartan_conjugacy_cases,'scalar_Frobenius_cases':scalar_cases,
   'necessary_one_model_patterns':patterns,'p5_all_hyperplanes_checked':len(rows),'p5_invariant_three_space_shapes':fixed,
   'runtime_seconds':time.perf_counter()-started}
Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_b57_exact_arithmetic.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k not in ('p5_invariant_three_space_shapes','necessary_one_model_patterns')},indent=2))
