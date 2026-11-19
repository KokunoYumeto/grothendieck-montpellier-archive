import sys
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
print(len(core.ROWS), len(core.RUNS))
tests = ["LM7_PUSH D.50, E.58; refereed", "TOTASPH C.8–C.10 (interpolation audited)", "F149-B6; Proved",
         "LM5 F.21–F.23, F.35, F.39, F.48 (proofs read)", "AN D.30", "S6_02 B.4.2", "LM4 F.21-F.22",
         "CK-A3, CK-A6, CK-A7", "AS-A.3 = AR.3", "LM6 E.19, E.21, E.35–E.39: the class",
         "TOTAL_EXACT_2 A.30–A.34 reduction", "DF A.4--A.8", r"ORIGINAL LM7\_PUSH~E.61/LM7\_PUSH~E.65 pur",
         "R1 (attached LM8 G.10)", "LM8 B.31 are not", "STRATA B.1-B.2 and C.1 checked", "POLESB.2B.5",
         "GT C.2.1 about", "TOTEX D.4 = PRETOT F.3; TOTEX D.5 = PRETOT F.6", "LM1 E.3; LM1 E.10"]
for t in tests:
    print(t, "->", [(a, b) for a, b, c, d in core.cross_refs(t, "X")])
