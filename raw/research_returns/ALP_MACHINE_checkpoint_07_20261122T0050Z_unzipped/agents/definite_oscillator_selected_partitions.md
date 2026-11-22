# AM-DO-025: the actual common-character compact chain and its exact degrees

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

The selected increasing even-rank chain in the recovered source has
an exact local compact-type match. The failure of the unchanged
trivial-character second edge in AM-DO-023 is therefore not an
obstruction to this selected chain. The computation below uses the
source's actual character exponents, bilinear theta convention, and
coefficient weights. It also computes the polynomial degree required
at each edge. It does not prove global nonvanishing or the arithmetic
row identities.

## 1. Source data and conventions

Fix one selected complex embedding and an actual `HCParam` for ranks

\[
 d=t+1,\qquad N_j=k+jd,\qquad 0\le j\le m.
 \tag{DO25.1}
\]

Here \(k,m\) are even, \(t\) is odd, and the other source rank
conditions are retained. The real numbers \(e_j,b_j\) are
integers, the \(u_i\) are half-integers, and

\[
 u_{k-1}>-b_0,\qquad
 e_j-b_j\ge\frac{d+2}{2},\qquad
 b_{j+1}-e_j\ge\frac{d+2}{2}.
 \tag{DO25.2}
\]

These are `Params.lean`, `HCParam`, lines 50–69, with the decreasing
\(u_i\) forced by its interlacing inequalities. The actual
character on edge \(j\to j+1\) has infinity exponent
\(-e_j\): `ChainParSucc.lean`, `Com.Is.exp`, and
`DataTheta.lean`, `ThetaX.chrOf_inf`. This means
\(\mu_{j+1}(z)=(z/\bar z)^{-e_j}\).

Use **equal source labels** \(\chi_S=\chi_T=\mu_{j+1}\)
on this definite edge, exactly as required by `PinColT.om` and
`PinX.mv` in `LevChiEqOne.lean`. In conventional Konno–Konno
parameters the pair is \((\mu_{j+1},\mu_{j+1}^{-1})\).
The inverse is necessary because the recovered `splitFacO` is
\(\chi_T(x)^{-1}\chi_S(y)\) on determinant roots. This
conversion is checked and corrected explicitly in AM-DO-023.

For source rank \(a=N_j\) and target rank \(b=N_{j+1}\),
the oscillator's holomorphic Fock module is consequently

\[
 \det_a^{e_j-b/2}\boxtimes\det_b^{-e_j+a/2}
       \otimes\operatorname{Sym}(\mathbf C^b\otimes(\mathbf C^a)^*).
 \tag{DO25.3}
\]

The source theta operator is bilinear:

\[
                  (T_\phi f)(h)=\int_{[U(a)]}
                          \vartheta_\phi(g,h)f(g)\,dg.
 \tag{DO25.4}
\]

This is literally `liftT_apply` in
`Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`,
lines 160–167, and `KerDat.lift` in `JointSmooth.lean`, lines 79–82.
Thus the source oscillator must contain the **contragredient** of
the input coefficient type. Confusing (DO25.4) with an integral
against \(\bar f\) reverses this type test.

## 2. Identification with the actual selected coefficient partitions

Write \(w_j=(w_{j,0},\ldots,w_{j,N_j-1})\) for the source's
dominant integral weight `Wts.lamTrue u j τ`. Write
\(\nu_j\) for `Wts.nuW u (j+1) τ`. The recovered source
already proves the precise identities

\[
 \nu_{j,i}=w_{j,i}+e_j-\frac{N_{j+1}}2,
 \tag{DO25.5}
\]

and

\[
 w_{j+1}=
 \left(w_j-\frac d2\mathbf1_{N_j},\,
       \left(-e_j+\frac{N_j}2\right)\mathbf1_d\right).
 \tag{DO25.6}
\]

Exact locators are
`Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`,
`Wts.lamN`, `lamTrue`, and `nuW`, lines 462–469; and
`Formalism/LocalToGlobal/Columns/BaseLemmas.lean`,
`lamTrue_old`, lines 496–510, `lamTrue_new`, lines 512–530, and
`nuW_eq_true`, lines 542–552. These source identities are used as
settled equalities, rather than replaced by freely chosen weights.

The \(\nu_j\) are actual nonnegative partitions, as proved in
§3 below. The Schur summand indexed by \(\nu_j\) in (DO25.3)
has source type

\[
 \det_a^{e_j-b/2}\otimes S_{\nu_j}((\mathbf C^a)^*),
 \tag{DO25.7}
\]

whose highest weight, in decreasing order, is

\[
 \left(e_j-b/2-\nu_{j,a-1},\ldots,
                    e_j-b/2-\nu_{j,0}\right)
               =(-w_{j,a-1},\ldots,-w_{j,0}).
 \tag{DO25.8}
\]

This is precisely the contragredient required by (DO25.4).
The target type of the same Schur summand is

\[
 \det_b^{-e_j+a/2}\otimes S_{\nu_j}(\mathbf C^b).
 \tag{DO25.9}
\]

Its highest weight consists of \(-e_j+a/2+\nu_{j,i}\)
for the first \(a\) entries and \(-e_j+a/2\) on the final
\(d\) entries. Substitution of (DO25.5) gives exactly
(DO25.6). Therefore every selected adjacent pair is a matching local
compact theta type with the **same prescribed character on both
members of the edge**.

The Schur summand occurs with multiplicity one under the compact
product group. This is the polynomial Cauchy decomposition
\(\operatorname{Sym}(T\otimes S^*)=
\bigoplus_\nu S_\nu(T)\otimes S_\nu(S)^*\). The primary
oscillator reference is Konno and Konno (2007), §5.1, Fact 5.1,
Lemma 5.2, the highest vectors (5.4)–(5.5), and Lemma 5.3,
printed pp.72–74, with the character convention fixed in AM-DO-023.
Since \(b>a\), every partition of length at most \(a\)
appearing above is permitted. Its total homogeneous degree is
\(|\nu_j|\). No determinant twist external to the selected
source data has been introduced.

This is a representation-theoretic occurrence statement. An
equivariant global theta map can still vanish on an occurring local
type; the computation does not assert otherwise.

## 3. Exact recurrence and gap consequences

Define

\[
       \Delta_j=e_{j+1}-e_j-d\qquad(0\le j<m-1).
 \tag{DO25.10}
\]

Then the selected polynomial partitions satisfy the exact recurrence

\[
 \boxed{\nu_{j+1}
       =(\nu_j+\Delta_j\mathbf1_{N_j},\,
                         \Delta_j\mathbf1_d).}
 \tag{DO25.11}
\]

Moreover

\[
                  \nu_{0,k-1}\ge1,\qquad \Delta_j\ge2.
 \tag{DO25.12}
\]

In particular all displayed weights \(\nu_j\) are nonnegative
partitions, with strictly positive final entry.

**Proof.** Apply (DO25.5) at \(j+1\), and insert (DO25.6).
For an old entry the change from \(\nu_{j,i}\) is

\[
 -\frac d2+e_{j+1}-\frac{N_{j+2}}2-e_j
                                      +\frac{N_{j+1}}2
      =e_{j+1}-e_j-d=\Delta_j.
\]

For a new entry, its value is
\(-e_j+N_j/2+e_{j+1}-N_{j+2}/2=\Delta_j\).
This proves (DO25.11).

The two gaps in (DO25.2) add to
\(e_{j+1}-e_j\ge d+2\), so \(\Delta_j\ge2\).
At stage zero the source weight is
\(w_{0,i}=u_i-\rho_k(i)\), where
\(\rho_k(i)=(k-1)/2-i\). This is `lamN_eq` and
`lamTrue_zero` in `BaseLemmas.lean`, together with `rhoVec` in
`DataCoeff.lean`, line 39. Hence

\[
 \nu_{0,k-1}=u_{k-1}+e_0-\frac{d+1}{2}.
 \tag{DO25.13}
\]

Because \(u_{k-1}\) is a half-integer, \(b_0\) is an
integer, and \(u_{k-1}>-b_0\), one has
\(u_{k-1}+b_0\ge1/2\). Adding
\(e_0-b_0\ge(d+2)/2\) proves (DO25.13) is at least one.
The starting weight is dominant, so all its entries are at least
one. Recurrence (DO25.11) adds a nonnegative constant to every old
entry and appends entries no greater than those old entries, proving
dominance and positivity inductively. All entries are integers by
the parity and integrality conditions. This proves (DO25.12) and the
partition assertion. \(\square\)

## 4. Exact degree evolution and its sharp rank-only lower bound

Let \(D_j=|\nu_j|\), the homogeneous degree at edge
\(j\to j+1\) for this embedding. Then

\[
 \boxed{D_0=\sum_{i=0}^{k-1}u_i
                   +k e_0-\frac{k(k+d)}2,\qquad
        D_{j+1}=D_j+N_{j+1}\Delta_j.}
 \tag{DO25.14}
\]

Therefore

\[
 \boxed{D_j\ge k(2j+1)+d\,j(j+1)}
 \tag{DO25.15}
\]

and across the \(m\) selected edges,

\[
\begin{split}
 \sum_{j=0}^{m-1}D_j
   &=mD_0+\sum_{r=0}^{m-2}(m-1-r)N_{r+1}\Delta_r,\\
 \sum_{j=0}^{m-1}D_j
   &\ge k m^2+\frac d3(m^3-m).
\end{split}
 \tag{DO25.16}
\]

**Proof.** Summing (DO25.5) at \(j=0\), the entries of
\(\rho_k\) sum to zero, giving the first equality in
(DO25.14). Summing (DO25.11) gives the second. Since
\(D_0\ge k\), \(\Delta_r\ge2\), and
\(\sum_{\ell=1}^{j}N_\ell=jk+d j(j+1)/2\), induction
gives (DO25.15). Summing the exact recurrence counts the increment
at index \(r\) exactly \(m-1-r\) times and gives the first
line of (DO25.16). Finally
\(\sum_{j=0}^{m-1}(2j+1)=m^2\) and
\(\sum_{j=0}^{m-1}j(j+1)=(m^3-m)/3\), proving its second
line. \(\square\)

The lower bounds are attained among the displayed `HCParam`
conditions. Indeed choose the \(u_i\) in decreasing consecutive
half-integers, take \(u_{k-1}=-b_0+1/2\), set
\(e_0-b_0=(d+2)/2\), and take both successive gaps in
(DO25.2) equal to \((d+2)/2\). The interlacing integer
\(v_i\) is then the unique midpoint between \(u_i\) and
\(u_{i+1}\). These choices have \(\nu_0=\mathbf1_k\)
and \(\Delta_j=2\), and every entry is of the required parity.
The partitions become

\[
 \nu_j=((2j+1)^k,(2j)^d,(2j-2)^d,\ldots,2^d),
 \tag{DO25.17}
\]

where exponents denote repeated parts and the last list is empty for
\(j=0\). The source's further `Hyp3` noncompact-gap conditions
may force larger spacings. The sharpness statement here concerns
the stated `HCParam` constraints, not a claimed sharp construction
for all of `Hyp3`.

The degree in (DO25.14) is the degree of the selected Schur summand,
not an arbitrary direction used to illustrate a formal-group slope.
It is a usable exact input to subsequent derivative, norm, and
denominator estimates. It does not itself measure a net arithmetic
gain: the finite family, integral row lattice, normalization periods,
class masses, and terminal detector remain to be inserted. On the
\(E'\) realization, the dyadic eigenbasis change from AM-DO-022
still has index \(2^3\) and degree-\(D\) denominator bound
\(2^D\); no type calculation removes that basis cost.

## 5. Exact source locators and retained gates

All paths below are relative to the recovered source root
`work/research/alpoge_source`.

| Statement used | Exact source |
|---|---|
| Ranks and gap hypotheses | `Formalism/LocalRingCardinality/Params.lean`, `Ranks.N`, lines 35–36; `HCParam`, lines 50–69; `sExp`, `sExp'`, `wG`, lines 71–75 |
| Compact Harish–Chandra parameter | `Formalism/LocalRingCardinality/DataTheta.lean`, `TPar.Xpar`, lines 545–548 |
| Character infinity type | `DataTheta.lean`, `ThetaX.chrOf_inf`; `Development/AbelianVarietyTheory/Definitions/LatticeFrames/ChainParSucc.lean`, `Com.Is.exp`, line 40 |
| Coefficient definitions | `Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`, `Wts.lamTrue`, `Wts.nuW`, lines 464–469 |
| Exact selected recurrence | `Formalism/LocalToGlobal/Columns/BaseLemmas.lean`, `lamTrue_old`, `lamTrue_new`, `nuW_eq_true`, lines 496–552 |
| Bilinear upward kernel | `Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`, `liftT_apply`, lines 160–167 |
| Equal characters on the definite edge | `Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean`, `PinX.mv`, lines 100–101, and `PinColT.om`, line 110 |
| Integral polynomial convention | `Formalism/LocalRingCardinality/DataCoeff.lean`, `rhoVec`, `hcToWeightQ`, `DomWeight.dual`, and the Weyl-module definitions |

No Lean compilation is claimed. The source equality bodies cited in
§2 were directly read; the new assertions are the complete
oscillator/type identification, explicit partition recurrence, and
degree formulas proved above. Membership of the desired arithmetic
row in the **global** iterated image, the six actual `AdmS` statements,
and the `MainX` terminal equation remain distinct obligations.

Primary reference: Konno, T., & Konno, K. (2007). On doubling
construction for real unitary dual pairs. *Kyushu Journal of
Mathematics, 61*(1), 35–82. https://doi.org/10.2206/kyushujm.61.35
