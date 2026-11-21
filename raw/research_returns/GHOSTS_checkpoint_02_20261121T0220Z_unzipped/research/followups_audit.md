# Milne and van Hoften--Sempliner followup audit

2026-11-21. GHOSTS `/root/cm_transport`; GPT-6 Astra Pro, inherited effort not separately exposed.

## C15. Milne's report: exact scope and one sign correction

Read the attached report, *On the Hodge, Tate, and standard conjectures for abelian varieties*, hexagon:2611.00244v1, dated 9 November 2026, §§1.1--1.12 and §§2.1--2.5, and the concluding standard-conjecture discussion §§3.5--3.12. The report presents the rationality theorem and CM Hodge theorem as the two separate inputs. Its §2.3 expressly does not claim that CM Hodge is already known to imply Hodge for all abelian varieties. Its lifting discussion §1.9 cites Kisin--Zhou Theorem2.2.7 and is contextual; it does not replace the precise data and normalization of OpenAI [32], Corollaries3.4/6.4. Its standard-conjecture consequence gives a positive form on appropriate primitive algebraic classes, not an effective-cycle degree estimate for arbitrary surface representatives.

**Source correction, not a transcription correction.** In §3.6, printed and PDF p.8, the displayed primitive pairing is written as

    (a,b) ↦ a·b·xi^(g-2r)

and called positive definite. With the usual intersection normalization it requires the factor (-1)^r. A direct counterexample to the unsigned display is A=E×E, xi=theta_1+theta_2 and a=theta_1-theta_2: a·xi=0 but a^2=-2. The corrected form is

    (a,b) ↦ (-1)^r a·b·xi^(g-2r).

The original PDF p.8 was re-extracted and visually rendered and inspected; the sign is genuinely absent from the printed display. This does not refute Theorem3.5 or the cited standard-conjecture result, and it does not affect codimension two, where (-1)^r=1. It must not be put in the Grothendieck transcription ledger.

## C16. van Hoften--Sempliner: algebraicity, not quantified cycle construction

Read the attached hexagon:2610.00259v2, *The Hodge conjecture for CM abelian varieties*, Introduction §§1.1--1.4; Theorem2.3.4 and its complete proof, printed pp.7--8; Theorem4.0.2, p.12; and the complete proof subsection4.2.8, including Lemmas4.2.9--4.2.10, pp.19--22. TheoremI is used as a task input, not independently reproved here.

Theorem2.3.4 first clears rational Hodge morphisms by unspecified integers m_i, maps a surface into the product B_i, and obtains a cycle pairing nontrivially with a one-dimensional eigenspace. It then applies algebraic Chow--Kunneth and CM projectors and the perfect pairing on algebraic classes supplied by numerical=homological equivalence. This is a correct qualitative passage from one nonzero surface period to algebraicity of the eigenspace, given its cited inputs. Its dual-cycle selection does not state an integral height or degree bound.

Theorem4.0.2 asserts existence of a compact open level and four Hodge morphisms with nonzero cup product. In its proof, Lemma4.2.9 uses real approximation to choose a rational isometry near a real splitting isometry; Lemma4.2.7 then supplies a finite Schwartz test function, and the concluding finite-character decomposition selects nonvanishing summands. The passages read give no numerical bound for the rational isometry denominators, chosen level, m_i, or degrees of the resulting dual algebraic cycles. Thus this followup supports the CM algebraicity input but does not close a quantitative T9 gate on its own.

The authors' §1.3 explicitly describes their argument as a variant inspired by the OpenAI paper and does not claim a line-by-line verification of that paper. This is a statement about the scope of the supplied source, not an authentication objection.

## Actual check events

| statement | type | outcome | exact locator |
|---|---|---|---|
| C15-MILNE-SCOPE | used and rechecked in this run | Report's separation of rationality, CM Hodge, and consequences checked; no quantitative bound imported | §§1.1--1.12,2.1--2.5,3.5--3.12 |
| C15-MILNE-SIGN | targeted proof check | Unsigned display is false for odd codimension; corrected by (-1)^r, explicit E×E counterexample; theorem unaffected | §3.6, printed/PDF p.8; rendered image visually checked |
| C16-VHS-2.3.4 | targeted proof check | Complete short algebraicity argument read; valid given cited projector and equivalence inputs; no effective degree conclusion supplied | printed pp.7--8 |
| C16-VHS-4.0.2 | used and rechecked in this run | Statement and proof subsection4.2.8 read for quantitative scope; underlying deep theta/Siegel--Weil inputs not independently reproved | printed pp.12,19--22 |

All events: 2026-11-21, GPT-6 Astra Pro, inherited effort not exposed, GHOSTS `/root/cm_transport`. No formal verification claim.
