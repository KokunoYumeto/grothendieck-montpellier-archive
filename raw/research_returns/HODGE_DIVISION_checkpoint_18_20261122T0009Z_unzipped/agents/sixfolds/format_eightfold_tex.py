#!/usr/bin/env python3
"""Convert independently approved eightfold-obstruction sections E801--E808."""
from pathlib import Path
import hashlib
import re
import subprocess

root = Path(__file__).resolve().parent
source = (root / "eightfold_obstructions.md").read_text()
start = source.index("## SF-E807.")
end = source.index("## Sources, checks, and remaining scope")
start_odd = source.index("## SF-E808.")
local_extension = source[start:start_odd]
odd_extension = source[start_odd:end]
approved = source


def convert(text, target):
    result = subprocess.check_output(
        ["pandoc", "-f", "markdown+tex_math_single_backslash", "-t", "latex"],
        input=text.encode()).decode()
    result = result.replace("\\tightlist\n", "")
    for n in range(801, 809):
        result = re.sub(
            r"(\\subsection\{SF-E" + str(n) + r"\.[\s\S]*?\})\\label\{[^}]*\}",
            lambda m: m[1] + "\\label{SF-E" + str(n) + "}",
            result, count=1)
    assert result.count("\\(") == result.count("\\)")
    assert result.count("\\[") == result.count("\\]")
    assert not any(ord(x) < 32 and x not in "\n\t\r" for x in result)
    assert "\\tightlist" not in result
    assert "$" not in result
    begins = re.findall(r"\\begin\{([^}]+)\}", result)
    ends = re.findall(r"\\end\{([^}]+)\}", result)
    assert sorted(begins) == sorted(ends)
    target.write_text(result)
    return {
        "file": target.name, "lines": len(result.splitlines()),
        "inline_pairs": result.count("\\("),
        "display_pairs": result.count("\\["),
        "sha256": hashlib.sha256(result.encode()).hexdigest(),
        "PDF_compilation_claimed": False,
    }


print(convert(approved, root / "eightfold_obstructions.tex"))
print(convert(local_extension, root / "rm_local_extension_draft.tex"))
print(convert(odd_extension, root / "rm_odd_ramification_draft.tex"))
(root / "rm_local_extension_draft.md").write_text(local_extension)
