# SA08 — Complexe de De Rham à puissance divisée

## Dossier, scope and principal findings

**Alexander Grothendieck's Montpellier papers, cote 136; supplied part 1 of the topic.** The assessment is dated 19 November 2026. This dossier consolidates all 437 entries of the supplied `NOTES_INDEX.tsv`, the six Pro transcriptions and their doubts tables, and the three Codex continuations. Every indexed verdict was made by reading the note with the passage it concerns. Scripts serialize those authored decisions, combine explicitly selected duplicates and check coverage; they do not infer verdicts from headings or keywords.

The centre of these papers is a **weighted integral divided-power de Rham construction**, together with the arithmetic and categorical machinery for recovering modules from their *ombres*. Its strongest established comparison must be stated with both gradings. It is not exhausted by a general aspiration to replace integral cochains with a commutative algebra. The sequence then broadens to integration, coefficients in a topos, admissible generalized theories, dual coalgebras, filtered coefficients, universal operations and an unfinished partial-product construction. Separate reused typescripts concern SGA 7 monodromy and Sullivan's rational models. The final continuation reviews cohomology operations, algebraic K-theory and additive-group Ext. These strata have different dates, authorship and mathematical purposes.

The consolidation has six especially consequential findings:

1. **The weighted comparison and its cup-product factors are already published.** Cartan's 1976 account, explicitly referring to Grothendieck's IHES lecture of 12 December 1975, gives the weightwise comparison, including its endpoint, and the binomial factors needed to recover ordinary products. Later results have their own ranges and coefficients. [SA08-C012–SA08-C013; @Cartan1976, §7 pp. 269–271.]
2. **Finite nonnegative shadow recovery is stronger than some earlier summaries allowed.** The arithmetic works for arbitrary coefficient modules. The exact coefficient left adjoint supplies the missing injective-preservation argument for the special higher-Ext assertion. This proof is reconstructed and independently checked in this run; it is not an unsupported claim that an exact later printed theorem was found. [SA08-C014, SA08-C029, SA08-C032, SA08-C035; proof memoranda.]
3. **The literal infinite negligible class fails.** Elementwise annihilation by sufficiently high divided-power tails is not extension-closed. A localizing Serre closure is a real replacement, not an innocuous change of wording. Coherent multiplication remains a further question after linear recovery. [SA08-C033–SA08-C034, SA08-C217–SA08-C221, SA08-C223–SA08-C226, SA08-C287.]
4. **Several constructions require precise qualifications that change their truth value.** These include arbitrary coefficient presheaves, preservation of acyclicity by nonlinear functors, flat convolution versus nonflat convolution, naturality in independent variables versus a single diagonal variable, and ordinary algebraic duality versus completed duality. The tables contain concrete counterexamples with their hypotheses checked. [SA08-C053, SA08-C104, SA08-C255, SA08-C285, SA08-C926, SA08-C949.]
5. **Questions already answered elsewhere remain in the historical problem index.** The index distinguishes an open step on these pages from a problem still open today. Breen's later Ext formula, the derived décalage theorem, and modern cochain uniqueness and homotopy reconstruction results answer precise nearby questions; none is used to settle a different category merely by similarity of subject. [SA08-C114, SA08-C929, SA08-C952–SA08-C957; @BMT2016; @Mandell2002; @Breen1978.]
6. **The archive needs a mathematical reading register even where the transcription is faithful.** Some alarms match defects already visible in the printed SGA source; others concern an uncertain symbol, a missing index, a blank sign or an untyped construction. No manuscript scan was supplied, and no diplomatic reading has been changed. The mathematical alternative is kept separate from the reading of the ink.

## 1. What is actually supplied

### The whole topic and this part

| Cote | Catalogue subject and extent | Treatment here |
|---|---|---|
|136|Divided-power de Rham complex; catalogue 375 pages; the topic table reports 318 Pro pages|All nine attached transcription files and all 437 indexed notes in this part are read and consolidated.|
|137|Dévissage of demi-simplicial complexes and multiplicative structures; 85 pages; 42 Pro pages in the topic table|Explicitly designated “other part”; no transcription or indexed note of this cote is supplied here.|
|138|Arithmetic study of maps; 132 pages; catalogue dates 1976–77 with uncertainty|Explicitly designated “other part”; no substantive coverage is invented.|
|139|Émile Picard medal; 2 catalogue pages|Explicitly designated “other part”; recorded as a catalogue object, not a mathematical manuscript in this attachment set.|

The catalogue's page totals and transcription-production counts are not counts of the scan markers actually attached to this run. The supplied files contain **317 scan markers: 272 in the six Pro files and 45 in the three Codex files**. The largest scan label is 376; pencil foliation, scan labels and catalogue extent are different systems. The absence of a marker is not evidence that its physical page was blank. [Source:`TOPIC.md`; `SA08_statistics.json`; SA08-914–SA08-916.]

| File / scan span | Supplied scan markers | Indexed entries | Main live material and interleaving |
|---|---:|---:|---|
|MPL_136_002-046|44|100|Historical outline; PD simplex; shadows; arithmetic; early homotopy questions; administrative and SGA donor faces|
|MPL_136_047-094|46|70|Representable cochains; Stokes integration; coefficients; internal constructions; Sullivan and SGA donors|
|MPL_136_095-141|46|9|Generalized theories; localization; dual coefficient coalgebras; SGA and English donor material|
|MPL_136_189-234|45|95|Free PD algebras; four de Rham/Koszul variants; operators; normalized models; SGA and Stoia donor material|
|MPL_136_235-281|46|75|Filtered and completed coefficients; cutoff categories; derived recovery; SGA donor material|
|MPL_136_282-327|45|88|Tail arithmetic; negative coefficients; universal additive and PD structures; curve example; SGA donors|
|K136-01, 328–342|15|—|Curve Euler normalization; convolution; polynomial laws; rank and reconstruction diagrams|
|K136-02, 343–361|15|—|Limits and realization; operators; half differential algebra; Sullivan donors; Eilenberg–Zilber and operations|
|K136-03, 362–376|15|—|Décalage; stable operations; Eilenberg–Mac Lane homology; K-theory; additive-group Ext|

The Pro span 142–188 is not attached. Within the supplied spans, the missing markers are 19, 47, 79, 122, 214, 243 and 319; the nominal 047–094 packet begins at 48. The second Codex segment omits 344, 347, 354 and 356. These are inventory facts, not reconstructed contents. The `second_pass/` material described by the task is absent for this attachment set; the supplied Pro/Codex texts therefore remain the current readings. This is an expected source condition.

### Entry granularity and provenance

The nine indexed entries for 095–141 include large composite sections. Their constituent discussions cannot honestly be compressed into nine mathematical claims. Each indexed entry therefore has **one primary verdict row**, while additional semantic facets are recorded in the item list and in `SA08_entry_item_expansion.tsv`. This preserves the 437-row contract without either dropping embedded content or inventing additional indexed entries. The Codex notes are leads without indexed verdict rows; directly checked continuation items have empty `sources` lists and explain that origin explicitly. One additional Pro item, SA08-523, records a proposition found by reading the full transcription that had no independently indexed note; it likewise creates no verdict row.

Three registers remain separate throughout: what the supplied transcription says; what an opened publication establishes; and what this run reconstructs or checks. Earlier-run ideas are labelled as such. The six-stage tables retain their original packet records under `work/`, and `SA08_id_aliases.tsv` resolves cross-packet merges without renumbering surviving IDs.

## 2. Order, dates and the author's objects

The opening title is *Complexe DR à p.d. et ombres des modules*. The cover/plan annotation says 1976. Cartan's printed account gives the precise lecture date 12 December 1975 and appeared in 1976; its proof note already mentions Miller's preprint. Those facts do not authorize erasing the written 1976 annotation. The administrative sheets date their own meetings or announcements. Neither they nor the later bibliographical years establish the composition date of every handwritten leaf. [SA08-1, SA08-71–SA08-77; @Cartan1976, §7.]

The SGA 7 typescripts belong to the 1967–1969 seminar and its 1972 publication. They precede the live PD exposition. Class A in this dossier can therefore describe a donor-draft-to-own-publication match; it must not be read as a claim of a post 1975 development. The English donor sheets match Sullivan's Tokyo 1973 lecture text, published 1975, at several exact places. The hosted version differs at the intervening wording of scan 349. Scan 109's English sheet is conservatively identified by its content and compared with Sullivan's later exposition without inventing a precise draft date or authorial inscription absent from the leaf. [SA08-C067–SA08-C077, SA08-C193–SA08-C196, SA08-C921–SA08-C922; @SGA7IX1972; @Sullivan1975; @Sullivan1977.]

The notation is most safely organized by the following distinctions:

| Object or index | Meaning that must be retained |
|---|---|
|\(\Phi\)|The simplex coordinate object, or more generally the middle term of a chosen unit extension|
|\(\Psi\)|The quotient in \(0\to kT\to\Phi\to\Psi\to0\), with the applicable flatness/splitting hypotheses|
|\(\Gamma_k(T)\)|The divided-power coefficient algebra; its marked \(T\) is not the torus \(T\) of the SGA donors|
|\(\Gamma^p\Phi\otimes\Lambda^q\Psi\)|Complementary PD degree \(p\), cochain/exterior degree \(q\), total weight \(w=p+q\)|
|\(\tau_N\)|A degree cutoff; its inclusion and section adjoints are different functors|
|\(\tau_\infty\)|A proposed stable extraction/localization whose exact definition must travel with any theorem|
|\(\mathbf Z_p\)|Prime localization in the early arithmetic argument; actual \(p\)-adic coefficients in the later filtered discussion must be distinguished contextually|

In particular,\(T\) is in exterior degree 0 and weight 1. Over \(\mathbf Z\),\(T^2=2T^{[2]}\). Treating it as an odd alternating element because its weight is 1 changes the construction. The differential changes \((p,q)\) to \((p-1,q+1)\) and preserves total weight. [SA08-C010–SA08-C013, SA08-C161.]

## 3. From ordinary de Rham theory to the weighted PD simplex

The initial historical list passes through smooth and analytic de Rham theory, Stein acyclicity, arithmetic comparison questions and Sullivan's rational forms. Some names and priority questions are compressed or uncertain. They are not expanded into precise arithmetic theorems without a source. The integral construction begins with a visible repair: the usual barycentric relation \(\sum X_i=1\) cannot simply be inserted into a PD ideal. The replacement uses \(\sum X_i=t\), with \(t\) in a specified PD ideal \(J\subset S\). Eliminating a coordinate is then legitimate. The resulting objectwise resolution of \(S\) and its augmentation to \(S/J\) have distinct roles. The author explicitly warns that this does not automatically compute ordinary cohomology for every coefficient triple. [SA08-5–SA08-15; SA08-C001–SA08-C009.]

For the universal marked coefficient algebra \(S=\Gamma_k(T)\), the fixed-weight strand is the relevant cochain complex. Positive complementary-degree coefficient objects admit actual simplicial contractions; this is stronger than mere homological acyclicity. The exceptional complementary-degree-zero term must be retained in a good truncation argument. Under the stated exactness and section-acyclicity conditions, weight \(w\) computes \(H^q(X,k)\) for \(0\le q\le w\), with vanishing above \(w\). One cannot justify the endpoint by incorrectly declaring the final coefficient term acyclic. [SA08-C011–SA08-C012, SA08-C172; @Cartan1976, §7.]

The product has a similarly exact form. Representatives in weights \(r,s\) induce \(\binom{r+s}{r}\) times the ordinary cup product. When sufficiently many compatible weights are available, these coefficients have gcd 1, so the ordinary pairing is recovered integrally. This is a cohomological recovery mechanism, not a product-preserving identification of a single unweighted alternating PD algebra with ordinary integral cohomology. [SA08-C013, SA08-C015, SA08-C226.]

Two earlier-run tests are useful only with their strengthened hypotheses stated. An unweighted alternating \(\mathbf F_2\)-algebra cannot reproduce the ordinary nonzero odd square in \(H^*(BC_2;\mathbf F_2)\). A PD structure imposed on the ordinary positive-degree ideal of \(H^*(\mathbf CP^2;\mathbf Z)\) would require the primitive square to be divisible by 2. Neither argument refutes the actual weighted comparison. [SA08-8, SA08-106, SA08-111; `work/early/proofs.md`.]

The subsequent literature is not one theorem with interchangeable ranges. Garvín and collaborators prove their fixed-length integration comparison in the explicit strict range \(p<q\) for arbitrary simplicial sets. Their separate nonextendability remark shows that a stronger extension property fails; it does not by itself decide the cohomology comparison at the endpoint. Cenkl–Porter's 1982 paper gives binomial compatibility and a DASH/bar-coalgebra enhancement, not strict multiplicativity of the original integration map. Their 1984 cubical theorem changes coefficient rings with the weight, using inverses of primes at most that weight. Cenkl's later obstruction concerns a strong natural unital commutative all-degree cochain model. The scope of each is separately recorded. [SA08-276–SA08-278, SA08-305, SA08-307, SA08-311; @GarvinEtAl1998, Proposition 3.2, Remark 3.3 and Theorem 4.2; @CenklPorter1982, pp. 10–11; @CenklPorter1984, Theorems 4.1–4.2; @Cenkl1989, §5 Theorem 2.]

## 4. Shadows: arithmetic recovery, derived recovery and the infinite quotient

### The arithmetic theorem

The all-pairs relations
\[
\binom ji(x_j-x_i)=0\qquad(j>i\ge N)
\]
force the family \((x_i)\) to be constant in an arbitrary abelian group. The proof localizes at a prime \(\ell\) and compares the indices with a sufficiently large \(\ell^r-1\), where the relevant binomial coefficients are units. Finite Bézout arguments then recover the integral assertion. No bounded-exponent, finite-generation or completion assumption is needed. The sparse auxiliary lemma has a narrower conclusion: it identifies an adjacent pair, not every variable in a finite truncated configuration. [SA08-C027–SA08-C029; `work/early/proofs.md`; exact arithmetic outputs.]

The weighted analogue identifies a compatible family with \(\xi_k=\binom{k}{i}\xi\) in its specified nonnegative range. It proves full faithfulness of the induced shadow functor and the nonnegative section unit. It does not prove that high truncation is fully faithful on all graded modules. A module concentrated immediately below the cutoff is an elementary counterexample to that stronger assertion. The four-functor chain involving quotient, inclusion, truncation and section has to be written with the correct variance. The lower-degree cutoff also has a strict endpoint; an additional coefficient equation incorrectly kills a valid characteristic-two map. [SA08-C014, SA08-C031–SA08-C032, SA08-C036–SA08-C042, SA08-C213–SA08-C214.]

### The special higher-Ext assertion

The early page states a higher-Ext vanishing corollary without the needed derived argument. Underived full faithfulness and exactness of an embedding do not imply it in an arbitrary abelian-category setting; an explicit dual-number/triangular-category example in the proof memorandum exhibits the failure. For the particular nonnegative one-generator PD category, however, the extra argument exists. [SA08-C035, SA08-C220–SA08-C221, SA08-C223–SA08-C225.]

Write \(i(M)=M\otimes_k\Gamma_k(T)\). A left coefficient adjoint is presented by
\[
L(P)=\left(\bigoplus_{n\ge0}P_n\right)\big/
\left([T^{[m]}x]_{n+m}-\binom{n+m}{n}[x]_n\right).
\]
After prime localization, cofinal degrees \(\ell^r-1\) express this functor as a filtered colimit of degree evaluations with unit binomial denominators. Consequently \(L\) is exact over arbitrary \(k\). The coefficient embedding therefore preserves injectives. Together with the exact cutoff adjunction and the nonnegative underived unit, this proves the special finite-tail derived recovery and its Ext corollary. The full proof is in `work/late/proofs.md`,§5, with independent reviews in the early and root records. The earlier restricted characteristic-p and rational-base arguments are retained as limited independent routes, explicitly superseded in scope by the general proof.

Nagpal–Snowden's later theory is relevant to divided-power modules but has different finiteness and completeness hypotheses. Its examples cannot be transferred to refute the induced-target assertion without checking the target. Conversely, this run's proof does not establish a claim of historical novelty or an exact published match. [SA08-C035, SA08-C286; @NagpalSnowden2017.]

### Negative degrees and three negligible classes

The negative-degree coefficient presentation represents \(\mathbf Q\), giving \(\operatorname{Hom}_{\mathbf Z}(\mathbf Q,M)\), not \(M\otimes\mathbf Q\). Evaluation at 1 can have a kernel, as a nonzero map to \(\mathbf Q/\mathbf Z\) shows. Coherent compatible roots are stronger than mere infinite height. The intersection \(\bigcap_n nM\) need not be the maximal divisible subgroup; the supplied infinite-height construction diagnoses the false literal identification. [SA08-C043–SA08-C047, SA08-C239, SA08-C286; `work/late/proofs.md`,§8.]

The infinite quotient encounters a different obstruction. Let \(S=\Gamma_{\mathbf F_p}(T)\) and \(I=S_+\). The modules \(I/I^2\) and \(S/I\) satisfy the literal elementwise eventual-tail-annihilation condition, whereas \(S/I^2\) does not: its class of 1 is hit by arbitrarily high \(T^{[p^r]}\). Thus the literal class is not Serre. Uniformly bounded modules are Serre but fail closure under arbitrary coproducts. The localizing Serre closure of bounded modules is a valid replacement; the exact adjoint above proves its stated induced-module recovery in the specified derived setting. None of this identifies the replacement with the author's literal class, proves every proposed colimit formula, or supplies strong monoidal recovery. [SA08-C033–SA08-C034, SA08-C217–SA08-C219, SA08-C223, SA08-C287; @Gabriel1962.]

## 5. Integration, coefficients and theories in a topos

The historical “demi-simplicial” terminology in these passages uses the full simplex category, including degeneracies. Interpreting it as the modern face-only category changes both representability and the contraction argument. Cochains are represented by their values on standard simplices, with the right-adjoint indexing direction fixed by the actual Hom formula. [SA08-37, SA08-79; SA08-C048–SA08-C049.]

The Stokes map is constructed inductively from objectwise exactness and vanishing above simplex dimension. The boundary cancellation is checked: deleting a pair of vertices in its two possible orders gives opposite signs. The dual \(\kappa_n\) construction is the same orientation-sensitive issue in the representing object. Cartan's natural integration theorem matches the precise additive comparison. Multiplicativity on cohomology requires additional flat-cycle conditions; chain-level strict multiplicativity and higher coherent compatibility remain different targets. [SA08-C050, SA08-C054–SA08-C055, SA08-C124; MP-SA08-20, MP-SA08-22; @Cartan1976, Theorems 2–3 pp. 266–267.]

The unrestricted coefficient-presheaf sentence on scan 64 is false under its literal simplicial-slice interpretation. On the simplicial circle, take the presheaf supported on vertex-degenerate simplices and zero on edge-degenerate ones. The proposed global-section tensor complex is zero, while an explicit injective-diagram calculation gives nonzero first cohomology. This counterexample preserves the locally constant theorem and does not purport to refute every corrected sheaf-theoretic construction. [SA08-87; SA08-C052–SA08-C053; `work/early/proofs.md`,§9.]

The internal construction starts from a unit extension with flat quotient and sufficiently tensor-stable acyclicity of its positive divided and exterior powers. A tentative inference from “flat and flasque” to contractible is visibly corrected. Actual simplicial contractions provide the intended example; ordinary acyclicity of a flat complex alone does not. Absolute section-acyclicity does not establish all slice conditions or \(f_*\)-acyclicity in a relative direct-image theorem. Similarly,\(k\)-flatness does not automatically make an ordinary tensor extension over \(\Gamma_k(T)\) preserve quasi-isomorphisms. [SA08-C061–SA08-C066, SA08-C101–SA08-C104; MP-SA08-24–MP-SA08-30.]

The later generalized-theory category makes the intended comparison problem explicit. It proposes a stable extraction, common refinements, a localization groupoid and independence of choices. Connectedness, simple connectedness and contractibility of a full higher nerve are not synonyms. A compatible map between two already established comparison objects is a quasi-isomorphism by two-out-of-three; that does not prove the common-refinement or fraction conditions. Mandell's 2002 uniqueness theorem is a strong precise analogue for enhanced cochain theories, but no opened source identifies its category with this PD/\(\tau_\infty\) category. [SA08-C114–SA08-C115, SA08-C188; @Mandell2002, pp. 548–549.] Guillén–Navarro–Pascual–Roig give a localized multiplicative comparison under a PID base, free bidegree modules, simplexwise cochain homotopy equivalence and degreewise simplicial contractibility. Those explicit acyclic-model hypotheses do not identify the weighted PD localization either. The first arXiv submission was 30 June 2005 and the journal publication 2008. [@GuillenNavarroPascualRoig2008, Theorem 8.1 p. 372, Theorem 9.2 p. 373 and Corollary 9.3 p. 376.]

The representing coefficient construction also separates ordinary polynomial coalgebras from their completed dual algebras. Finite homogeneous duality is exact in the stated setting; an infinite dual is a product. Interchanging that product with scalar extension or ordinary colimits requires hypotheses. The represented point can carry the unprocessed coefficient algebra rather than ordinary chains of a point; an extraction convention must be specified before treating that as a contradiction. [SA08-C116–SA08-C124, SA08-C189–SA08-C192; SA08-314.]

## 6. De Rham/Koszul calculations and nonlinear normalization

The free constructions in 189–234 clarify four elementary complexes that earlier summaries risk conflating. In one variable, the relevant coefficients are:

| Algebra and differential | Formula | Integer coefficient |
|---|---|---:|
|Ordinary polynomial de Rham|\(d(x^n)=n x^{n-1}dx\)|\(n\)|
|Divided-power de Rham|\(d(x^{[n]})=x^{[n-1]}dx\)|1|
|Ordinary polynomial Koszul|\(\delta(x^{n-1}dx)=x^n\)|1|
|Divided-power Koszul|\(\delta(x^{[n-1]}dx)=n x^{[n]}\)|\(n\)|

These formulas explain where an integral acyclicity argument works and where torsion remains. The total-weight Euler relation \(d\delta+\delta d=\Theta\) is checked on generators and by exact operator calculations. Calling \(\Theta\) “cohomological degree” would give a false vanishing claim. The extended operator list supports rewriting into normal order; it does not by itself prove linear independence of a proposed normal basis. [SA08-C149–SA08-C161; MP-SA08-98; @BMT2016, Proposition 6.6 and Remark 6.7 p. 288.]

The proposed return map in the simplex sequence on 346 composes to multiplication by the weight \(p\). It is a splitting after inverting \(p\); the displayed formula is not an integral right inverse. This checks one candidate, not an impossibility theorem for every natural splitting. [SA08-C060, SA08-C917; MP-SA08-23.]

The normalized exterior-power model is especially sensitive to notation.\(N\Lambda^r\Psi\) has its rank-one term in degreer. For \(r\ge1\),\(N\Lambda^r\Phi\) has the two rank-one terms in degrees \(r-1,r\); at \(r=0\), the constant exterior power has only degree 0. The unnormalized \(\Lambda^{m+1}k^{m+2}\) has rank \(m+2\), not 1. [SA08-C168; MP-SA08-50.]

The corresponding divided and symmetric powers do not share that answer. For the standard \(\Psi\), over \(\mathbf Z\), the quadratic normalized complexes have the form
\[
N\Gamma^2\Psi:\quad\mathbf Z\xrightarrow{\ \pm2\ }\mathbf Z
\quad\text{in degrees2 and1},\qquad
N\operatorname{Sym}^2\Psi:\quad\mathbf Z\xrightarrow{\ \pm1\ }\mathbf Z.
\]
Thus the first has \(H_1=\mathbf Z/2\), and the second is acyclic. Over \(\mathbf Q\), the first is also acyclic. This checks the queried \(\Gamma^s\Psi\) term and exposes the risk in scan 239's uncertain \(\Pi_*\)/\(K_*\) identification and all-weight nonflasqueness claim. The correct exterior result cannot be silently transferred to \(\Gamma\). [SA08-C169, SA08-C205, SA08-C958; MP-SA08-51; saved exact matrices and the direct quadratic proof.]

The derived décalage comparison does provide a precise framework. For finitely generated projective \(M\) over a commutative ring, the checked indexing is
\[
L_i\Gamma^d(M,n)\simeq L_{i+d}\Lambda^d(M,n+1)
\simeq L_{i+2d}\operatorname{Sym}^d(M,n+2),
\]
with the multiplicative compatibility in the cited theorem. This is a derived construction using appropriate resolutions. A functor preserves a specified simplicial homotopy because it preserves the equations of maps; it need not preserve arbitrary quasi-isomorphisms of unresolved complexes. [SA08-C167, SA08-C929–SA08-C930; @BMT2016, §3.4 Proposition 3.5 p. 270; @DoldPuppe1961.]

## 7. Filtered coefficients, universal structures and the curve example

The filtered pages retain a weaker comparison after deleting an unfiltered assertion. Their completed PD polynomial presentation requires compatible topology, quotient and continuous differential. The associated-graded freeness assumption is real mathematical input. Cartan's graded universal theorem does not establish exactness of arbitrary completion. [SA08-C201–SA08-C205; MP-SA08-60.]

The \(p\)-adic computation is redone using \(a_p(i)=i-v_p(i!)\), with
\[
a_p(i+1)-a_p(i)=1-v_p(i+1).
\]
Raw values can fall at prime powers. The lower envelope relevant to a filtration must not be confused with the raw sequence. At 2,\(a_2(i)\) is the binary digit sum and equals 1 at arbitrarily large powers of 2, giving the exceptional failure of the naive cofinality/separation inference. For odd primes the growth and envelope behave differently. Even cofinal filtration levels do not identify the associated graded with a free divided-power algebra. [SA08-C206–SA08-C208; `work/late/proofs.md` and exact valuation output.]

The later additive constructions use the density of simplices and free additive cocompletion. Yoneda is valid without finite-dimensionality when the full representable functor is retained. Replacing it by an unrestricted algebraic bidual or a finite list of tests requires extra conditions. Bare additive chain information does not determine cup products;\(\mathbf CP^2\) and \(S^2\vee S^4\) have the same free chain-homotopy type and different cup squares. Dold–Kan is an additive equivalence; ordinary tensor products and nonlinear operations need transported structure or explicitly controlled comparison maps. [SA08-C048, SA08-C247, SA08-C289–SA08-C290, SA08-C909–SA08-C913; @Kelly1982; @SchwedeShipley2003; @Richter2009.]

Ordinary convolution from a cocommutative coalgebra is formal. A divided-power convolution law is extra information. In the flat-coalgebra case it can be constructed using the canonical identification of divided powers with symmetric tensors and iterated comultiplication; the proof checks the PD axioms and does not require the target ideal to be flat. There is a specified nonflat counterexample. The proposed uniqueness statement also depends on whether zero indices and full additive naturality are included; positive-index relations alone admit a characteristic-two counterexample. The general six-way comparison of universal power data remains an axiom-sensitive programme. [SA08-C255, SA08-C257, SA08-C259, SA08-C285; @SGA4XVII, XVII 5.5.2.4–5 p. 374; @Roby1963; @Roby1968.]

The curve example must be read just as carefully. The literal split projective bundle \(\mathbf P(\Omega^{-1}\oplus\Omega)\), for a nonzero-degree line bundle on a compact curve, fails the asserted holomorphic-connection property. The oper comparison involves a nonsplit jet extension. The following Euler calculation distinguishes the defining \(\mathrm{SL}_2\) circle from its projective boundary action, whose weight is doubled. Hence the alternatives \(g-1\) and \(2g-2\) concern a real normalization issue, with orientation and the chosen lift still to be specified. Uniformization does not itself give a canonical algebraic splitting in families. [SA08-C264, SA08-C901; MP-SA08-80, MP-SA08-90; @BHR2021.]

## 8. The final continuation: operations, stable homology and Ext

The Eilenberg–Zilber review distinguishes shuffle symmetry from Alexander–Whitney's generally nonsymmetric map. With the conventional homological differential, a degree-two homotopy has \(d\ell-\ell d\), and the extra \((-1)^i\) in the transcribed Alexander–Whitney formula fails already in degree 1. These are convention-dependent mathematical alarms; the ink remains unchanged. [SA08-C924–SA08-C925.]

The Dold attribution required a more substantive repair. The original theorem concerns natural transformations in **independently varying inputs**. It proves acyclicity of that natural-Hom complex. A separate positive free group-ring resolution \(W\) is then chosen and mapped into it; freeness of \(W\) is not an assertion that Hom itself is free. Specializing the inputs afterwards is another step. The insertion “pour X variable” does not by itself impose independent-variable naturality. For diagonal-only naturality in arity 2, the four coordinate maps \((x,y)\mapsto(x,x),(x,y),(y,x),(y,y)\) give four independent degree-zero natural operations, detected on a discrete two-point set, where positive normalized chains vanish. Thus the literal diagonal-only augmentation-to-\(\mathbf Z\) assertion is false. [SA08-C926–SA08-C927; @DoldSteenrod1961, Theorem 1.6 and §§1.7–1.12, printedpp 259–262; `work/root/codex_proof_checks.md`,§17.]

The power-operation formula contains a genuinely blank sign exponent. The questioned Adem identity has a different defect: with ordinary composition,\(\mathrm{Sq}^1\mathrm{Sq}^2=\mathrm{Sq}^3\); its additional term is detected on the degree-one generator of \(H^*(\mathbf RP^\infty;\mathbf F_2)\). Milnor's dual-algebra degrees and coproduct are checked with the prime and conjugation conventions kept explicit. The recorded Bocksteins cannot be exchanged without changing the corresponding left/right action. [SA08-C928, SA08-C934–SA08-C938, SA08-C945; @Milnor1958; @SteenrodEpstein1962.]

Cartan's stable Eilenberg–Mac Lane calculations require their range. In offsets 2–5, in the checked stable range \(i<n\), the groups are
\[
G/2G,\qquad {}_2G,\qquad G/2G\oplus G/3G,
\qquad {}_2G\oplus{}_3G.
\]
The program and proof memorandum check the low coefficient complexes and the quotient/torsion dependence on \(G\). The phrase “entirely prime torsion” cannot include the fundamental-degree homology group \(H_n(K(\mathbf Z,n);\mathbf Z)=\mathbf Z\), and it fails in unrestricted unstable degrees. The claimed symmetry likewise needs the stable qualifications that the page itself says Cartan imposes. [SA08-C939, SA08-C943–SA08-C946; @Cartan1955IX; @Cartan1955X; @Cartan1955XI.]

The connectivity bound on 373 is not certifiable until its smash/tensor and free-abelian notation is typed. Under the ordinary-space interpretation,\(G=\mathbf Z,n=p=4\) gives two \(\mathbf Z/2\) summands in degree 10 on the smash-product side and one on \(K(\mathbf Z,8)\), below the claimed bound 11. This is a counterexample to that interpretation, not a decision about the intended replacement object. [SA08-C948; `work/root/codex_proof_checks.md`,§15.]

The K-theory leaf contains recognizable classical results, with the stable elementary-group convention and regularity conditions restored explicitly. The elementary commutator identity proves perfectness in the stable group. The Steinberg construction must not be transferred without qualification to arbitrary finite \(\mathrm{SL}_n\). Quillen's Gersten/coniveau/Bloch-formula results provide the stated regular finite-type-over-a-field scope, not an assertion for every scheme. [SA08-C940–SA08-C942; @Quillen1973, §7 Theorems 5.4, 5.11, 5.19; @MilnorK1971; @MerkurjevSurvey.]

Finally, the additive-group Ext calculation requires its category. A Witt-vector extension is an extension of abelian sheaves whose middle object is not killed by \(p\); it is not an extension in \(\mathbf F_p\)-module sheaves. Standard power operations are Frobenius-semilinear in their scalars in positive degrees as well as degree 0. Unrestricted coefficient extension also fails for an infinite discrete space: a sequence of polynomials of unbounded degree is not in the ordinary tensor-product image. [SA08-C949–SA08-C951.]

In the specified big-site \(\mathbf F_p\)-linear setting over \(\mathbf F_p\), Breen's published positive even Ext group is \(\mathbf F_p[F]/(F^{v_p(i)+1})\) in degree \(2i\), while positive odd Ext vanishes. The transcribed exponent without \(+1\) would already incorrectly annihilate degree 2. Over more general perfect fields, the twisted Frobenius ring and its two actions must be retained. The leaf itself states perfect-site vanishing for i>1 before explicitly changing to Fp-module sheaves at line 836. The perfected-site theorem is separate: Mathew's AppendixA gives positive-degree vanishing in its precise perfect étale setting; it does not compute the nonperfect result. The first arXiv submission was 23 May 2022, and the paper was published in 2023; an earlier circulation date was not established. [SA08-C952–SA08-C956; @Breen1978, Theorem 1.3 p. 47 and §VII, pp.  116–125; @Mathew2022, TheoremA.1.]

The later answers do not fill every handwritten proof gap. The edge-map vanishing, the extension from \(P^0\) to arbitrary powers, and the final product/bar calculation each retain their own problem records. Breen's group calculation and a proposed Yoneda-algebra structure are different assertions. No personal reason for abandoning those individual steps has been located. [SA08-C954–SA08-C957; MP-SA08-113–MP-SA08-116.]

## 9. Reused typescripts: exact source matches and limits

The SGA donors concern fixed and toric parts, Néron models, Barsotti–Tate groups, blended extensions, monodromy pairings, uniformization and mixed Hodge structures. Their presence on reused paper must not be converted into applications of the PD complex. Exact own-publication matches include the semistable reduction and orthogonality results, the abelian-part construction, the extension-theoretic monodromy formulas and the integral positive pairing under an ample polarization. Published requests left to the reader remain requests; locating them in print is not an independent proof. [SA08-C069–SA08-C077, SA08-C130–SA08-C142, SA08-C175–SA08-C186, SA08-C197–SA08-C199, SA08-C267–SA08-C279, SA08-C288, SA08-C501–SA08-C502; @SGA7IX1972.]

The equal-characteristic full-faithfulness input has a precise later history. De Jong's 1998 Corollary 1.2 treats Hom of \(p\)-divisible groups over the characteristic-\(p\) discrete valuation setting; the finite \(p\)-basis hypothesis belongs to the distinct F-crystal theorem. The 1999 erratum must be read without incorrectly concluding that it destroys the cited corollary. The good-reduction criterion and the global dimension-one extension request are likewise separated. [Relevant middle claims and primary audit; @deJong1998; @deJong1999Erratum.]

Four important donor alarms survive comparison with the published original:

| Supplied locus / published passage | Mathematical issue |
|---|---|
|Scans 57, 59; SGA 7 IX 12.3.10, p. 472|The incidence target is printed as \(\mathbf Z^{I\times J}\), while the normalization/graph calculation requires the direct-sum vertex target. The preceding branch hypotheses matter.|
|Early mixed-Hodge donor; IX 13.4.6, p. 494 and 13.4.17(c), p. 498|The extreme filtration indices conflict; a decreasing-index reconstruction reverses them.|
|Scan 284; IX 3.5(ii), p. 350|The inclusion \(V\subset V^\perp\) conflicts with the proof's reverse direction.|
|Blended-extension donor; IX 9.3, p. 421|The roles of \(P,Q\) are interchanged between parts of the displayed setup.|

These are not permissions to “correct the transcription”: a faithful transcription can faithfully preserve a source error. The source and proposed repair are both retained. The same caution applies to completeness, strict-locality, polarization, factoriality and residue-field conditions in the algebraization/Picard statements. [SA 08_readings.tsv; early and late primary-source checks.]

The Sullivan donor identification is exact at the matched minimal-model and TheoremD passages. The Heisenberg period calculation has the expected unit diagonal and iterated-integral cross term; a bottom-right 0 would make its matrix singular. The hosted text does not decide the exact wording or ink of scan 349. Minimal models, their nilpotent finite-type homotopy interpretation and the broader nonsimply-connected programme remain distinct. The separately headed Stoia Gorenstein text is not attributed as a new Grothendieck theorem; unavailable original-access leads are marked as such in the bibliography. [SA08-C067–SA08-C068, SA08-C193–SA08-C196, SA08-C921–SA08-C922; @Sullivan1975; @Sullivan1977.]

## 10. What is established by November 2026

Modern results make the historical questions more precise, but do not authorize a single unqualified “solved” label for the manuscript category.

| Opened comparison | Exact relevant content | What it does not identify automatically |
|---|---|---|
|Cartan 1976; Cenkl–Porter; Garvín and collaborators|Weighted or filtered comparisons, specified degree bounds and products/enhancements|An unrestricted ordinary integral commutative cochain model|
|Mandell 2001|The \(p\)-complete nilpotent finite-\(p\)-type theorem over the algebraic closure, with a separate field-dependent appendix|Replacing \(\overline{\mathbf F}_p\) silently by \(\mathbf F_p\)|
|Mandell 2002|Axiomatic uniqueness of an enhanced cochain theory|The same theorem for an unspecified historical PD localization|
|Guillén–Navarro–Pascual–Roig 2008|Localized multiplicative acyclic-model comparison under its PID, freeness and contractibility hypotheses|The same result for an unspecified weighted PD localization|
|Mandell 2006|Integral \(E_\infty\)-cochains classify the stated nilpotent finite-type homotopy types; faithfulness without fullness|Full faithfulness of the bare PD/cochain functor|
|Ekedahl; Toën; Horel|Numerical, affine and binomial models, each with explicit target and source hypotheses|Equality among their categories or with the author's proposed virtual objects|
|Richter–Sagave|Strict commutativity in a diagram category with its comparison to \(E_\infty\)-cochains|Strict commutativity of ordinary integral cochains in an unchanged target|
|Bachmann–Burklund 2026|Full faithfulness of \(E_\infty\)-coalgebra chains over a separably closed characteristic-\(p\) field for \(p\)-complete nilpotent spaces, without the earlier finite-type restriction|An identification of the manuscript's ordinary co-PD coefficient coalgebra with that enhanced coalgebra category|

The last comparison was first submitted to arXiv on 24 February 2024 and published on 23 March 2026. Its published essential-image condition uses the stated Verschiebung formulation; an earlier preprint's wording is not silently substituted. Thus it would also be inaccurate to describe every modern comparison as still subject to a finite-type restriction. [SA08-308–SA08-312, SA08-455–SA08-458; @Mandell2001; @Mandell2002; @Mandell2006; @Ekedahl2002; @Toen2020; @Horel2024; @RichterSagave2020; @BachmannBurklund2026.]

The literature classifications are **fate classifications**, not truth certificates for the transcription. Class E can accompany a false transcribed formula when its correct classical statement is known; the page-status and counterexample fields say why. Class C specifies the part answered and the part not matched. Class D records a bounded search with no exact later treatment located, not a proof of novelty. Class F means the intended hypothesis-complete claim is not identifiable. Class A's donor chronology is qualified above. Every claim has a search record and an exact-reference list; the reference annotations state whether the original theorem, an author version, a later primary exposition or only metadata was opened.

## 11. What the earlier notes got right and where they needed correction

The strongest earlier notes already recognized the two gradings, the special coefficient algebra, the need for higher multiplicative structure, and the danger of equating different integral homotopy models. Those readings survive the passage checks. The most useful corrections are more specific than a general change of interpretation:

- The primitive-square and odd-square arguments apply to strengthened unweighted assertions, not to Cartan's weighted theorem.
- Binomial rigidity is valid for arbitrary coefficient modules; invalid integer division must be replaced by prime-local units/Bézout arguments. The sparse lemma and the all-pairs theorem have different conclusions.
- Finite nonnegative derived recovery has a valid special proof, although the proposed abstract categorical shortcut is false.
- Elementwise negligible, uniformly bounded and localizing-Serre-generated classes are different. Using the same word “torsion” obscures the failed extension property.
- Flat acyclicity, actual contractibility, universal section-acyclicity and relative acyclicity are different conditions. The page's own retraction is part of the evidence.
- Infinite algebraic duals introduce products, and product/tensor interchange needs hypotheses. The negative-tail term is Hom from \(\mathbf Q\), not tensor rationalization.
- The correct exterior-power normalization does not identify divided or symmetric powers with the same Eilenberg–Mac Lane object.
- The convolution theorem requires a flatness or extra-data condition. A relation checked only at positive indices cannot silently be used at index 0.
- The variable-input repair in the Dold paragraph remains insufficient under diagonal-only naturality; the exact original theorem separates multivariable acyclicity from a free resolution.
- The unqualified coefficient-extension, Steenrod semilinearity, stable-range and Ext-exponent formulas require the precise corrections recorded in the claims and readings.

Earlier context links to La Longue Marche, Les Dérivateurs, S 6 and named runs are preserved as provenance. They do not supply missing proofs, chronology or axioms for the de Rham construction. The external project files were not supplied as independently inspectable endpoints. The exact targets were not resolved by a bounded search of the available files; their reported links therefore remain provenance-only, without a verified second endpoint. The target queries and access limits are recorded in `work/integration/project_access_audit.md`. They therefore remain explicitly unverified leads in `SA08_project_links.tsv` and the provenance supplement; they are excluded from the table of established mathematical links. The local note attributions and manuscript endpoints were checked. [SA08-2, SA08-238, SA08-283, SA08-303, SA08-401; separate project tables.]

## 12. Reading priorities and future work

Every recorded mathematical alarm has its exact file/scan/line locus in the readings table. The highest-impact scan checks concern the direction of adjunctions and the cutoff inequalities; zero versus positive complementary degree; the \(\Gamma/\Lambda\) and \(\Pi_*/K_*\) notation; the missing normalized-object mark; the nesting coefficient for divided powers; the signs in Alexander–Whitney and degree-two homotopies; the blank operation exponent; the two geometric Euler normalizations; and the missing \(+1\) in the Ext exponent. An alternative supported by mathematics remains an alternative until the ink is examined.

The ranked directions are in `SA08_directions.md`. Their leading targets are coherent multiplicative recovery, choice independence of admissible theories, the correct infinite quotient and the actual half-differential-algebra obstruction. Each direction names its items, claims and problems, states the result it would establish, records the precise known boundary and gives one concrete first step. They are not developed here. The problem index also retains historically open questions that are now resolved, as well as cancelled attempts and notation-dependent questions whose intended theorem is still unclear.

The one explicit later retrospective about interruption of this line, in *Pursuing Stacks*, is used only for its own scope. It is not turned into a psychological explanation of every abandoned lemma. Where neither the pages nor an opened source gives a reason, the problem record says so. [@GrothendieckPS1983, §94; related but distinct §§111, 119.]

## 13. Counts and verification record

<!-- STATISTICS_START -->
| Measure | Count |
|---|---:|
|Indexed entries / verdict rows|437|
|Consolidated items|335|
|Items with indexed source entries|318|
|Direct Codex lead/metadata items|16|
|Additional Pro full-text item without an indexed note|1|
|Claim records, including three labelled reconstructions|315|
|Consolidated historical problems|114|
|Readings to check against scans|172|
|Checked local/publication link records|138|
|Separate external-project provenance leads|40|
|Ranked directions|12|
|Check-event rows|1443|
|Bibliography works|90|
|References with an opened URL/DOI|84|
|Original-access leads marked unverified|6|

**Indexed-entry verdicts:** kept: 266, merged: 146, corrected: 25. No source entry is silently dropped; withdrawal on the manuscript is recorded in item kind and page status rather than deleting an accurate note about that withdrawal.

| Item kind | Count |
|---|---:|
|title, date or page count|20|
|unproved claim|53|
|self-flagged step|65|
|withdrawn in the same text|22|
|other|52|
|idea of the earlier run|53|
|reading question|49|
|conjecture|9|
|unpursued implication|12|

| Claim class | Meaning in this dossier | Count |
|---|---|---:|
|A|Own-publication match, with donor chronology distinguished|46|
|B|Developed by others into an established result|34|
|C|Partial development or a precise remaining scope gap|90|
|D|No exact later development located in the recorded bounded search|8|
|E|Known antecedent or classical result|118|
|F|Intended claim not identifiable with complete hypotheses|19|

| Page-status reporting bin | Count |
|---|---:|
|stated, cited or reproduced|119|
|construction, computation or proof sketched|72|
|proved or formal on the pages|23|
|open, questioned or deferred on the pages|56|
|withdrawn or corrected by him|17|
|false or defective as stated/transcribed|25|
|explicit reconstruction record|3|

<!-- STATISTICS_END -->

The claim-status bins above are a display summary of the full, occurrence-specific `status_on_pages` fields. A merged record can contain a proved special case, a later corrected formulation and an unproved extension; the detailed record, not its reporting bin, determines the assessment. The three explicitly labelled reconstruction records give refined theorem IDs for check events and are not attributed verbatim to Grothendieck.

All 437 indexed entries appear exactly once in the verdict table. Semantic facets of a composite entry may point to several items, with one primary verdict item. The Codex continuation items and the directly recovered Pro proposition create no extra verdict rows. Cross-packet merges retain all occurrences and their source IDs; the compound tail-coefficient problem is distributed between its positive, adjunction, derived and negative questions without dropping its loci.

The check ledger distinguishes reading and matching a published result, a targeted proof check, an independent elementary re-proof, an exact computation and a refutation. Opening a theorem statement is not labelled as proving it. Finite tests support, rather than replace, the general arguments in the proof memoranda. The main computations include binomial rigidity and cutoff witnesses, PD coefficients and identities, the four elementary complexes, normalized face matrices, the operator relations, filtration valuations, graph incidence, the diagonal-natural-operation counterexample, low stable coefficient complexes and the stated counterexamples. Programs, outputs, including failed preliminary runs where material, and proof-scope notes are retained.

The bibliography uses exactly `note = {verified}` when an actual URL or DOI was opened and `note = {unverified}` otherwise. Its separate annotation records the narrower verification scope. A verified metadata record is not represented as a checked proof. Search queries, source URLs, source-response identifiers and hashes are preserved in the retrieval audit; copyrighted external full-text caches and the original supplied attachments are not redistributed in this archive.

## 14. How to use the archive

Start with the entry verdict for a particular Pro note, follow its canonical item, then consult the linked claim and problem records. For a Codex-only question, use the direct continuation items or the claim's scan/line location. The line numbers are one-based lines of the supplied original transcription files; note-file locations are labelled separately. Earlier packet abbreviations are expanded in the consolidated locator fields, with original records retained for checking.

The principal mathematical arguments are in `work/early/proofs.md`, `work/middle/mathematical_checks.md`, `work/late/proofs.md`, and `work/root/codex_proof_checks.md`. The source-comparison and search memoranda explain why a nearby publication was or was not treated as an exact match. `SA08_claim_audit.json` preserves attribution, search-family and proof-scope metadata that does not fit the required claim schema. `SA08_id_aliases.tsv` is the stable-ID bridge for subsequent merging with the other part of this topic.

This dossier supplies the foundation for a future scan-based commentary: the readings are preserved, the mathematical statements have explicit scope, the historical questions remain indexed, and the next research tasks have definite boundaries.
