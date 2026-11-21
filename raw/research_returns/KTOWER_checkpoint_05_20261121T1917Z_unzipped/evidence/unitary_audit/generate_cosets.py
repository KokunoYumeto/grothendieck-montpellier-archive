"""Save the explicit 57 integral numerators used in KT-U3-SPECTRUM.

This imports only the new elementary arithmetic module, not any K17 data.
An Eisenstein integer [a,b] denotes a+b*omega, omega^2+omega+1=0.
The actual rational unitary representative is numerator/(3+omega).
"""
from itertools import product
from pathlib import Path
import json
from character_trace import O, I, W, PI, BARPI, UNITS, add, sub, mul, conj, gram, det


def representatives():
    rows=[]
    lines=set()
    for first in range(3):
        for tail in product([O]+UNITS, repeat=2-first):
            v=[O]*first+[I]+list(tail)
            r=sum(x!=O for x in v)
            alpha=BARPI
            for _ in range(r-1):
                alpha=mul(W,alpha)
            delta=sub(alpha,PI)
            assert all(x%r==0 for x in delta)
            c=tuple(x//r for x in delta)
            A=[[add(PI if i==j else O,mul(c,mul(v[i],conj(v[j]))))
                for j in range(3)] for i in range(3)]
            assert gram(A)==[[(7,0) if i==j else O for j in range(3)] for i in range(3)]
            assert det(A)==mul(mul(PI,PI),alpha)
            line=tuple((a-3*b)%7 for a,b in v)
            R=[[(a-3*b)%7 for a,b in row] for row in A]
            assert line not in lines
            lines.add(line)
            image_found=False
            for j in range(3):
                col=[R[i][j] for i in range(3)]
                nonzero=[i for i,x in enumerate(col) if x]
                if nonzero:
                    t=pow(col[nonzero[0]],-1,7)
                    assert tuple(t*x%7 for x in col)==line
                    image_found=True
            assert image_found
            rows.append({'support_size':r, 'line_mod_pi':line,
                         'unit_lift':v, 'numerator':A})
    assert len(rows)==57
    assert [sum(row['support_size']==r for row in rows) for r in (1,2,3)]==[3,18,36]
    return rows


if __name__=='__main__':
    rows=representatives()
    dest=Path(__file__).with_name('minuscule7_cosets.json')
    dest.write_text(json.dumps({'ring':'Z[omega], omega^2+omega+1=0',
       'pair_encoding':'[a,b] means a+b*omega', 'denominator':PI,
       'checks':'57 distinct projective image lines; Gram 7I; determinant pi^2*alpha',
       'representatives':rows},indent=2)+'\n')
    print('Saved all 57 cosets; support multiplicities 3,18,36; exact checks passed.')
