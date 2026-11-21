#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from stable_defect_correction import coefficient,tags,constraints,witnesses,trace_from_fixed_pairs
from two_row_positive import LABELS,ROWS,SIZES,_line_correction

HERE=Path(__file__).resolve().parent
count=0;wc=0
for x,b,s in product(range(5),range(5),range(2,7)):
    tr=[trace_from_fixed_pairs(x,b,s,g) for g in range(7)]
    for label,row in zip(LABELS,ROWS):
        total=sum(size*chi*v for size,chi,v in zip(SIZES,row,tr))
        assert total%120==0
        got=coefficient(x,b,s,label)
        assert got==total//120,(x,b,s,label,got,total//120)
        count+=1
    if s==2:assert tr==[_line_correction(g,x,b) for g in range(7)]
for label in LABELS:
    for x,b,s in ((2,1,4),(0,0,5),(3,2,3)):
        seen=0
        for tag,point in witnesses(x,b,s,label):
            matrix=constraints(x,b,s,tag)
            assert all(sum(a*v for a,v in zip(row,point))==rhs for row,rhs in zip(matrix['A_eq'],matrix['b_eq']))
            assert all(sum(a*v for a,v in zip(row,point))<=rhs for row,rhs in zip(matrix['A_ub'],matrix['b_ub']))
            seen+=1;wc+=1
        assert seen==coefficient(x,b,s,label)
        count+=1
message=f'PASS: {count} exact correction comparisons, including literal fixed-pair induction; {wc} fully enumerated matrix witnesses.\n'
message+='Tag counts:'+str({str(label):len(tags(label)) for label in LABELS})+'\n'
(HERE/'STABLE_DEFECT_CORRECTION_CHECK.txt').write_text(message);print(message,flush=True)
