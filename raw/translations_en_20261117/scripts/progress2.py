import json, pathlib, time
R = pathlib.Path(__file__).resolve().parent.parent
time.sleep(175)
st = json.load(open(R / "_work2/runs/state.json"))
usd = sum(((v.get("input_tokens", 0) - v.get("cached_tokens", 0)) + 0.1 * v.get("cached_tokens", 0) + 5 * v.get("output_tokens", 0)) / 1e6 for v in st.values())
log = (R / "_work2/layer.log").read_text(encoding="utf-8").splitlines()
pk = [l for l in log if "MPL_" in l or "STOP" in l or "DONE" in l]
print(sum(1 for v in st.values() if v.get("status") == "completed"), "done of", len(st), f"${usd:.2f} |", pk[-1] if pk else "")
