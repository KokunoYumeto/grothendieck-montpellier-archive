"""Small exact certificates independent of the cone-search recursion.
Uses standard-T multiplication followed by triangular dual-KL conversion.
"""
import pathlib,sys,itertools,json
out=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(out/'dependencies'))
import e4lib as L
import consult_a157422a_dimension_ring_verify as V
rows=[]
for d in range(5):
 count=0
 for w in itertools.product((1,2,3),repeat=d):
  co=L.dualcoords(L.word_elt(w))
  assert all(c>=0 for p in co.values() for c in p.values()),w
  count+=1
 rows.append({'length':d,'all_words_verified_positive':count})
w=(1,2,1,3,2);co=L.dualcoords(L.word_elt(w))
neg={''.join(str(x+1) for x in a)+','+''.join(str(x+1) for x in b):p for (a,b),p in co.items() if any(c<0 for c in p.values())}
expected={4:-2,2:16,0:36,-2:16,-4:-2}
expected2={3:-4,1:20,-1:20,-3:-4}
assert neg=={'2431,2314':expected,'2314,2431':expected,'3421,2314':expected2,'2314,3421':expected2},neg
repair=L.word_elt(w)
for donor in ((1,2,3,2,3),(1,2,1,3,2,3)):
 repair=L.tadd(repair,L.word_elt(donor))
assert all(c>=0 for p in L.dualcoords(repair).values() for c in p.values())
_,table=V.table(V.TRUE)
e='g2_12';square={z:int(c.subs(V.Dsym,0)) for (a,b,z),c in table.items() if a==b==e and c.subs(V.Dsym,0)}
assert square=={e:16}
assert table['mu',e,e]==1
res={'short_word_checks':rows,'first_negative_word':w,'negative_coordinates':neg,'positive_repair_words':[w,(1,2,3,2,3),(1,2,1,3,2,3)],'sign_point_e_square':square,'unit_constant':1,'scope':'Exact polynomial identities plus exhaustive all-word positivity through length four.'}
(out/'local_obstructions_verified.json').write_text(json.dumps(res,indent=2))
print('PASS all 121 words through length four, length-five coordinate obstruction and repair, and sign-point square.')
