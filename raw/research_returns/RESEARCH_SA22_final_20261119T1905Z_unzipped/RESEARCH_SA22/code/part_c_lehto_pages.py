from pathlib import Path
import os, subprocess, time, json, datetime
import fitz

base = Path('/workspace/scratch/9c53b536a97f')
private = base / 'source_reading'
project = base / 'RESEARCH_SA22'
env = os.environ.copy()
env['LD_LIBRARY_PATH'] = '/tmp/part_a567_djvu/unpack/usr/lib/x86_64-linux-gnu'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
t0 = time.perf_counter()
source = private / 'lehto_virtanen1973.djvu'
selection = private / 'lehto_virtanen1973_pp81_100.pdf'
command = ['/tmp/part_a567_djvu/unpack/usr/bin/ddjvu', '-format=pdf', '-page=87-106', str(source), str(selection)]
run = subprocess.run(command, capture_output=True, text=True, env=env)
if run.returncode:
    raise RuntimeError(run.stderr)
paths = []
front = fitz.open(private / 'lehto_virtanen1973_front.pdf')
for page in [0,1]:
    path = private / f'lehto_virtanen1973_front{page+1}.png'
    front[page].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(path)
    paths.append(str(path))
selected = fitz.open(selection)
for printed in [81,83,85,88,92,93,94,95,100]:
    path = private / f'lehto_virtanen1973_p{printed}.png'
    selected[printed-81].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(path)
    paths.append(str(path))
report = {'started_utc': started, 'elapsed_seconds': time.perf_counter()-t0,
          'scope': 'Original-source page rendering, not mathematical testing; all page images outside deliverable.',
          'djvu_page_offset': 6, 'converted_pages':20, 'rendered_pages':len(paths),
          'command':command, 'returncode':run.returncode, 'stdout':run.stdout, 'stderr':run.stderr, 'images':paths}
payload = json.dumps(report, indent=2)
(project / 'code/part_c_lehto_pages_output.json').write_text(payload+'\n')
(project / 'code/part_c_lehto_pages_output.txt').write_text(payload+'\n')
print(json.dumps({k:v for k,v in report.items() if k != 'stderr'},indent=2))
