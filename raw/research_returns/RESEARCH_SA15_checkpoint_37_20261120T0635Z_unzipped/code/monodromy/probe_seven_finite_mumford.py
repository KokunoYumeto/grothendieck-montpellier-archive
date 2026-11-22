"""Finite-parameter rational-coordinate probe, with all failures retained.

No geometric nodality conclusion is made by this exploratory program.
"""
from pathlib import Path
import datetime
import json
import signal
import time
import traceback
from sympy import Poly,symbols
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.rings import ring

start=time.perf_counter()
root=Path(__file__).resolve().parent.parent
def timeout(*unused):
    raise TimeoutError("Finite-parameter coordinate probe exceeded 90 seconds")
signal.signal(signal.SIGALRM,timeout)
signal.alarm(90)
result={"status":"RUNNING"}
try:
    aa=symbols("a0")
    K=MonogenicFiniteExtension(Poly(aa**4+aa+1,aa,modulus=2))
    K.gcd=lambda x,y: K.one if x or y else K.zero
    K.quo=K.exquo=lambda x,y: x/y
    gen=K.generator
    vals=[sum((gen**i for i in range(4) if n>>i&1),K.zero) for n in range(16)]
    enc={str(v):i for i,v in enumerate(vals)}
    choices=[]
    for rv in vals[2:]:
        zv=(rv**2+1)/rv**3
        av,bv=zv**2,zv**2+zv+1
        for tv in vals:
            if tv**2+tv!=rv**2: continue
            cg=zv*rv**2+tv
            if not cg: continue
            for bv0 in vals:
                if bv0**2+bv0!=zv+1: continue
                for wv in vals:
                    if wv**2+wv!=av*tv**5+bv*tv**3: continue
                    choices.append((rv,zv,tv,bv0,wv))
    assert choices
    choice=next((row for row in choices if row[1]**2+row[1]+1==0),choices[0])
    encoded=[enc[str(x)] for x in choice]
    print(json.dumps({"stage":"parameters","choice_r_z_t_beta_w":encoded,"choice_count":len(choices)}),flush=True)
    Rp,pp=ring("p",K)
    FF=Rp.to_field()
    p=FF.gens[0]
    r,z,t,beta,w=map(FF,choice)
    a,b,D=z**2,z**2+z+1,r**2
    u,v=z*(t+r),z*t**2+t+1/D
    gp=z*p**2+(z+1)*p+beta
    hp=u*p**2+v*p+w
    d1=a*p**4+b*p**2
    cg=z*D+t
    c=D*cg
    Z=hp+t**2*gp+D*d1+t*cg
    E=t*gp+hp+(t+1)*cg
    A3=(Z*E+c*cg)/D
    A2=(Z+c)*gp+c*d1+A3
    ell=p+A3**2/(a*Z**2)
    kappa=(b+a*(D+1))/a
    tau=c/Z
    cx=kappa+tau**2
    dd=p*ell+p**2+cx
    print(json.dumps({"stage":"quadratic","ell_degrees":[ell.numer.degree(),ell.denom.degree()],"constant_degrees":[dd.numer.degree(),dd.denom.degree()]}),flush=True)
    n1=tau*d1+(A2/Z)*ell+(A3/Z)*(ell**2+cx)
    n0=cx*((A2/Z)+(A3/Z)*ell)
    nu=(n0+tau*n1)/(cx+tau*ell+tau**2)
    eta_minus_y=n1+nu*(ell+tau)+nu*p
    print(json.dumps({"stage":"ordinate","nu_degrees":[nu.numer.degree(),nu.denom.degree()]}),flush=True)
    def serial(F):
        return {"numerator":[[e[0],enc[str(c)]] for e,c in F.numer.terms()],
                "denominator":[[e[0],enc[str(c)]] for e,c in F.denom.terms()]}
    result={
        "status":"PASS_FINITE_COORDINATES_ONLY",
        "sparse_integer_coordinates":{name:serial(F) for name,F in [("ell",ell),("constant",dd),("nu",nu),("eta_minus_y",eta_minus_y),("Z",Z)]},
        "modulus":"a0^4+a0+1",
        "choice_r_z_t_beta_w":encoded,
        "choice_count":len(choices),
        "ell":str(ell),"constant":str(dd),"nu":str(nu),
        "eta_minus_y":str(eta_minus_y),
        "scope":"One finite-parameter rational-coordinate computation. No triple-fibre exclusion or nodality is inferred.",
    }
except Exception:
    result={"status":"EXPLORATORY_FAILURE","traceback":traceback.format_exc()}
finally:
    signal.alarm(0)
    result["actual_timestamp_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result["runtime_seconds"]=time.perf_counter()-start
    (root/'outputs/probe_seven_finite_mumford.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
