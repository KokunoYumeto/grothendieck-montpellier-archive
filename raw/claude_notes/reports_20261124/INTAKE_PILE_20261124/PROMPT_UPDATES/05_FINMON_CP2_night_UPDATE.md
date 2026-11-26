# Update of `TO_SEND/PRO/8_Derivateurs_mathematics/05_FINMON_CP2_night` (25 Nov 2026)

- **By.** Claude Opus 5.5 at effort max, agent a34c04448e8299803 (the Dérivateurs field expert), on the brief
  `PROMPT_UPDATE_BRIEF.md` of the main session 329fb1e6 (Claude Opus 5.5 at effort max).
- **Sent?** The prompt is not in `TO_SEND/PRO/SENT_PRO.tsv` (no row matching FINMON) and does not sit in a SENT folder.
- **Backup.** `TO_SEND/PRO/_backups_20261125/05_FINMON_CP2_night/` (the PROMPT.md and ZIP as they were).
- **The send folder** keeps PROMPT.md and its one ZIP.

## Changes, with their evidence

1. **New input R8: Ben-Bassat, arXiv:2610.38760v1 (28 Oct 2026), "On a Conjecture of Fiedorowicz".**
   - **Source.** The e-print source was fetched from `https://arxiv.org/e-print/2610.38760` (SHA256 of the gzip
     `9077990d…bc`) and put in the ZIP as `literature/benbassat_2610.38760v1/`.
   - **What the prompt now quotes**, by line of `Fiedorowicz2.tex`, each opened at the statement:
     - Theorems A, B and C (lines 142-193);
     - the 1795-element `M_{CP²}` (lines 1240-1252: `35 + 4·5·88 = 1795`);
     - the 122-element `M_122` and the sentence "determining the least order of a finite monoid M with BM ≃ CP² remains
       open" (lines 1328-1376);
     - §7 and Conjecture 7.1 (lines 1269-1290).
2. **New input R9: our converse.**
   - **Source.** `derivateurs_companion_20261109/pro_reviews_max_20261112/1_CATHOT/OWN_RESULTS.md` §2 (Theorems 2.1, 2.2,
     Corollaries 2.3-2.5). It is put in the ZIP as `expert/CATHOT_OWN_RESULTS_20261112.md`, with the second derivation
     `expert/CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`.
   - **Statements.** Quoted from the file. I read the statements and the short reductions 2.1 ⇐ 1.1 and
     2.2 ⇐ 2.1 + Hatcher 4C.1.
   - **The consequence written into the prompt.** Ben-Bassat's Conjecture 7.1 is false (`RP²`). This is also
     `OLDER_NOTES.md` item 1.
   - **Check state, as recorded.** Claude Fable 5.2 at effort max (author, 12 Nov). A second Claude Fable 5.2 at effort
     max (12 Nov). The older-notes finder, Claude Opus 5.5 at effort high (24 Nov), read the proofs in full.
3. **New input R10: Carcacía-Campos, arXiv:2611.09718 (6 Nov 2026), minimal acyclic categorical models.**
   - **Source.** The e-print source is in the ZIP.
   - **Statements quoted**, with their labels and lines in `Acyclic_models_v8_1.tex`: `thm:bouquets` (l. 471),
     `thm:moore` (l. 637), `thm:RPn` (l. 740), `thm:lens` (l. 815), `cor:nu-product-wedge` (l. 342), `cor:infinite`
     (l. 513). CP² does not occur (checked by search).
   - **Where it came from.** It is named in `TOPICALITY_GCT_AG_DER.md` (item 3, "Literature since").
4. **New input R11: Sweeney, arXiv:2502.05276v2, and Martinian–Steinberg, arXiv:2511.12657.**
   - Their e-print sources are in the ZIP.
   - The abstracts were opened.
   - Both are named in `TOPICALITY_GCT_AG_DER.md` item 3 and `OLDER_NOTES.md` item 1.
5. **New input R12: my map's item K7** (`MAP_HOMOTOPY_CATEGORIES.md`, in the ZIP as
   `expert/MAP_HOMOTOPY_CATEGORIES_20261125.md`). The rest of the map (K1-K6; Hora, Sun and Pongrácz) does not bear on
   this prompt's questions and was not added.
6. **Settled or overtaken items.** No item of the prompt is settled by outside work. Ben-Bassat does not determine
   least sizes; Carcacía-Campos does not treat CP².
7. **New questions** (Part A, after item 5, in the order of importance):
   - **A.6: the least order of a finite monoid of type CP².** FINMON claims 23 (`B:CP23`, `B4-CP2`). This is
     exactly the question Ben-Bassat states as open, with his 122 and 1795. The upper bound, the lower bound and the
     list of minimal monoids are to be proved completely.
   - **A.7: `ν(CP²)`.** This is Carcacía-Campos's invariant: the least number of objects of a finite acyclic category of
     type CP². The lower bound 5 comes from the dimension of the nerve; a minimal model is to be given completely, with
     the least number of arrows at that object count.
8. **Part C.1** now states:
   - the characterization (Ben-Bassat's Theorem C with our Theorems 2.1 and 2.2);
   - the refutation of Conjecture 7.1, each step checked by the run;
   - `m` and `ν(CP²)`.
9. **Part C.2** (literature record) now starts from R8, R10 and R11 and what they cite: Fiedorowicz 1984/2002, McDuff
   1979, Burke 2021, and Nico's conjectures.
10. **A correction to the prompt's rules.** The paper-completeness lint failed on the prompt as drafted (and as
    backed up): it is missing the rule "known results are cited with locators, not re-proved". I added one sentence
    to the paper deliverable: "Known results are cited with exact locators ..., not re-proved; a short derivation is
    given only where the source does not state the form you use. Every new result is proved in full."
11. **Kept unchanged.** The main questions (Part A.1-A.5, Part B), the push paragraph, the three-hour ledger check, the
    checkpoint rules, CHECK_EVENTS.tsv and every rule of proof. No minimum, way out or cheaper alternative was added.

## The ZIP

`FINMON_CP2_background.zip`: 1264 → 1279 members, 3.80 MB → 4.12 MB. Every earlier member is kept unchanged, and the
ZIP stays flat (no ZIP inside). The new members are listed with origin, bytes and SHA256 in
`MANIFEST_ADDED_20261125.tsv` at the root:
- `literature/benbassat_2610.38760v1/`;
- `literature/carcacia_campos_2611.09718v1/`;
- `literature/sweeney_2502.05276v2/`;
- `literature/martinian_steinberg_2511.12657v1/`;
- `expert/CATHOT_OWN_RESULTS_20261112.md`;
- `expert/CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`;
- `expert/MAP_HOMOTOPY_CATEGORIES_20261125.md`.

## Lints

- `push_rule_pro_prompts.py --lint-math PROMPT.md`: `files: 1 failing lint: 0`.
- `paper_completeness_lint.py PROMPT.md`: `ok` (it failed before change 10, on the prompt as drafted as well).

## Proposals: findings of the field that deserve a prompt of their own

None of these is built; the main session decides. Each comes from `MAP_HOMOTOPY_CATEGORIES.md`. Before building any
of them, check whether a waiting prompt can take it.

1. **Shapes of pushouts of profinite topoi and hole filling** (map K2).
   - **Main question.** For profinite groups and boundary maps as in LM5 C.2, when does the bicategorical pushout of
     classifying topoi of profinite groups compute the shape (étale homotopy type) of the glued object? For discrete
     groups the answer is proved in K2: exactly when the homotopy pushout is aspherical, by Whitehead's theorem for
     injective edge maps.
   - **The profinite analogue.** Its likely form is goodness (Serre) plus injectivity of the profinite edge maps. Apply
     it to hole filling for étale fundamental groups of curves, where the capped-surface defect π₂(S²) = Z appears in
     genus 0.
   - **Why.** It decides when LM5's mixed and filled topoi carry the right homotopy type. LM5 C.3 and SA10 B2.2 found the
     discrete defect independently.
   - **Inputs.** LM5 `sections/C.tex` (C.1-C.5); SA10 parts B (B2.1, B2.2); K2; Lurie HTT 7.1.6; Moerdijk on
     classifying topoi of profinite and localic groups.
2. **The nerve of the category of admissible PD theories** (map K1).
   - **Main question.** Is B𝒜 contractible, i.e. are the C.3 questions A-CS and A-TL true in the strongest form?
     Equivalently, is the countable gate 𝒞^[d]_ω (or ℰ^[d]_ω) cofiltered up to the run's replacements?
   - **Why.** K1 shows that the run's reductions preserve the homotopy type of the nerve, so this is the natural target.
   - **Inputs.** SA08 Part C, SA08_C3_D031 (A-003, A-006, A-S09-24 to -30, AT12, AT28), K1.
   - **Routing.** It belongs in the next C.3 prompt if one is waiting.
3. **Exit categories of M̄_{g,n} and constructible sheaves** (map K6).
   - **Main questions.**
     - Prove that forgetting a mark, T_{0,n+1} → T_{0,n}, is not W_∞-smooth for every n ≥ 4. The step that remains is
       locality of BISITE's lifting categories under the product decomposition near D_{12}.
     - Give the exit-category description of M̄_{g,n} where conditional infima exist (EXIT_TOWER A.2 = SA10 A4.5), and
       its failure elsewhere.
   - **Why.** It joins the companion's six operations on Cat (BISITE F.10-F.17, RESIDUE H, I) to the Teichmüller tower
     (cotes 147, 148, 150).
   - **Inputs.** BISITE `A_results.csv`/`BISITE_results.csv` F.15-F.17 and D.11; EXIT_TOWER cp28; SA10 (A1.2, A4.5,
     C5.08); RESIDUE H.3-H.6; Lurie HA A.9.
4. **FREX successor** (already proposed in `DERIVATEURS.md`), with two additions:
   - the topos dictionary of K3: exactness over R as exactness of π_! on Cont(Aut M) ≃ Sh(A^op, J_at), Caramello 2014;
   - the gate of `TOPICALITY_GCT_AG_DER.md` item 4: is the signed integer averaging of A.9-A.10 a Z-valued
     Harman-Snowden measure?

   Its main questions stay A.3(iii) and the total version of C.4.
