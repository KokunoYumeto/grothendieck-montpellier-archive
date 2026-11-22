# Main A candidate: arbitrary henselian fpqc descent

Run: RESEARCH_SA17_FINISH. Agent: descent_groups, GPT-6 Astra (inherited effort).
Date: 2026-11-19. This is a research record, not a proof of the remaining gate.

## Exact target and established reductions

Over F_p[t], P(R)=alpha_p(R^h_(t)). The B research branch has proved filtered-colimit compatibility, fppf descent, fpqc separatedness, arbitrary fpqc descent over complete noetherian local bases, and over noetherian G-ring bases. Its full record is notes/B_research.md and notes/B_finish_A_fpqc.md. Those restricted results do not imply arbitrary-base fpqc descent. The strengthened adic condition 4 is false for this candidate (root A_finish_adic, independently audited by B); this branch concerns only the main original local-complete condition.

After replacing a henselian base A and its faithfully flat cover B by t-henselizations, the remaining assertion is: if b in B has b^p=0 and

    (1+t*c)(b tensor 1 - 1 tensor b)=0,

for a finite tensor c in B tensor_A B, then b lies in A. The displayed condition is the actual henselization kernel criterion. Membership of the difference in every t^n(B tensor_A B) is weaker and must not replace it. The finite algebra A[b] is not known to be a pure submodule of B; tensoring its inclusion is not justified. Partial A-linear retractions on finitely many relations give identities z_(i+1)=b*z_i with z_0 a unit and z_p=0 but do not force b into A, because the resulting coefficient functionals remain independent. The complete-base Matlis retraction proof is stronger and does not extend automatically to arbitrary A.

## Positive henselian loops: a precise possible H1 reduction

Opened K. Cesnavicius, The affine Grassmannian as a presheaf quotient, arXiv:2401.04314v3, Proposition 3, printed pp.2-3. It proves the fpqc H0 equalizer for R{u}, with u an independent polynomial variable. The injectivity proof uses Raynaud--Gruson I3.2.6 over the coefficient ring, not purity over its polynomial ring. Thus it does not survive passage to u-t merely by citing purity.

For a faithfully flat A->B, let C_n=(B tensor_A ... tensor_A B){u}, with n+1 factors, and C_(-1)=A{u}. The element u-t is a nonzerodivisor in every C_n: multiplication by the monic polynomial u-t is injective before henselization, and henselization is flat. Quotienting C_n by u-t identifies it with the t-henselization of the corresponding tensor power (henselization commutes with this finite quotient base change). Therefore exactness of the positive-loop augmented Cech complex in degree 1, together with its known degree-0 exactness, would prove the desired degree-0 equalizer after specialization u=t. Explicitly, lift a degree-0 cocycle b after specialization to beta in C_0. Its differential is (u-t)gamma. Regularity implies d gamma=0. If gamma=d eta, then beta-(u-t)eta is a degree-0 cocycle before specialization and descends by Proposition 3.

For alpha_p, one may choose beta killed by p-th power. Etale base change commutes with Frobenius kernels: relative Frobenius for an etale algebra is an isomorphism, so alpha_p(B^h)=alpha_p(B) tensor_B B^h as B-modules. Write b as a finite sum of p-nilpotents from B times henselian coefficients and lift those coefficients to B{u}. The resulting lift beta is p-nilpotent. This observation alone has not produced the necessary H1 vanishing. In particular neither the positive-loop H0 theorem nor coefficient-ring purity is being presented as a solution.

## Exact primary-source boundaries

A.J. de Jong--N. Olander, On weakly etale morphisms, JPAA228 (2024),107532, original PDF https://pure.uva.nl/ws/files/230886016/On_weakly_tale_morphisms.pdf, Theorem2 and Lemma10, printed pp.4-5, were opened. Lemma10 proves the full module-valued henselized Cech complex is acyclic for a faithfully flat WEAKLY ETALE cover over a Z/N-algebra. Its proof uses the classical structure sheaf on the pro-etale site; the identification of pullback structure sheaves uses the weakly etale assumption. It has not been extended here to arbitrary flat covers. Example9 shows a characteristic-zero henselian Cech H1 obstruction even for a Zariski cover, so a characteristic-independent cohomological shortcut is unavailable.

S. Devadas, Henselian schemes in positive characteristic, arXiv:2212.08644, https://arxiv.org/pdf/2212.08644, was opened. Theorem3.2.6, printed p.21, states higher-cohomology vanishing for the henselized sheaf of a quasicoherent sheaf on Spec A in positive characteristic. Theorem3.2.8, printed p.22, algebraizes FINITELY PRESENTED quasicoherent sheaves on an affine Henselian scheme. It does not state an unqualified equivalence for all quasicoherent sheaves. Section5.2.11 on henselian-finite-presentation flat morphisms does not approximate arbitrary flat covers. No fpqc descent theorem for henselian schemes is being assumed from this paper.

## Independent audit of the root literal7 argument, 14:20 UTC

Let A be complete noetherian local. If t is invertible, P_A is terminal; if t is nilpotent, P_A is alpha_p. Otherwise t belongs to the maximal ideal and is not nilpotent. A finite local actually modular model must have residue field k(A), by the minimal-field clause. On all centered Artin local A-tests, P equals alpha_p. Pro-Yoneda for complete finite local algebras therefore identifies the proposed model, with its universal section, with A[x]/x^p and x.

Set R0=A[u]_(m_A,u), R=R0[epsilon]/epsilon^2. The simple-root Hensel property gives f in t*R0^h_(t) with f^p-f=t*u. Finite algebra base change identifies R^h with R0^h[epsilon]/epsilon^2, so epsilon*f belongs to P(R). The map R0->R0^h is injective since t lies in its Jacobson radical. If f belonged to R0, choose a minimal prime q of A avoiding t; reducing would give a rational root of X^p-X=t*u over Frac(A/q)(u). Its pole at infinity is simple, whereas any pole of g^p-g has order divisible by p. This is impossible. Thus epsilon*f is not in alpha_p(R), contradicting actual modularity of that sole possible model. Condition7 is vacuous in this case. This targeted check passes for every prime including2.

For the root condition8 argument, the finite-type test qualification remains essential. On an irreducible noetherian base, either t is nilpotent, or D(t) is dense and P is terminal there. The known necessity argument for a representable functor then applies on the relevant open for finite-type test schemes. It does not repair the separate arbitrary-test defect A:8-literal.

## Search status

Queries in this branch include henselization + faithfully flat + equalizer; henselian + fpqc descent + sheaf; henselisation + fpqc + counterexample; finitary fpqc checking noetherian bases; Henselian scheme quasicoherent cohomology. Both search engines were used. Only primary sources above were relied on; automatically generated course pages returned by search were discarded. No exact arbitrary-flat descent theorem or counterexample has yet been found. No novelty claim is made for an unresolved search.

## 14:24 UTC: independent full audit of the root H counterexample to L2

The root pivot uses H itself, not its henselized quotient. For every F_p[t]-algebra R put

    H(R)={x in R : x^p=0 and x in t*R*x}.

Equivalently there is a in R with (1-t*a)*x=0. This defines an additive subfunctor of alpha_p: if (1-ta)x=0 and (1-tb)y=0, then (1-ta)(1-tb) annihilates x+y, and equals 1-t(a+b-tab); scalar multiples are immediate. The argument works for p=2.

Conditions1 and2 hold for arbitrary rings and arbitrary faithfully flat covers. A compatible cover-point descends to x in alpha_p(R) by ordinary affine fpqc descent. Put M=R*x, considered as a submodule of R. Flatness identifies M tensor_R R' with R'*x inside R'. The condition upstairs says the image of x in (M/tM) tensor_R R' vanishes. Faithful flatness implies its image in M/tM vanishes, so x lies in tM. This proves the full fpqc equalizer, not only noetherian or finitely presented flat descent. Zariski locality follows either from that result or from local ideal membership. The affine sheaf therefore extends in the usual way to all S-schemes.

Condition3 holds: a section is described by the two finite equations x^p=0 and x=t*a*x for the unknowns x,a. Both an element and one witness a descend to a stage in a filtered ring colimit, and both equations hold after enlarging the stage. Equality of two sections is equality of their x coordinates and also descends. No sheafification is needed.

The strengthened condition4 holds. Let A be noetherian, complete and separated for an ideal I, and let x_n in H(A/I^n) be compatible. Completeness gives x in A, and separatedness gives x^p=0. Lift a witness a_n for x_n to A. Then x-t*a_n*x belongs to I^n, so

    x belongs to (t*x)+I^n for every n.

The ideal I is in the Jacobson radical of A, since each 1-i has its convergent geometric-series inverse. The finite A-module A/(t*x) is therefore I-adically separated by the Krull intersection theorem. Hence x belongs to (t*x), as required. Injectivity is the separatedness of A. Equivalently, for every noetherian pair (A,I), the canonical map H(Ahat)->lim_n H(A/I^n) is bijective. The proof does not require compatibility of the witnesses a_n and does not require the principal ideal (t*x) to be flat.

Condition5 holds in its universal form. For an Artinian local A over F_p[t], t is either a unit or nilpotent. If t is a unit, H_A equals alpha_p on ALL A-algebras. If t is nilpotent, 1-t*a is a unit on every A-algebra for every a, so H_A is terminal. Thus the respective finite local A-models are A[X]/X^p and A. Translating by a chosen alpha_p section gives the same finite prorepresenting model for deformations based at any Artinian section, not just the zero field-valued point. For a nonlocal Artinian A the finite product decomposition applies. This is stronger than a check on tangent spaces or on residue fields alone.

Condition6 holds because a valuation ring is reduced, so alpha_p, and therefore H, has exactly the zero section on it. The assertion survives every base change in the axiom.

Condition8 holds under the finite-type test convention already isolated in A:8-literal. On an irreducible noetherian S', either t vanishes on its reduction and is globally nilpotent (by quasi-compactness/noetherianity), in which case H_{S'} is terminal, or D(t) is a nonempty dense open containing the generic point and H on that open is alpha_p. In each case the necessity argument for a finite represented functor gives an open modularity neighborhood of the stated generic modular point. No assertion is made for the known defective arbitrary-test version of8.

Condition7 fails explicitly. Take A=F_p[[t]], B=A, xi=0. Relative to A, every local test whose closed point maps to the closed point of Spec A has t in its maximal ideal. Thus every 1-t*a is a unit, H is terminal on that centered test category, and (Spec A,0) is actually locally modular at the closed point. Its residue field F_p is the unique minimal field of definition. This use of F_A agrees with the explicit formulation on scan2; it is not a claim of modularity of Spec A relative to Spec F_p[t] before base change. At the generic point K=F_p((t)), H_K=alpha_p. The element epsilon in K[epsilon]/epsilon^2 is nonzero, has p-th power zero, and is in H because t is invertible. It cannot be the pullback of the zero section of Spec K. Therefore the generic localization of (Spec A,0) is not modular. All primes p are included.

Conclusion of this targeted audit: the root's H functor satisfies1-6, with the strengthened noetherian adic4, and the intended finite-type8, while failing actual7. It refutes L2 under the same explicit convention for8 used throughout the corrected representability programme. It does not refute the main A1 theorem, which includes7. No finite experiment could replace the universal descent and noetherian-closure proofs, so no finite certificate is claimed for this infinite example.

### Terminological/novelty lead

H may be viewed as the subgroup of alpha_p sections vanishing on a neighborhood of V(t), or an extension-by-zero construction from D(t). This may locate older instances of the counterexample. Initial searches for extension-by-zero + alpha_p, representability + fppf, and Murre condition F7 returned no exact primary match. This is only an ongoing literature search, not a priority assertion.

### Exact source for the L2 adic-closure step

Opened Stacks Lemma10.51.5, Tag00IQ, https://stacks.math.columbia.edu/tag/00IQ. Part(2) states that the I-adic intersection in any finite module over a noetherian ring is zero when I is in the Jacobson radical. This is the nonlocal version actually used on A/(t*x); citing only the local Krull-intersection lemma would leave that hypothesis implicit.

### Failed interior-equivalence-relation route for main P

For b nilpotent, the closed relation R_b defined by b tensor1=1tensorb has the same underlying space as the full pair groupoid. The henselian annihilator condition gives an open neighborhood of all V(t) on which it equals the pair groupoid. It also contains an open neighborhood of the diagonal, since 1+t*mu(c) is a unit in B. Diagonal-neighborhood alone is insufficient: for A=k[epsilon]/epsilon^2, B=A times A and b=(0,epsilon), R_b equals the pair groupoid on the diagonal components but has nonflat off-diagonal components. Trying to take the interior and prove it is an open equivalence relation used openness of composition; arbitrary flat morphisms need not be open. Thus that proof is invalid for arbitrary fpqc covers. Even if the interior relation were constructed, representability of its quotient as a weakly etale scheme/space would still have to be proved before applying de Jong--Olander Theorem1. No such result is claimed.

### Waterhouse bounded-sheafification theorem checked

Opened William C. Waterhouse, Basically bounded functors and flat sheaves, Pacific J.Math.57(1975),597-610, https://msp.org/pjm/1975/57-2/pjm-v57-n2-p35-s.pdf, Lemma3.1, Theorems3.2-3.3 and5.1, Corollary5.3. The approximation of a faithfully flat cover uses a countable Skolem--Loewenheim iteration to enlarge small subalgebras until all finite linear relations have the required solutions. Small means cardinality bounded by a chosen infinite cardinal, not finitely generated or finitely presented. Corollary5.3 guarantees existence and the same cardinal bound for fpqc sheafification. Applied to alpha_p/H it controls set-theoretic size, but it does not prove preservation of ordinary filtered ring colimits. For a countable base it may require countably generated, nonnoetherian approximation rings. The theorem is not being used as a finitary-sheafification assertion.

## 14:58 UTC: repair of the interior relation, and the remaining effectivity gate

The root supplied a valid replacement for the invalid flat-openness step above. If a flat morphism X->T factors through a closed subscheme R defined by a finitely generated ideal I, then its image is contained in the interior of R. At an image point t with preimage x, the local flat map O_(T,t)->O_(X,x) is faithfully flat; since I maps to zero, I_t=0. Finite generation gives an open neighborhood of t on which I vanishes. This argument does not assert that arbitrary flat maps are open.

Apply this lemma to the closed equality relation R_b inside Spec(B tensor_A B), defined by the single element b tensor1-1tensorb, and let O be its interior. It contains the diagonal because the annihilator 1+t*c restricts to the unit 1+t*mu(c) in the t-henselian ring B. It contains all of V(t), since 1+t*c is invertible there. Symmetry holds by its definition. On O_12 intersect O_23 inside Spec(B tensor_A B tensor_A B), transitivity of equality gives a map to R_b under pr_13. This map to Spec(B tensor_A B) is flat, being a restriction of a flat projection. The preceding lemma therefore shows that it factors through O. Consequently O really is an open equivalence relation for arbitrary faithfully flat A->B.

This repairs construction of the equivalence relation; it does not prove representability of Spec B/O. If its quotient were a weakly etale scheme (or a space to which the same henselian lifting theorem applies) over A, its closed t-fibre would be Spec(A/t), and de Jong--Olander Theorem1 would supply the unique section lifting that closed-fibre section. Uniqueness after the henselian base change B would identify the original quotient map with that section, and b, which is invariant on O, would descend to A. The outstanding gate is thus an exact quotient/effectivity statement, not transitivity. The standard quotient theorem for a flat groupoid locally of finite presentation cannot be invoked for arbitrary B/A.

An open diagonal does not force finite presentation: for a multiplicative set S, B=A times S^(-1)A is faithfully flat with open diagonal, while its second factor need not be locally of finite presentation. The quotient by its diagonal is nevertheless a weakly etale scheme. This example shows why an argument that labels the desired quotient etale without a finiteness proof is invalid.

### Reduced noetherian base lemma

There is a direct restricted consequence. Let k be a field, let B be a k-algebra, and let b be nilpotent in B. If the equality relation R_b contains an open neighborhood of the diagonal, then b=0. For a prime q of B choose a geometric point with algebraically closed residue extension K. Base changing the second factor of B tensor_k B along B->K sends b to zero. The resulting map B->B tensor_k K is flat, and the point induced by the same geometric point in both factors lies over the diagonal, where b vanishes on a neighborhood. The induced local ring map at that point is faithfully flat, so b vanishes in B_q. This holds for all q.

Now let A be reduced noetherian, A->B flat, and b nilpotent with the same diagonal-neighborhood condition. There is an injection A->product_q k(q), where q ranges over the finitely many minimal primes. Tensoring with the flat module B preserves it. In each B tensor_A k(q), the field lemma kills b. Thus b=0 in B. In particular nilpotent descent data of the present type vanish over any reduced noetherian base, without a G-ring assumption. This partial result does not handle nonreduced bases or prove arbitrary-ring fpqc descent.

### Exact source boundaries for quotients

Opened SGA3 ExposeIV section6, https://grothendiecksga.com/read/sga3/fr/IV-6.html. Corollary6.4.3 concerns equality of canonical and fpqc quotients and describes sections by invariant subschemes; it does not by itself assert representability of an arbitrary open-relation quotient. Opened https://www.numdam.org/item/10.24033/bsmf.1732.pdf: its correct author/title are Daniel Ferrand, Monomorphismes et morphismes absolument plats, Bull.SMF100(1972),97-128. Its local weakly-etale rigidity results assume noetherian base; they are not an arbitrary-base quotient theorem.

### 15:12 UTC: the reduced-base lemma extends to arbitrary reduced rings

The noetherian hypothesis in the preceding reduced-base lemma can be removed. For reduced A, inject A into A'=product_q k(q), over all minimal primes; A' is absolutely flat. Tensoring with the flat A-module B gives an injection B->B'=B tensor_A A'. For each prime p of A', the localization A'_p is a field. The diagonal-neighborhood hypothesis survives base change to A'_p, and the field lemma gives b=0 in B' tensor_(A') A'_p. As this holds at every prime p, b=0 in B'. Hence b=0 in B. This avoids the invalid identification of tensor product with an infinite product. The absolutely-flat intermediate ring, not finiteness of the set of minimal primes, is the reason the argument works.

It follows that over an arbitrary (possibly nonreduced) base A, such a nilpotent b belongs to Nil(A)*B: apply the reduced-base lemma to A_red -> B tensor_A A_red, which is flat. Consequently b is a finite linear combination of nilpotent elements from A with coefficients in B, and those finitely many base nilpotents generate a nilpotent ideal. This is a useful nilpotent-devissage reduction, but does not by itself descend those coefficients or their annihilator relation.

### Source discipline correction

The grothendiecksga.com IV.6 page cited above is a secondary transcription/translation pointer and is not being used as an opened primary SGA3 source. The primary French text has now been opened at the editor's IMJ archive: https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp4-13oct24.pdf (ExposeIV, edited original text, version13Oct2024). The exact Corollary6.4.3 will be checked there. Its quasi-compactness hypothesis on R->X is an additional unresolved issue for the full interior O, which need not itself be quasi-compact.

### Accessible versus finitary sheafification: 2026 primary check

Opened and read the complete two-page paper Ko Aoki--Robert Burklund, Inaccessibility of the flat topology, arXiv:2607.09440v1 (10July2026), https://arxiv.org/abs/2607.09440, direct original PDF saved as sources/Aoki_Burklund_2026_flat_topology.pdf. Remark7 explicitly recalls that Waterhouse preserves accessibility via aleph_1-filtered approximation by countable rings. It does not assert preservation of ordinary filtered colimits. Theorem6 constructs, for every regular cardinal kappa, a kappa-filtered family of maps admitting faithfully flat refinements whose colimit admits no such refinement. It distinguishes such covering maps from faithfully flat maps themselves, which are stable under filtered colimits. Neither statement settles the special quotient alpha_p/H or main P.

### Open quotient atlas: precise additional representability step

The B agent observed that X=Spec B -> Q=X/O has scheme-representable pullbacks, even before Q itself is represented. Over T->Q choose an fpqc cover T'->T on which the section lifts to X. Then X times_Q T' is an open subscheme of X times_A T', obtained by pulling back O. Ordinary quasi-affine descent is not quite sufficient: Stacks uses quasi-compactness in the definition of quasi-affine. The precise theorem is Gabber's effective descent for ind-quasi-affine morphisms, Stacks Lemma40.15.3, Tag0APG, https://stacks.math.columbia.edu/tag/0APG, opened in full. Every quasi-compact open of an open subscheme of an affine is quasi-affine, so this theorem applies without requiring O->X quasi-compact. It gives a scheme representing X times_Q T. The relative diagonal of Q over A is likewise represented by open immersions, by fpqc descent of open immersions.

This remains short of representability of Q itself. Opened Stacks Section110.56, Tag078E, https://stacks.math.columbia.edu/tag/078E: the infinite product of projective lines is an fpqc sheaf with representable diagonal and a flat, surjective, universally open, affine atlas, but is not an algebraic space. Its diagonal is closed rather than open, so it does not refute the special open-diagonal criterion needed here. No general fpqc-atlas-to-algebraic-space implication is being used.

The SGA3 primary boundary check is complete: ExposeIV, Corollary6.4.3, editor's IMJ PDF p68, printed p245 (original marginal pages248-249), explicitly assumes R->X faithfully flat and quasi-compact, then identifies the fpqc and canonical quotient and describes its sections by stable open/closed subschemes. It asserts no general representability of that quotient. The secondary transcription is not relied on.


## 15:32 UTC: numbered partial propositions persisted

Created sections/A_finish_fpqc.tex with A:fpqc-schematic-interior, A:fpqc-open-relation, A:fpqc-reduced-base, and A:fpqc-nilpotent-base-reduction. Added result and check rows to the owned A45_D tables. The schematic open interior is explicitly the locus where the ideal sheaf vanishes, not topological interior: the latter distinction is essential because delta b is nilpotent. All proofs are complete; arbitrary fpqc descent remains expressly unresolved. The product-of-fields reduction is reproved in the text and its primary Stacks 092A source is added to references/A45_D.bib.


## 15:35 UTC: infinitely t-divisible square-zero test is positive

For A=A0 semidirect K epsilon, with A0 a complete DVR, K=A0[1/t], and epsilon squared zero, let B be flat faithfully flat and t-henselian over A, and put B0=B/(K epsilon)B. Flatness identifies the square-zero ideal in B with K tensor_A0 B0=B0[1/t] epsilon, and B0 is flat faithfully flat and t-henselian over A0. The reduced-base proposition puts every relevant nilpotent b in that ideal. Write b=epsilon u with u in B0[1/t]. The annihilator relation becomes (1+t c0) delta(u)=0 in C0[1/t], C0=B0 tensor_A0 B0. Choose n with v=t^n u in B0. Flatness over the DVR makes C0 t-torsion-free, hence (1+t c0) delta(v)=0 in C0 itself. Encoding v by epsilon v over the complete Noetherian base A0[epsilon]/epsilon^2 and using the established complete-base fpqc result yields v in A0, hence u in K and b in A. Parent independently targeted-checked this argument and confirmed the complete-base result applies.

More generally, the same complete-base result implies the module-valued equalizer criterion for every A0-module M: for a finite M use the complete Noetherian square-zero ring A0 semidirect M and B0 semidirect (M tensor B0); for general M choose a finite submodule containing the finitely many coefficients of z. Flatness of B0 and C0 preserves its inclusion and the annihilator relation. Thus z in M tensor B0 with (1+t c)delta z=0 comes from M. This deals with arbitrary square-zero extensions of a complete Noetherian A0 even if the extension does not split: first descend modulo the square-zero ideal, subtract any lift, and use the module criterion for the remaining element. Finite nilpotent thickenings can be handled by the same finite filtration of both base ideals and coefficient modules. No reduction from an arbitrary ring to these bases has been found.

The quotient route remains open. Search refinements: Delta(Q) is open, so locally of finite presentation, a stronger hypothesis than the nonalgebraic infinite-product example Stacks078E. Nevertheless this cannot force Q/S locally of finite presentation: S disjoint union Spec(A_p) is a flat surjective scheme with open relative diagonal, while A_p may require infinitely many inverted elements. The appropriate hoped-for conclusion is representability by a weakly etale scheme or algebraic space, not an etale morphism.


## 15:53 UTC: arbitrary fpqc gate closed; full independent audit

Read the complete newly written sections/A_finish_fpqc_solution.tex and independently checked all six numbered statements. The finite module capture plus strict-local indecomposable preservation closes the former arbitrary-base gate. All six targeted checks are persisted separately in checks_A_solution_audit.tsv; parent and author informed. The endomorphism-ring proof does not assume End is finitely generated over A. The Jacobson-kernel and minimal-generator polynomial idempotent-lifting proof makes the non-Noetherian case valid. Primary Stacks0752 (Proposition11.8.5) was opened in full for the central division algebra splitting assertion, including the imperfect separably closed residue-field case. The written global proof uses spreading from strict henselizations into pointed finite-presentation etale neighborhoods, which cover the original base, and relies only on already-proved fpqc separatedness for their overlap comparison.

Earlier statements in this log recording the gate as unresolved are historical and are superseded by A:hensel-fpqc. The open-relation quotient approach remains unused; no representability theorem for that quotient was needed.
