# Separate post-CP36 arc lead at e=2p(p-1)

Status: exploratory, not a proved result, canonical input or current-gate update. A full universal coefficient proof and two independent audits are required.

For p>=5 put q=p^2, N=q-1, e=2p(p-1), d=eN, and b=(p-1)(p^2-2). In the same universal height-two formal group and exact homogeneous coordinate as B62, set u=X^b, Y0=X, Y1=[p]_u(X), Y2=[p]_u(Y1), and P(X)=Phi_u(Y2), where [p]_u(T)=T Phi_u(T).

The intended modulo-p leading degrees are

    v_X(Y0)=1,
    v_X(Y1)=q,
    v_X(Y2)=J=b+pq,
    v_X(P mod p)=b+(p-1)J=pb+pq(p-1)=eN=d.

The first step selects T^q because b+p>q; the second selects u T^p because b+pq<q^2. In the final division series the u T^(p-1) term should be uniquely first, because b<p(p-1)J. The proof must check all universal higher coefficients, not just these three displayed monomials. P(0)=p. If those statements hold in the exact coordinate, Weierstrass preparation gives an Eisenstein DVR of index d. Its actual valuations are 1,q,J, so its x has exact order p^3.

The tame degree-N action is x -> zeta x and the semilinear point map is aT with a=zeta^(-1). The identity b == -(p-1) modulo N holds. Hence u transforms by a^(p-1), the exact B62 homogeneity fixes P, and the marked point is fixed. Descent gives base index e. The already-audited finite-flat quotient, finite twist and compatible Kummer lifting should then construct an actual p^3 comparison with unequal finite characters {zeta,zeta^p} and {1,zeta^(p+1)} (up to the common inverse convention).

The proposed full upper bound at actual p^4 uses existing B64/B76: n4 detects dimension since v_p(e)=1; e< p^4 excludes mixed comparisons; at a=eN the actual-target recurrence has q1=2p-1,q2=2p^2-1,q3=2p^3-1>2pN=a/(p-1). If the lower arc is fully proved, the result would be nu_min(p,2p(p-1),2)=3 for every p>=5. At p5 this is e40.

## Broader one-high-step calculation, not claimed

For a general p-divisible e and a positive integer A, the same pattern Y0=X^A, Y1 leading qA, Y2 leading b+pqA requires

    b=eN/p-q(p-1)A,
    e/p^3 < A < e/p^2,
    b == -(p-1)A modulo N.

The first two inequalities are exactly the strict q-step then p-step conditions. For p>=5 and e>p^2 one can attempt the same integer-interval selection as in B63, avoiding N|A to keep unequal finite characters. This suggests sharpness of the B76 mixed threshold at valuation-one indices and actual level p^3, but it is not yet a theorem. Higher coefficients, actual valuations after the Eisenstein quotient, faithful/nonfaithful tame action, and the inherited extension-lifting proof all remain to be written and independently checked.

No numerical program has yet been executed for this outline; no theorem is inferred from the displayed integer choices alone.
