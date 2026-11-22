# Independent full review of C.3bh

**File:** research/agents/cycles/integral_divisor_classification.tex.
**Reviewer:** GPT-6 Astra (OpenAI), ChatGPT Pro mode; RESEARCH_SA06 /root/frobenius; inherited effort not separately exposed.
**Verdict:** complete mathematical proof and finite-certificate inspection **PASS**.

The statement is exactly the excellent henselian normal coefficient-field scope of C.3z, including its residue-field identification and regular-puncture hypotheses. We freshly reread C.3z's complete statement to check this scope. It makes no mixed-characteristic claim.

For dimension one the source puncture and empty target have zero Picard group. For dimension two the regular noetherian zero-dimensional target is a finite union of field spectra, again with zero Picard group. C.3z supplies all integral surjectivity assertions in dimensions at least four. These exhaust the positive entries.

The two cubics are smooth in the stated characteristics, including characteristic three. The named points P and O are distinct. For odd characteristic, the projective hyperplane x=0 cuts 2P+O and the hyperplane z=0 cuts 3O, yielding div(x/z)=2P−2O. In characteristic two, y=0 cuts 3P and z=0 cuts 3O, yielding div(y/z)=3P−3O. The Abel isomorphism proves nonzero order two and three respectively; no infinite-order point is needed. These points persist over every fixed algebraically closed field, including the algebraic closure of the prime field.

The strict-cone Picard injection is integral. A source pullback which becomes trivial on the puncture is an exceptional divisor line bundle; restricting to E and comparing degree forces its integer coefficient to vanish. The actual family O(Delta−{O}×E) on E×E has endpoint fibres P−O and zero, and its fixed-product pullback supplies ordinary algebraic equivalence. No local-Picard equivalence convention is substituted.

The chosen transverse hyperplane sections factor into three distinct lines in the claimed characteristic ranges. Their punctures are regular zero-dimensional schemes. Thus they supply the dimension-two injectivity failure. In dimension three, the regular strict-local ambient puncture has Picard group zero, while its quartic-free cubic divisor is exactly the preceding strict cone because strict henselization commutes with the quotient. This gives the integral surjectivity failure. The two negative dimension-three entries need not share one pair, and the statement correctly says so.

C.3bg supplies the remaining injectivity failures in every dimension at least three, in every positive characteristic, over the algebraic closure of the prime field. The displayed dimension partition is exhaustive; the isomorphism column follows logically from the two preceding columns. The final distinction from the rational table is accurate.

## Fresh primary input

Opened and read the entire Stacks Project Lemma52.27.5, Tag0F2H, https://stacks.math.columbia.edu/tag/0F2H . Its exact regular-local-ring statement gives zero Picard group on the puncture, without a characteristic restriction. The proof invokes the class-group/divisor comparison and factoriality of regular local rings. Existing C.3x/z/bg source audits are reused, not falsely described as fresh complete primary rereadings.

## Finite certificate

Inspected the entire owner program code/check_integral_divisor_table.py and its complete output/check_integral_divisor_table.json. All seven exact polynomial/point checks are correct. Retained owner run:14:11:07.526597UTC,0.199945221s. No independent program execution is claimed. These identities are supplemental to the mathematical proof, not finite evidence promoted to an all-dimension theorem.

Audit completed 2026-11-19T14:15:31.438862+00:00.
