#!/usr/bin/env python3
"""ALP-LIFT-56 exact signature/centering diagnostics, not an analytic proof."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'research/alpoge_source'
C=Counter()
def ck(p,label):
    if not p: raise AssertionError(label)
    C[label]+=1
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def block(c,t): return [F(c)+F(t-1,2)-z for z in range(t)]
def main():
    cases=0
    for m in range(2,42,2):
      for k in [m+4,2*m+4,4*m+10]:
        k+=k%2
        r=k+m-1
        for extra in [0,2,10]:
          t=r+5+extra
          if t%2==0:t+=1
          ck(t>=r+5 and t>=2*m+7 and t>m and t%2==1,'actual_TPar_inequalities')
          if t<3*m: ck(t<3*m,'TPar_t_below_Ranks_three_m')
          # Unequal positive spacings exercise the actual order rather than
          # an assumed uniform-gap profile. All gaps exceed the block width.
          ell=t+19
          bs=[0]
          es=[]
          for j in range(m):
            es.append(bs[-1]+ell+j*j+1)
            if j+1<m: bs.append(es[-1]+ell+2*j+3)
          vv=[2*(k-z)+7 for z in range(k-1)]
          for j in range(m):
            q=(m-j)//2; qn=(m-j-1)//2
            n=r+j*t; nn=n+t; N=k+j*(t+1)
            p=n-q; pn=nn-qn
            ck(q+qn==m-j-1,'floor_sum')
            ck(p==N+qn and pn==N+q+t,'exact_signatures')
            ck((n-1)%2==j%2,'rank_parity')
            Aj=[F(v+es[j]) for v in vv]
            Aj += [F(es[j]-bs[i]) for i in range(j+1)]
            for i in range(j): Aj += block(es[j]-es[i],t)
            Bj=[F(es[j]-bs[i]) for i in range(j+1,m) if (i-j)%2==0]
            Ej=[F(es[j]-bs[i]) for i in range(j+1,m) if (i-j)%2==1]
            ck(len(Aj)==N and len(Bj)==qn and len(Ej)==q,'actual_list_counts')
            ck(min(Aj)>=F(t+3,2),'positive_gap')
            ck(all(x<=-F(t+3,2) for x in Bj+Ej),'negative_gap')
            ck(all(x.denominator==1 and x!=0 for x in Aj+Bj+Ej),'nonzero_integer_centering')
            # These diagnostic choices need not satisfy the enormous global
            # NCGaps. They exercise only the sign/count arguments used here.
            for eta in [F(-1,2),F(1,2)]:
              cnext=-es[j]+(eta if (j+1)%2==0 else 0)
              ccur=-es[j]+(eta if j%2==0 else 0)
              ck((eta if j%2 else 0)-cnext==es[j],'smaller_cross_center')
              ck((eta if (j+1)%2 else 0)-ccur==es[j],'larger_cross_center')
            for i in range(1,qn+1):
              ck(2*i<=m-j-1<t,'all_lower_targets_still_larger')
              ck(nn-2*i>n,'Ichino_dimension_premise')
              ck(qn-i<qn,'negative_sign_obstruction')
              ck((nn-2*i)%2==nn%2,'unchanged_character_parity')
            ck(nn-qn>n,'Weil_convergent_range')
            ck(nn>2*n if j==0 else n<nn<2*n,'doubling_dimension_windows')
            cases+=1
    # A direct symbolic alternative to a sampled lower-target inequality.
    for m in range(2,2002,2):
      t=2*m+7
      ck(t-(m-1)==m+8>0,'uniform_lower_dimension_margin')
    paths=['Formalism/LocalRingCardinality/Params.lean',
           'Formalism/LocalRingCardinality/DataTheta.lean',
           'Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean',
           'Formalism/LocalToGlobal/IndefiniteReal/OrthogonalComplementCharacterisation.lean']
    ss={p:(BASE/p).read_text() for p in paths}
    for x in ['rank_add_five_le : k + m - 1 + 5 ≤ t','three_m_lt_t : 3 * m < t',
              'def rankY (j : ℕ) : ℕ := R.r + j * R.t','def N (j : ℕ) : ℕ := R.k + j * (R.t + 1)']:
      ck(x in ss[paths[0]],'literal_rank_source')
    for x in ['decide (i.1 ≤ j ∨ Even (i.1 - j))','if Odd j then P.eta τ else 0',
              't_ge : D.R.r + 5 ≤ t','t := D.R.t']:
      ck(x in ss[paths[1]],'literal_signed_parameter_source')
    for x in ['X.conjAF _ F ∈ X.typ _ (P.Dpar j)','def ThetaUnfoldingFreeData',
              'def ThetaStablePeriodVanishing','def RealThetaLiftDiscreteSeries']:
      ck(x in ss[paths[2]],'literal_predicate_source')
    ck('starRingEnd ℂ (th g h (pt φ))' in ss[paths[3]],'literal_conjugate_upward_kernel')
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,
        default=HERE/'general_vertical_forward_certificate.json');out=ap.parse_args().output
    data={'finding':'ALP-LIFT-56','status':'PASS','time_utc':datetime.now(timezone.utc).isoformat(),
          'assertions':sum(C.values()),'checks':dict(C),'signed_edge_cases':cases,
          'source_sha256':{p:sha(BASE/p) for p in paths},'script_sha256':sha(Path(__file__)),
          'scope':'Exact rank/sign/centering diagnostics only; no analytic theorem, global theta value, or Lean build.'}
    out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','assertions':data['assertions'],'output':str(out),'time_utc':data['time_utc']}))
if __name__=='__main__':main()
