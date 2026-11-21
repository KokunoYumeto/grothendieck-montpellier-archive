# DEG_L / T7 research report

Run: DEG_L, 2026-11-21. Agent: `/root/semireg_t7`, GPT-6 Astra Pro, inherited effort not exposed. This is a working report for integration by the root agent. No assertion below proves semiregularity of a particular unexamined image surface. The universal assertion that every level version of the 032 morphism is semiregular is false, even after replacing the undefined embedding normal bundle by the natural deformation complex of a morphism.

## 1. What the attached construction actually produces

In the attached 032 main paper, Proposition 3.1, pp. 11–12, starts with a smooth connected projective surface `Y`, four rational Hodge maps, and a nonzero four-factor period. Lemma 2.2 clears denominators to obtain morphisms `f_i:Y -> B(v_i)`. Set `A=product_i B(v_i)`, `g=dim A=4s`, and `f=(f_i)`. The geometric surface cycle is

\[
z=f_*[Y]\in\mathrm{CH}^{g-2}(A).
\]

The paper explicitly proves only that `dim f(Y)=2`. The period is a nonzero pairing of `cl(z)` with a four-factor class; it does not show that `f` is a closed immersion, that its image is smooth, or that its image is a regular embedding. Four divisor correspondences subsequently turn that nonzero functional into a codimension-two algebraic class (032, equations (3.3)–(3.5)).

The actual surface `Y` in the theta construction is a compact smooth quotient of the complex two-ball: 032 §4.1, pp. 13–14; Corollary 6.7, p. 45; and §7, p. 46. Corollary 6.7 and §7 permit passage to every sufficiently deep principal level and explicitly pull back the one-form classes and maps. Thus there is no single canonical embedded surface determined by the four sign functions.

**S-01 (domain correction; checked).** Let `f:Y -> A` be one choice from 032 and let `pi:Y' -> Y` be a connected finite étale cover of degree `d>1`. The pulled-back rational Hodge maps still satisfy the surface criterion, with period multiplied by `d`. The resulting map `f'=f o pi` is not a closed immersion.

*Proof.* Pullback is a rational Hodge map, and integration of the pullback of a top-degree class multiplies the integral by `d`. Every point of `Y` has `d` distinct preimages under the étale cover, all with the same image under `f'`. Hence `f'` is not injective on geometric points and cannot be a closed immersion. The proper pushforward is `f'_*[Y']=d f_*[Y]`. In particular the 032 input and nonzero period remain valid although the embedding premise required to write Bloch's normal bundle is absent. ∎

This does not disprove semiregularity of the reduced image `f(Y)`, when that image happens to be smooth. That is a different object, and the map's generic degree must be retained when identifying its cycle class.

## 2. A precise corrected semiregularity test

For a **smooth closed immersion** `i:Y -> A`, of a surface in a `g`-dimensional abelian variety, set `p=g-2` and `N=N_{Y/A}`. Bloch's map is

\[
\sigma_i:H^1(Y,N)\longrightarrow H^{g-1}(A,\Omega_A^{g-3}).
\]

Buchweitz–Flenner, §8.1 and Proposition 8.2, pp. 199–200, give its Serre-dual description. For an abelian ambient variety this reduces T7 to an explicit map involving the conormal sequence.

**S-02 (exact dual gate; checked).** Let `W=H^0(A,Omega_A^1)`. The immersion is semiregular if and only if

\[
\mu_i:H^1(A,\mathcal O_A)\otimes\bigwedge^3W
 =H^1(A,\Omega_A^3)
 \longrightarrow H^1(Y,N^*\otimes K_Y)
\tag{S2}
\]

is surjective. The map first restricts forms to `Y` and then applies the natural exterior-power map

\[
\bigwedge^3(i^*\Omega_A^1)\longrightarrow N^*\otimes\bigwedge^2\Omega_Y^1
 =N^*\otimes K_Y
\]

associated to `0 -> N* -> i*Omega_A^1 -> Omega_Y^1 -> 0`.

*Proof.* The source of the dual of `sigma_i` is, by Serre duality on the `g`-fold `A`, `H^1(A,(Omega_A^{g-3})^* tensor K_A)=H^1(A,Omega_A^3)`. Its target is, by Serre duality on the surface, `H^1(Y,N* tensor K_Y)`. The exterior-power map just displayed is the defining dual map in Buchweitz–Flenner §8.1, and Proposition 8.2 identifies the resulting map with Bloch's. Finally `Omega_A^3=O_A tensor wedge^3 W`; finite-dimensional duality makes injectivity equivalent to surjectivity. ∎

No theta-period calculation in 032 computes (S2). Positivity of one period is a scalar condition in degree four. Surjectivity of (S2) controls every normal obstruction and requires information about the conormal sequence and its cohomology.

## 3. Nonzero four-factor periods do not imply semiregularity

**S-03 (explicit counterexample to the generic inference; checked).** There is a smooth surface in a CM abelian threefold with a nonzero product of two holomorphic and two antiholomorphic degree-one classes, for which Bloch's map is not injective.

*Construction and proof.* Let `E` be any CM elliptic curve, `B=E x E`, and let `L=O_E(3[0]) boxtimes O_E(3[0])`. This is very ample. Choose a smooth connected member `C` of `|L|`, which exists by Bertini; connectedness also follows from ampleness. Since `K_B=O_B` and `L^2=18`, adjunction gives `g(C)=10` and `N_{C/B}=K_C`. Let

\[
A=B\times E,\qquad Y=C\times E\subset A.
\]

This is a smooth divisor, and

\[
N_{Y/A}=K_C\boxtimes\mathcal O_E,
\quad h^1(Y,N_{Y/A})=h^1(C,K_C)+h^0(C,K_C)h^1(E,\mathcal O_E)=1+10=11.
\]

For a divisor, Bloch's target is `H^2(A,O_A)`, of dimension `binom(3,2)=3`. Hence the kernel of its semiregularity map has dimension at least eight.

The curve `C` dominates both elliptic factors of `B`: otherwise it would be contained in a fibre, which is incompatible with its ample divisor class. Thus the pullback `alpha` of a nonzero holomorphic one-form from the first factor is nonzero on `C`. Let `beta` be a nonzero holomorphic one-form on the last factor `E`. The holomorphic two-form `alpha wedge beta` is nonzero on `Y`, and

\[
\int_Y (\alpha\wedge\beta)\wedge\overline{(\alpha\wedge\beta)}\ne0.
\]

This follows either by the product formula and positivity of `i alpha wedge bar alpha`, `i beta wedge bar beta`, or by the Hodge–Riemann bilinear relations. It is precisely a nonzero four-one-form period of the sort that supplies the surface criterion. ∎

This is **not** a counterexample asserted to be the particular 032 ball quotient. It refutes the proposed implication from a nonzero period to semiregularity and shows why the conormal calculation cannot be replaced by positivity.

## 4. Rigidity obstructs the intended deformation mechanism

**Background checked in a primary source.** Calabi–Vesentini, *Sur les variétés complexes compactes localement symétriques*, Bull. Soc. Math. France 87 (1959), Théorème 3, p. 315, proves `H^1(Y,T_Y)=0` for a compact smooth complex ball quotient of dimension at least two. Theorem 4 on the same page states local stability. The precise available PDF is `https://www.numdam.org/article/BSMF_1959__87__311_0.pdf`, PDF page 6 (zero-based index 5). This is sufficient; there is no need to rely on an uninspected Annals locator.

For any immersion `i:Y -> A`, let `G` be the smallest abelian subvariety whose translate contains `i(Y)`. Equivalently, after choosing a basepoint, it is the image of `Alb(Y) -> A`. The pullback on `H^1(O)` has kernel of dimension `g-dim G`. It is injective exactly when the surface generates all of `A`.

**S-04 (rigid generating surface; checked).** Suppose `Y` is a smooth projective surface with `H^1(Y,T_Y)=0`, and `i:Y -> A` is a smooth closed immersion whose image generates `A`. Then the obstruction map for extending the embedded surface in first-order deformations of `A`,

\[
\mathrm{ob}_i:H^1(A,T_A)\longrightarrow H^1(Y,N_{Y/A}),
\]

is injective. If `i` is semiregular, the infinitesimal Hodge locus of the **entire** fundamental class `i_*[Y]` is zero-dimensional, even before imposing a polarization.

*Proof.* Since `T_A=Lie(A) tensor O_A`, restriction on first cohomology is

\[
\mathrm{id}_{\operatorname{Lie}(A)}\otimes i^*:
\operatorname{Lie}(A)\otimes H^1(A,\mathcal O_A)
\longrightarrow\operatorname{Lie}(A)\otimes H^1(Y,\mathcal O_Y).
\]

It is injective because the homomorphism `Alb(Y) -> A` is surjective, so its pullback on `H^1(O)` is injective. The normal sequence and `H^1(T_Y)=0` show that `H^1(Y,i^*T_A) -> H^1(Y,N)` is also injective. Their composite is `ob_i`, hence is injective. By Buchweitz–Flenner, Corollary 4.12, p. 172, and Proposition 8.2, p. 200,

\[
\sigma_i\bigl(\mathrm{ob}_i(\kappa)\bigr)
 =\kappa\mathbin{\lrcorner}\,i_*[Y].
\]

The right side is the infinitesimal variation of the Hodge type of the full class. If `sigma_i` is injective, the vanishing of the right side forces `kappa=0`. ∎

**Refinement when `Y` does not generate `A`.** Without the generation hypothesis, the same proof gives the exact kernel

\[
\ker\mathrm{ob}_i=\operatorname{Lie}(A)\otimes
\ker\bigl(H^1(A,\mathcal O_A)\to H^1(Y,\mathcal O_Y)\bigr).
\tag{S4a}
\]

If `sigma_i` is injective this is also the tangent kernel for the Hodge type of the full fundamental class. Its dimension is `g(g-dim G)`. In a polarized decomposition up to isogeny into `G` and a complement, the surviving polarized directions are the directions of the complement: the generated quotient must remain constant.

**Generation is not implied by the four-factor criterion.** The period says that one alternating four-linear functional does not vanish. It does not say that the direct-sum map `H^1(A,Q) -> H^1(Y,Q)` is injective. Even when every individual map is nonzero, duplicate factors can force the image into a diagonal. If a CM type is imprimitive, `B(v)` can itself have repeated isogeny factors, and a nonzero Hodge map from its `H^1` can have a kernel. Thus one must either check generation or use (S4a).

**Geometric meaning for Route 2.** A smooth local deformation of an embedded rigid `Y` is locally a deformation of the same source. A map from it to the variable abelian variety factors through the fixed `Alb(Y)`. The quotient which it generates is therefore a locally constant rational Hodge quotient. Consequently, deforming the same rigid source does not produce a positive-dimensional varying generated abelian variety. A projector can make a four-factor class `t` remain Hodge on a much larger Shimura subvariety, but that does not make `i_*[Y]` remain Hodge there. Bloch's theorem for `Y` applies to the latter class, not to an arbitrarily chosen projected component.

**Rejected stronger generation inference.** A nonzero Weil component alone does not force generation either. Let \(E\) have CM by an imaginary quadratic field \(K\), put \(A=E^n\times E^n\), and let \(K\) act as \((a,\bar a)\). The diagonal \(Y=E^n\) has a nonzero extreme Weil pairing: pullback maps each of the two \(K\)-eigenspaces in \(H^1(A,\mathbf C)\) isomorphically onto \(H^1(Y,\mathbf C)\). Nevertheless the generated subvariety is only the diagonal. The logical error is inferring injectivity on a direct sum from injectivity on each summand when their images can intersect. If the ambient abelian variety is simple, a positive-dimensional image does generate it; this qualified observation is valid.

## 5. Correcting the map, and a quantitative failure at deep levels

For a morphism `f:Y -> A` with `dim f(Y)=2`, the appropriate object is its cotangent complex. Since both varieties are smooth, its derived dual is represented by

\[
[T_Y\xrightarrow{df}f^*T_A]
\quad\text{in cohomological degrees }0,1.
\]

The differential is generically injective in characteristic zero and therefore injective as a map of coherent sheaves: its kernel is a torsion-free subsheaf of `T_Y` with generic rank zero. Put `N_f=coker(df)`. It need not be locally free. Nevertheless,

\[
T^2_{Y/A}(\mathcal O_Y)
 =\operatorname{Ext}^2_Y(L_{Y/A},\mathcal O_Y)
 \cong H^1(Y,N_f).
\tag{S5a}
\]

Buchweitz–Flenner, Proposition 7.21, Lemma 7.22, and the definition immediately before Theorem 7.23, pp. 198–199, give the natural semiregularity map for this morphism:

\[
\tau_f:T^2_{Y/A}(\mathcal O_Y)
 \longrightarrow
 \bigoplus_{r=0}^{g-2}H^{r+2}(A,\Omega_A^r).
\tag{S5b}
\]

It factors through `Ext^2_A(Rf_*O_Y,Rf_*O_Y)` and the Atiyah-trace semiregularity map. No unproved normal-bundle premise is needed to define it.

The factorization is `tau_f = sigma_{Rf_*O_Y} o psi_f`. Noninjectivity of `tau_f` does **not** by itself imply noninjectivity of `sigma_{Rf_*O_Y}`: a kernel vector may already be killed by `psi_f`. The dimension argument below is a theorem about the morphism deformation problem. It must not be silently transferred to the perfect-complex deformation problem.

**S-05 (dimension obstruction; checked).** Let `Y` be a compact smooth complex ball quotient surface, and let `f:Y -> A` be a morphism with two-dimensional image. Then

\[
\dim\ker\tau_f\ \ge\ gq(Y)-\binom{2g}{g-2},\qquad q(Y)=h^1(Y,\mathcal O_Y).
\tag{S5c}
\]

In particular, `tau_f` is not injective when `q(Y)>binom(2g,g-2)/g`. For a map to a surface-cycle component target of Bloch's degree alone, the corresponding upper bound on the target dimension is `g binom(g,3)`.

*Proof.* By Calabi–Vesentini, `H^1(T_Y)=0`. The exact sequence `0 -> T_Y -> O_Y^{oplus g} -> N_f -> 0` therefore gives an injection `H^1(O_Y)^{oplus g} -> H^1(N_f)`. Thus the domain of (S5b), identified by (S5a), has dimension at least `gq(Y)`. On an abelian `g`-fold,

\[
h^{r+2}(A,\Omega_A^r)=\binom gr\binom g{r+2}.
\]

Vandermonde's identity, using `binom(g,r+2)=binom(g,g-r-2)`, gives

\[
\sum_{r=0}^{g-2}\binom gr\binom g{r+2}=\binom{2g}{g-2}.
\]

Rank–nullity proves (S5c). The single component `H^{g-1}(A,Omega_A^{g-3})` has dimension `binom(g,g-3)binom(g,g-1)=g binom(g,3)`. ∎

**S-06 (the universal level version is false; checked, using a known Betti theorem).** Fix one nonzero 032 four-factor construction `f:Y -> A`. There are connected finite étale covers `pi_j:Y_j -> Y` for which all four pulled-back Hodge maps and their nonzero period remain valid, but for which `tau_{f o pi_j}` is not injective. The same conclusion holds within a cofinal system of principal congruence covers.

*Proof.* The nonzero period implies `H^1(Y,C) != 0`. The source is an arithmetic compact ball quotient. Venkataramana, *Virtual Betti numbers of compact locally symmetric spaces*, arXiv:math/0611733, Theorem 1, pp. 1–3, proves that the direct limit of `H^1` over finite covers is either the cohomology of the compact dual or is infinite-dimensional. The compact dual of the two-ball is `P^2`, whose first cohomology is zero. Pullback under a finite cover is injective over `Q`, by transfer. Hence the direct limit is nonzero and is infinite-dimensional. It follows that `q(Y_j)` is unbounded along a suitable sequence of covers. Apply S-05, with the same fixed target `A`. S-01 gives persistence of the input period and rational Hodge maps.

For principal congruence covers, use the congruence version explicitly identified in Venkataramana's final Remark, p. 3, with Borel's argument. The proof of Theorem 1 works on congruence covers because conjugation by rational group elements and finite intersection preserve the congruence property. If the cohomology direct limit stabilized in a finite-dimensional space, a congruence subgroup would act trivially; the closure of its normal closure in the simple real group is the full group, forcing the harmonic forms to come from the compact dual. Principal levels are cofinal among congruence subgroups. Thus their first cohomology is unbounded as well. This matches the deeper-principal-level persistence explicitly recorded in 032 Corollary 6.7 and §7. ∎

**Scope.** S-06 refutes semiregularity for *all* choices of sufficiently deep level of the original map, including its natural Buchweitz–Flenner repair. It does not say that a particular initial level map has a nonzero kernel, nor that the reduced image fails Bloch semiregularity. Those are narrower questions requiring their own calculation.

## 6. Attack on the cover obstruction: equivariant descent

**S-07 (cover-invariant obstruction space; checked).** Let `pi:Y' -> Y` be a finite étale Galois cover with deck group `H`, and let `f'=f o pi` be as above. Then

\[
N_{f'}\simeq\pi^*N_f,\qquad
H^1(Y',N_{f'})^H\simeq H^1(Y,N_f).
\tag{S7}
\]

*Proof.* The identity `T_{Y'}=pi^*T_Y` and flatness of `pi` identify the cokernel sequences, proving the first formula even when the normal sheaves have torsion. Since `pi` is finite, its pushforward is exact on coherent sheaves. The projection formula identifies `pi_*pi^*N_f` with `N_f tensor pi_*O_{Y'}`. The averaging idempotent `|H|^{-1}sum_{h in H}h` splits the invariant summand `O_Y` of `pi_*O_{Y'}`. Taking cohomology and this direct summand gives the second formula. ∎

Thus the obstruction growth in S-06 can be removed by restricting to equivariant deformations and descending. It does not create new deformation directions or prove injectivity at the base level. After descent the exact remaining gate is the base map's semiregularity, or a different object whose chosen Chern character stays of Hodge type. The same operation also removes the artificial degree growth from a source cover: `f'_*[Y']=deg(pi)f_*[Y]`, so the normalized class is unchanged. It must not be confused with division along a Hecke orbit where the **target** abelian variety varies.

The root report can invoke Markman's actual repair as evidence for the appropriate next step: the supplied Markman source §1.5 explicitly says that the first sheaf `E` is not semiregular; equivariant normalization and descent produce a different semiregular sheaf. The concrete criterion is Lemma 8.3.4 (LaTeX label `lemma-criterion-for-semiregularity`): surjectivity of the obstruction map and equality of its kernel with the Chern-character-contraction kernel imply injectivity. This is a statement about a constructed sheaf and its full obstruction space, not a theorem that any cycle with the right period is semiregular.

## 7. Derived replacement and its exact extra Hodge data

There is always a perfect complex on the abelian ambient variety,

\[
\mathcal E=Rf_*\mathcal O_Y.
\]

Perfection is Buchweitz–Flenner Lemma 7.22, and follows here also from smoothness of `A`. Grothendieck–Riemann–Roch gives the exact Chern character

\[
\operatorname{ch}(\mathcal E)
 =f_*\left(1+\frac{c_1(T_Y)}2+
       \frac{c_1(T_Y)^2+c_2(T_Y)}{12}\right),
\tag{S8}
\]

because `td(T_A)=1`. Its three possible nonzero components are in codimensions `g-2`, `g-1`, and `g`. The first is the surface class. The last has degree `chi(O_Y)`. The middle is a separate curve class. Consequently, full semiregularity of this perfect complex, were it known, would require preserving the relevant **full** Chern-character data, not merely the projected four-factor class. Buchweitz–Flenner Theorem 5.1 allows a subset `I` of Chern components only when the map to exactly those components is itself injective. Selecting fewer Hodge conditions cannot be done without strengthening the injectivity assertion.

**S-08 (multiplicity cannot force derived semiregularity; checked).** Let `E` be a perfect complex on a smooth projective variety, with `Ext^2(E,E) != 0`. For every integer `m>=2`, the direct sum `E^{oplus m}` is not semiregular for the Atiyah-trace map.

*Proof.* There is an identification

\[
\operatorname{Ext}^2(E^{\oplus m},E^{\oplus m})
 =\operatorname{Ext}^2(E,E)\otimes\operatorname{End}(\mathbf C^m).
\]

The Atiyah class is `at(E) tensor id`; each component of the semiregularity map is the corresponding component for `E` tensored with the ordinary matrix trace. Thus any nonzero `u in Ext^2(E,E)` tensored with a nonzero traceless matrix is in the kernel. ∎

This is a precise warning about the proposed derived workaround: representing the correct multiple of a cohomology class does not determine a semiregular object. It is not a claim that every object representing that multiple fails.

## 8. How a successful semiregular replacement would give bounded division

The useful deformation statement is the following conditional implication, to be integrated with the root agent's proper-Chow/Hilbert proof.

Let `Acal -> S` be a smooth projective abelian scheme over a smooth connected complex algebraic base, and `t` a flat rational Hodge class. Suppose one has, at a point `s0`, a finite signed sum of smooth regularly embedded subvarieties `Z_j` with fixed integer coefficients representing `N t_s0`. Suppose each `Z_j` is Bloch semiregular and **its full class** remains Hodge on `S`. Bloch/Buchweitz–Flenner imply local extension in the Hilbert functor. With the Hilbert polynomial fixed, the relative Hilbert scheme is projective over `S`. A component containing the local extension dominates an analytic neighborhood, hence has image all of irreducible `S`. Specialization retains the flat cohomology class, so the coefficients `N` and the degrees are uniformly bounded on all fibers.

For sheaves or perfect complexes, replace the individual fundamental-class conditions by the Chern components `I` for which the corresponding partial Atiyah-trace map is injective. Properness or a bounded Quot presentation of the actual extending objects must be supplied; semiregularity alone is a local statement, not a properness theorem.

The 032 papers supply the cycle and its nonzero testing period. They do **not** supply the regular embedding, injectivity of the relevant map, or preservation of the full unprojected class along Route 2. S-04 shows that the rigid generating surface itself is an especially restrictive object for this purpose. A different sheaf/object, after extraction or equivariant descent, is the exact remaining geometric gate.

## 9. Current states and approaches tried

| Question | State | Strongest justified gate or result |
|---|---|---|
| Is the surface in 032 given as a regular embedding? | Refuted as a universal input claim | S-01: deeper allowed covers give noninjective maps; image smoothness is not proved. |
| Does a nonzero four-factor period imply semiregularity? | Refuted | S-03, explicit CM divisor example with kernel dimension at least eight. |
| Bloch semiregularity of a specified smooth reduced 032 image | Open | S-02: explicit surjectivity of `mu_i`, with the actual conormal sequence and scheme structure required. |
| Semiregularity of every deep-level 032 morphism, using a morphism deformation complex | Refuted | S-05–S-06: obstruction dimension exceeds the fixed Hodge target. |
| Can the same rigid generating surface deform through nontrivial abelian moduli? | No for a smooth embedded deformation | S-04: injective ambient obstruction; if semiregular, full class has zero tangent Hodge locus. |
| Does cover-equivariant descent remove the dimension obstruction? | Proved | S-07; returns precisely to base-level obstruction, no new uniformity. |
| Does replacing the cycle by `Rf_*O_Y` automatically repair T7? | Not established; universal class-to-object inference refuted | S-08; (S8) records all extra Hodge data; Markman Lemma8.3.4 supplies the concrete obstruction-map gate. |
| Does a suitable semiregular replacement yield bounded division? | Proved conditional implication, root handling full proof | Need injectivity for a finite list of full classes/Chern components, then local extension plus proper Hilbert/Chow dominance. |

Attempts intentionally not promoted to findings: (i) claiming any ball quotient image embeds in an abelian variety; no such theorem was found or used; (ii) inferring injectivity from Hodge positivity; disproved by S-03; (iii) applying an abelian-subvariety semiregularity theorem to a generically finite surface image; object mismatch; (iv) relying solely on full derived-category invariance under a Fourier–Mukai transform without first constructing and checking a semiregular object; it moves the same obstruction issue; (v) treating high-level source covers as Hecke movement in the target; they only scale the same cycle.

## 10. Grothendieck language and locator discipline

All constructions concern correspondences acting on rational Chow groups and their Betti/Hodge realizations. The obstruction spaces distinguish an algebraic representative from its class modulo homological or numerical equivalence. Semiregularity is not a property of a motive or of a numerical class alone; S-08 illustrates the extra deformation data of a chosen realization by an object. The properness step belongs to Grothendieck's Hilbert/Quot framework (FGA, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert*, Bourbaki Exp. 221). The cotangent complex and Atiyah-class formulation are in the later Illusie/Buchweitz–Flenner development of that deformation framework.

No Grothendieck handwritten archive scan was supplied in the ZIP, and this subagent has not inspected any such scan. Therefore it supplies no invented cote/scan attribution and no transcription correction. The root should retain this limit in the transcription table and use only cotes/scans it actually verifies.

## 11. Removing the unwanted Chern components at the K-theory level

**S-09 (integral Chern-component extraction; checked).** Let `A` be an abelian `g`-fold, let `0 <= p <= g`, and let `xi in K_0(A)` satisfy `ch_j(xi)=0` for `j<p`. Fix `m>=2`, write `M=[m]^*` for the integral endomorphism of `K_0(A)`, and set

\[
D_{g,p,m}=\prod_{j=p+1}^{g}(m^{2j}-m^{2p}),\qquad
\eta=\prod_{j=p+1}^{g}(m^{2j}\operatorname{id}-M)\xi.
\tag{S9}
\]

Empty products have value one. Then `eta` is integral and

\[
\operatorname{ch}(\eta)=D_{g,p,m}\operatorname{ch}_p(\xi).
\]

Here equality is in rational Betti cohomology; no claim about injectivity of the Chow realization is needed. If `z=sum a_i Z_i` is an integral codimension-`p` cycle with class `N_0 t`, take `xi=sum a_i[O_{Z_i}]`. On a smooth variety the leading Chern character of `O_Z` is its fundamental cycle, so the hypotheses hold and `ch(eta)=D_{g,p,m}N_0 t`.

*Proof.* Pullback by `[m]` multiplies `H^{2j}(A,Q)` by `m^{2j}`. Thus the `j`th Chern component of the polynomial expression is the same scalar polynomial evaluated at `m^{2j}`, times `ch_j(xi)`. For `j>p` its factor indexed by `j` is zero; for `j<p` the input is zero; for `j=p` it is `D_{g,p,m}`. The polynomial has integer coefficients and `[m]^*` acts on integral `K_0`, so `eta` is integral. Any integral K-class on a smooth projective variety is represented by an actual perfect complex, using finite locally free resolutions and shifts for negative terms. ∎

For an arbitrary K-class with lower components, the full rational interpolation projector is

\[
\Pi_p=\prod_{\substack{0\le j\le g\\j\ne p}}
 \frac{M-m^{2j}}{m^{2p}-m^{2j}},
\qquad \operatorname{ch}(\Pi_p\xi)=\operatorname{ch}_p(\xi).
\]

Clearing its fixed denominator gives the same conclusion. This removes the additional curve and top-degree classes in (S8), as well as any unwanted Künneth components once an algebraic correspondence projector has first produced the desired algebraic class. It is a construction at a single known algebraic fiber, not a proof that the resulting object deforms.

For Route 2, a more useful character gate permits the polarization. If `L` has class `theta`, add to `eta` an integral combination of `[L^a]`; the resulting character is

\[
N t+P(\theta),\qquad P(\theta)=\sum_a b_a e^{a\theta},\quad b_a\in\mathbf Z.
\tag{S9b}
\]

Every component remains Hodge on a polarized family where `t` does. The exact remaining problem is to find a **semiregular actual representative** of such a K-class. The direct-sum representative supplied by K-theory is not expected to have this property; S-08 gives an explicit failure mechanism. Nontrivial extensions, equivariant descent, or another change of object must be analyzed. Section 14 below proves a reason to retain polarization data in this gate.

## 12. A full Fourier--Mukai invariance refinement

The supplied 032 companion proves transport of obstruction evaluation and Chern-character contraction in Proposition 5.2, pp. 45–49; it deliberately does not assert naturality on arbitrary Ext classes. Its trace construction nevertheless allows the following short refinement. This is a proof supplied here, not a claim that Proposition 5.2 already states it.

**S-10 (full trace-map invariance; checked refinement).** Let `Phi:Perf(A)->Perf(B)` be a fixed enhanced Fourier--Mukai equivalence between smooth projective abelian varieties, with inverse adjunction data as in companion §5.2. Then the full Atiyah-trace maps fit into a commutative square

\[
\sigma_{\Phi Q}\circ\Phi_{\rm Ext}
 =\Phi^{H}_{HH}\circ\sigma_Q
\quad\text{on }\operatorname{Ext}^2_A(Q,Q),
\tag{S10}
\]

where `Phi^H_HH` is the isomorphism defined by the perfect Serre pairings in equations (5.30), (5.34), (5.35). In particular full semiregularity is invariant under this equivalence. The transport may mix the target Hodge bidegrees, so this does not assert invariance of a single selected component.

*Proof.* Use exactly the companion's notation `H_A=LDelta^*O_Delta`, `Sigma_A=Delta_*(omega_A[g])`, `T^{-2}(A)=Hom(O_Delta,Sigma_A[-2])`, and its partial trace and HKR normalization. The class

\[
b_Q(v)=\operatorname{Tr}_{Q,H_A[2]}(A_Q^H[2]\circ v)
 \in\mathbb H^2(A,H_A)=HH_{-2}(A)
\]

has HKR image `sigma_Q(v)` by §5.1.4, equations (5.20), (5.24), and the displayed definition after (5.23). For `delta in T^{-2}(A)`, let `delta_Q:Q->S_AQ[-2]` be its evaluation. The same trace-compatible adjunction used in equation (5.37), now shifted by two, gives

\[
\langle b_Q(v),\delta\rangle_{A,-2}
 =\operatorname{Tr}_{A,Q}(\delta_Q[2]\circ v).
\tag{S10a}
\]

For completeness, if `delta':H_A->omega_A[g-2]` is the adjoint coefficient map, the left side is the Serre trace of `delta'[2] o b_Q(v)`. Naturality of the perfect partial trace (5.24) moves `delta'[2]` inside that trace; evaluation of `Delta_*delta' o eta_Delta` then gives the right side. No odd shift is exchanged.

The convolution argument proving (5.33) applies with the same shift and gives

\[
(\Psi^{-2}\delta)_{\Phi Q}
 =\theta_Q[-2]\circ\Phi(\delta_Q).
\tag{S10b}
\]

Indeed the adjacent inverse kernels cancel by exactly the same fixed unit, counit and triangle identities; all morphisms are shifted coherently by the enhancement. Combining (S10a), (S10b) and trace preservation (5.31) gives

\[
\begin{aligned}
\langle b_{\Phi Q}(\Phi_{\rm Ext}v),\Psi^{-2}\delta\rangle_{B,-2}
 &=\operatorname{Tr}_{B,\Phi Q}
   \bigl(\theta_Q\circ\Phi(\delta_Q[2]\circ v)\bigr)\\
 &=\operatorname{Tr}_{A,Q}(\delta_Q[2]\circ v)
 =\langle b_Q(v),\delta\rangle_{A,-2}.
\end{aligned}
\]

By (5.34) the last expression also equals `pairing(Phi_*^HH b_Q(v),Psi^{-2}delta)`. The tests exhaust `T^{-2}(B)` and the pairing is perfect, proving equality of the two Hochschild classes. Apply the fixed HKR maps and (5.35). Both vertical maps are isomorphisms, proving the kernel assertion. ∎

Thus a mere Fourier--Mukai equivalence cannot remove an established full semiregularity kernel of an object. Equivariant descent changes the object/category and is a different operation. In particular this does not transfer S-06's map-level kernel to a sheaf: the distinction involving `psi_f` after (S5b) remains necessary.

## 13. Complete intersections and graph embeddings do not supply the missing theorem

**S-11 (ample complete-intersection counterexample; checked).** Let `A` be an abelian fourfold, let `L` be very ample, and let `Y=D_1 cap D_2` be a smooth transverse intersection with `D_1,D_2 in |L|`. Then

\[
h^1(Y,N_{Y/A})=24,
\qquad h^3(A,\Omega_A^1)=16.
\]

Consequently `Y` is not Bloch semiregular; its kernel has dimension at least eight. One may take `A=E^4` for a CM elliptic curve.

*Proof.* Put `I=I_Y`. The twisted Koszul sequence is

\[
0\longrightarrow L^{-1}\longrightarrow\mathcal O_A^{\oplus2}
 \longrightarrow I\otimes L\longrightarrow0.
\]

Because `K_A=O_A`, Kodaira vanishing gives `H^j(A,L)=0` for `j>0`; Serre duality gives `H^j(A,L^{-1})=0` for `j<4`. Hence

\[
H^2(A,I\otimes L)\simeq H^2(A,\mathcal O_A)^{\oplus2}.
\]

The restriction sequence `0->I tensor L->L->L|Y->0` now gives `H^1(Y,L|Y)=H^2(A,I tensor L)`, of dimension `2 binom(4,2)=12`. Transversality gives `N_{Y/A}=(L|Y)^{oplus2}`, of dimension 24 in first cohomology. The Bloch target for codimension two has dimension `binom(4,3)binom(4,1)=16`. Apply rank--nullity. ∎

This does not conflict with results about complete intersections in projective space, where the ambient coherent cohomology is different. The actual 032 source is not presented as a complete intersection in its product of CM abelian varieties in the first place.

The graph construction does give a regular embedding: choose `j:Y->P^M` and take `(f,j):Y->A x P^M`. For a rigid source, however, the injection in S-04 persists. Its normal sequence begins `0->T_Y->f^*T_A oplus j^*T_{P^M}->N_graph->0`. Since `H^1(T_Y)=0`, the `H^1(f^*T_A)` summand injects into `H^1(N_graph)`. If `f(Y)` generates `A`, every nonzero deformation of the abelian factor has a nonzero graph obstruction. Thus graph semiregularity plus preservation of the **entire graph class** would again force the abelian factor to have no infinitesimal movement. The extra projective factor repairs the embedding premise, not the Route-2 Hodge-class premise.

## 14. A primary-source no-go for a pure Weil character in the coherent-sheaf case

**S-12 (polarization data cannot simply be discarded; checked).** Let `A_0` be a projective member of Voisin's marked four-dimensional `Q(i)`-Weil torus family: the lattice has a `Z[i]` action and both eigenspaces in `H^{1,0}` have dimension two. Let `0 != t` be a rational Weil class. There is no fully Buchweitz--Flenner-semiregular coherent sheaf `F` on `A_0` with

\[
\operatorname{ch}_1(F)=\operatorname{ch}_3(F)=0,
\qquad \operatorname{ch}_2(F)=t.
\tag{S12}
\]

The rank and top-degree character are unrestricted.

*Proof.* Work in the smooth marked family of unpolarized Weil tori through `A_0`, described in Voisin §3, equations (3.1)–(3.8), pp. 1066–1067. Lemma 3.1 proves that the whole rational Weil space remains of type `(2,2)` on this family. Hence all components with indices `I={1,2,3}` in (S12) extend horizontally with the required Hodge types. In dimension four the full semiregularity target is precisely the product with these indices. If `F` were semiregular, Buchweitz--Flenner Theorem 5.1, pp. 174–175, and its proof on p. 179 give a coherent flat sheaf in a neighborhood of the central parameter, with these same horizontal Chern components. Voisin Proposition 3.2, pp. 1069–1071, and Proposition 2.1, p. 1059, show that a very general torus in this family has `NS=0` and that every coherent analytic sheaf on it has `c_2=0`. The exceptional loci form a countable union of proper closed analytic loci; every sufficiently small parameter neighborhood contains such a very general point. On that fiber both `c_1=0` and `c_2=0`, so `ch_2=(c_1^2-2c_2)/2=0`, contradicting the nonzero horizontal class `t`. ∎

Primary source: Claire Voisin, *A counterexample to the Hodge conjecture extended to Kähler varieties*, IMRN 2002 no. 20, 1057–1075, `https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/hodgeimrn.pdf`. The correct published locators are Theorem 1.1, Proposition 2.1, Lemma 3.1 and Proposition 3.2; a circulating preprint version numbers the headline theorem differently.

**Scope.** This theorem is stated for coherent sheaves and the indicated fourfold Weil family. It does not extrapolate to every CM field or dimension. For arbitrary perfect complexes the same contradiction would require an analytic effectivity theorem for the formal perfect-complex deformation in this nonprojective family. The algebraic/formal Pridham result below alone is not that theorem, so this report does not claim the perfect-complex extension. Keeping a nonzero polarization term as in (S9b) avoids this particular contradiction: its Hodge locus confines the deformation to polarized tori, on which Voisin's `NS=0` conclusion does not apply.

## 15. Exact all-order perfect-complex lifting statement available from Pridham

The checked primary version is J. P. Pridham, *Semiregularity as a consequence of Goodwillie's theorem*, arXiv:1208.3111v4 (4 November 2024), 22 pp., `https://arxiv.org/pdf/1208.3111` (also the author's `semireg2.pdf`). The relevant locators are Corollary 2.22, p. 18; Corollary 2.25, pp. 19–20; Remark 2.27, p. 20; and Remarks 2.28–2.29, pp. 20–21.

In the specialization needed here, take a smooth proper scheme `X` over a local Artinian complex algebra `R`, a square-zero ideal `J`, and a perfect complex `F` on `X_(R/J)`. Corollary 2.25 identifies the image of its obstruction under the semiregularity map followed by the inclusion into truncated de Rham cohomology with the failure of the topological Chern class to lie in the relevant Hodge filtration. Remark 2.27 supplies the needed injectivity of that inclusion from degeneration of Hodge--de Rham. Thus if the relevant Chern components remain Hodge, those components of the obstruction's semiregularity image vanish. An injective partial or full semiregularity map then forces the obstruction itself to vanish. Factoring nilpotent extensions into small extensions and applying base change gives compatible formal lifts to all orders.

This is an all-obstruction statement for perfect complexes, not merely a curvilinear one. Remark 2.28 gives the morphism-to-perfect-complex obstruction map `psi_f`; Remark 2.29 recovers Bloch's map for a codimension-`p` locally complete intersection. Formal existence, analytic/algebraic effectivity, and properness or boundedness of a parameter space remain separate steps. For ordinary coherent sheaves the analytic effectivity needed in S-12 is already explicitly supplied by the proof of Buchweitz--Flenner Theorem 5.1; for an arbitrary perfect complex it should be cited separately when used.

