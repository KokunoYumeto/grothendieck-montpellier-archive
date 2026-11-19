# SA05 (Theorie des motifs I), sweep 2 part 1. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
import re
DOCS = "SA05-17"
NEW = [
    ("ff_motives", "motives over finite fields: the Weil-number protorus, the Artin-Tate quotient and the mu_2 factor, the rational Frobenius, real and p-adic fibre functors, gerbes (cote 15, scans 2-14)",
     "(notes) FF01-FF22 and R01, R02, R05, R08, R09 of MPL_12_150-168+15_002-033"),
    ("deuring", "Deuring's gerbes and norm categories: rank-one objects over maximal orders, Azumaya algebras and the reduced norm, the definite quaternion and supersingular cases, Kummer and square classes (cote 15, scans 16-32)",
     "(notes) D01-D30 and R10 of MPL_12_150-168+15_002-033; D09 records a revision withdrawn in the same text; D30 a self-flagged independence margin"),
    ("tannakian", "tensor categories and the tannakian formalism (cote 10, B series): the plan 'Generalites sur les operations (x) sur une categorie' with an appendix on coalgebras, comodules and bialgebras, examples of tensor categories, a tannakian category over k with diagonalizable band",
     "(notes) Codex sheet notes B10-04 to B10-10; the plan on scan 115"),
    ("hodge_mumford", "the Hodge group, the letter to Mumford (Algiers, 1 November 1965) and transcendental descriptions of motives in characteristic 0 by double lattices (cote 13)",
     "(notes) H13-01: 'I have become aware that I have been a bit rash with the conjectures'; J13-01: 'Groupe de Hodge', 'Lettre a Mumford'; J13-02: 'Descriptions transcendantes de motifs en car 0 ... doubles reseaux'; J13-03: 'si on admet la conjecture de Hodge'"),
]
FOLDER = {"K11-01": "SA05-1", "K11-02": "SA05-1", "K11-03": "SA05-1", "K11-04": "SA05-1",
          "K12-01": "SA05-8", "K12-02": "SA05-8", "K12-03": "SA05-9", "K12-07": "SA05-9", "K12-08": "SA05-9",
          "K12-04": "SA05-10", "K12-05": "SA05-10", "K12-06": "SA05-11", "K12-09": "SA05-12",
          "K14-01": "SA05-12", "K14-07": "SA05-1", "K15-03": "SA05-17", "K15-04": "SA05-17", "K15-09": "SA05-10", "K15-10": "SA05-17",
          "K16-01": "SA05-16", "K16-03": "SA05-16", "K16-04": "SA05-11", "K18-01": "SA05-17", "K18-02": "SA05-4", "K18-03": "SA05-10",
          "K18-04": "SA05-17", "B10-01": "SA05-4", "B10-02": "SA05-4", "B10-03": "SA05-4",
          "B10-04": "tannakian", "B10-05": "tannakian", "B10-06": "tannakian", "B10-07": "tannakian", "B10-08": "tannakian",
          "B10-09": "tannakian", "B10-10": "tannakian",
          "H13-01": "hodge_mumford", "J13-01": "hodge_mumford", "J13-02": "hodge_mumford", "J13-03": "hodge_mumford",
          "J13-04": "hodge_mumford", "J13-05": "hodge_mumford"}
P = "MPL_12_150-168+15_002-033"
RULES = [
    (r"^Standard-conjecture dictionary", "SA05-2", P, "heading"),
    (r"^(S15:|Titles and internal|Visible manuscript)", "SA05-17", P, "heading"),
    (r"^M(09|10|30)\b", "SA05-9", P, "heading"),
    (r"^M(17|18|19|31)\b", "SA05-11", P, "heading"),
    (r"^M24\b", "SA05-2", P, "heading"),
    (r"^M2[5-8]\b", "SA05-8", P, "heading"),
    (r"^M\d\d\b", "SA05-12", P, "heading"),
    (r"^FF\d\d\b", "ff_motives", P, "heading"),
    (r"^D\d\d\b", "deuring", P, "heading"),
    (r"^R(01|02|05|08|09)\b", "ff_motives", P, "heading"),
    (r"^R10\b", "deuring", P, "heading"),
    (r"^R(11|12|13|14)\b", "SA05-17", P, "heading"),
    (r"^R07\b", "SA05-11", P, "heading"),
    (r"^R(03|04|06|15|16)\b", "SA05-12", P, "heading"),
]


def SCANS(e, t):
    if e["entry_id"].startswith("codex:"):
        s = re.findall(r"^\|\s*(\d{1,3})\b|\*\*Scan (\d{1,3})|^- Scan (\d{1,3})", t, re.M)
        return ",".join(sorted({str(int(x)) for g in s for x in g if x}, key=int))
    return ""


def FALLBACK(e, t):
    if e["entry_id"].startswith("MPL_15_139-194:records"):
        op = " ".join(t.split()[:12])
        if re.search(r"Title sheet|Cover/title|Reused typescript", op):
            return ("SA05-17", "opening-read (title sheet or reused typescript)")
        s = int(e["scans"].split(",")[0])
        return ("SA05-8" if s <= 168 else "SA05-10", "opening-read; section by scan (139-168 Serre group, CM, Hodge; 172-178 absolute cohomology of Z(n))")
    if e["entry_id"].startswith("codex:B12"):
        return ("SA05-17", "opening-read; subject not identified (EGA-style numbering 7.5.3)")
    return None


FORCE = {
    "MPL_11_043-058+56:records:research_leads#1": ("SA05-1", "opening-read", "not assessed", "one long record (2,290 words) over cote 11, scans 43-58; opens on a reused English typescript (scan 43). "),
    "codex:H13-01#1": ("hodge_mumford", "entry-read", "not assessed", "read (opening): the letter to Mumford, Algiers 1 Nov 1965, opens 'I have become aware that I have been a bit rash with the conjectures'. ", "a link across folders"),
}
FLAGS = [
    ("a link across folders", "codex:H13-01 (cote 13, scans 14-16) and codex:J13-01 to J13-05 (cote 13); new item on the Hodge group",
     "Cote 13 holds the letter to Mumford (Algiers, 1 Nov 1965, signed A Grothendieck, with a P.S.) that opens 'I have become aware that I have been a bit rash with the conjectures', with the cover 'Groupe de Hodge / Lettre a Mumford' and a text 'Descriptions transcendantes de motifs en car 0 ... doubles reseaux'. Which conjectures he withdraws is the first thing part 2 should read on the scans; it bears on SA06-4 (Tate classes, the letter to Serre) and on the period items SA06-2 and SA07-2.",
     "Codex notes H13-01#1-2, J13-01#2, J13-02#2, J13-03#1, openings read"),
    ("a link across folders", "MPL_12_150-168+15_002-033 FF01-FF22, D01-D30 (cote 15, scans 2-32); SA06-8, SA06-9, SA06-10",
     "The cote 15 half of this package is on motives over finite fields and Deuring's gerbes, the objects of SA06-8 (Deuring gerbes), SA06-9 (CM motives over finite fields) and SA06-10 (real fibre functors and Artin-Tate). Placed in SA05 as two new items and linked; the merge belongs to the global build.",
     "headings of #37-#88"),
    ("a link across folders", "codex:B10-04 to B10-10 (cote 10, scans 60-140); SA07-1, SA15-6",
     "Cote 10's B series holds a tannakian text (plan on scan 115: 'Chapitre 1. Generalites sur les operations (x) sur une categorie', an appendix on coalgebras, comodules and bigebras, 'Chapitre 2. Relations entre (x)-categories et ... foncteur fibre'; 'Quelques exemples de categories tensorielles', scan 102). SA07-1 (reconstruction from fibre functors) and SA15-6 (tannakian categories of crystals) are the same formalism.",
     "Codex title-sheet notes B10-04#2, B10-07#2, B10-08#2, read"),
]
OBJ = {"ff_motives": {"cross_topic": "= H046 (CM motives over finite fields; SA06-9); linked H03R (SA06-10)"}, "deuring": {"cross_topic": "= H045 (Deuring gerbes; SA06-8)"},
       "tannakian": {"cross_topic": "linked SA07-1 (H047), SA15-6 (H0AH)"}, "hodge_mumford": {"cross_topic": "linked SA06-4 (H041), SA06-2, SA07-2"}}
NOTES = """
What the gap list added to SA05:
- MPL_12_150-168+15_002-033 (104 Pro notes, new to the register): the headings say what each note is about and their prefixes give the clusters. M (cote 12, scans 150-167: the construction of the category of motives, effectivity, projectors, Kunneth, Tate inversion, the niveau decomposition, positivity, Nori-Ayoub and Andre) goes to SA05-12, with the niveau notes to SA05-9, the positivity notes to SA05-11, the lettering note to SA05-2 and the Nori-Ayoub-Andre notes to SA05-8. FF (cote 15, scans 2-14) and D (scans 16-32) are two new items, motives over finite fields and Deuring's gerbes. R notes follow their witness scans.
- The Work and Codex notes of the K folders follow the sweep-1 folder map, extended to the new folders by their 'What the pages do': K14-01 (structure of effectivity) and K12-09 to SA05-12; K14-07 (the graph of a homomorphism) to SA05-1; K15-09 and K18-03 (archimedean fibres, two conjugations) to SA05-10; K16-01 and K16-03 (grading by projectors, Hodge algebras, L and Lambda) to SA05-16; K16-04 (a letter to Coates on the index conjecture) to SA05-11; K18-02 (distributions and tangent maps) to SA05-4; the reused typescripts and papers K15-03 (reflexive modules, VI.5), K15-04 (maps of ringed spaces), K15-10 (invariant forms), K18-01 (papers and bibliography, Saavedra), K18-04 (valuations) to SA05-17.
- New Codex folders: B10-01 to B10-03 (sections 10-11 of a group-scheme text: projective limits, affine group preschemes) join SA05-4; B10-04 to B10-10 are a new tannakian item; H13-01 and J13 (the letter to Mumford, the Hodge group, double lattices) a new item. B12-01 and B12-02 (cote 12, 'Exemples 7.5.3', 'le plus important probleme reste ...') are placed by the scans they cite, else SA05-17; their subject is not identified from the openings.
- MPL_15_139-194 research leads (31, cote 15, scans 139-178; that package's notes are in no sweep-1 table): scans 139-168 (tori over Weilian fields, the connected group S_K^0 = T_K/R, CM structures and CM bimodules, the characters psi_Sigma, fibre functors to Hodge objects) join SA05-8; scans 172-178 ('Calculs de cohomologie absolue des Motifs de Tate Z(n)', with self-flagged '=0?' and '[est-on nul ??]') join SA05-10; the covers (157: 'Corps de classes commutatif = Motifs a groupe fondamental motivique connexe commutatif'; 172) and the reused typescript leaves n. 413 go to SA05-17.
- For part 2: codex:B10-02#1 records a circled handwritten 'fausse Formule' beside the canonical-map formula of Lemma 11.1 (cote 10, scan 43), on the group-scheme text.
"""
CHECKS = [("codex:H13-01#1", "2026-11-18", "the note's quotations checked against the page (cote 13, scans 14, 19, 20; images read in sweep 2 part 2)", "agree; the letter withdraws a conjecture (see REPORTS/mumford_letter_cote13.md)", "sweep2/REPORTS/mumford_letter_cote13.md")]
