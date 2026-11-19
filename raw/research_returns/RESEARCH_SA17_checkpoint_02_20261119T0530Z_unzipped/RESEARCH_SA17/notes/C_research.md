# Part C research log

Started 2026-11-19 04:01 UTC, GPT-6 Astra (OpenAI, ChatGPT Pro mode), child finite_lambda.

## Exact objects

Cote 133 transcription scan 26 defines distinguished functors as finite coproducts of Inj(I,-)/H; equivalences are natural transformations eventually bijective. Scan 28 uses exact K, whereas scan 6 WG is the split completion of isometry classes, without metabolic relations.

## Working discoveries

- Burroughs (1974), Proposition 1.1 and Theorem 1.2, opened publisher PDF, proves R_Z(S_*) polynomial. Its proof quotes Heller--Reiner in an implausibly broad Dedekind form (trivial group would contradict Pic); underlying theorem remains to inspect before generalizing to Z_p.
- Distinguished FI functors have a unique support species, finite supported. Eventual equivalence between such functors should be an actual isomorphism by support recovery. Their additive ring is direct sum of B(S_n), with product formed by pairs of supports whose union is all of the label set. This is not the induction product.
- Subset powers fail the special lambda product identity already on the free C_2-set of size two. Symmetric-power opposite lambda is a distinct pre-lambda structure, with lambda^2(free2)=free2-1. Need explicit failure for this too.
- Promising uniform split WG counterexample in each odd characteristic p: on BC_p let V_j be the indecomposable Jordan module of length j; X=H(V_2), Y=V_p with invariant dot product. In the split Green ring, psi^p(V_p)=p and psi^p(V_2)=2V_p-2V_(p-1). Since V_2 V_p=2V_p, multiplicativity defect after forgetting forms is 4p(V_p-V_(p-1)-1), nonzero. Need fully check proof and finite p=3 certificate.

## Sources opened

- John Burroughs, Operations in Grothendieck Rings and the Symmetric Group, Canadian J. Math. 26 (1974), 543--550, DOI 10.4153/CJM-1974-050-3. PDF opened in full via web. Prop.1.1, Thm.1.2 inspected.
- Serge Bouc and Karl Rokaeus, A note on the lambda-structure on the Burnside ring, version 31 August 2009, https://www.lamfa.u-picardie.fr/bouc/Burnside2.pdf. Intro distinguishes inverse symmetric powers; Thm.1.1 gives explicit virtual subset formula.

## Checkpoint 1 research state (2026-11-19 04:40 UTC)

C.tex now contains full proofs or scoped reductions for all results listed in results_C.csv. They have not yet undergone a separate-agent proof audit. Both exact finite-code certificates ran successfully: logs/C_finite_certificates.json and logs/C_group_certificates.json. The word "Proved" marks the stated scoped claim, not the entire open-ended prompt item.

### Main determinations

1. All Q-algebras are classified by K0(k)=Z. Every nonzero ring of positive characteristic N fails by the explicit Newton relation p_N=0. This includes composite characteristic. Z is known from Burroughs. The DVR argument uses G0 resolution/localization and integral Specht lifts; it covers every mixed-characteristic DVR and every Z_p. The ring Z_(2)[u]/(u^2-1) is local, characteristic zero, torsion-free, has K0=Z, and fails in degree two by the determinant u, which is neither 1 nor -1.
2. Distinguished FI functors are finite species evaluated on all subsets. Eventual equivalences preserve least supports and identify no additional objects. Product counts overlapping supports with union all labels. Composition extends by finite differences to the group completion. Subset powers and inverse symmetric powers are different prelambda structures; both fail specialness, with program-checked fixed-point defects. Therefore L7 is false if it asserts a special lambda ring or scan19's simultaneous subset/symmetric-inverse convention. Its weaker assertion of a prelambda ring with composition is true. No novelty or priority claim is made about FI-sets.
3. L8 is true in characteristic zero by universal orthogonal representations and semisimple metabolic splitting. Exact GW in Zibrowius cannot be silently substituted for scan6's split WG. In each odd characteristic, actual forms H(V2) and Vp on BCp give Adams-p multiplicativity defect 4p(Vp-V_(p-1)-V1) in the split Green ring. An etale Cp torsor of proper curves gives a fully faithful tensor functor; Krull-Schmidt preserves the nonzero class. Waterhouse Thm4.1(1),p536 supplies E/Fp with trace1, hence Cp rational points and a free quotient torsor. Split BO_m is computed in characteristic zero over arbitrary fields for split O_m by symmetric simples and multiplicity forms. The hyperbolic SW formula is re-derived with the mu4 Bockstein correction a cup y and Laborde's injective nonisotropic splitting.
4. The exact ordinary-group center/derived criteria are proved by a normalized-cocycle twist. All alternating pairings occur; admissible pairings have Ext1_Z(Q,C) torsors of extensions. The corrected zeta must use centrality modulo C, not only modulo N'. Crossed-module pairs alone lose Hall's commutator pairing: Heis(F3)^2 and Heis(F9) have identical pairs but distinct rank distributions 16/64 and0/80. Hall's original Section2 p133 is visually checked. The perfect-field formal splitting assertion is false even up to isogeny, already for a multiplicative BT self-extension overFp with unipotent Frobenius. A bounded-exponent commutative kernel yields a corrected quotient-isogeny splitting, and multiplicative BT extensions split rationally exactly when their Galois representations do.

### All-rings C.1 gate and successive approaches

- A blanket "local characteristic zero" theorem is false by the determinant counterexample above. Generic splitting cannot simply be inferred from locality; its generic fibre is Q x Q.
- A reduction through Heller--Reiner as quoted by Burroughs was rejected: the broad Dedekind statement would contradict Pic(k) already for the trivial group. The original AMS article was blocked (403); the DVR proof instead uses explicit resolution/localization and the unitriangular Specht matrix.
- Positive characteristic cannot be treated just by comparing ranks over fields: nonreduced rings of characteristic p^r still need an exact relation. The invariant vector in the augmentation module supplies the uniform characteristic-N relation.
- Current proposed regular case: for finite free symmetric-group algebra over a noetherian base, the integral Specht modules should generate G0 over G0(k), by noetherian induction on support and their fiberwise generation. For a regular noetherian ring, resolutions identify R_k with G0(kS_n). If K0(k)=Z and a characteristic-zero point exists, this would imply the polynomial property. This argument is being proved; not yet in the claim ledger as a theorem.
- Current proposed stronger singular-domain counterexample: R=Z_(2)[a,b,c]_(2,a,b,c)/(bc-a(2-a)) and T=[[a-1,b],[c,1-a]]. Direct multiplication gives T^2=1 on the free moduleR^2. R is expected normal with Cl(R)=Z, generated by (a,b), while (2) is prime principal. R[1/2] is regular and connected; the + eigenspace of T corresponds to the nontrivial ideal class. If the class-group computation is established, this refutes sufficiency of connected generic fibre and K0=Z even for normal local domains. The class-group calculation is the precise current gate; no theorem claim yet.
- General singular and nonnoetherian mixed-characteristic classification remains open. Finite presentation permits descent of individual representation data, but does not automatically descend all equalities or classify rings; this is not being advertised as a solution.

### Remaining C.3/C.4 scope gates

- BO_m over positive-characteristic or nonfield bases is not computed by the semisimple formula. A possible structural replacement uses indecomposable self-dual representations, types, and hermitian forms over residual division algebras; this needs a full proof before inclusion.
- The smooth reading of formal I/II is refuted. The narrower noncommutative bounded-unipotent reading of I is not settled by the commutative Ext argument. The result is not silently extended to it.
- The manuscript's a-toric variants and global existence of an initial crossed-module realization are not settled by the relative twist theorem; it assumes one baseline G0, as the later pages do.

### Source and image audit

Official cote133 PDF was fetched from https://grothendieck.umontpellier.fr/133.pdf. Scans6,26,36 were visually inspected; their PNGs were moved outside the deliverable to external_sources/C_scans. Exact working-text anchors: split WG lines114ff; distinguished definition1056ff; scan36 I/II1367ff; corrected zeta scan47 about1857ff; scan49 twist about1959ff; scan53 derived test2160ff. The transcription is used as a locator, not authority.

Hall1940 was fetched via the official GDZ IIIF manifest and its article rendering: https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0182/LOG_0014.pdf. Section2 p133 conditions(1)-(3) visibly retain commutator compatibility. Its PDF has no OCR; rendered pages132-133 were inspected. The PDF and images remain outside the deliverable.

Tate1967 Sections1.2-1.4 and Proposition1 Section2.2 were opened. Laborde1976 SectionsII-III p50 were opened, verifying exactly the etale splitting and class axioms used. Zibrowius arXiv1308.0796v4 LaTeX source was downloaded and read, and the NYJM publisher PDF opened; Definition1.2, Proposition3.17, Corollary3.18 have been checked. The split/exact distinction is decisive.

The supplied study's hyperbolic SW derivation (readings/133_002-018_030-054.md lines80-124) has been rederived and credited. Michel Hua's project is credited for the link between scan4's formula and the deleted w composed with alpha=1 on scan9. The ordinary-group analysis of scans47-54 in the supplied study is credited and rederived; the Ext1-fiber formulation and explicit non-isoclinism example are given with no priority claim.

### Gate resolved at 04:42 UTC: normal local-domain counterexample

The proposed R=Z_(2)[a,b,c]_(2,a,b,c)/(bc-a(2-a)) example is now fully proved and inserted as Proposition C:normal_domain_counterexample. The full Cl(R) calculation was unnecessary. The height-one prime I=(a,b) is not principal by its two independent generators modulo mI. Since R is normal and (2) is a prime principal divisor, any principalization after inverting2 can be adjusted by a power of2 to agree with I at every height-one prime, then the normal-domain intersection criterion forces a principalization overR, contradiction. The positive eigenspace of T is I[1/2], giving the determinant obstruction in Pic(R[1/2]). Stacks031S and031T were opened for exactly the normality/intersection inputs. Symbolic certificate completed successfully; its initial structural SymPy-expression equality was replaced by expanded difference=0, with no change in the underlying mathematical identity.

### Regular and nonnoetherian positive cases proved (04:48 UTC)

The regular-noetherian theorem is now written: for every nonzero regular noetherian k, the property is equivalent to characteristic0 and K0(k)=Z. The supporting Lemma C:Specht_G0 uses associated-prime A-submodule filtrations and noetherian induction on support to span G0(kSn) by integral Specht tensors with G0(k). Regularity permits finite underlying-k-projective resolutions; a characteristic-zero residue field then proves injectivity. No finite-dimension assumption is needed because the locally-free loci of successive syzygies form an increasing open cover of quasi-compact Spec(k). Proposition C:filtered_colimits proves stability under arbitrary filtered colimits by finite matrix descent, giving explicit nonnoetherian mixed-characteristic local examples. These additions require independent review.

The parent has independently checked the key normal-domain counterexample outline (height-one ideal, adjustment by divisor2, eigenspace projection). This is logged as a targeted outline check rather than a full proof audit.

### Source gate closed and universal orthogonal obstruction (04:57 UTC)

Dipper--James--Mathas original Newton Institute preprint pp12--13 was OCRed and then visually checked: Theorem3.26 integral cellular basis, Definition3.28 free Specht lattices, Theorem3.30 complete absolutely irreducible simple heads. Graham--Lehrer author PostScript manuscript (tokyo.ps, dated2003-03-19) was downloaded in full, converted, and Proposition2.4(i),(ii) read for unitriangularity. The publisher PDF delivered a non-PDF denial; no claim to have inspected that publisher file. The integral modular Specht source gate is closed by these opened primary sources.

A further uniform theorem is now written: WG_sp(BO_m) is not special in characteristic p>2 for every m>=p+4, over every ground field. The standard representation restricted over the algebraic closure to W=H(V2)+Vp has self-Adams defect 8p(Vp-V_(p-1)-1). Its proof uses the augmentation-ideal identity V_(p-1)^2=1+(p-2)Vp and the explicit exterior series of V3. The exact certificate computes actual matrix Jordan forms and exterior powers at p=3,5,7; it gives defects (-24,-24,24), (-40,0,0,-40,40), and (-56,0,0,0,0,-56,56).

The structural computation of split WG(BG) over algebraically closed fields of characteristic not2 is also written. Forgetting the symmetric form is injective: any self-adjoint invertible comparison of two forms has a polynomial square root. Its image is the free subgroup generated by symmetric-type indecomposables, twice alternating-type indecomposables, and sums of a nonselfdual indecomposable with its dual. This is a full description in terms of the split Green ring, including products/exterior powers, but does not classify modular O_m indecomposables by highest weights. Thus the arbitrary-base BO_m scope remains explicitly open.

Further all-rings approach explored: nilpotent invariance cannot be assumed (rank-one p-torsion units over positive-characteristic dual numbers already contradict it). For flat mixed-characteristic dual numbers, involutions such as [[1,epsilon],[epsilon,-1]] are candidate generic-kernel classes; no invariant proving nonzero has been established. Reduction modulo2 alone loses the candidate because exact relations imply 2[L_(1+epsilon)]=2[1]. This failed detection is recorded rather than claimed as a new counterexample.

### Generic-comparison kernel obstruction (05:02 UTC)

For every prime p, k=Z_(p)[epsilon]/(p epsilon,epsilon^p) is local characteristic0 with generic fibreQ and K0 of every integer localization equalZ, yet fails C1. The rank-one Cp-character u=1+epsilon has orderp. Its induction toSp has p-cycle trace sum_(a=1)^(p-1)u^a=p-1+epsilon^(p-1), outside constants, whereas all rho monomials are permutation representations with integer traces. Subtracting induced trivial gives a nonzero class killed by generic comparison. This is separate from the earlier flat normal-domain obstruction, whose nontrivial class is visible in generic Pic. Code and output check all ring-law triples in the81-element quotient(Z/9)[epsilon]/(3epsilon,epsilon^3) and the six-matrix S3 action.

This disproves a proposed sufficient criterion using only K0(k)=Z and K0(k[1/N])=Z. It does not settle the general singular mixed-characteristic case, including flat nilpotent bases. No blanket nilpotent-invariance assertion is used.

The original manuscript images28,29,47,49,53 were now visually read in addition to6,26,36. Scan29 visibly inserts polynomial-overZ, and scan47's corrected centrality is modulo pi1; scan49 leaves a sign to convention, fixed by our explicit cocycle law; scan53 states the derived-test surjectivity. Images remain outside the deliverable.

A tail-only gap in the first distinguished-functor proof was closed: a tail natural isomorphism is not defined on a small supportA. Instead, choose E with complement size greater than the target degree. Equivariance under Sym(E\A) forces the target support insideA; the transposition argument then gives equality. Common large ambient sets prove naturality and independence.

### Orthogonal-group structural gate narrowed to nonfield bases (05:08 UTC)

Opened original QSS1979 (J.Algebra59 pp264--289), Theorem2.2/Cor2.3 radical reduction, Prop2.4 transfer, Prop2.5 existence/types, Theorems3.2--3.3 hermitian Krull-Schmidt, and Application3.4(3). Opened earlier QSSS1976 (MSMF48 pp93--101), Cor3.5 p97. The previously independently derived algebraically-closed injectivity is exactly known there; its paper proof has been replaced by the exact source application and the status updated to Known, specialization checked. The full any-field characteristic-not2 structure formula is now stated: direct sum of hermitian Grothendieck groups over the residual division algebras of self-dual indecomposables, plus integer hyperbolic generators for nonselfdual pairs. Products/exteriors are calculated by lifting forms, performing actual tensor/exterior operations, decomposing, and reducing. The radical need not be a tensor ideal, so tensoring only the semisimple quotient would be wrong.

This gives WG(BO_m) structurally over all fields with2invertible. It does not enumerate every modular O_m indecomposable, nor solve arbitrary nonfield coefficient bases; these remain explicit. The elementary polynomial-square-root argument from the initial draft is retained as a check: for formsq1,q2 onM, a=q1^-1 q2 is invertible selfadjoint and has a polynomial square root over algebraically closedk via local Hensel lifting and CRT. It matches the original theorem and supplies no novelty claim.

Root independently reviewed and passed the entire Specht G0 generator lemma, including central associated-prime filtration, finite-matrix spreading, and support induction. The regular-resolution comparison remains under root review.

Additional literature search: Swan1963 The Grothendieck ring of a finite group and Heller--Reiner1964 were sought through original publisher/author sources. Full Swan and AMS scans remain blocked; snippets paraphrasing an arbitrary integral-domain result are not used. Burroughs's full PDF was re-read to confirm his exact definition and the overbroad Dedekind paraphrase. No further general theorem is inferred from that paraphrase.

### All-rings gate narrowed again (05:24 UTC)

Corollary C:allrings_injectivity completely classifies injectivity over every commutative ring: exactly nonzero characteristic0. A characteristic0 residue field supplies a ring retraction. Proposition C:allrings_obstructions splits off Lambda and gives the exact sequence0->ker(beta)->I->im(beta) intersect(reducedK0(kQ) tensorLambda)->0. This is explicitly an obstruction reduction, not a completed classification.

Theorem C:tame_degree treats arbitrary rings in whichd! is invertible, without noetherianity/reducedness: Z[1/d!]Sn is a product of matrix rings, using integral Specht action matrices and cellular semisimplicity on each residue field. Therefore any local residue-characteristicp base is polynomial in degreesn<p.

Theorem C:regular_modular_locus is the strongest new positive reduction: for fixedn, noetherian char0 k withK0Z needs regularity only at primes containingn!, not at characteristic0 points. Proof uses the exact category of finiteA=kSn-modules of finite k-projective dimension. Any lattice extending an A[1/n!]-projective has finite k-pd locally everywhere and hence globally; this gives surjectivity. Kernel classes arise by clearing a stabilized isomorphism and are Euler classes of supported finite modules. Specht support induction stays insideV(n!), where every coefficient module has finite k-pd. Its K0(k) class vanishes because K0(k)->K0(k[1/n!]) is onto by the same lattice argument and both areZ via rank. The comparison is therefore injective.

Consequently singularities lying only over characteristic0 are harmless underK0Z; the noetherian unresolved gate is now singularities meeting positive-characteristic fibres. Flat nilpotent examples remain in that gate. This is a genuine narrowing from globally regular bases; root review requested.

The characteristic2 quadratic edge case is explicitly proved and exhaustively checked: all strict forms have even rank, preventing exterior square ofH of rank1; onH tensorH/F2, pure-tensor compatibility forces q=ad orbc and factor isometries exchange them, so there is no natural quadratic tensor rule. This concerns quadratic, not symmetric bilinear, forms.
