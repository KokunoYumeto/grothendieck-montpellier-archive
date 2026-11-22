# AM-K024 — a scalable sharp upper bound in the actual ordinary E′ selected rows

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

This is a fixed-rank, varying-HC-family statement for the actual ordinary host A=J² with E′=Q(ζ₂₈). It applies to the selected compact Cauchy summands identified in AM-DO-025. It uses the exact primitive-kernel coefficient from accepted DP58. It does not introduce conjugate-action J factors, and it does not identify the output of a later automorphic class integral.

The result gives both a bound for the finite jet functional matrix B and a single allowed finite Schwartz input realizing that bound. It excludes a uniform local slope larger than 1/1220 across the indicated source-selected family. There is no net global cost conclusion.

## 1. Fixed selected edge and exact statement

Fix an admissible source rank record and a stage j with
\[
 a=N_j,\qquad b=N_{j+1}=a+d,\qquad d=t+1\ge2.
\tag{SC1}
\]
Fix word-independent source HC data at each of the six holomorphic embeddings of E′. Let \(\nu_\tau^*\) be the resulting actual selected partitions on this edge. They are positive antitone partitions of length a by AM-DO-025. Put
\[
 D_0=\sum_\tau|\nu_\tau^*|,\qquad
 \mathcal F_0=\prod_{\tau}\prod_{i=1}^{a}\nu_{\tau,i}^*!,\qquad
 c_0=v_{11}(\mathcal F_0).
\tag{SC2}
\]
All these data are fixed as r varies.

Label the six embeddings by \((i,\epsilon)\), \(i=1,2,3\), \(\epsilon=\pm\), using \(z_{i,\pm}=u_i\pm i v_i\) on A=J². These are the actual E′ eigencharacters, with the underlying J character i. Set
\[
 A_r=11^r,\qquad B_r=121\,11^r,\qquad
 T_r=A_r+B_r+D_0=122\,11^r+D_0.
\tag{SC3}
\]

### Theorem SC4

For each r≥0 there are integers \(0\le h_r\le A_r\), \(0\le k_r\le B_r\) and actual source HC data whose selected partitions on this edge are
\[
\begin{array}{ll}
 \nu_{3,+}=\nu_{3,+}^*+h_r e_1,&
 \nu_{3,-}=\nu_{3,-}^*+(A_r-h_r)e_1,\\
 \nu_{2,+}=\nu_{2,+}^*+k_r e_1,&
 \nu_{2,-}=\nu_{2,-}^*+(B_r-k_r)e_1,\\
 \nu_{1,+}=\nu_{1,+}^*,&
 \nu_{1,-}=\nu_{1,-}^*.
\end{array}\tag{SC4}
\]
There is a primitive integral polynomial \(P_r\) in the exact source-and-target Cauchy summand for these selected types whose degree is Tᵣ and whose normalized source jet functional has image-ideal valuation at most
\[
                         \frac{11^r-1}{10}+c_0.
\tag{SC5}
\]

Choose the least M=29^e≥3Tᵣ+2 and κ=M². A single tuple of the actual DP59 half-orbit then satisfies
\[
 a_r=M^{-T_r}[P_r(\partial)F_{\mathcal S_{\mathbf t'}}]_0\ne0,
 \qquad
 v_{11}(a_r)\le\frac{11^r-1}{10}+c_0.
\tag{SC6}
\]
Its finite Schwartz vector has norm one; no interpolating coefficient height is used. Its actual identity theta-kernel value is \(C^{2ab}a_r\), with the one fixed period \(C=\theta_0c\).

Consequently, for any γ>1/1220 and fixed constant C₀, the lower bound
\[
              v_{11}(a)\ge\gamma T-C_0
\tag{SC7}
\]
cannot hold for every allowed selected local coefficient in this fixed-rank HC family. This assertion concerns the union of the explicitly displayed selected types. It does not assert a bound for every vector in one fixed type or one fixed later theta image.

## 2. The source HC change is literal

At each embedding, increase only the initial entry u₀ of the fixed source HC record by an arbitrary nonnegative integer ητ. Leave its other u entries, every v entry, and every e,b entry fixed.

In Formalism/LocalRingCardinality/Params.lean, lines 50–69, the only interlacing condition involving u₀ is \(u_0>v_0\). It remains true after this increase. The last-u condition is unaffected because k≥2; the half-integer condition remains true; the e,b gaps and integer conditions are unchanged. Thus this is an actual HC record. Choosing the same change for every word preserves the source's word-compatibility equations.

The initial source weight is \(w_{0,i}=u_i-\rho_k(i)\). Increasing u₀ by ητ increases its first entry by ητ and changes no other entry. The exact recurrence DO25.6 copies this change into the first entry of every subsequent source weight. Formula DO25.5 therefore gives
\[
                     \nu_{j,\tau}=\nu_{j,\tau}^*+\eta_\tau e_1.
\tag{SC8}
\]
Taking the four η's in (SC4) gives precisely those selected partitions. Their dominance is preserved by increasing the first entry.

All e entries remain unchanged, so the actual common source-and-target character on every edge is unchanged. This is stronger than freely choosing six unrelated partitions. It does not, however, preserve a size window that independently bounds u₀. Such a window must grow with the indicated HC changes.

### Full analytic Hyp3 is preserved when the fixed baseline satisfies it

Suppose additionally that the fixed baseline TPar satisfies the source's stronger Hyp3 in CayleySignature.lean, lines 110–118, including the condition \(1801\le r+t\). Then every u₀ modification used above satisfies that same Hyp3.

To check every clause, the 1801 condition and the parity and eta clauses are unchanged. Interlace was checked above. DataTheta.lean, TPar.Dpar, lines 538–544, depends only on v,b,e,t,eta, so every discrete parameter set and therefore every NCGaps inequality is literally unchanged. In TPar.Centred, lines 550–554, only the inequalities involving u₀ can change. Interlacing implies \(u_i\ge u_{\mathrm{last}}>-b_0\), and \(e_j\ge e_0>b_0\): the e,b entries alternate strictly increasingly. Thus \(u_i+e_j>0\). Increasing u₀ consequently increases its absolute value \(|u_0+e_j|\); its required lower bound is preserved. All other Centred inequalities are unchanged.

This proves full analytic Hyp3 preservation, as well as preservation of IsMu because e is fixed. Hence SC4–SC20 apply within a genuinely Hyp3-admissible analytic parameter family whenever one such baseline is supplied. They still do not preserve separately fixed SizeData₂ upper windows or identify an iterated arithmetic row.

## 3. A primitive source-highest polynomial with one spare column

Use an a-by-b symbol matrix \(Z_\tau\) for each label. Reserve column 1. On columns 2,…,a+1 define the residual prefix-minor polynomial
\[
 Q_0(Z)=
 \prod_\tau\prod_{\ell=1}^{a}
 \det\bigl(Z_{\tau,\{1,\ldots,\ell\},
                         \{2,\ldots,\ell+1\}}\bigr)^{
                           \nu_{\tau,\ell}^*-\nu_{\tau,\ell+1}^*},
 \qquad \nu_{\tau,a+1}^*=0.
\tag{SC9}
\]
These columns exist because b≥a+1. The same columns can be reused for the six labels: they are independent sets of variables.

For \(0\le h\le A_r\), \(0\le k\le B_r\), put
\[
\begin{split}
 P_{r,h,k}={}&
 Z_{3,+,1,1}^{h}
 Z_{3,-,1,1}^{A_r-h}
 Z_{2,+,1,1}^{k}
 Z_{2,-,1,1}^{B_r-k}\,Q_0(Z).
\end{split}\tag{SC10}
\]
Every factor in Q₀ is invariant when an earlier row is added to a later row. A monomial using only row 1 retains this invariance. The row degrees are exactly (SC4), with h,k in place of hᵣ,kᵣ. The product of the residual diagonal terms and the displayed first-column monomial has coefficient one. Hence Pᵣ,h,k is primitive in the polynomial coefficient lattice.

### Exact common source-and-target Schur label

The row-invariance assertion places this polynomial in the source-highest subspace of its indicated row weight. It also determines the target representation. Indeed, for each embedding the actual Cauchy decomposition is
\[
 \operatorname{Sym}(T\otimes S^*)
       =\bigoplus_\mu S_\mu(T)\otimes S_\mu(S)^*.
\tag{SC11}
\]
In a source irreducible \(S_\mu(S)^*\), the specified maximal-unipotent invariant line has the source highest weight corresponding to μ, and no other such invariant weight. Since the partitions label pairwise distinct source highest weights, the invariant subspace of the row weight ν in (SC11) occurs only in its μ=ν summand. Thus
\[
 P_{r,h,k}\in
 \bigotimes_\tau
      S_{\nu_\tau}(T_\tau)\otimes
              (\text{source highest line in }S_{\nu_\tau}(S_\tau)^*).
\tag{SC12}
\]
Restoring the fixed determinant twists in DO25.3 gives exactly the contragredient selected source type and the selected target type DO25.7–9.

The target vector need not be its highest vector, but it lies wholly in that same irreducible target representation. It does not split among different target Schur labels. No rational projector or projection denominator is introduced: the integral polynomial itself is already in the required Cauchy summand. A demand for one separately fixed target-highest coefficient would be an additional restriction, not part of (SC12).

This argument is over characteristic zero, where the source comparison lives. Its integral assertion is the explicit polynomial with coefficients in R. Any further comparison with a differently normalized abstract Weyl pairing retains the normalization factors studied in the parent's selected-Schur metric report; none is set to one here.

## 4. The actual primitive-kernel input and the exact filler factorial

The Hom variety is \(A^{ab}=J^{2ab}\) with its ordinary J factors. On the first ordinary J factor at row 1, column 1, let X₃ and X₂ be the differential symbols for the two primitive integral directions of actual E-labels 3 and 2. They satisfy
\[
             X_3=Z_{3,+,1,1}+Z_{3,-,1,1},\qquad
             X_2=Z_{2,+,1,1}+Z_{2,-,1,1}.
\tag{SC13}
\]
This follows from the exact coordinate change z±=u±iv. Any unit changes to the DP49 unit-arrow display coordinates preserve the valuations below.

Accepted DP58, equations ES11–12 and the mixed monomial evaluation recorded in DP65 EH16–17, gives the actual unit-parameter primitive kernel in these ordinary directions:
\[
 v_{11}\!\left(
 \partial_{X_3}^{A_r}\partial_{X_2}^{B_r}
                   F_{-\kappa}(0)\right)
                         =\frac{11^r-1}{10}.
\tag{SC14}
\]
The parameter −κ is a unit for every allowed M. AM-K018 matches the full-O_E source gauge on these ordinary J factors. DP54 and DP59 give the integral unit algebraic prefactor that cancels the local frame unit, so (SC14) is an actual permitted integral-local-section functional value. The pure primitive kernel is not substituted for the fixed sigma section without this exact prefactor comparison.

On the filler columns choose the ordinary integral algebraic monomial whose linear logarithmic term is
\[
              \prod_{\tau,i}z_{\tau,i,i+1}^{\nu_{\tau,i}^*}.
\tag{SC15}
\]
It has degree D₀. The residual highest polynomial Q₀ has matching monomial coefficient one; every other supported monomial has a different exponent. Since its degree is D₀, higher terms of the coordinate changes or of every reduced frame cannot contribute. Therefore the filler evaluation is exactly
\[
                    Q_0(\partial)(\text{filler germ})|_0
                                      =\mathcal F_0.
\tag{SC16}
\]
No factorial is inverted. The underlying change between the ordinary J coordinates and the E′ coordinates has unit determinant at 11. Thus the prefactor in (SC15) is integral in the actual formal coordinate lattice.

Take the product of the first-column primitive-kernel prefactor, these filler monomials, and normalized unit prefactors on unused entries. It is an actual integral formal local section of \(\mathcal L^\kappa\). Factorization between the first column and filler columns gives
\[
 v_{11}\!\left(
 M^{-T_r}
 [X_3^{A_r}X_2^{B_r}Q_0(\partial)F_S]_0
 \right)
                         =\frac{11^r-1}{10}+c_0.
\tag{SC17}
\]
The displayed \(M^{-T_r}\) is a unit. This is a construction in the finite jet module B; globalizing it is the separate integral interpolation step of AM-K022.

## 5. Weight extraction without a projection denominator

Expanding (SC13) gives the exact identity of differential polynomials
\[
 X_3^{A_r}X_2^{B_r}Q_0
    =\sum_{h=0}^{A_r}\sum_{k=0}^{B_r}
          \binom{A_r}{h}\binom{B_r}{k}P_{r,h,k}.
\tag{SC18}
\]
Every coefficient is an integer. Apply this equality to the single integral formal section just constructed. If every nonzero component value had valuation greater than the right side of (SC17), their integral linear combination would have greater valuation too. Consequently at least one pair (hᵣ,kᵣ) has
\[
 v_{11}\!\left(
  M^{-T_r}[P_{r,h_r,k_r}(\partial)F_S]_0
          \right)
                         \le\frac{11^r-1}{10}+c_0.
\tag{SC19}
\]
Terms whose binomial coefficient is divisible by 11 cause no difficulty: the argument only uses integrality, and does not divide by a binomial coefficient. This proves the image-ideal bound (SC5) for an actual selected row. It does not assert equality or a matching lower bound for that row.

Now use AM-K022 with D=Tᵣ. Its allowed half-orbit span realizes every integral algebraic Tᵣ-jet for M≥3Tᵣ+2. Equivalently, J30 identifies its derivative image ideal with that of the finite jet module. Expanding one realizing section in its integral allowed basis and applying the nonarchimedean valuation inequality chooses an individual tuple obeying (SC6). The canonical tuple consists of global algebraic points and sections by carried DP59(c), even when the interpolating coefficients were complete-local.

The finite Schwartz vector is a single Heisenberg translate of the fixed norm-one vacuum. Hence its norm is one, and its translation coefficient vector is a standard basis vector. The actual all-polynomial identity DO26.4 gives the fixed period \(C^{2ab}\), with no degree-dependent replacement.

Finally
\[
 \frac{(11^r-1)/10+c_0}{122\,11^r+D_0}
                              \longrightarrow\frac1{1220}.
\tag{SC20}
\]
This proves the failure of every larger uniform slope in (SC7).

## 6. What this closes and what it leaves

The old DP65 construction used both ordinary and conjugate-action J factors in a generalized harmonic module. The present proof uses only ordinary J powers in the actual E′ Hom variety and proves membership in the precise compact source-and-target selected summand. The full-O_E gauge comparison from AM-K018 therefore applies directly. The first-row growth is implemented inside the actual source HC record; the common edge character is unchanged.

The bound is for actual selected **kernel coefficients** in the permitted half-orbit. At the first edge, the parent's class-supported construction AM-R-012 can use such a nonzero coefficient, retaining its source mass, compact norm, selected-polynomial norm and common period. At a later edge, the input is already constrained to a previous automorphic theta image. The restricted class matrix may cancel these coefficients or avoid these witnesses. Neither (SC19) nor the exact finite saturation theorem identifies that image or preserves this value after integration.

Likewise, varying the first HC gaps grows the source size window. The archimedean Schur norm, source class mass, denominator normalizations and the global height identity remain separate costs. The local upper slope cannot by itself be promoted to a statement about the net error or gain of the full Alpöge machine.

## 7. Exact input locators

- Accepted DP58, research/explicit_sharp_jets_linear_levels_DP58.md, §3, ES11–12 and the mixed monomial evaluation; accepted DP65, research/embedding_labelled_harmonic_witness_DP65.md, §5, EH16–17, for the explicitly recorded evaluation of that same carried primitive kernel.
- Accepted DP54, research/global_theta_finite_jets_DP54.md, and DP59, research/theta_translate_span_DP59.md, §§6–8: the integral unit frame prefactor, its finite-jet realization and the actual allowed translate lattice.
- AM-K018: full-O_E source gauge match on ordinary J products; AM-K022: explicit M≥3D+2 threshold, factorial convention, permitted individual tuples, and equality of finite determinantal ideals.
- AM-DO-022: ordinary E′ host and prime-to-11 coordinate change. AM-DO-025, DO25.3–9: exact determinant twists, Cauchy decomposition and selected source/target labels.
- Formalism/LocalRingCardinality/Params.lean, HCParam, lines 50–69: literal u₀ variation. Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean, lines 462–469, and Columns/BaseLemmas.lean, lines 496–552: actual selected-weight identities, carried as in AM-DO-025.
- Formalism/LocalRingCardinality/DataTheta.lean, TPar.Interlace, Dpar and Centred, lines 529–554; Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean, NCGaps and the stronger Hyp3, lines 110–118: exact preservation of the full baseline analytic admissibility conditions.

All new reductions are proved above. No Lean execution, full later-chain realization, or finite computational certificate is claimed by this report.
