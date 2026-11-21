# Separate next construction, not accepted or integrated

Created before CP08 all-file freeze. I45 remains immutable. These deductions need a complete standalone proof and independent review.

## Stronger Hessian count

Use I45 notation: first nonzero row i, first nonzero b at k, J nonzero a positions before k, total b moments zero, A_pre=a_k v_k. Let k=k1<k2<k3 be the first three nonzero b positions. For every intermediate zero-b position j before k3, its row is a_j times minus the partial b moment; that partial moment has at most three nonzero terms and is nonzero by Vandermonde independence. Thus a_j=0. The row k2 gives a_k2=0 and 2a_k=0. The row k3 then has zero previous a moment and a nonzero three-column b prefix, so a_k3=0.

Let R_A(T)=sum_{j in J}a_j/(T-h_j)+a_k/(T-h_k), omitting a_k if zero. Its first three moments vanish: their vector is 2a_k v_k, which is zero either in characteristic2 or because the k2 row killed a_k. Its numerator degree is therefore at most |supp A|-4.

If a_k=0, the residue rows at k1,k2,k3 give three distinct roots of R_A, hence |J|>=7. If a_k!=0 (possible only char2), residue rows k2,k3 give two roots, hence |J|+1>=6, or |J|>=5. I45's other rational function S still has |J| roots and needs B>=|J|+4. Thus distance t-i>=2|J|+3 is at least13 in every characteristic and17 outsidechar2. This would give actual reset-Hessian vanishing for runs<=11/allchar and<=15/nonchar2. No sharpness claim.

## Connector count through nine

For the I44/I45 two-bad quadratic F, square poles make P,Q disjoint. Under a hypothetical one-pole identity, the type order starts with Q and ends with P; otherwise an endpoint internal row has just one neighbor. Write maximal type blocks Q1,P1,...,Qk,Pk. If k=1 then B0=0 and F factors, impossible. If k>=2, I45 endpoint row sums force every P block except the last to have coefficient sum0, and every Q block except the first to have sum0. Hence |P1|>=2 and |Qk|>=2.

For each p in P1, the simple-pole row equation makes T(T)=e/(a_u-T)+d*sum_{q in Q1}q/(a_q-T) vanish at its node. Its total residue is0 by the row-sum equation, so its nonzero numerator has degree at most |Q1|-1. The at least2 roots from P1 force |Q1|>=3. Symmetrically the last Q block supplies at least2 roots of alpha/(a_v-T)+beta*sum_{p in Pk}p/(a_p-T), so |Pk|>=3. The four distinct blocks require at least3+2+2+3=10 internal coordinates. Therefore every constrained connector of length<=9 would survive.

## Expected combination, not yet claimed

All minimal runs<=9 retain ranks. At weights10/11, longer runs are saturated or have only a remainder3 determinant budget; I45's invariant-anchor/nonchain cases handle them. The stronger all-characteristic Hessian bound11 would then give weights<=11 and full multilinear n<=19 in every characteristic. Outsidechar2 the scalar threshold15 exceeds the currently preserved weight range; no extra weight claim follows yet.

## Possible sharp rank-test obstruction to pursue later

P16 with d2 gives four disjoint rational pole groups of sizes4,2,2,4 and identity R1R2+R1R4+R3R4=0. Pick u from R1 and v from R4 as the two single anchors; the remaining internal types have block sizes Q1=3,P1=2,Q2=2,P2=3, total10. This matches the lower bound. Full upper-unipotent covariance for a chain G(s)=I+a sE12+b sE23+c s^2E13 gives updates a+=p,b+=q,c+=a*q and constraint p*(b+q)=a*q. For pure p/q steps, a Q block starts at a=0 and a P block at b=0; the P16 zero-residue block sums appear consistent. This suggests an actual homogeneous translation-invariant width3 rank-preservation obstruction at weight12, but no construction or irreducibility theorem has been completed. It is not a two-pole scalar counterexample.
