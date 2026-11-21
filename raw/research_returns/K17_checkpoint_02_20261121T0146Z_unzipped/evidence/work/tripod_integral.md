# K17 subsidiary research: pro-p tripod kernel and integral generators

Researcher: GPT-6 Astra Pro, agent `/root/tripod_integral`; effort setting not exposed. Date: 2026-11-21 (UTC). This is a source-checked research memo, not a claim to have reproved the cited literature. New deductions below have full short proofs and received a whole-proof reading. The stipulated Alpöge RH/Dirichlet-GRH results are not challenged or used to invent an unstated step-17 theorem.

## Executive findings

1. For odd regular p, the equality of the tripod kernel field with the maximal pro-p extension of Q(mu_p) unramified outside p follows from Sharifi, **Theorem 1.1**, together with Brown's rational Deligne–Ihara theorem. This is established background, not a new consequence of step 17.
2. Integral nonzero Soulé elements sigma_m already exist for every odd prime p. Their existence, the surjectivity of the full-domain Soulé characters, and integral free generation are different assertions.
3. Vandiver(p) is equivalent to surjectivity of all full-domain Soulé characters kappa_m (odd m >= 3). It does **not** imply integral free generation of the Galois-image Lie algebra. An explicit arithmetic counterexample is p=37: Vandiver holds, so all K_(4k)(Z) tensor Z_37 vanish, and all full-domain kappa_m are onto; nevertheless the degree-32 abelianization of the integral Galois-image Lie algebra is nonzero. A free graded Lie algebra on odd generators has zero even-degree abelianization. See the proof below.
4. The p=37 counterexample refutes the integral-free-generation inference. It does **not** refute the field equality. A separate complete pro-2 argument developed in this run now proves the kernel equality at2 from the free-product arithmetic presentation, Brown, and a Magnus/measure argument; see `work/pro2_moment_proof.md`. This is a checked deduction in this run, not a theorem located in the literature and not an Alpöge consequence. A separate nonlinear pole argument now also proves equality at37 as a checked deduction: work/irregular37_pole_proof.md. The complete multi-even extension has now passed two independent whole-proof audits and parent review: work/multieven_pole_proof.md. It proves kernel equality for any odd Vandiver prime with surjective odd-character H1 cup product, and therefore for every odd p<1000 using Sharifi2007 Cor5.9 and the verified Vandiver range. Together with the separate2 proof this covers every prime below1000, while the unconditional all-prime question remains unresolved.
5. The current rational grt_1 status needs updating: a recent primary manuscript by Hirose (16 Oct 2026), arXiv:2610.23719, Theorem 4 and §1.2, derives equality of the de Rham mixed-Tate motivic Galois group with GRT. It must not be described as still open merely on older memory. This is a separate rational result; it does not identify an arithmetic Z_p lattice or settle the kernel field. The attached war-game round 2 retains the OpenAI 008 result as claimed/unrefereed; it does not supply the actual round-1 B3/S9 rows.

## 1. Exact notation and kernel statement

Fix an algebraic closure Qbar of Q. Put X=P^1_Q minus {0,1,infinity}, F_p=pi_1^et(X_Qbar)^(p), and

rho_p:G_Q -> Out(F_p),
Omega_p^* = Qbar^(ker rho_p),
Omega_p = maximal pro-p extension of Q(mu_p) unramified at every finite prime not above p.

At p=2, the phrase unramified outside p permits ramification at the real place; imposing total reality changes the question. The field Q(mu_(p^infinity)) lies in Omega_p^*. Ihara's containment is Omega_p^* subset Omega_p. Thus

ker rho_p = Gal(Qbar/Omega_p^*),

not Gal(Omega_p^*/Q) and not Gal(Omega_p/Q(mu_p)). The desired equality is Omega_p^*=Omega_p, equivalently ker rho_p=Gal(Qbar/Omega_p).

Primary verified source: Sharifi, *Relationships between conjectures on the structure of pro-p Galois groups unramified outside p*, Proc. Sympos. Pure Math. 70 (2002), 275–284. Author's 13-page preprint: https://www.math.ucla.edu/~sharifi/publ/galstr.pdf. Definition on preprint pp.1–2; Theorem 1.1 on p.2. Browser reference `turn867444955view0`.

Let K=Q(mu_(p^infinity)), G=Gal(Omega_p^*/K). The weight filtration is obtained from the lower central series of F_p: Omega^*_(m-1) is the fixed field of the action on F_p/F_p(m+1), and F^m G=Gal(Omega_p^*/Omega^*_(m-1)). Then g_p=direct sum gr^m g_p, gr^m g_p=F^mG/F^(m+1)G, is a graded Z_p-Lie algebra. Each graded piece is a finite free Z_p-module of Tate twist m (Sharifi pp.1–2).

For m odd >=3, choose sigma_m in F^mG such that kappa_m(sigma_m) generates the nonzero image ideal kappa_m(F^mG). Let s be the free graded Z_p-Lie algebra on generators s_m in odd degrees m>=3; let S be the free pro-p group on corresponding generators (with the topology specified by Sharifi/Ihara). The maps are

psi:s -> g_p, s_m |-> sigma_m,
Psi:S -> G, s_m |-> sigma_m.

**Sharifi Theorem 1.1.** For an odd regular prime p, Psi is surjective. If the rational Deligne–Ihara conjecture holds for p, then psi and Psi are isomorphisms and Omega_p=Omega_p^*.

Brown, *Mixed Tate motives over Z*, Ann. of Math. 175 (2012), 949–976, Theorem 1.1 and the paragraph immediately following it on p.950 prove the motivic faithfulness statement of Introduction Conjecture 1, from which rational Deligne–Ihara follows as explained on p.949. Source: https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf; browser `turn517407318view0`. The comparison is explicitly restated in Ishii's 2026 paper below, so there is no need to infer an integral theorem from Brown directly.

**Checked deduction T-KERNEL-REG.** For every odd regular prime p, Omega_p=Omega_p^*, and psi is an isomorphism of graded Z_p-Lie algebras. Proof: Brown supplies the precise rational conjecture in Sharifi's theorem; apply Theorem 1.1. This proves the corrected field formulation of LM6 A.44. Nothing from Alpöge step 17 is needed.

Current verification: Shun Ishii, *On the kernels of the pro-p outer Galois representations associated to once-punctured CM elliptic curves*, arXiv:2312.04196v3 (6 Jan 2026), §1, Theorem 1.1 and Remark 1.1.1 (p.2). Source https://arxiv.org/pdf/2312.04196, browser `turn517407318view1`. He explicitly states the odd-regular theorem, Brown's removal of its rational Deligne–Ihara assumption, and the arithmetic role of regularity: Gal(Omega_p/Q(mu_p)) can be generated by (p+1)/2 elements iff p is regular (NSW (10.7.13)); in that case it is free pro-p of this rank. This condition concerns the full cyclotomic class group, not just its plus part.

## 2. What "integral generators" can mean

The following four claims must not be merged:

(A) A nonzero integral sigma_m exists in gr^m g_p.
(B) The character kappa_m:G_(Q(mu_(p^infinity)))^ab -> Z_p(m) is onto.
(C) There exists sigma_m in F^mG such that kappa_m(sigma_m)=1 after a fixed Z_p-basis of Z_p(m).
(D) The map psi from a free graded Z_p-Lie algebra on odd sigma_m is an isomorphism.

(A) holds for every odd p by Soulé nonvanishing and Sharifi Proposition 2.3. The element is chosen primitive relative to the *actual image ideal* of kappa_m on F^mG; this does not say that ideal is Z_p. (B), simultaneously for all odd m>=3, is equivalent to Vandiver(p). (C) can fail even at regular primes because of factorials in the weight filtration. (D) holds at regular odd primes and fails, for example, at p=37.

Source for (B) with a verified exact locator: Shun Ishii, *On Kummer characters arising from Galois actions on the pro-p fundamental groups of once-punctured CM elliptic curves*, arXiv:2312.04175v2 (4 Sep 2024), Theorem 1.1(1)–(3), p.2. It states: nonzero for every odd m>=3; onto if m=1 mod (p-1); all odd m onto iff Vandiver(p). It recalls the Kummer definition just above: reduction modulo p^n corresponds to p^n-th roots of the product of (1-zeta_(p^n)^a)^(a^(m-1)), for a prime to p. Changing a compatible primitive-root system changes kappa_m only by a p-adic unit. Source https://arxiv.org/pdf/2312.04175, browser `turn649307698view0`. Ishii cites Ichimura–Sakaguchi, *The nonvanishing of a certain Kummer character chi_m (after C. Soulé), and some related topics*, Adv. Stud. Pure Math. 12 (1987), 53–64. The original 1987 theorem-number locator has not been verified here; cite Ishii Theorem 1.1, not an invented 1987 statement number.

The notation kappa_m:G_Q -> Z_p(m) must be handled carefully: on G_Q it is interpreted cohomologically as a crossed homomorphism (cocycle), whereas on the cyclotomic kernel the action on the target is trivial and it is a genuine continuous character. An image-index statement must name its domain and normalization.

**Checked deduction T-FACTORIAL.** For every odd p and odd m>=3,

kappa_m(F^mG) subset (m-1)! Z_p(m).

Proof: Sharifi equation (2.10), preprint p.7, states on F^mG

kappa_m = (p^(m-1)-1)(m-1)! lambda_m^(p),

where lambda_m^(p) is integral, obtained by the embedding of g_p into Ihara's stable derivation algebra D tensor Z_p and the integral coefficient map lambda_m:gr^m D -> Z. The factor p^(m-1)-1 is a p-adic unit, proving the assertion. At p=3,m=5, the image lies in 3Z_3, so (C) fails. Yet Vandiver3 holds, all full-domain characters (B) are onto, and the odd regular prime theorem gives (D). This example proves that (B),(C),(D) are distinct, even in the regular case. It does **not** refute the cohomological index formula for the full-domain cyclotomic element.

Sharifi Proposition 2.3 gives the finer formula, when m=k+j(p-1), k>=3,j>=0:

v_p(kappa_m(sigma_m))=v_p((jp)!)+v_p(kappa_m(sigma_k)).

The recursion is equations (2.6)–(2.7), preprint p.5. Corollary 2.4 applies Vandiver to this formula; it is a lattice statement involving the stable derivation algebra, not a proof of integral free generation.

For the K-theoretic index formula, the correct normalized object is the cyclotomic class c_m in H^1_et(Z[1/p],Z_p(m)); the quotient H^1/(Z_p c_m), not an unspecified image of a map on G_Q, is the standard formulation. Kurihara1992 §5 Proposition5.1 and Remark5.2 (verified by the separate K-theory researcher) record the Euler-system inequality and the equality. In this normalization, vanishing of H^2 gives a primitive cyclotomic cohomology class. Passing to F^mG is a further restriction and introduces the factorial issue above. The main paper should use the K-theory agent's exact comparison statement and range.

## 3. Explicit arithmetic counterexample at p=37

Primary source: W. G. McCallum and R. T. Sharifi, *A cup product in the Galois cohomology of number fields*, Duke Math. J. 120 (2003), 269–310. Author's dated 5 Dec2003 34-page version: https://www.math.ucla.edu/~sharifi/publ/pairing.pdf. Browser `turn867444955view1` / `turn271584137view2`. Local PDF and extracted text: work/mccallum_sharifi_pairing.pdf and .txt.

Important exact locators:

- Theorem 7.5, preprint p.20: the pairing < , >_32 for p=37 is nontrivial (computed by the authors). We cite their theorem; no attempt is made to portray this run as repeating their Magma class-group calculation.
- Corollary 8.3, preprint p.23: for p=37,r=32 the explicit relation has nonzero [x_3,x_29] coefficient -11 (and several others). This provides a specific nonzero e_(3,32), up to a nonzero scalar depending on normalization.
- Theorem 9.1, preprint p.25: the Bernoulli/cup-product relation in the weight-graded image Lie algebra.
- Proposition 9.6, preprint p.28: a nonzero e_(i,m) with i<m/2 forces failure of integral freeness by some degree <=m.
- Theorem 9.7, preprint p.28: if p satisfies Vandiver, m is the first irregular even index, and rational Deligne holds through m, then gr^m g=Z_p xbar_m+gr^m h; if some e_(i,m) nonzero with i<m/2, then gr^m h is strictly contained in gr^m g and gr^m(g^ab) is nonzero.
- Corollary10.5, preprint p.33, and its following sentence: Theorem7.5 gives generalized Greenberg for Q(mu_37), meaning pseudonullity over the compositum of all Z_p-extensions (not merely plus cyclotomic Greenberg). Together with Sharifi Theorem1.3 this gives an independent *literature route* to non-surjectivity, without the sharper degree32.

Write h_p=im psi, the Lie subalgebra generated by the chosen primitive Soulé elements.

**Checked deduction T-37 (refutation of Fable's integral-free-generation inference).**

For p=37,

(1) K_(4k)(Z) tensor Z_37 =0 for every k>=1;
(2) every full-domain kappa_m, m odd>=3, is onto Z_37(m);
(3) (g_37^ab)_32 is nonzero, and h_37,32 is strictly contained in g_37,32.

In particular g_37 is not generated over Z_37 by a family consisting of one generator in each odd weight >=3. It cannot be a free graded Z_37-Lie algebra on such a family.

Proof. Vandiver at37 follows either from the primary verified computation in Buhler–Harvey or from the short exact modular certificate in work/vandiver37_certificate.py supplied by the K-theory researcher: the only irregular index is32, q149,z16 give V48 and V^4=142 not1 modulo149, satisfying the verified Vandiver criterion. The modern Kurihara/Quillen–Lichtenbaum equivalence gives (1), with k>=1. Ishii Theorem1.1(3) gives (2). The same exact Bernoulli computation shows32 is the smallest irregular even index. Brown's theorem supplies rational Deligne in every degree. McCallum–Sharifi Corollary8.3 supplies e_(3,32) nonzero, and3<16. Their Theorem9.7 therefore gives (3). If g_37 were generated as a graded Z_37-Lie algebra by elements of odd weights, its abelianization would be generated by their odd-weight images and would have zero component in every even weight. This contradicts (3). All implications preserve the ring Z_37; no tensoring with Q_37 is used to erase the finite abelianization obstruction. QED.

This is a complete proof of the stated *deduction from cited theorems*. It does not reprove the theorem of McCallum–Sharifi. Full-proof reading check: every hypothesis of Theorem9.7 is matched (odd irregular37, Vandiver37, least irregular weight32, rational Deligne through32, nonzero cup coefficient with3<16); its conclusion is about the weight32 *abelianization*, which is strong enough to rule out any all-odd homogeneous integral generating family, not merely one badly chosen family.

The conclusion does not say h_37 is nonfree: by rational Deligne the source free integral Lie algebra maps injectively (each source graded piece is torsion-free), so h_37 is a free subalgebra. The obstruction is that it is a proper nonsaturated sublattice of the entire image in degree32. The abstract image g_37 remains torsion-free degree by degree; its abelianization can have37-torsion.

**Checked deduction T-EVEN-GATE.** Suppose an odd prime p satisfies Vandiver. If Psi is not surjective and m is the least weight where the corresponding finite-weight map Psi_m is not surjective, then m is even and p divides B_m. Proof: Sharifi Theorem4.1 says an odd first defect would force failure of Vandiver, while an even first defect forces p|B_m. Apply its two alternatives. This precisely explains why eliminating the even eigenspaces of the cyclotomic class group is not the same as imposing regularity: an integral generation obstruction can survive in even weight, as32 at37.

## 4. The kernel equality remains a separate gate

Let H_p=Gal(Omega_p/Q(mu_(p^infinity))) and let q_p:H_p -> G_p=Gal(Omega_p^*/Q(mu_(p^infinity))) be restriction. This is a canonical continuous surjection with kernel N_p=Gal(Omega_p/Omega_p^*). Then Omega_p=Omega_p^* iff N_p=1.

The construction of nonzero sigma_m, surjectivity of all full-domain kappa_m, and the rational free Lie algebra control quotients of G_p. They do not show N_p=1. Sharifi's regular-prime proof uses the free pro-p structure of Gal(Omega_p/Q(mu_p)) and the precise number of its generators; Vandiver controls only the plus class-group part and does not furnish this free group. Ishii's2026 Remark1.1.1 explicitly isolates this dependency.

At p=37, the failure of integral odd generation does not imply N_37 is nontrivial. The comparison may be faithful while retaining extra integral arithmetic directions. Thus T-37 by itself neither proves nor refutes the field equality. A subsequent separate nonlinear argument in work/irregular37_pole_proof.md does prove the equality at37; it has two independent whole-proof audits and parent review.

### 4.1 The p=2 route: now a checked deduction

Sharifi's theorem is explicitly odd-prime; its proof cannot simply be cited at2. A separate argument was developed, written in full, and checked by the initiating researcher, two independent agents, and the parent researcher. The complete clean proof is `work/pro2_moment_proof.md`; the initial candidate and source-audit trail are preserved. It concludes **Omega_2^*=Omega_2**, allowing complexification at the real place.

The arithmetic input is Gras–Jaulent, *Note on 2-rational fields*, arXiv0805.1168, Theorem/Definition0 and Theorem2: P=Gal(Omega_2/Q)=C_2*Z_2. Its cyclotomic abelianization is Z_2^×. Passing to Q(i) yields a free rank2 group on gamma,h, and its cyclotomic kernel H is the inverse limit of finite-rank free groups H_n on conjugates gamma^i h gamma^(-i), i mod2^n. Hence each Magnus degree-r coefficient is a bounded measure on Z_2^r, and every nontrivial element has a first nonzero finite degree.

Let U be the actual rational outer-image prounipotent group. Hain–Matsumoto Proposition8.3/Theorem8.4 pp25–26 gives density of H in U and identifies its graded Lie algebra; Brown gives freeness on odd weight generators. The filtered-to-completed lifting lemma in the clean proof makes this the completed free Lie algebra, not just a graded comparison. The coefficient of the odd generator s_m on gamma^x h gamma^(-x) is a_m u^(mx), with a_m nonzero by density and u a topological generator of1+4Z_2. A kernel element with first Magnus measure mu would make its multivariate Amice transform vanish at every tuple u^m−1 with odd m>=3. These points accumulate at u−1 inside the convergence disc; the analytic identity theorem forces mu=0, a contradiction. The proof includes the finite-weight integration/substitution justification needed to make this formal-looking argument continuous.

No published p2 kernel theorem was located in the current literature search. Ishii2026 and Rasmussen–McLeman2026 still single out the odd-regular theorem. This deduction should therefore be labeled by its actual provenance and checks, without a claim of novelty. It does not use K4k2-vanishing or step17.

Additional exact Brown comparison: *From the Deligne–Ihara conjecture to multiple modular values*, arXiv1904.00179, §§2.1–2.3 pp1–4. Conjecture1 p2 is the actual pro-l outer-filtration rational freeness for every prime; Theorem2.1 and its following paragraph p4 explicitly give its proof from the motivic theorem. Retrievals `turn301647671view0`, `turn740492810view0`.

### 4.2 Irregular-prime continuation

The p2 proof requires a Gamma-equivariant free orbit basis, not merely abstract pro-p freeness. In fact, H_p is already free pro-p at every odd prime, including irregular primes: Iwasawa's original Theorem2, *Riemann–Hurwitz formula and p-adic Galois representations for number fields*, Tohoku33(1981), pp273–274, identifies this freeness with mu=0, and Ferrero–Washington supplies mu=0 for the abelian cyclotomic tower. The original theorem and its whole proof were read. This does not make the finite-base group Gal(Omega_p/Q(mu_p)) free. Despite freeness of H_p, the linear-moment argument has a concrete blind part: for odd p, the p-ramified Iwasawa module M=H_p^ab has

M^+ isomorphic to (A_infinity^−)^vee(1),

where A_infinity is the direct limit of p-class groups in the cyclotomic tower. This is Sharifi's Iwasawa notes Proposition3.4.7, obtained from the Kummer exact sequence Corollary3.3.14; Proposition3.4.1 shows that the minus class groups at finite levels inject into A_infinity^−. At an irregular prime this plus component is nonzero. All odd Soulé linear coordinates vanish on it by complex-conjugation equivariance. Thus even with abstract freeness, the first Magnus coefficient need not be separated by the odd linear moments used at2. Such directions may become visible in commutators — the degree32 result at37 is one example — but the first-degree detection argument alone cannot establish kernel equality. The initial continuation is `work/irregular_moment_gate.md`, including the original Iwasawa URL and exact source/module distinction. The nonlinear separation gate has since been closed at37 in `work/irregular37_pole_proof.md`: a unit odd–odd cup coefficient supplies a quadratic meromorphic moment with a genuine pole, and ordered-pair localization detects the extra even direction. The broader multi-even extension is now checked in work/multieven_pole_proof.md: cyclic companion modules, partial fractions, and colored-pair Laurent coefficient separation handle repeated roots and arbitrary lambda. The sufficient general-prime hypothesis is Vandiver plus odd cup surjectivity, yielding every odd p<1000 from published inputs.

## 5. Motives, grt_1 and the exact coefficient issue

In the attached Deligne–Goncharov LaTeX:

- Sec1ccc.tex §1.6 defines MT(O_S) as a subcategory of rational MT(k), with Ext^1(Q(0),Q(n))=K_(2n-1)(k) tensor Q for n>=2, and Ext^2=0.
- Proposition1.7 is the l-adic unramified-realization criterion.
- Proposition1.9(i),(ii) keeps the higher Ext^1 groups and gives vanishing Yoneda Ext^2 for MT(k)_Gamma.
- Sec2ccc.tex Proposition2.3 says the motivic graded Lie algebra is free; §2.4 warns its free generating family is not canonical.

The base ring O_S tells where the motives are unramified. It does not change the rational coefficient field Q into Z or Z_p. Rational Ext^2 vanishing kills torsion and is not an integral vanishing theorem. This is why DG2.3 does not prove the integral Deligne–Ihara statement.

Brown2012 Theorem1.1 and pp949–950 supply the faithful motivic action, hence the rational g_p is free on one odd generator in each weight>=3. In characteristic zero this supplies the expected motivic Lie algebra inside grt_1. Its integral image can be smaller than any natural coefficientwise lattice; an integral model and normalization must be specified before asserting equality.

Current additional source, beyond the attachments: Minoru Hirose, *Confluence relations, Hoffman basis over Z_(2), and the Deligne–Drinfeld conjecture*, arXiv:2610.23719v1 (16Oct2026), Theorem4 and §1.2 p2. It proves spanning of the confluence quotient by Hoffman words over Z_(2) and explicitly derives rational equality of the de Rham mixed-Tate motivic Galois group with GRT. Browser `turn673654050view0`; source https://arxiv.org/pdf/2610.23719; PDF saved work/hirose_2026.pdf. The exact theorem statement and its stated motivic consequence were read. Its entire10-page proof has not been audited in this subsidiary review, and the current task should not relabel that as an independent proof check.

This recent rational identification has no bearing on the counterexample T-37: the coefficientwise associator lattice, a Z_(2)-span of motivic periods, the image of the arithmetic pro-p Galois group, and its Lie lattice are different integral objects. No integral equality follows just because all become the same rational Lie algebra.

Source availability correction: PROGRAM_WARGAME_ROUND2_20261112.md §1.2 contains new rows B13–B16 and amendments B1,B2,B4,B11; it references B3 in a book-level table but does not reproduce the B3 claim. S9 is also only referenced. The detailed original B3 and S9 rows from round1 are absent from the attached ZIP. The prompt itself supplies their intended subject; do not invent a precise line-level locator or pretend to have checked the missing statement.

## 6. Source registry and check classification

L-SHARIFI: Primary author's PDF, locators1.1,1.3,2.3,2.4,eq2.10,3.3,4.1. Statements and the relevant proof paragraphs were read. Full proofs of1.1,1.3,2.3,4.1 were read as literature-use checks; this is not a new independent proof of them.
L-MCS: Primary author's PDF, Thms7.5,9.1,9.7,Prop9.6,Cor8.3,10.5. Statements and proofs of the short9.6/9.7 deduction read; computational7.5 cited, not replicated.
L-BROWN: Primary Annals PDF, intro Conj1,Thm1.1 and its following paragraph pp949–950. Used and rechecked as a cited theorem, not a full proof audit.
L-ISHII-2026: Primary arXiv2312.04196v3,§1 Thm1.1 and Remark1.1.1,p2. Used to verify scope of the kernel theorem.
L-ISHII-SOULE: Primary arXiv2312.04175v2,§1 Thm1.1,p2. Used to verify exact domain and onto equivalence.
L-DG: Attached LaTeX1.6,Prop1.7,Prop1.9,Prop2.3,§2.4. Used and rechecked as rational-coefficient statements.
L-HIROSE-2026: Primary arXiv2610.23719v1,Theorem4,§1.2. Statement inspected; not used for arithmetic conclusions and no full proof audit claimed.
T-KERNEL-REG,T-FACTORIAL,T-37,T-EVEN-GATE: Short deduction proofs above fully read after writing; no fault found, hypotheses checked against original sources. T-PRO2-MOMENT: complete proof in the separate file read in full, with two independent agent audits and parent review; current status checked deduction.

## 7. Next concrete gates and approaches tried

- Kernel irregular: tried applying Vandiver/vanishing to Sharifi regular argument. Gate shrank to the extra even-weight defect; p37 shows this repair cannot give integral free odd generation. The actual remaining kernel condition is N_p=1 and requires comparison of the full ramification group with the image, allowing its irregular relations.
- Kernel2: resolved by the separate Magnus/measure proof `work/pro2_moment_proof.md`, with full self-reading and two independent whole-proof audits. Its extra arithmetic input is the explicit C2*Z2 presentation, with real places treated correctly. This is a checked deduction in this run, not a step17 consequence.
- Integral normalization: resolved by distinguishing full kappa_m from its restriction to F^mG and recording exact factorial equation.
- grt1: updated current rational source and kept it separate from integral arithmetic lattices. No reason to claim step17 promotes any grt1 statement.
