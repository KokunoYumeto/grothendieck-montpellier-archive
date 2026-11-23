#!/usr/bin/env python3
"""Fresh recovery diagnostics, not a replay of the lost DO069 script.
Exact rational phase/rank checks plus R053/K085 arithmetic.
This does not verify analytic theorems, source proofs, or a full error ledger.
All output must stay in the authorized recovery_pending/definite directory.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

ROOT = Path('/tmp/alpa66/work/recovery_pending/definite')
WORK = Path('/tmp/alpa66/work')
checks = []
def check(ok, name, **meta):
    if not ok:
        raise AssertionError((name, meta))
    checks.append({'name': name, 'pass': True, **meta})

class QI:
    __slots__ = ('r','i')
    def __init__(self, r=0, i=0):
        if isinstance(r,QI):
            self.r,self.i=r.r,r.i
        else:
            self.r,self.i=F(r),F(i)
    def __add__(self, other):
        o=QI(other); return QI(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return QI(-self.r,-self.i)
    def __sub__(self, other): return self+-QI(other)
    def __rsub__(self, other): return QI(other)+-self
    def __mul__(self, other):
        o=QI(other);return QI(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self, other):
        o=QI(other);q=o.r*o.r+o.i*o.i
        return self*QI(o.r/q,-o.i/q)
    def __eq__(self, other):
        o=QI(other);return self.r==o.r and self.i==o.i
    def conj(self):return QI(self.r,-self.i)
    def __repr__(self):return f"QI({self.r},{self.i})"
def trhalf(z):return QI(z).r

# Rank/parity and the earlier sigma=0 boundary.
rank_cases=0
for k in range(2,18,2):
 for m in range(2,20,2):
  for t in (3,7,13,21):
   for j in range(m):
    nj=k+m-1+j*t;Nj=k+j*(t+1);qj=(m-j)//2
    check(nj-2*qj>=Nj-1,'positive_core_rank',k=k,m=m,t=t,j=j)
    check(Nj%2==0,'compact_rank_even')
    check(nj%2==(1-j)%2,'vertical_rank_parity')
    if m-j>=2 and (m-j)%2==0:
      rho=(m-j-2)//2
      check(nj==Nj+2*rho+1,'BF_lower_rank')
      check(k+m-1+(j+1)*t==k+(j+1)*(t+1)+2*rho,'BF_upper_rank')
      check(j%2==0,'BF_actual_even_edge')
    elif m-j>=3:
      sigma=(m-j-3)//2
      check(nj==Nj+2*sigma+2,'FB_lower_rank')
      check(k+m-1+(j+1)*t==k+(j+1)*(t+1)+2*sigma+1,'FB_upper_rank')
      check(j%2==1,'FB_actual_odd_edge')
      if j==m-3:
       check(sigma==0 and qj==1,'earlier_FB_boundary_has_lower_rank_one')
    rank_cases+=1

# Exact rational Gaussian models for the full nonzero-coordinate phase.
phase_cases=0
for a in range(1,7):
 for ell in (-1,-2,-5):
  for seed in range(1,9):
   xi=QI(0,seed+1)
   c=QI(F(seed,3),F(2-seed,5))
   g=[F(i+2, i+1) for i in range(a)]
   av=[QI(F(seed+i+1,2),F(seed-2*i,3)) for i in range(a)]
   w=[QI(F(i+1,3),F(seed-i,4)) for i in range(a)]
   t=QI(F(seed+2,7),F(seed-3,5))
   pt=[-c.conj()*av[i].conj()*g[i] for i in range(a)]
   dw=[w[i].conj()*ell/g[i] for i in range(a)]
   dpt=[pt[i].conj()*ell/g[i] for i in range(a)]
   wo_pt=[-c*ell*av[i] for i in range(a)]
   cc=c*c.conj()
   cen_co=trhalf(xi*cc*ell*t)
   cen_s=trhalf(xi*cc*ell*t.conj())
   sym_row=trhalf(xi*sum((pt[i].conj()*ell*w[i]/g[i] for i in range(a)),QI()))
   sym_col=trhalf(xi*sum((dpt[i].conj()*g[i]*dw[i]/ell for i in range(a)),QI()))
   check(dpt==wo_pt,'D_ptS_equals_J_tPt',a=a,ell=ell,seed=seed)
   check(cen_s==-cen_co,'central_trace_conjugates_once')
   check(sym_row==-sym_col,'dagger_half_pairing_antisymplectic')
   check(cen_s+sym_row==-(cen_co+sym_col),'full_nonzero_coordinate_Jacobi_phase')
   translated=[(w[i]+pt[i]).conj()*ell/g[i] for i in range(a)]
   check(translated==[dw[i]+wo_pt[i] for i in range(a)],'full_translated_argument')
   kappa=[-z for z in dw]
   check([-z for z in kappa]==dw,'BF_core_parity_f_minus_z')
   tau=-xi;zp=c.conj();z=xi*zp
   check(tau*zp==-z,'actual_line_link_map')
   check(tau.conj()*ell*tau==(xi*xi.conj())*ell,'actual_line_link_norm')
   phase_cases+=1

# Generic flag normalisation preserves the final Heisenberg coefficient.
for rho in range(1,10):
 beta=[QI(F(i+2,3),F(i+1,5)) for i in range(rho-1)]
 scales=[QI(1) for _ in range(rho)]
 for i in range(rho-2,-1,-1):
  scales[i]=scales[i+1]/beta[i]
 for i in range(rho-1):
  check(scales[i+1]/scales[i]==beta[i],'generic_flag_ratio')
 check(scales[-1]==1,'last_frame_scalar_fixed')

# R053 exact rational-pi volume arithmetic.
f=168;m=164;s=11
D0=7**140*29**144*5**84*13**84
def pow2_lt(num,den,e):
    return num < (den<<e) if e>=0 else (num<<(-e)) < den
def pow2_gt(num,den,e):
    return num > (den<<e) if e>=0 else (num<<(-e)) > den
def volume_data(dim,C):
    h=f*dim
    return (528*C*C)**h,math.factorial(h)*D0**dim
table=[
(0,7,1248091,736324),(1,4,156091,571052),(2,1,19591,406064),
(3,-2,2529,243312),(4,-5,396,95909),(5,-8,130,7357),
(6,-11,96,-16746),(7,-14,92,-20129),(8,-17,92,-20129),
(9,-20,92,-20129),(10,-23,92,-20129),(11,-26,92,-20129)]
for t,b,C,vlog in table:
 check(b==math.ceil(F(2184-995*t,336)),'R053_exact_ceiling_b',t=t)
 check(C==math.ceil(F(91)+9750*(F(2)**b)),'R053_exact_radius_ceiling',t=t)
 num,den=volume_data(m,C)
 check(pow2_lt(num,den,vlog),'R053_volume_upper',t=t)
 check(pow2_gt(num,den,vlog-1),'R053_volume_lower',t=t)
check((8192**4+1)<2*5793**2*8192**2,'uniform_negative_column_radius')
check(325**21*7**35*29**36<1636**42,'full_rd_rank_five_cover')
num,den=volume_data(5,7429)
check(pow2_lt(num,den,14254) and pow2_gt(num,den,14253),'class_general_W0_volume_interval')
check(14254<14861,'retained_W0_bound_conservative')
cells=[];bad=[];good=[]
for i in range(12):
 for u in range(12-i):
  t=11-i-u;b=table[t][1];vlog=table[t][3]
  E4=-474429+4*vlog+4*1176*b-4*997*t-4*996*335*i
  item={'i':i,'u':u,'t':t,'E4':E4}
  cells.append(item)
  (good if E4<-4*4096 else bad).append(item)
check(len(cells)==78 and len(good)==72,'R053_complete_profile_enumeration')
check(max(x['E4'] for x in good)==-130265,'R053_maximum_passing_exponent')
old=F(-14033453,4)+10956*11+332665*10
check(old==F(-244789,4),'DO066_fresh_whole_cell')
check({(x['i'],x['u'],x['t']) for x in bad}==
 {(0,8,3),(0,9,2),(0,10,1),(0,11,0),(1,9,1),(1,10,0)},
 'R053_exception_set')
check(74<2**7 and F(-130265,4)<-32566 and old<-32566,'R053_union_charge_32559')

# K085 exact constants with rational pi upper envelope.
R=F(17424,133)
check(R**16<2**113,'K085_alpha_bound_power')
check(133**4+1<2*95**2*133**2,'K085_negative_column_radius')
check(2**168*D0<1500**168,'K085_full_root_discriminant')
check(D0*5**84<1636**168,'K085_full_root_discriminant_cover')
check(2**960+83-668*2**485>2**959,'K085_actual_selected_degree')
check(3**334<2**530,'K085_rank_pattern_bound')
num=(22*168*1731**2)**1512*2**168
den=7**1512*math.factorial(756)**2*D0**9
check(pow2_lt(num,den,19700),'K085_fibre_ceiling_9850')
check(pow2_gt(num,den,19698),'K085_fibre_9849_insufficient')
num=(22*168*376**2)**84*2**168
den=7**84*math.factorial(84)
check(pow2_lt(num,den,1945),'K085_gamma_ceiling_1945')
check(pow2_gt(num,den,1944),'K085_gamma_lower_interval')
E=(1+107+9850+1945+168+530+343*996*11+22
 +F(669*168,4)*F(113,16)-F(281,4)*335*167
 +168*(F(9,2)-F(959,4)))
check(E==F(-5481,8) and E<-685,'K085_final_exponent')
check(F(665,4)>0,'K085_monotone_gamma_exponent')

# Exact source-interface fingerprints. These are string presence checks,
# not verification of Lean theorem proofs.
sources=[
('research/alpoge_source/Formalism/LocalRingCardinality/DataTheta.lean',
 ['t_odd : Odd t','t_ge : D.R.r + 5 ≤ t']),
('research/alpoge_source/Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsThetaFam.lean',
 ['def Step.lift','liftS s.om s.vW.μ s.vW.𝓕 G Φ','vT : VolM D σ V₀.rank']),
('research/alpoge_source/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/TowerEx.lean',
 ['def UpBF','def UpFB','∃ Φ ∈ 𝒮, B.per ψ φ (s.lift G Φ) ≠ 0',
  '∃ Φ ∈ 𝒮, J.per ψ B.ζ omz φ (s.lift G Φ) Φ₀ ≠ 0']),
('research/alpoge_source/Formalism/LocalToGlobal/BesselHermitianTheta/TiedWeil.lean',
 ['om_swap :','th : ∀','(T.petC V : ℂ) * ∫ g in 𝓕']),
('research/alpoge_source/Formalism/LocalToGlobal/IndefiniteReal/OrthogonalComplementCharacterisation.lean',
 ['eq : ∀ F : CCs, ∀ φ v g,','liftInt ν 𝓕 th (pt φ)']),
]
source_records=[]
for name,needles in sources:
 p=WORK/name;raw=p.read_bytes();text=raw.decode()
 for needle in needles:check(needle in text,'source_interface_present',file=name,needle=needle)
 source_records.append({'file':name,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})

parser=argparse.ArgumentParser()
parser.add_argument('--output',default=str(ROOT/'recovery_exact_diagnostics.json'))
args=parser.parse_args()
out=Path(args.output).resolve()
if ROOT.resolve() not in out.parents:
 raise ValueError('Output outside authorized controlled recovery directory')
result={
 'status':'PASS',
 'at':datetime.now(timezone.utc).isoformat(),
 'kind':'fresh reconstructed Python diagnostic; not the lost original script replay',
 'assertions':len(checks),
 'rank_cases':rank_cases,
 'phase_cases':phase_cases,
 'R053':{'table':table,'profile_count':len(cells),'passed':len(good),'bad':bad,
         'old_cell':str(old),'charge':32559},
 'K085':{'exponent':str(E),'charge':685},
 'sources':source_records,
 'limitations':['No analytic theorem verified automatically','No Lean build or stipulated-proof audit',
               'No complete prior-error ledger replay','No automatic promotion of a reconstructed proof'],
 'checks':checks}
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','at','kind','assertions','rank_cases','phase_cases']},ensure_ascii=False))
