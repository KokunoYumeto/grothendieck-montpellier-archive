"""Shared loader for sweep 2 (Claude Opus 5.5 at effort max). Read-only over results_register."""
import csv, collections, re, sys, pathlib
csv.field_size_limit(10**9)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
DOC = pathlib.Path(r"C:\Users\user\Documents")
RR = DOC / "results_register"
OUT = RR / "sweep2_global"
def load_register():
    with open(RR / "REGISTER.tsv", encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f, delimiter="\t")
        rows = list(rd)
    return rows
def load_edges():
    with open(RR / "EDGES.tsv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))
def load_flags():
    with open(RR / "FLAGS.tsv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

# newer locations of results tables retired since sweep 0 (read-only lookups)
MOVED = {
 "s6_pro_prompts_20261112_work/returns/S6_06_BLIND_checkpoint_33_20261118T1008Z_unzipped/S6_06_BLIND/S6_06_BLIND_results.csv":
 "s6_pro_prompts_20261112_work/returns/S6_06_BLIND_checkpoint_35_20261118T1208Z_unzipped/_from_earlier_checkpoints/S6_06_BLIND_checkpoint_33_20261118T1008Z_unzipped/S6_06_BLIND/S6_06_BLIND_results.csv",
}
FINMON_RESULTS = DOC / "derivateurs_companion_20261109/pro_prompts_max_20261112_work/FINMON/FINMON_checkpoint_20_decoded_20261117/FINMON_results.csv"
def results_path(res):
    p = DOC / res
    if p.exists(): return p
    if res in MOVED and (DOC / MOVED[res]).exists(): return DOC / MOVED[res]
    # try _from_earlier_checkpoints of a newer return of the same run
    parts = res.split("/")
    ret_folder = "/".join(parts[:-2]); base = parts[-2]
    parent = DOC / "/".join(parts[:-3])
    old = parts[-3]
    for d in sorted(parent.glob(base + "_*_unzipped"), reverse=True):
        q = d / "_from_earlier_checkpoints" / old / base / parts[-1]
        if q.exists(): return q
    return None
def load_extra():
    """tag -> dict of the results-table columns not carried in REGISTER.tsv"""
    rows = load_register()
    out = {}
    done = set()
    for r in rows:
        if r["results"] in done: continue
        done.add(r["results"])
        p = results_path(r["results"])
        if not p: continue
        with open(p, encoding="utf-8-sig", newline="") as f:
            rd = csv.DictReader(f)
            seen = collections.Counter()
            for row in rd:
                rid = (row.get("id") or "").strip()
                if not rid: continue
                seen[rid] += 1
                tag = f"{r['run']}:{rid}" + (f"#{seen[rid]}" if seen[rid] > 1 else "")
                out[tag] = {k: (v or "") for k, v in row.items() if k not in ("id","statement","status","where_proved","depends_on","notes") and not (k or "").startswith("manuscript")}
    return out
