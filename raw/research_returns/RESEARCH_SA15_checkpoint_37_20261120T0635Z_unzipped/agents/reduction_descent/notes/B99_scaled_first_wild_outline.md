# Separate post-B98 outline: valuation-one absolute ramification

Status: exploratory, not a promoted theorem or checkpoint gate change.

Let p>=5, e=t*p*(p-1), with p not dividing t. For an actual p^3 comparison of whole potentially supersingular height-two groups with irreducible residual inertia and unequal special characters, all B97 first/second/third point valuations appear to scale by t. The denominators forcing degrees p and p^3 remain unchanged. The degree-p second-point alternative still has primitive valuation t(p-1), prime to p, so the full translation-plane contradiction still applies. Every second point should therefore have degree q=p^2 and every third point relative degree q.

If the first layer has dimension two, its actual primitive point stabilizer remains central, making its degree-p^4 point field Galois. The two-level coordinate values become A=t*p*(p-1), D1=q*A, D2=q^2*A. The critical break is a0=t*(q-1)*(p-1), and j0=D1-a0 is congruent to -t modulo p, nonzero. All strict coefficient comparisons in the B97 proof are multiplied by t; the zero/nonzero coefficient boundary must nevertheless be written explicitly before claiming a theorem.

The exact point conductors would be c1=t*(q-1)*(p-1) and c2=t*(q^2-1)*(p-1). The actual two-column proof of the full terminal-character bound p^(r1-2)*c2 uses only these conductors and the unchanged degrees, not t=1.

For a traceless first layer, mu_(p^2) is in K and the Cohen-field degree gives K/K0(mu_(p^2)) tame of degree t. The actual last cyclotomic field has break t*(q-1)^2 after the degree-(q-1) good extension. Thus the prior traceless contradiction scales by t.

For a traceful first layer, mu_(p^2) is absent. Put K1=K0(mu_p), C0=K0(mu_(p^3)), C=KC0. Then [K:K1]=tp, [C:K]=p^2 and [C:C0]=tp. The intersection is K1 because p^2 does not divide [K:K1] and the only possible nontrivial p-subextension would contain mu_(p^2). For a degree-tp Eisenstein polynomial of a uniformizer of K, each derivative term has residue i-1 modulo tp: v_K(a_i) and v_K(i) are divisible by tp. The leading valuation is tp^2-1 and cannot cancel. Consequently d(K/K1)<=tp^2-1. Every derivative term for C/C0 has valuation at least tp-1.

Transitivity would give

    d(C/K) >= tp-1 + tp*2p^2(p-1) - p^2*(tp^2-1).

Dividing the cyclic-p^2 different formula by p-1 gives the exact scaled inequality

    delta1 + p*delta2 >= t*p*(p^2-p-1).

The actual first cyclotomic quotient forces delta1<=t(p-1), hence delta2>=t*(p^2-p-2+1/p). The terminal contradiction is then the B98 strict difference multiplied by t. No new source or numerical program has been invoked for this outline. A full typed proof, supplement and both independent audits are still required.

## Next concrete cases, distinguished by scope

* First-wild family: (p,e,h)=(7,42,2) remains bounded2..3 by B77, with its irreducible residual branch already excluded by B98; its reducible residual branches remain.
* p-prime p5 family: B75 explicitly leaves (5,752,2) bounded3..4. This is not the next unrestricted p5 ramification index.
* p5 wild multiples of four after e20: e40 remains an open full case. The already proved B63 lower example gives index>=2. The B64 actual-target recurrence at a=e*(25-1)=960 gives q1=9,q2=49,q3=249>=240=a/4; with the B76 dimension and mixed reductions at n4 this gives index<=3. This numerical consequence is separately derived from existing proofs, not a new sharpness assertion.

No claim that any one of these is globally the smallest unresolved B.4 instance is made; the small-prime and higher-height families are separate.
