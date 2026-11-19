"""Repair inline-math delimiters in the newly written audit note only."""
from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / "notes/B_A017_audit.md"
lines = p.read_text().splitlines(keepends=True)
out = []
display = False
for line in lines:
    if r"\[" in line:
        display = True
    if display:
        out.append(line)
        if r"\]" in line:
            display = False
        continue
    positions = []
    stack = []
    for i, c in enumerate(line):
        if c == "(":
            stack.append(i)
        elif c == ")" and stack:
            a = stack.pop()
            if not stack:
                value = line[a+1:i].removesuffix("\\")
                mathematical = (
                    "\\" in value or "_" in value or
                    any(s in value for s in ("=", "<", ">", "[-1]", "[-2]")) or
                    re.fullmatch(r"[a-zA-Z]", value)
                )
                if mathematical and not value.startswith("https://"):
                    positions.append((a, i+1, "$" + value + "$"))
    for a, b, replacement in reversed(positions):
        line = line[:a] + replacement + line[b:]
    out.append(line)
p.write_text("".join(out))
