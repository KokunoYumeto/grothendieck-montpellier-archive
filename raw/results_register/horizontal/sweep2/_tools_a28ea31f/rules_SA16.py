# SA16 (Courbes elliptiques), sweep 2 part 1. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
DOCS = "SA16-17"
NEW = [
    ("atkin", "congruences for the coefficients of modular forms and congruence Hecke operators (A.O.L. Atkin's typescripts kept in cote 63)",
     "(notes) Atkin, 'Congruences for modular forms' (pencil date 1968) and 'Congruence Hecke operators': congruences found partly by computation (powers of 19; q = 17, 19, 23); the author's own reservations"),
    ("mw_reduction", "Mordell-Weil, minimal models and reduction of elliptic curves (English typescript in cote 63, contents on scan 3)",
     "(notes) Theorem 4.1 with the finite-index assertion left to the reduction-to-minimal-form algorithm; the node and the cusp; the estimate nu <= ord(Delta) - 3 qualified 'if I'm not mistaken'"),
    ("cm_table", "elliptic curves with complex multiplication over Q: the class-number-one discriminants, their j values and conductors (French typescript, cote 63, scans 78-85)",
     "(notes) footnote: the integrality of the Frobenius eigenvalues on H^i(X, Z_l) and |alpha| = q^(i/2) not yet proved; after 163 'plus peut-etre une autre valeur d?'"),
]
FOLDER = {"K62-01": "SA16-12", "K62-02": "SA16-12", "K62-03": "SA16-12", "K63-02": "SA16-12", "K63-01": "SA16-2",
          "H63-01": "mw_reduction", "H63-02": "mw_reduction", "H63-03": "SA16-2", "H63-04": "SA16-2",
          "H63-05": "atkin", "H63-06": "atkin", "H63-07": "atkin", "H63-08": "cm_table", "H63-09": "SA16-2"}
RULES = [
    (r"Title sheet", "SA16-17", ":records:"),
    (r"(reused typ|typescript|typed).{0,200}(valuation|ordered-group|n°272)|(valuation|ordered-group).{0,200}(reused typ|typescript)", "SA16-7", ":records:"),
    (r"reused typ|typescript|typed sheet|typed page|typedproof|typed proof", "SA16-6", ":records:"),
]
FORCE = {
    "codex:H63-01#1": ("mw_reduction", "entry-read", "not assessed", "read in full; the text is another author's typescript in English. "),
    "codex:H63-02#1": ("mw_reduction", "entry-read", "not assessed", "read in full. "),
    "codex:H63-04#1": ("SA16-2", "entry-read", "not assessed", "read (first 150 words); the Formulaire's sections 6-7: automorphisms (order 24), curves without additive fibres, modular forms in characteristic 2 and 3 (a1, b2). ", "a link across folders"),
    "codex:H63-08#1": ("cm_table", "entry-read", "not assessed", "read in full; dating evidence, see TOPIC_NOTES. "),
}
FLAGS = [
    ("a link across folders", "codex:H63-03#2 (cote 63, scan 16) and codex:H63-09#2 (cote 63, scans 87-93)",
     "Cote 63 holds two versions of the Weierstrass formulary: 'COURBES ELLIPTIQUES : FORMULAIRE, d'apres J. Tate, mis au gout du jour par P. Deligne' (scan 16 on) and 'COURBES ELLIPTIQUES - FORMULAIRE (Traduction libre d'un manuscrit inedit de TATE)' (scan 87 on). Both are placed under SA16-2 with his own discriminant and j calculations of cote 62; a reader of SA16-2 should compare his normalization (1 - j/1728) with the Formulaire's.",
     "Codex title-sheet notes H63-03#2, H63-09#2 (headings and opening read)"),
    ("a link across folders", "codex:H63-04#1 (cote 63, scans 30-33)",
     "Handwritten margins on the typed Formulaire: 'faux si S pas connexe' beside Proposition 6.9 (I) (only automorphisms), 'structure ?' at the order 24, 'pourquoi ?' at 'se limiter aux courbes sans fibres additives', and 'Reste a prouver' before Proposition 7.2. Whose hand it is is not settled by the notes; if it is his, these are his objections to the Deligne text. Worth a passage read in part 2.",
     "Codex step note H63-04#1, read"),
]
CHECKS = [("codex:H63-04#1", "2026-11-18", "the margins read on the page (cote 63, scans 30 and 32, at 110 and 250 dpi); the hand compared with cote 13 scan 14 and cote 62", "agree with the note's readings; 'Reste à prouver' is typed, not a margin; the hand is probably his", "sweep2/REPORTS/hands_formulaire_and_tate.md")]
OBJ = {
    "atkin": {"cross_topic": "none found among my topics; a link across folders to any modular-forms congruence item elsewhere"},
    "cm_table": {"cross_topic": "SA16-19 (exceptional j)"},
    "SA16-2": {"statement+": "(sweep 2) cote 63 also holds the Tate-Deligne Formulaire in two versions (H63-03/04, H63-09)"},
}
NOTES = """
What the gap list added to SA16:
- The 42 research leads of MPL_62_002-050 restate the Pro notes scan by scan; they are placed with the sweep-1 item of the same scan (scan-overlap), the title sheet under SA16-17, and the reused typescripts under SA16-6 (completion, filtered modules) or SA16-7 (valuations, n. 272).
- The Codex sheet notes on K62/K63 follow the sweep-1 Work folders (SA16-12, SA16-2).
- The H63 series is new: other authors' typescripts kept in cote 63. Three new items: Atkin's congruence typescripts, an English typescript on Mordell-Weil and minimal models, a French typescript with the CM table. The Tate-Deligne Formulaire (two versions) joins SA16-2.
- Dating evidence (mine, from the notes, not checked on the scans): the CM typescript (H63-08, scans 78-81) says the integrality of the Frobenius eigenvalues on H^i(X, Z_l) and |alpha| = q^(i/2) are not proved, and lists the class-number-one discriminants with "plus peut-etre une autre valeur" after 163, so it was written before Stark and Baker (1966-67).
- The K62-02 Codex note finds no self-marked step; nothing beyond SA16-12.
- Which typescript is by whom rests on the title sheets the Codex notes transcribe; the Mordell-Weil typescript has no title in the notes.
"""
