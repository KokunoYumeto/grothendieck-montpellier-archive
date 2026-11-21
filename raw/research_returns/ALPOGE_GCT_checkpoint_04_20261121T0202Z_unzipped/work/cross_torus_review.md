# Independent torus-counterexample calculations

Reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Date: 2026-11-20 UTC.

These calculations were made independently from the mathematical specifications sent by the authors, before reading their full drafts. They are genuine independent proofs of the two specified examples; they are not yet a claim to have checked every sentence of those later drafts. The original input-scope passages were inspected directly as detailed below.

## P-F14: unbounded modular index at fixed rank

Let `N>=2`, let `H=G_m`, and let `rho_N:H->GL_2` be `t -> diag(t^(N+1),t)`. Both characters are polynomial and the representation is faithful because its second coordinate recovers `t`. Take outer highest weight `lambda=(1)` and target character `pi=2`. Then `V_(n lambda)=Sym^n(C^2)`. Its monomial basis is `x^k y^(n-k)`, for `0<=k<=n`, and that monomial has torus weight `(N+1)k+n-k=n+Nk`. The weight equals `2n` if and only if `Nk=n`. This equation has exactly one admissible solution when `N` divides `n`, and none otherwise, including the correct value one at `n=0`. Therefore

`f_N(n)=1_{N divides n}` and `sum f_N(n)T^n=1/(1-T^N)`.

Let `zeta` be a primitive `N`th root of unity. This generating function has a genuine simple pole at `zeta`. If it were written as a polynomial numerator divided by a product of factors `1-T^a_j`, at least one factor would have to vanish at `zeta`; a polynomial numerator cannot create a pole where the denominator is nonzero. Thus some `a_j` is divisible by `N`, so `max a_j >= N`. This conclusion does not require numerator positivity. The displayed form attains equality, so the minimum possible maximum denominator weight is exactly `N`.

The source parameter is `rank(x)=rank H+rank G+comb(lambda)+comb(pi)=1+2+1+1=5`. Hence no fixed polynomial in this parameter can bound the modular index as `N` varies. The source's PH3 assertion fails in that broad parameter scope. The constituents are the constants zero or one, so the positivity and saturation indices of this particular example are zero. It does not refute PH2 by itself.

## P-F15: unbounded positivity and saturation indices at fixed rank

Let `N>=3` be odd. Define `rho_N(t)=diag(t,t^3,t^(N+1))` from `G_m` into `GL_3`, again faithful because of its first coordinate. Use the same outer weight `lambda=(1)` and character `pi=2`. A degree-`n` monomial has exponents `(u,v,w)` with `u+v+w=n` and torus weight `u+3v+(N+1)w=n+2v+Nw`. It has target weight `2n` precisely when

`2v+Nw=n`.

Conversely, every nonnegative solution `(v,w)` of this equation yields the nonnegative exponent `u=n-v-w=v+(N-1)w`. This is a bijection, so the stretching function is the number of such solutions and its series is

`F_N(T)=1/((1-T^2)(1-T^N))`.

Here is a complete constituent calculation independent of the earlier two-weight lemma. Use period `2N` and residues `0<=b<2N`. In the equation `2v+Nw=b`, oddness of `N` forces `w` to have the parity of `b`. Since `w<2`, the value at `b` is one when `b` is even or when `b>=N`, and zero exactly when `b<N` is odd. For `n=b+2Nk`, admissible `w` ranges from the least nonnegative integer of that parity to `floor(n/N)`, and increasing `k` by one adds exactly one solution. Thus the constituent polynomial is

`q_b(X)=X/(2N)+c_b`,

where `c_b=1-b/(2N)` when `b` is even or `b>=N`, and `c_b=-b/(2N)` when `b<N` is odd. The minimum of all constants is `-(N-2)/(2N)`, achieved at `b=N-2`.

Shifting the quasi-polynomial by an integer `p` relabels the constituents and replaces every constant by `c_b+p/(2N)`. Their common linear coefficient is positive. Therefore all constituent coefficients are nonnegative if and only if `p>=N-2`, proving the exact positivity index `p(f_N)=N-2`.

For the source's strict saturation condition, every nonzero constituent must be strictly positive at every positive integer argument. These linear polynomials are increasing, so after the shift this is equivalent to strict positivity at argument one. The smallest value is `(p+1-(N-2))/(2N)`. For integer `p>=0`, it is strictly positive exactly when `p>=N-2`. Hence the exact saturation index is also `s(f_N)=N-2`.

Now `rank(x)=1+3+1+1=6`, independent of `N`. Thus the rank-only bounds of broad GCT VI Hypotheses 3.3.2(a) and 3.3.3 fail in the printed input scope. This calculation does not address the separate almost-all density assertion 3.3.2(b).

## Source-scope check

Directly read: supplied `sources/LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex`, Section 3.4 and its two input subsections, together with the corresponding text extraction `work/positivity_sources/GCTVI.txt`.

- Section **3.4**, printed pp. **52--53**, defines `rank(x)` as the sum of the ranks of `H` and `G` and the combinatorial sizes of the stretched highest weights. It includes the description of `rho` in the ordinary and combinatorial input lengths, but does **not** include it in `rank(x)`.
- Section **3.4.1**, printed pp. **53--54**, permits a direct sum of irreducible polynomial representations as a basic explicit polynomial homomorphism. It explicitly includes polynomial one-dimensional torus characters and does not bound their exponents.
- Section **3.4.2**, printed pp. **55--56**, defines a torus character's combinatorial length to be the dimension of the torus, permits direct sums with additive specifications, and specifies a `GL_m` highest weight by its nonzero parts. These rules yield the fixed values five and six above.
- Hypotheses **3.3.2(a)**, **3.3.3**, **3.3.4**, printed p. **51**, quantify absolute polynomial bounds in `rank(x)`, across this allowed subgroup-restriction input. The general subgroup problem is one of the cases enumerated in Hypothesis 3.3.1; no nonzero-at-one restriction is inserted into 3.3.2(a), 3.3.3, or 3.3.4.

These are text-level source checks, not a new scan-image inspection. The examples use **reducible** inner representations and vary the embedding with `N`. They therefore do not refute fixed-embedding finite-generation statements or the narrower irreducible-inner generalized plethysm Hypotheses 1.6.5--1.6.7. A repaired uniform parameter must account for the magnitudes of the embedding weights; even their binary length alone cannot give polynomial bounds for these exact indices, since the indices grow linearly in `N` while the binary description has length `O(log N)`.

No historical-priority claim is made.

## Subsequent whole-draft review

After the independent proofs above, I read the entire author draft `work/positivity_torus.tex`. Its two propositions, proof of closed embeddings, exact constituent representative argument, source locators, rational-polytope models, and binary-input conclusion all pass. The binary input length is of order `log N` because it explicitly contains the positive exponent `N+1`; therefore the unbounded indices grow exponentially in that length, not merely faster than the fixed rank parameter. I reported the single LaTeX typo `+operatorname{rank}G` to the owner for correction. No mathematical correction was needed. This additional event is an independent-agent targeted whole-proof review of the actual draft.

I subsequently read the added actual multiplicity-algebra paragraph and its full surrounding proof. The equation `u=v+(N-1)w` gives the polynomial algebra `C[xy,x^(N-1)z]`; distinct exponent pairs prove algebraic independence over every field. Its generator degrees are exactly two and `N`, so the smooth affine plane is the actual diagonal multiplicity algebra, with its varying grading, and not merely an unrelated algebra with matching dimensions. The stated compactly supported cohomology and constant shifted intersection complex follow from the affine-plane purity and duality facts already independently inspected for PLE-F7. The newly added floor formula counts admissible `w` of the required parity correctly also at `n=0,1`; it gives a binary-polynomial-time evaluation algorithm. The source scope and all earlier index calculations remain unchanged. This addition passes.
