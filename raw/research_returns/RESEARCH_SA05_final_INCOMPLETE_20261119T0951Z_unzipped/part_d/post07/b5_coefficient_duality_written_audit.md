# Independent audit of the finite-field coefficient-duality dependency

19 November 2026, Part D. I read the complete `part_b/b5_finite_field_coefficient_duality.md`. This is an audit of the written local proof; I did not independently reopen Kahn's primary source in this check.

The dual formula for the Chow-heart generator is correct:

\[
P_{X,n}^{\vee}=P_{X,d-n},\qquad
\operatorname{Hom}(1,P_{X,n}[i])=CH^n(X,-i)_{\mathbb Q}.
\]

For the specified exterior degree-one Weil extension, placing its generator on the left gives precisely

\[
b_P^i(a+eb,c+ed)=(-1)^i\operatorname{ev}(a,d)+\operatorname{ev}(b,c).
\]

The negative-degree vanishing forced by perfect duality and Chow negativity yields all of Parshin's rational vanishing. The remaining degree-zero evaluation is the ordinary complementary Chow intersection pairing, so its nondegeneracy is exactly rational equals numerical equivalence. Finite-dimensionality of numerical cycles and adjointness of dual idempotents justify the converse and passage to all Chow-heart summands.

On the projective line, the total trace degree is three. The even hyperplane class produces no extra Koszul sign. The two cross-blocks are exactly the claimed point pairings. In the second block, putting

\[
Q=P(-1)[-2]
\]

gives another Chow-heart object and the exact identifications

\[
W^i(Q)=W^{i-2}(P(-1)),\qquad
W^{1-i}(Q^\vee)=W^{3-i}(P^\vee(1)).
\]

Thus the projective-line reduction passes with the displayed shifts and twists. The note correctly keeps its all-Chow-heart hypothesis separate from a category containing only homogeneous pure summands. Algebraic Künneth projectors modulo homological equivalence do not by themselves supply the Chow-idempotent decomposition needed to remove that distinction. Neither conjecture is declared proved.
