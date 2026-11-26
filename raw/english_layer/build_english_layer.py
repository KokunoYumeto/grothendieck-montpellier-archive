"""The English layer of the archive: one place, by the archive's own sections, built from every translation run.

Claude Opus 5.5 at effort max, 22 Nov 2026. Rebuild after each run or intake:
  python -I -B build_english_layer.py
It reads, and never edits, the runs and the text of record. A run is a folder translations_en_<date> with files.tsv
(id, cote, scan, source, sha256, ...) and en/<cote>/<id>.tex; the run of 17 Nov 2026 has an older layout and is read
separately. A page held for its content is never copied, whatever run translated it. Where the French has changed
since a page was translated, STATUS.tsv says so: that is the list of pages to translate again.
"""
import collections
import csv
import hashlib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 8)
L = pathlib.Path(__file__).resolve().parent
T = L.parent
D = T.parent
NL = chr(10)


def rows(p):
    with open(p, encoding="utf-8", errors="replace", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE))


def sha(b):
    return hashlib.sha256(b).hexdigest()


info = {str(m["cote"]): m for m in json.loads((D / "grothendieck_archive_montpellier/MANIFEST.json").read_text(encoding="utf-8"))}
state = {(r["cote"], int(r["scan"])): r["state"] for r in rows(D / "STATE/PAGE_STATE.tsv")}

# the newest run of each page wins
english, decision, checked = {}, {}, {}
old = T / "translations_en_20261117"
if old.is_dir():
    for d in old.iterdir():
        if d.is_dir() and re.fullmatch("[0-9]+(?:-[0-9]+)?", d.name):
            for f in sorted(d.glob("*.tex")):
                m = re.search("scan([0-9]{3})[.]tex$", f.name)
                if m:
                    english[(d.name, int(m.group(1)))] = ("20261117", f, "")
for run in sorted(T.glob("translations_en_2*")):
    if not (run / "files.tsv").is_file():
        continue
    date = run.name.rsplit("_", 1)[-1]
    if (run / "READINESS.tsv").is_file():
        for r in rows(run / "READINESS.tsv"):
            decision[(r["cote"], int(r["scan"]))] = r["decision"]
    marks = {r["page"]: r["verdict"] for r in rows(run / "CHECK.tsv")} if (run / "CHECK.tsv").is_file() else {}
    for r in rows(run / "files.tsv"):
        f = run / "en" / r["cote"] / (r["id"] + ".tex")
        if f.is_file():
            key = (r["cote"], int(r["scan"]))
            english[key] = (date, f, r["sha256"])
            checked[key] = marks.get(r["id"], "")

table, count, wanted = [], collections.defaultdict(collections.Counter), set()
for key in sorted(state, key=lambda k: (int(info[k[0]]["order"]), k[1])):
    c, n = key
    section = info[c]["folder"]
    why = decision.get(key, "")
    run = path = french = ""
    if c.startswith("140-"):
        status = "English edition (grothendieck-longue-marche)"
    elif why.startswith("held"):
        status = why
    elif key in english:
        run, src, french = english[key]
        now = T / "text_of_record/pages" / c / ("%s_scan%03d.tex" % key)
        same = bool(french) and now.is_file() and sha(now.read_bytes()) == french
        status = "English, current" if same else "English from an older French: translate again"
        dst = L / "pages" / section / c / ("%s_scan%03d.tex" % key)
        data = src.read_bytes()
        if not dst.is_file() or dst.read_bytes() != data:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(data)
        wanted.add(dst)
        path = dst.relative_to(L).as_posix()
    elif state[key] == "second pass done":
        status = why if why and why != "translate" else "second pass done: to translate"
    else:
        status = "no second pass yet"
    table.append((section, c, str(n), status, run, checked.get(key, ""), french, path))
    count[c][status] += 1

gone = []
if (L / "pages").is_dir():
    for f in (L / "pages").rglob("*.tex"):
        if f not in wanted:
            gone.append(f)  # a page that was since held, or that left the text
            f.unlink()

(L / "STATUS.tsv").write_text(
    "section\tcote\tscan\tstatus\trun\tform_check\tfrench_sha256\tpage" + NL + "".join("\t".join(r) + NL for r in table),
    encoding="utf-8", newline=NL)

out = ["# The English layer of the Montpellier archive", "",
       "Built by `build_english_layer.py`; don't edit it by hand. `pages/` follows the archive's 22 sections, then the cote,",
       "one file per scan. `STATUS.tsv` has every page with writing: its English, the hash of the French it was made from,",
       "or the reason it has none.", "",
       "AI-translated by GPT-6.1 Sol at reasoning effort max (OpenAI Responses API, Flex), from our AI transcription, with",
       "every doubt mark and alternative reading kept. The form of each page is checked by script; a sample was read",
       "against the French by Claude Opus 5.5 at effort max. No human has checked it against the manuscripts.", "",
       "The rights in the original work belong to its author or the author's representatives or heirs. Our transcription,",
       "translation, corrections and typesetting were produced by AI. They have no human author and, in our understanding,",
       "are not protected by copyright; where any right of ours exists nonetheless, it is dedicated to the public domain",
       "under CC0 1.0. All of this work reproduces or translates the original work, so nothing here licenses or authorizes",
       "any reproduction, translation or other use of that work. This edition is published for educational, non-profit",
       "purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here,",
       "please open a GitHub issue and we will take it down.", ""]
total = collections.Counter(r[3] for r in table)
out += ["| State | Pages |", "|---|--:|"] + ["| %s | %d |" % kv for kv in total.most_common()] + [""]
last = ""
for c in sorted(count, key=lambda c: int(info[c]["order"])):
    k = count[c]
    if c.startswith("140-") or not any(not s.startswith("no second pass") for s in k):
        continue
    sec = info[c]["folder"]
    if sec != last:
        last = sec
        out += ["", "## %s" % sec.replace("_", " "), "",
                "| Cote | Title | Pages | English, current | English, older | To translate | Other |", "|---|---|--:|--:|--:|--:|--:|"]
    n = sum(k.values())
    cur = k["English, current"]
    older = k["English from an older French: translate again"]
    todo = k["second pass done: to translate"]
    title = re.sub(r"\[[0-9]+\]", "", info[c]["title"]).replace("|", "/")
    title = title if len(title) <= 110 else title[:107].rsplit(" ", 1)[0] + " ..."
    out.append("| %s | %s | %d | %d | %d | %d | %d |" % (c, title, n, cur, older, todo, n - cur - older - todo))
(L / "README.md").write_text(NL.join(out) + NL, encoding="utf-8", newline=NL)
print("pages with writing %d | %s" % (len(table), dict(total.most_common())))
print("copies removed:", len(gone))
