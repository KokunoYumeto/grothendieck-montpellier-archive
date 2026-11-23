#!/usr/bin/env python3
"""ALP-LIFT-55 exact literal-size elimination diagnostics."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'research/alpoge_source'
C=Counter()
def ck(p,label):
    if not p: raise AssertionError(label)
    C[label]+=1
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ml=F(29,400);nl=F(799,100);kl=F(999,100);ku=F(1001,100)
    first=F(1,100)+2
    ck(5*F(1,2)+2==F(9,2),'main_exponent_cancellation')
    low=-5*ml+nl+first
    ck(low==F(3855,400),'lower_epsilon_exponent')
    ck(ku==F(4004,400),'upper_epsilon_exponent')
    ck(ku-low==F(149,400),'exact_L_elimination')
    mm=26-ml;ff=104+nl;kk=234+kl
    ck(mm==F(10371,400),'m_logL_coefficient')
    ck(ff==F(11199,100),'f_logL_coefficient')
    ck(kk==F(24399,100),'k_logL_coefficient')
    for coef,extra,want,bit in [(mm,0,F(10371,149),69),
                               (ff,1,F(44945,149),301),
                               (kk,0,F(97596,149),655)]:
        z=coef*F(400,149)+extra
        ck(z==want,'weak_elimination_exponent')
        ck(bit<z<bit+1,'weak_integer_bit_floor')
    ck(F(101,100)-1==F(1,100),'SizeG_division_exponent')
    ck(8**100==2**300,'strong_scale_exact_power')
    ck(300*mm==F(31113,4)>7778,'strong_m_exponent')
    ck(1+300*ff==33598,'strong_f_exponent')
    ck(300*kk==73197,'strong_k_exponent')
    ck(343<2**300,'unchanged_scale_excluded')
    ck(11388>7778,'retained_host_floor_remains_stronger')
    for k in range(6,134,2):
        ck(k>1 and k%2==0,'positive_log_rank')
    paths=['Formalism/SharpRestriction/ElevenLe.lean',
           'Formalism/LocalRingCardinality/DataParams₂.lean',
           'Formalism/LocalRingCardinality/Params.lean',
           'Formalism/SharpRestriction/ParConsts.lean']
    ss={p:(BASE/p).read_text() for p in paths}
    for s in ['L.sc.x ^ szTh L * (D.R.m : ℝ) ^ 5 * D.R.f * L.sc.L * L.sc.x ^ L.sc.eps ≤ D.R.k',
              '(D.R.k : ℝ) ≤ L.sc.x ^ (9 / 2 + 10 * L.sc.eps + szTh L)',
              '((D.R.k : ℝ) * L.sc.b) ^ 8 ≤ (D.host.g i : ℝ)',
              'Real.log (D.host.g i : ℝ) ≤ L.sc.x ^ szTh L * L.sc.L',
              'SizeBm L ∧ SizeXpp L ∧ SizeG L']:
        ck(s in ss[paths[0]],'literal_size_source')
    for s in ['eps_lt : eps < 1 / 52','def b : ℝ := Real.exp s.L','def L : ℝ := s.x ^ s.eps']:
        ck(s in ss[paths[1]],'literal_scale_source')
    ck('m_add_three_le_k : m + 3 ≤ k' in ss[paths[2]],'literal_positive_k')
    ck('sizes : ∀ x, x1 < x → ∀ i : Ix x, SizesAt (L x i)' in ss[paths[3]],'literal_family_quantifier')
    data={'finding':'ALP-LIFT-55','status':'PASS','time_utc':datetime.now(timezone.utc).isoformat(),
          'assertions':sum(C.values()),'checks':dict(C),
          'strong_bounds':{'L_log2_strict_lower':300,'m_log2_strict_lower':'31113/4',
                           'f_log2_strict_lower':33598,'k_log2_strict_lower':73197},
          'source_sha256':{p:sha(BASE/p) for p in paths},'script_sha256':sha(Path(__file__)),
          'scope':'Necessary inequalities only; no full source record, theta calculation, or DP44 sign.'}
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'universal_size_scale_certificate.json')
    out=ap.parse_args().output;out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','assertions':data['assertions'],'output':str(out),'time_utc':data['time_utc']}))
if __name__=='__main__':main()
