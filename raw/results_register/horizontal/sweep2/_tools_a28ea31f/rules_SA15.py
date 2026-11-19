# SA15 (Cristaux), sweep 2 part 1. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
import re
DOCS = "SA15-12"
NEW = [
    ("pd", "divided-power structures (cote 5): PD-ideals and the algebra Gamma_A, the operations pi^n and their relations, p-adic valuations of n! and digit sums, normal forms, the DVR condition e <= p-1, logarithm and exponential",
     "(notes) cote 5, scans 5-14, 21-27, 32-36, 39-47: constructions announced 'On va construire', relations 'Quelles sont les relations?', several confidence-rated recomputations by the note-writer"),
    ("pcoh", "p-adic cohomology before crystals: the letter 'sur coh. p-adiques' (cote 5, scans 49-53) and the cote 7 text (scans 18-53): Washnitzer-Monsky cohomology, coefficient rings W(k), comparison with de Rham, the Gauss-Manin connection, stratified sites, rigid-analytic GAGA, constant Z_p coefficients",
     "(notes) 'un exces d'optimisme nous ferait esperer' (constant Z_p coefficients), 'Il semble que le theoreme suivant soit vrai', 'Une definition de la coh. p-adique independante de ...', 'Il est sans espoir que cette approche ...'"),
    ("cdt", "crystalline Dieudonne theory of abelian schemes, Barsotti-Tate groups and finite flat group schemes: the Dieudonne crystal, liftings and Serre-Tate, the universal extension, formal moduli and their smoothness, anti-equivalences over Lambda_n (cote 6, scans 22-32 and 52-66)",
     "(notes) 'je m'etais canule' withdraws an earlier expectation (6:22); section 2.7 retracts the preceding conjectures (6:27); 'Je n'ai pas verifie' (6:24); formal moduli of dimension g(g+1)/2 for a polarization (6:57)"),
    ("ell_red", "reduction of elliptic curves over p-adic fields: ordinary good reduction, the extension class in H^1(K, L^-2 (x) T_p(G_m)), Serre's canonical liftings, integrality of the invariant (cote 6, scans 33-37)",
     "(notes) 'J'ai envie de conjecturer' (6:35), 'est-ce tjrs un entier' (6:36), 'on peut conjecturer' and 'Je conjecture' (6:37)"),
    ("tate_hodge", "Hodge-Tate theory: 'Gribouillis de Tate sur sa theorie' and 'Questions diverses en theorie de Tate-Hodge' (cote 6, scans 38-46): Tate isomorphisms with H^q(X, Omega^p), a conjectured canonical isomorphism, the link with Washnitzer-Monsky",
     "(notes) items a-f of 6:41 are questions and conjectures; who wrote which sheet (Tate or Grothendieck) is open in the notes"),
    ("bonred", "good reduction of abelian schemes ('Bonne reduction et ...', cover dated 14 March 1967; cote 100): extension of abelian schemes over a normal base, full faithfulness and essential surjectivity of the restriction to the generic fibre, descent data and polarizations, moduli with rigidification, the use of Tate's theorem",
     "(notes) 'Je sais maintenant prouver le theoreme de ...' (100:50), 'On gagne!' (100:53), 'Il reste a prouver la ...' (100:17)"),
    ("etale_duality", "global duality for etale cohomology without relative purity, for a compactifiable smooth map and general coefficient rings (the letter docketed 'Lettre Deligne / sur coh. p-adiques', cote 5, scan 50)",
     "(notes) 'qui permet d'eviter tout recours au theoreme de purete relative'; 'Je pense qu'il vaut le coup d'inclure cette forme generale'"),
]
FOLDER = {"K4-01": "SA15-9", "K8-01": "SA15-2", "K9-01": "SA15-10", "K9-02": "SA15-11"}
PK = ["MPL_5+6_001-037", "MPL_6_038-067+7_001-060", "MPL_8_079-081+9+4+100"]
OVERLAP_SKIP = PK
DOCRX = re.compile(r"reused|errata|correction sheet|proof-correction|preface|signed letter|cancelled letter|^the cover|cover (bears|heading|reads|labels|announces)"
                   r"|UNIVERSIT|upside down|Kuiper|S[ée]minaire Cartan|THEOREM 12|Italian vocabulary|APA-style", re.I)
RANGES = {
    "5": [(3, 3, "SA15-1"), (4, 4, "SA15-12"), (5, 14, "pd"), (15, 20, "SA15-2"), (21, 27, "pd"), (28, 31, "SA15-1"), (32, 36, "pd"),
          (37, 37, "SA15-1"), (38, 38, "SA15-12"), (39, 39, "pd"), (40, 40, "SA15-12"), (41, 41, "pd"), (42, 42, "SA15-12"),
          (43, 43, "pd"), (44, 44, "SA15-12"), (45, 48, "pd"), (49, 53, "pcoh")],
    "6": [(2, 7, "SA15-1"), (8, 12, "SA15-2"), (13, 21, "SA15-1"), (22, 32, "cdt"), (33, 37, "ell_red"), (38, 46, "tate_hodge"),
          (47, 51, "SA15-3"), (52, 66, "cdt")],
    "7": [(3, 17, "SA15-1"), (18, 53, "pcoh"), (54, 60, "SA15-1")],
    "8": [(79, 81, "SA15-8")],
    "9": [(2, 14, "SA15-10"), (15, 29, "SA15-11")],
    "4": [(2, 12, "SA15-9")],
    "100": [(2, 53, "bonred")],
}


def _opening(t, n=14):
    t = re.sub(r"\*\*Kind:[^*]*\*\*", "", t)
    t = re.sub(r"[#*`>|]", "", t)
    return " ".join(t.split()[:n])


P1, P2, P3 = PK
CORR = {}
def _c(pkg, nums, item, note):
    for n in nums:
        CORR[f"{pkg}#{n}"] = (item, note)
_c(P1, [5, 6, 7], "bonred", "moved in part 2: the isolated printed leaf 'THEOREM 12' (Serre-Tate, good reduction of CM abelian varieties), not divided powers or a bare document. ")
_c(P1, [24, 25, 27], "SA15-12", "moved in part 2: the upside-down reused typescript on 5:10 (a divisor of A^5 and its projections), not divided powers. ")
_c(P1, [37, 38], "SA15-12", "moved in part 2: a proof-correction list for another document (pages 64-76). ")
_c(P1, [114, 115, 116, 117, 118], "SA15-12", "moved in part 2: an isolated printed leaf on divisors and quasi-functions of an abelian variety (5:34). ")
_c(P1, [125, 126, 127, 128, 129], "SA15-12", "moved in part 2: an isolated printed leaf with a dyadic estimate |phi(2^h m) - 2^h phi(m)| <= (2^h - 1) d (5:36), a height-type argument. ")
_c(P1, [189, 190, 191, 192, 193, 199, 200, 201, 202, 203, 204, 205], "SA15-12", "moved in part 2: an EGA typescript on differentials of complete semi-local rings (draft 18.13.4-5, refs 0,20.4.5-8; 5:46, 5:48), with his margin 'Prendre un anneau topologique plus general ?'. ")
_c(P1, [207, 208, 209, 210], "etale_duality", "moved in part 2: the duality part of the letter docketed 'Lettre Deligne' (5:50). ")
_c(P1, [338, 339], "SA15-2", "moved in part 2: weight-i bicrystal structures at every prime (6:16), an F-crystal matter. ")
_c(P2, [10, 16, 20, 21], "SA15-12", "moved in part 2: the reused typescript on spectral theory (n. 357; 6:42-46), not the Tate-Hodge questions. ")
_c(P2, [104, 105, 106, 107, 108, 109, 110], "pcoh", "moved in part 2: 7:16-17 are about the p-adic cohomology candidate ('Mon espoir initial ... C'est faux malheureusement'). ")
_c(P3, [24, 25, 26], "pcoh", "moved in part 2: the cancelled sheet 9:9 asks how to define the Gauss-Manin connection on R f_*(Omega) directly. ")
_c(P3, list(range(27, 41)), "bonred", "moved in part 2: 9:11-14 are on inertia characters and potentially good reduction (Tate's theorem, Raynaud's criterion, 'faux par Tate'). ")
_c(P3, [165, 166, 167, 173, 174, 175, 176, 182, 183, 191, 197, 198, 204, 205, 211, 223, 224, 225, 231, 232, 238, 245, 246, 247,
         253, 254, 259, 260, 266, 267, 275, 291, 292, 293, 301, 302, 303, 310, 311, 312, 317, 318, 319, 320, 321], "SA15-12",
   "moved in part 2: an even-numbered sheet of cote 100 (6-46) is reused paper (English quotient-theory typescripts, a preface of 27 Oct 1963, EGA III-IV errata and page proofs, letters), not his good-reduction text. ")
CAPS = {P1: [(75, 10**6), (160, 60), (250, 42), (340, 36), (445, 34)], P2: [(110, 32), (255, 28)], P3: [(148, 26), (349, 24)]}


def _readbasis(e):
    pkg, n = e["entry_id"].rsplit("#", 1)
    n = int(n)
    for hi, cap in CAPS.get(pkg, []):
        if n <= hi:
            w = int(e.get("words") or 0)
            return "entry-read" if w <= cap else f"entry-read (first {cap} words)"
    return "entry-read"


def SCANS(e, t):
    m = re.search(r"Cote (\d+), scans? (\d+)", e.get("heading", ""))
    return str(int(m.group(2))) if m else ""


def FALLBACK(e, t):
    if not any(e["entry_id"].startswith(p) for p in PK):
        return None
    hd = e.get("heading", "")
    op = _opening(t)
    rb = _readbasis(e)
    if e["entry_id"] in CORR:
        return (CORR[e["entry_id"]][0], rb + "; placement corrected in part 2", CORR[e["entry_id"]][1])
    if hd.startswith("References") or DOCRX.search(op):
        return ("SA15-12", rb + " (a document, title or reused sheet)")
    m = re.search(r"Cote (\d+), scans? (\d+)", hd)
    if not m:
        return None
    c, s = m.group(1), int(m.group(2))
    for a, b, it in RANGES.get(c, []):
        if a <= s <= b:
            return (it, rb + "; section of the text by cote and scan, confirmed by the reading")
    return None


FORCE = {}
FLAGS = [
    ("a link across folders", "MPL_5+6_001-037, cote 6, scans 33-37 (entries #421-#444); SA16",
     "The crystals package carries a short text 'Reduction des courbes elliptiques': ordinary good reduction, the extension class in H^1(K, L^-2 (x) T_p(G_m)), Serre's canonical liftings, and three conjectures in his words ('J'ai envie de conjecturer', 'on peut conjecturer', 'Je conjecture'). Its object is SA16's (elliptic curves); placed here as SA15's new item and linked.",
     "openings of #421-#444, read"),
    ("a link across folders", "MPL_8_079-081+9+4+100, cote 100, scans 2-53 (entries #149-#349); SA18-11",
     "Cote 100 holds 'Bonne reduction et ...' (cover dated 14 March 1967): extension of abelian schemes from the generic fibre, descent data, polarizations, rigidified moduli, Tate's theorem invoked twice, 'Je sais maintenant prouver le theoreme de ...' (100:50). Its object is SA18's (abelian varieties: integral models, SA18-11). The same scans carry EGA IV errata sheets (14.4.8, 14.4.10, 15.6.3-4; III 3.4, 4.3.6; IV 3.1.10), a letter signed 'L Illusie' and a cancelled letter of 7 April 1967; those go to SA15-12.",
     "openings of #149-#349, read"),
    ("a link across folders", "MPL_5+6_001-037 cote 5 scans 49-53 and MPL_6_038-067+7_001-060 cote 7 scans 18-53; SA15-1",
     "Two texts on p-adic cohomology before the crystalline site (a letter 'sur coh. p-adiques' and the cote 7 draft on Washnitzer-Monsky, W(k) coefficients, de Rham comparison and Gauss-Manin) are placed as one new item; the cote 7 draft runs straight into the 'sites ad hoc' and 'faisceaux speciaux' of scans 54-60 and the crystalline site of sweep 1 (cote 7, scans 61-72).",
     "openings read"),
    ("the same thing noted with different readings or statements", "MPL_6_038-067+7_001-060#1-#2 (cote 6, scans 38-40); new item Hodge-Tate",
     "The cover 'Gribouillis de Tate sur sa theorie' names Tate; the note says the attribution of the hands on the following sheets is not established. Items a-f of scan 41 (Tate isomorphisms, a link with Washnitzer-Monsky) should not be ascribed to Grothendieck or to Tate until the hands are compared on the scans.",
     "openings of #1-#8, read"),
]
OBJ = {"ell_red": {"cross_topic": "linked SA16-13 (H0AP), SA16-19"},
       "bonred": {"cross_topic": "linked SA18-11 (H002, integral models and local duality)"},
       "cdt": {"cross_topic": "linked SA14-2 (H0A1, universal vector extension); SA18-8, SA19-3 (Oda, Dieudonne modules)"},
       "pcoh": {"cross_topic": "SA15-1 inside the topic"},
       "tate_hodge": {"cross_topic": "SA15-11 inside the topic"},
       "etale_duality": {"cross_topic": "the SGA 4 duality themes (link only)"},
       "SA15-8": {"statement+": "(part 2) cote 8 scans 79-81 continue it: the canonical class in Ext^2 / H^2 of an endomorphism sheaf, the obstruction to lifting a representation over Z/n^2 Z ('D'apres Illusie'), injectivity of H^2(B_pi, -) -> H^2(S, -)"},
       "SA15-12": {"statement+": "(part 2) also: the reused sheets of cote 100 (even scans 6-46: English typescripts on quotients by group actions with a preface dated Harvard, 27 Oct 1963; EGA III-IV errata and page proofs, 'Bon a tirer' 14 March 1967; a letter of 7 April 1967 on EGA IV 15.5-15.6; a letter signed L Illusie, 24 Feb 1968), printed leaves in cote 5 (5:10, 5:34, 5:36), an EGA typescript on differentials (5:46, 5:48), the spectral-theory typescript n. 357 (6:42-46)"},
       "pcoh": {"cross_topic": "SA15-1 inside the topic; SA05-2 (the Lefschetz-type cycle route to independence of l, 7:28-31)", "statement+": "(part 2) the cover of 5:49 reads 'Lettre Deligne / sur coh. p-adiques': the letter of 5:50-53 is docketed as Deligne's"}}
NOTES = """
What the gap list added to SA15:
- Three Pro packages that NOTES_INDEX missed (1,049 notes): MPL_5+6_001-037 (cote 5 and cote 6 scans 2-37), MPL_6_038-067+7_001-060 (cote 6 scans 38-66, cote 7 scans 3-60) and MPL_8_079-081+9+4+100 (cote 8 scans 79-81, cotes 9, 4 and 100). The topic grows from 80 Pro notes to more than 1,100.
- Method: I read the opening words (about eleven) of every note; the item follows the section of the text the note's cote and scan belong to, and notes whose opening names a document, a cover, a reused typescript, an errata sheet or a letter go to SA15-12. Each note also carries its own 'Kind' in PLACEMENT.
- New items: divided powers (cote 5); p-adic cohomology before crystals (letter on cote 5, the cote 7 draft); crystalline Dieudonne theory of abelian schemes and Barsotti-Tate groups (cote 6); reduction of elliptic curves (cote 6, scans 33-37); Hodge-Tate theory (cote 6, scans 38-46); good reduction of abelian schemes (cote 100, March 1967). Cote 6 scans 2-21 (crystals, p-crystals, Dieudonne modules, bi-crystals and weights) join SA15-1 and SA15-2; Barsotti's question and Manin (6:47-51) join SA15-3; cote 9 joins SA15-10 and SA15-11; cote 4 joins SA15-9; cote 8 scans 79-81 continue SA15-8.
- Many notes in these packages are the note-writer's own recomputations ('Confidence: high. Reason: ...') and research suggestions ('Research question: ...'); they are notes about the page, not his statements.
"""
CHECKS = [("MPL_6_038-067+7_001-060#1", "2026-11-18", "the attribution of hands decided on the images (cote 6, scans 38-45; scan 39 contrast-enhanced)", "6:39 is in Tate's hand; 6:38 and 6:40-46 are his", "sweep2/REPORTS/hands_formulaire_and_tate.md")]
