from pathlib import Path
import hashlib,json,runpy,time,datetime,io,contextlib
base=Path(__file__).resolve().parent.parent
src=base.parent/'monodromy/code/nonordinary_uniform_five_self_isogeny_identities.py'
author=base.parent/'monodromy/outputs/nonordinary_uniform_five_self_isogeny_identities.json'
original=author.read_bytes()
copy=base/'code/independent_nonordinary_uniform_five_self_isogeny_identities.py';copy.write_bytes(src.read_bytes())
buf=io.StringIO();start=time.perf_counter()
with contextlib.redirect_stdout(buf):ns=runpy.run_path(str(copy))
elapsed=time.perf_counter()-start
assert author.read_bytes()==original
(base/'outputs/independent_uniform_five_self_isogeny.stdout.txt').write_text(buf.getvalue())
res=ns['result'];assert res['status']=='PASS' and len(res['identities'])==9 and set(res['identities'].values())=={'0'}
record={'status':'EXACT_CODE_PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'author_output_sha256':hashlib.sha256(original).hexdigest(),'author_output_preserved':True,'isolated_runtime_seconds':elapsed,'internal_runtime_seconds':res['runtime_seconds'],'identity_count':9,'scope':'Full universal identity program read and isolated rerun. Complete geometry proof read; a three-point evaluation independence bridge was requested before final full-proof verdict.'}
(base/'outputs/independent_uniform_five_self_isogeny_code_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
