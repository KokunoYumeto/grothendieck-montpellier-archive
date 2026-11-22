"""Bounded primitive pseudo-remainder elimination for the norm-eleven lead.

Every removed coefficient factor is retained. No specialization or geometric
conclusion is justified merely by a generic polynomial gcd.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, time, signal, traceback
from post_CP27_binary_coefficient_ring import cmul, divmodp, gcdp

start=time.perf_counter()
agent=Path(__file__).resolve().parents[1]
answer={"status":"RUNNING","stages":[],"removed_parameter_factors":[]}

def timeout(*unused):
    raise TimeoutError("Primitive elimination exceeded60seconds")

signal.signal(signal.SIGALRM,timeout)
signal.alarm(60)

def trim(p):
    p=list(p)
    while p and not p[-1]:p.pop()
    return p

def record_factor(f,why):
    if f not in (0,1):
        answer["removed_parameter_factors"].append({"factor_hex":hex(f),"degree":f.bit_length()-1,"reason":why})

def primitive(p,why):
    p=trim(p)
    if not p:return p
    g=0
    for x in p:
        g=gcdp(g,x)
        if g==1:return p
    record_factor(g,why)
    out=[]
    for x in p:
        q,r=divmodp(x,g);assert not r;out.append(q)
    return out

def pmul(p,q):
    out=[0]*(len(p)+len(q)-1) if p and q else []
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]^=cmul(x,y)
    return trim(out)

def pseudodiv(p,q):
    p=trim(p);quot=[0]*max(1,len(p)-len(q)+1)
    lc=q[-1];power=0
    while p and len(p)>=len(q):
        shift=len(p)-len(q);lead=p[-1]
        p=[cmul(x,lc) for x in p]
        quot=[cmul(x,lc) for x in quot]
        quot[shift]^=lead
        for i,x in enumerate(q):p[shift+i]^=cmul(lead,x)
        p=trim(p);power+=1
    return trim(quot),p,power

def pgcd(p,q,name):
    p=primitive(p,name+" initial left")
    q=primitive(q,name+" initial right")
    sequence=[]
    while q:
        if len(p)<len(q):p,q=q,p
        while p and len(p)>=len(q):
            shift=len(p)-len(q);lead=p[-1];lc=q[-1]
            record_factor(lc,name+" pseudo leading coefficient")
            p=[cmul(x,lc) for x in p]
            for i,x in enumerate(q):p[shift+i]^=cmul(lead,x)
            p=primitive(p,name+" intermediate content")
        sequence.append({"next_L_degree":len(p)-1,"max_v_degree":max((x.bit_length()-1 for x in p),default=-1)})
        p,q=q,p
    row={"stage":name,"seconds":time.perf_counter()-start,"gcd_L_degree":len(p)-1,"sequence":sequence,"gcd_coefficients_hex":[hex(x) for x in p]}
    answer["stages"].append(row)
    print(json.dumps({k:row[k] for k in ["stage","seconds","gcd_L_degree"]}),flush=True)
    return p

try:
    raw=json.loads((agent/'outputs/post_CP27_eleven_rational_quintic.json').read_text())
    assert raw['status']=='PASS_UNIVERSAL_QUINTIC_IDENTITIES_ONLY'
    take=lambda x:[int(v,16) for v in x['numerator_L_coefficients_v_binary_hex']]
    A=primitive(take(raw['A']),'A initial content')
    f,g,c3,c2,e=map(take,raw['triple_conditions'])
    h=pgcd(c3,c2,'exceptional_c3_c2')
    exceptional=pgcd(h,e,'exceptional_with_last')
    stripped=[]
    for idx,p in enumerate([f,g]):
        p=primitive(p,'generic initial content'+str(idx));count=0
        while len(p)>=len(A):
            quot,rem,power=pseudodiv(p,A)
            if rem:break
            record_factor(A[-1],'A exact-division leading coefficient')
            p=primitive(quot,'A quotient content'+str(idx));count+=1
        stripped.append(p)
        row={'stage':'strip_A_'+str(idx),'power':count,'remaining_L_degree':len(p)-1,'max_v_degree':max(x.bit_length()-1 for x in p),'seconds':time.perf_counter()-start}
        answer['stages'].append(row);print(json.dumps(row),flush=True)
    generic=pgcd(*stripped,'generic_after_A')
    answer.update({'status':'PASS_GENERIC_ELIMINATION_ONLY','A_coefficients_hex':[hex(x) for x in A],
                   'generic_gcd_hex':[hex(x) for x in generic],
                   'exceptional_gcd_hex':[hex(x) for x in exceptional],
                   'scope':'Exact generic pseudo-remainder identities only. All removed leading coefficients and contents are retained; no exceptional-parameter, special-fibre, nodality or full-monodromy conclusion.'})
except Exception:
    answer.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0)
    answer['actual_utc']=datetime.now(timezone.utc).isoformat()
    answer['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP27_eleven_primitive_elimination.json').write_text(json.dumps(answer,indent=2)+'\n')
    print(json.dumps({k:answer[k] for k in ['status','actual_utc','runtime_seconds']},indent=2))
