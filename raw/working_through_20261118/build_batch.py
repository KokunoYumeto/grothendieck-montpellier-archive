"""Build the working-through programme in bulk, in waves (19 Nov 2026, the coordinator's message of ~01:5x UTC: account
4's Pro, sent by hand, about 200 prompts of 30-90 minutes over 48 hours).

The queue (QUEUE.tsv, written once, so the numbering stays fixed across waves):
- the topics in the order of the neglect table (results_register/horizontal/sweep2/GLOBAL/NEGLECT.tsv: least
  researched first; La Longue Marche and the Dérivateurs last), round-robin, so that prompts sent together are on
  different topics (memory cancel-lm-derivateurs-bias);
- within a topic, its object prompts (OBJECTS_PLAN.tsv) and its folder ranges (UNITS_PLAN.tsv) alternate, each in its
  plan's order (his chronology); the ranges alternate variant A and variant B, so that the returns give the A/B
  comparison the pilots never gave;
- prompts estimated over 90 minutes are left out of the queue.
Each prompt is built into batch_20261119/<NNN>_<id>_<V>/ (V: O for an object, A or B for a range), flat, with the
builders of this folder (lint --lint-math, privacy pass, zips under 400 MB); ORDER.tsv lists what is built.

usage: python -I -B build_batch.py N        (build the next N prompts of the queue)
Written by Claude Opus 5.5 at effort max (agent a11a6de3, no sub-agents), 19 Nov 2026."""
import collections
import json
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wt_common as W  # noqa: E402
import build_object_prompts as O  # noqa: E402
import build_working_through as U  # noqa: E402

HERE = W.HERE
BATCH = HERE / "batch_20261119"
QUEUE = BATCH / "QUEUE.tsv"
ORDER = BATCH / "ORDER.tsv"
NEGLECT = W.D / "results_register/horizontal/sweep2/GLOBAL/NEGLECT.tsv"
MAX_MINUTES = 90
LAST = {"SA28", "SA29", "SA30", "SA31", "SA32"}  # around La Longue Marche and the Dérivateurs: after every other topic
QCOLS = ["n", "id", "topic", "kind", "variant", "expected_minutes", "cote", "scans_or_pages", "folder"]
OCOLS = ["n", "id", "topic", "kind", "variant", "expected_minutes", "files", "MB", "cote", "scans_or_pages", "lint",
         "privacy_redactions", "folder", "built_utc"]


def rows_of(p):
    return list(W.csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


def make_queue():
    rank = [r["topic"] for r in rows_of(NEGLECT)]
    objs = [r for r in rows_of(O.PLAN) if r["eligible"] == "yes" and int(r["expected_minutes"] or 0) <= MAX_MINUTES]
    units = [r for r in rows_of(U.PLAN) if int(r["expected_minutes"] or 0) <= MAX_MINUTES]
    topics = rank + sorted(({r["topic"] for r in objs} | {r["sweep_topic"] for r in units}) - set(rank))
    per = {}
    for ti, t in enumerate(topics):
        ob = sorted((r for r in objs if r["topic"] == t), key=lambda r: int(r["rank"]))
        un = sorted((r for r in units if r["sweep_topic"] == t), key=lambda r: int(r["rank"]))
        q, i, j = [], 0, 0
        while i < len(ob) or j < len(un):
            if i < len(ob):
                r = ob[i]
                q.append(dict(id=r["prompt_id"], topic=t, kind="object", variant="O", expected_minutes=r["expected_minutes"],
                              cote=r["cote"], scans_or_pages=r["cotes_scans"][:80]))
                i += 1
            if j < len(un):
                r = un[j]
                q.append(dict(id=r["unit_id"], topic=t, kind="range", variant="AB"[(j + ti) % 2],
                              expected_minutes=r["expected_minutes"], cote=r["cote"], scans_or_pages=r["scans"]))
                j += 1
        per[t] = collections.deque(q)
    order = []
    for tier in ([t for t in topics if t not in LAST], [t for t in topics if t in LAST]):
        while any(per[t] for t in tier):
            for t in tier:
                if per[t]:
                    order.append(per[t].popleft())
    for n, x in enumerate(order, 1):
        x["n"] = n
        x["folder"] = f"{n:03d}_{x['id']}_{x['variant']}"
    BATCH.mkdir(parents=True, exist_ok=True)
    QUEUE.write_text(W.tsv(order, QCOLS), encoding="utf-8", newline="")
    return order


def main(n_new):
    BATCH.mkdir(parents=True, exist_ok=True)
    # regenerate both plans first, so that every id of the queue resolves
    units_o, objs, items, idx = O.plan()
    urows, D = U.plan()
    queue = rows_of(QUEUE) if QUEUE.exists() else make_queue()
    done = {r["folder"] for r in rows_of(ORDER)} if ORDER.exists() else set()
    built = rows_of(ORDER) if ORDER.exists() else []
    todo = [q for q in queue if q["folder"] not in done][:n_new]
    known_o = {u["id"] for u in units_o}
    known_u = {r["unit_id"] for r in urows}
    for q in todo:
        folder = BATCH / q["folder"]
        if folder.exists():
            shutil.rmtree(folder)
        folder.mkdir(parents=True)
        if q["kind"] == "object":
            if q["id"] not in known_o:
                print("skipped (no longer in the plan):", q["id"])
                shutil.rmtree(folder)
                continue
            bj = O.build(q["id"], units_o, objs, items, idx, folder=folder)
        else:
            if q["id"] not in known_u:
                print("skipped (no longer in the plan):", q["id"])
                shutil.rmtree(folder)
                continue
            bj = U.build(q["id"], urows, D, variants=q["variant"], folders={q["variant"]: folder})[0]
        files = sorted(p for p in folder.iterdir())
        mb = round(sum(p.stat().st_size for p in files) / 1e6, 1)
        built.append(dict(n=q["n"], id=q["id"], topic=q["topic"], kind=q["kind"], variant=q["variant"],
                          expected_minutes=bj.get("expected_minutes", q["expected_minutes"]), files=len(files), MB=mb,
                          cote=q["cote"], scans_or_pages=q["scans_or_pages"], lint="pass" if bj["ok"] else "FAIL " + bj["lint"][:80],
                          privacy_redactions="; ".join(f"{k} {v}" for k, v in sorted(bj.get("privacy", {}).items())) or "none",
                          folder=q["folder"], built_utc=f"{W.NOW():%Y-%m-%d %H:%M}"))
        built.sort(key=lambda r: int(r["n"]))
        ORDER.write_text(W.tsv(built, OCOLS), encoding="utf-8", newline="")
    ok = sum(1 for r in built if r["lint"] == "pass")
    print(f"WAVE DONE: {len(todo)} built now; {len(built)} in ORDER.tsv ({ok} lint pass); "
          f"{sum(float(r['MB']) for r in built):.0f} MB; queue {len(queue)}; last n {max(int(r['n']) for r in built) if built else 0}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 40)
