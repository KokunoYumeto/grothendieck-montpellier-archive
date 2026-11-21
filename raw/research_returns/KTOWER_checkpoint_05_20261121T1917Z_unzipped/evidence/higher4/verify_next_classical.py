"""Fresh complete classical replays for e=32,34,36, with exact reconciliation.

This reruns the two already audited finite-model implementations. It is a
fresh same-code replay, not a new independent mathematical construction.
Only elapsed time is ignored when comparing complete numerical objects.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import importlib.util
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ALT = HERE/'hecke_minus7/higher4'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def numerical(row):
    return {k: v for k, v in row.items() if k != 'elapsed_seconds'}


def main():
    source = HERE.parent/'gl2_uniform.py'
    spec = importlib.util.spec_from_file_location('checked_level_three', source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    original = HERE.parent/'gl2_next_weights.json'
    data = json.loads(original.read_text())
    rows = []
    for e in (32, 34, 36):
        saved = next(r for r in data['degrees'] if r['e'] == e)
        fresh = module.compute(e, [7, 13])
        assert numerical(saved) == numerical(fresh)
        rows.append({'field': -3, 'e': e, 'dimension': fresh['dimension'],
                     'entire_numerical_object_equal': True,
                     'data_sha256': digest(original), 'source_sha256': digest(source)})
        print('PASS complete initial-field classical replay', e, flush=True)
    source = ALT/'gl2_twist_residual_certificate.py'
    content = source.read_text()
    prefix = content[:content.index('parser = argparse.ArgumentParser()')]
    namespace = {'__file__': str(source), '__name__': 'checked_level_seven'}
    exec(compile(prefix, str(source), 'exec'), namespace)
    for e in (32, 34, 36):
        path = ALT/f'gl2_e{e}_candidate_certificate.json'
        report = json.loads(path.read_text())
        assert report['source_sha256'] == digest(source)
        assert report['driver_sha256'] == digest(ALT/'gl2_next_moduli.py')
        for saved in report['cases']:
            fresh = namespace['calculate'](e, saved['modulus'])
            assert numerical(saved) == numerical(fresh)
            assert fresh['unit'] and fresh['unresolved_pivot_obstruction'] is None
            rows.append({'field': -7, 'e': e, 'modulus': fresh['modulus'],
                         'dimension': fresh['dimension'],
                         'cubic_determinant': fresh['cubic_determinant'],
                         'entire_numerical_object_equal': True,
                         'data_sha256': digest(path), 'source_sha256': digest(source)})
            print('PASS complete alternate-field classical replay', e,
                  str(saved['modulus']), flush=True)
    output = {'status': 'PASS all nine complete classical model replays',
              'checked_utc': datetime.now(timezone.utc).isoformat(),
              'replay_script_sha256': digest(Path(__file__)), 'results': rows,
              'scope': 'Fresh same-code replays of both audited classical implementations; no new construction or K-group conclusion.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
    print(output['status'], flush=True)


if __name__ == '__main__':
    main()
