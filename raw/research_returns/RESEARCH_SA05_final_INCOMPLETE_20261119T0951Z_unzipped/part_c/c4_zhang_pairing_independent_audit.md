# Independent audit of the bounded Zhang pairing issue

Recorded on 19 November 2026 after the full written audit at 09:04–09:05
UTC, checked against the session clock. This is a check of a specific retained author version, not a
claim about every version of the published article.

## Source actually read

We read the definitions and displayed pairings in §1.1, author pp. 8–9,
and the complete proof of Theorem 1.3.1, author pp. 14–16, in Shou-Wu
Zhang, *Standard conjectures and height pairings*, arXiv:2009.07089v3,
https://arxiv.org/pdf/2009.07089. The retained files are
sources/root_post08/Zhang2022v3.pdf and its extracted text. After the
initial pairing audit, we also read the complete Appendix Proposition
A.1.1 proof on author pp. 37–38 and independently checked both parts.

We also read every line of root_post08_zhang_audit.md and the complete
code/check_zhang_pairing_example.py. The exact polynomial output is
retained beside the program. We checked the formulas mathematically;
we did not rerun or overwrite the root agent's certificate.

## Geometric verification

The model starts with the projective cubic over the 5-adic integers
whose affine equation is

\[
y^2=x(x-1)(x-5).
\]

The generic cubic is smooth. The only singular point of its special
fibre is the affine origin. Blowing up the ideal \((5,x,y)\) gives the
following strict-transform equations in the \(x\)-chart:

\[
xw=5,\qquad v^2-x+6-w=0.
\]

The relative Jacobian has rows \((w,0,x)\) and \((-1,2v,-1)\).
On the special fibre, if exactly one of \(x,w\) is nonzero, the minor
\(x-w\) is nonzero, so the morphism is smooth there. At
\(x=w=0\), the second equation gives \(v=2,3\) in the residue field.
Since \(2v\) is then a unit, an étale local elimination leaves the
regular strictly semistable equation \(xw=5\).

In the \(5\)-chart the equation is

\[
b^2-5a^3+6a^2-a=0.
\]

The only simultaneous zero of the derivatives of its special-fibre
equation would have \(b=0,a=1/2\), which does not lie on that equation.
This argument proves smoothness over the algebraic closure. The
exceptional tangent conic is
\(Y^2+X^2-PX=0\); its three derivatives have no common projective zero.
It has a rational point and is therefore a projective line. The two
charts cover this conic because \(P=X=0\) is impossible on it.

The other component is the normalization of the original nodal cubic,
parametrized on its affine part by
\(x=v^2+1,y=v(v^2+1)\). It too is a projective line and meets the
exceptional component at precisely \(v=2,3\). The chart calculation
establishes transverse intersections and multiplicity one. Thus the
asserted proper regular strictly semistable model is verified directly.

## Cohomological conclusion and limits

For the geometric special fibre \(Y\), the normalization sequence gives
\(H^1(Y,\mathbf Q_3)\simeq\mathbf Q_3\) and
\(H^3(Y,\mathbf Q_3)=0\). The graph line has Frobenius weight zero.
Supported duality gives

\[
H^1_Y(X,\mathbf Q_3)
 \simeq H^3(Y,\mathbf Q_3)^\vee(-2)=0.
\]

Consequently Zhang's actual definition gives
\(H^1_\psi(Y)=H^1(Y,\mathbf Q_3)\). The displayed pairing on this
one-dimensional space is induced by degree-one cup product and is
alternating, hence zero. The literal unconditional perfection claim for
this pairing on author p. 9 is therefore false.

The always-valid quotient duality pairs \(H^i_\psi(Y)\) with the kernel
of the complementary supported-to-ordinary map, rather than with the
displayed complementary \(H_\psi\) group. This follows by taking the
annihilator of the image of the adjoint map. We checked this exact
finite-dimensional argument in the root note.

Theorem 1.3.1 uses the full supported localization duality. Its proof
does not need the erroneous perfection claim. Its final display on
author p. 16 must use \(W_iH^i(X_\eta)\), not
\(W_iH^i(X_s)\): the former is the image identified earlier in the
proof, and the Hochschild–Serre comparison concerns the generic fibre.
After this local subscript repair, the stated weight argument passes.

This example is not a counterexample to local invariant cycles for
curves, to geometric weight–monodromy, or to the finite exterior-power
criterion. It does not count as movement on any universal research gate.

## Supplementary check of the exact Lefschetz-module input

For Appendix Proposition A.1.1(1), a primitive vector in degree \(i\)
of a Lefschetz module with centre \(n/2\) is killed by
\(L^{n+1-2i}\). A degree-preserving \(L\)-linear map into a module
with centre \(m/2>n/2\) therefore has zero image on that vector,
because \(L^{m-2i}\) is injective there and
\(m-2i\ge n+1-2i\). Primitive strings generate the source, so the
entire map is zero.

For part (2), take an extension with submodule centre \((n+1)/2\)
and quotient centre \(n/2\). Lift a primitive quotient vector in
degree \(i\) to a vector \(v\) of the extension and put
\(r=n+1-2i\). Its \(L^r\)-image lies in the submodule, and the
Lefschetz isomorphism from degree \(i\) to degree \(n+1-i\) of
that submodule supplies a unique correction \(u\). Then \(v-u\)
is the unique primitive lift. Extending these lifts along their
\(L\)-strings gives an \(L\)-linear splitting. Part (1) makes it
unique. The printed use of both \(k\) and \(i\) in the source's
primitive-lifting display is read with \(k=i\). This check does not
use the preceding paragraph about construction of a lowering operator.
