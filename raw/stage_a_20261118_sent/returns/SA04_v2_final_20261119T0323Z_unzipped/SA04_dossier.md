# SA04 — Grothendieck’s Montpellier papers: part 4 of Géométrie et topologie combinatoire

**Completed audit of the supplied part; reference date 19 November 2026.**  
Cotes 93, 98 and 100, with the separately indexed material in cote 161-5.

## 1. What this dossier establishes

These folders preserve several substantial lines of work, interleaved with reused printed papers, typescripts, correspondence, administrative leaves and cancelled calculations. The strongest continuous mathematical threads are crystalline realizations and deformation of Barsotti–Tate groups; projective differential invariants and connections; Gauss–Manin, Picard–Fuchs and Cartier constructions; norms and cohomological base change; and extension or algebraization of abelian schemes. The archival topic title does not turn those threads into one finished theory. The overview follows their order in the supplied sequences and their own objects before discussing external project leads.

Every one of the 432 rows of the supplied NOTES_INDEX has a verdict based on reading its note and the corresponding transcription. Cote 100 has no indexed note rows in this particular index, but its entire supplied transcription is included in the claims audit. The eight cote 98 index rows are composite sections containing 89 nested notes; those notes were reviewed separately without inventing additional indexed entries. The detailed registers also include transcription-derived items and explicitly identified audit refinements.

Several outcomes are particularly useful for the next folder companions.

* The crystalline programme has a close, passage-level parallel in Grothendieck’s Montréal lectures, Chapter V, published in 1974 from the 1970 course. Its open formulations and qualifications survive in that publication. A publication match is therefore sometimes a match to a programme or stated theorem, not evidence of a proof on the archive leaf. [C-SA04-1–33,48–49; GrothMontreal1974, V, pp.107–120.]
* The Néron/BT extension argument has an exact published counterpart in SGA 7 I, IX5.9 and Remark 5.9.1. The original scan makes the later Tate dependency explicit in IX5.11. Both archive witnesses remove the initial semiabelian-target restriction; the final reduction uses the absence of an additive subgroup in any Néronian generic fibre. [C-SA04-672–676; SGA7I, IX, pp.382–386; RBLR1990, §10.1 Proposition 8.]
* The projective-connection calculations largely survive with precise normalizations. Their existence does not establish the manuscript’s strongest universal classification claims. Characteristic two is a structural boundary for the Lie-algebra reconstructions, not merely a missing denominator in an otherwise unchanged proof. [C-SA04-120–123,201–251; Deligne1970, I§5; parts/b/proof_checks.md.]
* Several literal statements are false under their retained hypotheses. Two consequential arithmetic examples distinguish rational Frobenius-fixed vectors from eigenvalue multiplicity, and disprove the one-step rational Verschiebung-lift criterion for torsion sections. These conclusions do not refute the adjacent, stronger connection-theoretic questions. [C-SA04-644,647–648,702; parts/root_computation_notes.md; parts/b/root_supplement_proofs.md.]
* The current notes already correct some mistakes attributed to earlier contextual material. In particular, the cote 98 Tor statement includes input flatness, bounded kernels and extensions are already listed, and the all-degrees base-change assertion concerns a finite complex. The remaining wrong-ring resolution step is repaired explicitly. [C-SA04-488–511; parts/c/analysis.md, §§8–9.]

The problem index includes questions settled later, questions answered by this audit, authorial doubts, and formulations that still cannot be identified precisely. It is not a list of present open conjectures. Likewise, the claims map includes mathematical claims in printed material and earlier-run constructions when these must be checked to audit the notes; their attribution is stated and is never silently transferred to Grothendieck.

## 2. Scope, witnesses and conventions

### 2.1 The indexed universe and the physical sequences

| Supplied package or sequence | Indexed rows | Coverage in this dossier |
|---|---:|---|
| MPL_93_047-091 | 325 | Every indexed entry; overlapping Pro and Codex witnesses; the crystalline continuation in Codex scans 37–46 |
| MPL_93_221-236+161-5 | 99 | Cote 93 scans 221–236 and the distinct cote 161-5 scans 3–29 |
| MPL_98 | 8 | All eight composite sections and all 89 nested notes; all 43 supplied scan faces, numbered 2–44 |
| MPL_8_079-081+9+4+100 | 0 | The cote 100 portion, beginning at its own cote marker at Pro line 1313; all four K100 Codex files compared |
| Other K93 Codex sequences | 0 additional rows | The supplied earlier and later passages, including scans 3–36 and 135–220; claims without indexed notes are retained |

The supplied K93 sequence does not contain scans 92–134, and other smaller scan-marker gaps are recorded in SOURCE_MANIFEST. Cote 100 has a catalogue count of 52 pages but a maximum supplied marker of 53; scan 47 is absent. Scan labels, catalogue page counts and numbers of supplied faces are different quantities. None was converted into another by assumption.

Cote 161-5 is an archival object in its own right. It is not shorthand for cote 93 scans 161–165. Conversely, cotes 8, 9 and 4 in the mixed package provide context outside this part’s main scope. Repeated scan numbers in that mixed file were checked against cote boundaries; all final source locators use the relevant cote 100 occurrence.

TOPIC lists 30 catalogue rows: cotes 69–91, 93, 94, 97, 98, 100, 101 and 102. SOURCE_SCOPE inventories every one. The 27 rows outside 93, 98 and 100 belong to the other parts; their texts are not supplied here and are not represented as independently audited. This is the part-4 boundary required for the subsequent dossier merge, not a claim to have reviewed the entire Montpellier topic.

No scan images and no second-pass change files were supplied. The diplomatic TeX files are unchanged. Where Pro and Codex differ, both readings remain visible; mathematical plausibility supplies evidence for a scan question, never a decision about the ink. All line numbers count the supplied UTF-8 text from one. The source manifest gives file hashes, line counts and scan-marker locations.

### 2.2 Three levels of assertion

The registers distinguish:

1. **The supplied page:** a brief quotation, its cote/scan/line, its cancellation or question mark, and the attribution of printed versus handwritten material.
2. **The checked literature:** an exact theorem or construction with its hypotheses, an opened URL or DOI, and the dates that can actually be established.
3. **The audit’s reconstruction:** modern notation, added hypotheses, a proof, a counterexample, or an inference connecting passages.

A note may accurately report a false formula. Its textual verdict can therefore be “kept” while the associated claim is “false as stated.” Conversely, a correct theorem in a modern paper does not vindicate a note that drops a source hypothesis. This distinction is especially important for the cancelled analysis exercises, the characteristic-two projective constructions and the cote 98 base-change arguments.

Class A means an exact assertion was located in Grothendieck’s own published work; it does not assert that an undated leaf predates publication, or that Grothendieck originated an explicitly attributed theorem. Class E records material already standard in the relevant setting. Class C identifies the precise gap between a source formulation and the qualified result checked. Class D records a searched but unlocated exact development, not proof that no such publication exists. Class F records an identification or formulation limit.

The bibliography’s verified label means that its recorded link or DOI was opened. Its annotation distinguishes metadata, a theorem statement, and a proof passage. Four references remain explicitly unverified. They are not used as if their original proofs had been read. First circulation, a public lecture, a submitted preprint, receipt by a journal and publication are separately recorded when the evidence permits.

## 3. Cote 93 in the order of its surviving sequences

### 3.1 Elliptic curves, orientation and a detached analytic fragment: scans 3–36

The opening material reuses Deligne’s elliptic-curve formulaire. It records general Weierstrass coordinate changes, the invariant differential, the discriminant and modular invariants, low-characteristic normal forms and exceptional automorphisms. Its printed results belong to Deligne’s reference text; the annotations have their own evidential status. The checked catalogue establishes the IHES preprint M/68/28 in 1968, and the opened Antwerp image edition establishes the 1975 publication. These dates do not date the marginal computations. [C-SA04-601–605,688–693,720–725; RDeligne1968; RDeligne1975.]

The five coefficient transformations were recomputed as integer-polynomial identities after clearing the permitted powers of the invertible change-of-scale parameter. The Legendre discriminant and j formula, the displayed low-characteristic transformations and the finite Fourier coefficients were checked. The identity between Eisenstein series and the discriminant was verified through the saved truncation modulo \(q^{17}\); the program does not claim that a finite truncation proves the infinite modular-form identity.

One apparent error was withdrawn during the audit. The formulaire explicitly allows the relevant singular genus-one fibres. Consequently, its affine parameter space with a marked invariant differential need not invert the discriminant. Treating its proposition as a moduli statement only about smooth elliptic curves would impose a different definition and manufacture a missing-discriminant defect. C-SA04-602 retains the source’s actual convention.

The exceptional pointed automorphism groups have orders 24 in characteristic two and 12 in characteristic three. The characteristic-two group law was checked over \(\mathbf F_4\), with an exhaustion argument explaining why the finite calculation captures all automorphisms. The j-ramification annotation is a definite formal-deformation question over \(W(k)\), not an unidentified general curiosity. Explicit special-fibre parameters give
\[
j=\frac{z^6}{1+z^2}\quad(p=3),\qquad
j=\frac{z^{12}}{1+z^3}\quad(p=2).
\]
Their orders are checked, while the full mixed-characteristic quotient by automorphisms remains a separate comparison problem. The unfinished corollary on scan 21 is not filled in from those calculations. [C-SA04-603,605,688,690; MP-SA04-151.]

The Wanderley offprint introduces a categorical orientation structure and a boundary map called the Stokes map. Its author is **Marcus Wanderley**. The neighbouring sketches concern boundary orientations and double covers; they are not a statement of an analytic integration theorem. The printed exclusion of dimension four belongs to its historical local-topological result. Quinn’s later annulus theorem addresses that dimension under its own hypotheses; it does not settle every boundary-margin extension. [C-SA04-606–607,694; RWanderley1981, supplied offprint and unverified external record; RQuinn1982, §2.2.2, pp.506–507.]

Detached Banach-space lines do not contain all the operator hypotheses required for their conclusion, and are recorded at that limit. The exponential Schwarzian calculation is complete:
\[
G(f)=-2\frac{f'''}{f'}+3\left(\frac{f''}{f'}\right)^2,
\qquad G(e^f)=G(f)+(f')^2.
\]
The intermediate coefficient three conflicts with the final coefficient one; the final line already supplies the correct identity. [C-SA04-608–609; source scan 36; exact symbolic output.]

### 3.2 Crystals, filtered realizations and Tate extension: scans 37–54

The next sequence begins with the contravariant crystal of a BT group, its Frobenius and Verschiebung, and the Hodge extension. It proceeds through finite-flat and truncated categories, deformation, universal vector extensions, the comparison for an abelian scheme’s BT group, passage up to isogeny, realizable filtrations, period functors and generic-fibre full faithfulness. Chapter V of the Montréal lectures is the closest sustained published parallel. It preserves both the main constructions and many of the qualifications or prospective formulations. [C-SA04-1–33,48–49; GrothMontreal1974, V.]

The comparison fixes the type of several formulas without deciding their ink. The Frobenius/Verschiebung identities must have the correct source and target. The crystal functor is contravariant. An extra dual in the covariant comparison changes its meaning. These alarms are supported by the exact printed arrows, not by an assumed preferred notation.

Four distinctions control the modern assessment. First, perfect-base Dieudonné theory is not ordinary-crystal full faithfulness on every singular base. Lau’s perfect-ring categories retain admissibility and truncation conditions, while de Jong’s survey records a failure of unrestricted ordinary-crystal full faithfulness. Second, a filtered isocrystal with the correct total dimensions need not be weakly admissible: the checked two-dimensional example has equal total Hodge and Newton numbers but violates the stable-line inequality. Third, a field-valued rational correspondence is not automatically an integral or relative correspondence. Fourth, Zariski openness of a realizability locus is not proved by a theorem about an analytic period domain. [Lau2013, Definition 6.1 and Theorem 6.4; deJongICM1998, §2(x); ColmezFontaine2000, §4.1; Hartl2008; AnschutzLeBras2023, Proposition 5.4.2.]

The deformation statements also differ in scope. On a base on which p is locally nilpotent, the BT theorem assumes one of three alternatives: nilpotent divided powers, connected fibres of the group, or connected fibres of its Cartier dual. The abelian deformation statement in the Montréal programme permits an arbitrary base with locally nilpotent divided powers; it should not be silently narrowed merely to fit the familiar p-nilpotent Serre–Tate formulation. Characteristic-zero rigidity of the universal vector extension is separately registered. [C-SA04-6,14,48–49; GrothICM1970, §4; GrothMontreal1974, V§4; FonsecaMatthes2022.]

Global denominators matter. On a disjoint union of characteristic-p points, quasi-endomorphisms with denominators \(p^n\) on successive components do not come from one element of the rationalization of the product of integral Hom groups. This proves the warning about the global isogeny category. A nilpotent-invariance statement requiring one p-power to kill the ideal cannot survive removal of that bound without another argument. [C-SA04-18–19; parts/a/proof_checks.md, §1; GrothICM1970, §5.]

The equal-characteristic Tate question has a clear later answer. De Jong’s ICM §3 Theorem 2 extends generic-fibre morphisms of BT groups over an integrally closed Noetherian domain. The p-basis hypothesis in the preceding F-crystal theorem does not belong to this BT theorem. The original 1998 paper and its 1999 erratum were checked separately: the erratum changes an auxiliary assertion and semistable-reduction definition, not the generic-Hom conclusion. Ordinary crystals without Frobenius, F-crystals with nondegenerate Frobenius, and BT groups remain separate records. [C-SA04-27–33,448; deJong1998; deJongErratum1999; deJongICM1998, §3, p.261.]

### 3.3 Reused analysis exercises and Euler characteristic: scans 50–70

The analysis exercises on scans 50 and 52 are cancelled reused sheets of uncertain authorship. They contain weighted Liouville and Fourier arguments, factorization and pseudo-resolvent calculations. The audit verifies their mathematics because the indexed notes discuss it; it does not recast them as Grothendieck’s research conjectures.

The consequential defects include a geometric-weight exponent, a missing Fourier normalization, a big-O/little-o distinction, the sign of the exterior Cayley estimate, a Neumann radius evaluated at the wrong point, and the wrong perturbation target. Each literal failure has a checked example or calculation. Corrected weighted Liouville and pseudo-resolvent arguments are written in the proof appendix. An exact-wording lead to Bourbaki’s spectral-theory exercises was found, but the primary exercise text could not be collated; that attribution remains a lead. [C-SA04-34–47; parts/a/proof_checks.md, §2; Bourbaki1967; Bourbaki2019; deJeuJiang2017; KurbatovKurbatovaOreshina2016.]

The Euler sequence starts from cohomological finiteness, additivity, products and fibrations, then narrows toward relative polyhedra and recursive conical spaces. The change from sheaf cohomology to singular cohomology is mathematically material: one may use closed/open and Mayer–Vietoris sequences only in categories where the relevant exactness holds. Finite constant-coefficient cohomology does not alone imply the local-system Euler lemma needed for arbitrary fibration multiplicativity. The earlier notes’ telescope example is checked fully: its base and contractible double cover both have rational Euler number one, while the two-point fibre has Euler number two. This refutes the broad preliminary formula, not the later narrowed conical question. [C-SA04-50–60; parts/a/proof_checks.md, §3.]

Under explicitly added compactness, metrizability and recursive local-contractibility hypotheses, the compact conical core admits a modern ANR and finite-homotopy-type argument. The radial retraction gives the intended end comparison. Homotopy finiteness is weaker than triangulation, and a theorem for topological manifolds does not automatically settle singular recursive links. The dimension-four triangulation doubt has a negative example inside the manifold subclass. [C-SA04-62–70; MP-SA04-18–20; GuilbaultMoran2019, Proposition 2.9; West1977, Corollary 5.3; Manolescu2015, §2.2.]

Administrative and theme-list leaves interspersed here are retained as metadata. They do not provide a construction joining Euler characteristic to Cartier or Gauss–Manin theory.


### 3.4 Projective differential invariants and bundles: scans 72–91

The analytic invariant is a cocycle on local coordinates, invariant under constant homographies. The source normalization is \(G=-2S\) for the usual Schwarzian \(S\); Deligne’s \(\theta\) is \(S/6\), so \(G=-12\theta\). The local projective-coordinate torsor, osculating two-jets and second-order differential equation have an exact comparison in Deligne I§5. Local nonemptiness and sheaf surjectivity do not select a global projective connection. [C-SA04-120; Deligne1970, I5.8–5.10; Dumas2009, §§3.1–3.2.]

The integral expression uses Hasse derivatives:
\[
Q(f)=-\frac{D_3f}{D_1f}
       +\left(\frac{D_2f}{D_1f}\right)^2,\qquad
G_0(f,g)=(Q(g)-Q(f))\,dt^2.
\]
In characteristic zero, G=12G0; the Hasse formula defines G0 integrally without requiring12 to be invertible. Its composition and projective-invariance identities were checked in a universal localized polynomial ring, so this verification survives arbitrary base change with invertible first jets. Its square test is \(1/(4t^2)\) where \(2t\) is invertible. The cube test vanishes in characteristic two and cannot certify nonvanishing there; the retained alternatives use \(t+t^2\) and \(t+t^3\). These are all-base calculations with stated localizations, not extrapolations from finitely many primes. [C-SA04-122; programs/a_computations.py and b_computations.py.]

The proposed universal target and uniqueness assertions are stronger. Adding an unused coherent direct summand defeats an unrestricted claim that every target is isomorphic to the quadratic-differential target. A meaningful replacement must specify naturality, differential order, target generation and the base category. Fixed-characteristic uniqueness is yet another question. Hoshi’s characteristic-two comparison and Wakabayashi’s odd-prime framework concern precisely specified, different targets; neither supplies the manuscript’s unrestricted assertion. [C-SA04-123,201–203; MP-SA04-24,51–53; BHoshi2024; BWakabayashi2021.]

The successive quotient constructions pass from translations and scalings to affine and projective transformations. Their outputs are respectively functions, forms, frames, connections and torsors; they should not be collapsed into one sheaf. For a nowhere-vanishing local frame of an n-differential in the complex analytic setting, with n nonzero, the root-and-primitive construction gives
\[
c_n(f)=-\frac2n\frac{f''}{f}
       +\frac{2n+1}{n^2}\left(\frac{f'}{f}\right)^2.
\]
The coefficient, tensor-power formula, horizontal-frame sign and quadratic variation were recomputed. Pro takes local coordinates as the source of the map sending g to dg−df, whereas Codex takes all holomorphic functions; both targets are one-forms. This difference changes surjectivity. Likewise, a possible interpretation of the zero-index arrow using \(\mu_0=\mathbf G_m\) remains an earlier-run idea conditional on the ink; it is not refuted as a mathematical identity. [C-SA04-204–227; MP-SA04-54–59,68–69.]

The projective-bundle sequence then compares Brauer–Severi curves, Azumaya algebras, Lie algebras, marked sections and extensions. An unmarked projective line bundle can have a Brauer obstruction; it need not be \(\mathbf P(E)\) globally. A marked section supplies extra rigidification. Trace kernels and scalar quotients differ at two, and identifying divided and symmetric squares after inverting two does not erase that difference integrally. Grothendieck’s published Brauer exposition gives an exact comparison for the obstruction and local splitting. [C-SA04-228–242; BGrothendieckBrauerI, §§5,8.]

In characteristic two, the Lie algebra \(\mathfrak{pgl}_2\) has extra automorphisms and outer derivations. Its automorphism group has dimension six in the explicitly computed model, versus dimension three for the projective group. This breaks the proposed Lie reconstruction while leaving the fppf quotient \(\mathrm{SL}_2/\mu_2=\mathrm{PGL}_2\) intact. The final connection matrix contains the checked relation \(c_{12}=-2c_{23}\), and the author’s correction requiring two invertible must remain visible. Restricted transverse first-order data can be unique while full connections still form a quadratic-differential torsor. [C-SA04-232–251; parts/b/proof_checks.md.]

The Postnikov scratch leaf at scan 83 is separate. A vanishing first k-invariant does not say that its ambient \(H^3\) group vanishes. One looping can have a nonzero first invariant; two compatible loopings force the relevant two-type to split, without a generally natural choice of splitting. The finite cochain calculation checks the chosen algebraic model; the realization and double-loop theorems remain external inputs with checked locators. [C-SA04-80–84; Arlettaz2000, §7; BauesConduche1995, Theorem 1.9.]

### 3.5 Connections, Cartier and arithmetic questions: scans 135–220

The resumed projective discussion distinguishes its simple-pole condition at infinity from more general regular-singular conventions. The Riemann–Roch dimensions are checked with the low-genus cases stated separately. The genus-one translation-invariance question keeps its own hypotheses. It is not resolved merely by saying that every curve connection is flat. [C-SA04-610–612; MP-SA04-154.]

The source then constructs connections as splittings of first principal parts, extends them to the de Rham complex and describes affine torsors with compatible flat connection. In the smooth characteristic-zero setting, those torsors are classified by degree-one de Rham hypercohomology and their automorphisms by degree zero. A compatible infinitesimal stratification is obtained by Taylor expansion. The source’s broader assumption of flat differentials is not automatically sufficient on arbitrary singular morphisms. [C-SA04-613–618; EGAIV4, 16.7.1–7; MP-SA04-155–156.]

The equality of the two Manin-section constructions, explicitly left to verify at scan 159, is completed. The positive jet is the ordinary jet minus the horizontal extension. Applying the connection gives the jet of the affine covariant derivative; naturality of the operator then gives
\[
\nu(\Delta)=\mu(D),\qquad D\circ v=\Delta\circ d_E.
\]
Here \(v:E\to E^{\prime\prime}\) is the quotient and \(D\) is the induced operator on \(E^{\prime\prime}\). Changing a lift adds a term killed by the induced comparison, so the identity descends and glues. This proof uses the supplied stratification and does not require the converse factorization assertion on scan 160. It was checked independently and supplemented by a finite symbolic jet calculation. [C-SA04-620; MP-SA04-157; parts/root_computation_notes.md; parts/c/analysis.md, §11.1.]

The filtered de Rham construction at scans 162–167 is explicitly related to Katz–Oda. The derived projection formula, flatness with coefficients, first-quadrant spectral-sequence indexing and Leibniz rule are separate obligations. An ordinary tensor product cannot replace a derived one merely because the displayed formula is familiar. [C-SA04-621–623; KatzOda1968, §2 Theorem 1 and §3.]

The Cartier sequence provides several elementary but consequential checks. The canonical inverse Cartier map lands in de Rham cohomology. A closed-form representative chosen from a p-basis is not itself natural: in characteristic two the defect for \(x+y\) is the nonzero exact form \(d(xy)\). A splitting into exact forms and chosen representatives is basis-dependent. The uniqueness axiom must annihilate exact forms coming from arbitrary forms, not only from forms already assumed closed. [C-SA04-624–626; RCartier1957, §3 Theorem 1; RSeshadri1959.]

For an integrable connection, p-curvature is Frobenius-linear in the derivation, so its coefficient object is the Frobenius pullback of one-forms. Ordinary tensor power is wrong in rank greater than one: the cross terms in \((dx+dy)^{\otimes2}\) survive. For a derivation D of a commutative ring of characteristic p, with c acting by scalar multiplication, the Jacobson formula
\[
(D+c)^p=D^p+c^p+D^{p-1}(c)
\]
has both saved finite certificates and a universal proof using the commutator identity and the divisibility of the intermediate Bell coefficients. [C-SA04-627–629,705; parts/root_computation_notes.md.]

For a smooth curve in characteristic p, the pairing on \(F_*\mathcal O/\mathcal O\) induced by \(C(f\,dg)\) is perfect. Its antidiagonal condition is \(i+j=p\), not \(p-1\). At \(p=5\) the displayed matrix has determinant \(-1\), not \(+1\); for odd p, the correct canonical square-root comparison is expressed through the Pfaffian with its normalization. At p=2 the quotient has rank one and gives a line-bundle self-duality instead. Cartier’s top-degree duality trace must also be distinguished from the ordinary function trace for a purely inseparable field extension. [C-SA04-630–634; RRaynaud1982, §4.1, Theorem 4.1.1.]

The assertion about a pointless smooth conic over every imperfect field of characteristic two fails over a separably closed imperfect field: every nonempty smooth variety over such a field has a rational point. The surviving construction needs an additional field or Brauer condition. The higher-dimensional analogue of the Cartier pairing is recorded separately as a programme question. [C-SA04-635–636; RStacks056U; MP-SA04-161–162.]

The monodromy pages use a notion of étale local triviality stronger than vanishing curvature. Ordinary connections, stratified objects, finite monodromy and representations of the historical enlarged group are distinct categories. On a nonnormal base that group need not be profinite. The broad relative reconstruction on scan 191 therefore remains a problem with its flatness, finite-presentation, fibre and section hypotheses written out. The opened field-case theorem of dos Santos and relative pro-étale comparison of Lara do not prove all those quantifiers. [C-SA04-638–640,698–701,703,709; MP-SA04-164,202–203,208; BDosSantos2007Supplement, §2.4 Proposition 13; BLara2019Supplement, Theorem 3.1.]

The arithmetic sequence asks whether almost-everywhere zero p-curvature forces finite monodromy. The general conjecture remains open in the primary literature checked on 19 November 2026. Bost’s theorem gives the recorded number-field solvable-group case, including rank one. Patel–Shankar–Whang treat their rank-two generic-curve setting. Lam–Litt’s nonabelian isomonodromy theorem has different hypotheses and conclusions; it is not a general solution. An IAS announcement on 13 October 2025 precedes their first arXiv submission on 12 January 2026. Litt’s problem page, edited 8 May 2026, still identifies the specified general Gauss–Manin direct-summand case as open. [C-SA04-641–643; MP-SA04-165–167; RBost2001, Theorems 2.3,2.9; RPSW2021; RLamLitt2026; RLamLittAnnouncement2025; RLittProblem2026.]

The adjacent one-step Verschiebung question is weaker and false. Take
\[
S=\operatorname{Spec}\mathbf Z[1/30],\qquad
E:y^2=x^3-2x,\qquad P=(2,2).
\]
Its discriminant 512 is a unit on \(S\). Every closed residue field is \(\mathbf F_p\), \(p\ge7\). The rational two-torsion point \((0,0)\) makes \(\#E(\mathbf F_p)\) even, and Hasse’s bound places that number strictly between zero and \(2p\). It cannot equal the odd number \(p\), so p does not divide it. Multiplication by p is bijective on rational points; Frobenius is also bijective there, and \(VF=[p]\), so \(P\) has a rational Verschiebung lift at every closed point. Yet good reductions at 3 and 5 bound the rational torsion order by two, while \(P\) is not two-torsion. This checks every retained hypothesis. The counterexample does not retain the connection data of the stronger universal-vector-extension question. [C-SA04-644,702; MP-SA04-168; BMilne2021Supplement, II§5 and IV§9; BChaiOort2009Supplement, §10.24.]

The finite-field torsion calculation has a different failure. For
\[
C/\mathbf F_2:\quad z^2+(x^2+x+1)z=x^5+x^3+x^2+1,
\]
the Artin–Schreier form has three geometric simple poles, so the smooth projective curve has genus two and geometric p-rank two. Two independently written algorithms give point counts \(3,7,9,31\), zeta numerator \(1+T^2+4T^4\), and \(\#J(\mathbf F_2)=6\). Rational two-torsion therefore has dimension one, while the root one has algebraic multiplicity two modulo two. Rational torsion is a fixed space, not an algebraic multiplicity without a semisimplicity hypothesis. [C-SA04-645–648; MP-SA04-170; RMilne2008; RAS2025, §2.2; outputs/c_review_genus2.json.]

Finally, the Picard hierarchy distinguishes arbitrary connections, integrable connections, zero p-curvature and nilpotent p-curvature. The universal vector extension requires the specified Picard, closed-form and base-change hypotheses. The nilpotent locus is a formal completion along the whole zero-p-curvature locus, not just the identity. A square-zero-base example distinguishes the formal kernel \(P_{\mathrm{cin}}\) from \(P_{\mathrm{cip}}\). Characteristic-p reasoning does not automatically prove the wider p-locally-nilpotent-base assertion. The truncated de Rham obstruction to an integrable connection and the additive-polynomial cokernel question remain precisely qualified. [C-SA04-649–654,706–708; RMazurMessing1974, I§§2–4; MP-SA04-171–175,206–207.]

### 3.6 Periods, formal operators and square-zero comparisons: scans 221–236

The period pages begin with logarithmic derivatives and local path integrals, then apply operators annihilating periods to remove path ambiguity. The distinction between closed cycles and open arcs is decisive. In the product family with \(\omega=dx\), horizontal endpoints zero and one, and annihilator \(D=1\) of the zero de Rham class, the open integral is one. Thus an open-horizontal-arc vanishing assertion fails under all its stated local hypotheses. Moving endpoints contribute the usual boundary term; two intersecting sections cannot always both be made horizontal. The deleted implication from relative to absolute closedness is separately refuted and retained as already corrected in the source. [C-SA04-401–411; parts/c/analysis.md, §2.]

The formal Poincaré argument works over a \(\mathbf Q\)-algebra by contracting homogeneous forms with the Euler field and dividing by their positive degree. In characteristic p, \(x^{p-1}dx\) gives the obstruction. This is not a counterexample to a divided-power Poincaré lemma with different objects. [C-SA04-414.]

The “formally exact” premise of the operator sequences is not defined well enough to identify one theorem with all the displayed variances and auxiliary-module quantifiers. EGA’s principal-parts representation is a verified comparator, not a substitute definition. Several consequences are nevertheless checkable: the circled injection follows conditionally from the preceding quotient presentation; killing the horizontal generators is equivalent to factoring through their module quotient; the resulting quotients form a strict projective system because the transition maps are surjective. The unfinished integrability characterization remains separate. [C-SA04-412–418; EGAIV4, 16.8.4 and 16.11.2.]

For local smooth lifts across a square-zero thickening of the base, the difference of lift maps is a relative derivation into the square-zero ideal. Cartan contraction supplies the chain homotopy between the corresponding relative de Rham maps. The final torsor construction is repaired additively with its complexes in degrees \(-1,0\), and a complete roof defining one derived morphism is written. Its canonicity is relative to the supplied torsor and homotopy data. The boxed universal derived-Hom isomorphism is false already for two rank-two free modules, where the right side has rank four. The valid derived morphism survives that failure. These sheets do not establish an unrestricted crystalline equivalence or general nil-invariance theorem. [C-SA04-419–423; MP-SA04-108; parts/c/analysis.md, §3.]

## 4. Cote 161-5: printed Serre results and a later comparison draft

The first printed work is Serre’s **Sur les groupes de Galois attachés aux groupes p-divisibles**, written in December 1966 and published in 1967. It is not the 1979 Hodge–Tate paper. The 1968–1969 Annuaire cover and later annotations provide separate chronological layers. Serre’s acknowledgment of Grothendieck’s suggestion concerning algebraic groups and motives does not transfer authorship of the printed propositions. [SA04-401–403 and the cote 161-5 records; Serre1967; Serre1979.]

The audit checks the weight calculations, determinant exponent and binomial divisibility, while carrying the root-system classification from the printed argument and opened references. The ramification lemma initially deferred is proved on the next page and must not remain labelled an unanswered question. A request for a direct proof of an established inertia statement is likewise a request about method, not evidence that the theorem is still open. [C-SA04-424–449; MP-SA04-109–115.]

A red equality between the full inertia algebraic group and the group generated by Hodge–Tate data omits neutral components. A nontrivial finite ramified quadratic character is Hodge–Tate of weight zero: its cocharacter is trivial but its inertia image has two elements. Sen’s comparison, as stated in Serre’s later paper, gives the neutral group. Its exact local-field and residue-field conditions remain in the register. [C-SA04-431,444; Serre1979, §1.4 Theorem 2.]

The handwritten comparison category is generated by all the specified two-weight Hodge–Tate objects, while BT objects form a fully faithful subcategory. A semistable noncrystalline Tate-curve representation shows why those categories cannot simply be equated. Fontaine’s admissibility conditions and Liu’s integral correspondence belong to their precise settings. The changed fields, duals, twists and incomplete qualification prevent identifying the draft’s tensor-extension existence and uniqueness questions as one fully specified modern open theorem. [C-SA04-450–454; MP-SA04-116–118; Fontaine1979, §§3.4–3.6 and 6.5; Liu2013, Theorem 2.2.1; Gunton2021.]

The final nonabelian-cohomology pages are made precise in the abstract group-extension setting. Once a section is chosen, other sections are crossed homomorphisms; fixing a subgroup restriction imposes a normalized cocycle and restricts the conjugators. Quotient descent requires normality. An arbitrary restriction fibre must be studied after twisting; the neutral fibre alone does not prove injectivity. The author’s replacement of “torsor” by “homogeneous space” reflects the stabilizer. [C-SA04-456–460; parts/c/analysis.md, §5.]

The last torus diagram also distinguishes point fields:
\[
(\operatorname{Res}_{K/\mathbf Q_p}\mathbf G_m)(\mathbf Q_p)=K^\times,
\quad
(\operatorname{Res}_{K/\mathbf Q_p}\mathbf G_m)(K)
=(K\otimes_{\mathbf Q_p}K)^\times.
\]
The valuation sequence splits after choosing a uniformizer, without a preferred choice. These verified pieces do not complete an undefined arithmetic extension-of-sections problem. [C-SA04-461–462; MP-SA04-119–120.]


## 5. Cote 98: norms, group-set sites and bounded coherent families

### 5.1 Determinant norms and the degree axioms

The norm sequence begins with the alternating determinant line inside a tensor power. Its image is a locally split line without dividing by a factorial; it is not the whole sign-eigenspace in small characteristic. For a finite locally free algebra, the determinant of multiplication supplies a multiplicative polynomial law and a symmetric-power section. The differential is the trace, direct sums multiply norms, and finite locally free towers satisfy transitivity. Universal arguments and saved examples are distinguished. The exact published comparisons are Ferrand’s polynomial-law construction and SGA 4 XVII6.3. [C-SA04-464–470; Ferrand1998, §§2.5.1,3.1; SGA4XVII, 6.3.1–6.3.15.]

Finite local freeness is substantive. Constant fibre length alone does not supply the required section. Arbitrary presheaves likewise need a symmetric-descent condition before an operation on ordered fibres descends. The invariant-orbit-sum argument commutes with base change for permutation modules without averaging by the group order; it fails for an arbitrary module action. [C-SA04-465–466,468,472.]

The single-integer degree axioms fail at the empty base: pulling any degree-r map back to the empty object makes it an identity, forcing \(r=1\), incompatible with disjoint-sum degree two. A locally constant rank or a suitable degree predicate is a repair, explicitly labelled as such. For finite sets or finite \(G\)-sets with prescribed fibre cardinalities, the multiset section and its composition are canonical. Étale covers and finite locally free schemes provide related but different models. The final contracted-product sentence remains unfinished. [C-SA04-471,473–475; MP-SA04-121–123.] A separate later comparison with Hilbert–Chow constructions is checked under its own hypotheses. [C-SA04-476; Rydh2008II, §6.]

### 5.2 Group-set sites, coverings and monodromy

The sheaf equivalence is checked by evaluating on the regular orbit and using descent to recover fixed points on quotient orbits. The variance of right translations matters for the induced left action. For infinite \(G\), the category of \(G\)-sets with finitely many orbits need not be closed under fibre products, so the Čech construction must be understood in a larger site or at the sheaf level. Coinduction preserves injectivity only after starting with an injective underlying abelian group. These details are part of the proof, not optional modernization. [C-SA04-477–482; Stacks03NP; Stacks00VZ; HochschildSerre1953.]

The low-degree Picard–Brauer sequence retains the filtration piece in degree three and the correct later differential. A fixed-cover injection can fail because a nontrivial Picard differential enters. The nonsplit real conic gives an explicit obstruction: the invariant degree-one bundle on its complexification has descent obstruction \(-1\), which is not a complex norm. This does not refute the qualified field-extension case with Artinian nerve and zero Picard groups. [C-SA04-483–484.]

The cancellation of trivial local coefficients is justified. Circle reflection acts by minus one on first cohomology; the mapping torus calculation detects the resulting two-torsion. The action cannot generally be reconstructed merely from the permutation of connected components. The corresponding interpretation is refuted conditionally, with the ambiguous acting group and ink left unresolved. [C-SA04-485–487; outputs/c_computations.txt.]

### 5.3 Bounded families, field positions and Tor/Ext

The boundedness theorem requires both quotients of a fixed coherent sheaf and a finite set of Hilbert polynomials in the projective Noetherian setting. Fixed polynomial alone is insufficient: \(\mathcal O(n)\oplus\mathcal O(-n)\) on \(\mathbf P^1\) has fixed polynomial but unbounded \(h^0\). Fixed source and associated cycle alone are also insufficient: the quotients \(\mathcal O(n)\) of \(\mathcal O^2\) have varying polynomials. Properness controls general boundedness operations; on the affine line, the cokernels of multiplication by \(x^n\) have unbounded length. These examples test the tentative strengthening, not the established FGA theorem. [C-SA04-488–495; Grothendieck1961IV, Theorem 2.1 and Proposition 1.2; Grothendieck1962Err.]

Field extensions must retain their relative positions. Transitivity of the geometric equivalence relation uses a tensor product over the specified middle field, followed by a prime quotient and a fraction field. An arbitrary prescribed compositum can destroy the alignment of two objects. A sufficiently large algebraically closed field represents every finite-data class and converts isomorphism into an automorphism-orbit statement; this does not mean that it contains every field extension. Reduced support and primary-component operations retain the source’s inseparability and nonuniqueness qualifications. [C-SA04-492–498; Stacks01ZR, Lemma 32.10.2; parts/c/analysis.md, §8.]

The Tor proof has a specific repair. A resolution free over \(B_i\) need not be flat over the common ring \(B\). Taking \(B=k[x]\) and \(B_i=M_i=k\) exposes the missed \(\operatorname{Tor}_1^B(k,k)\). Resolve instead over polynomial \(B\)-algebras surjecting onto the \(B_i\); their finite free terms are \(B\)-flat, and the kernel ideals act null-homotopically on the tensor complex, hence trivially on its homology. The stated input flatness and flatness of the required output Tor groups then give the base-change edge isomorphisms in the specified range. [C-SA04-503–506; Stacks0620, Example 15.63.3; parts/c/analysis.md, §9.]

For Ext, finite free terms prevent the common-denominator failure of infinite products. Terminal-cokernel flatness prevents a new kernel from appearing after specialization. The actual finite-complex assertion is valid in all its complex degrees under the listed flatness assumptions; only identification with Ext is restricted to the requested range. Comparison maps are checked for homotopy independence, localization and gluing. An unrestricted relative Ext hope is not supplied by a theorem requiring a perfect first argument, base-flat bounded second argument and proper support. [C-SA04-507–511; EGAIII2, §7.7; Stacks0A1J, Lemma 36.30.7.]

### 5.4 The reused typescripts

The topology sheets contain quotient and gluing exercises. The small finite-space counterexample proves the sheet’s own negative exercise about arbitrary overlaps; it is not a refutation of a positive theorem on the page. Open-overlap and closed-overlap conditions are treated separately and verified. [C-SA04-516–519.]

The abelian-variety sheets use translation-invariant line bundles, isogenies, ampleness and finite-dimensional jet flags. The Picard-zero qualification in the pullback identity is essential. Modern comparison uses Milne’s Arithmetic Geometry chapter, distinct from his 2008 course notes cited elsewhere. A first full-rank homogeneous jet system has only the zero solution; the preceding last nonzero kernel gives the intended line. The source author and the pencil annotator remain unidentified. [C-SA04-520–527; MilneAV, §§7–10; MP-SA04-131–132.]

## 6. Cote 100: abelian schemes, algebraization and Néron targets

### 6.1 The abelian/BT square and its effectivity problems

The opening draft compares an abelian scheme with its restriction to an open set and its p-divisible group over the base. Full faithfulness, essential surjectivity and representability of an algebraicity locus are different assertions. The source’s finite geometrically unibranch cover and étale-depth alternatives cannot be replaced by “normal base” without changing the problem. [C-SA04-655–657; MP-SA04-176–178.]

Grothendieck’s 1966 paper gives exact associated-point tests for existing abelian schemes and a specified morphism. Its Proposition 1.2 is not a universal closed-locus theorem. Its §2.1 open-and-closed statement has a reduced finite-type characteristic-zero setting. Section 4.9 explicitly asks the normal-base extension question; Krishnamoorthy–Pál’s Corollary 6.12 answers that case. The broader nonnormal alternatives in the archive require their own arguments. [Groth1966, Theorem 1.1 p.63, Proposition 1.2 p.64, §2.1 p.67, §4.9 pp.77–78; RKP2021, Corollary 6.12.]

The chronology is correspondingly restrained. A May 1966 letter concerns preparation of the paper, and its §4 is dated 5 August 1966. Nominal issue metadata is not evidence for an earlier circulation of the final text. Nor does physical proximity prove that every draft leaf was written for that publication. [RGrothMumford1966; Groth1966.]

The compatible-local-ring family assertion is marked doubtful and probably false by the author. The stronger uniform-neighbourhood question asks for one neighbourhood that works for every subsequent family and comparison; ordinary spreading out chooses the neighbourhood after the datum. No exact supporting theorem was located for either broad formulation. Their class D records the actual search limit and the on-page doubt, not a claim of new open problems. [C-SA04-658–660; MP-SA04-179–180.]

Proper descent of morphisms into formally unramified targets, rigidity of BT Hom, descent of abelian objects and effectivity of a marked formal moduli problem are separately recorded. Rydh’s effective descent theorem for quasi-compact étale morphisms does not establish descent of arbitrary abelian schemes. Artin’s algebraization criteria retain effectivity and versality conditions. [C-SA04-661–664; Groth1966, Lemma 1.2.1; RRydh2010, Theorem 5.17; RArtin1969, Theorems 1.6–1.7.]

### 6.2 Formal algebraization and countable curve tests

The next sequence proposes testing algebraization after proper surjection or on normalized one-dimensional subschemes, using countably many polarization loci. EGA’s ample-line algebraization theorem is a precise sufficient result; it does not prove the full unpolarized criterion. Gluing algebraizations on irreducible components also requires compatibility and effectivity on their scheme-theoretic intersections. [C-SA04-665–667; REGAIII1, 5.4.1 and 5.4.5; RKP2021, Corollary 7.7.]

Two local steps are completed in the audit. For a proper smooth formal scheme over a complete Noetherian local base, algebraization lifts through a nilpotent thickening by the \(H^2\) obstruction, \(H^1\) choices and \(H^0\) automorphisms, compared with their formal counterparts. This is the smooth lemma; EGA’s broader reduced-base question must not be cited as its proof. The countable-avoidance lemma is proved by finite Cohen normalization and a Baire specialization. The resulting curve is not contained in any prescribed proper closed subset; it need not be disjoint from them, since they may all contain the closed point. Class D for that lemma concerns an unlocated exact publication, although its mathematical proof is supplied. [C-SA04-668–669; MP-SA04-188–189; parts/root_computation_notes.md; parts/b/root_review_merge_proposals.md.]

The extensions to proper flat schemes and pairs \((X,L)\) retain the Picard-zero correction and distinguish uniqueness from effectivity. Lack of infinitesimal automorphisms does not imply algebraization, and \(L\) is not explicitly ample in the relevant passage. Pro and Codex disagree about rational projectivity versus projective algebraicity, AND versus OR in a pair of conditions, and projective versus quasi-finite covers. These differences are included in the reading table and in the claim qualifications. [C-SA04-670–671; MP-SA04-190–191; parts/a/c100_codex_witness_audit.md.]

### 6.3 The Raynaud typescript and its generalization

The final typescript treats morphisms from a p-divisible group to an S-Néronian group over a trait. Connected–étale reduction, semistability, finite base change and smoothening are steps in its argument. The initial semiabelian generic-fibre restriction is bracketed and marked unnecessary; the final handwritten application explicitly treats an arbitrary Néronian target. That progression is preserved, rather than stopping at the first formulation. [C-SA04-672–675; cote 100 scans 48–53.]

The exact primary parallel is SGA 7 I, IX5.9 and 5.9.1, with Raynaud attribution. Its proof distinguishes a pushout-representability hypothesis and an unpublished input. IX5.11 states exactly how unrestricted Tate full faithfulness removes the remaining generic-characteristic limitation. De Jong supplies that later input. The archive also claims a restricted multiplicative-target case and calls the étale-target case easy; those sentences do not constitute a proof of unrestricted equal-characteristic Tate. [SGA7I, IX, pp.382–386; deJong1998; deJongErratum1999.]

The no-additive-subgroup step is both matched to BLR and independently proved. If a closed embedding \(\mathbf G_{a,K}\to G_K\) existed, its nonzero tangent vector \(v\) could be scaled by every \(\pi^{-n}\). The Néron property would extend each scaled map over the DVR. Thus every \(\pi^{-n}v\) would lie in the finite free Lie lattice of the model, forcing \(v\) into the intersection of all its \(\pi^n\)-multiples, which is zero. This proves the exact rationale for the broader target, without certifying every image or representability step. [C-SA04-676; RBLR1990, §10.1 Proposition 8, pp.293–294; independent proof and targeted review in the appendices.]

### 6.4 GIT, EGA corrections and correspondence

The GIT preface and examples belong to Mumford’s reused text. Its geometric-reductivity conjecture is matched to Haboush’s theorem. The p-power-degree formulation follows from extracting the appropriate coefficient of an invariant evaluated at \(x+tv\), with a nonzero binomial coefficient modulo p. Kempf’s optimal destabilization keeps the source’s perfect-field hypothesis; an imperfect-field extension requires additional results. The checked action example has a geometric quotient and trivial stabilizers while the action is not proper. [C-SA04-677–680,687; RHaboush1975; RSastrySeshadri2011; RKempf1976; RKempf1978; RBate2013.]

The literal finite-isometry fixed-point statement for a convex building set is too strong: the quaternion group acting on the whole rank-one building supplies a counterexample. The modern Centre Conjecture includes a subbuilding alternative and its precise building hypotheses. Its resolution therefore cannot be substituted verbatim for the printed sentence. [C-SA04-681,695; RRamosCuevas2013.]

The EGA correction leaves have identifiable dates for their own documents. The conormal basis argument appears in the final EGA IV4, 19.1.5. The proposed non-Noetherian openness strengthening is not already the printed EGA IV3, 15.6.3, which still inherits local Noetherianity. An unidentified errata sheet remains unidentified. Illusie’s letter is on **scan 30**, dated 24 February 1968 in both witnesses; it concerns editorial plans for Riemann–Roch and Künneth material, not a complete theorem proved in the letter. [C-SA04-683–686; EGAIV4, pp.186–187; REGAIV3, p.237; RIllusieLetter1968.]

## 7. What changes in the earlier notes

The verdict table is the authoritative entry-level account. The most useful changes fall into the following categories.

| Issue | Retained conclusion |
|---|---|
| A note accurately diagnoses a false formula | Keep the note’s textual verdict; record the claim’s counterexample separately |
| Deligne’s singular genus-one convention | Withdraw the audit’s initial missing-discriminant alarm; preserve the actual definition |
| An apparently global surjectivity or uniqueness statement | Distinguish sheaf-local existence, global sections and the extra target hypotheses |
| Zero-index interpretation and isolated cancellation words | Retain as conditional earlier-run ideas where the two witnesses differ |
| Characteristic-two Lie reconstruction | Record concrete structural failure without discarding the valid group quotient |
| Cote 98 flatness, kernels/extensions and finite-complex scope | Preserve corrections already present in the supplied current notes |
| Serre’s printed results and neutral-component comparison | Preserve authorship, hypotheses and the difference between a theorem and a requested direct proof |
| Néron target generality | Include the source’s later removal of the semiabelian restriction |
| Apparent duplicate problems | Merge exact repeated formulations while retaining all source occurrences and proof/refinement IDs |
| External project interpretations | Keep their originating note IDs and run names; do not promote unseen packets to checked results |

The 163 reading alarms are not 163 proven transcription errors. Some are simple signs or indices, others are genuine witness conflicts, missing definitions, cancellation scope or possible imprecision in reused print. Their weight measures mathematical dependence; their confidence concerns the evidence for inspection. No diplomatic reading was changed.

## 8. Present state and future directions

The most productive unresolved targets are sharply bounded formulations: the generated target in integral Schwarzian universality; relative enlarged-monodromy reconstruction; formal exactness and stratification under weaker smoothness hypotheses; abelian/BT effectivity beyond normal bases; the polarization-locus step in curve-test algebraization; and the exact comparison-data category in the Hodge–Tate draft. These survive the audit because the checked literature has different quantifiers or because the source leaves a mathematical definition incomplete.

Other tasks are mainly companion-writing or scan work. The Manin equality, the smooth nilpotent algebraization lemma, the countable-avoidance argument and the no-additive-subgroup step are already checked here. The rational Verschiebung criterion and eigenvalue-multiplicity formula have explicit negative answers. Repeating them as open research proposals would misstate the result of this run.

SA04_directions contains 30 ranked tasks, each tied to item, claim and problem IDs, with its aim, known boundary, first concrete step and a separate few-hour feasibility assessment. Its top positions concern integral Schwarzian universality, relative monodromy and formal exactness; high intellectual interest does not mean a few hours can settle the general problem. The next run should choose one of those bounded tasks. None of the directions is developed here beyond the proof checks needed to decide the present source claims.

The links table has three explicit kinds. Folder links compare supplied endpoints and distinguish an authorial cross-reference from an audit connection. Published-work links identify exact passages. The “our projects” rows, also extracted into the separate SA04_project_leads table, preserve the links made by the earlier notes to La Longue Marche, Les Dérivateurs, S6, S20, Hua98 and named runs. Their source-note endpoints were read; absent project packets and external cotes remain leads, not independently verified destination results. The separate archive leads to cotes 159 and 64 likewise await those sources. This keeps the topic’s own constructions from being rewritten through later project vocabulary.

## 9. Evidence, computations and reproducibility

The detailed analyses and proof appendices in parts/a, parts/b, parts/c and the root notes support the registers. Search ledgers retain actual query groups, primary URLs, checked locators, failed retrievals and a claim-level mapping to searched fates. A mapping row is not counted as another search. The search used Numdam, arXiv, EGA, SGA, author papers and bibliographies, collected-work catalogues, zbMATH discovery and MathOverflow leads. Inaccessible records and unsuccessful exact searches are recorded rather than silently filled from memory.

The saved programs and proof appendices distinguish three forms of evidence:

* **Universal algebra or proof:** polynomial identities over a specified universal ring, exact chain or module arguments, and written proofs with all retained hypotheses.
* **Exact finite computation:** explicit characteristic-two groups, finite-field point counts, matrices, truncated power series and small cochain complexes, with their finite range stated.
* **Source and structural checking:** line navigation, indexing, serialization, identifier resolution, bibliography normalization and package validation.

No source verdict was generated by matching a heading or keyword. The serialization programs contain judgments already made by direct reading. No finite sample is labelled a universal proof without its accompanying argument.

CHECK_EVENTS records textual use, targeted proof checking, independent re-proofs, computations, carried background and refutations at the level actually performed. A theorem read in a reference is not marked independently reproved. A reviewer of another stream’s proof is not credited with a separate proof or with opening a reference they did not open. The model is GPT-6 Astra Pro; a numerical reasoning-effort setting was not exposed and is not invented.

The original attachments, downloaded primary PDFs and raw source OCR are not duplicated in the ZIP. SOURCE_MANIFEST records the supplied inputs; bibliographic and retrieval ledgers record external sources. The original supplied archives are needed to rerun source-navigation checks. Some earlier helper programs retain the original workspace path; REPRODUCING.md explains relocation. The final data files are canonical, while component files preserve the stages and corrections that produced them. ID_ALIASES records the exact retired IDs; older component counts are pre-consolidation counts.

The final checks verify the 432-entry bijection, required fields and vocabularies, active identifiers, bibliography resolution, event coverage, source bounds and cote boundaries, direction references, and package contents. Their scope is structural and evidential consistency; it is not a machine proof of every mathematical theorem in the dossier.


## 10. Final register counts

These counts describe the final consolidated registers. Component audit files retain their earlier local counts as provenance. A status on the pages is distinct from a literature class and from present truth.

| Register | Count |
|---|---|
| Indexed source entries | 432 |
| Consolidated items | 448 |
| Claim records, including explicit audit refinements | 372 |
| Historical problems and questions | 131 |
| Undecided scan-reading alarms | 163 |
| Links | 90 |
| Check events | 1422 |
| Bibliography records | 140 |
| Ranked future directions | 30 |
| Catalogue rows inventoried | 30 |
| Other-part catalogue rows, inventory only | 27 |

### Entry verdicts

| Verdict | Count |
|---|---|
| kept | 276 |
| merged | 120 |
| corrected | 33 |
| withdrawn | 3 |
| rests on a misreading | 0 |

The zero count in the last category does not imply that no mathematical reading alarm exists. The supplied notes often already identify the defect, or their conditional interpretation is retained with a correction.

### Item kinds

| Kind | Count |
|---|---|
| conjecture | 11 |
| unproved claim | 150 |
| unpursued implication | 4 |
| idea of the earlier run | 42 |
| reading question | 75 |
| self-flagged step | 67 |
| withdrawn in the same text | 19 |
| title, date or page count | 13 |
| other | 67 |

There are 65 transcription-derived or audit-supplement items without invented index rows. The 89 nested cote98 items deliberately repeat their composite parent’s source-entry ID; this does not create extra verdict rows.

### Claims by literature class

| Class | Meaning | Count |
|---|---|---|
| A | Exact assertion in his own published work; attribution and chronology qualified | 38 |
| B | Developed by others into an established result | 97 |
| C | Partly developed, or an exact broader scope remains unsupported | 72 |
| D | Exact development not located after the recorded search | 3 |
| E | Previously known or standard in the stated setting | 135 |
| F | Not identifiable as one precise retained theorem | 27 |

The three class-D records are C-SA04-659,660,669: the doubtful local-ring effectivity lemma, the uniform-neighbourhood question, and the countable-avoidance lemma. The last has a completed proof in this audit; class D concerns its exact bibliographic match.

### Claims by status on the pages

| Status | Count |
|---|---|
| proved there | 36 |
| proof sketched | 137 |
| stated without proof | 85 |
| corrected by himself later | 15 |
| false as stated | 34 |
| open on the pages | 65 |

The false-as-stated count includes conditional literal readings and reused printed material. It is not a count of certain errors by Grothendieck. Counterexamples and the exact hypotheses they test are given in the corresponding records and proof appendices.

### Links and bibliography

| Link kind | Count |
|---|---|
| folder | 26 |
| published work | 33 |
| our projects | 31 |

| Reference status | Count |
|---|---|
| verified | 136 |
| unverified | 4 |

The four unverified original works are Cohen1959, HillePhillips1957, Spencer1969 and RWanderley1981. The Wanderley offprint is supplied evidence; its external reference lacks an opened reliable URL or DOI. The other records distinguish later checked citations from an original text not opened.

### Check events by actual operation

| Operation | Count |
|---|---|
| carried as background without fault found | 6 |
| computation or formal certificate | 113 |
| independent re-proof | 146 |
| refuted, with the refined statement's id | 39 |
| targeted proof check | 40 |
| used and rechecked in this run | 1078 |

Each event’s outcome states its scope. These totals count logged operations, not independent theorems or independent human reviewers.
