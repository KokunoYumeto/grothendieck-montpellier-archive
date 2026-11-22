# C.3bk: complete independent proof audit

**PASS, completed 2026-11-19 15:10:31 UTC.** We read the complete seven-step `../real_weil/C3_higher_product_integral_kernel_draft.tex`, including its final consequences and limitations. This is an independent-agent re-proof by `/root/cycles`, GPT-6 Astra Pro, RESEARCH_SA06, not an independent-model verification.

The certified mathematical scope is the exact order-p ordinary restriction kernel for every algebraically closed characteristic-p field in the stated ranges: r=2,N≥4; r=3,N≥7; r≥4,N≥3r−1. The examples can be defined over the algebraic closure of the prime field. The proof itself does not claim the remaining high intervals, nor rational nonvanishing.

## 1. All-factor geometry and cohomology

The cubic models and their rank-two divisor cup are precisely the all-characteristic inputs independently audited for bj. The characteristic-three cubic is smooth by the full derivative calculation, while the Fermat cubic covers every other prime, including two. The two normal quadratics along the displayed line yield the off-diagonal nondegenerate bilinear form without a factor of two.

For each cubic, the hypersurface sequence proves H^j(W,A^n)=0 for j>0,n≥0. Tensoring the factors and adjoining the curve and projective space gives every vanishing in (C.3bk.4). In particular all cohomology of L^n in degrees at least two vanishes for n≥0; H¹(L^n) vanishes for n≥2. These statements have no dependence on the number of factors or on p. The product has Pic⁰ equal to the curve Jacobian because the cubic and projective factors have trivial Pic⁰.

The incidence choices form the intersection of nonempty opens in one irreducible affine parameter space. Successive very ample sections give the expected smooth base scheme, or an empty base after the dimension threshold. The three displayed tensor coefficients provide an explicit rank witness. The tensor product of the rank-two maps has nonzero image on that witness. For m=0,r=2, a three-dimensional coefficient space cannot be contained in the two-dimensional kernel of the cubic cup. In each case the rank conditions meet the smooth-divisor open. All these opens are defined over finite fields and therefore contain closed points after finite extension. The finite enumeration specifies the choices without pretending that this infinite family of searches has been executed or timed.

We checked smoothness of the incidence divisor at base points using independence of section differentials and away from them using the projective-coordinate derivative. The separate m=0 assertion uses the imposed Bertini smoothness. No characteristic-zero Bertini statement is substituted in positive characteristic.

## 2. Actual resolution and principal target

The total-line equation and Segre graph contraction retain the properties checked in bj for any number of smooth cubic factors. The line coordinate has the inverse external-product weight, so F+τℓH is a well-defined section. The primitive linear equation in τ is integral because F and ℓH have no common factor. The connected exceptional product lies in the regular locus. Properness removes the image of all remaining nonregular points when the base is localized at the vertex.

Consequently the entire resulting projective resolution is regular, and m_R O_Z=I_V holds chart by chart from the complete degree-one Segre generators. Each projection to W_i survives and gives an actual divisor line bundle. The strict transform of f=τℓ is the split line bundle over the smooth incidence divisor. Thus both punctures in the theorem are regular. The dimension is m+2r exactly.

## 3. The actual Picard family and nonzero ordered product

The first Picard extension has vector part U₀=H¹(V,L), and its extension-class image is the rank-three space spanned by the g_j. The ordinary Verschiebung kills the relevant coherent H¹ and has étale kernel (Z/p)³. The integral Hom–Ext calculation gives a lifted homomorphism b whose finite kernel-point images span U and are independent. Because the product cup is nonzero on U, at least one such point η gives the desired nonzero coherent class.

The designated Künneth summand is exactly

H⁰(P^m,O(1)) ⊗ (⊗ H¹(W_i,A_i⊗Ω¹_Wi)) ⊗ H¹(C,K_C).

Its cohomological degree is s+1=r and its differential degree is s=r−1. The fixed ordered product of one divisor from each cubic enters this summand with coefficient one up to the fixed sign; it is not a power of a sum of divisors. Therefore no factor s! appears, even if p≤s.

The target first neighbourhood is split. The vector component of the restriction of b vanishes by properness, while its Picard component factors through Verschiebung and kills η. The divisor sequence gives the exact quotient H¹(T,L_T)=U₀/U and the higher target uniqueness vanishings. No assertion that Pic⁰(T)=J is needed.

We checked the full actual-family construction. Pullback of the normalized Poincare bundle to a smooth proper curve through 0 and η has vanishing first mixed obstruction. The first lift is normalized by a constant inverse fibre. All higher obstruction groups vanish by the displayed cohomology and the one-dimensional parameter. Formal existence followed by finite-data Popescu descent and henselian smooth lifting modulo m² gives an actual bundle on the fixed product Z×P. Higher endpoint uniqueness and the punctured Picard comparison prove A^p|_X=O_X and A|_Y=O_Y. This is sufficient for ordinary algebraic equivalence and does not rely on a varying henselized parameter space.

## 4. All-degree Milnor cohomology, not ordinary K-groups

The proof expands the full higher-degree divisibility induction from our auxiliary file. The projective-space localization shifts are G^{a−1,b−1}; the open affine group lifts by projection. For product point blow-ups, proper/open compatibility makes c−ρ*ρ_*c supported on the exceptional P¹×Q. These two operations preserve divisibility on the diagonal b=a+1. The base curve groups are k*, the tame-symbol cokernel of a direct sum of k*, and zero above degree one. This proves H^{r−1}(V,K^M_r) divisible in every characteristic. No higher Milnor–Quillen comparison is asserted.

The relative symbol sheaf J_r is locally generated by symbols with one entry 1+i; ordinary unit and Steinberg lifting justify the exactness. Thus pJ_r=0. Local smoothness splits the square-zero algebra and proves the injectivity on the left of the conormal sequence. Its rank-one conormal submodule gives the canonical exterior-power kernel I⊗Ω^{r−1}. Ordinary dlog defines τ_r, with the stated coefficient-one normalization and zero image for symbols with multiple infinitesimal entries. The proof retains those symbols rather than falsely setting them to zero at p=2.

The actual line transitions define a relative Čech cocycle and hence a sheaf-cohomology class, without assuming the cover is acyclic for J_r. Its coherent image is nonzero. The preceding divisible group kills the connecting map to the p-annihilated relative cohomology, so the relative class injects into H^r(E,K^M_r). This is the precise absolute detector required later.

## 5. Every exceptional class is removed in exactly the advertised ranges

For m≥r, the top projective-bundle coefficient starts a triangular elimination. For m=r−1 the remaining coefficient is an integer b and the recurrence gives b c^r=0. Intersecting with the required additional power of the ample class gives a strictly positive integer times b, so b=0. This uses integer Chow coefficients even when p divides the intersection degree.

The two additional endpoints are fully integral. The product Chow decomposition follows by the actual point-product blow-up maps and projective-bundle formula; their external generators and self-intersections give the stated cubic ring. This is not an unsupported Künneth theorem for arbitrary varieties.

For r=2,m=0, the equations A·d=0 and d⊗K_C+A⊗λ=0 give 4d+deg(λ)A=0. Pairing with A²=3 forces deg(λ)=0, then d=0, and the primitive exceptional coefficient −1 of A forces λ=0. This proves the new fixed-field N=4 endpoint, including over the algebraic closure of a finite field.

For r=3,m=1, the recurrence reduces to c²(d₁+d₂+λ)=0. Its pure cubic components give the two integer equations in (C.3bk.21). Their pairings force x=y=0 and hence d₁=d₂=0 in free cubic Picard lattices. The remaining pure and mixed coefficients give 3λ=0 and 2λ=0. Thus λ=0 in the full Picard group. This is the same complete proof in `exceptional_cubic_lattice_draft.tex`; its new general Smith reduction is not required for bk.

## 6. Nonvanishing of the actual cycle and its quantifiers

If β vanished on X, Chow localization and self-intersection would put its exceptional preimage in the kernel just proved zero. Hence β would vanish on the regular resolution itself. Descending the finitely many line bundles and a hypothetical finite rational-equivalence witness to one regular finite-type étale stage makes the integral Milnor Bloch formula and its product compatibility applicable in the usual smooth setting. The étale stage with unchanged residue field has the same first infinitesimal neighbourhood. Restriction to it contradicts the nonzero relative class. No Bloch formula for E or unproved cohomology-limit comparison is needed.

The actual A family multiplied by the fixed divisors proves ordinary algebraic triviality. Its pth power and target triviality give an exact-order-p restriction kernel. The final synthesis correctly distinguishes universality over all algebraically closed coefficient fields from the fixed algebraic-closure-of-finite-field examples supplied here. The earlier lower-dimensional examples may require their specified transcendental fields. No rational conclusion is drawn from these p-torsion classes.

## 7. Exact sources and finite checks

For this audit we freshly followed the individual Stacks Lemma33.47.3 link and read Tag0FD6, https://stacks.math.columbia.edu/tag/0FD6 . It is the same complete lemma/proof earlier read under its section Tag0FD4; the individual locator in bk is correct. Exact Jiang Theorems2.4/2.8(3) with their integral maps and Stacks02TX were freshly reopened in this window for the exceptional-lattice proof. The full Rost, Kerz, Braunling and relative-conormal source records are retained in `K2_COHOMOLOGY_SOURCE_AUDIT.md` and the bj review. Earlier Picard formal-existence sources were reused as audited antecedents, not all claimed freshly reopened in this specific pass.

No bk-specific finite certificate was present at the time of this completed proof check. The nine-case cubic-lattice code/output was separately inspected and executed by this agent, with its exact runtimes retained. It supports the lattice calculations but does not replace the proof of the all-r geometry or the actual-family construction. Any later bk-specific computational review will be separately dated.
# Finite certificate addendum, 2026-11-19 15:17:33 UTC

I read the entire author program `../real_weil/code/check_C3bk_higher_product_kernel.py` and all 91 recorded check outcomes plus the exact matrices, recurrences, degrees, tensor-cup metadata and prior-certificate hashes in `../real_weil/output/C3bk_higher_product_certificate.json`.  The finite certificate passes inspection.  Its author execution began at 15:10:53.456062 UTC and took 0.176992202999827 seconds; I did not rerun it.  The determinant −12288 is −3·4⁶, the degree-3 coefficient system has determinant 3 over the integers, and the independent 2/3 coefficient equations kill all Picard torsion.  The 91 checks comprise 33 recurrence/degree checks, four endpoint checks, and 54 coefficient-one tensor-cup checks.  The program expressly does not certify Bertini, formal-to-actual family existence, sheaf arguments, or arbitrary-r geometry.  Those were independently proved in the preceding review.

