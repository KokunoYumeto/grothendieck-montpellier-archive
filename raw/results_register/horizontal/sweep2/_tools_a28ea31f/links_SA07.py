# SA07 (Théorie des motifs III): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA07-18", "SA07-16", "SA07-15", "SA07-3", "SA07-6", "SA07-17", "SA07-7", "SA07-1", "SA07-2", "SA07-4", "SA07-10",
         "SA07-14", "SA07-13", "SA07-11", "SA07-12", "SA07-20", "SA07-19", "SA07-5", "SA07-9"]
STATUS = {
    "SA07-18": ("his text; known", "Homological formalism: relative exactness, derived functors, extraordinary inverse images (cote 19)."),
    "SA07-16": ("his text; known", "Operations on representation rings (cote 10)."),
    "SA07-15": ("his text; known", "Polarizations and Weil forms (cote 10; Weil 1958)."),
    "SA07-3": ("his construction; known as definitions", "The motivic category and its groups, correspondence rings, Lefschetz and Tate gradings, the A-D lettering."),
    "SA07-6": ("his text; known", "Cycle classes, orientations and comparison maps."),
    "SA07-17": ("his claims", "Lefschetz elements and their converse, local Picard groups and the Brauer group (cote 16)."),
    "SA07-7": ("his text; known", "Real structures and Hodge theory of motives."),
    "SA07-1": ("his programme", "Reconstruction of varieties and places from their motivic realizations."),
    "SA07-2": ("his conjecture, open", "Periods: the period torsor and his 'conjecture de transcendance N° 1'; open, known in special cases (Chudnovsky 1976 for CM elliptic curves)."),
    "SA07-4": ("his question; known in parts", "Linear against nonlinear comparisons (= SA05-14, SA06-1)."),
    "SA07-10": ("his self-flagged steps", "Steps he marks as unverified, withdrawn or to check on cote 18."),
    "SA07-14": ("= SA18-14", "See SA18."),
    "SA07-13": ("= SA18-13", "See SA18 and REPORTS/cote47_scan009_chi_factor.md."),
    "SA07-11": ("= SA18-11", "See SA18."),
    "SA07-12": ("= SA18-12", "See SA18."),
    "SA07-20": ("= SA18-20", "See SA18."),
    "SA07-19": ("the notes' answers", "Planning questions."),
    "SA07-5": ("reused typescripts", "Lie theory, Cartan subalgebras, root systems (cote 15, 195-228; cote 18)."),
    "SA07-9": ("documents", "Covers, pagination, letterhead; the chatB apparatus."),
}
DEPENDS = [
    ("SA07-3", "SA07-15", "proof", "", "polarizations give semisimplicity"),
    ("SA07-3", "SA07-16", "proof", "", "lambda-operations on the motivic category"),
    ("SA07-6", "SA07-3", "proof", "", "cycle classes as morphisms of motives"),
    ("SA07-7", "SA07-3", "proof", "", "real structures on realizations"),
    ("SA07-1", "SA07-3", "proof", "", "fibre functors on the motivic category"),
    ("SA07-2", "SA07-1", "proof", "", "the period torsor is Isom between the Betti and de Rham fibre functors"),
    ("SA07-2", "SA07-7", "proof", "", "complex conjugation and real periods"),
    ("SA07-4", "SA07-1", "our note", "", ""),
    ("SA07-10", "SA07-2", "his page", "cote 18", "the steps he marks are on the period pages"),
    ("SA07-17", "SA07-12", "proof", "", "Lefschetz elements of the cote 16 programme"),
    ("SA07-13", "SA07-14", "his page", "47:3-4", ""),
    ("SA07-11", "SA07-14", "proof", "", ""),
    ("SA07-20", "SA07-12", "his page", "cote 16, scans 25-29", ""),
    ("SA07-6", "SA07-18", "proof", "", "Gysin maps and extraordinary inverse images"),
]
ITEMLINKS = {
    "SA07-2": [("open", "Grothendieck's period conjecture; special cases: Chudnovsky (1976), CM elliptic curves", "literature", "")],
    "SA07-15": [("known", "Weil (1958), Variétés kählériennes", "literature", "")],
    "SA07-18": [("known", "SGA 4; Hartshorne, Residues and Duality (1966)", "literature", "")],
    "SA07-6": [("known", "cycle class maps (SGA 4 1/2, Cycle)", "literature", "")],
    "SA07-12": [("open", "the standard conjectures", "literature", "")],
    "SA07-13": [("known since", "Mukai (1981)", "literature", "")],
    "SA07-4": [("known in parts", "Faltings (1983); Mochizuki (1999)", "literature", "")],
}
ENTRYLINKS = {}
CORRECTIONS = []
INTRO = """
SA07 is cotes 10, 16, 18, 19 and part of 15 (Théorie des motifs III): polarizations and representation rings (cote 10),
the motivic category and its realizations, cycle classes, real structures, reconstruction from fibre functors, periods
and his 'conjecture de transcendance N° 1' (cote 18), homological formalism (cote 19), reused Lie typescripts (cote 15).
The second chat MPL_15_195-228+18_002-017_chatB is placed as a parallel witness of the main chat.
"""
