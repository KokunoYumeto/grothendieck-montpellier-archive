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


## 16. A single exponential polarization term still fails for coherent sheaves

**S-13 (checked).** In S-12, take a polarization $L$ whose Rosati involution induces conjugation on $\mathbf Q(i)$ and set $\theta=c_1(L)$. For any integer $a$ and nonzero rational $\lambda$, a coherent sheaf with

\[
\operatorname{ch}(F)=r e^{a\theta}+\lambda t+c[\mathrm{pt}]
\]

cannot be fully semiregular.

*Proof.* The Rosati condition places $\theta$ in the mixed component $V_\sigma\otimes V_{\bar\sigma}$ of $\bigwedge^2H^1(A,\mathbf C)$. The Weil space is $\bigwedge^4V_\sigma\oplus\bigwedge^4V_{\bar\sigma}$, and each eigenspace has dimension four. Therefore $\theta t=0$. Twisting by the actual line bundle $L^{-a}$ preserves coherence and, as a Fourier–Mukai autoequivalence, full semiregularity. Its Chern character is $r+\lambda t+c[\mathrm{pt}]$. S-12 excludes it. ∎

This proves a precise limitation of adding polarization data: one exponential is removed by a line-bundle twist and does not help. The argument does not exclude arbitrary polarization polynomials, and it does not extend the coherent-sheaf no-go to arbitrary perfect complexes.

## 17. Perry's equivariant theorem gives a smaller exact bounded-division gate

The primary source is Alexander Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511v2, dated 24 June 2026, 29 pages, https://arxiv.org/pdf/2604.00511. Its exact relevant statements are Theorem 1.2, p. 3; Definition 2.6 and Lemma 2.7, pp. 5–6; Remark 2.3 and Remark 2.5, p. 5; Theorem 4.1, pp. 10–11; and the proof of Theorem 1.2, pp. 26–28. The source version was checked from the PDF cover, not inferred from a search snippet.

**S-14 (conditional bounded-division corollary; checked).** Let $\pi:A\to S$ be an abelian scheme over a smooth irreducible finite-type complex algebraic variety, fix a relatively very ample line bundle $H$, put $\theta=c_1(H)$, and let $t$ be a global flat codimension-$p$ rational Hodge class. Suppose that on one fibre $A_0$ there are:

1. A finite subgroup $G\subset A_0\times A_0^\vee$ with a specified coherent action on $\operatorname{Perf}(A_0)$ by translations and tensoring by line bundles.
2. A weakly $G$-semiregular perfect complex $E_0$ with $\operatorname{Ext}^{i}(E_0,E_0)=0$ for every $i<0$.
3. An algebraic $B_0\in H^2(A_0,\mathbf Q(1))$, $\lambda\in\mathbf Q^\times$, and $P\in\mathbf Q[x]$ for which the **full** equality

\[
e^{B_0}\operatorname{ch}(E_0)=\lambda t_0+P(\theta_0)
\tag{S14}
\]

holds in even rational cohomology.

Then the signed integral complexity $c_t(s)$ of DIV1 is uniformly bounded on all of $S$. In detail, one integer $C$ bounds both the positive integer multiplier $N_s$ and the $H$-degrees of two effective integral cycles whose difference represents $N_st_s$, for every complex point $s$.

This also gives a common multiplier on the entire family: set $N=\operatorname{lcm}(1,\ldots,C)$ and multiply each fibre's cycles by $N/N_s$. The common degree bound $D=NC$ then works for representatives of $Nt_s$ on every fibre.

*Proof.* The full class $w=\lambda t+P(\theta)$ is a global flat Hodge section extending $e^{B_0}\operatorname{ch}(E_0)$. Perry Theorem 1.2(2) makes $w_s$ algebraic on **every** fibre. The class $P(\theta_s)$ is algebraic, so division by $\lambda\ne0$ gives algebraicity of $t_s$ on every fibre. DIV1(2) now supplies a uniform bound. A concrete sufficient form of hypothesis 2 is a specified equivariant structure for which the full map $\sigma_{E_0}$ is injective on $\operatorname{Ext}^2(E_0,E_0)^G$, along with the negative-Ext vanishing: Definition 2.6 and Lemma 2.7 imply the weak version in characteristic zero. ∎

The proof uses no properness assertion for a moduli space of complexes. Perry supplies all-fibre algebraicity, and DIV1 provides bounded division. The bound is existential. The theorem concerns a finite subgroup of the **target** translation and degree-zero line-bundle group, with coherence data; an arbitrary deck group of a source surface is not automatically such a subgroup.

This is genuinely smaller than the original geometric gate. It permits a perfect complex rather than a smooth embedded surface, an algebraic central $B$-field rather than an untwisted character, and semiregularity only in an equivariant category. The remaining requirements are still substantive: a representative of the projected K-class must have no negative self-Ext, a compatible equivariant structure, the displayed full character, and injectivity on invariant degree-two self-Ext (or the weaker categorical condition). The K-theory projector S-09 does not prove these requirements.

Perry Theorem 6.3 does allow broader categorical group actions, but adds hypotheses on geometric origin of the invariant category and on a lift of the topological K-class section. The proof of Theorem 1.2 verifies these hypotheses for the stated finite subgroups of $A_0\times A_0^\vee$; they must not be dropped when applying the general theorem to a deck group.

## 18. What source-cover symmetry does and does not provide

**S-15 (canonical-lift obstruction; checked).** Put $E=Rf_*\mathcal O_Y$ for a proper map from a smooth projective source to an abelian variety.

For a finite étale Galois source cover $\rho:Y'\to Y$ with group $K$, the natural action on $E'=R(f\rho)_*\mathcal O_{Y'}$ is an internal action over the identity of the target. Under the trivial categorical action of $K$ on $\operatorname{Perf}(A)$, the canonical lift can be semiregular only if $E$ is fully semiregular. Indeed,

\[
(E')^K=Rf_*(\rho_*\mathcal O_{Y'})^K=Rf_*\mathcal O_Y=E.
\]

The invariant category for the trivial action is the finite product of copies of $\operatorname{Perf}(A)$ indexed by the irreducible representations of $K$. The trivial-representation component of the canonical lift is $E$. Both degree-two self-Ext and the Hochschild semiregularity map split by these factors, so a kernel for $E$ remains a kernel in the canonical equivariant lift. Also, $f\rho k=f\rho$ forces any translation satisfying this geometric equivariance to be zero, since a nonzero translation fixes no point.

There is a genuine special case producing target tensor symmetries. Suppose the cover is the pullback of an isogeny $q:A'\to A$, so $Y'=Y\times_A A'$. Let

\[
G=\ker(q^*:A^\vee\to(A')^\vee)\subset A^\vee,\qquad
R=q_*\mathcal O_{A'}=\bigoplus_{P\in G}P.
\]

The multiplication of this finite étale algebra supplies coherent isomorphisms $P\otimes Q\simeq PQ$ and hence a tensor action of $G$. Equivariant objects are equivalently $R$-module objects, giving $\operatorname{Perf}(A)^G\simeq\operatorname{Perf}(A')$. The canonical equivariant lift of $q_*q^*E=R(f\rho)_*\mathcal O_{Y'}$ corresponds to $q^*E$ under this equivalence.

This canonical construction still cannot eliminate an existing full kernel. Adjunction identifies the pullback on degree-two self-Ext with the map

\[
\operatorname{Ext}^2_A(E,E)
\longrightarrow\operatorname{Ext}^2_A(E,E\otimes R).
\]

The unit $\mathcal O_A\to R$ is split by $(\deg q)^{-1}\operatorname{Tr}_q$, so this map is injective. Perry Remark 2.3 gives naturality of the full semiregularity morphism for $q^*$, hence an injection

\[
\ker(\sigma_E)\hookrightarrow\ker(\sigma_{q^*E}).
\]

Thus the canonical equivariant lift in this target-induced case can be semiregular only if the original object is.

The qualification **canonical** matters: weak equivariant semiregularity is existential over possible equivariant structures. S-15 does not exclude all relinearizations or all new objects with the same K-class. It shows that the two automatic cover constructions do not supply the needed repair. It also concerns the full object semiregularity kernel; S-06 only supplies a kernel of the composite map-level obstruction map and therefore cannot by itself be substituted into this conclusion.

## 19. Independent source confirmation and the analytic scope still open

Perry Remark 2.3 states functoriality of the semiregularity morphism on the **entire mapping complex**, not only on an obstruction-evaluation image. Remark 2.5 identifies its degree-two part with Buchweitz–Flenner after HKR. An equivalence induces isomorphisms on mapping complexes and Hochschild homology, independently confirming the full-kernel invariance in S-10. The raw versus Todd-modified HKR convention does not affect the kernel statement, and for abelian varieties the tangent bundle is trivial and the Todd class is one.

The arbitrary-perfect-complex extension of S-12 remains unproved here. Zhaoting Wei, *Deformations of cohesive modules on compact complex manifolds*, arXiv:2308.01266v2 (4 September 2023), Definition 1.1, Theorem 1.1 (= Theorem 3.11), and §5 do provide analytic deformation and Kuranishi results for objects of the derived category. Their displayed family is over the **fixed** product $X\times\Delta$. The theorem was not verified in the relative form where the complex structure of $X$ varies, which is required for the unpolarized Weil-torus contradiction. Likewise the Buchweitz–Flenner lecture notes on deformation theory, §5.5, treat complexes with specified coherent terms; this does not by itself supply the needed relative analytic effectivity for an arbitrary perfect complex. Perry's theorem resolves the algebraic-family gate S-14, but is not an analytic theorem for Voisin's nonprojective torus family.

## 20. Vector-bundle realization is available, but does not supply semiregularity

**S-16 (checked).** On a smooth projective variety $X$ with an ample line bundle $L$, any integral K-class $\xi$ has an actual vector-bundle representative after adding a single polarization exponential:

\[
[V]=\xi+r[L^{-m}],\qquad m,r\geq1.
\]

*Proof.* Write $\xi=[U]-[W]$ for vector bundles, using finite locally free resolutions and grouping terms by parity. For sufficiently large $m$, the bundle $W\otimes L^m$ is globally generated. The exact primary ampleness criterion is Stacks Project Proposition 28.27.13(7)–(8), Section 28.27, tag 01PR, https://stacks.math.columbia.edu/tag/01PR. Choose a finite surjection $\mathcal O_X^{\oplus r}\to W\otimes L^m$ and let $K$ be its kernel. The target is locally free, so the surjection splits locally and $K$ is locally free. Tensoring by $L^{-m}$ gives $[K\otimes L^{-m}]=r[L^{-m}]-[W]$. Now take $V=U\oplus(K\otimes L^{-m})$. A redundant zero generating section makes $r\geq1$ if necessary. ∎

Applied to the integral K-class from S-09, this yields a bundle with $\operatorname{ch}(V)=r e^{-m\theta}+\lambda t$. In S-13's fourfold setting and with $\lambda t\ne0$, such a bundle is necessarily **not fully semiregular**. Thus the difficulty is not simply realizing the corrected K-class by a coherent object. The trace-injectivity condition is an independent, obstructed requirement. S-16 does not rule out weak equivariant semiregularity, which remains the more flexible S-14 gate.

## 21. A nonzero-rank perfect deformation has an ordinary tensor–determinant representative

**S-17 (proved, conditional on the successful deformation).** Let $F$ be a weight-one perfect complex of positive virtual rank $r$ on a finite Kummer gerbe $\mathcal X\to X$. Then

\[
F^{\otimes^{\mathbf L}r}\otimes\det(F)^{-1}
\]

has weight zero and descends to an ordinary perfect complex $K$ on $X$. The determinant exists for arbitrary perfect complexes by Knudsen–Mumford, *The projectivity of the moduli space of stable curves I*, Theorem 2, p.42; its base-change property is part of the extended determinant definition on pp.40–42. The determinant of a weight-one complex has inertia weight equal to its alternating rank $r$, so the two weights cancel. Étale descent of the weight-zero category gives the asserted perfect complex on the base.

For the Perry deformation in S-14 with full normalized character $w=P(\theta)+\lambda t$, $P(0)=r>0$, $n\ge2$, and $\theta t=0$, put $p_1=[x]P(x)$. Then

\[
\operatorname{ch}(K_0)=e^{-w_1}w^r,
\qquad
\operatorname{ch}(K_s)_{\le n}
=\bigl(e^{-p_1\theta_s}P(\theta_s)^r\bigr)_{\le n}
  +r^r\lambda t_s.
\]

The central B-field cancels exactly: $\operatorname{ch}(E_0)^r e^{-c_1(E_0)}=e^{-w_1}w^r$. The coefficient is $rP(0)^{r-1}\lambda=r^r\lambda$. Higher terms such as $t^2$ do not enter codimension $n$. A negative virtual rank is made positive by shifting the existing deformation. This argument does not handle rank zero; root's DER4 Adams construction does.

The remainder is constructive. Over a smooth affine deformation neighborhood, Stacks Lemma 36.37.2, tag 0F8F, gives a bounded bundle presentation. The relative proof of S-16 adds $R[H^{-m}]$ to realize $[K]$ by an actual bundle. Add $a$ trivial summands to make its rank at least $n$ and twist by $H^k$ to make it globally generated. Through codimension $n$ the resulting character is $Q(\theta)+\mu t$, where

\[
Q(x)=e^{kx}\bigl(e^{-p_1x}P(x)^r+R e^{-mx}+a\bigr),
\qquad \mu=r^r\lambda.
\]

Set $C_n=[u^n]\exp(\sum_{j=1}^n(-1)^{j-1}(j-1)![x^j]Q(x)u^j)$ and $\beta=(-1)^{n-1}(n-1)!\mu$. A general degeneracy cycle represents $c_n=C_n\theta^n+\beta t$; it is nonempty because its Weil component is nonzero. Fulton Theorem 14.4 and Examples 14.4.2–3, pp.254–256, supply the effective cycle. Thus $C_n>0$. If $v=\int\theta^{2n}$ and $d$ clears the two coefficients' denominators, the fixed integers

\[
N=|d\beta|,\qquad D=dC_nv
\]

give signed effective representatives of $Nt$ with both degrees $D$. The fixed-$N$, fixed-$D$ proper-image argument in DIV1 extends these identical constants from the dense open image to every fibre. All details, including the determinant descent and coefficient calculation, are in the full S-17 proof in `semireg_t7_proofs.tex`. The transformation is made **after** deformation; its output need not be semiregular.

## 22. Canonical categorical induction cannot remove a full kernel

**S-18 (proved).** Let a finite group act coherently by exact autoequivalences on a smooth proper complex linear enhanced category $\mathcal C$, with smooth proper equivariant category $\mathcal C^G$. Canonical induction has underlying object $\bigoplus_{g\in G}gE$ and maps a morphism $u$ to the block diagonal map $\bigoplus_g g(u)$. The identity summand recovers $u$ by inclusion and projection. Hence induction is injective on every morphism space, including self-$\operatorname{Ext}^2$.

Perry Remark 2.3, p.5, gives functoriality of the entire semiregularity morphism. Therefore

\[
\ker\sigma_E\hookrightarrow\ker\sigma_{\operatorname{Ind}(E)}.
\]

This applies to actions combining target translations and tensoring by degree-zero line bundles. It improves the automatic source-cover test S-15 but retains the necessary qualification: the **canonical induced lift** is not semiregular when the original kernel is nonzero. A different equivariant structure on the same underlying object is not excluded; weak equivariant semiregularity in Perry Definition 2.6 is existential over lifts. The complete elementary proof is in the S-18 LaTeX proposition.

## 23. Independent checks of the replacement-object tests DER1–DER6

The complete proofs of root's DER1–DER4 in `derived_candidates.md` and DER5–DER6 in `derived_functors.md` have been independently read and checked. Actual targeted checks and limitations are recorded in `CHECK_EVENTS_semireg.tsv`.

The decisive strengthening is DER5: convolution by any perfect $F$ with $\chi(F)\ne0$ is faithful on every morphism space. Mukai's original equation (3.7), p.160, including its complete proof, was inspected in the scan: Fourier–Mukai sends convolution to tensor product without a shift in this direction. The transformed kernel has virtual rank $\chi(F)$; coevaluation followed by graded trace is multiplication by that nonzero rank, which proves injectivity. In particular $\Phi_{\mathcal I_\Delta}=(-)*\mathcal I_0$ and $\chi(\mathcal I_0)=-1$ for every positive-dimensional abelian variety. Thus the evaluation cone preserves an existing full semiregularity kernel for **every perfect input**, without the global-generation or higher-cohomology assumptions used in the earlier DER2 proof.

DER4 passed the central-gerbe sign check independently using Hotchkiss, arXiv2212.10638v1, Lemma 4.6, p.15, and Definition 4.16, p.18. A positive tautological root has Chern class $B$; applying the band-order Adams operation gives the descended central class $\psi^M(E_0)\otimes L_0$, hence the coefficient $M^n\lambda$. The source expression $\exp(-/n)$ uses a dash for the argument and does not insert a negative sign. The integral Newton homogeneity, weight-zero descent, relative bundle realization, effective Chern cycle and exact fixed-$N$ closure all pass. The explicit bound is conditional on a successful initial S-14 object and on finite chosen generation twists; it is not a uniform estimate from the original 032 level.


## 24. What Markman's genus-three calculation uses, and the quantitative genus-four failures

The qualitative fourfold adjunction test and the failure of the ample imaginary-quadratic secant characters are prior results: rStation paper 37, version 4 (24 October 2026), Theorems A–C and its free-translation variant Theorem B_G. We verified the conventions against the supplied 032 trace calculation. The quantitative applications below are the present checks of the supplied May 2025 Markman constructions; no novelty is claimed for the qualitative failures.

The genus-three mechanism uses the exact invariant self-Ext calculation. In the supplied Markman source, Lemma 8.3.2 computes ext1 of an orbit union of n disjoint Abel–Jacobi curves as 3n+3. Calabi–Yau threefold duality gives the same ext2; Lemmas 8.3.7–8.3.8 and Proposition 8.3.9 identify the evaluation image, whose invariant part has dimension six. Corollary 8.3.12 identifies its kernel with the annihilator of the Chern character. Lemma 8.4.1 and Lemma 9.3.2 pass to the product: the invariant degree-two space has dimensions 6+6+36=48. This exact computation, together with the equivariant descent, supplies semiregularity. It cannot be transplanted by replacing genus three with genus four: Serre duality then pairs Ext2 with itself, and the positive Euler characteristic changes the dimension equation.

**S-19 (checked).** In Example 8.2.3, set ell=d+1 and quotient the first cyclic construction by the translation group of order ell. The quotient ideal E has 2d isolated points. Its Euler pairing is 8d. At a reduced isolated point in a regular four-dimensional local ring, Ext1(m,m) has dimension four. The rank-one unit–trace splitting gives

\[
\operatorname{Ext}^1(E,E)=H^1(\mathcal O)\oplus H^0(\mathcal Ext^1(E,E)),
\quad e_1\ge4+8d,
\quad e_2=8d-2+2e_1\ge24d+6>28.
\]

Thus the full semiregularity target of dimension 28 cannot receive it injectively, for any d, including d=1. Simplicity makes every linearization differ by a character, so the conclusion covers every linearization for this specified cyclic action. It also covers the conjugated translation–tensor action after the theta twist. It does not identify arbitrary source-cover symmetries with target symmetries.

**S-20 (checked).** The partial-normalization complex in the same example has cohomology I in degree zero and a zero-dimensional Q in degree one. Purity of the finite normalization pushforward implies Hom(Q,D0)=0; codimension two implies Hom(D0,O)=Ext1(D0,O)=0. The truncation and defining triangles therefore show that the complex is gluable and simple. Normalizing four points for each pair adds 4 binom(ell,2)=2d ell point classes, so it has the same Chern character as the first construction. Its quotient has Euler 8d and rank one, whence e1≥4 and e2≥8d+6. The Chern contraction rank is 12. If m=e2 and a=rank(sigma)=rank(ob), then 12≥2a−m, yielding

\[
\dim\ker\sigma\ge(m-12)/2\ge4d-3>0.
\]

All linearizations for the stated free cyclic action fail. External products with a nonzero perfect object and subsequent derived equivalences preserve these particular full kernels. These operations do not establish failure for a different replacement object.

### Detailed S-20 convention verification retained for checking, not presented as a new criterion

The following is the complete calculation that was removed from the paper fragment after the prior-work identification. It verifies the normalization and the exact rank needed for the quantitative application.

```latex
First we check the adjunction in (S20.1). Fix a nonzero volume
form on $Y$. Serre duality gives a perfect pairing on
$\operatorname{Ext}^2(E,E)$, while contraction and integration
give the perfect pairing
\[
 HT^2(Y)\otimes H\Omega^{-2}(Y)\longrightarrow\mathbf C.
\]
Indeed its $p$-th block pairs
$H^{2-p}(\wedge^pT_Y)$ with $H^{p+2}(\Omega_Y^p)$,
for $0\le p\le2$.
The evaluation identity (5.21) in the supplied 032 companion
is $\operatorname{ob}_E(\xi)=\xi\mathbin{\lrcorner}
\exp(a_E)$. Its equations (5.20) and (5.24), or directly the
definition of perfect trace with coefficients, then give
\[
 \int_Y\operatorname{Tr}
       \bigl(\operatorname{ob}_E(\xi)\circ u\bigr)
   =\langle\xi,\sigma_E(u)\rangle,
 \qquad u\in\operatorname{Ext}^2(E,E).
\]
The volume form is implicit in the integral. Both morphisms
have degree two, so no odd exchange sign is introduced.
The factorial in each block is the same $1/p!$ in evaluation
and in the trace map. Thus $\sigma_E$ is the transpose of
$\operatorname{ob}_E:HT^2(Y)\to\operatorname{Ext}^2(E,E)$.
In particular injectivity of $\sigma_E$ is equivalent to
surjectivity of $\operatorname{ob}_E$.
The entire identity
$\sigma_E\operatorname{ob}_E=c_E^2$ is Proposition~5.1,
equation (5.9), of that companion; it also appears in Markman's
extended diagram preceding Lemma~8.3.4. The tangent bundle
is trivial, so its Todd correction is one.
If $\sigma_E$ is injective, the two observations imply
(S20.1). This fourfold criterion was also stated previously
as Theorem~A of the rStation paper~37, version~4, cited in the
source ledger; the argument here checks its conventions
against the supplied primary trace calculation.

We next compute the contraction rank. Put
$U=H^1(Y,\mathcal O_Y)$ and $T=H^0(Y,T_Y)$, and choose
dual bases so that a nondegenerate rational polarization
class is $\theta=\sum_{i=1}^4 x_i\wedge y_i$, with
$x_i\in H^0(\Omega_Y^1)$ and $y_i\in U$.
Let $s^2=-d$ and
\[
 w=\alpha+\beta
   =c_+e^{s\theta}+c_-e^{-s\theta},
 \qquad c_\pm=\frac{1\pm1/s}{2}.
\]
For
$\xi=(\eta,M,\nu)\in\wedge^2U\oplus(U\otimes T)
\oplus\wedge^2T=HT^2(Y)$, set
\[
 A=M\mathbin{\lrcorner}\theta\in\wedge^2U,
 \qquad B=\tfrac12\nu\mathbin{\lrcorner}\theta^2
             \in\wedge^2U,
 \qquad D=\eta-dB.
\]
The map $M\mapsto A$ is surjective and $\nu\mapsto B$ is
an isomorphism. The contraction convention is the one fixed
in (5.3) of the companion; reversing the bivector convention
merely changes the variable $B$ by its negative.
Exterior differentiation of the exponential gives
\[
 \xi\mathbin{\lrcorner}e^{\pm s\theta}
      =(D\pm sA)e^{\pm s\theta}.
\]
It follows that the first two Hodge blocks of
$\xi\mathbin{\lrcorner}w$ are
\[
 D+A,\qquad\theta\wedge(D-dA).
\]
The map $\theta\wedge:\wedge^2U\to H^3(\Omega_Y^1)$
is injective: if $\theta\wedge\gamma=0$, independence of
the $x_i$ gives $y_i\wedge\gamma=0$ for every $i$, hence
$\gamma=0$. The coefficient matrix on $(D,A)$ has
determinant $-(d+1)\ne0$. These two blocks therefore already
have rank twelve. Every block factors through the same two
six-dimensional spaces, so the full contraction rank is
exactly twelve.

The same rank holds for $e^{b\theta}w$, for any rational $b$.
Indeed the substitution
\[
 \eta' =\eta+bA+b^2B,\qquad A'=A+2bB
\]
is an invertible shear together with the unchanged variable
$B$, and reduces the two exponential slopes $b\pm s$ to
the preceding calculation after the invertible multiplication
by $e^{b\theta}$ on the target. This observation applies on
the quotient with the rational polarization whose pullback
is the original principal class.

```


## 25. S-21: arbitrary effective finite target actions

The all-group extension is now written and checked in the TeX fragment. Let G be a finite effective subgroup of A×Ahat with a specified coherent translation–tensor action on Perf(A), where dim(A)=4. For every nonidentity element, its Hochschild coefficient sector vanishes: a nonzero translation has graph disjoint from the diagonal, and a nontrivial degree-zero tensor factor has no cohomology. Perry 2018 Theorem 4.4 and Remark 4.5 therefore identify the invariant category's Hochschild cohomology with that of A.

The invariant category is smooth proper by Bayer–Perry, Proposition 3.15, author PDF pp20–21; its entire proof has now been read. The ordinary invariant volume form gives its Serre functor [4]. Perry 2018 Definition 6.1 and Remark 6.2 then give equality of Hochschild homology dimensions. If F and I are forgetting and induction, additivity and FI=direct sum of the group actions give F_*I_*=|G|. Equal dimensions make F_* an isomorphism in degrees zero and minus two, and I_*F_*=|G| as well. Categorical Riemann–Roch, in Shklyarov Theorem 3.5 and its Hom formulation (3.7), (3.9), gives the exact identity

\[
\chi_A(E,E)=|G|\chi_{\operatorname{Perf}(A)^G}(\widetilde E,\widetilde E).
\]

The restricted Serre transpose identity and the full forgetful trace diagram imply that semiregularity of the lift forces e2_G=rank(c2), while e1_G≥rank(c1). For an imaginary-quadratic secant character e^B ch(E)=a alpha+b beta, the exact ranks are 12 and 8. The Euler pairing is 8d(da²+b²) integral(theta^4)/24>0. Thus, assuming only equivariant negative self-Ext vanishing,

\[
 e_0^G\ge2+\frac{\chi_A(E,E)}{2|G|}>2.
\]

In particular, the lift cannot be simple in the invariant category; no simplicity of the underlying object is required. The statement covers arbitrary coherent mixtures of translations and degree-zero tensor products, rather than only the free-translation Fourier–Mukai models covered in the earlier result. It does not refute general corrected characters on the final Weil eightfold, nor arbitrary non-effective actions with a nontrivial identity-functor kernel.

The same proof supplies a reusable numerical condition for *any* character, not just a secant one:

\[
\frac{\chi_A(E,E)}{|G|}-2e_0^G+2\operatorname{rank}(c_E^1)
\le\operatorname{rank}(c_E^2),
\]

provided the lift is fully semiregular and has no negative invariant self-Ext. This is the all-effective-target-action version of the CY4 test and is the next-object filter.


## 26. S-22: the balanced RM character passes the numerical test but has no rank-one torsion-free realization

The numerical example in the real-multiplication remark of rStation37 is

\[
v_q=\cos(\sqrt q\,\theta_1)\cos(\sqrt q\,\theta_2)
=1-\frac q2(\theta_1^2+\theta_2^2)
 +\frac{q^2}{4}\theta_1^2\theta_2^2.
\]

Here the two complex tangent eigenspaces of the real quadratic field each have dimension two. The pure-spinor definition is Markman, arXiv:2509.23079, §11.2.1, pp40–41; at q=1 this is exactly (alpha+tildealpha)/2. Its ranks (8,18) and positive Euler pairing 4Dq² are compatible with the simple CY4 numerical test in the principal q=1 rank-one case. That compatibility alone does not produce a sheaf.

**Effectivity obstruction.** No nonzero effective surface class lies in the real span of theta1² and theta2² for this genuine field action. Every mixed holomorphic two-form omega in V1* tensor V2* has zero pairing omega wedge conjugate(omega) with either class. Positivity on an effective cycle forces all such forms to vanish on each component. Its tangent bivector then has no mixed part. A decomposable bivector in wedge²V1 plus wedge²V2 must lie in one summand (its square is twice the product of the two summands), so every tangent plane equals one eigenspace. Irreducibility makes that choice constant. On a resolution, every one-form annihilating the chosen eigenspace pulls back to zero. The induced Albanese homomorphism has positive-dimensional image with tangent space in that eigenspace. This is impossible: a nonrational element of the real quadratic field acts by an irrational scalar on it, whereas every positive-dimensional abelian subvariety has nonzero rational homology. This argument does not assume A simple.

For a rank-one torsion-free sheaf E, the double dual is a line bundle L and L/E has an effective leading codimension-two cycle. If e^B ch(E)=v_q, the first Chern equation gives c1(L)=−B and that leading cycle would have class q(theta1²+theta2²)/2. Its theta-degree is 4Dq>0, contradicting the preceding argument. Therefore the numerically eligible rank-one candidate is not the character of any pure rank-one sheaf.

The factorization also makes the contraction ranks transparent: each formal complex two-dimensional factor has ranks 1,4,1 in degrees 0,1,2. The fourfold ranks are therefore 8 and 1+16+1=18. For a scalar multiple Nv_q and any effective finite coherent target action, a gluable equivariantly simple semiregular lift would necessarily have

\[
\chi_G=4Dq^2N^2/|G|\in\{2,4\},\qquad
|G|\in\{Dq^2N^2,2Dq^2N^2\}.
\]

The two values follow from e2_G=18, e1_G≥8, e0_G=1 and CY4 duality; the positive Euler characteristic must be even. Thus the nonequivariant integral-polarization case with q=1 forces D=N=1, precisely the rank-one pure-sheaf case already excluded. This leaves higher-rank equivariant objects with those restricted group orders and derived objects that are not pure sheaves. It does not answer Markman's broader Question11.2.2, which asks only restricted semiregularity of a different character in the RM space.

## 27. S-23: full semiregularity permits a nilpotent endomorphism algebra

The object O_A direct sum O_p is a useful exact control. Its self-Ext dimensions are (3,8,12,8,3), Euler2, and it is fully semiregular. The degree-two cross groups vanish. The structure sheaf has trace image H²(O_A); the skyscraper has trace image H⁴(Omega²_A). The second assertion follows from the Koszul evaluation of bivectors and 032 Proposition5.1: bivectors map isomorphically to its six-dimensional Ext2 and contraction with [p] is an isomorphism onto H⁴(Omega²). These two trace images are disjoint, so the sum is injective. The endomorphism O_A→O_p provides a nonzero square-zero element in a three-dimensional triangular algebra.

Consequently there is no general implication from full semiregularity to simplicity, endomorphism dimension at most two, or a semisimple endomorphism algebra. This example lies outside the imaginary-quadratic character plane. It explains why the remaining equivariantly nonsimple gate cannot be dismissed using only an abstract CY4 statement.

## 28. S-24: all iterated self-extensions of the positive-Euler seed fail

This result addresses nonsplit extensions, rather than only direct sums. Fix a heart in Perf(A)^G and an object Ftilde in it with End(Ftilde)=C, the imaginary-quadratic secant character, and k=chi_G(Ftilde,Ftilde)≥2. Suppose Etilde has a length-m filtration with every quotient Ftilde. Left exactness of Hom and induction in both variables show that objects with filtration lengths a,b have Hom dimension at most ab. Thus e0_G(Etilde)≤m². K-theory gives chi_G(Etilde,Etilde)=m²k, while scaling the nonzero character leaves contraction ranks (8,12) unchanged.

If Etilde were fully semiregular, the all-group CY4 calculation would imply

\[
12=m^2k-2e_0^G+2e_1^G
\ge m^2(k-2)+16\ge16,
\]

a contradiction. The argument assumes neither a split filtration nor functorial persistence of the original trace kernel. It applies in particular to every iterated self-extension of the actual quotient ideal from S-19, for which k=8d. The hypothesis is scalar endomorphisms, not simplicity as an object of the abelian heart; the latter would not hold for an ordinary ideal sheaf. The fixed action, fixed numerical ray and k≥2 are explicit restrictions. Cones or extensions with constituents of different characters remain open.


## 29. S-25: correlated finite actions also fail on the actual simple secant product

Let F be a simple gluable perfect object on an abelian fourfold X with the ample imaginary-quadratic normalized character. Let K be any simple gluable perfect object on an abelian variety Y. Then no Fourier–Mukai image of F external product K admits a semiregular lift for any effective finite translation–tensor subgroup of the target, including correlated groups that are not products. This is a direct obstruction for the genus-four secant-square eightfold construction, not just for its originally chosen product action. It also applies when the second factor has a different character; therefore a new simple second factor alone cannot repair this full weak-semiregularity gate while the first factor stays on the excluded character plane.

The full proof has five parts.

1. The identity-sector proof from S21 is dimension-independent: on any abelian g-fold the nonidentity sectors vanish, the invariant category is CYg, and induction plus equal Hochschild dimensions makes forgetting an isomorphism on HH_-2. Thus an invariant ordinary full kernel gives an equivariant full kernel.

2. A finite stabilizer subgroup of a simple gluable object can be coherently lifted while fixing that object. Choose functor representatives phi_h and isomorphisms lambda_h:phi_h(Q)→Q. Both the natural multiplication-isomorphism space and its evaluation on Q are scalar torsors. Choose the unique multiplication mu_g,h for which lambda_gh mu_g,h(Q)=lambda_g phi_g(lambda_h). Naturality makes its two associativity composites agree on Q, and faithful scalar evaluation makes them agree as natural transformations. Negative HH and negative self-Ext vanish, so there is no further enhanced coherence obstruction. Bayer–Perry Lemma3.3 and Corollary3.4, pp15–16, provide the precise passage from two-categorical to enhanced actions. This construction changes factor coherence if necessary; it does not assume projective factor cocycles were already trivial.

3. A translation–tensor operation fixing F external product K fixes each factor. This holds for arbitrary simple perfect complexes. Restrict the product isomorphism to a point where the second factor has nonzero derived fiber. Finite complexes of vector spaces split into shifts, so one gets an isomorphism between finite sums of shifts of F and of phi(F). In the composite with its inverse, a diagonal identity of a shift of F is a finite sum of scalar endomorphisms. A nonzero term makes that shift a retract of a shift of phi(F); scalar endomorphisms force the retract to be an isomorphism. A possible shift is zero because translation–tensor operations preserve the least and greatest standard cohomological degrees. Repeat for the second factor.

4. For a correlated group H on the product, apply step2 to its projected stabilizer H_X. S21 supplies a nonzero H_X-invariant full kernel u in Ext2(F,F). The conjugation action is independent of scalar choices. The class u external product id_K is nonzero and remains a full kernel by Perry2026 Remark2.3. Since both factors are gluable and simple, the degree-zero product-isomorphism space is one-dimensional; hence every original product linearization is a scalar times the product of factor isomorphisms. Its conjugation fixes u external product id_K, even when the original factor cocycles cancel only on the product. Step1 converts it into a nonzero equivariant kernel.

5. Orlov Theorem2.10 and Corollary2.13, author PDF pp9–12, identify translation–tensor groups under every derived equivalence of abelian varieties. Thus any finite target action pulls back to one of the correlated actions just considered. The original full proofs and scans of pp11–12 have been read; the conclusion uses the conjugation statement of Corollary2.13, not merely an abstract isomorphism of abelian varieties.

The result retains simplicity and gluability of both factors. It excludes all coherent finite target actions on these fixed products and their derived-equivalent images, rather than only canonical induction or product descent. It does not rule out nonsimple factors, unrelated corrected objects on the final eightfold, or a deformation theorem based on a condition weaker than full weak semiregularity.


## 30. S-26: the remaining RM gate is an exact tangent-space equation

For an equivariantly simple gluable object of normalized character Nv_q, put k=4Dq²N²/|G|. Its full trace is injective if and only if e2_G=18. The forward direction is CY4 adjunction; conversely, sigma composed with evaluation already has rank18, so a degree-two self-Ext space of dimension18 forces trace injectivity. Serre duality gives the exact equivalent condition

\[
e_1^G=10-k/2.
\]

Thus the two cases are k=4 with e1_G=8, or k=2 with e1_G=9. In the principal nonequivariant rank-one case, the task is now to construct a simple gluable non-pure perfect complex with Ext1 dimension eight. All eight tangent directions are already supplied by translation and degree-zero tensor evaluation. This is an exact replacement for the full-trace check, not a claim that the required object exists.

The effectivity proof also restricts cohomological amplitude. If H0 is rank-one torsion free, the object has no negative cohomology, all positive cohomology has codimension at least two, and the positive even-degree cohomology has codimension at least three, the normalized ch2 is the negative of an effective cycle. Hence it cannot be the balanced RM character. In particular amplitude[0,1] objects of this usual torsion-free form fail. Within this form, an allowed derived candidate must have a surface-supported even positive-degree term; amplitude[0,2] is the first remaining possibility.

## 31. S-27: a concrete two-sheaf cone narrows the derived construction problem

Let A,T be coherent sheaves with End(A)=End(T)=C and Ext^i(T,A)=0 for i=0,1,2. A nonzero e in V=Ext3(T,A) defines

\[
A\longrightarrow E_e\longrightarrow T[-2]\xrightarrow{e}A[1].
\]

The cone has H0=A, H2=T, no other cohomology, scalar endomorphisms, and no negative self-Ext. The proof uses only the long exact Hom sequences: all negative pairwise groups between A and T[-2] vanish; endomorphisms induce scalars on the two ends, and the nonzero extension forces them equal, with kernel Ext2(T,A)=0.

There is an intrinsic injection V/Ce into Ext1(E_e,E_e): for the triangle maps i:A→E and p:E→B=T[-2], send v to i[1] v p. The map Hom(E,A[1])→Hom(E,E[1]) is injective because its preceding connecting map sends Hom(E,B)=Cp to e p=0. The kernel of V→Hom(E,A[1]) is Ce by the other long exact Hom sequence. Thus no deformation-effectivity input is needed. Consequently a balanced RM cone in the principal nonequivariant case requires dim V≤9 and is fully semiregular exactly when Ext1 has dimension8.

This supplies a more concrete remaining existence gate: find a rank-one torsion-free A and surface-supported T with the required full character sum, the three displayed Ext vanishings, and a nonzero degree-three extension whose tangent dimension is eight. It leaves the excluded pure-sheaf and amplitude[0,1] forms. No pair satisfying the nonsplit RM character equation and tangent bound has yet been found. We have not claimed that arbitrary K-theory realization produces such a cone.


## 32. S-28: the cone construction has an exact Yoneda tangent criterion

The earlier injection is the first term of an exact sequence. Set B=T[-2] and V=Ext3(T,A), and let

\[
\delta_e:\operatorname{Ext}^1(A,A)\oplus\operatorname{Ext}^1(T,T)
\longrightarrow\operatorname{Ext}^4(T,A),
\qquad (a,b)\longmapsto a[1]e+e[1]b.
\]

The plus sign uses the standard shifted-triangle convention with connecting map minus e[1]. Because Hom(A,B[k]) vanishes for k≤1, each degree-one endomorphism of E induces unique degree-one maps on its two ends. The morphism-of-triangles axiom identifies their image with ker(delta_e). The two exact Hom sequences used for S27 identify the kernel with V/Ce. Therefore

\[
0\longrightarrow V/\mathbf C e\longrightarrow\operatorname{Ext}^1(E,E)
\longrightarrow\ker\delta_e\longrightarrow0.
\]

For the balanced principal nonequivariant character, let rho be the simultaneous HH1 evaluation on A and T and let h=dim ker(rho). The degree-one character contraction has rank8, so HH1 evaluation on E is injective. Its intersection with the fixed-end extension tangent V/Ce has dimension h. Hence h≤dim V−1 and ker(delta_e) contains the 8−h dimensional simultaneous orbit image. The exact sequence and S26 prove the equivalence

\[
E\text{ fully semiregular}\quad\Longleftrightarrow\quad
\dim V=h+1\quad\hbox{and}\quad\ker\delta_e=\operatorname{im}\rho.
\]

In particular, a pair with zero simultaneous infinitesimal stabilizer requires Ext3(T,A) to be one-dimensional, and requires the Yoneda map to have rank ext1(A,A)+ext1(T,T)−8. This is both necessary and sufficient after the full character equation and S27 hypotheses have been met. It replaces the earlier bound dim V≤9 by a precise rank test. No sheaf pair realizing the nonsplit balanced RM character has yet been constructed.


## 33. S-29: transverse surfaces give a two-case cohomology gate

For a concrete rank-one construction on a simple complex abelian fourfold, take smooth connected surfaces Z,S meeting transversely in D, A=I_Z tensor L, and T=i_*M. Put M'=M tensor L^{-1}|S, N=K_S tensor (M')^{-1}, and d=length(D). Regular-immersion duality and the Tor-independent restriction of I_Z give the exact identity

\[
R\operatorname{Hom}_X(T,A)=R\Gamma(S,N\otimes I_D)[-2].
\]

Thus Ext0 and Ext1(T,A) vanish automatically; Ext2, Ext3 and Ext4(T,A) are respectively H0, H1 and H2 of N I_D. The exact duality sources are Stacks Project Lemma48.9.7 (0A9X), Lemma48.10.3 (0E2N), and Lemma48.15.5 (0BQZ); the complete three proofs have been read, including the Koszul shift minus2. Each sheaf has scalar endomorphisms and no infinitesimal translation–tensor stabilizer. For the ideal this follows from the finite translation stabilizer of Z and its line-bundle double dual; for i_*M it follows from the finite stabilizer of S and injectivity of the Picard restriction differential because S generates the simple ambient variety.

For a fully semiregular cone with principal balanced RM character, S28 therefore requires H0(N I_D)=0 and H1(N I_D)=C. Since each end has at least eight tangent directions, the Yoneda target must have dimension at least eight. Serre duality identifies its dimension with h0(M'), so h0(M')≥8. The restriction sequence is then

\[
0\longrightarrow H^0(N)\longrightarrow \mathbf C^d
\longrightarrow\mathbf C\longrightarrow H^1(N)\longrightarrow0.
\]

It follows that exactly two cohomology cases remain:

| Case | h1(M') | h2(M')=h0(N) | Evaluation H0(N)→H0(N|D) |
|---|---:|---:|---|
| 1 | 0 | d−1 | Injective with one-dimensional cokernel |
| 2 | 1 | d | Isomorphism |

The corrected equality is h2(M')−h1(M')=d−1. An earlier exploratory message had the two terms reversed; the complete saved proof uses the displayed exact sequence and the corrected sign. The first two cohomology conditions, full character equality and exact Yoneda rank test in S28 are also sufficient; the section bound is a necessary consequence.

The character equality forces [Z]−[S]=(theta1²+theta2²)/2. The latter class has nonnegative pairing with S. Debarre1995 Examples(1), pp188–189, and Proposition1.4, pp189–190, imply S−S=X in a simple abelian variety, so S² is a positive integer. It is even because the integral cohomology ring is an exterior algebra and every degree-four square has paired cross terms. Therefore d=S²+((theta1²+theta2²)/2)·S≥2.

In particular, an acyclic M' cannot work. If H>0(M')=0, Serre duality gives H0(N)=H1(N)=0, and Ext3(T,A) has dimension exactly d. The exact tangent sequence yields ext1(E,E)≥d+7. Since the balanced Euler pairing is4, ext2(E,E)≥2d+16. The CY4 transpose identity and contraction rank18 then give dim ker(sigma2_E)≥d−1≥1. Thus large positive twists, although convenient for ordinary K-theory realization, cannot solve this cone gate. The remaining candidate must realize one of the two special complementary-canonical cohomology patterns above. No such matching RM pair is asserted to exist.


## 34. S-30: an integral lattice obstruction closes the simple rank-one balanced RM gate

The principal balanced character is numerically eligible over rational cohomology, but it fails an integral-lattice condition for a genuine real quadratic field. This argument is independent of the sheaf-cone ansatz. Let F=Q(sqrt(Delta0)), with Delta0>1 squarefree; let D=integral(theta^4)/24 and C=(theta1²+theta2²)/2. For every nonzero rational a such that aC is integral, the new necessary condition is

\[
t=a^2D\in\mathbf Z_{>0},\qquad \Delta_0\mid t.
\]

Here Delta0 is the squarefree radicand, not necessarily the field discriminant. The proof uses the integral exterior algebra of H1 and Smith normal form; it does not assume the field action preserves the chosen integral lattice.

Write H1_R=U direct sum W for the two real four-dimensional eigenspaces, and take the primitive top form nu. If c=aC is integral, the formula

\[
\iota_{R_c(x)}\nu=(\iota_xc)\wedge c
\]

defines an integral map on wedge²H1. Its real eigenspace calculation is R_c=tP, where P is identity on wedge²U direct sum wedge²W and zero on U tensor W. Also c²=2t nu; squares of integral four-forms have even top coefficient, so t is an integer. Choose a rational field endomorphism T with T²=Delta0. Then 2P−I=(wedge²T)/Delta0. If p divides Delta0 but not t, P is p-integral, so this last map is an integral involution. If m_i are the integral p-adic Smith exponents of T, every m_i+m_j must then equal1. Three indices force every m_i=1/2, impossible. This applies also at p=2 and proves the divisibility.

For a rank-one perfect object with normalized character v_q, the normalizing B-field is minus c1(E). Tensoring by det(E)^{-1} therefore produces an actual perfect object with character v_q, so qC is integral and Dq²=chi(E tensor det(E)^{-1}) is a positive multiple of Delta0. If E is simple and gluable, its degree-one contraction gives ext1≥8 and its Euler pairing is4Dq². The CY4 transpose identity and contraction rank18 imply the quantitative lower bound

\[
\dim\ker\sigma_E^2\ge2Dq^2-2\ge2\Delta_0-2>0.
\]

Thus **every simple gluable rank-one balanced RM seed fails full semiregularity, including arbitrary derived objects**. More strongly, for principal theta and q=1, no rank-one perfect object has this normalized character at all, without any simplicity or amplitude hypotheses. This closes the principal rank-one cone existence problems left by S26–S29: their conditional exact sequences remain valid, but their required nonsplit RM character equation is impossible. The conclusion does not exclude nonsimple higher-rank replacements, other corrected characters, or a condition weaker than full semiregularity.

There are also exact higher-rank restrictions. For e^B ch(E)=N v_q, with positive integral rank N, c1(E)=ell, the character equation gives

\[
N^2qC=Nc_2(E)-(N-1)\ell^2/2.
\]

The right side is integral on a torus. Consequently Delta0 divides N^4Dq². For an equivariantly simple gluable fully semiregular lift with k=chi_G in {2,4}, this becomes

| Equivariant Euler k | Necessary integral condition |
|---|---|
| 4 | Delta0 divides N² times the order of G |
| 2 | 2 Delta0 divides N² times the order of G |

For a nonequivariant object, N must be a multiple of Delta0, and N must also be even in the Euler2 case. Moreover the normalizing B-field must be genuinely fractional. If it were the Chern class of a line bundle Q, chi(E tensor Q)=NDq² would be a positive integer s, while full semiregularity and simplicity would give 4Ns=chi(E,E)≤4. This forces N=s=1, already excluded. Equivalently, the determinant of the bundle or perfect complex must have no Nth root in Pic(X). This additional observation was supplied and checked independently by the parent during review.

The complete saved proof has been read. An independent finite-basis calculation checked all28 bivectors, obtaining projection dimensions12 and16 and C²=2nu. This supports the contraction convention; the argument over every integral lattice and prime is the proof above. No formal proof-assistant verification is claimed.

## 35. S-31: low-rank vector bundles also fail the balanced character equation

A further Chern-polynomial obstruction applies even before semiregularity. Normalize the Chern roots x_i of a rank-N bundle by replacing each with x_i+B. This remains a polynomial of degree at most N even for fractional B. For the character N v_q, Newton's identities give

\[
\bar c_1=\bar c_3=0,\qquad
\bar c_2=NqC,\qquad
\bar c_4=N(N-6)Dq^2\nu.
\]

Rank1 contradicts the nonzero second Chern class. Ranks2 and3 contradict the nonzero fourth Chern class, since their normalized Chern polynomials have degree at most2 or3. Thus the balanced character has no vector-bundle realization in any of these ranks, regardless of the B-field. This does not exclude torsion-free sheaves of ranks2 or3, whose higher Chern classes may be nonzero.

Combined with S30, a nonequivariant simple gluable fully semiregular vector-bundle candidate must have rank at least4, divisible by the squarefree radicand Delta0, and a determinant without an Nth root. The first ranks allowed by these tests are4 for Q(sqrt2), and6 for Q(sqrt3). These numerical permissions do not assert existence or semiregularity; they identify the next genuinely smaller construction problem.


## 36. S-32: ramification at two forces an even polarization or group degree

There is a stronger obstruction when the divisor space is exactly the real quadratic field times the polarization and the integral homology is stable under the maximal local order at2. Let F=Q(sqrt(Delta0)) with Delta0 squarefree and congruent to2 or3 modulo4, so2 ramifies. Write D=integral(theta^4)/24. If D is odd and u is a rational2-adic unit, then for every positive integer N and integral divisor class ell,

\[
uC-\ell^2/(2N)\notin H^4(X,\mathbf Z_2).
\]

The proof is local and includes the required lattice normal form. The ring R=Z2[sqrt(Delta0)] is a DVR by Eisenstein (using sqrt(Delta0)−1 when Delta0 is odd), and L2=H1(X,Z2) is free of R-rank4. The trace pairing Tr(xy/(2sqrt(Delta0))) is perfect on R. Thus the polarization is the trace of a perfect alternating R-form, which has two symplectic hyperbolic planes. This uses only the local maximal-order action and odd D, not a global class-number-one hypothesis.

Put omega=sqrt(Delta0). Minimality of the rational divisor space and local unimodularity of theta give ell=theta((a+b omega)·,·), with a,b in Z2. Evaluate the alleged integral class on three explicit four-tuples drawn from the two hyperbolic planes. The required congruences are

\[
 b^2/N\equiv u/(2\Delta_0),\qquad
 a^2/N\equiv u/2,\qquad ab/N\equiv0
 \pmod{\mathbf Z_2}.
\]

If Delta0 is even, the first two terms force incompatible parities for v2(N). If Delta0 is odd, both diagonal valuations are−1 and force the cross term to have valuation−1, contradicting its integrality. This is an obstruction in every rank, including genuinely fractional normalization.

For normalized character N v_q, the second Chern identity reads c2(E)=ell²/2+(Nq C−ell²/(2N)). Thus the local obstruction applies whenever Nq is a2-adic unit. A simple gluable fully semiregular lift for an effective finite target group has k=4D(Nq)²/|G| in{2,4}. If D|G| were odd, k2 would force an odd valuation of the rational square (Nq)², while k4 would make Nq a2-adic unit. Both are impossible. Hence

\[
2\mid D|G|.
\]

In particular, the principal nonequivariant balanced RM construction fails in every rank under these maximal-order and divisor-space hypotheses. For a principal polarization k4 would force q=1/N, so the character equation itself fails in that case. The proof was independently developed and checked with the bounds agent; S33 treats the corresponding odd ramified primes.


## 37. S-33: odd ramification gives an Euler-integrality obstruction in every rank

The bounds agent extended the local method to odd ramified primes; the full saved proof and its independent third-character certificate have been read here and by the parent. Let p be an odd ramified prime of F, assume p does not divide D, and assume maximal local order action on H1(X,Zp). It is enough that the determinant class ell belongs to F theta. For a normalized character

\[
e^{-\ell/N}\operatorname{ch}(E)
   =N-uC+(u^2/N)\,\theta^4/24,
\]

with p-adic unit u, no actual positive-rank perfect object E exists. This assertion does not need simplicity or gluability.

In the local trace-symplectic basis, write the determinant endomorphism r=a+b sqrt(d). Integrality of the second Chern class forces

\[
b^2/N\equiv u/(2d),\qquad a^2/N,\ ab/N\in\mathbf Z_p.
\]

If m=vp(N) and k=vp(b), these equations give m=2k+1>0, vp(a)≥k+1 and r²/N≡u/2 modulo the ramified uniformizer. The complete character gives the exact Euler formula

\[
\chi(E)=D\,\frac{\operatorname{Nm}_{F/\mathbf Q}(Nu-r^2)}{N^3}.
\]

Since u−r²/N is a local unit, the numerator has p-valuation2m and the denominator valuation3m. Thus the proposed Euler characteristic has valuation−m, contradicting its integrality. A separate local check reaches the same contradiction from the (4,2) block of ch3: its coefficient is bar(r)(r²−Nu)/N², which has negative valuation. Divided powers of integral two-forms on a torus show this third-character argument also works at p=3; no stronger unproved integral Chern-character assertion is used.

Together S32 and S33 show that, when NS_Q=F theta and maximal local order action holds at every ramified prime, an equivariantly simple gluable fully semiregular balanced object must satisfy

\[
\operatorname{rad}(|\operatorname{Disc}(F)|)\mid D|G|.
\]

For a principal polarization and trivial group, the entire positive-rank balanced RM construction therefore fails, including arbitrary perfect objects and genuinely fractional determinant normalization. This strengthens the rank-one obstruction S30. It does not cover nonprincipal polarizations carrying the required bad primes, nontrivial group actions, determinant classes outside F theta, nonmaximal local orders, or different corrected characters. The actual rank-zero coherent candidate in Markman Example11.2.7/Lemma11.2.8 has a different character; these balanced-character restrictions do not by themselves refute that construction or its weaker restricted-semiregularity question.


## 38. S-34: rank-one determinant descent excludes every finite target action

**Checked theorem.** Let a rank-one perfect complex on an abelian fourfold with genuine real multiplication of type (2,2) have normalized balanced character `v_q`, with positive rational `q`. It has no fully semiregular lift that is simple and gluable in the equivariant category, for any effective finite coherent subgroup of translations and degree-zero tensor operations. Underlying simplicity and underlying negative-Ext vanishing are unnecessary. The statement requires neither maximal local orders nor `NS_Q=F theta`.

For `L=det(E)`, determinant sends the specified equivariance maps to `t_a L tensor P -> L`. Because virtual rank is exactly one, it retains the original scalar coherence: `det(c id_E)=c`. Conjugation by tensoring with `L^{-1}` therefore cancels both the tensor factors and the full scalar two-cocycle. The resulting action is ordinary translation; its projection to the abelian variety is injective by effectivity and the determinant equation. The finite translation quotient is an etale isogeny.

The normalized object descends explicitly by taking the averaging-idempotent summand of its finite pushforward. Etale-local splitting of the cover proves that pushforward is perfect, and direct-summand closure gives a perfect descended object. All self-Ext groups become exactly the invariant self-Ext groups. Full trace naturality, together with the S-21 injectivity of forgetting on `HH_{-2}`, transports full semiregularity. The quotient object would thus be rank one, simple, gluable and fully semiregular. The real-multiplication action and rational polarization descend through the isogeny; clearing a polarization denominator changes `q` to `q/m^2`, so S-30 applies and gives the contradiction.

**Exact source scope.** Knudsen–Mumford Theorem 2, p. 42, and the extended determinant construction on pp. 40–42 supply the perfect determinant and pullback compatibility; the rank-one scalar calculation is explicit in the proof. Stacks Proposition 35.5.2, tag 023T, supplies quasi-coherent descent, and Lemma 36.12.4, tag 09UG, supplies fpqc-local perfection. Both entire Stacks proofs were read. The perfect-complex descent is proved by finite averaging, rather than attributed to the sheaf-only proposition. Full trace transport imports the already checked S-10/S-21 and Perry 2026 Remark 2.3.

**Scope of the remaining gate.** Finite target actions cannot rescue rank one. Higher rank leaves a possible N-torsion pure-tensor subgroup and a coherence class whose Nth power vanishes. Bounds agent is investigating that residual descent problem separately.
