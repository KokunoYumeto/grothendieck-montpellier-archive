"""Preserve primary page images for the Hilbert spectral-continuity audit."""
from pathlib import Path
import hashlib
import subprocess

root = Path(__file__).resolve().parents[1]
pdf = root / "notes/geometry_PTT_1966_scan.pdf"
print("PDF", pdf)
print("SHA256", hashlib.sha256(pdf.read_bytes()).hexdigest())
for page in (199, 200, 214, 266, 378):
    prefix = root / "notes" / f"category_memoir_followup_{page:03d}"
    command = ['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile', '-r', '120', '-png', str(pdf), str(prefix)]
    print("COMMAND", repr(command), flush=True)
    result = subprocess.run(command, text=True, capture_output=True)
    print("EXIT", result.returncode)
    print("STDOUT", result.stdout)
    print("STDERR", result.stderr)
    print("IMAGE", prefix.with_suffix('.png'), flush=True)
