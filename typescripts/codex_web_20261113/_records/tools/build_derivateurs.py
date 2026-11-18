"""Batch K round D: the manuscript of Les Derivateurs (cotes 157-1 to 157-5, 2,140 scans) for GPT-6.2 Astra at
reasoning effort max (ChatGPT Work), 18 Nov 2026. Written by the main session, Claude Opus 5.5 at effort max.

The user, 18 Nov 2026 (USER_INPUTS P6893-P6896): Les Derivateurs counts as untranscribed; "it is still worth doing to
just transcribe those [too] via 6.2", like the rest of the archive, then diff with the edition of Kunzer, Malgoire and
Maltsiniotis, "their literal transcription", as the witness. Plan: task_notes/derivateurs_transcription.md.

Each folder is a blind first reading on template K2, as rounds 7-9: the edition, our French and our English are not
shown (Hua's text is a witness after the freeze only where he has the pages; he has none of 157). Blank scans and the
IMAG logo sheet are left out by the tests of rounds 7-8 (build_k_rounds78.scan_info). Folders of at most 16 scans per
cote (build_handwriting_k.chunks), ids K<cote>-NN, round "D". The material sentence comes from two sample pages looked
at on 18 Nov (157-1 scan 12, 157-5 scan 400).

usage: python -I -B tools/build_derivateurs.py --plan          (ink and logo tests of every scan; writes the plan)
       python -I -B tools/build_derivateurs.py --build N       (builds the next N planned folders into drag_next/,
                                                                splits them into drag_split_next/, appends ROUNDS.tsv
                                                                and ASSIGNMENTS.tsv rows with round D, lints them)
"""
import csv
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_k_rounds78 as R  # noqa: E402
import k_material  # noqa: E402

K, B, CW, T = R.K, R.B, R.CW, R.T
PLAN = CW / "K_DERIVATEURS_PLAN_20261118.json"
COTES = ["157-1", "157-2", "157-3", "157-4", "157-5"]
LINT = pathlib.Path.home() / "Documents/claude_tools/push_rule_pro_prompts.py"
WHAT = ("batch K round D, 18 Nov 2026: Work first reading of the manuscript of Les Derivateurs (157-1 to 157-5), "
        "blind (the edition of Kunzer, Malgoire and Maltsiniotis is not shown; it is the witness of the later "
        "comparison); template PROMPT_TEMPLATE_HANDWRITING_K2.md, for GPT-6.2 Astra Max")
MATERIAL = ("These are his handwritten notes for Les Dérivateurs. Sample pages of this file, looked at before the task "
            "was made, are in his dense, fast working hand: word endings often reduced to a stroke, many formulas and "
            "commutative diagrams, insertions, underlinings and struck passages, with his own page number at the top "
            "of the sheet and the archive's pencil number at the bottom left.")

_orig_sentence = k_material.sentence


def sentence(x):
    if x["cote"] not in COTES:
        return _orig_sentence(x)
    s = MATERIAL
    if len(x["scans"]) > 1 and x["scans"][-1] - x["scans"][0] + 1 > len(x["scans"]):
        s += (" The scans are not all consecutive: scans of this file that are not listed are blank or belong to "
              "other tasks.")
    return s + " " + k_material.TAIL


k_material.sentence = sentence  # make_prompt() imports k_material inside the function: it gets this one


def load():
    if PLAN.exists():
        return json.loads(PLAN.read_text(encoding="utf-8"))
    return dict(folders=[], blank={}, logo={}, missing_image={}, already_read={})


def plan():
    P = load()
    if P["folders"]:
        print("plan exists:", len(P["folders"]), "folders; delete", PLAN.name, "to replan")
        return
    cache = json.loads(R.CACHE.read_text(encoding="utf-8")) if R.CACHE.exists() else {}
    with tempfile.TemporaryDirectory() as tmp:
        ref = R.thumb(B.page_image(R.pdf_of(R.LOGO_REF[0]), R.LOGO_REF[1], tmp))
    ids = R.existing_ids()
    got = set()
    for r in csv.DictReader(open(CW / "ASSIGNMENTS.tsv", encoding="utf-8"), delimiter="\t"):
        if r["cote"] in COTES:
            got |= {(r["cote"], int(n)) for n in r["scans"].split(",") if n.strip().isdigit()}
    for cote in COTES:
        scans = list(range(1, R.n_pages(cote) + 1))
        P["already_read"][cote] = sum(1 for n in scans if (cote, n) in got)
        info = R.scan_info(cote, [n for n in scans if (cote, n) not in got], cache, ref)
        live = []
        for n, (ink, dist) in sorted(info.items()):
            if ink < 0:
                P["missing_image"].setdefault(cote, []).append(n)
            elif ink < 0.0003:
                P["blank"].setdefault(cote, []).append(n)
            elif dist < 12:
                P["logo"].setdefault(cote, []).append(n)
            else:
                live.append(n)
        j = R.next_index(cote, ids)
        for part in K.chunks(live):
            fid = f"K{cote}-{j:02d}"
            ids.add(fid)
            P["folders"].append(dict(id=fid, cote=cote, scans=part, round="D", package=f"DERIVATEURS_{cote}",
                                     packages=[f"DERIVATEURS_{cote}"]))
            j += 1
        PLAN.write_text(json.dumps(P, indent=1, ensure_ascii=False), encoding="utf-8")
        print(cote, "scans", len(scans), "live", len(live), "blank", len(P["blank"].get(cote, [])),
              "logo", len(P["logo"].get(cote, [])), "missing", len(P["missing_image"].get(cote, [])), flush=True)
    print("planned:", len(P["folders"]), "folders,", sum(len(f["scans"]) for f in P["folders"]), "pages")


def built(fid):
    return any((CW / b / fid).is_dir() for b in ("drag", "drag_next", "done", "drag_split_next"))


def build(n):
    P = load()
    todo = [x for x in P["folders"] if not built(x["id"])][:n]
    recs, failed = [], []
    for x in todo:
        try:
            r = K.build_next(x["id"], x["cote"], x["scans"], "")
        except SystemExit as e:
            failed.append((x["id"], str(e)))
            print("FOLDER FAILED:", x["id"], e, flush=True)
            continue
        if r:
            r["round"] = x["round"]
            recs.append(K.add_hua(x, r))
            (CW / "drag_next" / x["id"] / "PROMPT.md").write_bytes(K.make_prompt(x, P["folders"]).encode("utf-8"))
            print("built", x["id"], len(x["scans"]), "scans", flush=True)
    with open(HERE / "BUILD_LOG.jsonl", "a", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    ids = [r["id"] for r in recs]
    if not ids:
        print("nothing built; failed:", failed)
        return
    s = subprocess.run([sys.executable, "-I", "-B", str(HERE / "split_for_chrome.py"), "--dst", "drag_split_next",
                        "drag_next"] + ids, capture_output=True, text=True, cwd=str(CW))
    print(s.stdout[-1200:], s.stderr[-600:])
    rounds = CW / "drag_split_next" / "ROUNDS.tsv"
    have = {row[0] for row in csv.reader(open(rounds, encoding="utf-8"), delimiter="\t")}
    assign = CW / "ASSIGNMENTS.tsv"
    have_a = {row[0] for row in csv.reader(open(assign, encoding="utf-8"), delimiter="\t")}
    byid = {x["id"]: x for x in todo}
    bad = []
    with open(rounds, "a", encoding="utf-8", newline="") as fr, open(assign, "a", encoding="utf-8", newline="") as fa:
        wr = csv.writer(fr, delimiter="\t", lineterminator="\n")
        wa = csv.writer(fa, delimiter="\t", lineterminator="\n")
        for fid in ids:
            x = byid[fid]
            parts = len(list((CW / "drag_split_next" / fid).glob(f"{fid}_scans_part*.zip")))
            if parts == 0:
                print("NOT SPLIT:", fid)
                bad.append(fid)
                continue
            lint = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint-codex",
                                   str(CW / "drag_split_next" / fid / "PROMPT.md")], capture_output=True, text=True)
            if lint.returncode != 0:
                print("LINT FAILED:", fid, lint.stdout[-400:], lint.stderr[-200:])
                bad.append(fid)
                continue
            if fid not in have:
                wr.writerow([fid, "D", x["cote"], len(x["scans"]), parts])
            if fid not in have_a:
                wa.writerow([fid, x["cote"], ",".join(str(s) for s in x["scans"]), len(x["scans"]), x["package"], WHAT])
    print("built and queued:", len(ids) - len(bad), "of", len(todo), "| held back:", bad, "| failed:", failed)
    print("queued:", " ".join(f for f in ids if f not in bad))


if __name__ == "__main__":
    if "--plan" in sys.argv:
        plan()
    elif "--build" in sys.argv:
        build(int(sys.argv[sys.argv.index("--build") + 1]))
