# Independent complete audit of C.3ae

Reviewer: `/root/frobenius`. Tool clock at certification: **2026-11-19 08:53:01 UTC**. Result: **passed**.

We read the complete typed `cycles/higher_local_surjectivity.tex` after it appeared, including the integral cokernel statement, explicit equations, normalization, specialization invariant, conormal obstruction, Hodge projection, and actual-family argument. The conclusion is an integral surjection from the cokernel of **ordinary algebraically trivial codimension-two restriction** to `Pic^0(C)(C)`, for every local dimension at least seven. This is stronger than a single rational witness, but it is not a theorem about the image of arbitrary `CH^2(X)`.

## 1. The algebraic local scheme

The four displayed matrices agree entry for entry with the first tuple in the retained rank computation and with the tuple used in the basepoint computation. The coefficient of the linear fiber variable has no common divisor with the Fermat equation: `F=ell G=0` has codimension two in the smooth base. The graph description therefore gives an integral hypersurface with no extra vertical component. The differential of F makes it smooth near the entire exceptional divisor.

The Segre blowdown is proper and is an isomorphism away from its zero section. Removing the closed image of the singular locus is legitimate because that image misses the vertex. Normality of the resulting model supplies factorization through the finite normalization. Its connected exceptional divisor maps to one point of the finite fiber, and surjectivity shows there are no other points over the vertex. The dimension is `m+4=N`.

For complete explicitness, the scheme-theoretic fiber assertion can be justified in one sentence: every function in the normalized local maximal ideal vanishes on V, while the Segre coordinate functions `t x_i w_j z_k` generate `O(-V)` because their coefficient sections are basepoint free. Hence `m O_Z=O(-V)`. This is an immediate clarification of the written construction, not an additional existence hypothesis.

The strict transform of `f=t ell` is the split line bundle over H. The four-section surjection has kernel of rank m, so H is the smooth projective bundle of lines in that kernel. The normal line and the transversality of the two divisors are correct. Étale descent and nilpotent invariance of pointed étale neighborhoods preserve the specified first neighborhood.

## 2. Exact finite certificates

The earlier independent certificate audit was repeated with a distinct column-wise matrix construction and finite-field `DomainMatrix` operations. Rank is 57 for the 64 by 57 matrix, and the determinant of its first 57 rows is **47 modulo 101**. We also recomputed all twelve projective charts using lexicographic rather than grevlex Groebner bases; all are `[1]`. This is emptiness over the geometric fiber, not merely absence of F101-points. Properness of the common-zero scheme over Z promotes the empty fiber at 101 to an empty generic fiber.

The independently reproducible code is `code/audit_quartic_certificates.py`, with exact outputs in `output/audit_quartic_certificates.json` and `.out`. These computations certify only the linear algebra and basepoint freeness; the following steps are the separate mathematical audit.

## 3. The specialization invariant

Chow localization on the fixed proper model times a fixed proper parameter gives a lift of every class on the puncture. Two lifts differ by a boundary pushforward. Refined restriction changes that difference by multiplication by the normal Chern class `-(h+a)`, exactly the stated denominator. Thus sigma is well-defined on ordinary Chow groups, including all rational-equivalence witnesses.

The parameter-fiber embeddings and the exceptional-divisor embedding are independent regular embeddings. Their refined pullbacks commute. Hence sigma, projective-bundle evaluation, intersection with tau, and proper pushforward all commute with parameter fibers. There is no change of the parameter-dependent étale neighborhood in this argument.

For rank E equal to m at least three, the first projective-bundle relation has codimension at least three. Therefore in codimension two the quotient by `h+a` is exactly the base Chow group, with evaluation `b0+h b1+h^2 b2 -> b0-a b1+a^2 b2`. The source formula follows from the transverse refined restrictions to V and to the strict transform of the principal divisor. This argument remains integral.

## 4. The first-neighborhood obstruction

We independently opened the primary Stacks statements <https://stacks.math.columbia.edu/tag/0FEX> (Lemma 42.58.1) and <https://stacks.math.columbia.edu/tag/0FEZ> (especially Remark 42.59.9). They give the rational Chern-character realization on the regular scheme and its compatibility with refined pullback. The alternative argument through smooth finite-type pointed étale models is also valid, since the cycles, virtual bundles, and maps are finite data and the parameter is fixed and proper.

For a rank-one conormal kernel, the second exterior-power sequence has exactly the displayed kernel `L tensor Omega^1`. Its cohomological boundary is contraction with the first-neighborhood extension class. The local transition-matrix/Atiyah-class calculation in the draft supplies a lift of the degree-two Chern character through the middle term. Consequently every closure class satisfies the required necessary vanishing. No converse deformation criterion or unproved sufficiency of a Hodge condition is used.

The projection of the construction to `P^m × W` shows that the extension class has only a curve-tangent component. The three `delta(z_k G)` classes are the basis of the degree-five Fermat Jacobian quotient. Taking the source basis Serre-dual to them makes the obstruction coefficients precisely the displayed integers, without an unproved coordinate normalization.

## 5. The Hodge projection and boundary corrections

The Euler and normal sequences give the dual descriptions `H^1(Omega_W^1)/C H_W = R4^*` and `H^1(Omega_W^1(1))=R3^*`. Multiplication by a coordinate is dual to `R3 -> R4`. Thus the certificate matrix acts on exactly the claimed quotient; no unmentioned self-dual monomial basis is needed. The hyperplane class is killed by all these twisted multiplication maps.

In the selected target component, contraction can only act on the curve differential. Its source is exactly `H^1(W,Omega_W^1) tensor H^0(C,K_C) tensor H^1(P,O_P)`. Projective-space differential terms cannot enter that component. The injectivity of the 64 by 57 matrix makes the primitive W-component vanish. Pairing with tau then annihilates the remaining hyperplane component.

The correction terms are explicitly controlled. Since the K3 surface has no first cohomology of O and no global one-forms, a varying mixed divisor component on `W × C × P` comes from `C × P`. Multiplication by a adds `H_W`, which pairs to zero with tau. All other divisor terms, and the codimension-zero term, are constant in the parameter. Thus the boundary correction cannot restore a varying Picard component.

The intersection numbers `H_W^2=4`, `H_W D_W=1`, `D_W^2=-2`, `tau H_W=0`, and `tau D_W=-9` are correct.

## 6. Actual families and the conclusion

Every ordinary algebraic-equivalence generator can be compactified to a smooth proper parameter curve by closing its cycle in the fixed product; its specified open fibers do not change. The constructed line bundle on `C × P` has zero mixed Hodge component, so its classifying map to `Pic^0(C)` is constant. Indeed the induced homomorphism from the Jacobian of P has zero map on `H^1(O)`; over C it therefore has zero differential and is the zero homomorphism. This proves vanishing of rho on the source **ordinary** group.

The target classes obtained from `D_W` and a degree-zero divisor on C are actual ordinary algebraic families. Their rho image is exactly `-9` times the input. Divisibility of the complex points of `Pic^0(C)` gives the asserted integral cokernel surjection. The specified transcendental point yields a nontorsion Abel class because all torsion points of this Qbar-defined Jacobian are Qbar-defined and the Abel map is a closed immersion over Qbar. The resulting rational failure of surjectivity follows.

No remaining mathematical gap was found in this typed proof. The distinction between ordinary algebraically trivial cycles and arbitrary Chow classes is essential and is correctly retained.
