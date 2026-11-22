# AM-K025 — an adjacent-gap factorial bound for the actual highest bideterminant

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

**Scope.** The general bound below applies to every selected partition in the ordinary E′ construction. Its zero-content growing-chain example satisfies the literal HC equations only; it does not assert the additional Hyp3, NCGaps, or global SizeData₂ inequalities. Those stronger hypotheses may force much larger adjacent gaps. The result is a local kernel image-ideal bound before restriction to a previous automorphic theta image.

## 1. The bound uses adjacent differences, not the row lengths

Fix a source rank a, target rank b≥a, and the six actual E′ holomorphic labels τ. Let \(\nu_\tau\) be nonnegative antitone partitions of length a. Put
\[
 \delta_{\tau,n}=\nu_{\tau,n}-\nu_{\tau,n+1}\ge0,
 \qquad \nu_{\tau,a+1}=0,
\tag{AG1}
\]
and use the actual primitive highest bideterminant
\[
 P_\nu=\prod_\tau\prod_{n=1}^a
                  \det(Z_{\tau,[1,n],[1,n]})^{\delta_{\tau,n}},
 \qquad D=\sum_\tau|\nu_\tau|.
\tag{AG2}
\]
Both its source and target vectors are highest vectors in the exact selected Cauchy summand. No projection onto either compact type is required.

For M=29^e≥3D+2, let \(I_\nu\) be the image ideal of the normalized derivative functional \(M^{-D}P_\nu(\partial)\) on the actual integral formal section lattice, equivalently on the actual permitted DP59 half-orbit by AM-K022 J30. Then
\[
 \boxed{
 0\le v_{11}(I_\nu)
       \le \sum_{\tau}\sum_{n=1}^a
                                n\,v_{11}(\delta_{\tau,n}!).
 }\tag{AG3}
\]
Equivalently, the upper bound is
\[
 \frac1{10}\sum_{\tau,n}
          n\bigl(\delta_{\tau,n}-s_{11}(\delta_{\tau,n})\bigr).
\tag{AG4}
\]
If every adjacent difference is at most 10, then \(I_\nu=R\): its exact 11-content is zero, and an individual allowed tuple has unit value.

**Proof.** For one fixed label and one prefix size n, use the anti-diagonal determinant term
\[
       (-1)^{n(n-1)/2}\prod_{i=1}^n Z_{i,n+1-i}.
\tag{AG5}
\]
All these choices are simultaneously uniquely leading terms. To see this, choose a constant C>ab and assign positive variable weights \(w_{ij}=C-ij\). A term indexed by a permutation π has weight \(nC-\sum_i i\pi(i)\). Its maximum is uniquely achieved by the reversing permutation: if i<j but π(i)<π(j), swapping those two images decreases the sum by \((j-i)(\pi(j)-\pi(i))>0\). Repeated swaps give the unique reversal. Thus the product of the anti-diagonal terms is the uniquely leading term of (AG2) and has coefficient ±1.

Different prefix sizes use disjoint anti-diagonals, because their variables satisfy different equations i+j=n+1. Consequently the leading monomial has exponent exactly \(\delta_{\tau,n}\) on each of the n variables of that anti-diagonal. Its exponent factorial is therefore
\[
                   \beta!=\prod_{\tau,n}
                                      (\delta_{\tau,n}!)^n.
\tag{AG6}
\]
Apply the highest-symbol interpolation AM-K022 J12 to this monomial. It gives \(\pm\beta!\in I_\nu\), with no factorial inverse or reduced-frame integrality assumption. This proves the upper bound. AM-K023 NF1 proves Hurwitz integrality of the entire actual integral local section module at 11, so \(I_\nu\subset R\), giving the lower bound. If every δ≤10, (AG6) is a unit. The integral allowed basis then contains an individual tuple with unit evaluation. ∎

This can be substantially smaller than the diagonal-monomial bound
\(\sum_{\tau,i}v_{11}(\nu_{\tau,i}!)\). The improvement is an exact monomial calculation inside the same highest bideterminant, with the same selected source and target types.

## 2. Literal minimal HC chain: exact unit content at every stage

This section is **HC-only**. It does not claim admissibility under the stronger 1801 or NCGaps hypotheses.

Fix an already admissible rank record with \(k\) even, \(d=t+1\) even, and put H=(d+2)/2. At every holomorphic embedding use
\[
 b_j=j(d+2),\qquad e_j=H+j(d+2),\qquad
 u_i=k-\tfrac12-i,\qquad v_i=k-1-i.
\tag{AG7}
\]
The two interlacing gaps are 1/2; the last u is 1/2>−b₀; and both e,b gaps equal H. All required integer or half-integer conditions hold. Formula DO25.5 gives \(\nu_0=(1^k)\), while the literal recurrence DO25.11 has \(\Delta_j=e_{j+1}-e_j-d=2\). Therefore
\[
 \nu_j=((2j+1)^k,(2j)^d,(2j-2)^d,\ldots,2^d)
\tag{AG8}
\]
at each label. Its nonzero adjacent differences are
\[
       \delta_k=1,\qquad
       \delta_{k+hd}=2\quad(1\le h\le j).
\tag{AG9}
\]
Thus every selected highest bideterminant in this chain has exact local content zero at 11.

For source rank a=k+jd and target rank b=a+d, its total six-label degree and an exact interpolated value are
\[
 D_j=6\{k(2j+1)+d\,j(j+1)\},
\tag{AG10}
\]
\[
 M^{-D_j}P_{\nu_j}(\partial)F_S(0)
       =2^{\,6kj+3d\,j(j+1)}
\tag{AG11}
\]
for a suitable integral formal section S; the six identical determinant signs multiply to +1. The level can be the least power 29 at least \(3D_j+2\). An individual permitted tuple has unit value, although its value need not be the specific power of 2 in (AG11). Its finite Schwartz norm is one.

The nonzero degrees grow quadratically with j. This rules out a positive local lower bound depending only on total selected degree across all HC records. It leaves open the more restrictive family forced by the global machine, and it does not imply that these unit coefficients survive any later class integral.

## 3. The universal finite cutoff clarifies this scope

AM-K023 NF5 implies, for every integral formal section on each A entry,
\[
 \partial_{1,\pm}^{121}f=0,\qquad
 \partial_{3,\pm}^{121}f=0,\qquad
 \partial_{2,\pm}^{1331}f=0
                       \quad(\bmod11).
\tag{AG12}
\]
Indeed iterating the first or third eleventh-power identity eleven times gives a multiple of \(z^{11}=0\) in the Hurwitz algebra; its coordinate multiplier commutes with that derivative. The middle identity then reduces its 1331st power to a 121st first-label power.

Consequently a nonzero evaluated derivative modulo 11 on A^{ab} has, in each entry, exponents at most 120,120 on the first labels, 1330,1330 on the middle labels, and 120,120 on the third labels. Their sum is 3140 per entry. Therefore
\[
             D>3140ab
 \quad\Longrightarrow\quad
 B(P)\subset11R
\tag{AG13}
\]
for every homogeneous polynomial P of degree D, including every selected row. This is a uniform first divisibility statement for the full integral local section module. It cannot be iterated after dividing by 11 without a further stable-lattice argument.

There is no conflict with (AG8): its degree is far below this dimensional cutoff for the indicated ranks. More generally the adjacent-gap criterion and the cutoff give finite, independently checkable tests that any proposed admissible HC specialization must pass.

## 4. Sources and status

The finite interpolation and permitted span are AM-K022, using carried DP59. The integral local source gauge and Hurwitz module are AM-K018 and AM-K023. The exact selected partitions and determinant twists are AM-DO-025. The HC clauses are Formalism/LocalRingCardinality/Params.lean, lines 50–69.

All new claims are proved above by the leading-monomial argument and the already established operator identities. No new computational certificate or Lean execution is asserted. The general bound (AG3) remains valid for the larger source gaps; only the special unit family is restricted to the stated HC scope.
