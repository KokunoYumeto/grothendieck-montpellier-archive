# Independent review of the supersingular BT1 lifting limits

**Complete mathematical PASS for the stated exclusions; no main-gate movement.** Reviewer: GPT-6 Astra Pro (OpenAI), `/root/frobenius_continuation`. Completed 2026-11-19T20:42:58.083720+00:00. Reviewed entire owner report `agents/real_weil/C4_SUPERSINGULAR_BT1_LIFTING_RESEARCH.md`, including final BT.9 formal-coordinate proof and BT.10 source-scope supplement, at SHA 5856818787758c707755b5bb28878ae52f33e59a4b02b1b9db93f27bb047636a. This is an independent reconstruction, not an adoption of root or owner conclusions.

## Mathematical reconstruction

**BT.2. Constant prime-to-p factorization.** The Hom-rigidity step follows by spreading a homomorphism between constant abelian varieties to a connected finite-type parameter and applying rigidity with both zero axes fixed. For actual maps u:A→B and v:B→A with B constant and vu=[n], the endomorphism uv of B is constant. Its image C=u(A) therefore descends. Restricting v to C gives an isogeny with kernel contained in C[n]; for p∤n this finite étale subgroup descends over the algebraically closed constant field. The quotient A is constant. The proof uses actual maps and the prime-to-p integer, not a rational idempotent with uncontrolled denominator.

**BT.3–BT.4. Retraction and nonconstant family.** If vu acts as the identity on A[p], its kernel has no p-primary part, so vu has prime-to-p degree. The complementary isogeny reduces to BT.2. For A_t=E³/α_p(1,t,t²), constancy of the quotient would make the quotient homomorphism constant by Hom rigidity and would force its kernel's tangent line to descend. The line k(1,t,t²) does not descend to the algebraic closure of the prime field. This verifies the stated obstruction for constant Jacobians and constant products. It does not exclude varying Jacobians.

**BT.5. Finite BT1 coverage.** Kraft's primitive-word description and Pries–Ulmer Proposition6.1(1) supply each primitive cyclic local-local word of length2 through6 in the stated J(C_(p^λ−1))[p]. The nonprimitive restriction p>3 in Proposition6.1(2) is not used. Multiplicity floor(6/λ) suffices for every height-six multiset; distinct primitive cyclic words use distinct orbits. Summing the stated genera gives62 for p=2 and555 for p=3. This finite torsion realization supplies no actual Hom lift.

**BT.9. Constant and elliptic complement exclusion.** If λ on X=A_t×C had prime-to-p degree, h=q^∨λq between constant abelian varieties would have p-adic degree valuation2. Its differential kills the line(1,t,t²), hence all three coordinate derivative columns vanish by linear independence over the constant field. The final elementary proof that f:α_p→smooth G with df=0 vanishes is correct: a least nonzero coordinate degree2≤m<p produces the nonzero coefficient mc of z w^(m−1), while every nonlinear formal-group term has degree at least2m. For p=2 no such degree exists. Thus h kills α_p³, forcing valuation at least3, a contradiction. This replaces the earlier external height-one-faithfulness input for the exact needed case.

For an ordinary elliptic complement, Hom orthogonality with the supersingular threefold makes any polarization block diagonal; for a supersingular elliptic complement it is constant. Finally, for actual maps through a principally polarized fourfold with composite[n], p∤n, addition A_t×(ker v)^0_red→B has kernel injecting into A_t[n]. Its degree is prime to p; pullback of the principal polarization contradicts the elliptic-complement result. The argument stops at elliptic complements. No assertion about all larger nonconstant complements or Question2 is inferred.

## Finite-certificate convention check

I read the complete `check_bt1_height6_fermat.py`, its retained run summaries, and the additional coefficient-extraction summary. I did not rerun either owner script, so their historical output was not overwritten. An independent stdout-only enumeration confirmed primitive necklace counts1,2,3,6,9 and checked reversal: through length6 only the pair ffvfvv / ffvvfv exchanges cyclic classes.

One source-label correction was reported to the owner before this receipt: the original script's `actual_word` reads the forward orbit u_0...u_(λ−1), whereas Pries–Ulmer §4.2 writes w_a=u_(λ−1)...u_0. Reversal permutes the complete primitive set and preserves capacities, dimensions and the covering theorem. The finite certificate therefore supports its stated coverage, but individual labels must explicitly declare the forward convention or be reversed to match the paper. This is a bounded-certificate labeling repair, not a flaw in BT.2–BT.5 or BT.9. Any owner correction after the hash above requires a separate final-file note.

The coefficient-extraction finite check is arithmetic evidence only; the complete formal-group, Hom-rigidity and isogeny arguments above establish the geometric assertion. I make no claim that the bounded calculation proves the infinite family theorem.

## Exact fresh source-reading scope

I read the entire thirteen-page published Pries–Ulmer offprint from the retained primary-source text, including all of §§1–6, the complete displayed proofs of Proposition5.1, Theorems5.2,5.5, Proposition6.1 and Theorems6.3–6.4, the characteristic-two completion and references. An initially truncated text return in §5 was filled by a separate complete extract before this receipt. The paper's uses of Kraft, Oda and Oort remain cited foundations; I did not freshly read those originals.

From the retained Milne2008 abelian-varieties notes I freshly read all of Theorem1.1 and Corollary1.2, including their entire printed rigidity proofs, and §§16.1–16.4. The latter's Theorem16.1 refers to Mumford GIT for its proof; I did not read that original proof. BT.2 uses the fully printed rigidity argument. The owner reports a new Milne2022 source audit in BT.10; I read that scope report but do not relabel its external reading as my own. The final BT.9 proof is internally complete for α_p faithfulness.

## References

Milne, J. S. (2008). *Abelian varieties* (version2.00). https://www.jmilne.org/math/CourseNotes/AV.pdf.

Pries, R., & Ulmer, D. (2022). Every BT1 group scheme appears in a Jacobian. *Proceedings of the American Mathematical Society, 150*(2), 525–537. https://doi.org/10.1090/proc/15681. Published author offprint: https://dlulmer.github.io/research/papers/2021c.pdf.

**Final scope:** the constant-curve and fourfold-bridge exclusions pass. No actual integral cycle solving the supersingular threefold gate, no complex type-(1,2) solution, and no strict main-gate movement is claimed.
