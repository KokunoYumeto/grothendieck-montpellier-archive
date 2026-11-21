# Independent complete proof review: G-27

Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Actual review completed: 2026-11-21 06:26:38 UTC.

The whole proof was read at SHA256 `1c3a8c771b4eeb7355958a21364cf42526cfcfceb4e1f36f48c194228db3ff08` in `work/root/g27_fragment.tex`. The added introductory sentence after the proof environment was then inspected; final SHA256 `d627bfa4381ed5e8eb3bf15a2bb4fefdb1697b74899a55a44f28ffbb6130bda4` has no mathematical change.

**Outcome: PASS, complete written proof read and its estimates and semigroup argument independently rederived.**

## Checks

The two R32 applications satisfy their exact row ranges: the upper degree-n cone uses a nonrectangular label in fewer than 2n-2 rows, while the lower degree-m cone has q=r-1 between m and 2m-2. The latter tail may be rectangular; stability and the exact quotient dimension remain available without a period-one assertion. I treated the previously checked all-degree Pieri bound and exact image dimensions as stated inputs.

The displayed dimensions follow by subtracting the respective SL group dimensions from the enhanced dimensions. I recomputed their difference at n=m+1 and r=m+1: the given lower bound is m squared minus m minus two, which is positive. The lower dimension bound follows from q at least m and m squared minus q at least m squared minus 2m plus two. Both rings consequently have the positive dimensions required by the Hilbert estimates.

The common ambient bound dominates the lower one because q<r, b_B is at most b, and ms+(q-1)e' is at most ns+(r-1)e. The analogous parameter degree inequality ms+e' at most p also holds. The cited common weighted-generator Veronese construction does not require period one. Its E is divisible by beta factorial and is at least beta squared.

The new semigroup step is sound. If g is the gcd of the nonzero homogeneous generator degrees of B, then g is at most beta. Dividing those degrees by g gives a gcd-one set whose maximum is at most beta/g. The established residue bound therefore implies, in particular, occurrence of every multiple of g at least beta squared in the original grading. Since B is a domain, products of nonzero homogeneous generators cannot vanish. Conversely every occurring homogeneous degree is divisible by g. Because g divides beta factorial, it divides E.

For j=Ek+t, if B_j is nonzero then g divides t. The degree 2E-t is divisible by g and at least E, hence at least beta squared, so a nonzero multiplier exists and embeds B_j into B_{E(k+2)}. If B_j is zero the upper inequality is immediate. No nonexistent multiplier in a forbidden residue is used. For A the period-one point gives a nonzero element in degree E+t, embedding A_{E(k-1)} into A_j. Thus the two inequalities require period one only on the lower-bound side.

The degree estimate for the standard lower Veronese gives at most (pE) raised to v-1. Chardin's bound and linear Noether normalization give exactly the displayed binomial estimates. Their exact ratio is

    k(k+1)(k+2) / [v(k+v)(k+v+1)],

which is at least k/(4v) for k at least v+1. The stated integer threshold makes floor(j/E) strictly greater than 4v(pE) raised to v-1 and automatically satisfies that range. Strict comparison therefore holds in every residue, including lower-ring nonoccurrence residues.

Finally, the below-face occurrence uses only the determinant's nonrectangular R32 point, and the strict half-space uses the previously proved nonzero-exponent phase. The theorem makes the correct fixed-direction eventual assertion; it does not control all earlier degrees or remove the unresolved rectangular/next-row conditions.

No new primary source was opened for this review, and no numerical computation was used. R32 was independently completely reviewed immediately beforehand; earlier source and dimension inputs retain their existing scopes.
