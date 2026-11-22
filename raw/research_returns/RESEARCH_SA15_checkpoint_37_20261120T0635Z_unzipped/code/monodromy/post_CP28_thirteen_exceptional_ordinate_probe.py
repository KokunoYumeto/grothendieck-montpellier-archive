"""Finite algebraic probe of full residual divisors at mu^5=1.

All roots are searched in one specified finite field.  Exhaustion of the
geometric locus is not asserted.  Any displayed packet is an exact witness.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback,signal
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx
start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','packets':[]}
def timeout(*unused):raise TimeoutError('Finite residual-divisor probe exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    K=fq_default_ctx(2,24,'c');R=fq_default_poly_ctx(K);X=R.gen()
    z=(X**3+X*X+1).roots()[0][0]
    a=z*z;delta=z+1;b=a+z+1;e=1/(delta*delta)
    beta=(X*X+X+delta).roots()[0][0]
    A=R([a,a+1,0,a*a+1,0,0,0,a*a]);aroots=A.roots()
    out.update({'field':str(K),'z':str(z),'beta':str(beta),'A_roots_found':len(aroots),'rows':[]})
    for L,_ in aroots:
        H=a*a*L**6+(a*a+1)*L*L+(a+1);J=a*a*L**4+(a*a+1)
        j=a*L+delta**2;k=delta**4
        b2=J*e**2+a*a*e**4*j*j;b1=1+H*e+a*a*e**4*k
        T=b1**3+j*j*b1*b2*b2+k*b2**3
        if T != K(0):continue
        croots=(X**3+j*X*X+k).roots()
        Bvalues={}
        for Z,_ in croots:Bvalues.setdefault(str(b2*Z*Z+b1*Z),[]).append(Z)
        row={'L':str(L),'C_roots_found':len(croots),'B_multiplicities':[len(v) for v in Bvalues.values()],'U_root_counts':[]}
        for Zs in Bvalues.values():
            if len(Zs)<2:continue
            Bv=b2*Zs[0]*Zs[0]+b1*Zs[0]
            uroots=(a*a*X**4+J*X*X+H*X+beta+delta+a*a*e**4*j*k+Bv).roots()
            row['U_root_counts'].append(len(uroots))
            for U,_ in uroots:
                M=U+delta/a+e*j;packets={}
                for Z in Zs:
                    proots=(X*X+L*X+U+e*Z).roots()
                    for p,_ in proots:
                        d1=a*p**4+b*p*p;d2=d1*d1+b*p
                        G=z*p*p+delta*p+beta;F=G+d1
                        assert Z==delta+F+d2
                        A1=delta*d1;A2=Z*d1+delta*d2;A3=Z*(F+delta)+delta*delta
                        Kap=delta/a+delta*delta/(Z*Z)
                        n1=A1+L*A2+(L*L+Kap)*A3;n0=Kap*A2+L*Kap*A3
                        det=delta*delta+Z*delta*L+Z*Z*Kap
                        assert det != K(0),'The chosen finite sector contains an unresolved ordinate denominator.'
                        nu=(Z*n0+delta*n1)/det
                        eta=(n1+nu*(Z*L+delta))/Z
                        yroots=(X*X+X+a*p**5+b*p**3).roots()
                        for y,_ in yroots:
                            const=eta+nu*p+y
                            key=(str(nu),str(const))
                            # Exact Mumford remainder identity.
                            q=R.gen();u=q*q+L*q+M;v=nu*q+const
                            assert not ((v*v+v+a*q**5+b*q**3)%u)
                            packets.setdefault(key,[]).append({'p':str(p),'y':str(y),'Z':str(Z)})
                for (nu,const),pts in packets.items():
                    if len(pts)>=3:
                        out['packets'].append({'L':str(L),'M':str(M),'nu':nu,'constant':const,'points':pts})
        out['rows'].append(row)
    out['status']='PASS_FINITE_PACKET_PROBE_ONLY'
    out['scope']='Finite field root search and exact divisor remainders only. No universal norm-thirteen or geometric exhaustion assertion.'
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_exceptional_ordinate_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'actual_utc':out['actual_utc'],'runtime_seconds':out['runtime_seconds'],
                      'packet_count':len(out['packets']),'row_count':len(out.get('rows',[])),
                      'traceback':out.get('traceback')},indent=2))
