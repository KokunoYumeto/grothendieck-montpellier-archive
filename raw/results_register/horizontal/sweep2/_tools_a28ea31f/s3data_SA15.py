DEPENDS = [
    ("SA15-9", "uses", "SA15-1", "read", "4:3 (8.1.1: crystalline cohomology 'au sens des catégories dérivées', H_DR = H (x)^L_W k)", "was 'his page' in sweep 2"),
    ("SA15-9", "uses", "SA15-2", "read", "4:5-6 (8.4: semisimple parts for the p-linear Frobenius; 8.4.2 F_p-local systems)", "was 'his page' in sweep 2"),
    ("SA15-9", "uses", "SA06-6", "read", "4:4 (8.3: weak Lefschetz with torsion, 'Nous admettrons ... cohomologie cristalline')", "other topic"),
    ("SA15-16", "uses", "SA15-1", "read", "6:23 (1º: H^1_DR of a lifting depends only on A and S -> T: a crystal)", "was 'his page' in sweep 2"),
    ("SA15-16", "uses", "SA15-2", "read", "6:22-23 (the Frobenius DR(f)^(p) -> DR(f); F and V on DR^1, FV = VF = p)", "was 'his page' in sweep 2"),
    ("SA15-19", "uses", "SA15-16", "read", "100:48-50 (p-divisible groups over a trait; Tate's theorem used twice)", "was 'his page' in sweep 2"),
]
CORRECTIONS = [
    ("sweep2 SA15-9 status", "'his text, partly admitted; known in substance'", "refined: section 8 'Une estimation (heuristique) du nombre des valeurs propres de frobenius dans la cohomologie évanescente qui sont des unités p-adiques' (4:3-12, sheet 8.4.4 on 4:2): Lemma 8.4.3 proved on the page; 8.5 conditional on crystalline ingredients; 8.5.7 ('Je pense que v est injectif') true for every smooth ample Y (proved in sweep 3); 8.6 an open question of his", "read 4:2-12"),
    ("sweep2 SA15-16 status", "'his conjectures, some withdrawn on the page; known since'", "refined: 1º-3º (Dieudonné crystal, comparison with the classical module, liftings = liftings of the Hodge filtration) are true over nilpotent PD thickenings (Messing 1972; Mazur-Messing 1974; BBM 1982); 2.7 refutes them over arbitrary nilpotent thickenings (supersingular points), which is what 1º-3º state", "read 6:22-27"),
    ("sweep2 SA15-19 places", "'his pages: cote 100, scans ... 48-53'", "100:48-51 are a typescript ('Modèles de Néron et groupes p-divisibles'; 100:53 calls its theorem 'le th. de Raynaud'), with his margin '[ ] inutile'; 100:52-53 are his handwritten extension to every group with a Néron model", "read 100:48-53"),
]
CHECKS = [
    ("MPL_8_079-081+9+4+100 (4:6)", "re-derived Lemma 8.4.3: Frobenius on the de Rham complex kills Omega^(>=1), so F_DR = beta alpha and F_O = alpha beta (alpha the augmentation, beta induced by x -> x^p), and alpha is an isomorphism on semisimple parts", "agrees", "sweep3/SA15/STUDY.md §1"),
    ("MPL_8_079-081+9+4+100 (4:2)", "re-derived 8.4.4 a): for i > n, (H^i (x) k)_ss lies in (H^i_DR)_ss = H^i(X, O_X)_ss = 0, so F is nilpotent on H^i (x) k, on Tors^i (x) k and on pTors^i; hence (H^n (x) k)_ss = H^n(X, O_X)_ss", "agrees", "sweep3/SA15/STUDY.md §1"),
    ("MPL_8_079-081+9+4+100 (4:8)", "proved 8.5.7 ('Je pense que v est injectif') for every smooth ample Y, n >= 2: a semisimple x with v(x) = 0 is F^k of a semisimple x_k with v(x_k) = 0, which comes from H^(n-1)(X, O(-Y)), so x comes from H^(n-1)(X, O(-p^k Y)) = 0 for k large (Serre duality and vanishing)", "proved: his conjecture is true; his two special cases are included", "sweep3/SA15/STUDY.md §1"),
    ("MPL_8_079-081+9+4+100 (4:7)", "checked 8.5.4: for an F-crystal over a finite field, the rank of the semisimple part of F mod p equals the number of unit-root (slope 0) Frobenius eigenvalues", "agrees; standard (slope filtration)", "sweep3/SA15/STUDY.md §1"),
    ("MPL_5+6_001-037 (6:27)", "re-derived the counterexample 2.7: a stratification relative to k making Frobenius horizontal would carry F^2 = 0 from a point of Hasse invariant zero to its infinitesimal neighbourhoods, contradicting the modular family; the argument fails for PD stratifications (t^p is horizontal and vanishes only at 0)", "agrees", "sweep3/SA15/STUDY.md §2"),
    ("MPL_5+6_001-037 (6:22)", "checked the self-correction 'je m'étais canulé': V = p^i F^-1 preserves the lattice DR^i only given an isomorphism (not an isogeny) with the dual of DR^(2d-i) twisted; in general only a bi-isocrystal", "agrees", "sweep3/SA15/STUDY.md §2"),
    ("MPL_8_079-081+9+4+100 (100:52-53)", "checked his extension of the typed theorem to every G_K with a Néron model: factorization through a semi-abelian subgroup (centralizers stabilize; p^nu G for p = char K; no G_a when K is perfect), G_K has no G_a since it has a Néron model, then the Néron property and Raynaud's theorem", "agrees; justifies his margin '[ ] inutile' on 100:48", "sweep3/SA15/STUDY.md §3"),
]
READ = {
    ("MPL_8_079-081+9+4+100", "4"): ("read in full (4:2-12)", "section 8, unit roots in vanishing cohomology"),
    ("MPL_5+6_001-037", "6"): ("read in part (6:22-27)", "the Dieudonné crystal and 2.7; scans 1-21, 28-37 not read in sweep 3"),
    ("MPL_8_079-081+9+4+100", "100"): ("read in part (100:48-53)", "Néron models and p-divisible groups; scans 3-45 not read in sweep 3"),
}
READY = {
    ("MPL_8_079-081+9+4+100", "4"): "4:2-12 (section 8 and the sheet 8.4.4): ready for an edition once its open readings are compared with the Codex witness K4-01 (11 of the 12 pages)",
}
EXTRA_DELIV = [
    ("Codex folders K4-01, K8-01, K9-01, K9-02", "4, 8, 9", "see the folders' inventories", "", "", "", "Codex web transcription with Work math notes; second witness of MPL_8_079-081+9+4+100", "not read in sweep 3", "after the two witnesses are compared", "the rest of SA15 (cotes 5, 6, 7, 8, 100) has a single transcription"),
]
