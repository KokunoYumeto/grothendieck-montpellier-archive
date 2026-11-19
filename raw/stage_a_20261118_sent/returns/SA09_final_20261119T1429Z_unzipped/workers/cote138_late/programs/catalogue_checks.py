"""Manually transcribed passport/group assertions in scans115–116, checked
against the complete finite permutation enumeration. No grouping of note
verdicts or palaeographic selection is automated.
"""
from pathlib import Path
import json,math,itertools,collections
W=Path(__file__).resolve().parents[1]
ms=json.loads((W/'outputs/finite_maps_all.json').read_text())
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def conj(h,a):return mul(mul(h,a),inv(h))
def order(a):
 e=tuple(range(len(a)));b=a;k=1
 while b!=e:b=mul(b,a);k+=1
 return k
def full_type(m):
 r=tuple(a-1 for a in m['r']);s=tuple(a-1 for a in m['sigma']);ri=inv(r);dist=collections.Counter()
 for h in itertools.permutations(range(len(r))):
  if conj(h,s)!=s:continue
  if conj(h,r)==r:dist[order(h)]+=1
  if conj(h,r)==ri:dist[math.lcm(order(h),2)]+=1
 return dict(sorted(dist.items()))
for m in ms:m['full_group_element_orders']=full_type(m)
assert all(m['pinned_kernel_order']==1 for m in ms)
# Nomenclature D_n means a dihedral group of order2n.
rows=[]
def a(scan,line,p,group):rows.append({'scan':scan,'line':line,'passport':[list(v) for v in p],'source_group':group})
a(115,881,[(1,),(1,),(1,)],'C2')
for li,p in [(888,[(2,),(1,1),(2,)]),(892,[(1,1),(2,),(2,)]),(896,[(2,),(2,),(1,1)])]:a(115,li,p,'V4')
a(115,904,[(3,),(1,1,1),(3,)],'S3')
a(115,908,[(3,),(2,1),(2,1)],'C2');a(115,912,[(2,1),(2,1),(3,)],'C2')
for li,p,grp in [
(920,[(3,1),(2,1,1),(4,)],'C2'),(924,[(4,),(2,1,1),(3,1)],'C2'),
(928,[(2,2),(2,1,1),(4,)],'V4'),(932,[(4,),(2,1,1),(2,2)],'V4'),
(940,[(4,),(1,1,1,1),(4,)],'D4'),(944,[(2,1,1),(2,2),(4,)],'V4'),
(948,[(4,),(2,2),(2,1,1)],'V4'),(955,[(2,2),(2,2),(2,2)],'D4'),
(959,[(3,1),(2,2),(3,1)],'C2'),
(966,[(5,),(1,1,1,1,1),(5,)],'D5'),(970,[(4,1),(2,1,1,1),(5,)],'C2'),
(974,[(5,),(2,1,1,1),(4,1)],'C2'),(982,[(5,),(2,1,1,1),(3,2)],'C2'),
(986,[(3,2),(2,1,1,1),(5,)],'C2'),(990,[(5,),(2,2,1),(2,2,1)],'C2'),
(994,[(2,2,1),(2,2,1),(5,)],'C2')]:a(115,li,p,grp)
for li,p,grp in [
(1005,[(5,),(2,2,1),(3,1,1)],'C2'),(1009,[(3,1,1),(2,2,1),(5,)],'C2'),
(1013,[(4,1),(2,2,1),(3,2)],'C2'),(1017,[(3,2),(2,2,1),(4,1)],'C2'),
(1025,[(3,2),(2,2,1),(3,2)],'C2'),(1029,[(4,1),(2,2,1),(4,1)],'1')]:a(116,li,p,grp)
signatures={'1':{1:1},'C2':{1:1,2:1},'V4':{1:1,2:3},'S3':{1:1,2:3,3:2},'D4':{1:1,2:5,4:2},'D5':{1:1,2:5,5:4}}
for row in rows:
 matches=[m for m in ms if m['passport']==row['passport']]
 row['number_oriented_classes']=len(matches)
 row['observed_full_group_order_distributions']=[m['full_group_element_orders'] for m in matches]
 row['result']='all matching classes have stated group' if matches and all(m['full_group_element_orders']==signatures[row['source_group']] for m in matches) else 'MISMATCH'
n6bouquets=[m for m in ms if m['passport'][0]==[6] and m['passport'][1]==[2,2,2]]
out={'claims_checked':len(rows),'rows':rows,'degree6_three_loop_bouquets':n6bouquets,'new_reading_alarm':{'scan':119,'line':1091,'scope':'shift(6.5,-1.3)','source_group':'C2','interpretation':'one vertex and three nested noncrossing loops','possible_full_symmetry_orders':[m['full_aut_order'] for m in n6bouquets],'conclusion':'Order2 is incompatible with either genus-zero three-loop bouquet. Nested ribbon type has V4; scan must decide the drawing and label.'},'all_77_sphere_classes_have_trivial_cell_pinning_kernel':True}
(W/'outputs/catalogue_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checked':len(rows),'mismatches':[x for x in rows if x['result']=='MISMATCH'],'new_alarm':out['new_reading_alarm']},ensure_ascii=False,indent=2))
