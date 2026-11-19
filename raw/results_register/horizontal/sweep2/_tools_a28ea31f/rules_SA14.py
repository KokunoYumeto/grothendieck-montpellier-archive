# SA14 (Picard), sweep 2 part 1. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
import re
DOCS = "SA14-13"
NEW = [
    ("kummer", "the Kummer class and transgression for the Picard of a curve: finite Kummer classes, one and two punctures, vanishing statements, the semiabelian bridge, three obstruction constructions (cote 57, scans 141-147, 'Curve Picard')",
     "(notes) P05-P11 of MPL_57_133-179: a possible proof of the Kummer comparison, passage from finite Kummer classes, the last vanishing statement left unproved"),
    ("pseudo", "pseudomorphisms (cote 57, scans 166-171): separatedness, the quasi-coherence proposition (withdrawn), codimension-one regularity, normality relaxations, minimal primes, a birational fundamental-group statement",
     "(notes) N01-N06 and the heading T03 of MPL_57_133-179"),
]
FOLDER = {"K57-01": "SA14-9", "K57-02": "SA14-9", "K57-03": "SA14-4", "K57-04": "SA14-4", "K57-07": "SA14-4", "K57-08": "SA14-4",
          "K57-05": "SA14-2", "K57-06": "SA14-6", "K57-09": "SA14-8", "K57-10": "SA14-11", "K58-01": "SA14-11", "K58-02": "SA14-11",
          "K59-01": "SA14-14", "K59-02": "SA14-14", "A57-01": "SA14-6", "A57-02": "SA14-9"}
P = "MPL_57_133-179"
OVERLAP_SKIP = [P]
RULES = [
    (r"^Source key", "SA14-13", P, "heading"),
    (r"^(T\d\d|JAC08)\b", "SA14-13", P, "heading"),
    (r"^(FW\d\d|JAC0[1-7])\b", "SA14-1", P, "heading"),
    (r"^C0\d\b", "SA14-8", P, "heading"),
    (r"^(D0\d|Q0\d|P0[1-4])\b", "SA14-4", P, "heading"),
    (r"^(P0[5-9]|P1[01])\b", "kummer", P, "heading"),
    (r"^N0\d\b", "pseudo", P, "heading"),
    (r"^U0[1-4]\b|^U06\b|^U08\b", "SA14-11", P, "heading"),
    (r"^U05\b", "SA14-8", P, "heading"),
    (r"^U07\b", "SA14-5", P, "heading"),
]


def SCANS(e, t):
    if e["entry_id"].startswith(P):
        return ",".join(sorted(set(re.findall(r"\b57:(\d{3})", t)) | set(re.findall(r"P57\((\d{3})\)", t))))
    return ""


def FALLBACK(e, t):
    if not e["entry_id"].startswith(P):
        return None
    m = re.search(r"\b57:(\d{3})", t)
    if not m:
        return None
    s = int(m.group(1))
    it = ("SA14-4" if s <= 140 else "kummer" if s <= 146 else "SA14-8" if s <= 156 else "SA14-4" if s <= 164
          else "pseudo" if s <= 171 else "SA14-4")
    return (it, "heading + first cited scan (section of the text)")


FORCE = {
    "MPL_60_036-070:records:research_leads#1": ("SA14-13", "entry-read", "not assessed", "read in full: a preamble ('provisional ... context is unopened'), no mathematics. "),
    "codex:A57-01#1": ("SA14-6", "entry-read", "not assessed", "read (first 110 words): English text 'Local Picard schemes' (scans 3-13): group schemes P_n over k, an inverse system, the cokernel of (5), essential constancy. "),
    "codex:A57-02#1": ("SA14-9", "entry-read", "not assessed", "read (first 110 words): English letter(s): Raynaud extending his construction; an earlier proof valid only if the Pic functor of one factor is representable; 'I am convinced however that Corr is always separated'. ", "a link across folders"),
}
FLAGS = [
    ("a link across folders", "MPL_57_133-179#2-#8 (FW01-FW07) and #9-#16 (JAC01-JAC08) (cote 57, scans 133-179)",
     "Fifteen notes of the new Pro package read cote 57 against the programme's carry questions: FW against the missing Fourier verification of cote 47 (FW02: 'the current a verifier is a Kummer ...' at 57:144), JAC against the seven theorems of the cote 44 letter (Theorems 1-7 at 57:133-173). Placed under SA14-1 (carry questions). Whether the 'a verifier' of scan 144 is the Fourier check is the notes' reading, not the page's; a passage read of 57:144 L21-32 settles it.",
     "headings and openings of MPL_57_133-179 #2-#16"),
    ("a link across folders", "codex:A57-02#1 (cote 57, scans 20-22); SA14-9",
     "An English letter in cote 57 says Raynaud is extending his construction, that an earlier proof needed the Pic functor of one factor representable, and that 'Corr is always separated' (divisorial correspondences). Links SA14-9 (Picard functor of a product) to SA14-4 (existence and separation of Pic). The writer and addressee are not named in the note.",
     "Codex step note A57-02#1, read"),
]
OBJ = {"kummer": {"cross_topic": "SA14-14 (sections of torsors and their classes)"},
       "SA14-1": {"statement+": "(sweep 2) MPL_57_133-179 FW01-07 and JAC01-08 read cote 57 against the Fourier check and the seven theorems"}}
NOTES = """
What the gap list added to SA14:
- MPL_57_133-179 (95 Pro notes, cote 57, scans 133-179, new to the register): the notes are grouped by their own prefixes, and the headings say what each is about. T and JAC08 (titles, covers, chronology, the Benjamin letter) go to SA14-13; FW and JAC01-07 (read against the carry questions) to SA14-1; C (Picard of curves with several components) and U05 to SA14-8; D, Q and P01-P04 (Picard by divisors, the Picard functor, representability) to SA14-4; P05-P11 to a new item on the Kummer class for the Picard of a curve; N to a new item on pseudomorphisms; U01-U04, U06, U08 (commutative algebra) to SA14-11, U07 to SA14-5. The R and SF notes (reading questions, self-flags) go by the first scan they cite, to the section of the text that scan belongs to (133-140, 157-164, 172-179: SA14-4; 141-146: Kummer; 147-156: SA14-8; 165-171: pseudomorphisms).
- The Codex sheet notes on the K57-K59 folders follow the sweep-1 folder map; A57-01 ('Local Picard schemes', English) joins SA14-6, A57-02 (an English letter on Corr and Raynaud's construction) joins SA14-9.
"""
CHECKS = [("MPL_57_133-179#3", "2026-11-18", "the place of 'à vérifier' checked on the image (cote 57, scan 144)", "agrees: it qualifies xi_n = delta_n(eta), the Kummer-boundary comparison", "sweep2/REPORTS/cote57_scan144_a_verifier.md"),
          ("MPL_57_133-179#78", "2026-11-18", "the self-flagged step checked on the image (cote 57, scan 144)", "agrees", "sweep2/REPORTS/cote57_scan144_a_verifier.md"),
          ("MPL_57_133-179#2", "2026-11-18", "FW01's statement that these pages do not supply the cote 47 check, compared with 57:144", "agrees", "sweep2/REPORTS/cote57_scan144_a_verifier.md")]
