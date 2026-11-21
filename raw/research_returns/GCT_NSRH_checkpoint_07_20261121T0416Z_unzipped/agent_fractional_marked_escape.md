# F55: an actual fractional mixed trace model and the all-places gate

Author: /root/rectangular_and_theta. Date: 21 November 2026 UTC.

This note resolves a particular remaining distinction in F54: the unrestricted fractional mixed-weight exception can be realized on the actual tensor module, rather than only by a scalar algebraic function. The constructed operator commutes with the actual right action and retunes both its identity trace and the marked-X trace. It deliberately does not commute with all ordinary left operators. It is regular at one collision place, but has poles at the other place above v=1.

The complementary theorem proves that regularity at every place above v=1 rules out marked-X retuning for arbitrary genuine mixed spectra. That is an additional hypothesis, not a consequence of having an algebraic coefficient scheme. The parent's separate continuous-branch argument is not assumed or reproduced here.

## 1. Actual module and selected coefficient cover

Use the established F21/F43 regular bimodule
\[
 M=(W_3\otimes W_3\oplus W_1\otimes W_1)\otimes\epsilon_+
 \ \oplus\ (W_1\otimes W_1)\otimes\epsilon_-
\]
\[
 \qquad\oplus\ (W_3\otimes W_1\oplus W_1\otimes W_3)\otimes N(\delta)
 \ \oplus\ (W_1\otimes W_1)\otimes N(D-2).
 \tag{E1}
\]
The four right-isotypic multiplicities are 20,4,16,4. Their actual dimensions are 20,4,32,8, totaling 64. The final multiplicity factor is exactly W_1^V tensor W_1^W, of dimension four. The W_1 factors are the sl_2-highest-weight-one factors of the polynomial GL_2 modules of partition (2,1), with their determinant twists retained.

Put
\[
 \delta(v)=v+v^{-1},\quad D(v)=\delta(v)^2,\quad
 \Delta(v)=\frac{(D(v)-1)(D(v)-4)}{D(v)^2}.
 \tag{E2}
\]
The marked element X is the actual regular polynomial expression in P_1,P_2 established in F54 Part3. On (E1) it is zero except on the last rank-eight sector, where it is Delta(v) times the identity. In particular X(1)=0 as an actual matrix on the regular tensor lattice.

Let
\[
 s=\sqrt2>0,\qquad K_0=\mathbb Q(s),\qquad v=t^2,
 \qquad \eta=\Delta(2)=\frac{189}{625}.
 \tag{E3}
\]
The selected base point is t=s, so v=2. The extension points are
\[
 t_n=s^n=2^{n/2},\qquad v_n=2^n\quad(n\ge1).
\]
The chosen collision point is t=-1, lying above v=1. These are points of one fixed algebraic coefficient cover. No unrelated functions or fields are selected separately at successive n.

The regular F21/F43 comparison to the original tensor basis is defined over
\[
 S_0=\mathbb Q[v,v^{-1},\delta(v)^{-1},
                  (D(v)-1)^{-1},(D(v)-2)^{-1}].
\]
All module and operator constructions below are pulled back from that actual comparison. In particular the final rank-eight direct summand is selected by a regular commutant decomposition from F43, not by dividing the algebra element X by Delta at the collision.

## 2. Explicit rational functions

Define
\[
 g(t)=2(1+t)^2,\qquad
 h(t)=\frac{\eta g(t)}{\Delta(t^2)},
 \tag{E4}
\]
\[
 \lambda(t)=\frac{h(t)}2-1-2s,\qquad
 u(t)=1+\frac{g(t)-h(t)}{20}.
 \tag{E5}
\]
The apparent singularity of h at the chosen collision cancels. Indeed
\[
 \Delta(t^2)=
 \frac{(t-1)^2(t+1)^2(t^2+1)^2(t^8+t^4+1)}
      {(t^4+1)^4},
\]
so
\[
 h(t)=
 \frac{2\eta(t^4+1)^4}
      {(t-1)^2(t^2+1)^2(t^8+t^4+1)}.
 \tag{E6}
\]
Thus h,u,lambda are all regular at t=-1. Exact values are
\[
\begin{array}{c|ccc}
t&h(t)&u(t)&\lambda(t)\\ \hline
s&6+4s&1&2\\
-1&126/625&6187/6250&-562/625-2s.
\end{array}
 \tag{E7}
\]
At the remaining small extension point t=2,
\[
 h(2)=\frac{1503378}{203125},\qquad
 \lambda(2)=\frac{548564}{203125}-2s\ne0.
 \tag{E8}
\]
The last inequality follows because the first term is rational and s is irrational.

## 3. One finite localization contains every required point

Let R_0 be the pullback of S_0 to K_0[t,t^-1], further localized at t-1 and t^2+1. Equation (E6) belongs to R_0: t^8+t^4+1 is already a unit because
\[
 D(t^2)-1=(t^8+t^4+1)/t^4.
\]
Set
\[
 R=R_0[u(t)^{-1},\lambda(t)^{-1}].
 \tag{E9}
\]
This is one finite localization of a finite algebraic coefficient cover. We now verify that t=-1 and every t_n are still allowed.

Every factor inherited from S_0 is nonzero at v=1 and at v>1. At t=-1, the two extra factors are -2 and 2; (E7) makes u and lambda nonzero. At t_n>1 the extra factors are also nonzero. At n=1, (E7) gives u=1 and lambda=2. At n=2, (E8) makes lambda nonzero.

For all n>=3, use t_n>=2s and 0<Delta(v_n)<1. Then
\[
 \lambda(t_n)
 =\frac{\eta(1+t_n)^2}{\Delta(v_n)}-1-2s
 >\eta(1+2s)^2-1-2s
 =\frac{1076-494s}{625}>0.
 \tag{E10}
\]
The final inequality follows already from s<2, giving numerator greater than 88.

To check u at every n>1, observe that Delta(v) is strictly increasing for v>1. Indeed D(v) is strictly increasing there and
\[
 \frac{d}{dD}(1-5/D+4/D^2)=\frac{5D-8}{D^3}>0
 \quad(D>4).
\]
Thus Delta(v_n)>eta for n>1. Since g(t_n)>0, (E4) gives h(t_n)<g(t_n), and hence
\[
 u(t_n)>1\qquad(n>1).
 \tag{E11}
\]
This proves all required denominators nonzero, for the collision and every extension point, using a fixed finite localization.

The collision order has not changed: v-1=(t-1)(t+1), and t-1 is a unit at t=-1. Delta(t^2) therefore still vanishes to order exactly two there. The actual coherent center and module are their original pullbacks at this place.

## 4. The actual right-action-compatible automorphism

On (E1), define the R-linear operator F as follows.

- On the full epsilon_+ isotypic block of rank20, F is u(t) times the identity. This includes both W_3 tensor W_3 and W_1 tensor W_1 multiplicity summands of that scalar right type.
- On epsilon_-^4 and N(delta)^16, of total dimension36, F is the identity.
- On the final block (W_1^V tensor W_1^W) tensor N(D-2), use the ordered multiplicity basis
  \[
  g_+\otimes g_+,\quad g_+\otimes g_-,\quad
  g_-\otimes g_+,\quad g_-\otimes g_-,
  \]
  and put
  \[
  F=\operatorname{diag}(1,s,s,\lambda(t))\otimes I_2.
  \tag{E12}
  \]

Every factor is regular over R, and
\[
 \det F=u(t)^{20}(s^2\lambda(t))^2
       =4u(t)^{20}\lambda(t)^2
\]
is a unit. Thus F is an invertible regular operator over the same coefficient base.

This is an operator on the actual tensor lattice. Let iota be the established regular A-linear F43 isomorphism from the original tensor module to (E1); the transported operator is explicitly iota^{-1} F_block iota, with the rightmost map applied first. Both comparison maps are regular over R. The named right generators remain exactly their original matrices under that comparison.

F commutes with the actual right action: on the scalar isotypic blocks it is scalar on the full multiplicity space, and on each N(a) block it acts on the multiplicity factor while the right matrices act on N(a). This can also be read directly from the Kronecker products in (E12). No division by Delta is used in defining F.

This is a right-action comparison, not equality between the actual algebra and the full Frobenius centralizer. Nor is it an invariant-Hom realization forcing conjugation Frobenius on M to be the identity.

## 5. Both identity and marked traces retune exactly

On the final rank-eight sector, (E12) gives
\[
 \operatorname{Tr}(F|_{M_2})=2(1+s+s+\lambda(t))=h(t).
 \tag{E13}
\]
The marked trace is consequently
\[
 \operatorname{Tr}_M(X(t^2)F(t))
      =\Delta(t^2)h(t)=\eta g(t).
 \tag{E14}
\]
The ordinary identity trace is
\[
 \operatorname{Tr}_M F(t)
      =20u(t)+36+h(t)=56+g(t).
 \tag{E15}
\]

At t=s, the full base spectrum is
\[
 1^{\,58},\qquad s^{\,4},\qquad 2^{\,2}.
 \tag{E16}
\]
On the marked sector alone it is 1 with multiplicity2, s with multiplicity4, and 2 with multiplicity2. The eigenvalue of X on that sector is eta. Since s^2=2,
\[
 \operatorname{Tr}(F(s)^n)
      =58+4s^n+2\cdot2^n
      =56+2(1+s^n)^2,
\]
\[
 \operatorname{Tr}(X(2)F(s)^n)
      =\eta(2+4s^n+2\cdot2^n)
      =\eta\,2(1+s^n)^2.
 \tag{E17}
\]
Substituting t=t_n=s^n into (E14)--(E15) therefore proves, for every n>=1,
\[
 \boxed{\operatorname{Tr}F(t_n)=\operatorname{Tr}(F(s)^n),}
\]
\[
 \boxed{\operatorname{Tr}(X(v_n)F(t_n))
                 =\operatorname{Tr}(X(2)F(s)^n).}
 \tag{E18}
\]
Both comparisons use genuine finite-dimensional operators and the actual marked algebra element.

Under the specified normalization v=Q^(1/2), the base is Q=4. The marked base weights are 0,1/2,1, and its radii are distinct. Thus this example lies outside both sufficient hypotheses of F54's actual marked-module obstruction: it is neither common-radius nor integrally mixed in that normalization. It makes no assertion of an ordinary mixed geometric realization with integral Deligne weights.

## 6. Exact failures of the stronger comparisons

### The ordinary left action

The F43 operators satisfy E_V(g_- tensor g_+)=g_+ tensor g_+ on the final multiplicity factor. At the base, (E12) gives
\[
 (F(s)E_V-E_VF(s))(g_-\otimes g_+)
       =(1-s)(g_+\otimes g_+)\ne0.
 \tag{E19}
\]
Tensoring with any nonzero right-factor vector gives the same nonzero commutator on the actual rank-eight sector. Thus the operator does not commute with all named ordinary left operators. The source's row/opposite-composition convention is retained; (E19) is stated as composition of the actual linear operators on vectors.

This is exactly the exception permitted by the F54 both-actions supplement. That supplement proves that commuting with both actual left and right images would force a scalar base operator on this sector and would exclude marked retuning without any weight assumption.

### Fixed generator-word traces

The actual rank-two right blocks have trace Tr(P_1|N(a))=D(v), while the epsilon_+ block has P_1=D(v) and the epsilon_- block has zero. Hence
\[
 \operatorname{Tr}(P_1(v)F(t))
   =D(v)\left(20u(t)+16+\frac{h(t)}2\right)
   =D(v)\left(36+g(t)-\frac{h(t)}2\right).
 \tag{E20}
\]
At the fixed base, for all n,
\[
 \operatorname{Tr}(P_1(2)F(s)^n)
   =D(2)\left(37+2s^n+2^n\right)
   =D(2)\left(36+\frac{g(t_n)}2\right).
 \tag{E21}
\]
For n>1, h(t_n)<g(t_n) and D(v_n)>D(2). The positive expression in (E20) is therefore strictly larger than (E21). The fixed P_1 insertion already fails at every n>1. Multiplying by the respective D factors shows the same strict failure for P_1 squared.

Thus (E18) does not satisfy the two-word composition comparison of F54. Full spectral retuning also fails: u(t_n)>1 for n>1, whereas the corresponding epsilon_+ base eigenvalues have every power equal to one. This failure does not require retaining sector labels: F(s)^n has eigenvalue one with multiplicity exactly 58, while F(t_n) has that eigenvalue with multiplicity at most 40 (the 36 unchanged dimensions, the two fixed marked dimensions, and at most two more if lambda(t_n)=1), since u(t_n)>1 and s>1.

### The other collision place

At t=+1, h has a pole of order two. Its numerator in (E6) is nonzero, and its only vanishing denominator factor there is (t-1)^2. Both u and lambda also have order-two poles, with respective leading terms -h/20 and h/2. These are actual eigenvalue functions. Consequently no change of finite free lattice can make F regular at that place: a regular matrix over its DVR has integral eigenvalues, while these have negative valuation.

The finite localization (E9) explicitly removes t=+1 and retains t=-1. The selected collision is a legitimate place above v=1, but this is not regularity at every place over v=1 and is not an identification with VIII's prescribed global integral form or a designated continuation of its algebraic branch. No continuity of the selected places is inferred from the coefficient scheme.

## 7. An algebraic trace has a nonzero place above one

The following lemma isolates the complementary all-places condition.

**Lemma E22.** Let f be one algebraic function over C(v). Suppose its selected regular values at v=b^n, b>1, satisfy
\[
 f_{b^n}=\sum_{i=1}^s m_i\alpha_i^n
\]
for all sufficiently large n, with m_i positive integers and alpha_i nonzero. Put N=sum m_i. Then the trace field C(v,f) has a place above v=1 at which f is regular and has residue N.

**Proof.** F54 Part1 gives L>0 and integers a_i such that alpha_i^L=b^(a_i). Let P(v,Y) be the irreducible minimal polynomial of f over C(v), clearing denominators when evaluating, and set
\[
 p(t)=\sum_i m_i t^{a_i}\in\mathbb C[t,t^{-1}].
\]
At n=Lr, the trace values are p(b^r). Therefore
\[
 P(t^L,p(t))=0
\]
at infinitely many t=b^r. It is a rational function of t and thus vanishes identically.

Identify C(v) with its subfield of C(t) by v=t^L. Since P is irreducible and has p(t) as a root, the assignments
\[
 v\longmapsto t^L,\qquad f\longmapsto p(t)
 \tag{E23}
\]
define a field embedding C(v,f) into C(t). Restrict the ordinary t=1 place to that subfield. Because t^L-1 has a simple zero at t=1 in characteristic zero, it is a place over v=1. The Laurent polynomial p is regular there, with p(1)=N. This proves the statement. QED.

This lemma does not say that every place above one has that residue. The explicit model has normalized marked function g(t)=2(1+t)^2, with g(-1)=0 and g(1)=8. That is precisely why specifying just one regular collision place leaves an exception.

## 8. Extending that place to the full coefficient field

For use with an actual matrix family, the trace-field place must extend to its whole finite coefficient field. Here is the explicit algebraic step.

Let K=C(v,f), let O be the valuation ring of the place in Lemma E22, and let L/K be the finite field generated by all matrix and action coefficients. The restricted valuation has value group Z, since v-1 has valuation one. Thus O is a DVR.

Let B be the integral closure of O in L. In characteristic zero this extension is separable. Its finiteness is the standard normalization result [Stacks, Lemma 10.161.8, tag 032L](https://stacks.math.columbia.edu/tag/032L). The following independently checked trace-pairing derivation is the standard proof recorded there, not a new result. Choose a K-basis of L and multiply its members by powers of a uniformizer until each is integral over O. The algebra A generated by these integral elements is a finite O-module and spans L over K. If x is integral over O, then Tr_(L/K)(xA) lies in O, since traces of integral elements are integral and O is integrally closed. The nondegenerate field trace pairing therefore puts B inside the finite dual lattice
\[
 A^*=\{x\in L:\operatorname{Tr}_{L/K}(xA)\subset O\}.
\]
As O is Noetherian, B is finite over O.

There is a prime q of B above the maximal ideal of O by [Stacks, Lemma 10.36.17, tag 00GQ](https://stacks.math.columbia.edu/tag/00GQ). Equivalently, the uniformizer does not become a unit in B, since its inverse in K is not integral over O, so a maximal ideal above it exists. The localization B_q is a one-dimensional integrally closed Noetherian local domain, hence a DVR by [Stacks, Lemma 10.119.7, tag 00PD](https://stacks.math.columbia.edu/tag/00PD). Its residue field is a finite extension of the original residue field C and is therefore C. This is a place of L extending the one constructed in Lemma E22. In particular the residue of f remains the nonzero integer N.

The three cited primary statements and their hypotheses were directly read on 21 November 2026. The final paper fragment cites these known results and gives only their short application to the trace-field place, as requested; the present proof record retains the checked elementary derivation. A selected scalar branch is not silently assumed to extend to all coefficient functions.

## 9. The all-places marked-trace obstruction

**Theorem E24.** Let L/C(v) be a finite coefficient field for an algebraic operator F on the actual rank-64 tensor module. Assume the regular-evaluation, base invertibility and right-action commutation hypotheses of F54 Part3, and suppose its marked-X trace identity holds at all sufficiently large extension degrees.

If, at every place of L above v=1, F is regular on the pulled-back actual tensor lattice and X specializes to zero, this is impossible, with no common-radius or integral-weight assumption.

**Proof.** At b>1 the actual Delta-sector has dimension eight. Right-action commutation makes it invariant under the invertible F_b. If its eigenvalues, counted with multiplicities, are alpha_i, the normalized algebraic trace function
\[
 f(v)=\Delta(b)^{-1}\operatorname{Tr}_M(X(v)F(v))
\]
has selected values sum alpha_i^n by the marked law. Lemma E22 supplies a place of its trace field above v=1 with residue f=8. Section 8 extends that place to L.

By the all-places hypothesis, the matrix F is regular on the actual lattice there and X specializes to zero. Hence the residue of Tr(XF) is zero and the residue of f is zero. This contradicts its residue eight. QED.

The same proof works if at every such place X specializes to a nilpotent operator commuting with the regular specialization of F, since XF is then nilpotent and has trace zero. It also works for any fixed nonzero marked-sector rank, replacing eight by that rank.

All-places regularity is a genuine additional hypothesis. The construction (E4)--(E18) violates it at t=+1 while satisfying the selected negative-sheet regularity, right action, ordinary identity trace and marked trace. No assertion is made that an unspecified GCT arithmetic realization automatically has the stronger property. Requiring regularity in a global integral form may motivate testing it, but that comparison must itself be established.

## 10. Separate Grothendieck dictionary

The positive example is a finite algebraic coefficient cover v=t², localized at an explicitly listed finite set of functions, with the actual pulled-back coherent algebra and tensor module. The regular basis comparison defines an actual right-module automorphism. The trace equalities are algebraic identities of this specified operator family; they are not inferred from the mere existence of coherent sheaves and are not an assertion of a new geometric Frobenius or integral-weight realization.

The selected negative collision and removed positive collision are different points in the normalization over the same v=1 point. The complementary theorem uses a field embedding, restriction of the t=1 place, finite normalization and extension of that place to all coefficient data. This is ordinary affine/normalization and module language within the EGA framework already audited, together with the torus-character and genuine-weight-line argument of F54 Part1 in the SGA3 framework. The precise normalization, lying-over and DVR facts are the three primary Stacks lemmas cited in Section 8; the EGA framework correspondence alone is not used as their specific locator. No new archival locator is needed.

Continuous scalar-branch compatibility is an additional analytic comparison, not a property supplied automatically by the algebraic scheme. The parent's separate argument addresses that condition. The present theorem instead quantifies over all algebraic places above one.

The actual right action, ordinary left invariance, full centralizer, identity traces, marked traces and fixed-word traces are separate requirements. The example and complementary theorem specify which of those hold and which extra condition gives the obstruction. They do not select the designated canonical basis, bar globalization, or the target multiplicity inequalities.

## 11. Author check record

All cancellation formulas, base and collision values, nonvanishing at every extension point, actual block actions, trace identities, left commutator, generator-trace failures and place arguments are proved above.

The accompanying verify_fractional_marked_escape.py checks the rational identities, exact special values, right-block commutators and explicit left failure using exact SymPy arithmetic. Its finite computations supplement the all-n inequalities and field/place proofs; they do not replace them. A fresh complete independent review is requested before integration. No formal proof-kernel or independent proof of the full EGA/SGA formalism is claimed.

