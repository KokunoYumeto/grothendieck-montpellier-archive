"""Monitor authorized discovery files and launch complete exact replays.

Root-owned tool session IDs cannot be polled from this agent. Only the
explicitly anticipated k29 serialization failure is restarted here.
"""
from pathlib import Path
import json
import os
import subprocess
import sys
import time

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ENV = dict(os.environ, PYTHONINTMAXSTRDIGITS='0')
ES = (26, 28, 30)
seen = {}
replays = {}
handles = []
restarted_k29 = False
restart_process = None
started = time.monotonic()

while time.monotonic()-started < 7200:
    log = HERE/'k29_discovery.log'
    text = log.read_text() if log.exists() else ''
    if (not restarted_k29 and 'ValueError: Exceeds the limit' in text
            and '4300' in text):
        target = HERE/'k29_serialization_limit_failure.log'
        suffix = 1
        while target.exists():
            target = HERE/f'k29_serialization_limit_failure_{suffix}.log'
            suffix += 1
        log.replace(target)
        stream = log.open('w')
        handles.append(stream)
        restart_process = subprocess.Popen(
            [sys.executable, str(HERE/'compute_higher_fast.py'), '29'],
            stdout=stream, stderr=subprocess.STDOUT, env=ENV)
        restarted_k29 = True
        print(json.dumps({'event':'restarted k29 after observed serialization failure',
                          'preserved_log':str(target),
                          'pid':restart_process.pid}), flush=True)
    fresh = []
    for e in ES:
        path = HERE/'fast'/f'harmonic_k{e-1}_exact_exploration.json'
        state = 'not present'
        if path.exists():
            try:
                data = json.loads(path.read_text())
                primes = sorted(r['p'] for r in data['results'])
                state = ('complete' if primes == [7,13] and
                         'elapsed_seconds' in data else f'available primes {primes}')
            except json.JSONDecodeError:
                state = 'write in progress'
        if seen.get(e) != state:
            seen[e] = state
            print(json.dumps({'e':e, 'discovery':state}), flush=True)
        if state == 'complete' and e not in replays:
            fresh.append(e)
    if fresh:
        with (HERE/'collector.log').open('a') as out:
            completed = subprocess.run(
                [sys.executable, str(HERE/'collect_higher.py')],
                stdout=out, stderr=subprocess.STDOUT, env=ENV)
        if completed.returncode:
            raise RuntimeError('Collector failed; inspect collector.log')
        summary = json.loads((HERE/'combined_higher4_residuals.json').read_text())
        for row in summary['degrees']:
            if row['e'] in fresh:
                print(json.dumps({k:row[k] for k in
                                  ('e','unitary_dimension','classical_dimension',
                                   'removed_bounded_support_moduli',
                                   'residual_support_moduli')}), flush=True)
        for e in fresh:
            stream = (HERE/f'harmonic_e{e}_replay.log').open('w')
            handles.append(stream)
            process = subprocess.Popen([
                sys.executable, str(HERE.parent/'harmonic_hecke_certificate.py'),
                '--data', str(HERE/f'harmonic_hecke_e{e}_exact_data.json'),
                '--report', str(HERE/f'harmonic_hecke_e{e}_certificate.json')],
                stdout=stream, stderr=subprocess.STDOUT, env=ENV)
            replays[e] = {'process':process, 'reported':False}
            print(json.dumps({'event':'launched full independent replay',
                              'e':e, 'pid':process.pid}), flush=True)
    for e, job in replays.items():
        code = job['process'].poll()
        if code is not None and not job['reported']:
            job['reported'] = True
            print(json.dumps({'event':'independent replay finished',
                              'e':e, 'exit_code':code}), flush=True)
    if restart_process is not None and restart_process.poll() not in (None,0):
        raise RuntimeError('Updated k29 discovery failed; inspect its new log')
    if len(replays) == len(ES) and all(j['reported'] for j in replays.values()):
        assert all(j['process'].returncode == 0 for j in replays.values())
        print('ALL THREE FULL MODEL REPLAYS COMPLETE', flush=True)
        break
    time.sleep(15)
else:
    print('MONITOR TIME LIMIT: inspect saved logs and running replay status', flush=True)
