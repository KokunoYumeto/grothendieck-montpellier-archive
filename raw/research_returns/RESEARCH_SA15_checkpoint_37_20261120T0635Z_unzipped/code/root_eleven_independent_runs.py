"""Freeze and independently rerun every universal norm-eleven certificate stage."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,time,traceback
w=Path(__file__).resolve().parents[1]
agent=w/'agents/monodromy'
env=w/'outputs/root_eleven_independent_environment'
assert not env.exists()
(env/'code').mkdir(parents=True)
(env/'outputs').mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=agent/'nonordinary_uniform_eleven_theta_geometry_candidate.tex'
assert sha(candidate)=='f240bd69cb86e8401c4896902faf709726852f4740b5d4455e0b1fec55b48cb9'
shutil.copy2(candidate,env/'candidate.tex')
names=['post_CP27_eleven_verified_interpolation',
       'post_CP27_eleven_rational_quintic',
       'post_CP27_eleven_flint_elimination',
       'post_CP27_eleven_A_zero_elimination',
       'post_CP27_eleven_bad_parameter_orbits',
       'post_CP27_eleven_certificate_reconstruction']
inputs={}
for name in names+['post_CP27_binary_coefficient_ring','gf16_exact_domain']:
    p=agent/'code'/f'{name}.py'
    inputs[str(p.relative_to(w))]=sha(p)
    shutil.copy2(p,env/'code'/p.name)
author={}
for name in names:
    p=agent/'outputs'/f'{name}.json'
    inputs[str(p.relative_to(w))]=sha(p)
    author[name]=json.loads(p.read_text())
    shutil.copy2(p,env/f'{name}.author.json')
p=agent/'outputs/probe_eleven_finite_quintic.json'
inputs[str(p.relative_to(w))]=sha(p)
shutil.copy2(p,env/'outputs'/p.name)
volatile={'seconds','runtime_seconds','total_runtime_seconds','actual_utc'}
def mathematical(x):
    if isinstance(x,dict):return {k:mathematical(v) for k,v in x.items() if k not in volatile}
    if isinstance(x,list):return [mathematical(v) for v in x]
    return x
record={'status':'RUNNING','candidate_sha256':sha(candidate),
        'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'frozen_inputs':inputs,'stages':[],
        'scope':'Independent unchanged-source universal interpolation, quotient algebra, full three resultant recomputations, factor products and explicit Bezout identity. Geometry is separately audited.'}
out=w/'outputs/root_eleven_independent_runs.json'
def save():out.write_text(json.dumps(record,indent=2)+'\n')
save()
try:
    for name in names:
        cmd=[sys.executable,str(env/'code'/f'{name}.py')]
        # The original worker entry point is used for the two discovery programs.
        # This avoids their 60-second discovery wrapper while preserving all source
        # bytes. The retained independent harness imposes its own 180-second cap.
        worker=name in ['post_CP27_eleven_flint_elimination','post_CP27_eleven_A_zero_elimination']
        if worker:cmd.append('--worker')
        before=time.perf_counter()
        with (env/f'{name}.stdout.txt').open('w') as stdout, (env/f'{name}.stderr.txt').open('w') as stderr:
            run=subprocess.run(cmd,cwd=env,stdout=stdout,stderr=stderr,timeout=180)
        elapsed=time.perf_counter()-before
        assert run.returncode==0,(name,run.returncode)
        actual=json.loads((env/'outputs'/f'{name}.json').read_text())
        assert actual['status'].startswith('PASS'),(name,actual)
        assert mathematical(actual)==mathematical(author[name]),name
        row={'program':name,'entry_point':'original --worker' if worker else 'original main',
             'subprocess_elapsed_seconds':elapsed,'reported_runtime_seconds':actual.get('runtime_seconds'),
             'all_mathematical_fields_equal_author':True,'status':actual['status']}
        record['stages'].append(row)
        save()
        print(json.dumps(row),flush=True)
    assert all(sha(w/rel)==digest for rel,digest in inputs.items())
    record['status']='PASS_ALL_SIX_UNIVERSAL_STAGES'
    record['author_sources_and_outputs_unchanged']=True
except Exception:
    record['status']='INDEPENDENT_RUN_FAILURE'
    record['traceback']=traceback.format_exc()
finally:
    record['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    save()
    print(json.dumps({k:v for k,v in record.items() if k!='frozen_inputs'},indent=2),flush=True)
if record['status']!='PASS_ALL_SIX_UNIVERSAL_STAGES':raise SystemExit(1)
