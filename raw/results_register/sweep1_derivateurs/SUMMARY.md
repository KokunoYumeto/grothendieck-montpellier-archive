# Sweep 1 over the register, scope `derivateurs`: summary

Claude Opus 5.5 at effort max, sweep 1, 18 Nov 2026 (launched by the main session, Claude Opus 5.5 at effort max).
Brief: `results_register/SWEEP1_BRIEF.md`. Every return in this scope is by GPT-6 Astra (ChatGPT Pro mode) and
unrefereed. Read-only on everything outside this folder. Files here:

| File | What it holds |
|---|---|
| `PLACEMENT.tsv` | every row (1,586): part, chapter, section of the sketch's outline, how placed, note |
| `MERGES.tsv` | 185 relations among rows (82 canonical items): same, stronger, weaker, refines, refuted by |
| `FLAG_VERDICTS.tsv` | the 95 flags of the scope (64 proved-cites-refuted, 31 no-id dependencies) and 34 found here |
| `XREF_EDGES.tsv` | 71 cross-run "uses" edges read from `depends_on`, missing from EDGES.tsv (23 replace wrong edges) |
| `CORRECTIONS.md` | 15 corrections and refinements (C1-C15) |
| `CHECK_EVENTS.tsv` | the 10 checks I made |

## 1. Counts

- **Rows:** 1,586 = 1,474 of the Dérivateurs line (15 runs) + TOTEX 58 + PRETOT 54. Status: Proved 1,179, Refuted
  211, Known 122, Open 62, Unresolved 4, audited 8.
- **Placement:** all 1,586 placed; 1,326 by a script rule (run and section letter of the id, written after reading
  every statement in short form), 260 by reading the row. Part I 24 (moduli), Part II 1,506 (II.1 small categories
  439, II.2 localizers 815, II.3 dérivateurs 170, II.4 finite models 82), Part IV 56 (stratified spaces). The outline
  has 44 sections; their titles are in `PLACEMENT.tsv`.
- **Merges:** 185 relations, 82 canonical items, 184 member rows: same 87, refines 46, weaker 26, refuted by 15,
  stronger 11. 21 open rows are answered by later runs (CORRECTIONS C3); one more (GALOIS:B.14) in part.
- **Flags:** the 64 "proved row cites a refuted row" are all sound uses of the refutation (read at statement and
  dependency level; four of them re-checked as mathematics). The 31 "dependency names no id" point to the literature
  (14), to another run's id (11), or both (6). New: 23 cross-run citations that sweep 0 parsed as same-run edges;
  11 proved or known rows citing an open row (10 sound, 1 artifact of the parsing). 531 rows carry "proved; no check
  recorded" (a records gap; FREX and DER_LOCALIZERS have check events of their own).
- **Checks of mine:** 10 (`CHECK_EVENTS.tsv`): 3 targeted proof checks, 2 independent re-proofs, 2 computations,
  3 comparisons of a statement with the manuscript. No error found in a proof.

## 2. The corrections that matter most

1. **XVI ms. 118, footnote 56** (C2). The intake of S2COUNT/REVLOC (Claude Fable 5.2 at effort high, 17 Nov) says
   REVLOC F.1 proves the footnote's doubt right. It does not: the footnote sits on Corollaire 7.7.2
   (Loc (6' a, 8, 9) => Loc (1 ter, 3 bis)); REVLOC:F.1.1, DER_FOLLOWUP:G.9 and DER_LOCALIZERS:A5.4 prove the
   corollary, even without Loc (9), so the footnote's "probablement faux" is wrong. REVLOC:F.1 (checked by me in
   full) is about the axioms without Loc (6' a). The later intake (Claude Fable 5.2 at effort max) had flagged the
   record; it is still uncorrected.
2. **Twenty-one open rows are settled** (C3), among them the main question of the totality line, total => exact (no:
   C_delta, TOTEX2), CATHOT D.6 (no: a six-arrow monoid has continuum many classes into S^2), POLES A.16 (no: four
   runs), GALOIS B.13 (decided by set theory: Vopenka's principle gives yes, no measurable cardinals gives no). The
   status lines in the companion and the readers should follow.
3. **The register's dependency graph has wrong same-run edges** (C7): 23 citations of other runs ("PRETOT F.1",
   "TOTASPH C.6", "GALOIS C.7") became edges inside the citing run, and 71 cross-run edges are missing. Fix in
   `build_register.py`; the edges are in `XREF_EDGES.tsv`.
4. **Refuted rows mostly state the counterexample** (C8): 165 of 211 are true statements, so a "uses a refuted row"
   flag is almost always a sound use. The handbook's item model should split each into the refuted claim and the
   proved counterexample that refines it.
5. **Open questions missing from the register** (C9): FREX, DER_FOLLOWUP and TOTEX2 have no Open rows, but FREX and
   DER_FOLLOWUP keep their main questions open in their reports. Sweep 0 should read the ledgers.
6. **Notation** (C11-C13): W-dagger and W-tilde each name two classes; T_n means two different classes in TOTEX and
   DER_FOLLOWUP; "total" is written without its localizer.
7. **FREX corrects the Dérivateurs expert** (Claude Fable 5.2 at effort max) on three of its Leads and confirms two
   of its findings (C5). And C1: the exactness of Delta_inj is Isbell-Mitchell 1973, Th. 3 (Known).

## 3. Per chapter: proved, open, and the strongest proved reduction of each open item

### II.1 Small categories (439 rows: Proved 363, Refuted 44, Known 20, Open 12)
- **Proved, the main line.** Total W_inf-asphericity = ordinary colimits of simplicial sets are homotopy colimits
  (TOTAL_ASPHERICITY:C.5, = STRATA:G.2) = weak contractibility of every component of every El_A(H) (TOTEX:A.1). With
  a weakly terminal object, total = filtered (C.13; Isbell-Mitchell 1976). His conjecture at II ms. 36ter is false:
  Delta_inj (C.10; Isbell-Mitchell 1973). Filtered = total + sifted = total + one positive abelian EM test
  (PRETOT:F.3, TOTEX:F.2). All Cat-valued comparisons are weak equivalences iff every component is filtered
  (PRETOT:F.1). The strict chain filtered < exact < total < quasi-filtered, witnesses Delta_inj, C_delta, repaired K*
  (TOTEX2:D.1). Truncated totality: the classes Q_n are all distinct, witnessed by A_n(F_2) (DER_FOLLOWUP:A.8-A.9).
  Presheaf totality: on Delta the total presheaves are the acyclic, resp. contractible, simplicial sets (PRETOT:A.2);
  total W_Z does not give total W_inf (PRETOT:A.5). Exactness and totality of a Fraisse category depend only on the
  topological group (FREX:A.1, A.26); the predimension family C(k,a,b) is total for all parameters, and exact <=>
  amenable <=> extremely amenable <=> b >= (k-1)a (FREX:D.2-D.6).
- **Open, with the strongest proved reduction:**
  - *Amenable => exact over Q?* (FREX A.3 (iii); not a register row). Exact does not give amenable (FREX:A.11);
    amenable does not give exactness over F_2 or Z (FREX:A.19). Reduced to groups with non-metrizable universal
    minimal flow (FREX:A.23), with an extra analytic condition on any counterexample (FREX:A.30).
  - *The total-index exactness question of FREX C.4* (not a register row): the all-prime implication is refuted;
    filtered Kan totalizations and Kan assemblies over exact bases are excluded (FREX:C.25-C.27); three-arrow
    obstructions exist in every degree (C.28); ultraproducts fail (C.29).
  - *The free-monoid comparison over C_delta* (FREX G.1/G.2, from DER_FOLLOWUP's reductions D.8-D.10; not a register
    row): reduced to the kernel of a transgression from H_2 of the quotient tree to the cut stabilizers
    (FREX:G.30-G.33); FREX:G.34 shows the transgression cannot be bypassed.
  - TOTEX:F.5 is a literature-access row (partly answered by FREX for Oberst 1968).

### II.2 Test categories and fundamental localizers (815 rows: Proved 590, Refuted 121, Known 56, Open 36, Unresolved 4, audited 8)
- **Proved, the main line.** XII Théorème 2 is false: W_inf fails W(7), W(7 bis), Loc (6 b, c) (POLES:B.8, G.2); W_Z
  is the least reversible localizer (POLES:D.1); no localizer has both poles (POLES:D.2); reversible localizers and
  localizing subcategories of spectra form a Galois connection that is not a bijection (POLES:F.4, F.7); an
  accessible reversible non-RT-fixed localizer exists in ZFC (DER_LOCALIZERS:A.7, A.9). Absolute Theorem A does not
  give relative Theorem A, even with Loc (8), (9) (REVLOC:F.1, checked); forward gluing and filtered colimits do
  (REVLOC:F.1.1). Accessibility of W^lc_D depends on set theory (REVLOC:H.2, H.3). Strict retraction holds in the Hot
  class (INDLOCAL:D.1) and fails in the Cat_hot class (D.19). The VII path comparisons hold for arbitrary wide
  markings (PATHS:C.P1-C.P3). Acyclic simple overgroups and cardinal-controlled Kan-Thurston (INDLOCAL:A.1,
  GALOIS:B.11).
- **Open, with the strongest proved reduction:**
  - *REVLOC D.2.4* (the zero finite thick subcategory): about fifty computation rows D.2.10-D.2.61 toward it; no
    decision. *REVLOC D.3.2* (the projective-space interval): D.3.1 (no largest non-total reversible localizer).
  - *DER_LOCALIZERS A3.decision* (a non-RT-fixed reversible localizer with nonzero stable part and no finite spectra):
    reduced by A34.6 to one accessible reversible closure generated by A = Q Sigma^3 V, V connected primary, with a
    sufficiently connected A-null H-space in the same ideal. *A4.equality*: reduced to contractibility of P_{BC_2} H
    for every countable simply connected primary sphere-null H-space (A4.5, A4.6). *A4.interval*, *A4.size*:
    endpoints only (A4.7, A4.3). *C.raw_gate*: proved on the sufficient scopes C.11, C.13, C.15, C.23, C.27, C.29.
  - *The S^2 frontier in dimension two* (INDLOCAL A3(iii); S2COUNT E:E2, E3gap, E4gap): mu >= 2^aleph0 excluded
    (INDLOCAL:A.20); the exact answer mu < kappa when kappa^aleph0 = kappa (S2COUNT:E:exact); finite mu done (A.10);
    open interval aleph0 <= mu < 2^aleph0 for S^2.
  - *Strict-bifibration models of local systems* (STRATA E.11; instances BISITE B.21, PATHS E.11; RESIDUE A.8): proved
    for 1-type bases and for all-monic or all-epic bases (STRATA:E.8-E.10, RESIDUE:A.6).
  - *CATHOT E.17* (local presentations of invariant ind-objects): INDLOCAL B classifies invariant ind-objects;
    whether that settles E.17 is for sweep 2. *CATHOT E.27*, *PATHS B.8, C.9, C.10, D.22*, *RESIDUE B.10, D.7, D.9,
    E.6, J.2, J.3*, *BISITE C.10*, *RESIDUE C.8* (five objects suffice, RESIDUE:C.3; minimality open): reductions as
    stated in each row.

### II.3 Dérivateurs (170 rows: Proved 113, Known 24, Refuted 26, Open 7)
- **Proved.** For every derivator, W^lc_D satisfies absolute and relative Theorem A (GALOIS:B.1, B.3); the chain
  W^lc in W^1 in W^coh cap W^hom in W_D (A.2), W^1 not a localizer (A.5); exact values for truncated spaces, rings and
  spectra (C); reconstruction of spaces from enhanced local systems (F.1-F.3). Every accessible fundamental localizer
  is W_D for D = HOT_W (REVLOC:G.2: the expert's unchecked aside in the REVERSIBLE_LOCALIZERS prompt, now proved).
  Final Der 6 does not force pointedness; it gives RT-fixedness (DER_LOCALIZERS:A2.3, A2.4). The naive
  finite-dimensional local-system class fails two-out-of-three; the repaired class is Toen schematization
  (DER_LOCALIZERS:D.1, D.4).
- **Open:** a functorial D -> D' with W_{D'} = W^lc_D for bare derivators (GALOIS:E.11 = G.6); reconstruction from
  ordinary fibre functors only (F.8); properness of W^lc for general E (B.14; not proper for K(n) and KU,
  REVLOC:E.7, E.9); BISITE:F.18 (strict higher indexing); RESIDUE:I.7.

### II.4 Finite models of homotopy types (82 rows: Proved 64, Refuted 9, Known 7, Open 2)
- **Proved.** A six-element monoid M has BM ~ wedge of S^n (n >= 2) and continuum many classes into S^2 and S^3;
  every category with at most five arrows has countably many; a finitely dominated BC has countably many
  (S2COUNT:A.M1, B:main, B:smallcategories, B:finitedomination). So CATHOT D.6 is answered no. Sphere and RP^2
  minima (CATHOT:G.7-G.16); the five-element sphere monoid is the unique non-1-type monoid of order at most 5
  (RESIDUE:A.5).
- **Open:** a_pos(RP^2) in [28, 49] and the intrinsic classification of the types of finite categories (CATHOT:G.17;
  FINMON, outside this scope, carries the finite-model line).

### I.2 Moduli (24 rows) and IV.1 Stratified spaces (56 rows: Open 5)
- **Proved.** Exit-path and entrance categories of the strata of M_{0,n}-bar (STRATA:F; counts 4, 26, 236 checked);
  for every stable (g,n) the entrance forgetful functor is W_inf-proper (RESIDUE:H.5), not always smooth
  (BISITE:F.16; STRATA:F.11 refuted); the Teichmüller groupoid with its Lego presentation (STRATA:F.17). EI
  categories and constructible coefficients (STRATA:B); gluing along a sieve and its cosieve (STRATA:C, POLES:G.19).
- **Open:** STRATA:A.6, B.5, B.12 (unrestricted coefficient dictionaries); BISITE:D.12 and RESIDUE:G.3 (topological
  realization over a locally compact base; RESIDUE:G.1 refutes one proposed realization).

## 4. Runs not taken in before (field_experts/INTAKE_LEDGER.md), and what I found in them

- **FREX** (cp10, 18 Nov 11:58 UTC; 145 rows; no intake). Still running. Main results: exactness and totality are
  invariants of the topological automorphism group; exact does not give amenable (finite posets with an independent
  order, FREX:A.11) and amenable does not give exactness over F_2 or Z (ordered punctured F_2-vector spaces, A.19,
  A.33); the complete profile of the cocycle categories A_r(Lambda) (Q-exact iff Lambda torsion, F_p-exact iff p is
  invertible on Lambda, Z-exact iff Lambda = 0; C.13); the predimension family classified (D). Open: A.3 (iii), C.4,
  G.1/G.2 (section 3). It corrects three of the expert's Leads and confirms two of its findings (CORRECTIONS C5). Its
  register has no Open rows (C9).
- **DER_LOCALIZERS** (cp08, 18 Nov 09:54 UTC; 100 rows; no intake). Still running; its review 6 records one stalled
  review. Settled: the shift and Der 6 questions (A2), relative Theorem A and Corollaire 7.7.2 (A5), interval
  recognition (B), the finite-dimensional local-system localizer (D: the naive class is not a localizer; the repaired
  class is schematization); the unrestricted linear theorem is refuted (C.26). Five rows open (section 3). It agrees
  with REVLOC and DER_FOLLOWUP on footnote 56 (C2).
- **S2COUNT** (final, 16 Nov; the earlier intake read its register at statement level only). The finite-category
  programme for S^2 at V ms. 51-52 and VII ms. 121 is answered no (S2COUNT:B:main). Its load-bearing step A.M1 (the
  homotopy type of BM) is still unread by anyone; my check covers the deduction from it and the finite-domination
  bound. Its TASK rows are task records, not statements (C10). Its E rows agree with INDLOCAL A (same results, audits).
- **REVLOC** (cp17; 11 of 152 rows named by an intake; its register holds titles only). F.1 checked in full
  (correct); F.1.1 settles footnote 56 against the footnote (C2); H.2/H.3 settle GALOIS B.13 relative to set theory;
  E.7, E.9 settle instances of GALOIS B.14; G.2 proves the expert's aside. D.2.4 stays open after about fifty
  computation rows.
- **RESIDUE** (2 of 85 rows named by an intake). Its open F.5, F.6, F.7 are answered by TOTEX2 and PRETOT (C3); its
  B.3 is an earlier refutation of absolute => relative Theorem A; its H rows hold moduli results placed in Part I.

## 5. For sweep 2

The cross-run graph from `XREF_EDGES.tsv`; the split of refuted rows (C8); the open questions from the ledgers (C9);
REVLOC's statements from its sections (C10); CATHOT E.17 against INDLOCAL B; S2COUNT A.M1 read in full; who wrote
footnote 56 (Grothendieck or the editors).
