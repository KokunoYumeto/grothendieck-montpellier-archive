# SA06 (Theorie des motifs II), sweep 2 part 1. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
import re
DOCS = "SA06-13"
NEW = []
FOLDER = {"K14-02": "SA06-3", "K14-03": "SA06-3", "K14-05": "SA06-3", "K14-06": "SA06-3", "K14-04": "SA06-4",
          "K14-08": "SA06-6", "K14-09": "SA06-7", "K15-02": "SA06-8", "K15-05": "SA06-10", "K15-06": "SA06-16",
          "K15-07": "SA06-15", "K15-08": "SA06-15", "B15-01": "SA06-8"}
R = "MPL_15_034-086:records"
RULES = [
    (r"reused (printed|typescript|analytic)|Reused (printed|typescript|analytic)", "SA06-11", R),
]


def SCANS(e, t):
    if e["entry_id"].startswith("codex:"):
        s = re.findall(r"^\|\s*(\d{1,3})\b|\*\*Scan (\d{1,3})|^- Scan (\d{1,3})", t, re.M)
        return ",".join(sorted({str(int(x)) for g in s for x in g if x}, key=int))
    return ""


def FALLBACK(e, t):
    eid = e["entry_id"]
    if eid.startswith(R):
        s = int(re.split(r"[,/]", e["scans"])[0])
        return ("SA06-8" if s <= 79 else "SA06-9", "opening-read; section by scan (34-79 Deuring and Brandt categories; 84-86 commutative band, Riemann algebra)")
    if eid.startswith("codex:B15"):
        return ("SA06-8", "opening-read; cote 15 Deuring text by its pages")
    return None


FORCE = {}
FLAGS = []
OBJ = {}
NOTES = """
What the gap list added to SA06:
- The 31 research leads of MPL_15_034-086 (cote 15, scans 34-86) follow the sweep-1 placements of the same scans where they exist, else the section of the text: the Deuring and Brandt categories, mu_n- and mu_2-gerbes, supersingular Frobenius (scans 34-79) to SA06-8; the commutative band and the Riemann algebra (84-86) to SA06-9; the reused printed analytic typescript leaves (ODE, implicit functions, majorants; printed pages 16-30, interleaved on scans 67-79) to SA06-11.
- The Codex sheet notes follow the sweep-1 folder map; B15-01 ('Categories de Deuring. 1. Categories A-lineaires et (x)-enveloppes'; '2. Domaines d'existence maximaux') joins SA06-8, B15-02 and B15-03 go by the scans they cite.
- SA05's new items on motives over finite fields and Deuring's gerbes (SA05-18, SA05-19) are the same objects as SA06-8, SA06-9 and SA06-10; the merge belongs to the global build.
"""
