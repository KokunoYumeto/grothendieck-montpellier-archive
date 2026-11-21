# F64 — Perverse weight grading fails to commute with the actual flag convolution

Author: /root/rectangular_and_theta, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This is a concrete continuation of F62. It tests two specified extraction procedures on the same actual standard rank-one flag kernels. It does not assert that every filtered or nonproper construction is impossible. In particular the positive closed-orbit kernel at the end is a valid restricted construction; it is a change of chosen generator, not an exact monoidal extraction preserving the original open-kernel relation.

## 1. Setting and the precise splitting operation

Retain F62's finite field k=F_q, ell-adic coefficient field E, X=P^1, Y=X times X, diagonal i:Delta→Y and open complement j:O→Y. In the mixed constructible derived category put
\[
 \mathcal I=i_*E_X,\qquad
 \mathcal B=E_Y,\qquad
 \mathcal H=j_!E_O.
 \tag{WG1}
\]
Convolution is the actual pull-tensor-compact-push operation of F62; I is its unit.

For a mixed complex A on a finite-field variety define the additive splitting operation
\[
 \mathsf G(A)=
 \bigoplus_{r,w}\operatorname{gr}^W_w\,{}^pH^r(A)[-r].
 \tag{WG2}
\]
The perverse weight filtration and its strict functoriality are BBD Theorem5.3.5, pp136–137. We retain the original Weil structures on its graded pieces. On morphisms WG2 applies perverse cohomology and its functorial weight graded map, then takes their finite direct sum. Thus it is an explicitly defined additive operation. No triangulated exactness or compatibility with convolution is assumed.

The operation preserves the Grothendieck class and every finite-extension stalk Euler trace: perverse cohomology reconstructs the derived Euler class with its shifts, and each finite weight filtration reconstructs its perverse class. This assertion is only an additive Euler statement.

Open restriction is perverse t-exact and preserves both weight bounds. It therefore commutes with the weight filtration: restricting the filtration gives pure graded pieces of the same weights or zero, and uniqueness identifies it with the weight filtration on the restriction. Consequently
\[
                  j^*\mathsf G(A)\simeq\mathsf G(j^*A).
 \tag{WG3}
\]
The t-exactness is the smooth relative-dimension-zero case of the BBD discussion immediately before Proposition4.2.5, pp108–109; the two weight bounds follow from j^*=j^! and BBD5.1.14, p128. This is not an assertion that an arbitrary closed restriction preserves purity.

## 2. The weight filtration of the actual open kernel

The ordinary localization triangle is
\[
             \mathcal H\longrightarrow\mathcal B
             \longrightarrow\mathcal I\longrightarrow\mathcal H[1].
 \tag{WG4}
\]
The objects
\[
             P=\mathcal B[2],\qquad Q=\mathcal I[1]
\]
are perverse, pure of weights 2 and 1 respectively. They are shifted constant sheaves on smooth connected varieties, with closed pushforward for Q. The shift convention is exactly BBD5.1.8.

After shifting WG4 by 2 and taking perverse cohomology, the only nonzero part is the short exact sequence
\[
                 0\longrightarrow Q
                 \longrightarrow\mathcal H[2]
                 \longrightarrow P\longrightarrow0.
 \tag{WG5}
\]
In particular H[2] is perverse; this conclusion follows directly from the triangle and does not require an unverified affine t-exactness premise.

Because Q and P have weights 1 and 2, WG5 is the weight filtration:
\[
 W_1(\mathcal H[2])=Q,\qquad
 \operatorname{gr}^W_2(\mathcal H[2])=P.
\]
Uniqueness of the weight filtration justifies the identification. It follows that
\[
               \mathsf G(\mathcal H)
                  =\mathcal B\oplus\mathcal I[-1].
 \tag{WG6}
\]
Also G(B)=B and G(I)=I. The open-kernel extension has become an explicit direct sum while its Euler class remains [H]=[B]-[I].

## 3. A complete two-factor failure of convolution compatibility

### Proposition WG-A

The operation G is not strong monoidal for the unchanged standard convolution, even on the two-fold product of H:
\[
       \mathsf G(\mathcal H\star\mathcal H)
            \not\simeq
       \mathsf G(\mathcal H)\star\mathsf G(\mathcal H).
 \tag{WG7}
\]

### Proof

Since I is the unit and B is the constant full kernel,
\[
 \mathcal B\star\mathcal I=\mathcal I\star\mathcal B=\mathcal B,
 \qquad
 \mathcal B\star\mathcal B
     \simeq \mathcal B\otimes R\Gamma(P^1,E)
     \simeq\mathcal B\oplus\mathcal B(-1)[-2].
 \tag{WG8}
\]
These are actual geometric identifications: the middle point is an independent P^1 and the product is proper. The cohomology of P^1 is E in degree zero and E(-1) in degree two.

Using WG6 and distribution over finite direct sums,
\[
 \mathsf G(\mathcal H)\star\mathsf G(\mathcal H)
   \simeq
   \mathcal B\oplus
   \mathcal B[-1]^{\oplus2}\oplus
   \mathcal B(-1)[-2]\oplus
   \mathcal I[-2].
 \tag{WG9}
\]
Restriction to O removes the last summand, so its ordinary degree-zero cohomology is E_O and is nonzero.

On the other hand F62 identifies
\[
                  j^*(\mathcal H\star\mathcal H)=\mathcal K,
\]
where K is the relative G_m compact-pushforward complex. Its only ordinary cohomology sheaves are
\[
                  H^1\mathcal K=E_O,\qquad
                  H^2\mathcal K=E_O(-1).
 \tag{WG10}
\]
On the smooth two-dimensional O these are lisse. Its perverse cohomology is therefore
\[
 {}^pH^3(\mathcal K)=E_O[2],\qquad
 {}^pH^4(\mathcal K)=E_O(-1)[2],
 \tag{WG11}
\]
and zero otherwise. One can check the degrees directly by restricting the perverse t-structure to complexes of lisse sheaves, where it is the ordinary t-structure shifted by two. Equivalently, apply perverse cohomology to F62's Chern triangle; its two end terms are in perverse degrees four and two. Both displayed perverse sheaves are already pure, of weights 2 and 4.

Hence WG3 gives
\[
 j^*\mathsf G(\mathcal H\star\mathcal H)
       \simeq E_O[-1]\oplus E_O(-1)[-2].
 \tag{WG12}
\]
Its ordinary degree-zero cohomology is zero. This contradicts the nonzero degree-zero cohomology of the restriction of WG9. The two objects cannot be isomorphic, proving WG7. QED.

The difference on the open stratum is the nonzero pair E_O direct sum E_O[-1], whose Euler class vanishes. Thus the calculation is fully consistent with preservation of all trace functions. What fails is the required operation comparison, not the Euler identity.

The proof does not depend on choosing a noncanonical splitting of a pure arithmetic Frobenius module. It uses the canonical weight filtration and the stated perverse cohomological shifts.

## 4. Perverse cohomology alone and ordinary cohomology do not solve it

Consider the additive perverse-cohomology splitting
\[
                   \mathsf P(A)=\bigoplus_r{}^pH^r(A)[-r].
 \tag{WG13}
\]
Since H[2] is perverse, P(H)=H. But by WG11,
\[
 j^*\mathsf P(\mathcal H\star\mathcal H)
        =E_O[-1]\oplus E_O(-1)[-2],
\]
whereas
\[
 j^*(\mathsf P(\mathcal H)\star\mathsf P(\mathcal H))
        =\mathcal K.
\]
F62's nonzero Chern class proves that these are not isomorphic. Thus perverse-cohomology splitting alone is not strong monoidal for this convolution.

Exactly the same argument applies to ordinary cohomology splitting
S(A)=direct sum_r H^r(A)[-r], since H is an ordinary sheaf and K has the nonsplit two-degree extension. Moreover it does not commute with the actual relative compact-pushforward followed by ordinary base cohomology: F62 gives total dimension two for RΓ(O,K), but four for RΓ(O,S(K)). These are precise incompatibilities, not a claim that weight filtrations or truncation functors do not exist.

## 5. The intermediate-extension quotient is not an exact monoidal extraction

The quotient H[2]→B[2] in WG5 is the known intermediate-extension quotient:
\[
                  j_{!*}E_O[2]=E_Y[2].
\]
The constant rank-one local system extends to smooth Y; BBD Lemma4.3.2, pp112–113, gives this middle-extension identity. It is a canonical proper pure candidate, but it changes the chosen generator.

### Proposition WG-B

There is no exact strong-convolution functor from a triangulated kernel subcategory containing H,I and the required scalar shifts and localization triangles to the same standard kernel category which:
1. sends the unit I to I;
2. commutes with Tate twists and cohomological shifts;
3. sends H to B.

### Proof

Let L denote the scalar coefficient class [E(-1)[-2]]. F62's actual two localization triangles give, in the kernel Grothendieck group,
\[
                    [H]^2=(L-1)[H]+L[I].
 \tag{WG14}
\]
An exact functor induces an additive K0 map; strong monoidality preserves the product. The three hypotheses would therefore force
\[
                    [B]^2=(L-1)[B]+L[I].
\]
But the actual proper relation WG8 gives
\[
                    [B]^2=(L+1)[B].
\]
Subtracting forces 2[B]=L[I]. Restriction to O gives 2[E_O]=0, impossible: ordinary generic Euler rank on O is an integer-valued homomorphism and sends this class to 2. This proves the proposition. QED.

The functor is required to preserve the unchanged convolution and scalar comparison. Without exactness, an induced additive Euler relation is not automatic; without preserving the coefficient/unit, the proof does not apply. It does not rule out changing the algebra presentation or choosing B as a different canonical generator.

## 6. A positive restricted construction that does exist

The closed kernel B has the genuine proper relation WG8. Iterating the same correspondence gives actual coherent isomorphisms
\[
       B^{\star r}
       \simeq R\Gamma(P^1,E)^{\otimes(r-1)}\otimes B
       \simeq R\Gamma((P^1)^{r-1},E)\otimes B
       \quad(r\ge1).
 \tag{WG15}
\]
All parenthesizations integrate the same independent middle factors. The associativity maps come from that common product correspondence. Its cohomological coefficients are positive Tate multiplicities with the usual projective Lefschetz maps.

Thus the classical closed/IC kernel supplies the expected proper positive model in this rank-one setting. This is a known construction, not a new general canonical-basis theorem. It does not make G or P monoidal on the original category, and it is not an extraction functor sending the old open generator to the new one while preserving its relation.

No assertion is made that G is naturally the identity on a full subcategory containing every possible derived morphism between these split objects. The actual proper kernel operations WG8 and WG15 are the positive construction being claimed.

## 7. What this says about the vanishing factor and the v=1 cell condition

The canonical weight graded operation preserves the derived Euler class, and therefore preserves any formal character and its evaluation at v=1 wherever the original comparison defines that evaluation. It nevertheless fails to preserve the actual convolution. Perverse or ordinary cohomology splitting removes the Chern extension but fails for the same operation.

Consequently this specific procedure cannot simultaneously be used as a strong monoidal extraction of the nonproper torus coefficient and as an unchanged model of the standard ambient action. F62 already showed that the torus coefficient has no tensor inverse in the finite derived coefficient category. The present result tests a different proposed repair, passing to canonical weights or cohomology, and supplies a separate explicit failure.

This is not an assertion that all filtered monoidal enhancements, Rees constructions, or spectral-sequence models are impossible. Such a construction would have to retain the missing extension/differential data or change the target operation, and prove its comparison. The two objects in WG7 identify exactly what an unchanged-operation claim must explain.

For IV's designated nonstandard cell refinement, equality of the Euler specialization alone still does not identify the actual coordinate submodules or their maps. If an additional extraction claimed strict effective generator matrices in that same regular cellular comparison, F58 would apply. This report does not deduce an IV/VIII basis identification from the standard flag example.

## 8. Separate Grothendieck dictionary and primary checks

BBD's actual weight filtration is canonical and strictly functorial. It produces graded perverse objects, but BBD does not assert that the reconstructed additive splitting WG2 commutes with arbitrary convolution. The counterexample computes the two sides using actual six-operation correspondences and their perverse degrees.

The effective/virtual character distinction remains the SGA3 I4.7.2–3/cote90 scan17 and SGA6 V Sections2–3/cote133 scan18 framework. The zero Euler pair E_O plus E_O[-1] is not a zero derived object. A K0 identity therefore cannot identify the two geometric compositions. SGA6 I Definition4.7 pp121–122 and Example4.8 p122 supplies the bounded coefficient-complex language; no lambda-ring structure is asserted for the kernel algebra.

The standard affine locally free sheaves use EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90–92. The proper closed-kernel convolution is an actual product pushforward, and its projective coefficient follows from the usual Kunneth/projective-space facts. No archival text is claimed to identify this rank-one construction with the nonstandard canonical category.

Original primary contexts read for this note:
- BBD Section4.0, p102: lisse sheaf on a smooth d-dimensional variety shifted by d is perverse.
- BBD discussion preceding Proposition4.2.5, pp108–109: f^*[d] is perverse t-exact for f smooth of relative dimension d; for the open immersion d=0.
- BBD Lemma4.3.2 and its proof, pp112–113: extension of an irreducible lisse sheaf on a smooth irreducible variety is its intermediate extension from a dense open.
- BBD5.1.8, pp126–127: the cohomological shift in complex weights.
- BBD5.1.14, p128: the six-operation upper/lower weight bounds, applied to open j^*=j^!.
- BBD Theorem5.3.5 and its strictness proof through Lemma5.3.6, pp136–137: the unique finite increasing weight filtration and strict functoriality.
- F62's primary Milne projective-space, compact-support and operation locators, already freshly checked in agent_F62_nonproper_kernel_review.md. The construction here uses those same actual kernels and triangles.

Local original BBD files: primary_sources/BBD.pdf and primary_sources/BBD.txt.
Primary publication URL: https://www.numdam.org/item/AST_1982__100__1_0/.

Actual proof checks:
1. Reconstructed the perverse long exact sequence of WG4 shifted by 2, including all indices in WG5.
2. Identified the canonical weight filtration from the weights 1 and 2, rather than choosing an arbitrary splitting.
3. Recomputed both sides of the proposed monoidal comparison and their restrictions to O.
4. Verified the perverse indices 3,4 of the coefficient K using the two-dimensional lisse convention.
5. Checked the exactness, scalar and unit assumptions needed for the K0 obstruction WG-B.
6. Checked the positive proper-kernel iteration separately and retained its different-generator scope.
7. Retained the distinction between Euler specialization and the designated nonstandard cellular fiber.

Independent whole-proof review is requested before integration. No master paper or shared master log has been edited.

