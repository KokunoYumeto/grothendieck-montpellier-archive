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
