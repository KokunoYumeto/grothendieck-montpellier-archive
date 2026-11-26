"""Look up pequalnp.com fleet lemmas in our local mirror: search the title, plain statement, formal (Lean) statement,
tags and id of every lemma, and show each match with its status and the local path of its checked Lean proof.

Data: RESULTS.json (rebuilt hourly by refresh_fleet_mirror.py from data.pequalnp.com) and the fleet's Lean tree,
exported to ../fleet_lean (git archive of brilliant-hq/pequalnp-proofs upstream/main; commit in
fleet_lean/UPSTREAM_COMMIT.txt).

usage:
  python -I -B fleet_lookup.py REGEX [REGEX ...]        every lemma matching ALL regexes (case-insensitive)
  python -I -B fleet_lookup.py --id L-meta-647 [...]    exact ids
  options: --status checked|conjecture|refuted|...   --program meta|gct|clb|pcx|lib|alg
           --full (whole statements)   --limit N (default 30)   --json
Written 24 Nov 2026 by Claude Opus 5.5 at effort max (session 672ae3a0), for the intake agents that map our results
onto the fleet's graph."""
import json, pathlib, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
LEAN = HERE.parent / "fleet_lean"
args = sys.argv[1:]


def opt(name, default=None):
    if name in args:
        i = args.index(name)
        v = args[i + 1]
        del args[i:i + 2]
        return v
    return default


def flag(name):
    if name in args:
        args.remove(name)
        return True
    return False


ids = []
while "--id" in args:
    ids.append(opt("--id"))
status, program = opt("--status"), opt("--program")
limit = int(opt("--limit", "30"))
full, as_json = flag("--full"), flag("--json")
rx = [re.compile(a, re.I) for a in args]

data = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))
rows = data["lemmas"]
hits = []
for r in rows:
    if ids and r["id"] not in ids:
        continue
    if status and r.get("status") != status:
        continue
    if program and r.get("program") != program:
        continue
    hay = " ".join(str(r.get(k) or "") for k in ("id", "title", "plain_statement", "formal_statement", "tags"))
    if all(x.search(hay) for x in rx):
        hits.append(r)

if as_json:
    print(json.dumps(hits[:limit], ensure_ascii=False, indent=1))
    sys.exit(0)
print(f"{len(hits)} match(es) among {len(rows)} lemmas" + (f"; showing {limit}" if len(hits) > limit else ""))
for r in hits[:limit]:
    cut = None if full else 500
    print("=" * 100)
    print(f"{r['id']} | {r.get('status')} (since {r.get('status_at')}) | program {r.get('program')} | kind {r.get('kind')}"
          f" | layer {r.get('layer')} | attempts {r.get('attempt_count')} | seat {r.get('seat')}")
    print("title:", r.get("title"))
    if r.get("plain_statement"):
        print("plain:", (r["plain_statement"] or "")[:cut])
    if r.get("formal_statement"):
        print("formal:", (r["formal_statement"] or "")[:cut])
    if r.get("depends_on") or r.get("used_by"):
        print("depends_on:", r.get("depends_on"), "| used_by:", r.get("used_by"))
    pf = r.get("proof_file")
    if pf:
        local = LEAN / pf if not str(pf).startswith("lean/") else LEAN / pf
        print("proof:", pf, "| local:", local if local.exists() else "(not in the local export)")
    if r.get("ours"):
        print("our mentions:", r.get("ours") if isinstance(r.get("ours"), (int, str)) else len(r.get("ours")))
