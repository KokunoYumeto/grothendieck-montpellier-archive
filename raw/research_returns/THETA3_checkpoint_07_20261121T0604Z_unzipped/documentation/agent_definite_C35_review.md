# THETA3-C35 independent whole-proof review

Reviewer: GPT-6 Astra Pro, `/root/definite_bridge`; reasoning effort inherited and not exposed. Date: 2026-11-21.

**Result: PASS at the explicitly stated horizontal formal-chart scope.** I read all of the final `paper_C35.tex`, including the clarification that evaluation at `X=-q` is a formal polynomial identity rather than a standard representation-density interpolation point or an arithmetic Siegel–Weil formula.

## Reconstructed proof

The Rosati convention sends the first coordinate `bar(a)` of each labelled homomorphism to `a` in the dual equation. Direct multiplication gives the displayed Gram matrix, determinant `a bar(a)`, and the three integral generator changes give exactly `diag(a bar(a),1,1)` with unimodular change of basis. There is no missing polarization scalar.

For the map `Phi(P,Q,T)=(T-aP-Q,T-aP,T-Q)`, its output `(u,v,w)` satisfies `Q=v-u`, `T=w+v-u`, and `aP=w-u`. Thus integral row and column operations reduce it to `[a] x 1 x 1`. The finiteness and flatness proof for `[a]` is valid over the given DVR: a nonzero integral multiple factors through it, properness and fibrewise finiteness give finiteness, fibrewise surjectivity and the regular local dimensions give miracle flatness. Flat pullback of the regular zero section produces a regular sequence of length `3 dim(B)`. The product of the three graph Koszul resolutions therefore has no higher homology and resolves the actual torsion kernel. The degree is the norm because the rational CM homology has rank one over `E`.

The formal closure comparison uses precisely the graph ideals already proved in C33, with free toroidal coordinates. Flat formal base change preserves this Koszul calculation, and the toroidal parameters remain a regular sequence on the finite flat torsion intersection. The boundary Gysin pullback is consequently the asserted actual torsion cycle. The labels and prime-to-p chart isogenies are retained, and no proper contraction of the entire formal chart is assumed.

At the specified inert CM primes, each strict one-dimensional height-two formal factor contributes length `p^(2 r_nu)`. The prime-to-p torsion factor has one reduced identity point. Tensor products multiply the local lengths, giving `p^(2 sum r_nu)`.

For the coherent local density, an integral overlattice of `diag(p^(2r),1,1)` splits off its self-dual rank-two summand. The remaining possibilities have indices `j=0,...,r`, type one before the final self-dual lattice, and type zero at the final lattice. The weighted sum is `(1-X) sum_{j=0}^{r-1} X^(2j)+X^(2r)=sum_{j=0}^{2r}(-X)^j`. Its value at one is one and its derivative there is `r`. The difference at `-q` between the ranks indexed by `r` and `r-1` is `q^(2r-1)+q^(2r)`, giving the exact factor `q/(q+1)`. The even determinant valuation makes this the coherent split case, so the nonsplit odd-valuation derivative-intersection theorem is correctly not invoked.

## Primary sources actually read

- Li–Zhang, local file `work/external/LiZhang_KRProof.txt`: all of §§3.1–3.5 through Theorem 3.5.1 and its full proof, and Example 3.5.2 (printed pp16–18). This includes the normalization at `X=(-q)^(-k)`, Definition 3.2.1, cancellation by a self-dual summand, the precise local KR theorem scope, and the weighted overlattice formula.
- Milne, `work/external/Milne_AV.txt`: Lemma 10.8 and the complete following complex-torus degree argument (printed p46), and Proposition 10.23 with its complete proof (pp52–53).
- Stacks Project Tag 00R4, Lemma 10.128.1: full statement and induction proof of miracle flatness, read from the primary page `https://stacks.math.columbia.edu/tag/00R4`.
- Stacks Project Tag 0BFG, Lemma 39.9.8: full statement and proof of finite locally free multiplication on an abelian variety, read from `https://stacks.math.columbia.edu/tag/0BFG`.
- The C33/C34 graph-closure and labelled-boundary inputs were independently whole-proof checked earlier; their exact Lan source reads are recorded in `agent_definite_C33_review.md` and `agent_definite_C34_review.md`.

No additional vertical Rapoport–Zink comparison, arithmetic intersection identity, or unspecified normalization is inferred.
