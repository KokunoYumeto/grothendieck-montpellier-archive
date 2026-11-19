# SA18 (Varietes abeliennes), sweep 2 part 1. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
import importlib.util, pathlib
_p = pathlib.Path(__file__).with_name("second_pass.py")
_s = importlib.util.spec_from_file_location("second_pass", _p); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
CHECKS_IMPORTED = _m.events("SA18")
DOCS = "SA18-19"
NEW = [
    ("grp_field", "schemes and group schemes over a field (cote 53, J series): connected and irreducible components, a geometric-irreducibility criterion and its 'rectificatif', finite etale schemes, representability of Hom(G, G_m), immersions of monoids, induced operations",
     "(notes) open on the sheets: base S or base k; 'Hom(G, G_m) representable ?'; 'u(G) stable par specialisation ?' answered in the margin 'Oui. Je prouve ...'; an English marginal 'I still see difficulty in accepting b)' on scan 17"),
]
FOLDER = {"K45-01": "SA18-1", "K45-02": "SA18-1", "K46-01_2": "SA18-6", "K46-03": "SA18-6", "K46-02": "SA18-10",
          "K49-01": "SA18-17", "K50-01": "SA18-17", "K51-01": "SA18-17", "K51-02": "SA18-17", "K52-01": "SA18-17",
          "K54-01": "SA18-14", "K55-01": "SA18-18", "K56-01": "SA18-16", "K56-02": "SA18-16", "K56-03": "SA18-2",
          "K47-01": "SA18-13", "C45-01": "SA18-3", "C46-01": "SA18-7", "H48-01": "SA18-2",
          "J53-01": "grp_field", "J53-02": "grp_field", "J53-03": "grp_field", "J53-04": "grp_field", "J53-05": "grp_field"}
FORCE = {
    "codex:C45-01#1": ("SA18-3", "entry-read", "not assessed", "read (first 95 words): scan 72, the lambda-structure and the filtration by powers of the augmentation ideal, qualified 'sans doute'; placed with the quadratic forms and Delzant (lambda-ring of quadratic forms). "),
    "codex:H48-01#1": ("SA18-2", "entry-read", "not assessed", "read (first 95 words): cote 48, cover, section plan 'sur un corps', compatibility check 'laissee au lecteur', 'theoreme de l'isotrivialite sur un corps'. "),
    "codex:J53-01#1": ("grp_field", "entry-read", "not assessed", "read (first 95 words). "),
    "codex:J53-03#1": ("grp_field", "entry-read", "not assessed", "read (first 95 words). "),
    "codex:J53-05#1": ("grp_field", "entry-read", "not assessed", "read in full. "),
    "work:K47-01#2": ("SA18-13", "entry-read", "not assessed", "read (first 140 words). "),
    "work:K47-01#3": ("SA18-13", "entry-read", "not assessed", "read in full. "),
    "work:K47-01#6": ("SA18-13", "entry-read", "not assessed", "read (first 140 words). ", "suspected misreading"),
}
FLAGS = [
    ("suspected misreading", "work:K47-01#6 (cote 47, scan 009); SA18-13",
     "The Work model remark M1 (high confidence): at chi = 3 the displayed power should have quadratic and cubic coefficients 1/3 and -1/27, while the written coefficients give 1 and -1/9, a factor chi. With M3 (proposed divisibility denominator k! chi^(k-2)), either the ink reads a different power of chi or the page has a slip. To decide on the scan; it bears on the 'formulas mod torsion' question Q2 ('Ces formules sont-elles bien vraies mod torsion ?').",
     "Work K47-01 #3 and #6, read"),
    ("a link across folders", "codex:J53-03#1 (cote 53, scans 16-17); SA18 new item on schemes and group schemes over a field",
     "Cote 53 asks 'Hom(G, G_m) representable ?' for group schemes over a field and leaves the base (S or k) open; this is Cartier duality for groups of multiplicative type, the object of SA19-2 (duality of group schemes). An English marginal ('I still see difficulty in accepting b)', scan 17) suggests a correspondent's or reader's hand on these sheets.",
     "Codex step notes J53-01#1, J53-03#1, read"),
    ("a link across folders", "codex:H48-01#1 (cote 48); SA18-2",
     "Cote 48 (new to the register) has a section plan 'sur un corps' and the 'theoreme de l'isotrivialite sur un corps'; placed under SA18-2 (tori and reductive groups). It may be the SGA 3 isotriviality of groups of multiplicative type; the notes do not say.",
     "Codex step note H48-01#1, read"),
]
OBJ = {"grp_field": {"cross_topic": "linked SA19-2 (duality of group schemes: Hom(G, G_m)); H0CB"}}
NOTES = """
What the gap list added to SA18:
- The Codex sheet notes on the K folders follow the sweep-1 Work folders; K47-01 (Work and Codex) goes to SA18-13, the Fourier transform of cote 47.
- New folders: C45-01 (cote 45, scan 72: lambda-structure and the augmentation filtration) joins SA18-3; C46-01 (definition of the Verschiebung) joins SA18-7; H48-01 (cote 48, isotriviality over a field) joins SA18-2; the J53 series (cote 53, five folders) is a new item on schemes and group schemes over a field.
- The second-pass verdicts on MPL_16+47+54+44 (Claude Opus 5.5 at effort max, 17 Nov; inputs/SA18/second_pass) are imported here as one check event per verdict on the R, S, F and D items that NOTES_INDEX lists (35 events, 33 entries). The same package is placed in SA07, SA18 and SA19; the events are written once, here. The first-pass notes 16:s:i that the second pass also checks are not NOTES_INDEX entries of these topics and have no entry id here.
"""
CHECKS = [("work:K47-01#6", "2026-11-18", "the expansion of (1 - x/chi)^chi recomputed (chi = 3) and the denominators read on the image (cote 47, scan 9, 220 dpi)", "agrees with the note: the page's coefficients of degree k >= 2 are chi times too large, a slip of his", "sweep2/REPORTS/cote47_scan009_chi_factor.md")]
