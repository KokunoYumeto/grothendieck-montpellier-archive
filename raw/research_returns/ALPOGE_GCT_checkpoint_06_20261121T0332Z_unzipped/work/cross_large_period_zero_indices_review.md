# Independent whole-proof review: P-F33

Reviewer: GPT-6 Astra Pro, inherited/undisclosed effort, `/root/bridges`.
Completed: 2026-11-21 01:47:43 UTC.
File: `positivity_large_period_zero_indices.tex`.
Outcome: **PASS**, including the full rational-singularity argument.

## Algebra and resolution

The quadratic xy-z^2 is irreducible, and the exhibited point proves it does not divide x^(M+2)+y^(M+2). Primitivity and the fraction-field linear polynomial in w prove the hypersurface is a domain. The complete-intersection statements apply. The Jacobian calculation gives exactly the w-axis, of codimension two, so R1 and S2 prove normality. The canonical shift from the one-relation graded resolution is (M+2)-(M+3)=-1, and its Hilbert-series reciprocity has the stated sign and exponent.

On w nonzero, blowing up the axis has exactly the displayed strict-transform charts. Cancellation of the square of each chart coordinate is legitimate: the original ring is a domain, and the displayed equation is saturated with respect to that coordinate. Along the exceptional divisor the x and y charts have a unit derivative in the opposite affine ratio; the z chart has XY=1 and hence a nonzero derivative. Off that divisor the blowup is an isomorphism over the smooth complement of the singular axis. It is a proper resolution on this open set.

The exceptional divisor is the constant conic over G_m. The exceptional ideal restricts as O_P2(1), which becomes O_P1(2) on the conic. Thus its jth conormal power has degree 2j, not negative degree. Each has vanishing higher cohomology over the affine base, and the short exact sequences of thickenings give vanishing on every thickening. Formal functions identifies the completion of each higher direct image with a zero inverse limit. These coherent modules are supported on the axis; a power of its ideal annihilates them, so their completions equal the modules themselves. This proves the required punctured rationality, rather than merely an analytic smoothness assertion. The degree-zero pushforward is also the structure sheaf, as the target is normal and the resolution is proper birational.

The graded criterion applies at the origin: R0=C is a local ring essentially of finite type over a characteristic-zero field, the algebra is normal and finitely generated, it is Cohen--Macaulay, its punctured spectrum is rational, and its a-invariant is negative. There is no isolated-singularity assumption imported into the argument.

## Hilbert function and indices

I independently expanded the paired numerator summands. Substitution k=(s-r)/M gives

`(1/2+1/M)s(s+1)+(r+1)(M-r)/M`.

The absent negative-degree terms at r=0 or 1 are exactly the zero binomial values used in the proof. At s=0, the actual constituent is r=0 and equals one. Hence the formula is global, including the initial point. Every constituent has positive quadratic, linear, and constant coefficients. Positivity and strict saturation hold at every positive argument of every constituent, not just on its realized residue. Thus p=s=0 in the source's literal definitions.

At a primitive Mth root, M>=3 ensures 1-zeta^2 is nonzero, giving a true simple pole. Any period must be divisible by M, while the displayed formula already has period M. The average constant is (M+1)(M+2)/(6M), and the initial range s<M has the unchanged binomial value. Both final observations check.

## Fresh primary-source reads

- Kurano--Sato--Singh--Watanabe, Theorem 5.6, printed p.3262, https://www.math.utah.edu/~singh/publications/kurano_sato_singh_watanabe.pdf . Own refs `turn695608791view0`, `turn474093062view0`. The exact theorem allows nonstandard positive grading and local R0, and asks for rationality off V(R_+), precisely the punctured condition here.
- Stacks 031S (Lemma 10.157.4), 0DWA (Lemma 47.21.8), 01XT (Lemma 30.8.1), and 02OC (Theorem 30.20.5) were opened and checked. Own refs `turn695608791view4`, `turn695608791view3`, `turn695608791view2`, `turn695608791view1`. Formal functions allows any ideal of a Noetherian affine base, so completing along the entire axis is within its statement.

No correction was required. This is a countermodel for a general poles/reciprocity-to-indices implication; it has no asserted ordinary plethysm identification.
