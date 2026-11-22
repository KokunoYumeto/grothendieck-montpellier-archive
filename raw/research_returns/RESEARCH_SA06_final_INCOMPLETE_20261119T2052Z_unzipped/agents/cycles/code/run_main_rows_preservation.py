"""One scoped timed rerun of the preserved comparison; owned outputs only."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib, hashlib, io, json, runpy, sys, time, traceback

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
PROGRAM = ROOT / 'agents/cycles/code/compare_main_rows_review15_exact.py'
OUT = ROOT / 'agents/cycles/output'
read_paths = set()
capture = False

def audit(event, args):
    if capture and event == 'open' and isinstance(args[0], (str, bytes)):
        path = Path(args[0]).resolve()
        if path.is_file() and path.is_relative_to(ROOT):
            read_paths.add(path)

sys.addaudithook(audit)
stdout, stderr = io.StringIO(), io.StringIO()
started = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()
code = 0
namespace = None
capture = True
try:
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        namespace = runpy.run_path(str(PROGRAM), run_name='__main__')
except BaseException:
    code = 1
    traceback.print_exc(file=stderr)
finally:
    capture = False
elapsed = time.perf_counter() - tick
ended = datetime.now(timezone.utc).isoformat()

def fingerprint(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}

stdout_path = OUT / 'review15_main_rows_rerun.stdout.txt'
stderr_path = OUT / 'review15_main_rows_rerun.stderr.txt'
stdout_path.write_text(stdout.getvalue())
stderr_path.write_text(stderr.getvalue())
inputs = [fingerprint(path) for path in sorted(read_paths)]
(OUT / 'review15_main_rows_rerun.inputs.json').write_text(json.dumps(inputs, indent=2)+'\n')
if namespace is not None:
    snapshot = {'review15_TASKS': namespace['prior'], 'current_TASKS': namespace['now']}
    (OUT / 'review15_main_rows_rerun.tasks.json').write_text(json.dumps(snapshot, indent=2, ensure_ascii=False)+'\n')
original_stdout = OUT / 'review15_main_rows_original.stdout.txt'
result = {
    'program': fingerprint(PROGRAM),
    'cwd': str(ROOT),
    'argv': ['python', 'agents/cycles/code/run_main_rows_preservation.py'],
    'started_utc': started, 'ended_utc': ended, 'runtime_seconds': elapsed,
    'exit_code': code, 'actual_read_input_count': len(inputs),
    'stdout': fingerprint(stdout_path), 'stderr': fingerprint(stderr_path),
    'byte_identical_to_preserved_original_stdout': stdout_path.read_bytes()==original_stdout.read_bytes(),
    'original_run_timing': {
        'tool_reported_wall_time_seconds': 0.282543695,
        'utc_start_end': 'Not instrumented in the original run; not reconstructed.',
        'tool_chunk_id': 'afa8f5', 'exit_code': 0
    },
    'original_receipt_writer_timing': {
        'tool_reported_wall_time_seconds': 0.188568427,
        'in_program_save_timestamp_utc': '2026-11-19T20:45:29.711778+00:00',
        'utc_start_end': 'Not instrumented in the original run; not reconstructed.',
        'tool_chunk_id': '3b5e30', 'exit_code': 0
    },
    'scope': 'Administrative 41-row comparison only. Root writes and normalization saves intercepted by the exact preserved comparison program. No mathematical, TeX, bibliography or root register change.'
}
(OUT / 'review15_main_rows_rerun.run.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
raise SystemExit(code)
