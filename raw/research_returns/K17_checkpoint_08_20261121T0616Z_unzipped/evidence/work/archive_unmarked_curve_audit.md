# Whole-proof audit: the unmarked full-curve counterexample

**Verdict: PASS for the stated automorphism counterexample and its scoped functorial-recovery consequence.**

Reviewer: GPT-6 Astra Pro, K17/archive_kummer, 2026-11-21. The complete work/archive_unmarked_curve_section.tex was read. Reviewed SHA256: 5afa9741b5caa653806808a2c27d9e0be92c470124e3f3bfa4a76bdf302e404e. The complete relative and generic-recognition sections were also read to check the precise imported statements and section-conjugacy conventions.

## 1. The actual geometric groups

For \(S=\mathbb G_{m,\mathbb Q}\), the choice \(t=1\) gives the arithmetic section, and the covers \(v^n=t\), based at \(v=1\), identify the geometric kernel \(A\) with \(\widehat{\mathbb Z}(1)\). The arithmetic action is cyclotomic. This produces the actual semidirect product \(G=A\rtimes G_{\mathbb Q}\), not just an abstract group of the correct shape.

The fixed rational tangential basepoint on the constant tripod gives \(\pi_1(C)=\Delta\rtimes G_{\mathbb Q}\). Its chosen inertia \(I\) is cyclotomic. Geometric self-normalization gives \(N_\Delta(I)=I\). Consequently, once the product formula is applied, the full relative curve group and the actual full normalizer are

\[
\Pi=(A\times\Delta)\rtimes G_{\mathbb Q},
\qquad N_\Pi(I)=(A\times I)\rtimes G_{\mathbb Q}.
\]

Indeed an element normalizes \(I\) precisely when its \(\Delta\)-component does, since the chosen arithmetic section normalizes it and \(A\) centralizes \(\Delta\).

## 2. Primary source checks

The complete relevant statements and proofs were freshly read in work/references/sga1_reedition.txt:

* Exposé IX, Théorème 6.1, printed pages 195–196: the arithmetic exact sequence for a quasi-compact geometrically connected scheme over a field. All three schemes used here satisfy these hypotheses.
* Exposé XI, Proposition 6.1 and Sections 6.2–6.5, printed pages 233–235: the Kummer cover, its étaleness when the exponent is invertible, and its cohomology normalization. Every exponent is invertible over \(\mathbb Q\).
* Exposé XIII, Corollaire 2.12, printed pages 290–292: the punctured-curve presentation, including its characteristic-zero argument. For genus zero and two punctures this is \(\widehat{\mathbb Z}\); in characteristic zero the prime-to-characteristic quotient is the full group.
* Exposé XIII, Proposition 4.6 and proof, printed pages 310–311: the geometric Künneth formula. The first factor is a smooth finite-type curve over \(\overline{\mathbb Q}\); the required strong desingularization in dimension at most one is available. Again all primes are allowed.

The natural map from the arithmetic product group to the fiber product over \(G_{\mathbb Q}\) is an isomorphism on geometric kernels by Künneth and on arithmetic quotients by construction. The elementary exact-sequence argument therefore proves the stated arithmetic fiber-product isomorphism. There is no unjustified use of a proper-only Künneth theorem for these open curves.

Stix, On cuspidal sections of algebraic fundamental groups, author version dated 24 February 2012, Proposition 16 and its complete proof on printed page 8, were freshly retrieved and read at https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf (retrieval turn645703535view1). The tripod has negative Euler characteristic, and the proposition gives exactly the geometric self-normalization used above. The tangential section itself is the previously established relative comparison specialized to \(\operatorname{Spec}\mathbb Q\).

## 3. Automorphism, fixed data, and Kummer slope

For \(u_2=3\) and \(u_\ell=1\) at all odd primes, multiplication by \(u\) is a continuous automorphism of \(A\) commuting with \(G_{\mathbb Q}\). Scaling only \(A\), and fixing \(\Delta\) and \(G_{\mathbb Q}\), therefore defines an actual automorphism of the complete displayed diagram. It fixes \(I\) pointwise, every geometric cusp inertia subgroup inside \(\Delta\), the rational base section, and the constant tangent section as a section transported along the base automorphism. The base group \(G\) itself is deliberately allowed to move.

Under the common Kummer normalization, the class of the normal vector \(tb\) is represented by the cocycle \(c_t(a,g)=a\). This satisfies the crossed-homomorphism identity because the two copies of inertia have the same cyclotomic action. Its normalization at the base section is zero, as seen from the compatible roots \(v=1\). Hence the formula is verified at every finite level and at the inverse limit.

Transporting a section must include the inverse base automorphism; it is \(\alpha_Ns\alpha_G^{-1}\), not merely \(\alpha_Ns\). Its geometric restriction is consequently multiplication by \(u^{-1}\), exactly as in the text.

The units of \(\mathbb Q[t,t^{-1}]\) are precisely \(a_0t^m\). The highest-minus-lowest-exponent argument proves this directly. Their Kummer restrictions to \(A\) are the ordinary integer slopes \(m\). An \(I\)-coboundary restricts to zero on \(A\), since \(A\) acts trivially on \(I\); therefore these slopes are invariants of the section classes at issue.

If the transported class were geometric, its slope would require \(m=u^{-1}\). The 2-adic coordinate would imply \(3m=1\) in \(\mathbb Z_2\), and injectivity of \(\mathbb Z\to\mathbb Z_2\) would imply the impossible integer equation \(3m=1\). No appeal to completed units being actual units is made. Changing the common inertia sign changes both slopes and preserves the contradiction.

## 4. Functorial scope

The counterexample concerns \(I\)-conjugacy classes of splittings of the marked normalizer extension, consistently with the relative and generic-recognition sections. It does not silently replace them by a different quotient of section classes.

The smaller diagram has an automorphism that fails to preserve the geometric subset for its exhibited realization. Thus no rule invariant under every automorphism of this smaller diagram can select exactly that subset. A recovery of the full generic marking that both recovers the geometric realization and lifts every smaller-diagram isomorphism would force this automorphism to lift. The previously established marked-recognition result would then preserve the subset, a contradiction.

The text explicitly excludes the stronger assertions that would not follow: it does not fix \(G\) pointwise, retain the scheme realization or generic marking, rule out additional rational-point data, or rule out a noncanonical choice not respected by all isomorphisms. The counterexample keeps one rational base section and one constant tangent section, as claimed. No mathematical correction is requested.
