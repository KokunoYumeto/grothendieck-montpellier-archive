#!/usr/bin/env python3
"""Selected exact mixed scalar rows and a searched polynomial row identity.

This imports only the definitions of the separately retained R-row program.
Any asserted all-parameter identity is checked symbolically, never inferred
from evaluations at sample genera.
"""
from pathlib import Path
source=Path(__file__).with_name('calc_levi_scalar_rows.py').read_text()
exec(compile(source.split('chords=list')[0],'levi_scalar_definitions','exec'))
data=pickle.loads(Path(__file__).with_name('calc_levi_scalar_rows.pickle').read_bytes())
K=data['K'];L=sp.Matrix([[-1,4,0,0,0],[1,0,1,0,0],[0,0,0,1,1]]);LK=L*K
rows=list(data['rows']);names=list(data['names']);finished=False

def selected_test(name,row):
    global finished
    row=[sp.factor(x) for x in row]
    old=sp.Matrix(rows).subs(s,3).rank()
    new=sp.Matrix(rows+[row]).subs(s,3).rank()
    if new==old:
        print('DEPENDENT_AT3',name,flush=True);return
    rows.append(row);names.append(name)
    M=sp.Matrix(rows);A=M.subs(s,3)
    joined=A.col_join(LK.subs(s,3)).rank()
    print('INDEPENDENT_ROW',name,'RANK_AT3',new,'JOINED_OUTPUT_RANK_AT3',joined,flush=True)
    if joined!=new:return
    _,pivots=A.rref();pivots=list(pivots)
    square=M[:,pivots];determinant=sp.factor(square.det())
    numerator=LK[:,pivots]*square.adjugate()
    defect=numerator*M-determinant*LK
    if any(sp.expand(x)!=0 for x in defect):
        print('GENERIC_IDENTITY_NOT_YET',name,flush=True);return
    print('EXACT_POLYNOMIAL_IDENTITY_PASSED',flush=True)
    print('SELECTED_ROW_NAMES',names,flush=True)
    print('PIVOT_COLUMNS',pivots,flush=True)
    print('PIVOT_DETERMINANT',determinant,flush=True)
    print('NUMERATOR_MATRIX',[[sp.factor(x) for x in row] for row in numerator.tolist()],flush=True)
    with Path(__file__).with_suffix('.pickle').open('wb') as file:
        pickle.dump(dict(M=M,LK=LK,K=K,L=L,s=s,names=names,pivots=pivots,determinant=determinant,numerator=numerator),file)
    finished=True

selected_test('R_bxy',[evaluate(T,(-2,-3,-4,-1),plans_R()) for T in inputs])
if not finished:
    chords6=list(pairings(tuple(range(6))))
    for name,constants in [('abx',(-1,-2,-3,-4)),('axy',(-1,-3,-4,-2)),
                            ('bxy',(-2,-3,-4,-1)),('xyu',(-3,-4,-5,-6))]:
        for j,chord in enumerate(chords6):
            plans=plans_ES(chord)
            selected_test('ES1_'+name+'_'+str(j),[evaluate(T,constants,plans) for T in inputs])
            if finished:break
        if finished:break

def plans_ES_wedge(keep,chord):
    plans={}
    for output,glue,sign in bracket_plans():
        tail=output[2:]
        for rotation in range(7):
            word=tail[rotation:]+tail[:rotation]
            for perm in permutations(range(3)):
                caps,orientation=canonical_caps((glue,(output[0],output[1]))+
                   tuple((word[i],word[j]) for i,j in chord)+
                   tuple((word[keep[i]],11+perm[i]) for i in range(3)))
                plans[caps]=plans.get(caps,0)+sign*orientation*parity(perm)
    return {caps:c for caps,c in plans.items() if c}

if not finished:
    wedge_plans=[plans_ES_wedge((0,1,3),((2,5),(4,6))),
                 plans_ES_wedge((0,1,3),((2,6),(4,5)))]
    for name,constants in [('axu',(-1,-3,-5,-2,-4,-6)),
                           ('xuz',(-3,-5,-7,-4,-6,-8)),
                           ('abx',(-1,-2,-3,-2,-1,-4)),
                           ('axy',(-1,-3,-4,-2,-4,-3))]:
        for j,plans in enumerate(wedge_plans):
            selected_test('ES3_'+name+'_'+str(j),[evaluate(T,constants,plans) for T in inputs])
            if finished:break
        if finished:break
if not finished:
    print('SELECTED_ROWS_INSUFFICIENT_FOR_OUTPUT_INCLUSION',flush=True)
    with Path(__file__).with_suffix('.pickle').open('wb') as file:
        pickle.dump(dict(M=sp.Matrix(rows),LK=LK,K=K,L=L,s=s,names=names),file)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
