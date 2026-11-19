# Cote 68, scans 33–56, and cote 161-6

## Scope and evidence

This part consolidates all 53 indexed entries in the Pro package `MPL_68_033-056+162-1+162-6`, merged into 45 items, and adds a complete reading of both Codex cote-161-6 transcriptions. The actual Pro transcription contains 21 leaves from cote 68. Despite the package name, it contains no transcription of cote 162-1 or 162-6. Those names occur in contextual comparisons and earlier project leads; they supply no archival endpoint here. Their absence is a property of the supplied package. Exact file coverage is in `coverage.md`.

The supplied cote-68 sequence runs from the end of the two-player discussion through exponential algebra, an N-player restart, orientation axioms interleaved with three literary versos, and graded determinant axioms. Cote 161-6 proceeds through Euclidean icosahedra, cyclotomic arithmetic, frames and topoi, graph embeddings in surfaces, and coset descriptions of symmetric graphs. The individual mathematical leaves have no authorial dates. The official Montpellier catalogue gives bracketed dossier estimates—cote 68 from 1978 to at least 1983, cote 161-6 from 1973 to about 1977. These are external estimates, not dates read on these leaves. Its whole-dossier counts, 55 and 33 pages, also differ from the selected 21 cote-68 leaves supplied here. [MontpellierCatalog, cote 68 footnote 58 and catalogue entries.]

Three layers remain separate: the literal transcription, a checked external result with its hypotheses, and the present reconstruction. A mathematically compelling replacement never decides uncertain ink. A cancelled passage can be correct, and a later live passage can repeat an error withdrawn in an earlier margin. The reading index preserves those distinctions. No scans, second-pass files or proof-assistant certificates were used.

## 1. Games: terminal data and well-founded induction

Cote 68, scan 33, lines 2–43, expressly restricts the successor clauses to nonterminal positions. Terminal outcomes are independent boundary data. On scan 34, condition 1 quantifies over every proposed winner without repeating the restriction. This stronger condition does not invalidate the proposition's sufficient implication: a minimal-rank counterexample still contradicts the successor conditions. It does invalidate necessity in the final equivalence. One terminal winner satisfies the outcome assignment while having no required successor. SA23-303–305 and C-SA23-misc-001–003 retain this distinction; the earlier notes correctly identify that a contextual diagnosis had overstated the defect.

“No infinite play” supplies a well-founded relation, not one finite bound on all play lengths. Ordinal induction is the appropriate proof. Apt and Simon's Theorem 14 treats well-founded win/lose games and Theorem 17 treats draws. These results support the determinacy framework, while the exact terminal convention is reconstructed from the transcription. The graph-kernel interpretation in SA23-306 additionally assumes terminal positions are losing and cannot silently replace the more general terminal data. [AptSimon2021, Theorems 14 and 17.]

The N-player leaf, scan 48, defines players, initiative, trajectories and a cyclic scheduler. Its scheduler uniqueness assertion is correct under the explicit coverage condition: for every player (a), choose an outgoing move (x\to y) with (j(x)=a); any scheduler must send (a) to (j(y)). Surjectivity of (j) alone supplies no equation for a player appearing only at terminals. A circular-permutation requirement is additional structure. The deletion of “winning” in favour of “terminal” is substantive: this leaf gives no payoff data or N-player equilibrium theorem. [SA23-307–308; C-SA23-misc-004; scan 48, lines 505–558.]

## 2. Exponentials and finiteness conditions

### Finite exponential algebra

In an associative unital rational algebra, finite exponential and logarithm biject nilpotent elements and unipotent units. Commuting elements satisfy the usual laws. A power-stable rational subspace consisting of nilpotents is preserved by these finite polynomials, without a common exponent. A nil subalgebra (L) gives a group (1+L), commutative exactly when (L) is commutative, by expanding ((1+x)(1+y)). If the uncertain marginal converse instead concerns the universal exponential addition identity, substitute (tx,sy) and compare the (ts) term. This proves a universal assertion, not a statement about one accidental pair. [C-SA23-misc-005–010; MP-SA23-misc-01; Milne2017, Proposition 14.32 and Corollary 14.33, with its field and finite-type hypotheses distinguished from our algebraic proof.]

The supplied Example 2 explicitly inserts the hypothesis that (J) is nilpotent. If (J^r=0), endomorphisms carrying (M) into (JM) raise the (J)-adic filtration, so any product of (r) of them vanishes. In the preceding central-coefficient example, mere nilness of (J) suffices element by element: each finite sum uses finitely many central nilpotent coefficients, which generate a nilpotent ideal. SA23-310 therefore corrects the contextual assertion that the stronger hypothesis was absent. The earlier warning remains useful but does not refute the qualified manuscript example.

The script checks exp/log modulo (x^n), (2\leq n\leq9), commuting coefficients and corrected intertwiner coefficients. These finite checks support the instances; the general proof is finite formal algebra. The literal “exp 1 = 0” remains a reading alarm. Its meaningful companion to (\exp0=1) is (\log1=0), but no transcription is altered.

### Formal, uniform and local nilpotence

The one-parameter theorem needs a universal-ring input. For the nilpotent-scalar formal additive functor, evaluate on (K[t]/(t^n)). The compatible coefficients obey

\[
\binom{i+j}{i}a_{i+j}=a_i a_j,
\qquad a_n=\frac{a_1^n}{n!}.
\]

For the ordinary additive functor, evaluate at (t\in K[t]). Its image is an actual polynomial in (U[t]), whose finite support forces (a_1) nilpotent. This proves the assertions for targets (U\otimes_K-), without requiring finite projectivity of (U). [C-SA23-misc-011–012; scans 37–38, lines 137–238.]

A module-functor action instead gives (M\to M[t]). Each vector has a finite orbit polynomial, but the whole module may have no uniform bound. Thus ordinary additive-group actions correspond to locally nilpotent endomorphisms. Translation on (\mathbb Q[x]), generated by (D=d/dx), refutes the uniform assertion: (D^n(x^n)=n!\ne0) for every (n). Finite generation restores a common exponent by taking bounds on generators; finite projectivity additionally gives the endomorphism base-change isomorphism. Yuan explicitly proves the arbitrary-module result over a rational algebra. Milne's rational-representation theorem is related field-valued context. [C-SA23-misc-013–014; QiaochuYuan2017, “In characteristic zero”; Milne2017, Theorem 4.8.]

Intertwiners survive this correction. From (f\exp(u)=\exp(v)f), truncate the logarithm separately on each vector and its image to obtain (fu=vf), even for locally nilpotent operators. The longer manuscript proof needs (\operatorname{Hom}(M,N)) as ambient space and coefficients (-1/(i+j+1)!). The tensor generator is (u\otimes1+1\otimes v). Treating multiplication as a tensor morphism proves the stated derivation/automorphism correspondence even for nonassociative, nonunital algebras. Tensor, symmetric and exterior algebras inherit the action, but uniform nilpotence on the initial module gives only degreewise nilpotence, hence local nilpotence on the unbounded tensor algebra. [C-SA23-misc-015–017,039.]

The Hom warning is substantial. Take (K=\mathbb Q[\epsilon]/(\epsilon^2)) and (M=K\oplus\mathbb Q). The canonical endomorphism base-change map has four-dimensional source and target over (\mathbb Q), but rank three. The nonzero map from the second summand to (K) sending (1) to (\epsilon) dies on reduction. The saved calculation gives the commuting-matrix family, kernel and missing image direction. This verifies the earlier notes' example, without assigning a motive for the cancelled (U_0) notation. [SA23-311,316; C-SA23-misc-018; ED-SA23-misc-02.]

The unrestricted functor question has two negative answers. On (A\mapsto A_{\mathrm{red}}), the distinct natural endomorphisms zero and identity have identical formal exponentials, because every nilpotent test scalar acts by zero. Formal injectivity fails. Ordinary surjectivity from uniformly nilpotent endomorphisms already fails for polynomial translations. Both are actual examples in the stated functor class. [SA23-317; C-SA23-misc-019; MP-SA23-misc-03.]

### Globalization and differential automorphisms

The sheafwise abbreviation “locally nilpotent” matters. A locally nilpotent derivation of a reduced local rational algebra is zero: its exponential sends a unit to a unit in (A[t]), which must be constant; the derivation therefore kills units, and every local-ring element is a unit or differs from a unit by 1. Characteristic-zero derivations preserve the nilradical, so this gives identity on reduction. Stalkwise nilpotence permits local finite exponentials to glue: if (D^n(a)) vanishes at a stalk, it vanishes on a neighbourhood, as do its higher iterates. Conversely (d/dx) on (\mathbb Q[x]) is not locally nilpotent after adjoining (x^{-1}), so it does not refute a genuinely sheafwise assumption. [C-SA23-misc-020; MathlibPolynomialNilpotent, the documented polynomial-unit lemmas; DuboulozLiendo2014, Theorem 2.1, whose semi-affine rational-integrability hypotheses are different.]

For an automorphism (u) of a commutative rational algebra, set (J=(u(a)-a:a\in A)). With (m_a) denoting multiplication by (a),

\[
[u,m_a]=m_{u(a)-a}u.
\]

An iterated commutator is multiplication by a product of differences followed by (u). Since (u(1)=1), its vanishing is precisely the corresponding power of (J) vanishing. Thus (u) has differential order at most (n) exactly when (J^{n+1}=0). The exact definitions were checked in EGA IV, Definition 16.8.1, pp.39–40, Proposition 16.8.8, pp.42–43, and Stacks Tag 09CH. [C-SA23-misc-021.]

The upper margin correctly replaces unipotence as an equivalent condition by sufficiency, with the same bound. To supply the missing argument, suppose (D^m=0). Its (m)-fold commutator with multiplication by (a) is multiplication by (m!(Da)^m), hence ((Da)^m=0). Substitute (a=\sum t_i a_i) and extract the coefficient of (t_1\cdots t_m): polarization yields (Da_1\cdots Da_m=0). Therefore the ideal generated by (D(A)) has zero (m)-th power. This exact power identity also follows from Zhao's Corollary 2.4 in the checked 2022 revision. [C-SA23-misc-023; Zhao2017, v2, printed p.7.]

If (u-1) is nilpotent, the finite polynomial family

\[
u^t=\sum_j\binom tj(u-1)^j
\]

is multiplicative for integers (t). Polynomial identity over a rational vector space extends this to formal (t), and differentiation at zero proves (D=\log u) is a derivation. Each of (D) and (u-1) is a polynomial without constant term in the other, so their image-generated ideals coincide. The preceding power identity then gives the order bound. Finite exponential conversely carries a nilpotent derivation to an algebra automorphism and preserves the exponent. [C-SA23-misc-023–024.]

Necessity fails on (A=\mathbb Q[\epsilon]/(\epsilon^2)), (u(\epsilon)=2\epsilon). This is a unital rational-algebra automorphism, with (J=(\epsilon)), exact differential order one, and (u-1) acting as identity on (\mathbb Q\epsilon). It is not unipotent. It also acts by 2 on (J/J^2), refuting the live associated-graded claim. Separately (D(\epsilon)=\epsilon) is a derivation whose image lies in the nilpotent ideal (I=(\epsilon)), but none of its positive powers vanishes on \(\epsilon\). A sufficient repair is filtration raising, for example (D(A)\subset I) and (D(I)\subset I^2), paired with automorphisms trivial on (\operatorname{gr}_I). [C-SA23-misc-022,025,029; MP-SA23-misc-04.]

The lower corollary reasserts the withdrawn equivalence, and both stages remain indexed. Likewise “every differential operator” is not silently restricted to automorphisms: on reduced (\mathbb Q[t]), (d/dt) has order one, contradicting the literal universal bound zero. The valid residual assertion is that, for nilpotent nilradical, an automorphism is differential exactly when it induces identity on reduction. Relative (K)-linearity follows from finite exp/log and is distinct from (A)-linearity. [C-SA23-misc-026–028; EGAIV4, Theorems 16.11.2 and 16.12.2; Stacks09CH, Example 10.133.5.]

## 3. Orientations, signs and determinants

The orientation leaves begin with two-element torsors and their contracted products. Enumerating four unary and sixteen binary maps agrees with the direct proof. These facts identify the equivalent formulations of a natural Stokes map. On scan 50, existence of a theory and existence of the unique normalized morphism between two theories are separately questioned; uniqueness alone proves neither. [C-SA23-misc-030–032; MP-SA23-misc-05–06.]

The model is \((\det V\setminus0)/\mathbb R_{>0}\). The dimension-zero normalization and ordered normal convention determine the Stokes maps. Its character is forced to be \(\operatorname{sign}\det\): the manuscript treats a parabolic subgroup, and shears plus diagonal matrices extend the argument to all \(GL_n(\mathbb R)\). Freed explicitly gives the determinant-sign torsor and exact-sequence construction; his quotient-before-subspace order is retained as a separate convention. [C-SA23-misc-032–033; Freed2013, Exercises 2.6 and 2.9, equations 2.7 and 2.11, pp.15–16.]

Exchanging dimensions (p,q) gives \((-1)^{pq}\). With the inward-normal-last convention supported by the sheet's basis calculation, taking a boundary in the first factor gives \((-1)^q\); in the second factor no extra sign occurs. Outward-normal-first differs in dimension (n) by \((-1)^n\), with normalized theory conversion \(t_n=(-1)^{n(n+1)/2}\). This supports the candidate exponent (q) without deciding its ink. The unfinished flag symbol \(I(\omega,\omega')\) has a plausible determinant completion, but its full target is absent and no unique intended formula is assigned. [C-SA23-misc-034–036; MP-SA23-misc-07; KnudsenMumford1976, pp.20–21.]

The final leaf states graded determinant axioms on finite free modules, not an existence/uniqueness theorem. Exterior powers supply a model. Natural rank-one normalization is stronger than objectwise identification: under the weak reading, \((\det V)^{\otimes3}\), placed in degree \(\operatorname{rank}V\), has the right symmetry but scalar character \(a\mapsto a^3\). Finite-projective extension must allow all invertible lines and locally constant degree. Complement independence is equivalent to trivial action of the block shear carrying one complement to another. The square's type and arrow problems remain reading alarms. [C-SA23-misc-037–038; SA23-336–341.]

Modern determinant-functor theorems impose additional coherence. Muro–Tonks–Witte's answer to a question from a 1973 Grothendieck letter is not evidence that these abbreviated axioms already imply that universal property. Earlier-run conditional (K_1)-character twists remain constructions under conditions, not an exhibited counterexample ring. [MuroTonksWitte2015, Definition 1.2.3 and introduction.]

The typed leaves at scans 51, 53 and 55 are distinct revised witnesses of XVIII, “Les épousailles (2)”, with “11” in the headings and visible page 82 on scan 53. One witness does not silently complete another, and 82 is not a date. The official catalogue tentatively associates this extract with Récoltes et Semailles or Réflexions mathématiques; this supports the uncertainty, not a settled work identity. [SA23-342–344; MontpellierCatalog, cote 68 footnote 58.]

## 4. Icosahedra and arithmetic angles

In oriented Euclidean dimension three, an ordered orthonormal pair determines a positive frame. Consequently (SO_3) acts simply transitively and (O_3) has a stabilizer of order two. The phrase “doublement transitive” cannot automatically be read as modern two-transitivity. For

\[
x_i=u\cos\alpha+(v\cos i\theta+w\sin i\theta)\sin\alpha,
\]

the equal-edge equation is \(\cos\alpha=\cos\theta/(1-\cos\theta)\). At \(\theta=\pi/3\) the triangle collapses; at \(\theta=\pi\) the triple is dependent. For \(\theta=2\pi/5\), \(\cos\alpha=1/\sqrt5\), and the twelve points \(\pm u,\pm x_i\) give the icosahedron. The literal latitude-circle description is wrong: the centre is \((\cos\alpha)u\), radius \(\sin\alpha\), while \(4\sin^2(\alpha/2)\) is a squared chord distance. [C-SA23-misc-040–043.]

The displayed matrix is checked exactly, including all three identities marked “à prouver”, the omitted distance comparison and the unfinished \(\gamma x_1\) calculation. Its images are

\[
(u,x_0,x_1,x_2,x_3,x_4)
\longmapsto(x_0,-x_2,-x_3,x_1,u,x_4).
\]

The neighbouring cap's summit is (x_0), not the literal (u). Enumeration gives twelve vertices, thirty edges, twenty faces, 120 graph automorphisms and sixty rotations. Central inversion immediately refutes identifying the full graph group with \(\Gamma'\). Dual incidence gives the same full group for the dodecahedral graph. The cyclic orders distinguish rotations from orientation reversal. The circle-bundle margin does specify its base, the sphere (S): quotienting each tangent-circle fibre by (C_5), via \([z]\mapsto z^5\), raises transition functions to their fifth powers. [C-SA23-misc-044–048; ED-SA23-misc-08–11,27; SimoesPereira2016 for the rotation group (A_5).]

The exploratory “60 degrees?” is false: \(\arccos(1/\sqrt5)\) is approximately 63.4349488 degrees. The conflicting half-angle and cosine trials remain distinct scratch calculations. The conditional group argument is correct: an order-three permutation commuting with a transitive fifteen-point action has five three-cycles, and a faithful action of a sixty-element group on these five cycles identifies it with (A_5). Faithfulness is essential; (C_{60}) acting through regular (C_{15}) refutes its omission. [C-SA23-misc-055–056; MP-SA23-misc-15–16.]

The cyclotomic computation is integral. In (A[T]/\Phi_5(T)), with 5 invertible, (t=T+T^{-1}) satisfies (t^2+t-1=0), with trace and norm (-1) and discriminant 5. Inversion fixes exactly the span of (1,T^2+T^3), equivalently (A[t]). For (f=c_0+c_1T+c_2T^2+c_3T^3), the constant coefficient of \(\beta(f)-f\) is (-c_1); this forces (c_1=0), even in characteristic two. The remaining equations give (c_2=c_3). No averaging by 2 is needed. Primitive fifth roots form a (C_4)-torsor over \(\mathbb Z[1/5]\), but a twist of \(\mu_n\) is not étale at primes dividing (n): \(\mu_p\) is nonreduced in characteristic (p). The undefined symbol for a proposed alternative construction blocks a stronger identification. [C-SA23-misc-049–052; MP-SA23-misc-13–14; Stacks03PK.]

The scheme-level assertions are only partly identified. Scan 22 proposes étale-local existence of icosahedra, local conjugacy under (SO(Q)), and finite étale (A_5) stabilizers, but does not specify the configuration, base and nondegeneracy hypotheses sufficiently. Its displayed base and later division by 5 also conflict. Ji checks good-prime specializations of explicit matrices, excluding 2 and 5 for his icosahedron normalization. Liedtke–Satriano's recent arithmetic results concern finite flat linearly reductive group schemes with excellent-Dedekind hypotheses and classify already fppf-locally conjugate subgroups using normalizer torsors. Neither proves the unrestricted configuration assertion. Their statement that \(\operatorname{Aut}(\mu_n)\) is constant étale must not be confused with \(\mu_n\) itself being étale. [C-SA23-misc-058–059; ED-SA23-misc-17; Ji2023, §3.1 Proposition 3.1; LiedtkeSatriano2025, Theorems 4.7, 5.2 and Proposition 7.1.]

Grothendieck's Esquisse §4, pp.21–25, directly connects arithmetic angle algebra and the regular-polyhedron programme, including bad characteristics. This is a checked topic link and a programme, not proof of an all-base theorem. An unsuccessful exact-match search does not promote an inadequately formulated sentence to a new open theorem.

## 5. Frames and topoi

The rectangle-generated frame discussion has one precise gap. Generation and separation give uniqueness and the finite-meet part of the proposed extension. Arbitrary-join preservation uses a cover-refinement assertion whose axiom (e) ends at an implication sign. Scan 14 is wholly cancelled; on scan 16 only the upper proof block is cancelled, while the finite-meet part remains live. Correct product-site constructions do not automatically establish the proposed rectangular-grid refinement or recover the missing axiom. [C-SA23-misc-053; MP-SA23-misc-12; Lafforgue2024, slides 47–48.]

The entire topos sheet, scan 23, is cancelled, but its principal questions have affirmative answers. For small (C) and a Grothendieck topos (E), \(E^{C^{op}}\) is a Grothendieck topos. Given (f:C\to C') and a geometric morphism (g:E\to E'), the inverse image is precomposition followed pointwise by (g^*), and its right adjoint is

\[
\pi(f,g)_*=g_*^{C'}\circ\operatorname{Ran}_{f^{op}}^E
\cong\operatorname{Ran}_{f^{op}}^{E'}\circ g_*^C.
\]

The equality uses preservation of limits by (g_*). For (E=\operatorname{Sh}(D,J)), sheaves on (C\times D) with trivial topology in (C) and (J)-covers in (D) are precisely (C)-presheaves of (J)-sheaves. The product-site theorem gives \(E^{C^{op}}\simeq\widehat C\times E\), including the groupoid and presheaf cases on the page. Lafforgue's slide 47 states the exact product-site theorem. No original SGA proposition number is invented where an inspected locator was not obtained. [C-SA23-misc-060–061; MP-SA23-misc-18–19.]

## 6. Graph embeddings and coset graphs

Cyclic dart orders determine an oriented regular neighbourhood of a finite tamely embedded graph, with discs for isolated vertices and annuli for isolated circles. A positive-valence vertex of degree (d) has ((d-1)!) cyclic orders. If \(\sigma\) cycles darts at vertices and \(\tau\) reverses them, the boundary components are the cycles of \(\sigma\tau\), up to composition convention. Euler characteristic gives

\[
b(\partial U)=b_1(X)+b_0(X)-2g(U).
\]

The queried (b_1+b_0) omits genus. An alternating rotation of a two-loop bouquet gives one boundary component and genus one; a planar rotation on the same graph gives three boundaries and genus zero. Both are explicitly calculated. Boundary cycles supply the requested combinatorial index and the planarity criterion. [C-SA23-misc-062–063,070; MP-SA23-misc-20–21; SageRibbonGraphs.]

The classification by ribbon neighbourhood and complementary boundary partitions, genera and punctures is the extended-combinatorial-map description, with finite-type, tameness and component-incidence hypotheses. Genus under gluing includes the cycle rank of the incidence graph. For connected (U,S), glued circles indexed by (J), and complement pieces indexed by \(\Lambda\),

\[
g(S)=g(U)+\sum_{\lambda\in\Lambda}g_\lambda+|J|-|\Lambda|.
\]

Two annuli glued along both circles form a torus; the incidence graph contributes the missing genus one. [C-SA23-misc-064–065; MP-SA23-misc-22; ColinMesmay2014, arXiv-version Lemma 5.]

Inside one oriented-homeomorphism orbit, mapping classes act transitively on embedding isotopy classes, yielding (G/H). The identification with all outer automorphisms is too broad: the oriented torus mapping class group is (SL_2(\mathbb Z)), whereas \(\operatorname{Out}(\mathbb Z^2)=GL_2(\mathbb Z)\). Punctures and boundary need peripheral conventions. For a connected graph surjecting on the fundamental group of a closed oriented aspherical surface, the stabilizer is trivial by homotopy-to-isotopy injectivity. The proposed disc-complement shorthand does not extend unchanged to punctured surfaces: the core circle of an open annulus is a counterexample. [C-SA23-misc-066–068; MP-SA23-misc-24; Epstein1966, Theorem 6.3, with its exact qualifications.]

The scan-30 stabilizer question has the strongest precise literature match. For a finite graph embedded in the interior of a compact oriented surface and an orientation-preserving homeomorphism (h), agreement of the maps on each component's fundamental group up to inner conjugacy gives homotopy of graph maps. The already given (h) supplies oriented congruence. Colin de Verdière and de Mesmay's arXiv-version Theorem 14 then gives ambient isotopy; the converse follows from homotopy invariance. Their full proof explicitly attributes the characterization to Ladegaillerie's 1984 article. The original article was not opened: the checked proof is the later independent one. [C-SA23-misc-069; MP-SA23-misc-23; ColinMesmay2014, arXiv Theorem 14, renumbered Theorem 4 in the author final version.]

The dates are separated: a 2012 conference precursor, arXiv circulation on 10 October 2013, online publication on 30 October 2013, and the journal issue in January 2014. Esquisse, written 1984 and published 1997, §3 pp.13–14, identifies the earlier 1974–76 work. Récoltes et Semailles, note 94, manuscript pp.399–401 in the opened HTML transcription, gives the author's account of a 1975 solution and 1976 thesis defence. This HTML is not collated to scans, and the author's judgments about publication delay are not adopted as independently established causes. [Esquisse1997; RecoltesNote94; Ladegaillerie1984, original marked unverified.]

Yagasaki provides the exact topological mechanism for the quotient question: local extension and principal restriction bundles for proper embeddings of compact PL polyhedra in surfaces. After imposing these hypotheses, the relevant homotopy sequence is

\[
\cdots\to\pi_1H\to\pi_1G\to\pi_1\operatorname{Emb}
\to\pi_0H\to\pi_0G\to\pi_0\operatorname{Emb}.
\]

The ambiguous middle degree must be \(\pi_1G\). Yagasaki's later component-homotopy classification is related but does not replace the graph-isotopy theorem or whole orbit calculation. [C-SA23-misc-071; MP-SA23-misc-25; Yagasaki2000, Theorem 1.1 and Corollary 1.1; Yagasaki2002.]

The final coset calculations are elementary but label-sensitive. Evaluation gives \(\operatorname{Hom}_G(G/H,E)=E^H\). General graph automorphisms form the subgroup of vertex/dart permutations satisfying compatibility; for independent isolated vertices and isolated circles the asserted product with a wreath product is correct. A transitive loop graph (A=G/H,S=G/H'), (H\subset H'), has reversal given by a nontrivial order-two coset in \((H'\cap N_G(H))/H\); faithfulness means the core of (H) is trivial. This entire block is cancelled, although the calculation is sound. [C-SA23-misc-054,072–073.]

For nonloops, let reversal be represented by (s\in N_G(H)), (s^2\in H). Then

\[
gH\longmapsto(gH',gsH')
\]

is injective exactly when (H'\cap sH's^{-1}=H), and nonloops require (s\notin H'). This proves the final questioned implication. The boxed stabilizer labels are reversed relative to the typed map and remain an ink alarm. The earlier free-standing normalizer-intersection equality is not valid in general: distinct order-two subgroups of (S_3) have trivial intersection, whose normalizer is all (S_3), but the intersection of their normalizers is trivial. The uncertain intended subgroups prevent a stronger special-case identification. [C-SA23-misc-057,074; MP-SA23-misc-26.]

## Register and completion

The tables contain 53 entry verdicts, 53 subject items (45 from indexed notes and eight additional Codex units), 74 claims, 23 authorial problems including answered and cancelled flags, four editorial tasks, and 58 reading alarms. Claim classes are 51 B, 20 C and 3 F: established mathematics; precisely restricted or refuted overstatements; and genuinely unidentifiable formulations. No class D is inferred merely from an unsuccessful search, and present familiarity alone does not establish chronological class E. Every claim has an actual query mapping and hypothesis assessment in `search_log.jsonl`; computations, mathematical arguments and limits are separated in `check_events.tsv` and `reference_checks.json`.

Hua's modernizations, the orientation finding, LM7_PUSH, EXIT_TOWER and FINMON remain in a separate project-lead table. Their named records and purported Lean status are not supplied and are not independently certified. The determinant functor symbol \(\Delta\) supplies no identification with a GT character of the same name. Ranked directions propose bounded follow-up work; none is developed into a new research programme in this consolidation.
