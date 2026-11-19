# Independent supplement: cote 93, scans 189–213

Run SA04; reviewed 19 November 2026 by GPT-6 Astra Pro, reasoning effort inherited and not separately exposed. These are new checks in this run. A source comparison is not counted as a proof. Source locators are relative to `source/SA04_texts/`. The manuscript layer is undated; publication dates below do not date these sheets. No novelty claim is made.

## C-SA04-702: the rational Verschiebung-lift criterion is false

### Exact source and retained hypotheses

`codex/K93-05_transcription.tex`, scan 197, line 99, explicitly takes an integral finite-type scheme S dominating Spec Z. Scan 198, lines 104–106, then asks whether a section ω of an abelian scheme A/S is torsion if, at every closed point s, its reduction lifts through Verschiebung A_s^(p) → A_s. The question is introduced as a consequence suggested by part a) of c), not as a requirement that the section retain a specified lift to a universal vector extension. The following example satisfies the stronger, arithmetically meaningful interpretation: each lift is over the residue field k(s) itself. It does not merely use fppf-local surjectivity.

Let S = Spec Z[1/30], let A be the smooth projective elliptic scheme with affine equation

    y² = x³ − 2x,

and let P = (2,2). Its discriminant is 512, which is invertible on S. Thus A/S is an abelian scheme, S is integral and of finite type over Z, and S dominates Spec Z. Every closed residue field is F_p for a prime p ≥ 7.

### Every closed reduction has a rational Verschiebung lift

The point T = (0,0) is a nonzero point of order two on every such reduction, so N_p = #A(F_p) is even. Hasse's inequality gives

    0 < N_p ≤ p + 1 + 2√p < 2p       (p ≥ 7).

The only positive multiple of the odd number p strictly below 2p is p, which is odd. Therefore p does not divide N_p. Multiplication by p is consequently a bijection of A(F_p).

Relative Frobenius F:A→A^(p) is a bijection on F_p-rational points, and V∘F = [p]. Hence V:A^(p)(F_p)→A(F_p) is also a bijection. In particular, P modulo p has a rational Verschiebung lift at **every** closed point of S.

The needed Hasse estimate is opened in James S. Milne, *Elliptic Curves*, second edition, World Scientific, 2021, Chapter IV, §9, Theorem 9.4, printed p. 150 (PDF p. 154), [author PDF](https://jmilne.org/math/Books/EC2.pdf). Relative Frobenius and the identities VF=FV=p are opened in Ching-Li Chai and Frans Oort, *Moduli of abelian varieties and p-divisible groups*, Clay Mathematics Proceedings8 (2009), §§10.23–10.24, printed pp.530–531, [publisher volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip08c.pdf). These citations support the ingredients; the parity argument and its application here are independently written above.

### P has infinite order

The same elliptic curve has good reduction at both 3 and 5. Direct enumeration, saved in `programs/b_supplement_computations.py` and `outputs/b_supplement_computations.json`, gives #A(F_3)=4 and #A(F_5)=10. The rational torsion subgroup injects under these good reductions, so its order divides gcd(4,10)=2. Since P is neither the identity nor a point with y=0, P is not of order one or two. It therefore has infinite order.

The specialization result is opened in Milne, Chapter II, §5, Corollary 5.7, printed p. 66 (PDF p. 70); the adjacent Proposition 5.4 and proof on pp. 66–67 identify the torsion-free formal kernel. Only the good primes 3 and 5 are used. These primes may be omitted from S while still being used to prove a fact about the rational generic point. As an additional exact check, the program gives 2P=(9/4,−21/8).

This refutes scan 198 e), including rational lifts at every closed point, and is a refinement of root claim C-SA04-644. It does **not** refute the p-curvature conjecture: passing to the underlying abelian section discards the connection or universal-vector-extension data appearing in scan 197 c). The present counterexample is an independent argument in this audit, not a claim that the manuscript contains it and not a claim of historical novelty.

## C-SA04-700/701: zero p-curvature does not make every quasi-coherent module locally trivial

Scan 189, `codex/K93-04_transcription.tex:306–320`, defines a trivial object as f*F with the canonical connection and then asserts an equivalence of Zariski-local triviality, étale-local triviality, flatness with zero p-curvature, and descent to Λ=O_S[O_X^p], for quasi-coherent E.

Under the ordinary interpretation of localization on X over the fixed base S, take S=Spec F_p, X=A¹_S, and E=O_X/(x^p), with the connection induced by d. The ideal (x^p) is stable under every derivation. The connection is flat and has zero p-curvature: on the quotient its operators are induced by derivations on the structure sheaf, so ∇_D^p=∇_(D^[p]). It is exactly the Frobenius pullback of O_(X')/(u).

At the origin E has nonzero torsion, and away from it E is zero. It cannot become a vector-space pullback under an étale neighborhood of the origin. Such a pullback is free, and faithful flatness preserves the nonzero annihilator obstruction. Thus the stated quasi-coherent local-triviality equivalence fails under this interpretation. If the phrase “localization of (X→S)” allows changing the base in an unusual non-Cartesian category, that category must be specified before assigning a different verdict; mathematics alone does not settle the transcription.

The correct Cartier equivalence is between quasi-coherent modules on X' and quasi-coherent modules on X with integrable connection and zero p-curvature, assuming the smooth characteristic-p or local p-basis hypotheses. This exact smooth formulation is opened in Katz1970 Theorem5.1, printed pp.190–191, [author-hosted primary text](https://web.math.princeton.edu/~nmk/old/nilpconn.pdf). For finite locally free modules, descent preserves and reflects local freeness, so a descended bundle can be trivialized locally and its pullback has a horizontal frame. The vector-bundle local-triviality version is therefore valid. C-SA04-700 records the literal counterexample; C-SA04-701 records the surviving exact equivalence, rather than silently replacing the source's category. Line320 also mixes a coherent source with a quasi-coherent target; the full equivalence must use matching categories.

## C-SA04-705: the literal tensor-power p-curvature target needs correction

On scans 208–209, `codex/K93-06_transcription.tex:72–123`, the displayed target uses (Ω¹)^(⊗p), and the Cartier defect is written as ω^(⊗p)−F*C(ω). For a flat connection, intrinsic p-curvature is Frobenius-linear on vector fields; its sheaf target is End(E)⊗F*Ω¹_(X'/S). For a line bundle, omit End(E).

There is no general identification of F*Ω¹ with the full p-fold tensor power when the relative dimension exceeds one. In characteristic two on a surface, the literal expression (dx+dy)⊗(dx+dy)−dx⊗dx−dy⊗dy equals dx⊗dy+dy⊗dx, which is nonzero. It therefore cannot define the claimed additive Frobenius-power map into the ordinary tensor square. The exact four-coordinate calculation is saved in `b_supplement_computations.py`.

On a curve the line-bundle identity F*Ω¹≅(Ω¹)^⊗p makes the notation harmless. In higher dimension an intended Frobenius-power submodule in Sym^pΩ¹ may also repair the notation. These are possible readings, not permission to alter the source. The check is conditional on interpreting the printed ⊗ literally.

## C-SA04-706: the kernel label in equation (4.1)

Scan 212, `codex/K93-06_transcription.tex:178–194`, defines the nilpotent locus using the formal completion of the vector p-curvature target, but equation (4.1) labels the kernel Pcip, the zero-p-curvature locus. Its kernel must instead be Pcin, the nilpotent locus. The subsequent equation (4.2) distinguishes the two correctly.

For an explicit test take S=Spec(F₂[ε]/ε²), X=A¹_S, and the line-bundle connection ∇=d+εx dx. It is flat. For D=∂/∂x, D²=0 in characteristic two and

    (D+εx)² = ε,

because the two mixed xD terms cancel and ε²=0. Thus its p-curvature is nonzero and square-zero. It belongs to Pcin but not Pcip, while mapping to zero in the quotient of the p-curvature vector sheaf by its formal completion. This contradicts the literal kernel label. The saved matrix [[0,1],[ε,0]] on the quotient with basis 1,x squares to εI; the displayed differential-operator argument proves the assertion on the full polynomial ring.

## C-SA04-707/708: the universal Verschiebung extension and its vector pushout

Work over a perfect field of characteristic p and in the category of commutative finite-type group schemes with fppf-exact extensions. Let B be an abelian variety, α=ker(V_B:B^(p)→B), and let H be affine with V_H=0. For any extension 0→H→E→B→0, naturality of Verschiebung makes V_E vanish on H^(p). It descends through E^(p)/H^(p)=B^(p) to a map u:B^(p)→E lifting V_B. Restrict u to α to obtain h:α→H. The map (z,t)↦u(z)+t identifies the pushout of the Verschiebung extension along h with E. Any other lift differs by a group map B^(p)→H, which is zero: a morphism from a proper geometrically connected abelian variety to an affine group is constant, and a group homomorphism sends the identity to the identity. This proves uniqueness and universality in this exact category. The general-base version is not inferred.

Put A=B*. Cartier duality identifies α^D with β=kerF_A, a height-one group with Lieβ=LieA. For finite commutative group schemes over a field, primitive elements in O(α)=O(β)* are exactly linear functionals on the augmentation ideal modulo its square; hence Hom(α,Ga)=Lieβ=LieA. It follows that the universal map to vector groups, when maps between vector groups are required to be linear, has target the vector space Lie(A)^dual. Since Verschiebung is zero on vector groups, applying the preceding universal extension to these targets yields the universal vector extension of B as the pushout along α→Lie(A)^dual.

The word linear matters: in characteristic p, group homomorphisms between vector groups include additive polynomials, so this is not a universal property with all such morphisms. The finite group being enveloped is α, not β. For example β=μ_p has no nonzero maps to Ga, despite having a one-dimensional Lie algebra; interpreting the source's nearest antecedent as β would give a wrong formula. The source's concluding arrow from α supports the corrected interpretation, but no ink-level reading is claimed.

Chai–Oort §10.24 supplies the natural Verschiebung construction. The standard vector-extension Hom-to-Ext universal property is directly opened in Fonseca–Matthes2022 §2.2, pp.2–3, which cites Mazur–Messing PropositionI.1.10. Searches did not locate an opened primary theorem with precisely the manuscript's Vkilled-affine universal formulation. The proof above establishes the mathematical statement under explicit hypotheses; it does not establish its historical provenance or novelty.

## Relation to the remaining root audit

The main claim register must keep the relative pro-étale reconstruction question separate from the finite-monodromy theorem over an algebraically closed field. It must also preserve the condition that a **given stratified line bundle**, not only its underlying line bundle, have a prime-to-characteristic tensor power trivial as a stratified object. The complete reconstructed statements, bibliographic limits, and hypotheses are in C-SA04-698/699 and the supplementary problems register.

