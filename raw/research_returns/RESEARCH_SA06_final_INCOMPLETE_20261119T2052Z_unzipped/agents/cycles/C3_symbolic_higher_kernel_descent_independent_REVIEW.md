# Independent complete review of symbolic higher-kernel descent

**Mathematical PASS, with the exact HG field-K3 source qualification retained. Auxiliary result; no main-gate movement.**

Reviewer: GPT-6 Astra Pro (OpenAI), `/root/cycles_continuation`, RESEARCH_SA06; reasoning effort not separately exposed.

The entire `../frobenius/C3_symbolic_higher_kernel_descent_RESEARCH.md`, SHA256 `85b47038007a3a86d8468f3b48bc759056f0f783fb25630f6710ee716e7fa551`, was read, including HD.1–HD.4 displays, all six proof sections and the source ledger. I independently reconstructed the argument and the geometric smoothness calculations. A source-label correction to the final ledger was requested and is explained below; it does not change the mathematics.

## Point fields and the imperfect-field construction

Only finitely many point-supported K2 terms occur. Splitting their maximal separable residue subextensions by one finite Galois extension leaves a product of purely inseparable fields. Separability of this base change makes the tensor products reduced. If the residual extension has exponent e, bilinearity gives p^(2e){a,b}={a^(p^e),b^(p^e)}. The latter symbol is defined over the new base field. Thus rational K2 coefficients descend without a purely inseparable extension of the parameter curve.

The projection formula then gives constant symbols times the actual point-divisor class, retaining its inseparable degree. On a regular curve the Cartier formula [O_a]=[O_C(a)]-1 remains valid for every closed point, since an invertible module over its residue field is trivial. The constant ET.9 degree matrix still suffices.

The extension of VE to the infinite imperfect field has the necessary extra choices. The high-twist sections defining the evaluation divisors are chosen with geometrically reduced zeros and poles, hence finite-etale supports. Without this choice an inseparable support point could obstruct geometrically simple zero interpolation. The required conditions are nonempty open first-jet conditions on affine coefficient spaces over the infinite field. Both prescribed rational endpoints are retained. The extra simple zero can be at a finite separable point and need not be rational.

In odd characteristic, requiring both h and h+4 to have simple geometric zeros handles all branch points. If the chosen unit is -1, the endpoint lies over h=-4 and the nonzero derivative is imposed there. In characteristic two the simple-zero Artin–Schreier local equation is smooth. At the pole a0, clearing denominators gives unit linear coefficients at g=0 and g=infinity, so the boundary points are smooth and rational. This proves smoothness over the actual base, rather than inferring it from regularity over an imperfect field. The original marked Dennis–Stein and descent calculations then apply with the genuine residue pushforwards; the unit1 still gives literal zero.

## Independent check of the symbol curve

For (f-1)^2(g-1)^2=c f g with c nonzero, the unique point over f=0 is (0,1), and its derivative in f is -c. Every geometric component dominates the f-line, since there is no vertical component, and would contain this unique smooth point. Hence there is exactly one geometric component, and it is reduced. The other three boundary points are smooth by the identical inverse-coordinate calculation.

In characteristic two the interior derivatives are -cg and -cf, which are nonzero there. In odd characteristic, dividing the equation and its derivative equations at an interior singular point forces f=g=-1 and c=16. Writing f=-1+x,g=-1+y gives quadratic term 4(x^2+y^2). It has two distinct tangent lines because the characteristic is not2 and the algebraically closed constant field contains a square root of -1. The normalization is smooth; in this exceptional case the curve is itself defined over the constant field. The only singular requested endpoint is a=b=-1, whose Milnor symbol is2-torsion and can be discarded rationally. Every other requested endpoint is smooth and remains rational on normalization. Thus the proper K2 symbol construction is valid in the stated imperfect-field scope.

## Actual separable descent and exact endpoints

For the finite separable extension L/F, after a finite Galois splitting extension the Weil restriction is the product of the conjugate smooth projective curves. It is consequently smooth and geometrically connected. The projective model can be descended using the tensor product of the conjugate ample line bundles, with its permutation descent datum. This is not an assertion that projectivity descends without an ample line bundle.

The universal evaluation map followed by finite flat perfect pushforward gives an actual class over E_F times that Weil restriction. Tor-independent finite flat base change identifies its two fibres with the traces of the original two fibres. A smooth geometrically connected proper curve through the two rational endpoint tuples exists by the same geometric Bertini argument. Thus trace preserves the exact proper-family subgroup. No purely inseparable Weil restriction is used, where properness would fail.

Finally r commutes with restriction. Hence r^2 res(kappa)=res(r^2 kappa), and projection formula gives its trace equal to [F':F]r^2 kappa. There is no need to commute r with pushforward on arbitrary classes. Rational division gives HD.1. For the original component tuple, the constant h0 construction supplies an actual HK family over k(u); its zeros and branch values satisfy the above smoothness checks. Applying HD.1 therefore produces the exact whole-exceptional endpoint over k(u) required before RF. It still supplies no ambient family lift or node cancellation.

## Source-label correction and exact reading scope

I freshly opened and read all printed text of Stacks Section97.11, Tag05Y8. It supplies restriction-of-scalars representability and base-change, but does not state a properness theorem. Its Lemma97.11.4 explicitly omits its functorial proof; I do not describe that omitted proof as freshly read. The owner's final ledger should attribute those scopes to this section and obtain properness from the split-product description and fpqc descent.

I also freshly opened and read the complete printed statements/proofs of Stacks Lemma35.23.16, Tag02L1; Lemma39.25.3, Tag0CCJ; and Lemma37.50.1, Tag0B45. These give properness descent, effective finite locally free descent of the projective scheme, and the proper-plus-ample projectivity criterion. The short displayed proofs invoke their listed earlier lemmas; not every foundational predecessor was freshly reopened. The symmetric ample-line descent is the explicit argument above.

- The Stacks Project Authors. (2026). *Restriction of scalars*, Section97.11. https://stacks.math.columbia.edu/tag/05Y8
- The Stacks Project Authors. (2026). *Properties of morphisms local in the fpqc topology*, Lemma35.23.16. https://stacks.math.columbia.edu/tag/02L1
- The Stacks Project Authors. (2026). *Descending quasi-projective schemes*, Lemma39.25.3. https://stacks.math.columbia.edu/tag/0CCJ
- The Stacks Project Authors. (2026). *Projective schemes*, Lemma37.50.1. https://stacks.math.columbia.edu/tag/0B45

All existing VE/bq/ET.9, regular localization, Matsumoto, perfect pushforward and HG coherent-operation source audits are reused at their recorded scopes. The extra field input FK retains exactly HG's qualification concerning the original motivic spectral-sequence and Adams-compatibility construction. No general singular purity, purely inseparable parameter properness, or unproved symbolic ambient lift is imported. The actual supported-node gate and UK.7 remain unchanged.

Saved: 2026-11-19T20:38:55.633094+00:00
