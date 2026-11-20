"""Score a pilot set sent by pilot12_send.py against DM01's decisions, and cost it per design (20 Nov 2026, main session,
Claude Opus 5.5 at effort max).

The reference is DM01's decision on each mark (GPT-6 Astra, ChatGPT Pro mode, on the scan): 'first' (C's first reading),
'alternative' (another of C's readings), 'other' (a reading C did not list). A model's answer is right when it lands on
the same reading; 'undecidable' is counted apart (an abstention). P1 answers a letter (the readings were shown in random
order); P2 gives a free reading, matched to the readings by comparing letters only (accents, case, spaces, braces and
LaTeX spacing ignored).
Prices: the Message Batches API at half the standard price (claude-api skill, shared/models.md, 20 Nov 2026):
Claude Haiku 5.5 $0.05 / $0.25, Claude Sonnet 5.5 $1 / $5, Claude Opus 5.5 $2 / $10 per million input / output tokens.
python -I -B pilot12_score.py small -> pilots_api_20261120/<set>/scores.tsv, SUMMARY.md"""
import collections
import csv
import json
import pathlib
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
SET = sys.argv[1] if len(sys.argv) > 1 else "small"
D = pathlib.Path(__file__).resolve().parent.parent / "pilots_api_20261120" / SET
PRICE = {"haiku": (0.05, 0.25), "sonnet": (1.0, 5.0), "opus": (2.0, 10.0),  # $ per million tokens, batch
         # GPT-6.2 Sol, OpenAI Batch API (developers.openai.com/api/docs/pricing, read 20 Nov 2026): $1 input, $5 output
         "solmedium": (1.0, 5.0), "solhigh": (1.0, 5.0), "solmax": (1.0, 5.0)}
LABEL = {"haiku": f"Claude Haiku 5.5 at effort {'high' if SET.endswith('_v2') else 'medium'}", "sonnet": "Claude Sonnet 5.5 at effort medium", "opus": "Claude Opus 5.5 at effort high"}
items = {r["id"]: r for r in csv.DictReader(open(D / "items.tsv", encoding="utf-8"), delimiter="\t")}
LABEL.update({f"sol{e}": f"GPT-6.2 Sol at reasoning effort {e}" for e in ("medium", "high", "max")})


def key(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = re.sub(r"\\(mathrm|text|mathit|operatorname|left|right|,|;|!| )", "", s)
    return re.sub(r"[\s{}$~\\.,;:'’`\"()]", "", s).lower()


def last_json(text):
    for line in reversed((text or "").strip().splitlines()):
        line = line.strip().strip("`")
        if line.startswith("{") and line.endswith("}"):
            try:
                return json.loads(line)
            except Exception:
                pass
    m = re.findall(r"\{[^{}]*\}", text or "")
    for cand in reversed(m):
        try:
            return json.loads(cand)
        except Exception:
            pass
    return None


rows = []
cost = collections.defaultdict(float)
tok = collections.defaultdict(lambda: [0, 0, 0])
for line in open(D / "results.jsonl", encoding="utf-8"):
    r = json.loads(line)
    mt, z, design, mid = r["custom_id"].split("-", 3)
    it = items[mid]
    alts = it["alts"].split(" || ")
    order = [int(x) for x in it["order"].split(",")]
    ref = it["dm01_decision"]
    # exact text first (K and k are different readings), then the letters-only comparison among the other alternatives
    ref_idx = 0 if ref == "first" else (next((k for k, a in enumerate(alts) if a.strip() == it["dm01_reading"].strip()), None) if
                                        any(a.strip() == it["dm01_reading"].strip() for a in alts) else
                                        next((k for k in range(1, len(alts)) if key(alts[k]) == key(it["dm01_reading"])), None)) if ref == "alternative" else None
    if r["type"] != "succeeded":
        rows.append(dict(model=mt, zoom=z, design=design, id=mid, cls=it["in_class"], kind=it["kind"], ref=ref, answer="(error)", verdict="error"))
        continue
    u = r["usage"]
    inp = u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)
    out = u.get("output_tokens", 0)
    cost[(mt, z, design)] += inp * PRICE[mt][0] / 1e6 + out * PRICE[mt][1] / 1e6
    t = tok[(mt, z, design)]
    t[0] += inp
    t[1] += out
    t[2] += 1
    j = last_json(r.get("text", "")) or {}
    reading = str(j.get("reading", ""))
    if design == "p1":
        a = str(j.get("answer", "")).strip().strip('"').upper()
        if a in ("NEITHER",):
            pick = "neither"
        elif a in ("UNDECIDABLE",):
            pick = "undecidable"
        elif len(a) == 1 and "A" <= a <= "G" and ord(a) - 65 < len(order):
            pick = order[ord(a) - 65]
        else:
            pick = "unparsed"
    else:
        conf = str(j.get("confidence", ""))
        hits = [k for k, al in enumerate(alts) if al.strip() == reading.strip()] or [k for k, al in enumerate(alts) if key(al) == key(reading)]
        pick = hits[0] if hits else ("undecidable" if not reading or reading.lower() in ("?", "illegible", "undecidable") else "neither")
    if pick == "undecidable":
        verdict = "abstained"
    elif pick == "unparsed":
        verdict = "unparsed"
    elif ref in ("first", "alternative"):
        verdict = "right" if pick == ref_idx else "wrong"
    elif ref == "other":
        verdict = "right" if (pick == "neither" and (design == "p1" or key(reading) == key(it["dm01_reading"]))) else \
            "half (saw it is neither)" if pick == "neither" else "wrong"
    else:
        verdict = "no reference"
    rows.append(dict(model=mt, zoom=z, design=design, id=mid, cls=it["in_class"], kind=it["kind"], ref=ref,
                     ref_reading=it["dm01_reading"], answer=pick if isinstance(pick, str) else alts[pick], reading=reading[:80],
                     verdict=verdict, stop=r.get("stop_reason", ""), out_tokens=out))
with open(D / "scores.tsv", "w", encoding="utf-8", newline="") as fh:
    cols = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0].keys()).index(k) if k in rows[0] else 99)
    w = csv.DictWriter(fh, cols, delimiter="\t")
    w.writeheader()
    w.writerows(rows)

L = [f"# Pilots 1 and 2, set '{SET}': {len(items)} marks of DM01 (cote 1), scored against DM01's decisions", "",
     "| Model | Zoom | Prompt | Right | Wrong | Abstained | Other | Right on the Hua class | Cost | Cost per mark | In / out tokens per request |",
     "|---|---|---|---|---|---|---|---|---|---|---|"]
for mt in ("haiku", "sonnet", "opus", "solmedium", "solhigh", "solmax"):
    for z in ("word", "line", "both"):
        for design in ("p1", "p2"):
            rs = [r for r in rows if (r["model"], r["zoom"], r["design"]) == (mt, z, design)]
            if not rs:
                continue
            c = collections.Counter(r["verdict"] for r in rs)
            cl = [r for r in rs if r["cls"] == "1" and r["ref"] != "undecided"]
            t = tok[(mt, z, design)]
            L.append(f"| {LABEL[mt]} | {z} | {'readings offered' if design == 'p1' else 'free reading'} | {c['right']} | {c['wrong']} | {c['abstained']} | "
                     f"{len(rs) - c['right'] - c['wrong'] - c['abstained']} | {sum(1 for r in cl if r['verdict'] == 'right')} of {len(cl)} | "
                     f"${cost[(mt, z, design)]:.4f} | ${cost[(mt, z, design)] / max(1, len(rs)):.5f} | "
                     f"{t[0] // max(1, t[2]):,} / {t[1] // max(1, t[2]):,} |")
L += ["", f"Total cost of the set: ${sum(cost.values()):.3f}.", ""]
(D / "SUMMARY.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
