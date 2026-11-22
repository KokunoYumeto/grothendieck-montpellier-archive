"""The central check register (18 Nov 2026; the user: "keep track of what was checked, how many times, how ... in a very
centralized register", "in a standardized and very, very easy to do way"). Written by the main session (Claude Opus 5.5
Max). Merges every CHECK_EVENTS*.tsv under results_register/ and the stage A returns into CHECK_REGISTER.tsv, one row a
check, in six columns (id, date_utc, who, how, result, where) plus the source file; and CHECK_COUNTS.tsv: per id, how
many checks, by whom and how. Other column names are mapped onto the six. Rerun at will:
    python -I -B results_register/build_check_register.py"""
import csv, pathlib, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10**8)
D = pathlib.Path("C:/Users/user/Documents")
ROOTS = [D / "results_register", D / "grothendieck_archive_transcription_20261110/stage_a_20261118_sent/returns",
         # 19 Nov 2026 (main session, Claude Opus 5.5 at effort max): the research returns, the working-through returns and
         # pilot verdicts, and the French-school checks were missing; their own check events belong in the one register
         D / "grothendieck_archive_transcription_20261110/research_returns",
         D / "grothendieck_archive_transcription_20261110/working_through_20261118",
         D / "french_school_pro_checks_20261117_work"]
MAP = {"id": ["id", "statement_id", "statement id", "statement", "entry_id", "item_id", "claim_id", "node", "lineage"],
       "date_utc": ["date_utc", "date", "when", "time"],
       "who": ["who", "checker", "model", "by"],
       "how": ["how", "type", "kind", "event_type", "check_type", "sub"],
       "result": ["result", "outcome", "verdict", "detail"],
       "where": ["where", "evidence", "locator", "source", "file"]}
# CHECKEDNESS_EVENTS.tsv (the ledger of 18 Nov, a1cd5fb4): node -> id, kind -> how, detail -> result, source -> where
rows = []
for root in ROOTS:
    # 19 Nov: also <name>_CHECK_EVENTS.tsv (intakes, readings); repeats are merged below
    for f in sorted(set(root.rglob("*CHECK_EVENTS*.tsv")) | set(root.rglob("CHECKEDNESS_EVENTS.tsv"))):
        if f.name.startswith("CHECK_REGISTER"): continue
        try:
            r = csv.DictReader(open(f, encoding="utf-8", errors="replace"), delimiter="\t")
            hdr = {h.strip().lower(): h for h in (r.fieldnames or [])}
            pick = {k: next((hdr[c] for c in cands if c in hdr), None) for k, cands in MAP.items()}
            # 19 Nov 2026: a run's own ids (A-004, B.2, ...) repeat across runs; under the three added roots they are
            # prefixed with the run's name (RESEARCH_SA08:A-004), taken from the nearest return folder (*_unzipped), so
            # CHECK_COUNTS does not merge different statements. Publication working copies (*_publish*) repeat a return's
            # files and are left out.
            ns = ""
            if root in ROOTS[2:]:
                parts = f.relative_to(root).parts[:-1]
                if any("_publish" in q for q in parts):
                    continue
                ret = [q for q in parts if q.endswith("_unzipped")]
                if ret:
                    ns = re.sub(r"_(checkpoint_\d+|final(_INCOMPLETE)?)(_\d{8}T\d{4}Z)?_unzipped$", "", ret[-1])
                    ns = re.sub(r"_unzipped$", "", ns)
            for x in r:
                row = [(x.get(pick[k]) or "").strip() if pick[k] else "" for k in MAP] + [f.relative_to(D).as_posix()]
                if ns and row[0] and not row[0].startswith(ns):
                    row[0] = f"{ns}:{row[0]}"
                rows.append(row)
        except Exception as e:
            print("skipped", f, e)
# 19 Nov 2026 (main session, Claude Opus 5.5 at effort max): one event, one row. Sweep 3's reading-level CHECK_EVENTS
# files repeat rows of its topic-level files (1,901 rows, found by a0c4bb37): the same six fields from several files
# are one event, kept once with the first file as source_file and the others in also_in. Rows with all six fields
# empty are never merged.
seen, ded = {}, []
for r in rows:
    k = tuple(r[:6])
    if any(k) and k in seen:
        j = seen[k]
        ded[j][7] = (ded[j][7] + "; " if ded[j][7] else "") + r[6]
        continue
    seen[k] = len(ded)
    ded.append(r + [""])
dups = len(rows) - len(ded)
rows = ded
out = D / "results_register/CHECK_REGISTER.tsv"
with open(out, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(list(MAP) + ["source_file", "also_in"]); w.writerows(rows)
print(f"merged {dups} repeated rows (same six fields in more than one file)")
cnt = collections.defaultdict(lambda: [0, collections.Counter(), collections.Counter()])
for r in rows:
    c = cnt[r[0]]; c[0] += 1; c[1][r[2][:60]] += 1; c[2][r[3][:60]] += 1
with open(D / "results_register/CHECK_COUNTS.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["id", "checks", "who", "how"])
    for k, (n, who, how) in sorted(cnt.items(), key=lambda kv: -kv[1][0]):
        w.writerow([k, n, "; ".join(f"{a} x{b}" for a, b in who.most_common()), "; ".join(f"{a} x{b}" for a, b in how.most_common())])
print(f"CHECK_REGISTER.tsv: {len(rows)} checks on {len(cnt)} ids from {len({r[6] for r in rows})} files")
