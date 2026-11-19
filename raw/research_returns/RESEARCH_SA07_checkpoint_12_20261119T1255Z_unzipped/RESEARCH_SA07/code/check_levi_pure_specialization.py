#!/usr/bin/env python3
"""The exact source-to-input map for all complement genera s>=3.

MSS2015 arXiv:1404.3351v2, printed pp7 and25--27: all five source
chord vectors are literal inputs below. No source download is needed.
The raw detector signs are (+,-,+,-,-). The polynomial determinant,
its nonzero factors for s>=3, and the source theorem justify injectivity;
this computation makes no mixed-kernel or arithmetic vanishing claim.
"""
from pathlib import Path
from time import perf_counter
import runpy
import sympy as sp
started=perf_counter()
SOURCE_COLUMNS = [[18, -2, -16, -2, 2, 0, -16, 11, 5, 0, 5, -5, 16, -3, -13, -2, -1, 3, 2, 3, -5, 0, 0, 0, -2, -3, 5, 2, 1, -3, -16, 3, 13, 11, 0, -11, 5, -5, 0, -3, -8, 11, -2, -3, 5, 0, -5, 5, 5, 0, -5, -5, 0, 5, 5, -5, 0, 0, 0, 0, 16, -11, -5, -3, 0, 3, -13, 5, 8, 11, 0, -11, 2, 3, -5, 2, -2, 0, 1, -3, 2, -3, 0, 3, 5, 0, -5, -2, -1, 3, -18, 2, 16, 2, -2, 0, 16, -11, -5, 0, -5, 5, -16, 3, 13], [16, 4, -7, 4, -4, 0, -7, -8, -3, 0, -3, -4, 7, 3, 2, 4, -2, -3, -4, -6, 3, 0, 0, 0, 4, 6, -3, -4, 2, 3, -7, -3, -2, -8, 0, 8, -3, 2, 0, 6, 8, -8, 4, 6, -3, 0, 3, 4, -3, 0, 3, -4, 0, -2, -3, 2, 0, 0, 0, 0, 7, 8, 3, 3, 0, -6, 2, -2, -8, -8, 0, 8, -4, -6, 3, -4, 4, 0, 2, 6, -4, 3, 0, -6, -3, 0, 3, 4, -2, -3, -16, -4, 7, -4, 4, 0, 7, 8, 3, 0, 3, 4, -7, -3, -2], [4, 0, -3, 0, 0, 0, -3, -2, -1, 0, -1, 2, 3, -1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, -2, -1, -3, 1, -2, -2, 0, 2, -1, 4, 0, 0, 4, -2, 0, 0, -1, 0, 1, -2, -1, 0, 1, 2, 0, -4, -1, 4, 0, 0, 0, 0, 3, 2, 1, -1, 0, 0, 2, -4, -4, -2, 0, 2, 0, 0, 1, 0, 0, 0, -2, 0, 0, -1, 0, 0, -1, 0, 1, 0, 2, 1, -4, 0, 3, 0, 0, 0, 3, 2, 1, 0, 1, -2, -3, 1, -2], [-2, -4, -2, -4, -2, 0, -2, 1, 1, 0, 1, 5, 2, 1, 5, -4, -3, -1, -2, -3, -1, 0, 0, 0, 2, 3, 1, 4, 3, 1, -2, -1, -5, 1, 0, -1, 1, -3, 0, 3, 0, 1, 2, 3, 1, 0, -1, -5, 1, 0, -1, 5, 0, 3, 1, -3, 0, 0, 0, 0, 2, -1, -1, 1, 0, -3, 5, 3, 0, 1, 0, -1, -2, -3, -1, 4, 2, 0, 3, 3, -2, 1, 0, -3, 1, 0, -1, -4, -3, -1, 2, 4, 2, 4, 2, 0, 2, -1, -1, 0, -1, -5, -2, -1, -5], [-2, -1, 1, -1, -2, 0, 1, 1, 1, 0, 1, -1, -1, -2, -4, -1, 0, 2, -2, -3, -1, 0, 0, 0, 2, 3, 1, 1, 0, -2, 1, 2, 4, 1, 0, -1, 1, 3, 0, 3, 6, 1, 2, 3, 1, 0, -1, 1, 1, 0, -1, -1, 0, -3, 1, 3, 0, 0, 0, 0, -1, -1, -1, -2, 0, -3, -4, -3, -6, 1, 0, -1, -2, -3, -1, 1, 2, 0, 0, 3, -2, -2, 0, -3, 1, 0, -1, -1, 0, 2, 2, 1, -1, 1, 2, 0, -1, -1, -1, 0, -1, 1, 1, 2, 4]]
data=runpy.run_path(str(Path(__file__).with_name('check_levi_single_line_input.py')))
keys=list(data['diagrams'](8,0,0))
pure=[T for T,label in zip(data['inputs'],data['labels']) if label[0]=='pure']
B=sp.Matrix([[T.get(key,0) for T in pure] for key in keys])
assert B.shape==(105,5) and B.rank()==5
signs=[]
for pairs in data['pairings'](tuple(range(8))):
 order=[x for pair in pairs for x in pair]
 signs.append((-1)**sum(order[i]>order[j] for i in range(8) for j in range(i+1,8)))
C=sp.Matrix(105,5,lambda i,j:signs[i]*SOURCE_COLUMNS[j][i])
change,free=B.gauss_jordan_solve(C)
assert free.rows==0 and B*change==C and change.det()==5
print('SOURCE_VECTORS_IN_PROGRAM_BASIS',change)
print('SOURCE_CHANGE_DETERMINANT',change.det())
s=sp.Symbol('s',integer=True)
base=sp.Matrix([[18,16,4,-2,-2],[-2,4,0,-4,-1],[-16,-7,-3,-2,1],[11,-8,-2,1,1],[-3,3,-1,1,-2]])
eig=[2*s*(2*s+1)*(2*s+2)*(2*s+3),(2*s-2)*2*s*(2*s+1)*(2*s+2),(2*s-2)*2*s*(2*s+1)*(2*s+2),(2*s-2)*(2*s-1)*2*s*(2*s+1),(2*s-4)*(2*s-2)*2*s*(2*s+1)]
source_detector=base*sp.diag(*eig)
raw_detector=sp.diag(1,-1,1,-1,-1)*source_detector*change.inv()
expected=3538944*s**5*(s-2)*(s-1)**4*(s+1)**3*(2*s-1)*(2*s+1)**5*(2*s+3)
assert sp.factor(raw_detector.det()-expected)==0
assert expected.subs(s,3)>0
J=sp.Matrix([[-104,-288],[-26,-72],[104,288],[32,192],[-32,-192]])
L=sp.Matrix([[-1,4,0,0,0],[1,0,1,0,0],[0,0,0,1,1]])
assert J.extract([0,3],[0,1]).det()==-10752
assert L.rank()==3 and L*J==sp.zeros(3,2)
print('RAW_PURE_DETECTOR_DETERMINANT',sp.factor(expected))
print('RAW_PURE_DETECTOR_DETERMINANT_AT_S3',expected.subs(s,3))
print('EXACT_GEOMETRIC_DETECTOR_COLUMNS',J)
print('EXACT_DETECTOR_QUOTIENT',L)
print('PASS: input dimension12 for every s>=3; all factors are positive there')
print('SCOPE: input and detector maps only; the mixed-kernel inclusion remains unproved')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
