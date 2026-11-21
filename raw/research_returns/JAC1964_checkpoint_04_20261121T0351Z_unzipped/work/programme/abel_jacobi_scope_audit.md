# Abel–Jacobi injectivity and algebraic grade-one cycles: scope audit

Run JAC1964-20261121; /root/programme_audit; GPT-6 Astra Pro; effort setting not exposed. This note records the specific primary results checked and the exact deductions they permit. It does not assert that no other theorem exists in the literature.

## The required arithmetic statement

For the actual motive N and fields fixed by JAC-P17, the map needed to turn the Selmer dimension calculation into a Chow dimension bound is

\[
\alpha_{k,\ell}:\operatorname{CH}^2(N_k)_{\mathbf Q}
 \otimes_{\mathbf Q}\mathbf Q_\ell
 \longrightarrow H^1_f(k,H_\ell(N)(2)).
\]

Injectivity must hold after this scalar extension. An injective Q-linear map into a finite-dimensional Q_l-vector space would not suffice: if a belongs to Q_l but not Q, the map Q²→Q_l given by (x,y)↦x+ay is injective over Q, while its scalar extension has kernel containing (−a,1). Likewise, injectivity for torsion cycle classes, or for reductions modulo powers of l, does not eliminate an arbitrary rational or divisible kernel. Finite generation of the relevant full Chow group has not been established here.

AR23 now proves surjectivity of the regulator and identifies its image using eta over Q and eta,T eta over Q(i). Its displayed complements exist over Q5. That fact supplies neither a rational Chow complement nor a real-height decomposition.

## What the classical grade-one claim says

Beauville, *Sur l’anneau de Chow d’une variété abélienne*, Math. Ann. 273 (1986), 647–651, was read directly from the author's original scan. Proposition 5, printed p650, proves injectivity of the grade-zero ordinary cycle-class map in codimensions p=0,1,g−1,g. For an abelian threefold this covers every grade-zero codimension. Remark 3, printed p651, explicitly discusses injectivity of the Abel–Jacobi map on grade one as an additional ingredient needed for the conjectural filtration; it is not a proved consequence of Proposition 5. The Fourier shift preserving grade is Proposition 1 on printed p648:

\[
\mathcal F:\operatorname{CH}^p_{(s)}(A)
 \xrightarrow{\sim}\operatorname{CH}^{g-p+s}_{(s)}(\widehat A).
\]

Primary scan: https://math.univ-cotedazur.fr/u/beauvill/pubs/Chow.pdf .

Gordon–Murre, *Chow motives of elliptic modular surfaces and threefolds*, arXiv:alg-geom/9610007v2, §6.5.4–6.5.6, author pp51–52, makes the logical distinction particularly explicit. Their Chow–Künneth results give the inclusion F²CH²⊂ker AJ. Equality is Conjecture 6.5.5. Proposition 6.5.6 identifies equality with injectivity on the modular middle summand. Thus even a theorem establishing Murre (B) and (D) must not be read as a theorem identifying the next filtration step with the Abel–Jacobi kernel. This concerns the classical Abel–Jacobi map and is not itself an arithmetic scalar-extension theorem.

Primary: https://arxiv.org/pdf/alg-geom/9610007 .

## The narrower algebraically trivial question

The projector onto N has Hodge types (3,0),(0,3). A curve correspondence from a degree-zero divisor has realization H¹(C)→H³(N)(1), which vanishes because the two sides have incompatible Hodge types. Consequently every algebraically trivial N-class has zero projected classical and rational etale Abel–Jacobi image. Injectivity on this subgroup would therefore amount to its vanishing in rational Chow. Vanishing of the cohomological family map does not by itself prove vanishing of the actual correspondence or its action on rational Chow groups.

There is a particularly small geometric obstruction, compatible with AR15a. Suppose z∈CH²(N) is a nonzero algebraically trivial class. After a finite extension, express z as a finite sum of Gamma_i,* D_i with C_i smooth projective curves and D_i∈Pic⁰(C_i)_Q. At least one term remains nonzero after projection to N. Insert the degree-one projector on that curve and the N-projector on J. The resulting nonzero correspondence

\[
 Z_i\in\operatorname{CH}^2(C_i\times J)_{\mathbf Q},\qquad
 Z_i=(\pi_1^{C_i}\otimes\pi_N)Z_i
\]

is homologically trivial by the preceding Hodge-type argument. It lies in the degree-four Chow–Künneth component of the fourfold C_i×J, since 1+3=4. Thus a nonzero algebraically trivial N-class would violate Murre (D) in codimension two for this explicit product decomposition of some curve times J. This is a conditional obstruction, not a proof of Murre (D) for that fourfold. Transport through h¹(C_i)≅h¹(Jac(C_i)) and then Fourier transform gives precisely the grade-zero CH²(Jac(C_i)×J) obstruction proved in AR15a. No bound on the genus of C_i, and no reduction of all such families to translations, has been proved.

Two close product theorems were checked directly:

* Xu–Xu, *Remarks on Murre’s conjecture on Chow groups*, arXiv:1110.0668v1, Theorem 3.3 and Corollaries 3.7–3.9, especially author p9: for an abelian threefold X and a curve C, their conclusion is Murre (A) and (B) for X×C. It does not assert (D). Their assumption on grade-zero algebraically trivial cycles is on X over the function field, and the proof uses it to obtain (B) on the product, not the missing degree-four injectivity. Primary: https://arxiv.org/pdf/1110.0668 .
* Kenichiro Kimura, *Murre’s conjectures for certain product varieties*, arXiv:math/0509249v2, author p2, isolates the unresolved piece pi1(C1)⊗pi1(C2)⊗pi2(S) acting on CH²_hom(C1×C2×S). Theorem 2.1, author p3, proves vanishing only for the listed support/Cartier conditions and assumes NS(S)_Q=QH and absence of Hodge classes in the indicated pairwise H¹ tensor products. These hypotheses fail for S=E_i²: it has several independent divisor classes, and H¹(E_i)⊗H¹(E_i²) contains nonzero Hodge classes. The theorem therefore does not kill the Fermat family component. Primary: https://arxiv.org/pdf/math/0509249 .

These checked results supply no unconditional vanishing of the algebraically trivial grade-one radical. The existing positive algebraic representative controls its quotient; the rational Chow kernel remains separate.

## Why the standard Somekawa reduction misses this group

Gazaki–Love, *Torsion phenomena for zero-cycles on a product of curves over a number field*, Research in Number Theory 10 (2024), article35, §1.1 and §2.4, equation (2.13), recalls the Raskind–Spiess decomposition of CH0 of a product of curves into Somekawa groups. On E³ this is CH³, whereas the primitive Fermat group is CH²_(1). Beauville's Fourier formula above sends CH²_(1) of a threefold to CH²_(1) again. It sends CH³_(s) to CH^s_(s); reaching codimension two requires grade two, not grade one. Hence Fourier does not convert the needed group into the cited zero-cycle Somekawa group.

Multiplication by theta also cannot give an injection into zero-cycles: the whole N summand is primitive and is annihilated by that Lefschetz operator, including the known nonzero eta. More elaborate correspondences would require their own injectivity proof; none is provided by the zero-cycle decomposition.

There is a further scope distinction inside the zero-cycle results. Gazaki–Love §1.2 and Lemma2.15/equation(2.16) separate the subgroup generated by componentwise rational points from the full Albanese kernel, which also uses points over finite extensions. Their Remark2.17 needs the componentwise property over every finite extension to infer the full torsion statement. Finiteness for the componentwise subgroup at the one base field cannot be substituted for that uniform hypothesis.

Primary: https://link.springer.com/article/10.1007/s40993-024-00519-4 .

## Status of the modular route

The separate note cm_transfer_audit.md records the missing actual algebraic correspondence from a suitable Kuga–Sato component to N. An agreement of compatible realizations, absolute-Hodge motives, or separately constructed Chow realizations does not supply a map on rational Chow groups. Even after an algebraic transfer is supplied, a theorem on the whole modular Griffiths group needs a checked argument after projection to the selected newform component. None of these observations yields the scalar-extended arithmetic Abel–Jacobi injectivity requested above.
