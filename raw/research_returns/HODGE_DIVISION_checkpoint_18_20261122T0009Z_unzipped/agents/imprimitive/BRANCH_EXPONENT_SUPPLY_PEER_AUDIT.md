# Independent audit of HD-FS1 and HD-FS2

**Auditor:** /root/imprimitive, GPT-6 Astra Pro, effort inherited/not externally exposed, HODGE_DIVISION.  
**Date and interval:** 2026-11-21, approximately 13:22–13:27 UTC.  
**Audited proof:** research/branch_exponent_supply.tex, complete HD-FS1/HD-FS2.  
**Outcome:** **PASS**, with the explicit scope below.

This is a whole-proof mathematical audit. It does not certify a numerical degree bound for the correspondences, reprove integral Brauer induction, or claim that an arbitrary CM Jacobian has the Hodge conjecture. The final Hodge-conjecture implication retains its stated hypothesis on all powers of the fixed Fermat Jacobian.

## 1. The cyclic determinant and the Abel fibre

For a connected degree-\(m\) cyclic cover and faithful nontrivial character, each nontrivial inertia has zero invariant space. Consequently the character local system extends by zero at the branch points and has no degree-zero or degree-two cohomology. Its degree-one dimension is
\[
v=2g(B)-2+r.
\]
The relation in the punctured surface group excludes \(r=1\). The case \(v=0\) is the unit determinant and was separated correctly.

The kernel \(N\) of the product map
\(\Delta^v\rtimes S_v\to\Delta\) is normal. The rational cohomology of the finite quotient \(C^v/N\) is exactly the invariant cohomology. On the residual faithful character part, every curve factor must contribute \(H^1_\chi\). The geometric permutation action on these odd-degree factors includes the Koszul sign. Thus permutation invariants are the ordinary exterior power \(\bigwedge^v H^1_\chi\), a line. The quotient cohomology is pure because pullback embeds it into the pure cohomology of the smooth projective product.

Over the symmetric power of the punctured curve, the residual cover is a torsor even along diagonals: locally the sheet labels modulo \(N\) retain their product. At a divisor containing a branch point, the residual stabilizer contains the original nontrivial inertia, irrespective of the multiplicity of that point. The faithful-character stalk is therefore zero. This checks the claimed extension-by-zero description, not just its restriction away from the diagonals.

For \(r>0\), \(v\geq 2b\). Away from \(L_0=K_B(D)\), Serre duality makes the evaluation obstruction the section space of a nontrivial degree-zero line bundle, hence zero. The kernel dimension is \(b-1\). Choosing a splitting and normalizing one nonzero evaluation coordinate identifies the complement with
\(\mathbb A^{b-1}\times(\mathbb C^*)^{r-1}\). A loop in one of the remaining evaluation coordinates has the corresponding nontrivial inertia character. The circle complex therefore has invertible differential, and both ordinary and compactly supported cohomology vanish. Proper base change and the derived pushforward supported at \(L_0\) give the stated restriction isomorphism. When \(b=0\), the Picard space is already a point.

The unramified case also checks. For \(b\geq2\), the Abel map in degree \(2b-2\) has fibres \(\mathbb P^{b-2}\), except for \(\mathbb P^{b-1}\) over \(K_B\). Powers of a relatively ample class identify the lower even direct images with constants, and proper base change identifies the remaining direct image with a rank-one skyscraper. The nontrivial local system on the Picard torus has zero cohomology, so only the skyscraper survives. The restriction over the simply connected canonical linear system splits into projective spaces. The genus-one unramified case had already been removed by \(v=0\).

## 2. Why the inertia exponent, rather than the deck-group order, suffices

The residue sequence gives the stated vector space \(W\oplus R\), with evaluation hyperplanes \(w_i=0\). For \(r\geq3\) they are distinct. On the complement, the cyclic torsor is Kummer. Its valuations away from these hyperplanes are multiples of \(m\). Matching the hyperplane valuations modulo \(m\), including the last one through the degree relation, leaves a divisor \(mE\); the torsion-free Picard group of projective space makes \(E\) principal. This justifies the Kummer equation globally.

The transverse evaluation loop is the original local inertia, so each Kummer exponent satisfies \(m\mid Ma_i\). Pulling back \(w_i\) to \(u_i^M\) therefore makes every Kummer factor an \(m\)-th power. No assumption that \(m\mid M\) is used.

The projective bundle over the degree-\(M\) Fermat hypersurface has dimension \(b+r-2\) and maps generically finitely onto the Abel fibre. The rational lifts extend because the source is normal and the target finite over the base: each lifted coordinate is integral over the local ring of the source and hence belongs to it. A dominating component meets every base fibre, and residual deck-group translates cover the entire fibre, which is a single orbit. Thus finitely many translates cover every component of the reduced inverse image.

For \(r=2\), the evaluation hyperplanes coincide and their monodromies cancel. The generic Kummer torsor splits, so finite unions of projective spaces dominate the reduced fibre. The proof does **not** need the fibre itself to be smooth or a disjoint union: its components may meet along the common hyperplane.

The Shioda–Katsura blowup construction gives the required full-cohomology supply. In the induction step, a degree-\(M\) generically finite morphism from the blowup of \(F_M^{d-1}\times F_M^1\) has smooth centre \(F_M^{d-2}\times F_M^0\). The blowup formula supplies its cohomology from lower dimensions, and push-pull divided by the degree supplies the target. This is an algebraic-correspondence argument, so it is stronger than a vector-space dimension identity. The projective-bundle formula adds only Tate twists.

## 3. Purity and the returning correspondence

Deligne's Proposition 8.2.5 applies to **any** proper surjection from a smooth variety to a proper variety, exactly the situation here. Its proof identifies the kernel of pullback with \(W_{v-1}H^v(T)\). The pure weight-\(v\) determinant line, embedded by the restriction isomorphism, has zero intersection with that kernel by strictness. It therefore survives on a smooth supplier component \(Y_0\).

Writing \(d=\dim Y_0\), Poincaré duality provides a class \(\beta\) of degree \(2d-v\) pairing nontrivially with the pullback of the determinant. The degree is \(r-2\) in the ramified case and zero in the unramified case. Full-cohomology supply applies to this \(\beta\); it need not itself be a Hodge class at this stage.

A component of \(Y_0\times_Z C^v\) dominating \(Y_0\), followed by a projective resolution, supplies maps \(h,l\). Its graph correspondence acts as \(l_*h^*\), and projection formula gives
\[
\int_{C^v}Q^*\alpha\,l_*h^*\beta
=\deg(h)\int_{Y_0}p^*\alpha\,\beta\ne0.
\]
The output degree is \(v\), since \(l_*\) adds \(2(v-d)\). Thus the correspondence really returns to the cohomology degree containing the determinant.

Applying the inverse-character projector preserves this pairing: the polarization pairs the \(\chi\) and \(\chi^{-1}\) summands. Its degree-\(v\) image is the one-dimensional determinant for \(\chi^{-1}\), so the image is nonzero and therefore the entire line. Scalar conjugation supplies the original character line. This verifies the direction of supply; mere detection on a smooth alteration would not have sufficed.

## 4. Integral Brauer induction and cancellation

Integral Brauer induction gives an equality of honest representations after moving negative terms to the other side. Frobenius reciprocity identifies the multiplicity spaces of the induced linear characters with the faithful cyclic character spaces of \(C/\ker\chi\to C/H\). Intermediate inertia is obtained from intersections with cyclic stabilizers and quotienting, so its generators are images of powers of conjugates of original inertia generators. Their orders divide \(M\).

Taking determinants gives \(D_+=D_V\otimes D_-\). The polarization pairs \(D_-\) nondegenerately with the determinant of the contragredient/conjugate minus representation. The pairing is realized by curve diagonals, the algebraic \(H^1\) projector, and finite group-algebra projectors. Tensoring and contracting therefore cancels an actual dual determinant factor, with a Tate shift. It does not require extracting any root of an algebraic class.

For disconnected covers, choosing a component and restricting the representation to its stabilizer reduces the argument to the connected case by induction and determinant tensor products. Finally, semisimplicity of polarizable rational Hodge structures supplies rational Hodge preimages in the fixed supplier powers. Under the explicitly stated Hodge-conjecture hypothesis, those preimages are algebraic and remain algebraic after composition of the correspondences.

## Primary-source checks

- Deligne, *Théorie de Hodge III*, Publ. Math. IHÉS **44** (1974), Theorem 8.2.4(iii), printed pp.38–39; Proposition 8.2.5 and its complete proof, including (8.2.5.2), printed p.39. Read in the original Numdam journal PDF. The proposition has precisely the proper-surjective/smooth-source generality used here. The proof invokes the stated simplicial weight theorem; I did not reprove all of Deligne's mixed-Hodge construction.
- Shioda–Katsura, *On Fermat varieties*, Tohoku Math. J. **31** (1979), Lemmas 1.1–1.2, printed pp.98–99; Theorem 1.7 and diagram (1.25), printed pp.101–102; Lemmas 2.1–2.3 and Proposition 2.4 with proof, printed pp.103–104. Read the journal PDF, including the displayed diagram and cohomology formulas. The primary J-STAGE PDF was downloaded directly after the browser fetch timed out.
- Integral Brauer induction is the published Serre input already identified in the proof, §10.5, Theorems 19–20. This audit checked its required integral form and the subsequent cancellation argument; it does not claim a new proof of Brauer induction.

The \(E_8\) specialization uses only that all original branch orders divide \(12\). Large character orders arising in Brauer induction do not enlarge the fixed Fermat exponent. Quantitative correspondence degrees and the elliptic decomposition of \(J(F_{12})\) are separate results.
