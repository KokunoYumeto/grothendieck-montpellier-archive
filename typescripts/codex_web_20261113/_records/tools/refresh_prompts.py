"""Rewrite PROMPT.md of unsent batch-K folders from the current template (18 Nov 2026, the main session, Claude Opus
5.5 at effort max), after PROMPT_TEMPLATE_HANDWRITING_K2.md took the lessons of the CTRL-148 control.

For each folder: drag_next/<ID>/PROMPT.md from build_handwriting_k.make_prompt(); then split_for_chrome.py
--prompt-only rewrites drag_split_next/<ID>/PROMPT.md and <ID>_PROMPT.zip (the scan zips are kept); then the lint.
A folder already sent (a chat row in SENT_K_20261117.tsv) is never touched.
usage: python -I -B tools/refresh_prompts.py --skip N     (all unsent ROUNDS.tsv rows after the first N unsent)
       python -I -B tools/refresh_prompts.py ID ...
"""
import csv
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_k_rounds78 as R  # noqa: E402

K, CW = R.K, R.CW
LINT = pathlib.Path.home() / "Documents/claude_tools/push_rule_pro_prompts.py"
allk = (json.loads(K.PLAN_JSON.read_text(encoding="utf-8"))["folders"]
        + json.loads(R.PLAN78.read_text(encoding="utf-8"))["folders"]
        + json.loads((CW / "K_ROUND9_PLAN_20261118.json").read_text(encoding="utf-8"))["folders"])
byid = {x["id"]: x for x in allk}
sent = {r[0] for r in csv.reader(open(CW / "SENT_K_20261117.tsv", encoding="utf-8"), delimiter="\t")
        if len(r) >= 5 and r[4].startswith("https://chatgpt.com/")}
args = sys.argv[1:]
if args[:1] == ["--skip"]:
    rows = [r[0] for r in csv.reader(open(CW / "drag_split_next" / "ROUNDS.tsv", encoding="utf-8"), delimiter="\t")][1:]
    unsent = [i for i in rows if i not in sent]
    ids = unsent[int(args[1]):]
else:
    ids = args
ids = [i for i in ids if i not in sent and i in byid and (CW / "drag_next" / i).is_dir()
       and (CW / "drag_split_next" / i).is_dir()]
PRE = (HERE / "PREAMBLE.tex").read_bytes()  # the builders' preamble (lua-ul from 18 Nov 2026) goes with every folder
for i in ids:
    (CW / "drag_next" / i / "PROMPT.md").write_bytes(K.make_prompt(byid[i], allk).encode("utf-8"))
    for base in ("drag_next", "drag_split_next"):
        (CW / base / i / "PREAMBLE.tex").write_bytes(PRE)
s = subprocess.run([sys.executable, "-I", "-B", str(HERE / "split_for_chrome.py"), "--prompt-only", "--dst",
                    "drag_split_next", "drag_next"] + ids, capture_output=True, text=True, cwd=str(CW))
print(s.stdout[-600:], s.stderr[-400:])
bad = []
for i in ids:
    lint = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint-codex",
                           str(CW / "drag_split_next" / i / "PROMPT.md")], capture_output=True, text=True)
    if lint.returncode != 0:
        bad.append(i)
        print("LINT FAILED:", i, lint.stdout[-300:])
print("refreshed:", len(ids), "| lint failed:", bad)
print("from", ids[:1], "to", ids[-1:])
