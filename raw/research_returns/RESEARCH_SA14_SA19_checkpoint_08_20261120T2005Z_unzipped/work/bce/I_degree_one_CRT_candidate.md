# Degree-one continuity candidate for Part I

GPT-6 Astra (OpenAI), 20 November 2026. Full argument: `I_degree_one_CRT_candidate.tex`. Status: **candidate awaiting separate audit**. The broad full presentation remains Undecided.

The argument has two parts, both uniform in the number of nonzero finite matrix entries.

1. **Source tails.** Given degree-zero neighborhoods V_L,V_R with V_L T V_R inside a closed small neighborhood, let P_0 be the finite source set constrained by V_R. For a finite matrix with sources outside P_0, localize A away from the union of those finitely many incomparable primes. Chinese remainder interpolation approximates each target row at all its source primes by one element of this semilocal ring. Clear all denominators by u outside every source prime. Multiply u by v outside those sources but in the required powers of the finitely many constrained target primes. The matrix is approximated by a single b theta c, with b in V_L and c in V_R. Individual I4 continuity passes the uniform bound to the finite matrix.

2. **A fixed source column.** Choose a parameter-power cyclic input N=Ae⊂E_p with I=Ann(e) small at p. The finite module M=Ext_A^h(A/I,A) embeds in E_p[I]. At every adjacent q, its localization is exactly the kernel of the adjacent differential on E_p[I]. Finitely many global generators m_i=c_i e therefore show that a finite column vanishing on e has coefficient decomposition c_q=sum b_qi c_i+r_q, with b_qi in A_q and r_q in I Â_p. The first terms have uniformly small image outside a finite target set, by product-diagonal continuity and the fixed c_i. The remainders use h parameter-power generators. Approximate their coefficients p-adically and clear finitely many denominators; this yields at most h words b theta c with both coefficients in the prescribed neighborhoods. Finitely many exceptional targets use I4. Thus each fixed source column is continuous.

Combining the uniform source-tail bound with the finitely many exceptional columns gives continuity on the dense subgroup of finite adjacent-arrow matrices. Completeness gives a unique additive degree-one map, compatible with B on both sides and carrying b theta c to b T c. The proof does not use T²=0; that relation becomes essential for higher degrees.

The main audit points are the semilocal interpolation (sources have the same height and are incomparable), the exact kernel identity for localized Ext^h, and the bounded h-word decomposition of the remainder. None of these is replaced by a claim that infinite sums are automatically convergent in the target.
