# Reproducible input preparation performed in this run.
# Extract all uploaded archives except OBJ_H0D6_results.zip.
from pathlib import Path
from zipfile import ZipFile
archives = {
    "context": "/mnt/data/OBJ_H0D6_context.zip",
    "entries": "/mnt/data/OBJ_H0D6_entries.zip",
    "pages": "/mnt/data/OBJ_H0D6_pages.zip",
    "scans": "/mnt/data/OBJ_H0D6_scans.zip",
}
out = Path("/mnt/data/H0D6_work")
for name, path in archives.items():
    with ZipFile(path) as z:
        z.extractall(out / name)
# The results archive was opened only after ENTRY.md was written.
