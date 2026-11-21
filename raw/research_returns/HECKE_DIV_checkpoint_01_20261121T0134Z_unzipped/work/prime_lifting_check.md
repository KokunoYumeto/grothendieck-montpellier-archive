# P6 / R26: arithmetic bounded-degree lifting, including varying multipliers

Date: 2026-11-21 UTC. Checker: GPT-6 Astra Pro; effort not exposed; agent /root/reductions. This note independently reconstructs the argument requested by /root, then checks its hypotheses and source locators. It is not a full independent proof of the external parameter-space and base-change theorems.

## Verdict

**The proposed conclusion is correct.** One may allow the positive integers N_v to vary, provided the two effective integral parts have one common degree bound and the ℓ-adic class is one fixed global section. For a proof, replace the blanket assertion about a flat universal cycle on a mixed-characteristic Chow scheme by a finite type parameter cover carrying genuine relative cycles, followed by flattening and a discrete-valuation-ring specialization argument. A universal Chow cycle is not in general a universal flat subscheme.

The result is valid for smooth projective schemes, not just abelian schemes. It is existential. It produces neither an explicit bound nor a bounded representative from pointwise algebraicity alone.

## Precise theorem

Let F be a number field with a fixed embedding into C. Let U be a nonempty open of Spec O_F, let ℓ be invertible on U, and let f:X→U be smooth and projective with relatively ample line bundle L. Put r=dim(X/U)−p. Let

    t_ℓ ∈ H^0(U,R^{2p}f_*Q_ℓ(p))

be nonzero. Suppose the geometric generic value of t_ℓ corresponds, under the chosen Betti–étale comparison, to t_B⊗1 for a rational Betti class t_B∈H^{2p}(X_C,Q(p)). The following are equivalent:

1. t_B is the class of a rational algebraic cycle on X_C.
2. There exist N≥1 and D≥0 such that, at every closed place v of a nonempty open U′⊂U, there are effective integral r-cycles Z_v^+,Z_v^- on X_{bar κ(v)} satisfying deg_L Z_v^±≤D and cl_ℓ(Z_v^+−Z_v^-)=N(t_ℓ)_v.
3. The same condition, with one N and D, holds at infinitely many distinct closed places of U.
4. There is D such that at infinitely many distinct closed places v there are such cycles of degree at most D and positive integers N_v, with no assumed bound on N_v, satisfying cl_ℓ(Z_v^+−Z_v^-)=N_v(t_ℓ)_v.

More precisely, from condition 4 one obtains one of its positive integers N_0 and effective integral cycles Z^± on X_{bar F} with degree at most the original D and cl_ℓ(Z^+−Z^-)=N_0t_ℓ. These cycles give the Betti equality as well. After deleting finitely many primes, their reductions give condition 2 with this N_0 and the same degree bound D.

The theorem does not require a bound on the residue-field extensions over which the geometric cycles are defined. The global-section assumption is essential to make all the specializations refer to the same class; arbitrarily chosen identifications of geometric cohomology groups are not a substitute for it.

## Parameter lemma with mixed-characteristic details

For fixed r and D there is a finite type U-scheme T and two families of effective integral r-cycles on X×_U T with the following properties:

- Every geometric pair (Z^+,Z^−) of degrees at most D occurs at a geometric point of T.
- After decomposing T into finitely many parameter schemes and applying proper modifications if needed, each family is a finite integral linear combination with nonnegative coefficients of closed subschemes flat and projective over its parameter scheme, of pure relative dimension r.
- Each parameter scheme has fixed degrees d_+,d_−≤D for the two fibre cycles.

Here “occurs” means equality as an effective cycle, including multiplicities. It does not require each individual cycle component to remain geometrically integral at every parameter point.

**Construction and justification.** Replace L by L^m for a fixed relatively very ample power. An r-cycle's degree is then multiplied by m^r, so the original bound is recovered by dividing by this fixed factor. The bounded-degree relative Chow spaces exist over the noetherian base U as projective schemes h-representing the effective-cycle sheaves. This is Suslin–Voevodsky, Theorem 4.4.11 and Corollary 4.4.13, not merely the characteristic-zero Chow-functor representability statement. Take the finite disjoint union of the products for the allowed degree pairs.

An identity map to an h-representing Chow scheme gives a universal section of the h-sheaf of cycles. By the definition of sheafification, an h-cover represents this section by actual relative cycles. Since the Chow schemes are of finite type and quasicompact, take a finite type covering family and a common refinement for the two cycles. Its disjoint union surjects on geometric points. Decompose the reduced parameter schemes into their finitely many irreducible components. On each, the relative cycles are determined by their generic cycles. Apply simultaneous flattening to the finitely many closures of their generic supports. The strict transforms give flat projective families; their associated relative cycles equal the pullbacks of the original cycles because relative cycles are determined by their generic values. Their specializations consequently give the prescribed geometric cycles, and their degrees are constant.

This construction can be read explicitly in Anderson (2019), Lemma 6.3.19, Lemma 6.3.24 and Theorem 6.3.25, pp.188–193; the latter is a proper-topology refinement of Suslin–Voevodsky's representability. Suslin–Voevodsky §3.2 supplies the associated relative cycles of flat subschemes, while their Theorem 2.2.2 is the flattening input. It is harmless that the resulting parameter cover T need not remain projective: the proof below requires finite type and finitely many irreducible components, not properness of T→U.

This route avoids claiming that FGA's fixed-Hilbert-polynomial theorem directly bounds all subschemes of a fixed degree. It also avoids assuming a fine mixed-characteristic moduli interpretation for a coarse Chow scheme.

## Proof of 4 ⇒ 1

Write the finite type parameter scheme T as the union of its finitely many irreducible components. A component whose generic point maps to a closed point v of U is contained entirely in that fibre: the image of a specialization is a specialization, and a closed point of U has no distinct specializations. Therefore all vertical components are contained over a finite set E of places. Every component meeting T over U∖E dominates U.

Choose a place v∉E among the infinitely many places in condition 4, and a geometric point y of T whose fibre cycles are the given Z_v^±. The pair is defined over a finite extension of κ(v), and a suitable closed point of the finite type parameter fibre may be chosen. Pick an irreducible component C of T containing its underlying point. Then C dominates U. Give C its reduced structure and denote its generic point by ξ.

There is a discrete valuation ring R and a morphism Spec R→C taking the generic point to ξ and the closed point to y's underlying point. Moreover Frac(R) can be taken to be κ(ξ), a finitely generated field over F. This is Stacks Project, Lemma 28.5.10, Tag 054F. Geometric residue fields may be enlarged to compare with the initially chosen cycles. Pull back the two flat cycle families to Spec R. Their special fibre cycles are Z_v^± after extension of the residue field; their generic fibre cycles Z_K^± are effective integral r-cycles of the same degrees, where K=Frac(R).

For a smooth proper family over a trait with ℓ invertible, smooth proper base change supplies an isomorphism

    sp : H^{2p}(X_{bar K},Q_ℓ(p)) → H^{2p}(X_{bar κ(R)},Q_ℓ(p)).

For a flat family of cycles, specialization commutes with its cycle class. The integral multiplicities of special fibre components are included in this statement. Thus

    sp(cl_ℓ(Z_K^+−Z_K^−) − N_v(t_ℓ)_{bar K})
      = cl_ℓ(Z_v^+−Z_v^−) − N_v(t_ℓ)_v
      = 0.

Because sp is an isomorphism, the generic expression is zero. This is the entire lifting step. The equality is exact in Q_ℓ-cohomology; no reduction modulo ℓ^k, compactness assertion about the integers N_v, or limiting argument is involved.

As K is finitely generated over the given number field, it embeds in C extending the chosen embedding of F. Betti–étale comparison, functorial for algebraic cycle classes, gives

    cl_B(Z_C^+−Z_C^−)=N_v t_B.

Indeed both sides lie in rational Betti cohomology, and equality after tensoring with Q_ℓ implies equality over Q. Dividing the integral signed cycle by the nonzero integer N_v proves condition 1.

To obtain cycles over bar F of the same degrees, spread the cycle pair over the characteristic-zero parameter component containing its generic point. After extending F algebraically if necessary, choose a closed point on that component. Specialization along a trait from the geometric generic point to this closed point, or the characteristic-zero local constancy of cycle classes, preserves the equality. Every closed point of a finite type bar F-scheme is bar F-valued. Consequently the pair is defined over a finite extension of F and keeps the two degrees. Set N_0=N_v.

The ordinary and geometric fibres in this proof should not be conflated. All cycle-class equalities use geometric fibres, and the transition to geometric residue fields is allowed; no descent to the original finite residue field is asserted.

## Remaining implications

Condition 1 provides a rational signed algebraic cycle. Because X is defined over bar F, a rational class represented over C is also represented by a cycle over bar F: spread its finitely many components over a finite type bar F-algebra, and take a closed point on a connected parameter component, preserving the Betti class. Clear its finitely many coefficient denominators, separate positive and negative coefficients, and obtain effective integral cycles Z^± with class Nt_B. Their components are defined over a finite extension F′/F.

Take their schematic closures in the projective model after base change to O_{F′}. Remove finitely many places so all the closures are flat. At each remaining geometric residue fibre their effective fundamental cycles have the original degrees; specialization of classes gives Nt_v because t_ℓ is the fixed global section and the generic equality holds. This proves 1⇒2. The implications 2⇒3⇒4 are immediate.

## Why varying N_v causes no obstruction

The proof only needs one good place outside E and retains that place's integer. In fact it gives a little more. On a fixed horizontal irreducible parameter component, at most one rational number N can occur in a fibre equality cl(Z^+−Z^-)=Nt_ℓ. Any such equality transports through a trait to the same geometric generic cycle class. Two occurrences N and N′ would give (N−N′)t_ℓ=0 at that generic point; nonzero t_ℓ forces N=N′. Therefore, outside E, the integers occurring for degree≤D pairs belong to a finite set indexed by the finitely many horizontal parameter components. Along an infinite set of places, one integer occurs infinitely often.

This is a finiteness conclusion, not an effective formula for max N. It depends on a fixed class, model, polarization and degree bound. It must not be read as a universal numerical estimate independent of those data.

## Comparison with the literature and application to 032

Brünjes and Serpé's *Uniform bounds and ultraproducts of cycles*, arXiv:0901.4853, Definition 2.3 and Theorems 3.1 and 3.4, gives closely related lifting results from bounded complexity at infinitely many primes. Their Definition 2.3(ii) includes a bound on the integer clearing rational coefficients. The present trait proof explains why for a fixed global class and bounded degrees of the integral positive and negative parts one may first allow N_v to vary: finitely many parameter components force only finitely many possible values away from finitely many primes. The proof here uses geometric fibre cycles and does not require their fields of definition to have bounded degree.

The independently supplied source 032, Remark 8.5 (printed pp.50–51), states that for an abelian variety A over Qbar with good reduction, a rational Hodge class has a rational algebraic specialization represented by one cycle simultaneously in the prime-to-p and crystalline realizations. The statement concerns general A/Qbar, not only CM A; its argument uses the CM transport cited there as [32], Corollaries 3.4 and 6.4. This audit read that remark but has not independently re-proved its cited CM transport.

Assuming that remark's result and choosing the compatible global realizations, each good place supplies some integer N_v and some integral effective pair after clearing rational coefficients. **It does not supply one common degree bound.** The theorem above makes the remaining arithmetic gate exact: a bound for the degrees of both integral effective parts on infinitely many good fibres is equivalent to algebraicity of the original class. This is stronger than knowing that the class lies in the Q_ℓ-span of cycle classes at every prime, and it is also stronger than having unrelated finite bounds at individual primes.

## Exact source log

1. **Suslin, A., & Voevodsky, V. (2000). Relative cycles and Chow sheaves.** In Voevodsky, Suslin, and Friedlander, *Cycles, transfers, and motivic homology theories*, Annals of Mathematics Studies 143. Theorem 4.4.11 and Corollary 4.4.13, author manuscript printed pp.79–81 (PDF indexes78–80), establish projective h-representability over a noetherian base. Theorem 2.2.2, author manuscript p.9, is the flattening input. Author-hosted PDF: https://www.math.ias.edu/Voevodsky/files/files-original/Dropbox/Published_papers/Motives/Collection/s2.pdf . Web refs: turn282660516view0, turn949376090view0, turn949376090view1, turn130701249view0. These are directly opened statement and proof passages; not every theorem in the chapter was re-proved.
2. **Anderson, O. (2019). Chow schemes in mixed characteristic [Doctoral dissertation, University of Liverpool].** Lemmas 6.3.19 and 6.3.24 and Theorem 6.3.25, pp.188–193; Corollary 6.3.23(3), p.191, identifies perfect-field points. Thesis PDF https://livrepository.liverpool.ac.uk/3033935/1/201095136_Mar2019.pdf . The web reader returned406, but the ordinary HTTPS download with a browser User-Agent succeeded and the PDF text was directly read locally at work/anderson_chow_mixed.pdf. Its results corroborate the precise proper-cover version used in the parameter lemma; the published Suslin–Voevodsky result is the principal reference.
3. **Artin, M., Grothendieck, A., & Verdier, J.-L. (1973). SGA4, Exposé XVI, Corollaire2.2.** Smooth-proper specialization. Directly inspected in French re-edition at https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf , p.139 (PDFindex145), original pagination214 indicated in the margin. Web refs turn492465929view0 and turn509177171view0. Use the locally constant sheaf Q_ℓ(p), obtained from the corresponding finite-coefficient statements.
4. **Grothendieck, A. (1971). SGA6, ExposéX, Appendix§7, equations(7.13.4), (7.13.9), (7.13.10), pp.578–579.** The original scans were downloaded and visually inspected at https://wstein.org/sga/sga/6/6t_578.html and https://wstein.org/sga/sga/6/6t_579.html . They explicitly give compatibility of specialization with Chern/cohomological cycle classes and the geometric Q_ℓ diagram. Local image files work/sga6_page578.jpg and work/sga6_page579.jpg. The ensuing integral-cycle diagram(7.13.12) was seen in an online French/English transcription; its original page580 was unavailable as an individual image, so the directly checked citation here is the sufficient rational diagram(7.13.10), not an assertion of having read originalp580.
5. **The Stacks Project Authors. Lemma28.5.10, Tag054F.** Every specialization in a locally noetherian scheme is realized by a DVR; its fraction field can be a prescribed finitely generated extension of the generic-point residue field. https://stacks.math.columbia.edu/tag/054F . Web ref turn209713884view3. Statement and proof directly read.
6. **Brünjes, L., & Serpé, C. (2009). Uniform bounds and ultraproducts of cycles. arXiv:0901.4853.** Definition2.3(i)–(ii), pp.4–5; Theorem3.1, pp.6–7; Theorem3.4, pp.7–8. https://arxiv.org/pdf/0901.4853 . Web ref turn826639527view0. This is related prior work, not the source of the independent trait proof above. The paper's introduction also states extension to arbitrary number fields.

## Checks actually completed

- Independent reconstruction of the implication with N_v varying: finite parameter cover, horizontal component, DVR and injective specialization.
- Targeted full-proof reading of the reconstruction: confirmed the global-section hypothesis, geometric residue fields, effective multiplicities, constancy of degree, characteristic-zero comparison, and descent to bar F.
- Source check: original SGA6 equations on pp.578–579 visually read; SGA4 specialization statement, Stacks trait lemma and Suslin–Voevodsky representability statements directly read; Anderson's detailed flattening/proper-cover proof passages read locally.
- Correction to an abbreviated proof: replace “the universal Chow cycle is flat over the Chow scheme” by the finite-cover/flattening parameter lemma. No numerical bound is claimed.
