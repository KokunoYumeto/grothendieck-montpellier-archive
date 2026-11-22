# Part A proof development

20 November 2026, 01:18 CET. These are working proof notes, not a certification before the proofs are written and checked.

## A.1: negative in characteristic zero, without any finiteness hypothesis

Let A=K[[t_1,...,t_n]], k⊂K characteristic zero, n>0. Put f=exp(t_1). The ordinary differential eta=df−f dt_1 lies in every t_1^N Ω(A/k): write f=P_N+t_1^N g_N and use the formal identity f'=f to obtain eta=t_1^N(dg_N−g_N' dt_1). It is nonzero: f is transcendental over K(t_1,...,t_n), proved by differentiating the minimal polynomial or by the norm/log-derivative argument. A derivation of Frac(A) killing K and the t_i and sending f to1 detects eta. A projective module embeds split into a direct sum of copies of A; that direct sum is t_1-adically separated. Therefore Ω(A/k) is not projective and A/k is not formally smooth. We must explicitly prove the finite polynomial/norm argument and the derivation extension.

The familiar same-field statement is cited in Matsumura, Commutative Ring Theory (1989), p.215, according to a secondary locator found during searching; the book page has not yet been opened. No claim of novelty.

## A.2: candidate full criterion

For characteristic p and n>0, candidate: A/k formally smooth in the discrete topology iff K/k is separable and [K:K^p] is finite (absolute p-rank, not merely finite relative p-rank).

Negative case 1: dim Ω(K/k)=infinity. If Ω(A/k) were projective, embed it split into free M=⊕_J A. The images of da for a∈K span an infinite-dimensional subspace modulo m. Pick a_i and fresh coordinates j_i outside supports of dt and all previous da_l, with the j_i-coordinate of da_i a unit. For f=Σ a_i t^i, coordinate derivations with D_j(t)=0 are t-adically continuous. Thus the j_i-coordinate of df is nonzero, contradiction to finite support. This avoids any unproved assertion that the coefficient-differential inclusion splits.

Negative case 2: dim Ω(K/k)<infinity but [K:K^p]=infinity. Then [kK^p:K^p]=infinity, so choose a_i∈k linearly independent over K^p. For one variable f=Σ a_i t^(pi) has df in every t^NΩ(A/k). It is nonzero because for F=K((t)), ker(d:F→Ω(F/k))=kF^p, and KF^p is the union of E((t^p)) for finite intermediate E/K^p in K. Such f has coefficients spanning an infinite-dimensional K^p-space. Use retraction A→K[[t_1]] to transfer the negative formal-smoothness assertion to all n. Prove p-basis/kernel facts, do not assume continuity of derivations into arbitrary modules.

Positive case: separability allows finite p-basis of k to extend to a finite p-basis of K. Add t_i for an absolute p-basis of A. Given square-zero C→C/J in char p, define A^p→C canonically by pth powers of arbitrary lifts, extend over k using k⊗_{k^p}A^p≅kA^p, then lift the finite relative p-basis arbitrarily. Their pth-power relations hold automatically. This gives the required lift. Ω(A/k) is the free module on that relative p-basis.

Source correction: K22-02_transcription.tex lines 91–99 states finite p-basis of K/k even while allowing nonperfect k. Taking k=K=F_p(s_1,s_2,...) refutes that general wording (empty relative p-basis). Under the earlier perfect-base branch it is correct. Both readings will be treated.

## Other source issues

A.3 definition 4.7 is for noetherian preadic rings, although preceding Theorem4.6 is more general. The supplied extract does not define condition P (it belongs to missing section3). For discrete base and noetherian complete target, 4.8 identifies P with flatness once the reduction is formally smooth. Need a proof of the full flat formally smooth adic lifting result, not only the local separable-residue case.
