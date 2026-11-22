# Independent review: bounded VIII multiplication-integrality audit

Reviewer: `/root/rectangular_and_theta`, GPT-6 Astra Pro. Date: 2026-11-21 UTC; inherited reasoning effort not exposed.

## Target and verdict

I read the complete `agent_viii_multiplication_integrality_audit.md`, initially SHA `e3d0eebc15ba2b79e09f22fc29555cb1ca80e48bc503996882e632107026f41d`, and checked the two corrected page locators in final SHA `d7758f7ac22afad354135e87df51cebba268cdf6270c19c4b3a6ab27eb6f7f11`. **Full mathematical/source-scope PASS.** This is a bounded negative-search result, not a proof of global integrality or absence of denominators.

The only corrections were printed page numbers: Section5's vector convention is p27, and Section5.2 starts on p29, with Figures3--5 on pp35--37. The final report incorporates both. No mathematical assertion changed.

## Exact primary checks

I checked the supplied VIII TeX against the saved original arXiv0709.0751v2 PDF, SHA `504345a1ffd36900ba6166df17cb595f335ba7f15be1fe2739318fa0b7fb80be`, using its actual page text. This was source-text inspection, not a new visual inspection of all tables.

I read the full relevant conjecture and definition passages: Conjecture2.7 with the explicit rational nonnegative coefficient convention, p15; Conjecture3.4, p24; the Section5 vector definition, p27; and Section5.1.2's distinction between ambient expansions and multiplication constants, p29. I matched all thirteen displayed `c(...)` labels in Figure2, p34, to the six formulas. Their multiplicities are 3,1,4,2,1,2. The irregular first gamma label is not repaired or used to infer another constant.

I checked Section5.2's limited one-element ambient computation, the complete Section5.3 introduction on p31 (quadratic coefficient field and monomial-basis roles), the balance expression and its nonmonomial denominators on p33, and the displayed one-half/algebraic coefficients of Figure6 on p38. These examples are correctly distinguished from the raw multiplication formulas being audited.

I read Section5.4.1's actual rescaling and trace/norm instructions, pp48--49, and matched the captions and page locations of Figures24--35. The raw-constant vectors are Figures24--26 and30--32; Figures27 and33 are coefficient-field traces; Figures28--29 and34--35 are coefficient-field norms. The stated normalization exponents are not supplied for individual figures. I also read the complete relevant VII Section7.1 scaling context around the supplied labels `eqscalingP2`, `eqscalingQ2`, and the displayed integral Laurent formula for hat-f-p. The report correctly refuses to identify this with every omitted VIII scaling choice or recover an unprinted raw denominator.

## Exact formulas, counts and proofs

I read the entire `verify_viii_multiplication_integrality.py` and reran it successfully. It confirms the six Laurent expansions and integral coefficients, the thirteen raw labels and the 542 signed integer cells across the twelve specified tables. The raw formulas were manually matched to the actual source; the script's six hard-coded formulas alone would not establish that coverage. I checked the table parsing and inspected the figure captions/source bodies. No unprinted multiplication table was computed.

The primitive-factor argument is correct: `(u-u^-1)^a` is primitive in the integer Laurent UFD. If the exact quotient of an integral raw formula is rational Laurent, Gauss's lemma forces it to be integral Laurent. This does not apply to arbitrary rational rescaling and does not make the omitted original constants Laurent.

I independently reconstructed the grouped-integrality lemma. An uninserted finite Euler trace has integer signed multiplicities after grouping equal nonzero Frobenius roots. Eventual equality with a finite Laurent power sum forces equality of every grouped coefficient by a shifted Vandermonde matrix. For a non-root-of-unity beta each exponent is separate; for finite order only residue-class sums are constrained. The integer-valued sequence `(1+(-1)^n)/2` is a valid example showing why pointwise integrality is insufficient. Jordan blocks do not change these traces. An arbitrary inserted endomorphism is correctly excluded from the premise.

The six integral formulas have the stated finite mixed Tate witnesses under the explicitly chosen normalization `q_src=Q^n`: positive coefficients in cohomological degree zero and negative coefficients in degree one, with twist `E(-j)`. These constructions make no multiplication/action/canonical-label comparison and imply no common pure weight. The finite-spectrum rational-dilation obstruction is only referenced for a genuinely non-Laurent rational function; no audited raw multiplication formula is alleged to supply one.

## Final scope

The report does not claim that the conjecture requires integral coefficients, that every actual source constant is Laurent, that normalized integer tables establish raw integrality, or that ambient/balance coefficients are multiplication constants. It adds no actual fractional-multiplicity counterexample. Its separate Grothendieck paragraph correctly distinguishes rationalized K0 from actual finite objects. No root master file or shared event log was edited.

## Final whole-fragment match, 2026-11-21 05:30 UTC

I read the entire final `finding_F65_integrality_audit.tex`, SHA `a2dcbce72c230034f0e3020584783c3d691fb4cfb9a5cf1d3eef42fbefe862f3`, and reread the complete final report, SHA `8cd13ba244efb01f85cf6ffdae50a935687c030522fd5900bc09c2849a091e9a`. **Whole-fragment/source-report match PASS.** The six formulas and full vectors, thirteen-label and 542-cell scope, corrected printed page locators, exact source-role distinctions, grouped-integrality proof, explicit mixed Tate complexes, and separate F65 dictionary are all retained. No unprinted multiplication constant or omitted normalization exponent is inferred.

The only proof change from the previously reviewed report replaces the Gauss-lemma citation with its short direct denominator argument. I reconstructed it: if the exact rational Laurent quotient is `g/N` with least common positive coefficient denominator N, then `Nf=(u-u^-1)^s g`. For any prime p dividing N, reduction in the domain `F_p[u,u^-1]` forces every coefficient of g to be divisible by p, because `(u-u^-1)^s` remains nonzero, including in characteristic two. Dividing g and N by p contradicts minimality. Thus N=1. This uses only an exact Laurent quotient and does not extend to arbitrary rational-function normalization.

The fragment's actual witness `E(-j)[-1]` has cohomology in degree one, giving the required negative Euler sign. The shifted Vandermonde comparison needs only eventual equality and invertible Frobenius; it makes no semisimplicity or weight assumption. All action, canonical-label, purity, and bounded-search limitations survived the final text. No mathematical correction is needed.
