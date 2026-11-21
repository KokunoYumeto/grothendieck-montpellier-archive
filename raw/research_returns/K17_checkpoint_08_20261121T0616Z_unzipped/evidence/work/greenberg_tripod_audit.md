# Independent full audit: the Greenberg kernel deduction

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro, 21 November 2026. Effort not exposed. **Verdict: PASS for the conditional deduction under the explicitly stated one-variable Greenberg hypothesis.** I read every section, 1–10, of `work/greenberg_magnus_adaptation.md` and independently reconstructed the mathematical argument. The reviewed full-draft hash is `782714b02793482cb42b26bf90f4b75c5a6324f6422af4b6ae8840fb7456dc6e`. The separate cup/extension lemma is in `work/cup_ext_pole_section.tex`, with its independent archive audit in `work/cup_ext_archive_audit.md`.

This is a paper-proof audit, not formal verification. It proves an implication from Greenberg, not Greenberg itself, and makes no assertion of novelty. The intended representation is equivariant for the commuting Gamma and Delta actions, as expressed by hypothesis 3 and the arithmetic construction; spelling out the word “equivariant” would be a useful notation clarification.

## G-A: actual generators and topology

The compact torsionfree abelianization is a product of copies of Zp, by duality with divisible p-primary groups. Metrizability gives a countable convergent product basis. The open quotient H → H_ab lets one lift a basis converging to zero to group elements converging to one. The previously checked exact prime-to-p eigenlift construction works inside invariant neighborhoods, so the parity of these actual lifts is controlled.

The compact free group on those lifts surjects onto H because its closed image is Frattini-surjective. Projectivity of the free target gives a section. The section's closed image is itself Frattini-surjective in the source, hence is the entire source. Thus this is an isomorphism of the whole H. The proof does not use finite-generation Hopficity and does not infer group finite index from finite index in an abelianization.

The finite-rank free-group projections detect every element: every finite quotient kills a tail of the convergent free sequence. The assigned degree, one for odd letters and two for even letters, is separated. At fixed assigned degree the coefficient module is the stated completed tensor module. This construction remains integral until the explicit bounded rational change below.

## G-B: odd coordinates and actual even companions

Finite Lambda generation gives continuous integral maps between U and a finite free Lambda module with compositions equal to one fixed power of p. Tensoring degreewise gives corresponding scalar compositions. The completed tensor modules are products of Zp and are torsionfree, so these maps remain injective and become isomorphisms after inverting p. Their bounds may depend on the fixed degree; no bound uniform in all Magnus degrees is required.

In an odd character, Gamma equivariance makes every target linear coefficient a scalar times evaluation of the corresponding bounded power series at u^m−1. The scalar is nonzero because the actual image is dense in the finite target quotient and its weight-m abelian coordinate is nonzero. Rescaling each rational target generator is legitimate in the weight completion: any finite weight sees only finitely many rescalings.

For each even component, the actual conjugates of an integral multiple of a rational cyclic generator have abelian classes forming a rational basis. Their assigned degree-two terms are an invertible finite linear change of the original even letters plus quadratic odd tensors. The inverse change subtracts those tensors and inverts a finite matrix. It is a homogeneous triangular automorphism of the fixed-degree rational tensor algebra with bounded coefficients. Consequently it preserves the first nonzero assigned degree of every actual group element.

The crucial companion identity is exact: the actual ordered characteristic-polynomial product is in the closed derived subgroup, and its degree-two term is precisely the odd–odd tensor C. Since every even lift has target length at least two, there is no length-two BCH correction from multiplying even lifts. Thus q(z)B(z)=C, with z=u^(m+n), is the actual leading-coefficient relation. It is the same extension datum used in K17-CUP-EXT, not a substitute with matching characteristic ideal.

## G-C: substitution and pole separation

The finite partial-fraction change preserves the common numerator in each even component and allows all multiplicities. Removing a finite collection of possible integer denominator-zero weights leaves Cartesian residue-class tails with interior p-adic accumulation. Each analytic identity is obtained only after clearing its finitely many denominators.

Continuity of substitution can be verified before changing coordinates. Finite-rank projections tend uniformly to the identity on every finite group quotient. The continuous image in each finite target-weight quotient is compact, hence its coefficient functions are bounded. At a fixed target weight only finitely many assigned degrees contribute, since every source letter has target length at least its assigned degree and all target generators have positive weights. The compact limit therefore gives the same coefficient as actual rho. Bounded rational changes in the fixed leading degree preserve this calculation. There is no application of a compact-free universal property directly to a noncompact rational unipotent group.

I reconstructed the final Laurent extraction in full. Choose a nonzero pattern with the largest number of pairs and then a componentwise maximal pole-order vector for its selected roots and positions. Selected pairs are disjoint, so the required odd residue types can be chosen independently. Set their divisors equal to independent variables S_j. Every other denominator has nonzero constant term in the fraction field of the surviving base variables: at the same position it has a different root, and at a different position it couples independent selected blocks. Such denominators are units in the power-series ring in the S_j.

The coefficient of the chosen negative Laurent monomial receives no contribution from a pattern missing a selected pair, from another root, from an extra pair, or from an incomparable pole-order vector. The surviving term is exactly the nonzero singleton coefficient times the product of the nonzero divisor restrictions of C. The field has no zero divisors. This proves injectivity, including the empty-pair case and repeated roots.

## G-D: arithmetic modules and source scope

I separately reread the complete proof of Wake–Wang-Erickson, *Ordinary pseudorepresentations and modular forms*, Proposition 2.2.6, pp.3–4, and the relevant exceptional-character statement in Lemma 5.2.7, p.13, in `work/wake_wang_erickson_ordinary.txt` with the earlier checked rendered notation. The reflected character is theta=omega a^−1. Its even unramified Ext group vanishes after inverting p under Greenberg. Since R=Lambda[1/p] is a one-dimensional noetherian UFD, it is a PID, and the odd ramified component is free of rank one over R.

I also reread Sharifi's Coleman sequence, Theorem 5.5.31 with proof, p.148, and Proposition 6.1.1, pp.151–152, in `work/sharifi_full_iwasawa.txt`. It supplies the exceptional omega component as the ideal (gamma−u), and the omega^−1 component is free. Their unramified components vanish by the stated Stickelberger input. These exceptional characters are distinct for p≥5; the proof explicitly leaves p=2,3 to the earlier separate results.

The earlier checked Kummer comparison and Ferrero–Washington make the even module finite over Zp; H free makes it torsionfree. Greenberg gives characterwise pseudocyclicity of the minus unramified module, hence cyclicity of each even rational component. No integral Lambda freeness or integral cyclicity is silently inserted.

The hypothesis is one-variable finiteness of Xplus for the cyclotomic tower. It is not the multivariable pseudo-nullity conjecture appearing elsewhere in Sharifi's work.

## G-E: cups and the maximal-pro-p comparison

I independently read WWE, *Pseudo-modularity and Iwasawa theory*, §2.1, Corollary 2.1.3/Conjecture 2.1.5, and the complete proofs of Corollaries 8.1.2–8.1.3 and Theorem 8.2.3, pp.48–51. Under Greenberg, Corollary 8.1.3 gives the integral varpi isomorphism after removing source p-primary torsion. Thus varpi itself is surjective. I read FK §§7.1.8–7.1.10 and 7.2.8–7.2.14 in the 2012 author version; §7.1.10 directly gives finite-level cyclotomic-unit symbol generation from this surjectivity. No simple-zero hypothesis is used.

The finite coefficient convention is consistent: Gamma^(p^n) has base field Q(mu_(p^(n+1))); reducing the FK p^(n+1) class-group quotient yields the p^n target. The omitted even characters have zero targets by the exceptional unramified vanishings and the surjective norm projections. Norm surjectivity follows from disjointness of the Hilbert p-class field and the totally ramified cyclotomic step. A component of unit characteristic power series is finite and then zero because the minus module has no p-torsion. The minus p-unit line is cyclic roots of unity; its self-cup is zero for odd p, and mixed-parity cups do not enter the even target. No Vandiver assertion about all of H¹ is used.

The comparison with actual group cohomology is especially useful. If N is the kernel from the full étale fundamental group to its maximal pro-p quotient P and A is a finite p-primary P-module, a nonzero P-equivariant homomorphism N → A would produce a strictly larger pro-p quotient. Hence H¹(N,A)^P=0. The five-term sequence gives H¹(P,A)=H¹(G,A) and injectivity in H². The universal finite étale tower has zero H¹, since each finite torsor is killed at a later cover. Cartan–Leray consequently gives H¹(G,A)=H¹_et(S,A) and an H² injection. Cup generation of the even étale target and unique lifting of each input then make the even H² comparison an isomorphism.

I freshly opened and read Milne, *Lectures on Étale Cohomology*, version 2.21, Theorem 14.9 with proof, Remark 14.10, Example 14.11, and Proposition 14.13, printed pp.96–98: https://www.jmilne.org/math/CourseNotes/LEC.pdf, retrieval `turn794240536view0`. This verifies the precise tower spectral sequence used. No assertion that the entire arithmetic scheme is a K(pi,1) is required.

## Verdict

Combining the arithmetic inputs with K17-CUP-EXT supplies every actual pole restriction required by the full-H separation proof. A tripod-kernel element is cyclotomically trivial and hence lies in H; its rational image is trivial, so injectivity kills it. The conditional equality Omega_p^*=Omega_p under one-variable Greenberg therefore passes this audit. The proof still assumes that finiteness hypothesis; no unconditional non-Vandiver case or converse is inferred.

Primary URLs, in addition to Milne above: https://arxiv.org/pdf/1510.01661v4 ; https://arxiv.org/pdf/1505.05128 ; https://www.math.ucla.edu/~sharifi/iwasawa.pdf ; https://www.math.ucla.edu/~sharifi/sharificonj.pdf . FK locators refer explicitly to the retrieved 15 August 2012 author version, not an uninspected final publication.

## Final TeX translation readback

I subsequently read all of `work/greenberg_kernel_section.tex` (560 lines), including K17-RATIONAL-MAGNUS, K17-ETALE-PROP, the arithmetic application, and K17-GREENBERG-KERNEL, together with its new bibliography. The exact reviewed TeX hash is `192a459b0bf3852117aa2bfb395e8df59975d464782cafa0e321c2968b4e847d`. **PASS:** the translation retains every substantive step and explicitly includes Gamma×Delta equivariance. I reread Sharifi Proposition3.4.1 and its complete proof once more to check the finite-target citation: the proposition explicitly states both injection into the direct limit and surjectivity of the inverse-limit minus norm projections. Thus its use for the omitted finite targets is exact. No correction to the clean TeX was requested.

The author's subsequent finite-generation clarification was also independently checked. Finite Kummer H¹ makes P finitely generated. Adjusting its finite generators by powers of the Gamma section gives finitely many h_i in H; quotienting by their closed normal closure leaves a procyclic group surjecting onto Gamma=Zp, hence exactly Gamma. Therefore their conjugates normally generate H and their abelian classes generate M over Lambda. A finitely generated pro-p group is second-countable, as is its closed subgroup H. This elementary argument replaces the less precise weak-Leopoldt attribution and introduces no additional hypothesis. The resulting TeX hash `346946f43c4fb9160072cbddfb502cf01b588cdf4f6ed16d601ecbb94c1e42cc` also passes.

## Commuting section clarification (2026-11-21 02:46:46 UTC)

The added paragraph was read in full. A finite coprime Delta complement acts on the H-torsor above a Gamma generator. Nonabelian H^1(Delta,H)=1 follows from finite coprime complement conjugacy and compactness, so the torsor has a fixed lift. Its closed procyclic subgroup is a pro-p group mapping onto the infinite procyclic Gamma, hence is Z_p and maps isomorphically. This supplies precisely the commuting section required by the proof. PASS; no extra hypothesis.
