#!/usr/bin/env python3
"""Exploratory floating evaluation only; not a theorem or certificate.

Tests the proposed selfdual rank-three quotient row against the full DO125
normalization, using the already certified K120 positive rational moments.
The quotient geometry and universal theta interface require separate proof.
"""
import json, math
from pathlib import Path
from datetime import datetime, timezone

P = Path(__file__).resolve().parent
W = P.parents[1]
f = 168
host = next(r for r in json.loads((W/'agents/definite_oscillator_large_t_certificate.json').read_text())['rows'] if r['host']=='J56')
T, g0, g1 = (int(host[k]) for k in ['T','g0','g1'])
Q = g0*g1
U = 77*Q*Q-14
D0 = 7**140*29**144*5**84*13**84
R = 17424/133
theta = 2**-20
qlo, qhi = 251124964, 251124965
log = math.log2
lfac = lambda n: math.lgamma(n+1)/math.log(2)
lc = lambda n,k: log(math.comb(n,k))
logDvar = (log(334**2*400/399*97*2113**2/(64*2049))-log(100*2**955-97))
vartheta = 334-log(334)-lc(334,167)
G1 = 1+166+lfac(82)+lfac(83)-lfac(166)
coarea = log(23479/23450)+2-log(527)/2
logDp = 333/2*log(1480/1653)+1557/80/math.log(2)+log(1670/1757)/2
cn = log(168)+lc(336,168)-336
M15 = log(6015684926187167549292201834533348561577984)-log(2618017117694612446410293519)
K = log(336)+M15-cn+f*log(7841/5000)+lfac(168)+f*(2*log(365729/500)-log(f)-2*log(314159/100000))
cn3 = log(504)+lc(1008,504)-1008
K3 = 1+2*log(1008)-cn3+504+lfac(504)+504*(2*log(365729/500)-log(f)-2*log(314159/100000))

table = json.loads((W/'recovery_pending/kummer/narrow_selected_band_shifted_gamma_moments_certificate.json').read_text())
r1=table['moments'][0]['pi_coefficient']
anchors={1:log(355/113)+log(int(r1['numerator']))-log(int(r1['denominator']))}
for name in ['selfdual_isotropic_quotient_support_twenty_seven_certificate.json','quotient_remaining_moments_probe.json']:
 for row in json.loads((P/name).read_text())['moment_enclosures']:
  anchors[row['j']]=log(int(row['upper']['numerator']))-log(int(row['upper']['denominator']))
def ml(j):
 if j in anchors:return anchors[j]
 a=max(a for a in anchors if a<j);b=min(a for a in anchors if a>j)
 return ((b-j)*anchors[a]+(j-a)*anchors[b])/(b-a)
def logadd(vals):
 m=max(vals);return m+log(sum(2**(v-m) for v in vals))
rows=[]
for X in [2111,2120,2140,2160,2165,2170,2200]:
 lq=log(R)-log(U)+(54*log(T)-334*log(Q)-X)/f
 common=(1+3/1024+lc(168,27)+log(164)+f/2*logDvar+f*(vartheta+G1+coarea+logDp)
         -(f+log(D0))/2+335*f/2*log(R/U)+8931*log(T)-336*167*log(Q)
         -337*X/2-335*f/2*lq-f*log(U))
 for k in range(160,165):
  d=k+3;pref=common+lc(164,k)+d*f*log(355/113)-d*log(D0)
  terms=[]
  for l in range(k+1):
   for transverse in ['main','correction']:
    j=l+3 if transverse=='main' else l
    coeff=lc(k,l)+(k-l)*K+(K3 if transverse=='correction' else 0)
    if j:
     val=coeff+j*f*(lq-log((1-theta)*R))+f*ml(j);ej=j
    else:
     val=coeff+f*(ml(1)+lq-log(theta*R*k));ej=1
    e=ej-167
    pat=334*(math.log1p(2**(e*log(g0)))+math.log1p(2**(e*log(g1))))/math.log(2)
    terms.append({'l':l,'kind':transverse,'j':j,'full_exponent':pref+val+pat})
  worst=max(terms,key=lambda r:r['full_exponent'])
  rows.append({'X':X,'k':k,'full_log2_diagnostic':logadd([r['full_exponent'] for r in terms]),'worst_term':worst})
result={'status':'FLOATING_DIAGNOSTIC_ONLY_EXACT_MOMENT_INPUTS_NO_THEOREM','completed_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,
 'new_local_identity':'Green <=2 Q^(-335*167) (NEJ)^167 NFJ0; central NFJ0 cancels; exact pattern product prod(1+qv^(j-167))^2',
 'scope':'High denominator screening for remaining k160..164. All two-term transverse terms retained; j167 has exact2^668 pattern. No new charge.'}
(P/'quotient_remaining_exact_pattern_float_probe.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
