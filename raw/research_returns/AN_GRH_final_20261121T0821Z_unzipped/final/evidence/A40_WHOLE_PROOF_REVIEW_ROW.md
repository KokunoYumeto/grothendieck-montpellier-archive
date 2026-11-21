# A40 whole-proof review

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

**Result: PASS.** Read the complete source at SHA256 `397ab7b7ba43114d2eb278d19c10cf91849d8f1373e53e213c9acfdf2b9c485d`, then checked the narrow changes producing SHA256 `bc403f8bfcc174ec4214d802a79c2c0cbf83fa2873a1f0c4af5970f468d6fbe6`. This is a targeted whole-proof reading and a narrow update check; it is not a separately authored independent re-proof or formal verification. No source correction is required.

## Mathematical checks

The Rosati intersection normalization gives Theta dot TTheta = 3. Thus no translate of either curve coincides with the other; the two-dimensional difference map is finite, generically separable, degree three, and flat. The vertical component has multiplicity one. Removing it gives an effective residual divisor with both projection degrees two, self-intersection two, and arithmetic genus six. The degree-two effective-divisor relation has the stated positive T sign.

Every component of the residual divisor has positive degree over both factors. Consequently every reducible or nonreduced case consists of two automorphism graphs counted with multiplicity. Their induced unitary Jacobian automorphisms u,v give Phi_5(u^{-1}v)=0, hence an order-five curve automorphism. An ordinary genus-two curve in characteristic two has three hyperelliptic branch points. Its automorphism group maps into S_3 with kernel of order two, excluding order five. This proves integrality, including the potentially doubled-graph case.

For smoothness, each normalized irreducible component of the critical Gauss fibre product has nonconstant separable projections. The differential of h=Tz_P-2z_Q is nonzero because d[2]=0. If h had image in TTheta, differentiation forces the lifted point s to equal P or its hyperelliptic conjugate. The first case would make the varying Q a two-torsion class; the second would make TTheta a translate of Theta. Both are impossible. The finite intersections of h(Z) with TTheta therefore exclude only finitely many parameter values for singularities away from the vertical component. The proof separately checks the residual divisor at that component: outside finitely many branch-value parameters, the coefficient after removing its local parameter has a simple Gauss-map zero in the second variable. This resolves the base-component issue without an unsupported Bertini assertion.

The smooth residual curve has genus six, so its degree-two projections to genus two cannot be purely inseparable. The norm/pullback matrices and their signs check exactly. The image of J^2 has dimension four, its polarized complement dimension two, and the product of projection involutions has order five on the Jacobian and hence on the curve. The invariant subvariety has dimension two, giving genus two for the cyclic quotient. Riemann--Hurwitz then forces zero different, proving the cyclic degree-five cover is etale. On the quotient, the reflections act as minus one on the Jacobian and thus are hyperelliptic.

The final matrix addition is correct: sigma squared has matrix [[0,-1],[1,T]], so N_1 sigma^2 U_1=T. All necessary finite data descend to a finite field extension, and rationalizing any chosen lift of an arbitrary prescribed target point gives an entirely split degree-five source fibre because the deck transformations are constant. The auxiliary smoothness parameter is not confused with that prescribed point.

The A38 application therefore establishes actual transferred images with a fixed bad canonical prime. It does not prove that both images fail, that every cover fails, or that the source is rank one or its prescribed point is Weierstrass. These limits are explicit and appropriate.

## Primary-source checks

Reopened the author PDFs and read the full relevant displayed proofs:

- J. S. Milne, *Abelian Varieties* (2022), Theorem 17.3 and its proof, pp.35–36: Rosati trace/intersection normalization. The proof's auxiliary Lemma17.4 and its displayed explanation were also read; no claim of reading all its external references.
- The same source, Lemma8.3 and complete proof, p.13: finite-flat intersection pullback.
- J. S. Milne, *Jacobian Varieties* (2021), Theorem12.1(b), pp.38–39, and its complete displayed uniqueness proof: faithfulness. The full proof of Torelli existence in part(a) was not required or claimed read.
- Stacks Project, Lemma10.128.1, Tag00R4, complete statement and displayed proof: miracle flatness.

Primary URLs: https://jmilne.org/math/xnotes/AVs.pdf ; https://jmilne.org/math/xnotes/JVs.pdf ; https://stacks.math.columbia.edu/tag/00R4 .

Retrieval references in this review: turn463859421view0, turn906127129view0, turn906127129view1, turn463859421view1, turn906127129view2, turn985729020view0, turn567618956view0.
