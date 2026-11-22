# Independent full review: F65 joint source normalization

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited effort is not exposed. Date: 2026-11-21 UTC.

## Verdict and exact target

**PASS after the explicit proper-point scope refinement.**

Final report: agent_joint_normalization_gate.md, SHA256 7a97eee4d519d31ae3759dd28f2e679e5377b715df221af239bd1edb4fa1b006.

I read the entire original report at426ea91f..., read the whole expanded mathematical/source/dictionary body atd2f553eb..., and independently reconstructed both joint propositions and the isolated escape. The sole final delta restricts the proper-pushforward corollary to proper structure morphisms to the finite-field point and records the exact BBD dual-stability argument. That delta has been read and checked. Generated-fragment review is separate and has not yet occurred.

This review is a mathematical and primary-source-context check. It does not claim a fresh visual reading of the rendered source PDFs; the exact supplied original TeX contexts were read. The original local BBD context was also reread. The accompanying symbolic script was read and rerun, but it is not the proof of the arithmetic conclusions.

## 1. Source normalization and two coefficient types

I independently read IV's complete Hecke convention paragraph and the following Kazhdan--Lusztig parameter comparison, and VIII's complete Section3 convention following the Wedderburn display. IV uses (T-u)(T+u^-1)=0 and explicitly matches u to the quantum-group parameter; its conventional KL parameter has square root u. VIII's right-hand section explicitly replaces the earlier quantum parameter by the square root of its right-hand q. The equation q_src=u squared is therefore correctly stated for the corresponding example. It is a formal parameter comparison, not an arithmetic weight assignment.

I read the actual four scalar definitions in VIII Section5.1 and checked their comparison with D and (D-2) squared. The identities for b1,b2,c1,c2 match the genuine rank-three degree-five relation. The printed repeated b1 is not being silently repaired or used to distinguish ambiguous basis families.

The transition table has the raw entry h=4(q^1/2+q^-1/2), and the multiplication table has the exact entries

- c=-(q squared+q+1)(q-1) squared/q squared = -q squared+q+q^-1-q^-2;
- d=(1+q) squared/q = q+2+q^-1.

The exact source lines for both multiplication triples were reread. The surrounding VIII positivity passage is signed/factored and does not assert unsigned effectivity of every raw multiplication constant.

The final report correctly records the source's W/V column-label inconsistency: the caption discusses W1,W2 while the following prose names columns belonging to V1 in the preceding cell list. The result uses the raw h entry and its ambient-transition role, not an invented resolution of those labels. Proposition JN-B avoids that cross-table issue entirely.

## 2. Finite power sums and purity

For distinct nonzero roots, an eventual relation is determined by taking consecutive indices, yielding a Vandermonde matrix multiplied by an invertible diagonal matrix. Thus every visible root and its grouped Euler multiplicity is fixed.

For an integral-weight mixed complex, hidden cancellation can remove a root but cannot create a new visible root absent from its cohomology. The report correctly uses only integer-weight necessity in the mixed hypothesis.

For a pure point complex of weight w, an eigenvalue of point weight m can occur only in degree m-w. This is precisely the smooth/lisse clause of BBD5.1.8 on a point. Consequently it cannot cancel between opposite parities. The Euler sign at that root is fixed, and Jordan blocks contribute ordinary dimensions just as stated. No arithmetic semisimplicity is required.

## 3. JN-A: transition integrality plus multiplication purity

Under q_src=Q^(an), the two visible h roots are Q^(a/2) and Q^(-a/2), with point weights a and -a. A bounded ordinary mixed integral-weight realization therefore forces a to be an integer.

The four visible c roots then have weights 4a,2a,-2a,-4a, all even. For any one pure complex weight, their possible degrees have the same parity. Their required multiplicities have signs -,+,+,-, which is impossible. All roots remain distinct for negative as well as positive nonzero a. The excluded a=0 degeneration is correctly separated.

The two complexes need not share a weight or operation. The required common parameter rule and both scalar trace identifications are explicit extra assumptions. The result is not attributed as a stated source conjecture about these two different tables.

## 4. JN-B: two multiplication constants alone

For the positive constant d, the visible root1 has weight zero and positive multiplicity2. It forces the pure complex weight w_d to be even. The other visible roots have point weights 2a and -2a and positive multiplicity1. Their allowed degrees must both be even integers. Since w_d is even, 2a is an even integer, hence a is an integer.

The previous c contradiction now applies. This proof is valid even if the two pure complexes have different pure weights. It does not use transition coefficients, canonical-label choices or an ambient-basis hypothesis.

This is a precise obstruction to jointly realizing these two raw constants as pure point Euler traces. It does not refute the source's signed/factored positivity, nor does it exclude mixed constructions or a different specified trace normalization.

## 5. The genuine isolated half-step escape

At a=1/2 the proposed c complex is

L_2[-1] direct sum L_1 direct sum L_-1[2] direct sum L_-2[3].

Its point weights are 2,1,-1,-2 and its cohomological degrees are 1,0,-2,-3. The difference weight minus degree is one in every summand. Its Euler coefficients are therefore -,+,+,-, exactly c(Q^(n/2)). All eigenvalues are ell-adic units, so the chosen finite arithmetic lines extend continuously to point Galois representations. No geometric half-Tate object is asserted.

With the same parameter rule, h would require roots of weights one-half and minus one-half, outside the explicit integral mixed-weight hypothesis. The second multiplication constant d is also not pure: its constant root requires an even complex weight, while its two outer roots of weights ±1 require an odd one. Thus the single c escape is real but does not evade either joint theorem.

The change q_src=u squared makes this isolated normalization u=Q^(n/4), which is correctly distinguished from the prior u=Q^(n/2), q_src=Q^n normalization.

## 6. Necessary proper-pushforward scope correction

I requested a real qualification in the corollary. A pure complex obtained by proper pushforward to a positive-dimensional base need not have pure point stalks. Thus properness alone cannot justify applying this point-complex theorem to arbitrary extracted stalk coefficients.

The final report now requires proper structure morphisms X to Spec F_Q, with X of finite type, or a separately proved pure-point extraction. For those point targets, BBD5.1.13-14, p128, gives both weight inequalities: compact pushforward preserves the upper bound, its dual preserves the lower bound, and properness identifies f_! with f_*. The pushforward is therefore pure as the needed point complex. This final scope and source refinement is correct.

The complete original BBD5.1.13-14 context was reread, not inferred from a secondary paraphrase.

## 7. Exact script and dictionary

Script verify_joint_normalization_gate.py, SHA256 c92c4402289105e518bf57b64b76a75066f2c0b1a4373220f421a58fdde93bd5, was read and rerun successfully. It checks the four presentation identities, the two multiplication-coefficient expansions and the four isolated pure-complex degree signs. The report itself supplies the Vandermonde, integrality and parity proofs; the script does not purport to test them numerically.

The dictionary correctly separates a formal torus grading from an assigned Frobenius weight and distinguishes the coefficient tables. EGA/SGA representation and perfect-complex anchors do not supply the additional trace comparison. The exact BBD point-purity convention is applied in its actual setting. No lambda-ring on a noncommutative word algebra, canonical projector, source lattice or perverse coefficient category is inferred from these scalar calculations.

No further mathematical correction is required. Final-fragment match remains pending until the author generates that fragment.

## 8. Complete final-fragment match

I read all 257 lines of finding_F65_joint_normalization.tex, SHA256 be6d20e6081ad2bd55a55a951a94d6255adc69275021a96ea7b1ddbbf645bb18, and matched the complete proof and separate dictionary to the final reviewed report.

**Final-fragment PASS.** It retains the source convention and presentation identities, exact three coefficients and source column-label caveat, both complete joint proofs, eventual-equality and Jordan scope, the genuine isolated pure complex with all four correct shifts, and the precise proper-structure-morphism restriction. No purity of arbitrary stalks or unprovided canonical-label comparison is inferred. No new mathematical claim appears beyond the reviewed report. This remains a proof/text match, not a fresh syntax or visual audit.

Final typography-only delta: the author replaced literal section signs on seven lines by the equivalent LaTeX section commands to avoid an unavailable text font. The affected locator lines were inspected; their mathematical and bibliographic content is unchanged. Final fragment SHA256 3c6049c38bb1ad080e9c7448b0fcde131635e82fbf77a37c7c6aa8810fc56b41. This exact delta also passes. The author's separate successful three-page syntax compile is reported by the author, not claimed as a new compile by this reviewer.
