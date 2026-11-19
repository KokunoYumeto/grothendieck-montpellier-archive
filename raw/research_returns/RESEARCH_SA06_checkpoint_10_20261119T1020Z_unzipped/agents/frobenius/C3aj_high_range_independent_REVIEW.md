# Independent complete-proof audit: C.3aj

**Outcome: passed.** Frobenius read the entire typed draft `research/agents/real_weil/C3_high_range_surjectivity_draft.tex`, its auxiliary product Hodge fragment, and the precise source passages. Final certification: tool clock **2026-11-19 09:26:20 UTC**. The requested explicit complex-conjugation sentence was added by the owner and reread before certification.

## Exact assertion

For every r≥2 and N≥2r+2, the construction supplies an algebraizable excellent normal strict-local complex ring with regular punctures X and Y, and an integral cokernel map onto Pic^0(C)(C)/Pic^0(C)(Kbar). The countable algebraically closed field Kbar contains all finite construction data. The quotient is nonzero and uniquely divisible. This proves rational nonsurjectivity of ordinary algebraically trivial cycles in this entire range.

The quotient by Kbar is essential: the incidence boundary is proved constant on every proper family, not identically zero as a divisor class. The proof does not silently replace the boundary by zero.

## 1. Geometry and fields

The jointly Hodge-generic tuple of quartics exists with the stipulated NS groups, rational endomorphism fields, and pairwise nonisomorphic transcendental structures. The finite coefficient field K0 is countable even though its selected complex embedding is Hodge generic. The finitely many independent section coefficients produce a further countable field K.

The external line bundle M is very ample. General m+1 sections have smooth transverse base locus of expected codimension or empty base locus. This and the rank-three condition are independent nonempty Zariski opens over K0, so the specified algebraically independent coefficients satisfy both.

The incidence divisor H is smooth at the base locus because its section differentials are independent. Its projective-bundle open is integral and the exceptional part has codimension m≥2. The construction F+tℓG has the stated line-bundle degree, is smooth near its exceptional V, and is integral: its graph is dense and the locus F=ℓG=0 has codimension two in the smooth base and cannot be another divisor component. The full Segre contraction, normalization and proper shrinking yield the same regular strict-local model mechanism as C.3ae. The connected exceptional fibre implies a single point over the vertex. The full coordinate set generates the exceptional ideal, regardless of the base locus of the chosen linear section ℓ.

The strict transform of f=tℓ is Tot(L_H^−1), is smooth, and meets V transversely in H. All geometry preceding complex base change is defined over Kbar. Dimension is m+2r=N.

## 2. Integral incidence and boundary calculation

With s=r−1, τ=product(4D_ν−H_ν), the operator Φ_P has codimension one on C×P. It uses only divisor intersections and proper pushforward, so it does not assume p:H→S is flat. Its exact identities are

`p_* h^(m−1)=1`, `p_* h^m=a`, and `p_* h^(m+j)=0` for j≥1.

For boundary classes γ∈CH^(r−1)(H×P), weak Lefschetz gives an ambient lift of the H^(2r−3)(H)⊗H1(P) cohomology component. It does not claim a Chow lift. Writing that lift as Σh^jζ_j yields exactly

`Ψ_*(ζ)=pr_C,* τ(2a ζ_0 + a² ζ_1)`.

Every relevant odd class has its odd degree on C. A K_C insertion gives H3(C)=0. A W_ν degree-four term is killed by τ_ν. In the other terms there are exactly j+1 missing degree-two factors, so a^(j+1) must insert a hyperplane in one or more missing positions; the product includes deg(τ_νH_ν)=0. Thus the mixed component vanishes for all ambient cohomology classes. The classifying homomorphism of parameter Jacobians is zero, so the line bundle has equal fibre classes integrally.

## 3. The countable boundary subgroup

Every cycle on the smooth projective H_C is ordinarily algebraically equivalent to a cycle over Kbar. For an integral component, its fixed-polynomial Hilbert scheme is projective of finite type over the algebraically closed Kbar. Its irreducible component is defined over Kbar and contains a Kbar-point. A chain of proper integral curves, normalized, joins that point to the chosen complex point. The universal flat family gives actual proper-curve equivalences with integral coefficients. Lower-dimensional or embedded components do not affect the fundamental cycle in the fixed dimension.

Since Ψ kills such differences and is defined over Kbar, its entire image lies in Pic(C)(Kbar). Localization and self-intersection therefore make ρ on the actual strict-local puncture well defined modulo exactly that subgroup, including rational-equivalence witnesses and changes of closure. Refined restriction and proper pushforward commute with parameter fibres. No finite-type parameter space for cycles on the puncture is invoked.

Pic(C)/Pic(C)(Kbar) is naturally Pic^0(C)/Pic^0(C)(Kbar), since all degree classes have a Kbar representative. Divisibility is inherited from complex Jacobian points. If nλ is Kbar-rational, every point of its finite [n]-fibre is Kbar-rational, proving torsion-freeness and hence unique divisibility.

## 4. Chern obstruction and the Hodge calculation

The conormal exterior-power sequence is exact, with kernel L⊗Ω^(r−1). Its connecting homomorphism is contraction with the first-neighbourhood deformation class. The rational Chern-character isomorphism for the finite-dimensional regular projective model supplies a virtual bundle for any chosen cycle closure. Its Hodge Chern class lifts through the middle conormal term by its Atiyah class. Refined restriction is compatible with the Chern character. Thus the stated contraction vanishes; no sufficient lifting criterion is asserted.

The deformation class has only a C-tangent component. In the selected target summand, a projective-space differential cannot disappear, so h^j b_j with j>0 contributes nothing. Nor can a W factor with another differential or cohomological degree enter. The only relevant b0 component is the selected tensor of H1(Ω1) on every quartic, H0(K_C), and H1(O_P).

The auxiliary Hodge lemma proves that the rational antecedent has every W factor in NS. For each quartic, the common kernel of multiplication by all linear forms on H1(Ω1) is precisely the hyperplane line; the Jacobian-ring dual calculation proves this for every smooth quartic. Since τ_ν is independent of H_ν, some w_ν has μ_wν(τ_ν) nonzero. The special three sections (product w_ν)z_i give three independent target vectors with coefficients x_i. This proves the rank-three open condition. It does not claim this special witness tuple has good base locus.

All NS tensors with a hyperplane factor are killed. The remaining τ tensor coefficient in H0(K_C)⊗H1(O_P) must vanish by the rank-three map. Its complex conjugate vanishes because the original cycle, Kunneth projections and NS tensors are rational. This last explanation is now explicit in the typed file. It gives zero full mixed component.

## 5. Actual source families and integral target

The exact source formula is `Φ_P(b|_H)=pr_C×P,* τ(b0+a b1)`. The b0 mixed component vanishes by the Chern obstruction and τ_νH_ν=0. The b1 mixed component has one missing W degree-two factor, forcing the a insertion into that factor and giving the same zero intersection. Consequently every actual proper-curve source-family difference is killed by ρ. Compactifying a smooth open curve and closing its cycle on the fixed product retains its original fibres, so this covers ordinary algebraic equivalence.

The target θ uses only first Chern classes of pulled-back line bundles, so it remains defined for the nonflat incidence projection. Its Poincare family provides actual ordinary algebraic equivalences. Direct pushforward gives ρθ=(-9)^s times the Jacobian class modulo Kbar. Divisibility provides the integral cokernel surjection.

The chosen q=(u:v:1), u transcendental over Kbar and v^4=−1−u^4, has no nonzero multiple of its Abel difference [q−o] over Kbar. Finiteness of [n] and the Abel closed immersion prove this. Hence the quotient is nonzero and the failure persists after rationalization.

## Opened primary sources in this audit

- The complete product Hodge source audit is in C3_product_Hodge_source_audit.md, reusing the exact Brevik–Nollet, Huybrechts, CDK, Zarhin and Beauville passages and adding Milne's exact D10 representation locators. The product lemma was independently read and passed by real_weil before the full C3aj audit.
- Grothendieck, *Techniques de construction… IV: les schémas de Hilbert*, Bourbaki exposé 221 (1961), full primary scan https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf opened as turn203735446view0. Theorems 3.1–3.2, printed pp.259–260, the projectivity proof and Hilbert specialization pp.264–266 were read from the local primary transcription. The separate erratum, printed p.302, was also read completely; its corrections do not alter the fixed-polynomial projective Hilbert theorem used here. Owner's local PDFs and acquisition/hashes are retained.
- Stacks Lemma 42.58.1, Tag 0FEY, reopened as turn876918694view0: rational Chern character isomorphism for a quasi-compact regular scheme, finite type over a Noetherian base with dimension function, affine diagonal and bounded relative dimension function. These hypotheses hold for the projective regular model over the excellent local base.
- Stacks Remark 42.59.9, Tag 0FF8, reopened as turn610205893view1: compatibility of Chern classes and Chern character with lci Gysin and the fundamental class. This is precisely the restriction step used.

No remaining mathematical gap was found. This proof audit does not verify unneeded claims about all cohomological Kunneth summands, unrestricted cycle deformation, or an unquotiented Pic(C) invariant; the typed statement does not make those claims.
