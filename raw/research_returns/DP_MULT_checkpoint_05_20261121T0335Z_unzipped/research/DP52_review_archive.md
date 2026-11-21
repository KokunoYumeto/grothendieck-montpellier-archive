# DP52: independent complete proof review

**Result: PASS for the complete saved version identified below.** No mathematical correction is required to its four proofs. The revised statement contains a positive endpoint construction, so the failed quadratic certificate is correctly restricted to the unchanged source wrapper.

Checker: `/root/archive_binomial`, GPT-6 Astra Pro. Runtime reasoning effort is not exposed. Targeted source/proof review began at observed 2026-11-21 03:15:10 UTC. The complete revised memo §§1–7 was then read in full in one output between observed 03:23:03 and 03:23:25 UTC, including all new EP9–11 arguments and final scope paragraphs. This is an independent mathematical and source-text check, not a Lean execution or an audit of any unrelated RH argument.

Whole memo SHA256: `7f0c16ed860a560f105beab2d54f5fb8f31559a721af828a4c194accf44aa2ee`.

The exact frozen memo, separate complete-section hashes and timing are in `late_proof_snapshots/DP52_check_metadata_archive.json`. Actual source ranges and their hashes are in `late_proof_snapshots/DP52_source_reads_archive.json`.

## 1. Smaller-parameter transport: DP52(a)

I checked every requirement against the actual `Ranks`, `TPar`, `Interlace`, `Centred`, `Dpar`, `Xpar`, `TParity`, `NCGaps` and `Hyp3` definitions.

The statement assumes a rebuilt smaller rank record with the same k and an explicitly identified complex-place set. Restricting b,e preserves the required odd t, the lower bound r′+5≤t, all retained parity conditions and all four centredness clauses. Interlacing retains b₀ because M′≥2; all other discarded conditions concern discarded array indices.

The finite-set proof is exact, including Boolean signs. At j≤M′ every block index i<j is retained, so Xpar is unchanged; Dpar only loses the tail singleton entries. The source's natural-number subtraction in its parity Boolean is unchanged on every retained i,j, and the final odd-j translation is the same. Possible coincidences between finite-set elements do not affect the inclusion. The cubic noncompact threshold decreases because r′+M′t≤r+Mt, preserving every strict gap.

The transport to **any** new ThetaX package is justified by its actual `etaT_pos` field. Both packages have etaT infinity type +1/2, so the old Hyp3 condition forces the retained parameter eta to be −1/2 in the new package too. The only retained numerical condition not automatic from truncation is precisely 1801≤r′+t. The sufficient old margin r+t≥1801+(M−M′) is correct. No equality of old and rebuilt endpoint spaces is inferred from equality of parameter sets.

## 2. The full nonzero-period induction: DP52(b)

I directly read all six exact AdmS statements and their quantifiers, plus the ThetaX additivity, cusp-stability, conjugation and odd-rank period fields.

The initial representation sequence and all finite upward decompositions come from the first input. Terminal nonvanishing comes from the second. At each step, first fix the position/Fourier–Jacobi witness if the period is below the terminal index; additivity in the conjugated vector then selects one nonzero summand. At the terminal index the same argument uses the top-period additivity. The selected source vector belongs to the required type because its representation is contained in that type.

The unfolding statement only promises a nonzero lower period conditional on the lower lift being cuspidal. The proof supplies this condition correctly. The subspace consisting of cusp vectors satisfying IsDv is a complex subspace despite the conjugate-linearity of conjAF: the inverse image of a complex subspace under a conjugate-linear map is again closed under complex scalar multiplication. The sixth input and the explicit cusp-stability fields make it stable under both action families. The second clause of the fifth input supplies every lower-tower vanishing required by the fourth, so the lower lift is cuspidal. Its finite-type datum then permits the first clause of the fifth input to give IsDv. The unfolding statement finally gives the nonzero period. There is no circular assumption of cuspidality.

The finite recursion constructs all constrained vectors and data; the unconstrained larger indices admit zero extensions. At j=0, M≥2 excludes the terminal alternative. The actual rank formulas give r−k=M−1, an odd nonnegative integer because M is even. Bper_odd therefore replaces the Fourier–Jacobi datum by zero exactly as PointsLemma requires. No additional minimum length appears in this proof.

The proposition named TowerRallisLemma is correctly distinguished from a theorem already executed by Lean. The separate source thetaG example uses the stated common auxiliary Hilbert space, identity actions and inner-product periods; the memo does not identify it with the intended geometric local kernels. Its illustrative source blocks were read for this classification, without extending the review to the source's RH argument.

## 3. Endpoint construction and the weaker actual-type theorem: DP52(c)

The exact `periodC` definition, the complete `periodC_eq_ipCl` proof and `recPer` definition were read. The ambient rank is a parameter, not a fixed numerical endpoint. The source's finite-class functional extension, inverse-stabilizer weights and conjugate-linear representing map yield the stated bilinear period and inner-product identity. The separately read `ptEv_gram_unit` has no X.Ok argument.

Replacing the sole use of hX in periodC by a directly supplied point-goodness certificate is therefore valid. The new proof also constructs both point and row certificates, rather than leaving them hypothetical. I read the entire source `formGSD_ok` proof and checked all its components:

- Finitely many decorated-lattice representatives remain sufficient for FormG because their representative moves are unitary isometries paired with the identity level element, already in FormG. This is the crucial subgroup step; the argument does not incorrectly infer finite smaller-group orbits from a larger-group statement.
- Stabilizers inject under FormG.incl into the finite decorated-lattice stabilizers.
- Finite level-character values are roots of unity. The scalar and its inverse are algebraic integers, so they preserve the coefficient lattices; this proves both lattice-equivariance fields.
- A conjugation-compatible complex embedding of K makes a root of unity c satisfy conjugate(c)c=1, which preserves the hermitian pairing under the scalar twist.

These are exactly the five fields of GSD.Ok. The only field-package inputs in that source proof are conjE and conjK. Direct reads of rowVal_eqv and ptOk show that their coefficient-equivariance proofs use only emb_star, in addition to the displayed lattice identities. No use of quad is hidden in this weakened proof.

For E=K=Q(ζ₇) and the actual three embeddings, canonical conjugation and the abelian Galois action give all three compatibilities. Thus the finite-class point and row goodness data, their endpoint period, and its inner-product identity are constructed for the stated rank, weight and level inputs. This is a positive construction at that layer, not an obstruction inferred from a failed wrapper and not an assumption that a false X.Ok certificate exists.

The source recPer remains attached to recChain hX; the memo explicitly does not infer a new entire chain from the weakened period definition. Also, the period map may have zero restriction to a particular iterated theta image. The theorem proves existence of the class-space map at the supplied inputs, without claiming the missing geometric identification or nonzero restriction.

## 4. The exact field/type calculation: DP52(d)

The common-subfield definition and both Ok.quad and Core.quad were directly read. For type {1,2,3}, equality of the selected embeddings includes z=σ₃(z). The listed powers of 3 modulo7 run through all six units, so σ₃ generates the Galois group and the common fixed field is Q. Coefficient-field enlargement, a common injective postcomposition, conjugation and simultaneous relabeling do not change this conclusion. The source's required quadratic degree therefore fails independently of the chain length.

The general Galois-CM characterization is correct: degree-two common field makes the selected embeddings all the extensions of one of its embeddings; that field must be imaginary, because otherwise the conjugate CM type would supply another g distinct extensions of the same embedding. Conversely an induced imaginary-quadratic type has precisely the indicated quadratic common field. The type {1,2,4} example is now explicit: ζ+ζ²+ζ⁴ has sum with its conjugate −1 and product2, hence polynomial T²+T+2 and field Q(√−7). It is not a relabeling of the actual Jacobian type.

This field mismatch is a literal obstruction to the unchanged source certificate. The new proof in §4 bypasses it for the endpoint period, so it is not an intrinsic obstruction to every mixed-type period construction.

## 5. Scope, source use and remaining gate

The complete memo closes three separate issues: exact smaller-parameter transport with its explicit residual numerical bound; the finite nonvanishing induction under all six stated theta identities; and an actual mixed-type row/point period construction using weaker conjugation hypotheses. It correctly keeps those results separate from construction of a geometric theta family satisfying all identities and selected local/global estimates at once.

The remaining gate is the identification with the intended iterated theta image, the rebuilt class kernels and the quantitative certificates for that same family. No upper bound on true selected gains, unchanged global cost theorem, or impossibility of a shorter chain follows from this memo. The initial ramified-lattice nontriviality theorem and the generic bilinear periodN wrapper are reported with their own limited scope.

During drafting I requested that the newly proved positive endpoint construction be reflected in the opening and concluding scope paragraphs; the reviewed version does so. I also suggested the explicit quadratic calculation for the contrasting type, now included. These were scope/explicitness refinements, not a discovered mathematical counterexample. No theorem from an earlier, narrower memo version is silently promoted to this final hash.
