# SA19 (Jacobiennes): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA19-6", "SA19-1", "SA19-5", "SA19-2", "SA19-7", "SA19-14", "SA19-13", "SA19-3", "SA19-11", "SA19-12", "SA19-20",
         "SA19-4", "SA19-8"]
STATUS = {
    "SA19-6": ("his notes; known", "Formal groups, Witt rings, power-series operations."),
    "SA19-1": ("his text; known", "Generalized Jacobians and geometric class field theory (Rosenlicht; Serre, Groupes algébriques et corps de classes, 1959)."),
    "SA19-5": ("his construction", "Local cohomology and local relative Jacobians attached to chains of primes; the K43-04 Codex return for scans 49-63 is unfinished."),
    "SA19-2": ("his text; known in substance", "Duality for commutative group schemes over local fields and over curves (Serre; Milne, Arithmetic Duality Theorems)."),
    "SA19-7": ("his sketches", "Classification and gluing for categories of curves (cote 43, scans 178-)."),
    "SA19-14": ("= SA18-14", "See SA18."),
    "SA19-13": ("= SA18-13", "See SA18 and REPORTS/cote47_scan009_chi_factor.md."),
    "SA19-3": ("the notes' reading", "Cote 47 and the seven theorems of cote 44 read against Oda."),
    "SA19-11": ("= SA18-11", "See SA18."),
    "SA19-12": ("= SA18-12", "See SA18."),
    "SA19-20": ("= SA18-20", "See SA18."),
    "SA19-4": ("reused typescripts", "Atiyah on Thom complexes, Stiefel manifolds; used as paper."),
    "SA19-8": ("documents", ""),
}
DEPENDS = [
    ("SA19-1", "SA19-6", "proof", "", "local symbols in characteristic p use Witt vectors"),
    ("SA19-5", "SA19-1", "proof", "", "local relative Jacobians generalize the generalized Jacobian of a modulus"),
    ("SA19-2", "SA19-1", "proof", "", "geometric class field theory as a duality"),
    ("SA19-2", "SA19-6", "proof", "", "Witt groups and formal groups in local duality in characteristic p"),
    ("SA19-13", "SA19-14", "his page", "47:3-4", "the Poincaré bundle"),
    ("SA19-11", "SA19-14", "proof", "", ""),
    ("SA19-3", "SA19-13", "our note", "", ""),
    ("SA19-3", "SA19-14", "our note", "", ""),
    ("SA19-20", "SA19-12", "his page", "cote 16, scans 25-29", ""),
]
ITEMLINKS = {
    "SA19-1": [("proved in a run (same statements)", "ANABELIAN_A1_SUCCESSOR:B.68 (generalized Jacobian J_m, J_m[n] exact and étale, the Abel map on abelianized pi_1; his_places cite cote 43, scans 113, 132-133)", "register", "the run proves the form it uses"),
               ("known", "Rosenlicht; Serre, Groupes algébriques et corps de classes (1959)", "literature", "")],
    "SA19-2": [("known", "Serre (local class field theory, proalgebraic groups); Milne, Arithmetic Duality Theorems", "literature", "")],
    "SA19-6": [("known", "Witt vectors; Dieudonné; Lazard", "literature", "")],
    "SA19-13": [("known since", "Mukai (1981)", "literature", "")],
    "SA19-12": [("open", "the standard conjectures", "literature", "")],
}
ENTRYLINKS = {}
CORRECTIONS = [
    ("codex:K43-04", "a Codex return listed as notes on scans 49-63", "it holds a status line only: first-pass files for 49-63, second readings for 49-56, audit and freeze remaining; those pages rest on the Pro notes", "entry read"),
]
INTRO = """
SA19 is cotes 43-44 (Jacobiennes): generalized Jacobians and class field theory, duality for commutative group schemes,
local cohomology and local Jacobians, formal groups (cote 43); the letter of cote 44 (via the shared package
MPL_16+47+54+44, items 11-14 and 20, the same objects as SA18's). The register's run ANABELIAN_A1_SUCCESSOR cites cote 43
for its generalized-Jacobian statement B.68.
"""
