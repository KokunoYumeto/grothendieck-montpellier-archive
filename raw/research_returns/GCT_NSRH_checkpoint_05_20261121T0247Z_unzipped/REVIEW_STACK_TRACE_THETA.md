# Fresh final-text review of F35: stack trace, actual groups, convergence, and duality

Reviewer: `/root/rectangular_and_theta`. Check completed 2026-11-21, approximately 00:55 UTC. This is a fresh full mathematical read of the complete generated fragment, with independent reconstruction of its calculations and direct inspection of the cited primary statement contexts. It is not proof-kernel verification, and it does not claim to reprove the general Laszlo–Olsson or Sun theorems.

## Exact object reviewed

- `finding_F35.tex`, SHA256 `ddd9f9eead23d6c9cfb0111b2a98dc6556f1d47a79c38a9ae7ee8226607db9b8`.
- Sun, *L-series of Artin stacks over finite fields*, published PDF `primary_sources/Sun_L_series_2012.pdf`, SHA256 `88d1ad98148c61ceb99c82197655551620cb6a680fe602bd86d30e10b9d7f8f3`.
- Laszlo–Olsson, *The six operations for sheaves on Artin stacks II: Adic coefficients*, published PDF `primary_sources/Laszlo_Olsson_II_2008.pdf`, SHA256 `98a409a24838feb09191152269b7359b7e3da4183d6aea6beb8af0d26c703dab`.

Primary URLs are https://msp.org/ant/2012/6-1/ant-v6-n1-p03-s.pdf and https://numdam.org/item/10.1007/s10240-008-0012-5.pdf . This review concerns the fragment itself. A later main-paper insertion or edit requires a text/hash match.

## Verdict

**PASS: no mathematical blocker or correction found.** The finding really constructs the entire all-extension scalar trace sequence by an actual finite-type Artin stack. Its unbounded compact cohomology, absolutely convergent trace, termwise duality, and failure of an independent bound on the visible dual spectrum are all supported by the displayed calculations. The final scope restrictions are necessary and correctly stated.

## Source applicability checked directly

Sun Theorem 1.1, printed p.49, concerns every finite-type Artin stack over a finite field, uses geometric Frobenius, and asserts absolute convergence of the compact-support Euler trace and equality with groupoid mass. It is applicable to the stated finite disjoint union and quotient stack. No assumption of finite stabilizer groups is silently imposed.

Sun Definition 4.1, p.84, requires every positive absolute eigenvalue moment and observes that bounded complexes are convergent. Theorem 4.2, p.85, applies to bounded-above, mixed, geometrically stratifiable convergent complexes and preserves the convergence under the relevant compact pushforward. The constant sheaf used here satisfies these requirements: it is bounded, constant, and punctually pure of weight zero. The stronger direct moment calculation in the fragment independently checks convergence after pushforward.

Sun Theorem 4.8 and §4.8.2, pp.89–90, give the classifying-stack symmetric-algebra cohomology and compact-support dual weights. Example 7.4, p.109, explicitly gives

\[
H_c^{-8-2s}(BGL_2)=\mathbf Q_\ell(s+4)^{\oplus(\lfloor s/2\rfloor+1)}.
\]

Sun Theorem 1.4, p.50, has the sharper bound weight at most cohomological degree for constant coefficients when stabilizers are affine; it matches the fragment's computed weights.

Laszlo–Olsson's opening assumptions, p.169, require an affine excellent finite-dimensional base, invertible coefficient prime, and finite étale cohomological dimension on finite-type base schemes. A finite field with \(\ell\ne p\) meets these hypotheses. §9.1, Lemmas 9.1.1–9.1.2, p.198, supply the duality and smooth dualizing-complex formulas. Theorem 11.0.14, p.204, is the compact-support Künneth isomorphism for bounded-above constructible inputs. The constant inputs here are bounded; the unbounded-below output is permitted. The calculation does not incorrectly invoke a bounded-output theorem for schemes.

## Geometry and mass

With \(U=\mathbf A^6\times\mathbf G_m^8\) and \(G=(GL_2)^4\), the action is trivial, so the quotient is \(U\times BG\). The atlas has relative dimension 16 and \(U\) has dimension 14, giving smooth stack dimension \(-2\). The points in the disjoint union have dimension zero, so the full stack is not equidimensional; the text explicitly preserves that distinction.

Every \(GL_2\)-torsor over a field is the frame torsor of a two-dimensional vector space and is trivial. Counting independent columns yields

\[
|GL_2(\mathbf F_Q)|=Q(Q-1)^2(Q+1).
\]

Thus the mass is \(Q^6(Q-1)^8/[Q^4(Q-1)^8(Q+1)^4]=Q^2/(Q+1)^4\), and the 24 points and 16 components give exactly the stated trace sequence for every positive extension degree.

## Actual cohomology, with all signs and Tate twists checked

Write \(\sum a_s z^s=(1-z)^{-4}(1-z^2)^{-4}\). Four copies of the polynomial ring on Chern classes of degrees 2 and 4 produce \(a_s\) degree-\(2s\) classes with twist \(-s\). Together with the exterior cohomology of the eight-dimensional torus, this gives

\[
H^i(\mathcal Y)=\bigoplus_{b+2s=i}
\mathbf Q_\ell(-(b+s))^{\oplus\binom8b a_s},\qquad 0\le b\le8.
\]

The compact degrees and twists add independently as follows:

- Affine factor: degree 12, twist \(-6\).
- Torus factor: degree \(16-b\), twist \(-(8-b)\), multiplicity \(\binom8b\).
- Four classifying factors: degree \(-32-2s\), twist \(s+16\), multiplicity \(a_s\).

Their sum is precisely degree \(-4-b-2s\) and twist \(b+s+2\). Each degree has finitely many summands. The terms with \(b=0\) and arbitrary \(s\) prove unboundedness below. Their weight is \(-2(b+s+2)=j-b\le j\), as required by the cited affine-stabilizer estimate.

The illustrative mixed group also checks:
\(H_c^{-6}=\mathbf Q_\ell(3)^4\oplus\mathbf Q_\ell(4)^{28}\).

## Absolute convergence and effective versus visible multiplicities

For \(x=q^{-n}\), Euler sign is \((-1)^b\), not a sign attached to the Tate exponent. Summing gives

\[
x^2(1-x)^8(1-x)^{-4}(1-x^2)^{-4}
=x^2/(1+x)^4.
\]

For every real \(t>0\), the ungrouped absolute moment is

\[
q^{-2t}(1+q^{-t})^8(1-q^{-t})^{-4}(1-q^{-2t})^{-4}
=\frac{q^{-2t}(1+q^{-t})^4}{(1-q^{-t})^8}<\infty.
\]

Consequently regrouping by eigenvalue is legitimate. The coefficient of the visible eigenvalue \(q^{-(j+2)}\) is the coefficient of \(z^j\) in
\((1-z)^8\sum a_sz^s=(1+z)^{-4}\), namely \((-1)^j\binom{j+3}{3}\). In particular, at \(q^{-3}\), the actual multiplicities four and eight occur in degrees \(-6\) and \(-5\), giving \(4-8=-4\). This verifies that the construction does not mistake signed visible coefficients for negative-dimensional groups.

After adjoining the 24 points and multiplying by 16, the support is bounded, locally finite away from zero, and has all positive absolute moments finite. These are the admissibility hypotheses used by F32. The text invokes uniqueness only in that stated class.

## Duality and the limitation of the construction

The smooth dualizing complex in dimension \(-2\) is \(\mathbf Q_\ell(-2)[-4]\). Hence

\[
H_c^{-4-i}(\mathcal Y)=H^i(\mathcal Y)^\vee(2).
\]

This matches every summand of the independently computed formulas. A compact root \(q^{-(b+s+2)}\) pairs with \(q^{b+s}=q^{-2}/\alpha\). After grouping, all \(q^j\), \(j\ge0\), remain visible with nonzero coefficients \((-1)^j\binom{j+3}{3}\). Therefore this dual support is unbounded and its ordinary geometric-Frobenius trace does not converge by terms tending to zero. Actual duality thus coexists with failure of the separate bounded-dual-spectrum hypothesis. The statement does not impose the dimension-\(-2\) pairing on the isolated points; duality for the full stack is componentwise.

Finally the fragment explicitly supplies one scalar trace sequence only. It does not identify operators for both nonstandard generators, their multiplication, a simultaneous family of words, a canonical basis, or the opposite path-output sign. No claim about all possible stack models is made. These qualifications correctly prevent this constructive example from being overstated.

Check event: `F35-FINAL-FULL-READ-THETA-PASS`.

## Scoped main-paper insertion check

At main-paper SHA256 `0d2604a625f4210e29cfd786f8934a13cfab786a07365fbbbb95a961e2cd8a9d`, the entire F35 subsection/proof/scope body matches the reviewed fragment exactly. Its separately relocated Grothendieck paragraph also matches exactly. The trailing bibliography-key comments are not substantive body text. This is an exact scoped insertion check, not a review of all later main-paper material.
