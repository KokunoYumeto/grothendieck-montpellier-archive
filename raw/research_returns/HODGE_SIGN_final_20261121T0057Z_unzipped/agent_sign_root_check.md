# Independent full check of root HS-01–HS-05 and strengthened HS-04B

2026-11-21. GPT-6 Astra Pro, effort not exposed, /root/sign_geometry.

I read every sentence of the proofs in root_sign_analysis.md and independently reconstructed the argument. HS-01–05 pass, subject to explicit minor conventions: B>0 and C finite in HS-01, q a prime power and d≥1 for geometric HS-03. HS-04 is correctly only a smoothness-only counterexample; its constant sheaf also fails base middle concentration. The proof below strengthens it, preserving that base condition.

## HS-04B (parent candidate, independently re-proved)

Let q be odd, r=q^n, and χ_n=χ_q∘Norm_{F_r/F_q} the compatible nontrivial quadratic character, extended by zero at zero. Put

    t_n(x)=χ_n(x²−1),   P(x,y)=xy−1,   ε=χ_q(−1).

Then |t_n(x)|≤1, P=0 is smooth, and

    M_n=−1,
    N_n=ε^n(r−3),
    R_n=(εq²)^n−3(εq)^n−1.

The base sheaf ℱ=j_!Lχ(x²−1) on A¹, with j:A¹\{±1}→A¹, has compactly supported cohomology concentrated in degree1, with H_c¹=Q_l and Frob eigenvalue1. The restriction of ℱ⊠ℱ to xy=1 does not have compactly supported cohomology concentrated in degree1: on G_m\{±1} it is geometrically constant up to the unramified character ε. In particular it has nonzero H_c². The desired parity e=(−1)^{2−1}=−1 does not make R effective: the coefficient of (εq²)^n in −R is −1.

**Proof.** The finite double cover p:G_m→A¹ is x=(u+u^{-1})/2, with deck involution u↦u^{-1}. Its coordinate ring is finite over F_q[x], since u²−2xu+1=0 and u^{-1}=2x−u. The cover is branched only over x=±1. Its invariant direct-image summand is Q_l and its anti-invariant summand is ℱ (zero stalk at each branch point). Thus p_*Q_l=Q_l⊕ℱ. Compact-support cohomology of G_m is Q_l in degree1 and Q_l(−1) in degree2; that of A¹ with constant coefficients is Q_l(−1) in degree2. Their direct-summand difference proves the asserted cohomology of ℱ and hence M_n=−1. Equivalently, elementary point counting on y²=x²−1 identifies (x−y)(x+y)=1 and gives the same sum.

On xy=1, for x≠0,±1,

    (x²−1)(x^{-2}−1)=−(x²−1)²/x²,

so t_n(x)t_n(x^{-1})=χ_n(−1)=ε^n. The other possible x=±1 give zero, and x=0 is not on the hyperbola. There are r−3 allowed x, proving N_n and then R_n=rN_n−M_n². Since q>1, the three possible nonzero roots εq², εq, 1 are distinct except that εq never equals1 in either case, and the coefficient −1 at εq² in −R cannot be represented by an effective Frobenius module. Uniqueness of the finite power-sum expansion follows, for example, from the distinct simple poles of Σ_n R_n T^n. ∎

**Scope.** This special restriction passes through coinciding ramification loci; geometric ramification cancels on the curve. It disproves the claim that smoothness of the hypersurface, even together with base middle concentration and pointwise weight zero, is enough. It does not disprove a carefully stated generic non-characteristic restriction theorem with boundary control. It is therefore an exact demonstration of why the missing boundary/transversality hypothesis matters.

No Lean formal certificate or exhaustive search was performed. All check events are in agent_sign_events.tsv.
