# SA06 (Théorie des motifs II): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA06-3", "SA06-7", "SA06-5", "SA06-6", "SA06-4", "SA06-2", "SA06-15", "SA06-10", "SA06-9", "SA06-8", "SA06-16",
         "SA06-1", "SA06-14", "SA06-12", "SA06-17", "SA06-11", "SA06-13"]
STATUS = {
    "SA06-3": ("his text; known", "Algebraic and Albanese equivalence of cycles (Weil; Samuel; Murre)."),
    "SA06-7": ("his claims; known in part", "Boundedness of families of cycles, zero-cycles and the Albanese (Mumford 1969; Bloch-Srinivas 1983)."),
    "SA06-5": ("his text; known", "Ampleness: the Nakai-Mumford criterion (Kleiman 1966)."),
    "SA06-6": ("his claims; known in part", "Lefschetz theorems and programmes; hard Lefschetz (Deligne, Weil II, 1980)."),
    "SA06-4": ("conjectures, open", "Tate classes and the letter to Serre; the Tate conjecture is open, known for divisors on abelian varieties over finite fields (Tate 1966) and number fields (Faltings 1983)."),
    "SA06-2": ("his claims; known in part", "Effectivity and the motivic group, cocharacters, sl2, Nori-Ayoub, periods."),
    "SA06-15": ("his claims; known in part", "Fibre functors in characteristic p: crystalline and de Rham-Hodge realizations."),
    "SA06-10": ("his claims; known", "Real fibre functors, polarizations and gerbes; the Artin-Tate quotient (Deligne-Milne 1982)."),
    "SA06-9": ("his claims; known conditionally", "CM motives over finite fields, = H046 (Milne 1994; Tate 1966 for abelian varieties)."),
    "SA06-8": ("his text; known in substance", "Deuring gerbes and Brandt categories, = H045 (Deuring 1941); 'Catégories de Deuring' (B15-01)."),
    "SA06-16": ("his notes; known", "Étale cohomology of curves over finite fields (Weil; SGA 4 1/2)."),
    "SA06-1": ("his question; known in parts", "Linear against nonlinear: Tate Hom against anabelian Hom (Faltings 1983; Mochizuki 1999)."),
    "SA06-14": ("his agenda", "Scan 170: odd-weight motives, Weil-type abelian varieties, positivity, class fields."),
    "SA06-12": ("the notes' answers", "Planning questions."),
    "SA06-17": ("credited comparison", "Michel Hua's findings for cotes 14-15."),
    "SA06-11": ("reused leaves", "Typed and printed leaves (analytic typescripts on ODE and implicit functions, printed pp. 16-30)."),
    "SA06-13": ("documents", ""),
}
DEPENDS = [
    ("SA06-7", "SA06-3", "proof", "", "zero-cycles and the Albanese"),
    ("SA06-6", "SA06-5", "proof", "", "Lefschetz theorems through ample hyperplane sections"),
    ("SA06-4", "SA06-3", "proof", "", "Tate classes against algebraic cycles"),
    ("SA06-2", "SA06-4", "our note", "", "Tate effectivity"),
    ("SA06-15", "SA06-2", "proof", "", "fibre functors on effective motives"),
    ("SA06-10", "SA06-2", "proof", "", "effectivity from a cocharacter"),
    ("SA06-9", "SA06-4", "proof", "", "the Tate conjecture over finite fields"),
    ("SA06-9", "SA06-16", "proof", "", "Frobenius on H^1 of curves"),
    ("SA06-8", "SA06-9", "proof", "", "the supersingular part"),
    ("SA06-1", "SA06-4", "our note", "", "Tate Hom against anabelian Hom"),
    ("SA06-14", "SA06-9", "his page", "scan 170 agenda", ""),
    ("SA06-14", "SA06-2", "his page", "scan 170 agenda", ""),
]
ITEMLINKS = {
    "SA06-3": [("known", "Weil; Samuel; Murre", "literature", "")],
    "SA06-7": [("known in part", "Mumford (1969); Bloch-Srinivas (1983)", "literature", "")],
    "SA06-5": [("known", "Nakai; Kleiman (1966)", "literature", "")],
    "SA06-6": [("known in part", "Deligne, Weil II (1980), hard Lefschetz", "literature", "")],
    "SA06-4": [("open", "the Tate conjecture; Tate (1966), Faltings (1983) for abelian varieties", "literature", "")],
    "SA06-10": [("known", "Deligne-Milne (1982)", "literature", "")],
    "SA06-9": [("known conditionally", "Milne (1994); Tate (1966)", "literature", "")],
    "SA06-8": [("known in substance", "Deuring (1941)", "literature", "")],
    "SA06-16": [("known", "Weil; SGA 4 1/2", "literature", "")],
    "SA06-1": [("known in parts", "Faltings (1983); Mochizuki (1999)", "literature", "")],
}
ENTRYLINKS = {}
CORRECTIONS = [
    ("SA06-8, SA06-9, SA06-10", "the same objects also placed in SA05 (SA05-19 = H045, SA05-18 = H046) from the cote 15 half of MPL_12_150-168+15_002-033", "merge in the global build", "item comparison"),
]
INTRO = """
SA06 is cotes 14-15 (Théorie des motifs II): algebraic and Albanese equivalence, boundedness and zero-cycles, ampleness,
Lefschetz theorems, Tate classes and the letter to Serre, effectivity and fibre functors, real fibre functors and the
Artin-Tate quotient, CM motives over finite fields and Deuring gerbes (with the research leads of MPL_15_034-086), étale
cohomology of curves over finite fields.
"""
