# Independent full audit of C.3av

**Verdict:** PASS of the complete typed mathematical proof, with the stated interval and coefficient-field qualification. Reviewed file: `research/agents/real_weil/C3_positive_characteristic_low_range_draft.tex`. Review completed on 19 November 2026, at the tool-clock time recorded in the accompanying event file. We do not claim a fresh independent execution of the owner's finite certificate in this audit; the argument below verifies the general formulas directly.

## 1. Quantifiers and dimensions

The assertion covers every prime, every `r >= 1`, and `r+2 <= N <= 2r+1`. The definitions `d=2r-N+2` and `s=N-r-2` give `d>=1`, `s>=0`, `r=d+s`, and `N=d+2s+2`. The base field is an algebraic closure of the function field of a positive-dimensional variety over the algebraic closure of a finite field. It is not the algebraic closure of a finite field. The latter distinction is necessary because ordinary algebraically trivial cycle groups there are torsion.

## 2. Hasse matrix and terminating choice

Let `m=d+2`. The choice `e=m` when `p` does not divide `m`, and `e=m+1` otherwise, ensures `p` does not divide `e`. The Fermat member at parameter zero is smooth; properness of the relative singular locus therefore gives a nonempty smooth open subset of the parameter line.

For degree `e=m`, the top coherent cohomology has the one Cech basis vector with all exponents one. The coefficient of the highest power of the parameter in its Hasse matrix is one. For `e=m+1`, the basis is indexed by the `m` vectors `1+epsilon_j`. After extracting the common product of coordinates, the highest coefficient of matrix entry `(i,j)` is the coefficient of the monomial with exponent `p epsilon_j-epsilon_i` in `(sum y)^(p-1)`. It is zero for `i != j` and one for `i=j`. Thus the determinant really is monic of degree `g(p-1)`, with `g=1` or `m`. This computation includes characteristics two and three. The conjunction of smoothness and determinant nonvanishing is a nonempty open of an affine line over a finite field. Enumeration of finite extensions and finite-field elements terminates. The stated projective Jacobian-ideal test is finite and effective.

The hypersurface is geometrically integral: if a positive-dimensional projective hypersurface were reducible, its components would meet and create a singular point. The coherent cohomology statements follow from the standard hypersurface sequence and projective-space cohomology.

## 3. Witt modules, including `d=1`

The exact Witt-vector sequence gives `0 -> M_(n-1) -> M_n -> H^d(O) -> 0`. For `d>=2`, the preceding coherent group vanishes. For `d=1`, the potentially problematic preceding connecting map vanishes because `H^0(W_n O)=W_n(F_q)` projects surjectively onto `H^0(O)=F_q`. This is a genuine repair of the curve endpoint, not an appeal to a higher-dimensional vanishing statement.

Coordinate Frobenius is semilinear and bijective by induction. Truncation is surjective by top-degree coherent vanishing. The identity `p=VFR` gives `pM_n=V M_(n-1)`, and the additive short exact sequence gives length `gn`. Hence `M_n/pM_n` has dimension `g`; Nakayama and equal lengths give `M_n ~= W_n^g`. Bases can be chosen compatibly under truncation. The proper Witt inverse-limit comparison is the unnumbered display at the start of printed p. 7, following the unnumbered derived comparison on p. 6 of BBE Section 2. The inverse limit is `W^g` and Frobenius is bijective, so it is a nonzero unit-root module. Only this top-degree statement is proved or used; full ordinarity of the hypersurface is not inferred.

## 4. Suspension and integral inverse

The paired partial derivatives force all paired coordinates to zero because `p` does not divide `e`. Euler's formula then reduces any hypothetical singular point to a singular point on the original smooth hypersurface. The two distinct roots of `lambda^e=-1` exist in the algebraic closure in every characteristic under the chosen degree condition.

Each join resolution is a projective `s`-space bundle over the original `d`-fold. Its cycle has codimension `d+s=r` in the product. The two join images meet precisely in the original hypersurface, away from their vertices. Their paired tangent directions are complementary because the roots are distinct. This gives multiplicity one, and the composition has codimension `2r-(d+2s)=d`, as required for the diagonal. The integral identity `transpose(Gamma_1) Gamma_0=Delta` is correctly typed. The case `s=0` is the diagonal convention.

## 5. Generic-point spread and support

The difference of the geometric generic point and a constant point is ordinarily algebraically trivial, using the curve itself in dimension one and a smooth complete-intersection curve through the two points in higher dimension. The corresponding incidence pushforward retains this ordinary algebraic equivalence.

A hypothetical rational hyperplane relation descends to a finite extension of the original function field. Transfer, spreading, and closure give the asserted equality with a nonzero integer multiplier and an error supported on a proper subset of the source. The constant correspondence is retained and acts by zero in positive cohomological degree. Inseparable transfer degrees cause no difficulty because the subsequent coefficients have characteristic zero.

The support argument is the already-certified C.3at Step 3, which we reread in this audit: alter each source-support image to a smooth projective variety of dimension less than `d`, lift each correspondence rationally using a closed point of a generic proper fibre, and divide by its degree. The action factors through degree `d` cohomology of the altered source. BBE's slope-below-one comparison and Witt cohomological dimension make that group have no slope below one. All finite data descend to a finite field extension, so every correspondence map used in the slope argument is Frobenius equivariant. We do not claim a fresh reopening of de Jong's source in this audit; it is the previously certified input to C.3at.

## 6. Exact twist calculation and weak Lefschetz

The incidence correspondence sends the nonzero slope-zero source to `H^n(V)(s)` and has a left inverse. The hypothetical cycle `B` has codimension `r-1` and therefore sends it to `H^(n-2)(V)(s-1)`.

If `s=0`, that target is `H^(d-2)(V)(-1)` and has slopes at least one; negative degrees vanish. If `s>=1`, the complement of the smooth hypersurface in projective space is smooth affine of dimension `n+1`. Monsky-Washnitzer vanishing above that dimension, rigid Poincare duality, and compact-support localization give rational crystalline weak Lefschetz in degrees below `n`. These are exactly the inputs explicitly recalled in BBE's proof of Corollary 1.2, printed p. 4. Thus the target is zero when `n-2` is odd, and otherwise has the single normalized slope `(n-2)/2-(s-1)=d/2>0`. There is no equivariant map from slope zero. This uses rational cohomology throughout, and does not assume an integral crystalline weak-Lefschetz statement.

The multiplier of the incidence map is nonzero in the rational crystalline coefficient field, even if divisible by the characteristic. Hence the spread equality contradicts the left inverse on the nonzero unit-root space.

## 7. Strict local realization and source Chow vanishing

The displayed ambient polynomial strict henselization has dimension `N`. The homogeneous hypersurface ring is Cohen-Macaulay and regular outside its vertex; its vertex has codimension at least two. It is therefore normal. Its homogeneous coordinate ring is the full section ring generated in degree one, by the hypersurface sequence. Strict henselization commutes with the indicated quotient. The integral strict-cone injection of C.3e therefore applies to the hyperplane quotient. The incidence family and the curve family pull back as actual families on the fixed puncture.

Kerz's Theorem 7.1 applies to the excellent regular local ring containing the infinite field in question, and Theorem 7.5 gives the integral Milnor Bloch formula. On a local Zariski space, global sections equal the closed-point stalk and are exact. Therefore positive-degree Zariski cohomology, hence positive-codimension Chow groups of the local scheme, vanish. Localization then gives the asserted integral vanishing on the ambient puncture.

## 8. Opened primary-source ledger

1. Berthelot, Bloch, and Esnault, *On Witt vector cohomology for singular varieties*, author PDF, 42 pages: <https://page.mi.fu-berlin.de/esnault/preprints/helene/80WittCohomology051014.pdf>. Freshly opened in full; equation (1.1), proof of Corollary 1.2 on printed p. 4, and Section 2 on printed pp. 6–7 read. Screenshots of the latter two pages were opened, and the local full-text transcription was subsequently checked line by line: the proper inverse-limit isomorphism on p. 7 is UNNUMBERED. Equation (2.3), on p. 8, is an unrelated Mayer–Vietoris diagram. The initial audit incorrectly attached that equation number; parent caught this source-locator error and it was corrected at 11:15:10 UTC. No mathematical use changes. Retrieval references include `turn800285807view0`, `turn179202402view0`, and `turn179202402view1`.
2. Huang, Lian, Yau, and Yu, *Hasse-Witt matrices, unit roots and period integrals*: <https://archive.ymsc.tsinghua.edu.cn/pacm_download/311/8917-Hasse-Witt3.pdf>. Freshly opened in full and Corollary 2.3, author p. 8, together with the hypersurface explanation read. The matrix formula applies to the present non-Calabi-Yau degree as well. Retrieval references `turn338776288view1` and `turn484499332view2`.
3. Kerz, *The Gersten conjecture for Milnor K-theory*: <https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf>. Freshly opened in full; the excellence convention at the beginning of Section 7, Theorem 7.1 on author p. 21, and Theorem 7.5 on author p. 22 read. Retrieval references `turn800285807view1` and `turn868952243view1`.

No mathematical correction is requested. The owner's heading can be finalized after its normal integration checks. The conclusion is confined to the stated low-dimensional interval and transcendental algebraically closed coefficient fields.
