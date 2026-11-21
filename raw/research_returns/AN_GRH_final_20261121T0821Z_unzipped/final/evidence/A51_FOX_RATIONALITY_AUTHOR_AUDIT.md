# A51 algebra supplement: author whole-proof audit

Date: 2026-11-21.

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source: `A51_FOX_RATIONALITY_SUPPLEMENT.tex`.

SHA256: `ef80c2a2f4e124d439d529d385639ab640c40bece4c910ccdb605f429bfd985c`.

Bibliography: `A51_FOX_RATIONALITY_BIB.tex`, SHA256 `6de7e27405d7a623ba3aba26e12accf33a9dd38a6b01b414bee4c1a93d110969`.

## Verdict

**PASS: complete author proof and scope read.** I read all three parts and the complete bibliography after drafting. I then checked the explicit trivial-conductor convention, the corrected displayed exponent, and the added integral-source caveat. This is an author read, not a separate independent re-proof. I have not completed an independent whole reading of the separate main A51 manuscript by row_audit.

## Proof checks

The compatible averages in (FX.2) evaluate as asserted on every finite-level character. Their differences isolate exact conductors and give a finite sum at each quotient level. The chosen unit 1-B defines an actual automorphism. In the semilinear case, u preserves the conductor projectors and acts on each primitive character with the stated common orbit length. The additive cokernel of 1-c times the cyclic permutation has the single relation 1-c^d after basis elimination. The valuation formula follows by the stated binomial argument for b at least two, including p=2. Finite unramified coefficient extension detects the same elementary-divisor exponents. The construction is explicitly abstract and does not claim Weil weights, polarization, Jacobian realization, or an actual point-section collision.

The rational-function proof correctly separates uniformizer content from primitive numerator and denominator. Prime-to-p roots retain exact order after reduction, their minimal polynomial degrees over the fixed residue field tend to infinity, and those degrees eventually exceed both reduced-polynomial degrees. This proves eventual constant valuation at every primitive root of a high level. A fixed integral evaluated matrix has exponent bounded by its determinant valuation through Smith invariants. Connecting these cokernels to actual primitive rational groups is an additional hypothesis; the supplement does not assert it. The A47 consequence is conditional and restricted to the stated genus-two characteristic-two setting.

## Source issue checked directly

After the initial Asvin scope review, the effective-Galois reader noticed the integral premise in printed Lemma11. I opened and read the complete retained Lemmas11 and12. The claim about the natural image in Lemma11 fails for multiplication by ell on an elliptic curve: pullback on integral H1 and the induced Tate map are both multiplication by ell on a rank-two free Z_ell module, with cokernel (Z/ell)^2. Surjectivity of the abelian-variety isogeny does not imply surjectivity on its integral Tate module. The supplement now reports the finite-matrix description as the paper's statement and does not use that geometric integral premise. No conclusion about a repaired rational-coefficient theorem or the entire paper is claimed.

The complete independent algebra arguments (FX.1)–(FX.9) and the coefficient-prime limitation in abstract Section3 do not depend on the faulty integral inference. The earlier note at SHA9007417e remains unchanged as an exact historical review snapshot; the present supplement contains the subsequent qualification.

## Primary scope and limits

The companion source manifest retains the five primary PDFs and extracted text, exact hashes, URLs, reference IDs and precise reading scopes. The source paragraph distinguishes full profinite presentation, completed arithmetic Fox coefficients, tower-prime congruences, and the actual fixed rational Fourier function required by Sinnott. The full proofs of the general finite-presentation theorem and Asvin's long congruence theorems were not independently audited.

No new finite arithmetic computation, actual curve enumeration, infinite geometric tower construction, or universal primitive-factor supply theorem was performed. This supplement records a completed attempted route with a precise missing hypothesis. It is not main-gate movement and has no separate finding number.

## Final citation-scope delta

Final source SHA256: `5d23ca9743c256c0226e6c37382bf9edd15fcea75b24beaba5b69db1f83a4fa7`.

After the complete reading above, the parent requested one exact-source wording correction: the general printed Lemma11 inference is from a **surjective map of abelian varieties**, which need not be an isogeny when the genera differ. The source replaced only “from an isogeny” with that wording (and reflowed the next line). I checked the precise delta against the printed proof. The explicit elliptic isogeny counterexample and all mathematics are unchanged. This is a targeted citation-scope delta check in addition to the earlier complete proof reading.
