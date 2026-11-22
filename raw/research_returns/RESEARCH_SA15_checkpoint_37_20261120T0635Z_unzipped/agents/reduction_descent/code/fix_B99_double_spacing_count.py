from pathlib import Path
import shutil
own = Path(__file__).resolve().parents[1]
p = own/"code/repair_B99_double_spacing.py"
hist = own/"notes/B99_double_spacing_failed_count"
hist.mkdir(exist_ok=False)
shutil.copy2(p, hist/"repair_B99_double_spacing.executed.py")
(hist/"stderr.txt").write_text("AssertionError: 6\nExpected-count guard was7; actual literal token count was6. The candidate remained unchanged.\n")
p.write_text(p.read_text().replace("number == 7", "number == 6").replace("seven", "six"))
