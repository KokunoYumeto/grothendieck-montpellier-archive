import sys, re
sys.path.insert(0, r"C:/Users/user/Documents/results_register/horizontal/sweep2/_tools_a28ea31f")
import hsweep2 as H
pkg, n = sys.argv[1], int(sys.argv[2])
lo, hi = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (0, 10**6)
for e in H.gap("SA15"):
    if not e["entry_id"].startswith(pkg):
        continue
    num = int(e["entry_id"].rsplit("#", 1)[1])
    if not lo <= num <= hi:
        continue
    t = H.body(e)
    t = re.sub(r"\*\*Kind:[^*]*\*\*", "", t)
    hd = e["heading"]
    m = re.search(r"Cote (\d+), scans? (\d+)", hd)
    cs = f"{m.group(1)}:{int(m.group(2))}" if m else hd[:20]
    k = re.search(r"[—-]\s*([a-z][a-z ]+)$", hd)
    k = "".join(w[0] for w in k.group(1).split()) if k else ""
    w = " ".join(H.clean(re.sub(r"[#*`>|]", "", t)).split()[:n])
    print(f"{num}|{cs}|{k}|{w}")
