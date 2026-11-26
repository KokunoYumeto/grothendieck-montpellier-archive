# Fermat sections: proofs and verification records

This workbench studies Grothendieck's question about sections of the arithmetic fundamental group of Fermat curves. The main paper gives the full-group Selmer theorem and separates the deduction about all sections from its local input. A companion studies solvable and pro-3 quotients.

The papers are self-contained mathematical arguments. Published inputs are cited with exact statements. This directory contains only original text, calculations and verification records; external sources and input attachments are not redistributed.

## Reading order

1. `papers/fermat/main.pdf` and its editable LaTeX project.
2. `papers/quotients/main.pdf` and its editable LaTeX project.
3. `QUESTIONS.tsv`, `STATEMENTS.tsv`, and `CHECK_EVENTS.tsv` for the precise mathematical and verification status.
4. `checks/` for independent calculations and expected output.

This is an unfiled workbench edition. The custodian assigns the WB number and permanent record page. Local statement tags remain stable; no number in the central registry is claimed.

Canonical proposed repository: https://github.com/KokunoYumeto/k-theory-and-galois-groups-workbench
Permanent record registry: https://github.com/KokunoYumeto/mathematics-workbenches

## Reuse

Original mathematics, text and code are dedicated to the public domain under CC0 1.0. Citations identify third-party works; their copyright is unaffected. No human verification has been performed or claimed. See each paper's method note for the precise model-checking provenance.

## Mathematical state

The full profinite theorem covers every odd exponent. The finite-derived, metabelian and prosolvable theorem covers every odd exponent divisible by 3, 5, 7, 11, 13 or 19. At every exponent3^r,5*3^r or7*3^r with r>=1, the geometric pro-3 theorem covers the full group, every finite derived quotient, and every finite lower-central quotient. The general formulation uses torsion-free ordinary lower-central factors and requires no global lift of a quotient section. Other odd exponents for the smaller groups remain open. Arbitrary noncuspidal pro-3 sections exist at every power-of-3 level and fail the Selmer condition at 3.

The companion also proves an exact split-prime finite-descent criterion. A rational consequence of the quadratic-Hilbert Euler-system machinery, with explicit CM image conditions, now proves the required split-prime Tate–Shafarevich vanishing for the known rank-zero exponent-13 Prym. The all-prime finite-derived, metabelian and prosolvable results therefore include every odd exponent divisible by 3, 5, 7, 11, 13 or 19. The arithmetic proof has passed whole exposed audits and a separate statement-only reproof. The independent proof was frozen before exposure and its different CM image argument has passed the full comparison. For the three pro-3 families n=3^r, 5*3^r and 7*3^r (r>=1), compact integral Selmer localization at3 is proved without a rank or Tate–Shafarevich assumption. A broader conditional criterion for n=3^r q^s removes the boundary obstruction when r=1 or q is congruent2,4,5,7mod9, once compact Selmer localization at3 is injective. A sharp rank obstruction explains the remaining boundary-localization range. For the septic family,592 exact principal-ideal witnesses and an unconditional explicit-formula bound prove the needed three-class vanishing in an explicit degree-56 field. The exact full class number is not needed or asserted. The question table gives the complete remaining gates.

At exponent17, every simple factor of the Fermat Jacobian has positive rational rank, so the rank-zero abelian target method cannot settle that case. At exponent19, the genus-nine Jacobi quotient has a rational rank-zero sixfold complement. A rigorous interval certificate proves 9.96 < Lprime(J,1) < 9.99 by factoring its L-function into three degree-six CM functions, checking every finite input exactly, and bounding both analytic tails. Zhang’s rank-one theorem then gives full Tate–Shafarevich finiteness and adds all odd multiples of19 to the smaller-group classification. The conditional arithmetic implication has a separate statement-only reproof and complete comparison. The independent numerical reconstruction is complete, frozen before exposure, whole-compared and independently replayed. The whole-section statement-only reconstruction is also complete, frozen before exposure, and has passed the root comparison. The first missing prime remains17. Its local Brauer-zero set at17 is now proved to contain just the three rational coordinate cusps, and compact T17 localization is injective throughout the17-power tower. These local statements do not supply the missing all-prime global bridge. The paper states a sufficient positive-rank split-prime criterion and the exact unverified local hypothesis. Compact localization at the base exponent11 is also proved for every coefficient prime: a certified simple zero gives finite whole Sha, and the rational rank-one factor decomposition controls logarithms and the integral torsion kernel. This adds no new affine pro3 exponent.

The compact source-localization theorem now holds for every odd regular prime p and every Fermat exponent p^r, without rank or Tate–Shafarevich hypotheses. At base five and seven the stronger integral source-H1 injection is also stated directly. The separate statement-only proofs and their complete comparisons are preserved.

For every odd exponent, the companion proves a further prosolvable sufficient criterion: a stable cyclic subgroup of order nine in the pulled-back Frey representation forces cuspidality. Any hypothetical noncuspidal section therefore has an irreducible three-adic representation and is integral at a density-one set of primes. The criterion does not assert that the invariant subgroup always exists, and density one does not give finite ramification. The complete exposed proof and source checks are recorded; a separate statement-only reconstruction is in progress at this edition's freeze.

At exponent31, the order-three quotient separates a positive-rank fivefold from a rationally simple tenfold whose rank is either zero or two. The exact CM-field class numbers are one and three, and the whole Jacobian's central value and first derivative vanish. These computations identify why the nineteen argument does not carry over; they do not prove the complementary rank-zero or Tate–Shafarevich condition. A separate explicit group-cohomology example proves that generation by conjugate local subgroups, even with zero local invariants, cannot replace compatibility of their coboundary parameters. Exact relation and character-module criteria state what remains to be tested.

## Records and reproducibility

Every numbered theorem, lemma, proposition, corollary, definition, hypothesis, and remark appears in the statement inventory. Check events distinguish unexposed same-model re-proofs, post-exposure comparisons, certified computations, and published background inputs. The source table gives exact statements, pages, addresses, and reading limitations; the source-hash table fingerprints excluded external artifacts.

Each paper has its own `BUILD.md`, deposit sheet, editable sources, and PDF. The mathematical certificate commands and expected bounds are in those build files and the original check records. `FORMAT_PREPARATION.md` explains stable local tags, registry allocation, the supplied filing utility, validation, and the manifest protocol. No central WB number is fabricated.


Long exact numerical witness records are stored in line-aligned parts below the format-1 per-file limit, with complete SHA-256 reconstruction manifests. To reconstruct all original long records in a separate working folder, run `python3 tools/reassemble_records.py /tmp/fermat-record-replay`. The helper verifies every chunk and the reconstructed files. Each final paper also includes its own standalone certificate inputs and commands.

The separately frozen statement-only septic proof is also reproducible directly from its text inputs: `python3 records/fresh_checks_target15_rerun.py --gp /absolute/path/to/gp`. It requires PARI/GP and python-flint, creates isolated temporary copies, verifies 590 principal witnesses and two ideal-class relations, checks complete coverage of the 592 bounded prime ideals, and proves the strict root-discriminant contradiction. Expected output is `all_assertions: PASS` and `preserved_inputs_unchanged: true`. Its full proof, exposure record, input hashes, independent code, root replay and whole-proof comparisons are preserved separately.
