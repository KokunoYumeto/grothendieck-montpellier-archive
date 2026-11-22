# Full fpqc solution for the henselized candidate

Status at 2026-11-19T15:53:58Z: proved, subject only to normal integration and build checks.

The complete numbered proof is in `sections/A_finish_fpqc_solution.tex`. It closes the last exact gate for P(R)=alpha_p(R^h_(t)) and proves the counterexample to the main criterion with original condition4, actual condition7, and locally finite-type tests in8. The stronger adic condition4 still fails for P; L2 is settled by the separate H example.

## Proof architecture

1. A normalized tensor e for an integral element b is captured in a finitely presented A-module with a monic-polynomial operator. Finitely many relations kill the tensor's error; B_b is then a direct summand after flat base change.
2. Over strictly henselian local A, finite modules with one operator split into finitely many summands with local endomorphism rings. The proof lifts idempotents by a minimal-generator matrix and henselian factorization of its characteristic polynomial. No finiteness of End_A[T](M) is assumed.
3. Finite presentation makes the endomorphism ring commute with flat base change by a finite Hom kernel and a commutator kernel. The residue division algebra is a finite purely inseparable field, so every local residue extension preserves locality.
4. A finite exchange argument selects the rank-one summand; faithful flatness descends its single generator and scalar operator. Therefore an integral individual separable element of a flat local algebra over a strictly henselian local base lies in that base.
5. For the P cocycle, the exact henselization kernel is killed by 1+tc; multiplication normalizes it to e. Localize the henselized cover at a prime over the closed point, apply the local theorem, and propagate equality back to the whole cover using the faithfully flat map into the henselization of its overlap with that localization.
6. Over an arbitrary base, strict henselizations provide descended sections. Finitarity spreads both section and its matching equality to pointed finite-presentation etale neighborhoods. Separatedness glues the sections.

## Exact sources and scope

Opened Stacks04GG, Lemma10.153.3(3)-(4) and(10); Stacks074X, Proposition11.8.5 and Lemma11.8.6(4); Stacks09XI, Lemma15.11.6(3); and Stacks0EM7, Lemmas15.12.1-2. Full proof of the new combined statement is given in the paper, rather than attributed to these ingredients. Earlier searches on separable elements, locally strongly separable subalgebras, module endomorphism rings, equivariant Lazard, weakly etale envelopes and henselian fpqc descent were recorded in B_finish_A_fpqc.md and B_finish_A_envelopes.md. Root additionally found Siddoway1990, On endomorphism rings of modules over henselian rings, DOI10.1080/00927879008823967, but only publisher metadata was opened; it is not used as support for the full theorem. No novelty or priority claim is made.

## Audits

Root read the entire written proof and reported PASS. Descent_groups read the entire written proof and reported PASS; its six direct audit records are in checks_A_solution_audit.tsv. Representations independently audited the local algebra chain and supplied the primary division-algebra source. The root audit and own used/rechecked records are in checks_A_solution.tsv. Fixes after audit: restored a missing TeX backslash before quad, changed all rings to all base rings to permit noncommutative endomorphism algebras, and corrected three etale accents.

No finite exhaustive computation is appropriate for this arbitrary-ring theorem, and none is claimed.
