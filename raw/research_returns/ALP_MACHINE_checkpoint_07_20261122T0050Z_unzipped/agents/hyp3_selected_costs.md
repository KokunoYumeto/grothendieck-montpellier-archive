# AM-K026 — a full-Hyp3 family, exact selected norm correction, and the remaining cost interval

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

This result goes beyond the HC-only unit examples. It supplies an explicit family satisfying every numerical clause of the source's stronger analytic Hyp3, computes the adjacent-gap content bound and the exact hook/mass factors, and proves that the K024 upper slope survives the selected target metric normalization. It still does not identify the second restricted class-image lattice or the full D7/SizeData₂ arithmetic adapter.

The classical/source inputs are retained as theorems. In particular the noncompact-gap spacing lemma is used at its exact recovered interface, and the hook norms are the parent's AM-R-011.

## 1. A concrete full-Hyp3 baseline

Fix an admissible source rank record with k,m even, t odd, r=k+m−1, d=t+1, and \(1801\le r+t\). Put
\[
 S=r+mt,\qquad Q=S^3+2,\qquad G=2Q+d=2S^3+t+5.
\tag{HC1}
\]
At every CM embedding define
\[
 u_i=k-\tfrac12-i,\quad v_i=k-1-i,\quad
 b_j=jG,\quad e_j=(j+\tfrac12)G.
\tag{HC2}
\]
The integer G is even. Set eta to the required \(-\operatorname{infTy}(\eta_T)\).

### Proposition HC3

These parameters satisfy the literal HCParam record and the stronger Hyp3 of CayleySignature.lean, lines 110–118, including the 1801 condition, Centred and NCGaps. The actual selected compact partitions are
\[
 \nu_j=
 Q\,((2j+1)^k,(2j)^d,(2j-2)^d,\ldots,2^d)
\tag{HC3}
\]
at every one of the six labels.

**Proof.** All u values are half-integral and v,b,e are integral. The two u,v interlacing gaps equal 1/2; the last u equals 1/2>−b₀=0. The b,e entries alternate strictly increasingly, and both HC gaps equal G/2, which exceeds \((t+3)/2\). Thus both the HC record and TPar.Interlace and TParity hold.

For Centred, u and v are positive, and every e is at least G/2. Thus the required u+e and v+e absolute values exceed \((t+3)/2\). For any i,j, \(|e_j-b_i|=|j+1/2-i|G\ge G/2\). If j′≠j and \(x\in\operatorname{block}(-e_{j'},t)\), then
\[
 |x+e_j|\ge |j-j'|G-(t-1)/2
                   \ge G-(t-1)/2>(t+3)/2.
\]
This checks every Centred clause in DataTheta.lean, lines 550–554.

For NCGaps apply the accepted source theorem noncompact_gaps_of_spacing in ExistsTowerOfLocalSetting.lean, lines 99–103. Its required lower spacing is
\(2(r+mt)^3+t+3\), and G exceeds that by 2. Its other hypotheses are \(-b_0<v_i\), pairwise b spacing at least G, and \(e_j<b_{j+1}\); all were just checked. This gives the exact NCGaps predicate for every j≤m. The 1801 and eta clauses hold by construction.

Finally \(w_{0,i}=u_i-\rho_k(i)=k/2\). Hence DO25.5 gives
\(\nu_0=e_0-d/2=Q\) in every row. The exact increment is
\(\Delta_j=e_{j+1}-e_j-d=G-d=2Q\). Recurrence DO25.11 gives (HC3). ∎

This supplies the source's full analytic parameter conditions. It does not assert that these numbers satisfy every separately prescribed global upper window, or that an unchanged old induced-CM D7 record has been instantiated on the ordinary E′ host.

## 2. Compulsory first divisibility and an explicit upper bound

Write \(a=k+jd,\ b=a+d\), and
\[
 R_j=kj+d\,j(j+1)/2.
\]
The total degree and the anti-diagonal upper bound from AM-K025 are
\[
 D_j=6Q\{k(2j+1)+d\,j(j+1)\},
\tag{HC4}
\]
\[
 U_j=6k\,v_{11}(Q!)+6R_j\,v_{11}((2Q)!).
\tag{HC5}
\]
The nonzero prefix differences are Q at k and 2Q at k+d,…,k+jd. In particular
\[
 U_j=\frac{D_j}{10}
       -\frac6{10}\{k\,s_{11}(Q)+R_j\,s_{11}(2Q)\}.
\tag{HC6}
\]

For this family every stage satisfies the universal mod-11 cutoff:
\[
                              D_j>3140ab.
\tag{HC7}
\]
Indeed every part is at least Q, so \(D_j\ge6aQ\). The target rank b is at most
\(N_m=k+m(t+1)=S+1\). Since S≥r+t≥1801, the elementary inequality
\(6(S^3+2)>3140(S+1)\) proves (HC7).

There is also an exact minimum, rather than just this coarse comparison:
\[
 \frac{D_j}{ab}
   =\frac{6Q}{d}\left(1-\frac{k^2}{ab}\right),\qquad
 \min_{0\le j<m}\frac{D_j}{ab}
                         =\frac{6Q}{k+d}.
\tag{HC7a}
\]
To verify the identity, expand \(ab=k^2+kd(2j+1)+d^2j(j+1)\). The product ab strictly increases with j, so the displayed ratio strictly increases. Its minimum is at the first edge.

Consequently the exact selected highest-row image ideal satisfies
\[
                      \boxed{1\le v_{11}(I_{\nu_j})\le U_j.}
\tag{HC8}
\]
The lower bound is only one factor of 11. Neither the large degree nor the cutoff justifies iterating it after dividing the module by 11. The width of (HC8) is an unresolved quantitative gap, not an exact gain calculation.

Increasing the u₀ entries as in AM-K024 preserves this same full Hyp3 and only increases D at the fixed edge. Thus every member of that family remains above the cutoff, while K024 still gives selected coefficients with upper asymptotic rate at most 1/1220. These two facts are compatible: compulsory first divisibility does not determine an asymptotic slope.

## 3. A fully explicit two-edge instance

Take
\[
 k=6,\quad m=2,\quad t=1795,\quad d=1796,\quad r=7,
\quad \mathrm{ord}=3.
\tag{HC9}
\]
All the source rank inequalities hold, and r+t=1802≥1801. The values are
\[
 S=3597,\quad Q=46\,539\,457\,175,\quad
 G=93\,078\,916\,146.
\tag{HC10}
\]
Thus
\[
 (b_0,b_1)=(0,93\,078\,916\,146),\qquad
 (e_0,e_1)=(46\,539\,458\,073,139\,618\,374\,219).
\]
The u entries are \(11/2,9/2,7/2,5/2,3/2,1/2\); the v entries are 5,4,3,2,1.

The exact numerical consequences are:

| Quantity | Stage 0 | Stage 1 |
|---|---:|---:|
| Compact edge a→b | 6→1802 | 1802→3598 |
| Selected partition at each label | \(Q^6\) | \((3Q)^6,(2Q)^{1796}\) |
| Total six-label degree D | 1,675,420,458,300 | 1,008,044,642,410,500 |
| D/(3140ab), approximately | 49,350.1104664 | 49,514.7022745 |
| Proven lower bound for \(v_{11}(I_\nu)\) | 1 | 1 |
| Adjacent-gap upper bound U | 167,542,045,704 | 100,804,464,197,676 |
| Least e with \(29^e\ge3D+2\) | 9 | 11 |
| Permitted level M | 14,507,145,975,869 | 12,200,509,765,705,829 |

The certified factorial values are
\[
 v_{11}(Q!)=4\,653\,945\,714,\qquad
 v_{11}((2Q)!)=9\,307\,891\,431.
\tag{HC11}
\]
Every integer and every source rank, Interlace, Centred and NCGaps check in this example is reproduced by hyp3_selected_cost_certificate.py. The program compares all opposite-sign discrete parameters for j=0,1,2; the minimum nonvacuous gap is G, against the required \(S^3=46\,539\,457\,173\). Common eta shifts cancel from these differences.

## 4. Exact hook and class-mass factors for that instance

Let Hν be the hook product of one label. The source coefficient partition is
\(\eta_0=0\) and \(\eta_j=(\nu_{j-1},0^d)\) for j≥1. Thus the actual uniform insertion exponent is Q at stage 0 and 2Q thereafter. AM-R-011 gives the exact recurrence
\[
 H_{\nu_j}
   =H_{\eta_j}
       \prod_{i=1}^{a}
        \frac{(\eta_{j,i}+q_j+a-i)!}{(\eta_{j,i}+a-i)!},
 \quad q_0=Q,\quad q_j=2Q\ (j\ge1).
\tag{HC12}
\]
The ratio is the actual coefficient norm insertion. Its product over stages telescopes to \(H_{\nu_{m-1}}/H_{\eta_0}\); these ratios must not also be counted as independent uncancelled row-metric losses.

For the example:

| Exact 11-adic factor | Stage 0 | Stage 1 |
|---|---:|---:|
| \(v_{11}(H_\nu)\), one label | 27,923,674,284 | 16,800,744,033,680 |
| \(v_{11}(H_\nu/H_\eta)\), one label | 27,923,674,284 | 16,772,820,359,396 |
| \(v_{11}(I_a(M))\), R012 class index | 0 | 1182 |
| \(v_{11}(\dim\rho)\), six-label source coefficient | 0 | 0 |

Here the mass convention is the exact AM-R-012 convention
\[
 I_a(M)=M^{6a^2}\prod_{\ell=1}^{a}(1-29^{-\ell})^6.
\tag{HC13}
\]
At 11 its valuation is independent of the exponent e in M=29^e, because M is an 11-unit. The source dimension is computed by the Weyl dimension formula for η; at stage 1 it is the six-label product for \((Q^6,0^{1796})\). This is an integer dimension, not a denominator inserted into a polynomial projection.

For scale, high-precision numerical evaluations give
\[
 \log H_{\nu_0}\approx6.5798135173845434\cdot10^{12},\qquad
 \log H_{\nu_1}\approx4.0756480430066282\cdot10^{15}.
\tag{HC14}
\]
These logarithms are numerical evaluations of the exact factorial products, not standalone interval certificates. All exact valuations are computed with integers.

The actual primitive highest creation norm remains, by AM-R-011,
\[
 \log\|\phi_j^{\rm hw}\|_\infty
  =-\frac{ab}{2}\log\det(2Y)
       +3\log H_{\nu_j}
       +|\nu_j|\sum_{i=1}^3\log\frac{\pi}{2G_i}.
\tag{HC15}
\]
The algebraic-to-analytic kernel period is still \(C^{2ab}\). Subtracting its logarithmic absolute value gives an additional explicit term \(-2ab\log|C|\); that period is not removed by (HC12). Source class extraction also retains (HC13) and its compact dimension exactly as in R012.

These formulas exhibit concrete archimedean and finite factors on a full-Hyp3 family. The interval (HC8) is too wide to identify the actual local gain, and no sum of the separate factors is labelled a total DP44 error.

## 5. Exact metric correction for the scalable K024 selected vector

The target vector in K024 was shown to lie in the exact selected Cauchy summand, but it need not be its highest vector. Its normalization can be computed exactly, with no projector bound.

Fix one residual partition \(\lambda\) of length a. On the spare column let
\[
       P_h=Z_{1,1}^{h}\,Q_\lambda(Z_{\text{columns }2,\ldots,a+1}).
\tag{HC16}
\]
The variables in its two factors are disjoint. The Fischer monomials are orthogonal, so
\[
                    \|P_h\|_{\rm F}^2=h!\,H_\lambda.
\tag{HC17}
\]
Its selected source partition is \(\lambda+h e_1\). In the Cauchy realization with unit source highest vector and the target compact metric whose highest vector has norm one, AM-R-011 therefore gives the exact target squared norm
\[
                  \theta_\lambda(h)
                  =\frac{h!H_\lambda}{H_{\lambda+h e_1}}.
\tag{HC18}
\]
No independent hook penalty is added to (HC17): (HC18) is the comparison between the two ways of expressing that same norm.

Put \(L=\lambda_1+a-1\) and \(c_j=\lambda_1-\lambda_j+j-1\), j=2,…,a. The hook factorial/Vandermonde formula from R011 gives
\[
 \boxed{\theta_\lambda(h)=
  \frac1{\binom{h+L}{L}}
       \prod_{j=2}^{a}\frac{h+c_j}{c_j}.}
\tag{HC19}
\]
The c_j are distinct integers in {1,…,L}. Cancelling them from the rising factorial gives the equivalent manifestly positive formula
\[
 \theta_\lambda(h)
   =\prod_{s\in\{1,\ldots,L\}\setminus\{c_2,\ldots,c_a\}}
                         \frac{s}{h+s}.
\tag{HC20}
\]
There are exactly λ₁ factors. In particular
\[
        0<\theta_\lambda(h)\le1,\qquad
        |\log\theta_\lambda(h)|=O_\lambda(\log(h+1)).
\tag{HC21}
\]

The corresponding source compact dimension obeys
\[
 \frac{\dim S_{\lambda+h e_1}(\mathbf C^a)}
      {\dim S_\lambda(\mathbf C^a)}
                         =\prod_{j=2}^{a}\frac{h+c_j}{c_j}.
\tag{HC22}
\]
Removing a determinant twist does not change that dimension, so it is precisely the dimension ratio for the actual row coefficient η.

For the finite valuation, Kummer's carry formula, or directly Legendre's formula, gives
\[
 v_{11}\binom{h+L}{L}\le\lfloor\log_{11}(h+L)\rfloor
 \quad(h+L\ge1).
\]
Thus (HC19) implies
\[
 v_{11}(\theta_\lambda(h))
 \ge-\lfloor\log_{11}(h+L)\rfloor-\sum_{j=2}^{a}v_{11}(c_j).
\tag{HC23}
\]
The analogous upper bound and (HC22) give absolute valuation bounds of order log(h+1), with the residual rank and partition fixed.

Apply this at the four growing labels of K024, with
\((h,A_r-h,k,B_r-k)\), and write Θ for the product of their θ factors. Scaling the target vector to norm one multiplies its polynomial and its kernel coefficient by Θ^{-1/2}. This is an explicit algebraic scalar; it is not silently treated as an integral lattice unit. Combining (HC23) with K024 gives
\[
 v_{11}(a_r/\sqrt{\Theta})
       \le\frac{11^r-1}{10}+c_0+O(\log T_r).
\tag{HC24}
\]
The upper slope bound remains 1/1220. With the primitive polynomial kept instead, its exact actual creation norm is
\[
\begin{split}
 \|\phi_{r,h,k}\|_\infty^2={}&
  \det(2Y)^{-ab}
  h!(A_r-h)!k!(B_r-k)!
       \prod_\tau H_{\nu_\tau^*}\\
 &{}\cdot
  \left(\frac{\pi}{2G_3}\right)^{A_r}
  \left(\frac{\pi}{2G_2}\right)^{B_r}
  \prod_\tau
   \left(\frac{\pi}{2G_{i(\tau)}}\right)^{|\nu_\tau^*|}.
\end{split}\tag{HC25}
\]
Dividing this expression by Θ gives exactly the R011 norm with the new selected hook products. These are alternative normalizations of the same vector, not additive costs.

For fixed ranks, the AM-R-012 source class index has \(\log I_a(M)=O(\log T_r)\) at M=O(Tᵣ), and its 11-valuation is constant in e. Equation (HC22) gives \(\log\dim\rho=O(\log T_r)\) and \(v_{11}(\dim\rho)=O(\log T_r)\). Therefore the exact class-supported first extraction and the target metric comparison change this fixed-rank valuation upper bound by at most O(log Tᵣ). The creation norm (HC25), the fixed period, and all other primes remain present.

For the explicit first-edge baseline \(\lambda=(Q^6)\), this simplifies to
\[
 \dim S_{(h,0^5)}(\mathbf C^6)=\binom{h+5}{5},\qquad
 \theta_\lambda(h)=
            \frac{\binom{h+5}{5}}{\binom{h+Q+5}{Q+5}}.
\tag{HC26}
\]
These formulas make the full-Hyp3 normalized first family completely explicit. They do not control an arbitrary irreducible component after further global decomposition or the second restricted class-image lattice.

## 6. What is still needed for actual g/e

The actual finite local section matrix B is now bounded above on selected families, and its first forced divisibility on a fully admissible analytic family is proved. The permitted finite half-orbit adds no saturation loss by K022. The selected compact metric and first source class extraction have explicit factors.

What remains is not a choice of polynomial normalization: it is the integral image of the already produced source vector under the next selected class matrix, including its fixed branch maps and mass pairing. A larger local gain might hold on that restricted image even when it fails on the full permitted selected kernel family. Conversely no existence theorem for a later nonzero theta representation supplies its valuation content or a controlled integral projection. The current results neither prove such a gain nor rule it out.

### Source locators and certificate

- Formalism/LocalRingCardinality/Params.lean, Ranks and HCParam, lines 7–69.
- Formalism/LocalRingCardinality/DataTheta.lean, TPar.Interlace, Dpar and Centred, lines 529–554.
- Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean, NCGaps and stronger Hyp3, lines 110–118.
- Formalism/SharpRestriction/CuspSpanNormBounds/UnimodularSchurMeasures/ExistsTowerOfLocalSetting.lean, noncompact_gaps_of_spacing, lines 99–103; the separate integer constructor begins at line 181 and its Hyp3 theorem at line 199. The proof here uses the spacing theorem with the displayed constant-midpoint family; it does not claim that this is the different terminal midpoint choice made by that constructor.
- AM-R-011, R11.7–17: exact Fischer hook norm, determinant insertion and normalized row metric. AM-R-012: exact class-supported extraction and mass. AM-K022–025: finite jets, common source gauge, normal forms, adjacent-gap upper bound and the scalable witness.
- hyp3_selected_cost_certificate.py and its JSON output: exact rank/Hyp3 comparisons, factorial and hook valuations, source dimension valuation, 29-level and index valuation; numerical logarithms are explicitly marked as such.
