"""Save one completed archive through the current prepared-upload helper.

The helper owns preparation, byte transfer, finalization and identity metadata.
Its raw receipt stays in the private helper directory. The research record
retains the ordered result with transfer credentials and local xattrs omitted.
This script must not be rerun after an uncertain upload outcome.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
kind = sys.argv[1]
if kind == "final":
    basename = "RESEARCH_SA22_final.zip"
    stem = "root_save_final_archive"
    build_record = ROOT / "code/root_timed_final_archive_output.json"
else:
    number = int(kind)
    basename = f"RESEARCH_SA22_checkpoint_{number:02d}.zip"
    stem = f"root_save_checkpoint_{number:02d}"
    build_record = ROOT / f"code/root_timed_checkpoint_{number:02d}_output.json"
archive = ROOT.parent / basename
output = ROOT / "code" / (stem + "_output.json")
assert not output.exists(), "Do not repeat an archive write after a recorded outcome."
assert archive.is_file() and archive.stat().st_size < 500_000_000
expected = json.loads(build_record.read_text())["archive"]
assert archive.stat().st_size == expected["bytes"]
assert hashlib.sha256(archive.read_bytes()).hexdigest() == expected["sha256"]
helper_dir = ROOT.parent / ".library-upload-run"
helper = helper_dir / "library_upload.py"
assert helper.is_file()
request = {"uploads": [{"local_path": str(archive), "purpose": "create_library_file"}]}
started = time.perf_counter()
started_utc = datetime.now(timezone.utc).isoformat()
process = subprocess.run([sys.executable, str(helper)], input=json.dumps(request) + "\n",
                         text=True, capture_output=True, cwd=ROOT.parent)
finished_utc = datetime.now(timezone.utc).isoformat()
seconds = time.perf_counter() - started
private = helper_dir / "receipts"
private.mkdir(mode=0o700, exist_ok=True)
(private / (stem + ".stdout")).write_text(process.stdout)
(private / (stem + ".stderr")).write_text(process.stderr)

secret_keys = {"upload_url", "download_url", "signed_url", "required_headers",
               "authorization", "cookie", "token", "access_token", "xattrs"}

def sanitized(value):
    if isinstance(value, dict):
        return {k: ("[private transfer detail omitted]" if k.lower() in secret_keys
                    else sanitized(v)) for k, v in value.items()}
    if isinstance(value, list):
        return [sanitized(x) for x in value]
    if isinstance(value, str):
        return re.sub(r"https?://\S*(?:[?&](?:sig|signature|token|X-Amz-[^=\s]*)=)\S*",
                      "[private transfer URL omitted]", value, flags=re.I)
    return value

try:
    receipt = sanitized(json.loads(process.stdout))
except ValueError:
    receipt = {"interpretation": "Helper output was not a JSON receipt; inspect the private outcome before any further action.",
               "stdout_bytes": len(process.stdout.encode()),
               "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest()}
record = dict(archive=basename, started_utc=started_utc, finished_utc=finished_utc,
              seconds=seconds, helper_exit_code=process.returncode,
              request=request, receipt=receipt,
              stderr_bytes=len(process.stderr.encode()),
              stderr_sha256=hashlib.sha256(process.stderr.encode()).hexdigest(),
              outcome_policy="Inspect the ordered receipt; do not infer success solely from the process return code or repeat an uncertain write.")
output.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
sys.exit(process.returncode)
