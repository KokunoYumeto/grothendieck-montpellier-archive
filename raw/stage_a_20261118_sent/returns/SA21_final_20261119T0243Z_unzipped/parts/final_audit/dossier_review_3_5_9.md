# Targeted dossier review: III–V and IX correspondences

Reviewed the relevant passages of `SA21_dossier.md` against the finalized III–V and IX09–13 claim records, proofs, reading alarms and source checks. No new research or mathematical rerun. Line numbers below refer to the dossier version inspected on 19 November 2026.

## Concrete corrections

### 1. IV–V paragraph, line83: failed construction is not by itself a disconnection proof

Current wording says that a two-point set disproves connectedness **because** the external-product construction has an empty top residual. The construction's failure alone would establish only failure of that proposed proof. The actual disconnection is established by the separate complete enumeration in C-SA21-5-008.

Suggested replacement for that sentence:

> On a two-point underlying set, the five elementary admissible figures have three comparison components. The proposed external-product construction also fails: it leaves an empty residual at its top.

Evidence: C-SA21-5-008; `parts/cotes_3_5/proof_checks.md`, its C5-008 paragraph and R-SA21-5-008; `outputs/computations.json`, `set_figures_two_points` and `boxtimes_counterexample`.

### 2. IX span paragraph, line127: morphism/comorphism convention and kernel subject

“The manuscript's specified complement-preserving morphisms” conflates the two classes. In the convention on IX104, **comorphisms** preserve complements; **morphisms** have complement-preserving transposes. The proposed factorization is a comorphism followed by such a morphism. Also, “Any nontrivial target ... has zero kernel” assigns the kernel to the target instead of to the map.

Suggested replacements:

> The universal factorization as a complement-preserving comorphism followed by a morphism whose transpose preserves complements also fails.

> Any complement-preserving join map from this six-element lattice into a nontrivial complete ortholattice has zero kernel, forcing its orthogonal transpose to take top to top.

The remainder of the proof summary can stay. Evidence: C-SA21-9-039/065/066; IX104, J156-9-13:182–184; `parts/cotes_9_09_13/proof_checks.md`, P10–P11.

### 3. IX OR-product paragraph, line125: identify the reconstructed coordinate pairing

The product computation is correct, but C-SA21-9-057 explicitly labels its relation as a reconstruction: the transcription on IX101 compares the wrong coordinates and is ill-typed for different factors. The dossier currently presents the product without that qualification.

Suggested short insertion before the114/234 counts:

> Using the coordinatewise OR relation, with the transcription's cross-coordinate indices left for scan review, ...

Evidence: C-SA21-9-057/058; IX101, J156-9-13:107–109; `parts/cotes_9_09_13/readings.tsv` and proofP8. This does not question the computed numbers or the Ischi comparison; it preserves the reconstruction/source distinction.

### 4. Literature table, line142: replace the unspecified adjoint-lemma locator

The PasekaVetterlein2025 row says “specified adjoint lemmas” but supplies no numbers. The checked source version and locators are explicit in the source ledger.

Suggested locator:

> arXiv v3, Lemma2.3, Proposition2.4 and Lemmas3.4–3.7

The current first-arXiv and journal dates are correct. If the revision is mentioned, it is v3 of28October2025; the corrected Proposition6.10 is not used. Evidence: `parts/cotes_9_09_13/source_checks.md`, IX-R5, and its exact-key check event.
