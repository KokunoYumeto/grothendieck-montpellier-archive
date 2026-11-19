"""Exploratory exact degree6 tangent calculation: the new three-handle block.

This program makes no arithmetic-image or universal-quotient inference.
"""
from functools import lru_cache
from time import perf_counter
from pathlib import Path
import json

started=perf_counter()
source=Path('/workspace/scratch/f6dbb6638732/output/RESEARCH_SA07/code/check_genus_two_tangent_space.py').read_text()
namespace={}
exec(source[:source.index('six, eight =')],namespace)
add,scale,bracket,standard,lyndon,pivot_minor,determinant_mod=[namespace[x] for x in
 ['add','scale','bracket','standard','lyndon','pivot_minor','determinant_mod']]
alphabet='abcdef'

def words(degrees,prefix=''):
    if not any(degrees):
        yield prefix
    else:
        for i,n in enumerate(degrees):
            if n:
                ds=list(degrees);ds[i]-=1
                yield from words(tuple(ds),prefix+alphabet[i])

def basis(degrees):
    return [w for w in words(degrees) if lyndon(w)]

n=(2,1,1)
degrees=tuple(x for count in n for x in (count,count))
rows=basis(degrees)
letters={x:{x:1} for x in alphabet}
labels=[];polys=[]
for i,x in enumerate(alphabet):
    deg=list(n);deg[i//2]-=1
    ds=tuple(v for v in deg for _ in range(2))
    for word in basis(ds):
        image=bracket(standard(word),letters[x])
        y=alphabet[i^1]
        polynomial=bracket(image,letters[y]) if i%2==0 else bracket(letters[y],image)
        labels.append((x,word));polys.append(polynomial)
matrix=[[p.get(w,0) for p in polys] for w in rows]
print('BLOCK',n,'SHAPE',len(rows),len(labels))
pr,pc=pivot_minor(matrix,101)
det=determinant_mod([[matrix[i][j] for j in pc] for i in pr],101)
print('RANK_MOD101',len(pr),'NULLITY_UPPER_OVER_Q',len(labels)-len(pr),'MINOR',det)
z=[bracket(letters[alphabet[2*i]],letters[alphabet[2*i+1]]) for i in range(3)]
x,y,z3=z
A=[add(bracket(y,bracket(x,z3)),bracket(z3,bracket(x,y))),
   scale(bracket(x,bracket(x,z3)),-1),scale(bracket(x,bracket(x,y)),-1)]
special={}
for ai,zi in zip(A,z): special=add(special,bracket(ai,zi))
assert not special
images={letter:bracket(A[i//2],letters[letter]) for i,letter in enumerate(alphabet)}
assert all(images.values())
print('EXACT_KERNEL: A1=[z2,[z1,z3]]+[z3,[z1,z2]], A2=-[z1,[z1,z3]], A3=-[z1,[z1,z2]]; both generators of each handle share Ai.')
assert len(pr)==359 and len(labels)==360 and det
print('PASS: the new block has rational nullity exactly1; three permutations and the three two-handle blocks give total dimension6.')

# A concrete map out of the proper-surface Lie quotient detects a two-handle
# tangent derivation that vanished after filling in genus2.
v={c:{c:1} for c in 'xyz'}
sub={'a':v['x'],'b':v['y'],'c':v['x'],'d':v['z'],
     'e':v['x'],'f':scale(add(v['y'],v['z']),-1)}
zs=[bracket(sub[alphabet[2*i]],sub[alphabet[2*i+1]]) for i in range(3)]
assert not add(add(zs[0],zs[1]),zs[2])
detect=bracket(bracket(zs[1],bracket(zs[0],zs[1])),sub['a'])
assert detect
print('PROPER_QUOTIENT_DETECTOR: a,c,e map to x; b maps to y; d maps to z; f maps to -y-z. The surface relation maps to0.')
print('D12(a) NONZERO_WORD',min(detect),'COEFFICIENT',detect[min(detect)])
print('LIMIT: no nonzero q6 value, universal-image membership, or arithmetic normalizer is inferred.')
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-started,'.9f'))
