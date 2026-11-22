# Full independent audit: all-dimensional endpoint lifting

Reviewed `research/agents/real_weil/C3_all_dimension_endpoint_draft.tex`, equations AE.1–AE.14, on 19 November 2026. Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, run `/root/frobenius`; effort setting not exposed. Complete mathematical reading finished at 17:17:08 UTC; the fresh Bruns–Vetter construction and full proof were then read. **Full proof and source-scope PASS.** No independent finite program or build rerun is claimed.

The result is conditional on an actual regular projective modification with a full exceptional effective Cartier divisor of ample conormal. It does not assert resolution in arbitrary dimension, nor vanishing of the remaining singular-exceptional quotient.

## 1. Determinantal identity in perfect K-theory

I independently checked the Eagon–Northcott signs, symmetric-power multiplicities and the universal identity. For a rank-n bundle V and m=n-i+1 columns, the q-th exterior-power term has multiplicity binomial(q-1,m-1) and sign (-1)^(q-m+1). The natural construction uses dual symmetric powers, so it does not divide by factorials or invoke a characteristic-zero identification. The cases i=1 and i=n reduce respectively to the determinant divisor and the Koszul zero section, with the same signs. For general i the partial alternating binomial identity gives

`det(V) epsilon_i(V) = sum_{j=i}^n gamma^j(V-n)`

as an exact vector-bundle K0 identity. Therefore epsilon_i differs from gamma^i only in the next gamma filtration. This is stronger than an equality in coherent G-theory or in a Chow associated graded, and preserves the Cartan-kernel information needed here.

The source was freshly opened in full: Bruns and Vetter, *Determinantal Rings* (1988), author-authorized PDF <https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf>. I read Section 2.C, printed pp.16–18, Theorem 2.16, p.18, and its full proof through Propositions 2.17–2.18, pp.18–20. The theorem is explicitly for a noetherian ring and an expected-grade maximal-minor ideal, not merely a generic matrix over a field. The natural dual complexes and their split exactness off the degeneracy locus are the precise input used.

## 2. Products and singular support

The virtual-bundle reduction is valid. Dualizing a sufficiently positive generating sequence writes an arbitrary bundle as a difference of two actual, equally ranked, sufficiently positive bundles. The quotient of a trivial bundle is globally generated; tensoring its generating sections with first-jet generators of the positive line bundle gives the claimed first-jet generation. Expanding the inverse gamma series treats arbitrary products of gamma generators, not only a single operation. Ranks may harmlessly be treated componentwise if the exceptional fibre is disconnected.

On the fixed finite smooth stratification of the reduced support times P, the general matrices meet the rank-one-drop strata transversely. Expected-grade follows from the Cohen–Macaulay ambient and the codimension estimates; deeper loci may occur for an individual matrix, but the final intersection avoids all of them because its incidence codimension is d+i_a+2>d+1. Near the final intersection, every determinantal ideal is reduced by an invertible minor to i_a actual functions. Their combined d functions have independent differentials on every stratum met and form a regular sequence in the Cohen–Macaulay thickening. The tensor product of the actual Eagon–Northcott resolutions is therefore the perfect class of that lci curve. No smoothness or normal-crossing assumption on the reduced exceptional support is needed.

The endpoint incidence conditions correctly force the finite zero-dimensional schemes C_o and C_t to meet only top-dimensional smooth strata and to be regular immersions of codimension d in D. They need not be reduced. General choices are justified over an arbitrary algebraically closed field, including small positive characteristics, by first-jet incidence dimensions rather than a characteristic-zero transversality assertion.

## 3. The regular threefold flag

The d by (d-1) conormal matrix drops rank in codimension two, so a general choice avoids rank drop on the one-dimensional curve. Nakayama upgrades the reduced-support condition to a split rank-(d-1) subbundle on the possibly nonreduced curve. The flag equations are consequently part of its actual regular-sequence ideal. This is exactly what makes C Cartier in H; it does not replace a nonreduced closure by its reduction.

All prefixes and the two selected endpoint fibres can be included among the finitely many jet-open conditions. The sections extend to the actual fixed Z times P by Serre vanishing. Independent ambient differentials give a regular threefold near its full closed fibre. Excellence makes its nonregular locus closed, and properness over a local scheme forces any nonempty such locus to meet the closed fibre. The same argument excludes wrong-dimensional components. Hence the immersion is regular everywhere. The full exceptional intersection is a Cartier surface, with C Cartier on it.

At the two endpoints the parameter, flag and exceptional equations form regular sequences in either order. This supplies the needed Tor independence and flatness near those endpoints. Global flatness over all of P is not assumed or needed. The empty flag for d=1 is consistent with all dimension and Cartier assertions.

## 4. A finite tensor power, actual algebraization, and exact endpoint equality

Relative Serre vanishing for the ample conormal over P kills all positive higher direct images for sufficiently large powers. Since P is a proper curve, Leray gives eventual H2 vanishing even if some other fibres of H over P have dimension two. Each earlier Picard obstruction is killed by p; only finitely many stages precede the uniform vanishing bound. Thus one finite p-power of O_H(-C) lifts to a compatible formal line bundle.

The two ideals defining the exceptional and base-adic topologies have the same radical on the proper noetherian W, so their powers are cofinal. Proper existence plus full faithfulness algebraizes the bundle and its inverse. Popescu descent and the henselian lift of the specified R/m^M point preserve the entire required finite jet, rather than only the residue fibre. The resulting Q is an actual line bundle on the fixed W with the stated restriction.

The perfect pushforward j_*(1-Q) is legitimate because j is a regular immersion. At either chosen endpoint, successive Cartier sequences give the sum of twists of O_Cu. Every invertible module on a finite Artinian scheme is free of rank one, so this is exactly p^e[O_Cu] in perfect K0(D). No gamma-filtration pushforward theorem is silently used. After division by p^e and summation, the discarded F_gamma^(d+1) terms vanish on the projective d-dimensional reduced support by Weibel II.8.8.5.

## 5. The ordinary-quotient consequence

The point restriction K0(Z)_Q to K0(E)_Q uses the already audited FF.4 and has no SNC requirement. Its lambda compatibility, finite gamma filtration on E, and distinct Adams eigenvalues give the displayed top-weight projector. The rational Chern comparison and its finite-model justification identify the top weight with CH^d(Z)_Q.

Nilpotent invariance is an isomorphism of rational lambda rings, so an exceptional gamma-top family lifts to the thickening in that filtration. Endpoint lifting then gives an actual ordinary cycle relation through ch_d. The converse takes the inverse Chern character on a smooth finite model of the actual cycle family. Proper-curve compactification is only asserted for ordinary cycles on the fixed regular product; it is not asserted for arbitrary perfect families on a singular product. Chow localization and closure of actual families then give exactly AE.13–AE.14.

## Scope and minor presentation points

The theorem gives equality of the two specified restrictions, not a lift of the whole exceptional family. It is therefore compatible with the already exhibited nonzero whole-family negative-K obstructions. No affine-parameter extension is inferred. In particular, the unresolved Cartier-tail problem for a closure from an affine parameter is absent here because the degeneracy curve is constructed on the entire proper exceptional product before the flag is chosen.

I reported one minor TeX comma in AE.3 and the optional componentwise-rank clarification to the owner. Neither changes the proof. Earlier EL/EP, Weibel, KST/GH, Drinfeld and formal-algebraization source audits are reused here; this receipt claims a fresh primary opening only for the exact Bruns–Vetter construction and proof described above.

## Final promotion and additional height locator

At 17:29:41 UTC I checked the final-path edits in `real_weil/C3_all_dimension_endpoint.tex`, now Statement C.3bn: the multiplication and componentwise-rank clarifications are present. I also freshly read Bruns–Vetter Theorem2.1 and its proof, printed pp.10–11, in the same author-authorized primary PDF. It gives the general determinantal height bound needed to combine the stratified lower bound with Cohen–Macaulayness and obtain the exact expected grade. This confirms the final added locator. The original full audit time and scope above are preserved; no new full-program or build rerun is claimed.
