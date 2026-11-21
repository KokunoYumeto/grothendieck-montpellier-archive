# Named generators and the exact canonical-positivity comparison gate

Date: 2026-11-21 UTC. Author: /root/gct_statements, GPT-6 Astra Pro; inherited reasoning effort is not separately exposed. This report records a full-context primary-source audit and new elementary implications. It does not claim to prove the source conjectures or to refute their signed/factored statements.

## 1. Conclusion

**The attached IV and VIII do not assert that all named P_i or Q_i have coefficientwise nonnegative Laurent action matrices in their designated canonical cell bases.** The words positive and negative applied to the generators refer to the two spectral projection operators before rescaling. VIII's right-algebra positivity conjecture explicitly allows an overall sign and a power of a difference of opposite powers of the parameter. Its own rank-three example prints negative multiplication constants. IV's tensor-basis conjecture imposes crystal, cellular, and specialization compatibility, while its examples and discussion explicitly retain signed/factored coefficients.

F57 and F58 therefore exclude specified additional strict-effectivity packages. They are not refutations of those published conjectures. The exact additional premise can be stated either at the action level or as a stronger based-algebra package; §5 proves the implication without hiding a generator-membership assumption.

In this report v is our Laurent variable. The original VIII source uses q on the coordinate side and q^(1/2) on the dual-algebra side. A change to our v must be stated before an arithmetic grading assignment is made. Arithmetic field size is a separate prime power, not the source's parameter merely renamed.

## 2. Primary source/version and exact locator table

All source files are supplied under the following directories:

- IV: LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex, matching arXiv cs/0703110v4, 6 June 2013.
- VII: LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/main.tex, matching arXiv 0709.0749v2.
- VIII: LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex, matching arXiv 0709.0751v2, 1 September 2008.

IV is a later revision than the IV used in VII/VIII. Its cellular algebra basis and VIII's conjecturally constructed bases should not be identified without an explicit comparison.

| Primary locator | Exact role and scope |
|---|---|
| IV, Definition 5.3, §5.3, p. 29; label d upper based, source 2138–2151 | An upper based ordinary quantum-group module has weight-compatible basis, integral stability, bar compatibility, and a crystal basis at infinity. These axioms do not state unsigned action coefficients for the nonstandard right generators. |
| IV, Definition 13.2, §13.5, p. 73; source 4472–4479 | The extension to U_q^tau explicitly permits tau(b) in ±B. This definition concerns the ordinary left quantum-group action, not a based-module theory for the nonstandard Schur algebra. |
| IV, Conjecture 19.1, pp. 130–131; label cj canonical basis X^r, source 7920–7967; following discussion source 7973–7980 | The two-row tensor basis must be an upper based U_q^tau-module and have the specified generic cells, specialized quasi-cells, and fat-cell subquotients. There is no requirement that every P_i or Q_i matrix have nonnegative Laurent coefficients. The following discussion says that a based-module theory for the nonstandard Schur algebra would be an additional strengthening. |
| IV, Remark 11.19, p. 67; source 4181–4195 | The source describes positivity only after extracting powers of v-v^-1 and allowing all coefficients of either sign. It expressly says a weak positivity property cannot in general be strengthened in the discussed setting. |
| IV, Example 19.3, pp. 133–135; label ex ns Schur-Weyl duality canonical basis r4; source 8083–8095; Figures 21–22, p. 135 | The displayed Q_i coefficients belong to one-half the integer span of delta, D, D-2, and c0=D-4. Integer span means signed coefficients. The actual cross-edge c0=(v-v^-1)^2 is nonzero generically and zero at v=1. The explicit basis satisfies Conjecture 19.1 while exhibiting this behavior. |
| VIII, opening of §3, p. 18; label scanonicalB, source 1274–1289 | P_i and Q_i are rescaled positive and negative spectral generators chosen to belong to the ambient integral form. The K_Q-form is generated ring-theoretically by them. Ring generation includes subtraction; it is not generation of an effective cone. |
| VIII, Conjectures 3.1–3.2, §3.3, pp. 21–23; labels cunimindegright and cunimindegright2 | The designated E(r) and Eopp(r) are defined by a minimum-degree lift/globalization procedure. The statements do not identify every P_i or Q_i with a basis element or a nonnegative Laurent combination of basis elements. The text immediately notes that nonstandard basis elements need not have the familiar single-leading-monomial form. |
| VIII, Conjecture 3.3, §3.4.1, p. 23; label ccelldecompright | Cells of E(r) and Eopp(r) are conjectured to yield irreducible left/right modules. This is a cell realization, not a positivity assertion for arbitrary named elements acting on the cells. |
| VIII, Conjecture 3.4, §3.5, p. 24; label cposkroneckerright; external expansion equation (13), label eqexpincanZright | Each multiplicative/comultiplicative constant and external canonical expansion coefficient is allowed to be ±(q^(1/2)-q^(-1/2))^a f(q), with a nonnegative integer and f bar invariant, coefficientwise nonnegative rational, and unimodal. The same statement applies to Eopp(r). |
| VIII, Conjecture 3.7, §3.5.2, pp. 25–26; label coppquasicell; equation (15), label eqmult1 | Specialized quasi-subcells use precisely the terms with vanishing-factor exponent zero. Terms with positive exponent may disappear at q=1. Thus the specialization mechanism explicitly permits the changing zero-pattern that strict unsigned Laurent action would forbid. |
| VIII, Conjecture 2.7, §2.4.2, p. 15; label cposkroneckerleft; equation (9), label eqyincanZ | External coefficients of CB(A_r^H) in the specified tensor basis CB(Z) are conjectured nonnegative rational polynomials. Its multiplication/comultiplication constants still have signs and vanishing factors. This is the coordinate/Schur side, not the named generators of the commuting right algebra B_r^H. |
| VIII, §5.1.2, p. 29, and Figure 2, p. 34; label fmultkron2 | The experimental rank-three constants explicitly include negative signed/factored polynomials. They are presented as confirming Conjecture 3.4, not as exceptions to it. |

The printed section numbering in VIII has §3.5 for Kronecker positivity, followed by §§3.5.1–3.5.2 for the subsequent topics. That numbering is retained rather than regularized silently.

## 3. The generator terminology is spectral, not an effective-basis assertion

VII §5, label sbr, source 906–923, defines p_(X,i)^(+,H) and p_(X,i)^(-,H) by their actions as the positive and negative spectral projection operators in equation (4), label eqide. The nonstandard algebra is generated by either set. Its Kronecker example in §7.2, source 2040–2054, calls the rescaled versions P_i and Q_i. VIII §3 then chooses the rescaling so that the elements lie in the ambient integral form.

These facts assert named algebra elements, spectral projections before rescaling, and integral-form membership. They do not assert that those elements are classes of effective objects in the unknown canonical category. A projection can have negative entries in a specified basis; integral membership likewise imposes no order condition on its coefficients.

For the present Kronecker normalization in IV, P_i+Q_i=D with D=(v+v^-1)^2. Passing from P_i to Q_i subtracts an operator from the scalar D. A positive P_i realization therefore does not automatically make Q_i effective, or conversely. The additional full-algebra summand N# in F57 is what converts the displayed Q-word on N into an actual P-word obstruction. That conversion is already proved using the source's Theta-op contragredient; it is not supplied just by replacing P with Q informally.

The signs in IV §11.1's preliminary Hecke-generator formulas have a known parameter-exponent inconsistency with §3.1. The F57/F58 conclusions use the explicit named P+Q=D normalization, the source's matrices, and the stated contragredient rule, not an uncorrected literal combination of those preliminary formulas.

## 4. A concrete printed coefficient demonstrates the signed scope

VIII Figure 2, p. 34, prints

\[
 c(\gamma_2^1,\gamma_1^1;\gamma_{21}^1)
             =-\frac{(q^2+q+1)(q-1)^2}{q^2}.                       \tag{G1}
\]

For real q>0, q≠1, this is negative. It is nevertheless of the required form. Writing v=q^(1/2),

\[
 -\frac{(q^2+q+1)(q-1)^2}{q^2}
       =-(v-v^{-1})^2(v^2+1+v^{-2}).                               \tag{G2}
\]

The normalized factor v^2+1+v^-2 has nonnegative coefficients and is bar invariant; it is q+1+q^-1 in the original variable. The source presents these constants as satisfying its positive/unimodal convention. No separate claim about how to insert zero coefficients between the two half-parameter parity classes is needed here. The negative sign alone shows that a statement making every raw multiplication constant nonnegative would misstate the very example the paper cites as evidence for Conjecture 3.4. We have reread the whole surrounding positivity subsection and the figure, not just extracted this sign.

This is a source-reading observation, not a new computation of the full rank-three canonical multiplication table. The table was computed in the source; our independent check of (G2) is elementary algebra only.

The signed/factored class is not closed under addition. Both 1 and -(v-v^-1)^2 belong to it, but their sum 3-v^2-v^-2 does not: its value at v=1 is 1, which rules out a positive vanishing-factor exponent, while its mixed coefficient signs rule out either overall sign with exponent zero. Thus a property of individual canonical multiplication constants cannot be promoted to that same property for every named-word trace. The actual F57 trace likewise has value 4096 at v=1 and mixed coefficient signs with either overall sign, but it is not an individual constant covered by Conjecture 3.4. This is why its failure of the signed/factored form would not itself refute that conjecture.

Conjecture 2.7 has a genuinely unsigned clause, but its scope is different. It concerns expansions of chosen elements of the nonstandard Schur algebra A_r^H in an externally fixed tensor basis of End(X^tensor r). The named P_i belong to the commuting right algebra B_r^H. No source statement identifies all those P_i with the canonical Schur elements in that clause. Nor does a positive external expansion imply that changing back to an internal basis preserves coefficientwise positivity. The source itself still gives signed/factored internal structure constants.

## 5. Exact additional axiom that would imply the F57 hypothesis

Here is a precise KL-style strengthening, stated independently of the source.

Let R=Q[v,v^-1] and R_+=Q_(>=0)[v,v^-1]. Let A be an R-algebra free on a finite basis C. Suppose:

1. Every product cc', with c,c' in C, has coefficients in R_+ in the C basis.
2. Every named P_i lies in the effective cone R_+ C.
3. The specified module M is a coordinate cellular subquotient of the regular module with its C basis: it is obtained from spans of basis subsets which are stable under the action, with the quotient basis given by the surviving C elements.

Then every P_i action matrix on M has entries in R_+.

**Proof.** Write P_i=sum_c h_(i,c)c with h_(i,c) in R_+. Multiplication by each c has nonnegative C coefficients by assumption 1; multiplication by P_i is their R_+-linear combination, hence has nonnegative entries. Restriction to a coordinate stable submodule and projection to a coordinate quotient retain the corresponding entries without subtraction. The induced matrix on M remains entrywise in R_+. This proves the claim.

Assumptions 1 and 2 are separate. Positivity of basis multiplication does not say an arbitrary algebra element is effective. Conversely effectiveness of the generators does not make products of basis elements positive. The minimal necessary added action premise is simply

\[
                     P_i C_M\subseteq R_+ C_M                     \tag{G3}
\]

for the designated cell basis C_M; the stronger package above is one sufficient way to prove it.

If the cell realization covers every generic simple of the actual full rank-four algebra, as a strengthened version of VIII Conjecture 3.3 would, it includes the actual N# of F57. Then (G3) would force its P-word trace into R_+. The negative coefficient proved in F57 is a contradiction. Therefore that complete strict package cannot hold for the actual full rank-four algebra and the named P_i. This is independent of which alternative basis of N# is proposed.

The same conclusion applies to a finite graded semisimple kernel/module-category model whose effective generator objects decompose into nonnegative graded multiplicities on those designated simple states. It does not apply to Euler classes of complexes, signed/factored normalizations, or an effective model of a larger module whose projector onto N# is not effective. Effectivity of that projector is an independent premise, explicitly retained in F57.

## 6. Exact additional axiom that would imply the F58 hypothesis

For the two-row tensor module, retain IV Conjecture 19.1(ii)–(iii), including its coordinate cellular meaning from §2.4, and add the assertion that all named P_i, or all named Q_i, have entries in R_+ in that regular basis.

F58 then applies directly. A nonzero nonnegative Laurent polynomial cannot vanish at the positive point v=1; therefore the graph of nonzero named-generator entries, and its strongly connected cells, cannot change there. Yet the actual six-dimensional generic simple in Figure 21 has a specified proper three-dimensional coordinate cellular submodule after specialization. The two required quasi-cells are a genuine refinement. Thus the conjunction is impossible.

This is a contradiction to the added unsigned action axiom together with the exact cell-refinement premise, not to IV Conjecture 19.1 alone. IV's displayed c0 cross-edge illustrates how its permitted signed/factored coefficients solve this particular zero-pattern requirement.

VIII Conjecture 3.7 builds the same type of allowed disappearance directly into equation (15): nonzero structural coefficients with positive exponent delta vanish at q=1, and quasi-subcells use the delta=0 terms. Its basis is Eopp, not automatically the revised IV tensor basis. A comparison identifying these particular bases and their cellular subquotients would be another hypothesis; it is unnecessary for the direct IV/F58 application.

## 7. Normalization boundaries, with short proofs

### 7.1. Positive Laurent rescaling of named generators does not remove F57

Suppose each actual generator is replaced by

\[
                 P_i'=\epsilon_i h_i(v)P_i,
 \qquad\epsilon_i\in\{1,-1\},\quad
       0\ne h_i\in\mathbb Q_{\ge0}[v,v^{-1}].
\]

For the F57 word, its new trace is epsilon H(v)p((v+v^-1)^2), where H is the product of the h_i with the word multiplicities, hence nonzero and coefficientwise nonnegative. If epsilon=+1, the highest Laurent coefficient is negative: the highest coefficient of p is -1 and that of H is positive. If epsilon=-1, evaluation at v=1 is -4096 H(1)<0, so the Laurent polynomial has a negative coefficient. Thus these generator rescalings and sign choices cannot produce a strict positive Laurent action on this specified summand. No assertion is made for division by arbitrary non-Laurent factors or for changing the module/action comparison.

### 7.2. Removing the vanishing factor is not a regular normalization of the same fiber

In the local ring R_1=Q[v,v^-1]_(v-1), v-v^-1 has positive valuation and is not a unit. Inverting it removes the v=1 specialization: no ring map from that localization to Q can send v to 1, since an invertible element would be sent to zero. In the Figure 21 coordinate basis, diagonal changes by units of R_1 preserve the order-two vanishing of the c0 edge, because the new entry differs by a ratio of units. General basis mixing must be checked against the coordinate-submodule premise; if it preserves the designated coordinate submodule, F58 still applies.

Accordingly, stripping a factor coefficient by coefficient is not by itself a construction of a basis change, a functor, or coherent relation maps preserving the specified specialization fiber. A signed/factored geometric interpretation could still supply such operations by mixed or nonproper geometry; no nonexistence theorem for that broader task is asserted.

### 7.3. Purity concerns the translated raw coefficient, not just its stripped factor

The separately proved F57 pure-point criterion says that f(v) can be the Euler trace of a point complex pure of one weight w under v=q_arithmetic^(n/2) precisely when (-1)^w f(-v) is effective. Any nonzero polynomial divisible by v-v^-1 fails that test because f(-1)=0, while the effective polynomial would have positive total dimension at v=1. Thus the raw nonzero factors allowed in the published conjecture cannot all be interpreted as single-pure-weight point-complex traces under that variable rule. This is a comparison restriction, not a failure of the conjectured positivity of the stripped f.

The explicit geometric repair of c0 is the mixed point complex RΓ_c(G_m²,Q_ell(1)); its coefficient sheaf is pure before the nonproper compact pushforward. This demonstrates why the bridge must specify where purity is imposed. A pure coefficient sheaf on a source, a pure point complex, a positive graded dimension, and an inserted correspondence trace are four different claims.

## 8. What remains open after these deductions

F57 does not settle the P-only strict-kernel problem for the two-row quotient in a basis unconstrained by the source's specialization cells. F58 settles its conjunction with the specified cell-refinement requirements, and permits alternative mixed/factored realizations. Neither result computes VIII's entire designated canonical basis, proves or disproves its normalized positivity or unimodality, or constructs the required effective labels in general.

The direct source comparison gate is now explicit: a proposed geometric realization must identify the designated basis and specify which named elements are effective, which operations produce the signed vanishing factors, and how the specialization filtration is retained. If it claims strict generator effectivity or pure raw point coefficients, the preceding proved tests apply. If it only claims normalized positivity, those extra axioms cannot be silently imported from the classical KL example.

## 9. Verification and primary links

Actual checks in this report:

- Full source context read: IV Definitions 5.3 and 13.2; all six clauses and following discussion of Conjecture 19.1; Remark 11.19; Example 19.3 coefficient paragraph and Figure 21 description.
- Full source context read: VIII §3 generator definition, minimum-degree globalization and its limitations, Conjectures 3.3–3.4 and 3.7 with equation (15), §5.1.2 and Figure 2; also the complete Conjecture 2.7 and the definition of its external basis at equation (9).
- Primary PDF numbering check: VIII arXiv 0709.0751v2, exact displayed statements and Figure 2; IV local primary PDF text for Definitions 5.3/13.2 and prior independently rendered/source-matched Figure 21/22 checks.
- New elementary proof checks: effective-algebra-to-cell-action implication, normalization invariance of the negative trace, local-ring valuation and specialization statement, and the purity normalization corollary.
- Not newly recomputed: the full VIII rank-three multiplication table. Equation (G1) is a precisely located published computation, and only its factorization and implications are independently checked here.

Primary URLs:

- https://arxiv.org/pdf/cs/0703110
- https://arxiv.org/pdf/0709.0751
- https://arxiv.org/pdf/0709.0749

Web retrievals used for numbered matching (parent must open before citing them in user-facing web citations): VIII master turn459325043view0; exact Conjecture 3.4/3.7 turn337158977view0 and turn337158977view3; generators turn337158977view2; complete Conjecture 2.7 turn804100306view0; Figure 2 turn804100306view1. Most substantive reading was from the supplied LaTeX, not search snippets.
