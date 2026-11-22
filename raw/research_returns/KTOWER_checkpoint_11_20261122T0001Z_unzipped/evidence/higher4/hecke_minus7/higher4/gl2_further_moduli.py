"""Run the frozen all-twists GL2 model for e=38 or 40 on candidate moduli.

The full alternate-field model is calculated. Initial-field support
exhaustion is a separate assertion and is not inferred from these inputs.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('e', type=int, choices=(38, 40))
    parser.add_argument('moduli', nargs='+', type=int)
    args = parser.parse_args()
    assert all(m > 1 for m in args.moduli)
    assert len(set(args.moduli)) == len(args.moduli)
    source = HERE/'gl2_twist_residual_certificate.py'
    paths = {'source': source, 'driver': Path(__file__)}
    start_hashes = {k: digest(p) for k, p in paths.items()}
    started = datetime.now(timezone.utc).isoformat()
    text = source.read_text()
    prefix = text[:text.index('parser = argparse.ArgumentParser()')]
    namespace = {'__file__': str(source), '__name__': 'frozen_gl2_further_model'}
    exec(compile(prefix, str(source), 'exec'), namespace)
    rows = []
    for modulus in args.moduli:
        row = namespace['calculate'](args.e, modulus)
        rows.append(row)
        print(json.dumps({k: row[k] for k in ('e', 'modulus', 'dimension',
              'cubic_determinant', 'determinant_gcd', 'unit',
              'unresolved_pivot_obstruction', 'elapsed_seconds')}), flush=True)
    end_hashes = {k: digest(p) for k, p in paths.items()}
    assert start_hashes == end_hashes
    report = {
        'status': 'Exact full integral GL2 calculations for explicit candidate moduli',
        'e': args.e, 'all_units': all(r['unit'] for r in rows), 'cases': rows,
        'source_sha256': start_hashes['source'],
        'driver_sha256': start_hashes['driver'],
        'start_sha256': start_hashes, 'end_sha256': end_hashes,
        'started_utc': started,
        'completed_utc': datetime.now(timezone.utc).isoformat(),
        'candidate_moduli': args.moduli,
        'complete_initial_field_support_claimed': False,
        'scope': 'Complete finite GL2 model; initial-field exhaustiveness and U3 comparison separate.',
    }
    out = HERE/f'gl2_e{args.e}_candidate_certificate.json'
    temporary = out.with_suffix('.tmp')
    temporary.write_text(json.dumps(report, indent=2)+'\n')
    temporary.replace(out)
    print(json.dumps({'output': str(out), 'all_units': report['all_units']}), flush=True)


if __name__ == '__main__':
    main()
