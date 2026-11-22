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

## Continuation B.3 and item R — 2026-11-19, agent dieudonne

This continuation is GPT-6 Astra (OpenAI, ChatGPT Pro mode), run
RESEARCH_SA17_FINISH-20261119. The prior checkpoint is retained; the
following checks concern the steps specifically requested by the new prompt.

### Independent detector proof and executable certificate: closed

We reconstructed **every** divided power on the nine-dimensional algebra
B_p, independently of the previous proof by a divided-p criterion. For
z=a x²+b xy+c y²+d u+e v+f uv the complete generating polynomial is

    1+z T+de uv T²+(a^p u+c^p v)T^p
       +(a^p e+c^p d)uv T^(p+1)+a^p c^p uv T^(2p).

Terms of equal degree are added, so the de uv correction appears in γ₂
at p=2. The proof in B:finite-PD checks the additive, scalar, product,
composition, and nilpotence axioms for all primes. In particular this is
not an inference from the finite computation. The monomial quotient has
basis 1,x,y,x²,xy,y²,u,v,uv, which proves uv is nonzero independently of
the PD structure. All three PD presentations map to this detector;
(a,b,c,d) maps to (x,y,x,y) and every extra variable maps to zero.
These are maps of presentations, not embeddings of the original base
rings as closed subschemes of the same detector.

`code/B_finish_PD_detector.py` independently builds the quotient
multiplication table from monomial divisibility and checks the full PD
identities exhaustively for p=2 and p=3. It does not import the old
certificate. Its output is `logs/B_finish_PD_detector.json`. The p=2
run ranges over 512 ring elements and 64 ideal elements; the p=3 run
over 19683 and 729 respectively. Scalar identity counts are 131072 and
86093442; additive identity counts 16384 and 3188646. The script also
checks all products, iterated operations and the zero tails, with the
finite support bounds explained in its documentation. Each of the six
base/prime evaluations gives uv, with coordinates (0,0,0,0,0,0,0,0,1).
Recorded runtimes are 0.094406 and 5.816666 seconds. All assertions pass.

Stacks Tags 07LI and 07GS were reopened. The current displayed divided-p
formula in 07LI still omits the de uv term at p=2; substituting u+v
refutes that displayed formula. The corrected detector and the original
nonvanishing lemma are valid, so no counterexample base is lost.
No priority is claimed for this correction or this reconstruction.

### Positive union and closure continuation — 2026-11-19, after 14:01 UTC

The focused A branch is closed as a possible answer to strengthened L2:
root's Proposition A:hensel-adic-failure proves failure of adic effectivity
for P(R)=alpha_p(R^h_(t)) for every prime. I audited every used step;
the separate full note is `notes/B_finish_A_fpqc.md`, and the actual
targeted-proof event is appended to `checks_B.tsv`. This was an audit of
root's proposed proof, not a second independently discovered proof.

The following new B propositions are written in `sections/B.tex`.

* **B:reduced-PD-excellent.** The ordinary crystal functor is fully
  faithful on reduced excellent locally noetherian PD-torsion-free
  characteristic-p schemes. This is a deduction from de Jong–Messing,
  Proposition 4.4 and Section 1, using the proof of Theorem 4.6. Rational
  fullness supplies p^n h=D(psi). On a torsion-free universal envelope,
  the crystalline map on p^n-torsion is zero. Finite-group crystalline
  faithfulness on reduced bases makes psi kill G[p^n]; division of psi
  by [p^n], followed by cancellation on the envelope, gives integral
  fullness. At each finite group level, both a local group map and its
  equality with h modulo p^m spread to a principal open: the latter is
  an equality of finitely many entries in finite projective crystalline
  modules. Faithfulness gives compatibility and gluing. This spells out
  the local-to-global passage rather than assuming that a whole
  p-divisible-group map is finitely presented.
* **B:positive-closure.** Let Q be the quasisyntomic F_p-algebras, PF the
  reduced F-finite PD-torsion-free algebras, and PE the reduced excellent
  noetherian PD-torsion-free algebras. A local p-basis, in Lau's actual
  convention (equation (2.1)), implies Q: the Frobenius presentation is
  an infinite regular-sequence presentation, and its cotangent triangle
  splits because the map induced by Frobenius is null-homotopic. The
  excellent lci class also lies in Q. The literal union is therefore
  U=Q union PF union PE. Q is closed under finite ring products,
  arbitrary filtered colimits and étale localization/descent. PF and
  PE are each closed under finite ring products, finite polynomial
  extension and étale localization. For these assertions, Stacks Tags
  0G5Z, 08S9, 08R2, 07QS and Lau Lemma 4.7/Corollary 4.8 were opened
  and their exact hypotheses used. No assertion about excellence
  descending from an arbitrary ind-étale cover is used.
* PD torsion freeness itself is closed under arbitrary filtered
  colimits. For functorial polynomial presentations take D_i to be the
  completed PD envelopes. Stacks 05GG identifies their reductions with
  those of the ordinary envelopes. The latter commute with filtered
  colimits by the universal property. Thus C_n=colim_i D_i/p^n is flat
  over Z/p^n. In E=lim_n C_n, multiplication by p^n identifies C_m with
  p^n C_(m+n); these identifications give compatible division and prove
  E/p^n=C_n. If px=0 then x_(n+1) lies in p^n C_(n+1), so x_n=0 for
  every n. Hence E has no p-torsion and is the required completed
  envelope. This deals explicitly with completion in the nonnoetherian
  case, not by commuting a completion with a colimit without proof.
* The étale local closure U_et of U is a distinct stated class. Full
  faithfulness descends to it, using the uniqueness of local group
  morphisms and descent of group schemes and crystals. U_et is closed
  under étale localization/descent and finite ring direct products,
  since their spectra are finite disjoint unions. A ring direct product
  here does not mean the tensor product corresponding to a scheme
  fibre product.
* **B:closure-reduction.** The following are equivalent: PF union PE
  is contained in Q; U is stable under finite ring direct products;
  U is stable under arbitrary filtered colimits. If R in (PF union PE)
  is not Q, then R times F_p[epsilon]/epsilon^2 is neither reduced nor
  Q, refuting product closure. Moreover colim_n R[t_1,...,t_n] is not
  noetherian and not F-finite; its augmentation to R makes L_R a
  retract of the derived restriction of its cotangent complex, so it
  is not Q either. This is an exact reduction, not a proof that the
  inclusion holds or that a witness against it exists. No constituent
  closure property is misreported as a proof for the literal union.
* **B:positive-exclusion.** Q is PD torsion free (explicitly recorded in
  Lau's introduction, also by the quasiregular semiperfect-cover
  argument used above), as are PF and PE by definition. PD torsion
  freeness is étale local by Lau 4.7/4.8. Each of R0, R and R_infinity
  has the explicit nonzero p-torsion element certified by B:finite-PD,
  hence lies outside U and U_et. In contrast the field, dual numbers
  and perfect nonnoetherian ring in B:base-kinds all belong to Q.
  The prompt's literal request to put every B:base-kinds base outside
  the union contradicts those positive examples; the consistent
  corrected exclusion is proved and this wording conflict is explicit.

The current precise remaining B gate is the inclusion PF union PE
subset Q, or a counterexample to it; this controls the requested raw
union product and filtered-colimit answers. The corresponding general
filtered-colimit question for U_et and arbitrary infinite ring products
has not been proved. Finite ring products are the only products in the
proved closure assertion. This limitation is not hidden by the word
"products".

Further searches in this continuation included the exact phrases
"PD torsion free" + "quasisyntomic"/"quasi", "PD-torsion-free" +
"cotangent", "divided power envelope" + "torsion-free" + "converse"/
"complete intersection"/"if and only if"/"linear type"/
"determinantal", "PD-regular" + "immersion", and French combinations
of "enveloppe", "puissances divisées", "sans torsion", and
"intersection". Stronger-engine primary-source checks were also run.
No opened source in these searches supplied either the needed
converse or a certified nonquasisyntomic reduced PD-torsion-free
example. This reports the search outcome only; it is not a theorem
that no such result exists.

Two potentially relevant additional primary sources were inspected:
Arthur Ogus, *The saturated de Rham-Witt complex for schemes with
toroidal singularities* (18 June 2021), Lemma 5.1, p.32, proves that
the p-torsion in a PD envelope is a PD ideal and then passes to its
torsion-free quotient. It does not prove that the original envelope
is torsion free. Mathew's *Some recent advances in topological
Hochschild homology*, Construction 7.15 and the following
discreteness criterion, is a sufficient quasiregularity criterion;
the converse needed here is not stated. The newer Gardner–Madapusi
classification and Hoff–Lau sheared-display comparison keep a
stronger target, as previously recorded, and cannot be treated as
ordinary-crystal full faithfulness on additional bases without a
separate fully faithful comparison.

### Reopened primary sources and Known deductions

Source downloads and hashes are inventoried in
`logs/B_finish_source_inventory.json`, with repeatable fetching in
`code/B_finish_fetch_sources.py`. The new source directory is
`references/B_finish_sources/`; it contains the originals and extracted
text/LaTeX. Kisin's public author DVI initially returned 403 under the
default request; the public `people.math.harvard.edu` URL with an ordinary
browser user agent succeeded, and dvipdfmx/pdftotext produced the local
PDF and text. This was not an inference from its abstract.

* B:square-zero-Hom: reopened Lau, *Relations*, Lemmas 3.2–3.4.
  Lemma 3.4 prints “kernel” after asserting injectivity; the needed
  cokernel bound is proved directly in our section. For pI=I²=0,
  lift points fppf locally, apply p, and use p-divisibility to prove
  uniqueness. Iteration gives the stated uniform finite-thickening bound.
* B:effectivity: reopened de Jong 1995, Lemma 2.4.4. The explicit
  finite projective Hopf algebra argument in our section treats the
  nonnoetherian p-complete setting rather than silently importing
  noetherian hypotheses. Finite projective modules lift by idempotents;
  multiplication, comultiplication and the exact BT transition diagrams
  pass through the complete inverse limit.
* B:NiceIV: reopened Lau, *Smoothness*, Remark 2.6 and Corollary 2.7.
  Remark 2.6 explicitly allows non-nilpotent divided powers for the
  infinitesimal and unipotent alternatives. Its proof uses the nilideal
  in the Cartier-dual algebra to obtain nilpotent divided powers on the
  relevant product ideal. Canonical-p compatibility belongs to the
  separate display comparison in Corollary 2.7, not to Remark 2.6.
* B:DVR-classification: reopened Kisin's Appendix A.2, A.5 and A.6,
  author-preprint pages 29–33, and the perfect-residue-field assumption
  on page 1. The classifying filtration is the inverse image of the
  Hodge filtration. The PD ring S is p-torsion-free, hence a map
  commuting with φ and respecting that filtration commutes with φ/p.
  A.6 is integral for odd p and an isogeny equivalence at p=2. Reduction
  equality follows through S→W(k), perfect-field Dieudonné faithfulness,
  and nilpotent rigidity. Breuil 4.2.2.9 is the opened odd-prime
  predecessor. No extension of this classification to imperfect residue
  fields is claimed; the separate background theorem B:NiceV supplies
  that case.
* B:positive-crystals: reopened ALB v4 and published Remark 1.19,
  Proposition 4.29, Remark 4.30, crystalline comparison Theorem 4.44
  and main Theorem 4.74. Its unqualified introductory use of
  “crystalline Dieudonné theory” is made precise by admissibility in
  Proposition 4.29/Remark 4.30. The theorem in our section correctly
  retains the admissible-filtration essential-image condition.
  Reopened Lau v2 (12 July 2026), Lemmas 3.2–3.3, Theorems 7.6 and
  7.9, and Corollary 7.10. Reducedness in class (4) makes forgetting
  the admissible filtration fully faithful. Reducedness already implies
  F-nilpotence; this redundancy will be stated explicitly.
* B:divided-target: reopened Lau Theorem 9.3 and Corollary 9.5. The
  latter has injective Hom map with cokernel killed by p in
  characteristic p; it does not assert integral fullness. The former
  retains divided Frobenius. We also searched/opened Hoff–Lau,
  *Sheared displays and p-divisible groups*, v2 (27 May 2026),
  introduction and Sections 4–5, and Gardner–Madapusi's general
  classification. Their stronger targets do not directly enlarge the
  class for the ordinary crystal in scan 114.

### Literature union: narrower remaining gate, not yet closed

The new prompt explicitly asks for a **union of documented classes**.
It does not require a universal maximality theorem excluding every
possible additional base. Thus the old “maximal set of all bases” wording
in B:largest-literature-class was unnecessarily strong. The sourced
positive union itself can be stated; its requested unrestricted closure
properties still need a proof or a counterexample.

For characteristic-p rings the quasisyntomic condition is stable under
filtered colimits, using cotangent complexes and filtered exactness,
and under finite direct products and étale localization. Local-p-basis
and excellent lci classes are compatible with those facts. The difficult
extra class is reduced F-finite PD-torsion-free rings. Neither
F-finiteness nor excellence is preserved under arbitrary filtered
colimits. It is invalid to infer full faithfulness by saying that entire
BT groups or completed crystals descend to one finite stage: in general
their infinitely many compatible levels need not do so. Hoff–Lau's
finite-presentation lemma applies to a specific system of ideals in a
semiperfect ring, not to arbitrary filtered colimits.

Searches included exact variants of “PD-torsion free”, “quasisyntomic”,
“filtered colimit”, “divided power envelope”, “not complete intersection”
and “linear type”, and the current primary papers' backward citations.
No source proving that every reduced F-finite PD-torsion-free ring is
quasisyntomic has yet been located. Lau's introduction says that ALB
also yields the filtered PD-torsion-free theorem, but does not state
that ring-class inclusion, so we have not substituted it for a proof.

Two attempted routes remain exploratory: (a) find an explicit reduced
F-finite PD-torsion-free non-quasisyntomic ring, then examine its
polynomial ring in infinitely many variables; (b) study products of
complete intersections with unbounded numbers of equations, potentially
through an ultraproduct. Neither route has yet produced a certified
counterexample. In particular a product of one-variable truncated
polynomial rings is not a valid quick counterexample: it can have a
regular-principal presentation over a ring with a p-basis.

The prompt's demand that “each base of B:base-kinds” lie outside the
union has a literal contradiction: that remark deliberately lists both
positive and negative examples. The negative bases are the three
counterexample rings, and those are the bases to exclude. The field,
dual numbers and perfect polynomial perfection in the same remark
belong to the positive union by their displayed positive theorems.


## Cross-audit requested by root — 2026-11-19T14:22:39Z

Audited `sections/C_finish_nildivisible.tex`, C:divisible_nil_invariance. The proof passes. For the H^2 error cocycle, averaging gives c(g,h)=a(g)+g a(h)-a(gh), and replacing r_g by (1-a(g))r_g kills it. For a lifted linear map, d(g)=g f-f is a 1-cocycle; b=N^(-1) sum_h d(h) satisfies d(g)=b-g b, so f+b is equivariant. The Hom module of corrections is a direct summand of a finite matrix module over J, hence multiplication by N is bijective there. Reduction is surjective on Hom sets and reflects isomorphisms, but is correctly not asserted faithful.

Every admissible Grothendieck-group relation lifts: lift the equivariant quotient map E to B, lift an underlying linear section, correct it by the inverse of ps, and identify its finite projective equivariant kernel with the chosen lift of A using uniqueness of lifts. Conversely, reduction preserves these sequences because their underlying k-module sequences split. The presentation by isomorphism classes and all such relations therefore gives the claimed K0 isomorphism.

For merely nil J, inverse multiplication by N is k-linear. If L is finitely generated inside J then L^r=0 for some r. Any r elements of L^[N]=sum_a N^(-a)L, after multiplying them separately by suitable N-powers, lie in L; hence a power of N kills their product. That product lies in J, where multiplication by N is injective, so it is zero. Thus the saturation is nilpotent and uniquely N-divisible, and the directed union of these ideals is J. The already established finite-matrix filtered-colimit theorem includes equivariant maps and underlying split exact sequences, so the last passage is justified. The example Z_(2) plus Q epsilon, epsilon^2=0, has the stated local, nonnoetherian, fibre and K0 properties.

One wording caution sent to root and representations: in the final fibre corollary, restriction to a residue-field point kills epsilon; base change of A[epsilon]/epsilon^2 along A to F_2 instead gives F_2[epsilon]/epsilon^2, which is not a field. The intended residue-point statement is correct. This check is a targeted proof audit of another agent's proof, not an independent discovery.


## L2 open-support candidate: independent targeted audit — 2026-11-19T14:27:18Z

Root returned to the earlier subfunctor H(R)={x in R : x^p=0 and x belongs to tRx}. Its prior fpqc and finite-equation checks were already in this agent's notes; the new observation is that it also satisfies the strengthened noetherian adic condition4 and fails actual7. The audit passes in the corrected finite-type interpretation of8. To avoid any ambiguity over whether modularity is relative to the original base or its A-base change, take the base itself to be S=Spec F_p[[t]].

Define H on affines by the displayed formula and extend by Zariski gluing. Equivalently x^p=0 and (1-ta)x=0 for some a. The membership condition is local: Rx/(tRx) is a module, and vanishing of the image of x is detected locally. For a faithfully flat R to Rprime, first descend x in alpha_p by ordinary affine descent. Flatness identifies Rprime tensor Rx with Rprime x, and faithful flatness detects vanishing of x in Rx/(tRx). Thus the local witness in Rprime implies a witness in R, with no need to descend the chosen coefficient itself. The same criterion establishes fpqc descent, and its finite existential equations establish filtered-colimit compatibility.

For every noetherian I-adically complete ring A and compatible x_n in H(A/I^n), completeness supplies x in A with x^p=0. A coefficient a_n for x_n can be lifted to A, giving x in (tx)+I^n for every n. The fixed principal ideal (tx) is I-adically closed: I lies in the Jacobson radical by completeness, and Krull intersection applied to the finite module A/(tx) gives intersection I^n(A/(tx))=0. Hence x in (tx), which is exactly H(A). Injectivity follows from separatedness. This treats all noetherian adic rings, not only complete local rings.

Over an Artinian local S-algebra A, t is either nilpotent or invertible. In the first case H is identically the terminal functor on all A-algebras because 1-ta is always invertible; in the second it is alpha_p on all A-algebras. Thus the finite universal Artinian representing schemes are Spec A and alpha_(p,A), respectively. Valuation rings and fields are reduced, so H has only zero sections on them; uniqueness follows. For irreducible noetherian Sprime, either t lies in the generic prime and is locally nilpotent, so H is terminal everywhere, or D(t) is a dense open containing the generic point and H there is alpha_p. The given modular point z lies over that open. The represented-functor finite-type spreading argument already proved in A:8-literal verifies8. Literal8 without finite-type test restrictions is not being restored.

For7 choose A=B=F_p[[t]] over this same S and xi=0. On every local test centered at the closed point, t is in the maximal ideal, so 1-ta is a unit and H=0. The structural local S-map to Spec A is unique. A test centered over the generic point has no local map to the closed-point local pair, and its residue section is not eligible under the closed residue-field specialization condition. The minimal field of definition is F_p. Therefore this is an actual locally modular pair under even the original-S reading. At the prime (0), however, K=F_p((t)) has t invertible, and H over K is alpha_p. The local K-test K[epsilon]/epsilon^2 has nonzero section epsilon (epsilon^p=0 for every prime), with zero residue section, whereas pulling back xi gives only zero. Thus xi_(0) is not modular. This refutes L2 unconditionally under the corrected8 already in force. The audit was sent promptly to root; root owns the final theorem statement and result-table update.


## Closure reduction sharpened — 2026-11-19T14:30:41Z

The same inclusion PF union PE subset Q is also equivalent to filtered-colimit closure of U_et. If it fails, choose R in PF union PE outside Q and a prime p with R_p outside Q. Let T=R[t_1,t_2,...], q=pT+(all t_i), and B=T_q. The augmentation B to R_p splits the inclusion, so the cotangent retract obstructs Q. The t_i have independent classes in the maximal ideal modulo its square, detected by the coordinate derivations to kappa(p), so B has infinite embedding dimension. It is neither noetherian nor F-finite: an F-finite local ring C has C/m^2 finite over its Frobenius image, the field kappa(m)^p, forcing m/m^2 finite dimensional. If an etale cover of T had a member of U over q, its local ring would be faithfully flat and essentially etale over B. QSyn descends by cotangent amplitude, noetherianity descends faithfully flatly, and F-finiteness descends using the relative Frobenius isomorphism (opened Stacks 0EBS). All three possibilities contradict B. Thus T is outside U_et as well. The prior note describing U_et filtered-colimit closure as a separate gate is sharpened by this equivalence; arbitrary infinite ring products remain a separate unproved scope issue.

## Rejected positive witness (xy,xz): all-prime obstruction, 2026-11-19

The exploratory computation for R=F_p[x,y,z]/(xy,xz) is now explained
by an all-prime proof. This ring cannot witness PD-torsion-freeness
outside the quasisyntomic class. We searched the exact combinations
“divided power”/“PD envelope”, “xy”, “xz”, “torsion”, and “p^2”; no
priority is claimed for the following calculation.

Let P=Z_p[x,y,z] and let D be the ordinary universal PD envelope of
(p,xy,xz), with the canonical divided powers on p. Stacks Lemma
60.2.4 (opened in Section 60.2, https://stacks.math.columbia.edu/tag/07H7)
gives the presentation

    D = P<U,V> / (U-xy, V-xz, z^q U^[q] - y^q V^[q] for all q>=1).

Here P<U,V> is the divided-power polynomial algebra, and U^[q]
denotes its q-th divided power. To justify that these are ALL the
relations, a relation r xy+s xz=r0 with r0 in pP reduces modulo p
to r y+s z=0. Therefore r=zh+pa, s=-yh+pb, and
r0=px(ay+bz), for some h,a,b in P. Its corresponding divided-power
relation is the divided power of

    h(zU-yV)+pa(U-xy)+pb(V-xz).

Every positive divided power of either p-multiple lies in the
ordinary ideal (U-xy,V-xz), by the canonical formula p^n w^n/n!.
The addition formula thus reduces all relations to the divided
powers of zU-yV. Induction using the same addition formula shows
that the ideals generated by these and by
z^q U^[q]-y^q V^[q] (q>=1) agree. This proves the presentation,
including its compatibility with the canonical divided powers of p.

Put s=p^2, r=p and q=s-r. The element

    tau = z^q gamma_s(xy) gamma_r(xz)
          - y^q gamma_r(xy) gamma_s(xz)

is killed by p. Indeed the q-th scalar syzygy, multiplied by
U^[r]V^[r], gives binom(p^2,p)*tau=0. The binomial coefficient has
p-adic valuation exactly one, so it is p times a unit of Z_p.

To prove nonvanishing, give x,y,z the standard multigrading and
U,V degrees (1,1,0),(1,0,1). In degree (s+r,s,s), the free algebra
has Z_p-basis

    e_(m,n)=x^(s+r-m-n)y^(s-m)z^(s-n) U^[m]V^[n],

for nonnegative m,n with m<=s, n<=s, m+n<=s+r. The relations are
exactly their homogeneous multiples of the three families

    (m+1)e_(m+1,n)-e_(m,n),
    (n+1)e_(m,n+1)-e_(m,n),
    binom(m+h,h)e_(m+h,n)-binom(n+h,h)e_(m,n+h),

whenever the terms exist; in the third family h>=1 and also
m+h<=s, n+h<=s, m+n+h<=s+r. Consider modulo p the coefficient
functional lambda at the corner (m,n)=(s,r). An incoming linear
relation has coefficient s or r, both divisible by p; an outgoing
one cannot occur because m+n=s+r is maximal. In a scalar syzygy
having this corner as its first term, 0<h<=s-r<s, so
binom(s,h)=0 modulo p because s=p^2. Having this corner as its
second term would require m=s and m+h<=s with h>0, impossible.
Thus lambda annihilates every relation, but lambda(tau)=1. Hence
tau is nonzero already modulo p in D. Stacks Lemma10.96.3, Tag05GG,
identifies D/p with its p-adic completion modulo p, so the class
also survives in the completed universal PD envelope. Therefore
R is not PD torsion free for ANY prime p.

The supplementary executable `code/B_finish_PD_two_generator.py`
checks the finite graded relation certificate for p=2,3,5,7. Its
output is `logs/B_finish_PD_two_generator.json`: basis sizes are
22,79,466,1597; linear relation counts 34,138,880,3094 and scalar
syzygy counts 29,250,4195,28084. The corner functional annihilates
all of them and takes value1 on tau, and the multiplier has
p-valuation1 in each case. This is distinct from the original
nine-dimensional finite detector, whose required p=2,3 certificates
on all three original bases remain in B_finish_PD_detector.py/json.
No claim that this new tau is horizontal, or that it is a new
ordinary-crystal counterexample, is needed or asserted here.


## Closure gate resolved negatively — 2026-11-19T14:56:38Z

The former inclusion PF union PE subset QSyn is false for every prime. The full proof is now in `notes/B_finish_partial_perfection.md` and in the manuscript as B:PD-not-QSyn. Take P=F_p[a^(1/p-infinity),b^(1/p-infinity)], J=ker(P to F_p), and R_star=P x_Fp F_p[c,d]. This is reduced and F-finite, with p^2 explicit Frobenius generators. It is not QSyn because the presentation P[c,d] to R_star has nonflat conormal J direct-sum J; nonflatness follows from the regular-sequence syzygy (b,-a) and 1 not in J.

For PD torsion freeness, use the ordinary envelope D of (p,ac,ad,bc,bd) in Z_p[a,b,c,d] and partial Frobenius on a,b. On each homogeneous bidegree (u,v), its e-th iterate multiplies by a^(u(p^e-1))b^(v(p^e-1)). The envelope becomes p-torsion-free after inverting either a or b. Hence every homogeneous torsion class of positive degree is killed by some iterate; the zero-degree summand is Z_p[c,d]. The colimit envelope is p-torsion-free, and its completion is the universal completed envelope in a legitimate Lau ambient with mod-p p-basis c,d. The ambient identification is proved by the mod-p^n universal properties, not assumed from arbitrary presentations.

Root reported a full targeted audit PASS, opening Lau v2 Section4 (presentation, Proposition4.2, Definition4.3) and BMS2 Lemma4.34 on printed page25. Root checked the Frobenius constants, nonflat conormal, multigrading, torsion-killing, and completion comparison. The check is logged as targeted proof check, not independent re-proof. The example is infinite and no finite exhaustive certificate is claimed.

The now-proved corollary B:largest-literature-class states the raw union U and its etale-local closure U_et distinctly. U is preserved by etale extensions/localizations but membership does not descend under etale covers and U is not stable under finite ring products or filtered colimits. The product R_star times dual numbers is the first two counterexamples. The finite polynomial extensions of R_star lie in PF, while their infinite-variable colimit lies outside even U_et, using the already audited localization/infinite-embedding-dimension proof. U_et is stable under etale localization/descent and finite ring products. Thus all requested raw-union closure gates are settled; arbitrary infinite products of U_et are not asserted as an additional theorem. The literal contradiction in excluding every B:base-kinds example remains corrected by excluding the three negative bases and retaining the positive ones.

## Supplementary proposition integrated — 2026-11-19T15:22:49Z

The complete all-prime proof of B:PD-two-generator-rejected is now a numbered proposition in sections/B.tex. It proves the presentation and all relation bounds, nonzero p-torsion via the corner functional, and survival under completion. No horizontality or further ordinary-crystal counterexample is asserted. The existing p=2,3,5,7 certificate is referenced without a duplicate computation count.
