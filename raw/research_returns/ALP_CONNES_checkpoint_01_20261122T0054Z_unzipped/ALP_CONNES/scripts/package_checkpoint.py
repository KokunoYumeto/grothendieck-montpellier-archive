#!/usr/bin/env python3
"""Create a new full checkpoint only when its scheduled time has arrived."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import hashlib
import json
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
index = int(sys.argv[1])
if index < 1:
    raise ValueError("Checkpoint index starts at one")
anchor = datetime(2026, 11, 22, 0, 9, 19, tzinfo=timezone.utc)
due = anchor + timedelta(minutes=45*index)
now = datetime.now(timezone.utc)
if now < due:
    raise RuntimeError(f"Not due: checkpoint {index} is scheduled for {due.isoformat()}")
target = root.parent / f"ALP_CONNES_checkpoint_{index:02d}.zip"
if target.exists():
    raise FileExistsError(target)
record = {"checkpoint": index, "scheduled_utc": due.isoformat(),
          "created_utc": now.isoformat(), "contents": []}
payloads = []
for path in sorted(root.rglob("*")):
    if not path.is_file() or path.suffix.lower() == ".zip":
        continue
    if "__pycache__" in path.parts:
        continue
    data = path.read_bytes()
    name = "ALP_CONNES/" + path.relative_to(root).as_posix()
    payloads.append((name, data))
    record["contents"].append({"path": name, "bytes": len(data),
                               "sha256": hashlib.sha256(data).hexdigest()})
with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name, data in payloads:
        z.writestr(name, data)
    z.writestr("CHECKPOINT_MANIFEST.json", json.dumps(record, indent=2) + "\n")
with zipfile.ZipFile(target) as z:
    if z.testzip() is not None:
        raise RuntimeError("ZIP integrity failure")
print(json.dumps({"file": str(target), "bytes": target.stat().st_size,
                  "entries": len(payloads)+1, "created_utc": now.isoformat()}))
