"""File Codex-web returns (<ID>_out.zip) from Downloads and the Noether Multilingual folder (13 Nov 2026).
User, 13 Nov ~20:3x UTC: "Why am I dragging these in here? They go to the downloads folder. I'll let you".
Per return: test the zip, refuse absolute or '..' paths, unpack into returns/<ID>/, compare the returned pages with the
scans sent (drag/<ID>/<ID>_scans.zip), delete the zip, move drag/<ID> to done/<ID>, and move the Drive copy to _done/.
Exact duplicates of an already filed zip are deleted; a different second return goes to returns/<ID>_2.
Written and run by the main session (Claude Opus 5.5 at effort max). Log: tools/FILE_RETURNS.log"""
import hashlib, pathlib, re, shutil, subprocess, sys, time, zipfile
sys.stdout.reconfigure(encoding="utf-8")
CW = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110/codex_web_20261113")
RC = "C:/Users/user/Documents/claude_tools/rclone/rclone.exe"
DRIVE = "gdrive:Codex web upload 2026-11-13"
SOURCES = [pathlib.Path("C:/Users/user/Downloads"),
           pathlib.Path("C:/Users/user/Documents/Papors/Chatnotes/CHat translates and clean/Noether Multilingual")]
PAT = re.compile(r"^([ABCH]\d+-\d+)_out(?:\s*\(\d+\))?\.zip$")
LOG = open(CW / "tools/FILE_RETURNS.log", "a", encoding="utf-8")
def log(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.write(s + "\n"); LOG.flush()
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def scan_numbers(names):
    return sorted({int(m.group(1)) for n in names for m in [re.search(r"scan(\d+)\.(?:tex|jpg|jpeg|png|pdf)$", n, re.I)] if m})
log("=== run", time.strftime("%Y-%m-%d %H:%M:%S"), "local")
dry = "--dry" in sys.argv
filed_hashes = {}
zips = sorted((p for d in SOURCES for p in d.glob("*_out*.zip") if PAT.match(p.name)), key=lambda p: p.stat().st_mtime)
drive_moves = []
for z in zips:
    ID = PAT.match(z.name).group(1)
    drag, done = CW / "drag" / ID, CW / "done" / ID
    if not drag.exists() and not done.exists():
        log(ID, "UNKNOWN folder (not in drag/ or done/): left in place", z); continue
    h = sha(z)
    known = filed_hashes.get(h) or next((q for q in (CW / "returns").glob(ID + "*/.zip_sha256") if q.read_text().strip() == h), None)
    if known:
        log(ID, "exact duplicate of a filed return:", "deleted" if not dry else "would delete", z)
        if not dry: z.unlink()
        continue
    with zipfile.ZipFile(z) as zf:
        bad = zf.testzip()
        names = zf.namelist()
        if bad or any(n.startswith(("/", "\\")) or ".." in pathlib.PurePosixPath(n).parts or ":" in n for n in names):
            log(ID, "REFUSED (bad member or unsafe path):", bad, z); continue
        dest = CW / "returns" / ID
        k = 2
        while dest.exists() and any(dest.iterdir()):
            dest = CW / "returns" / f"{ID}_{k}"; k += 1
        if dry:
            log(ID, "would unpack", len(names), "members to", dest.name); continue
        zf.extractall(dest)
    (dest / ".zip_sha256").write_text(h, encoding="utf-8")
    filed_hashes[h] = dest
    pages = scan_numbers(n for n in names if "/pages/" in n)
    src = (drag if drag.exists() else done) / f"{ID}_scans.zip"
    sent = scan_numbers(zipfile.ZipFile(src).namelist()) if src.exists() else []
    missing = [s for s in sent if s not in pages]
    extra = [s for s in pages if s not in sent]
    has_tex = any(n.endswith(f"{ID}_transcription.tex") for n in names)
    log(ID, "->", dest.relative_to(CW).as_posix(), "| pages", len(pages), "of", len(sent), "sent",
        "| MISSING", missing if missing else "none", "| extra", extra if extra else "none",
        "| transcription.tex", "yes" if has_tex else "NO", "| from", z.parent.name)
    z.unlink()
    if drag.exists():
        if done.exists():
            shutil.move(str(drag), str(CW / "done" / f"{ID}_dup_{time.strftime('%H%M%S')}"))
        else:
            shutil.move(str(drag), str(done))
        drive_moves.append(ID)
for ID in drive_moves:
    r = subprocess.run([RC, "moveto", f"{DRIVE}/{ID}", f"{DRIVE}/_done/{ID}", "-q"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    log(ID, "Drive ->_done:", "ok" if r.returncode == 0 else "FAILED " + r.stderr[-300:])
log("=== end; drag/ now holds", len([p for p in (CW / "drag").iterdir() if p.is_dir()]), "folders")
