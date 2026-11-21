# Independent audit of the actual cubic triangular obstruction

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro. 21 November2026.

Object: `work/cubic_uppertriangular_bridge.md`, entire saved text read and reconstructed. Verdict: **PASS for the algebraic construction and its stated scope.** No arithmetic Triple-NV assertion is certified.

## Reconstructed argument

1. The degree-two module is the actual extension of the finite torsion module by the completed exterior square of the free quotient. If a polynomial q annihilates its torsion quotient, q(D)y lies in the exterior-square term. An eigenfunctional n of eigenvalue t consequently extends by n(q(D)y)/q(t), provided q(t) is invertible. On the generic triple divisor, both proper pair products remain nonconstant, so their annihilator values are nonzero. An equivariant difference factors through the annihilated torsion module and is therefore zero. This proves existence, uniqueness, and annihilator independence of UT.1.

2. The central functional UT.2 is the e14 coefficient of the matrix commutator. Its compatibility on the exterior square is immediate, and Jacobi follows from the matrix Lie algebra. It therefore descends to the actual W3. Both mixed [Q,Tplus] contributions are retained. Multiplying the three eigenvalues gives alpha; adding the three Delta characters gives the specified odd character.

3. The free resolution R --q--> R of R/(q) computes Ext1(R/(q),K_alpha) as K/q(alpha)K. The extension class is the image of its actual relation q(D)y. When alpha is any root, this is K; the calculation does not require a simple root. Changing the lift adds q(alpha) times a scalar. Thus the scalar is the actual substituted cubic residue, and its nonzero value is equivalent to nonsplitting of the stated pushout.

4. The rational free Q quotient introduces no further module extension obstruction: choose lifts of its finite R-basis. The correction has degree three, so it does not change brackets through degree three. This is an algebraic statement about the specified weighted Lie quotient. It does not assume a localization theorem for continuous group cohomology.

5. The cyclotomic multiplier argument is correct. For a nontrivial even theta, Hasse's unit-index formula gives full rational rank of the corresponding cyclotomic-unit line; at trivial theta the norm of 1-zeta is p. The Kummer classes are nonzero. The inflation kernel from Gamma has odd cyclotomic Delta character and therefore cannot kill an even class. The previously checked norm-transfer map kills Iwasawa torsion and is nonzero on the relevant free rank-one quotient. Its three one-variable multipliers remain nonzero on the generic triple divisor, including the third variable after the stated invertible formal change of variables.

## Primary checks actually performed

Sharifi's complete Iwasawa notes, local `work/sharifi_full_iwasawa.pdf/.txt`: Theorem4.3.3 and its whole proof, printed pp108–109; Proposition6.1.5 and its whole proof, p152. These were read afresh in this audit. The rational nonzero multiplier needs only the finite-index statement, not Vandiver or an integral unit-index assertion.

LLSWW, `work/higher_reciprocity/lam_liu_sharifi_wake_wang_augmentation.pdf/.txt`: Definitions3.3.1–3.3.2, Lemma3.3.3 and Theorem3.3.4 with their whole proofs, printed pp24–27, were read afresh for source matching. Their matrix calculation is applicable as a model, but the statement uses untwisted outer characters. The present universal Gamma characters require the corresponding twisted Borel calculation; see the companion denominator note.

Follow-up source clarification: the entire §§3.1–3.2, pp21–23, were also read. Their general UGMA definition already allows all three coefficient twists. The restriction applies to the later Bockstein comparison, not to the definition of a specified Massey value.

## Precision points retained

- UT.1 gives a Lie coordinate. After exponentiating, the pair group coordinate includes the half-product of the two first coordinates. Defining the group map through exp avoids losing that term.
- A common power of p can also absorb the fixed class-three exponential/BCH denominators. This matters at p=3 but is harmless after rationalization.
- This audit does not assert that continuous cohomology commutes with a function-field localization, or that an untwisted source theorem proves a twisted statement verbatim.
- The nonzero cyclotomic multipliers remove a possible defect in the inputs. They do not make the central extension nonzero.

The full source audit and precise remaining arithmetic support condition are in `work/higher_reciprocity/triple_nv_source_audit.md`. The verified construction is a strict clarification of the gate, with the arithmetic nonvanishing still outstanding.

## Final twisted-cochain theorem: complete independent audit

Object: the complete `work/cubic_twisted_obstruction_section.tex`, including the final added cyclotomic-representative paragraph. Final reviewed SHA-256: `46013fd13c4f54c9969ce5dae1774452a342330b311af422d71d4634af9f1994`. Verdict: **PASS for K17-CUBIC-TRIANGULAR, K17-CUBIC-TWISTED and K17-CUBIC-CYCLOTOMIC-INPUTS as stated.** This is an independent whole-proof reconstruction, not a numerical or formal proof-assistant check.

The matrix blocks in (CT.13) have the correct coefficient characters. Direct multiplication of the left and right two-by-two blocks gives the claimed action on the four-entry module, with the top-right entry of character chi_1 chi_2 chi_3. Multiplication of U by the inverse right block leaves the central matrix unit fixed. The differential of the indicated quotient cocycle is therefore exactly the central cocycle c, with the signs in (CT.11)–(CT.14). In particular, the pair coordinates are the exponential group coordinates, not the uncorrected Lie coordinates.

The localization statement concerns the algebraic localization of the complex of continuous A-valued cochains. Flatness identifies its cohomology with the localized cohomology; no comparison with an unrestricted complex of function-field-valued cochains is used. Vanishing supplies one scalar denominator and a bounded central lift. Its logarithm respects the assigned weighted filtration through degree three: first coordinates kill torsion, and complex conjugation kills the inappropriate degree-two or degree-three coordinates. Thus it splits the actual Ext pushout. Conversely, a zero actual relation scalar gives a consistent central lift on the full finite cyclic companion, including repeated roots. The finite rational free basis and the continuous bounded integral spans provide a common denominator for this lift and its degree-three exponential. This establishes the reverse implication without an infinite collection of unrelated denominators.

The final paragraph was checked separately after the full read. Once restrictions to H agree, the difference eta of the global and chosen cocycles inflates from Gamma times Delta. Subtracting the coboundary of eta(gamma)/(z_i-1) kills gamma and therefore all Gamma by continuity. The cocycle identity on the commuting pair gamma, delta then gives (z_i-1) eta(delta)=0, so the same cocycle also vanishes on Delta. This is one additional bounded scalar denominator. The argument identifies the localized H1 inputs while preserving the specified pair defining system.

The theorem's final limitation is essential and correct: the construction gives the actual class, its exact coefficient extension, and the rootwise nonvanishing criterion. It does not prove an arithmetic nonzero value, a fixed-order Bockstein-image surjectivity theorem, or a new full-kernel theorem.
