# Independent whole-proof audit: compact U(3) Hecke computation

**Finding K17-U3-HECKE-AUDIT.** 2026-11-21 UTC; checker `/root/vandiver_k`, GPT-6 Astra Pro, effort not exposed; run K17.

**Verdict: PASS for the precise theorem K17-U3-HECKE.** I independently read the entire `u3_hecke_section.tex`, every line of the standalone `u3_orbit_certificate.py`, and its entire JSON output, then reran the verifier. I reconstructed the mathematical correspondence separately from the exact arithmetic. No correction is requested. This audit does not incorporate a broader global coverage theorem or the source's rank-two conductor calculation into this finite theorem.

## 1. Class number and integral stabilizer

The covering-radius squared of the Eisenstein lattice is 1/3. The Euclidean algorithm and PID conclusion follow with strict norm decrease. A shortest vector in any positive definite Hermitian O_E-lattice is primitive; a nonprimitive vector would be divisible by a nonunit and have greater norm than its quotient. Over the PID, it extends to a basis. The orthogonal projection of the complement is again a discrete free O_E-lattice, so successive shortest primitive choices give a genuine basis of the original lattice.

For Gram–Schmidt lengths a,b,c, reducing the coefficient along the shortest vector gives an actual lattice vector of length at most b+a/3. Hence b ≥ 2a/3. Applying the same argument to the projected rank-two lattice gives c ≥ 2b/3. Thus 1 = abc ≥ 8a³/27, so the positive integral minimum a equals one. A norm-one vector splits integrally: its Hermitian pairing with every lattice vector lies in O_E, allowing exact projection subtraction. The complement is integral and determinant one. The rank-two argument 1 ≥ 2a²/3 again forces a norm-one vector, and rank one finishes the classification.

Every adelic translate is locally selfdual and its global intersection is integral unimodular; conversely the localizations recover the translate. Thus the proved lattice classification supplies class number one for the full adelic lattice stabilizer. This is an isometry in the original rational Hermitian space: an orthonormal O_E-basis gives its rational unitary matrix. The integral stabilizer consists precisely of monomial unitary matrices, since the norm of an integral vector is a sum of nonnegative integers and every norm-one vector has one unit coordinate. Consequently Γ = μ₆³ semidirect S₃, exactly as used in the coefficient calculation.

## 2. Complete coefficient space

For the bidegree (5,5) polynomial space, Δ is surjective onto bidegree (4,4). I checked the displayed recurrence directly: for R = Σ z_i conjugate(z_i) and F of bidegree (4,4),

    Δ(R^(j+1) Δ^j F) = (j+1)(11−j) R^j Δ^j F + R^(j+1) Δ^(j+1) F.

The given coefficients cancel consecutively, and Δ⁵F = 0. The harmonic kernel therefore has dimension 21²−15² = 216. The highest-weight vector conjugate(z₁)⁵z₃⁵ for the displayed inverse action has weight (5,0,−5); its irreducible representation has dimension 6·6·12/2 = 216. Compact semisimplicity therefore identifies the whole harmonic kernel with that representation, rather than just embedding an unverified component.

Independent sixth-root actions force equal holomorphic and antiholomorphic exponents in every coordinate because each exponent difference lies in [−5,5]. Hence the entire invariant subspace is the symmetric degree-five space in x_i = z_i conjugate(z_i), with the five listed partitions. I reconstructed the Laplacian matrix: Δ x_i^n = n² x_i^(n−1), and sums over distinct monomial permutations give precisely the four rows printed in (UH.5). The first four columns have determinant 25·16·18·9 = 64800, so the kernel has dimension one. The stated coefficient vector lies in it and takes value two at e₁. Thus the algebraic modular-form space is exactly one-dimensional.

## 3. Every neighbor and the actual action

For each listed U, the integral identity U*U = pI gives g = U/π in G(Q), with U⁻¹ = U*/p. At π, all elementary-divisor valuations of U are zero or one; rank one modulo π forces (0,1,1). Thus g has exponents (−1,0,0). Hermitian duality gives (0,0,1) at the conjugate factor. It is integral invertible at all other primes. Its enlarged π-lattice is determined exactly by im(U mod π), a line in the projective plane over F_p, and the conjugate lattice is forced. These data classify the full right-coset set, with p²+p+1 elements.

The automorphic convention F(γgk) = ρ(γ)F(g) makes evaluation at the sole class identify the Hecke operator with the sum of ρ(g_line) over those right cosets. Since ρ(g)f(z) = f(g⁻¹z), g⁻¹e₁ = U*e₁/conjugate(π); its coordinates are the conjugates of the **first row** of U, divided by conjugate(π). The resulting contribution is exactly p⁻⁵ f(N(U₁₁),N(U₁₂),N(U₁₃)). Right changes by Γ preserve f. Left elements of the subgroup preserving C e₁ act by a scalar of absolute value one on that line and preserve the evaluation. This verifies the orbit reduction using the actual inverse-action convention.

The p+1 lines in the last-two-coordinate plane have rational representatives in the rank-two unitary subgroup by the independently proved rank-two class number one. They fix e₁. The first coordinate line has the displayed diagonal representative with scalar of absolute value one. Thus all p+2 exceptional terms have first-row norm pattern (p,0,0).

For the remaining normalized lines (1,a,b), the subgroup acts by independent images of μ₆ on a,b and by interchange. At seven its unit image is the entire nonzero field, giving orbit sizes 12 and 36. At 13 the image is exactly the nonzero squares; distinguishing zero, square and nonsquare and interchanging the two entries gives precisely the five listed orbits of sizes 12,12,36,72,36. The verifier enumerates these sets, proves them disjoint, and checks their union against all (1,a,b) with (a,b) ≠ (0,0). No unenumerated line remains.

The seven matrices are checked by exact Eisenstein arithmetic. Their columns have Gram pI, and every nonzero reduction is a scalar multiple of the stated representative line. The combined table and division by f(e₁) = 2 reproduce the scaled values 157899 and 6110859.

## 4. Direction and normalization

The computed matrices give the negative minuscule at the selected split factor. Complex conjugation exchanges the two local factors, carries every such right coset bijectively to a positive minuscule coset, and preserves every first-row norm and the polynomial f. Therefore the two operators have the same eigenvalue on this actual invariant line. This is a direct equality of the sums, not an inference from their common degree.

I freshly retrieved the author's primary paper, B. Gross, *On the Satake isomorphism*, https://people.math.harvard.edu/~gross/preprints/sat.pdf. Web retrieval references: `turn147389490view0`, `turn232441165view0`. I read the measure/convolution definition and coset formula in §2 and all of §3 through (3.13)–(3.14). Formula (3.14), printed p.8, says that the unnormalized positive diag(π,1,…,1) characteristic function has Satake transform q^((n−1)/2) times the standard character. At rank three this factor is p. Compact volume is one, so the right-coset sum has no division by |Γ| and no stabilizer-volume multiplier. Thus the result is indeed A_p = p⁵T_p⁺ = p⁶t_p.

The local direct PDF download returned HTTP 403, so this audit records the successful primary web reading without claiming a saved local PDF. The Satake theorem is used as published background; its entire underlying general proof is not claimed to have been independently reconstructed. The specialized factor and all finite arithmetic are reconstructed here.

## 5. Actual replay and scope

The standalone verifier imports only the Python standard library and reads no external data. I reran it successfully. It checks all seven matrices, complete disjoint unit orbits, the harmonic equation, weighted sums, and exact primality/product factorizations. Its output gives:

| p | cosets | weighted sum | A_p | p¹²+p⁶+1−A_p |
|---:|---:|---:|---:|---:|
|7|57|315798|157899|13841246952|
|13|183|12221718|6110859|23298083838432|

The proof already supplies the rank-four matrix minor and all geometric coverage; the verifier need not rediscover these conceptual arguments. I also read the U3 part of the separate full-neighbor replay script, including its exact line coverage and five additional vector identities, but did not rerun that second script in this audit because the standalone proof/certificate already resolves the finite arithmetic risk.

This proves exactly the group/level/coefficient Hecke theorem. Other automorphic representations enter the arithmetic argument only after the separately audited global and source-interface coverage statements. No full K₁₂ assertion is part of this audit.
