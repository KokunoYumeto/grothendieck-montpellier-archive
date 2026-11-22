"""Finalize compact provenance for the stopped public-preview route."""
import datetime,hashlib,json,pathlib,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
START=datetime.datetime.now(datetime.timezone.utc).isoformat();T=time.perf_counter()
p=ROOT/'code/part_c_lieberman_books_web_output.json';d=json.loads(p.read_text())
for c in d['calls']:
 b=pathlib.Path(c['raw_cache_path']).read_bytes();c['raw_cache_bytes']=len(b);c['raw_cache_sha256']=hashlib.sha256(b).hexdigest()
d['volume']['bound_extent_and_target_pages_verified']=False
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
out={'started_utc':START,'runtime_seconds':time.perf_counter()-T,'raw_web_records_hashed':len(d['calls']),'compact_metadata_path':str(p.relative_to(ROOT)),'compact_metadata_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'network_requests':0,'mathematical_checks':0,'theorem_or_source_status_changes':0}
(ROOT/'code/part_c_lieberman_books_finalize_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
