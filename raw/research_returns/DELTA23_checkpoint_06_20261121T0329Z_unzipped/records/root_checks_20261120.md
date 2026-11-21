# Root proof checks, 20 November 2026 UTC

Model: GPT-6 Astra Pro. Effort: inherited, setting not exposed. Run DELTA23.

## 23:18 — D23.P1–P2

Read the entire proof in `work/agents/pentagon/four_point_central_flips.tex`.
Independently checked the geometric forgetting argument: every distinct
four-subset omits a labelled puncture of the support, which kills an inner
commutator. On the surviving four-punctured sphere the first and last pair
curves are complementary and isotopic. The finite quotient's second derived
group is central of order two; change of marking fixes its unique nonidentity
element. Products of the constructed words therefore give every tuple.
Normality of the simultaneous congruence kernel makes the full group's action
on these coordinates just the label permutation, proving the orbit claim.
The cubic sign changes under minus identity; the harmonic exponent changes by
two and its parity stays fixed. No actual GT element is asserted.

Reran `check_four_point_central_flips.py`: generated group order 24, derived
order 8, second derived order 2, and displayed word minus identity. PASS.
This run checks only the finite algebra; the whole-proof reading above checks
the stated geometric and profinite reasoning.

## D23.F1–F5 — completed whole-proof review

Read both whole files and the added split completion argument. The configuration-space splitting, finitely generated free-kernel completion argument, pure centralizer induction, monodromy marking and arithmetic path conventions pass. Completed checks are recorded in CHECK_EVENTS.tsv.

## 23:40 UTC — further completed checks

Read and checked the complete proofs of P6, F9, F10, F12, F13, C9 and C10. F12 explicitly depends on the supplied universal normal-subgroup version of E.58; the absent D.50 proof was not checked. F9 now fixes the periodic-braid sign by an explicit angular isotopy, which removes the requested marking gap. Reran the P6 affine intertwiner, F13 exhaustive46656-element matrix enumeration, and C9 six-dimensional intertwiners. Bigelow section4.2 primary formula was opened and compared. Exact scope is in the event rows.
