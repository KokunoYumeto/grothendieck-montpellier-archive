# SA02: quadratic algebras, their products and the chi-split extensions (cotes 84, 90, 91): what is where

Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 2026-11-18.

The topic holds three cotes:
- **Cote 84:** quadratic algebras over a ring, the product of two and of three of them, the relative trace and norm; extensions of invertible modules with a chi-trivialisation and their signs; and, on the backs of the leaves, the Récoltes et Semailles typescript.
- **Cote 90:** KG(X) over a Dedekind ring, and the EGA IV henselization typescript.
- **Cote 91, scans 2-18:** Hom functors by non-projective methods, around Greenberg-Néron; restricted enveloping algebras.

Heavy notes: the Pro packages MPL_84_*, MPL_90+91_002-018 (GPT-6 Astra, ChatGPT Pro mode). Light notes: Work and Codex K84-*, K90-01, K91-01.

The pieces of sweep 2 part 2 are in `sweep2/REPORTS/`: `cote84_scan120_lemma_hypothesis.md` and `cote84_chi_split_extension_signs.md`.

How to read an entry:
- **Where:** cote and scans, the notes it is in (package or folder), and the notes files. Scans are the PDF pages of the cote in `grothendieck_archive_montpellier`.
- **Depends:** what the item uses and what uses it, with the basis: his page, our note, or a proof (ours).
- **Claims:** his claims on the item, linked to what proves, refutes or refines them (CLAIM_LINKS.tsv).
- **Units:** the companion units that discuss it (UNIT_LINKS.tsv).
- **Flags, corrections:** from FLAGS.tsv and CORRECTIONS.tsv.

## Quadratic algebras and their products (cote 84)

### SA02-1: the product of two quadratic algebras: u = 2u_1u_2 + b_2u_1 + b_1u_2, the rank-four tensor product and its quadratic subalgebra

- **Status on his pages:** stated and calculated; identity correct (checked). **Kind:** construction/identity.
- **Where:** cote 84, scans 19,51,97-102,104,106,117,146,160,170,172,174,176,178-182,184,186,188,190,192,198.
- **Notes (81 entries):** MPL_84_146-193 (44); MPL_84_097-145 (7); work:K84-02 (6); work:K84-04 (6); work:K84-12 (6); MPL_84_097-145:records:research_leads (6); codex:K84-02 (2); codex:K84-04 (2) ....
- **Notes files:** `codex_web_20261113/returns/K84-02/out/K84-02_mathnotes.md`; `codex_web_20261113/returns/K84-02/out/K84-02_notes.md`; `codex_web_20261113/returns/K84-04/out/K84-04_mathnotes.md`; `codex_web_20261113/returns/K84-04/out/K84-04_notes.md`; `codex_web_20261113/returns/K84-12/out/K84-12_mathnotes.md`; `codex_web_20261113/returns/K84-12/out/K84-12_notes.md` ....
- **Depends:** related: SA01-28 (our note); used by: SA02-2 (his page), SA02-3 (his page), SA02-4 (his page).
- **Claims:**
  - SA02-C1 (84/190): "the norm of u1*u2, written with a doubtful "-|+" sign". **decides the sign: "-"**: the identity u^2 + b1b2 u + b1^2 c2 + b2^2 c1 - 4c1c2 = 0 (sweep 1, Groebner remainder 0).
- **Corrections:** 84/190: norm of u1*u2 with "-|+" -> "-".
- **Units (22):** K84-02.u01, K84-02.u02, K84-02.u03, K84-02.u04, K84-02.u05, K84-02.u06, K84-02.u07, K84-02.u08 ....
- **Flags:** suspected misreading (1); the same thing noted with different readings or statements (1); a link across folders (Pro 84a, 84b and Work K84-02, -04, -12).
- **Other topics:** SA01 (quadratic algebras K83-04..08; lambda-split extensions MPL_83 E01-E07; the trace identity with its -4cc'c'' term).

### SA02-2: relative trace and norm for quadratic algebras ("quasi-quadratic" algebras): definition, uniqueness, transitivity, base change, axioms

- **Status on his pages:** stated; several steps under faithfulness only. **Kind:** definition/proposition.
- **Where:** cote 84, scans 35,39,102-110,113-115,148,172,190,192.
- **Notes (41 entries):** MPL_84_097-145 (17); MPL_84_097-145:records:research_leads (8); work:K84-03 (6); work:K84-08 (6); codex:K84-03 (2); codex:K84-08 (2).
- **Notes files:** `codex_web_20261113/returns/K84-03/out/K84-03_mathnotes.md`; `codex_web_20261113/returns/K84-03/out/K84-03_notes.md`; `codex_web_20261113/returns/K84-08/out/K84-08_mathnotes.md`; `codex_web_20261113/returns/K84-08/out/K84-08_notes.md`; `inputs/SA02/pro/MPL_84_097-145_notes.md`; `returns/MPL_84_097-145_unzipped/.../research_leads.md`.
- **Depends:** used by: SA02-3 (his page); uses: SA02-1 (his page).
- **Units (13):** K84-03.u01, K84-03.u02, K84-03.u03, K84-03.u04, K84-03.u05, K84-03.u06, K84-03.u07, K84-03.u08 ....

### SA02-3: three quadratic algebras: the contracted triple product, the even subgroup of F_2^3, fixed ring vs scalar image, the étale case and the universal map

- **Status on his pages:** programme; partly proved, partly conjectured. **Kind:** construction/conjecture.
- **Where:** cote 84, scans 111-124,170,172,190,192.
- **Notes (29 entries):** MPL_84_097-145 (16); MPL_84_097-145:records:research_leads (13).
- **Notes files:** `inputs/SA02/pro/MPL_84_097-145_notes.md`; `returns/MPL_84_097-145_unzipped/.../research_leads.md`.
- **Depends:** uses: SA02-1 (his page), SA02-2 (his page).
- **Claims:**
  - SA02-C2 (84/120): "Lemme: a gamma-stable subscheme X of X_J with k -> Gamma(X_J, O_X_J) (~ k^J) injective equals X_J". **refutes as written; refines**: counterexample (Spec k/a)_J; corrected lemma (Gamma(X, O_X), X closed) proved by his own argument.
  - SA02-C3 (84/118-121): "the étale case of the triple product: Spec(A) -> X1^X2^X3 constant; a = (1/4) T_A/k(a) for invariant a when 2 is invertible". **stated with his proof**: his proof on 119-121, which uses the lemma of 120 in its corrected form (the application is to a closed immersion with k -> A injective).
- **Corrections:** 84/120: b) k -> Gamma(X_J, O_X_J) (~ k^J) injective; "sous-schéma" -> k -> Gamma(X, O_X) injective; "sous-schéma fermé".
- **Flags:** suspected misreading (1); suspected misreading at 84/120 (X_J).

### SA02-14: a product with two parities on monoids R_0, R_1 (cote 84, scan 2)

- **Status on his pages:** not checked. **Kind:** construction.
- **Where:** cote 84, scans 2.
- **Notes (8 entries):** work:K84-01 (6); codex:K84-01 (2).
- **Notes files:** `codex_web_20261113/returns/K84-01/out/K84-01_mathnotes.md`; `codex_web_20261113/returns/K84-01/out/K84-01_notes.md`.
- **Units (16):** K84-01.u01, K84-01.u02, K84-01.u03, K84-01.u04, K84-01.u05, K84-01.u06, K84-01.u07, K84-01.u08 ....

## Extensions with a chi-trivialisation (cote 84)

### SA02-4: extensions of invertible modules with a chi-trivialisation: the product of extensions, splitting changes, cocycles and the "strange signs" (= H01R)

- **Status on his pages:** worked over many sheets; conditional, with self-flagged questions. **Kind:** construction.
- **Where:** cote 84, scans 67-68,82,97-98,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174.
- **Notes (117 entries):** MPL_84_146-193 (39); MPL_84_097-145 (28); MPL_84_097-145:records:research_leads (10); work:K84-05 (6); work:K84-06 (6); work:K84-07 (6); work:K84-09 (6); work:K84-11 (6) ....
- **Notes files:** `codex_web_20261113/returns/K84-05/out/K84-05_mathnotes.md`; `codex_web_20261113/returns/K84-05/out/K84-05_notes.md`; `codex_web_20261113/returns/K84-06/out/K84-06_mathnotes.md`; `codex_web_20261113/returns/K84-06/out/K84-06_notes.md`; `codex_web_20261113/returns/K84-07/out/K84-07_mathnotes.md`; `codex_web_20261113/returns/K84-07/out/K84-07_notes.md` ....
- **Depends:** related: SA01-17 (our note), SA01-36 (a proof (ours)); used by: SA02-9 (our note); uses: SA02-1 (his page).
- **Claims:**
  - SA02-C4 (84/130): "after a change of splitting, pi_p'(eta, zeta) = pi_p(eta, zeta) + U(eta)". **corrects: + chi U(eta)**: b'1 (x) b'2 = b1 (x) b2 + chi U, checked by hand.
  - SA02-C5 (84/132): ""Je dis que U'' = U + U'"". **proves under the plus convention**: computation under the plus convention, checked by hand; B11.
  - SA02-C6 (84/140): ""2 - chi = 1" as the normalization of f1*f2 on L1 (x) L2". **refutes the condition; refines**: with pi_i = chi on L_i the terms give lambda1 lambda2 (u1*u2) with no condition (checked; B19); his own correction on 152.
  - SA02-C7 (84/136): "(U1*U2)(x1*x2) = -chi U1(x1) (x) U2(x2), "signe étrange !"". **open (his own flag)**: B13: the -id of the dual extension on 134; not reconciled with one convention.
- **Corrections:** 84/130: last line pi_p' = pi_p + U(eta) -> pi_p' = pi_p + chi U(eta); 84/132: (b1 - chi U1) (x) (b2 - chi U2) = b1 (x) b2 + chi U; b''_i = b'_i - chi U'_i -> the plus convention throughout: b'_i = b_i + chi U_i; 84/140: 2 - chi = 1 -> no condition on chi.
- **Units (22):** K84-05.u01, K84-05.u02, K84-05.u03, K84-05.u04, K84-05.u05, K84-05.u06, K84-05.u07, K84-05.u08 ....
- **Other topics:** SA01-17 (lambda-split extensions and the product *); K84-10 (SA01-36, = H01R).

### SA02-9: a local chi-groupoid of rank-one modules: multiplication without division, invertibility, automorphisms when chi has an annihilator

- **Status on his pages:** not on the pages (notes' proposal). **Kind:** notes' proposal.
- **Where:** cote 84, scans 146,154,164,170.
- **Notes (4 entries):** MPL_84_146-193 (4).
- **Notes files:** `inputs/SA02/pro/MPL_84_146-193_notes.md`.
- **Depends:** uses: SA02-4 (our note).

## Group schemes over a Dedekind ring; henselization (cote 90)

### SA02-10: KG(X) (cote 90): saturation over a Dedekind ring, the module criterion, finite dual algebras, projective covers, stable hulls

- **Status on his pages:** stated; proofs deferred or marked for rewriting. **Kind:** proposition.
- **Where:** cote 90, scans 2; cotes 90+91, scans 2,4,6,8,10,14,16,20,22,24.
- **Notes (24 entries):** MPL_90+91_002-018 (16); work:K90-01 (6); codex:K90-01 (2).
- **Notes files:** `codex_web_20261113/returns/K90-01/out/K90-01_mathnotes.md`; `codex_web_20261113/returns/K90-01/out/K90-01_notes.md`; `inputs/SA02/pro/MPL_90+91_002-018_notes.md`.
- **Depends:** related: SA01-38 (our note).

### SA02-11: henselization, ordinary and strict, on the reused leaves of cote 90

- **Status on his pages:** sketched; withdrawn parts. **Kind:** proposition.
- **Where:** cotes 90+91, scans 3,9,11,13,21,23.
- **Notes (6 entries):** MPL_90+91_002-018 (6).
- **Notes files:** `inputs/SA02/pro/MPL_90+91_002-018_notes.md`.
- **Depends:** related: SA01-39 (our note); uses: EGA IV (18.5.10), (18.8.1), (18.8.5), (18.6.9), (17.5.7) (his page).

## Representability; restricted Lie algebras (cotes 90-91)

### SA02-12: Hom functors by non-projective methods (cote 91, around Greenberg-Néron): the relative product, condition R, flattening, the relative unramified Hom theorem

- **Status on his pages:** stated; proofs incomplete. **Kind:** theorem (stated).
- **Where:** cotes 90+91, scans 5-14,16-18; cote 91, scans 2-3,19-20,34,47-48,59,73-74,87,99,114.
- **Notes (98 entries):** MPL_90+91_002-018 (26); work:K91-01 (6); work:K91-02 (6); work:K91-03 (6); work:K91-04 (6); work:K91-05 (6); work:K91-06 (6); work:K91-07 (6) ....
- **Notes files:** `codex_web_20261113/returns/K91-01/out/K91-01_mathnotes.md`; `codex_web_20261113/returns/K91-01/out/K91-01_notes.md`; `codex_web_20261113/returns/K91-02/out/K91-02_mathnotes.md`; `codex_web_20261113/returns/K91-02/out/K91-02_notes.md`; `codex_web_20261113/returns/K91-03/out/K91-03_mathnotes.md`; `codex_web_20261113/returns/K91-03/out/K91-03_notes.md` ....
- **Depends:** uses: SA03-2 (our note).
- **Corrections:** cote 91: cote 91 split between SA02 (scans 2-18) and SA03 (19-143) -> one subject (Hom functors, Greenberg-Néron): merge SA02-12 with SA03-2 and SA03-.
- **Other topics:** EGA/SGA material on Hom schemes (literature).

### SA02-16: restricted enveloping algebras (cote 91, scan 129)

- **Status on his pages:** not checked. **Kind:** proposition.
- **Where:** cote 91, scans 129.
- **Notes (8 entries):** work:K91-10 (6); codex:K91-10 (2).
- **Notes files:** `codex_web_20261113/returns/K91-10/out/K91-10_mathnotes.md`; `codex_web_20261113/returns/K91-10/out/K91-10_notes.md`.

## The requested LM bridge (a question the notes put to the pages)

### SA02-5: the requested LM bridge B12: quaternion algebras, twisted P^1 and PGL_2, the LM2 congruence questions

- **Status on his pages:** not on the pages. **Kind:** research question put to the pages.
- **Where:** cote 84, scans 97-98,100,104,110,116,119,146,154,160,170,172,192.
- **Notes (10 entries):** MPL_84_146-193 (6); MPL_84_097-145 (4).
- **Notes files:** `inputs/SA02/pro/MPL_84_097-145_notes.md`; `inputs/SA02/pro/MPL_84_146-193_notes.md`.
- **Depends:** related: SA01-2 (our note).
- **Flags:** LM/Derivateurs lens (2); LM/Derivateurs lens.
- **Other topics:** La Longue Marche (research register B12, LM2).

## Documentary and apparatus

### SA02-6: the reused autobiographical typescript on the backs of cote 84 (childhood, father, meditation from 1976, acceptance) (= H01T)

- **Status on his pages:** documentary. **Kind:** documentary (non-mathematical text).
- **Where:** cote 84, scans 125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163,165,167,169,171,179,191.
- **Notes (94 entries):** MPL_84_146-193 (56); MPL_84_097-145 (27); MPL_84_097-145:records:research_leads (11).
- **Notes files:** `inputs/SA02/pro/MPL_84_097-145_notes.md`; `inputs/SA02/pro/MPL_84_146-193_notes.md`; `returns/MPL_84_097-145_unzipped/.../research_leads.md`.
- **Depends:** related: SA01-37 (a proof (ours)), SA21-11 (our note).
- **Corrections:** MPL_84_097-145 research leads #6, #32, #46: 102 "supprimant"; the marker on 129; typed pages 474-479 absent -> 102 "supposant"; marker 106 then 1; typed 474 present, 475-478 in K84-10.
- **Flags:** the same thing noted with different readings or statements (1); a link across folders (2); a link across folders (pp. 475-478 in K84-10).
- **Other topics:** other reused typescripts: SA01-24 (cote 83); typed pp. 475-478 are in K84-10, scans 146-160 (SA01-37, = H01T).

### SA02-7: the yin-yang pairs of the same typescript: enumeration, later regrouping, cultural claims

- **Status on his pages:** documentary. **Kind:** documentary (non-mathematical text).
- **Where:** cote 84, scans 173,175,177,179,181,183,185,187,189,191,193.
- **Notes (62 entries):** MPL_84_146-193 (62).
- **Notes files:** `inputs/SA02/pro/MPL_84_146-193_notes.md`.

### SA02-8: the notes' apparatus for cote 84 (conventions, counts, coverage, limits, title sheets)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cote 84, scans 97-149,151,153-155,157,159-163,165-173,175-177,179-181,183-193.
- **Notes (27 entries):** MPL_84_097-145 (13); MPL_84_146-193 (13); MPL_84_097-145:records:research_leads (1).
- **Notes files:** `inputs/SA02/pro/MPL_84_097-145_notes.md`; `inputs/SA02/pro/MPL_84_146-193_notes.md`; `returns/MPL_84_097-145_unzipped/.../research_leads.md`.

### SA02-13: the notes' apparatus for cotes 90-91 (citation key, plan, Hua findings, open register entries)

- **Status on his pages:** apparatus. **Kind:** apparatus.
- **Where:** cotes 90+91, scans 2,4,8,35,124,172,608.
- **Notes (5 entries):** MPL_90+91_002-018 (5).
- **Notes files:** `inputs/SA02/pro/MPL_90+91_002-018_notes.md`.

## Counts

- Items: 15; placed entries: 614.
- DEPENDS rows: 29; CLAIM_LINKS: 7; UNIT_LINKS: 73; CORRECTIONS: 7; part-2 check events: 10.
