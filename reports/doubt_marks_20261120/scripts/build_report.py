"""The doubt-mark report as HTML (20 Nov 2026, main session, Claude Opus 5.5 at effort max). The user, 19 Nov 2026
23:04 UTC: "I need an actual report on all the doubt marks, all their types, all the ways that we've suggested fixing
them, and all their effectiveness, HTML, and it needs to be complete and rigorous"; "Base it on intakes from the more
recent pro runs, including partials." Every number below is computed here from the data files that dm_followup.py,
dm_inventory.py, pilots_vs_sp35.py and hua_offsets.py wrote, and from the returns themselves; none is typed by hand.
python -I -B build_report.py -> ../DOUBT_MARKS_REPORT_20261120.html"""
import collections
import csv
import datetime
import html
import json
import pathlib
import re
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "data"
D = pathlib.Path("<project root>")
T = D / "grothendieck_archive_transcription_20261110"
SPR = T / "second_pass_returns"
PIL = T / "second_pass_claude_pilot_20261119"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%d %b %Y, %H:%M UTC")


def rd(name):
    return list(csv.DictReader(open(DATA / name, encoding="utf-8"), delimiter="\t"))


marks, pages, inv, invp = rd("marks.tsv"), rd("pages.tsv"), rd("inventory_marks.tsv"), rd("inventory_pages.tsv")
pil, dmchk, hoff = rd("pilots_vs_sp35.tsv"), rd("dm01_check.tsv"), rd("hua_offsets.tsv")
runs = json.loads((DATA / "runs.json").read_text(encoding="utf-8"))
yld = json.loads((D / "STATE/SECOND_PASS_YIELD.json").read_text(encoding="utf-8"))
dmd = max(SPR.glob("DM01_*_unzipped"), key=lambda p: re.search(r"(\d{8}T\d{4})Z_unzipped$", p.name).group(1))  # the newest return
_mcp = re.search(r"_(?:checkpoint_(\d+)|final[^_]*)_(\d{8}T\d{4})Z_unzipped$", dmd.name)
dm_cp_time = datetime.datetime.strptime(_mcp.group(2), "%Y%m%dT%H%M").replace(tzinfo=datetime.timezone.utc)
dm_cp_label = (f"checkpoint {int(_mcp.group(1))}" if _mcp.group(1) else "its final") + f", {dm_cp_time:%d %b %H:%M} UTC"
# the ended-run rule of 20 Nov 2026: a run whose newest return is 3 hours old or more has ended at that return
dm_ended = (datetime.datetime.now(datetime.timezone.utc) - dm_cp_time).total_seconds() >= 3 * 3600
dm_dec = list(csv.DictReader(open(dmd / "decisions.tsv", encoding="utf-8"), delimiter="\t"))
dm_met = list(csv.DictReader(open(dmd / "audit/METRICS.tsv", encoding="utf-8"), delimiter="\t"))
dm_oth = list(csv.DictReader(open(dmd / "other_errors.tsv", encoding="utf-8"), delimiter="\t"))
dm_oth_places = len({(o['scan'], o['the reading']) for o in dm_oth})
dm_wf = (dmd / "WORKFLOW.md").read_text(encoding="utf-8")
dm_pat = (dmd / "PATTERNS.md").read_text(encoding="utf-8")
dm_prompt = (T / "doubt_marks_pro_20261119/DM01_1_001-160/PROMPT.md").read_text(encoding="utf-8", errors="replace")
import zipfile  # noqa: E402
_dmz = zipfile.ZipFile(T / "doubt_marks_pro_20261119/DM01_1_001-160/DM01_1_001-160_texts.zip")
dm_total_marks = sum(1 for line in _dmz.read("MARKS.tsv").decode("utf-8", "replace").splitlines()[1:] if line.strip())
wf_steps = re.findall(r"^### (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC) — (.+)$", dm_wf, re.M)
tokens = json.loads((PIL / "TOKENS_20261119.json").read_text(encoding="utf-8"))
e_stats = json.loads((PIL / "E_capped_high/AGENT_STATS_E1.json").read_text(encoding="utf-8"))
f_score = list(csv.DictReader(open(PIL / "F_diff_check/out/SCORE_vs_SP04.tsv", encoding="utf-8"), delimiter="\t"))
f_dec = list(csv.DictReader(open(PIL / "F_diff_check/out/decisions.tsv", encoding="utf-8"), delimiter="\t"))

# ---------------------------------------------------------------- labels
DESIGN_ORDER = [
    ("CLAUDE13", "Claude Opus 5.5 at effort max, block second pass (13 Nov)", "Pro first reading"),
    ("G_LARGE", "GPT-6 Astra (ChatGPT Pro mode), one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov)", "Codex web"),
    ("G_PIECE", "GPT-6 Astra (ChatGPT Pro mode), one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov)", "Codex web"),
    ("G_THREE", "GPT-6 Astra (ChatGPT Pro mode), three readers and a main reader (SP34)", "Codex web"),
    ("G_WF", "GPT-6 Astra (ChatGPT Pro mode), three readers and the reading workflow of 21:07 UTC (SP35)", "Codex web"),
    ("G_DEEP", "GPT-6 Astra (ChatGPT Pro mode), three fresh readers per page, deep zoom (SP36 on)", "Codex web"),
    ("DM01", "GPT-6 Astra (ChatGPT Pro mode), doubt marks only, its own workflow (DM01)", "Pro first reading"),
    ("DM_LIVE", "GPT-6 Astra (ChatGPT Pro mode), live-text doubt marks only, DM01's workflow (DM02 on)", "Claude second pass"),
]


class _Group(dict):
    """20 Nov 2026: every three-reader piece from SP36 on (SP39-SP56 and the remainder pieces SP58 on) is the deep-zoom
    design; every doubt-mark run after DM01 is the live-text design."""

    def __missing__(self, run):
        m = re.match(r"SP(\d+)$", run)
        if m and int(m.group(1)) >= 36:
            return "G_DEEP"
        if re.match(r"DM\d+$", run) and run != "DM01":
            return "DM_LIVE"
        raise KeyError(run)


GROUP = _Group({"CLAUDE13": "CLAUDE13", "SP02": "G_LARGE", "SP04": "G_LARGE", "SP12": "G_LARGE", "SP14": "G_LARGE", "SP31": "G_PIECE",
                "SP32": "G_PIECE", "SP33": "G_PIECE", "SP34": "G_THREE", "SP35": "G_WF", "DM01": "DM01"})
DLABEL = {k: v for k, v, _ in DESIGN_ORDER}
DROUTE = {k: r for k, _, r in DESIGN_ORDER}
ROUTE_LONG = {"Pro first reading": "GPT-6 Astra (ChatGPT Pro mode)", "Codex web": "GPT-6 Astra at reasoning effort max in Codex web",
              "Work": "GPT-6.2 Astra at reasoning effort max in ChatGPT Work", "API (typescripts)": "Claude Opus 5.5 at effort high (Message Batches API), typed pages",
              "Claude second pass": "Claude Opus 5.5 at effort max (13 Nov second pass)", "Pro second pass": "GPT-6 Astra (ChatGPT Pro mode), second pass"}
CONF = {"first reading confirmed", "first reading confirmed (neighbours changed)", "same up to accents, case or punctuation"}
ALT = {"another listed alternative chosen", "another listed alternative chosen (neighbours changed)"}
THIRD = {"a reading not among the alternatives"}
GONE = {"nothing there"}
READ = {"read"}
STILL = {"still doubtful, same reading", "still doubtful, reading changed", "still illegible", "narrowed to a doubtful reading"}
NOAL = {"not aligned (large rewrite here)", "not aligned (mark inside a dropped command)"}
RESOLVED = CONF | ALT | THIRD | GONE | READ
CHANGED = ALT | THIRD | GONE | READ
OUTCOLS = [("C's first reading confirmed", CONF, "#3b8f5a"), ("another of C's alternatives", ALT, "#d08a1e"),
           ("a reading C did not list", THIRD, "#c0392b"), ("removed / illegible read", GONE | READ, "#8e44ad"),
           ("still doubtful (same reading)", {"still doubtful, same reading"}, "#9aa5b1"),
           ("still doubtful (reading changed)", {"still doubtful, reading changed", "narrowed to a doubtful reading"}, "#c3cbd3"),
           ("still illegible", {"still illegible"}, "#6c7a89"), ("not aligned", NOAL, "#e9e3d5")]


def esc(x):
    return html.escape(str(x))


def pct(a, b, d=1):
    return f"{100 * a / b:.{d}f} %" if b else "–"


def num(x):
    return f"{x:,}" if isinstance(x, int) else str(x)


def table(head, rows, cls="", note=None, num_cols=None):
    num_cols = set(range(1, len(head))) if num_cols is None else set(num_cols)
    h = "".join(f"<th{' class=n' if i in num_cols else ''}>{esc(c)}</th>" for i, c in enumerate(head))
    b = "".join("<tr>" + "".join(f"<td{' class=n' if i in num_cols else ''}>{c if isinstance(c, Raw) else esc(num(c))}</td>" for i, c in enumerate(r)) + "</tr>" for r in rows)
    n = f"<p class=tnote>{note}</p>" if note else ""
    return f"<div class='tw {cls}'><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>{n}"


class Raw(str):
    pass


def bar(counter, total):
    if not total:
        return Raw("")
    segs = []
    for lab, keys, col in OUTCOLS:
        v = sum(counter[k] for k in keys)
        if v:
            segs.append(f"<span style='width:{100 * v / total:.2f}%;background:{col}' title='{esc(lab)}: {v} ({100 * v / total:.1f} %)'></span>")
    return Raw(f"<div class=bar>{''.join(segs)}</div>")


LEGEND = Raw("<div class=legend>" + "".join(f"<span><i style='background:{c}'></i>{esc(l)}</span>" for l, _, c in OUTCOLS) + "</div>")


def spearman(xs, ys):
    n = len(xs)
    if n < 5:
        return None

    def rank(v):
        o = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[o[j + 1]] == v[o[i]]:
                j += 1
            for q in range(i, j + 1):
                r[o[q]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = rank(xs), rank(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sx = sum((a - mx) ** 2 for a in rx) ** 0.5
    sy = sum((b - my) ** 2 for b in ry) ** 0.5
    return sxy / (sx * sy) if sx and sy else None


S = []  # the sections, in order
TOC = []


def section(sid, title, body):
    TOC.append((sid, title))
    S.append(f"<section id='{sid}'><h2>{esc(title)}</h2>{body}</section>")


# ================================================================ figures used in several places
n_inv = len(inv)
inv_pages_with = len({(r["cote"], r["scan"]) for r in inv})
kinds_inv = collections.Counter(r["kind"] for r in inv)
n_fu = len(marks)
fu_pages = len(pages)
by_design = collections.defaultdict(collections.Counter)
for m in marks:
    by_design[GROUP[m["run"]]][m["outcome"]] += 1
by_run = collections.defaultdict(collections.Counter)
for m in marks:
    by_run[m["run"]][m["outcome"]] += 1


def rates(c):
    n = sum(c.values())
    res = sum(c[k] for k in RESOLVED)
    ch = sum(c[k] for k in CHANGED)
    return n, res, ch


pro_runs = [r for r in by_run if r.startswith("SP")]
pro_c = collections.Counter()
for r in pro_runs:
    pro_c.update(by_run[r])
pro_n, pro_res, pro_ch = rates(pro_c)
dm_n, dm_res, dm_ch = rates(by_design["DM01"])
cl_n, cl_res, cl_ch = rates(by_design["CLAUDE13"])
in_del = sum(r["in_deleted"] == "1" for r in inv)
del_ratio = {}
for _code, _, _ in DESIGN_ORDER:
    _a = collections.Counter(m["outcome"] for m in marks if GROUP[m["run"]] == _code and m["in_deleted"] == "1")
    _b = collections.Counter(m["outcome"] for m in marks if GROUP[m["run"]] == _code and m["in_deleted"] != "1")
    _na, _ra, _ = rates(_a)
    _nb, _rb, _ = rates(_b)
    if _na and _nb and _rb:
        del_ratio[_code] = (_ra / _na) / (_rb / _nb)
dr_lo, dr_hi = min(del_ratio.values()), max(del_ratio.values())
dm_undec = sum(r["decision"] == "undecided" for r in dm_dec)
# DM01 decisions joined with our context flags (same order on each page: checked by dm01_check.tsv)
dm_marks = [m for m in marks if m["run"] == "DM01"]
_dd, _mm = collections.defaultdict(list), collections.defaultdict(list)
for _d in dm_dec:
    _dd[int(_d['scan'])].append(_d)
for _m in dm_marks:
    _mm[int(_m['scan'])].append(_m)
dm_join = [pair for _s in sorted(_dd) if len(_dd[_s]) == len(_mm.get(_s, [])) for pair in zip(_dd[_s], _mm[_s])]
dm_join_left_out = sorted(_s for _s in _dd if len(_dd[_s]) != len(_mm.get(_s, [])))
dm_undec_del = sum(1 for d, m in dm_join if d["decision"] == "undecided" and m["in_deleted"] == "1")
dm_del = sum(1 for d, m in dm_join if m["in_deleted"] == "1")
# DM01 pace
dm_sec = []
for r in dm_met:
    try:
        a = datetime.datetime.fromisoformat(r["reader_started_utc"].replace(" UTC", "+00:00").replace("Z", "+00:00"))
        b = datetime.datetime.fromisoformat(r["committed_utc"].replace(" UTC", "+00:00").replace("Z", "+00:00"))
        dm_sec.append((int(r["scan"]), int(r["marks"]), (b - a).total_seconds(), int(r["page_views"]), int(r["crop_views"])))
    except Exception:
        pass
dm_prog = (dmd / "progress.log").read_text(encoding="utf-8").splitlines()
dm_t0 = datetime.datetime.strptime(dm_prog[0][:19], "%Y-%m-%d %H:%M:%S")
dm_t1 = max(datetime.datetime.strptime(re.search(r"(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)", l).group(1), "%Y-%m-%d %H:%M:%S") for l in dm_prog if "done" in l)
dm_hours = (dm_t1 - dm_t0).total_seconds() / 3600
dm_rate = len(dm_dec) / dm_hours if dm_hours else 0
dm_left = (dm_total_marks or 0) - len(dm_dec)

# ---------------------------------------------------------------- checked or not yet checked; marks per 100 words by zone
# 20 Nov 2026 (the user): a doubt mark can mean not yet checked, or checked and still doubtful; and the share of marks in
# mathematics says little while most of the text is mathematics, so the marks are counted per 100 words of each zone.
CHK_ORDER = [("Pro second pass", "checked against the scan, still doubtful"), ("doubt-mark run", "checked against the scan, still doubtful"),
             ("struck-out text the doubt-mark run left out", "not yet checked"), ("Claude pass of 13 Nov only", "not yet checked"),
             ("first reading only", "not yet checked")]
chk_c = collections.defaultdict(collections.Counter)
chk_pg = collections.defaultdict(set)
for r in inv:
    _b = r.get("checked_by", "")
    chk_c[_b][r["kind"]] += 1
    chk_c[_b]["struck" if r["in_deleted"] == "1" else "live"] += 1
    chk_pg[_b].add((r["cote"], r["scan"]))


def _nk(b):
    return sum(chk_c[b][k] for k in ("single", "choice", "illegible"))


n_chk = sum(1 for r in inv if r.get("checked") == "yes")
n_unchk = n_inv - n_chk
rows = []
for _b, _lab in CHK_ORDER:
    if not _nk(_b):
        continue
    c = chk_c[_b]
    rows.append([Raw(f"<b>{esc(_lab)}</b>: {esc(_b)}"), len(chk_pg[_b]), c["live"], c["struck"], c["single"], c["choice"], c["illegible"], _nk(_b), pct(_nk(_b), n_inv)])
rows.append(["All", inv_pages_with, n_inv - in_del, in_del, kinds_inv["single"], kinds_inv["choice"], kinds_inv["illegible"], n_inv, pct(n_inv, n_inv)])
t_chk = table(["The mark", "Pages with such a mark", "In live text", "In struck-out text", "Single", "Choice", "Illegible", "All", "Share"], rows,
              note="Checked: the page's text of record is a Pro second pass or a doubt-mark run, so a reader has looked at the place on the scan "
                   "and left the doubt. DM01 took every mark of its pages; the later doubt-mark prompts take the live-text marks only. The pages "
                   "of the 13 Nov Claude pass count as not second-passed (the decision of 20 Nov), so their marks count as not yet checked.")
ZONES = [("prose", "prose"), ("math", "mathematics"), ("diagram", "drawings and diagrams")]


def _grp(base):
    return "checked" if base == "Pro second pass" or base.startswith("doubt marks settled") else "unchecked"


zw = collections.defaultdict(lambda: [0, 0])
for p in invp:
    _g = _grp(p["base"])
    for _zn, _ in ZONES:
        for _sl in ("live", "struck"):
            _w, _l = int(p.get(f"w_{_zn}_{_sl}") or 0), int(p.get(f"l_{_zn}_{_sl}") or 0)
            for _key in ((_g, _zn, _sl), ("all", _zn, _sl), (_g, _zn, "both"), ("all", _zn, "both")):
                zw[_key][0] += _w
                zw[_key][1] += _l
zm = collections.Counter()
for r in inv:
    _g = _grp(r["base"])
    _sl = "struck" if r["in_deleted"] == "1" else "live"
    for _key in ((_g, r.get("zone", ""), _sl), ("all", r.get("zone", ""), _sl), (_g, r.get("zone", ""), "both"), ("all", r.get("zone", ""), "both")):
        zm[_key] += 1
w_all = sum(zw[("all", _zn, "both")][0] for _zn, _ in ZONES)


def per100(g, zn, sl):
    _w = zw[(g, zn, sl)][0]
    return f"{100 * zm[(g, zn, sl)] / _w:.2f}" if _w else "–"


rows = []
for _sl, _slab in (("live", "live text"), ("struck", "struck-out text"), ("both", "all text")):
    for _zn, _zlab in ZONES:
        _w, _l = zw[("all", _zn, _sl)]
        rows.append([Raw(f"<b>{esc(_slab)}</b>") if _zn == "prose" else "", _zlab, _w, pct(_w, w_all), zm[("all", _zn, _sl)], pct(zm[("all", _zn, _sl)], n_inv),
                     per100("all", _zn, _sl), per100("unchecked", _zn, _sl), per100("checked", _zn, _sl),
                     f"{1000 * zm[('all', _zn, _sl)] / _l:.2f}" if _l else "–"])
t_zone = table(["Text", "Zone", "Words", "Share of all words", "Open marks", "Share of all marks", "Marks per 100 words",
                "per 100 words, not yet checked", "per 100 words, after a check", "Marks per 1,000 letters"], rows, num_cols={2, 3, 4, 5, 6, 7, 8, 9},
               note="Words are counted the way the alignment counts them: the whitespace-separated pieces of the text with its LaTeX commands "
                    "written out and each doubt mark written with its first reading, so a formula counts as its symbols and commands "
                    "(<code>$f\\colon X\\to Y$</code> is five words). Letters are the characters of those words. Mathematics is whatever is inside "
                    "<code>$...$</code>, <code>\\[...\\]</code>, <code>\\(...\\)</code> or a display environment; drawings are <code>tikzcd</code> and "
                    "<code>tikzpicture</code>. 'After a check': pages whose text of record is a Pro second pass or a doubt-mark run. In drawings "
                    "most words are drawing code (coordinates, <code>\\draw</code>, <code>node</code>), so their rate does not compare with the "
                    f"other two. The zones hold {100 * (w_all / max(1, sum(int(p['words']) for p in invp)) - 1):.1f} % more words than the "
                    "alignment counts, because a word glued to a formula (<code>d'$X$</code>) counts once on each side.")
_w_math, _mk_math = zw[("all", "math", "both")][0], zm[("all", "math", "both")]
p_chk = f"""<p><b>{n_chk:,} of the open marks ({pct(n_chk, n_inv)}) have been checked against the scan and stayed doubtful</b>
({_nk('Pro second pass'):,} on Pro second passes, {_nk('doubt-mark run'):,} on the pages DM01 finished); <b>{n_unchk:,} ({pct(n_unchk, n_inv)})
have not been checked yet</b>: {_nk('first reading only'):,} on pages with only a first reading and {_nk('Claude pass of 13 Nov only'):,} on the pages of
the 13 Nov Claude pass. The text itself does not tell the two apart; a way to mark a checked doubt is proposed in section 10.</p>
<p><b>Mathematics, per word.</b> {pct(_w_math, w_all)} of the words of the text of record are mathematics and {pct(_mk_math, n_inv)} of the open
marks sit there: per 100 words, {per100('all', 'math', 'both')} marks in mathematics against {per100('all', 'prose', 'both')} in prose (in live text,
{per100('all', 'math', 'live')} against {per100('all', 'prose', 'live')}; section 1).</p>"""

# ================================================================ 0. summary
hua_pool =[m for m in marks if m["run"] != "CLAUDE13" and m["outcome"] in RESOLVED]
def hua_eval(rows, cls):
    rs = [m for m in rows if m["hua"] == cls]
    n = len(rs)
    return n, sum(m["outcome"] in CONF for m in rs), sum(m["outcome"] in ALT for m in rs), sum(m["outcome"] in THIRD | GONE | READ for m in rs), \
        sum(m["final_eq_hua"] in ("yes", "loose") for m in rs)
h_alt = hua_eval(hua_pool, "Hua = C's other alternative")
h_first = hua_eval(hua_pool, "Hua = C's first reading")
h_third = hua_eval(hua_pool, "Hua has a third reading")
cl_alt = hua_eval([m for m in marks if m["run"] == "CLAUDE13" and m["outcome"] in RESOLVED], "Hua = C's other alternative")
inv_hua = collections.Counter(r["hua"] for r in inv)
n_inv_alt = inv_hua["Hua = C's other alternative"]
open_np = [r for r in inv if r["state"] in ("nothing prepared",)]
summary = f"""
<div class=lede>
<p><b>{n_inv:,} doubt marks</b> stand open in the text of record today, on {inv_pages_with:,} of its {len(invp):,} pages:
{kinds_inv['single']:,} single readings marked doubtful (<code>\\unsure{{a}}</code>), {kinds_inv['choice']:,} choices between readings
(<code>\\unsure{{a|b}}</code>) and {kinds_inv['illegible']:,} illegible places (<code>\\illegible{{n}}</code>). Every route marks
its doubts the same way. {in_del:,} of the marks ({pct(in_del, n_inv)}) sit inside struck-out text.</p>
{p_chk}
<p><b>The second passes leave most of the first reading's doubt marks in place.</b> On the {fu_pages:,} pages they have finished
({n_fu:,} marks of witness C), the Pro second passes settled {pct(pro_res, pro_n)} of C's marks, the Claude block pass of 13 Nov
{pct(cl_res, cl_n)}, and the doubt-marks-only run DM01 {pct(dm_res, dm_n)}. Where a mark was settled, C's first reading was
wrong {pct(pro_ch, pro_res)} of the time in the Pro passes and {pct(dm_ch, dm_res)} in DM01.</p>
<p><b>DM01 did real work and built its own method.</b> In {dm_hours * 60:.0f} minutes it recorded a decision on each of the
{len(dm_dec)} marks of {len(dm_met)} pages: it settled {len(dm_dec) - dm_undec}, changed C's reading at
{sum(d['decision'] in ('alternative', 'other') for d in dm_dec)} of them, left {dm_undec} undecided ({dm_undec_del} of these in
struck-out text), and found {dm_oth_places} errors outside the marks. It kept a timed record of its workflow ({len(wf_steps)} entries), with the measured effect of
each change (section 5). At its measured pace the remaining {dm_left:,} marks of cote 1 take about
{dm_left / dm_rate:.0f} hours.</p>
<p><b>Hua's text, at the same place, is a strong sign only when it agrees with C.</b> Where Hua has C's first reading and a
Pro pass settled the mark, the pass confirmed C at {h_first[1]} of {h_first[0]} ({pct(h_first[1], h_first[0])}). Where Hua has
C's other alternative, the Pro passes still kept C's first reading at {h_alt[1]} of {h_alt[0]} ({pct(h_alt[1], h_alt[0])}) and
chose Hua's at {h_alt[2]} ({pct(h_alt[2], h_alt[0])}); the Claude pass of 13 Nov, which settled far fewer marks, went the other
way ({cl_alt[2]} of {cl_alt[0]} for Hua's alternative). No scan has decided between them yet. This bears on
{inv_hua["Hua = C's other alternative"]:,} open marks, the head of the fix queue; Hua is uncertain at the same place at
{inv_hua['Hua also uncertain here']:,} more.</p>
<p><b>{in_del:,} open marks ({pct(in_del, n_inv)}) are inside struck-out text,</b> and every pass settles those less often than marks in live text:
at {100 * dr_lo:.0f}-{100 * dr_hi:.0f} % of the live-text rate, depending on the pass (section 2).</p>
<p><b>Deep zoom:</b> the data so far cannot separate the effect of zoom depth from the page and the design (section 4); the
deep-zoom pieces with fresh readers (SP36, SP37, SP38, SP57) have {sum(1 for p in pages if GROUP[p['run']] == 'G_DEEP')} finished pages
between them.</p>
</div>"""
section("summary", "Summary", summary)

# ================================================================ 1. the marks: types and inventory
by_base = collections.defaultdict(collections.Counter)
pages_base = collections.Counter(r["base"] for r in invp)
pages_base_with = collections.defaultdict(set)
for r in inv:
    by_base[r["base"]][r["kind"]] += 1
    pages_base_with[r["base"]].add((r["cote"], r["scan"]))
rows = []
for b in sorted(by_base, key=lambda x: -sum(by_base[x].values())):
    c = by_base[b]
    n = sum(c.values())
    rows.append([Raw(f"{esc(b)}<br><small>{esc(ROUTE_LONG.get(b, ''))}</small>"), pages_base[b], len(pages_base_with[b]), c["single"], c["choice"], c["illegible"], n,
                 f"{n / pages_base[b]:.1f}" if pages_base[b] else "–"])
rows.append(["All", len(invp), inv_pages_with, kinds_inv["single"], kinds_inv["choice"], kinds_inv["illegible"], n_inv, f"{n_inv / len(invp):.1f}"])
t_base = table(["Base reading of the page (its route)", "Pages", "Pages with a mark", "Single", "Choice", "Illegible", "All marks", "Marks a page"], rows)
by_state = collections.defaultdict(collections.Counter)
for r in inv:
    by_state[r["state"]][r["kind"]] += 1
st_pages = collections.Counter(r["state"] for r in invp)
rows = [[s, st_pages[s], c["single"], c["choice"], c["illegible"], sum(c.values())] for s, c in sorted(by_state.items(), key=lambda kv: -sum(kv[1].values()))]
t_state = table(["Where the page stands (STATE/PAGE_STATE.tsv)", "Pages", "Single", "Choice", "Illegible", "All marks"], rows)
ctx = [("inside struck-out text (\\deleted)", "in_deleted"), ("in a margin note (\\margin)", "in_margin"), ("in an insertion (\\inserted)", "in_inserted"),
       ("in mathematics", "in_math"), ("in a drawing or diagram", "in_diagram")]
rows = []
for lab, key in ctx:
    c = collections.Counter(r["kind"] for r in inv if r[key] == "1")
    n = sum(c.values())
    rows.append([lab, c["single"], c["choice"], c["illegible"], n, pct(n, n_inv)])
t_ctx = table(["Where the mark sits", "Single", "Choice", "Illegible", "All", "Share of all marks"], rows,
              note="A mark can sit in several of these at once (a struck formula in a margin note).")
na = collections.Counter(min(int(r["nalts"]), 4) for r in inv if r["kind"] == "choice")
wl = collections.Counter("1 word" if int(r["words"]) <= 1 else "2-3 words" if int(r["words"]) <= 3 else "4 words or more" for r in inv if r["kind"] != "illegible")
t_shape = table(["Shape", "Marks"], [["choice between 2 readings", na[2]], ["choice between 3 readings", na[3]], ["choice between 4 or more", na[4]]] +
                [[f"first reading of {k}", wl[k]] for k in ("1 word", "2-3 words", "4 words or more")])
cote_c = collections.Counter(r["cote"] for r in inv)
cote_pages = collections.Counter(r["cote"] for r in invp)
cote_np = collections.Counter(r["cote"] for r in inv if r["state"] == "nothing prepared")
rows = [[c, cote_pages[c], v, f"{v / cote_pages[c]:.1f}", cote_np[c]] for c, v in cote_c.most_common(30)]
t_cote = table(["Cote", "Pages in the text of record", "Open marks", "Marks a page", "On pages with nothing prepared"], rows, num_cols={1, 2, 3, 4})
HUA_ORDER = ["Hua = C's first reading", "Hua = C up to accents/case", "Hua = C's other alternative", "Hua has a third reading", "Hua also uncertain here",
             "Hua has nothing here", "Hua has a reading", "Hua not aligned here", "Hua's page does not match (ratio < 0.25)", "no Hua text for the page"]
hk = collections.defaultdict(collections.Counter)
for r in inv:
    hk[r["hua"]][r["kind"]] += 1
rows = [[h, hk[h]["single"], hk[h]["choice"], hk[h]["illegible"], sum(hk[h].values()), pct(sum(hk[h].values()), n_inv)] for h in HUA_ORDER if hk[h]]
# the page-wide match it replaces
try:
    pw = collections.Counter(r["hua"] for r in csv.DictReader(open(D / "STATE/DOUBTS_VS_HUA.tsv", encoding="utf-8"), delimiter="\t"))
except Exception:
    pw = collections.Counter()
t_hua = table(["What Hua's text has at the same place (matched word by word)", "Single", "Choice", "Illegible", "All", "Share"], rows,
              note=("The page-wide match of STATE/doubts_vs_hua.py (a word anywhere on the page), over the pages with nothing prepared, had: " +
                    "; ".join(f"{esc(k)} {v:,}" for k, v in pw.most_common()) + ". The positional match here is stricter: 'Hua = C's first reading' now "
                    "means the same word at the same place.") if pw else None)
mism_pages = len(hoff)
mism_fixed = sum(1 for r in hoff if r["best_offset"])
body = f"""
<p>Every reading route writes its doubts with the same two commands, defined in each route's preamble: <code>\\unsure{{...}}</code>
and <code>\\illegible{{n}}</code>. A <code>|</code> at the top level of <code>\\unsure</code> separates alternatives (<code>\\unsure{{a|b}}</code>,
a <em>choice</em>); without it the one reading is marked doubtful (<code>\\unsure{{a}}</code>, a <em>single</em> mark). A <code>|</code> that leaves an
empty side, as in <code>\\unsure{{g=|f|}}</code>, is an absolute value, not a choice. The question marks <code>??</code> and <code>(?)</code> that
also occur in the texts are not counted: many are Grothendieck's own. The counts are over the text of record
(<code>text_of_record/</code>, the best reading of each of {len(invp):,} pages, La Longue Marche excluded: its edition is its text).</p>
<h3>By route</h3>{t_base}
<h3>By where the page stands</h3>{t_state}
<h3>Checked and still doubtful, or not yet checked</h3>{t_chk}
<h3>By where the mark sits</h3>{t_ctx}
<h3>Marks per 100 words: mathematics, prose, drawings</h3>{t_zone}
<h3>By shape</h3>{t_shape}
<h3>The 30 cotes with the most open marks</h3>{t_cote}
<h3>Against Hua's text at the same place</h3>{t_hua}
<p>On {mism_pages:,} pages Hua's page aligns with ours under 25 %. Trying his pages three either side of the usual one
(his page <i>n</i> is our scan <i>n</i>&nbsp;+&nbsp;1) matched {mism_fixed} of them, so these are not numbering errors: his
text of those pages is laid out or worded differently (<code>data/hua_offsets.tsv</code>).</p>"""
section("inventory", "1. The doubt marks: types and where they are", body)

# ================================================================ 2. what the second passes did with them
rows = []
for code, lab, route in DESIGN_ORDER:
    c = by_design[code]
    n, res, ch = rates(c)
    np_ = len([p for p in pages if GROUP[p["run"]] == code])
    rows.append([Raw(esc(lab)), route, np_, n, bar(c, n), pct(res, n), pct(ch, res), pct(sum(c[k] for k in STILL), n)])
t_design = table(["Second pass", "C (the first reading) by", "Pages finished", "C's marks", "What happened to them", "Settled", "C's first reading wrong, where settled", "Still doubtful"],
                 rows, num_cols={2, 3, 5, 6, 7})
rows = []
for run in ["CLAUDE13"] + sorted(r for r in by_run if r != "CLAUDE13"):
    c = by_run[run]
    n, res, ch = rates(c)
    rinfo = runs.get(run, {})
    rows.append([run, rinfo.get("kind", "13 Nov blocks"), len([p for p in pages if p["run"] == run]), n, bar(c, n), pct(res, n), pct(ch, res),
                 c["first reading confirmed"] + c["first reading confirmed (neighbours changed)"], sum(c[k] for k in ALT), sum(c[k] for k in THIRD), sum(c[k] for k in STILL)])
t_run = table(["Run", "Newest return", "Pages", "Marks", "Outcome", "Settled", "First reading wrong", "Confirmed", "Other alternative", "Unlisted reading", "Still doubtful"],
              rows, num_cols={2, 3, 5, 6, 7, 8, 9, 10})
rows = []
for code, lab, _ in DESIGN_ORDER:
    for k in ("choice", "single", "illegible"):
        c = collections.Counter(m["outcome"] for m in marks if GROUP[m["run"]] == code and m["kind"] == k)
        n, res, ch = rates(c)
        if n:
            rows.append([Raw(esc(lab)) if k == "choice" else "", k, n, pct(res, n), pct(ch, res)])
t_kind = table(["Second pass", "Kind of mark", "Marks", "Settled", "First reading wrong, where settled"], rows, num_cols={2, 3, 4})
rows = []
for code, lab, _ in DESIGN_ORDER:
    for lab2, key in (("in struck-out text", "in_deleted"), ("in mathematics", "in_math"), ("in a margin note", "in_margin")):
        a = collections.Counter(m["outcome"] for m in marks if GROUP[m["run"]] == code and m[key] == "1")
        b = collections.Counter(m["outcome"] for m in marks if GROUP[m["run"]] == code and m[key] != "1")
        na_, ra, _ = rates(a)
        nb_, rb, _ = rates(b)
        if na_:
            rows.append([Raw(esc(lab)) if key == "in_deleted" else "", lab2, na_, pct(ra, na_), nb_, pct(rb, nb_)])
t_ctx2 = table(["Second pass", "Context", "Marks there", "Settled there", "Marks elsewhere", "Settled elsewhere"], rows, num_cols={2, 3, 4, 5})
# Hua at the place against the outcome (Pro passes and DM01; Claude 13 Nov separately)
def hua_table(sel, title):
    rows = []
    for h in HUA_ORDER:
        rs = [m for m in sel if m["hua"] == h]
        if not rs:
            continue
        c = collections.Counter(m["outcome"] for m in rs)
        n, res, ch = rates(c)
        eqh = sum(1 for m in rs if m["outcome"] in RESOLVED and m["final_eq_hua"] in ("yes", "loose"))
        rows.append([h, n, pct(res, n), pct(sum(c[k] for k in CONF), res), pct(sum(c[k] for k in ALT), res), pct(sum(c[k] for k in THIRD | GONE | READ), res),
                     pct(eqh, res)])
    return f"<h4>{esc(title)}</h4>" + table(["What Hua has at the mark", "Marks", "Settled", "of these: C's first", "C's other alternative", "a reading C did not list",
                                              "the pass's reading = Hua's"], rows)
pro_sel = [m for m in marks if m["run"] != "CLAUDE13"]
cl_sel = [m for m in marks if m["run"] == "CLAUDE13"]
y = yld["total"]
ycorr = y.get("C corrected", 0)
y_mark = y.get("  found by C's own doubt mark", 0)
y_diff = y.get("  found by a C-H diff, H right", 0) + y.get("  found by a C-H diff, neither right", 0)
y_none = y.get("  found only by a correcting pass (H agreed with C)", 0) + y.get("  found only by a correcting pass (H has no text there)", 0)
rows = []
for run, c in sorted(yld["per"].items()):
    cc = c.get("C corrected", 0)
    rows.append([run, c.get("rows", 0), cc, c.get("C corrected, high confidence", 0), c.get("  found by C's own doubt mark", 0),
                 c.get("  found by a C-H diff, H right", 0) + c.get("  found by a C-H diff, neither right", 0),
                 c.get("  found only by a correcting pass (H agreed with C)", 0) + c.get("  found only by a correcting pass (H has no text there)", 0)])
rows.append(["All", y.get("rows", 0), ycorr, y.get("C corrected, high confidence", 0), y_mark, y_diff, y_none])
t_yield = table(["Run", "Places ruled in its changes log", "C corrected", "of which high confidence", "at C's own doubt mark", "where Hua differs from C", "neither (only a full pass)"], rows)
pg_d = collections.defaultdict(lambda: collections.Counter())
for p in pages:
    c = pg_d[GROUP[p["run"]]]
    c["pages"] += 1
    for k in ("c_words", "c_marks", "f_marks", "f_new_marks", "unmarked_blocks", "unmarked_trivial"):
        c[k] += int(p[k])
rows = []
for code, lab, _ in DESIGN_ORDER:
    c = pg_d[code]
    n = c["pages"]
    if not n:
        continue
    sub = c["unmarked_blocks"] - c["unmarked_trivial"]
    rows.append([Raw(esc(lab)), n, f"{c['c_words'] / n:.0f}", f"{c['c_marks'] / n:.1f}", f"{c['f_marks'] / n:.1f}", f"{c['f_new_marks'] / n:.1f}",
                 f"{sub / n:.1f}", f"{100 * sub / c['c_words']:.2f}" if c["c_words"] else "–"])
t_unm = table(["Second pass", "Pages", "Words a page (C)", "C's marks a page", "Marks a page after the pass", "New marks a page", "Changes outside the marks a page",
               "per 100 words"], rows, note="Changes outside the marks: blocks of words that differ between C and the final text where neither has a doubt mark, drawings left out, "
               "and leaving out blocks that differ only in accents, case or punctuation. They include notation changes as well as misreadings: they measure how much "
               "a pass rewrote, not how many errors it caught.")
chk = collections.Counter((r["dm_decision"], r["our_outcome"]) for r in dmchk)
agree = sum(v for (a, b), v in chk.items() if (a == "first" and b in CONF) or (a == "alternative" and b in ALT) or (a == "other" and b in THIRD | GONE)
            or (a == "undecided" and b in STILL))
body = f"""
<p><b>How this was measured.</b> For each page a second pass has finished (only the pages its <code>progress.log</code> marks done, so
partial returns count), three texts are lined up word by word: witness C as the pass received it, the pass's final page, and
Hua's page. Each of C's marks is looked up in the final text between the nearest words the two share, and the final reading
there is compared with C's alternatives. Whether a pass was right is not measured here: no scan was read for this report.
The method was checked against DM01, which records its own decision for every mark: of its {len(dmchk)} marks the script
classifies {agree} the same way ({pct(agree, len(dmchk))}). The others are marks glued into one word with a neighbouring mark
that stayed doubtful (<code>data/dm01_check.tsv</code>).</p>
<p>The runs covered: the newest return of every Pro second pass in <code>second_pass_returns/</code> (finals and checkpoints),
DM01's newest checkpoint ({dm_cp_label}), and the Claude block pass of 13 Nov (<code>second_pass/out/</code>, whose C is the Pro first reading).</p>
{LEGEND}
<h3>By design</h3>{t_design}
<h3>By run</h3>{t_run}
<h3>By kind of mark</h3>{t_kind}
<h3>Struck text, mathematics, margins</h3>{t_ctx2}
<h3>Hua's text at the mark, against what the pass did</h3>
<p>Hua's text is an independent reading of the same page. Where it agrees with C's first reading, the Pro passes confirmed C at
{pct(h_first[1], sum(1 for m in hua_pool if m['hua'] == "Hua = C's first reading"))} of the settled marks. Where it has C's other
alternative, they still kept C's first reading at {pct(h_alt[1], h_alt[0])}, while the Claude pass of 13 Nov chose Hua's
alternative at {pct(cl_alt[2], cl_alt[0])} of the few such marks it settled. Either C's first reading is mostly right there and
the Claude pass changed readings it should not have, or the Pro passes lean towards witness C. The two populations also differ
(different first readers, different cotes). Only the scan at a sample of these places can say which.</p>
{hua_table(pro_sel, "Pro second passes and DM01")}{hua_table(cl_sel, "Claude block pass of 13 Nov")}
<p class=tnote>The last column compares the pass's reading at the mark with Hua's, word for word, ignoring accents and case: Hua's
conventions differ from ours in places, so it undercounts agreement.</p>
<h3>Every correction the Pro passes logged, and what pointed at it</h3>
<p>This uses the passes' own changes logs (<code>STATE/second_pass_yield.py</code>), not the alignment: {ycorr:,} corrections of C,
{pct(y_mark, ycorr)} at one of C's doubt marks, {pct(y_diff, ycorr)} where Hua's text differs from C, and {pct(y_none, ycorr)} that only a
full correcting pass found.</p>{t_yield}
<h3>How much each pass rewrote</h3>{t_unm}"""
section("passes", "2. What the second passes did with the doubt marks", body)

# ================================================================ 3. the Pro workflows compared
rows = []
for run in sorted(r for r in by_run if r != "CLAUDE13"):
    ri = runs.get(run, {})
    c = by_run[run]
    n, res, ch = rates(c)
    pp = [p for p in pages if p["run"] == run]
    sub = sum(int(p["unmarked_blocks"]) - int(p["unmarked_trivial"]) for p in pp)
    rows.append([run, Raw(esc(DLABEL[GROUP[run]].split(", ", 1)[1] if ", " in DLABEL[GROUP[run]] else DLABEL[GROUP[run]])), ", ".join(ri.get("cotes", [])), len(pp),
                 ri.get("pages_per_hour") or "–", f"{sum(int(p['c_marks']) for p in pp) / len(pp):.1f}" if pp else "–", pct(res, n),
                 f"{ch / len(pp):.1f}" if pp else "–", f"{sub / len(pp):.1f}" if pp else "–",
                 ri.get("crops_per_done_page") if ri.get("crops_per_done_page") is not None else "–",
                 f"{ri['crop_scale_median']:.1f}" if ri.get("crop_scale_median") else "–", pct(int((ri.get("crop_scale_share_ge4") or 0) * 1000), 1000) if ri.get("crop_scale_share_ge4") is not None else "–",
                 ", ".join(ri.get("crop_sources", [])) or "none"])
t_wf = table(["Run", "Design", "Cotes", "Pages", "Pages an hour", "C's marks a page", "Marks settled", "C's reading changed at a mark, a page",
              "Other changes a page", "Crops a page", "Median zoom", "Crops at 4x or more", "Crop record"], rows, num_cols={3, 4, 5, 6, 7, 8, 9, 10, 11},
             note="Pages an hour: from the run's progress.log, its first line to its last page done. Zoom: output pixels over source pixels, from the crop logs "
             "(SP31 and SP32 logged only their crop images, so their zoom is unknown; SP12 kept no crop record).")
def same_cote(c1, runs_):
    out = []
    for run in runs_:
        c = by_run[run]
        n, res, ch = rates(c)
        pp = [p for p in pages if p["run"] == run]
        out.append([run, len(pp), n, pct(res, n), pct(ch, res), f"{ch / len(pp):.1f}" if pp else "–"])
    return table(["Run", "Pages", "C's marks", "Settled", "First reading wrong, where settled", "Readings changed at marks, a page"], out)
body = f"""
<p>Every Pro second pass so far worked on pages first read in Codex web, so witness C comes from one route throughout. The pieces still
differ in cote, handwriting and density, and the newer designs have few pages, so differences between runs are not effects of
the design alone. The fairest comparisons are on the same cote:</p>
<h3>Cote 156-5: one reader (SP33) against three readers (SP34)</h3>{same_cote('156-5', ['SP33', 'SP34'])}
<h3>Cote 156-3: two one-reader pieces (SP31, SP32)</h3>{same_cote('156-3', ['SP31', 'SP32'])}
<h3>Cote 71: the deep-zoom pieces with fresh readers (SP36, SP37)</h3>{same_cote('71', ['SP36', 'SP37'])}
<h3>All runs</h3>{t_wf}"""
section("workflows", "3. The Pro workflows compared", body)

# ================================================================ 4. deep zoom
def _cpm(scan):
    r = next((x for x in dm_sec if x[0] == scan), None)
    return f"{r[4] / r[1]:.2f}" if r and r[1] else "–"


page_res = collections.defaultdict(lambda: [0, 0, 0])
for m in marks:
    k = (m["run"], m["cote"], m["scan"])
    page_res[k][0] += 1
    page_res[k][1] += m["outcome"] in RESOLVED
    page_res[k][2] += m["outcome"] in CHANGED
rows = []
for run in sorted(r for r in runs if r.startswith(("SP", "DM"))):
    pp = [p for p in pages if p["run"] == run and p.get("crop_scale_med") not in ("", None) and page_res[(run, p["cote"], p["scan"])][0] >= 3]
    if len(pp) < 5:
        continue
    sc = [float(p["crop_scale_med"]) for p in pp]
    cr = [int(p["crops"]) for p in pp]
    rr = [page_res[(run, p["cote"], p["scan"])][1] / page_res[(run, p["cote"], p["scan"])][0] for p in pp]
    chg = [page_res[(run, p["cote"], p["scan"])][2] for p in pp]
    r1, r2, r3 = spearman(sc, rr), spearman(cr, rr), spearman(sc, chg)
    rows.append([run, len(pp), f"{statistics.median(sc):.1f}", f"{statistics.median(cr):.0f}", f"{r1:+.2f}" if r1 is not None else "–", f"{r2:+.2f}" if r2 is not None else "–",
                 f"{r3:+.2f}" if r3 is not None else "–"])
t_zoom = table(["Run", "Pages with crop data and 3+ marks", "Median zoom", "Median crops a page", "Zoom vs share settled", "Crops vs share settled", "Zoom vs readings changed"],
               rows, note="Spearman rank correlations between pages of the same run. +1: always rises together; 0: no relation; -1: opposite.")
across = []
for run in sorted(r for r in runs if r.startswith(("SP", "DM"))):
    ri = runs[run]
    if ri.get("crop_scale_median"):
        n, res, ch = rates(by_run[run])
        across.append((float(ri["crop_scale_median"]), res / n if n else 0, run))
r_across = spearman([a for a, _, _ in across], [b for _, b, _ in across])
# DM01: the box each decision cites, decided against undecided
def box_w(s):
    v = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", s or "")]
    return (v[2] - v[0]) if len(v) == 4 else None
dbw = collections.defaultdict(list)
for d in dm_dec:
    w = box_w(d["crop"])
    if w:
        dbw["undecided" if d["decision"] == "undecided" else "decided"].append(w)
body = f"""
<p>The guess to test: fewer but deeper zooms catch more. Two kinds of evidence exist so far, and neither is a controlled test.</p>
<p><b>Between runs.</b> The median zoom of a run against the share of C's marks it settled, over {len(across)} runs with zoom data:
Spearman {f'{r_across:+.2f}' if r_across is not None else '–'} ({', '.join(f'{r} {a:.1f}x: {100 * b:.0f} %' for a, b, r in sorted(across))}).
The runs differ in cote, design and size, so this cannot isolate the zoom.</p>
<p><b>Within runs, page by page.</b> Pages that got deeper or more crops are the harder pages, so a correlation here runs both ways:
a hard page draws deep crops and also keeps more doubts.</p>{t_zoom}
<p><b>DM01, mark by mark.</b> The crop box each decision cites is {statistics.median(dbw['decided']):.0f} px wide (median) for the
{len(dbw['decided'])} decided marks and {statistics.median(dbw['undecided']):.0f} px for the {len(dbw['undecided'])} undecided ones. DM01 also
reported that grouping neighbouring marks into one shared band crop, with a tight detail crop only for a feature still open, cut its
crops per mark from {_cpm(7)} (scan 7) to {_cpm(8)} (scan 8) (section 5; its pages differ, so it is not a controlled measure).</p>
<p><b>What would settle it.</b> The same pages read twice by the same design, once with crops capped at about 2-3x and once with
tight crops at 8-10x, scored mark by mark against each other and against the scan at the places they disagree. Nothing like this
has run yet; SP36 and SP37 (deep zoom, fresh readers) are the first returns with the deep setting, on cote 71, which no other design has read.</p>"""
section("zoom", "4. Deep zoom: what the data says", body)

# ================================================================ 5. DM01
dec_c = collections.Counter((d["decision"], d["confidence"]) for d in dm_dec)
rows = [[dec, dec_c[(dec, "high")], dec_c[(dec, "medium")], dec_c[(dec, "low")], sum(dec_c[(dec, x)] for x in ("high", "medium", "low"))]
        for dec in ("first", "alternative", "other", "undecided")]
t_dmdec = table(["Decision", "High", "Medium", "Low", "All"], rows)
rows = []
for d, m in dm_join:
    pass
dd = collections.Counter((d["decision"], m["in_deleted"] == "1") for d, m in dm_join)
rows = [[dec, dd[(dec, True)], dd[(dec, False)]] for dec in ("first", "alternative", "other", "undecided")]
t_dmdel = table(["Decision", "Mark in struck-out text", "Mark in live text"], rows)
rows = [[d["id"], d["scan"], Raw(f"<code>{esc(m['mark'][:70])}</code>"), d["decision"], Raw(f"<code>{esc(d['reading'][:50])}</code>"), d["confidence"], d["what the ink shows"][:170]]
        for d, m in dm_join if d["decision"] in ("alternative", "other")]
t_dmch = table(["Mark", "Scan", "C has", "Decision", "DM01 reads", "Confidence", "What the ink shows (its words, shortened)"], rows, num_cols={1})
rows = [[s, mk, f"{sec / 60:.1f}", f"{3600 * mk / sec:.0f}" if sec else "–", pv, cv, f"{cv / mk:.2f}" if mk else "–"] for s, mk, sec, pv, cv in dm_sec]
t_dmmet = table(["Scan", "Marks", "Minutes (reader start to commit)", "Marks an hour", "Page views", "Crop views", "Crops a mark"], rows)
pat_heads = re.findall(r"^### (.+)$", dm_pat, re.M)
oth = "".join(f"<li>scan {esc(o['scan'])}: {esc(o['place'])}: C has <code>{esc(o['the reading'])}</code>; {esc(o['what the ink shows'][:260])}</li>" for o in dm_oth)
body = f"""
<p>DM01 is the run the user proposed on 19 Nov at 21:58 UTC: one long Pro run on the doubt marks of one cote only, with full freedom to
design its own workflow, record it, change it as it goes and measure each change. It covers cote 1 ({dm_total_marks or '?':,} marks on its
pages). Its newest checkpoint ({dm_cp_label}) holds {len(dm_met)} pages, scans {min(s for s, *_ in dm_sec)}-{max(s for s, *_ in dm_sec)},
done between {dm_t0:%H:%M} and {dm_t1:%H:%M} UTC.</p>
<h3>Its decisions</h3>{t_dmdec}
<p>Where it decided, C's first reading held at {sum(d['decision'] == 'first' for d in dm_dec)} marks and was wrong at
{sum(d['decision'] in ('alternative', 'other') for d in dm_dec)}: {sum(d['decision'] == 'alternative' for d in dm_dec)} times another of C's alternatives,
{sum(d['decision'] == 'other' for d in dm_dec)} times a reading C had not listed:</p>{t_dmch}
<p>Most undecided marks are in struck-out text:</p>{t_dmdel}
<h3>Errors it found outside the marks</h3><p>{dm_oth_places} places{'' if dm_oth_places == len(dm_oth) else f' ({len(dm_oth)} rows: some places were logged twice)'}.</p><ul>{oth}</ul>
<h3>Its pace</h3>{t_dmmet}
<p>{len(dm_dec)} marks in {dm_hours * 60:.0f} minutes from its first line to its last page: about {dm_rate:.0f} marks an hour. The
{dm_left:,} marks left on cote 1 would take about {dm_left / dm_rate:.0f} hours at that pace, about {dm_left / dm_rate / 0.75:.0f}
checkpoints.</p>
<h3>Its workflow record (WORKFLOW.md), entry by entry</h3><ol>{''.join(f'<li><b>{esc(t[11:16])} UTC</b>: {esc(s)}</li>' for t, s in wf_steps)}</ol>
<p>What it changed, in its own measured terms (WORKFLOW.md):</p><ul>
<li><b>A fresh reader for every page</b> from scan 4, so that earlier images do not stay in a reader's context.</li>
<li><b>A page's marks split between readers</b> by their number. Its last thresholds (from 19 Nov 23:30 UTC): three readers
at 18 marks or more, two at 6-17, one below 6. Its first were 24, then 30 and 10.</li>
<li><b>Neighbouring marks on one band crop</b>, with a tight crop only for a feature still open.</li>
<li><b>A stopping rule for struck text</b>: once enlarged views and one independent look show no distinguishing stroke, the
doubt stays. On scan 16 four independent re-checks of obscured ink settled nothing more.</li>
<li><b>Independent re-checks only where a plausible competing reading has a visible feature.</b> The abbreviation
"unift" on scans 20-21 was recovered this way.</li>
<li><b>Count the baseline letters before accepting a power or an index</b> (scan 30: A^2 was A^*A).</li>
<li><b>Evidence in one or two sentences a mark</b> (from scan 25), a due-only checkpoint timer, and a staged
coordinator that keeps reader slots free.</li></ul>
<p>It marks every comparison between pages as observed, not controlled: pages differ in density and cancellation. The full
intake of this and the other recent returns is in <code>INTAKES_20261120.md</code>.</p>
<h3>The recurring patterns it recorded (PATTERNS.md)</h3><ul>{''.join(f'<li>{esc(p)}</li>' for p in pat_heads)}</ul>"""
section("dm01", "5. DM01, the doubt-marks-only run", body)

# ================================================================ 6. Pro's own methods and whether they are in the prompts
PD = D / "TO_SEND/PRO/2_Archive_second_passes"
unsent = sorted(p for p in PD.glob("[0-9][0-9]_*/PROMPT.md"))
sent = sorted(p for p in (PD / ".SENT").glob("[0-9][0-9]_SP*/PROMPT.md"))  # the second-pass pieces; DM01 has its own column
METHODS = [  # (method, where it came from, the wording that shows it in a prompt)
    ("Three independent readers of every page, and a main reader who decides", "the user, 19 Nov ~20:26 UTC (SP34 on)",
     r"three (independent |fresh )?(sub-?agents|readers)"),
    ("Fresh readers for every page (no reader carries an earlier page's images)", "the user, 19 Nov 21:11 UTC; DM01 on its own from scan 4",
     r"three fresh sub-agents|three new sub-agents|fresh reader"),
    ("The readers' brief improved from their disagreements, each version kept", "the 21:10 UTC rewrite", r"improve the brief|readers' brief"),
    ("A workflow record for the next runs (brief versions, crops a page, what worked)", "the 21:10 UTC rewrite; DM01", r"_workflow\.md|WORKFLOW\.md"),
    ("Page once, halves once, then one tight crop per open place, never re-cropped", "the reading workflow, 19 Nov 21:07 UTC",
     r"crop each of them once|one crop settles one place|do not crop a decided place again"),
    ("Deep zoom: a few thousand pixels across, contrast raised", "the user, 19 Nov 21:10 UTC", r"thousand pixels"),
    ("C's doubt marks listed as places to decide on the ink", "the two-witness prompts (14 Nov on)",
     r"doubt mark of witness C\W{0,4} is a place to decide|a doubt mark of C"),
    ("Evidence as the visible strokes, with the crop", "the two-witness prompts", r"letters, strokes, lines or marks"),
    ("All three readings listed where the readers differ", "the three-reader rewrite", r"three readings in the record|lists all\s+three readings"),
    ("One notation table kept across the pages, and recurring signs made to agree", "the three-reader rewrite", r"one notation|notation table"),
    ("The transcription frozen by hash (SP31-SP33: before the mathematical context; three-reader prompts: when every page is decided)",
     "SP31-SP33; the three-reader prompts", r"SHA-256|transcription frozen|hashed"),
    ("Witness S: the readings the sweeps decided on the scan", "the 20:5x UTC build", r"witness S"),
    ("Per-reader structured records (JSON: differences, strokes, crop coordinates, a verdict per doubt mark)", "Pro's own, in the SP34 and SP35 returns",
     r"structured record|JSON record|crop coordinates|coordinates of (the|each) crop"),
    ("Decisions applied to the text by a script per page (decide_NNN.py)", "Pro's own, in the SP34 return", r"by script|decide_\d|script that applies"),
    ("Further independent readings where a place stays open, instead of re-cropping", "Pro's own, in the SP34 and SP35 returns",
     r"further independent reading|another independent reading|fourth reader"),
    ("Neighbouring marks read on one shared band crop, a tight crop only for a feature still open", "Pro's own, DM01, 22:36 UTC",
     r"band crop|shared crop|neighbou?ring marks share"),
    ("A stopping rule for struck text (no distinguishing stroke left: keep the doubt, no more crops)", "Pro's own, DM01, 22:29 UTC",
     r"stopping (rule|criterion)"),
    ("A page's marks split between readers by their number (1, 2 or 3 readers)", "Pro's own, DM01, 22:16 UTC",
     r"disjoint (sets|subsets) of marks|split the marks"),
    ("The first readers' recurring misreadings listed for script checks (PATTERNS.md)", "the user's DM design, 21:58 UTC", r"PATTERNS\.md|recurring misreadings"),
]
rows = []
for lab, src, rx in METHODS:
    n_un = sum(1 for p in unsent if re.search(rx, p.read_text(encoding="utf-8", errors="replace"), re.I))
    n_se = sum(1 for p in sent if re.search(rx, p.read_text(encoding="utf-8", errors="replace"), re.I))
    in_dm = bool(re.search(rx, dm_prompt, re.I))
    rows.append([lab, src, f"{n_se} of {len(sent)}", f"{n_un} of {len(unsent)}", "yes" if in_dm else "no"])
t_meth = table(["Method", "Where it came from", "In the sent prompts", "In the unsent prompts", "In DM01's prompt"], rows, num_cols={2, 3},
               note=f"Unsent: the second-pass pieces in TO_SEND/PRO/2_Archive_second_passes ({', '.join(p.parent.name.split('_')[1] for p in unsent)}); sent: the pieces in its .SENT folder ({', '.join(p.parent.name.split('_')[1] for p in sent)}). "
               "A method counts as present when the prompt carries its wording (the pattern in build_report.py); a 'no' for witness S on a piece means its pages had no sweep row.")
body = f"""<p>The methods of the second-pass prompts and the ones Pro invented on its own in its returns, with where each came from and
which prompts carry it, by their wording. Three findings:</p><ul>
<li><b>What Pro invented is in no prompt.</b> The per-reader JSON records with crop coordinates and a verdict on each doubt mark, the
decisions applied by a script per page, and the extra independent readings for places still open (SP34, SP35), and DM01's shared
band crops, stopping rule for struck text and splitting of a page's marks between readers: the prompts carry none of these. The public
METHODOLOGY.md described the first three as the design; it is corrected to say they are what the returns did.</li>
<li><b>The pieces forbid what DM01 does with its readers.</b> The unsent second-pass prompts say "never split the pages among readers":
every page is read three times, independently. DM01 gives each mark one reader and a second only where a new reading competes. The two
answer different questions (three independent readings of everything, against throughput on the marks).</li>
<li><b>The deep zoom, fresh readers, tight crops and the workflow record are in every unsent piece</b> ({len(unsent)} prompts).</li></ul>
{t_meth}"""
section("methods", "6. Pro's own methods, and whether the prompts carry them", body)

# ================================================================ 7. the pilots
rows = []
for r in tokens:
    pilot, role, eff, calls, out, cw, cr, wt = r[:8]
    rows.append([pilot, role, eff, calls, f"{out / 1000:.0f}k", f"{cw / 1000:.0f}k", f"{cr / 1e6:.1f}M", f"{wt / 1e6:.2f}M"])
for aid, s in e_stats.items():
    wt = s["output"] + 0.25 * s["cache_write"] + 0.02 * s["cache_read"] + 0.2 * s["input"]
    rows.append(["E", f"reader {aid[-4:]}", "high", s["calls"], f"{s['output'] / 1000:.0f}k", f"{s['cache_write'] / 1000:.0f}k", f"{s['cache_read'] / 1e6:.1f}M", f"{wt / 1e6:.2f}M"])
t_tok = table(["Pilot", "Agent", "Effort", "Tool calls", "Output", "Cache write", "Cache read", "Weighted (output 1, cache write 0.25, read 0.02, input 0.2)"], rows, num_cols={3, 4, 5, 6, 7})
pa = collections.defaultdict(collections.Counter)
for r in pil:
    a = pa[r["reader"]]
    a["marks"] += 1
    a["res"] += int(r["reader_resolved"])
    a["sp"] += int(r["sp35_resolved"])
    a["same"] += int(r["same_reading"])
    a["both"] += int(r["reader_resolved"]) and int(r["sp35_resolved"])
    a["bothsame"] += int(r["reader_resolved"]) and int(r["sp35_resolved"]) and int(r["same_reading"])
    a.setdefault("scans", 0)
scans = collections.defaultdict(set)
for r in pil:
    scans[r["reader"]].add(r["scan"])
rows = [[who, ", ".join(sorted(scans[who], key=int)), a["marks"], a["res"], a["sp"], a["same"], f"{a['bothsame']} of {a['both']}"] for who, a in pa.items()]
t_pil = table(["Claude reader (Claude Opus 5.5)", "Scans", "C's marks", "Settled by the reader", "Settled by SP35", "Same reading as SP35", "Same, where both settled"], rows,
              num_cols={2, 3, 4, 5})
f_agree = sum(1 for r in f_score if r["agree"] == "True")
f_cnt = collections.Counter(d["decision"].lower() for d in f_dec)
# ---------------------------------------------------------------- the API pilots 1 and 2 (20 Nov 2026; pilot12_*.py)
API = HERE.parent / "pilots_api_20261120"
# Each request's model tag: Claude ("haiku", "haikumax", "sonnet", "opus", ...) or an OpenAI model with its reasoning effort
# appended ("solhigh", "terramax", "lunahigh", ...). Batch prices, $ per million input / output tokens: the claude-api
# skill (Anthropic) and developers.openai.com/api/docs/pricing (OpenAI), read 20 Nov 2026.
_CLAUDE = {"haiku": ("Claude Haiku 5.5", 0.05, 0.25), "haikumax": ("Claude Haiku 5.5", 0.05, 0.25), "sonnet": ("Claude Sonnet 5.5", 1.0, 5.0),
           "sonnetmax": ("Claude Sonnet 5.5", 1.0, 5.0), "opus": ("Claude Opus 5.5", 2.0, 10.0), "opusmax": ("Claude Opus 5.5", 2.0, 10.0)}
_OAI = {"solsixone": ("GPT-6.1 Sol", 1.0, 5.0), "sol": ("GPT-6.2 Sol", 1.0, 5.0), "terra": ("GPT-6.1 Terra", 0.5, 2.5),
        "luna": ("GPT-6 Luna", 0.05, 0.25), "astra": ("GPT-6.2 Astra", 4.0, 20.0)}
_EFFS = ("low", "medium", "high", "xhigh", "max")


def api_model(mt, st):
    """-> (label with effort, input price, output price, sort key)"""
    if mt in _CLAUDE:
        name, pi, po = _CLAUDE[mt]
        eff = "max" if mt.endswith("max") else {"sonnet": "medium", "opus": "high"}.get(mt, "high" if st.endswith("_v2") else "medium")
        return f"{name} at effort {eff}", pi, po, (0, list(_CLAUDE).index(mt))
    for base in sorted(_OAI, key=len, reverse=True):
        if mt.startswith(base) and mt[len(base):] in _EFFS:
            name, pi, po = _OAI[base]
            return f"{name} at reasoning effort {mt[len(base):]}", pi, po, (1, list(_OAI).index(base), _EFFS.index(mt[len(base):]))
    return mt, 0.0, 0.0, (9,)


ZLAB = {"word": "the word crop", "line": "the line", "both": "the line and the word crop"}
api_parts, api_cost_total = [], 0.0
for sd in sorted(API.glob("*/scores.tsv")):
    st = sd.parent.name
    sc = list(csv.DictReader(open(sd, encoding="utf-8"), delimiter="\t"))
    its = list(csv.DictReader(open(sd.parent / "items.tsv", encoding="utf-8"), delimiter="\t"))
    res = [json.loads(line) for line in open(sd.parent / "results.jsonl", encoding="utf-8")]
    cost = collections.defaultdict(float)
    for r in res:
        if r["type"] != "succeeded":
            continue
        mt, z, de, _ = r["custom_id"].split("-", 3)
        u = r["usage"]
        _lab, _pi, _po, _ = api_model(mt, st)
        cost[(mt, z, de)] += (u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)) * \
            _pi / 1e6 + u.get("output_tokens", 0) * _po / 1e6
    api_cost_total += sum(cost.values())
    rows_ = []
    for mt in sorted({r["model"] for r in sc}, key=lambda m: api_model(m, st)[3]):
        for z in ("word", "line", "both"):
            for de in ("p1", "p2"):
                rs = [r for r in sc if (r["model"], r["zoom"], r["design"]) == (mt, z, de)]
                if not rs:
                    continue
                c = collections.Counter(r["verdict"] for r in rs)
                cl = [r for r in rs if r["cls"] == "1" and r["ref"] != "undecided"]
                n = len(rs)
                rows_.append([api_model(mt, st)[0], ZLAB[z], "readings offered" if de == "p1" else "free reading",
                              n, pct(c["right"], n), pct(c["wrong"], n), pct(c["abstained"], n),
                              f"{sum(1 for r in cl if r['verdict'] == 'right')} of {len(cl)}", f"${cost[(mt, z, de)] / max(1, n):.5f}"])
    api_parts.append(f"<h4>Set '{esc(st)}': {len(its)} of DM01's marks ({sum(1 for i in its if i['in_class'] == '1')} where Hua has C's other "
                     f"alternative), {len(res)} requests, ${sum(cost.values()):.2f}</h4>" +
                     table(["Model", "Image", "Prompt", "Marks", "Same as DM01", "Different", "Abstained",
                            "Same as DM01, where Hua has C's other alternative", "Cost per mark"], rows_, num_cols={3, 4, 5, 6, 8}))
API_NOTES_FILE = API / "NOTES.html"
API_PILOTS = ("".join(api_parts) + (API_NOTES_FILE.read_text(encoding="utf-8") if API_NOTES_FILE.is_file() else "")) if api_parts else \
    "<p>Not run yet.</p>"
body = f"""
<p>Six pilots ran on 19 Nov, all Claude Opus 5.5; A-E read cote 156-7 scans 2-6, the pages of Pro's SP35. A: a lead at effort max with
three readers at effort high. B: one reader at max. C: two readers at max who debate. D: two readers at high who debate. E: two readers
at high capped at 10 crops, one page. They were stopped at 21:00 UTC at the user's word, after about 5.5 weekly points; the lead of A
and the debates of C and D had decided nothing by then, so most readers' pages are intermediate (they kept doubts for the debate).
F: one reader at high checking only where C and Hua disagree, cote 156-4 scans 2-9.</p>
<h3>What they cost</h3>{t_tok}
<h3>At C's doubt marks, against SP35 on the same pages</h3>{t_pil}
<p class=tnote>SP35 is Pro's three-reader pass with the reading workflow of 21:07 UTC. "Same reading" counts marks where the reader's text and SP35's agree,
settled or not. Agreement is not accuracy: neither has been checked on the scan at these places.</p>
<h3>Pilot F against SP04</h3>
<p>Of {len(f_score)} places where C and Hua differ that F decided, {f_agree} ({pct(f_agree, len(f_score))}) agree with Pro's SP04. SP04 changed C at
{sum(1 for r in f_score if r['Pro final'] != r['C'])} of them; F decided {f_cnt['c']} for C, {f_cnt['h']} for Hua, {f_cnt['neither']} neither,
{f_cnt['notation']} notation only and {f_cnt['undecidable']} undecidable.</p>
<h3>The API route: pilots 1 and 2 (20 Nov, Message Batches API)</h3>
<p>On 19 Nov at 21:54 UTC the main session had estimated that checking the doubt marks through the API "would come to over $1,000", at
about a cent a place. That figure was an extrapolation from a text-only placement run (Claude Opus 5.5 at effort high, 136 requests,
about $3, standard endpoint), not a test of reading doubt marks. The pilots below are that test, run through the Message Batches API
at half price.</p>
{API_PILOTS}"""
section("pilots", "7. The pilots", body)

# ================================================================ 8. every way suggested
WAYS = [
    ("Settle C's doubt marks in a full second pass by Claude agents, one block of 15-18 scans each", "13 Nov plan", "run 13 Nov: 887 pages",
     f"settled {pct(cl_res, cl_n)} of C's marks on {len([p for p in pages if p['run'] == 'CLAUDE13'])} pages; first reading wrong {pct(cl_ch, cl_res)} where settled",
     "about 0.03-0.05 % of a week a scan (13 Nov meter)"),
    ("Pro second pass, one reader per piece, settling C's marks among everything else", "14 Nov plan", "SP02-SP33 run",
     f"settled {pct(rates(by_design['G_LARGE'])[1], rates(by_design['G_LARGE'])[0])} (large pieces) and {pct(rates(by_design['G_PIECE'])[1], rates(by_design['G_PIECE'])[0])} (pieces of 19 Nov)",
     "Pro run-hours (flat plan)"),
    ("Pro three readers and a main reader", "the user, 19 Nov ~20:26 UTC", "SP34 run; in the pieces SP35-SP57",
     f"settled {pct(rates(by_design['G_THREE'])[1], rates(by_design['G_THREE'])[0])} on {len([p for p in pages if p['run'] == 'SP34'])} pages so far", "5-7 pages an hour"),
    ("The reading workflow: page once, halves once, list what is open, one tight crop per open place", "the user, 19 Nov 21:07 UTC", "SP35 on; in SP36-SP57",
     f"SP35 settled {pct(rates(by_design['G_WF'])[1], rates(by_design['G_WF'])[0])} on {len([p for p in pages if p['run'] == 'SP35'])} pages", "Pro run-hours"),
    ("Deep zoom and fresh readers per page", "the user, 19 Nov 21:10-21:11 UTC", f"SP36-SP62 ({len({p['run'] for p in pages if GROUP[p['run']] == 'G_DEEP'})} of them back)",
     f"settled {pct(rates(by_design['G_DEEP'])[1], rates(by_design['G_DEEP'])[0])} on {len([p for p in pages if GROUP[p['run']] == 'G_DEEP'])} pages so far", "Pro run-hours"),
    ("A long Pro run on the doubt marks only, designing its own workflow", "the user, 19 Nov 21:58 UTC", (f"DM01 ended at {dm_cp_label} (cote 1, {len(dm_met)} pages); DM06 takes the rest" if dm_ended else "DM01 running (cote 1)"),
     f"settled {pct(dm_res, dm_n)}; {dm_rate:.0f} marks an hour; {len(dm_oth)} errors outside the marks", "Pro run-hours"),
    ("Hua's text as the pointer: settle first the marks where Hua has the other alternative", "the fix lists, 19 Nov 21:58 UTC", "listed (STATE/DOUBTS_VS_HUA.tsv); positional list in this report",
     f"where Hua had the other alternative, the passes chose it {pct(h_alt[2], h_alt[0])} of the time ({h_alt[0]} marks); {n_inv_alt:,} such open marks", "a targeted check per mark"),
    ("Diff C against Hua and check only the differences (pilot F)", "the user, 19 Nov", "pilot F run; in the pieces as witness H",
     f"{pct(y_diff, ycorr)} of the logged corrections were at such places; F agreed with SP04 at {pct(f_agree, len(f_score))}", "about 0.014 weekly points a page (F)"),
    ("Give the pieces the lists as places to check first (doubt marks, Hua disagreements, his-error claims, sweep rows)", "the user ('feed that list to Pro')", "witness C's doubt marks and witness S are in the pieces; the his-error list is not",
     f"the cheap lists point at {pct(y_mark + y_diff, ycorr)} of the logged corrections", "script edit, free"),
    ("Check the listed places through the batch APIs, each image once (pilot G)", "the user, 19 Nov", "not run", "not measured", "API dollars (Batch only)"),
    ("Claude agents reading whole pages (pilots A-E)", "the user, 19 Nov 20:31 UTC", "stopped 21:00 UTC",
     "on SP35's pages they settled far fewer of C's marks than SP35 (section 7)", "0.15-0.5 weekly points a page"),
    ("A fresh Work reading (GPT-6.2 Astra at reasoning effort max) and a diff", "18 Nov plan", "229 folders built, held", "not measured", "about 286 Work-hours"),
    ("Work correcting the first reading against the scan", "the user, 19 Nov", "needs a pilot", "not measured", "Work time"),
    ("Script checks of the first readers' recurring misreadings across the archive", "DM01's PATTERNS.md (the user's design)", f"{len(pat_heads)} patterns so far, none applied", "not measured", "script, free"),
    ("A local open-weights model trained on our errors and their fixes, on the RTX 4080 SUPER", "the user, 19 Nov 22:57 UTC", "an idea; not built", "not measured", "GPU time"),
]
t_ways = table(["Way", "Suggested", "State", "What it reached (measured here)", "Cost"], [list(w) for w in WAYS], num_cols=set())
section("ways", "8. Every way suggested to settle the doubt marks", f"<p>Each way, who proposed it and when, how far it has gone, and what this report measured for it.</p>{t_ways}")

# ================================================================ 9b. intakes: live against struck text, run by run
_rows = []
for _run in sorted(r for r in by_run if r != "CLAUDE13") + ["CLAUDE13"]:
    _ri = runs.get(_run, {})
    _rs = [m for m in marks if m["run"] == _run]
    _cells = []
    for _d in ("0", "1"):
        _sel = collections.Counter(m["outcome"] for m in _rs if m["in_deleted"] == _d)
        _n, _res, _ch = rates(_sel)
        _cells += [_n, pct(_res, _n), pct(_ch, _res)]
    _rows.append([_run, _ri.get("kind", "13 Nov blocks"), _ri.get("pages_done", len({(m['cote'], m['scan']) for m in _rs}))] + _cells)
t_intake = table(["Run", "Newest return", "Pages done", "Live-text marks", "settled", "first reading wrong", "Struck-text marks", "settled",
                  "first reading wrong"], _rows, num_cols={2, 3, 4, 5, 6, 7, 8})
body = f"""<p>The returns themselves are the pilots: each design ran on real pages, and each recorded its own method. Their intake
(each return's workflow file, README and progress log, with the measurements of this report) is in
<code>INTAKES_20261120.md</code>. A run whose newest return is 3 hours old or more counts as ended (the user, 20 Nov).</p>
<p>Split by where the mark sits, the doubt-marks-only run settles by far the most live-text marks, and struck-out text resists
every design:</p>{t_intake}"""
section("intakes", "9. The intakes: what each return did", body)

# ================================================================ 9a. what follows (for the user's decision)
def _n_open(cls, state=None):
    return sum(1 for r in inv if r["hua"] == cls and (state is None or r["state"] == state))
body = f"""<p>These follow from the measurements above. None is done; each is for your decision.</p><ol>
<li><b>Mark a checked doubt in the text itself</b> (your point of 20 Nov; a change of convention, for your decision). Today
<code>\\unsure{{a|b}}</code> means both "not yet checked" and "checked, still doubtful": the split in section 1 is inferred from where
a page's text of record came from, and is lost once pages are merged or edited. Proposal: an optional argument naming the check,
<code>\\unsure[DM01]{{a|b}}</code> ("DM01 looked at this place on the scan and could not decide"), written by every second pass and
doubt-mark run on each mark it leaves; a mark without it has not been checked. The preamble's definition becomes
<code>\\newcommand{{\\unsure}}[2][]{{...}}</code>, so every existing text compiles unchanged, and the readers can show checked doubts in
their own colour; the scripts (alignment, inventory, STATE) read the argument. Alternatives: a new command such as
<code>\\doubtful{{...}}</code> (does not say who checked), or the decisions kept only in each run's <code>MARKS.tsv</code> (no change
to the text, but the link to the mark breaks when the page is edited).</li>
<li><b>Decide who is right where Hua has the other alternative</b> (approved, 20 Nov). Where they settled such a mark, the Pro passes kept C at {pct(h_alt[1], h_alt[0])};
the 13 Nov Claude pass went with Hua at {pct(cl_alt[2], cl_alt[0])} ({cl_alt[2]} of {cl_alt[0]}). A scan check of a random sample of these marks (60-100 of the {_n_open("Hua = C's other alternative"):,} open ones,
a doubt-marks run like DM01 or pilot G on the batch APIs) would say which, and so how to treat the whole class.</li>
<li><b>Struck-out text</b> (the user, 20 Nov: live-text marks first, struck-out text after). {in_del:,} of the open marks ({pct(in_del, n_inv)}) are inside deletions. Every pass settles them at {100 * dr_lo:.0f}-{100 * dr_hi:.0f} % of
the rate of live text, and DM01 left {dm_undec_del} of its {dm_undec} undecided marks there. The prompts could let a reader keep a doubt in
struck text after one look (DM01's stopping rule) and spend the time on live text.</li>
<li><b>Carry DM01's own methods into the next DM prompts</b> (shared band crops, the stopping rule, a page's marks split by their number),
and Pro's SP34/SP35 inventions (per-reader records, decisions applied by script) into the unsent pieces, if wanted: a script edit of the prompts.</li>
<li><b>The pages of the 13 Nov Claude pass no longer count as second-passed</b> (the user, 20 Nov: "if they're not second
pass, they're not second pass"): {pct(cl_n - cl_res, cl_n)} of C's marks on them are still open ({sum(1 for r in inv if r['base'] == 'Claude second pass'):,} marks on {len(pages_base_with['Claude second pass']):,} pages). A
doubt-marks run on those pages would settle them.</li>
<li><b>Test deep zoom properly</b> (approved, cheaply, 20 Nov): the same pages read twice by the same design, crops capped at 2-3x against tight crops at 8-10x, scored
mark by mark (section 4).</li></ol>"""
section("next", "10. What follows, for your decision", body)

# ================================================================ 9. method, data, limits
body = f"""<ul>
<li><b>Scripts</b> (in <code>reports_20261120/doubt_marks/scripts/</code>): <code>texalign.py</code> (tokens, marks, alignment), <code>dm_followup.py</code>
(the second passes), <code>dm_inventory.py</code> (the open marks), <code>pilots_vs_sp35.py</code>, <code>hua_offsets.py</code>, <code>build_report.py</code> (this page).
Data in <code>data/</code>: <code>marks.tsv</code> (one row per mark of C on a finished page), <code>pages.tsv</code>, <code>runs.json</code>,
<code>inventory_marks.tsv</code> (one row per open mark), <code>inventory_pages.tsv</code>, <code>dm01_check.tsv</code>, <code>pilots_vs_sp35.tsv</code>, <code>hua_offsets.tsv</code>.</li>
<li><b>Validated</b> against DM01's own decisions: {agree} of {len(dmchk)} marks classified the same way.</li>
<li><b>Mathematics</b> is decided by the delimiters before a mark. Fixed on 20 Nov: a delimiter counts only after an even run of
backslashes, so the line break with spacing <code>\\\\[2pt]</code> (1,025 times on 582 pages) no longer opens a display, and
<code>$$...$$</code> counts as a display. Before the fix, marks after such a line break counted as mathematics; every count on this page uses
the fixed rule.</li>
<li><b>Not measured:</b> whether a pass's reading is right. That needs the scan at the places where readings disagree, or a reference text.</li>
<li><b>Hua's conventions</b> differ from ours in places, so exact agreement with Hua is undercounted.</li>
<li><b>Small samples:</b> SP34-SP37 and DM01 have {sum(1 for p in pages if p['run'] in ('SP34', 'SP35', 'SP36', 'SP37', 'DM01'))} finished pages between them.</li>
<li><b>Pages an hour</b> come from each run's progress.log and include its reading of the research notes where the prompt asks for them.</li>
</ul>"""
section("method", "11. Method, data and limits", body)

CSS = """
:root{--bg:#f7f6f2;--fg:#1d2329;--muted:#5d6670;--line:#d9d6cc;--card:#ffffff;--accent:#2f5d8a;--code:#efece4;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15191d;--fg:#e6e3dc;--muted:#a2a9b1;--line:#333a41;--card:#1c2227;--accent:#8db6df;--code:#262c32;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#15191d;--fg:#e6e3dc;--muted:#a2a9b1;--line:#333a41;--card:#1c2227;--accent:#8db6df;--code:#262c32;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font:15px/1.55 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;margin:0}
main{max-width:1180px;margin:0 auto;padding-block:28px 80px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1{font:600 30px/1.2 "Space Grotesk",Inter,system-ui,sans-serif;margin:0 0 6px;text-wrap:balance}
h2{font:600 22px/1.25 "Space Grotesk",Inter,system-ui,sans-serif;margin:44px 0 12px;padding-top:12px;border-top:1px solid var(--line);text-wrap:balance}
h3{font:600 16px/1.3 Inter,system-ui,sans-serif;margin:26px 0 8px}h4{font:600 14px/1.3 Inter,system-ui,sans-serif;margin:18px 0 6px;color:var(--muted)}
p,li{max-width:78ch}.sub{color:var(--muted);margin:0 0 18px}code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.92em}
nav{display:flex;flex-wrap:wrap;gap:6px 14px;margin:14px 0 8px;font-size:14px}nav a{color:var(--accent);text-decoration:none}nav a:hover{text-decoration:underline}
.lede{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:6px 20px}
.tw{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:8px;margin:8px 0}
table{border-collapse:collapse;width:100%;font-size:13.5px}th,td{padding:6px 10px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}
th{font-weight:600;color:var(--muted);background:var(--card);position:sticky;top:0}td.n,th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr:last-child td{border-bottom:none}small{color:var(--muted)}.tnote{color:var(--muted);font-size:13px;margin:4px 0 12px}
.bar{display:flex;width:220px;height:14px;border-radius:3px;overflow:hidden;background:var(--line)}.bar span{display:block;height:100%}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12.5px;color:var(--muted);margin:10px 0}.legend i{display:inline-block;width:11px;height:11px;border-radius:2px;margin-right:5px;vertical-align:-1px}
"""
page = f"""<title>Doubt Mark Report</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Space+Grotesk:wght@600&display=swap">
<style>{CSS}</style>
<main>
<h1>The doubt marks of the Montpellier archive transcription</h1>
<p class=sub>Generated {NOW} by <code>build_report.py</code> (Claude Opus 5.5 at effort max, main session), from the returns filed by then:
the newest return of each Pro second pass (partial returns included), DM01's newest checkpoint ({dm_cp_label}), the Claude block pass of 13 Nov, and the
text of record. Every number is computed from the files.</p>
<nav>{''.join(f"<a href='#{i}'>{esc(t)}</a>" for i, t in TOC)}</nav>
{''.join(S)}
</main>"""
out = HERE.parent / "DOUBT_MARKS_REPORT_20261120.html"
out.write_text(page, encoding="utf-8")
print("wrote", out, len(page), "chars;", len(S), "sections")

# 20 Nov 2026: a copy to share outside the project (the user links the report in a reply to Michel Hua): proposals and
# decisions are ours, not attributed to a person; section 10 is the next steps, not a list addressed to the reader; the
# usage meter is spelled out; no hardware details. Every replacement must apply, and nothing addressed to the user may stay.
PUB = [("DM01 is the run the user proposed on", "DM01 is the run we proposed on"),
       ("<td>the user (&#x27;feed that list to Pro&#x27;)</td>", "<td>our proposal, 19 Nov</td>"),
       ("<td>the user&#x27;s DM design, 21:58 UTC</td>", "<td>the DM design, 19 Nov 21:58 UTC</td>"),
       ("DM01&#x27;s PATTERNS.md (the user&#x27;s design)", "DM01&#x27;s PATTERNS.md (the DM design)"),
       ("<td>the user, ", "<td>"),
       ("at the user's word", "at our decision"),
       ("(the user, 20 Nov).", "(20 Nov)."),
       ("(the user, 20 Nov: live-text marks first, struck-out text after)", "(decided 20 Nov: live-text marks first, struck-out text after)"),
       (re.compile(r'\(the user, 20 Nov: "if they.re not second\s+pass, they.re not second pass"\)'), "(decided 20 Nov)"),
       ("on the RTX 4080 SUPER", "on a local GPU"),
       ("10. What follows, for your decision", "10. Next steps"),
       ("None is done; each is for your decision.", "None is done yet."),
       ("(your point of 20 Nov; a change of convention, for your decision)", "(a change of convention, not yet decided)"),
       ("after about 5.5 weekly points", "after about 5.5 % of the weekly Claude usage limit"),
       (" weekly points a page", " % of the weekly Claude usage limit a page"),
       ("% of a week a scan (13 Nov meter)", "% of the weekly Claude usage limit a scan"),
       ("<th>Where it came from</th>", "<th>Proposed</th>"),
       ("(Claude Opus 5.5 at effort max, main session)", "(Claude Opus 5.5 at effort max)")]
if "--public" in sys.argv:
    pub = page
    for a, b in PUB:
        n = len(a.findall(pub)) if isinstance(a, re.Pattern) else pub.count(a)
        if not n:
            sys.exit(f"public copy: replacement did not apply: {a}")
        pub = a.sub(b, pub) if isinstance(a, re.Pattern) else pub.replace(a, b)
    left = [m.group(0) for m in re.finditer(r".{0,70}(the user|\byour\b|RTX|weekly points).{0,40}", pub)]
    if left:
        sys.exit("public copy: still addressed to the user:\n" + "\n".join(left))
    pout = HERE.parent / "DOUBT_MARKS_REPORT_20261120_public.html"
    pout.write_text(pub, encoding="utf-8")
    print("wrote", pout, len(pub), "chars")
