"""Hash retained web-call caches and record the bounded route; no requests."""
import datetime,hashlib,json,pathlib,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
START=datetime.datetime.now(datetime.timezone.utc).isoformat();T=time.perf_counter()
p=ROOT/'code/part_c_lieberman_cambridge_web_output.json';d=json.loads(p.read_text())
for call in d['calls']:
 raw=pathlib.Path(call['raw_cache_path']).read_bytes()
 call['raw_cache_bytes']=len(raw);call['raw_cache_sha256']=hashlib.sha256(raw).hexdigest()
d['decision']='No advertised original Lieberman1968 content link was obtained. The candidate Cambridge author homepage was unavailable (web502; one ordinary GET503), not an empty inventory. No source status changes.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
out={'started_utc':START,'runtime_seconds':time.perf_counter()-T,'raw_web_cache_records_hashed':len(d['calls']),'compact_metadata_path':str(p.relative_to(ROOT)),'compact_metadata_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'network_requests':0,'mathematical_checks':0,'theorem_or_source_status_changes':0}
(ROOT/'code/part_c_lieberman_cambridge_finalize_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
