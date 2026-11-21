# Independent exact-version review of P-18

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/isolation`; run CUE-GCT-20261121-I.

Result: **PASS** after a complete fresh reading of `work/purity/P18_ordered_cubic_gate.tex`, SHA256 `87282923d4e8b02925d01cd6ca00ac3ed2cb57d7fa97634d8055ac9031714147`. The three blocks explicitly partition all variables, and the polynomial has degree one in each entire block. I rechecked every step of the disjoint trilinear proof and minimal-cubic support reduction against the prior working-note review reproduced below. The numerical hitting-set count is exactly I40 at D=3: `(n+1)^2*binom(6,3)=20(n+1)^2`; the required field size is max(2n+1,4), so every selector avoids every node and the four amplitude values are distinct. The map uses neither the block partition nor the witnessing order. The separate prolongation converse remains an audit and is not silently used in this final proof.

No repair is requested. No unrestricted cubic theorem or boundary-coordinate specialization is inferred. No numerical execution is claimed.

## Detailed rederivations

# Independent review of the cubic ordered-support working gate

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/isolation`; run CUE-GCT-20261121-I.

Result: **PASS** after a complete reading and independent rederivation of `work/purity/cubic_ordered_gate.md`. This checks exactly the three stated deductions and leaves the shared-boundary cases unresolved. It does not certify a general cubic hitting theorem.

1. **All-characteristic prolongation converse.** I checked the decoder factor `(a_j-a_i)(a_k-a_i)` for a quadratic partial. Its two contraction equations give omega1=a_i*omega0 and omega2=a_i*omega1. Reversing the outer indices changes every omega by the same alternating sign, so also omega1=a_k*omega0, including characteristic two. Distinct nodes force all three contractions to vanish. The cited HMM characterization then gives the cubic ideal membership. No division by three or Euler identity is needed.

2. **A zero block separates the exterior kernel equations.** Each contraction lowers left degree by zero or one, so only adjacent blocks contribute to a fixed output degree. If C1=0, all contractions of the C0 component vanish separately; if C2=0, those of C3 vanish separately. A nonzero extreme component is an actual specialization by zeroing the opposite variables and has no larger cut ranks. Minimality in essential variables therefore rules it out. Combined with P17's three-block lemma, this leaves only two adjacent support degrees at each prefix.

3. **Ordered intervals with at most two shared endpoints.** If the largest first support position exceeded the smallest second one, the prefix ending at that latter position would have counts zero and at least two in two support monomials. The analogous comparison of second and third positions gives the other inequality. Essentiality removes any intervening gap. Thus the three ordered intervals are disjoint or meet in one coordinate at each interface, exactly as stated. This is a necessary support condition, not an unjustified independent-variable decomposition at shared coordinates.

4. **Disjoint trilinear case.** Translation invariance follows because all positive translation coefficients have ideal degree below three. Its three first-order block contributions have distinct multidegrees, so each block translation derivative vanishes separately; linearity within a block gives the corresponding full translation identity. At the cut just before the last essential U variable, the earlier B_i already span the entire rank-r space because their sum is minus the last one. The remaining row X_last*B_last is independent by its X_last degree. Hence r+1<=3. The reverse argument bounds the W-side rank by two. Rank one on either side would factor the cubic into degrees one and two, forbidden by the prime ideal's minimum degree three. The resulting exact two-by-two middle representation is justified by the two coefficient support spaces.

5. **Middle slices and the final rank-four cut.** Every nonzero middle slice is a quadratic in the one-pair ideal. A rank-one slice matrix would give a product of nonzero linear forms, impossible in that prime ideal; hence each essential slice matrix is invertible. Separate middle translation makes their sum zero, requiring at least two slices. At a cut between essential middle variables, one invertible prefix slice makes the left-degree-two block have rank two, and one invertible suffix slice makes the left-degree-one block have rank two. Their row and column degree indices are disjoint, so total rank is at least four. This is characteristic-free.

The final warning about specializing a shared boundary coordinate to zero is correct: it does not preserve the same balanced rational ideal. The proof therefore stops at the stated one- or two-shared-variable boundary gate. No numerical execution or new external-source proof audit is claimed in this review.
