"""Pilot folders for a third pass by GPT-6.2 Sol (ChatGPT Work) on the two control folders, 17 Nov 2026 (night).

Written by Claude Opus 5.5 at effort high, for the main session. Plan: codex_web_20261113/PILOT_PLAN_THIRD_PASS.md.

What it builds, for CTRL-148 (cote 148, scans 44-58) and CTRL-145 (cote 145, scans 20-34):
- third_pass_pilot/second_pass_before_controls/<ID>/: the Claude second pass as it stood before the control runs
  corrected it (148: addenda A and B reversed; 145: rows 43-55 of its changes file reversed). This is the realistic
  input of a third pass: on the thousands of other pages no control run has corrected the second pass.
- third_pass_pilot/keys/<ID>_known_second_pass_errors.tsv: the places where that text was wrong, found by the control
  runs and confirmed on the scans (the reference for "known errors caught").
- third_pass_pilot/keys/V3-<ID>_places_key.tsv: the V3 places with the withheld second-pass reading.
- third_pass_pilot/build/<VAR>-<ID>/: PROMPT.md, PREAMBLE.tex, <VAR>-<ID>_scans.zip (unsplit).
Then split for Chrome with: python -I -B tools/split_for_chrome.py --dst drag_split_third third_pass_pilot/build <IDs>

Variants: V1 full independent transcription without the notes (for Sol at max); V2 the same (for Sol at high); V3 blind
reading of the places the second pass marked doubtful or changed; V4 check of the scans against the second pass's text.
usage: python -I -B tools/build_third_pass_pilot.py
"""
import csv
import hashlib
import io
import pathlib
import re
import shutil
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_handwriting_k as K  # noqa: E402
import reconcile_readings as RR  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
CW = K.CW
SP = CW.parent / "second_pass"
WORK = CW / "third_pass_pilot"
BUILD = WORK / "build"
KEYS = WORK / "keys"
PRE = WORK / "second_pass_before_controls"
CTRL = {c["id"]: c for c in K.CONTROLS}

SRC = {
    "CTRL-148": dict(dir=SP / "out/MPL_148_029-072", file="MPL_148_029-072_148_scan%03d.tex",
                     changes=SP / "out/MPL_148_029-072/MPL_148_029-072_148-044-148-058_changes.md",
                     add=[("A", SP / "work/MPL_148_029-072_148-044-148-058/apply_addendum.py"),
                          ("B", SP / "work/MPL_148_029-072_148-044-148-058/apply_addendum2.py")]),
    "CTRL-145": dict(dir=SP / "out/MPL_145", file="MPL_145_145_scan%03d.tex",
                     changes=SP / "out/MPL_145/MPL_145_145-020-145-038_changes.md"),
}
# 145: rows 43-55 of MPL_145_145-020-145-038_changes.md (after the CTRL-145 verdict), as (scan, now, before)
ROWS145 = [
    (20, r"$\sigma_0,\rho$ en fait avec relations", r"$\sigma_0,\rho$ avec les relations", "rows 43-44"),
    (21, r"les opérations des $\tilde\sigma_a$", r"les opérations des $\tilde\sigma_i$", "row 45"),
    (21, r"$\tilde\sigma_a$ est au dessus", r"$\tilde\sigma_{\unsure{i|0}}$ est au dessus", "row 46"),
    (21, r"$\varphi(\overset{\deleted{\sim}}{\dot\sigma}_a)$", r"$\varphi(\tilde\sigma_{\unsure{i|0}})$", "row 47"),
    (21, r"$\deleted{l}l_\infty$ en $l_1^{-1}$", r"$l_\infty$ en $l_1^{-1}$", "row 48"),
    (21, r"remonter $\dot\tau$ en trois manières, à savoir", r"revenir à nos trois \unsure{miroirs}, \unsure{d.} par",
     "rows 49-52"),
    (27, r"}_{=\unsure{\mathfrak S_3|\mathcal S_3}}", r"}_{\unsure{\mathfrak S_3|\mathcal S_3}}", "row 53"),
    (28, r"est le remontage correspondant", r"est le scindage correspondant", "row 54"),
    (30, r"\tilde\sigma_\infty$ $\longrightarrow$}", r"\tilde\sigma_\infty$}", "row 55"),
]
# 148, second addendum: the "majority" rows B7-B12 (two of three model readings, not settled by the ink)
MAJORITY148 = [(54, "repères"), (52, "importante"), (49, "ici"), (48, "d'échanger"), (48, "directe"),
               (56, r"\unsure{\widetilde\Sigma|\Sigma}")]


def addendum_pairs(path):
    src = path.read_text(encoding="utf-8").split("\nn_rep = 0")[0]
    ns = {}
    exec(compile(src, str(path), "exec"), ns)  # defines DST, F and R only
    return ns["R"]


def first_reading(s):
    return [t[0] for t in RR.tokens(s)]


def before_controls(cid):
    """{scan: text before the control corrections}, list of known errors."""
    c, s = CTRL[cid], SRC[cid]
    now = {n: (s["dir"] / (s["file"] % n)).read_text(encoding="utf-8") for n in c["scans"]}
    pre = dict(now)
    pairs = []  # (scan, before, now, source)
    if cid == "CTRL-148":
        for tag, path in reversed(s["add"]):
            R = addendum_pairs(path)
            for n in sorted(R):
                for k, (old, new) in enumerate(reversed(R[n])):
                    assert pre[n].count(new) == 1, (cid, tag, n, new[:60])
                    pre[n] = pre[n].replace(new, old)
                    src = f"addendum {tag}, scan {n:03d}, pair {len(R[n]) - k}"
                    if tag == "B" and any(m == n and key in new for m, key in MAJORITY148):
                        src += " (majority of three model readings, not settled by the ink)"
                    pairs.append((n, old, new, src))
    else:
        for n, new, old, src in ROWS145:
            assert pre[n].count(new) == 1, (cid, n, new)
            pre[n] = pre[n].replace(new, old)
            pairs.append((n, old, new, src + " of the changes file"))
    known = []
    for n, old, new, src in pairs:
        i = pre[n].find(old)
        kind = "wrong first reading" if first_reading(old) != first_reading(new) else "alternative or mark only"
        known.append(dict(scan=n, line=RR.line_of(pre[n], i), start=i, end=i + len(old), before=old, now=new,
                          kind=kind, source=src))
    return pre, sorted(known, key=lambda k: (k["scan"], k["start"]))


def change_rows(cid):
    """(scan, [lines], [codes]) for the rows of the second pass's own changes table (before any control)."""
    t = SRC[cid]["changes"].read_text(encoding="utf-8")
    if cid == "CTRL-148":
        t = t.split("## Changes", 1)[1].split("\n## ", 1)[0]
    else:
        t = t.split("| # | Scan, place | Before |", 1)[0]
    out = []
    for line in t.splitlines():
        if not re.match(r"\| \d+ \|", line):
            continue
        cells = [x.strip() for x in re.split(r"(?<!\\)\|", line)]
        if cid == "CTRL-148":
            scan, place, corr = int(re.search(r"\d+", cells[2]).group(0)), cells[3], cells[5]
        else:
            scan, place, corr = int(re.search(r"\d+", cells[2]).group(0)), cells[2], cells[4]
        if scan not in CTRL[cid]["scans"]:
            continue
        lines = []
        for a, b in re.findall(r"\b[lL]\.?\s?(\d+)(?:\s?[-–]\s?(\d+))?", place):
            lines += list(range(int(a), int(b or a) + 1))
        codes = [c.replace(r"\|", "|").strip() for c in re.findall(r"`([^`]+)`", corr)]
        out.append((scan, lines, [c for c in codes if len(c) >= 2], cells[1]))
    return out


def places(cid, pre):
    """V3 places: every doubt mark and every change of the second pass, as spans of the pre-control text."""
    spans = {n: [] for n in pre}
    for n, t in pre.items():
        for m in re.finditer(r"\\(unsure|illegible)\{", t):
            s, e = m.start(), RR.brace_end(t, m.end() - 1)
            w = re.search(r"\\(deleted|inserted)\{$", t[:s])
            if w and t[e:e + 1] == "}":
                s, e = w.start(), e + 1
            spans[n].append([s, e, "doubt"])
    unlocated = []
    for n, lines, codes, row in change_rows(cid):
        t = pre[n]
        got = False
        for code in codes:
            for m in re.finditer(re.escape(code), t):
                ln = RR.line_of(t, m.start())
                if not lines or min(lines) - 2 <= ln <= max(lines) + 2:
                    spans[n].append([m.start(), m.end(), "changed"])
                    got = True
        if not got:  # fall back to the whole lines named in the row
            for ln in lines or []:
                ls = t.split("\n")
                if ln <= len(ls) and ls[ln - 1].strip():
                    a = sum(len(x) + 1 for x in ls[:ln - 1])
                    spans[n].append([a, a + len(ls[ln - 1]), "changed (whole line)"])
                    got = True
        if not got:
            unlocated.append((n, row))
    out = []
    for n in sorted(spans):
        merged = []
        for s, e, k in sorted(spans[n]):
            # overlapping places, or places with only a few spaces or punctuation marks between them, are one place
            if merged and (s < merged[-1][1] or re.fullmatch(r"[\s,;:.]{0,3}", pre[n][merged[-1][1]:s])):
                merged[-1][1] = max(merged[-1][1], e)
                if k not in merged[-1][2]:
                    merged[-1][2] += "+" + k
            else:
                merged.append([s, e, k])
        out += [(n, s, e, k) for s, e, k in merged]
    return out, unlocated


def thirds(frac):
    hint = [name for name, a, b in (("s1", 0, .38), ("s2", .30, .70), ("s3", .62, 1.01)) if a <= frac < b]
    return " or ".join(hint)


def place_table(cid, pre, plist):
    rows, key = [], []
    tags = {}
    for k, (n, s, e, kind) in enumerate(plist, 1):
        tags[(n, s)] = f"P{k:03d}"
    for k, (n, s, e, kind) in enumerate(plist, 1):
        t = pre[n]
        page =[(s2, e2, tags[(n, s2)]) for (m, s2, e2, _) in plist if m == n]
        # masked text of the page, and where this place's tag sits in it
        buf, last, here = [], 0, 0
        for s2, e2, tag in sorted(page):
            buf.append(t[last:s2])
            if s2 == s:
                here = sum(len(x) for x in buf)
            buf.append(f"[[{tag}]]")
            last = e2
        buf.append(t[last:])
        mt = "".join(buf)
        tag = f"[[P{k:03d}]]"
        before = mt[max(0, here - 110):here]
        after = mt[here + len(tag):here + len(tag) + 110]
        fix = lambda x: re.sub(r"\s+", " ", x.replace("\t", " ")).strip()
        nlines = t.count("\n") + 1
        frac = RR.line_of(t, s) / nlines
        rows.append([f"P{k:03d}", f"{n:03d}", thirds(frac), fix(before), fix(after)])
        key.append([f"P{k:03d}", f"{n:03d}", RR.line_of(t, s), kind, fix(t[s:e])])
    return rows, key


def tsv(rows, head):
    b = io.StringIO()
    w = csv.writer(b, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    w.writerow(head)
    w.writerows(rows)
    return b.getvalue()


# ---------------------------------------------------------------- prompts

CKPT = ("**Checkpoints that survive a disconnection.** Once every hour of work, save a checkpoint ZIP of everything "
        "in `out/` so far to the user's Library, or wherever files survive the loss of the execution environment, "
        "named `{ID}_checkpoint_NN.zip` with NN counting up from 01; never overwrite an earlier checkpoint. Save "
        "checkpoints once an hour and at no other time. Leave the attached scans out of it: we have them. A checkpoint "
        "is never a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip "
        "holds the current deliverables and documentation; earlier checkpoints are not copied into it. Work that is "
        "in no checkpoint is lost.")

# (C) of claude_tools/PROCEDURE_UPDATE_20261117.md, in the Codex wording of PROMPT_TEMPLATE_HANDWRITING_K.md, for a
# task without notes: the statements are those the reading itself checks, uses or refutes
CHECK = ("**Check events.** For every statement your work checks, uses or refutes (a claim of his, by its scan and "
         "line), record its check events in `out/CHECK_EVENTS.tsv`, one row per event: statement id, date, who "
         "(model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate "
         "/ used and rechecked in this run / carried as background without fault found / refuted, with the refined "
         "statement's id), outcome. Give each event the type of what actually happened, neither more nor less: "
         "reading a statement while transcribing it is not a check of it. Write \"none\" under the header if there "
         "is no such event.")


def add_check(t):
    """the K template's paragraph (C), reworded for a task without notes; or a new one before the deliverables."""
    k = re.search(r"\*\*Check events\.\*\*.*?(?=\n\n## What to deliver)", t, re.S)
    para = wrap(CHECK)
    if k:
        return t[:k.start()] + para + t[k.end():]
    i = t.index("## What to deliver")
    return t[:i] + para + "\n\n" + t[i:]


def wrap(p, indent=""):
    import textwrap
    return "\n".join(textwrap.wrap(p, 118, initial_indent=indent, subsequent_indent=indent, break_long_words=False,
                                   break_on_hyphens=False))


def cut(t, a, b):
    """the text from marker a (included) to marker b (excluded)."""
    i = t.index(a)
    return t[i:t.index(b, i)]


def sub1(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)


def prompt_v1(base, vid):
    t = base
    m6 = cut(t, "6. **A second reading of every page, as a second reader.**", "7. **Assemble and check.**")
    new6 = wrap(
        "6. **A second reading of every page, as a second reader.** When every page is done, read each page again from "
        "the start against its three thirds. This is a full reading, not a skim: in an earlier series a \"second "
        "reading\" of 11-35 seconds per page found none of its six errors; a page needs several minutes. For each page, "
        "**first** read the crops line by line and note, before you open the page file, every accent and every word "
        "that looks misspelled or unusual, as you see it in the crop; **then** open the page file and compare. Check "
        "every display and inline formula symbol by symbol, every i and j in an index or exponent, every handwritten "
        "correction on a typed page, every margin note (read again in its own direction, letter by letter), every "
        "struck word or block and every word you wrote as live text that has any line near it, and every "
        "double-struck or script candidate. Correct, or mark doubt. Record the second reading in `out/" + vid +
        "_audit.md`, one short section per page: its start and end time (UTC) and every change made, as `before -> "
        "after` (or \"no change\"). Do not copy out the lists of words, formulas and marks you checked: the checking is "
        "the work, and the record holds only the changes. Then append `scan NNN audited <current UTC time>` to "
        "`out/progress.log`.").replace("\n", "\n   ", 0)
    new6 = new6.replace("\n", "\n   ") + "\n"
    t = t.replace(m6, new6)
    m8 = cut(t, "8. **The mathematical notes, after the freeze.**", "9. **If time or context runs short.**")
    t = t.replace(m8, "8. **Deliver.** Make `" + vid + "_out.zip` of the whole `out/` folder and offer it as a "
                  "download. This task has no\n   mathematical notes and no notes file: write none.\n")
    t = sub1(t, "each read twice, then the mathematical notes.", "each read twice.")
    t = sub1(t, "This task is long by design:", wrap(CKPT.replace("{ID}", vid)) + "\n\nThis task is long by design:")
    d4 = cut(t, "4. `" + vid + "_audit.md`", "\n7. `progress.log`.")
    t = t.replace(d4, "4. `" + vid + "_audit.md`, the record of the second reading (method 6): per page its times and "
                  "its changes.")
    t = sub1(t, "\n7. `progress.log`.", "\n5. `progress.log`.")
    t = sub1(t, "the times of `transcription frozen` and\n`mathnotes done`, whether the hashes still matched after the "
             "notes, and any page", "the time of `transcription frozen`, and any page")
    left = [w for w in ("mathnotes", "mathematical notes", "_notes.md") if w in t.replace(
        "This task has no\n   mathematical notes", "")]
    assert not left, left
    return t


def shared_blocks(base):
    images = cut(base, "The attached zip `", "**Look at every image yourself**")
    look = cut(base, "**Look at every image yourself**", "**The task is a complete transcription")
    rules = cut(base, "## Absolute rules", "## The attached draft")
    return images, look, rules


def prompt_v3(base, vid, c, row, n_places, scans_with):
    images, look, rules = shared_blocks(base)
    images = images.replace("for every scan page N", "for every scan page N that has a place to read")
    S = K.B.ranges(scans_with)
    return f"""**This file is the task: carry it out in full, now. The other attached files are its materials.**

# Reading task {vid}: Alexander Grothendieck's papers, Montpellier archive, cote {c['cote']}, {n_places} places on {len(scans_with)} scan pages

This is a reading of **selected places**, not a whole transcription. The pages are scans {S} of the file
`{c['cote']}.pdf` of the Montpellier archive, "{row['title']}" ({row['date']}): his handwritten working notes, in
French, with formulas, insertions, margin notes and struck passages.

**The places.** `places/{vid}_places.tsv` in the zip lists {n_places} places. Each is a short stretch of a page (a
word, a few words, a symbol, an index, a formula, sometimes a whole line) that earlier readers found hard. For each
place it gives the scan, the third of the page where it most probably stands (`s1`, `s2`, `s3`), and the text just
before and just after it as an earlier reader transcribed it, in LaTeX; other places inside that text appear as
`[[Pnnn]]`. **The place itself is withheld: you read it from the ink alone.** The context can be wrong in a detail;
use it only to find the place, never as a reading.

{images}{look}The rules and the two sections below were written for whole transcriptions. They apply to every reading you write
here: the same macros, the same care. There is no attached draft in this task. Where they speak of the doubts
file (deliverable 2), use the `ink` column of your answer file.

{rules}## Method

1. Unpack `{vid}_scans.zip` into your working folder and check its images against `MANIFEST.tsv` (names and
   SHA-256). Create the folder `out/` beside them. Read nothing but the attached files; do not search the web. Write
   the current time (UTC) as the first line of `out/progress.log`.
2. **Read each place, in order.** Open the whole page of its scan, then the third named in the list. Find the place
   from the context before and after it; if it is not in that third, look in the neighbouring thirds and on the whole
   page. Then read the place, from where the "before" text ends to where the "after" text begins, nothing more and
   nothing less: every word letter by letter, every formula symbol by symbol, every accent, index, exponent, struck
   or inserted mark. Write it in LaTeX with the macros of rules 4 and 6: `\\deleted{{...}}` for what is struck,
   `\\inserted{{...}}` for an insertion, `\\unsure{{a|b}}` where the ink does not decide between readings (your first
   choice first), `\\illegible{{n}}` for what you cannot read. If nothing stands there, write `(nothing)`.
3. After the last place of a scan, append `scan NNN done <current UTC time>` to `out/progress.log`.
4. **A second reading of every place.** When all places are read, read each place again in the ink before you look
   at your first answer; then compare, and correct or mark doubt. Note every change in the `ink` column, as
   `second reading: a -> b`. Append `second reading done <current UTC time>` to `out/progress.log`.
5. Make `{vid}_out.zip` of the whole `out/` folder and offer it as a download.

{wrap(CKPT.replace("{ID}", vid))}

Every one of the {n_places} places is read, from the ink, twice. Work through all of them completely; do not stop at
a sample, and do not ask whether to continue.

## What to deliver (all in `out/`, zipped as `{vid}_out.zip` and offered as a download at the end)

1. `{vid}_places_read.tsv`, UTF-8, tab-separated, with the header line
   `place	scan	reading	confidence	found	ink` and one line for every place of the list, in its order:
   - `reading`: the place in LaTeX, as the ink shows it;
   - `confidence`: high, medium or low;
   - `found`: yes, or no if you could not locate the place (then say in `ink` where you looked);
   - `ink`: a few words on what the strokes show that decides the reading, or why it stays undecided.
2. `progress.log`.

Your final message: the download link of `{vid}_out.zip`, the number of places read, how many were not found, how
many readings are high, medium and low, and how many changed at the second reading.
"""


def prompt_v4(base, vid, c, row):
    images, look, rules = shared_blocks(base)
    S = K.B.ranges(c["scans"])
    return f"""**This file is the task: carry it out in full, now. The other attached files are its materials.**

# Checking task {vid}: Alexander Grothendieck's papers, Montpellier archive, cote {c['cote']}, {len(c['scans'])} scan pages against a transcription

The pages are scans {S} of the file `{c['cote']}.pdf` of the Montpellier archive, "{row['title']}" ({row['date']}):
his handwritten working notes, in French, with formulas, insertions, margin notes and struck passages.

**The transcription to check.** Under `reading/` the zip holds a diplomatic LaTeX transcription of the same pages,
one file per page, `reading/{vid}_reading_pNNN.tex`. One reader made it and a second reader checked it on the scans.
It still contains errors, and the ones that remain are the kind that survive a check: a plausible word that fits the
sense in place of the written one, a struck mark read as live, a small sign or condition left out, a wrong index or
exponent, a missing or wrong accent, a doubt mark where the ink in fact decides, a confident reading where it does
not. **Your task is to find them: check the transcription against the ink, page by page and line by line, and list
every place where the ink disagrees with it.** A word you accept because it reads well is exactly where the risk is:
accept a word only when you have seen its letters in the ink. The transcription is the text you check, never a source
for a reading: every reading you write comes from the ink.

{images}{look}The rules and the two sections below were written for whole transcriptions. They say how this hand is read and how a
reading is written: use them for every reading you give in your flags. There is no attached draft in this task
(the transcription under `reading/` is not one). Where they speak of the doubts file (deliverable 2), use the
`evidence` column of your flags file. Do not correct his slips or his grammar: a slip on the page stays (rule 2), and
you flag only where the transcription differs from the ink.

{rules}## Method

1. Unpack `{vid}_scans.zip` into your working folder and check its images against `MANIFEST.tsv` (names and
   SHA-256). Create the folder `out/` beside them. Read nothing but the attached files; do not search the web. Write
   the current time (UTC) as the first line of `out/progress.log`.
2. **For each page, in order:** look at the whole page, then at its three thirds; then go through its reading file
   line by line, each line against the ink: every word letter by letter, every formula symbol by symbol, every accent,
   index and exponent, every struck or inserted mark, every margin note in its own direction. Write one line in the
   flags file for every place where they differ: a wrong word, sign, index or accent; something on the page that is
   missing from the transcription; something in the transcription that is not on the page; a struck mark written as
   live or a live one written as struck; a doubt mark (`\\unsure`, `\\illegible`) that the ink settles; a confident
   reading where the ink does not decide between candidates.
3. After each page, append `scan NNN checked <current UTC time>, K flags` to `out/progress.log`, K being the number of
   flags on that page (it can be 0; a page with no flag has still been read line by line).
4. **A second look at every flag.** When all pages are checked, look at the ink of each flag again and confirm it or
   withdraw it; a withdrawn flag stays in the file with the status `withdrawn`. Append `second look done <current
   UTC time>` to `out/progress.log`.
5. Make `{vid}_out.zip` of the whole `out/` folder and offer it as a download.

{wrap(CKPT.replace("{ID}", vid))}

Every line of the {len(c['scans'])} pages is checked against the ink. Work through all of it completely; do not stop
at a sample, and do not ask whether to continue.

## What to deliver (all in `out/`, zipped as `{vid}_out.zip` and offered as a download at the end)

1. `{vid}_flags.tsv`, UTF-8, tab-separated, with the header line
   `scan	line	transcription	ink_reading	kind	confidence	evidence	status` and one line per flag:
   - `line`: the line number in the reading file;
   - `transcription`: the text of the transcription at the place, copied exactly;
   - `ink_reading`: what the ink shows there, in LaTeX with the macros of the rules (`\\unsure{{a|b}}` where it does
     not decide);
   - `kind`: wrong word, wrong sign, index or exponent, accent, struck read as live, live read as struck, missing,
     added, doubt settled, doubt needed, or placement;
   - `confidence`: high, medium or low;
   - `evidence`: what the strokes show;
   - `status`: kept or withdrawn.
2. `progress.log`.

Do not rewrite the transcription and do not deliver a corrected copy of it: the flags are the result.

Your final message: the download link of `{vid}_out.zip`, the number of flags kept and withdrawn per page, and the
total.
"""


# ---------------------------------------------------------------- build

def scans_zip(cid, vid, keep_scans, extra):
    src = CW / "done" / cid / f"{cid}_scans.zip"
    out = BUILD / vid / f"{vid}_scans.zip"
    with zipfile.ZipFile(src) as z, zipfile.ZipFile(out, "w", zipfile.ZIP_STORED) as o:
        man = z.read("MANIFEST.tsv").decode("utf-8").splitlines()
        keep = [man[0]]
        for line in man[1:]:
            f = line.split("\t")
            if int(f[4]) in keep_scans:
                keep.append("\t".join([f[0].replace(cid + "_", vid + "_", 1)] + f[1:]))
        o.writestr("MANIFEST.tsv", "\n".join(keep) + "\n")
        for name in z.namelist():
            m = re.search(r"scan(\d{3})", name)
            if name != "MANIFEST.tsv" and m and int(m.group(1)) in keep_scans:
                o.writestr(name.replace(cid + "_", vid + "_", 1), z.read(name))
        for name, data in extra.items():
            o.writestr(name, data)
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None
        names = set(z.namelist())
        for line in z.read("MANIFEST.tsv").decode("utf-8").splitlines()[1:]:
            f = line.split("\t")
            assert f[0] in names and hashlib.sha256(z.read(f[0])).hexdigest() == f[2], f[0]
    return out


def main():
    for d in (BUILD, KEYS, PRE):
        d.mkdir(parents=True, exist_ok=True)
    report = []
    for cid, c in CTRL.items():
        row = K.B.row(c["cote"])
        pre, known = before_controls(cid)
        (PRE / cid).mkdir(exist_ok=True)
        for n, t in pre.items():
            (PRE / cid / (SRC[cid]["file"] % n)).write_bytes(t.encode("utf-8"))
        (KEYS / f"{cid}_known_second_pass_errors.tsv").write_text(tsv(
            [[f"{k['scan']:03d}", k["line"], k["kind"], k["before"].replace("\n", " "), k["now"].replace("\n", " "),
              k["source"]] for k in known],
            ["scan", "line_in_reading", "kind", "second_pass_had", "corrected_on_the_scan", "source"]), encoding="utf-8")
        plist, unlocated = places(cid, pre)
        prow, pkey = place_table(cid, pre, plist)
        covered = 0
        for k in known:
            hit = [p for p in plist if p[0] == k["scan"] and p[1] < k["end"] and k["start"] < p[2]]
            k["v3"] = ",".join(f"P{plist.index(p) + 1:03d}" for p in hit)
            covered += bool(hit)
        (KEYS / f"V3-{cid}_places_key.tsv").write_text(tsv(
            [r + [",".join(f"{k['scan']:03d}:{k['line']}" for k in known if pr[0] in k["v3"].split(","))]
             for r, pr in zip(pkey, prow)],
            ["place", "scan", "line_in_reading", "why_chosen", "second_pass_reading_withheld", "known_error_at"]),
            encoding="utf-8")
        wrong = [k for k in known if k["kind"] == "wrong first reading"]
        report.append(f"{cid}: {len(known)} known second-pass errors ({len(wrong)} wrong first readings), "
                      f"{covered} of them inside a V3 place ({sum(bool(k['v3']) for k in wrong)} of the wrong first "
                      f"readings); {len(plist)} V3 places; change rows not located: {unlocated}")
        base_cid = K.make_prompt(c, [])
        scans_with = sorted({p[0] for p in plist})
        for var in ("V1", "V2", "V3", "V4"):
            vid = f"{var}-{cid}"
            d = BUILD / vid
            if d.exists():
                shutil.rmtree(d)
            d.mkdir(parents=True)
            base = base_cid.replace(cid, vid)
            extra, keep = {}, set(c["scans"])
            if var in ("V1", "V2"):
                t = prompt_v1(base, vid)
            elif var == "V3":
                t = prompt_v3(base, vid, c, row, len(plist), scans_with)
                extra[f"places/{vid}_places.tsv"] = tsv(prow, ["place", "scan", "third", "before", "after"]).encode()
                keep = set(scans_with)
            else:
                t = prompt_v4(base, vid, c, row)
                for n, txt in pre.items():
                    extra[f"reading/{vid}_reading_p{n:03d}.tex"] = txt.encode("utf-8")
            t = add_check(t)
            assert "CTRL-1" not in t.replace(vid, ""), vid
            assert "your notes" not in t and t.count("CHECK_EVENTS.tsv") == 1, vid
            if var in ("V3", "V4"):
                t = t.replace("Make `" + vid + "_out.zip` of the whole", "Write `out/CHECK_EVENTS.tsv` (below). Make `"
                              + vid + "_out.zip` of the whole", 1)
            (d / "PROMPT.md").write_bytes(t.encode("utf-8"))
            shutil.copy2(CW / "done" / cid / "PREAMBLE.tex", d / "PREAMBLE.tex")
            z = scans_zip(cid, vid, keep, extra)
            report.append(f"  {vid}: PROMPT.md {len(t):,} chars, zip {z.stat().st_size / 1e6:.1f} MB")
    print("\n".join(report))
    (WORK / "BUILD_REPORT.txt").write_text("\n".join(report) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
