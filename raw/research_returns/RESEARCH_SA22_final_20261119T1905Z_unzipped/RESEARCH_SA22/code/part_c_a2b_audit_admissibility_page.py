"""Read the original admissibility definition; no mathematical check is run."""
import datetime
import json
import pathlib
import time
import fitz

root = pathlib.Path(__file__).resolve().parents[1]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
source = root / "sources/a2b_Solynin1999.pdf"
doc = fitz.open(source)
printed_page = 22
page = doc[printed_page - 3]
destination = root / "qa/part_c_a2b_audit_solynin_22.png"
page.get_pixmap(matrix=fitz.Matrix(1.8, 1.8)).save(destination)
payload = {
    "started_utc": started,
    "elapsed_seconds": time.monotonic() - tick,
    "source": str(source),
    "printed_page": printed_page,
    "pdf_page": printed_page - 2,
    "image_path": str(destination),
    "embedded_text": page.get_text(),
    "network_requests": 0,
    "mathematical_finite_checks": 0,
}
output = root / "code/part_c_a2b_audit_admissibility_page_output.json"
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
output.with_suffix(".txt").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({key: value for key, value in payload.items() if key != "embedded_text"}, indent=2))
