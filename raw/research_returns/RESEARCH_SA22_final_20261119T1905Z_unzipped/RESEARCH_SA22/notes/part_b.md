# Part B and L1: proof record and historical inventory

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `part_b_cycles`, 19 November 2026. No claim of priority. The complete proof text is in `sections/part_b.tex`; this record supplies the argument map, exact scopes, source audit and unresolved requirements. The owned result ledger currently has 56 rows covering 51 numbered statements, with 71 check events. Root owns the global manuscript and checkpoint.

## Inputs read and transcription decisions

All four faces of cote 66 were read from the supplied transcription, with the relevant study and correction rows. The official Montpellier source PDF was opened; all faces 002–005 were inspected, including the disputed words on 003 and 004. Subject 18 reads **artinien**. The Pour mémoire line refers to **SGA 1962**, hence SGA 2. Subject 25 asks whether the product of two algebraically trivial cycles is rationally trivial; on a surface the nontrivial square must be a **divisor square**, since a zero-cycle square has codimension four and is zero for dimension reasons. The adjoining question is whether an Albanese-trivial zero-cycle is rationally trivial.

## Core mathematical results

### B.1(a) and L1: affirmative, with a complete proof

Let X be a smooth projective complex fourfold, h an ample rational divisor class and alpha an algebraic class in H4(X,Q). Its Lefschetz decomposition is

`alpha = a h² + h b + gamma`, where b is primitive of degree two and gamma primitive of degree four.

The scalar a is determined by intersection with h². The inverse of hard Lefschetz L²:H²→H⁶ takes L alpha − a h³ to a rational (1,1)-class b, hence b is a rational divisor class by Lefschetz (1,1). Consequently gamma is also algebraic. Hodge–Riemann gives mutually orthogonal signs +,−,+ on these three summands. If alpha is numerically zero, it can be tested against its own three algebraic components; definiteness forces each to vanish. The reverse implication is cycle-class compatibility with product and trace. This is classical, explicitly recorded in Kleiman 1968 §3.10, not a newly solved standard conjecture.

The arbitrary characteristic-zero-field assertion is also proved, rather than asserted from the complex case. Numerical triviality is unchanged under field extension: spread a complementary cycle to a flat family over an integral finite type parameter, preserve its intersection number under specialization, and specialize to a closed point finite over the original field. Proper pushforward and the projection formula multiply the degree by the finite extension degree. Conversely test against pullbacks. Descent to a finitely generated characteristic-zero field, an embedding into C, and SGA 4 XVI Theorem 4.1/Corollary 1.6 then give all-prime geometric etale equivalence.

Locators: `thm:B1a-betti`, `lem:B-basechange-num`, `thm:B1a-etale`. Opened sources: Kleiman §3.10; Voisin 2010 §2.1 and Theorems 2.10–2.12; SGA4 XVI 1.6 and 4.1.

### B.1(b): the Ancona inference is insufficient; published and preprint conclusions separated

Ancona's numerical Hodge positivity is positivity **after quotienting by numerical equivalence**. It does not itself show that a homological radical is zero. The complete linear-algebra obstruction is diag(1,0): its numerical quotient is positive definite although its original space has a one-dimensional radical. Algebraic Lefschetz decomposition does not remove this defect.

The strongest published all-field conclusion directly established in the opened Ancona paper is equality for **infinitely many primes ell**, Theorem 1.6 = Theorem 3.20. Theorem 3.18 is numerical positivity; Proposition 3.11 and Corollary 3.12 explicitly distinguish the radical and homological semipositivity. Ancona Corollary 3.19 specializes an equality theorem already known on a finite-field fibre; it is not an unconditional all-prime assertion by itself.

The all-prime abelian-fourfold conclusion in this report explicitly uses **Broe's August 2026 preprint**, arXiv:2608.28651v1. Its full PDF and TeX were opened; its entire long proof has not been independently certified. Theorem 1.1 gives Tate on abelian fourfolds over finite fields. Corollary 8.1(i), using Kahn 2003 Theorem 1 p.978, gives rational = numerical with Q coefficients there, hence numerical = ell-adic. Ancona positivity and Corollary 3.19 then pass to arbitrary fields by spreading. Broe records the conclusion as Corollary 1.2 = 8.2. The manuscript title, ledger status and bibliography all mark this new-preprint dependence.

The exact abstract criterion and its scope are proved: algebraic Lefschetz decomposition plus positivity **on homological primitive classes** implies D; a specialization with both D and numerical positivity supplies such positivity upstairs. D descends through a generically finite surjective morphism by projection formula and f_*f^* = degree. Therefore fourfolds dominated in this sense by abelian fourfolds are included, subject to the same explicit preprint input in positive characteristic. No arbitrary-fourfold positive-characteristic assertion is made.

Locators: `prop:B1b-criterion`, `prop:B1b-gap`, `thm:B1b-abelian`, `prop:B1b-scope`.

### B.1(c): complete negative construction

Take two fixed skew lines in P4 and the generic quintic containing them, over the algebraic closure of Q in its 114 independent coefficients. There are 126 quintic monomials and precisely 114 vanish on both lines. The family is nonempty and generically smooth: the specific member

`F0 = x0^4 x2 + x0 x2^4 + x1^4 x3 + x1 x3^4 + x4^5`

contains the two lines and has no projective singular point, as verified by five affine Jacobian Groebner bases equal to [1]. Weak Lefschetz gives Pic(X)=Zh. The difference of the lines therefore has intersection zero with every divisor, so is numerically trivial. Ceresa–Collino 1983 III(3.3), p.290, says the 2875 lines on a generic quintic are independent modulo algebraic equivalence. The incidence of a quintic and an ordered skew pair is integral and dominates the hypersurface parameter space; transitivity of PGL on ordered skew pairs identifies our generic fibre with its generic situation. Any alleged algebraic-equivalence relation, including a nonzero multiple, spreads along a dominant finite-type parameter, contradicting that theorem. Thus numerical does not imply tau (some nonzero multiple algebraically trivial). This is a counterexample over an algebraically closed characteristic-zero field, and via a generic complex embedding over C.

Locator: `thm:B1c`. The computation verifies smoothness and parametrization only; it does not claim to compute the quotient by algebraic equivalence.

### B.2: complete square and Albanese counterexample, independently audited

Let E/Qbar be `y²=x³−x`, origin o, and choose (p,q) a point of E²(C) generic over Qbar. Put S=E² and

`a=pr1*([p]−[o]), b=pr2*([q]−[o]), D=a+b`.

These are algebraically trivial divisors, a²=b²=0, and

`D²=2z`, `z=(p,q)−(p,o)−(o,q)+(o,o)`.

The Albanese image is zero by addition in E². To prove z nontorsion, let f(t)=[t]+[(o,o)] and g(p,q)=[(p,o)]+[(o,q)] in Sym²S. For a nonzero holomorphic two-form omega on S, Mumford's induced form satisfies f*omega^(2)=omega, g*omega^(2)=0. Additivity gives n omega and zero for n f,n g.

Rational equivalence after adding the same auxiliary effective cycle is represented by a rational curve in a larger symmetric product (Mumford Lemma 3 pp.201–202). For each n,e,d the finite type incidence scheme over Qbar is

`W_(n,e,d)={(t,c,h): h(0)=n f(t)+c, h(infinity)=n g(t)+c}`.

Any irreducible component with dense image in S would give a dominant family of such rational equivalences. Resolve its parameter space in characteristic zero. An induced two-form on P1 times this parameter is pulled back from the parameter, so the endpoint forms agree; the auxiliary forms cancel. Pullback of differential forms by a dominant map in characteristic zero is injective. Hence n omega=0, impossible. Every image closure is therefore a proper Qbar-subvariety. A Qbar-generic point avoids all, so no n z vanishes. In particular D² remains nonzero with Q coefficients.

The exact positive replacement is also proved: the kernel of **CH0(S)^0 → Alb(S)** is generated integrally by z(p,q), and rationally by squares D²/2. Expand an arbitrary degree-zero zero-cycle into z terms and cycles on the two axes. Albanese-zero makes each axis divisor principal by Abel's theorem on E.

Independent reviewer `/root/part_c_algebra` found no mathematical flaw. Its suggested explicit incidence formulation has been incorporated. The apparent Bloch source gate is closed: the already opened official publisher excerpt contains printed pp.3–11, including Abel–Jacobi pp.3–4, Albanese universality and factorization Proposition 1.1(ii),(iii) p.10, and T(Y) on p.11. Every Bloch fact used is in those opened pages. The rest of the book has not been opened and is not claimed to have been.

Locators: `lem:B2-mumford`, `thm:B2-square`, `prop:B2-kernel`. Mumford journal year is **1969**, volume9(2),195–204; communication date 28 November1968.

## B.3: all 28 numbered subjects

The status “known with checked deduction” means that the precise theorem stated in the manuscript is supported by opened primary text and its application is checked. It does not claim an independent reproof of an entire foundational book. Broad historical research programmes are given explicit proved formulations; absent definitions or stronger unproved generalizations are identified rather than silently merged into those formulations.

| Subject | Exact proved formulation / outcome | Opened locator | Manuscript statement / scope |
|---|---|---|---|
| 1 | Derived etale-to-fppf comparison; crystalline/de Rham comparison for smooth PD lifts | Stacks 59.100.7–8, 60.17.4, 60.24.11 | `thm:B3-flat-crys`; comparison applies to etale coefficients, not every flat group |
| 2 | Finite-flat local/global duality, all primary parts; sheaf-valued abelian duality | Milne III6.10/8.2; Suzuki2014 A–C and2020 A | `thm:B3-flat-duality`, `thm:B3-abelian-duality`; residue/base fields perfect; global divisible obstruction retained |
| 3 | Equicharacteristic Euler lower bound; explicit failure of rank-plus-local-types equality | Miller2010 Thm1.0.7/Cor3.1.18; independent Cartier calculation; Suzuki above | `thm:B3-pprimary`; characteristic7 curves y²=x³−x and y²=x³−x+1 have same four tame permutation types, different p-ranks; branch positions are not falsely identified |
| 4 | Etale trace/index formulas; finite etale Euler multiplicativity for arbitrary proper schemes | Varshavsky Prop1.2.5/Cor1.2.6; Saito Thm4.9/6.13, Lem4.11(1),(3), eq4.19; curve fibre coefficients have negative Artin conductors | `thm:B3-trace`, `thm:B3-index`; nonproper multiplicativity refuted by Artin–Schreier A1 cover |
| 5 | Ogg–Shafarevich Euler identity in Grothendieck group with operator action retained | Raynaud Bourbaki286 PartI Thm1 p.133, formula(1ter)p.132 | `thm:B3-operators`; ell different from characteristic; no forgotten operator structure |
| 6 | Etale local terms plus explicit holomorphic/elliptic formula | Varshavsky above; Atiyah–Bott1967 ThmA pp.377–378 | `thm:B3-trace`, `thm:B3-holomorphic-lefschetz`; holomorphic isolated nondegenerate denominator derived from Dolbeault |
| 7 | Global duality using cycle complex for separated finite type schemes over number rings | Geisser2010 Thm7.8; Voevodsky Thm6.17 | `thm:B3-arithmetic-duality`; modified real-place compact support specified |
| 8 | Analytic holonomic de Rham/solution duality; connection/crystal comparison separately | Narvaez2004 Thm3.1.1 p.67; Stacks crystalline locators above | `thm:B3-dmodule`, `thm:B3-flat-crys`; shifts and quasi-nilpotence retained |
| 9 | Analytic dualizing complex and topological Serre duality | Ramis–Ruget1970 Thms1–2 pp.81–83 | `thm:B3-analytic-duality`; bounded dimension, countable at infinity, separated cohomology quotients; independent original-page audit corrected the Hausdorffness partner to Ext^(1−q), whereas the dual pairing uses Ext^(−q) |
| 10 | Algebraic and analytic RR beyond projective/smooth case; proper pseudo-coherent/perfect pushforward | Fulton–Gillet1983 RR pp.288–289; Levy1987 RR p.149/§3; Lipman–Neeman2007 Prop2.1/Ex2.2; Toen2012 Thm2.1 | `thm:B3-riemann-roch`; analytic target K-homology; nonnoetherian hypotheses precise |
| 11 | Neron-functor representability via boundedness | BLR1.3 Thm1 | `thm:B3-neron`; “schémas morcelés” has not been matched to a formal category, so the broader categorical heading is not marked settled |
| 12 | Neron models for abelian varieties over DVRs and Dedekind bases | BLR1.3 Thm1/Cor2;1.4 Thm3 | `thm:B3-neron`; Gm finite-type/local-finite-type distinction explicit |
| 13 | Artin–Popescu approximation and Greenberg linear DVR bound | Artin1969 Thm1.10/1.12; Greenberg1966 Thm1/Cor1; Stacks0AH5 | `thm:B3-approx`; no arbitrary-dimensional linear bound |
| 14 | Coherent topoi have enough points; explicit pointless topos; Artin stack criterion | Stacks00YQ,07Y4,07XJ | `thm:B3-topos`, `thm:B3-stacks`; atomless RO(R) proves unrestricted points assertion false |
| 15 | Shape, internal homotopy, fibre LES, internal Hurewicz, profinite complex comparison, infinitesimal example | Lurie6.5.1/7.1.6; Christensen–Scoccola2023 Thm3.12; SGA1XII5.1;SGA4XVI4.1 | `thm:B3-homotopy`; B alpha_p on fppf has infinitesimal pi1, absent on small etale site of reduced A1 |
| 16 | Prime-to-p specialization; explicit failure of full pi1 invariance | SGA1X Thm3.8/Cor3.9 originalp.283 | `thm:B3-specialization`; Legendre lambda=2+t over F3bar[[t]]; “vrai” is not silently identified with etale pi1 or Artin's unpublished example |
| 17 | Exact Pic0 representability/separation criterion for regular proper relative curve over DVR; cohomological-flatness criterion and justified universal H0 | Raynaud Picard1970 6.1.4,8.2.1 pp.66–67; original thesisII1.1–1.3 pp14–15 andIII1.1–1.2 p37 | `thm:B3-picard`, `thm:B3-raynaud-flatness`; perfect residue field, f_*O=O, gcd geometric multiplicities1; exactW for the flatness criterion |
| 18 | Affine fpqc descent, algebraic-space quotients, failure of unrestricted schematic descent; effective finite locally free artinian quotient | Stacks0245,02WW,08KE,03BM,03JE,07S6 | `thm:B3-descent`, `thm:B3-artinian`; free equivalence relation, not nonfree quotient with stabilizers |
| 19 | Distinct higher-cycle positive cones and degree norm | Fulger–Lehmann2017 Thms1.3/1.4/1.7/1.8 | `thm:B3-positive-cones`; PL,BPF,Upsef,Nef not falsely equated |
| 20 | All-characteristic Schubert/dominant-line-bundle vanishing | Brion–Kumar2005 Thm3.1.1(a),(b) | `thm:B3-homogeneous`; complete G/P/Schubert scope |
| 21 | Universal H0 characterization iff henselian pair iff all-degree restriction; completion-complement rigidity | Opened original Gabber1994 Theorem1 p326 and condition(b) p325; Stacks59.82.7 tag09ZI/15.11.6 tag09XI; HHW2024 Cor2.34/2.36; Bhatt–Mathew2021 Thm6.11/Rem6.12; FujiwaraCor6.6.4 not opened | `thm:B3-21`, `thm:B3-fujiwara`; theorems established; Gabber original requirement discharged, Fujiwara original access unresolved |
| 22 | Neutral/nonneutral Tannaka; intrinsic char0 criterion; super-line obstruction | Deligne–Milne2.11/3.2; Deligne1990 1.12/1.13/7.1 | `thm:B3-tannaka`, `thm:B3-nonneutral`; groupoids/gerbes and possible lack of k-fibre functor retained |
| 23 | Rational Chow pullback with regular target alone over finite type arithmetic schemes | Weber2015 Def4.1.12,Thm4.2.1,Cor4.2.3 pp.37–39 | `thm:B3-chow-pullback`; arbitrary X, not necessarily regular/lci; Q coefficients retained |
| 24 | Both questions answered: threefold numerical/tau false, characteristic-zero fourfold numerical/homological true | Kleiman§3.10; Ceresa–CollinoIII(3.3); Ancona/Broe distinctions above | B.1(a)–(c) |
| 25 | Both implications false by complete E² construction; exact Albanese-kernel generating result | Mumford1969 §1,Lemmas2–3; Bloch excerptpp.3–11 | B.2 |
| 26 | Relative generalized Jacobian universal factorization over arbitrary base under explicit curve hypotheses | Contou–Carrere1979 Thm1.4 p.204 | `thm:B3-rosenlicht`; all degree components and inverse limit retained |
| 27 | Higher adele resolution plus local formal Jacobian universal property | Braunling–Groechenig–Wolfson2016 Thm2.1/0.2; Contou–Carrere2013 1.4.4/1.6.6 | `thm:B3-adeles`; noetherian hypotheses; local “ombre” mediates morphisms, not an invented literal U→loop-group map |
| 28 | Rational triangulated motives, constructible six functors and duality | Cisinski–Deglise2019 14.2.9/15.2.1/15.2.4 | `thm:B3-motives`; no abelian mixed-motive category or motivic t-structure asserted |

## B.3: all nine Pour mémoire headings

For ILO, all page numbers in the manuscript refer to the **fully opened 2012 author version**, arXiv1207.3648v1, of the work published as Astérisque363–364 (2014). Chapter/theorem locators are always given. Published metadata/chapter ranges were separately opened. The published volume's complete PDF has not been opened.

| Heading | Precisely established result | Exact locator | Limit retained |
|---|---|---|---|
| Resolution | Functorial strong resolution of generically reduced noetherian qe Q-schemes; prime-to-ell alterations over arbitrary fields | Temkin2012 Thm1.2.1; ILO IntroductionThm3(1),X2.1 | Alteration is not a birational resolution in arbitrary characteristic |
| Purity | Ri!Z/n=Z/n(−c)[−2c] for regular immersion between regular noetherian schemes | ILOXVI3.1.1,authorp.242 | n invertible, both schemes regular |
| Regular base change | qcqs direct image commutes with regular noetherian base change | ILOXIV2.5.3,authorpp.216–217 | n invertible; regular map need not finite type |
| Local duality/biduality | Normalized potential dualizing complex; constructible biduality | ILOXVII5.1.1/6.1.1,authorpp.287,293–294 | Dimension function; finite quasi-injective dimension iff finite Krull dimension |
| Finite type finiteness | Rf_* preserves bounded constructible torsion over noetherian qe base | ILOXIII1.1.1/1.1.2,authorp.195 | n invertible; properness and finite Krull dimension unnecessary |
| Affine cohomological dimension | Relative support-dimension inequality; absolute vanishing above affine dimension | ILOXV1.1.2/1.2.2,authorp.219 | Not a fibre-dimension-only bound |
| Grauert finiteness | Proper holomorphic coherent direct images coherent | Grauert1960 §6 HauptsatzI p.59;1963 correctionpp.35–36 | Technical correction read; incorrect closed-locus claim not used |
| Rigid analytic theories | Tate/Kiehl acyclicity, coherent modules, proper mapping, Raynaud formal-model equivalence | Bosch2014 4.3/10–11,6.1/4,6.3/9,8.4/3 | Complete rank-one field; quasi-separated/quasi-paracompact equivalence |
| Questions in SGA1962 | Explicit counterexample to XIII1.1; XI3.13(ii)/3.14 parafactoriality/factoriality | SGA2 originalpp.173–174 and132; independent toric Cech proof | The whole volume is not labelled affirmatively solved |

The SGA2 counterexample is fully verified: for A=k[u,v,x,y], R=A/(ux−vy), I=(u,v), the classes e_n=x^n/(uv^(n+1)) in H²_I(R)=R_uv/(R_u+R_v) are all killed by u,v,x,y. Under u=ac,v=ad,x=bd,y=bc they are distinct monomials a^(−n−2)b^n c^(−1)d^(−1). Every R_u monomial has d-exponent≥0 and every R_v monomial c-exponent≥0; hence the e_n are linearly independent. The I-annihilator has infinite-dimensional maximal-ideal socle and cannot be finite over the noetherian ring A. This supplies a complete refutation without depending on a name-only reference to Hartshorne. The original article is now opened: `sources/hartshorne1970.pdf`, §3 pp.149–151, uses A=k[x,y][[u,v]], M=A/(xu+yv). Its scanned pages are saved as `qa/hartshorne1970_p149.png` through p151. Our polynomial variant needs no unproved completion comparison.

## Subject21: exact theorem and source gate

For an arbitrary pair (A,I), restriction H0(Spec A,F)→H0(Spec A/I,F) for **every** torsion etale abelian sheaf is equivalent to henselianity. Necessity tests finite maps Spec B→Spec A and the sheaves f_*Z/2: sections distinguish idempotents, and bijective idempotent lifting for every finite B is the henselian-pair criterion. Gabber then gives all-degree restriction. Complete I-adic pairs are henselian. A fixed single-sheaf reading is false: Gm and its point1 have equal H0 for Z/n but unequal H1.

For a henselian pair with finitely generated I, Fujiwara–Gabber rigidity compares cohomology on an open containing Spec A minus V(I) with its inverse image in the I-adic completion. This is a different operation from restricting the affine scheme to its closed fibre. HHW2024 Notation2.33, Cor2.34/2.36, Remark2.37 give precisely these statements and the exact original locators: Gabber1994 **§5 Corollary1**, Fujiwara1995 **Corollary6.6.4**.

**Unresolved source requirement:** the original complete Gabber1994 and Fujiwara1995 texts have not been opened. Our bounded retrieval and the independent audit found no functioning lawful full text. Springer explicitly marks Gabber subscription-only and supplies no SharedIt link. The current Fujiwara download is an Incapsula anti-bot response; the publicly archived2020 landing page was subsequently opened and explicitly denies full-text access without subscription. Crossref/OpenAlex/SemanticScholar yield no alternate original; OpenAIRE marks Fujiwara OPEN but merely repeats the same Euclid location. HAL finds neither DOI; Fatcat returns503. Public archive metadata marks the exact Duke issue files private, so those files were not requested; the CDX PDF query returns no snapshot. All attempts, URLs, response evidence and request runtimes are recorded in `notes/part_b_source_followup_20261119.md` and its named JSON manifests. The bibliography says **not opened** for both originals. This is a source-access gate, not a claim that the mathematics is unresolved. The unrestricted affine theorem uses the complete opened Stacks proof; the manuscript does not infer the original Gabber article's exact hypotheses from its abstract, or claim to have independently re-proved the original deep theorem. No login, paywall, archive or anti-bot restriction was bypassed.

The complete Bhatt–Mathew author version v4 of **The arc-topology**, published Duke Math.J.170(2021),1899–1988, was also opened. Theorem5.4 proves torsion etale arc descent; Theorem6.4 gives the formal-glueing homotopy-cartesian square; Corollary6.10 and Theorem6.11 (authorp.50) derive completion-complement rigidity from affine rigidity. The manuscript now spells out that deduction. Remark6.12 states that Fujiwara1995 assumed noetherianity and credits the nonnoetherian extension to Gabber (ILOXX§4.4). This closes the modern proof's previously implicit intermediate citation; it does **not** falsely mark the two original articles as opened.

## Reproducible checks and audit

`code/part_b_finite_checks.py` (output JSON saved) checks 126/114 quintic monomials, line containment, five projective Jacobian charts, D²=2ab modulo a²=b²=0, diag(1,0) radical, characteristic3 Legendre Hasse coefficient −t, characteristic7 Hasse coefficient3b and discriminants3/2, and symbolic toric socle identities for arbitrary n. The mathematical proof of generic Chow nonvanishing is geometric, not computational.

The structural audit currently finds **no missing bibliography key, duplicate label, unmapped numbered statement, or missing internal cross-reference**: 60 bibliography entries, 51 numbered statements, 56 result rows. Parent compiles and visually verifies the assembled paper. The two reported PartB overflow issues were corrected by a breakable path and a displayed duality identity; bold relative cohomology symbols were replaced by underlined Gamma/mathcal H to remove font fallbacks.

## Source trail and useful web reference IDs

Every bibliography entry in `sources/part_b.bib` has an opened/not-opened note and exact locators. Full PDFs and extracted text actually used are saved in `sources/`; fetch scripts and manifests record URLs, hashes, rejected non-PDF responses and elapsed time. The mistakenly recalled Saito arXiv identifier that led to a physics PDF was rejected before use and preserved under `rejected_arxiv_1402.6482.*`; the correct opened paper is1510.03018.

Parent must itself open a URL before citing a child source in final chat. Useful references from this branch:

- Ancona fullHTML https://arxiv.org/html/1806.03216v3 — `turn969924609view0`; full TeX `sources/ancona/fourfolds_2020.tex`.
- Broe metadata https://arxiv.org/abs/2608.28651 — `turn969924609academia7`; full PDF and TeX downloaded in this run.
- Kahn fullPDF https://numdam.org/item/10.1016/j.ansens.2003.02.002.pdf — `turn621079566view1`.
- Mumford fullPDF https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969e--0-cycles-Euclid.pdf — `turn873723994view2`, `turn167805125view1`.
- Bloch official excerpt https://assets.cambridge.org/97805211/18422/excerpt/9780521118422_excerpt.pdf — reopened `turn871609320view3`, independently `turn766539130view1`.
- Narvaez completePDF https://www.maths.tcd.ie/EMIS/journals/SC/2004/8/pdf/smf_sem-cong_8_59-87.pdf — `turn653953667view3`.
- Levy completePDF https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6397-11511_2006_Article_BF02392258.pdf — `turn482047991view1`.
- Lipman–Neeman authorPDF https://www.math.purdue.edu/~jlipman/papers/quasiperfect.pdf — `turn871609320view2`.
- HTT authorPDF https://people.math.harvard.edu/~lurie/papers/HTT.pdf — `turn871609320view0`.
- Christensen–Scoccola https://arxiv.org/abs/2007.05833 — `turn871609320view1`; fullv3 PDF locally opened.
- Weber fullPDF https://epub.uni-regensburg.de/31887/1/Dissertation%20Andreas%20Weber.pdf — `turn446941844view1`.
- Temkin metadata https://arxiv.org/abs/0904.1592 — `turn410598363view2`; full final author PDF locally opened.
- Grauert1963 completecorrection https://www.numdam.org/item/10.1007/BF02684291.pdf — `turn446941844view3`.
- ILO publishedmetadata https://www.numdam.org/issues/AST_2014__363-364_/ — `turn410598363view0`; chaptermetadata `turn134133433view0`–`view5`. Full opened authorversion is1207.3648v1.
- Gabber officialpaywall https://link.springer.com/article/10.1007/BF02773001 — independent reviewer `turn274609710view2`.

- Bhatt–Mathew fullPDF https://arxiv.org/pdf/1807.04725 — `turn760234705view1`; v4 dated14December2020, authorpp.38,48–51 opened.
- Hartshorne original volume https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0009/PPN356556735_0009.pdf — `turn760234705search12`; full volume downloaded, articlepp.145–164 extracted, §3pp.149–151 visually opened.

The machine-readable **37-row raw historical inventory** is `checks/part_b_inventory.tsv`, generated by `code/part_b_inventory.py`. Exact fragment line locators and corrections are also collected in `notes/part_b_audit_addendum.md`; mathematical labels remain stable even when line numbers shift. The generator must be re-run after edits.

## Exact inherited input IDs

The actual attached `inputs/RESEARCH_SA22_study/study/CHECK_EVENTS.tsv` contains one SA22-0 event, at line92: **SA22-0 (66/004, subject 24, second question)**. A new verification event retains that exact ID and maps it to `thm:B1a-betti` and `thm:B1a-etale`; the raw lead ID **L1** also remains in the owned events. The attached `CORRECTIONS.tsv` line53 is separately checked: its characteristic-zero correction is justified by those full proofs.

There are no subject21 or subject25 events in the attached CHECK_EVENTS table. New checks under **SA22-0 (66/004, subject 21)** and **SA22-0 (66/005, subject 25)** therefore explicitly say they are newly generated checks of the attached study/promptR9, not copied inherited event IDs. Their proof mappings are `thm:B3-21`/`thm:B3-fujiwara` and `thm:B2-square`/`prop:B2-kernel` respectively.

Kleiman1994's full original chapter was subsequently opened from Mainz University; original printedpp.16–18 visually read. Proposition4-3(2)(c),p.16 establishes B for abelian varieties. Section5 and Proposition5-1,pp.16–17 explicitly use positivity on algebraic cohomology classes and derive D from A(X,L). Both precise locators are now included in the manuscript, without treating Ancona's numerical positivity as that stronger hypothesis. PDF: `sources/kleiman1994.pdf`; images `qa/kleiman1994_pdf14.png`–`pdf16.png`; webref `turn239821777view0`.


## Literal named-original audit after checkpoint03

The task also requests the actual named source files. Complete available copies of SGA4,4half,5and6 have now been fetched, with the exact bounded passages read listed in their separate bibliography notes and the source follow-up. Toën2012 is not treated as originalSGA6. Four named originals remain reading requirements: Gabber1994, Fujiwara1995, Lieberman1968 and Raynaud's published thesis LNM119(1970). The first two have separate mathematical proofs and exact locators supplied through opened modern primary sources; Lieberman's actual use is supplied by opened Kleiman originals; the thesis is not needed to justify a theorem here but remains a literal requested-source gate.

Raynaud's title is *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Paris thesis1968, published1970. Original publisher front matter, contents and institutional thesis identity have been opened; mathematical text has not. This is distinct from the opened Picard1970 article and from LNM169. InternetArchive metadata marks the PDF/OCR private; the public CERN lead returns an Anubis challenge. No restricted content or challenge bypass was attempted. Precise statuses and durations are retained in the dedicated source/program records.

## B.1(b): exact method domain and certified geometric members

The independently reviewed `prop:B1b-criterion` gives the exact conditional domain of the componentwise-definiteness argument: the Lefschetz projections preserve algebraic classes and the signed primitive pairing on homological algebraic classes is positive definite. The criterion's converse under numerical positivity identifies precisely the remaining radical obstruction. Numerical positivity alone does not verify the stronger hypothesis. This answers the requested scope of the specified argument without inventing a further requirement to classify all fourfolds up to isomorphism.

The independently audited fragment `sections/part_b1b_class.tex` is now included before B.1(c). It adds three proved statements: transfer through algebraic-correspondence factorizations of the identity on H4 (`B1b-correspondence`); invariance under blowups along positive-codimension smooth centers (`B1b-blowup`); and numerical–homological equality in every codimension for Fermat cubic fourfolds and their geometric forms in every characteristic other than3 and every invertible prime (`B1b-fermat`). The last uses an explicit generically degree3 map from Bl_(E×E)(S×S), a complete seven-line Gram certificate on the Fermat cubic surface, and the descending-Gysin blowup argument. The original Shioda–Katsura construction and cohomology formulas have been read directly. No recent preprint is required for the Fermat result; the abelian all-prime seed retains its explicit Broe2026 dependency.

These yield substantial certified geometric membership: abelian and Fermat seeds, geometric forms, correspondence retractions, generically finite images, smooth-center blowup constructions, and actual specializations satisfying `prop:B1b-scope`. The exact intrinsic method criterion is complete; the examples are not presented as an exhaustive list of all geometric members. Ancona's original PropositionA.9 and RemarkA.10 were reopened, including the Fermat positivity proof and rank-two limitation. A.9 now supplies numerical positivity after D for this exact Fermat variety has separately been proved, so no circular inference from numerical positivity is used. Exact source lines2036–2058; web refs `turn130022901view0`/`turn130022901view1`, https://arxiv.org/html/1806.03216v3.

Independent proof audit and source details are in `notes/part_b1b_class_secondary_audit.md`; the author's detailed proof and program record is `notes/part_b1b_class_secondary.md`. The additional finite program checked27 lines and351 pairs over F4, with rank7 and selected determinant1 in0.02672153499952401seconds. Characteristic independence is proved by the displayed cube-root equations, not inferred from that finite computation. The owned PartB structural audit still counts51 statements in its main fragment; the included C fragment adds3, for54 numbered statements in the combined PartB text, with its own result/event records.


## Named Raynaud thesis: relevant original source gate closed,15:03UTC

Original LNM119 pp14–15 and37–38 have been fetched through the publisher's explicitly advertised public previews and visually read independently by this agent and root. The exact propertyW and its base-change compatibility are LemmasII1.1–II1.2/DefinitionII1.3; complete LemmaIII1.1 and DefinitionIII1.2 provide the cohomological-flatness criterion. `thm:B3-raynaud-flatness` gives a complete proof, replacing its cited local lemmaII2.9 by the explicit dual-basis/matrix argument. The strengthened `thm:B3-picard` first obtains cohomological flatness from the already opened PicardarticleTheorem8.2.1(iv) afterdelta=1, then Q is locally free and Qdual=O impliesQ=O, yielding universalH0=O. The bare fixed-base equality alone is not used to discard torsion. Full detailed proof/source boundaries are in `notes/part_b_raynaud_thesis_derivation.md`. The named-source requirement concerns these relevant original passages and their derivation, not an invented requirement to read every page of the book. Historical source-search records and the distinct p175retyping remain preserved.


## Gabber original main theorem now opened, 15:15UTC

Original publisherpp325–326 contain the exact arbitrary-ring/ideal definition and Theorem1 for every torsion abelian étale sheaf and everyq≥0. Both pages were visually read, and the original theorem plus condition(b) now supply the direct source derivation in `thm:B3-21`. The parent independently checked the original images and the converse. The later§5Corollary1 and full original proof are not claimed opened; their reading is not an additional requirement when the actual main theorem supplies the needed statement. The full Stacks proof remains separately opened. Exact retrieval, hypothesis and deduction records: `notes/part_b_gabber_original_derivation.md`. The remaining owned-area named-original requirements are Fujiwara1995 and Lieberman1968, each assigned to its continuing source audit.
