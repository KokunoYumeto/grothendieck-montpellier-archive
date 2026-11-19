#!/usr/bin/env python3
"""Exact five-coordinate quotient of the two actual Johnson bracket tensors."""
import ast
from pathlib import Path
from itertools import combinations
from time import perf_counter
import sympy as sp
start=perf_counter()
task=Path(__file__).resolve().parents[2]
source=task/'code'/'check_genus_three_single_line.py'
if not source.exists():source=task/'output'/'RESEARCH_SA07'/'code'/'check_genus_three_single_line.py'
tree=ast.parse(source.read_text())
selected=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef))]
ns={}
exec(compile(ast.Module(body=selected,type_ignores=[]),str(source),'exec'),ns)
ns.update(alphabet='abcdef',prime=101)
ns['v']={x:{x:1} for x in ns['alphabet']}
ns['chords']=list(ns['matchings'](tuple(range(8))))
add,scale,bracket,pair=(ns[k] for k in ('add','scale','bracket','pair'))
v=ns['v'];letters=ns['alphabet'];deltas={}
for a,b,c in combinations(letters,3):
 deltas[a+b+c]={x:add(add(scale(bracket(v[b],v[c]),pair(x,a)),scale(bracket(v[c],v[a]),pair(x,b))),scale(bracket(v[a],v[b]),pair(x,c))) for x in letters}
cols=[]
for program in [['cdf','cef','aef','def','bef','cde'],['bce','adf','adf','abd','bce','abc']]:
 D=deltas[program[-1]]
 for name in reversed(program[:-1]):D=ns['derbracket'](deltas[name],D)
 values=ns['contractions'](D)
 cols.append([values[i] for i in (0,1,2,7,13)])
J=sp.Matrix.hstack(*map(sp.Matrix,cols))
assert J.extract([0,3],[0,1]).det()==-10752
L=sp.Matrix.vstack(*[x.T for x in J.T.nullspace()])
assert L.rank()==3 and L*J==sp.zeros(3,2)
print('RAW_FIVE_DETECTOR_COLUMNS',J)
print('EXACT_QUOTIENT_L',L)
print('PASS: ker(L)=span of the two detector columns; no arithmetic vanishing is asserted')
print('ACTUAL_WALL_SECONDS',perf_counter()-start)
