#!/usr/bin/env python3
"""Exact three-chart monomial certificate for the fixed-generic-fibre blowup."""
from pathlib import Path
import datetime
import json
import time
import sympy as sp

root = Path(__file__).resolve().parents[1]
started = time.monotonic()
started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
x, y, t = sp.symbols('x y t')
records = []
for name, coords, substitutions, exceptional in [
    ('x', sp.symbols('X V U'), None, 0),
    ('y', sp.symbols('Y A B'), None, 0),
    ('t', sp.symbols('T C D'), None, 0),
]:
    e, a, b = coords
    if name == 'x':
        substitutions = {x: e, y: e*a, t: e*b}
    elif name == 'y':
        substitutions = {x: e*a, y: e, t: e*b}
    else:
        substitutions = {x: e*a, y: e*b, t: e}
    boundary = sp.expand((x*y*t).subs(substitutions, simultaneous=True))
    vertical = sp.expand(t.subs(substitutions, simultaneous=True))
    monomial = sp.Poly(boundary, *coords).monoms()[0]
    vertical_monomial = sp.Poly(vertical, *coords).monoms()[0]
    columns = [sp.Poly(substitutions[z], *coords).monoms()[0] for z in (x,y,t)]
    matrix = sp.Matrix(3, 3, lambda i,j: columns[j][i])
    determinant = int(matrix.det())
    assert monomial == (3,1,1)
    assert abs(determinant) == 1
    assert vertical_monomial[exceptional] == 1
    assert all(exponent in (0,1) for exponent in vertical_monomial)
    assert sum(vertical_monomial) == (1 if name == 't' else 2)
    records.append({
        'chart': name,
        'coordinates': list(map(str, coords)),
        'substitution': {str(z): str(v) for z,v in substitutions.items()},
        'total_boundary_monomial': str(boundary),
        'reduced_boundary_monomial': str(e*a*b),
        'vertical_equation': str(vertical),
        'vertical_exponents': list(vertical_monomial),
        'torus_exponent_determinant': determinant,
    })
output = {'started_utc': started_utc, 'results': records,
          'charts_checked': 3, 'assertions_checked': 15,
          'elapsed_seconds': time.monotonic()-started,
          'scope': 'Exact local monomial substitutions, SNC supports, and reduced vertical multiplicities. Properness, global component identification and cover comparison are proved geometrically in the manuscript.'}
(root/'code/part_b_special_fibre_checks_output.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
