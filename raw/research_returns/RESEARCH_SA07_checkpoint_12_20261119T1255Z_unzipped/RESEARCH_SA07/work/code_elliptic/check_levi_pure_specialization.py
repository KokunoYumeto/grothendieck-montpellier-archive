#!/usr/bin/env python3
"""Independent certificate for the five pure-W vectors at every s >= 3.

This checks source-coordinate conversion only; it does not construct the
mixed-normalizer matrix. Source: MSS2015 arXiv v2, pp. 7 and 25--27.
"""
from contextlib import redirect_stdout
from datetime import datetime, timezone
from hashlib import sha256
from io import StringIO
from pathlib import Path
from time import perf_counter
import json
import re
import runpy
import sympy as sp

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
PROGRAM = WORK / 'calc_levi_single_line_input.py'
SOURCE = WORK / 'sources_audit_next/MoritaSakasaiSuzuki2015_v2.txt'
START = datetime.now(timezone.utc).isoformat()
T0 = perf_counter()
LOG = StringIO()

with redirect_stdout(LOG):
    data = runpy.run_path(str(PROGRAM))
    pairings = data['pairings']
    diagrams = data['diagrams']
    pure = [t for t, label in zip(data['inputs'], data['labels']) if label[0] == 'pure']
    keys = list(diagrams(8, 0, 0))
    assert len(keys) == 105 and len(pure) == 5
    B = sp.Matrix([[t.get(key, 0) for t in pure] for key in keys])
    assert B.rank() == 5

    # In the source Phi(C)=sgn(i1,j1,...,i4,j4) times the inserted
    # omega tensor. The input script's diagram has no such global sign.
    signs = []
    for pairs in pairings(tuple(range(8))):
        order = [i for pair in pairs for i in pair]
        inversions = sum(order[i] > order[j] for i in range(8) for j in range(i+1, 8))
        signs.append((-1)**inversions)
    raw = SOURCE.read_text().replace('\u2212', '-')
    cols = []
    for i in range(1, 6):
        match = re.search(r'C' + str(i) + r'\s*=\s*\((.*?)\)', raw, re.S)
        assert match, i
        block = re.sub(r'-\s+(\d)', r'-\1', match.group(1))
        entries = [int(x) for x in re.findall(r'-?\d+', block)]
        assert len(entries) == 105, (i, len(entries))
        cols.append([sign*c for sign, c in zip(signs, entries)])
    C = sp.Matrix(105, 5, lambda r, c: cols[c][r])
    change, parameters = B.gauss_jordan_solve(C)
    assert parameters.rows == 0 and B*change == C and change.det() != 0
    print('SOURCE_ORIENTATION_CONVERSION: Phi(C)=sgn(C) times script diagram')
    print('SOURCE_C_IN_PROGRAM_BASIS', str(change))
    print('SOURCE_CHANGE_DETERMINANT', str(change.det()))

    # Independent exact check of the published detector determinant.
    # Columns are v1,...,v5; detector indices are 1,2,3,8,14.
    base = sp.Matrix([[18,16,4,-2,-2],[-2,4,0,-4,-1],
                      [-16,-7,-3,-2,1],[11,-8,-2,1,1],[-3,3,-1,1,-2]])
    s = sp.symbols('s', integer=True, positive=True)
    eig = [2*s*(2*s+1)*(2*s+2)*(2*s+3),
           (2*s-2)*2*s*(2*s+1)*(2*s+2),
           (2*s-2)*2*s*(2*s+1)*(2*s+2),
           (2*s-2)*(2*s-1)*2*s*(2*s+1),
           (2*s-4)*(2*s-2)*2*s*(2*s+1)]
    D = base*sp.diag(*eig)
    det = sp.factor(base.det()*sp.prod(eig))
    assert base.det() != 0 and D.subs(s,3).det() != 0
    assert det == sp.factor(D.det())
    print('MSS_DETECTOR_BASE_DETERMINANT', base.det())
    print('MSS_DETECTOR_DETERMINANT', det)
    print('MSS_DETECTOR_AT_S3', D.subs(s,3))
    print('MSS_DETECTOR_DETERMINANT_AT_S3', D.subs(s,3).det())
    print('PROGRAM_DETECTOR_AT_S3', D.subs(s,3)*change.inv())
    print('PROGRAM_DETECTOR_DETERMINANT_AT_S3', sp.factor((D.subs(s,3)*change.inv()).det()))
    print('ALL_S_GE_3: each eigenvalue factor displayed above is strictly positive')
    print('PASS: formal pure basis specializes isomorphically for every s >= 3')
    print('SCOPE: no mixed-normalizer matrix or all-genus q6 claim')

ELAPSED = perf_counter()-T0
LOG.write(f'INDEPENDENT_ACTUAL_WALL_SECONDS {ELAPSED:.9f}\n')
OUT = HERE / 'check_levi_pure_specialization.out'
OUT.write_text(LOG.getvalue())
META = dict(start_utc=START, wall_seconds=ELAPSED, exit_code=0,
            input_program=str(PROGRAM), program_sha256=sha256(PROGRAM.read_bytes()).hexdigest(),
            primary_source=str(SOURCE), scope='Levi input and pure-W specialization only')
(HERE/'check_levi_pure_specialization.json').write_text(json.dumps(META, indent=2)+'\n')
print(LOG.getvalue(), end='')
