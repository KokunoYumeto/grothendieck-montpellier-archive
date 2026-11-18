"""Build the Stage A topic-dossier prompts (18 Nov 2026): one text-only ChatGPT Pro prompt per topic of the Montpellier
archive (large topics in parts by cote), consolidating the research notes of the returned Pro transcription packages.
Template: STAGE_A_TEMPLATE.md. Plan: second_pass/PLAN_WORKING_THROUGH_PRO_20261118.md, section 1a; task file
Documents/task_notes/stage_a_dossiers.md.

Per prompt folder SA<NN>_<slug>/ (flat, for upload): PROMPT.md, SA<NN>_notes.zip, SA<NN>_texts.zip (split into parts
under 8.95 MB when larger), SA<NN>_PROMPT.zip, README.md. Index: STAGE_A_PACKAGES.tsv.
usage: python -I -B build_stage_a.py [--dry]
Written by the main session (Claude Opus 5.5 at effort max), 18 Nov 2026."""
import collections, csv, io, json, pathlib, re, subprocess, sys, zipfile

sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path("C:/Users/user/Documents")
T = D / "grothendieck_archive_transcription_20261110"
OUT = T / "stage_a_20261118"
RET = T / "returns"
CW = T / "codex_web_20261113"
SP = T / "second_pass" / "out"
API = T / "api_typescripts_20261112"
TEMPLATE = OUT / "STAGE_A_TEMPLATE.md"
LINT = D / "claude_tools" / "push_rule_pro_prompts.py"
LIM = 8_950_000
CHUNK = 620_000      # notes bytes per prompt (about 1-2 hours of Pro work)
SMALL = 200_000      # topics under this are grouped
GROUP = 450_000      # up to this many notes bytes per group of small topics
DRY = "--dry" in sys.argv

rows = json.load(open(D / "reports_20261117/archive_report_data.json", encoding="utf-8"))["rows"]
R = {str(r["cote"]): r for r in rows}

# horizontal first: the topics the vertical work never touched, then Pursuing Stacks, then the Longue Marche
ORDER = ["topologie combinatoire", "motifs", "De Rham", "stratifi", "Séminaire de Géométrie", "Picard", "Cristaux",
         "Courbes elliptiques", "Descentes", "Variétés abéliennes", "Jacobiennes", "Esquisse", "géométrie des formes",
         "enseignement", "Éléments de Géométrie", "RECHERCHE", "Dossiers rassemblés", "Pursuing stacks (",
         "Autour de Pursuing", "Longue Marche"]
API_DIRS = {"24": ["ega_v_cote24_blass"], "25": ["ega_v_cote25"], "119": ["esquisse", "cote119_rest"],
            "129": ["montreal_seminar_129"], "162-5": ["tapis_de_quillen_162-5"]}


def cote_key(c):
    m = re.match(r"(\d+)(?:-(\d+))?", c)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (9999, 0)


def cotes_of(pkg):
    m = re.match(r"MPL_(.+)$", pkg)
    cs = []
    if m:
        for t in m.group(1).split("_"):
            for c in t.split("+"):
                if c in R:
                    cs.append(c)
    return list(dict.fromkeys(cs))


def topic_rank(tp):
    for i, k in enumerate(ORDER):
        if k.lower() in tp.lower():
            return i
    return len(ORDER)


def entries_of(text):
    parts = re.split(r"(?m)^### ", text)
    out = []
    for n, part in enumerate(parts[1:], 1):
        head = part.splitlines()[0].strip() if part.strip() else ""
        km = re.search(r"\*\*Kind:\*\*\s*([^\n]+)", part)
        scans = sorted(set(int(x) for x in re.findall(r"scans?\s*0*(\d{1,3})\b", part, re.I)))
        out.append((n, head, (km.group(1).strip() if km else ""), scans))
    return out


finals = []
for nf in sorted(RET.glob("*_unzipped/*_notes.md")):
    d = nf.parent.name
    if "checkpoint" in d.lower():
        continue
    pkg = d[: -len("_unzipped")]
    if nf.name != f"{pkg}_notes.md":   # e.g. audit_notes.md in the same folder is not the package's notes
        continue
    cs = cotes_of(pkg)
    if cs:
        finals.append((pkg, nf, cs))

# packages per topic (a package spanning two topics goes to each)
by_topic = collections.defaultdict(list)
for pkg, nf, cs in finals:
    for tp in dict.fromkeys(R[c]["topic"] for c in cs):
        by_topic[tp].append((pkg, nf, [c for c in cs if R[c]["topic"] == tp]))

# codex folders by cote
codex = collections.defaultdict(list)
for f in sorted((CW / "returns").iterdir()):
    m = re.match(r"^[A-Z]{1,2}(\d+(?:-\d+)?)-\d+$", f.name)
    if m and m.group(1) in R:
        codex[m.group(1)].append(f)

# chunks
topics = sorted(by_topic, key=lambda tp: (topic_rank(tp), tp))
chunks = []   # (topics list, packages list, part k, of n)
pending_small = []
pending_bytes = 0


def flush_small():
    global pending_small, pending_bytes
    if pending_small:
        pk = [p for tp in pending_small for p in by_topic[tp]]
        chunks.append((list(pending_small), pk, 1, 1))
    pending_small, pending_bytes = [], 0


for tp in topics:
    pk = sorted(by_topic[tp], key=lambda x: (cote_key(x[2][0]), x[0]))
    size = sum(x[1].stat().st_size for x in pk)
    if size < SMALL:
        if pending_bytes + size > GROUP:
            flush_small()
        pending_small.append(tp)
        pending_bytes += size
        continue
    flush_small()
    n = max(1, -(-size // CHUNK))
    target = size / n
    parts, cur, cb = [], [], 0
    for x in pk:
        b = x[1].stat().st_size
        if cur and cb + b > target * 1.15 and len(parts) < n - 1:
            parts.append(cur); cur, cb = [], 0
        cur.append(x); cb += b
    if cur:
        parts.append(cur)
    for k, part in enumerate(parts, 1):
        chunks.append(([tp], part, k, len(parts)))
flush_small()


def slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "_", s.encode("ascii", "ignore").decode()).strip("_")
    return s[:40] or "topic"


def zip_parts(files, stem, folder):
    """files: list of (arcname, bytes). Returns the list of zip names written."""
    total = sum(len(b) for _, b in files)
    groups, cur, cb = [], [], 0
    for a, b in files:
        if cur and cb + len(b) > LIM * 2.5:   # text compresses well; split on raw size conservatively
            groups.append(cur); cur, cb = [], 0
        cur.append((a, b)); cb += len(b)
    if cur:
        groups.append(cur)
    names = []
    for i, g in enumerate(groups, 1):
        name = f"{stem}.zip" if len(groups) == 1 else f"{stem}_part{i}.zip"
        p = folder / name
        with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for a, b in g:
                z.writestr(a, b)
        if p.stat().st_size > LIM:
            raise SystemExit(f"{p} is {p.stat().st_size} bytes: lower the split size")
        names.append(name)
    return names


template = TEMPLATE.read_text(encoding="utf-8")
index = []
for i, (tps, pk, k, n) in enumerate(chunks, 1):
    S = f"SA{i:02d}"
    title = " + ".join(R[x[2][0]]["topic"] for x in pk[:1]) if len(tps) == 1 else "; ".join(tps)
    folder = OUT / (f"{S}_{slug(tps[0])}" + ("" if n == 1 else f"_part{k}"))
    cotes = sorted({c for x in pk for c in x[2]}, key=cote_key)
    topic_cotes = sorted({c for c, r in R.items() if r["topic"] in tps}, key=cote_key)
    notes_files, texts_files, idx_rows = [], [], []
    nentries = 0
    for pkg, nf, cs in pk:
        txt = nf.read_text(encoding="utf-8", errors="replace")
        notes_files.append((f"pro/{pkg}_notes.md", txt.encode("utf-8")))
        dbt = nf.parent / f"{pkg}_doubts.md"
        if dbt.is_file():
            notes_files.append((f"pro/{pkg}_doubts.md", dbt.read_bytes()))
        for (nn, head, kind, scans) in entries_of(txt):
            idx_rows.append((f"{pkg}#{nn}", pkg, ",".join(cs), head.replace("\t", " "), kind.replace("\t", " "),
                             ",".join(str(s) for s in scans)))
            nentries += 1
        spd = SP / pkg
        if spd.is_dir():
            for f in sorted(spd.glob("*_changes.md")) + sorted(spd.glob("*_notes_checked.md")):
                notes_files.append((f"second_pass/{pkg}/{f.name}", f.read_bytes()))
        tr = nf.parent / f"{pkg}_transcription.tex"
        if tr.is_file():
            texts_files.append((f"pro/{pkg}_transcription.tex", tr.read_bytes()))
        else:
            pages = sorted((nf.parent / "pages").glob("*.tex"))
            texts_files.append((f"pro/{pkg}_transcription.tex", b"\n\n".join(p.read_bytes() for p in pages)))
    cfolders = []
    for c in cotes if n > 1 else topic_cotes:
        for f in codex.get(c, []):
            cfolders.append(f)
            for nf2 in list(f.glob("out/*_notes.md")) + list(f.glob("*_notes.md")):
                notes_files.append((f"codex/{f.name}_notes.md", nf2.read_bytes())); break
            for tf in list(f.glob("out/*_transcription.tex")) + list(f.glob("*_transcription.tex")):
                texts_files.append((f"codex/{f.name}_transcription.tex", tf.read_bytes())); break
    api_used = []
    for c in topic_cotes:
        for dname in API_DIRS.get(c, []):
            cf = API / dname / f"{dname}_combined.tex"
            if cf.is_file():
                texts_files.append((f"api/{dname}_combined.tex", cf.read_bytes())); api_used.append(dname)
    texts_files.append(("PREAMBLE.tex", (CW / "tools" / "PREAMBLE.tex").read_bytes()))
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(["entry_id", "package", "cotes", "heading", "kind", "scans_cited"])
    w.writerows(idx_rows)
    notes_files.insert(0, ("NOTES_INDEX.tsv", buf.getvalue().encode("utf-8")))
    # TOPIC.md
    lines = [f"# {S}: {'; '.join(tps)}", "", "| cote | catalogue title | pages | Pro | Codex | API | in this run |",
             "|---|---|---:|---:|---:|---:|---|"]
    for c in topic_cotes:
        r = R[c]
        inrun = [x[0] for x in pk if c in x[2]] + [f.name for f in cfolders if re.match(rf"^[A-Z]{{1,2}}{re.escape(c)}-\d+$", f.name)]
        lines.append(f"| {c} | {r['title'].replace('|', '/')} | {r['pages']} | {r.get('pro', 0)} | {r.get('codex', 0)} | "
                     f"{r.get('api', 0)} | {', '.join(inrun) if inrun else 'nothing transcribed in this run' if c in cotes else 'other part'} |")
    texts_files.insert(0, ("TOPIC.md", ("\n".join(lines) + "\n").encode("utf-8")))
    # the prompt
    cl = ", ".join(cotes) if n > 1 else ", ".join(topic_cotes)
    cotes_line = (f"cotes {cl}" if len(tps) == 1 else "cotes " + cl)
    scope = ""
    if n > 1:
        scope = (f"**This run takes part {k} of {n} of the topic's notes:** the packages of cotes {', '.join(cotes)}. The other "
                 f"parts are other runs, and their dossiers are merged afterwards by script, so keep the ids of this run "
                 f"(`{S}-<n>`, `MP-{S}-<nn>`) and cover only the entries of this part's `NOTES_INDEX.tsv`; `TOPIC.md` "
                 f"lists the whole topic for orientation.")
    elif len(tps) > 1:
        scope = ("**This run takes several small topics together.** Keep them apart: one section of the dossier per topic, "
                 "each read in its own terms.")
    if not DRY:
        folder.mkdir(parents=True, exist_ok=True)
        for old in folder.glob("*.zip"):
            old.unlink()
    nz = zip_parts(notes_files, f"{S}_notes", folder) if not DRY else ["x"]
    tz = zip_parts(texts_files, f"{S}_texts", folder) if not DRY else ["x"]
    parts_note = lambda zs: "" if len(zs) == 1 else (f" (in {len(zs)} parts, `{zs[0]}` to `{zs[-1]}`: unpack all of them "
                                                     f"into one folder; together they are this zip)")
    api_line = ("; and `api/<name>_combined.tex`: typed texts of the topic transcribed by Claude over the API ("
                + ", ".join(api_used) + ")") if api_used else ""
    text = (template.replace("{S}", S).replace("{TOPIC_TITLE}", "; ".join(tps)).replace("{TOPIC}", "; ".join(tps))
            .replace("{COTES_LINE}", cotes_line).replace("{SCOPE_NOTE}", scope).replace("{NOTES_PARTS}", parts_note(nz))
            .replace("{TEXTS_PARTS}", parts_note(tz)).replace("{NENTRIES}", str(nentries)).replace("{NPKG}", str(len(pk)))
            .replace("{API_LINE}", api_line))
    assert "{" not in re.sub(r"\\[a-zA-Z]+\{[^}]*\}|`[^`]*`", "", text).replace("{verified}", "").replace("{unverified}", ""), S
    nb = sum(len(b) for a, b in notes_files if a.startswith("pro/") and a.endswith("_notes.md"))
    index.append((S, folder.name, "; ".join(tps), f"{k}/{n}", " ".join(x[0] for x in pk), ",".join(cotes), nentries,
                  round(nb / 1e6, 3), len(cfolders), ",".join(api_used)))
    if DRY:
        continue
    (folder / "PROMPT.md").write_text(text, encoding="utf-8")
    with zipfile.ZipFile(folder / f"{S}_PROMPT.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("PROMPT.md", text.encode("utf-8"))
    (folder / "README.md").write_text(
        f"# {S}: topic dossier, {'; '.join(tps)}" + ("" if n == 1 else f" (part {k} of {n})") + "\n\n"
        "Upload every file of this folder in a new ChatGPT chat with GPT-6 Astra in Pro mode, PROMPT.md as a file, no text"
        " typed. Text only, no scans: a light prompt.\n\n"
        f"- notes: {nentries} entries from {len(pk)} Pro packages ({', '.join(x[0] for x in pk)}); Codex folders: "
        f"{len(cfolders)}; API typescripts: {', '.join(api_used) or 'none'}.\n"
        "- Built by `stage_a_20261118/build_stage_a.py` (the main session, Claude Opus 5.5 at effort max) from the returns"
        " in grothendieck_archive_transcription_20261110/returns/, codex_web_20261113/returns/ and second_pass/out/.\n",
        encoding="utf-8")

with open(OUT / "STAGE_A_PACKAGES.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["S", "folder", "topics", "part", "packages", "cotes", "entries", "notes_MB", "codex_folders", "api"])
    w.writerows(index)
for row in index:
    print("\t".join(str(x) for x in row[:4]), row[6], row[7], sep="\t")
print("prompts:", len(index))
if not DRY:
    r = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint"] + [str(p) for p in sorted(OUT.glob("SA*/PROMPT.md"))],
                       capture_output=True, text=True)
    print(r.stdout[-600:])
