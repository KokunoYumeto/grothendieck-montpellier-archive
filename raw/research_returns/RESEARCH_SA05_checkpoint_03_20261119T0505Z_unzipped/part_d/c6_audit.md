# Independent C.6 audit: finite inertia on abelian motives

Date: 19 November 2026. Author within the run: Part D agent. This is a proof-development record, not a replacement for Part C's section. The proof below is supplied to the root and Part C for independent checking.

## Claim and status

Let K be a number field, v a finite place of residue characteristic p, and M a rational motive of abelian type in either Deligne's category of absolute Hodge motives or André's category of motivated motives. For every prime ell different from p write V_ell(M) for its ell-adic realization, restricted to a fixed decomposition group at v. The desired assertion is

> If V_ell0(M) is unramified at v for one ell0 != p, then V_ell(M) is unramified at v for every ell != p.

The argument below proves this using (i) Noot's weak Mumford–Tate lifting construction, (ii) semistable reduction and Néron–Ogg–Shafarevich for abelian varieties, and (iii) the October 2026 theorem proving Milne's rationality conjecture. It treats arbitrary tensor summands and arbitrary finite arithmetic descent. The proof uses the rationality theorem only for pairing a specialized Hodge projector with graphs of homomorphisms, which are Lefschetz classes. It does **not** need algebraicity of the specialized projector or the October 2026 CM Hodge theorem.

The prime p=2 is included by the rationality theorem. The coefficient prime ell=2 is included whenever p!=2. Nothing here identifies unramifiedness of the p-adic realization with good reduction: p is excluded from the assertion, as in the question.

The general-motive case remains a separate question. This argument uses the full faithfulness of Hodge realization for abelian motives and weak Mumford–Tate lifting to an abelian variety, and makes no assertion that either extends to arbitrary motives.

## Opened primary sources and exact locators

1. Rutger Noot, *Lifting systems of Galois representations associated to abelian varieties*, author PDF dated 2 October 2006, 50 pages, https://irma.math.unistra.fr/~noot/publications/pp-jrms.pdf . Local files: `sources/Noot2006.pdf` and `.txt`. The published article is *Journal of the Ramanujan Mathematical Society*, 21(4), 299–342 (2006). Source locators below use the author PDF's printed pages.
   - Definition 2.1, pp. 10–11: weak Mumford–Tate lift of an arbitrary abelian motive.
   - Theorem 2.12, pp. 15–18: essentially unliftable, Mumford–Tate decomposed abelian weak lift of an abelian variety.
   - Definition 2.10, p. 15: decomposition into abelian varieties with independent Q-simple adjoint groups.
   - Corollary 2.15, p. 20, including its proof: weak lift of an arbitrary abelian motive by selecting the simple factors that survive in its Mumford–Tate group.
   - Proposition 3.1 and Corollary 3.2, pp. 20–21: descent of weak lifts from C to an algebraically closed subfield. The proof uses finite maps of connected Shimura varieties; it cites Deligne 1979, 2.7.11(b).
   - Proposition 3.4, pp. 22–23, including its proof: generation by a weak lift and CM motives; its representation-theoretic proof works with an arbitrary abelian motive in place of h1(A).
   - Corollary 3.6, p. 23: a decomposed generator over an algebraically closed subfield.
   - Section 4.1, p. 23: after a finite field extension, the arithmetic realizations take values in the connected Mumford–Tate group; Proposition 4.5 gives compatibility for weak geometric lifts of abelian varieties.
   - Web openings: `turn118759548view1`, `turn588989165search34`.
2. *Milne's rationality conjecture*, ChatGPT and Claude, 13 October 2026, prepared with questions, feedback and light editing from Keerthi Madapusi; attribution is stated in Section 1.1, p. 3. Primary exposition hosted by Madapusi: https://keerthimadapusi.com/assets/ai-notes/milne-rationality/milne-rationality.pdf . Theorem 1.1, pp. 1–2, is the needed common rational pairing of a specialized rational Hodge class with any complementary rational Lefschetz class, simultaneously in every ell-adic realization ell!=p and in crystalline cohomology, including p=2. Web opening `turn795149840view1`; HTML proof also opened at https://keerthimadapusi.com/assets/ai-notes/milne-rationality/milne-rationality , refs `turn636262233view1`, `turn716611154view1`.
3. OpenAI, *Milne's rationality conjecture for abelian varieties*, 7 October 2026, Theorem 1.1, p. 1. Full primary manuscript mirror opened at https://mathcommunity.github.io/oai-math-revised/papers/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf , refs `turn636262233view0`, `turn716611154view0`. Corollary 6.4, p. 33, asserts common algebraic specialization using the CM Hodge theorem, but is stronger than what this proof needs. Direct GitHub and raw-GitHub opens were blocked by the web retriever (`DisabledError`); an archival urllib retrieval was attempted separately.
4. Kisin–Zhou, *Strongly compatible systems associated to semistable abelian varieties*, arXiv:2505.02165v1 (2025), Theorem 1.2 and Section 5.3.3. Local files in `../part_c/sources/kisin_zhou2025.*`. Theorem 1.2 gives the semistable G-valued Weil–Deligne comparison. Section 5.3.3 first passes to the field fixing Hodge cycles, and the introduction explicitly does not claim G-valued descent at arbitrary bad places. This is why a bare appeal to Theorem 1.2 is insufficient for the original K. The final proof below does not need its Weil–Deligne comparison.
5. Tim and Vladimir Dokchitser, *Character formula for Weil representations in terms of Frobenius traces*, primary author/institutional PDF https://discovery.ucl.ac.uk/id/eprint/10205744/1/weil2-ems.pdf . Theorem 1.1 and Corollary 1.3 reconstruct a semisimple Weil representation from traces over **all** suitable extensions where it becomes unramified. Corollaries 1.4–1.6 treat Weil–Deligne representations. Remark 1.9 discusses omissions in Saito 1997, Lemma 1. These are a viable alternative only after controlling the field of Hodge tensors; traces over extensions containing one fixed ramified extension do not suffice. The final proof below avoids this issue. Local `sources/DokchitserDokchitser2024.*`; opened `turn118759548view2`.
6. Milne, *Abelian motives and Shimura varieties in nonzero characteristic*, v2.2, 2 November 2025, https://www.jmilne.org/math/articles/SVp22.pdf . Definitions 0.12 and Section 1 distinguish the Néron condition from visibly good reduction (5.10). Theorem 1.10 has its proof omitted; the passage after Theorem 5.1 leaves the general extension as an exercise. Sections 1.23 and 5.7 only give statements after finite extension. These statements are not used as a completed proof of original-field inertia independence. Local `sources/MilneSVp22.*`.

## Lemma 1: a potentially unramified abelian motive has a potentially good abelian generator

Suppose V_ell0(M) is potentially unramified at v. There is a finite extension E/K and finitely many abelian varieties B_j/E, each potentially good at every place of E above v, such that M_E belongs to the tensor category generated by their h1 motives. Tate twists may be retained explicitly. The extension E can be enlarged to be Galois over K.

### Construction over Qbar

Fix the chosen complex embedding. Over Qbar an abelian motive M is generated by h1(A) and Tate objects for an abelian variety A/Qbar. Apply Noot Theorem 2.12 to A_C. Its weak lift B0_C has a product decomposition into abelian factors B_i with independent Q-simple derived groups, and these derived groups form a direct product (Theorem 2.9 and Definition 2.10). Proposition 3.1 descends B0_C to Qbar. Every factor B_i descends up to isogeny, since the relevant rational idempotents in End(B0_C) are defined over Qbar: Hom of abelian varieties is unchanged by extension of algebraically closed fields. Isogeny is sufficient throughout this rational motive category.

The surjection of Mumford–Tate groups associated with M selects precisely those Q-simple factors that act nontrivially on M. Their product B, as in the proof of Noot Corollary 2.15, satisfies

    pi_der : MT(B)^der -> MT(M)^der

with pi_der a central isogeny and with the adjoint Hodge homomorphisms identified. This is a weak Mumford–Tate lift of M; the construction takes place over Qbar.

The proof of Noot Proposition 3.4, with V_M replacing V_A, proves that M lies in <h1(B), CM>. The key argument is representation theoretic. On the common group formed from the central tori and MT(B)^der, the representation V_M is generated by the faithful V_B and characters. Choose an irreducible constituent W2 of V_M and an irreducible constituent W1 of a tensor construction in V_B such that W2 occurs in W3 tensor W1 for a representation W3 factoring through a torus. The contraction W2 tensor W1^dual -> W3 is nonzero, hence surjective after choosing W3 irreducible. Thus W3 itself is a Hodge subquotient of actual abelian Hodge structures, not a fractional or merely formal character. Its Mumford–Tate group is a torus, so it is a CM Hodge structure. The established equivalence of CM Hodge structures and CM motives makes W3 a CM motive. Full faithfulness of Betti realization for abelian motives then lifts the inclusion of V_M into the tensor category to the corresponding motive inclusion. Finitely many CM abelian varieties suffice for this one M.

This proof is valid in both requested categories: Deligne's absolute-Hodge theorem identifies Hodge maps on abelian motives with absolute-Hodge maps; André Theorem 0.6.2 identifies them with motivated maps. All the abelian varieties, projectors and finitely many comparison morphisms descend to one finite extension E/K.

### Potential good reduction, with the direction of transfer proved

Let H=MT(M_Qbar direct-sum h1(B)). The two projections to MT(M) and MT(B) identify its adjoint Hodge datum with the common adjoint datum above. Indeed, the Hodge homomorphism of H is contained in the fibre product over the identified adjoint groups, and it surjects on each factor by the definition of Mumford–Tate group. The derived group of H therefore has central isogenies onto both derived groups. In particular,

    H^der -> MT(M)^der

has finite kernel.

Enlarge E so that the ell-adic realizations of M direct-sum h1(B) take values in H(Q_ell) for every ell. This is legitimate because H is cut out by finitely many absolute Hodge tensors, each defined over a finite extension, and the same tensors have compatible realizations. Fix a place w of E over v. After a further finite local extension, M_ell0 is unramified and B is semistable. For inertia tau there, the element

    u_tau = (1, rho_{B,ell0}(tau)) in H(Q_ell0)

is unipotent, by semistable reduction for B. A unipotent element maps trivially into the torus H/H^der, so u_tau lies in H^der. It maps to the identity in MT(M)^der. A unipotent element in a finite group in characteristic zero is the identity. Consequently rho_{B,ell0}(tau)=1 for every such tau. Néron–Ogg–Shafarevich gives good reduction of B over this local extension.

The argument applies to **every** w over v, since potential unramifiedness of M_ell0 transfers from K_v to every such completion. Therefore B is potentially good at every w over v. The finitely many auxiliary CM abelian varieties are potentially good too: after fixing their Hodge tensors and taking a semistable extension, their inertia is both unipotent and contained in a torus, and hence trivial; apply Néron–Ogg–Shafarevich. Taking products gives the stated finite collection of potentially good generators.

This lemma only concludes potential good reduction of a generator. It does not claim that M was unramified over K merely because its restriction to E was unramified.

## Lemma 2: finite inertia characters for summands of potentially good abelian generators

Let N/K be a rational absolute-Hodge or motivated summand of a finite direct sum of motives induced from h^{i_a}(A_a)(m_a) over finite extensions of K. Assume every conjugate A_a is potentially good at v. Then the trace of every tau in I_v on V_ell(N) is a single rational number independent of ell!=p, and all these inertia representations factor through one finite quotient of I_v.

Choose a finite Galois extension L/K_v over which all conjugate abelian varieties have good reduction and all finite fields of induction split. A common such L exists because the collection is finite. Smooth proper base change shows that I_L acts trivially on the ambient representations for every ell!=p. Inertia I_v thus acts through the same finite quotient Delta=I_v/I_L on the ambient object and every summand. Tate twists are inertially trivial for ell!=p.

After splitting the induced varieties, the ambient special fibre is a finite disjoint union of abelian varieties, with finitely many cohomological degrees and twists. Néron uniqueness extends the descent isomorphisms to the good models. Every tau in Delta acts on the special fibre by a permutation of components and origin-preserving algebraic isomorphisms between them: inertia acts trivially on the algebraic closure of the residue field. Denote these isomorphisms by u_{tau,s}. Their actions on cohomology give the specified Galois action through smooth proper base change.

Let e be the motivic idempotent cutting out N. On each relevant product of two conjugate components its matrix entry is a rational Hodge class. Its ell-adic specialization is the matrix entry of e_ell, because realization and smooth proper specialization respect tensor operations, polarizations, Künneth projectors, duality and twists. We may treat one cohomological degree i and one twist at a time in the trace: the ambient Galois action preserves every original direct summand, so only the corresponding diagonal block of e contributes. Within an induced block, inertia may permute conjugate components, which is handled by the corresponding matrix entries of e.

The class of the graph of an origin-preserving isomorphism u:X0->Y0 of d-dimensional abelian varieties is a rational Lefschetz class on X0 x Y0. Set f(x,y)=y-u(x). Then Gamma_u=f^{-1}(0), and cohomologically

    [Gamma_u] = f^*[0_Y]
              = f^*(theta_Y^d / deg(theta_Y^d)).

Here theta_Y is any ample divisor class. The last equality holds in every Weil cohomology by the common degree normalization of top classes. Thus the graph is represented in every realization by the **same** rational polynomial in divisor classes. The formula remains valid at p=2 and does not require u to lift to the generic fibre.

For clarity, use the correspondence convention Z_*(x)=(pr2)_*([Z] cup pr1^*x). A graph Gamma_u acts by u_*=(u^{-1})^*. Therefore the alternating trace of e_* composed with u^* is the intersection of e with Gamma_u. If e is supported on cohomological degree i, its ordinary trace is (-1)^i times this pairing. The same identity, with the matrix entries indexed by the component permutation, holds on a finite disjoint union. Hence

    Tr(tau | V_ell(N))

is a finite sum, with rational coefficients and explicit signs (-1)^i, of pairings of specialized rational Hodge classes with complementary rational Lefschetz classes on products of good abelian varieties.

Theorem 1.1 of the October 2026 proof of Milne's rationality conjecture states that each such pairing is one rational number simultaneously for all ell!=p. This proves the assertion. No chosen common algebraic representative of the projector is needed.

## Descent to K and conclusion

Start with V_ell0(M) unramified at v. Apply Lemma 1, choosing E/K finite and Galois, so M_E is a summand of a finite direct sum P of h^{i_a}(A_a)(m_a) with A_a potentially good at every place above v. The use of a finite direct sum is harmless: tensor constructions in h1, their duals, and Tate twists occur as rational Künneth summands of powers of abelian varieties, and finite collections of auxiliary CM varieties can be included in those products.

Restriction and induction for rational motives give natural maps

    M -> Ind_E^K(M_E) -> M

whose composite is multiplication by [E:K]. Dividing the second map by [E:K] makes M a direct summand of Ind_E^K(M_E), and hence of Ind_E^K(P). This can also be checked after base change to E: the unit is the diagonal map into the direct sum over Gal(E/K), and the counit is the sum of the canonical identifications. These maps are defined by finite étale correspondences, so apply in both motivic categories.

The induced ambient object is the motive of the finite disjoint union of conjugate abelian varieties/powers, viewed as a smooth projective K-scheme; its components are all potentially good at v by Lemma 1. Lemma 2 now applies **over the original K**, not only over E. There is a common finite quotient Delta of I_v and a common rational trace t_tau on M for every tau in Delta. Since the ell0-realization is unramified,

    t_tau = dim_Q omega_B(M)

for every tau. In any other realization tau has finite order. Its eigenvalues are roots of unity, and in a complex embedding their sum equals their number. Equality in the triangle inequality implies that every eigenvalue is 1. Finite-order operators in characteristic zero are semisimple, so tau is the identity. Consequently I_v acts trivially on V_ell(M) for every ell!=p, as required.

The argument proves a slightly stronger intermediate statement: if an abelian motive is potentially unramified in one prime-to-p realization, then its finite inertia character (after the above common finite quotient) is rational and independent of the realization. It does not prove full Weil–Deligne compatibility for arbitrary abelian motives with nonzero monodromy.

## Earlier approaches and precise reasons for not using them

- Néron–Ogg–Shafarevich applied only to an initial generator A cannot infer good reduction of A from unramifiedness of a tensor summand M. Lemma 1 changes the generator by a weak Mumford–Tate lift and proves that this new generator is potentially good.
- Passing to one fixed ramified extension where everything is semistable loses the finite inertia quotient. The induction-and-trace step above explicitly recovers the inertia action over K.
- Kisin–Zhou's semistable theorem plus the Dokchitser–Dokchitser reconstruction theorem does give a route to individual GL-valued comparisons when all relevant Hodge tensors are fixed over the original field. The reconstruction needs traces over all suitable nonnormal extensions in F^nr, not merely those containing F. The field fixing the Hodge tensors can be ramified, so that route alone does not settle the full question.
- Commelin's quasi-compatibility theorem concerns Frobenius powers at places where both systems are already unramified; its definition does not give independence of the set of ramified places.
- Algebraic specialization (original rationality manuscript, Corollary 6.4) would suffice for the trace step, but the graph is already Lefschetz. The weaker rationality theorem is exactly enough and avoids invoking the CM Hodge theorem.

## Independent review requests and record

- Root asked to audit the finite-inertia trace argument, including all projector tensor constructions and component permutations.
- Part C independently read Noot Corollary 2.15 and Propositions 3.1/3.4. They confirmed the descent of B0 and its selected factors and the extension of Proposition 3.4's proof to arbitrary M. They proposed the common group H argument above, which eliminates any ambiguity about separately identifying adjoint monodromy operators. The completed independent verdict will be appended when received.

### Completed independent checks

Part C completed the weak-lift and descent audit and saved `../part_c/c6_weak_lift_independent_audit.md`. In particular, for the common group H, the kernel of H->MT(M) lies in {1} x Z(MT(B)), hence is central in H and intersects H^der in a finite group. Surjectivity on derived groups proves the required central isogeny. The elementwise argument with unipotents in that finite kernel passes. The reviewer also checked descent through B0 and its rational endomorphism idempotents, the arbitrary-M extension of Proposition 3.4, finite descent of the morphisms, and the induction splitting over K.

Root independently read the rationality theorem and checked the trace argument. The final insert explicitly treats every place above v before induction, the sign (-1)^i from the Künneth degree, and cross-component origin-preserving homomorphisms on good special fibres. Root confirmed that the CM Hodge theorem is not required.

The official raw GitHub PDF of the original rationality manuscript was successfully archived by urllib, despite the web retriever's DisabledError. The archived file is `sources/OpenAIRationality2026.pdf`, SHA256 `640701a0ea8d8026d2f019e571e052f2d106cad3f5216cf6f7fca0d643873234`. Madapusi's hosted exposition was also archived (`sources/MadapusiRationality2026.pdf`, SHA256 `be2ff9f442e8e566366566e7a996f0cb02d993dbea961aae8cc3082f6ba21951`). The downloader and manifest preserve both exact URLs and hashes.

Noot's own publication page, https://www.math.unistra.fr/~noot/publications/jrms.html (opened search ref `turn869652434search0`), verifies the journal bibliographic data and states that the preprint text is identical to the published article.
