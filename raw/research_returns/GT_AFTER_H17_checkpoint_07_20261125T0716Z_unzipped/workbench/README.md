# The arithmetic quotient after relation (IV)

This workbench contains original proofs, papers, independent computations, and a statement-level audit of the attached research archive. It does not contain copies of third-party papers or unchanged attached files.

The main question is the restriction of invariant quadratic characters of the normalized profinite Grothendieck–Teichmüller group to its intersection with the absolute Galois group. The invariant space and its restriction image both have countably infinite dimension. The complete image and relative restriction kernel remain open, as does GT=G_Q.

Exact arithmetic normalizations remove every rational Kummer coordinate, all Magnus terms through degree ten, and the entire dyadic metabelian multiplier. The resulting subgroup E has infinite index in the preceding D10. A further primitive mixed coordinate in degree eleven has exact arithmetic imageZ2; its kernel E-prime carries the same relative obstruction. Restriction from the original invariant character space to E-prime has exactly the known rational Kummer-plus-cubic kernel, on which arithmetic restriction is injective.

The complete corrected adelic CM-frame pair gives another arithmetic normalization, with quotient the Galois group of Q(sqrt(-3))ab Q(i)ab. Its exact intersection with rational radicals is computed. Both normalized signed frame comparisons are proved; consequently the exceptional quadratic character at three is zero. The remaining joint compatibility conditions are explicit tame cubic and harmonic residue tests. An explicit genus-ten finite-homology determinant is another relative character whose vanishing on GT is undecided.

## Contents

- `papers/arithmetic_quotient/`: the arithmetic quotient, character restriction, and arithmetic consequences.
- `papers/gentle_characters/`: the gentle group, graded computations, and the pentagon.
- `research/`: original computations and full audit notes.
- `STATEMENTS.tsv`, `CHECK_EVENTS.tsv`: permanent statement tags and accurately typed checks.
- `CROSSWALK.tsv`: earlier statement identifiers mapped to the paper; changed or removed statements retain their history.
- `SOURCES.tsv`: bibliographic records and check scopes, without copies of source texts.
- `QUESTIONS.tsv`, `LEDGER.md`: question status and dated research gates.
- `LITERATURE.md`: primary-source locators and dated search record.
- `versions/`: manifests of delivered versions.

No result is labeled human checked. Independent workers in this session use the same model family. The public repository addresses appearing in the papers identify the intended workbench and record locations; this package has not been published or pushed to either repository.

All original text and programs in this package are dedicated to the public domain under CC0 1.0.

## Proof and check status

The finite cubic, fifth, seventh, eighth, ninth and tenth layers have full proofs and exact arithmetic witnesses. The finite certificates and their separate computations remain in research. The ninth upper bound is now presented through an integral beta measure, which also proves the uniform all-odd bound. The fifth, seventh, eighth, ninth and tenth quadratic characters have precisely stated extension thresholds; they are not assumed to extend to the original normalized group.

The exact ninth and tenth normalizations have complete separate statement-only re-proofs. The earlier weight-seven independent attempt was partial for its last parity step; its subsequent complete targeted certificate check remains separately labeled. The uniform infinite normalization has a complete proof-informed reconstruction and targeted comparison, and a complete separate statement-only re-proof. The cubic identity has a complete targeted proof and primary-source check; its separate statement-only attack reached the algebraic reduction but remained partial at the geometric comparison. The mixed degree-eleven theorem has a complete targeted proof check and separate coefficient calculation; a statement-only attack is underway. Records distinguish these scopes.

The second paper proves a large explicit abelian quotient of the gentle group modulo the normal closure of GT, including the countable quadratic family and odd-primary quotients. Its complete quotient structure remains open. It also gives the exact weight-sixteen computation and distinguishes the deep frame character from all metabelian quadratic characters.

## Local release preparation

`records/RELEASE_WORKFLOW.md` describes the tested Format-1 staging, source-commit provenance, complete manifests and offline history restoration. The preparation tool has only been tested on a disposable fixture. No live version has been sealed or published.
