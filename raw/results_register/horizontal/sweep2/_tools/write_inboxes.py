"""Sweep 2, part 1: write each deep agent's gap list at the top of sweep1/INBOX/<agent>.md (broad agent a0c4bb37,
Claude Opus 5.5 at effort max, 18 Nov 2026). Rerunning replaces the gap-list section and keeps the rest.
usage: python -I -B write_inboxes.py"""
import csv, sys, collections, pathlib, re, datetime

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
H = pathlib.Path(r"C:\Users\user\Documents\results_register\horizontal")
G = list(csv.DictReader(open(H / "sweep2" / "inputs" / "GAP_INDEX.tsv", encoding="utf-8"), delimiter="\t"))
AG = {"a28ea31fa17dd65e1": "SA05 SA06 SA07 SA14 SA15 SA16 SA18 SA19",
      "a34c04448e8299803": "SA08 SA09 SA17 SA24 SA25 SA26 SA27 SA32",
      "ae4ae3dc17acaa440": "SA20 SA22 SA28 SA29 SA30 SA31",
      "a6d42bf6fe2b0d8a8": "SA01 SA02 SA03 SA04 SA10 SA11 SA21"}
LBL = {"pro_notes": "Pro notes not in NOTES_INDEX", "pro_records": "Pro records (research leads, pointers)",
       "codex_sheet_notes": "Codex notes on the sheets", "work_mathnotes": "Work and Codex-web math notes"}
now = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M UTC")
for ag, ts in AG.items():
    mine = [u for u in G if u["agent"] == ag and u["cls"] not in ("pro_chatB", "variant")]
    words = sum(int(u["words"]) for u in mine)
    cls, clw = collections.Counter(u["cls"] for u in mine), collections.Counter()
    for u in mine:
        clw[u["cls"]] += int(u["words"])
    src = collections.OrderedDict()
    for u in sorted(mine, key=lambda u: (u["topic"], u["cls"], u["entry_id"])):
        s = src.setdefault((u["topic"], u["entry_id"].split("#")[0], u["cls"]), [0, 0, u["source_file"]])
        s[0] += 1
        s[1] += int(u["words"])
    tops = sorted({u["topic"] for u in mine})
    L = [f"## Sweep 2, part 1: your gap list (from the broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026, {now})",
         "",
         "The user, 19:2x UTC: \"Yeah, gaps should be checked and integrated.\" Every entry below is read, placed and merged, not only listed.",
         "",
         f"**Your entries:** {len(mine)}, about {words:,} words, in {', '.join(tops)}.",
         "",
         "By class:"]
    L += [f"- {LBL.get(c, c)}: {cls[c]} entries ({clw[c]:,} words)" for c in cls]
    L += [
         "",
         "- **The full list** has one row per entry, with its file and line: `results_register/horizontal/sweep2/inputs/<SAnn>/GAP_INDEX.tsv`. Its columns are entry_id, cls, topic, source_file (relative to `C:/Users/user/Documents`), line, heading, label, words, scans and linked_to.",
         "- **The ids** follow one rule, set out in `results_register/horizontal/sweep2/GLOBAL/ID_RULE.md`.",
         "- **New since sweep 1:**",
         "  - Pro packages that NOTES_INDEX missed, or that came back after the inputs were built (09-11 UTC);",
         "  - the Codex notes on the sheets;",
         "  - every Work and Codex-web folder filed since then (rounds 7-9 and round D).",
         "",
         "**What to do**",
         "1. Your sweep-2 tables are in `results_register/horizontal/sweep2/SA<nn>/`: copies of your sweep-1 PLACEMENT, OBJECTS, FLAGS, CHECK_EVENTS and TOPIC_NOTES. Extend them there and leave `sweep1/` as it is.",
         "2. Place every entry of your GAP_INDEX files as in sweep 1 (`results_register/horizontal/HORIZONTAL_SWEEP1_BRIEF.md`, steps 1-5), under the entry_id given.",
         "   - Merge an entry into an existing item where it is the same object; new items continue your numbering.",
         "   - In cross_topic, name the global tag (\"= H0xx\", from `sweep1/GLOBAL/GLOBAL_OBJECTS.tsv`) where an item is a global object.",
         "3. Read the passage wherever his mathematics or a reading is at stake, and record the basis and fidelity honestly.",
         "4. Keep CHECK_EVENTS as in sweep 1. Placing or reading an entry is not a check.",
         "5. After each topic, check in to `results_register/horizontal/sweep2/CHECKINS/<your agent id>.md` with:",
         "   - the time (date -u) and the counts;",
         "   - the five most important flags;",
         "   - the objects that cross into other topics.",
         "",
         "**What I do (not yours)**",
         "- The second chats (chatB) and the variant folders: I link them by script.",
         "- The stale and double placements: I settle them in `sweep2/GLOBAL` (STALE_PLACEMENTS.tsv, DOUBLE_PLACEMENTS.tsv) and apply them in the global build. Leave those rows as they are.",
         "- The doubts files (`sweep2/inputs/DOUBTS_INDEX.tsv`) are reading registers. They are joined to items by scan, not read.",
         "",
         "**By source**", "", "| topic | source | class | entries | words | file |", "|---|---|---|---:|---:|---|"]
    L += [f"| {t} | {s} | {LBL.get(c, c)} | {n} | {w:,} | {f} |" for (t, s, c), (n, w, f) in src.items()]
    p = H / "sweep1" / "INBOX" / f"{ag}.md"
    old = p.read_text(encoding="utf-8") if p.exists() else ""
    old = re.sub(r"## Sweep 2, part 1: your gap list.*?(?=\n## From the broad agent|\Z)", "", old, flags=re.S)
    p.write_text("\n".join(L) + "\n\n" + old.lstrip(), encoding="utf-8")
    print(f"{ag}: {len(mine)} entries, {words:,} words, {len(src)} sources, topics {' '.join(tops)}")
