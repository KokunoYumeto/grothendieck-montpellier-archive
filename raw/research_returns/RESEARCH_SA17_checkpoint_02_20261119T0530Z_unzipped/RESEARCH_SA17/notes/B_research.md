# Part B research notebook

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), run RESEARCH_SA17-20261119, agent bt_crystals. This is a working record, not a claim that every requested item is settled.

## Sources opened in this run

- The supplied cote 129 transcription, scans 93-94 and 113-115, plus corresponding doubts and study. Original PDF fetched from https://grothendieck.umontpellier.fr/129.pdf; scans 94, 114, 115 rendered and visually inspected in this run. Scan 94 explicitly uses M, not Delta, in the tensor formula; scan115 explicitly says up to isogeny.
- E. Lau, *Divided Dieudonné crystals*, arXiv:1811.09439v2 (12 July 2026), PDF and LaTeX source. Read Introduction, §§3-4, §§7,9,11. Exact relevant locators: Lemmas 3.2-3.3, Remark 3.4, Theorems 7.6,7.9,9.3, Corollary 9.5, Proposition 11.3.
- Anschütz–Le Bras, *Prismatic Dieudonné Theory*, arXiv:1907.10525, PDF and LaTeX source; Cambridge published HTML. Relevant locators: Theorems 4.44,4.65,4.74; Remark 1.19; §5.2. Classical crystalline vs prismatic categories must be compared with their admissibility condition retained.
- de Jong, *Crystalline Dieudonné module theory via formal and rigid geometry*, IHÉS 82 (1995), PDF. Lemma 2.4.4 proves effectivity of compatible BT systems on an affine formal scheme. Its proof is by finite projective coordinate algebras and applies to the p-complete affine case needed here.
- de Jong–Messing, *Crystalline Dieudonné theory over excellent schemes*, BSMF 127 (1999), PDF. Theorems 2.1,3.1,4.6 and Lemma 4.7.
- Lau, *Relations between crystalline Dieudonné theory and Dieudonné displays*, arXiv:1006.2720, PDF. Lemmas 3.2-3.4 on nilpotent rigidity; note the displayed statement of Lemma 3.4 says “kernel” where its proof/use requires “cokernel”. The needed square-zero case is re-proved in the paper.
- Lau, *Frames and finite group schemes over complete regular local rings*, arXiv:0908.4588, PDF. §10, particularly Proposition 10.4 and Theorem 10.3, permits non-nilpotent divided powers for nilpotent displays.
- Zink, *The display of a formal p-divisible group*, author PDF. Theorem 3, Corollary 48, Theorem 94 and Corollary 97; the latter removes the nilpotence-of-divided-powers restriction for connected groups.
- Stacks Project, Tag 07LI, Example 60.22.1, and its reference to Proposition 60.21.3: explicit p-torsion horizontal scalar in the crystalline PD envelope. Its displayed finite witness needs a correction at p=2 (see below).
- Kothari–Mundinger, *Cartier–Dieudonné Theory of Connected Group Schemes*, arXiv:2609.30586 (September 2026), PDF, Theorem A and Proposition 4.1.1. Used to check the modern derived-co-Lie comparison, not as a substitute for the manuscript's object.
- Mondal, *Dieudonné theory via classifying stacks and prismatic F-gauges*, arXiv:2405.12967, PDF; §§3.3–3.5 inspected.
- Gardner–Madapusi, *An algebraicity conjecture of Drinfeld and the moduli of p-divisible groups*, arXiv:2412.10226, PDF; Introduction and §8.8 inspected for general/non-nilpotent deformation claims.

## Working conclusions and exact gates

### B.1 / L5

The canonical PD on pA is well-defined even with p-torsion: all coefficients p^n/n! are p-integral and divisible by p, so replacing a by a+c with pc=0 changes gamma_n(pa) by zero. For odd p, weighted PD powers of pA vanish modulo p^N in weight at least 2N. For p=2, those of 4A vanish in weight at least N. These bounds prove the asserted reduction once Grothendieck–Messing and affine effectivity are applied with explicit comparisons.

For every p-complete separated ring A, the up-to-isogeny functor in Nice V is fully faithful. At p=2 one first lifts a power-of-2 multiple of a mod-2 morphism to A/4; after clearing finite matrix denominators, nilpotent PD on 4A then lifts it to all A/2^N. Uniform first-step exponent is obtained from the square-zero rigidity argument, not assumed from pointwise lifting.

Integral full faithfulness on the whole BT category should hold exactly when p is odd or 2A=0. For necessity at p=2, use the Kummer ordinary BT extensions G_1 and G_{-1}, base-changed from Z_2. They have the same mod-2 reduction and Hodge line. Any lift of the canonical identity modulo 2 would produce r=1+2b with r²=-1; then 2(1+2b+2b²)=0 and the second factor is a unit, forcing 2=0. The equality of integral Hodge lines is proved over Z_2 using the isogeny with identity on the multiplicative part and multiplication by 2 on the étale part, then base-changed.

Gate: finish written proof with explicit Kummer group laws and source-locator checks; derive the DVR statement from the comparison in §5.2 of Anschütz–Le Bras.

### B.2

Both alternative group hypotheses in Nice IV are expected to be valid on arbitrary nilpotent PD thickenings (with p locally nilpotent), without PD-nilpotence: connected fibres by nilpotent displays, no multiplicative part by Cartier duality. Exact comparison is Zink Corollary 97 together with Lau's general equivalence for infinitesimal BT groups. Gate: explicitly type the display-frame factorisation and Hodge lifting equivalence, and verify the same crystal is meant on the full PD site.

### B.3

The general conjecture is false. On R=F_p[x,y]/(x,y)^2, use tau=gamma_p(x²)gamma_p(y²)-gamma_p(xy)^2. It is nonzero, killed by p, horizontal, and Frobenius kills it. Multiplication by tau is an extra morphism D(mu_{p-infinity}) -> D(Q_p/Z_p), whereas the corresponding group Hom(Q_p/Z_p,mu_{p-infinity}) is zero.

A reduced finite-type version is R=F_p[a,b,c,d]/(ac,ad,bc,bd), with tau=gamma_p(ac)gamma_p(bd)-gamma_p(ad)gamma_p(bc). Its derivatives vanish by the PD identities, and the substitution (a,c,b,d)=(x,x,y,y) detects nonzero tau in the first example. The ideal is (a,b) intersect (c,d), so R is reduced. Adding infinitely many independent variables and using the retraction gives a reduced nonnoetherian example.

Correction to the Stacks finite witness at p=2: for B=F_2[x,y,u,v]/(x³,x²y,xy²,y³,xu,yu,xv,yv,u²,v²), the divided square is delta_2(ax²+bxy+cy²+du+ev+fuv)=a²u+c²v+de uv. The source formula omits de uv. The omitted term is necessary at u+v. The full finite PD structure and all nontrivial axioms are exhaustively checked by code/B_finite_certificates.py.

Positive classes include characteristic-p quasisyntomic rings, bases locally admitting a p-basis, and the exact classes stated by Lau for ordinary/filtered/divided crystals. A literal “largest class” of all possible bases is not established by these results. Gate: precise essential-image description and treatment of whether that demand is an unproved global classification.

### B.4 / L6

L6 conflates two different objects. The manuscript's proposed Delta fits the triangle ell_G[-1] -> Delta(G) -> ell_{G^D}^vee. A candidate functorial construction is, locally, [H¹_dR(B/S) -> H¹_dR(A/S)] in cohomological degrees 0,1 for an abelian resolution 0->G->A->B->0. Raynaud's embedding theorem gives such resolutions on every base, Zariski locally. Product embeddings give quasi-isomorphisms, with quotient the identity complex on the auxiliary abelian scheme; parallel extensions differ by a chain homotopy. This should provide a global canonical perfect complex and the triangle from Hodge exact sequences.

Over a perfect field, Delta(G) is (M tensor^L_W k)[-1], while the co-Lie formula uses M itself: ell_G=(D/F D) tensor^L_D M. In particular, literal L6 with Delta in place of M is false already for alpha_p or mu_p; it gives dimensions 1,2,1 instead of 1,1. Correct side: D/F D is a right D-module; D/D F is generally a left quotient and cannot be substituted without a variance convention.

Gate: finish the canonical gluing proof and establish the precise perfect-field shifts on original scan 94; test all three order-p examples. No general-base D/DF tensor formula will be asserted without defining the ring sheaf and module actions.


## 04:40 UTC written checkpoint state

Sections B.1--B.4 now have complete candidate proofs in `sections/B.tex`; bibliography, result rows and check rows are written. These are targeted checks by this agent, not independent re-proofs. The finite certificate was executed successfully, with the scope recorded honestly.

Correction to preliminary B.4 notation: for the classical module M=Hom(G,CW), the crystalline module is P=sigma^*M. Opened ALB Proposition4.51 and Mondal Theorem3.8 explicitly confirm this. Thus Delta=(sigma^*M tensor^L_W k)[-1], and ell=(D/F D)tensor^L_D M. The twist disappears over F_p.

B.2 is fully verified by Lau Smoothness Remark2.6 itself; the display-frame argument is not an outstanding gate.

Remaining requested B.1 gate: a separate derivation for mixed-characteristic DVRs directly through classification theorems, with perfect-residue-field scope explicitly distinguished. The all-A theorem already proves the answer for arbitrary complete DVRs, but the requested alternative derivation still needs writing.

Remaining B.3 scope gate: the exact meaning and maximality of the largest class proved in literature. The written theorem gives quasisyntomic, local-p-basis, excellent lci, and reduced F-finite F-nilpotent PD-torsion-free positive classes with exact essential images where an equivalence is available. No theorem claiming that their union is a maximal set of all characteristic-p bases has been found. General unrestricted full faithfulness is refuted in each requested base kind, including reduced and nonnoetherian bases. Need not confuse this refutation with a maximality classification.

B.4 construction now uses abelian resolutions, natural co-Lie triangles, product refinements and a coherent Cech totalization. The local construction works on every base, not just p-nilpotent bases. Further targeted check should focus on descent coherence and normalization, not assume them from the original conjecture.

## Independent A.1 bridge attack, begun 04:46 UTC

Root requested that after the B checkpoint this agent attack the promotion of a finite pro-modular model over a complete local base to an actually locally modular model. For C local with A→C local, 1–4 and Artinian pro-modularity give injectivity of local B-maps into F(C), first for Noetherian C by completion and then by filtered approximation. For field-valued points over other primes, finiteness of B/A and valuative uniqueness also give injectivity: choose a valuation ring of the field centered at the closed point of A, use integrality to put both B-images inside it, then apply the centered local injectivity. This does not settle generic nilpotent collapse or descent on C-completion tensor C-completion.

### Henselized alpha_p candidate (not yet a counterexample)

Independently of root, I reached the candidate P(R)=alpha_p(R^h_(t)), for S=Spec F_p[t]. It is the étale sheafification of the Zariski-germ quotient alpha_p/H, with

    H(R)={x in R : x^p=0 and (1-ta)x=0 for some a in R}.

H itself is an fpqc sheaf: x belongs to tRx if and only if it does after faithfully flat scalar extension, because membership is vanishing in the quotient R-module Rx/tRx. H preserves filtered colimits, since it is expressed by two equations and one existential variable. On a local ring H is zero when t is in the maximal ideal, and is alpha_p when t is a unit. For the henselization map R→R^h_(t), its kernel equals the kernel of R→R[(1+tR)^(-1)]: this follows because the second map to the henselization is faithfully flat (t is in the Jacobson radical of the localization and its reduction modulo t is unchanged).

The plain Zariski-germ quotient is not an fpqc sheaf. For example, let R=F_2[t]_(t)[epsilon]/epsilon^2, let z^2-z=t and take the local étale branch z=0 over t=0. Its map R→B is faithfully flat. In B⊗_R B the off-diagonal branch has t invertible near the chosen pair of closed branches, so epsilon*z satisfies the germ cocycle, yet is not in R. Henselization corrects this particular failure.

Opened de Jong–Olander, *On weakly étale morphisms*, JPAA228 (2024),107532, Theorem2, full PDF https://pure.uva.nl/ws/files/230886016/On_weakly_tale_morphisms.pdf. It proves henselian descent only for faithfully flat **weakly étale** maps. It explicitly distinguishes the two possible henselized tensor products. Thus it proves pro-étale descent for P, not arbitrary fpqc descent.

### Proved auxiliary result: henselian descent over complete Noetherian local bases

Let (A,m) be complete Noetherian local, t∈m, and A→B faithfully flat. Write B^h for henselization along t. Then

    A → B^h ⇉ (B⊗_A B)^h

is an equalizer of rings. Consequently the corresponding equalizer holds for alpha_p-valued points.

Proof. A is t-adically complete and separated: a t-adic Cauchy sequence is m-adic Cauchy, its m-adic limit satisfies each congruence because all ideals t^nA are m-adically closed. B^h is flat over A and its image contains V(t), hence it is faithfully flat because every maximal ideal of A contains t. By the universal property, henselizing B^h⊗_A B^h along t gives (B⊗_A B)^h. If b∈B^h equalizes, its two images modulo t^n agree for each n; faithfully flat descent modulo t^n gives compatible a_n∈A/t^n. Let a∈A be their limit and d=b-a. Then d∈∩_n t^n B^h. The kernel description of henselization supplies a finite tensor c=Σu_i⊗v_i such that

    (1+t c)(d⊗1−1⊗d)=0.

There is an A-linear retraction λ:B^h→A. To prove this without an unsupported compactness assertion, let E be an injective hull of A/m. Faithful flatness makes E→B^h⊗_A E injective; injectivity of E supplies a retraction r to E. Then b↦(e↦r(b⊗e)) maps B^h to End_A(E)=A, and sends 1 to 1. The equality End_A(E)=A is the opened Stacks Lemma47.7.5, Tag08Z6 (Matlis), whose proof computes End(E)=lim A/m^n.

Apply λ⊗1 to the displayed tensor identity. Every λ(u_i d) and λ(d) is zero, because d is in all t^nB^h and A is t-adically separated. The result is

    d (1+t Σ λ(u_i)v_i)=0.

The second factor is a unit in B^h, since t lies in its Jacobson radical. Thus d=0 and b=a. Injectivity follows from faithful flatness. This proves the auxiliary result for arbitrary B, including non-Noetherian B.

Exact remaining candidate gates: arbitrary-base fpqc descent for P, and preservation of filtered colimits after possible fpqc sheafification. No counterexample to A.1 is asserted. One cannot replace arbitrary flat covers by filtered systems of finitely presented flat covers: opened Stacks Lemma110.78.1, Tag0ATF, explicitly gives counterexamples to that approximation, even over a finite-type F_p-algebra.

The candidate also appears unsuitable for strengthened adic condition4 in L2. For C=F_p[t][[s]][epsilon]/epsilon^2, I=(s), the inverse limit of the henselizations of C/I^n allows coefficients in unbounded independent Artin–Schreier extensions in the t-henselization; a fixed element of C^h_(t) is algebraic over C. A complete independence proof has not yet been written, so this remains a diagnostic, not a claimed refutation of adic effectivity.

## DVR classification gate closed

Proposition B:DVR-classification is now written. Kisin, *Crystalline representations and F-crystals*, original author DVI at https://www.math.harvard.edu/~kisin/dvifiles/wam.dvi, was downloaded and converted to PDF, then its text read. Appendix (A.2) defines the filtered crystalline evaluation; (A.5) defines its category; Proposition (A.6), author-preprint pp.31–33, is the odd-prime integral equivalence and the all-prime isogeny equivalence. The manuscript's Hodge-preserving morphism respects the classifying filtration by its preimage definition, and commutes with divided Frobenius because S is p-torsion free. Equality of its reduction with the prescribed map follows via S→W(k), classical perfect-field faithfulness, and nilpotent rigidity on A/p. Breuil's original arXiv math/0009252, Theorem4.2.2.9 (printed p.540), was also opened as the odd-prime predecessor. Perfect residue field is stated exactly; the separate all-A proof covers imperfect residue fields.

This closes the requested separate DVR derivation. The only outstanding B scope question is the requested maximal literature class in B.3; all concrete statements, examples, and specified morphism/image comparisons in B.1–B.4 are written.

## Targeted check of root's uniform Artin–Rees route to L1

The fixed-module lemma is valid. Let R be Noetherian, C finite, R^d→C a fixed surjection with kernel K, and choose N with K∩I^NR^d⊂IK. Suppose I lies in the Jacobson radical and φ:B→C is a map of finite modules inducing an isomorphism modulo I^N. Nakayama first gives φ surjective. Choose lifts in B of the fixed generators of C; their images generate B modulo I^N, hence generate B. If K′ is the resulting kernel R^d→B, then K′⊂K. The isomorphism modulo I^N gives K⊂K′+I^NR^d, hence K⊂K′+IK. Nakayama on the finite module K/K′ proves K=K′. Flat base change preserves the kernel and intersection, so the same N works after arbitrary flat localization. If the relevant target is a direct summand C_1 of C, apply the lemma to B⊕C_2→C_1⊕C_2 for the complementary summand C_2.

For a finite test scheme T and an actual separated locally quasi-finite local representing scheme X, the module map is O_X→O_T, so O_T is indeed the fixed target. Over the strict henselization of the base local ring, choose the finite local branches through the selected points. The residue fields of those branches are finite purely inseparable extensions of a separably closed field, hence separably closed. An étale branch map therefore has equal residue fields; since the source and target are finite local henselian rings, it is an isomorphism. The module lemma reflects this from the fixed I^N-thickening. The other components of T are adjoined to the source module to apply the fixed exponent.

Axiom8 says only that some nonempty open exists. Before applying it, remove all irreducible components of T_{V(I^N)} other than the closure of the selected generic point. The remaining open Z is irreducible, locally of finite type, and contains that generic point. The Artin–Rees comparison continues to use the original finite ambient T, so Z need not remain finite. Any nonempty 8-open is then dense in the desired component. After isolating the same component in the étale pullback of the original closed stratum C, its projection has relatively open nonempty image in C. This uses openness of the étale projection, not openness of a finite map. Generization stability follows from ordinary étaleness on each actual local representing scheme; Noetherian induction now yields constructibility and hence openness of the étale locus.

This targeted check supports the L1 route **conditional on actual local representability** F_{Spec O_{S,s}}=h_{X_s}. It does not promote a finite formal model to an actually modular model, and therefore does not resolve the separate actual-versus-pro-modular premise in axiom7. No finite computation is applicable to this argument.

## Henselized alpha_p: the fpqc gate narrowed to non-G/non-Noetherian bases

The functor P(R)=alpha_p(R^h_(t)) is an fppf sheaf and preserves filtered colimits. Here is the complete argument for the additional flat descent, beyond weakly étale descent. For a finite locally free A-algebra B, finite algebras over a henselian pair are henselian; hence B^h_(t)=B⊗_A A^h_(t), and the same identity holds for B⊗_A B. Ordinary finite faithfully flat descent therefore gives the P equalizer. Zariski (indeed étale) descent follows from de Jong–Olander, Theorem2, after replacing A by A^h. Stacks Lemma37.48.2, Tag05WN, opened in this run, says fppf covers are refined by successive Zariski and finite locally free covers, so these checks give the fppf sheaf assertion. Henselization is a filtered colimit of finitely presented étale neighbourhoods, and finite equations defining alpha_p descend at finite stages; thus P commutes with filtered colimits of rings.

More generally P has descent along faithfully flat maps A→B which are filtered colimits of smooth A-algebras B_i. Every A→B_i is already faithfully flat: it is smooth, and its spectral image contains the surjective image of SpecB→SpecA. A section and its equality on B⊗_A B descend to a common B_i by the colimit assertion, and fppf descent at that stage gives the descent to A.

Consequently, P satisfies arbitrary fpqc descent whenever A is a Noetherian G-ring. First take A local with t in its maximal ideal. Stacks Lemma15.51.14 (0AH2) and Popescu's theorem16.12.1 (07GC), both opened, make A→Ahat an ind-smooth faithfully flat map, along which the preceding paragraph proves P descent. For any faithfully flat A→B and henselian cocycle b in P(B), pull back to B⊗_A Ahat. The complete-local lemma already proved gives a_hat in P(Ahat). Its two pullbacks to P(Ahat⊗_A Ahat) agree after the faithfully flat base change by B, and hence agree because P is fpqc-separated. Descent along A→Ahat gives a in P(A); after the faithfully flat base change B→B⊗_A Ahat it equals b, so separatedness gives equality already over B. If t is a unit, P(A)=0 and all terms are zero. For a nonlocal Noetherian G-ring, apply the local argument at every maximal ideal, spread sections and their equalities to principal opens using filtered-colimit compatibility, and glue by Zariski descent.

Thus arbitrary fpqc covers of every finite-type F_p-algebra pass. This is a genuine narrowing of the gate; it is not yet a proof for all rings. Passing from these bases to arbitrary bases cannot be justified merely by writing an arbitrary flat map as a filtered colimit of finitely presented flat maps, since that assertion is false (0ATF).

An additional nearby result was opened: Česnavičius, *The affine Grassmannian as a presheaf quotient*, arXiv2401.04314v3, Proposition3 (pp.2–3), proves fpqc descent for R↦X(R{u}) for every affine X, with R{u} the henselization of R[u] along u. Its proof uses Raynaud–Gruson I, Corollary3.2.6 to prove injectivity of the relevant henselized tensor-product map. Since R^h_(t)=R{u}/(u−t), extending this theorem to the quotient would settle the candidate, but that extension needs a higher Čech-exactness or purity argument and has not been proved. Do not cite Proposition3 itself as the arbitrary-pair result.
