"""Independently check both inclusions of the stored finite Z_2 lattices."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sympy as sp


def v2(value):
    value = Fraction(str(value))
    if not value:
        return 999999

    def valuation(integer):
        integer = abs(integer)
        return (integer & -integer).bit_length() - 1

    return valuation(value.numerator) - valuation(value.denominator)


source = Path(__file__).with_name('pro2_integral_malcev_extended.json')
results = []
for cutoff in json.loads(source.read_text()):
    if cutoff['weight_cutoff'] < 18:
        continue
    for row in cutoff['graded']:
        actual = sp.Matrix([[sp.Rational(x) for x in r]
                            for r in row['actual_rows']])
        generated = sp.Matrix([[sp.Rational(x) for x in r]
                               for r in row['odd_generated_rows']])
        minima = [min(v2(x) for x in matrix)
                  for matrix in [actual * generated.inv(),
                                 generated * actual.inv()]]
        assert min(minima) >= 0, (row['weight'], minima)
        assert v2(actual.det()) == row['actual_determinant_v2']
        assert v2(generated.det()) == row['odd_generated_determinant_v2']
        results.append(dict(cutoff=cutoff['weight_cutoff'],
                            weight=row['weight'], rank=row['rank'],
                            determinant_v2=v2(actual.det()),
                            min_v2_two_way_changes=minima, index=1))

output = dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              method='Independent exact two-way change-of-basis matrices '
                     'and determinant valuations using Sympy Rational',
              results=results)
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2))
print(json.dumps({'checked_components': len(results),
                  'maximum_cutoff': max(x['cutoff'] for x in results),
                  'all_indices_one': True}))
