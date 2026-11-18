"""Build the working-through pilot packages, run A, for cote 22 (18 Nov 2026): two slices, WT22a (scans 2-18: the
offprints and the typescript with his annotations) and WT22b (scans 19-30: his handwritten notes).
Template: WT_A_TEMPLATE.md. Plan: second_pass/PLAN_WORKING_THROUGH_PRO_20261118.md; design:
grothendieck_archive_montpellier/COMPANION_DESIGN_20261118.md; task file Documents/task_notes/working_through_pilots.md.

Per slice, a flat upload folder WT22x/ with PROMPT.md, WT22x_scans_partK.zip (each under 8.95 MB), WT22x_witnesses.zip,
WT22x_context.zip, WT22x_results.zip, WT22x_PROMPT.zip, README.md.
usage: python -I -B build_wt_pilot.py
Written by the main session (Claude Opus 5.5 at effort max), 18 Nov 2026."""
import csv, io, pathlib, re, subprocess, sys, zipfile

sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path("C:/Users/user/Documents")
T = D / "grothendieck_archive_transcription_20261110"
HERE = T / "working_through_20261118"
PKG = "MPL_22+23_002-016"
RETD = T / "returns" / f"{PKG}_unzipped"
SCANS = T / "packages_done" / "P044_60_MPL_22+23_002-016" / f"{PKG}_scans.zip"
FIRST_PROMPT = T / "packages_done" / "P044_60_MPL_22+23_002-016" / "PROMPT.md"
OLD_CTX = T / "packages_done" / "P044_60_MPL_22+23_002-016" / f"{PKG}_context.zip"
HUA = D / "ai_math_sources_20261114/hua_michel/commutator_grothendieck-project"
EGA = D / "ega_fr_online_20261112/ega-fr/source/ega4"
API = T / "api_typescripts_20261112"
CODEX26 = T / "codex_web_20261113/returns/H26-01"
LINT = D / "claude_tools/push_rule_pro_prompts.py"
LIM = 8_950_000
TITLE = ("[EGA IV]. [Chapitre] 0 IV. Cohen, différentielles, algèbres formellement simples (Compléments) : tirés à part "
         "(1963), tapuscrit annoté (s.d.), notes manuscrites (s.d.)")
SLICES = [
    ("WT22a", range(2, 19), "offprints of chapter 0_IV of EGA IV with his annotations, the annotated typescript, and the "
                            "notes he wrote on the backs of typed sheets"),
    ("WT22b", range(19, 31), "his handwritten notes, among them his list of open questions (scans 19-21), written on the "
                             "backs of typed sheets"),
]
CONTEXT = [(EGA / f, f"ega_fr/{f}") for f in ["ega0-19-fr.tex", "ega0-19b-fr.tex", "ega0-20-fr.tex", "ega0-21-fr.tex",
                                              "ega0-22-fr.tex", "ega0-23-fr.tex", "ega4-16-fr.tex", "ega4-17-fr.tex"]]
CONTEXT += [(API / "ega_v_cote24_blass" / "ega_v_cote24_blass_combined.tex", "ega_v/cote24_ega_v_english_typescript.tex"),
            (API / "ega_v_cote25" / "ega_v_cote25_combined.tex", "ega_v/cote25_nouveau_ega_v_typescript.tex")]
CONTEXT_LIST = (
    "It holds: `ega_fr/`, the French text of EGA 0_IV, sections 19 to 23 (formally smooth algebras and Cohen rings, "
    "derivations and differentials, differentials in characteristic p, differential criteria of smoothness and "
    "regularity), and of EGA IV, sections 16 and 17 (differential invariants; smooth, unramified and étale morphisms), "
    "as LaTeX from our edition; `ega_v/`, the typescripts of EGA V in the archive (cotes 24 and 25), transcribed by "
    "Claude over the API; `folder23/`, the transcribed pages of cote 23 (EGA IV, Compléments: his notes, letters of "
    "1966 and 1968, a typescript; 15 of its 98 pages, by GPT-6 Astra in Pro mode); `folder26/`, cote 26 (EGA VI: plans, "
    "notations, open problems; 10 pages, by GPT-6 Astra at reasoning effort max in Codex). Cote 21 (chapter 0_III) "
    "has no transcription yet. Search these files for his objects and numbers: the passages of EGA that his pages "
    "annotate, draft or anticipate are the first grounds for the notes.")


def zip_files(path, files):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, data in files:
            z.writestr(arc, data)
    assert path.stat().st_size <= LIM, (path, path.stat().st_size)


def notes_index(text):
    rows = []
    for n, part in enumerate(re.split(r"(?m)^### ", text)[1:], 1):
        head = part.splitlines()[0].strip() if part.strip() else ""
        scans = sorted(set(re.findall(r"22_scan0*(\d{1,3})|scans?\s*0*(\d{1,3})\b", part)))
        flat = sorted({int(a or b) for a, b in scans})
        rows.append((f"{PKG}#{n}", head.replace("\t", " "), ",".join(str(x) for x in flat)))
    return rows


hua_batches = sorted((HUA / "transcripts" / "22").glob("batch-*.fr.tex"))
hua_text = {}
for b in hua_batches:
    t = b.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r"\\page\{(\d+)\}", t):
        hua_text[int(m.group(1)) + 1] = b.name
template = (HERE / "WT_A_TEMPLATE.md").read_text(encoding="utf-8")
scans_zip = zipfile.ZipFile(SCANS)
old_ctx = zipfile.ZipFile(OLD_CTX)
results_state = old_ctx.read("notes/RESULTS_STATE.md")
for S, rng, kinds in SLICES:
    out = HERE / S
    out.mkdir(exist_ok=True)
    for old in out.glob("*.zip"):
        old.unlink()
    # scans, in parts under the limit, every scan's three images together
    imgs = [i for i in scans_zip.infolist() if re.search(r"_22_scan(\d{3})", i.filename)
            and int(re.search(r"_22_scan(\d{3})", i.filename).group(1)) in rng]
    groups = {}
    for i in imgs:
        groups.setdefault(int(re.search(r"_22_scan(\d{3})", i.filename).group(1)), []).append(i)
    parts, cur, cb = [], [], 0
    for sc in sorted(groups):
        g = sorted(groups[sc], key=lambda i: i.filename)
        gb = sum(i.compress_size for i in g) + 2000
        if cur and cb + gb > LIM * 0.95:
            parts.append(cur); cur, cb = [], 0
        cur += g; cb += gb
    if cur:
        parts.append(cur)
    names = []
    for k, part in enumerate(parts, 1):
        name = f"{S}_scans_part{k}.zip"
        with zipfile.ZipFile(out / name, "w", zipfile.ZIP_STORED) as z:
            for i in part:
                z.writestr(i.filename, scans_zip.read(i.filename))
        assert (out / name).stat().st_size <= LIM, name
        names.append(name)
    # witnesses
    wfiles, pm = [], io.StringIO()
    w = csv.writer(pm, delimiter="\t", lineterminator="\n")
    w.writerow(["scan", "witness_O_file", "witness_H_batch", "H_has_text"])
    for s in rng:
        pf = RETD / "pages" / f"{PKG}_22_scan{s:03d}.tex"
        if pf.is_file():
            wfiles.append((f"ours/pages/{pf.name}", pf.read_bytes()))
        w.writerow([s, pf.name if pf.is_file() else "", hua_text.get(s, ""), "yes" if s in hua_text else "no"])
    notes = (RETD / f"{PKG}_notes.md").read_text(encoding="utf-8", errors="replace")
    wfiles += [("ours/first_pass_PROMPT.md", FIRST_PROMPT.read_bytes()),
               (f"ours/{PKG}_notes.md", notes.encode("utf-8")),
               (f"ours/{PKG}_doubts.md", (RETD / f"{PKG}_doubts.md").read_bytes())]
    ni = io.StringIO()
    w2 = csv.writer(ni, delimiter="\t", lineterminator="\n")
    w2.writerow(["entry_id", "heading", "scans_cited"])
    w2.writerows(notes_index(notes))
    wfiles.append(("ours/NOTES_INDEX.tsv", ni.getvalue().encode("utf-8")))
    for b in hua_batches:
        wfiles.append((f"hua/transcripts/22/{b.name}", b.read_bytes()))
    for extra in ["transcripts/preamble/grothendieck.sty", "CONTRIBUTING.md", "RIGHTS.md"]:
        if (HUA / extra).is_file():
            wfiles.append((f"hua/{extra}", (HUA / extra).read_bytes()))
    wfiles.append(("page_map.tsv", pm.getvalue().encode("utf-8")))
    wfiles.append(("README.md", (
        f"# {S}: the witnesses\n\n- `ours/`: witness O, the Pro first pass {PKG} (GPT-6 Astra, ChatGPT Pro mode, 9-10 Nov 2026):"
        " the page files of this slice, the package's notes and doubts (they cover cotes 22 and 23: the entries about this"
        " slice's scans are the ones to consume; `NOTES_INDEX.tsv` lists every entry with the scans it cites), and the"
        " first-pass prompt, which defines our macros.\n- `hua/`: witness H, the Commutator project of Michel Hua"
        " (github.com/Commutator-IO/grothendieck-project, commit aef7db2), batch files of cote 22 and their preamble;"
        " their page n is our scan n + 1. A witness, credited; never a basis.\n- `page_map.tsv`: per scan, the files"
        " of both witnesses.\n").encode("utf-8")))
    zip_files(out / f"{S}_witnesses.zip", wfiles)
    # context
    cfiles = [(arc, p.read_bytes()) for p, arc in CONTEXT if p.is_file()]
    for pf in sorted((RETD / "pages").glob(f"{PKG}_23_scan*.tex")):
        cfiles.append((f"folder23/{pf.name}", pf.read_bytes()))
    for pf in sorted(CODEX26.rglob("*.tex")):
        if "pages" in pf.parts or pf.name.endswith("_transcription.tex"):
            cfiles.append((f"folder26/{pf.name}", pf.read_bytes()))
    zip_files(out / f"{S}_context.zip", cfiles)
    zip_files(out / f"{S}_results.zip", [("RESULTS_STATE.md", results_state)])
    folder_note = (f"The folder's catalogue title: « {TITLE} ». It has 29 scans; this run takes scans {rng.start}-{rng.stop - 1}, "
                   f"and the other part of the folder is a separate run.")
    text = (template.replace("{S}", S).replace("{COTE}", "22").replace("{RANGE}", f"{rng.start:03d}-{rng.stop - 1:03d}")
            .replace("{COUNT}", str(len(rng))).replace("{KINDS}", kinds).replace("{FOLDER_NOTE}", folder_note)
            .replace("{PKG}", PKG).replace("{CONTEXT_LIST}", CONTEXT_LIST))
    note = (f"\n\n**The scans come in {len(names)} zips** (`{names[0]}` to `{names[-1]}`), each under 10 MB: unpack all of "
            f"them into the same folder; together they are `{S}_scans.zip`.\n" if len(names) > 1 else "")
    text = text.replace("## The attachments\n", "## The attachments\n" + note, 1)
    (out / "PROMPT.md").write_text(text, encoding="utf-8")
    with zipfile.ZipFile(out / f"{S}_PROMPT.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("PROMPT.md", text.encode("utf-8"))
    (out / "README.md").write_text(
        f"# {S}: working through cote 22, scans {rng.start}-{rng.stop - 1} (run A)\n\nUpload every file of this folder in a"
        " new ChatGPT chat with GPT-6 Astra in Pro mode, PROMPT.md as a file, no text typed. Scan-heavy: counts as a heavy"
        " prompt.\n\nBuilt by `working_through_20261118/build_wt_pilot.py` (the main session, Claude Opus 5.5 at effort"
        " max), 18 Nov 2026. Sources: the scans of package P044 (Montpellier archive PDFs), witness O = Pro return"
        f" {PKG}, witness H = Hua commit aef7db2, EGA from our French edition, EGA V and cotes 23 and 26 from our"
        " transcriptions, RESULTS_STATE.md of P044's context packet (13 Nov 2026).\n", encoding="utf-8")
    sizes = {p.name: round(p.stat().st_size / 1e6, 2) for p in sorted(out.iterdir())}
    print(S, sizes)
r = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint"] + [str(HERE / s / "PROMPT.md") for s, _, _ in SLICES],
                   capture_output=True, text=True)
print(r.stdout[-400:])
