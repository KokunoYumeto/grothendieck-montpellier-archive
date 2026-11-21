# DP53: independent complete residue-spectrum and prime-budget review

**PASS.** The complete memo §§1–7 and complete integrated theorem, proof and scope were independently read and challenged during observed 2026-11-21 03:24:58–03:28:12 UTC. The sole final wording change was read and verified at 03:29:26 UTC. Checker `/root/archive_binomial`, GPT-6 Astra Pro; runtime reasoning effort not exposed.

Whole memo SHA256: `d092d9c51eca2eae8624b85f9307e5f92b018d22ed1e66230c01a7c3631d2f74`.

Original whole-read fragment SHA256: `6257e5de6fce6c571a65aff961882fbf7c5d2f7b472edea3a0fa2d308ac3a946`.

Final integrated fragment SHA256: `c29611d491a93f28356000c1e2afc1f9bc22b70ef0e83df280fadb14757ee353`. Its only change explicitly calls the floor result the “same O(N) difference bound”. This is a clarification of the already proved result, not a mathematical correction. The final fragment occurs exactly once in main. Frozen texts, complete proof hash and exact delta are in `late_proof_snapshots/DP52_DP53_integrated_archive_metadata.json`.

## Integral directions and the full local spectrum

The global relative differential basis on the checked model away from 2 and7 gives fixed primitive integral Lie directions. After the unramified extension, distinct seventh-root character summands are integral direct summands, so the local normalized generator differs by a unit. This justifies the fixed global labels; no prime-dependent choice is hidden.

The CM height/type theorem is cited known background. Connectedness of each positive-dimensional orbit follows because a nonzero étale quotient carries a unital degree-f field action, forcing height at least f and therefore full height, incompatible with positive dimension. The same reasoning applies to the dual of a partial orbit. The already checked integral rank-cycle/Hodge arguments of DP45 and DP49 give the actual unit-arrow display, not only its isogeny class.

For the ordinary actual orbit, f=1. Killing lower logarithm terms is integral; height one makes p b_p a unit. The integral operator D^p/p!+b_pD gives D^p modulo p a nonzero base scalar times D. Iteration therefore takes unit values on a normalized coordinate at orders p^r, proving sharp slope zero. The induced ordinary factors become multiplicative over the strictly Henselian unramified base and give the corresponding zero sharp slope; alternating factors use the checked cyclic theorem.

I recomputed every table entry from the forward Frobenius action. For residue2, the cycles (1,2,4) and (3,6,5) give p/(p³−1), p²/(p³−1), and (p²+p)/(p³−1)=c₃. Residue4 reverses the first two entries. For residue3, the selected positions in (1,3,2,6,4,5) yield p/D, p²/D, p³/D in that cyclic order, hence (p,p³,p²)/D in global order. Residue5 uses (2,3,1,5,4,6) and gives (p³,p,p²)/D. Residue6 has one selected point in each two-cycle, giving c₂ three times; residue1 is ordinary. Every displayed total follows.

The comparison type is a subgroup of the six residues. Its orbits are selected constants for residues1,2,4 and alternate between selected and complementary cosets for3,5,6, giving zero or Σ_(r odd)p^(−r)=c₂. The exact common-variable identity checks independently: the numerator of 4c₃+2T−6c₂ over p⁶−1 is 8p²(p²+1), and division by six gives the displayed expression. The proof correctly does not infer the sign of the actual prime-sum constant from this formal identity.

## Prime sums with arbitrary fixed orders

For each fixed label i, multiplication by i permutes all six residues, exactly three of which send it outside Φ. Thus its leading 1/p coefficient has the same residue average as the comparison type. The entire periodic tail is bounded by 1/[p(p−1)], whose logarithm-weighted prime sum converges absolutely.

The exact unconditional analytic input is Rudnick §2 p.2 equation(1), directly read in source text and original pixels in ABA-CE61. It gives a bounded residue-class error, sufficient for the claimed uniform O(N), rather than merely an o(log X) conclusion. There are only three labels, so each bounded error may be chosen uniformly for X≥2; multiplication by arbitrary fixed nonnegative n_i gives an error bounded by a fixed constant times N. These orders may depend on an outer parameter but must be fixed while the prime varies. Excluding2 and7 changes only constants. Equal orders are not assumed.

## Integer floors and exact scope

The floor theorem compares the **difference** of the two lower certificates. Separate N log X expansions for fixed-n floor sums would be false after X exceeds every order and the sums saturate; no such assertion is made. The final wording makes this distinction explicit.

For n≥2, put Y=min(X,n). The first-power difference is n times a residue sum with coefficient sum zero, hence O(n), plus a rounding error at most θ(Y)=O(Y)=O(n). For all higher powers together, the two membership indicators differ in absolute value by at most one, giving at most n·Σ_p(log p)/[p(p−1)]=O(n), uniformly in the cutoff. Orders0 and1 give zero floors. Summing the three labels proves the complete O(N) comparison. No periodic term or rounding contribution has been omitted. In ordinary cases the zero lower certificate is simply integrality. The certificates are not asserted to be exact valuations at every order.

The transitive-group identity follows by counting equally frequent targets of each fixed point. Its fixed-weight extension is sound. The arithmetic application remains limited to the actual abelian mod7 distribution; the text correctly warns that a general nonabelian indicator need not be a class function and that another base field changes prime sampling.

## Integrated preservation and remaining boundary

The integrated proof retains actual integral directions, ordinary witnesses, all labelled orbits, the exact algebraic identity, arbitrary unequal fixed orders, the bounded analytic error, all floor estimates and the scope limitations. No mathematical correction was needed. The final sole wording refinement was independently checked after the complete read and is preserved in metadata; no unreviewed hash was silently accepted.

This establishes the bare derivative redistribution result. It does not upper-bound normalized theta-selected gain, reverse LinkG, permit prime-dependent reassignment, or dismiss a finite O(N) saving in a finite inequality. The actual selected kernels, endpoint image and normalization/cost data remain distinct inputs. No Lean execution or unrelated RH audit was performed.
