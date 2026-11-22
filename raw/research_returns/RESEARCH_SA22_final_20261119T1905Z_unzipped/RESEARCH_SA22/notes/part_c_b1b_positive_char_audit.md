# Independent audit of the abelian-fourfold deduction in B.1(b)

19 November 2026, 14:40–14:46 UTC. GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode; independent Part C reviewer. Requested by root as a theorem-level audit. The Part B author confirmed that the statement had not recently changed. No manuscript or bibliography was edited during the build freeze.

## Verdict and exact boundary of this audit

**No gap was found in the deduction from the stated Broe theorem to numerical–geometric étale homological equality for abelian fourfolds over arbitrary fields and every invertible prime.** In particular, no hidden ordinary-reduction condition, odd-characteristic restriction, density-one restriction on the prime, Tate conjecture for all powers, or ascent of the property D under arbitrary field extension is being used.

The result remains **Known with checked deduction from a 2026 preprint**, exactly as the manuscript labels it. This audit independently checks the theorem's stated scope, its temporary finite-extension assumptions, the Kahn implication and semisimplicity input, the Ancona specialization argument, and the passage to arbitrary fields. It does not independently certify every argument in Broe's proof of the Tate theorem or in the Markman results used there. No claim of a published theorem or an independently re-proved Tate theorem is made. This audit is verification, not a progress-ledger status change.

Target: sections/part_b.tex lines199–239, theorem thm:B1b-abelian and its proof. The earlier distinction in prop:B1b-gap is preserved.

## Actual original sources read

| Original | Exact passages checked | Local evidence and public source |
|---|---|---|
| Matt Broe, The Tate conjecture for abelian fourfolds over finite fields, arXiv2608.28651v1,19 August2026 | Theorem1.1, printedp1; Corollary1.2 and Remark1.3, p2; Assumption4.1 and Remark4.2, pp9–10; Section8, pp19–20, especially Corollary8.1(i) and Corollary8.2 with its proof | sources/broe.pdf; sources/broe.txt; sources/broe/TateAbelianFourfold.tex lines239–264,463–474,778–799. https://arxiv.org/abs/2608.28651v1 |
| Bruno Kahn, Équivalences rationnelle et numérique sur certaines variétés de type abélien sur un corps fini, Ann. Sci. ENS36(2003),977–1002 | Definition1(a)–(b) and Theorem1, p978; Lemma1.9 and Theorem1.10 with proofs, p982 | sources/kahn2003.pdf and .txt, text lines70–94 and276–294. https://numdam.org/item/10.1016/j.ansens.2003.02.002.pdf |
| Giuseppe Ancona, Standard conjectures for abelian fourfolds, Invent. Math.223(2021),149–212, opened v3 source | Global conventions; Definition3.8/Conjecture3.10; Proposition3.11 and Corollary3.12; Theorem3.18; Corollary3.19 and complete proof; Theorem3.20 | sources/ancona/fourfolds_2020.tex lines369–414,438–589, especially570–587. https://arxiv.org/html/1806.03216v3 |

The published Kleiman algebraic Lefschetz theorem is the manuscript's previously opened Theorem2A11, also Proposition4-3(2)(c) in Kleiman1994. It is not replaced by an assumption that an arbitrary fourfold has algebraic Lefschetz projectors.

## 1. What Broe's theorem actually says

Theorem1.1 fixes an arbitrary finite field k of characteristic p and an arbitrary prime ell different from p, and states surjectivity of the codimension-two cycle map from CH²(A) tensor Q_ell to the Galois-fixed part of H⁴(A over the algebraic closure,Q_ell(2)), for every abelian fourfold A/k. The source does not exclude p=2 or impose ordinarity, simplicity, a particular endomorphism algebra, or a positive-density set of primes. Its Corollary1.2, restated and proved as Corollary8.2, is exactly the arbitrary-field conclusion used in the manuscript.

Assumption4.1 is temporary. It arranges that geometric endomorphisms are defined over k and that classes fixed after finite extension are already fixed over k. A finite extension suffices: the endomorphism group is finitely generated, so finitely many generators descend; in the finitely many cohomological degrees0–8, there are only finitely many root-of-unity Frobenius eigenvalues, whose orders can all be killed by one extension. No infinite extension is needed.

The removal of that assumption in Remark4.2 is valid. If x is fixed over k and is the class of a Q_ell-linear combination z of cycles over a finite extension k'/k of degree m, pushforward to A has class equal to the sum of the m conjugates of x, namely m x. Dividing by m is legitimate in Q_ell even if ell divides m. Thus a Tate surjectivity proof after finite extension descends to the original finite field. The auxiliary isogeny replacements also preserve Tate surjectivity through the usual pull–push identities with rational coefficients. These reductions impose no residual restriction on the final theorem.

## 2. The Tate-to-D implication has its required semisimplicity

Kahn Definition1(a) puts the Chow motive of an abelian variety in the required rigid thick subcategory by definition. Definition1(b) requires the Tate conjecture on that variety in all codimensions for one invertible prime. It does **not** require the Tate conjecture on every power A^n. The stronger-looking Theorem1.10 concerns X times X', but Theorem1 is its case X'=Spec k.

Broe's codimension-two theorem supplies the only remaining degree for an abelian fourfold. Codimension one is Tate's divisor theorem. Multiplication by the square of a k-defined ample divisor gives the Galois-equivariant hard-Lefschetz isomorphism H²(1) to H⁶(3); its inverse on cohomology takes an invariant class to an invariant class, which is represented by a divisor, and multiplying that divisor by h² represents the original codimension-three class. Codimensions zero and four follow from the fundamental class and the k-rational origin. Thus the Tate hypothesis needed by Kahn holds in every degree.

The semisimplicity is not assumed without support. Kahn Lemma1.9, p982, proves that Frobenius is semisimple on the realization of every abelian-type motive. For an abelian variety, the Frobenius endomorphism lies in the center of the semisimple Q-algebra End(A) tensor Q. Its minimal polynomial is therefore squarefree in characteristic zero. This gives semisimplicity on H¹ and hence on its exterior powers; direct summands preserve it. There is no odd-p or odd-ell restriction. Kahn's Definition1(b) explicitly points to this lemma when discussing independence of the Tate condition from ell.

Kahn Theorem1 now gives rational equivalence equal to numerical equivalence with Q coefficients on A/k. The inclusions

    rational-zero cycles ⊆ ell-adically homological-zero cycles ⊆ numerical-zero cycles

then force equality of the last two for every invertible ell. This is precisely Broe Corollary8.1(i), not an inference from Ancona's numerical positivity alone. The fact that Kahn's proof of Theorem1.10 first proves homological–numerical equality is not circular: that preliminary implication uses Tate plus the separately established Frobenius semisimplicity, not the equality it is about to prove.

An independent linear-algebra check also verifies the exact finite-field conclusion without using the stronger rational-equivalence conclusion. Let V=H⁴(A over the algebraic closure,Q_ell(2)), with Frobenius T and its perfect intersection pairing q. Frobenius is a semisimple isometry. The restriction of q to V^T is nondegenerate: after extending the coefficient field to diagonalize T, the1-eigenspace is orthogonal to every eigenvector of eigenvalue different from1, so a vector radical on V^T would be radical on all V. Broe's theorem says that cycle classes span V^T over Q_ell. A numerical-zero cycle defined over k has class in V^T orthogonal to that whole span, hence has zero class. The analogous pairing in complementary degrees gives the other codimensions. This proves that no extra semisimplicity conjecture or all-powers Tate statement is hidden in the finite-field step.

## 3. Why Ancona's specialization transfers definiteness

Ancona's numerical positivity is correctly distinguished from homological positivity. His Proposition3.11 identifies the radical on algebraic homological classes with numerical-zero classes. His Corollary3.12 gives only semipositivity before that radical is removed. His Theorem3.18 gives numerical primitive positivity. Corollary3.19 uses numerical–homological equality on a special fibre to remove its radical, and then transfers the resulting definite form to the generic fibre. The manuscript follows that argument and does not replace it with the false positivity-on-a-quotient inference.

Here is a fixed-cycle version which also makes precise the spreading needed in the manuscript. Start with a rational codimension-two cycle z on an abelian fourfold over a finitely generated field K, and an ample class h. Algebraic Lefschetz projectors give the orthogonal decomposition of its class

    alpha = a h² + h beta + gamma,

where beta is an algebraic primitive divisor class and gamma is an algebraic primitive codimension-two class. There are only finitely many cycles and correspondences involved in this decomposition. Spread the abelian variety, h and these finite data to an abelian scheme over a nonempty integral finite-type base S over Z[1/ell], shrinking to make the chosen cycle closures flat and to retain the required smooth proper family. In positive characteristic one may take S over the corresponding prime field. A regular open of a model may be used if a specialization through regular traits is desired.

Choose a closed point s of S. Its residue field is finite and ell remains invertible. Smooth proper base change, with a chosen geometric specialization, is an isomorphism on cohomology, preserves products and traces, and sends the classes of the spread cycles to their fibre classes. Therefore a nonzero gamma stays nonzero, its primitiveness is preserved, and its rational self-intersection number is unchanged. On the special fibre, the finite-field result in the preceding section and Ancona's Theorem3.18 make the primitive homological form positive definite. Consequently gamma has positive square if nonzero.

If z is numerically trivial, test its class against the three algebraic Lefschetz components. Orthogonality gives zero for the square of each component. Positivity of the h² summand forces a=0. The divisor index theorem, together with numerical–homological equality for divisors, forces beta=0. The just-established primitive positivity forces gamma=0. Thus z has zero geometric ell-adic class.

This argument does not assert that a numerical-zero generic cycle remains numerically zero on a special fibre: new special-fibre cycles can prevent that assertion. It only preserves its self-intersection and uses definite special-fibre homological pairing. It also does not require finding one spread on which every possible generic cycle is flat; the finite collection needed for each fixed z suffices. These points remove potential overreadings of the concise specialization paragraph.

All other codimensions follow as stated. Divisors satisfy numerical–homological equality; algebraic Lefschetz carries this to one-cycles. Codimension zero and zero-cycles are handled by geometric connectedness and degree. The theorem does not assert rational–numerical equality over arbitrary positive-dimensional function fields: Kahn's stronger rational statement is used only over finite fields.

## 4. Arbitrary ground fields and imperfect fields

For an arbitrary field k and a fixed cycle z, descend A, its group law, a polarization and z to a subfield K finitely generated over the prime field. If z is numerically trivial over k, its model z_K is numerically trivial over K: every complementary cycle over K may be pulled back to k, where the intersection vanishes, and extension of the ground field preserves the degree. Apply the preceding finitely generated-field argument to z_K. Geometric étale cohomology and its cycle maps are invariant under extension of algebraically closed fields, so the vanishing of its class persists on A over an algebraic closure of k.

This is a deduction for each fixed descended cycle; it is **not** an assertion that D automatically ascends to every field extension from D on a previously fixed model. No perfectness hypothesis is imposed on the final k. A finitely generated field of positive characteristic can be spread over its perfect prime field; a general imperfect extension is treated by the same geometric cohomology comparison. The condition ell different from the characteristic remains necessary and is present in the theorem.

## Final audit table

| Potential failure | Outcome |
|---|---|
| Theorem only for ordinary or simple abelian fourfolds | Refuted as a reading of the source: Theorem1.1 is unrestricted. |
| Hidden exclusion of characteristic2 or ell=2 | None in the source theorem or the deduction; only ell different from p. |
| Temporary finite-extension assumptions fail to descend | Transfer with rational coefficients proves descent. |
| Tate required on all powers of A | Not needed by Kahn Theorem1; X'=Spec k in Theorem1.10. |
| Missing Frobenius semisimplicity | Supplied by Kahn Lemma1.9, p982, with proof. |
| Tate surjectivity does not by itself give D for general varieties | Correct caution, but semisimplicity is established here; the direct eigenspace proof above applies. |
| Ancona positivity used on the wrong quotient | Not in the current proof: finite-field D is supplied first, then Corollary3.19. |
| Numerical triviality incorrectly specialized | Not needed; preserve cohomology and the rational pairing instead. |
| D incorrectly ascended under arbitrary base change | Not in the current proof: descend each fixed cycle and then extend its vanishing. |
| Full Broe/Markman proof independently certified here | Explicitly not claimed; the source theorem remains a stated preprint input. |

No corrective TeX change is required for validity. A future optional citation refinement could add Kahn Lemma1.9, p982, alongside Theorem1, p978, but the current citation to the full theorem already supplies a legitimate known result. No finite computation or optional test was performed in this audit.
