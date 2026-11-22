"""Losslessly re-encode an existing frozen checkpoint; never resnapshot or overwrite it."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile
src=Path(sys.argv[1]).resolve();dst=Path(sys.argv[2]).resolve();report=Path(sys.argv[3]).resolve()
assert src!=dst and not dst.exists();dst.parent.mkdir(parents=True,exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
with zipfile.ZipFile(src) as old,zipfile.ZipFile(dst,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as new:
 for inf in old.infolist():
  data=old.read(inf.filename)
  new.writestr(inf,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
with zipfile.ZipFile(src) as old,zipfile.ZipFile(dst) as new:
 assert old.namelist()==new.namelist()
 for n in old.namelist():assert old.read(n)==new.read(n),n
r={'reencoded_utc':datetime.now(timezone.utc).isoformat(),'source':str(src),'delivery':str(dst),'source_sha256':sha(src.read_bytes()),'delivery_sha256':sha(dst.read_bytes()),'source_bytes':src.stat().st_size,'delivery_bytes':dst.stat().st_size,'same_member_names_and_bytes':True,'original_preserved':True,'new_research_snapshot':False,'scope':'Only DEFLATE compression level changes from6 to9. Every checkpoint member, including the original creation-time manifest, remains byte-identical. This is a transport encoding of the same scheduled checkpoint.'}
assert dst.stat().st_size<=536870912, 'Recompressed archive still exceeds upload limit'
report.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
