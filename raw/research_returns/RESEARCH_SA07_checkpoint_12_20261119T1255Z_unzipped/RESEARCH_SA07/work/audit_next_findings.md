# Checkpoint-03 mathematical and source addendum

Date: 19 November 2026. Agent: period_triangle, GPT-6 Astra Pro (OpenAI), inherited effort not independently specified. This record supplements the existing proof and source ledger; it does not replace earlier checks or silently erase unresolved source claims.

## Status changes

All 154 requested original note entries and all 307 assertion IDs remain present. Six assertions formerly classed as OPEN or DOCUMENTARY-GAP now have exact refutations:

| Original assertion | Previous status | Current result | Exact closure |
|---|---|---|---|
| I.P33.03 | OPEN | B.4.4 | The actual Artin–Tate realization has compact image `Z_ell × Z_p^times`, with every finite object crystalline, but has no open pro-p subgroup and therefore is not p-adic analytic in its inverse-limit topology. The two section maps and all compatibility equations are constructed. |
| I.B05.01 | DOCUMENTARY-GAP | F.3.10 | The complete LM6 A.50 is now read. Its noncuspidal branch produces a weight-one Jacobian character, and does not establish the cyclotomic-action premise needed for A.22. The original proof needs, and admits, the exact enlargement `N → NA`. |
| II.MB15.02 | DOCUMENTARY-GAP | F.3.10 | The same full-source check shows that the Stix cyclotomic criterion is not supplied in the residual Jacobian branch. A.22 remains open. |
| II.P16.02 | OPEN | F.3.11 | A discontinuous quotient of the multiquadratic Galois group gives an exact semilinear action on a two-point finite étale scheme which cannot descend algebraically. The actual tensor-Isom fpqc torsor remains effective. |
| II.P06.01 | OPEN | D.4.2, independently checked | The genuine Tate motive `Q(-2)` has integral scalar group `G_m` and image `(Zhat^times)^2`; square-class quotients at arbitrarily many odd primes prove infinite index. The exact map from the `Q(-1)` tensor group is `t → t^2`. |
| II.SF21.01 | OPEN | D.4.2, independently checked | The same Tate example refutes the unrestricted strengthened Tate statement under the manuscript's stated integral group convention. Named elliptic open-image results remain proved. |

Final inventory counts at this checkpoint are PROVED 195, REFUTED 44, OPEN 28, READING 30, DOCUMENTARY-GAP 9, and NAMED-CONJECTURE-IMPLICATION 1. Coverage has zero missing entries and zero duplicate assertion IDs. `open_rows_review_20261119.csv` preserves a review row for all 43 originally OPEN/DOCUMENTARY-GAP assertions, including the six now closed.

## Complete LM6 source and unchanged hypotheses

The full supplied archive `LM6_POINTS_AS_SECTIONS_final.zip` was retrieved unchanged. Its native Library identity is `libfile_b935f74c96a88191a5b3c3eed913961a`; the source ledger records its hash. It is an AI-produced research return, not a primary mathematical authority. The full A.22 statement and proof discussion are on pp.16–17, TeX lines 1255–1339; the full A.50 statement and proof are on pp.33–34, lines 2854–2958.

A.50 starts with a closed procyclic subgroup `A` of the geometric free profinite group `F`, and a closed subgroup `N` of the arithmetic group which normalizes `A` and has open arithmetic image. It does not require `A ⊂ N`. Its first Sylow step nevertheless uses that containment. The repair sets `N_tilde = NA` and `D_tilde = (N ∩ F)A`. Compactness makes the product closed, normalization makes it a subgroup, and the projection satisfies `p(N_tilde)=p(N)` and `N_tilde ∩ F=D_tilde`. Because `A` centralizes its pro-ell factor, the original conjugation character extends by `theta_tilde(na)=theta(n)`. Restriction recovers the original character. Every original hypothesis is preserved.

The subsequent proof gives a descended power character `lambda` on the open arithmetic image, with exponent `ell−1` for odd ell and exponent 1 for ell=2. The finite-cover detection argument gives either cusp inertia or a line in a Jacobian Tate module. The latter has Frobenius weight one, whereas the cyclotomic character has weight two. Therefore it does not fill the criterion's cyclotomic-action premise. The residual common-kernel subgroup problem in LM6 A.22 retains its OPEN status. Later restrictions, including A.36 and its derived-subgroup statement, were inspected for scope but are not all independently reproved here.

The free-pro-ell nonmetabelian step has an all-prime algebraic certificate: in the units of the noncommutative algebra truncated at degree six, the displayed double commutator has coefficient −1 at `XYYXX`. This exact integral coefficient survives every prime. `audit_next_certificates.py` verifies that coefficient and the full degree-five polynomial, rather than extrapolating from a finite collection of primes.

## Integral forms: arithmetic theorem closed, historical model retained

F.3.12 constructs both directions of the tensor-form classification: a form maps to its right tensor-Isom torsor, and a torsor maps to the objectwise contracted-product functor, with all tensor constraints descended. Gille–Moret-Bailly Proposition 5.1 proves that the resulting fppf torsor set is finite for every affine finite-type group scheme over the S-integers of a number field for a finite set S. Its original proof was read in full; no reductivity, smoothness, or connectedness hypothesis was inserted. For any affine finite-type group over the stated Dedekind ring, an fpqc trivializing section factors through a finitely generated subalgebra of a faithfully flat algebra. That subalgebra is torsion-free, hence flat, and every maximal ideal remains proper, hence it is faithfully flat. Noetherianity gives finite presentation. The resulting fppf section trivializes the torsor by its actual orbit map. Thus the same finiteness covers all fpqc-local forms without a flatness hypothesis on the group.

The lattice interpretation is also explicit: the double coset of an adele `a` maps to `V ∩ a Lambda_hat`, the inverse is obtained by choosing the finitely many nontrivial local lattice identifications, and the integral automorphism group is `G(Q) ∩ a K_f a^(-1)`. Borel's original Theorem 5.1 gives the required finite class set, including disconnected groups.

The unrestricted proalgebraic extension has an explicit counterexample. For finite free modules graded by the direct sum of countably many copies of `Z/2`, the automorphism group is the product of `mu_2`. Each sign sequence defines a tensor constraint. All such constraints become trivial over the single finite free cover `Z[i]`; the tensor square of each homogeneous generator proves that distinct sign sequences cannot be isomorphic over Z. Thus there are infinitely many actual integral forms, even fppf-locally trivial forms.

I.M09.01 remains OPEN only because the particular historical fixed-alpha integral form groupoid and its affine finite-type automorphism model have not been constructed from the inspected pages. The arithmetic finiteness theorem is no longer an unresolved step.

## Historical originals

The full Montpellier cote14 and cote16 scans were downloaded. This does not mean the entire dossiers have been read. Targeted visual reading covered cote14 original pp.43–44, and cote16 original pp.44 and 47; both complete Coates-letter primary-text transcriptions were read.

The 27 August 1965 letter to Serre defines its A on rational cycles modulo algebraic equivalence and its B as primitive middle-dimensional positivity. F.3.5 now gives the exact cycle-class quotient from those groups to cohomological algebraic classes and proves its product and Lefschetz compatibility. This is a dated explicit definition. The particular B and D in the 4 January 1967 Coates letter are still not separately defined in the inspected text. The letter of 6 January 1966 provides the exact inverse-Lefschetz characterization of C and the Cayley–Hamilton inverse construction. The dictionary rows therefore remain documentary gaps with narrower obligations.

The 1967 Coates letter records the withdrawal of the smooth-hypersurface idea and the suggestion to use singular hypersurfaces. Acquiring cote14 does not by itself establish that the suggested later construction was carried out. That construction has not yet been located or checked. None of these standard-conjecture letters dates the particular leaf 18:5 or settles the H4 mysterious-functor chronology.

## Independent checks of root results

The C.1.3 replacement reconstructs the group from Hodge-pair tensor invariants directly. It proves `G=H ∪ fH`, with connected H, by minimality of the Hodge cocharacter, normalization by the rational involution, averaged retractions, and tensor reconstruction. It does not use the older Deligne–Milne arithmetic normality argument. Root reviewed and integrated the replacement.

The G.2.2 arithmetic-specialization proof was independently checked. A finite map of modular curves gives a finite residue-field extension at both a closed point and the generic point; the latter is the case relevant to a transcendental value. The actual nonzero positive-depth coefficient at the point of evaluation makes the specialized E2 polynomial nonconstant. Both directions of algebraicity and the displayed specialization counterexample pass. This is an independent proof check; access to the original Bhowmik–Pathak preprint is recorded by root.

## Reproducibility records

- `audit_next_CHECK_EVENTS.tsv`: 66 addendum rows, using only the six prescribed event types.
- `audit_next_source_checks.csv`: 11 source/access records with locators, paths, and source hashes.
- `audit_next_references.bib`: 9 new bibliography entries, preserving primary-source versus AI-return status.
- `audit_claims.csv`, `audit_claims.md`, `audit_claims_coverage.json`: the full updated 307-assertion inventory.
- `open_rows_review_20261119.csv`: all 43 original open/documentary rows and their current exact gates.
- `audit_next_validation.json`: counts, changed IDs, and event-coverage validation.
- `output/RESEARCH_SA07/code/comparison_counterexamples.py` and its output: updated finite Artin–Tate section certificate.
- `output/RESEARCH_SA07/code/audit_next_certificates.py` and its output: all-prime commutator coefficient and integral tensor constraints.

The direct Serre Galois Cohomology PDF attempt returned only nine front-matter pages. Its theorem text was not obtained from that route; this failure is explicit in the source ledger. The opened primary Gille chapter states the criterion used and its Serre attribution. The root's combined report and event files were not modified by the record builder.
