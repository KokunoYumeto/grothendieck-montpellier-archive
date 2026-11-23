#!/usr/bin/env python3
"""Exploratory float-only all-phase triangle screen. Not a continuum proof or sector bound."""
import numpy as np, json, math
from scipy.special import betainc, betaln, gammaln
from pathlib import Path
from datetime import datetime, timezone
P=Path(__file__).resolve().parent
phase_grid=np.linspace(-1.,1.,401)
def triangle(t,w,y,yp,eta):
 A=t/2;v=math.sqrt(t);d=1+A+1j*w;c=abs(d);s2=c*c-1;s=math.sqrt(s2);D=math.sqrt(y/yp);R2=1-y
 Sm=R2-(c-D)**2/s2
 if Sm<=0:return None
 L2=4*D*c/s2
 h=phase_grid*math.sqrt((1-eta)*Sm/L2)
 rho=D*d/c*((1-2*h*h)+2j*h*np.sqrt(1-h*h))
 z1=(rho-d)*(-A+1j*w)/s2;z2=(rho-d)*(-v)/s2
 e1=v/s;e2=(-A-1j*w)/s
 n0=R2+z1.conjugate()*(rho-1)-v*(1-z1)*z2.conjugate()
 lc=v*e1*z2.conjugate();mc=e1*(rho-1)-v*(1-z1)*e2.conjugate();qc=v*e1*e2.conjugate()
 rr=np.sqrt(np.maximum(0,(1-eta)*Sm*(1-phase_grid**2)))
 vals=(abs(n0)+(abs(lc)+abs(mc))*rr+abs(qc)*rr**2)/math.sqrt(R2*(D*D-y))
 ix=int(vals.argmax());return float(vals[ix]),float(phase_grid[ix]),Sm
bands=[16/529,1/33,16/527]
rects=[(6,32,4,.95),(6,40,4,.95),(6,48,4,.95),(4,40,5,.97),(6,40,5,.97),(8,40,4,.95),(8,40,3,.93),(8,32,2,.9)]
rows=[]
for lo,hi,wm,eta in rects:
 best=(-1,None)
 for t in np.linspace(lo,hi,69):
  for w in np.linspace(0,wm,41):
   for y in bands:
    for yp in bands:
     val=triangle(float(t),float(w),y,yp,eta)
     if val is not None and val[0]>best[0]:best=(val[0],[float(t),float(w),y,yp,val[1]])
 tail=math.sqrt(2)*(1-betainc(1.5,166,1-eta))
 # Concavity upper bound for the one-variable beta tail.
 upper=math.sqrt(2)*eta**166/(166*math.exp(betaln(1.5,166)))*(math.sqrt(1-eta)+eta/(334*math.sqrt(1-eta)))
 rows.append({'t':[lo,hi],'abs_w_max':wm,'eta':eta,'sampled_triangle_max':best[0],'sampled_argmax':best[1],'conditional_beta_factor_float':tail,'conditional_beta_upper_float':upper,'upper_log2':math.log2(upper)})
 print(rows[-1],flush=True)
# Exact strengthened selected overlap comparison, independent of the float screen.
a=2*pow(637163,160000)*pow(100,309998)
b=pow(625000,160000)*pow(101,309998)
assert a<b
result={'status':'FLOATING_SCREEN_ONLY_NOT_SECTOR_BOUND','completed_utc':datetime.now(timezone.utc).isoformat(),'grid':'69 t x41 w x9 band pairs x401 normalized phases; no continuum coverage is claimed','rows':rows,'exact_overlap_integer_power':True,'exact_overlap_scope':'Only the stated integer power; full weight and singular-value interfaces remain separately required.'}
(P/'coherence_positive_majorant_probe.json').write_text(json.dumps(result,indent=2)+'\n')
print('saved',str(P/'coherence_positive_majorant_probe.json'),flush=True)
