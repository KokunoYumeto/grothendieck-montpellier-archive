#!/usr/bin/env python3
"""Exact base-curve counts for A09, using only Python's standard library."""
import json
from pathlib import Path

def mul(a,b):
    result=0
    while b:
        if b&1:result^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return result

def pow4(a,n):
    result=1
    while n:
        if n&1:result=mul(result,a)
        a=mul(a,a);n//=2
    return result

records=[]
for q in [2,4]:
    points=[]
    for x in range(q):
        for y in range(q):
            lhs=mul(y,y)^mul(mul(x,x),y)
            rhs=pow4(x,5)^x
            if lhs==rhs:points.append([x,y])
    records.append({'q':q,'affine_points':points,'point_at_infinity_count':1,'count':len(points)+1})
assert [r['count'] for r in records]==[4,4]
a1=2+1-records[0]['count']
a2=(records[1]['count']-4-1+a1*a1)//2
assert (a1,a2)==(-1,0)
charpoly=[1,-a1,a2,-2*a1,4]
jacobian_F2_order=sum(charpoly)
assert charpoly==[1,1,0,2,4] and jacobian_F2_order==8
result={'status':'PASS','field_F4':'F2[z]/(z²+z+1)','counts':records,'frobenius_polynomial_descending':charpoly,'Jacobian_F2_order':jacobian_F2_order,'meaning':'All four F2 points have the same prime-to-2 abelian Kummer class; A09/A11 separate their full point sections.'}
Path(__file__).with_name('base_counts_result.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,indent=2,ensure_ascii=False))
