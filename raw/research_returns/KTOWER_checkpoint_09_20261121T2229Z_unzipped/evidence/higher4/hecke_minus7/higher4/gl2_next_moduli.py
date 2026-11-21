"""Run the frozen all-twists GL2 calculation on explicit candidate moduli.

This supplies only the alternate-field calculation. The list of input moduli
is not claimed to exhaust the initial-field residual support.
"""
from pathlib import Path
import argparse, hashlib, json, sys
sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
source = HERE/'gl2_twist_residual_certificate.py'
text = source.read_text()
prefix = text[:text.index('parser = argparse.ArgumentParser()')]
namespace = {'__file__':str(source), '__name__':'frozen_gl2_next_model'}
exec(compile(prefix, str(source), 'exec'), namespace)
parser = argparse.ArgumentParser()
parser.add_argument('e', type=int)
parser.add_argument('moduli', nargs='+', type=int)
args = parser.parse_args()
rows = []
for modulus in args.moduli:
    row = namespace['calculate'](args.e, modulus)
    rows.append(row)
    print(json.dumps({k:row[k] for k in ('e','modulus','dimension',
          'cubic_determinant','determinant_gcd','unit',
          'unresolved_pivot_obstruction','elapsed_seconds')}), flush=True)
report = {
    'status':'Exact full integral GL2 calculations for explicit candidate moduli',
    'e':args.e, 'all_units':all(r['unit'] for r in rows), 'cases':rows,
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'candidate_moduli':args.moduli,
    'complete_initial_field_support_claimed':False,
    'scope':'Complete finite GL2 model; initial-field exhaustiveness and U3 comparison separate.',
}
out = HERE/f'gl2_e{args.e}_candidate_certificate.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'output':str(out), 'all_units':report['all_units']}), flush=True)
