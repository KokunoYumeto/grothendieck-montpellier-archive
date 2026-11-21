"""Coverage of the Montpellier archive, cote by cote: what had a reading before a cutoff, what got its first reading
since (Work or Pro), what got a second reading since, and what is still without one (out in Work now, queued, or in no
route). Written by the main session (Claude Opus 5.5 at effort max), 18 Nov 2026, for the morning report the user
asked for (P6765: "we filled this, the 50 pages missing there, the 20 pages missing there").

Sources (file names only; nothing inside the returns is read):
- Pro returns: returns/*_unzipped/**/pages/*.tex (early returns that name pages by package: the folder name's range);
- Work and Codex-web returns: codex_web_20261113/returns/<ID>/**/pages/*.tex;
- API typescripts: api_typescripts_20261112/*/pages/*.tex;
- the time of a reading: the creation time of its returns folder;
- sent Work folders: codex_web_20261113/SENT_K_20261117.tsv; queued: drag_split_next/ROUNDS.tsv; scans of a folder:
  ASSIGNMENTS.tsv; blank scans and the logo sheet: tools/K_ROUNDS78_SCANS_20261118.json (the round-7/8/9 tests).
usage: python -I -B tools/coverage_report.py [CUTOFF_UTC]   (default 2026-11-18T00:00; writes ../COVERAGE_<date>.md)
"""
import csv
import datetime as dt
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_k_rounds78 as R  # noqa: E402

K, B, CW, T = R.K, R.B, R.CW, R.T
SCAN_RE = K.SCAN_RE
cut = dt.datetime.fromisoformat((sys.argv[1] if len(sys.argv) > 1 else "2026-11-18T00:00")).replace(
    tzinfo=dt.timezone.utc)
P78 = json.loads(R.PLAN78.read_text(encoding="utf-8"))
PAGES = P78["pages_per_cote"]
CACHE = json.loads(R.CACHE.read_text(encoding="utf-8")) if R.CACHE.exists() else {}


def made(p):
    return dt.datetime.fromtimestamp(p.stat().st_ctime, dt.timezone.utc)


def page_keys(d, name_fallback):
    keys, bad = set(), False
    for f in d.rglob("*.tex"):
        if f.parent.name != "pages":
            continue
        m = SCAN_RE.search(f.name)
        if m and m.group(1) in PAGES:
            keys.add((m.group(1), int(m.group(2))))
        elif m:
            bad = True
    if bad and name_fallback:
        keys |= R.name_ranges(name_fallback, PAGES)[0]
    return keys


readings = {}  # (cote, scan) -> list of (time, route, source)


def add(keys, when, route, src):
    for k in keys:
        readings.setdefault(k, []).append((when, route, src))


for d in sorted((T / "returns").glob("*_unzipped")):
    add(page_keys(d, d.name), made(d), "Pro", d.name.replace("_unzipped", ""))
for base in ("returns", "returns_control"):
    for d in sorted((CW / base).iterdir()) if (CW / base).is_dir() else []:
        if d.is_dir():
            add(page_keys(d, None), made(d), "Work" if d.name.startswith(("K", "CTRL")) else "Codex web", d.name)
for d in (T / "api_typescripts_20261112").iterdir():
    pg = d / "pages"
    for f in pg.glob("*.tex") if pg.is_dir() else []:
        m = re.match(r"^[a-z0-9]+_(.+)_(\d{3})\.tex$", f.name)
        if m and m.group(1) in PAGES:
            add([(m.group(1), int(m.group(2)) + 1)], made(pg), "API", d.name)

assign = {r["folder"]: (r["cote"], [int(n) for n in re.findall(r"\d+", r["scans"])])
          for r in csv.DictReader(open(CW / "ASSIGNMENTS.tsv", encoding="utf-8"), delimiter="\t")}
sent = set()
for r in csv.reader(open(CW / "SENT_K_20261117.tsv", encoding="utf-8"), delimiter="\t"):
    if len(r) >= 5 and r[4].startswith("https://chatgpt.com/"):
        sent.add(r[0])
returned = {d.name.split("_")[0] for base in ("returns", "returns_control") if (CW / base).is_dir()
            for d in (CW / base).iterdir() if d.is_dir()}
rounds = [r[0] for r in csv.reader(open(CW / "drag_split_next" / "ROUNDS.tsv", encoding="utf-8"), delimiter="\t")][1:]
out_now = {(c, n): f for f in sent - returned if f in assign for c in [assign[f][0]] for n in assign[f][1]}
queued = {(c, n): f for f in rounds if f not in sent and f in assign for c in [assign[f][0]] for n in assign[f][1]}


P9F = CW / "K_ROUND9_PLAN_20261118.json"
P9 = json.loads(P9F.read_text(encoding="utf-8")) if P9F.exists() else {}
LISTED = {(c, n) for P in (P78, P9) for key in ("blank", "logo") for c, v in P.get(key, {}).items() for n in v}


def skip(c, n):  # blank or the logo sheet: the plans' lists, else the scan cache's test
    if (c, n) in LISTED:
        return True
    v = CACHE.get(c, {}).get(str(n))
    return bool(v) and (v[0] < 0.0003 or v[1] < 12)


rows, tot = [], dict(pages=0, skip=0, before=0, first_w=0, first_p=0, second=0, out=0, queued=0, none=0)
nolist = {}
for c in sorted(PAGES, key=lambda c: [int(x) for x in c.split("-")]):
    if c.startswith("140-"):  # La Longue Marche: transcribed by our pilot (longue_marche_pro_pilot_20261104), counted apart.
        # 19 Nov 2026: Les Derivateurs (157-*) is counted here. Its manuscript had no reading of ours before round D
        # (18 Nov); the Kuenzer-Malgoire-Maltsiniotis edition is a second witness, not our transcription (the user, P6893).
        continue
    s = dict(pages=PAGES[c], skip=0, before=0, first_w=0, first_p=0, second=0, out=0, queued=0, none=0)
    for n in range(1, PAGES[c] + 1):
        rs = sorted(readings.get((c, n), []))
        if not rs:
            if skip(c, n):
                s["skip"] += 1
            elif (c, n) in out_now:
                s["out"] += 1
            elif (c, n) in queued:
                s["queued"] += 1
            else:
                s["none"] += 1
                nolist.setdefault(c, []).append(n)
            continue
        if rs[0][0] < cut:
            s["before"] += 1
        else:
            s["first_w" if rs[0][1] == "Work" else "first_p"] += 1
        if any(t >= cut and r == "Work" for t, r, _ in rs[1:]):
            s["second"] += 1
    for k in tot:
        tot[k] += s[k]
    if s["first_w"] or s["first_p"] or s["second"] or s["out"] or s["queued"] or s["none"]:
        rows.append((c, s))

stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
L = [f"# Coverage of the Montpellier archive, cote by cote ({stamp})", "",
     f"Readings counted by when their return was filed: before or since {cut:%d %b %Y %H:%M} UTC. A page is "
     "**without a reading** when no return holds it; it is then out in Work now, queued (Work or Pro), or in no route. "
     "Blank scans and the logo sheet are left out. La Longue Marche (140-*, 1,584 pages) was transcribed by our pilot and is "
     "counted apart. Les Dérivateurs (157-*) is counted: its manuscript had no reading of ours before round D (18 Nov), and "
     "the printed edition is a second witness, not our transcription. Written by tools/coverage_report.py (Claude Opus 5.5 at effort max).", "",
     f"**All cotes:** {tot['pages']} scans; {tot['skip']} blank or logo; {tot['before']} read before; "
     f"**{tot['first_w'] + tot['first_p']} read for the first time since** ({tot['first_w']} by Work, "
     f"{tot['first_p']} by Pro); {tot['second']} given a second reading by Work since; still without a reading: "
     f"{tot['out']} out in Work now, {tot['queued']} queued, {tot['none']} in no route.", ""]
gap0 = tot["first_w"] + tot["first_p"] + tot["out"] + tot["queued"] + tot["none"]
L += [f"**The gaps:** {gap0} pages had no reading at the cutoff; {tot['first_w'] + tot['first_p']} of them "
      f"({round(100 * (tot['first_w'] + tot['first_p']) / gap0) if gap0 else 0} %) have one now.", ""]
done_now = [(c, s) for c, s in rows if s["first_w"] + s["first_p"] and not (s["out"] or s["queued"] or s["none"])]
still = [(c, s) for c, s in rows if s["out"] or s["queued"] or s["none"]]
L += [f"## Cotes completed since the cutoff ({len(done_now)}): every page now has a reading", ""]
L += ["- " + "; ".join(f"cote {c}: {s['first_w'] + s['first_p']} page{'s' if s['first_w'] + s['first_p'] != 1 else ''} filled"
                       + (f" ({s['first_w']} Work, {s['first_p']} Pro)" if s["first_w"] and s["first_p"] else
                          " (Pro)" if s["first_p"] else "")
                       for c, s in done_now), ""]
L += [f"## Cotes with pages still without a reading ({len(still)})", ""]
L += [f"- cote {c}: {s['out'] + s['queued'] + s['none']} left ({s['out']} out in Work now, {s['queued']} queued"
      + (f", {s['none']} in no route" if s["none"] else "") + ")"
      + (f"; {s['first_w'] + s['first_p']} filled since" if s["first_w"] + s["first_p"] else "") for c, s in still]
L += ["", "## Every cote with work since the cutoff", "",
      "| cote | scans | blank/logo | read before | first reading since (Work + Pro) | second reading since | "
     "out in Work | queued | in no route |", "|---|---|---|---|---|---|---|---|---|"]
for c, s in rows:
    L.append(f"| {c} | {s['pages']} | {s['skip']} | {s['before']} | {s['first_w']} + {s['first_p']} | {s['second']} | "
             f"{s['out']} | {s['queued']} | {s['none']} |")
if nolist:
    L += ["", "## Scans in no route (no reading, not blank, not out, not queued)", ""]
    L += [f"- cote {c}: scans {B.ranges(v)}" for c, v in nolist.items()]
outp = T / f"COVERAGE_{dt.datetime.now(dt.timezone.utc):%Y%m%d}.md"
outp.write_text("\n".join(L) + "\n", encoding="utf-8")
print(outp)
print(L[4])
