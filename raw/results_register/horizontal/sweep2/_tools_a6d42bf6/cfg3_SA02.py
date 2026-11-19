# Sweep 2 part 2, SA02 (cotes 84, 90, 91): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
DATE = '2026-11-18'
TITLE = 'SA02: quadratic algebras, their products and the chi-split extensions (cotes 84, 90, 91)'
INTRO = '''
The topic holds three cotes:
- **Cote 84:** quadratic algebras over a ring, the product of two and of three of them, the relative trace and norm; extensions of invertible modules with a chi-trivialisation and their signs; and, on the backs of the leaves, the Récoltes et Semailles typescript.
- **Cote 90:** KG(X) over a Dedekind ring, and the EGA IV henselization typescript.
- **Cote 91, scans 2-18:** Hom functors by non-projective methods, around Greenberg-Néron; restricted enveloping algebras.

Heavy notes: the Pro packages MPL_84_*, MPL_90+91_002-018 (GPT-6 Astra, ChatGPT Pro mode). Light notes: Work and Codex K84-*, K90-01, K91-01.

The pieces of sweep 2 part 2 are in `sweep2/REPORTS/`: `cote84_scan120_lemma_hypothesis.md` and `cote84_chi_split_extension_signs.md`.
'''
ORDER = [
 ('Quadratic algebras and their products (cote 84)', ['SA02-1', 'SA02-2', 'SA02-3', 'SA02-14']),
 ('Extensions with a chi-trivialisation (cote 84)', ['SA02-4', 'SA02-9']),
 ('Group schemes over a Dedekind ring; henselization (cote 90)', ['SA02-10', 'SA02-11']),
 ('Representability; restricted Lie algebras (cotes 90-91)', ['SA02-12', 'SA02-16']),
 ('The requested LM bridge (a question the notes put to the pages)', ['SA02-5']),
 ('Documentary and apparatus', ['SA02-6', 'SA02-7', 'SA02-8', 'SA02-13']),
]
DEPS = [
 ('SA02-2', 'SA02-1', 'his page', '84/105-106: the trace map is the pushout map of A1*A2'),
 ('SA02-3', 'SA02-1', 'his page', '84/111-115: the triple product is built from the pairwise products'),
 ('SA02-3', 'SA02-2', 'his page', '84/112-115: the three relative traces and norms; N1 N2 N3 = x^2 N_A/k'),
 ('SA02-4', 'SA02-1', 'his page', '84/101 and 136: the pushout relations x1*u2 = pi1(x1) (x) u2, u1*u2 = chi u1 (x) u2; at chi = 2 the trace of a quadratic algebra'),
 ('SA02-9', 'SA02-4', 'our note', '84/146-154: multiplication without division of chi-trivialised rank-one modules (Pro notes MPL_84_146-193)'),
 ('SA02-11', 'EGA IV (18.5.10), (18.8.1), (18.8.5), (18.6.9), (17.5.7)', 'his page', '90/15-25: the typed EGA IV references (Work K90-02 Pointers)'),
 ('SA02-12', 'SA03-2', 'our note', 'cote 91: Hom, Isom and Aut representability continues in SA03 (scans 19-58)'),
]
RELATED = [
 ('SA02-4', 'SA01-36', 'a proof (ours)', 'K84-10, scans 146-160: the same chi-split extensions (= H01R), filed under SA01'),
 ('SA02-1', 'SA01-28', 'our note', 'quadratic algebras and their discriminants on cote 83 (= H01A)'),
 ('SA02-4', 'SA01-17', 'our note', 'lambda-split extensions and their product on cote 83 (= H00Z)'),
 ('SA02-6', 'SA01-37', 'a proof (ours)', 'the same Récoltes et Semailles typescript: pp. 475-478 in K84-10'),
 ('SA02-6', 'SA21-11', 'our note', 'the same typescript reused in cote 156 (pp. 936, 951-953, 1074-1088)'),
 ('SA02-10', 'SA01-38', 'our note', 'K90-02, filed under SA01 (= H01J)'),
 ('SA02-11', 'SA01-39', 'our note', 'K90-02 typescript with pencil criticisms (= H01K)'),
 ('SA02-5', 'SA01-2', 'our note', 'the requested LM bridges B12 and B5'),
]
R = 'REPORTS/cote84_chi_split_extension_signs.md'; RL = 'REPORTS/cote84_scan120_lemma_hypothesis.md'
CLAIMS = [
 ['SA02-C1', 'the norm of u1*u2, written with a doubtful "-|+" sign', '84/190', 'SA02-1', 'the identity u^2 + b1b2 u + b1^2 c2 + b2^2 c1 - 4c1c2 = 0 (sweep 1, Groebner remainder 0)', 'decides the sign: "-"', 'a proof (computation)', 'sweep1/SA02/CHECK_EVENTS.tsv'],
 ['SA02-C2', 'Lemme: a gamma-stable subscheme X of X_J with k -> Gamma(X_J, O_X_J) (~ k^J) injective equals X_J', '84/120', 'SA02-3', 'counterexample (Spec k/a)_J; corrected lemma (Gamma(X, O_X), X closed) proved by his own argument', 'refutes as written; refines', 'a proof (ours)', RL],
 ['SA02-C3', 'the étale case of the triple product: Spec(A) -> X1^X2^X3 constant; a = (1/4) T_A/k(a) for invariant a when 2 is invertible', '84/118-121', 'SA02-3', 'his proof on 119-121, which uses the lemma of 120 in its corrected form (the application is to a closed immersion with k -> A injective)', 'stated with his proof', 'his page', 'MPL_84_097-145 research leads #22-#25'],
 ['SA02-C4', 'after a change of splitting, pi_p\'(eta, zeta) = pi_p(eta, zeta) + U(eta)', '84/130', 'SA02-4', 'b\'1 (x) b\'2 = b1 (x) b2 + chi U, checked by hand', 'corrects: + chi U(eta)', 'a proof (computation)', R],
 ['SA02-C5', '"Je dis que U\'\' = U + U\'"', '84/132', 'SA02-4', 'computation under the plus convention, checked by hand; B11', 'proves under the plus convention', 'a proof (computation)', R],
 ['SA02-C6', '"2 - chi = 1" as the normalization of f1*f2 on L1 (x) L2', '84/140', 'SA02-4', 'with pi_i = chi on L_i the terms give lambda1 lambda2 (u1*u2) with no condition (checked; B19); his own correction on 152', 'refutes the condition; refines', 'a proof (computation)', R],
 ['SA02-C7', '(U1*U2)(x1*x2) = -chi U1(x1) (x) U2(x2), "signe étrange !"', '84/136', 'SA02-4', 'B13: the -id of the dual extension on 134; not reconciled with one convention', 'open (his own flag)', 'our note', 'MPL_84_097-145 B13, B15'],
]
CORR = [
 ['SA02-K1', 'SA02-1', '84/190', 'suspected misreading (scan not viewed)', 'norm of u1*u2 with "-|+"', '"-"', 'the product identity checked in sweep 1', 'computation'],
 ['SA02-K2', 'SA02-3', '84/120', 'his slip', 'b) k -> Gamma(X_J, O_X_J) (~ k^J) injective; "sous-schéma"', 'k -> Gamma(X, O_X) injective; "sous-schéma fermé"', 'ink read on the scan (300 dpi); counterexample; his proof', 'scan image and proof'],
 ['SA02-K3', 'SA02-4', '84/130', 'his slip', 'last line pi_p\' = pi_p + U(eta)', 'pi_p\' = pi_p + chi U(eta)', 'ink read on the scan (220 dpi); computation', 'scan image and computation'],
 ['SA02-K4', 'SA02-4', '84/132', 'his slip (two conventions on one sheet)', '(b1 - chi U1) (x) (b2 - chi U2) = b1 (x) b2 + chi U; b\'\'_i = b\'_i - chi U\'_i', 'the plus convention throughout: b\'_i = b_i + chi U_i', 'ink read on the scan; computation', 'scan image and computation'],
 ['SA02-K5', 'SA02-4', '84/140', 'his slip, corrected by him on 152', '2 - chi = 1', 'no condition on chi', 'ink read on the scan; computation; his 152', 'scan image and computation'],
 ['SA02-K6', 'SA02-6', 'MPL_84_097-145 research leads #6, #32, #46', 'note corrected (the run\'s second audit, #49)', '102 "supprimant"; the marker on 129; typed pages 474-479 absent', '102 "supposant"; marker 106 then 1; typed 474 present, 475-478 in K84-10', 'research lead #49, from the scans', 'second audit of the Pro run'],
 ['SA02-K7', 'SA02-12', 'cote 91', 'placement', 'cote 91 split between SA02 (scans 2-18) and SA03 (19-143)', 'one subject (Hom functors, Greenberg-Néron): merge SA02-12 with SA03-2 and SA03-9', 'sweep 1', 'placement'],
]
B = 'MPL_84_097-145#'
CHECKS3 = [
 ['MPL_84_097-145:records:research_leads#24', 'reading checked on the scan image (84.pdf p. 120, 300 dpi)', 'agrees: the ink reads X_J in b) (roman X, as in "de X_J"), with "(~ k^J)"', '84.pdf page 120'],
 ['MPL_84_097-145:records:research_leads#24', 'his lemma as written tested on a counterexample', 'refuted as written: X = (Spec k/a)_J is closed, stable, satisfies b) and is not X_J', RL],
 ['MPL_84_097-145:records:research_leads#24', 'corrected lemma proved (his argument, completed)', 'proved: with k -> Gamma(X, O_X) injective and X closed, X = X_J', RL],
 [B + '50', 'reading checked on the scan image (84.pdf p. 130, 220 dpi)', 'agrees with the frozen reading: + U(eta) without chi', '84.pdf page 130'],
 [B + '51', 'reading checked on the scan image (84.pdf p. 132, 220 dpi)', 'agrees: both conventions in the ink; plus is the last word', '84.pdf page 132'],
 [B + '56', 'reading checked on the scan image (84.pdf p. 136, 220 dpi)', 'agrees: -chi with "signe étrange !"; u1*u2 = chi u1 (x) u2', '84.pdf page 136'],
 [B + '60', 'reading checked on the scan image (84.pdf p. 140, 220 dpi)', 'agrees: "(2 - chi)" partly struck and the live "2 - chi = 1"', '84.pdf page 140'],
 [B + '50', 'claim checked by computation (by hand)', 'agrees with B09: b\'1 (x) b\'2 = b1 (x) b2 + chi U, so 130 needs chi U(eta)', R],
 [B + '52', 'claim checked by computation (by hand)', 'agrees with B11: U\'\' = U + U\' under the plus convention; mixing leaves -2 chi (U1 (x) U\'2 + U\'1 (x) U2)', R],
 [B + '60', 'claim checked by computation (by hand)', 'agrees with B19: pi_i = chi on L_i gives lambda1 lambda2 (u1*u2), no condition on chi', R],
]
