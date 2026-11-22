from pathlib import Path
import os, subprocess, time, json, datetime

base = Path('/workspace/scratch/9c53b536a97f')
private = base / 'source_reading'
project = base / 'RESEARCH_SA22'
source = private / 'lehto_virtanen1973.djvu'
out = private / 'lehto_virtanen1973.txt'
decoder = Path('/tmp/part_a567_djvu/unpack/usr/bin')
env = os.environ.copy()
env['LD_LIBRARY_PATH'] = '/tmp/part_a567_djvu/unpack/usr/lib/x86_64-linux-gnu'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
t0 = time.perf_counter()
records = []
commands = [
    [str(decoder / 'djvused'), str(source), '-e', 'n'],
    [str(decoder / 'djvutxt'), str(source), str(out)],
    [str(decoder / 'ddjvu'), '-format=pdf', '-page=1-12', str(source), str(private / 'lehto_virtanen1973_front.pdf')],
]
for command in commands:
    t = time.perf_counter()
    run = subprocess.run(command, capture_output=True, text=True, env=env)
    records.append({'command': command, 'returncode': run.returncode,
                    'stdout': run.stdout, 'stderr': run.stderr,
                    'elapsed_seconds': time.perf_counter()-t})
report = {'started_utc': started, 'elapsed_seconds': time.perf_counter()-t0,
          'scope': 'Three local document-reading commands, no mathematical certificate; full book and text outside deliverable.',
          'text_bytes': out.stat().st_size if out.exists() else None,
          'records': records}
payload = json.dumps(report, indent=2)
(project / 'code/part_c_lehto_djvu_read_output.json').write_text(payload+'\n')
(project / 'code/part_c_lehto_djvu_read_output.txt').write_text(payload+'\n')
print(payload)
