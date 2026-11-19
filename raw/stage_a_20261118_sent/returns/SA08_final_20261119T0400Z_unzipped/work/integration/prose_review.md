# Independent prose review

Reviewed by GPT-6 Astra Pro; effort not exposed by runtime; SA08/early. Date: 19 November 2026. Read all of `outputs/SA08_dossier.md` (sections 1–14) and `outputs/SA08_directions.md`, comparing the mathematical statements with the already opened reference records and the early/root proof memoranda. No new literature search or new theorem proof was undertaken. Root retains control of prose edits.

## Definite corrections

1. **Dossier §8, paragraph after the four stable groups (line 189 in the reviewed draft):** `the fundamental group H_n(K(Z,n);Z)=Z` is the wrong name. Replace with **“the fundamental-degree homology group”** or **“the lowest nonzero reduced homology group.”** For n>1 the fundamental group is zero, while the displayed homology group is Z. The displayed formula and stable-range qualification are correct. **Root has already applied this correction; the corrected paragraph was reread.**

2. **Dossier §8, Mathew paragraph (line 197 in the reviewed draft):** replace **“The preprint first circulated in 2022”** with **“The preprint was first submitted to arXiv on 23 May 2022.”** The opened arXiv metadata does not establish that there was no earlier private circulation. The journal year 2023 is correct. The key `Mathew2022` intentionally retains the first-arXiv year and is not an error. **Root has already applied this correction; the corrected paragraph was reread.**

3. **Dossier §9 bibliography key:** `@deJong1999` is a conventional shorthand for the actual record `deJong1999Erratum`. This alias has now been added to `reference_aliases.json`; the rerun succeeds. `Cartan1955IX`, `Cartan1955X` and `Cartan1955XI` are all present and are three distinct sources.

## Concrete scope refinements

4. **Dossier §3, Garvín paragraph (initial line 81):** the explicit theorem gives p<q, while Remark 3.3 proves failure of (q+1)-extendability. The remark alone is not a proof that the cohomology comparison fails at p=q. The existing phrase “rules out silently upgrading” is cautionary rather than a literal endpoint counterexample, but the safer wording is: **“Their explicit theorem is restricted to p<q. The separate nonextendability remark shows that a stronger extension property fails; it does not itself decide the comparison at the endpoint.”** The directions currently do not claim endpoint failure and need no analogous correction.

5. **Dossier §4, end of the exact-adjoint proof (line 104 in the reviewed draft):** `earlier restricted field-case argument` understates the retained partial proof. Root’s Frobenius argument covers arbitrary F_p-algebras, and its rational argument covers Q-algebras with the stated grading limits. Prefer **“the earlier restricted characteristic-p and rational-base arguments.”** The full arbitrary-base nonnegative theorem is correctly attributed to the exact coefficient left adjoint, not to that earlier route.

6. **Dossier §5/§10 and direction 2, latest bounded literature addition:** the now-opened Guillén–Navarro–Pascual–Roig paper gives a closer monoidal acyclic-model comparison than a Mandell-only description. A short addition can state: **“Guillén–Navarro–Pascual–Roig’s Theorem 9.2 gives a localized multiplicative comparison under a PID base, free bidegree modules, simplexwise cochain homotopy equivalence and degreewise simplicial contractibility; it does not identify the weighted tau-infinity PD category.”** Relevant exact source locators are Theorem 4.10 p.360, Theorem 8.1 p.372, Theorem 9.2 p.373 and Corollary 9.3 p.376. First arXiv 30 June 2005; journal April 2008; Cambridge 2018 is a platform date. The present “no identification with this category” qualification remains correct. This is a bounded source update, not a new settlement claim.

## Identifier audit

`work/integration/prose_id_audit.json` expands numeric ranges before checking identifiers. At the audited aggregate snapshot, all 76 bibliography citation occurrences resolve after the de Jong alias. Of 490 item/claim/problem occurrences, three use retired IDs inside ranges:

| Location in initial dossier | Retired occurrence | Surviving ID |
|---|---|---|
|Principal finding 3, line 13|SA08-C222 within C217–C226|SA08-C035|
|§3 literature paragraph, line 81|SA08-306 within 305–307|SA08-277|
|§4 higher-Ext paragraph, line 97|SA08-C222 within C220–C225|SA08-C035|

When asserting that prose IDs are canonical, expand these ranges into surviving-ID lists, or state explicitly that range citations use the retained alias bridge. A simple endpoint replacement does not repair an interior retired ID.

The current `outputs/SA08_items.json` snapshot contains none of root’s Codex items 901–916, although all sixteen exist in `work/root/items.json`. Consequently prose occurrences 901,905–907,910–911,914–916 currently fail the aggregate lookup. These are valid source IDs awaiting the next compile, not invented prose references. Root was notified. All other expanded IDs resolve.

## Important qualifications that survived review

- The weighted endpoint, total-weight differential, binomial product and strengthened unweighted CP²/BC₂ obstructions are kept distinct.
- The arbitrary-base finite nonnegative recovery is separated from the false abstract categorical shortcut, negative Hom(Q,-) behaviour and the three different negligible classes.
- The unrestricted coefficient-presheaf counterexample is not extended to locally constant coefficients.
- The quadratic Gamma/Psi complex has differential ±2, its symmetric counterpart has a unit differential, and the exterior normalization is a separate result.
- The half-differential-algebra obstruction includes both the pushout and pullback classes, with tensor exactness stated.
- The flat convolution assertion does not require the target ideal to be flat and does not erase the nonflat or positive-index uniqueness counterexamples.
- Dold’s independent-variable hypothesis, the separate free resolution and the diagonal arity-two counterexample remain explicit.
- The stable Cartan range, the typed interpretation of the smash-product counterexample, Breen’s +1 exponent and the distinction between F_p-module sheaves and abelian sheaves are preserved.
- Mandell’s distinct coefficient theories, the nilpotent/finite-type restrictions where required, and the stronger 2026 Bachmann–Burklund scope are not conflated.
- The SGA donor publication precedes the PD leaves; publication matching is not called an independent proof, and source-level defects remain separate from ink readings.

## Latest bibliography status

After the final uniqueness source and dossier audit: 116 input records, 90 canonical works, 113 distinct used keys resolving to 87 cited works, 84 verified records and six explicitly unverified original-access leads. `REFERENCE_CHECK_EVENTS.tsv` has 90 bibliography-only integration events. Exact input hashes and current counts are in `reference_audit.json`; the successful result is retained in `logs/early_integrate_bibliography_output_007.json`. The preceding failed audit is preserved and identifies only the repaired de Jong shorthand.
