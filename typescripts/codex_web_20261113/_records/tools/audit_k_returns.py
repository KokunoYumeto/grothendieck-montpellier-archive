"""The running audit of the batch-K Work returns (GPT-6.2 Astra Max), 18 Nov 2026. Written by the main session, Claude
Opus 5.5 at effort max, at the user's word of 18 Nov 00:55 UTC (P6742): "just keep auditing it ... what are the basic
ass errors that it keeps running into anyway? How do we make it able to fix that?"

Per return filed since the cutoff (codex_web_20261113/returns/K*/), from its files only:
- the model (SENT_K_20261117.tsv), the hand grade of the cote (k_material.GRADE), whether Hua's text was a witness;
- progress.log: minutes a page for the first pass and for the second reading, the milestones (transcription frozen,
  witness check done, mathnotes done, hashes checked after the notes);
- the marks (\\unsure, \\illegible, \\deleted) a page; brace, $ and environment balance per page file;
- a LuaLaTeX compile of the standalone file in a temporary folder (no shell escape): errors, overfull boxes;
- the inventory (rows not transcribed), the doubts file (notation table, witness table), the math notes (sections,
  words, confidence labels), CHECK_EVENTS.tsv rows.
Writes ../AUDIT_K_RETURNS_<date>.tsv and .md (in codex_web_20261113/).
usage: python -I -B tools/audit_k_returns.py [CUTOFF_UTC] [--no-compile]
"""
import csv
import datetime as dt
import pathlib
import re
import shutil
import statistics as st
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
CW = HERE.parent
sys.path.insert(0, str(HERE))
import k_material  # noqa: E402

args = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith("--")
        and sys.argv[i - 1] not in ("--preamble", "--tag")]
cut = dt.datetime.fromisoformat(args[0] if args else "2026-11-18T00:00").replace(tzinfo=dt.timezone.utc)
COMPILE = "--no-compile" not in sys.argv
PRE = pathlib.Path(sys.argv[sys.argv.index("--preamble") + 1]) if "--preamble" in sys.argv else None
TAG = sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else ""
LUA = shutil.which("lualatex")

model = {}
for r in csv.reader(open(CW / "SENT_K_20261117.tsv", encoding="utf-8"), delimiter="\t"):
    if r and len(r) > 3:
        m = re.search(r"GPT-[\d.]+ \w+(?: \w+)?", " ".join(r[1:]))
        if m and r[0] not in model:
            model[r[0]] = m.group(0)


def ts(s):
    s = s.strip().replace("Z", "+00:00")
    try:
        return dt.datetime.fromisoformat(s)
    except ValueError:
        return None


def balance(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = t.replace("\\\\", " ").replace("\\{", "").replace("\\}", "").replace("\\$", "")
    bad = []
    depth = 0
    for ch in t:
        depth += (ch == "{") - (ch == "}")
        if depth < 0:
            break
    if depth != 0:
        bad.append("braces")
    if t.count("\\[") != t.count("\\]"):
        bad.append("\\[\\]")
    if (t.count("$") - 2 * t.count("$$")) % 2:
        bad.append("$")
    b = re.findall(r"\\begin\{([^}]+)\}", t)
    e = re.findall(r"\\end\{([^}]+)\}", t)
    if sorted(b) != sorted(e):
        bad.append("env")
    return bad


def compile_check(out, fid):
    if not (COMPILE and LUA):
        return "", "", ""
    with tempfile.TemporaryDirectory() as tmp:
        for f in out.iterdir():
            if f.is_file() and f.suffix in (".tex", ".sty"):
                shutil.copy(f, tmp)
        if (out / "pages").is_dir():
            shutil.copytree(out / "pages", pathlib.Path(tmp) / "pages")
        if PRE:
            shutil.copy(PRE, pathlib.Path(tmp) / "PREAMBLE.tex")
        try:
            subprocess.run([LUA, "-no-shell-escape", "-interaction=nonstopmode", f"{fid}_standalone.tex"], cwd=tmp,
                           capture_output=True, timeout=180)
        except subprocess.TimeoutExpired:
            return "timeout", "", ""
        log = pathlib.Path(tmp) / f"{fid}_standalone.log"
        if not log.exists():
            return "no log", "", ""
        lg = log.read_text(encoding="utf-8", errors="replace")
        errs = len(re.findall(r"^! ", lg, flags=re.M))
        over = [float(x) for x in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide", lg)]
        m = re.search(r"Output written on .*?\((\d+) pages?", lg)
        return errs, sum(1 for x in over if x > 2), (m.group(1) if m else "0")


rows = []
for d in sorted((CW / "returns").iterdir()):
    if not d.is_dir() or not d.name.startswith("K"):
        continue
    made = dt.datetime.fromtimestamp(d.stat().st_ctime, dt.timezone.utc)
    if made < cut:
        continue
    fid = d.name
    out = d / "out" if (d / "out").is_dir() else d
    pages = sorted((out / "pages").glob("*.tex")) if (out / "pages").is_dir() else []
    cote = (re.search(r"_(\d+(?:-\d+)?)_scan\d{3}", pages[0].name).group(1) if pages else "")
    r = dict(id=fid, cote=cote, model=model.get(fid, "?"), grade=k_material.GRADE.get(cote, "unsurveyed"),
             pages=len(pages), filed=made.strftime("%H:%M"))
    pl = (out / "progress.log").read_text(encoding="utf-8", errors="replace") if (out / "progress.log").exists() else ""
    lines = pl.splitlines()
    start = ts(lines[0]) if lines else None
    done = [ts(m.group(1)) for m in re.finditer(r"scan \d+ done (\S+)", pl)]
    aud = [ts(m.group(1)) for m in re.finditer(r"scan \d+ audited (\S+)", pl)]
    done, aud = [x for x in done if x], [x for x in aud if x]
    mile = {k: bool(re.search(k, pl)) for k in ("transcription frozen", "witness check done", "mathnotes done")}
    r["hash_after_notes"] = "yes" if re.search(r"(?i)(hash|sha-?256)[^\n]*(still )?match", pl) else "no"
    n = max(1, len(pages))
    r["first_min_pg"] = round((max(done) - start).total_seconds() / 60 / n, 1) if start and done else ""
    r["second_min_pg"] = round((max(aud) - max(done)).total_seconds() / 60 / n, 1) if aud and done else ""
    md = re.search(r"mathnotes done (\S+)", pl)
    end = ts(md.group(1)) if md else None
    r["total_min"] = round((end - start).total_seconds() / 60) if end and start else ""
    r["frozen"], r["witness"], r["mathnotes"] = (("yes" if mile[k] else "no") for k in mile)
    wm = re.search(r"witness check done[^\n]*", pl)
    r["witness_line"] = wm.group(0)[:120] if wm else ""
    tr = (out / f"{fid}_transcription.tex")
    t = tr.read_text(encoding="utf-8", errors="replace") if tr.exists() else ""
    words = len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", re.sub(r"\\[A-Za-z]+", " ", t)))
    r["words"] = words
    for k in ("unsure", "illegible", "deleted"):
        r[k] = len(re.findall(r"\\" + k + r"\b", t))
    r["unsure_per_100w"] = round(100 * r["unsure"] / words, 2) if words else ""
    r["unbalanced_pages"] = " ".join(f"{p.stem.split('_scan')[-1]}:{','.join(b)}" for p in pages
                                     for b in [balance(p.read_text(encoding='utf-8', errors='replace'))] if b)
    r["compile_errors"], r["overfull_gt2pt"], r["pdf_pages"] = compile_check(out, fid)
    inv = out / f"{fid}_inventory.csv"
    if inv.exists():
        ir = list(csv.DictReader(open(inv, encoding="utf-8", errors="replace")))
        r["inv_rows"] = len(ir)
        r["inv_not_yes"] = sum(1 for x in ir if (x.get("transcribed") or "").strip().lower() != "yes")
    else:
        r["inv_rows"], r["inv_not_yes"] = "missing", ""
    dbt = out / f"{fid}_doubts.md"
    dt_ = dbt.read_text(encoding="utf-8", errors="replace") if dbt.exists() else ""
    r["notation_table"] = "yes" if re.search(r"(?i)notation", dt_) else "no"
    r["witness_table"] = "yes" if re.search(r"(?i)witness check", dt_) else "no"
    mn = out / f"{fid}_mathnotes.md"
    m_ = mn.read_text(encoding="utf-8", errors="replace") if mn.exists() else ""
    r["math_words"] = len(m_.split())
    secs = ["What the pages do", "Statements left without proof", "Questions and conjectures", "Slips", "Pointers",
            "Remarks of the model"]
    r["math_sections"] = sum(1 for s in secs if s.lower() in m_.lower())
    r["math_conf_labels"] = len(re.findall(r"(?i)\b(high|medium|low)\b(?: confidence)?", m_))
    ce = out / "CHECK_EVENTS.tsv"
    r["check_events"] = max(0, len(ce.read_text(encoding="utf-8", errors="replace").strip().splitlines()) - 1) \
        if ce.exists() else "missing"
    rows.append(r)
    print(fid, r["model"], r["pages"], r["first_min_pg"], r["second_min_pg"], r["compile_errors"], r["unbalanced_pages"],
          flush=True)

stamp = dt.datetime.now(dt.timezone.utc)
tsv = CW / f"AUDIT_K_RETURNS_{stamp:%Y%m%d}{TAG}.tsv"
if rows:
    with open(tsv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def med(key, rs):
    v = [x[key] for x in rs if isinstance(x[key], (int, float))]
    return (round(st.median(v), 2), round(min(v), 2), round(max(v), 2)) if v else ("", "", "")


L = [f"# Audit of the batch-K Work returns filed since {cut:%d %b %H:%M} UTC ({stamp:%Y-%m-%d %H:%M} UTC)", "",
     f"{len(rows)} returns, {sum(r['pages'] for r in rows)} pages. Written by tools/audit_k_returns.py (Claude Opus 5.5 "
     "at effort max); it reads the returns' files only, and compiles each standalone file with LuaLaTeX.", "",
     "| measure | median | min | max |", "|---|---|---|---|"]
for k, lab in (("first_min_pg", "first pass, minutes a page"), ("second_min_pg", "second reading, minutes a page"),
               ("total_min", "whole session, minutes"), ("unsure_per_100w", "\\unsure per 100 words"),
               ("math_words", "math notes, words"), ("inv_rows", "inventory rows")):
    a, b, c = med(k, rows)
    L.append(f"| {lab} | {a} | {b} | {c} |")
by_model = {}
for r in rows:
    by_model.setdefault(r["model"], []).append(r)
L += ["", "By model: " + "; ".join(f"{m}: {len(v)} returns, {sum(x['pages'] for x in v)} pages" for m, v in by_model.items())]
flags = [("compile errors", [r for r in rows if isinstance(r["compile_errors"], int) and r["compile_errors"] > 0]),
         ("no PDF", [r for r in rows if r["pdf_pages"] in ("0", "")] if COMPILE and LUA else []),
         ("unbalanced page files", [r for r in rows if r["unbalanced_pages"]]),
         ("no 'transcription frozen'", [r for r in rows if r["frozen"] == "no"]),
         ("no 'mathnotes done'", [r for r in rows if r["mathnotes"] == "no"]),
         ("hashes after the notes not stated as matching", [r for r in rows if r["hash_after_notes"] == "no"]),
         ("inventory rows not 'yes'", [r for r in rows if isinstance(r["inv_not_yes"], int) and r["inv_not_yes"]]),
         ("second reading under 1 minute a page", [r for r in rows if isinstance(r["second_min_pg"], float)
                                                   and r["second_min_pg"] < 1]),
         ("no \\unsure at all", [r for r in rows if r["unsure"] == 0]),
         ("math notes missing sections", [r for r in rows if r["math_sections"] < 6]),
         ("overfull boxes over 2pt", [r for r in rows if isinstance(r["overfull_gt2pt"], int) and r["overfull_gt2pt"]])]
L += ["", "## Flags", ""]
for lab, rs in flags:
    L.append(f"- **{lab}**: {len(rs)}" + (": " + ", ".join(f"{r['id']}" + (f" ({r['unbalanced_pages']})" if lab ==
              'unbalanced page files' else f" ({r['compile_errors']})" if lab == 'compile errors' else '') for r in rs[:40])
              if rs else ""))
md = CW / f"AUDIT_K_RETURNS_{stamp:%Y%m%d}{TAG}.md"
md.write_text("\n".join(L) + "\n", encoding="utf-8")
print(md)
