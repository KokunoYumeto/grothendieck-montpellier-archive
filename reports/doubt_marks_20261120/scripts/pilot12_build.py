"""Pilots 1 and 2 of the doubt-mark report, over the Message Batches API only (50 % off) (20 Nov 2026, main session,
Claude Opus 5.5 at effort max; approved by the user on 20 Nov: pilot 1 and pilot 2, cheaply; every API run in the
50 %-off modes; cost per design measured on a small batch first).

Pilot 1: a blind check of the marks where Hua has C's other alternative: the readings in random order, no witness named.
Pilot 2: the same marks at two zoom depths: the word (DM01's own crop box, enlarged up to 10x) against the whole line
(the text width at about 1x).
The marks are DM01's (cote 1), whose decision on each, made on the scan by GPT-6 Astra (ChatGPT Pro mode), is the
reference. Two prompt designs: P1 offers the readings (random order, plus "neither"); P2 asks for a free reading,
matched to the readings by script.

python -I -B pilot12_build.py --set small|full [--models haiku,sonnet,opus]
  -> pilots_api_20261120/<set>/requests.jsonl, items.tsv, img/*.jpg (nothing is sent; pilot12_send.py sends)."""
import base64
import collections
import csv
import io
import json
import pathlib
import random
import re
import sys
import zipfile

from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import texalign as TA  # noqa: E402

DATA = HERE.parent / "data"
T = pathlib.Path("<project root>/grothendieck_archive_transcription_20261110")
DMB = T / "doubt_marks_pro_20261119/DM01_1_001-160"
SPR = T / "second_pass_returns"
SET = sys.argv[sys.argv.index("--set") + 1] if "--set" in sys.argv else "small"
MODELS = (sys.argv[sys.argv.index("--models") + 1] if "--models" in sys.argv else "haiku,sonnet,opus").split(",")
# 20 Nov, version 2: "both" sends the line (to find the place) and the word crop (for the detail) in one request
ZOOMS = (sys.argv[sys.argv.index("--zooms") + 1] if "--zooms" in sys.argv else "word,line").split(",")
OUT = HERE.parent / "pilots_api_20261120" / (SET + ("_" + sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else ""))
(OUT / "img").mkdir(parents=True, exist_ok=True)

MODEL = {"haiku": ("claude-haiku-5-5", "high" if "--tag" in sys.argv else "medium", 6000), "sonnet": ("claude-sonnet-5-5", "medium", 4000),
         "opus": ("claude-opus-5-5", "high", 8000)}

# ---- DM01's decisions, joined with what the alignment knows about each mark (page by page, in mark order)
dmd = max(SPR.glob("DM01_*_unzipped"), key=lambda p: re.search(r"(\d{8}T\d{4})Z_unzipped$", p.name).group(1))
dec = list(csv.DictReader(open(dmd / "decisions.tsv", encoding="utf-8"), delimiter="\t"))
fm = [m for m in csv.DictReader(open(DATA / "marks.tsv", encoding="utf-8"), delimiter="\t") if m["run"] == "DM01"]
dd, mm = collections.defaultdict(list), collections.defaultdict(list)
for d in dec:
    dd[int(d["scan"])].append(d)
for m in fm:
    mm[int(m["scan"])].append(m)
joined = {d["id"]: (d, m) for s in sorted(dd) if len(dd[s]) == len(mm.get(s, [])) for d, m in zip(dd[s], mm[s])}
zt = zipfile.ZipFile(DMB / "DM01_1_001-160_texts.zip")
mk = {r["id"]: r for r in csv.DictReader(io.StringIO(zt.read("MARKS.tsv").decode("utf-8", "replace")), delimiter="\t")}
zs = zipfile.ZipFile(DMB / "DM01_1_001-160_scans.zip")


def crop_box(d):
    try:
        x0, y0, x1, y1 = (int(v) for v in d["crop"].split(","))
        return (x0, y0, x1, y1) if x1 > x0 and y1 > y0 else None
    except Exception:
        return None


def alts_of(mark_text):
    m = re.match(r"\\unsure\{(.*)\}$", mark_text.strip(), re.S)
    if not m:
        return None
    return [a.strip() for a in TA.alternatives(m.group(1))]


usable = []
for i, (d, m) in joined.items():
    r = mk.get(i)
    if not r or d["decision"] not in ("first", "alternative", "other", "undecided") or not crop_box(d):
        continue
    al = alts_of(r["the mark as written"])
    if not al:
        continue
    usable.append(i)
cls = [i for i in usable if joined[i][1]["hua"] == "Hua = C's other alternative"]
rest = [i for i in usable if i not in cls and joined[i][0]["decision"] in ("first", "alternative", "other") and joined[i][1]["in_deleted"] != "1"]
rng = random.Random(20261120)


def pick(pool, n):
    pool = sorted(pool)
    rng.shuffle(pool)
    return pool[:n]


def kind(i):
    return "choice" if len(alts_of(mk[i]["the mark as written"])) > 1 else "single"


def sel(k, dec_):
    return [i for i in rest if kind(i) == k and joined[i][0]["decision"] == dec_]


if SET == "small":
    ids = pick([i for i in cls if joined[i][0]["decision"] != "undecided"], 5) + pick(sel("choice", "first"), 2) + \
        pick(sel("choice", "alternative"), 1) + pick(sel("single", "first"), 1) + pick(sel("single", "other"), 1)
else:
    ids = sorted(cls) + pick(sel("choice", "first"), 18) + pick(sel("choice", "alternative"), 12) + pick(sel("choice", "other"), 6) + \
        pick(sel("single", "first"), 24) + pick(sel("single", "other"), 12)
print(SET, "marks:", len(ids), "| class (Hua has C's other alternative):", sum(1 for i in ids if i in cls))


# ---- the context around the place, as plain text, with the other marks written with their first reading
def plain(latex):
    pieces, pos = [], 0
    for m in TA.find_marks(latex, TA.OURS):
        pieces.append(latex[pos:m["s"]])
        if m["name"] == "illegible":
            pieces.append(" [illegible] ")
        else:
            pieces.append((TA.alternatives(m["arg"] or "") or [""])[0])
        pos = m["e"]
    pieces.append(latex[pos:])
    return re.sub(r"\s+", " ", TA.to_plain("".join(pieces))).strip()


def context(i):
    r = mk[i]
    ctx, mw = r["the LaTeX around it"], r["the mark as written"]
    hits = [m.start() for m in re.finditer(re.escape(mw), ctx)]
    if not hits:
        return None, None
    k = min(hits, key=lambda h: abs(h - len(ctx) / 2))
    return plain(ctx[:k])[-170:], plain(ctx[k + len(mw):])[:170]


# ---- the two images of a mark: the word (DM01's crop, padded, enlarged up to 10x) and the line (text width, about 1x)
_page = {}


def page(scan):
    if scan not in _page:
        _page.clear()
        _page[scan] = Image.open(io.BytesIO(zs.read(f"1_scan{scan:03d}.jpg"))).convert("L")
    return _page[scan]


def images(i):
    d = joined[i][0]
    im = page(int(d["scan"]))
    W, H = im.size
    x0, y0, x1, y1 = crop_box(d)
    pw, ph = max(20, int(0.15 * (x1 - x0))), max(15, int(0.25 * (y1 - y0)))
    out = {}
    a = im.crop((max(0, x0 - pw), max(0, y0 - ph), min(W, x1 + pw), min(H, y1 + ph)))
    sc = min(10.0, 1400 / a.width, 1000 / a.height)
    out["word"] = (ImageOps.autocontrast(a.resize((round(a.width * sc), round(a.height * sc)), Image.LANCZOS), cutoff=1), sc)
    b = im.crop((int(0.03 * W), max(0, y0 - ph), int(0.97 * W), min(H, y1 + ph)))
    sc2 = min(1.0, 1568 / b.width, 1000 / b.height)
    out["line"] = (ImageOps.autocontrast(b.resize((round(b.width * sc2), round(b.height * sc2)), Image.LANCZOS), cutoff=1), sc2)
    return out


SYSTEM = ("You read handwritten mathematical manuscripts by Alexander Grothendieck (French, 1970s-1990s), from scans. "
          "You get one image cut from a scanned page and a transcription of the words around one place, shown as ⟦?⟧. "
          "Decide what the ink shows at that place, from the ink alone. The transcription around the place may itself "
          "contain errors; use it only to find the place.")


def prompt(i, design, order):
    left, right = context(i)
    al = alts_of(mk[i]["the mark as written"])
    nwords = max(1, len(al[0].split()))
    head = f"Text around the place: «{left} ⟦?⟧ {right}»\n(⟦?⟧ stands for about {nwords} word{'s' if nwords > 1 else ''} or symbols.)\n\n"
    if design == "p1":
        letters = "ABCDEFG"
        opts = "\n".join(f"{letters[k]}. {al[j]}" for k, j in enumerate(order))
        allowed = " | ".join(f'"{letters[k]}"' for k in range(len(order)))
        return head + ("Earlier readers proposed these readings for ⟦?⟧, listed in random order; any of them may be wrong:\n" + opts +
                       "\n\nWhich one does the ink show? End your reply with one line holding only a JSON object: "
                       '{"answer": ' + allowed + ' | "neither" | "undecidable", "reading": "what the ink shows, written like the '
                       'transcription (LaTeX for mathematics)", "ink": "the feature that decides it, in at most 20 words"}')
    return head + ("Read what the ink shows at ⟦?⟧, exactly, letter by letter, written like the transcription (LaTeX for mathematics). "
                   "End your reply with one line holding only a JSON object: "
                   '{"reading": "...", "confidence": "high" | "medium" | "low", "ink": "the feature that decides it, in at most 20 words"}')


reqs, items = [], []
for i in ids:
    left, right = context(i)
    if left is None:
        print("no context for", i)
        continue
    d, m = joined[i]
    al = alts_of(mk[i]["the mark as written"])
    order = list(range(len(al)))
    random.Random(i).shuffle(order)
    imgs = images(i)
    b64 = {}
    for z, (img, sc) in imgs.items():
        p = OUT / "img" / f"{i}_{z}.jpg"
        img.save(p, quality=90)
        b64[z] = base64.b64encode(p.read_bytes()).decode("ascii")
    items.append(dict(id=i, scan=d["scan"], kind=kind(i), in_class=int(i in cls), in_deleted=m["in_deleted"], dm01_decision=d["decision"],
                      dm01_reading=d["reading"], alts=" || ".join(al), order=",".join(map(str, order)), zoom_word=round(imgs["word"][1], 2),
                      zoom_line=round(imgs["line"][1], 2), w_word=imgs["word"][0].width, h_word=imgs["word"][0].height,
                      w_line=imgs["line"][0].width, h_line=imgs["line"][0].height, left=left, right=right))
    for mt in MODELS:
        model, effort, mx = MODEL[mt]
        for z in ZOOMS:
            for design in ("p1", "p2"):
                if z == "both":
                    content = [{"type": "text", "text": "Image 1: the whole line, as on the page."},
                               {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64["line"]}},
                               {"type": "text", "text": "Image 2: a magnified crop of the same line around the place, contrast raised."},
                               {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64["word"]}}]
                else:
                    content = [{"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64[z]}}]
                reqs.append({"custom_id": f"{mt}-{z}-{design}-{i}",
                             "params": {"model": model, "max_tokens": mx, "output_config": {"effort": effort}, "system": SYSTEM,
                                        "messages": [{"role": "user", "content": content + [{"type": "text", "text": prompt(i, design, order)}]}]}})
with open(OUT / "requests.jsonl", "w", encoding="utf-8") as fh:
    for r in reqs:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(OUT / "items.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, list(items[0].keys()), delimiter="\t")
    w.writeheader()
    w.writerows(items)
print("requests:", len(reqs), "| items:", len(items), "| bytes:", (OUT / "requests.jsonl").stat().st_size)
print("zoom word:", sorted(it["zoom_word"] for it in items))
print("zoom line:", sorted(it["zoom_line"] for it in items))
