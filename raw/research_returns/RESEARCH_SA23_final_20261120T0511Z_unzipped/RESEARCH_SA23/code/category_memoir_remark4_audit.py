"""Render exact primary pages for the alternative spectral-continuity route.

Page numbers passed to pdftoppm are physical PDF pages.  The audit note records
the printed chapter/page locators and what was actually read visually.
"""
from pathlib import Path
import hashlib
import subprocess

root = Path(__file__).resolve().parents[1]
pdf = root / "notes/geometry_PTT_1966_scan.pdf"
prefix = root / "notes/category_memoir_remark4"
print("PDF", pdf)
print("SHA256", hashlib.sha256(pdf.read_bytes()).hexdigest())
command = ['pdftoppm', '-f', '221', '-l', '223', '-r', '120', '-png', str(pdf), str(prefix)]
print("COMMAND", repr(command), flush=True)
result = subprocess.run(command, text=True, capture_output=True)
print("EXIT", result.returncode)
print("STDOUT", result.stdout)
print("STDERR", result.stderr)
for path in sorted(prefix.parent.glob(prefix.name + '-*.png')):
    print("IMAGE", path)
