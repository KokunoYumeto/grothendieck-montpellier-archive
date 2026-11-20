"""The pilot on GPT-6.2 Sol through the OpenAI Batch API (half price; Sol has no Flex tier) (20 Nov 2026, main session,
Claude Opus 5.5 at effort max; the user: "6.2 at medium, high, and max ... the literal cheapest semi-competent model ...
try it"). Same marks, images and prompt (readings offered, the line and the word crop) as the Claude set full_v2.
The key is read inside this process from a local note and never printed or written anywhere.

python -I -B pilot12_openai.py <name> <n_marks|all> [efforts]   e.g. sol_small 10 medium,high,max
-> pilots_api_20261120/<name>/requests_openai.jsonl, batch.json, results.jsonl (the Claude results' format), items.tsv"""
import csv
import json
import pathlib
import re
import shutil
import sys
import time

from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")
NAME = sys.argv[1]
NMARKS = sys.argv[2] if len(sys.argv) > 2 else "10"
EFFORTS = (sys.argv[3] if len(sys.argv) > 3 else "medium,high,max").split(",")
ROOT = pathlib.Path(__file__).resolve().parent.parent / "pilots_api_20261120"
SRC, OUT = ROOT / "full_v2", ROOT / NAME
OUT.mkdir(parents=True, exist_ok=True)
MODEL = "gpt-6.2-sol"

items = list(csv.DictReader(open(SRC / "items.tsv", encoding="utf-8"), delimiter="\t"))
if NMARKS == "all":
    ids = [it["id"] for it in items]
else:
    n = int(NMARKS)
    cls = sorted(it["id"] for it in items if it["in_class"] == "1")
    rest = sorted(it["id"] for it in items if it["in_class"] != "1")
    ids = cls[:n // 2] + rest[:n - n // 2]
keep = set(ids)
with open(OUT / "items.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, list(items[0].keys()), delimiter="\t")
    w.writeheader()
    w.writerows([it for it in items if it["id"] in keep])

bj = OUT / "batch.json"
note = pathlib.Path("<the note that holds the API key>").read_text(encoding="utf-8", errors="replace")
keys = re.findall(r"sk-[A-Za-z0-9_\-]{20,}", note)
del note
if not keys:
    sys.exit("no OpenAI key found in the note")
client = OpenAI(api_key=keys[0])
del keys

if not bj.is_file():
    lines = 0
    with open(OUT / "requests_openai.jsonl", "w", encoding="utf-8") as fo:
        for line in open(SRC / "requests.jsonl", encoding="utf-8"):
            r = json.loads(line)
            mt, z, design, mid = r["custom_id"].split("-", 3)
            if mt != "opus" or design != "p1" or mid not in keep:  # one copy of each Claude request is enough to convert
                continue
            p = r["params"]
            content = []
            for c in p["messages"][0]["content"]:
                if c["type"] == "text":
                    content.append({"type": "input_text", "text": c["text"]})
                else:
                    content.append({"type": "input_image", "image_url": f"data:{c['source']['media_type']};base64,{c['source']['data']}", "detail": "high"})
            for eff in EFFORTS:
                body = {"model": MODEL, "instructions": p["system"], "input": [{"role": "user", "content": content}],
                        "reasoning": {"effort": eff}, "max_output_tokens": 12000}
                fo.write(json.dumps({"custom_id": f"sol{eff}-{z}-{design}-{mid}", "method": "POST", "url": "/v1/responses", "body": body}) + "\n")
                lines += 1
    f = client.files.create(file=open(OUT / "requests_openai.jsonl", "rb"), purpose="batch")
    b = client.batches.create(input_file_id=f.id, endpoint="/v1/responses", completion_window="24h")
    bj.write_text(json.dumps({"id": b.id, "file": f.id, "requests": lines, "model": MODEL, "efforts": EFFORTS}), encoding="utf-8")
    print("sent OpenAI batch", b.id, "with", lines, "requests", flush=True)
bid = json.loads(bj.read_text(encoding="utf-8"))["id"]
t0 = time.time()
while True:
    b = client.batches.retrieve(bid)
    if b.status in ("completed", "failed", "expired", "cancelled"):
        break
    time.sleep(30)
print(f"batch {b.status} after {(time.time() - t0) / 60:.1f} min; counts {b.request_counts}", flush=True)
recs = []
for fid, ok in ((b.output_file_id, True), (b.error_file_id, False)):
    if not fid:
        continue
    for line in client.files.content(fid).text.splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        resp = (o.get("response") or {})
        body = resp.get("body") or {}
        rec = {"custom_id": o["custom_id"]}
        if ok and resp.get("status_code") == 200 and body.get("status") in ("completed", "incomplete"):
            text = "".join(c.get("text", "") for item in body.get("output", []) if item.get("type") == "message"
                           for c in item.get("content", []) if c.get("type") == "output_text")
            u = body.get("usage") or {}
            rec.update(type="succeeded", model=body.get("model"), stop_reason=body.get("status"), text=text,
                       usage={"input_tokens": u.get("input_tokens", 0), "output_tokens": u.get("output_tokens", 0),
                              "reasoning_tokens": (u.get("output_tokens_details") or {}).get("reasoning_tokens", 0),
                              "cached_tokens": (u.get("input_tokens_details") or {}).get("cached_tokens", 0)})
        else:
            rec.update(type="errored", error=json.dumps(o.get("error") or body.get("error") or resp)[:400])
        recs.append(rec)
with open(OUT / "results.jsonl", "w", encoding="utf-8") as fh:
    for rec in recs:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
print("results saved:", len(recs), "| errored:", sum(1 for r in recs if r["type"] != "succeeded"), flush=True)
