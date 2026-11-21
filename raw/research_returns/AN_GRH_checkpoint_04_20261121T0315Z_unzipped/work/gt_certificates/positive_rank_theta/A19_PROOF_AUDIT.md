# Whole-proof audit of A19

**Result: PASS.** The complete statement and proof in `A19_FINITE_SUPPORT_THETA.tex` were checked by the author and independently whole-read by root and effective_galois. Both independent reviewers reported PASS. The proof does not use the unavailable original Boxall chapter as a premise.

## Exact geometric bound

The Raynaud theta support is the translate i_B(X) of the genus-two Abel curve, defined over the finite field by the line bundle B itself. A rational base point or effective rational divisor for B is unnecessary. Three pairs R_i−S_i representing the same nonzero Jacobian point would yield two distinct moving degree-two systems. Genus-two Riemann–Roch makes each canonical, forcing S_2=S_3. Thus a nonzero translate intersects theta in at most two geometric points. This argument also excludes a nontrivial translation stabilizer and avoids assuming transversality of the intersection.

## Exact powering lemma

For U=I+M with M divisible by an odd prime ell, let w=Mv have exact order ell^s. Taking N=ell^(s−1), the binomial expansion gives (U^N−I)v=Nw plus higher terms. The j-th higher term has valuation at least s−1−v_ell(j)+(j−1), which is at least s for every j>=2. The borderline ell=3,j=3 has equality and still vanishes. Therefore the equality (U^N−I)v=ell^(s−1)w is exact, not merely an equality up to an invertible operator. The resulting point T has exact order ell, and U, hence U^N, fixes T.

## Isolation of one primary component

For A=Frobenius^d congruent to I on J[ell], its action on a finite ell-primary module belongs to a finite ell-group. Each primary component consequently has orbit length a power of that same prime. If A moves a torsion point supported on S, choose one moved ell-component and raise A to the product of the other component orbit lengths. This exponent is prime to ell, so it fixes the other components without fixing the chosen one. Applying the powering lemma then gives sigma(z)=z+T, with T nonzero ell-torsion and sigma(T)=T. Since sigma is a positive integral power of Frobenius, its full ell-point translation orbit lies on theta. All ell points lie in theta intersect (theta+T), contradicting the bound two. Thus z is rational over the stated finite extension.

## Finite bound and algorithm

The degree d may be taken as the lcm of the exact orders of Frobenius on J[ell], or as the lcm of the displayed GL4(Fell) group orders. All ell are odd, so these are etale rank-four torsion representations and Frobenius is invertible. The finite group J(F_(Q^d)) has order h_d=Res(P_J(T),T^d−1); the sign is positive because P_J has degree four. Its S-primary part is killed by N_S=product ell^(v_ell(h_d)). Enumerating X(F_(Q^d)) and retaining i_B(R) killed by N_S is therefore an exact terminating search over all geometric S-primary theta points. It is not claimed to be efficient. If S is empty, the statement reduces correctly to testing the origin.

## Scope of the conclusion

For a fixed candidate q, S={3,q} handles every pair of exponents, not only the squarefree order3q. It gives no uniform bound on the candidate q, so it does not prove universal incidence. The reformulation using [3](theta) is exact: a nonzero q-torsion point on that image lifts to a theta point of order q or3q. Poonen's variable-multiple theorem does not set the additional multiplier to one, so no existence assertion is extracted from it.

The primary Scanlon–Voloch paper was inspected for literature context and the Boxall bibliography. The publisher's Boxall chapter record confirms the title, volume215, year1995 and pages69–80, but its theorem text was inaccessible. A19 makes no claim to have read that original theorem or to improve its optimal bound.

Independent reviews: root reported a complete PASS; effective_galois separately reported a complete PASS and specifically checked the tight binomial case, primary isolation, exact finite field, resultant formula and [3](theta) reformulation. These are mathematical reviews, not formal proof-assistant verification.
