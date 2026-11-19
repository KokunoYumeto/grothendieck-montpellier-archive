"""Apply a block's edits.py to the first-pass pages and write the corrected pages once.
Usage: python -I -B apply_edits_a28ea31f.py <work_dir> <scan> [<scan> ...]"""
import sys, os, importlib.util
sys.stdout.reconfigure(encoding="utf-8")
wd = sys.argv[1]; scans = [int(s) for s in sys.argv[2:]]
spec = importlib.util.spec_from_file_location("e", os.path.join(wd, "edits.py")); e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
src = "../returns/MPL_15_139-194_checkpoint_01_unzipped/pages"
out = "out/MPL_15_139-194"
os.makedirs(out, exist_ok=True)
n_changes = 0
for s in scans:
    name = "MPL_15_139-194_15_scan%03d.tex" % s
    t = open(os.path.join(src, name), encoding="utf-8").read()
    for old, new, cnt in e.EDITS.get(s, []):
        c = t.count(old)
        assert c == cnt, (s, old, c, cnt)
        t = t.replace(old, new); n_changes += 1
    open(os.path.join(out, name), "w", encoding="utf-8", newline="\n").write(t)
print("wrote", len(scans), "pages;", n_changes, "edit rules applied")
