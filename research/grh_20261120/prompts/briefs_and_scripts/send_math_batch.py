"""Send the requests_NN.jsonl files of one folder (pilot/ or full/) through the Message Batches API (50 % off), wait,
and save the results with usage (21 Nov 2026, main session, Claude Opus 5.5 at effort max; adapted from
masullo_transcription/pilot_send_claude.py). Run through claude_tools/run_with_note_key.py (the key is read from the
user's note and never printed):
    python -I C:/Users/user/Documents/claude_tools/run_with_note_key.py send_math_batch.py pilot|full"""
import json, pathlib, sys, time
import anthropic

D = pathlib.Path(__file__).resolve().parent / (sys.argv[1] if len(sys.argv) > 1 else "pilot")
client = anthropic.Anthropic(default_headers={"accept-encoding": "gzip"})  # the SDK here fails on brotli replies
ids = D / "batches.json"
batches = json.loads(ids.read_text(encoding="utf-8")) if ids.is_file() else {}
for f in sorted(D.glob("requests_*.jsonl")):
    if f.name in batches:
        continue
    reqs = [json.loads(line) for line in open(f, encoding="utf-8")]
    b = client.messages.batches.create(requests=reqs)
    batches[f.name] = b.id
    ids.write_text(json.dumps(batches, indent=1), encoding="utf-8")
    print("sent", f.name, "->", b.id, len(reqs), "requests", flush=True)
t0 = time.time()
pending = dict(batches)
while pending:
    for name, bid in list(pending.items()):
        b = client.messages.batches.retrieve(bid)
        if b.processing_status != "ended":
            continue
        c = b.request_counts
        out = D / name.replace("requests_", "results_")
        with open(out, "w", encoding="utf-8") as fh:
            for r in client.messages.batches.results(bid):
                rec = {"custom_id": r.custom_id, "type": r.result.type}
                if r.result.type == "succeeded":
                    m = r.result.message
                    rec.update(model=m.model, stop_reason=m.stop_reason, usage=m.usage.model_dump(),
                               text="".join(getattr(bl, "text", "") for bl in m.content if bl.type == "text"))
                else:
                    rec["error"] = str(getattr(r.result, "error", r.result))[:500]
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"{name}: ended after {(time.time() - t0) / 60:.1f} min, succeeded {c.succeeded}, errored {c.errored} -> {out.name}",
              flush=True)
        del pending[name]
    if pending:
        time.sleep(30)
print("all results saved", flush=True)
