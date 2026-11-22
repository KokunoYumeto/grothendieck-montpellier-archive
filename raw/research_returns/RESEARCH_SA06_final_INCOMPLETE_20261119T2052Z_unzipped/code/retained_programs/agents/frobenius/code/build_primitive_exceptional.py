"""Build the separate primitive exceptional-boundary auxiliary, not the master."""
from datetime import datetime, timezone
import hashlib, json, os, re, subprocess, time
from pathlib import Path

base = Path(__file__).resolve().parents[1]
research = base.parents[1]
out = base / "output"
name = "C3_primitive_exceptional_check"
source = base / "C3_primitive_exceptional_boundary.tex"
if not source.exists():
    source = base / "C3_primitive_exceptional_boundary_draft.tex"
previous = out / "C3_primitive_exceptional_build.json"
if previous.exists():
    old = json.loads(previous.read_text())
    suffix = re.sub(r"[^0-9]", "", old["started_utc"])
    (out / ("C3_primitive_exceptional_build_"+suffix+".json")).write_text(previous.read_text())
    previous_out = out / "C3_primitive_exceptional_build.out"
    if previous_out.exists():
        (out / ("C3_primitive_exceptional_build_"+suffix+".out")).write_text(previous_out.read_text())
text = source.read_text()
keys = set()
for match in re.finditer(r"\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}", text):
    keys.update(x.strip() for x in match.group(1).split(","))
entries, origins = {}, {}
for path in sorted(research.rglob("*.bib")):
    if "output" in path.parts:
        continue
    data = path.read_text(errors="replace")
    starts = list(re.finditer(r"(?m)^@\w+\{([^,]+),", data))
    for j, match in enumerate(starts):
        key = match.group(1).strip()
        if key in keys and key not in entries:
            end = starts[j+1].start() if j+1 < len(starts) else len(data)
            entries[key] = data[match.start():end].strip()
            origins[key] = str(path.relative_to(research))
missing = sorted(keys-set(entries))
if missing:
    raise RuntimeError("Missing bibliography keys: " + ", ".join(missing))
(out / (name + "_refs.bib")).write_text("\n\n".join(entries[k] for k in sorted(keys))+"\n")
(out / (name + ".tex")).write_text((r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb,amsthm,mathtools,natbib,hyperref}
\setlength{\emergencystretch}{1.5em}
\begin{document}
\input{../SOURCE_FILE}
\bibliographystyle{plainnat}
\bibliography{C3_primitive_exceptional_check_refs}
\end{document}
""").replace("SOURCE_FILE", source.name))
env = dict(os.environ)
env["TEXMFHOME"] = str(research.parent / "texmf")
tex = ["lualatex", "-fmt="+str(research/"lualatex.fmt"),
       "-interaction=nonstopmode", "-halt-on-error", name+".tex"]
commands = [tex, ["bibtex", name], tex, tex, tex]
record = {"started_utc": datetime.now(timezone.utc).isoformat(),
          "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
          "bibliography_origins": origins, "passes": []}
start = time.perf_counter()
logs = []
for cmd in commands:
    t = time.perf_counter()
    result = subprocess.run(cmd, cwd=out, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    logs.append(result.stdout)
    record["passes"].append({"command": cmd, "returncode": result.returncode,
                              "runtime_seconds": time.perf_counter()-t})
    if result.returncode:
        break
record["runtime_seconds"] = time.perf_counter()-start
record["finished_utc"] = datetime.now(timezone.utc).isoformat()
pdf = out/(name+".pdf")
if pdf.exists():
    record["pdf_bytes"] = pdf.stat().st_size
log = (out/(name+".log")).read_text(errors="replace")
record["warnings"] = [x for x in log.splitlines()
                       if re.search(r"Warning|Overfull|Underfull|^!", x)]
record["output_line"] = next((x for x in log.splitlines()
                               if x.startswith("Output written on")), None)
(out/"C3_primitive_exceptional_build.out").write_text("\n".join(logs))
(out/"C3_primitive_exceptional_build.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
