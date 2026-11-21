### C11 refinement: an integral trace-zero operator gives the optimal uniform error one

Work in Katz's exact model G_alpha over the ring R of integers of a finite extension of Q_p, with [p](T)=pT+alpha T^Q, Q=p² and alpha a unit. The normalized invariant derivation D preserves R[[T]]. This includes the CM elliptic formal groups in Katz §IV; the following refinement is not asserted for an arbitrary formal logarithm with arbitrary pi in C_p solely from Katz's theorem.

**Statement.** For every integral f and a>=1,

    v_p(D^a f(0)) >= floor(ap/(p²−1))−1.

The constant1 is optimal uniformly in f and a.

**Proof.** Write A=R[[S]], B=R[[T]], with S=[p](T). Weierstrass division for the monic relation

    T^Q+(p/alpha)T−S/alpha=0

makes B free of rankQ over A, with basis1,T,...,T^{Q−1}. Newton identities for this polynomial give

    Tr(1)=Q,
    Tr(T^j)=0 for1<=j<Q−1,
    Tr(T^{Q−1})=−(Q−1)p/alpha.

It follows that Tr_{B/A}(B)=pA. For f inB put h=Tr(f)/p inA, regard h as a function in the target formal-group coordinate S, and put

    g=p f−[p]^*h.

Then Tr(g)=p Tr(f)−Qh=0. After splitting the generic p-torsion kernel, the trace is the sum over translations by G[p], so g satisfies Katz's precise torsion-trace equation. This equality also holds integrally, because the formal rings are p-torsion free. Katz Main Theorem3.11 therefore gives v_p(D^a g(0))>=floor(ap/(p²−1)). Invariance of D and [p]^*omega=p omega give

    D^a([p]^*h)(0)=p^a D^a h(0).

The last derivative is integral. Consequently

    p D^a f(0)=D^a g(0)+p^aD^a h(0)

has valuation at least floor(ap/(p²−1)), since that integer is at most a. Divide by p to prove the bound.

For sharpness take a=Q−1 and f(T)=T^{Q−1}. Normalization D(T)(0)=1 gives D^a f(0)=a!, whose valuation is p−1, whereas floor(ap/(p²−1))=p. Thus a uniform loss smaller than1 is impossible. ∎

For a formal group obtained from this model by integral base change to O_Cp, the bound extends to all O_Cp[[T]] functions. For fixed a, the derivative at0 depends continuously on only the first a coefficients. Approximate those finitely many integral coefficients by algebraic integral elements lying together in a finite extension of Q_p. Apply the DVR result there and pass to the closed valuation ball. Integral formal coordinate changes with unit linear coefficient preserve the normalized invariant-derivative valuation.

This is a constructive reduction to the known Katz theorem, not a re-proof of that theorem or an assertion of research priority. It improves the logarithmic error to the optimal uniform constant in the stated CM local model. It still requires an integral coefficient function; the raw theta-frame counterexample below shows why that hypothesis cannot be dropped.
