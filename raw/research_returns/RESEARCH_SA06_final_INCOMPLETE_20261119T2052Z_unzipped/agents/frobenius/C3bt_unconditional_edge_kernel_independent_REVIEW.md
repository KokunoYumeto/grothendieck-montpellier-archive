# C.3bt — independent full proof and primary-source review

**Reviewer:** GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; run `/root/frobenius`; effort setting not separately exposed.  
**Completed:** 19 November 2026, 18:41:12 UTC (actual clock tool).  
**Verdict:** PASS for the complete displayed scope. No mathematical correction requested. This receipt does not register or integrate the statement and claims no independent program or build rerun.

## Text actually read

- `agents/cycles/SNC_unconditional_edge_kernel_draft.tex`, all VE.1–VE.10, SHA-256 `532b6ba34ed6470cded14ef1d54e9aaf54a6fc68b02ae2394269e837ef47e7a9`.
- Its complete implication input `agents/real_weil/C3_unconditional_edge_totalization.tex`, UK.1–UK.7, SHA-256 `3bd775d235612661601f7b1192c869d2593a91635efb99a83a1e11324d649467`.

The preceding variable-unit research note was also read in full. Its norm-kernel gap is repaired by the new finite-divisor interpolation, rather than by asserting norm injectivity.

## 1. Parameter curve and interpolation

The zero cases are separated correctly. For a nonzero tuple of degree-zero bundles, a smooth proper curve through the two required points of the product Jacobian supplies one common parameter for all edges. The prescribed-point complete-intersection construction works over every algebraically closed field, including positive characteristic. The normalized Poincare bundles provide actual line bundles and specified trivializations at the zero endpoint.

For each of the finitely many marked evaluations, twisting by a sufficiently large effective divisor away from the two endpoints and using curve cohomology gives a rational section whose divisor avoids both endpoints. Its value at the zero endpoint can be normalized to exactly one in the specified fibre trivialization. This does not require the marked bundle to be trivial or torsion.

After these sections have been chosen, Riemann–Roch permits a rational function with only a pole at the zero endpoint, the prescribed nonzero value at the other endpoint, and zeros at every support point of every chosen divisor. A further prescribed simple zero can be imposed simultaneously. All conditions are finite evaluation or first-jet conditions in one sufficiently large linear system. They impose no characteristic bound.

## 2. The cover, including characteristic two and ramification

For the equation `(g-1)^2 = h g`, an additional simple zero of `h` gives an odd valuation of `h(h+4)` in odd characteristic. In characteristic two, the substitution in VE.4 gives the Artin–Schreier equation `y^2+y=1/h`; its simple pole cannot occur in an Artin–Schreier coboundary. Thus the function-field extension is a separable field extension of degree two in both cases. Normalization gives a smooth connected proper curve and a finite flat map between smooth curves.

The equation and its inverse show that zeros and poles of `g` occur only over the pole of `h`; conversely `g+g^{-1}=h+2` excludes a unit at a point above that pole. The endpoint with value `u` exists. At every point above one of the chosen divisor supports, the residue of `g` is exactly one.

Ramification is allowed and is actually expected at simple zeros of `h`. Pulling back a divisor introduces its ramification multiplicity. In the point pushforward description, this merely raises the residue unit to that multiplicity; the residue unit is one, so the contribution is zero. The argument does not incorrectly require the divisor to avoid the branch locus. The same reasoning handles wild characteristic-two ramification.

## 3. The normalized sheaf class

On each regular surface `C_e × P`, choose local frames extending the given trivialization on the boundary fibres. Near such a fibre the transition units have the form `1+z b'`, while `g=z^m v`. The symbol

`m <z,-b'> + {v,1+z b'}`

has the stated restriction away from the boundary. The minus sign matches Weibel's Dennis–Stein convention. Its pullback to the boundary fibre is zero term by term, including negative `m`.

Regular local Gersten injectivity applies to the sheaf of Quillen `K_2` on these smooth products. It identifies the local extensions on overlaps, proves their cocycle identity, and shows that changing normalized frames changes the resulting cocycle by a coboundary. No assertion about injectivity of a global affine `K_2` group is required. A Cech cocycle maps canonically to sheaf cohomology; no acyclic-cover claim is used.

At the nonzero endpoint the pulled-back cocycle is the ordinary cup of `u` with the line-bundle cocycle, and hence gives `u([L_e]-1)` in the first descent piece of the curve's actual `K_1`.

## 4. Exact marked restriction, rather than its norm

At a marked point, pull back the chosen rational section from the base curve. Its divisor is disjoint from the boundary and its value at every boundary point is one in the prescribed normalization. On the complement of that divisor it can therefore be used as a frame compatible with the boundary trivialization.

Comparison with the original normalized frames introduces symbols whose comparison units are also one at the boundary; the Dennis–Stein formula extends these symbols and gives no boundary point-unit contribution. The remaining local calculations occur where `g` is a unit. The ordinary Gersten divisor formula then gives exactly the finite sum in VE.8, with the pullback multiplicities retained.

Every term in that sum has coefficient the unit one. Consequently the marked restriction vanishes in `H^1(P,K_2)`, and then in `K_1(P)` under the descent bridge. No pushforward or norm is used to infer this vanishing. This is the substantive repair of the earlier variable-unit attempt.

## 5. Global `K_1` and the descent filtration

I freshly read Thomason–Trobaugh's exact spectral-sequence indexing and its complete proof. In their convention

`E_2^{a,b}=H^a(X,K_b) => K_{b-a}(X)`

and `d_r` has bidegree `(r,r-1)`. For a surface, every incoming differential to `(a,b)=(1,2)` has negative first index and every outgoing one has first index at least three. Thus this term survives unchanged and is `F^1_des K_1 / F^2_des K_1`.

Derived pullback of perfect complexes supplies the map of `K`-presheaves. The natural hypercohomology augmentation and Postnikov tower make the comparison with the indicated sheaf-cohomology pullbacks functorial. On a curve the second descent piece vanishes. Therefore any first-piece lift of the constructed sheaf class has precisely the horizontal and vertical restrictions already computed. Choosing the first piece excludes a determinant/unit term.

As an additional concrete verification for these particular Cartier inclusions, the second surface coniveau piece is generated by closed-point `K_1` pushforwards. Pullback to a disjoint curve is zero; when the point lies on the curve, the excess normal-line factor is `1-1=0`. This checks the necessary ambiguity statement without claiming that arbitrary pullback preserves codimension of supports.

The marked edge-family lemma is therefore an actual integral `K_1` construction on fixed proper products. Its proof does not rely on a formal family or an affine-only parameter.

## 6. Whole SNC descent and coherent ambiguity

UK.2 retains the canonical geometric nullhomotopy and the actual two-stage fibre, rather than replacing the diagram by homotopy groups. The characteristic-positive rational closed-union descent input is the one already audited in C.3bq. The two displayed long exact sequences are compatible with endpoint pullback.

The proof of component-surjectivity is valid without any semisimplicity assertion for `pi_0(T)`: an obstruction with Adams eigenvalue four maps to zero on the double curves and hence comes from triple-point `K_1(k)`, where the eigenvalue is two. It must vanish. The weight-two projector on projective `K_0` then produces a lift in `S(E)`.

For a component-kernel class, the stated operation removes the edge unit piece while retaining its boundary. Picard-times-unit generation and the already proved weighted restriction-degree identity reduce the edge data to a finite sum of degree-zero tuples, one constant unit at a time. Subtracting actual component `K_1` images changes no boundary; no full Picard restriction surjectivity is used.

The marked families make every required edge-to-vertex restriction literally zero in `K_1(P)`, so they lift to the actual fibre `T_P`. Their boundaries are actual perfect families, and the rational weight-two projector on `K_0(E × P)` puts their endpoint differences in the defined relation group. The argument can keep the unprojected fibre lifts while comparing edge images, and apply the projector to their boundaries afterwards. Any remaining difference has zero edge image and comes from triple-point `K_2(k)`. The previously audited proper-curve symbol construction and natural double boundary put this complete coherent ambiguity in `J_K(E)`. No unique fibre lift is assumed.

## 7. Exact conclusion and limits

The conclusion is the unconditional inclusion of the whole component-map kernel in `J_K(E)` under the stated negative SNC exceptional-surface hypotheses. Pointwise component-surjectivity is also proved.

The final denominator splitting is exact. The actual Poincare subgroup lying in both the proper-family and exceptional subgroups permits the two denominator summands to be adjusted separately into `S_00`; applying the now surjective component map gives UK.7. This is not a formal quotient by independently projected coordinates.

If all component Albanese kernels vanish rationally, the displayed quotient is zero. For arbitrary components, their induced proper-family and exceptional relations remain explicitly present. The theorem does not prove that every component Albanese-kernel class lifts to a globally compatible proper family, and it makes no universal top-Chow vanishing claim.

## Primary-source audit

Freshly opened/read in this review window:

- Thomason, R. W., and Trobaugh, T. (1990), *Higher algebraic K-theory of schemes and of derived categories*: Sections 3.14–3.15, printed pp.317–319; Theorem 10.3 and its complete proof, pp.383–386; Remark10.4; Appendix D.4 and its complete Postnikov proof, pp.424–426. Primary full published PDF: <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf>. Exact retrieved references include `turn627078483view0`, `turn375150305view0`–`view2`, and `turn285382548view1`. The printed page383 screenshot was requested; the mathematical reading here is of the full retrieved primary text, not an unsupported claim to have seen image bytes.
- Weibel, C. A., *The K-book*, author ChapterIII: Definition5.11 and the Dennis–Stein identities D1–D3, printed pp.43–44, freshly read during the preceding read-only checkpoint interval. Primary URL: <https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf>; retained local source `agents/frobenius/sources/Weibel_Kbook_III.pdf`. The normalization and specialization follow from the displayed identity and defining word. No fresh reading of the original Dennis–Stein paper is claimed.

Previously completed exact primary reads reused, with their scopes retained: Quillen's regular Gersten theorem and localization/projection formulas; Pedrini–Weibel Lemma5.2 and full proof pp.395–396; Geisser–Hesselholt A/C; Thomason–Trobaugh closed-union ingredients; Levine's arbitrary-scheme iterated-fibre/delooping paragraph on p.258 (distinct from regular-only Lemma2.1); WeibelII finite gamma filtration and projectors; and the prescribed-point Bertini proof. These are documented in the preceding C.3bq, C.3br, C.3bs, and C.3bo independent receipts. They are reused here, not advertised as additional fresh openings.

No finite computation or compilation is needed to establish the general interpolation, cover, descent, or totalization arguments. The owner remains responsible for final compilation and registration.

## Continuation final-text recheck

At 2026-11-19T18:47:34.242541+00:00, the continuation reviewer `/root/frobenius_continuation` re-read both complete current proof files, VE.1–10 and UK.1–7. The full mathematical PASS is retained, with no requested mathematical correction. Current SHA-256 values are:

- `agents/cycles/SNC_unconditional_edge_kernel_draft.tex`: `5a977ce45eafe1f2f51bed7edc06002af647905cdd989896b9c334c8afeebc75`.
- `agents/real_weil/C3_unconditional_edge_totalization.tex`: `71f2a345844ee778a73b21c108d8f3b46f7c556847198b7746f3aa10fa21be24`.

This recheck reuses the exact previously recorded primary-proof reads; it does not claim a fresh source opening, program rerun or compilation. The first proof-file comment still marks the owner draft unregistered; final owner promotion and integration remain separate actions.

At 2026-11-19T18:49:40.819495+00:00, the owner confirmed and the continuation reviewer checked the final first-line status comment. This is the sole change from the complete proof text just read; no mathematical or expository content changed. The stable final hashes are VE `5a977ce45eafe1f2f51bed7edc06002af647905cdd989896b9c334c8afeebc75` and UK `71f2a345844ee778a73b21c108d8f3b46f7c556847198b7746f3aa10fa21be24`. The owner promotion receipt, independently read in full, records promotion at 18:48:51.902100 UTC and the final seven-page build. This reviewer does not claim the owner's visual inspection as an independent visual pass.

Final heading-only recheck at 2026-11-19T19:01:30.299663+00:00: the manuscript heading is now “C.3bt. Proper edge families (Proved).” Its proof is unchanged; current stable VE SHA-256 is `60cba994d1e3e7d025d161c1a54e01cd93e031ed4c3babbe8a11fb68a772bb4b`. The first three source lines were freshly read. UK remains `71f2a345844ee778a73b21c108d8f3b46f7c556847198b7746f3aa10fa21be24`. Mathematical PASS is unchanged.
