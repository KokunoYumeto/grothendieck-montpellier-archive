"""Merge the SA12 sweep-3 readings' check events and corrections, and count the deliverables (SA12 lead
a65dbdc241d1a129a, Claude Opus 5.5 at effort max, 19 Nov 2026). python -I -B merge_sa12.py"""
import csv, re, glob, sys
BS = chr(92)
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
S = Path(r"C:/Users/user/Documents/results_register/horizontal/sweep3/SA12")
T = Path(r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
WHO = {"c29a": "Claude Opus 5.5 at effort max, a203d72bad105bea5 (reader A, stretch c29a), sweep 3 reader of SA12",
       "c29b_c31": "Claude Opus 5.5 at effort max, a3c8d7ded052a745e (reader B, stretch c29b_c31), sweep 3 reader of SA12",
       "c31_lead": "Claude Opus 5.5 at effort max, a65dbdc241d1a129a (SA12 lead, stretch c31_lead), sweep 3 reader of SA12"}

def rows(p):
    with open(p, encoding="utf-8", newline="") as fh:
        r = list(csv.reader(fh, delimiter="\t"))
    return r[0], r[1:]

ce_out, co_out = [], []
for st in ["c29a", "c29b_c31", "c31_lead"]:
    h, rs = rows(S / "readings" / f"{st}_CHECK_EVENTS.tsv")
    for r in rs:
        if not any(x.strip() for x in r):
            continue
        r = (r + [""] * 6)[:6]
        r[2] = WHO[st]
        if not r[5].startswith("readings/"):
            r[5] = f"readings/{st}.md; " + r[5] if not r[5].startswith(st) else "readings/" + r[5]
        ce_out.append(r)
    h, rs = rows(S / "readings" / f"{st}_CORRECTIONS.tsv")
    for r in rs:
        if not any(x.strip() for x in r):
            continue
        r = (r + [""] * 5)[:5]
        r[4] = WHO[st]
        co_out.append(r)
with open(S / "CHECK_EVENTS.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["id", "date_utc", "who", "how", "result", "where"]); w.writerows(ce_out)
with open(S / "CORRECTIONS.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["where", "what", "correction", "reason", "who"]); w.writerows(co_out)
from collections import Counter
print("check events", len(ce_out), Counter(r[3].split(",")[0].strip() for r in ce_out))
print("corrections", len(co_out))

# deliverables: per Pro package and Codex folder
def words(s):
    s = re.sub(r"(?m)^%.*$", "", s)
    return len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", s))
PRO = {"29": ["MPL_29_049-094", "MPL_29_095-140", "MPL_29_141-187"], "31": ["MPL_31_002-051"],
       "33": ["MPL_33_002-049", "MPL_33_050-097"]}
out = []
pro_scans = {}
for cote, pkgs in PRO.items():
    for pkg in pkgs:
        fs = glob.glob(str(T / "returns" / f"{pkg}_unzipped" / "**" / "pages" / f"*_{cote}_scan*.tex"), recursive=True)
        sc = sorted({int(re.search(r"scan(\d+)", f).group(1)) for f in fs})
        txt = "".join(open(f, encoding="utf-8").read() for f in fs)
        notes = glob.glob(str(T / "returns" / f"{pkg}_unzipped" / "**" / "*notes*.md"), recursive=True)
        pro_scans.setdefault(cote, set()).update(sc)
        out.append([pkg, cote, sc, len(sc), words(txt), txt.count(BS + "unsure"), "Pro", len(notes)])
CODEX = ["A29-01"] + [f"C29-0{i}" for i in range(1, 8)] + [f"K29-{i:02d}" for i in range(1, 12)] + \
        [f"K31-0{i}" for i in range(1, 4)] + [f"B37-0{i}" for i in range(1, 6)] + ["C32-01", "H35-01", "H37-01"]
for fo in CODEX:
    d = T / "codex_web_20261113" / "returns" / fo / "out"
    p = d / f"{fo}_transcription.tex"
    if not p.exists():
        out.append([fo, "?", [], 0, 0, 0, "missing", 0]); continue
    txt = p.read_text(encoding="utf-8")
    sc = sorted({int(x) for x in re.findall(BS + BS + r"scanpage\{(\d+)\}", txt)})
    files = sorted(x.name.replace(fo + "_", "") for x in d.iterdir() if x.is_file())
    out.append([fo, fo[1:3], sc, len(sc), words(txt), txt.count(BS + "unsure"), "Codex " + ",".join(files), 0])
def rng(sc):
    if not sc: return ""
    parts, a, b = [], sc[0], sc[0]
    for x in sc[1:]:
        if x == b + 1: b = x
        else: parts.append(f"{a}-{b}" if a != b else f"{a}"); a = b = x
    parts.append(f"{a}-{b}" if a != b else f"{a}")
    return ", ".join(parts)
for o in out:
    cote = o[1]
    wit = ""
    if o[6].startswith("Codex") and cote in pro_scans:
        both = [x for x in o[2] if x in pro_scans[cote]]
        wit = f"second witness to Pro on {len(both)} of {len(o[2])} scans" if both else "only witness"
    elif o[6].startswith("Codex"):
        wit = "only witness"
    print("\t".join(str(x) for x in [o[0], cote, rng(o[2]), o[3], o[4], o[5], o[6][:90], o[7], wit]))
