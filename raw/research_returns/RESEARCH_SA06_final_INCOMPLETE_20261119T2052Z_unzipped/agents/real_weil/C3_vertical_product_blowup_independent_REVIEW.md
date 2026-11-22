# Independent review: vertical-product and point-blow-up tests

**Verdict: PASS for VP.1–VP.2 and BP.1–BP.5 at their exact stated scopes. Auxiliary calculations only; no new main-gate movement.**

Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, run `/root/component_families`; effort setting not separately exposed.

Reviewed the entire file `agents/cycles/notes/Albanese_kernel_product_and_blowup_tests_1938.md`, including the unfinished crossed-boundary discussion and source-scope paragraph. An initial complete read was observed at 19:34:17 UTC; the complete text was reread during final receipt preparation. Current reviewed SHA256: **49b66dd3bcca718176e28b176e7de5bb12bebdaf775bddf4175740a714a14ddd**.

## Product construction

The elementary four-term zero-cycle identity is correct. Summing it for an Albanese-kernel class leaves the two proper curve projections; the curve degree/Abel map makes both projected Chow classes zero. Thus cross differences generate the entire kernel required in VP.1, without asserting a tensor-product presentation for all of CH0.

The fixed class [O_a]−[O_a0] has derived restriction zero at every marked point because its rank is zero. The relative K-fibre long exact sequence supplies the actual relative lift. The normalized diagonal on B×B is perfect, has zero fibre at b0, and has the stated fibres by regular Tor-independent intersection. Their relative exterior product is a fixed smooth proper B-family with exactly the claimed cross-difference endpoint. No extension from an affine parameter is assumed.

VP.2 follows with the exact already-audited rational positive-characteristic closed-union descent square and Adams projector: the relative class maps to the SNC union with zero restriction to the remaining components. The hypothesis that the entire boundary consists of disjoint vertical fibres is essential. This review does not extend the result to crossed boundaries or arbitrary components.

## Blow-up correction condition

For each point blow-up, divisor classes split into pullbacks and exceptional classes. Restriction to an exceptional curve gives degree minus its coefficient, whereas restriction to the strict transform of the old edge contributes that coefficient times the marked point. A plane correction contributes the same c_x to both new edge restrictions. Hence r_S,x=−a_x−c_x and r_T,x=−b_x−c_x, and their difference is b_x−a_x. Combining with equality on the old edge gives precisely

    sum_x (r_S,x−r_T,x)[x]=(M_S−M_T)|C.

The sign, cancellation of the plane parameter and necessity of the old component Picard-image condition all check. A global high section supplies only the sum of its marked points; it does not supply the required individual classes. This is a necessary condition for the proposed component-divisor correction method, not a claim that all possible K0-family corrections fail.

## Audit boundaries

The proof is self-contained at the level of these cycle, relative K-theory and divisor calculations, using the previously audited C.3br/bt descent inputs. The source scopes claimed in the cycles note were read as a ledger; this reviewer did not freshly reopen the Stacks Project proofs or earlier C.3 foundations for this receipt. No numerical program or new theorem on the remaining UK.7 quotient is claimed.

Receipt saved: 2026-11-19T19:43:20.056648+00:00
