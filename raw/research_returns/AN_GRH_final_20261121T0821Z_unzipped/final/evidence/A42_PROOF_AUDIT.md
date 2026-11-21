# A42 author proof and primary-input audit

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Canonical source: A42_FIXED_LANG_DENSITY.tex.  
SHA256: 4674c99fa0944da6928d469aaca6e128571f259603b791e294ec3bacba628d87.

## Scope and result

PASS: the entire first complete proof was read, followed by the final display-layout and Frobenius-twist wording changes. This is an author check, not an independent check or formal verification. There is no numerical certificate in this finding: its assertions are proved symbolically.

The result is an explicit refinement of the already known Lang quotient method. For a fixed finite set S, a fixed primary coset c, and extension degrees n avoiding the selected primes and the prime-to-ell parts of the mod-ell Frobenius orders, the rational S-primary subgroup stays equal to its ground-field subgroup. A single geometrically connected Lang pullback counts that coset with denominator d = #J(k)_S and error 2(d(g−1)+1)q^(n/2)/d. The prime-to-characteristic density and dense canonical-good corollaries follow.

No open row at the 05:15 review is closed. In particular this does not solve the universal prescribed-source-point cover-selection problem. The auxiliary characteristic-primary cover is used solely for counting; the allowable odd witness at each counted canonical-good point is supplied separately by A29.

## Complete proof checks

1. **Primary stability as equality of subgroups.** The eigenvalues of Frobenius on the geometric point group J[ell](bar k) have orders dividing h_ell, even when the matrix has a nontrivial unipotent part. For gcd(n, ell h_ell)=1, V_n(lambda) is nonzero for every eigenvalue: it is n at lambda=1 and (lambda^n−1)/(lambda−1) otherwise. Invertibility on J[ell] gives injectivity on each J[ell^a], since a nonzero kernel contains a point of order ell. The commuting factorization F^n−1=V_n(F)(F−1) proves equality of the actual fixed subgroups, not merely equality of their orders. This remains valid at ell=p because only geometric torsion points are used.

2. **Explicit admissible degrees.** The prime-to-ell part of the order of an element of GL_r(F_ell) divides the prime-to-ell part of that finite group's order, namely the product of ell^j−1 for 1≤j≤r. Thus the given M_0 is a valid larger modulus, including the characteristic-primary rank bound. The progression 1 mod M is infinite without any prime-distribution input. The case of zero geometric p-torsion and d=1 is included.

3. **Fixed quotient and translation.** The Lang kernel is the constant finite group J(k). Factoring out its prime-to-S subgroup H gives a fixed etale isogeny with constant kernel canonically isomorphic to G_S. Translating the Abel embedding by the ground-field point c gives one cover Y_c over k. Nothing requires B to be effective or X(k) to be nonempty.

4. **Full-characteristic connectedness.** A proper geometric monodromy subgroup would give a nontrivial intermediate etale isogeny to which the translated Abel map lifts. After subtracting the value at a geometric basepoint, Jacobian universality gives a homomorphic section. Its degree contradicts the nontrivial isogeny's degree. This proof includes characteristic-primary etale isogenies and is independent of a prime-to-p restriction. Unramified Riemann–Hurwitz gives genus d(g−1)+1.

5. **Norm scaling and split fibres.** If (F−1)y=x−c, then F^n(pi_H(y))−pi_H(y)=pi_H(N_n x−n c). The norm lies in J(k). On the stable S-primary subgroup its projection is n(x_S−c); all complementary primary components vanish under projection. Since n is invertible on G_S, splitting is precisely x_S=c. A constant finite torsor has d rational points over a split rational fibre and zero otherwise. The same cover is used over every extension, so there is no unstated identification of two different Lang maps.

6. **Exact count and asymptotic.** Weil's curve bound with the proved genus gives the stated error. The analogous bound on X gives the limiting proportion. Unbounded point counts imply infinitely many distinct geometric points and hence density on the Abel curve. The displayed sufficient threshold implies a count greater than one, enough to exclude the possible single point mapping to zero.

7. **Actual theta and canonical class.** In genus two and characteristic two, the locally exact differential line bundle lies on X=C^(1), has degree one, and satisfies B^2=omega_X. Therefore the actual Raynaud theta support is i_B(X), and kappa_R=−2 i_B(R). Taking S={2,r}, c_2=0 and a rational nonzero r-torsion c_r gives nonzero canonical r-component; r=3 always meets the even-order condition. All covers and point-section claims here use A29 over the finite field in which the counted point is rational. Twisting by the finite ground-field automorphism transports this to C.

8. **Limits.** Prescribing a finite list of components does not control the remaining prime factors of the entire order. Dense good points do not compel a prescribed finite set of reflection images to intersect that set. This is compatible with A41 and does not turn the auxiliary p-cover into an allowable pro-prime-to-p neighbourhood.

## Primary inputs actually read

- Bjorn Poonen, *Multiples of subvarieties in algebraic groups over finite fields*, IMRN 2005, no. 24, 1487–1498; author PDF dated 30 November 2004:
  <https://math.mit.edu/~poonen/papers/multiples.pdf>.
  Read the complete displayed Lemma 5.1 and its proof (author p.6), the complete adjacent proof of Theorem 1.4 (p.6), and complete Lemmas 6.1–6.2 and their proofs (p.7). These already supply the construction and primary-extension method. Also reread Theorem 1.8 and the complete displayed Lemma 6.4/6.6 proofs for the retained selection-gap scope. Web references in this run: turn482749454view1, turn171139796view0, turn171139796view1, turn802732682view0.

- J. S. Milne, *Jacobian Varieties*, author version dated 12 June 2021:
  <https://www.jmilne.org/math/xnotes/JVs.pdf>.
  Read complete Proposition 6.1 and its immediate proof, pp.19–20; Proposition 9.1 and all of its displayed development through the p^m Witt-vector completion, pp.30–32; Theorem 11.1 and the displayed derivation through Proposition 11.2/Lemma 11.3, pp.35–37. The referenced external proofs of the Artin–Schreier cohomology identification in Lemma 9.4 and other cited prerequisites were not independently reconstructed. A42's connectedness proof instead derives the needed assertion directly from Proposition 6.1. Web references: turn193881955view1, turn482749454view0, turn392687106view0.

- Existing complete A12 Lang proof, A19 finite-support statement, and A29 statement/pointed Lang construction were reread locally for compatibility. The new source uses only existing bibliography keys Poonen2005 and MilneJV.

## Reproducibility and classification

No search over curves, group elements, or cover equations was performed for A42. No new arithmetic numerical example is claimed. The proof gives a terminating finite-field search through admissible degrees and rational points once the curve and component c are specified, with the explicit sufficient size inequality in (PE.13). This is a proved count refinement and a source-credited consequence, not a claim that a formerly open universal incidence row has been resolved.
