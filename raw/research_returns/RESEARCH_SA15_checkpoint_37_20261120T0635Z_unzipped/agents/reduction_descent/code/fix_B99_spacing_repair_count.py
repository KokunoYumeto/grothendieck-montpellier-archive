from pathlib import Path
import shutil
own = Path(__file__).resolve().parents[1]
hist = own/"notes/B99_spacing_repair_failed_count"
hist.mkdir(exist_ok=False)
p = own/"code/repair_B99_spacing.py"
shutil.copy2(p, hist/"repair_B99_spacing.executed.py")
(hist/"stderr.txt").write_text("AssertionError: 15\nThe pre-write expected count was 8; the exact regex found 15 spacing tokens. No candidate mutation occurred.\n")
old = p.read_text()
assert old.count("assert number == 8, number") == 1
p.write_text(old.replace("assert number == 8, number", "assert number == 15, number"))
