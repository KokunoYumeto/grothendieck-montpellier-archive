# Final accepted-claim and scope audit

Date: 2026-11-21. Checker: `/root/bounded_specialization`, GPT-6 Astra Pro; inherited effort not separately observable. This is a mathematical and editorial audit, not formal verification.

## Result

No additional substantive mathematical gate was identified in the accepted statements. Every displayed theorem, proposition, lemma, and corollary in the assembled section files has an explicit proof. Source theorems and accepted 2026 inputs remain identified as inputs rather than being counted as new proofs. The new W04 result closes the auxiliary **complex** exact-minimum question once its section and status records are integrated.

The following scopes must remain explicit in the final package.

1. B01–B06 use **integral effective numerator cycles**, with multiplicities counted in degree. Prescribing a multiplier while allowing rational numerator cycles is a different and false statement; the counterexample is retained. Fixed-degree boundedness already forces a multiplier bound, so a separate hypothesis on denominators is unnecessary in the corrected setting.
2. The simultaneous arithmetic conclusions use an actual global cycle and compatible realizations. The fixed-ell lower bound and actual-cycle upper bound are distinguished. No integral comparison at the residue characteristic is inferred solely from a prime-to-characteristic equality.
3. The exact value 16 at every geometric good reduction is established for `t_star` and the primitive `t0`, with their specified action and polarization. W04 establishes exact 24 for `w` over the complex numbers and, by B03, outside finitely many good places. It does not establish exact 24 at every exceptional good place.
4. The uniform-family theorems fix the polarization lattice and rational flat vector, with denominator and norm charged. They do not give a bound depending only on the prime or self-intersection norm. The fixed-norm counterexample remains relevant.
5. R43 requires an exact Betti cocycle together with an explicit semialgebraic marking. An unnamed Betti basis or a numerical period is insufficient. R45 concerns the fibers of the specified good-reduction model and retains its theorem inputs, explicit polarization/lattice data, and marked geometric places.
6. R44 computes a valid exceptional integer, not a minimal one. R30–R31 use that computed integer; prime distribution is not a substitute for the geometric degree bound.
7. The framework map distinguishes homological equality from algebraic equivalence. Historical Grothendieck passages do not supply the numerical constants or effective-cycle preservation statements proved here. The Milne sign correction is separate from any Grothendieck transcription correction.
8. W04 is a computer-assisted finite proof using the proved exhaustive geometric reduction. Its exact-integer certificate and complete output are included. No formal proof assistant or independently rebuilt certificate for the cited deep inputs is claimed.

## Proof/check coverage inspected

The accepted findings in `QUESTIONS.tsv` map to the proof sections B01–B06, C01–C07/C18, P02–P14, V01–V07, R10–R13/R20–R24, R30–R31, R40–R45, and W01–W04. The main source-audit and framework sections preserve the source-dependent scope of C15–C16. The research directory has detailed proof checks for the new bounded-specialization, uniform-family, primitive-minimum, algorithmic, and small-surface results. Root and other agents have separate recorded readings; a group-ID event is not silently interpreted as a new execution by this checker.

For W01–W04 my whole-proof and code-scope checks are recorded in `small_surface_and_w_search_events.tsv`. For R42–R45 my events are in `effective_minimum_events.tsv`; additional R43 independent topology readings are recorded by the other agents. V07 has its own exact hand-proof event in `primitive_and_grh_events.tsv`. The master event file needs to include these latest per-agent rows before final delivery.

## Integration items observed and reported to root

At the time of this audit the main `GHOSTS.tex` did not yet input `sections/w_exact_minimum.tex`, and its final gate paragraph, `README.md`, and `QUESTIONS.tsv` still described `w` as unresolved. The opening of `small_surface_reduction.tex` also used the word “unresolved.” These are stale status descriptions, not mathematical gaps. Root was notified to integrate W04 and update the current status while retaining the historical ledger entries as history.

The final abstract should state the difference between the all-good-prime exact-16 results and the complex exact-24 result. The general algorithm should retain the explicit-input qualification. No out-of-scope classification of the exceptional reductions of `w` is needed to make the presently accepted theorem statements complete.
