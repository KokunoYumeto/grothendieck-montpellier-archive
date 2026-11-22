"""Literal isolated reruns of the six fully read norm13 algebra programs."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,time,traceback
w=Path(__file__).resolve().parents[1];a=w/'agents/monodromy'
folder=w/'code/audit_snapshots/norm13_root_algebra'
assert not folder.exists()
(folder/'code').mkdir(parents=True);(folder/'outputs').mkdir()
names=['post_CP28_thirteen_interpolation','post_CP28_thirteen_parameter_probe',
 'post_CP28_thirteen_three_anticommuting_probe','post_CP28_thirteen_three_unit_coordinates',
 'post_CP28_thirteen_pole_fibres','post_CP28_thirteen_linear_subresultants']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before={}
for name in names+['post_CP27_binary_coefficient_ring']:
 for sub,suffix in [('code','.py'),('outputs','.json')]:
  source=a/sub/(name+suffix)
  if source.exists():
   before[str(source.relative_to(w))]=sha(source)
   shutil.copy2(source,folder/sub/source.name)
def mathematical(obj):
 if isinstance(obj,dict):return {k:mathematical(v) for k,v in obj.items() if k not in ('actual_utc','runtime_seconds','seconds')}
 if isinstance(obj,list):return [mathematical(v) for v in obj]
 return obj
record={'status':'RUNNING','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Six fully read algebra sources and coefficient-ring dependency; unchanged isolated reruns. The full geometric proof audit is a separate event.',
 'runs':[],'author_hashes_before':before,'executed_failures':[]}
out=w/'outputs/root_norm13_algebra_reruns.json'
assert not out.exists()
try:
 for name in names:
  start=time.perf_counter()
  run=subprocess.run([sys.executable,str(folder/'code'/(name+'.py'))],cwd=w,capture_output=True,text=True,timeout=150)
  (folder/'outputs'/(name+'.stdout.txt')).write_text(run.stdout)
  (folder/'outputs'/(name+'.stderr.txt')).write_text(run.stderr)
  assert run.returncode==0,(name,run.returncode,run.stderr)
  independent=json.loads((folder/'outputs'/(name+'.json')).read_text())
  original=json.loads((a/'outputs'/(name+'.json')).read_text())
  assert independent['status'].startswith('PASS'),(name,independent)
  assert mathematical(independent)==mathematical(original),name
  row={'name':name,'status':'PASS','runtime_seconds':independent['runtime_seconds'],
       'wall_seconds':time.perf_counter()-start,'author_runtime_seconds':original['runtime_seconds'],
       'source_sha256':sha(folder/'code'/(name+'.py')),
       'output_sha256':sha(folder/'outputs'/(name+'.json')),
       'all_mathematical_fields_equal':True}
  record['runs'].append(row)
  out.write_text(json.dumps(record,indent=2)+'\n')
  print(json.dumps(row),flush=True)
 assert all(sha(w/path)==digest for path,digest in before.items())
 record['author_bytes_unchanged']=True;record['status']='PASS'
except Exception:
 record['status']='FAIL';record['executed_failures'].append(traceback.format_exc());raise
finally:
 record['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 out.write_text(json.dumps(record,indent=2)+'\n')
