"""Fresh complete classical replays for one of e=38,40.

Both already audited finite-model implementations are rerun. This is a
fresh same-code replay, not an independent mathematical construction.
Only elapsed time is ignored in complete numerical object comparisons.
Each degree has a separate atomic final report and start/end provenance.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import argparse
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('e', type=int, choices=(38, 40))
    args = parser.parse_args()
    e = args.e
    source_three = HERE.parent/'gl2_uniform.py'
    source_seven = ALT/'gl2_twist_residual_certificate.py'
    original = HERE.parent/'gl2_further_weights.json'
    candidate = ALT/f'gl2_e{e}_candidate_certificate.json'
    paths = {'replay': Path(__file__), 'source_three': source_three,
             'source_seven': source_seven, 'initial_data': original,
             'candidate_data': candidate, 'candidate_driver': ALT/'gl2_further_moduli.py'}
    start_hashes = {k: digest(p) for k, p in paths.items()}
    started = datetime.now(timezone.utc).isoformat()
    data = json.loads(original.read_text())
    saved_rows = [r for r in data['degrees'] if r['e'] == e]
    assert len(saved_rows) == 1
    spec = importlib.util.spec_from_file_location('checked_level_three', source_three)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fresh = module.compute(e, [7, 13])
    assert numerical(saved_rows[0]) == numerical(fresh)
    rows = [{'field': -3, 'e': e, 'dimension': fresh['dimension'],
             'entire_numerical_object_equal': True,
             'data_sha256': start_hashes['initial_data'],
             'source_sha256': start_hashes['source_three']}]
    print('PASS complete initial-field classical replay', e, flush=True)
    report = json.loads(candidate.read_text())
    assert report['e'] == e
    assert report['source_sha256'] == start_hashes['source_seven']
    assert report['driver_sha256'] == start_hashes['candidate_driver']
    assert report['start_sha256'] == report['end_sha256']
    assert report['all_units'] is True
    moduli = [r['modulus'] for r in report['cases']]
    assert len(moduli) > 0 and len(set(moduli)) == len(moduli)
    assert moduli == report['candidate_moduli']
    content = source_seven.read_text()
    prefix = content[:content.index('parser = argparse.ArgumentParser()')]
    namespace = {'__file__': str(source_seven), '__name__': 'checked_level_seven'}
    exec(compile(prefix, str(source_seven), 'exec'), namespace)
    for saved in report['cases']:
        assert saved['e'] == e
        fresh = namespace['calculate'](e, saved['modulus'])
        assert numerical(saved) == numerical(fresh)
        assert fresh['unit'] and fresh['unresolved_pivot_obstruction'] is None
        rows.append({'field': -7, 'e': e, 'modulus': fresh['modulus'],
                     'dimension': fresh['dimension'],
                     'cubic_determinant': fresh['cubic_determinant'],
                     'entire_numerical_object_equal': True,
                     'data_sha256': start_hashes['candidate_data'],
                     'source_sha256': start_hashes['source_seven']})
        print('PASS complete alternate-field classical replay', e,
              str(saved['modulus']), flush=True)
    end_hashes = {k: digest(p) for k, p in paths.items()}
    assert start_hashes == end_hashes
    output = {'status': f'PASS all {len(rows)} complete classical model replays for e={e}',
              'e': e, 'started_utc': started,
              'checked_utc': datetime.now(timezone.utc).isoformat(),
              'replay_script_sha256': start_hashes['replay'],
              'start_sha256': start_hashes, 'end_sha256': end_hashes,
              'results': rows,
              'scope': 'Fresh same-code replays of both audited classical implementations; no new construction or K-group conclusion.'}
    destination = HERE/f'verify_further_classical_e{e}.json'
    temporary = destination.with_suffix('.tmp')
    temporary.write_text(json.dumps(output, indent=2)+'\n')
    temporary.replace(destination)
    print(output['status'], flush=True)


if __name__ == '__main__':
    main()
