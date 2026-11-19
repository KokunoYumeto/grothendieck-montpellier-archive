"""Exact certificate for the E x P1 tautological-parity counterexample."""
from fractions import Fraction
from pathlib import Path
from time import perf_counter
import json

start = perf_counter()
basis = ['1', 'x', 'y', 'xy', 'z', 'xz', 'yz', 'xyz']
degrees = [0, 1, 1, 2, 2, 3, 3, 4]
identity = [1]*8
bottom = [1]+[0]*7
top = [0]*7+[1]
parity = [(-1)**d for d in degrees]

def rank(columns):
    matrix = [[Fraction(c[i]) for c in columns] for i in range(8)]
    r = 0
    for j in range(len(columns)):
        pivot = next((i for i in range(r, 8) if matrix[i][j]), None)
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        factor = matrix[r][j]
        matrix[r] = [a/factor for a in matrix[r]]
        for i in range(8):
            if i != r:
                factor = matrix[i][j]
                matrix[i] = [a-factor*b for a,b in zip(matrix[i],matrix[r])]
        r += 1
    return r

assert rank([identity,bottom,top]) == 3
assert rank([identity,bottom,top,parity]) == 4
output = dict(
    field='Q', variety='E x P1 over C, E: y^2 z=x^3-x z^2',
    point='(elliptic origin, infinity)',
    basis=basis, degrees=degrees,
    tautological_correspondence_diagonals=[identity,bottom,top],
    parity=parity,
    tautological_rank=3, augmented_rank=4,
    contradictory_identity_coefficients={'from_H1':-1,'from_H2':1},
    runtime_seconds=perf_counter()-start,
    scope='Certifies failure of the tautological-parity converse, not failure of the narrow Chow relations. Product stability and the factor cases prove those relations.'
)
path=Path(__file__).with_name('check_parity_span_output.json')
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
