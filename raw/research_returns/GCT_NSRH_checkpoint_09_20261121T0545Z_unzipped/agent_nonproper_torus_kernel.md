# F62 — Actual nonproper flag convolution, torus factors, and the missing global coefficient splitting

Author: /root/rectangular_and_theta, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This note tests the nonproper geometric alternative on an actual standard rank-one flag convolution inside the ordinary product-Hecke ambient setting used by IV. It constructs the relevant operations and localization maps, then proves a precise obstruction to replacing their relative coefficient by its constant fiber complex. The resulting scalar factors include the actual IV coefficient c_0 and the exact negative rank-three canonical coefficient printed in VIII. The latter comparison is an equality of coefficient traces, not an identification of the source's canonical labels or a proof of a nonstandard quadratic relation.

The Gysin, projective-bundle and compact-support identities used below are standard. Their exact primary locators are in Section 8. The new application is the explicit relative-coefficient and operation test, with all comparison assumptions stated.

## 1. The actual rank-one flag kernel and its composition maps

Fix a finite field k=F_q, a prime ell not dividing q, and E=Q_ell or a finite coefficient extension. Write E(r) for the Tate twist, so geometric Frobenius on E(r) is q^(-r). All cohomology calculations can first be made over the algebraic closure and retain their indicated Weil structures.

Let
\[
 X=P^1_k,\quad Y=X\times X,\quad
 i:\Delta\simeq X\hookrightarrow Y,\quad
 j:O=Y\setminus\Delta\hookrightarrow Y.
 \tag{NP1}
\]
The diagonal and off-diagonal are exactly the two relative-position strata for the standard rank-one flag variety. Define the standard off-diagonal kernel
\[
 \mathcal H=j_!E_O.
 \tag{NP2}
\]
For constructible complexes on Y use ordinary kernel convolution
\[
 \mathcal A\star\mathcal B
 =Rp_{13!}\bigl(p_{12}^*\mathcal A\otimes^L p_{23}^*\mathcal B\bigr).
 \tag{NP3}
\]
The unit is i_*E_X. Here p_{13}:X^3→X^2 is proper, but the sheaves extended by zero from open subsets implement the nonproper fibers below.

This is an actual associative geometric operation. Both parenthesizations of three kernels identify, by composition, projection formula and base change, with the single four-factor path pushforward
\[
 Rp_{14!}\bigl(p_{12}^*\mathcal A\otimes
 p_{23}^*\mathcal B\otimes p_{34}^*\mathcal C\bigr).
 \tag{NP4}
\]
The canonical functorial identifications for four kernels give the usual associativity pentagon. More concretely, for powers of H the common correspondence is the variety of sequences (x_0,...,x_r) with x_(a-1)≠x_a. Thus there is no inference of operation maps merely from an equality of point counts.

For H star H, put
\[
 Z=\{(x,y,z)\in X^3:x\ne y,\ y\ne z\},\qquad
 f:Z\to Y,\quad f(x,y,z)=(x,z).
 \tag{NP5}
\]
Then H star H=Rf_!E_Z. Over the diagonal the fiber is P^1 minus one point, namely A^1. Over O it is P^1 minus two distinct points, namely G_m.

Let
\[
 E_3=\{(x,y,z):x,y,z\ {\rm pairwise\ distinct}\},
 \quad \pi:E_3\to O,\qquad
 \mathcal K=R\pi_!E.
 \tag{NP6}
\]
The open/closed localization triangle on Y gives the actual relation maps
\[
 j_!\mathcal K\longrightarrow
 \mathcal H\star\mathcal H
 \longrightarrow i_*E_X(-1)[-2]
 \longrightarrow j_!\mathcal K[1].
 \tag{NP7}
\]
The diagonal restriction is the displayed affine-line compact cohomology because its family is a Zariski locally trivial affine-line bundle; its only compact direct image is the canonical top Tate line. The identifications follow from compact-support base change, not from an assumption that the off-diagonal family is a product.

For a rational pair over F_(q^n), write Q=q^n. The trace of H is the indicator of distinct points. Counting the possible intermediate y gives
\[
 h*h=(Q-1)h+Q\,1_\Delta.
 \tag{NP8}
\]
This is the usual unnormalized rank-one Hecke relation. Under v=Q^(1/2), T=v^(-1)h satisfies
\[
 T^2=(v-v^{-1})T+1,\qquad
 (T-v)(T+v^{-1})=0.
 \tag{NP9}
\]
This matches the correctly normalized ordinary Hecke convention used in IV. A sheaf realization of the half-weight normalization may use an arithmetic Weil line with eigenvalue sqrt(q); no integral Tate motive for that line is asserted. NP7 itself needs no half twist.

## 2. The off-diagonal family is a nontrivial line-bundle torsor

On O let
\[
 L_x=\operatorname{pr}_1^*O_{P^1}(-1),\quad
 L_z=\operatorname{pr}_2^*O_{P^1}(-1),\qquad
 \mathcal L=\operatorname{Hom}(L_x,L_z)=O(1,-1)|_O.
 \tag{NP10}
\]
There is a precise isomorphism over O
\[
                         E_3\simeq \mathcal L^\times,
 \tag{NP11}
\]
the complement of the zero section.

To prove it, two distinct lines x,z in k^2 give the direct sum k^2=x⊕z. A third line y distinct from both is the graph of a unique nonzero linear map x→z. Conversely the graph of any such map is distinct from both coordinate lines. These constructions are algebraic, commute with base change, and are inverse. This fixes the orientation: the chosen graph convention gives Hom(L_x,L_z), rather than its dual. Reversing the convention replaces the line bundle by its dual and only changes the Chern-class sign below.

The same torsor is PGL_2→PGL_2/T: a projective transformation is determined by the images of three ordered distinct points. The explicit graph description is the proof used here; no trivialization of this torsor is assumed.

Let
\[
 h_x=c_1(O(1,0)),\qquad h_z=c_1(O(0,1)).
\]
The diagonal in P^1×P^1 has class h_x+h_z. The Gysin sequence gives
\[
 H^0(O_{\bar k},E)=E,\qquad
 H^2(O_{\bar k},E)=
 \bigl(E(-1)h_x\oplus E(-1)h_z\bigr)/E(-1)(h_x+h_z),
 \tag{NP12}
\]
and all other ordinary cohomology groups vanish. In twisted notation,
\[
 c_1(\mathcal L)=h_x-h_z=2h_x\ne0
        \quad\hbox{in }H^2(O_{\bar k},E(1)).
 \tag{NP13}
\]
Indeed the map H^0(Delta,E)(-1)→H^2(Y,E) sends 1 to h_x+h_z and is injective. The next nonzero Gysin map H^2(Delta,E)(-1)→H^4(Y,E) is an isomorphism, since a point on the diagonal has degree one in Y. These two facts give NP12 and prove NP13. All coefficients are characteristic zero, so the factor 2 is nonzero even when the finite field has characteristic two.

Thus the torsor is not a product. More strongly, its compact pushforward is not the constant complex of a G_m fiber.

## 3. The actual connecting map is the nonzero Chern class

There is an actual distinguished triangle
\[
 \mathcal K\longrightarrow E_O(-1)[-2]
 \xrightarrow{\,c_1(\mathcal L)\,} E_O
 \longrightarrow\mathcal K[1],
 \tag{NP14}
\]
where the identification of the final E_O summand is chosen so that the map has the displayed sign. Reversing that identification changes the map by -1 and gives an isomorphic triangle.

Here is a direct specialized derivation which fixes the operation and its extension data. Compactify the line bundle as
\[
 p:\mathbb P(O_O\oplus\mathcal L)\to O,
\]
with sections s_0=P(O) and s_\infty=P(L). The complement of their union is L^\times. Write xi=c_1(O_P(1)) using the convention that P parametrizes lines. The projective-bundle formula, realized by the unit and xi maps and checked on fibers, gives
\[
 Rp_*E\simeq E_O\oplus E_O(-1)[-2].
 \tag{NP15}
\]
The two restrictions of xi are 0 and -c_1(L), because O_P(1) restricts to O and L^vee on those sections. The map from NP15 to E_O⊕E_O in the localization triangle therefore has the matrix
\[
 \begin{pmatrix}1&0\\1&-c_1(\mathcal L)\end{pmatrix}.
 \tag{NP16}
\]
Subtracting its first row from its second cancels the identity summand. Changing the sign of the remaining target identifies the other map with c_1(L). This proves NP14. All operations are actual maps of constructible complexes.

One may carry out the projective-bundle construction first over the smooth projective Y=P^1×P^1 with the extended bundle O(1,-1), and then restrict to O. Hence no extension of a projective-bundle theorem beyond its stated hypotheses is hidden in the argument.

NP14 gives
\[
 \mathcal H^1(\mathcal K)=E_O,\qquad
 \mathcal H^2(\mathcal K)=E_O(-1),
 \tag{NP17}
\]
with other cohomology sheaves zero. Every geometric stalk therefore has the cohomology of G_m with compact support. Nonetheless
\[
 \mathcal K\not\simeq
     E_O[-1]\oplus E_O(-1)[-2].
 \tag{NP18}
\]
The canonical two-degree extension class is the nonzero class NP13, so the truncation triangle does not split.

There is also a direct numerical cohomology certificate that avoids relying on classification language for extensions. Apply ordinary RΓ(O_bar{k},-) to NP14. The map in degree two is multiplication by the nonzero Chern class and is an isomorphism of the one-dimensional E(-1) spaces in NP12. The long exact sequence yields
\[
 H^1(O,\mathcal K)=E,\qquad
 H^4(O,\mathcal K)=E(-2),
 \tag{NP19}
\]
and no other hypercohomology. Thus the total dimension is two. For the proposed constant split complex in NP18, the total dimension is four: its nonzero groups occur in degrees 1,2,3,4, with Tate types E,E(-1),E(-1),E(-2). This proves nonisomorphism even after forgetting Weil structure.

Here RΓ(O,K) is ordinary cohomology on the base of a relative compact pushforward. It is not being identified with full compactly supported cohomology of E_3.

Consequently the standard scalar-coefficient replacement already fails at the operation level:
\[
 \mathcal H\star\mathcal H
 \not\simeq
 \mathcal H\otimes
       \bigl(E[-1]\oplus E(-1)[-2]\bigr)
 \ \oplus\ i_*E_X(-1)[-2].
 \tag{NP20}
\]
If such an isomorphism existed, restriction to O would contradict NP18. The two sides have the same Frobenius trace function at every finite extension. This is a specific example where equality of all pointwise trace functions still does not supply the requested coefficient-object splitting.

The outer localization triangle NP7 is itself nonsplit as well. Compactify Z in Y times P^1; its complement is the closed union of the two sections y=x and y=z, hence is proper over Y with finite geometric fibers. Its higher direct images vanish by proper base change, so the localization long exact sequence gives R^2 f_!E=E_Y(-1). A split NP7 would instead give R^2 f_!E=j_!E_O(-1) direct sum i_*E_X(-1). Both summands are nonzero, whereas the constant rank-one sheaf on the connected Y has endomorphism ring E and is indecomposable. This is impossible.

The valid relation is the nonsplit localization triangle NP7 with its actual nonconstant coefficient K; NP14 separately exhibits the coefficient's nonzero Chern-class boundary. Neither is the nonexistent split relation NP20.

## 4. The exact IV factor and the exact VIII printed coefficient

Take two independent copies of the rank-one construction, corresponding to the two ordinary Hecke factors of the ambient product. On O×O define
\[
             \mathcal K_2=(\mathcal K\boxtimes\mathcal K)(1).
 \tag{NP21}
\]
At every F_(q^n)-rational base point its stalk is the compact cohomology of a split two-dimensional torus, twisted by one. Its Euler trace is
\[
 Q^{-1}(Q-1)^2=Q+Q^{-1}-2
             =(v-v^{-1})^2,\qquad v=Q^{1/2}.
 \tag{NP22}
\]
This is precisely the actual coefficient c_0=D-4 in IV Figure 21, the edge whose vanishing is used in F58.

NP21 has actual operation maps: it is the relative compact pushforward of the product of the two torsors NP11, and is the tensor product of their localization triangles. Their compactifications supply the two boundary maps. The usual total-complex Koszul signs make the resulting square a genuine tensor product of triangles; no relation map is inferred from the polynomial NP22.

This relative coefficient is not constant. Restrict it to O×{o} for a rational base point o. The fiber of K at o is
C=E[-1]⊕E(-1)[-2] in the derived vector-space category. The restricted object is K tensor C, up to its Tate twist. Its ordinary base hypercohomology has total dimension 2 times 2=4 by NP19. A constant complex with the same stalk C tensor C has total dimension 2 times 4=8 on O, by NP12. Hence no global replacement by the constant two-torus coefficient is possible.

Now use the exact source computation in VIII Figure 2:
\[
 c(\gamma_2^1,\gamma_1^1;\gamma_{21}^1)
       =-\frac{(q_{\rm src}^2+q_{\rm src}+1)(q_{\rm src}-1)^2}
                    {q_{\rm src}^2}.
 \tag{NP23}
\]
Here q_src is the source's deformation variable; set q_src=Q only for the stated trace comparison. Define the point coefficient complex
\[
 \mathcal C_{\rm VIII}
   =R\Gamma_c((G_m)^2\times P^2,E(2))[1].
 \tag{NP24}
\]
Its trace is exactly
\[
 -Q^{-2}(Q-1)^2(1+Q+Q^2)
       =-(v-v^{-1})^2(v^2+1+v^{-2}).
 \tag{NP25}
\]
The shift [1] supplies the overall negative sign, twist (2) supplies Q^(-2), and the projective-plane factor supplies 1+Q+Q^2. These are ordinary integral Tate twists: no half-Tate geometric convention is needed for NP21 or NP24.

There is also a relative version with the actual nontrivial boundary data:
\[
 (\mathcal K\boxtimes\mathcal K)
       \otimes R\Gamma(P^2,E)(2)[1]
 \quad\hbox{on }O\times O.
 \tag{NP26}
\]
It has NP23's trace at every rational base point and inherits all maps of the two torsor localization triangles. Multiplying the preceding hypercohomology-dimension comparison by the three-dimensional total cohomology of P^2 again proves that it is not a constant coefficient complex.

These are verified realizations of these two particular source scalar coefficients. They do not identify NP21 or NP26 with a structure-constant object for the designated IV/VIII canonical labels. In particular no associator or quadratic for the nonstandard generator P_i is claimed from this scalar match.

The positive normalized factor v^2+1+v^-2 in NP25 is supplied here by the proper Lefschetz object RΓ(P^2,E)(1). Its three even cohomology groups and hyperplane maps are known explicitly. This is a concrete proper-factor extraction for a coefficient already known from the source, not a proof that unknown normalized source coefficients always admit such factors.

## 5. Powers, coherence, and a second exact normalization limit

For any a≥1, the product of a copies of NP11 is a (G_m)^a torsor over O^a. Its relative compact pushforward is K^{boxtimes a}, with its actual product localization maps. A compactification by the product of a P^1-bundles gives a cube of boundary maps; its totalization and Koszul signs are supplied by the derived tensor product. Thus powers of the vanishing factor have genuine coherent ambient geometric operations, not only independently chosen scalar Tate complexes.

If U is the arithmetic Weil line with geometric Frobenius sqrt(q)>0 under the specified complex embedding, then
\[
 U^{-a}\otimes K^{\boxtimes a}
\]
has fiber trace (v-v^-1)^a under v=q^(n/2). For even a this normalization is the ordinary twist (a/2). For odd a it is an arithmetic Weil coefficient line of odd integral weight, and no geometric integral Tate object for that half twist is asserted. An overall sign is supplied by an odd cohomological shift.

There is nevertheless no tensor inverse of the nonzero torus coefficient in the bounded finite-dimensional derived coefficient category. Indeed, over a field the total cohomology dimension satisfies
\[
 d(A\otimes^L B)=d(A)d(B).
\]
An invertible bounded coefficient object must therefore have d=1, and is a single one-dimensional line in one cohomological degree. RΓ_c(G_m,E) has total dimension two; its a-fold tensor power has dimension 2^a. It is not invertible. Likewise a relative inverse for K would pull back to an impossible inverse at a geometric point.

Therefore formal division by (v-v^-1)^a in the Laurent character ring is not implemented by tensoring with an inverse of the actual finite torus compact-pushforward object. An enlarged localization or a specified extraction operation would be extra data. Inverting the scalar factor also removes the v=1 fiber, as proved separately in the source-generator gate.

## 6. What this accomplishes for the actual main gate

The test supplies an actual geometric operation with coherent convolution and genuine boundary maps in the standard ambient rank-one flag geometry. It produces precisely the nonproper factor Q-1; taking two ordinary factors gives the actual IV c_0, and the displayed projective factor and shift give the actual VIII printed negative coefficient.

The calculation also supplies a concrete obstruction: the relative torus coefficient is controlled by a nonzero Chern-class extension invisible to every individual fiber trace. A proposal that treats the scalar factor as a constant coefficient object and replaces the convolution relation by a direct-sum relation is false already for this actual standard operation. This is stronger than the statement that mixed cohomology can occur.

Recovering canonical normalized positivity would therefore require at least:
- an identification of the actual designated canonical labels and their coefficient objects;
- the actual relative factorization or a functorial filtration/extraction, including its Chern-class boundary maps and compatibility with compositions;
- a proper pure Lefschetz realization of the extracted factor, with the grading and Frobenius comparison specified.

These are concrete requirements exposed by NP14 and NP20. The first two are not supplied by equality of all trace functions, and the last is not supplied merely by dividing an already computed scalar polynomial. For the particular VIII coefficient, the P^2 factor supplies the last item but does not supply the canonical-label identification.

The source specialization in F58 also remains a separate condition. The two-torus coefficient has nonzero total cohomology dimension four even though its formal Euler character c_0 evaluates to zero at v=1. Euler vanishing does not make the coefficient object or its maps vanish. Recovering the designated cell refinement needs the actual specialization/filtration comparison, not merely the torus point count.

This construction does not evade F59 by changing its conclusion: it has not supplied an actual nonstandard quadratic in the bounded ordinary Soergel category. The valid standard relation is a nonsplit triangle. Nor does it evade F60: no full actual finite-algebra presentation by the required ordinary isomorphisms is asserted. The coefficient objects are mixed after compact pushforward, so the pure-point criterion also remains intact.

## 7. Separate Grothendieck dictionary

The line bundle L=Hom(L_x,L_z) and its G_m torsor are actual affine/projective geometric objects. EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90–92 give the existing module/sheaf dictionary for their locally free sheaves. The first Chern class is the actual obstruction to splitting the relative compact-pushforward triangle, as proved by the two-section projective-bundle matrix NP16.

The standard six-operation framework supplies pullback, tensor product, compact pushforward, proper base change and localization. Those operations construct NP3, NP7 and NP14 before any Grothendieck-group or trace comparison. SGA5 III4.7 provides the trace-formula framework; it does not imply that an equality of trace functions is an isomorphism of complexes. The explicit NP18–NP20 discrepancy is precisely a test of that inference.

Internal coefficient characters use the torus-action vocabulary of SGA3 I4.7.2–3/cote90 scan17 and the effective/virtual distinction of SGA6 V §§2–3/cote133 scan18. The factor v-v^-1 is a virtual Euler character of a nonproper compact pushforward. It is neither an effective graded dimension nor an invertible object in the finite derived coefficient category. The bounded point coefficient complexes fit the perfect-complex framework of SGA6 I Definition4.7 pp121–122 and Example4.8 p122. No lambda-ring structure on the noncommutative kernel algebra is asserted.

The coefficient sheaves on the torsors may be pure before pushforward; the resulting relative and point compact pushforwards are mixed. The proper P^2 factor has its standard Lefschetz structure. No archival statement is being used to identify these constructions with the unknown nonstandard canonical category.

## 8. Primary locators and actual checks

Known geometric framework, read in the local original primary Milne text:
- Milne, Lectures on Etale Cohomology, Theorem16.1 and Corollary16.2, p108: purity and Gysin sequence for a smooth pair.
- Theorem16.7, p111: sheaf-level purity, including the indicated Tate twist.
- Theorem17.10, pp116–117: proper base change. The earlier Theorem17.3 is topological and is not the etale locator used here.
- Proposition18.4, pp121–122: compact direct images, their long exact sequence, constructibility and composition.
- Theorem22.1 and Remark22.3(b)–(d), pp135–136, with the ell-adic passage immediately following: ordinary/compact Kunneth and constructible coefficients.
- Proposition22.5, pp136–137: projection formula.
- Section23, pp138–139: cycle class of a smooth divisor and compatibility with the Kummer definition in codimension one.
- Theorem23.2, pp139–140: projective bundle and its hyperplane basis.
- Theorem23.3(a)–(b), p140: functoriality and line-bundle normalization of first Chern classes.
- Theorem24.1, p144, and Remark24.2(b), p145: compact top Tate line and the Gysin/cycle-class normalization.

Primary URL: https://www.jmilne.org/math/CourseNotes/LEC.pdf.
Local files: primary_sources/Milne_LEC.pdf and primary_sources/Milne_LEC.txt.

Actual source coefficients:
- IV, Example19.3, pp133–135 and Figure21 p135; supplied Apr13KroneckerGCT4.tex, lines8083–8095 and Figure21. The exact c_0 edge, P+Q=D normalization and its cellular significance were independently checked in F57/F58.
- VIII, Figure2 p34 and Section5.1.2 p29, supplied main.tex label fmultkron2: the exact coefficient NP23. The complete source positivity scope is checked in agent_named_generator_positivity_gate.md and REVIEW_NAMED_GENERATOR_GATE_THETA.md. Only the particular printed coefficient and its factorization are used here; no full multiplication table is newly recomputed.
- Ordinary rank-one Hecke normalization and ambient product are the correctly normalized IV Section3.1 conventions, not the exponent-swapped preliminary typo in Section11.1.

Checks performed for this report:
1. Constructed the torsor isomorphism by the graph of a map x→z, fixing L=O(1,-1).
2. Reconstructed the two-section restriction matrix and its sign convention from the projective-bundle hyperplane class.
3. Computed the full ordinary cohomology of O by the diagonal Gysin sequence.
4. Reconstructed all cohomology groups in NP17–NP19 and the 2-versus-4 and 4-versus-8 nonisomorphism certificates.
5. Checked the exact finite-extension trace normalizations for c_0 and the VIII constant, including shift [1] and total twist (2).
6. Checked the actual convolution correspondences, localization maps, external-product coherence and the distinction between a triangle and a direct-sum isomorphism.
7. Proved the finite derived tensor-invertibility obstruction directly by Kunneth.
8. Read the complete primary contexts listed above. No weight theorem is used to establish the nonsplitting or the exact coefficient trace identities.

Independent whole-proof review is requested before integration. No main paper or shared master log has been edited.

