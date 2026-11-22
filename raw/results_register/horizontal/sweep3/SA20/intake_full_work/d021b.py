"""D.021 F4 convention check: rerun d021.run with the transposed F4 Cartan matrix (roles of long and short roots exchanged).
Claude Opus 5.5 at effort max, acf08879a01b97ed4, 22 Nov 2026."""
import runpy
ns = runpy.run_path("d021.py", run_name="d021_lib")
orig = ns["cartan"]
def cartanT(t):
    A = orig(t)
    return [list(r) for r in zip(*A)] if t in ("F4", "G2") else A
ns["run"].__globals__["cartan"] = cartanT
for t in ["G2", "F4"]: ns["run"](t)
