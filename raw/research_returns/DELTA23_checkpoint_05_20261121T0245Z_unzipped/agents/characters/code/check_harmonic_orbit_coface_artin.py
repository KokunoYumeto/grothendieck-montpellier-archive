#!/usr/bin/env python3
"""Exact Artin replay for D23.C18. Path geometry is a separate requirement."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE.parent/'five_level_six'))
from cyclic12_cover import braid,wi
data=json.loads((HERE/'records/harmonic_orbit_coface_artin_simplifications.json').read_text())
a=(1,);b=(2,);c=(3,);x=a*2;y=b*2;K=c*2
Z=(a+b)*3;V=(b+c)*3;s=a+b+a;r=a+b;z4=(a+b+c)*4
def power(w,k):return w*k if k>=0 else wi(w)*(-k)
def comm(u,v):return u+v+wi(u)+wi(v)
for row in data['rows']:
    raw=tuple(row['raw_discovered_word'])
    target=tuple(row['target_word'])+power(z4,row['global_full_twist_exponent'])
    assert braid(raw)==braid(target),(row['face'],row['generator'])
assert len(data['rows'])==13
assert braid(s*2)==braid(Z)
assert braid(s+x+wi(s))==braid(y)
assert braid((s+c)*3)==braid(z4)
for u,v in [(x,c),(V,c),(Z,x),(Z,y),(Z,s)]:
    assert braid(comm(u,v))==braid(())
P=(a+b+c)*2
assert braid(P+s+c+wi(P))==braid(r+K)
out={'statement':'D23.C18','literal_crossing_word_identities':13,
     'half_rotation_square':True,'half_rotation_swaps_x_y':True,
     'periodic_sc_cube_fulltwist':True,'shared_periodic_conjugator':list(P),
     'all_required_commutators':True,
     'scope':'Exact Artin algebra; geometric path determination separate','result':'PASS'}
(HERE/'records/harmonic_orbit_coface_exact_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
