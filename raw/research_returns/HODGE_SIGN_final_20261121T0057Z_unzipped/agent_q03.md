# Q03: the erased openness remark at cote 34/64

Run: HODGE_SIGN, 2026-11-21. Investigator: GPT-6 Astra Pro, effort not exposed by runtime, agent `/root/q03_openness`. The full supplied transcriptions 34/53--63 were read before 34/64; 34/74 and the BRIDGES Q03/Q04 rows were then read. All arguments below have received a complete targeted reading after construction. No Lean or other formal certificate is claimed.

## Executive result

The literal text `[pi_0,H]` open **in pi'** is false. Its commutators lie in the geometric kernel H, whereas pi'/H=pi_0 is infinite. It is also undefined without an actual pi_0-action or a section, because an extension supplies only an outer action on a nonabelian H.

Three precise repairs are proved below:

* **Q3-04:** the canonical subgroup closure[pi',H] is open **in H**, with no solvability hypothesis. This is already a formal quotient of Theorem 1.1, cote 34/53.
* **Q3-05 + Q3-06:** if a continuous section s:pi_0 -> pi' is supplied, closure[s(pi_0),H] is open in H for every soluble pro-ell H of finite derived length. The proof uses Theorem 1.1 for all open subgroups, proves an FAb property, and then uses the terminating derived series.
* **Q3-07:** without a section, any such soluble pro-ell H on which the canonical **outer** pi_0-action is trivial is finite. This is an intrinsic variant, not an assertion that the manuscript intended this formulation.

Thus the BRIDGES Q03 row can be replaced by: literal statement refuted; two explicitly corrected openness statements proved; restoration of the exact crossed-out handwriting remains a palaeographic question. No higher-dimensional form of RH and no Alpoge theorem is needed. Weil I is sufficient because its curve case supplies the already used input in Grothendieck's 1.1, but it cannot make the literally transcribed assertion true.

## 1. The framework actually supplied by 1.1

Fix k finitely generated over its prime field; a normal, geometrically connected, locally finite type k-scheme X; ell different from char(k); and an open subgroup pi of pi_1(X). Write

    1 -> I -> pi -> Gamma -> 1,

where I=pi intersect pi_1(X_{k^sep}) and Gamma=pi_0 is an open subgroup of G_k. In 34/53, I is also written with a bar. For a profinite group J, let J(ell) be the maximal abelian pro-ell quotient, and take all commutator subgroups with their topological closure.

**Background Q3-B01.** Grothendieck, cote 34/53, Theorem 1.1, says that I(ell) is a finitely generated Z_ell-module and

    I(ell)_Gamma is finite.

The quantifier over **every open pi** is essential in the nonabelian argument. The following pages do not state a higher-dimensional purity theorem: 34/54 gives consequences for abelianization; 34/54--58 derives essential unipotence and isotriviality statements; 34/63 discusses geometric monodromy of higher direct images. The canceled remark 1.17 on 34/64 is a separate attempted extension.

Let N_0 be a pi-normal closed subgroup of I and suppose H=I/N_0 is pro-ell. Put P=pi/N_0, so

    1 -> H -> P -> Gamma -> 1.

P is the pi' of the remark. This quotient extension is not the abelian quotient extension pi' of 1.1 unless H is abelian; keeping the name P avoids the collision.

**Q3-03 (relative finite-abelianization property).** For every open subgroup P_1 of P, with J=P_1 intersect H, the coinvariant group J^ab_{P_1} is finite.

*Proof.* Let pi_1 be the inverse image of P_1 in pi. It is an open subgroup of pi_1(X). Its geometric kernel I_1=pi_1 intersect I maps surjectively to J: any lift in pi of an element of J has trivial arithmetic image and therefore belongs to I_1. Since J is pro-ell, the map I_1 -> J -> J^ab factors through I_1(ell). It is equivariant for the action of pi_1. The image Gamma_1 of pi_1 in G_k acts on I_1(ell), and the coinvariants I_1(ell)_{Gamma_1} are finite by 1.1 applied to pi_1. Their image is all of J^ab_{P_1}. Hence this last group is finite. No section, finite generation of H, analytic structure, or solvability was used. QED.

## 2. Why the ambient group in 1.17 cannot be right

**Q3-01 (literal refutation).** The assertion that closure[Gamma,H] is open in P is false even in an example where the action and the section are canonical enough to remove all ambiguity.

*Proof, minimal example.* Take k=F_q, X=Spec(k), pi=G_k=Z-hat, I=H=1, and P=Gamma=Z-hat. The trivial H is a soluble pro-ell group. Its commutator subgroup with Gamma is trivial, which is not open in the infinite profinite group Z-hat. All stated hypotheses of 1.1 and 1.17 hold. QED.

*Nontrivial geometric example.* Take k=F_2, X=G_m, ell=3, and the rational base point 1. The Kummer covers u -> u^{3^r} give the geometrically connected pro-3 quotient H=Z_3(1); the point 1 supplies a section. Arithmetic Frobenius acts on H by multiplication by 2. Consequently [Gamma,H] contains (2-1)H=H and equals H. Nevertheless P/H=G_{F_2}=Z-hat is infinite, so H is not open in P. This also shows directly that replacing the ambient group by H repairs a genuine dimension/topology mismatch, rather than a limiting issue in a proof.

For a general extension, Gamma is a quotient of P and has only a map Gamma -> Out(H). Choosing lifts of Gamma changes their action on H by inner automorphisms. Thus `[Gamma,H]` is not an intrinsic subgroup without additional convention. The expression `[P,H]` is intrinsic.

The mathematics proves that the displayed statement cannot stand as written. It does **not** prove which marks are on the absent image of the manuscript, or whether the problem is transcription or an abandoned draft assertion.

## 3. The canonical correction is immediate

**Q3-04 (canonical openness).** The subgroup C=closure[P,H] is open in H.

*Proof.* C is a closed normal subgroup of H. Because H is contained in P, C contains closure[H,H], so H/C is abelian. P acts trivially on H/C by the definition of C. Therefore the quotient map I -> H/C factors through the finite group I(ell)_Gamma of 1.1. Hence H/C is finite. A closed subgroup of finite index in a profinite group is open, so C is open in H. QED.

Equivalently H/C=(H^ab)_Gamma. This is precisely the abelian quotient controlled by 1.1, regardless of the nonabelian size or derived length of H. It is therefore misleading to call this correction a new consequence of all-dimensional purity.

## 4. Actual-action coinvariants: the nonabelian soluble correction

Suppose now that a continuous section s:Gamma -> P is given. Identify P with H semidirect Gamma by this section, and write alpha_gamma for its action on H. Define

    N = closure of the subgroup generated by h^{-1} alpha_gamma(h),
        for h in H and gamma in Gamma.

**Q3-05 (FAb coinvariant quotient).** N is normal in P. The quotient Q=H/N is pro-ell, and every open subgroup V of Q has finite abelianization.

*Proof.* Put delta_gamma(h)=h^{-1}alpha_gamma(h). For h,k in H,

    delta_gamma(hk) = k^{-1} delta_gamma(h) k delta_gamma(k).

Consequently conjugation of delta_gamma(h) by k is

    k^{-1} delta_gamma(h) k = delta_gamma(hk) delta_gamma(k)^{-1},

a product of generators and inverses of generators. The generated subgroup, and then its closure N, is H-normal. For eta in Gamma,

    alpha_eta(delta_gamma(h))
      = delta_{eta gamma eta^{-1}}(alpha_eta(h)),

so N is Gamma-stable. Thus N is normal in P.

Gamma acts trivially on Q, so the section gives an isomorphism of profinite groups

    P/N = Q x Gamma.

Let V be any open subgroup of Q, not necessarily normal. Let P_V be the inverse image of V x Gamma in P. This is open, and P_V intersect H maps surjectively onto V. Conjugation by V x Gamma acts trivially on V^ab: the V-factor acts by inner automorphisms and the Gamma-factor acts trivially. Hence V^ab is a quotient of the coinvariants (P_V intersect H)^ab_{P_V}. This group is finite by Q3-03. Therefore V^ab is finite. QED.

In particular, the conclusion is the **FAb** property of Q, not merely finiteness of Q^ab. FAb means that every open subgroup has finite abelianization. Merely knowing Q^ab finite does not justify the next step.

**Q3-06 (soluble FAb consequence).** If a profinite group Q is FAb and soluble of finite derived length, then Q is finite. Consequently, if H has finite derived length in Q3-05, N is open in H.

*Proof.* Define D^0Q=Q and D^{r+1}Q=closure[D^rQ,D^rQ]. Since Q^ab is finite, D^1Q is open. Inductively, if D^rQ is open in Q, the FAb property says that its abelianization is finite; thus D^{r+1}Q is open in D^rQ and hence open in Q. Finite derived length means D^dQ=1 for some finite d. Hence 1 is open in Q. A compact discrete group is finite. A quotient of a soluble group has at most its derived length, so Q=H/N has finite derived length if H does. Thus Q is finite and N is open in H. QED.

The word `resoluble` must here mean finite derived length. Replacing it by `prosolvable` is not an innocuous extension: every pro-ell group is already prosolvable, and the terminating-derived-series step would disappear.

## 5. Optional intrinsic statement with no section

**Q3-07 (trivial outer action on a soluble quotient).** Under the framework of section 1, suppose H has finite derived length and Gamma -> Out(H) is trivial. Then H is finite.

*Proof.* Let C=C_P(H), the closed centralizer of H in P. Triviality of the outer action says exactly that P=HC: if conjugation by p is conjugation by h, then h^{-1}p centralizes H.

Write D_i for the closed derived series of H. We prove inductively that D_i is open in H. This is true for D_0=H. Assume it holds for D_i. As D_i is characteristic in H, it is normal in P. The product R_i=D_i C is a closed subgroup of P, and P=HC shows

    [P:R_i] <= [H:D_i] < infinity;

thus R_i is open in P. Its conjugation on H, and hence on D_i, is induced by elements of D_i.

There exists an open normal subgroup U_i of P with U_i intersect H contained in D_i. Indeed D_i is an open neighborhood of 1 in the subspace H; choose an open neighborhood O in P whose intersection with H lies in D_i, and then an open normal U_i contained in O. Since D_i is normal in P, D_i U_i is an open subgroup of P and

    (D_i U_i) intersect H = D_i.

Set P_i=R_i intersect (D_i U_i). It is open, contains D_i, and P_i intersect H=D_i. Every element of P_i acts on D_i by an inner automorphism from D_i; hence it acts trivially on D_i^ab. Q3-03 applied to P_i therefore says that D_i^ab is finite. It follows that D_{i+1} is open in D_i, and so open in H. This completes the induction. At the finite terminal derived index d, D_d=1 is open in H, proving H finite. QED.

No Lie algebra of H, Malcev completion, semisimplicity, or finite-rank hypothesis enters this proof. It is useful if an intrinsic `arithmetic-constant soluble quotient` was intended, but it should not be substituted into the erased sentence without a fresh reading of its image.

## 6. Where purity enters, and where it does not

**Q3-02 (weight-to-finite-coinvariants lemma).** Let M be a finitely generated Z_ell-module with a continuous action of a profinite group G. Suppose some g in G has no eigenvalue 1 on M tensor Q_ell. Then M_G is finite. In particular this holds if g is a Frobenius at a finite-field point whose eigenvalues are pure of a nonzero weight (with either geometric or arithmetic Frobenius convention).

*Proof.* M/(g-1)M surjects onto M_G. Tensoring the first quotient with Q_ell gives the zero vector space because g-1 is invertible. It is a finitely generated torsion Z_ell-module and is therefore finite. Its quotient M_G is finite. Purity of weight w!=0 means all complex conjugates of the eigenvalues have absolute value q^{w/2}!=1, and in particular 1 is not an eigenvalue. Passing to inverses reverses the sign of w but not this conclusion. QED.

For a smooth projective curve C/F_q, Deligne, *La conjecture de Weil I*, (1.6)--(1.7), gives weight 1 on H^1(C_bar,Q_ell). Its dual has weight -1. The identity

    H^1(C_bar,Q_ell) = Hom_cont(pi_1(C_bar),Q_ell)

comes from the classification of finite etale constant-group torsors, followed by the inverse limit and tensoring. Thus Q3-02 applies to the geometric abelian pro-ell quotient. No diagonalizability of Frobenius is required.

Grothendieck's own finite-type spreading/specialization mechanism is explicitly recorded at **34/74, (2.5.4)--(2.5.6)**: extend the smooth projective curve over a finitely generated normal ring R, identify the lisse H^1 fibers, and specialize to a closed point with finite residue field. One such Frobenius with no eigenvalue 1 suffices. The same page also records an alternative abelian-variety argument using the finiteness of A(k). The reduction to curves is announced (then struck) at **34/54, first paragraph**; the theorem it supports is **34/53, 1.1**. We use the established 1.1 as background, rather than claiming to have reconstructed its omitted intermediate proof pages 65--73.

For published, independently accessible confirmation of this mechanism, Katz--Lang, *Finiteness theorems in geometric classfield theory*, L'Enseignement Math. 27 (1981), **Theorem 1; its proof in section II; Theorems 1(bis), 1(ter)**, reduces via Artin good neighborhoods and generalized Jacobians to abelian varieties and tori over finite fields. Their precise references for the good-neighborhood reduction are **SGA 4 XI 3.1 and 3.3**. This source is not being used as a replacement for the normal-scheme statement in the supplied 1.1.

A second, broader direct route for smooth finite-type varieties over finite fields is Weil II **(3.3.5)**: H^1 has weights at least 1, so its dual has weights at most -1, and Q3-02 applies. This extra theorem is unnecessary for the conclusions above; it is included only to locate accurately the distinction between smooth-projective purity in Weil I and the nonproper weight estimate in Weil II.

Therefore the logical dependence for the corrected statements is:

    curve RH / Weil I on curves
      + the geometric reductions already in 1.1
      => 1.1 for every open pi
      => Q3-03
      => Q3-04, or Q3-05 and Q3-06, or Q3-07.

There is no remaining purity gate in these corrected formulations. The literal ambient-group assertion remains false even if every Weil conjecture and every standard conjecture is assumed.

## 7. Locally finite type versus finite type

**Q3-08 (affine-open reduction for 1.1).** The lack of quasi-compactness in the supplied 1.1 does not obstruct transferring its finite-type conclusion to X, once the arithmetic/geometric fundamental groups are those in its displayed exact sequence.

*Proof.* A connected normal locally noetherian scheme is integral: its irreducible components are pairwise disjoint and locally open, and connectedness leaves only one. Let U be a nonempty affine open in X. It is finite type over k. If X' -> X is connected finite etale, X' is normal and connected, hence integral; its inverse image of U is a nonempty open and thus connected. The connected-cover criterion, SGA 1 V **6.9**, implies pi_1(U) -> pi_1(X) is surjective.

The same reasoning applies after separable closure of k: normality is preserved by separable algebraic base extension, and the assumed geometric connectedness ensures connectedness. Hence pi_1(U_{k^sep}) -> pi_1(X_{k^sep}) is surjective. For any open pi in pi_1(X), let pi_U be its inverse image in pi_1(U). The geometric kernel I_U maps onto I, with the same arithmetic image Gamma. It follows that I_U(ell) maps onto I(ell), and their Gamma-coinvariants have a surjection. Finite generation and finiteness of coinvariants for U therefore imply both conclusions for X. QED.

This addresses the only non-quasi-compact issue needed in the group-theoretic arguments. It does not silently apply the quasi-compact statement of SGA 1 IX 6.1 to an arbitrary non-quasi-compact scheme; the exact sequence for the supplied normal X is already the framework of 1.1.

## 8. Sources and verified locators

* Grothendieck archive, cote 34, scans 53--64, especially 53/1.1, 54 opening paragraph, 64/1.17; scan 74/(2.5.4)--(2.5.6). Supplied files read in full.
* SGA 1, Expose V, **Theorem 4.1** (Galois-category equivalence), **Proposition 6.9** (surjectivity and connected covers); Expose IX, **Theorem 6.1** (arithmetic/geometric exact sequence, quasi-compact case). Verified in the complete primary re-edition at https://arxiv.org/pdf/math/0206203 ; IX 6.1 is printed p.253 in the original pagination / p.195 in the re-edition.
* P. Deligne, *La conjecture de Weil I*, Publ. Math. IHES 43 (1974), **(1.6), (1.7)**, https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf . Web source ref `turn501471856view1`. Also verified using Milne's translation https://www.jmilne.org/math/Documents/DeligneWeilI.pdf ; beware the translation/text extraction's characteristic-polynomial versus reciprocal-root typo: the statement needed is explicitly about Frobenius eigenvalues.
* P. Deligne, *La conjecture de Weil II*, Publ. Math. IHES 52 (1980), **(3.3.5)**, printed p.206, https://publications.ias.edu/sites/default/files/Number40.pdf . Web source `turn593706566view1`, exact passage `turn921020268view3`. This corroborating route is not a dependency of Q3-04--07.
* N. Katz and S. Lang, *Finiteness theorems in geometric classfield theory*, Enseign. Math. 27 (1981), **Theorem 1**, proof in section II; **Theorems 1(bis), 1(ter)**, https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf . Web source `turn217060055view1`. The exact source proof was read in the primary PDF and its text extraction. Its citation to SGA 4 XI 3.1, 3.3 was verified there, not independently read in SGA 4.

External PDFs and extracted texts are scratch reference cache only, at `reference_cache/q03_sources`; do not include them in the deliverable ZIP. No claim is made that the recent web-search hit arXiv:2610.16760 was verified; it was not used.

## 9. Implications for the programme and unresolved textual point

* BRIDGES/Q03: literal formula refuted by Q3-01; canonical corrected formula proved by Q3-04; section-dependent nonabelian corrected formula proved by Q3-05--06; intrinsic trivial-outer-action variant proved by Q3-07.
* BRIDGES/Q04 remains settled as before. Q3-02 isolates the actual weight argument, and 34/74's formula should use additive zero, not the multiplicative identity 1.
* No standard conjecture changes status. No positive-weight arithmetic L-function RH follows from these group statements.
* Alpoge RH/Dirichlet-GRH and Masullo are not used. The conclusions are unconditional within the established etale fundamental-group and curve-RH framework.
* The only unresolved point is the exact intended wording of crossed-out 1.17: images of the manuscript were not supplied, and a mathematically forced correction is not palaeographic verification. The question as transcribed is nevertheless decided (false), and the natural precise corrected statements are decided (true).
