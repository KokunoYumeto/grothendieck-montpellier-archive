# Independent whole-proof review of R-30

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run CUE_GCT-20261121-purity.

Actual whole-proof review completed 2026-11-21 06:04:20 UTC during the checkpoint write freeze. Records written after release at 06:06:27 UTC. **PASS** for the complete submitted proof, SHA256 `58addc8f2b45d388bf03505a15816fd92ceec83a0dfd69b4490a10261e7c0c7d`. The later scope-only clarification, hash `a5f8e2e9076ab75e416e2d21bb074bf32b34bd24db00757c85c33bfe3bedd9b7`, was separately inspected: it correctly allows an independent padding line to add one essential variable beyond the span of the two sets of m factors and leaves that extra-row stability question open.

## Endpoint product normalization

I checked the entire nonconstant-spectrum k=m lemma. The Fourier vectors form a basis and the ordered tensor has zero moment. An operator preserving each ordered factor line is D times a circulant conjugate times D inverse. A nontrivial auxiliary extremal flag has a proper consecutive coordinate subspace (possibly viewed through its annihilator). A proper nonempty cyclic interval has no nonzero translation period; for every nonzero shift one corresponding off-block matrix entry is precisely that shift's circulant coefficient. Thus preserving the subspace forces every nonconstant circulant coefficient to vanish, leaving only a scalar. This establishes the finite stabilizer required by the ordered-tensor argument.

The existing minimum-weight and reverse Kempf–Ness normalization gives the desired product moment matrix. A unitary projective symmetry of that product commutes with its moment matrix, so it preserves the eigenspace flag determined by the auxiliary weight and hence the stable enhanced tensor. This proves only finite projective unitary stabilizer, exactly as stated; the underlying complex product stabilizer still has a torus.

## Rational padding tilt

The partition order and strict first-row inequality guarantee a smaller delta_j. If all deltas were equal, n/r<=a would contradict that strict inequality in the endpoint row range. The epsilon construction gives positive rational alpha,gamma of the same sum as A,B and smaller product. Its resulting rational t is in (0,1) for sufficiently small epsilon. I independently expanded the two-by-two determinant of `diag(delta)-a*ell*ell*`: it is `AB-a*(delta0-delta_j)*t`, exactly alpha*gamma. The remaining eigenvalues are untouched. The two new eigenvalues can avoid all old ones, so placing one in each block makes both endpoint spectra nonconstant.

## Compact and complex stabilizers at the full tensor

The block dimensions are in [2,m]. The prior prescribed-spectrum lemmas apply to both normalized rational block spectra. Orthogonality gives M(q)=C. Directional derivative independence and m>=3 separate the two off-diagonal infinitesimal block contributions; the compact projective stabilizers make each diagonal block scalar and degree m makes the scalars agree. Thus q has finite unitary projective stabilizer.

The full ordered padded enhanced tensor has zero traceless moment. Its compact stabilizer is finite because a projective symmetry preserves the q-factor line. The cited real-form result is applied at this full balanced tensor, where its hypotheses hold, and makes the complex vector stabilizer finite. A projective infinitesimal stabilizer has the same Lie algebra: zero moment makes the expectation of every complex traceless infinitesimal operator zero, so an eigen-scalar must be zero. Thus the tensor is stable. The minimum-weight argument then transfers stability under multiplication without any invalid additive product-moment assertion.

## Removal of the remaining finite group

Both explicit padded-form witnesses are valid. The q=P+Q polynomial is primitive and linear in y1 with coprime coefficients, hence irreducible. At r=2m its factor-block infinitesimal symmetries are diagonal; at r=2m-1 the first block is scalar because its m factor lines form a projective frame, and the second is diagonal. The displayed padding line forces one common scalar in either case. Unique factorization distinguishes q from the padding line even at exponent one. Therefore the finite-projective-stabilizer open for F is nonempty.

The stable enhanced open and that finite-F open meet in the irreducible parameter space including the auxiliary flag orbit. The flag is nontrivial because a rectangular strict direction is impossible at these endpoints. The PGL action on any such partial flag orbit is faithful: fixing every subspace of one proper nonzero dimension fixes each line. Thus a generic stable auxiliary flag avoids the fixed loci of the finite nonidentity padded-form symmetries. Any scalar symmetry of the resulting tensor is central, and the exponent ns-|eta|=r*nu_r makes its scalar action one. The invariant extraction and all-integer occurrence consequences then use the already checked G22/R28 arguments.

## Fresh primary-source check

I independently opened the primary Losev PDF, https://arxiv.org/pdf/math/0605756, and read the complete Theorem4 proof and the complete Theorem1 proof through equations (3)–(4), printed p2. At a moment-zero vector the compact orbit is isotropic; the resulting dimension inequality and the compact real form imply that the compact stabilizer Lie algebra is a real form of the complex stabilizer. This is the exact input used here. I did not audit the full proofs of the other theorems in the paper or the separate 1979 original.

No mathematical repair was requested. This is a complete independent-agent proof reading and rederivation, not a formal proof-assistant, external-referee, or bit-complexity certification.
