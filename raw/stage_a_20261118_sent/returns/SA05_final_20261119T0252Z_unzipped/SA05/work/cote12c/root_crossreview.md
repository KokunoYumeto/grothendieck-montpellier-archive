# Independent review of the root counterexamples

Reviewer: GPT-6 Astra Pro, subagent cote12c, 19 November 2026.

## Scope and result

I read root_checks.md §§3–5, the complete records SA05-C65–C70, C74–C76, C87 and C101–C111 (21 claims), and the corresponding manuscript passages. I also checked the relevant original numerical program and wrote a separate program which neither imports nor invokes it. No root file or transcription was edited.

The Legendre duality, the proper singular SNC calculation, the Howe curve obstruction, the Enriques homological example, and the section/retraction argument survive this review. The main revisions needed concern the scope of two conclusions and the precision of two arithmetic explanations:

1. The polynomial-ring units argument in C67 is conditional on a notation reading that the surrounding manuscript makes doubtful.
2. The supersingular product disproves the geometric ruledness implication in C70; nonruledness alone does not establish nonvanishing of its class in the displayed graded scissors quotient.
3. The punctured-curve calculation in C110 has the correct answer, but the final residue map should be described using normalized local invariants.
4. C104 should write End over the finite base field and fix the homological Tate-module convention. The existing rational argument can also be completed to disprove literal integral H²-vanishing, without a Sha-finiteness assumption.

## 1. Precise corrections and scope restrictions

### C67: polynomial brackets versus a purely transcendental field

The algebra fact in root_checks.md is correct: a unital homomorphism from a field to a polynomial ring over a field lands in its constant field, because nonzero elements must map to units.

Its application to the author's notation needs an explicit condition. Pro early L1763–1766 says that each field embeds into a purely transcendental extension of the other. At L1799–1801 the same manuscript writes L₀[t] for an extension field of the specified transcendence degree. Thus the earlier R′[s₁,…,s_N] very plausibly denotes a rational-function field rather than a polynomial ring. The units observation is a reading alarm for the literal polynomial interpretation; it should not be counted as a counterexample to the intended rational stabilization. Howe's curve example remains an obstruction under that intended interpretation.

Suggested change: remove “field-unit constraints” from C67's unconditional fate, or prefix that part by “if the brackets denote a polynomial ring.” Preserve the full rational-function interpretation for the actual lifting question.

### C70: the geometric implication and the ring-isomorphism question

Pro early L1561–1565 defines L(K) by scissor relations. At L1804–1806 the author asks about the graded quotient; L1807–1816 then asks whether γₙ(X)=0 implies ruledness and gives the supersingular product as a negative example.

For a supersingular elliptic curve E over an algebraically closed field, E² has algebraic H² and is not ruled. This proves the stated geometric implication is false. To conclude that the displayed graded-ring map is not injective, one must additionally prove that the class of E² is nonzero in the relevant quotient. Nonruledness of one representative is not that proof. In particular, freeness on birational classes cannot be silently inserted for the associated graded of the full scissors ring.

Suggested change: split C70 into the geometric assertion, refuted by the author's example, and the exact graded-ring identification, left at the bounded status already appropriate to its class C. Alternatively narrow C70's statement and fate to the geometric implication and keep the ring question in its problem record. The existing root_checks.md proof itself correctly stops at nonruledness.

### C110: normalize the residue map

Milne, Arithmetic Duality Theorems, II Proposition 2.1 and Remark 2.2(a), printed pp.163–165, gives the global sequence with the sum of local invariant maps. For a smooth proper geometrically connected curve C over a finite field and U=C\\{x₁,…,xᵣ}, r≥1, its prime-to-characteristic part is

\[
0\longrightarrow \operatorname{Br}(U)\{\ell\}
 \longrightarrow(\mathbf Q_\ell/\mathbf Z_\ell)^r
 \xrightarrow{\;\sum\;}\mathbf Q_\ell/\mathbf Z_\ell
 \longrightarrow0.
\]

Each local invariant identifies its summand with Q_l/Z_l. In the equivalent residue-field formulation, corestriction is the identity under the identification by evaluation on the local Frobenius; restriction, rather than this corestriction, carries the residue-degree multiplication.

Consequently the kernel is isomorphic to (Q_l/Z_l)^(r−1), and is zero for r=1. The root answer is correct. Replace “a nonzero finite-degree map” by “an isomorphism under the normalized local invariant.” A multiplication-by-degree interpretation would have a finite kernel and would not justify the asserted exact zero for one puncture. The theorem label is Proposition 2.1, not Theorem 2.1.

Primary text opened: https://www.jmilne.org/math/Books/ADTnot.pdf

### C104–C105: a fully specified constant-Jacobian calculation

Let C/F_q be a smooth proper geometrically connected curve of positive genus, J=Jac(C), A=J×C, and l different from the characteristic. Use geometric Frobenius and put

\[
V=T_\ell J\otimes\mathbf Q_\ell.
\]

This is the homological Tate module, of weight −1. The canonical Jacobian comparison gives H¹(Cbar,Q_l)=V^∨, so

\[
H^1(Cbar,V)=V^\vee\otimes V=\operatorname{End}(V).
\]

The group H²(Cbar,V)=V(−1) has weight 1 and hence no Frobenius invariant. Hochschild–Serre therefore gives

\[
H^2(C,V)=\operatorname{End}(V)_F.
\]

Frobenius on an abelian variety over a finite field is semisimple, so conjugation on End(V) is semisimple and the natural invariant-to-coinvariant map is an isomorphism. Tate's finite-field Hom theorem gives

\[
H^2(C,V)\simeq\operatorname{End}_{\mathbf F_q}(J)
                 \otimes_{\mathbf Z}\mathbf Q_\ell.
\]

The identity is nonzero. End over the algebraic closure would in general be the wrong group. No additional twist is needed with V defined as above; a formulation using cohomological H¹(J) instead of its dual must insert the corresponding dual/polarization twist.

There is also a direct completion of the argument for the actual torsor group H²(C,A). Milne II Proposition 5.1 says that H¹(C,A) is torsion and that its l-primary part has cofinite type. Thus its l-adic completion is finite. The inverse Kummer sequence, displayed as (5.2.1) on printed p.199, is, because C is proper,

\[
0\to H^1(C,A)^{\wedge_\ell}
 \to H^2(C,T_\ell A)
 \to T_\ell H^2(C,A)\to0.
\]

After tensoring with Q_l the first term vanishes. It follows that

\[
V_\ell H^2(C,A)\simeq H^2(C,V)\ne0.
\]

This proves that literal H²(C,A)=0 also fails for this example. It does not identify the torsion group itself with a rational vector space, and does not use the Sha-finiteness premise of Milne II Theorem 5.2(c).

For an explicit example, the independent program finds the smooth elliptic curve E/F₅ with equation y²=x³+3x+2. It has five rational points, trace 1, and Frobenius polynomial T²−T+5. For C=J=E the End invariant/coinvariant space has dimension 2, and hence V_l H²(C,E×C) has dimension 2.

Primary text opened: https://www.jmilne.org/math/Books/ADTnot.pdf, II §5, Proposition 5.1 and equation (5.2.1), printed pp.197–199. Tate's theorem is the root's separately checked primary input; I have not independently re-proved it.

## 2. Counterexamples which passed the independent review

### Legendre: both twists have the stated direction

Stacks tag 03VA was opened and read directly. It gives the all-extension trace identity used in the root proof, with vanishing H_c⁰ and H_c². At q=5 the right side is 2 for every extension degree. Finite-dimensionality and invertibility of Frobenius then determine the semisimplified eigenvalue multiset of H_c¹ as {1,1}; this is not an inference from the finite point-count sample.

The polarization is V^∨=V(1), and duality is

\[
H^1(Ubar,V)=H_c^1(Ubar,V^\vee)^\vee(-1).
\]

The successive eigenvalues are 1, 1/5, 5, 25. Therefore the ordinary H¹ weight is 4, and replacing V by V(2) gives coefficient weight −3 and H¹ eigenvalues 1. Geometric H⁰ vanishes, so the Hochschild–Serre edge identification is correct. Semisimplicity of H¹ is unnecessary for nonzero arithmetic H¹: any nonzero finite-dimensional space on which all eigenvalues are 1 has a nonzero fixed vector.

All relevant geometric hypotheses hold: U is the smooth affine curve A¹\\{0,1}; the coefficient comes from a smooth proper family of elliptic curves; q=5 avoids the singular characteristic; l≠2,5 is sufficient. The final claim remains conditional on the manuscript allowing arbitrary lisse geometric coefficients.

Primary source: https://stacks.math.columbia.edu/tag/03VA

### SNC arithmetic H⁴: dimension 4 is correct

I independently constructed both signed incidence matrices for the four coordinate planes. Their ranks are 3 and 3 and their product is zero. The three nonzero stratum rows have cohomology dimensions (1,0,1), (1,3,0) and (4,0,0), respectively.

For D equal to the union of the coordinate planes in P³, this gives

\[
H^2(Dbar)=\mathbf Q_\ell\oplus\mathbf Q_\ell(-1),\quad
H^3(Dbar)=\mathbf Q_\ell(-1)^3,\quad
H^4(Dbar)=\mathbf Q_\ell(-2)^4.
\]

The mixed-weight decomposition in H² is legitimate: the two Frobenius eigenvalues are distinct. Künneth for X=D×P¹ gives

\[
H^3(Xbar)=\mathbf Q_\ell(-1)^3,\qquad
H^4(Xbar)=\mathbf Q_\ell(-1)\oplus\mathbf Q_\ell(-2)^5.
\]

After twist (1), the arithmetic H⁴ has a three-dimensional coinvariant contribution from H³ and a one-dimensional invariant contribution from H⁴. Its dimension is 4. The strata are split and the relevant Frobenius actions are scalar, so a hidden unipotent extension does not alter this count.

X is proper and of finite type over F_q (and over Z), but singular. This refutes the unrestricted question; it does not refute the smooth proper statement. The root proof makes that distinction correctly.

### Howe, Enriques and the section/retraction argument

Howe's Theorem 1 was opened. The parameter t=2 over C satisfies t(t²−1)(t²+1)=30≠0, the characteristic is not 2, and the characteristic-11 exceptions do not apply. The two genus-two curves are geometrically nonisomorphic but have isomorphic unpolarized Jacobians. A rational map from a rational fibre to a positive-genus curve is constant. Thus a dominant map C′×P^m→C factors through C′, and Riemann–Hurwitz forces degree 1. The contradiction is valid. The adjective “unpolarized” is essential.

For the complex Enriques surface, the opened Dolgachev text supplies q=p_g=0, 2K=0, b₁=0 and b₂=10. Poincaré duality gives b₃=0; Lefschetz (1,1) gives algebraicity of rational H². The inverse intersection matrix constructs the Tate splitting in rational homological motives. Nonzero pluricanonical sections exclude a dominant separable rational parametrization by P² after resolution; a parametrization by a larger projective space restricts generically to one by P². No claim about an integral or full Chow motive is needed. Preserve the manuscript's > versus ≥ reading alarm: this counterexample addresses vanishing of positive primitive pieces, not vanishing of the unit.

Finally, s:C→C×P¹ is a regular nondominant map and p∘s=id_C. Contravariant functoriality and γ¹(C)≠0 contradict sending s to zero. All irreducibility and dimension conditions in the displayed source are satisfied. This argument does require the proposed functor on these regular maps, not merely on dominant rational maps; the root statement expressly uses that unrestricted interpretation.

Primary sources: https://arxiv.org/pdf/math/0304471, Theorem 1; https://arxiv.org/pdf/1412.7744, §3, printed pp.6–7.

### Analytic versus algebraic Lie dimension

The valuation argument for the roots of T²−T+5 is correct. The primes generated by the two roots are distinct primes above 5, so there is no nontrivial multiplicative relation. The algebraic torus generated by this Frobenius has dimension 2. For l≠5, an open congruence subgroup of its compact procyclic closure is an infinite procyclic pro-l group, hence has analytic dimension 1.

The independent elliptic-curve count above realizes the polynomial geometrically, so this can be made an actual cohomological example. It separates the analytic and algebraic candidates; it does not prove that no other l-independent one-dimensional Lie motive exists. C87's class C and current qualification are appropriate.

## 3. Review disposition for every requested claim

| Root claim | Review disposition |
|---|---|
| C65 | Retraction counterexample valid under the stated unrestricted functorial interpretation. |
| C66 | No false theorem asserted; the finite/compact maximal-subobject issue remains appropriately bounded. |
| C67 | Restrict the polynomial units observation to the literal polynomial interpretation; source context supports rational-function brackets. |
| C68 | Howe parameter, unpolarized hypothesis, factorization and Riemann–Hurwitz all check. |
| C69 | Rational homological Enriques example checks; retain positive-index and rational-equivalence-scope qualifications. |
| C70 | Geometric ruledness implication refuted; graded scissors-class nonvanishing is an additional unproved step. |
| C74 | P¹ counterexample valid when M_n means weight ≤n; a competing dimension-filtration reading remains a scan question. |
| C75 | Legendre ordinary H¹ weight 4 is correct for the unrestricted lisse-coefficient interpretation. |
| C76 | V(2) has weight −3 and nonzero arithmetic H¹; no semisimplicity gap. |
| C87 | Dimension separation valid; does not rule out all possible analytic-Lie motivic constructions. |
| C101 | Missing quotient in the lattice long exact sequence is decisive; the trivial Z test is correct. |
| C102 | The source's finite-kernel correction is sufficient for its finiteness comparison; no stronger integral isomorphism should be inserted. |
| C103 | Finite rational-point torsion is lost by rationalization; the explicit elliptic curve above supplies a nonzero finite example. |
| C104 | Correct after specifying End over F_q and V as the homological Tate module. |
| C105 | Rational counterexample checks; the Kummer argument above also proves actual H²(C,A) nonzero. |
| C106 | The bounded status is appropriate; no unrestricted Brauer–Sha formula was established by this review. |
| C107 | The bounded general-base status is appropriate; dimension-one duality is not a proof in arbitrary dimension. |
| C108 | The prime-to-p finite-error local conclusion is consistent with the qualified local-duality theorem; no issue found. |
| C109 | Kummer decomposition requires l invertible and the stated limit/completion terms; these qualifications are retained. |
| C110 | Corank r−1 and the one-puncture zero are correct; fix the normalization wording as above. |
| C111 | Singular SNC example has arithmetic H⁴ dimension 4; the smooth proper exception is essential and correctly retained. |

## 4. Reproducibility and evidence limits

The independent program is programs/crosscheck_root.py. It was executed successfully, and outputs/crosscheck_root.json contains the matrices, ranks, point counts, Frobenius dual-action matrix, invariant/coinvariant dimensions and all assertion outcomes. outputs/crosscheck_root_run.txt saves its complete stdout.

The separate crossreview/ directory records the additional opened-source requests, reading log and check events. The original late-scope totals and validation bundle are unchanged. This review did not independently reprove the existence theorem of Howe, Tate's Hom theorem, Deligne's weight theory, or general cohomological descent. It checked the exact hypotheses used here and supplied the written elementary deductions and independent finite calculations. No scan image was available and no diplomatic text was changed.

