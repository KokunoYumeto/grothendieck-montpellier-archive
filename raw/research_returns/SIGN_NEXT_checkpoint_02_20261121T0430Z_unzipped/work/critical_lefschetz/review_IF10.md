# Independent review: IF-10 CM geometric coefficient realization

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/critical_lefschetz.
Date: 2026-11-21 03:52:43 UTC.
Full IF-10 source read: `cm_geometric_realization.tex`, SHA256 `166758a4aa5de41cccdcfc62e6b0b585e30dc3acebcfb5309c103ce87af11b8e`.
New IF-09 divided-power paragraph read: `kernel_intertwiner.tex`, SHA256 `c6927a4e89b4ceb3c88ed499422991ecacab88139a97623b5596fe6f27a1f4f4`.

## Verdict and mathematical scope

**The complete IF-10 proof is accepted in its explicitly conditional, normalized form.** I independently reconstructed the eigensummand and matrix-unit construction, the saturated polynomial lattice, the pairing and inverse-character normalizations, and the effect of coefficient-field extension. No unresolved proof gap remains in this version. This is an actual construction with algebraic correspondences on powers of the specified CM elliptic curve. After the character normalization its objects are sums of unit motives. Consequently it is a geometric model of the supplied coefficient linear algebra, and does not prove that the original global theta chain has those motives, Frobenius eigenvalues, or L-functions. It also does not identify the maps with a common Lefschetz operator.

The coefficient-field hypothesis is essential. The cited source interfaces are rationality hypotheses and conditional descent theorems. They are now described accurately. IF-10 applies to a supplied instance with those properties; it does not instantiate the still missing global m=2 data or calculate its unprovided moments. It therefore advances the explicit geometric coefficient-model question without closing the stronger global Q6g assertion or its nonzero composed period.

## Independent derivation of the complete proof

### CM eigensummand and primitive lattice

On the square torus the stated action sends e to -f and f to e. Thus u=e+if is an i-eigenvector and the kernel equation over R gives exactly Ru, including at primes above 2. The matrix with columns u,f has determinant 1, so Ru is a direct summand of the ambient R-module; primitivity here does not require the rational projector to be integral.

With the specified push-to-second-factor convention, the cycle point-times-E acts on H0, E-times-point acts on H2, and their complement acts on H1. The transpose graph of [i] acts by pullback. Therefore (1-i[i]*)/2 on H1 is an algebraic idempotent with the asserted image. Its square is itself because [i]* squared is -1. Equality of actions is equality in the stated homological correspondence category, by the Kunneth/Poincare identification.

### Pairings, signs and cohomological exterior powers

Direct calculation gives psi(u,bar u)=-2i, the bilinear self-pairing zero, and Hermitian norm 2. For x=a u and y=b u, psi(x,bar y)/(-2i)=a bar(b), so division by 2 in the Hermitian form makes the chosen lattice generator have norm 1. The claim is restricted to the eigenspace and the selected complex embedding; no integral global cup-polarization assertion is made.

The column construction uses actual H^h(E^r), with one degree-one factor on each selected coordinate and degree zero on all other coordinates. Ordered cup products give the ordinary exterior signs. This avoids the common error of applying an unqualified categorical exterior-power projector to the odd motive h1. Each selected tensor has a coefficient equal to 1 on its all-e component, is primitive, and sits in a distinct integral Kunneth summand. Tensoring separate column blocks preserves these direct-summand embeddings. Hence the ambient exterior-tensor lattice has exactly the claimed saturated embedding.

Coordinate projections, insertions of degree-zero factors and ordered coordinate permutations identify every selected summand with M tensor-power d. Projecting to the source summand and including into the target summand gives E_JI; composition has delta_(I,L) E_JK. The fixed increasing order controls all degree-one signs. This explicitly supplies algebraic matrix units, including rectangular ones when the cohomological degree agrees.

### Cyclic polynomial projector and its lattice

For an integral basis matrix C of the primitive cyclic lattice T, C-transpose-C is a nonsingular positive rational Gram matrix. P=C(C-transpose-C)^(-1)C-transpose is the identity on T_Q and zero on its orthogonal complement. Inserting its entries into the preceding matrix units produces the claimed algebraic idempotent. Saturation proved in IF-08 implies that its rational image intersects the integral ambient tensor lattice in T; the quotient is free over Z and this property survives extension to R. The displayed determinant bounds the denominators by the adjugate formula.

All ambient selected monomials have Hermitian squared norm 2^d and are mutually orthogonal. Thus multiplication by 2^(-d) gives precisely the exterior Gram matrix on T, hence the normalized Fock form of IF-04. Neither the integral Fock dual nor the projector denominators are silently replaced by the native integral cup lattice.

Each coefficient A_beta and each finite K-valued combination B_J is now represented by the corresponding algebraic matrix-unit combination, with source and target projectors. Its entries on the specified lattice remain the original entries. Algebraicity of the rational correspondence does not imply integrality of its cycle coefficients; the proof correctly distinguishes these assertions.

### Determinants, negative powers and the prime-2 comparison

The determinant of r copies of M is M^r, with the ordered generator. The proof uses the abstract dual integral line already for every negative determinant exponent. Under the polarization, M-dual is the conjugate line with Tate twist, but its generator is represented by bar(u)/(-2i), not by bar(u). Evaluation is therefore 1 on the chosen abstract-dual generators. The algebraic polarization and its coevaluation give an inverse up to a nonzero scalar on the one-dimensional realization, so the tensor inverse exists in the homological category.

For the collapsed pair M^w and M^(-w), native saturated opposite eigenlines evaluate to the ideal (2i)^abs(w), up to a unit. The proof explicitly distinguishes this from a raw presentation with d positive copies and r*abs(s) negative copies: changing those native negative factors to abstract duals contributes (-2i)^(-r*abs(s)), while raw pairwise cancellation contributes (-2i)^min(d,r*abs(s)). These are precisely the factors needed to avoid an unnoticed change of 2-adic index.

After tensoring by M^(-w), the object is a sum of unit motives. Evaluation generators fixed to 1 identify all matrices, including maps changing d or w, with their original coefficient matrices. Finite invariant subspaces admit algebraic matrix projectors over the coefficient field. Their lattices and any nonfree global projective lattice are retained as specified lattices; the proof does not claim every such lattice is a native full cohomology lattice.

### Coefficient extension and numerical weights

A finite ring-of-integers extension is finite locally free and faithfully flat. Consequently each determinantal ideal extends, contraction recovers it, and at a local extension the uniformizer valuation is multiplied by the ramification index. This proves the stated comparison of Smith factors and local lengths, with no false equality of absolute finite indices across fields.

Independent summation of the partitions gives d=(113,841,889), and adding r*s for r=(8,24,40), s=(3,-96,-106) gives w=(137,-1463,-3351). At the modified numBig place the decrease is 3 in each weight, with unchanged differences -1600 and -1888. These are per embedding factor; the full exponent for a common M is their sum over embeddings, as the proof states.

Under the selected embedding M^w has type (w,0). Tate twists give (w-a,-a). Equality with (w'-b,-b) forces a=b and w=w'. Thus Tate twists cannot supply the nonzero unequal-character arrows in this specified model. The CM-character cancellation is a real change to the Hodge and Frobenius data. It cancels eta^w in the l-adic realization, and therefore does not preserve an unidentified automorphic L-function. The good-reduction exclusion at 2 is also explicitly separate from retaining a coefficient lattice at 2.

## Source interfaces independently read

- `ThDistC.lean`, Amb.JetsRat: existence of a K-valued preimage for each chiF-normalized period derivative is a defined hypothesis.
- `KernelLocalFactors/ThDistC.lean`, jetK_spec: given that hypothesis, the chosen algebraic moment realizes the normalized complex derivative.
- `JetFieldLeKR.lean`, KerEntTied.KerJets: the relevant product rhoDet*rhoDet' multiplies the period-normalized jet before algebraicity is asserted.
- `DataForms.lean`, KRat/KL/KL_spec: KRat is a rationality hypothesis, KL is conditional descent, and KL_spec identifies its complex realization.

These reads were source checks, not a new Lean build or verification of a closed global instance.

## New IF-09 divided-power obstruction

I read and independently checked the complete added paragraph. For one fixed integral symplectic raising operator, L^(a)L^(b)=binomial(a+b,a)L^(a+b). When a,b are positive, the binomial coefficient exceeds 1, so the composite maps into that integer multiple of the exterior lattice (or is zero). The fixed primitive norm-one output in the test chain therefore contradicts a saturated final integral embedding, and also contradicts an isometric integral embedding. The restriction to one fixed L remains essential; the paragraph retains it and does not exclude different Lefschetz pairs or tensor-functor realizations.

No contribution file was edited by this reviewer.
