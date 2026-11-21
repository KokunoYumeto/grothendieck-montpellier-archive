#!/usr/bin/env python3
"""Exact braid verification of the marked orbital coface table, D23.C16.
The geometry determining these crossing words is proved separately.
"""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE.parent/'five_level_six'))
from cyclic12_cover import braid,wi,red
p=HERE/'records/orbit_coface_artin_simplifications.json'
data=json.loads(p.read_text());z4=(1,2,3)*4

def power(w,k):return tuple(w)*k if k>=0 else tuple(wi(w))*(-k)
for row in data['rows']:
 a=tuple(row['common_conjugator']);w=a+tuple(row['raw_discovered_word'])+wi(a)
 t=tuple(row['target_word']);k=row['global_full_twist_exponent']
 assert braid(w+power(z4,-k))==braid(t),(row['face'],row['generator'])
x=(1,1);y=(2,2);K=(3,3);V=(2,3)*3;Z=(1,2)*3;delta=(1,2)
def comm(u,v):return u+v+wi(u)+wi(v)
assert braid((delta+K)*3)==braid(z4)
for u,v in [(x,K),(K,V),(Z,x),(Z,y)]:assert braid(comm(u,v))==braid(())
assert braid(delta+x+wi(delta))==braid(y)
assert braid(delta*2+x+wi(delta)*2)==braid(Z+wi(x+y))
assert len(data['rows'])==16
out={'statement':'D23.C16','literal_crossing_word_identities':16,'all_target_commutators':True,'periodic_deltaK_cube_fulltwist':True,'pure_cluster_rotation_identities':True,'scope':'Exact Artin word checks; geometric path marking supplied by the coface proof','result':'PASS'}
(HERE/'records/orbit_coface_exact_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
