# Independent review of the characteristic-five ordinary Picard kernel

**Statement:** finalized C.3bf; the independent review does not itself assign the parent's status.
**File reviewed:** research/agents/real_weil/C3_integral_picard_kernel_draft.tex, first complete version and revised direct-curve version saved at 13:49:26 UTC on 19 November 2026; subsequently the final Poincare-obstruction Step 5 and the finalized research/agents/real_weil/C3_integral_picard_kernel.tex were reread. The draft is now a supersession pointer.
**Reviewer:** GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06 /root/frobenius; inherited effort setting not separately exposed.
**Verdict:** full mathematical proof check **PASS** for the revised direct-curve proof. Exact Brion vector-extension source freshly opened and read. The owner's finite certificate and ordinary-Verschiebung source validation are separate receipts; this report does not claim to have run that program or freshly opened that latter source.

The revised Step 5 was completely read by actual tool clock 13:50:16 UTC, after an earlier complete reading of the first version. The primary Brion audit was then completed during the review begun by the parent at 13:50:08 UTC. No new mathematical construction was introduced after that review began.

## 1. Statement and geometric scope

The claim is integral: over \(k=\overline{\mathbf F}_5\), every local dimension \(N\ge4\) has the explicitly specified algebraizable normal strict-local example, regular puncture \(X\), and regular principal punctured divisor \(Y\), with an injected \((\mathbf Z/5)^3\) in the ordinary Picard restriction kernel. It does not contradict the rational Picard isomorphism or assert a higher-Chow kernel.

The C.3m equations remain valid in characteristic five. The derivative of the Fermat equation has invertible coefficient 4. The graph argument, proper Segre contraction, connected closed fibre, normalization and regular-neighborhood argument retain their exact hypotheses. On the regular resolution, the maximal ideal pulls back to \(I_V\): all its functions vanish on \(V\), while the Segre coordinates \(t x_i z_j\) generate the ideal locally. Thus the mod-\(\mathfrak m^2\) and first-neighborhood conditions used later actually agree.

The strict transform of the principal divisor is the split line bundle over the smooth incidence projective bundle \(H_0\). Its formal neighborhoods are consequently the claimed split thickenings. The pullback maximal ideal on this transform is likewise the ideal of its zero section.

## 2. Picard and restriction calculations

For \(V=\mathbf P^m\times C\), \(m\ge2\), and \(L=\mathcal O(1)\boxtimes K_C\), coherent Künneth gives
\[
H^1(V,L)=k^{m+1},\quad H^2(V,L)=0,\quad
H^1(V,L^n)=H^2(V,L^n)=0\ (n\ge2).
\]
The square-zero unit sequence therefore gives the actual vector extension of \(J=\operatorname{Pic}^0(C)\) by \(\mathbf G_a^{m+1}\), not merely a tangent-space dimension. Constants lift. Later Picard groups are isomorphic, and their global units have surjective transitions from the relevant second stage onward; this rules out a hidden inverse-limit ambiguity when endpoint classes are declared formally trivial.

On the incidence divisor, the sequence \(0\to\mathcal O_V\to L\to L_H\to0\) gives
\[
H^1(H_0,L_H)=H^1(V,L)/U,\qquad
U=\ell H^1(C,\mathcal O_C),\qquad \dim U=3.
\]
The multiplication map is injective by the canonical-section Serre pairing. Higher \(H^1\) and \(H^2\) vanish as stated. The target is split, so its formal identity component is \(J\times(U_0/U)\), and the vector restriction is the literal linear quotient. This is a full group calculation, not an inference that a zero derivative alone kills a group morphism.

## 3. Extension class and the finite étale group

The three \(z_iH\) images form the degree-five basis of
\[
k[z_0,z_1,z_2]/(z_0^3,z_1^3,z_2^3).
\]
The same Jacobian calculation as C.3m therefore gives an extension class of rank three and image \(U=\langle x_0,x_1,x_2\rangle\). Illusie's first-order line-bundle formula is used through the explicit transition-unit computation, which is characteristic independent; only division by 4 in the Fermat Jacobian calculation is required.

The Hasse–Witt coefficient calculation is consistent: for the three positive degree-four exponent triples, the diagonal exponent in \(F^4\) is a permutation of \((8,4,4)\), with coefficient \(4!/(2!1!1!)=12=2\) modulo 5. Off-diagonal exponents are not all multiples of 4, so their coefficients are zero. Thus the matrix is \(2I_3\).

For ordinary \(J\), Verschiebung \(v:J^{(5)}\to J\) has étale kernel \(K\simeq(\mathbf Z/5)^3\), and \(v^*\) on \(H^1(\mathcal O)\) is zero because its composition with the bijective Frobenius pullback is \([5]^*=0\). The natural extension classification is functorial under pullback. Hence \(v^*G\) splits.

The exact Hom–Ext sequence gives
\[
\operatorname{Hom}(K,\mathbf G_a)
\simeq \operatorname{Ext}^1(J,\mathbf G_a).
\]
The three independent vector-extension classes mean that the resulting map \(K\to U\) has rank three. As \(K\) is a constant elementary abelian group, this is an injection of group schemes. The full lift \(b:J^{(5)}\to G\) has kernel contained in \(K\), so it is a closed immersion. Its proper image restricts to \((v,0)\) in the split target, since a proper connected group has no nonconstant morphism to an affine group. The finite kernel on this image is exactly \(b(K)\).

### Exact fresh primary source

We independently opened the complete 74-page author PDF:
Michel Brion, *Some structure theorems for algebraic groups*,
https://www-fourier.univ-grenoble-alpes.fr/~mbrion/course_fin.pdf.

We read author pp. 47–48, equation (5.3.5), the explicit map
\(\operatorname{Ext}^1(A,\mathbf G_a)\to H^1(A,\mathcal O_A)\) and its stated isomorphism, equation (5.3.6), and **Remark 5.3.3(i)**. The last explicitly retains universal vector extensions in positive characteristic and avoids incorrectly importing the preceding characteristic-zero decomposition of arbitrary unipotent groups. The vector kernels in C.3bf really are vector groups.

The classification also has the elementary explanation used in the audit: coherent Künneth makes every \(H^1(A,\mathcal O_A)\) class primitive under addition. An addition isomorphism for the associated \(\mathbf G_a\)-torsor can be normalized at the origin; its associator and commutator are global additive-valued functions on the proper powers of \(A\), hence constants, and normalization makes them zero. This yields a unique group extension and its pullback functoriality.

## 4. Actual proper-curve family: the decisive revised step

The version read at 13:50 used a Picard-gerbe argument with its full multiplicative-times-additive band. The final owner version supersedes that argument with the following simpler actual-bundle construction, independently reread and passed by 13:55:03 UTC and checked again after finalization.

Choose a smooth proper curve \(P\subset B\) through the origin and the specified \(\alpha\). Pull the normalized actual Poincare line bundle on \(C\times J\) back along \(V\to C\) and \(v|_P\). Its first-neighborhood obstruction lies solely in \(H^1(V,L)\otimes H^1(P,\mathcal O_P)\), because the other two coherent Kunneth terms vanish. Illusie's mixed Atiyah/Kodaira--Spencer formula identifies it with the Poincare tensor pulled back through \(v^*:H^1(J,\mathcal O_J)\to H^1(J^{(5)},\mathcal O_{J^{(5)}})=0\), then contracted with \(\kappa\). Hence an actual line bundle exists on \(V_2\times P\).

Its represented map to \(G\) and \(b|_P\) have identical projection to \(J\). Their difference is a morphism from the connected proper curve to the affine vector group \(U_0\), hence is constant. Tensoring by the inverse actual fibre at the origin gives exactly the map \(b|_P\), with endpoint classes zero and \(\alpha\). This final proof needs neither a universal bundle over all of \(B\) nor a Picard-gerbe neutralization input.

For every later stage, \(H^2(V\times P,L^n)=0\) by the displayed Künneth decomposition and \(n\ge2\). Compatible line-bundle extensions therefore exist. Their uniqueness as families is not needed; individual endpoint classes are unique. Proper formal existence on \(\mathcal Z_{\widehat R}\times P\), followed by Popescu finite-presentation descent and smooth lifting for the henselian pair \((R,\mathfrak m^2)\), gives an actual line bundle on the **fixed** product \(\mathcal Z\times P\) matching the entire first jet.

This use of smooth lifting is legitimate: the map from the finite smooth \(R\)-algebra to \(R/\mathfrak m^2\) is the reduction of the given completed map and is retained as finite descent data. The henselian-pair lifting property gives an \(R\)-point with that specified reduction. Merely matching the closed fibre would have been insufficient.

The endpoint at the origin is formally trivial, with compatible trivializations supplied by the unit surjectivity already checked. Elkik's puncture comparison detects its actual triviality. The endpoint at \(\alpha\ne0\) cannot be an exceptional line bundle: its restriction to \(V\) is trivial, whereas \(\mathcal O(aV)|_V=L^{-a}\) is nontrivial for \(a\ne0\). Thus the actual ordinary class is nonzero.

First-jet uniqueness, followed by the same completion injection, makes the assignment from \(b(K)(k)\) independent of all choices and additive. On the target, its first jet is zero, later Picard restrictions are isomorphisms, and proper formal existence plus Elkik give actual triviality on \(Y\).

This proof avoids the unnecessary stronger assertion that a global Picard-functor identity component must first be identified with the local Picard scheme. It also avoids lifting a universal family over the whole three-dimensional abelian variety; using a curve is precisely what removes the additional parameter \(H^2\) obstruction.

## 5. Audit boundary

This report certifies the revised mathematical argument and the fresh Brion vector-extension scope. The concrete Hasse/Jacobian computation was independently rederived by hand here.

After writing the initial receipt, we inspected the **entire** owner's code/check_C3bf_integral_picard.py and its complete output/C3bf_integral_picard_certificate.json. The retained run started at 13:51:48.836254 UTC and took 0.07533210799738299 seconds; all 41 checks passed. The full Hasse matrix and determinant, three Jacobian images, universal Segre polynomial identity and split-target chart identity are correct. The finite dimension/exponent samples are explicitly distinguished from the all-dimension and all-exponent mathematical arguments. The constant-kernel enumeration has 125 distinct points and 124 nonzero points; since 5 is prime, its nonzero exponent-five points have exact order five. No independent rerun is claimed.

The exact ordinary-Verschiebung primary source remains a separately attributable validation event. The final proof no longer uses the peer's gerbe source check. No result row or parent review outcome is assigned by this report.

## 6. Final cited Brion source: independent fresh check

At 13:58--14:00 UTC we additionally opened the exact source now cited in the finalized theorem: Michel Brion, *Commutative algebraic groups up to isogeny. II*, complete 35-page author revision, https://www-fourier.univ-grenoble-alpes.fr/~mbrion/isogeny_II_rev.pdf. Section 3.2.3, equation (3.8), printed author p. 23, states the bifunctorial integral extension/coherent-cohomology isomorphism. The following positive-characteristic paragraph is explicitly before the subsequent characteristic-zero restriction. Thus this exact locator has the required all-characteristic scope. It is the original category of commutative algebraic groups, not its rational isogeny quotient, in equation (3.8). No direct opening of the Oort source cited by Brion is claimed.
