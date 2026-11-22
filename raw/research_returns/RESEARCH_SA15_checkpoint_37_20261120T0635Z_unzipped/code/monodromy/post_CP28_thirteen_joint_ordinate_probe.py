"""Exploratory simultaneous A=0, slope-change=0, repeated-value sector."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_mpoly_ctx,nmod_poly
start=time.perf_counter();agent=Path(__file__).resolve().parents[1];out={'status':'RUNNING'}
try:
    initial=json.loads((agent/'outputs/post_CP28_thirteen_parameter_probe.json').read_text())
    refined=json.loads((agent/'outputs/post_CP28_thirteen_ordinate_parameter_probe.json').read_text())
    ctx=nmod_mpoly_ctx.get(('L','z'),2,'lex')
    def decode(s):
        data={}
        for i,h in enumerate(s['numerator_L_coefficients_v_binary_hex']):
            v=int(h,16)
            while v:
                bit=v&-v;data[(i,bit.bit_length()-1)]=1;v^=bit
        return ctx.from_dict(data)
    def univariate(f):
        data=f.to_dict();assert all(i==0 for i,j in data)
        degree=max((int(j) for i,j in data),default=-1)
        return nmod_poly([int(data.get((0,j),0)) for j in range(degree+1)],2)
    enc=lambda f:hex(sum(int(c)<<i for i,c in enumerate(f.coeffs())))
    A=decode(initial['A']);D=decode(refined['slope_change']);T=decode(initial['T'])
    G=A.gcd(D);A1=A//G;D1=D//G
    Rjump=univariate(A1.resultant(D1,'L'))
    Rcommon=univariate(G.resultant(T,'L'))
    out.update({'status':'PASS_EXPLORATORY_JOINT_RESULTANT','gcd_A_slope':str(G),
                'A_quotient':str(A1),'slope_quotient':str(D1),
                'jump_resultant_hex':enc(Rjump),'common_resultant_hex':enc(Rcommon),
                'jump_factors':[(enc(f),int(n)) for f,n in Rjump.factor()[1]],
                'common_factors':[(enc(f),int(n)) for f,n in Rcommon.factor()[1]],
                'scope':'Exact algebra only. No asserted geometric conclusion.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_joint_ordinate_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
