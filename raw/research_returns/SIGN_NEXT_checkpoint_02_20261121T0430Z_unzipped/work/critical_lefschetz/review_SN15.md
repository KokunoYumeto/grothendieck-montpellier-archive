# Independent review of SN-15: bounded all-rank exterior-order index formulas

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/critical_lefschetz.
Date: 2026-11-21 03:54:14 UTC.
Read complete proof: `work/root/exterior_index_formula.tex`.
Source SHA256: `2fe0ad46e1365f3cc67e1073bc21e70a914c4158e8d9940a6f3690c6234a3029`.

## Verdict

**Accepted.** I independently reconstructed every step of the complete proof: the signed exterior decomposition into Boolean blocks, integral bounded PBW spanning, both entry formulas, the compressed-row count, the integrality/saturation identification, the Smith-factor conclusion and prime support. There is no remaining proof gap. This proves a finite polynomial-size index algorithm for all ranks. It does not calculate a theta period or identify an arbitrary theta matrix with the Lefschetz order.

The all-rank proof uses the previously proved IF-02 saturation/rank statement, as declared. The independent computational check below verifies entries directly on the signed full exterior basis; it is not a formal proof kernel and does not replace the all-rank argument.

## Independent full-proof derivation

### Exterior signs and Boolean blocks

Use the ordered exterior basis e1,f1,e2,f2,... . Fix all singleton states. A pair in an empty or full state remains in those two states under L,D; a singleton pair contributes zero to both operations and remains fixed. Wedge multiplication by e_i wedge f_i crosses every earlier degree-one factor twice, hence has positive sign. The two interior products likewise give the same preceding-index sign twice. Thus on the remaining v pairs L adds one element and D removes one element with coefficient +1, exactly as stated. Every v from 0 to n occurs; copies differ only in fixed singleton choices and have identical matrices. Exterior degree is n-v+2l for a source subset of size l.

The commutator is H=DL-LD, with eigenvalue v-2l=n-degree. Direct calculation then gives [H,L]=-2L, [H,D]=2D and DL=LD+H. The sign convention in every subsequent formula is correct.

### Bounded integral PBW spanning

Order letters L,H,D. Swapping any adjacent inversion has coefficient 1 on the exchanged word and integer coefficients on strictly shorter commutator words. Induction first on word length and then inversion count therefore terminates over Z. Since H is itself in Z[L,D], the resulting monomials L^a H^b D^c span exactly O_n, not a larger auxiliary order.

The powers L^(n+1),D^(n+1) vanish on every Boolean block. The spectrum of H is contained in the integers -n through n, so its displayed monic annihilating polynomial reduces every exponent b to at most 2n with integer coefficients. This proves the finite rectangular column bound without an unbounded closure loop.

For projector words, pi_j L=L pi_(j-2) and pi_j D=D pi_(j+2), with absent degrees zero. Move all projectors right and use their orthogonality. On the image of D^c pi_j the H eigenvalue is n-j+2c, an integer. Hence L^a D^c pi_j with the same bounds span O_n^pi integrally. There is no missing denominator from weight interpolation in this spanning argument.

### Entry formulas

For source S, target T, put l=|S|, k=|T| and t=|S intersection T|. After c contractions the surviving subset U has size s=l-c. It must lie in S intersection T, and the final a additions require k=s+a. There are binomial(t,s) choices of U. Ordering the removed and added elements contributes c! and a!, respectively; the intermediate H eigenvalue is v-2s. This yields a! c! binomial(t,s) (v-2s)^b, including zero cases and the b=0 convention. Removal followed by re-addition of an element in S intersection T is included by this count and creates no extra factor.

For projector columns the projection is applied first, so it is the source degree n-v+2l that appears in the indicator. This confirms that the stated indicator uses l, not k or s. Ordinary D/L then give the same factorial-binomial coefficient.

### Compression, dimensions and saturation

Simultaneous permutations of the v active pairs act transitively on source-target pairs with the same k,l,t. They commute with L and D. All tuples in the stated range occur. Recording one entry for each tuple therefore determines every repeated-block full matrix and is injective on the rational image algebra. A recorded vector is integral if and only if its full matrix is integral.

For fixed v, the four nonnegative cardinalities |S intersection T|, |T minus S|, |S minus T| and the complement sum to v. This is a bijection with the allowed triples k,l,t, giving binomial(v+3,3) rows. Summing over v gives binomial(n+4,4). The column count is (n+1)^2(2n+1). The rank from IF-02 is the sum of (v+1)^2 for v=0 through n, equal to (n+1)(n+2)(2n+3)/6.

The rational column span of M is the entire image algebra because the bounded monomials span O_n. Its saturated integral column span is exactly the image of A_n, by the preceding matrix-integrality criterion. Degree projectors lie in the rational image algebra (also directly obtainable by rational interpolation in H), so the same argument applies to M^pi. Smith normal form identifies saturation modulo the column lattice with the finite cyclic factors from the nonzero Smith entries. Unit factors and zero rows are handled correctly. Thus the determinant-gcd and index formulas hold as stated.

### Prime support and edge cases

IF-02 identifies A_n with the order generated by divided powers. Once n! is inverted, each divided-power generator is in O_n; the three orders therefore coincide after that localization. Their finite quotients can have only prime factors at most n. The n=0 case has one row, one column, matrix (1), rank 1 and index 1. For n=1 the support statement forces both indices to be 1, in agreement with the existing tables.

## Independent arithmetic checks

`review_SN15_entries.py` was written independently from signed exterior wedge and interior-product operations, without importing the author's matrix construction or closure programs. It checks the H commutator on every full exterior basis vector, then both compressed entry formulas on every source-target pair within its preserved Boolean block for all bounded columns, for n=0,1,2,3,4. It also checks that no output leaves its block. The result is **634,970 exact integer entry equalities**, all passing; the per-rank row counts are 1,5,15,35,70. The JSON output is `review_SN15_entries.json`.

I also compared the saved nonzero Smith factors and indices from `finite_index_formula_results.json` with both earlier IF-03 word-closure result files for n=1,2,3,4. All eight order comparisons agree, including every nonunit invariant factor. This is a comparison of saved computational certificates, not a new independent Smith implementation.

The reported ordinary indices are 1, 2^7, 2^27*3^4, and 2^81*3^33. The corresponding degree-projector indices are 1, 2^2, 2^10*3^2, and 2^32*3^10. These values respect the all-rank prime-support theorem.

No shared root file was edited by this reviewer.

## Subsequent full check: integral row compression and shift blocks

Date: 2026-11-21 03:55:44 UTC. Updated complete source SHA256: `2fe0ad46e1365f3cc67e1073bc21e70a914c4158e8d9940a6f3690c6234a3029`.

The entire new paragraph following the main proof was read independently. **Accepted.** Let z=v-k-l+t be the complement size. If t,z are positive, both replacement rows are admissible: the first decreases t and z by one; for the second, v is at least 2, k and l lie between 1 and v-1, and replacing (v,k,l,t) by (v-2,k-1,l-1,t-1) again decreases t and z by one. Thus the recursive reductions terminate in rows with t=0 or z=0.

For a fixed column, the first replacement contributes binomial(t-1,s); the second has s'=s-1, preserves k'=s'+a, and contributes binomial(t-1,s-1). Their H eigenvalues coincide because v-2-2(s-1)=v-2s. The exterior source degree also coincides because n-(v-2)+2(l-1)=n-v+2l. Pascal's identity therefore proves the complete row identity for both matrices, including the zero cases with s outside the allowed range. No inversion of an integer is involved.

The deleted rows are consequently integer combinations of the retained rows. Subtraction produces zero rows by unimodular operations. The excluded four-tuples have intersection and complement at least one, giving binomial(v+1,3) tuples at fixed v. Summing the retained count gives binomial(n+4,4)-binomial(n+2,4)=(n+1)(n+2)(2n+3)/6. Their rank is the already proved rank of the full matrix, hence the retained matrix has full row rank and its saturated column lattice is the whole integer row lattice.

Finally every nonzero entry has k-l=a-c. Grouping rows and columns by this shift is an integral permutation into independent rectangular blocks, not a rational string decomposition. The cokernel is the direct sum of the block cokernels. Collecting each prime's elementary-divisor exponents and sorting them, with zero exponents padded to the total rank, recovers the invariant factors of that direct sum. Thus the block procedure preserves all nonzero Smith factors.

This additional proof check is independent of the reported n=5 computation; I do not claim to have run that computation.
