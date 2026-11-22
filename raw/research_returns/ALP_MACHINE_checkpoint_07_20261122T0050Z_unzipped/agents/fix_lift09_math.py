from pathlib import Path
import re

p = Path("/workspace/scratch/66d4177eb491/work/agents/actual_torus_first_lift.md")
s = p.read_text()
lines = []
display = False
for line in s.splitlines(keepends=True):
    if line.strip() == r"\[":
        display = True
        lines.append(line)
        continue
    if line.strip() == r"\]":
        display = False
        lines.append(line)
        continue
    if display:
        lines.append(line)
        continue
    out = ""
    i = 0
    while i < len(line):
        slash_open = line.startswith(r"\(", i)
        plain_open = line[i] == "("
        if not slash_open and not plain_open:
            out += line[i]
            i += 1
            continue
        start = i + (2 if slash_open else 1)
        depth = 1
        j = start
        end = None
        while j < len(line):
            if line.startswith(r"\)", j):
                depth -= 1
                if depth == 0:
                    end = j
                    after = j + 2
                    break
                j += 2
                continue
            if line[j] == "(":
                depth += 1
            elif line[j] == ")":
                depth -= 1
                if depth == 0:
                    end = j
                    after = j + 1
                    break
            j += 1
        if end is None:
            out += line[i]
            i += 1
            continue
        body = line[start:end]
        math = (
            slash_open or "\\" in body or "^" in body or "_" in body
            or body in {"a", "b", "n", "F", "T", "K", "V", "W", "L", "P",
                        "I(t)", "h_K", "1,2,3", "011,110,111", "+,-,-",
                        "-,-,+", "-,-,-", "-1", "-7", "14/9<2"}
        )
        out += ("$" + body + "$") if math else line[i:after]
        i = after
    lines.append(out)
s = "".join(lines)
s = s.replace(r"\widehat{\mathbf Z}^{,3}", r"\widehat{\mathbf Z}^{\,3}")
p.write_text(s)
assert not any(ord(c) < 32 and c not in "\n\t\r" for c in s)
print("Repaired inline math and checked control characters.")
