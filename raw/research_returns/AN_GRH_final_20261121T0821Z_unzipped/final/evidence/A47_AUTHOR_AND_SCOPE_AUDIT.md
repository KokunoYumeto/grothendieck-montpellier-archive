# A47 author whole-proof and scope audit

Date: 2026-11-21. Author/reader: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

Current source: `work/row_audit/A47_BOUNDED_PRIMITIVE_EXPONENT.tex`, SHA256 `6fe00a4573c5df1288d66c1809116db4f97ffe96e1ba876c2b8df9df525b7aba`.

## Reading record

I read the complete first finished source at SHA256 `6f2193b82983e02c77e5baa9315369d7eb5e7c056f15beb02ed618ec326df395`, including the theorem, all five proof steps, the elliptic-compatibility paragraph and exact gate comparison. The whole proof passes. The subsequent narrow changes restored three omitted TeX spacing-command backslashes and explicitly named the geometrically pro-prime-to-p arithmetic fundamental group. These are also checked. No mathematical assertion changed. This is an author targeted proof check, not a formal verification or an independent re-proof.

The primary Stacks Lemma 53.12.4, Tag 0C1F, was reopened and its complete displayed statement and proof read at `https://stacks.math.columbia.edu/tag/0C1F`. It directly gives different exponent at least e-1 with equality exactly in the tame case, hence at least e in our wild case. Its referenced earlier lemmas were not all reread. Poonen's exact controlled-field source was already read in this run; the present manuscript cites Corollary 2.3 with its precise hypotheses instead of reproducing that known induction.

## Mathematical checks

The rational bound is on the actual primitive image of the Galois-invariant integral projector. The identity A p_n = n A gives M_n A delta = 0 before any constant extension. Exact order m divides M_n. The principal divisor has coefficients plus or minus m and degree 2^omega(n)m; exact order proves separability, including when m=1.

The controlled-field index divides 2^omega(n) times a power of p, hence is prime to the odd cyclic degree n. The cyclic action on the auxiliary curve is faithful and free, and the numerical inequality forces its genus and the quotient genus to be one.

The new step is the weighted integral orbit relation. If the two image orbits coincide, local pullback multiplicities give r_Q A = -r_P A sigma^(-j). Raising through the odd order t of the shift yields (r_Q^t+r_P^t)A=0 in the torsion-free integral group ring. This is impossible and requires neither degree two nor equal local indices.

Disjoint image orbits force every supported fibre to be a singleton. Hence the field index e divides m, is a nontrivial p-power, and is the total ramification index on both full n-point orbits. Their different contribution gives e<=g-1. The Galois compositum argument identifies the actual cover with the elliptic pullback and carries total ramification down to the prescribed base points. Thus the obstruction is exactly e=p^a dividing M_n, with e<=g-1; the range 2<=g<=p excludes it. When M_n=1 it is impossible in every genus and the numerical inequality is automatic, recovering A46.

The elliptic paragraph proves compatibility, not existence of collisions: free elliptic deck actions are translations, so A annihilates Pic^0 on the target and pulling back gives the positive-power principal divisor. This is why the sign argument alone does not remove the residual wild elliptic configuration for M_n>1.

## Exact old gate and what has not moved

The currently retained `final/proof_sources/open_section.tex` U01 and question IDs `Q-HOOLEY` and `Q-COMPOSITE-PRIMITIVE-BRIDGE` asked for a pointed cover with actual primitive rational p-primary torsion zero. For characteristic-two genus-two curves, including A33's ordinary O5 target, A47 allows the weaker input M_n < (sqrt(n)+1)/2^omega(n). It imposes no primitive-root or theta-incidence condition when this actual rational exponent can be established.

Compared with the already proved whole-Prym criterion A45, this is a smaller numerical threshold when M_whole > 2^(omega(n)-1) M_primitive. The two tests need not imply one another for composite n. For a prime power, the coefficient remains two and only the highest conductor is measured.

No universal construction supplying the new inequality is proved. In particular, this source does not establish a new actual composite positive-exponent witness beyond the union of existing examples, and does not use that absence as a reason to weaken its theorem. It establishes a new sufficient primitive-factor criterion; any review-level claim of progress on universal supply requires a separate argument. The existing actual degree39 example has primitive exponent2 and n39, so it fails this new threshold49 while passing A45's whole-field threshold9; it is not evidence of strictness of A47 over A45. The degree15 primitive-zero example already belongs to A46 and is not counted as new movement.

The literal source questions A1 B.24 (primitive-rank-zero existence) and B.5/B.32 (specified rational-unit witnesses) remain unchanged: positive exponent does not satisfy their literal vanishing requirements. Hooley supplies candidate arithmetic orders, not a bound for these actual finite-field primitive exponents or a prescribed-point cover. Passing to further constants cannot decrease the rational torsion exponent of an already defined factor.
