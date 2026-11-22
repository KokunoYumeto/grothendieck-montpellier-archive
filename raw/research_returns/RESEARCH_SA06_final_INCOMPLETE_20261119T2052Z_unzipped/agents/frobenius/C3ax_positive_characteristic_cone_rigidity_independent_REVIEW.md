# Independent audit of C.3ax

**Verdict: PASS.** We read the complete draft, now finalized at `research/sections/C3_positive_characteristic_cone_rigidity.tex` and freshly checked all three new K-theory inputs. Completion tool clock: **19 November 2026, 11:21:27 UTC**. The result is restricted to the stated strict henselian smooth projective cone construction. It makes no assertion about arbitrary local singularities.

## 1. Geometry and the abstract blow-up square

Normality and generation in degree one identify the vertex blow-up with the total space of the inverse ample line bundle. The base change to the strict henselian local ring is regular, noetherian, and proper over that ring, with exceptional divisor the original smooth projective variety. The projection to that variety is retained, so it is an actual retraction of the exceptional inclusion.

The pulled-back vertex ideal is the invertible ideal of the zero section: degree-one sections generate the line bundle. Hence its powers give exactly the split thickenings with graded pieces `O,L,...,L^(a-1)`. Since the residue field is already algebraically closed, the pointed strict henselization has the same Artinian quotients as the original local ring. Thus the thickenings in the pro-descent theorem are the asserted `V_a`, rather than different formal models.

## 2. Uniform finite detection in the procategory

KST Theorem A applies to every abstract blow-up square of noetherian schemes. It does not require resolution of singularities or characteristic zero. Its equivalent long exact sequence (1.6) gives the exact three-term segment used in the proof.

Both the local ring and each of its Artinian quotients have `K_0=Z`. These form constant pro-objects, and the first map is the graph of the structure-sheaf class. Its cokernel is canonically the constant pro-object `K_0(Z)`, via `(n,z) -> z-n[O_Z]`, up to the harmless sign convention in the Mayer–Vietoris sequence. The induced map into `{K_0(V_a)}` is therefore a monomorphism in pro-abelian groups.

This really supplies a single finite detecting level for the entire group. Represent the kernel by `H_a=ker(K_0(Z)->K_0(V_a))`. The transition maps are literal subgroup inclusions `H_b -> H_a` for `b>=a`. A pro-zero system has, for every fixed `a`, an eventually zero transition map into `H_a`. Such a map is an inclusion, so its domain is zero. Choosing one fixed index therefore gives `H_(a0)=0`. This is stronger than elementwise detection and avoids an unjustified interchange of a limit and a kernel.

## 3. Nilpotent K-theory after inverting the characteristic

Geisser–Hesselholt Theorem A, printed p. 29, explicitly concerns the nonconnective Bass-completed spectrum and every integer degree. For a nilpotent ideal in a ring in which the prime is nilpotent, the relative groups are primary torsion of bounded exponent. Thus localizing the relative spectrum at that prime kills all its homotopy groups. The bounded exponent is not required to be uniform in the degree or the thickening.

For each fixed `V_a`, use a finite affine cover. Intersections are affine because the scheme is separated. Thomason–Trobaugh Theorem 8.1, printed p. 367, gives the required nonconnective Mayer–Vietoris square for quasi-compact opens in a quasi-separated scheme. Iteration over the finite cover globalizes the affine equivalence. Localization of spectra is exact and commutes with finite homotopy limits. Thus `K(V_a)[1/p] -> K(V)[1/p]` is an equivalence, and the displayed `K_0` map is an isomorphism.

Flat localization preserves the finite-level injection. The resulting restriction `K_0(Z)[1/p] -> K_0(V)[1/p]` is injective and has the actual projection pullback as a right inverse. It is therefore an isomorphism with that inverse. No compatibility of an infinite sequence of nilpotence exponents is needed.

## 4. Rational Chow groups

The regular schemes used here have the resolution property: the finite models are projective over affine pointed-etale neighbourhoods. Each is smooth and quasi-projective over the coefficient field because it is etale over the total line bundle. Finite collections of vector bundles, cycles, and rational-equivalence witnesses descend to these models. The rational total Chern ring isomorphism on the finite smooth models passes to the strict-etale limit, by Fulton, Example 15.2.16(b), pp. 294–295. Restriction and the inverse projection pullback preserve Chow degree. Thus the isomorphism restricts degreewise; no Adams-operation assertion is needed. This records the parent’s final proof refinement after the initial audit, with the same conclusion.

The exceptional refined pullback is the lci pullback associated to its Cartier embedding. The inverse projection pullback is flat of relative dimension one in the indicated limit sense. These are correctly graded maps on codimension Chow groups.

## 5. Ordinary algebraic equivalence and localization

Both inverse maps preserve ordinary algebraic equivalence from actual fixed-product families. Flat projection pullback does so directly. Refined exceptional pullback can be performed on the actual product with a smooth proper parameter curve, and commutes with specialization at its points. No identification with local-Picard equivalence or formal families is used.

Localization gives the open Chow quotient, with boundary image identified by self-intersection as multiplication by minus the first Chern class of the ample bundle. The sign does not change the quotient subgroup. Ordinary-family localization is also right exact: closing a family in the fixed compactification gives an actual family, and any discrepancy of specified fibre cycles is exceptional. Thus the same quotient formula holds after ordinary algebraic equivalence. Rational coefficients do not alter this argument.

For the top degree on the smooth connected projective variety, ordinary algebraic equivalence identifies zero-cycles of the same degree. A connected curve chain through any pair of points supplies the actual relations. An ample complete-intersection curve has positive degree for the line bundle, so the image in the integer degree group is nonzero and its rational cokernel vanishes. The dimension-one case uses the entire curve and is included.

## 6. Freshly opened primary sources

1. Kerz, Strunk, and Tamme, *Algebraic K-theory and descent for blow-ups*, arXiv:1611.08466v4, author PDF dated 17 August 2017, 48 pages. The versioned PDF URL failed in this retrieval, but the unversioned primary URL <https://arxiv.org/pdf/1611.08466> returned the v4 document, identified on its first page. We read the noetherian setup, Theorem A on author p. 2, and the exact equivalent sequence (1.6) on author p. 3. Web reference: `turn484089099view1`.
2. Geisser and Hesselholt, *On relative and bi-relative algebraic K-theory of rings of finite characteristic*, JAMS 24 (2011), 29–49. Published primary PDF <https://math.mit.edu/~larsh/papers/025/bounded.pdf> opened in full. Theorem A and the immediately preceding nonconnective-spectrum convention on printed p. 29 were read. Web reference: `turn886693994view1`.
3. Thomason and Trobaugh, *Higher algebraic K-theory of schemes and of derived categories*, primary published PDF <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf> opened in full. Theorem 8.1, equations (8.1.1)–(8.1.2), and proof on printed p. 367 were read. The theorem is for quasi-separated schemes and quasi-compact open subschemes, exactly adequate here. Web references: `turn484089099view2`, `turn665074739view0`.

No mathematical correction is requested. There is no finite computation to rerun for this proof.
