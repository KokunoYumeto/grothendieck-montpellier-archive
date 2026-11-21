# Independent full review of F47

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; reasoning effort not exposed. Date: 21 November 2026 UTC.

**Result: PASS.** The complete report and complete generated fragment were read and all elementary arguments were independently reconstructed.

- Report: agent_positive_polarization_obstruction.md, SHA-256 8751d118826ec680415a7aa20c330116d8d3b099c0650fdc7c1188d315dc3152.
- Fragment: finding_F47.tex, SHA-256 5ca764240bced2e03a46dc875029c52ad16def2bd64b95a6557d7c7718ee436f.

The original rank-ten algebra and actual tensor lattice are inputs from the previously checked F19/F21. The relevant displayed formulas in the current main text were read again for this review. This review does not assert a new verification of the entire GCT source presentation, a formal proof-kernel check, or a numerical experiment.

## 1. The based-ring input and its scope

The primary EGNO lecture notes at https://math.mit.edu/~etingof/tenscat1.pdf were reopened. Definition 1.42.2 and Proposition 1.42.4 are on printed pages 76–77; Corollary 1.43.5 is on printed page 80. The definition includes the distinguished basis, the duality anti-involution, and the coefficient pairing, beyond nonnegative structure constants. The proposition gives the based Grothendieck ring for a semisimple multitensor category, and the corollary asserts semisimplicity of the complexification of a finite-rank based ring.

Retrieval refs: turn703507533view0; relevant retrieved passages turn185072692view0, turn185072692view1, turn185072692view2. The exact statements and surrounding short argument were inspected; this is not a claim to have checked all of EGNO.

The square-zero ideal J in the stated A1 is nonzero and its quotient is semisimple, so it is the Jacobson radical. It prevents the proposed algebra from being a complexified multifusion Grothendieck ring. The graded variant correctly imposes, rather than assumes, that its specialization has that categorical form. Arbitrary positive rings, split Grothendieck groups, and triangulated Grothendieck groups are outside this deduction.

## 2. The actual generator and radical calculation

At v=1, D=4 and the two central roots both equal 3/4. Thus the normalization e=P1/4 and f=P2/4 agrees with F19. Its central element z=(e-f)^2 is zero on the scalar factors and 3/4 plus a central square-zero generator on the matrix factor.

The displayed polynomial p has p(0)=0 and p(3/4+eta)=1, since eta squared is zero. Hence p(z) is exactly the matrix-block idempotent and n=p(z)(z-3/4) is the central element eta on that block and zero elsewhere. Its two-sided ideal is all four dimensions of J.

For self-adjoint images of e and f on a positive-definite Hermitian space, their difference, its square z, and every real polynomial in z are self-adjoint. In particular rho(n) is self-adjoint and square-zero. The norm identity in the report forces it to vanish, and therefore kills the full ideal J. This is a statement about the specified named operators, not merely a freely chosen involution on an abstract isomorphic algebra.

The resulting rank-six quotient is precisely the one already identified in F19, isomorphic to C[S3]. The finite-dimensional positive-adjoint assertion is correct. Positive definiteness and the self-adjointness hypotheses are both essential; ordinary Weil purity does not supply them.

## 3. Regular center pairings and the optimal valuation

The actual difference of roots is Delta=(D-1)(v-v^{-1})^2/D^2. Since the derivative of v-v^{-1} at v=1 is 2 and (D-1)/D^2 specializes to 3/16, its t-adic leading coefficient is 3/4 and its order is two.

In the regular basis (1,x), right multiplication by x has row matrix [[0,1],[0,Delta]]. Multiplying it against a symmetric Gram matrix gives the adjoint equation c=Delta*b, with no additional equation. The trace form is [[2,Delta],[Delta,Delta^2]], because the three multiplication traces are 2, Delta, and Delta^2. Its determinant is Delta^2; the leading principal minor and determinant prove positivity at every real noncollision point.

For a regular generically positive form, a and b are nonzero. On a sufficiently small positive real half-neighborhood, Delta>0, and positivity gives a>0, b>0 and b<a*Delta. If r=ord(b) were smaller than s+2, with s=ord(a), the ratio b/(a*Delta) would tend to positive infinity. Thus r>=s+2. Both terms of a*Delta-b have valuation at least s+2, so the determinant b(a*Delta-b) has valuation at least 2s+4>=4. This argument permits cancellation of leading terms and therefore does not inadvertently assume equality of valuations. The trace form attains order four.

The generalization to a positive Delta of order m on a real half-neighborhood gives the same argument with m in place of two and lower bound 2m. It concerns the regular center module with its specified self-adjoint multiplication operator, not every possible pairing on an unrelated representation.

## 4. The actual tensor form and the apparent contradiction

For both values a=delta and a=D-2, direct multiplication gives Pi*Ga=Ga*Pi^T, using the actual right-row matrices in F21. The off-diagonal entries a/D lie strictly between zero and one for positive real v, so the two eigenvalues 1 plus or minus a/D are positive. At the collision both matrices become [[1,1/2],[1/2,1]], which is nonsingular.

The multiplicities 20,4,16,4 have total dimension 64, and the scalar sectors have evident positive forms. The F21 change of basis has only the already inverted regular denominators and is invertible at v=1. Pulling the direct-sum form back therefore produces a regular positive form on the original tensor basis. Its specialized kernel is exactly J by F21. This confirms the sharp scope: a faithful model of the full rank-ten order is excluded, while the actual tensor representation is allowed.

## 5. Generated fragment and dictionary

The complete generated fragment retains each proof above, all positivity and regularity hypotheses, the exact root normalization, the multifusion restriction, and the distinction between an object's endomorphism algebra and the full based Grothendieck algebra. Its final caveat about VIII's signed-factor convention is appropriately limited.

The finite-flat trace map and determinant ideal follow from the explicit computation and require no unverified discriminant theorem. The SGA3, SGA6, and manuscript connections are framed as framework anchors rather than attributed GCT proofs.

One source-precision suggestion was sent to the author: the final archive sentence associates scans35/37/39 and48–49 with primitive projectors, polarization and conditional semisimplicity. The specifically inspected polarization wording was in cote16 scan43, a Coates letter. Adding scan43 or deleting “polarization” from that archival attribution would make the list exact. This is not a mathematical blocker and does not change the conditional operator theorem.

The affine equivalence should use the verified Stacks tag01IB until the original EGA locator is independently inspected. SGA6 Exposé V §§2–3 is appropriate for the lambda/gamma background in this paragraph and is not being used as a perfect-diagonal locator.

## 6. Review conclusion

All mathematical assertions and their complete elementary proofs pass. The known categorical theorem is correctly cited and scoped. The report and fragment do not infer positivity of a canonical GCT basis, a signed path comparison, a dual weight bound, or a general refutation of Mulmuley's program.
