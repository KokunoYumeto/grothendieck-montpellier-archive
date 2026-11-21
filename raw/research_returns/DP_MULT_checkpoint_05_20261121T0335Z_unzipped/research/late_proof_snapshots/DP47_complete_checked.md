# DP47 — the actual hyperbolic Poincaré pullback and the source's trace-one endomorphism

Date: 2026-11-21 UTC. Researcher: GPT-6 Astra Pro; effort is not exposed. This memo proves a local geometric identification. It does not instantiate a new global mixed-CM theta family or identify every selected harmonic jet with an ordinary one-variable derivative. The explicit hypotheses distinguish an actual integral polarized block from an arbitrary guessed scalar kernel.

## 1. The statement

Let \(R=W(k)\), where \(k\) is perfect and contains \(\mathbf F_{p^h}\), and let \(K=\operatorname{Frac}R\). Let \(G\) be either the Honda/Lubin–Tate model of DP37–DP41 with \(h\ge2\), or any actual arbitrary-unit singleton cyclic display model of DP46 with \(h\ge3\); put \(H=G^D\). Use its integral Teichmüller coordinates and invariant primitive Poincaré frame. The second case is a genuine extension of the statement, not an assumption that its unit arrows can be made one. Put \(B=\exp b\), where \(b\) is the unique invariant rational logarithmic splitting. Thus the two addition factors

\[
C_G(x,x';y)=\frac{B(x+_Gx',y)}{B(x,y)B(x',y)},\qquad
C_H(x;y,y')=\frac{B(x,y+_Hy')}{B(x,y)B(x,y')}
\tag{HP1}
\]

are normalized integral units. The coordinates need not make \(B\) integral.

Let \(A=G\times H\). Suppose its actual integral symmetric biextension is identified, compatibly with axial rigidifications, with the hyperbolic evaluation biextension

\[
\mathcal P_{\mathrm{hyp}}\bigl((x,y),(x',y')\bigr)
=\mathcal P(x,y')\otimes\mathcal P(x',y).
\tag{HP2}
\]

Suppose the commutative CM endomorphism ring preserves this decomposition, and its involution is the adjoint involution for (HP2). Let \(w_0+\overline{w_0}=1\). In these coordinates this means

\[
w_0=(a,(1-a)^D)
\tag{HP3}
\]

for an integral endomorphism \(a\) of \(G\) commuting with its Teichmüller action. The dual superscript denotes the actual Cartier-dual endomorphism, not an independently chosen scalar.

Adopt the source's convention

\[
\mathrm{ph}_1=\exp\bigl(h(z,z'')+h(z',z'')-h(z+z',z'')\bigr),
\tag{HP4}
\]

and identify its geometric addition factors with the \(C\)'s in (HP1). In the product frame a canonical gauge is

\[
h_0\bigl((x,y),(x',y')\bigr)
=-b(x,y')-b(x',y).
\tag{HP5}
\]

Then there is a normalized integral unit \(U_0\in R[[x,y]]^\times\) such that

\[
\exp\bigl(h_0(z,w_0z)\bigr)=U_0(x,y)\,B(x,y)^{-1}.
\tag{HP6}
\]

The coefficient of the primitive logarithm is exactly \(-1\), independently of \(a\). If one identifies the geometric biextension using the inverse convention, both signs reverse coherently; this changes the coefficient to \(+1\), not to a possibly nonunit difference of eigenvalues.

For any other source canonical gauge \(h\) of the same integral biextension, and in any normalized integral frame, there are an integral normalized unit \(U\) and a homogeneous quadratic form \(Q\) over \(K\) in the additive logarithm coordinates \(z_{\log}=(\log_Gx,\log_Hy)\) such that

\[
\exp\bigl(h(z,w_0z)\bigr)
=U(x,y)\,B(x,y)^{-1}\exp Q(z_{\log}).
\tag{HP7}
\]

Thus the exact local source expression \(f\exp(\kappa h_L)\), with an integral algebraic section germ \(f\) and an integer tensor power \(\kappa\ge0\), becomes

\[
\widetilde f(x,y)\,B(x,y)^{-\kappa}
  \exp\bigl(\kappa Q(z_{\log})\bigr),\qquad
\widetilde f=fU^\kappa\in R[[x,y]].
\tag{HP8}
\]

Here \(\kappa\) is a theta tensor power, not the number of lifts. For the unit-coefficient case of DP42 one requires \(p\nmid\kappa\).

## 2. Actual adjunction gives an integral unit

For an integral endomorphism \(a\) of \(G\), the universal Poincaré pairing has its canonical integral adjunction isomorphism

\[
(a\times1)^*\mathcal P\simeq(1\times a^D)^*\mathcal P.
\tag{HP9}
\]

This is the defining functoriality of the actual dual pairing: it preserves the biextension laws and the axial rigidifications. In an integral frame its scalar is a normalized integral unit. Consequently the ratio of the two rational bilinear sections, after applying (HP9), is a rational bihomomorphism \(G_K\times H_K\to\widehat{\mathbf G}_{m,K}\). Its logarithm is therefore a bilinear form in the additive logarithm coordinates.

Here that bilinear form vanishes. The invariant primitive frame carries the actual action

\[
(x,y_1,\ldots,y_{h-1})
\longmapsto
(\zeta x,\zeta^{-p}y_1,\ldots,\zeta^{-p^{h-1}}y_{h-1}),
\quad \zeta^{p^h-1}=1.
\tag{HP10}
\]

The Poincaré adjunction (HP9) is natural, and \(a\) commutes with this action, so its scalar in the invariant frame is invariant. Both pulled-back \(b\)'s are invariant as well. A logarithmic bilinear monomial \(X Y_i\) has character \(\zeta^{1-p^i}\). For \(1\le i<h\), the integer \(p^i-1\) is positive and strictly smaller than \(p^h-1\); no such character is trivial. Hence an invariant bilinear form is zero.

This proves the exact assertion

\[
J_a(x,y):=\frac{B(ax,y)}{B(x,a^Dy)}
\in R[[x,y]]^\times,\qquad
J_a(0,y)=J_a(x,0)=1.
\tag{HP11}
\]

No nonintegral exponentiation of an integral unit has been used. The unit is the scalar of an actual integral isomorphism. The absence of invariant bilinear terms identifies its rational splitting with the specific \(B\) of DP41 or DP46, rather than with \(B\) multiplied by an unspecified bilinear exponential.

For completeness, the characteristic-zero bilinearity claim is elementary. In additive logarithm coordinates, a formal power series additive in the first set of variables has only terms linear in those variables, by comparing the binomial coefficients in its additivity identity. Applying the same argument to the second set makes it bilinear. A normalized multiplicative bihomomorphism has an additive logarithm because formal logarithm converts products into sums.

## 3. The trace-one identity yields exactly one primitive factor

Set \(c=1-a\). Cartier duality is additive, so

\[
a^Dy+_Hc^Dy=y.
\]

By (HP1) and (HP11),

\[
\begin{aligned}
B(x,c^Dy)B(ax,y)
&=J_a(x,y)\,B(x,c^Dy)B(x,a^Dy)\\
&=J_a(x,y)\,
C_H(x;a^Dy,c^Dy)^{-1}B(x,y).
\end{aligned}
\tag{HP12}
\]

Every substitution in the \(C_H\) factor is an integral formal endomorphism, so its value and its inverse are integral normalized units. Define

\[
V_a=J_a\,C_H(x;a^Dy,c^Dy)^{-1}.
\]

Equation (HP5), pulled back by \(z\mapsto(z,w_0z)\), is the negative logarithm of the left side of (HP12). Thus (HP6) follows with \(U_0=V_a^{-1}\). The trace-one condition adds the two contributions to a single primitive Poincaré factor; there is no cancellation involving a factor \(a-c\).

This also verifies the source's adjoint compatibility for the product gauge (HP5). Each CM endomorphism acts on \(A\) as a pair of commuting integral endomorphisms, and its adjoint interchanges their Cartier duals. The difference between the two pulled-back gauges has exponential given by a product of the integral adjunction units (HP11), exactly the adjunction scalar of the hyperbolic biextension. Its two addition laws follow from (HP1); its symmetry is literal; its axial restrictions vanish. Therefore \(h_0\) is a canonical gauge for the geometric product frame, with the stated source sign convention.

## 4. Why the remaining gauge term is quadratic

First identify the integral frames and their cocycles. Let \(h\) and \(h_0\) be canonical gauges for this same frame. Dividing their exponential addition identities and using injectivity of formal exponential over \(K\) shows that \(h-h_0\) is additive in each argument. Its axes vanish. Thus in the additive logarithm coordinates it is a bilinear form \(L(Z,Z')\). The symmetry and adjoint identities give the corresponding symmetry and adjoint balance, although bilinearity alone suffices here.

An endomorphism becomes its tangent linear map in logarithm coordinates, so

\[
(h-h_0)(z,w_0z)=L(Z,dw_0\,Z)
\]

is a homogeneous quadratic form. Combining this with (HP6) proves (HP7) in the product frame.

A change between two normalized integral frames is multiplication by an integral normalized unit. A rational logarithmic splitting changes by the logarithm of that unit with the appropriate sign, so after pullback its exponential contributes another integral normalized unit. Only after this adjustment is the remaining difference asserted to be bilinear. The pullback is integral because \(w_0\) is integral. This proves (HP7) in an arbitrary such integral frame. Finally the tensor power in (HP8) is an ordinary nonnegative integer, so \(U^\kappa\) is integral. This completes the proof of DP47. \(\square\)

## 5. When the hyperbolic hypothesis is actual geometry

The hypothesis (HP2) is automatic for an integral polarized CM formal block satisfying the following explicit conditions:

1. The \(p\)-adic CM algebra has two conjugate integral idempotent factors \(e,\bar e\), and the formal block is \(A=eA\oplus\bar eA=G\oplus H\).
2. The polarization is prime to \(p\) on this block, so its associated map to the dual block is an isomorphism.
3. Its adjoint involution is CM conjugation.

Here is the direct argument. The polarization pairing is balanced:

\[
\mathcal B(az,z')\simeq\mathcal B(z,\bar a z').
\]

For \(z,z'\in eA\), take \(a=e\). The left side is \(\mathcal B(z,z')\), whereas the right side is \(\mathcal B(z,0)\), canonically trivial by the axial rigidification. The same applies to \(\bar eA\times\bar eA\). Thus the diagonal restrictions are trivial as biextensions, not merely trivial underlying line bundles.

The perfect polarization identifies \(H\) with the actual Cartier dual \(G^D\) through the cross pairing. Its opposite cross restriction is the transpose by the symmetry of the polarization biextension. Biadditivity then identifies the whole block with the product of its two cross restrictions, which is (HP2). All maps and trivializations are integral because the idempotents and the perfect polarization are integral. The trace-one relation gives (HP3) by applying the adjoint identification to the two block components of \(w_0\).

This argument concerns the biextension. At the level of finite torsion, the associated Weil pairing is alternating; this does not introduce a minus sign between the two cross factors in the symmetric biextension (HP2). Its transposition and double-duality conventions are already included in the definition of the polarization pairing.

If the polarization has a \(p\)-power defect on the block, or if the integral idempotent decomposition is unavailable, the unit primitive identification in this argument is not automatic. These hypotheses must not be replaced merely by a Newton-slope count. For a particular CM factor, an actual integral singleton/complement display or an actual integral CM isomorphism is required before transporting numerical radii. DP46 treats every arbitrary-unit singleton/complement display directly, so no trivialization of its unit arrows or finite-unramified twist is required. Once this actual integral normal form is supplied, DP47 removes the additional unknown scalar-kernel identity: the trace-one pullback contains exactly one primitive Poincaré class.

## 6. Consequence for primitive ordinary lines and its exact limit

For \(p\) odd, \(h>2\), \(p\nmid\kappa\), and a primitive mixed additive-logarithm line \(X=ut,\ Y=vt\), with \(u\) a unit and \(v\) primitive, (HP8) becomes

\[
F(t)\exp\bigl(-\kappa\,\beta(ut,vt)+c t^2\bigr),
\tag{HP13}
\]

where \(F(t)=\widetilde f(E_G(ut),E_H(vt))\), \(c\in K\), and \(\beta=b(E_G,E_H)\) is the actual primitive logarithm. The required nonvanishing condition is \(F\ne0\) as a power series. It is not implied by the statement that some algebraic theta section is globally nonzero. Multiplying the algebraic frame by an integral unit preserves this nonvanishing condition.

The primitive part is exactly in DP42's unit-coefficient situation, or in its arbitrary-unit extension DP46. The proof above is unchanged in the arbitrary-unit case: DP46 supplies the same actual torus characters and uniqueness of the invariant splitting, and no displayed argument uses a coefficient of an arrow being one. The effect of the remaining quadratic term is the separate DP48 theorem. In particular one must not silently discard \(c t^2\), assume \(c\) integral, or infer a stronger ordinary-line slope from a choice of canonical gauge. The selected harmonic values can be independent of a quadratic gauge under the source's particular second-order annihilation condition, but that is a different assertion from this ordinary one-variable restriction.

DP47 does not establish the global theta-lift path, nonzero selected minors, costs, or a shorter chain. It identifies the actual local normalized kernel for the specified polarized block, rather than postulating it.

## 7. Precise source comparison and primary references

The recovered author source has the following exact interfaces:

* “ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/CocycleRightZeroThd.lean”: integral FB data and adjunction laws 86–158; IsCanonGauge 174–183; hL 185; nabVal 187–189. In particular 177–180 fix the minus-coboundary sign in (HP4), and 182–183 give adjoint balance.
* “ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/WickVanishing/ExpConjConnectionIntegral.lean”: the actual theorem exp_conj_connection_integral 40–82 assumes **\(w_0+\operatorname{star}(w_0)=1\)** at 40. connection_first_identity 84–90 supplies ConnectionIntegrality. No skew relation \(w_0+\bar w_0=0\) is used.
* “Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/CanonGaugeSubIsBiadd.lean”: canonGauge_sub_isBiadd 16–60 supplies the two addition identities and adjoint balance for gauge differences.
* “Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/CanonGaugeIndependenceAll.lean”: gaugeExp_holds 19–21 and canonGauge_independence_all 23–26 supply the corresponding gauge/selected-column theorems under their stated conditions.
* “Formalism/SharpRestriction/Divisibility/GeneratorPowers/ExpTieAlg.lean”: nabVal_eq_const 413–419 identifies the invariant derivative expression. “ExpTiePf.lean”: tie_holds begins at 328 and explicitly constructs \(f\exp(\kappa h_L)\) at 333.

The actual display Poincaré pairing and its functoriality are the pairing of a display with its dual, not an arbitrary exponential: Zink, “The display of a formal \(p\)-divisible group”, Astérisque **278** (2002), §4.3, (216)–(220), and §4.4, Proposition 121, p.241; (243), p.246; Theorem 122, p.247. The explicit primitive coordinates, invariant frame, and \(B\) used here are those derived from this pairing in DP37–DP41 and the arbitrary-unit version DP46. This pass uses that already checked identification and proves the additional pullback identity (HP12).

The current source trace verifies the relevant trace-one hypothesis and gauge identities. It does not assert that the original old-host source contains a mixed genus-three global Datum. The local polarized-block criterion above states exactly when the new identity is geometric.
