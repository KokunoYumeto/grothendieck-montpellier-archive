# P2: duality, Roos topoi, reused analytic sheets, and arithmetic monodromy

Review date: **19 November 2026**. Reviewer: **GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p2**.

## 1. Coverage and the order of the papers

This shard covers every one of the **113 indexed Pro entries** in `MPL_33_147-181+34_002-017`, all **1,418 lines** of its transcription, its full doubts register, and all four supplementary Codex folders **K34-01–K34-04**, comprising **1,605 transcription lines** and their accompanying notes. Codex supplies claims and questions but receives no note-verdict rows. Every verdict was made by reading the actual passage. Scripts format these judgments, check literal anchors and carry out specified computations; they do not infer verdicts from headings or keywords.

The sequence has distinct authorship layers. Grothendieck's handwritten work at33:148–160 continues the Verdier-pairing and trace discussion at33:144–146. His programme at33:165–180 develops coefficient rings, biduality, uniform Ext bounds and support spectral sequences. Interleaved reused leaves contain Jan-Erik Roos's topos exposé, EVT revision sheets labelled *Tribu no.63*, English regular-local/quadratic-transform lemmas, and printed singular-operator calculations. None of the anonymous printed mathematics is automatically attributed to Grothendieck.

Cote34 begins an arithmetic-monodromy exposé. The Pro portion ends at the central tame quotient. Codex continues with the arithmetic theorem, geometric and compatibility questions, reductions through models and curves, and geometric fundamental-group coinvariants, abelian schemes, CM and semisimplicity. A proposition left blank at34:051 has a related curve argument at34:070–082; a claim announced near34:053 has its finite-field proof later. A cancelled draft at34:049 is replaced at34:050 with a stronger resolution hypothesis.

There are **121 items,142 claims,49 problems,82 scan questions and86 links**. The items comprise108 original Pro source objects and13 Codex-only objects; the latter create no additional verdict rows. Entry verdicts:107 kept, five merged, one corrected. Claim classes:A27,B12,C20,D0,E67,F16. Page statuses:proof sketched52; proved there17; stated without proof25; open on the pages33; false as stated14; corrected by himself later1. ClassF means the exact proposition/source/context is not identifiable; it does not announce an open modern conjecture. NoD label was assigned merely because a search failed. The final publication-scope check downgrades C203–204 to classC for their explicit Proposition4.4 collation gap; the recovered common-completion lemma C157 is classE and joins canonical C064 in assembly.

## 2. What changes in the earlier notes

The Pro notes are generally appropriately cautious: local pairing versus proper global trace; constructible versus unrestricted duality; internal versus global Ext; and project registers versus demonstrated results. The Fermat-quartic and purity tests belong to the earlier run and are independently checked here. The principal corrected item is connectedness in the group-cohomology/Tate-module comparison: finite components disappear in the inverse-limit Tate module but still contribute copies to H¹ of a disconnected group. Five duplicate entries are merged. Title lists and bibliography remain documentary items.

The claim map adds subsidiary propositions absent from the notes, especially Codex algebraic-envelope lemmas, the curve coinvariant proof, the finite-field refinement, and elementary assertions on the EVT leaves. The cap exercise receives a distinct unresolved record because its definition is missing.

The most consequential findings are:

* All-Dᵇ biduality fails already at a point; bounded constructible biduality is a different theorem (C107/C106).
* Global Ext≤2dim fails over a finite field; an internal/geometric-local statement has a valid dualizing-complex formulation (C111/C112).
* Ordinary codimension in the support estimate fails a smooth-curve purity test (C116).
* Finite étale completion equivalence for a henselian discretely valued field does not require the deleted excellence assumption (C147; SGA4X2.2.1).
* The Codex expressions T^n−1, finite-group vanishing in degree0, unique splittings, and an asserted radical-abelianization isogeny fail elementary tests (C172,175,176,181).
* A finite extension giving isotriviality cannot always be restricted to an extension of constants (C206).
* For ell=p, good reduction does not imply inertia semisimplicity. The published SGA7 criterion uses Barsotti–Tate reduction (C214).
* Original SGA7I3.7 gives echelon2 for H¹ of every finite-type scheme, stronger than the draft general bound3. Theorem3.5 itself is the smooth-projective-curve case (C228).

Where the ink may explain a failed formula, it remains a scan question. The transcription is unchanged.

## 3. Published outcomes and identification limits

### Duality and trace

The verified modern scope uses invertible finite coefficients and bounded constructible complexes, adding finite Tor dimension when the tensor/trace argument needs it. ILO2014 XVII0.2 and6.1.1 gives excellent-scheme duality; XVII2.1.2 fixes normalization and6.2.4.1 computes quasi-injective dimension. These do not settle an unspecified unbounded category or arbitrary coefficient-ring sheaf. Constructible approximation preserving injective stalks and incomplete polygon inequalities remain questions about the exact manuscript formulation.

Illusie's firsthand chronology distinguishes the1965–1966 seminar, drafting in the first half of1966, later finiteness input and1977 publication. Trace compatibility was a real earlier obligation. SGA4XVII's introduction dates Deligne's redaction to1968–1969 and says it partly used Grothendieck's notes. These identify a source family, not these exact leaves. The original Bourbaki279 dates its talk **December1964**, while the collected volume is dated1966; this distinction is retained despite a later historical sentence using1966. [Illusie2026,I.2–4; SGA4XVII,introduction; Bourbaki279,p41.]

The counit is Ru_!u!→id. A displayed Ru_* needs properness or a proper-support argument (C123; Stacks0G2B). Stacks03TI, Proposition64.10.2, verifies homotopy-independent alternating trace for perfect complexes. Merely finite flat terms in an unbounded complex do not provide a finite supertrace (C125).

### Roos and reused texts

SGA4VII expressly credits three oral Roos exposés; its small/big étale comparison is4.1. The stronger draft minimum-topos axioms and deferred representable local-isomorphism criterion are not equated with that published theorem. The Zariski retraction is separately matched with Stacks020Z; the Jacobson closed-point comparison with Stacks005T.

The *Tribu63* heading makes Bourbaki editorial material the relevant EVT lead. Both its official catalogue and the separate Grothendieck EVT bibliography were opened; neither identifies the cropped revision edition. Complete enough mathematical statements receive proofs below; absent definitions remainF. The Abhyankar-style and operator sheets likewise remain unattributed beyond their visible source families. Exact-phrase, theorem-number and backward-reference searches are logged. An unrelated theorem4.5.4 hit was rejected.

### Monodromy and semisimplicity

Illusie1994 Theorems1.2 and1.4 separates arithmetic monodromy, with cyclotomic-infinity hypothesis, from geometric cohomological quasi-unipotence over a henselian trait;1.5 gives the nilpotent operator. The notebook's conditional resolution method is not a proof of resolution in positive or mixed characteristic.

Handwritten “ExposéII” on geometric coinvariants is not identified with SGA7II by numbering. The printed exposé is Michèle Raynaud's finite-presentation text. Its original introduction proves the surface case and states a general conditional result. The handwritten coinvariant argument is checked on its own later pages: normalization and a generic curve, then proper-curve and boundary calculations, with an almost-all-primes refinement (C199–225).

Geometric semisimplicity is matched exactly with Deligne's *WeilII*, Corollary3.4.13,p210, for smooth proper direct images on a normal geometric base. Earlier3.4.1(iii) has finite-field purity hypotheses. Faltings's original1983 introduction states number-field semisimplicity and the endomorphism theorem needed for CM: a solvable connected reductive image is a torus, and its commutant supplies a CM algebra. Grothendieck1966 Proposition4.4 is a real manuscript citation with opened publication metadata, but its full text was not collated. [DeligneWeilII3.4.13; Faltings1983§1(a),(b); MilneCM3.3.]

Degreewise trace and common-Q-model questions are not settled by alternating trace theorems. Kato2019 AppendixA by Lu–Zheng concerns alternating traces; a rational character need not be realizable over Q. The2026 Ito–Zou author preprint proves arithmetic semisimplicity and weight–monodromy in its **hyper-Kähler** scope. Its6October2026 date and restricted quantifiers are retained; no general solution is inferred. [Kato2019,A.1–A.2; ItoZou2026,2.5,4.4.]

## 4. Counterexamples and reconstruction checks

### Biduality, Ext and injective stalks

Let V be the countable direct sum of F_ell. Its algebraic dual is the countable product. A nonzero functional on the quotient of that product by its finite-support subspace gives a member of V** vanishing on every finite-support vector but not zero. It cannot be evaluation by V: testing coordinate vectors forces every coefficient to vanish. Thus V→V** is not onto. Finite-dimensional/constructible biduality is unaffected (C107).

Take X=Spec F7, Lambda=F3, F=Lambda. Since mu3 is constant, Kummer gives

\[
\operatorname{Ext}^1_X(\Lambda,\Lambda)=H^1(X,\Lambda)
\cong\mathbf F_7^\times/(\mathbf F_7^\times)^3\ne0.
\]

The quotient has three elements, dimX=0, and every geometric stalk is injective as a Lambda-module. The program enumerates cubes. This tests global Ext only (C111). For a closed point i on a smooth curve over an algebraically closed field, purity gives Ri!Lambda=Lambda(−1)[−2], hence internal Ext²(i_*Lambda,Lambda)=i_*Lambda(−1). Its support has codimension1, contradicting ordinary codimension≥2. A shifted or doubled convention is not refuted (C116; Milne16.7).

The arrow-category extension

\[
0\to(0\to k)\to(k\xrightarrow{1}k)\to(k\to0)\to0
\]

does not split, although every stalk is an injective vector space. A section would have components1 and0, violating arrow compatibility. This disproves “injective stalks imply injective sheaf,” not the precise approximation question (C114).

### Universal Picard assertion

The complex Fermat quartic sum x_j⁴=0 contains the line x0=ax1,x2=bx3 when a⁴=b⁴=−1. Its gradient has no projective zero. If its Picard group were generated by the hyperplane class H, the line class would be mH, forcing 1=H·L=mH²=4m. The executable substitution verifies the line. The very-general theorem is not the universal assertion at34:005–006. Ji's opened abstract supplies a modern comparison with separate degree/torsion restrictions (C141).

### Algebraic-envelope errors

The identity2 has characteristic polynomial (T−1)², not T²−1. Averaging for a finite group in characteristic0 kills positive-degree cohomology, not H0. In Ga semidirect C2 with inversion action, every(a,−1) has order2 and gives a different complement; conjugation by(a/2,1) relates them. H¹-vanishing means conjugacy, not uniqueness (C172,175,176).

Let H=SL2 semidirect Ga² with its standard action. Its radical is R=Ga². Since SL2 is perfect and its commutators with the standard module span that module, H is perfect. Thus R/[R,R]→H/[H,H] is Ga²→0, not an isogeny. The torus-quotient part of a corrected solvable argument may survive, but the written general-isogeny step does not (C181).

For invariants versus coinvariants use A=diag(2,1) and B=((1,1),(0,1)) on Q². Common invariants vanish; images of A−1 and B−1 span only the first coordinate, leaving a one-dimensional coinvariant quotient. This is a logical linear-algebra test, not a claimed realization by the specific local abelian variety suggested on the page (C222).

### A constant extension does not remove every twist

Over Q(t), E:y²=x³−t²x has discriminant64t⁶. Under t=u²,x=u²X,y=u³Y it becomes Y²=X³−X, a constant CM elliptic curve. Its Tate action is potentially abelian. A finite extension of Q cannot make t a square because its t-adic valuation remains odd. Geometric inertia acts by−1 on H¹; this is impossible for a constant abelian variety and persists under an isogeny of rational Tate modules. In characteristic0 a radicial isogeny is an isomorphism. The finite extension used in the proof therefore cannot universally be replaced by a constant extension (C206). The same involution has trace−2, refuting the “natural integer” trace wording (C186).

### Good reduction with nonsplit p-adic inertia

Set R=W(Fbar5), K=FracR. This is a complete DVR field of characteristic0 with algebraically closed residue field. Choose an ordinary elliptic curve over that residue field and bases of its étale Tate module and its dual. Katz's Serre–Tate Theorem2.1 supplies compatible infinitesimal deformations with q=1+5; the polarization condition is automatic in dimension1. Algebraization of compatible polarized formal abelian schemes gives an elliptic scheme over R, hence good reduction.

Its connected–étale Tate extension is

\[
0\longrightarrow\mathbf Z_5(1)\longrightarrow T_5(E)
\longrightarrow\mathbf Z_5\longrightarrow0,
\]

with Kummer class q, by Katz's extension construction. The5-adic logarithm has v5(logq)=1. If q^(5^m) had a5^n-th root in K, that root would be a unit reducing to1 and hence lie in1+5R. Its logarithm would have valuation m+1−n, impossible when n>m since log(1+5R) lies in5R. Consequently no5-power multiple kills the Kummer class; its rational extension is nonsplit. The residue field is algebraically closed, so GK=I. Thus V5(E)|I is not semisimple despite good reduction (C214).

This is the manuscript's general henselian-trait setting; K is not claimed to be finite over Q5. Original SGA7IX5.12.1 restricts the ordinary-inertia translation to ell≠p. Its5.13 includes ell=p through Barsotti–Tate good reduction, which the example satisfies. Brinon–Conrad8.3.6–8.3.7 describes compatible nonsplit crystalline phenomena.

## 5. Elementary mathematics on reused sheets

### Extreme points and supporting functionals

For affine u:C→C′, let x be extreme in C′ and y extreme in u⁻¹(x). Any convex decomposition of y maps to one of x, so both images equal x; fibre extremality then makes the decomposition trivial (C150). Equivalently, x is extreme in A precisely when A minus{x} is convex (C232).

For compact convex A and extreme x, slices containing x form a neighbourhood basis. Given a neighbourhood U of x, cover compact A minus U by finitely many closed halfspaces avoiding x. Intersect them with A. The convex hull of their finite union is compact and cannot contain x, by extremality. Separating x from that hull gives a slice contained in U. A compact K missing x therefore misses a slice and cannot have closed convex hull A. Compactness matters: a dense nonclosed set can omit x (C233). No cap variant is inferred without the source definition (C241).

For the supporting-hyperplane warning let H=ell² and G=span{e0+en/n:n≥1}. G is norm dense: its generators converge to e0 and then all en lie in its closure; but e0 is not a finite linear combination of them. The topology sigma(H,G) is Hausdorff. The norm unit ball remains compact as the continuous image of a weakly compact set into a Hausdorff weaker topology. A continuous supporting functional at e0 must be a nonzero multiple of e0, by the equality case of Cauchy–Schwarz. No such functional is in G. Thus no continuous supporting hyperplane exists there. This checks the warning without inventing the absent old conjecture (C151).

### Locally convex sums and completeness

The direct sum E=sum E_i has the finest locally convex topology making each inclusion continuous. Outgoing continuous linear maps are exactly families with continuous restrictions. The quotient by transition relations represents the inductive limit; in the Hausdorff category take their closure. The product map is continuous, and sum G_i equals the intersection of inverse images of G_i under coordinate projections, hence is closed if all G_i are closed (C153,238,239).

For completeness suppose each E_i is Hausdorff complete. Every continuous seminorm p on E is dominated by q(x)=sum p(x_i), which is continuous. More generally, for continuous coordinate seminorms q_i, the map to the Banach ell¹-sum of completed E_i/kerq_i is continuous and extends to the completion of E. Each coordinate of a completion point z belongs to E_i. If infinitely many coordinates were nonzero, choose countably many and seminorms q_i with q_i(z_i)≥1. Its extended ell¹-image would have divergent norm, impossible. Thus z has finite support. Subtract that element of E: the remainder has zero coordinates and therefore zero image for every such q; those dominate all continuous seminorms, so Hausdorffness forces zero. E is complete (C154). This does not assume that every Cauchy net's entire range is bounded.

The compact-piece criterion at33:157 needs its ambient quantifier: a fixed closed zero-neighbourhood V has (x+V) intersect C contained in some compact C_n for every ambient x. Near a closure point the same compact piece traps C, giving closedness and local compactness. A Cauchy filter eventually lies in one such compact piece and converges (C235).

### Gegenbauer integrals

In the standard convention, for lambda>−1/2 and C_n^lambda(t)=sum a_d t^d, substitution u=t² gives

\[
I_n=\frac12\sum_d a_d B\left(\frac{d+1}{2},\lambda+\frac12\right),
\]

\[
J_n=\frac14\sum_d a_d B\left(\frac{d+1}{2},\lambda+\frac12\right)
\left[\psi\left(\frac{d+1}{2}\right)-\psi\left(\frac{d+1}{2}+\lambda+\frac12\right)\right].
\]

I integrates C_n against (1−t²)^(lambda−1/2) on[0,1]; J additionally includes logt. The program checks parity and exact examples at lambda=1/2,3/2 and n=0,…,5. The general derivation is elementary, but these samples do not certify the printed w_p, missing reference[18a], or original gamma normalization. The absent n in an odd polynomial term remains a scan question (C161).

## 6. Evidence and handoff

`search_log.tsv` explicitly maps every claim to actual search/opening groups and records successes and failures. `references.bib` has43 entries:41 opened references and two unidentified sources. Its annotations distinguish metadata, bibliographic leads and exact theorem collation. `check_events.tsv` distinguishes background use, local proof checks, independent proofs and computations. The SGA7 download URL and SHA256 are captured; a stalled OCR attempt was interrupted and its empty output was not used as evidence. Listed original pages were visually inspected.

`code/check_computations.py` and `outputs/computations.json` retain executable certificates. The initial symbolic-expression equality assertion was corrected to mathematical simplification; the initial failure and successful result remain recorded. Finite samples are not represented as proofs of unrestricted statements. None of the programs changes the supplied transcriptions.

The82 scan questions are mathematically justified alarms, including cases where different conventions permit different readings. Manuscript scans were not provided. Links distinguish exact continuation, source-family identification and unavailable project leads. Longue Marche, Dérivateurs, LM4, LM7, LM7_PUSH and war-game register states are not upgraded by analogy with local inertia or analytic symbols. `directions.md` ranks follow-on concordance and formulation tasks; it does not portray a cropped unidentified exercise as a newly discovered open problem.
