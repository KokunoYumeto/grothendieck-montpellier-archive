"""The central check register (18 Nov 2026; the user: "keep track of what was checked, how many times, how ... in a very
centralized register", "in a standardized and very, very easy to do way"). Written by the main session (Claude Opus 5.5
Max). Merges every CHECK_EVENTS*.tsv under results_register/ and the stage A returns into CHECK_REGISTER.tsv, one row a
check, in six columns (id, date_utc, who, how, result, where) plus the source file; and CHECK_COUNTS.tsv: per id, how
many checks, by whom and how. Other column names are mapped onto the six. Rerun at will:
    python -I -B results_register/build_check_register.py"""
import csv, pathlib, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10**8)
D = pathlib.Path("C:/Users/user/Documents")
ROOTS = [D / "results_register", D / "grothendieck_archive_transcription_20261110/stage_a_20261118_sent/returns"]
MAP = {"id": ["id", "statement_id", "statement id", "statement", "entry_id", "item_id", "claim_id", "node", "lineage"],
       "date_utc": ["date_utc", "date", "when", "time"],
       "who": ["who", "checker", "model", "by"],
       "how": ["how", "type", "kind", "event_type", "check_type", "sub"],
       "result": ["result", "outcome", "verdict", "detail"],
       "where": ["where", "evidence", "locator", "source", "file"]}
# CHECKEDNESS_EVENTS.tsv (the ledger of 18 Nov, a1cd5fb4): node -> id, kind -> how, detail -> result, source -> where
rows = []
for root in ROOTS:
    for f in sorted(list(root.rglob("CHECK_EVENTS*.tsv")) + list(root.rglob("CHECKEDNESS_EVENTS.tsv"))):
        if f.name.startswith("CHECK_REGISTER"): continue
        try:
            r = csv.DictReader(open(f, encoding="utf-8", errors="replace"), delimiter="\t")
            hdr = {h.strip().lower(): h for h in (r.fieldnames or [])}
            pick = {k: next((hdr[c] for c in cands if c in hdr), None) for k, cands in MAP.items()}
            for x in r:
                rows.append([(x.get(pick[k]) or "").strip() if pick[k] else "" for k in MAP] + [f.relative_to(D).as_posix()])
        except Exception as e:
            print("skipped", f, e)
out = D / "results_register/CHECK_REGISTER.tsv"
with open(out, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(list(MAP) + ["source_file"]); w.writerows(rows)
cnt = collections.defaultdict(lambda: [0, collections.Counter(), collections.Counter()])
for r in rows:
    c = cnt[r[0]]; c[0] += 1; c[1][r[2][:60]] += 1; c[2][r[3][:60]] += 1
with open(D / "results_register/CHECK_COUNTS.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["id", "checks", "who", "how"])
    for k, (n, who, how) in sorted(cnt.items(), key=lambda kv: -kv[1][0]):
        w.writerow([k, n, "; ".join(f"{a} x{b}" for a, b in who.most_common()), "; ".join(f"{a} x{b}" for a, b in how.most_common())])
print(f"CHECK_REGISTER.tsv: {len(rows)} checks on {len(cnt)} ids from {len({r[6] for r in rows})} files")
