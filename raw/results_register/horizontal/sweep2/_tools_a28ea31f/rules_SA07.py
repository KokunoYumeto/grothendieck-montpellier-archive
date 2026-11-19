# SA07 (Theorie des motifs III), sweep 2 part 1. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
DOCS = "SA07-9"
NEW = []
FOLDER = {"K10-01": "SA07-15", "K10-02": "SA07-15", "K10-03": "SA07-15", "K10-04": "SA07-3", "K10-05": "SA07-16",
          "K10-06": "SA07-16", "K10-07": "SA07-16", "K16-02": "SA07-17", "K19-01": "SA07-18", "K19-02": "SA07-18",
          "K19-03": "SA07-18", "K19-04": "SA07-18", "K19-05": "SA07-18", "K19-06": "SA07-18"}
C = "MPL_15_195-228+18_002-017_chatB"
B = "opening-read"
RULES = [
    (r"^(R27|R34|R35)\b", "SA07-5", C, B),
    (r"^R28\b", "SA07-9", C, B),
    (r"^(R29|R30|R31|R32|R33|R38)\b", "SA07-6", C, B),
    (r"^(R36|R37)\b", "SA07-3", C, B),
    (r"^PG\d\d\b", "SA07-2", C, B),
    (r"^RL0[23]\b", "SA07-2", C, B),
    (r"^RL01\b|^RL07\b", "SA07-3", C, B),
    (r"^RL04\b", "SA07-6", C, B),
    (r"^RL0[56]\b", "SA07-12", C, B),
    (r"^RL08\b", "SA07-4", C, B),
    (r"^(B0[6-8]|O0[1-4])\b", "SA07-4", C, B),
    (r"^(Reused typescripts|Complete ordered read|Context search|Per-note context|Period context|Periods and arithmetic|Lefschetz correspondences and standard|Linear/nonlinear comparisons and Oda|Additional references)", "SA07-9", C, "heading"),
    (r"^L5\.", "SA07-3", C, B),
    (r"^L[2346]\.", "SA07-12", C, B),
    (r"^P-A\.", "SA07-2", C, B),
    (r"^S2\.", "SA07-7", C, B),
    (r"^S3\.", "SA07-2", C, B),
    (r"^S[145]\.", "SA07-4", C, B),
]
FORCE = {}
FLAGS = []
OBJ = {}
NOTES = """
What the gap list added to SA07:
- The 28 Codex sheet notes on K10, K16-02 and K19 follow the sweep-1 folder map (SA07-15, -16, -3, -17, -18; title sheets to SA07-9).
- The 64 entries of the second chat MPL_15_195-228+18_002-017_chatB that the broad agent could not link by script are placed as parallel witnesses of MPL_15_195-228+18_002-017, under the main chat's item for the same series where there is one: PG (periods) to SA07-2, B and O (Hom comparisons, Oda) to SA07-4, the cote 18 R notes on fundamental classes, the Gysin claim and the integral model to SA07-6, the cote 15 R notes on the reused root-space and coalgebra typescripts to SA07-5, the L notes on cote 16 (ring and category, operator normalizations, lettering audit) to SA07-12, the semisimplicity notes to SA07-3, the worked elliptic example P-A (y^2 = x^3 - x + 1, discriminant -368, which I recomputed) to SA07-2, and the apparatus (read-through, context searches, references) to SA07-9.
- The second-pass check events on MPL_16+47+54+44 are in SA18's CHECK_EVENTS, written once.
"""
CHECKS = [
    ("MPL_15_195-228+18_002-017_chatB#89", "2026-11-18", "recomputed the discriminant of y^2 = x^3 - x + 1: -16(4(-1)^3 + 27) = -16 * 23 = -368",
     "agrees with the note", "sweep2/SA07/PLACEMENT.tsv"),
]
