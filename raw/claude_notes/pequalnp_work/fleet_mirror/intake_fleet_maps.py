"""Collect every pequalnp.com fleet lemma id named in the main session's intakes (field_experts/intake_20261121/intakes,
one level of run folders, .md and .tsv files) and table them with the lemma's current status and title from our mirror.
Writes INTAKE_FLEET_MAPS.md beside this script. Lines that mention the paper the user excluded are skipped.
usage: python -I -B intake_fleet_maps.py
Written 24 Nov 2026 by Claude Opus 5.5 at effort max (session 672ae3a0)."""
import collections, json, pathlib, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path("<local>/Documents/field_experts/intake_20261121/intakes")
IDRX = re.compile(r"\bL-(?:gct|meta|clb|pcx|lib|alg)-\d{3,4}\b")
SKIP = re.compile(r"(?i)tang(?!e)")
fleet = {r["id"]: r for r in json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))["lemmas"]}

hits = collections.defaultdict(list)
files = 0
for run in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    for f in sorted(list(run.glob("*.md")) + list(run.glob("*.tsv"))):
        files += 1
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if SKIP.search(line):
                continue
            for lid in set(IDRX.findall(line)):
                hits[lid].append((run.name, f.name, n, " ".join(line.split())[:260]))

order = {"conjecture": 0, "in_work": 1, "blocked": 2, "checked": 3, "refuted": 4, "retired": 5, "dead": 6}
ids = sorted(hits, key=lambda i: (order.get((fleet.get(i) or {}).get("status"), 9), i))
out = ["# Fleet lemmas named in the main session's intakes", "",
       f"Scanned {files} intake files in {sum(1 for p in ROOT.iterdir() if p.is_dir())} run folders; {len(ids)} fleet ids "
       "named. Status and title from our mirror (RESULTS.json; refreshed hourly from data.pequalnp.com). Open nodes "
       "(conjecture, in work) first: those are where an intake result may settle or refute a fleet node. Look up any id "
       "with `python -I -B fleet_lookup.py --id <id>`.", ""]
runs_by_status = collections.Counter()
for lid in ids:
    r = fleet.get(lid)
    st = r.get("status") if r else "not in the mirror"
    runs = sorted({h[0] for h in hits[lid]})
    runs_by_status[st] += 1
    out.append(f"## {lid} ({st}) {r.get('title') if r else ''}".rstrip())
    if r:
        out.append(f"attempts {r.get('attempt_count')}, seat {r.get('seat')}, kind {r.get('kind')}, "
                   f"used by {len(r.get('used_by') or [])} node(s); named in: {', '.join(runs)}")
    for run, fn, n, line in hits[lid][:6]:
        out.append(f"- {run}/{fn}:{n}: {line}")
    if len(hits[lid]) > 6:
        out.append(f"- ... {len(hits[lid]) - 6} more mention(s)")
    out.append("")
(HERE / "INTAKE_FLEET_MAPS.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print(f"files {files} | fleet ids {len(ids)} | by status {dict(runs_by_status)}")
