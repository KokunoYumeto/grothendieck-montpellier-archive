"""Mirror the pequalnp.com fleet's lemma graph, tagged, with cross-links to our work.

Fetches data.pequalnp.com (head, program maps, every lemma record cached by its hash in ../desk/lemma_cache, graveyard,
plan, seats, news), lists the accepted Lean files of brilliant-hq/pequalnp-proofs (git ls-tree on upstream/main of the
clone ../pequalnp-proofs, after a fetch), tags every lemma by topic and by structure, and links each fleet id to the
lines of our own files that mention it. Writes into this folder:
  RESULTS.tsv, RESULTS.json          one row per lemma (statements, status, tags, proof file, our mentions)
  BY_PROGRAM/<program>.md            readable, grouped by status, plain statements
  INDEX_BY_TAG.md                    tag -> lemmas
  OURS_BY_FLEET_ID.md                fleet id -> where our work mentions it
  GRAVEYARD.md, PLAN.md, SEATS.md    the fleet's dead approaches, plan and seats (as published)
  CHANGELOG.md                       appended at every run: new lemmas and status changes since the previous run
Polite: about 0.3 s between requests. usage: python -I -B refresh_fleet_mirror.py
Written 23 Nov 2026 by Claude Opus 5.5 at effort max (session 672ae3a0)."""
import collections, datetime, json, pathlib, re, subprocess, sys, time, urllib.error, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
BASE = "https://data.pequalnp.com/"
HERE = pathlib.Path(__file__).resolve().parent
WORK = HERE.parent
CACHE = WORK / "desk" / "lemma_cache"
CACHE.mkdir(parents=True, exist_ok=True)
CLONE = WORK / "pequalnp-proofs"
UA = {"User-Agent": "pequalnp-reader/1.0"}
NL = chr(10)
LET = {"c": "checked", "j": "conjecture", "w": "in_work", "r": "refuted", "x": "dead", "b": "blocked"}


def get(rel, parse=True):
    # retries with backoff: a single network timeout ended the 21:31 UTC run of 24 Nov 2026
    for attempt in range(5):
        try:
            req = urllib.request.Request(BASE + rel, headers=UA)
            raw = urllib.request.urlopen(req, timeout=60).read()
            time.sleep(0.3)
            return json.loads(raw) if parse else raw.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404 or attempt == 4:
                raise
        except Exception:
            if attempt == 4:
                raise
        time.sleep(5 * (attempt + 1))


# ---------- topic tags: (tag, regex on lower-cased title + plain + formal statement) ----------
TOPICS = [
    ("permanent", r"\bperm|permanent"),
    ("determinant", r"\bdet\b|det_|determinant|detpoly"),
    ("level-space", r"level space|level spaces|perm\(j|stays n!|perm\(j_n|ls\(\d|\blevel\b"),
    ("border-dc", r"border|hasborderdetexpression|orbit closure|orbitclosure|determinantal complexity|\bdc\("),
    ("padding", r"padd"),
    ("gct-obstruction", r"obstruction|mulmuley|occurrence|multiplicit"),
    ("riffle-rank", r"riffle"),
    ("sparse-poly", r"sparse|descartes|wronskian|\bdiv\b|divisible by \(x"),
    ("hessian", r"hessian"),
    ("edge-function", r"edge function|edgefinset|edge fn|\bf_g\b|accepting all edges|graph's edge"),
    ("graph-c4-girth", r"\bc4\b|4-cycle|four-cycle|girth|no 4-cycle|without 4-cycles|c4-free"),
    ("vertex-cover", r"vertex cover|cover number|\btau\b|τ"),
    ("forest-tree", r"\bforest|\btree\b|acyclic|\bstar\b|spider|\bpath\b"),
    ("projective-plane", r"projective plane|incidence|point-line|pg\(2|plane of order|\blines?\b.*\bpoints?\b"),
    ("line-degree", r"line-degree|linedegree|line degree"),
    ("not-gates", r"\bnot gate|not gates|negation|inverter|\bnot ladder|with s not"),
    ("monotone-circuit", r"monotone|\band and or\b|and/or|monotone2|and-or"),
    ("and-count", r"and count|and-count|andcount|number of and gates"),
    ("or-count", r"or count|number of or gates|boolean sum|or gates alone|rectifier"),
    ("last-gate", r"last gate|last-gate|\blgp\b"),
    ("promise-partial", r"promise|partial function|maximal independent|independent set"),
    ("exact-size", r"exact circuit size|least size|hascircuitsize|exactly when s|exact least|exact size|data lane|small values"),
    ("search-witness", r"^search|\bsearch\b|witness|exists a circuit|find seven|find a"),
    ("set-systems", r"set system|cycle rank|sunflower|intersect"),
    ("proof-complexity", r"resolution|refutation|\br\(lin\)|reslin|frege|cutting plane|polynomial calculus|nullstellensatz|proof system|res\("),
    ("pigeonhole", r"pigeon|\bphp\b|bphp"),
    ("sat-cnf", r"\bsat\b|3-sat|cnf|satisfiab|clause"),
    ("algorithm-search", r"candidate \d|decides 3-sat|algorithm|p = np|p=np"),
    ("time-alternation", r"alternation|sigmav|\bsigma_?\d|dtime|ntime|fp3|hlint|speedup|evasion|nlin|alt \d|three rounds of guessing"),
    ("threshold", r"threshold|thr∘thr|thrthr|\bthr\b|majority|\bmaj\b"),
    ("ac0-acc", r"\bac0|\bacc|mod \d|\bmod\b|parity"),
    ("formula", r"\bformula"),
    ("depth", r"\bdepth\b"),
    ("complexity-classes", r"np-complete|\bp is\b|\bnp is\b|exponential time|\bexp\b|nexp|p/poly|ppoly|\bnp\b"),
    ("counting", r"#|counting|count of"),
    ("tensor-rank", r"tensor|\brank\b"),
    ("polynomial-identity", r"identity testing|pit\b|hitting set"),
    ("kneser-codes", r"kneser|schur product|\bcode"),
    ("power-sums", r"power sum|p_2|p_4|p2|p4|fermat"),
    ("quadratic-forms", r"isotropic|quadratic form|bilinear"),
    ("smooth-geometry", r"smooth|bertini|gradient|tangent space|hypersurface|singular point"),
    ("sparse-poly", r"sign change|changes sign|sum of three cubes|two cubes|divides u|binomial"),
    ("tractable", r"tractable"),
    ("sanity-check", r"sanity"),
    ("oracles-relativization", r"oracle|relativ|\bbgs\b|p\^b"),
    ("poly-time-basics", r"polynomial-time|polynomial time|reducib|computable"),
    ("mcsp-natural-proofs", r"mcsp|natural property|natural proof"),
    ("pebbling", r"pebbl"),
    ("subdivision", r"subdivision|thread|\bhub"),
    ("circuit-structure", r"literal partition|minimum complex|pendant bit|borrowed cover|circuit moves|junk drop|low merge|exchange lemma|minimal circuit|readers|essential vector|lift error|aliasing"),
    ("graph-structure", r"peelable|cycle|degree|walk"),
]
TOPIC_RX = [(t, re.compile(rx)) for t, rx in TOPICS]


def struct_tags(d, title):
    tags = []
    t = (title or "").lower()
    if "hard link" in t or "a hard one" in t:
        tags.append("HARD-LINK")
    if t.startswith("target") or "target:" in t or d.get("kind") == "target":
        tags.append("TARGET")
    if t.startswith("search") or "search gap" in t:
        tags.append("SEARCH")
    if "restated" in t or "corrected" in t:
        tags.append("restated")
    if d.get("barrier"):
        tags.append("has-barrier")
    atts = d.get("attempts") or []
    if any(a.get("outcome") == "died" for a in atts):
        tags.append("attempt-died")
    if any((a.get("by") or "").startswith("seat-intake") and a.get("outcome") == "checked" for a in atts):
        tags.append("outside-proof")
    return tags


def proof_files():
    """lemma id -> accepted Lean file on the fleet's main branch."""
    out = {}
    try:
        subprocess.run(["git", "-C", str(CLONE), "fetch", "-q", "upstream"], timeout=180, capture_output=True)
        r = subprocess.run(["git", "-C", str(CLONE), "ls-tree", "-r", "--name-only", "upstream/main", "lean/PEqualNP"],
                           capture_output=True, text=True, timeout=120)
        files = r.stdout.split()
    except Exception as e:
        print("repository listing failed:", e)
        return out
    dirmap = {"Gct": "gct", "MetaComplexity": "meta", "CircuitLowerBounds": "clb", "ProofComplexity": "pcx",
              "Library": "lib", "Search": "alg"}
    for f in files:
        m = re.search(r"/Outside/L_([a-z]+)_(\d+)\.lean$", f)
        if m:
            out.setdefault(f"L-{m.group(1)}-{int(m.group(2)):03d}", f)
            continue
        m = re.search(r"/([A-Za-z]+)/L(\d+)\.lean$", f)
        if m and m.group(1) in dirmap:
            out.setdefault(f"L-{dirmap[m.group(1)]}-{int(m.group(2)):03d}", f)
    return out


OUR_SOURCES = ["*.md", "fleet_map/*.md", "fleet_map/maps/*.md", "mirror/*.md", "mirror/MIRROR_TREE.tsv",
               "mirror/proofs/*.md", "desk/CODEX_TO_CLAUDE_*.md"]
SKIP = {"CALIBRATION.md", "MATCHES.md"}


def our_mentions():
    """fleet id -> list of (file, line number, snippet) from our own files (the joint table: our rows only)."""
    idx = collections.defaultdict(list)
    rx = re.compile(r"L-(gct|meta|clb|pcx|lib|alg)-(\d{3})")
    files = []
    for pat in OUR_SOURCES:
        files += sorted(WORK.glob(pat))
    for f in files:
        if f.name in SKIP or f.parent == HERE:
            continue
        rel = f.relative_to(WORK).as_posix()
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for m in set(rx.findall(line)):
                idx[f"L-{m[0]}-{m[1]}"].append((rel, i, line.strip()[:220]))
    jt = WORK / "fleet_map" / "JOINT_GCT_LEMMA_SPACE.tsv"
    if jt.exists():
        rows = jt.read_text(encoding="utf-8", errors="replace").splitlines()
        head = rows[0].split("\t")
        ci = {h: k for k, h in enumerate(head)}
        for n, line in enumerate(rows[1:], 2):
            c = line.split("\t")
            if len(c) < len(head) or c[ci["side"]] == "swarm":
                continue
            for m in set(rx.findall(c[ci["cross_edges"]])):
                idx[f"L-{m[0]}-{m[1]}"].append(("fleet_map/JOINT_GCT_LEMMA_SPACE.tsv", n,
                                                 (c[ci["id"]] + ": " + c[ci["statement"]])[:220]))
    return idx


def dump_md(name, obj, title):
    """A readable dump of a published fleet file whose layout we do not fix: lists of records become bullet lists."""
    lines = [f"# {title}", "", f"Mirrored from data.pequalnp.com at {NOW}.", ""]

    def walk(o, depth=0):
        pad = "  " * depth
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, (dict, list)):
                    lines.append(f"{pad}- **{k}**")
                    walk(v, depth + 1)
                else:
                    lines.append(f"{pad}- **{k}**: {v}")
        elif isinstance(o, list):
            for v in o:
                if isinstance(v, (dict, list)):
                    lines.append(f"{pad}-")
                    walk(v, depth + 1)
                else:
                    lines.append(f"{pad}- {v}")
        else:
            lines.append(f"{pad}{o}")
    walk(obj)
    (HERE / name).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def main():
    head = get("head.json")
    ov = get(head["files"]["map"])
    pf = proof_files()
    ours = our_mentions()
    rows = []
    for p in ov["programs"]:
        mp = get(p["file"])
        for x in mp["nodes"]:
            lid = "L-%s-%03d" % (p["key"], x[0])
            f = CACHE / f"{lid}.{x[3]}.json"
            if not f.exists():
                try:
                    f.write_text(json.dumps(get(f"data/lemma/{lid}.{x[3]}.json")), encoding="utf-8")
                except Exception as e:
                    print("fail", lid, e)
                    continue
            d = json.loads(f.read_text(encoding="utf-8"))
            title = d.get("title", "")
            plain = d.get("plain_statement") or ""
            formal = d.get("formal_statement") or ""
            text = " ".join([title, plain, formal]).lower()
            topics = [t for t, rx in TOPIC_RX if rx.search(text)]
            status = d.get("status") or LET.get(x[1], x[1])
            atts = d.get("attempts") or []
            last = atts[-1] if atts else {}
            rows.append({
                "id": lid, "program": p["key"], "program_name": d.get("program"), "status": status,
                "status_at": d.get("status_at"), "proposed_at": d.get("proposed_at"), "kind": d.get("kind"),
                "layer": d.get("layer"), "title": title, "plain_statement": plain, "formal_statement": formal,
                "depends_on": d.get("depends_on") or [], "used_by": d.get("used_by") or [],
                "barrier": d.get("barrier"), "seat": d.get("seat"),
                "last_attempt": {k: last.get(k) for k in ("by", "outcome", "when", "ended_at", "why_died")} if last else None,
                "attempt_count": len(atts), "proof_file": pf.get(lid),
                "tags": topics + struct_tags(d, title) + ([f"status:{status}"]),
                "ours": [{"file": a, "line": b, "text": c} for a, b, c in ours.get(lid, [])],
            })
    rows.sort(key=lambda r: (r["program"], r["id"]))
    prev = {}
    pj = HERE / "RESULTS.json"
    if pj.exists():
        try:
            prev = {r["id"]: r["status"] for r in json.loads(pj.read_text(encoding="utf-8"))["lemmas"]}
        except Exception:
            prev = {}
    pj.write_text(json.dumps({"generated": NOW, "fleet_export": head.get("version"), "counters": head.get("counters"),
                              "status_line": head.get("status"), "lemmas": rows}, ensure_ascii=False, indent=0),
                  encoding="utf-8")
    with open(HERE / "RESULTS.tsv", "w", encoding="utf-8", newline="\n") as fh:
        cols = ["id", "program", "status", "status_at", "kind", "tags", "title", "plain_statement", "formal_statement",
                "depends_on", "used_by", "proof_file", "ours_count", "last_attempt_by", "last_outcome"]
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            la = r["last_attempt"] or {}
            vals = [r["id"], r["program"], r["status"], r["status_at"] or "", r["kind"] or "", ",".join(r["tags"]),
                    r["title"], r["plain_statement"], r["formal_statement"], ",".join(r["depends_on"]),
                    ",".join(r["used_by"]), r["proof_file"] or "", str(len(r["ours"])), la.get("by") or "",
                    la.get("outcome") or ""]
            fh.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in vals) + "\n")
    # by program
    (HERE / "BY_PROGRAM").mkdir(exist_ok=True)
    order = ["checked", "conjecture", "in_work", "blocked", "refuted", "retired", "dead"]
    for prog in sorted({r["program"] for r in rows}):
        pr = [r for r in rows if r["program"] == prog]
        cnt = collections.Counter(r["status"] for r in pr)
        out = [f"# Fleet program `{prog}` ({pr[0]['program_name']}): {len(pr)} lemmas", "",
               f"Mirrored {NOW} from fleet export {head.get('version')}. Status counts: {dict(cnt)}.",
               "Each entry: id, status (since), tags, title, plain statement; `proof:` the accepted Lean file; "
               "`ours:` how many lines of our files mention it (see OURS_BY_FLEET_ID.md).", ""]
        for st in order + sorted(set(cnt) - set(order)):
            sel = [r for r in pr if r["status"] == st]
            if not sel:
                continue
            out += [f"## {st} ({len(sel)})", ""]
            for r in sel:
                extra = []
                if r["proof_file"]:
                    extra.append(f"proof: `{r['proof_file']}`")
                if r["ours"]:
                    extra.append(f"ours: {len(r['ours'])}")
                if r["depends_on"]:
                    extra.append("uses " + ", ".join(r["depends_on"]))
                out.append(f"- **{r['id']}** ({(r['status_at'] or '')[:16]}) [{', '.join(t for t in r['tags'] if not t.startswith('status:'))}]"
                           f" {r['title']}" + (f" — {'; '.join(extra)}" if extra else ""))
                if r["plain_statement"] and r["plain_statement"] != r["title"]:
                    out.append(f"  - {r['plain_statement'][:900]}")
            out.append("")
        (HERE / "BY_PROGRAM" / f"{prog}.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    # tag index
    tagidx = collections.defaultdict(list)
    for r in rows:
        for t in r["tags"]:
            tagidx[t].append(r)
    out = [f"# Fleet lemmas by tag ({NOW})", "",
           "Topic tags come from keyword rules over title and statements (refresh_fleet_mirror.py, TOPICS); structural "
           "tags: HARD-LINK, TARGET, SEARCH, restated, has-barrier, attempt-died, outside-proof, status:<s>.", ""]
    for t in sorted(tagidx, key=lambda k: (-len(tagidx[k]), k)):
        sel = tagidx[t]
        c = collections.Counter(r["status"] for r in sel)
        out.append(f"## {t} ({len(sel)}: {dict(c)})")
        out.append(", ".join(f"{r['id']}{'*' if r['status'] == 'checked' else ''}" for r in sel))
        out.append("")
    (HERE / "INDEX_BY_TAG.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    # ours
    out = [f"# Where our work meets the fleet's lemmas ({NOW})", "",
           "For every fleet id mentioned in our files (pequalnp_work: notes, fleet_map program maps, the main session's "
           "field maps in fleet_map/maps/, the mirror tree, Codex's handoffs, our rows of the joint GCT table), the "
           "fleet's status and title, then each mention (file:line and the line).", ""]
    byid = {r["id"]: r for r in rows}
    for lid in sorted(ours, key=lambda k: (k.split("-")[1], k)):
        r = byid.get(lid)
        out.append(f"## {lid} ({r['status'] if r else 'not in the export'}) {r['title'][:160] if r else ''}")
        for a, b, c in ours[lid][:12]:
            out.append(f"- `{a}:{b}` {c}")
        if len(ours[lid]) > 12:
            out.append(f"- ... {len(ours[lid]) - 12} more")
        out.append("")
    (HERE / "OURS_BY_FLEET_ID.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    # published side files
    try:
        gy = get(head["files"]["graveyard"])
        ents = gy.get("entries", []) if isinstance(gy, dict) else gy
        out = [f"# The fleet's graveyard: refuted and dead lemmas ({NOW})", "",
               "Each entry resolved against the mirrored record: id, status, title, and why the last attempt died.", ""]
        for e in ents:
            lid = e[0] if isinstance(e, list) else (e.get("id") if isinstance(e, dict) else str(e))
            r = byid.get(lid)
            if r:
                why = (r["last_attempt"] or {}).get("why_died") or ""
                out.append(f"- **{lid}** ({r['status']}) {r['title']}" + (f" — died: {why[:400]}" if why else ""))
                if r["plain_statement"]:
                    out.append(f"  - {r['plain_statement'][:600]}")
            else:
                out.append(f"- {e}")
        (HERE / "GRAVEYARD.md").write_text(NL.join(out) + NL, encoding="utf-8", newline=NL)
    except Exception as e:
        print("graveyard", e)
    for key, name, title in (("plan", "PLAN.md", "The fleet's plan"), ("seats", "SEATS.md", "The fleet's seats"),
                             ("news", "NEWS.md", "The fleet's news index")):
        try:
            dump_md(name, get(head["files"][key]), title)
        except Exception as e:
            print("side file", key, e)
    # changelog
    cur = {r["id"]: r["status"] for r in rows}
    new = [k for k in cur if k not in prev]
    changed = [(k, prev[k], cur[k]) for k in cur if k in prev and prev[k] != cur[k]]
    with open(HERE / "CHANGELOG.md", "a", encoding="utf-8", newline="\n") as fh:
        fh.write(f"\n## {NOW} (export {head.get('version')}; counters {head.get('counters')})\n")
        if not prev:
            fh.write(f"- first snapshot: {len(cur)} lemmas\n")
        else:
            fh.write(f"- new lemmas ({len(new)}): " + ", ".join(f"{k} [{cur[k]}] {byid[k]['title'][:90]}" for k in new) + "\n")
            fh.write(f"- status changes ({len(changed)}): " + ", ".join(f"{k} {a}->{b}" for k, a, b in changed) + "\n")
        st = head.get("status") or {}
        fh.write(f"- strategy line ({st.get('seat')}, {st.get('at')}): {st.get('text')}\n")
    write_integration(rows, set(new) | {k for k, a, b in changed if b == "checked"}, head)
    print("lemmas", len(rows), "| with proof file", sum(1 for r in rows if r["proof_file"]),
          "| mentioned by us", sum(1 for r in rows if r["ours"]), "| new", len(new), "| changed", len(changed))


# Our lines of work and the fleet tags that feed them (a lemma may serve several lines).
LINES = [
    ("Level spaces and GCT (permanent, determinant, border complexity, obstructions)",
     {"level-space", "permanent", "determinant", "border-dc", "padding", "gct-obstruction", "hessian", "power-sums",
      "kneser-codes", "quadratic-forms", "smooth-geometry", "sparse-poly"}),
    ("Circuits on graphs and planes (edge functions, covers, NOT gates, exact sizes)",
     {"edge-function", "graph-c4-girth", "vertex-cover", "forest-tree", "projective-plane", "line-degree", "not-gates",
      "monotone-circuit", "and-count", "or-count", "last-gate", "promise-partial", "exact-size", "set-systems",
      "circuit-structure", "subdivision", "graph-structure"}),
    ("Proof complexity", {"proof-complexity", "pigeonhole"}),
    ("Time, alternation and the evasion chain", {"time-alternation", "complexity-classes", "oracles-relativization",
                                                 "poly-time-basics", "pebbling"}),
    ("SAT, algorithms and meta-complexity", {"sat-cnf", "algorithm-search", "mcsp-natural-proofs", "counting"}),
    ("Rank, riffle rank and identity testing", {"riffle-rank", "tensor-rank", "polynomial-identity"}),
    ("Circuit classes (AC0, ACC, threshold, formulas, depth)", {"ac0-acc", "threshold", "formula", "depth"}),
]


def write_integration(rows, fresh, head):
    """Checked fleet results grouped by our lines of work, newest first, for use in our notes and prompts."""
    chk = [r for r in rows if r["status"] == "checked"]
    out = [f"# Fleet results to integrate into our work ({NOW})", "",
           "Every Lean-checked lemma of pequalnp.com, grouped by our lines of work (by its tags), newest first. "
           "Statements and definitions are the fleet's: brilliant-hq/pequalnp-proofs, Apache License 2.0; cite the "
           "lemma id and its Lean file. NEW marks results checked since the previous refresh. A lemma can appear under "
           "several lines.", ""]
    for name, tags in LINES:
        sel = [r for r in chk if tags & set(r["tags"])]
        sel.sort(key=lambda r: r["status_at"] or "", reverse=True)
        out += [f"## {name} ({len(sel)} checked)", ""]
        for r in sel:
            mark = "**NEW** " if r["id"] in fresh else ""
            pf = f" — `{r['proof_file']}`" if r["proof_file"] else ""
            out.append(f"- {mark}**{r['id']}** ({(r['status_at'] or '')[:10]}) {r['title']}{pf}")
            if r["plain_statement"] and r["plain_statement"] != r["title"]:
                out.append(f"  - {r['plain_statement'][:700]}")
        out.append("")
    (HERE / "INTEGRATE.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def export_lean():
    """Keep ../fleet_lean an exact export of the fleet's Lean tree at upstream/main (re-exported when it moves)."""
    target = WORK / "fleet_lean"
    rev = subprocess.run(["git", "-C", str(CLONE), "rev-parse", "upstream/main"], capture_output=True, text=True).stdout.strip()
    stamp = target / "UPSTREAM_COMMIT.txt"
    if not rev or (stamp.exists() and stamp.read_text().strip() == rev):
        return
    tmp = WORK / "fleet_lean_new"
    subprocess.run(["rm", "-rf", str(tmp)], timeout=600)
    tmp.mkdir()
    tar = subprocess.run(["git", "-C", str(CLONE), "archive", "--format=tar", "upstream/main", "lean/PEqualNP"],
                         capture_output=True, timeout=600).stdout
    subprocess.run(["tar", "-x", "-C", str(tmp)], input=tar, timeout=600, check=True)
    (tmp / "UPSTREAM_COMMIT.txt").write_text(rev + "\n")
    subprocess.run(["rm", "-rf", str(target)], timeout=600)
    tmp.rename(target)


main()
# 24 Nov 2026: also keep the local Lean export and the table of fleet lemmas named in the main session's intakes
for step in (export_lean, lambda: subprocess.run([sys.executable, "-I", "-B", str(HERE / "intake_fleet_maps.py")],
                                                 timeout=600)):
    try:
        step()
    except Exception as e:
        print("extra step failed:", e)
