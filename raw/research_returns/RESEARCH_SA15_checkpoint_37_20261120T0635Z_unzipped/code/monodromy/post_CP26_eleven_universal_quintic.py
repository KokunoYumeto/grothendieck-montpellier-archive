"""Universal norm-eleven quintic algebra; exploratory, not a nodality proof."""
from pathlib import Path
from datetime import datetime, timezone
import json, time, signal, traceback
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start = time.perf_counter()
agent = Path(__file__).resolve().parents[1]
result = {"status": "RUNNING", "stages": []}

def timeout(*args):
    raise TimeoutError("Universal quintic bounded run exceeded60seconds")

signal.signal(signal.SIGALRM, timeout)
signal.alarm(60)
try:
    rr = symbols("r")
    base = GF(2).frac_field(rr)
    r = base.gens[0]
    Q, L, t = ring("L,t", base)
    con = Q.ground_new
    D = r*r
    z = (D+1)/r**3
    a, b = z*z, z*z+z+1
    gt = t*t+t+con(D)
    red = lambda x: x.div([gt])[1]
    mul = lambda x,y: red(x*y)
    alpha = t/con(D)
    beta = alpha+1
    gamma = con((r**6+r**5+r+1)/r**4)*t+con((r**3+r+1)/r**2)
    norm_gamma = red(mul(gamma, gamma.compose(t,t+1)))
    assert norm_gamma.degree(L) <= 0 and norm_gamma.degree(t) <= 0
    norm_value = norm_gamma[(0,0)]
    inverse_gamma = gamma.compose(t,t+1)/con(norm_value)
    assert mul(gamma,inverse_gamma) == 1
    inverse_alpha_squared = red((t+1)**2)
    assert mul(alpha*alpha,inverse_alpha_squared) == 1
    A4 = con(a*D)
    A2 = con((r**6+r**2+1)/r**4)
    A1 = con((r**4+1)/r**2)
    A = A4*L**3+A2*L+A1
    theta_const = red(con(a)*t**5+con(b)*t**3+t*t*con(z+1))
    L0 = red(con(a*D*D)*(L+t+1)+theta_const)
    aa,bb,gg = mul(alpha,alpha),mul(beta,beta),mul(gamma,gamma)
    C = [mul(inverse_alpha_squared,x) for x in
         [mul(L0,gg),gg,mul(L0,bb),bb,mul(L0,aa)+1,aa]]
    assert C[5] == 1

    def trim(p):
        while p and not p[-1]:
            p.pop()
        return p

    def padd(p,q):
        return trim([(p[i] if i<len(p) else Q.zero)+(q[i] if i<len(q) else Q.zero)
                     for i in range(max(len(p),len(q)))])

    def scale(p,c):
        return trim([mul(x,c) for x in p])

    def reduce_y(p):
        p=trim([red(x) for x in p])
        while len(p)>5:
            shift=len(p)-6
            lead=p[-1]
            for i in range(6):
                p[shift+i] += mul(lead,C[i])
            trim(p)
        return p

    def pmul(p,q):
        out=[Q.zero]*(len(p)+len(q)-1) if p and q else []
        for i,x in enumerate(p):
            for j,y in enumerate(q):
                out[i+j] += mul(x,y)
        return reduce_y(out)

    factor=mul(t*t,mul(inverse_gamma,inverse_gamma))
    u=scale([mul(bb,L0),bb,mul(aa,L0)+1,aa],factor)
    # On the quintic, u=t^2(1/Y+L0/Y^2); check without inverting Y.
    assert not padd(pmul(u,[Q.zero,Q.zero,Q.one]),
                    scale([L0,Q.one],red(t*t)))
    B=padd([Q.zero,Q.one],padd(scale(padd(scale(u,L*L),pmul(u,u)),A4),scale(u,A2)))
    P=padd(pmul(B,B),padd(scale(B,L*A),scale(u,mul(A,A))))
    result["stages"].append({"stage":"quintic_and_polynomial_u","seconds":time.perf_counter()-start})
    print(json.dumps(result["stages"][-1]),flush=True)

    def matrix_of(f):
        cols=[pmul(f,[Q.zero]*i+[Q.one]) for i in range(5)]
        return [[col[j] if j<len(col) else Q.zero for col in cols] for j in range(5)]

    def berkowitz(matrix):
        n=len(matrix)
        if not n:
            return [Q.one]
        sub=[row[1:] for row in matrix[1:]]
        c=berkowitz(sub)
        toe=[Q.one,matrix[0][0]]
        row=matrix[0][1:]
        vec=[line[0] for line in matrix[1:]]
        for power in range(n-1):
            toe.append(sum((mul(x,y) for x,y in zip(row,vec)),Q.zero))
            if power<n-2:
                vec=[sum((mul(x,y) for x,y in zip(line,vec)),Q.zero) for line in sub]
        return [sum((mul(toe[i-j],c[j]) for j in range(max(0,i-n),min(i,n-1)+1)),Q.zero)
                for i in range(n+1)]

    cp=berkowitz(matrix_of(P))
    cb=berkowitz(matrix_of(B))
    assert cp[0] == cb[0] == 1
    result["stages"].append({"stage":"universal_characteristics","seconds":time.perf_counter()-start,
                             "P_L_degrees":[f.degree(L) for f in cp],"B_L_degrees":[f.degree(L) for f in cb]})
    print(json.dumps(result["stages"][-1]),flush=True)
    one,c4,c3,c2,c1,c0=cp
    powq=lambda f,n: red(f**n)
    condition1=red(c2**4+c3**3*c2**2+c1*c3**4)
    condition2=red(c2**5+c4*c2**4*c3+c1*c2*c3**4+c0*c3**5)
    exceptional=red(c0+c4*c1)

    # Compare the entire characteristic polynomial with the retained exact F16 run.
    from gf16_exact_domain import K16,F16
    RL,ll=ring("L",K16)
    rval,tval=F16(2),F16(8)
    def eval_base(x):
        def poly_eval(p):
            return sum((F16(int(co))*rval**mon[0] for mon,co in p.items()),F16(0))
        return poly_eval(x.numer)/poly_eval(x.denom)
    def specialize(f):
        return sum((ll**i*(eval_base(co)*tval**j) for (i,j),co in f.items()),RL.zero)
    retained=json.loads((agent/'outputs/probe_eleven_finite_quintic.json').read_text())
    env={"L":ll,**{f"u{i}":F16(i) for i in range(16)}}
    for actual,expected in zip(cp,retained['charpoly_P']):
        assert specialize(actual)==eval(expected,{"__builtins__":{}},env)
    result.update({"status":"PASS_UNIVERSAL_QUINTIC_IDENTITIES_ONLY",
      "gamma_norm":str(norm_value),"quintic_coefficients_ascending":[str(f) for f in C],
      "A":str(A),"L0":str(L0),"u_coefficients_ascending":[str(f) for f in u],
      "charpoly_P":[str(f) for f in cp],"charpoly_B":[str(f) for f in cb],
      "triple_condition1":str(condition1),"triple_condition2":str(condition2),
      "triple_exceptional_c3":str(c3),"triple_exceptional_c2":str(c2),
      "triple_exceptional_last":str(exceptional),
      "scope":"Universal polynomial identities and exact retained F16 characteristic comparison only. No parameter-resultant, triple-fibre exclusion, nodality or full-image claim."})
except Exception:
    result.update({"status":"EXPLORATORY_FAILURE","traceback":traceback.format_exc()})
finally:
    signal.alarm(0)
    result['actual_utc']=datetime.now(timezone.utc).isoformat()
    result['runtime_seconds']=time.perf_counter()-start
    output=agent/'outputs/post_CP26_eleven_universal_quintic.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','actual_utc','runtime_seconds','stages']},indent=2))
