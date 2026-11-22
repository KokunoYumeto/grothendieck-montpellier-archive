# Part C source and search log

Run: GPT-6 Astra (OpenAI, inherited reasoning effort), `/root/part_c`, 20 November 2026. We assert no priority. Searches were for verification and comparison, not evidence of novelty.

## Manuscript and attached study rechecked

- `Codex_K29-08/K29-08_transcription.tex`: scans 131, 137–140. We re-read the relative functor, definition of admissibility, pointed rigidity, minimality and the initial Proposition 4.
- `Codex_K29-09/K29-09_transcription.tex`: scans 141–143. In particular, lines 21–25 explicitly impose closure under kernels of pairs and admissibility. The indicated transcription doubts concern other words and do not affect that condition.
- `study/readings/c29a.md`, discussion of scan 139: the cusp is valid for the broader assertion. We independently reconstruct it and prove that it remains minimal even when nonflat closed subgroup reductions are admitted in the fppf sense.
- `study/readings/c29b_c31.md`, scan 141–142 discussion: the proof on scan 142 invokes the desired uniqueness circularly. This invalid proof does not refute the literal kernel-closed assertion; the orbit-support argument supplies a valid proof.

## Searches and opened sources

Search families included: “Nori fundamental group reduced connected nonproper”; “finite flat torsors normal scheme fundamental group”; “Borne Vistoli finite stack reduced every morphism flat”; “pointed torsors representable proper flat nonreduced”; “Hall Rydh Hom stacks proper flat finite presentation”; “Raynaud Picard Cartier duality Proposition 6.2.1”; “SGA 1 XIII 6.2 constructible stack”; “SGA 3 finite flat quotient theorem 4.1”; and “SGA 3 height one groups restricted Lie algebra 8.1”.

1. Borne–Vistoli, arXiv:1204.1260v5. TeX archive and PDF downloaded. Section 5, especially Proposition 5.5(b), Theorem 5.7, Lemmas 5.12–5.13 and Remark 5.15, read against the PDF. Lemma 7.15(c) states that every morphism to a reduced finite stack is flat; its proof was read.
2. Nori, *The fundamental group-scheme* (1982), original repository PDF at `https://repository.ias.ac.in/36451/1/36451.pdf`. The local download initially failed, but the indexed full PDF opened successfully. Chapter II, §1, Definition 1 and Propositions 1–2, printed pp.85–87, were read in full, including the quotient/image proof. This directly confirms that properness is unnecessary with a rational basepoint. Web parser references: `turn290412468view0`, `turn360012276view0`.
3. Antei–Emsalem–Gasbarri, arXiv:1504.05082, TeX downloaded and the introduction/normal reduction read. Their relative group base must not be confused with the torsor base S of C.1(i).
4. SGA 1, arXiv:math/0206203, TeX downloaded. Exposé X, Proposition 1.2 and Theorem 1.3, establish the finite étale Stein component scheme for a proper flat family with geometrically reduced fibres. Exposé XIII, Corollary 6.2, gives 1-constructibility of the proper direct image of a 1-constructible stack. These exact hypotheses were checked.
5. Hall–Rydh, author PDF `https://davidrydh.se/papers/tannakian20181031.pdf`. Theorem 1.2 explicitly requires proper, flat, finitely presented source, and gives algebraicity, local finite presentation and affine diagonal for the pointed torsor stack. It does not assert that its class functor is a sheaf.
6. Raynaud, *Spécialisation du foncteur de Picard* (1970), Numdam original PDF. Proposition 6.2.1(1), Lemma 6.2.2 and proof, printed pp.50–51, opened. The proposition concerns relative R¹ and Hom into Pic; global pointed classes follow using the section and trivial pointed inertia. Web parser reference: `turn648453368view1`.
7. Mehidi–Poiret, arXiv:2407.10924, TeX downloaded. Theorem 2.2 and Remark 2.3 state the Raynaud correspondence in a convenient explicit form; the original source was subsequently opened rather than relying solely on this citation.
8. SGA 3 I, official Gille–Polo re-edition PDFs at `https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp5-13oct24.pdf` and `Exp7A-13oct24.pdf`. Exposé V, Theorem 4.1(iv), and VIIA, Theorem 8.1.2/Corollary 8.1.3, downloaded and read. The former applies because the quotient source is affine; the latter classifies subgroups of αp² as linear subspaces.

## Computation record

`code/check_counterexamples.py` performs exact arithmetic over GF(p) and symbolic Gröbner reductions. The current output contains 17 checks, elapsed 0.061371275 seconds. It verifies the cusp pushout and kernel fibre lengths for p=2,3,5,7; the smooth-surface pushout and nonflat-closure generator counts for p=2,3,5,7; the height-two family at p=2,3,5; the quadratic invariant algebra at p=3,5,7; the sign-eigenspace and cube-zero identity at p=3; the discriminant/Hasse coefficient of y²=x³−x in characteristic 3; and the two pointed maps of the trivial C2 torsor. These algebra checks do not purport to formalize descent, global connectedness, minimality or algebraic-stack representability: those arguments are written in the paper.

## Failed approach retained

The initial attempt to prove necessity in C.1(iii) used the αp² class `(m,h^p m)`. It fails because the class reduces through the allowed varying embedding `(1,h):αp→αp²`. We replaced it by the height-two group αp² × αp, whose kernel changes isomorphism type between αp² and αp × αp. The old attempt is not used in any checked statement.

## Gates recorded before the 01:57 completion

At the earlier stage, the exact kernel-lifting criterion covered every category satisfying the stated closure assumptions. The wider all-S-map constant-object variant was classified with rational marking, and in positive characteristic refuted whenever Γ(S,O) was not a field under geometric marking. The remaining field-descent issue was subsequently closed by C:all-constant-classification, as recorded below. We still do not replace it by the false claim that every finite L-subgroup of a k-descended group itself descends to k. Positive moduli refinements without finite presentation remain outside the hypotheses proved; the original universal representability questions are already refuted.

## 01:20 UTC: additional source and certificate

Vélu, *Isogénies entre courbes elliptiques*, C. R. Acad. Sci. Paris A273 (1971), 238–241, opened in Alexandru Ghitza's English translation at `https://aghitza.github.io/publications/translation-velu.pdf`, §3 equations (8)–(11), Remark 3. The source supplies the quotient isogeny and its field of definition. The specific degree-three identity is independently reduced to zero in `check_field_descent.py`. The proposed unrestricted 'global functions is a field' criterion is refuted by C:field-descent in characteristics zero and five.
## 20 November 2026, 01:42–01:57 UTC: exact descent criterion and A.2 audit

We searched `finite group scheme proper subgroup epimorphism`, `finite group schemes observable subgroup`, and `finite group scheme connected etale sequence arbitrary field`. The results locate the general theory of epimorphic/observable algebraic subgroups but no source was used as authority for the stronger finite-target-with-k-descent assertion. We prove that assertion in C:detect-proper-subgroup and claim no priority. We opened Edixhoven--van der Geer--Moonen, *Abelian varieties*, Chapter IV, Proposition 4.45 (author-hosted `https://www.math.ru.nl/~bmoonen/BookAV/Quotients.pdf`, dated 15 September 2011), for the precise arbitrary-field connected--etale sequence and perfect-field splitting. The finite quotient theorem remains SGA3 I V4.1(iv).

The exact geometric marking is in scan29/126, supplied K29-08 transcription lines80–84. Stacks Theorem59.45.2, tag04DZ (`https://stacks.math.columbia.edu/tag/04DZ`) was opened to check the cusp normalization's invariance of finite etale covers. The new program `code/check_pointing_and_detection.py` checks all25 GF25 elements, Frobenius fixed field and lack of rational points on the quadratic field torsor; it also exhausts all12 proper subgroups of cyclic groups of orders2–8 in the two-copy permutation construction. Output is `output/check_pointing_and_detection.json`, elapsed0.004885775 seconds.

For the A.2 approximation note, we opened Artin SGA4 XIV Corollary3.2 in the official re-edition, and Stacks Theorem59.51.3 (09YQ), Lemma59.51.4, Lemma59.73.2 and Lemma59.73.10 (09YU). These provide separately descent of constructible coefficients, continuity through affine inverse limits, generation of arbitrary torsion sheaves by constructibles, and commutation with filtered colimits. No finite computational example is needed for these two general lemmas. The original Raynaud PDF download, previously incomplete, was resumed successfully and validated as a51-page6,849,906-byte PDF; it is now saved as `sources/raynaud_picard.pdf`.

## 20 November 2026, 02:00–02:19 UTC: imperfect-field B.2 support

We re-read the checked B.1f--g finite-group detection argument and normal-to-regular birational Picard invariance, and the imperfect-field counterexample in B.2i. We opened the saved primary text of Schroer, *Albanese maps for open algebraic spaces*, revised 07/2023, Proposition 3.3, Lemma 4.1, Theorem 6.1 and Proposition 6.2. The arguments bound and stabilize maximal abelian parts in filtered compactification categories; they do not assert geometric normality of the relevant normalized graph. Searches for arbitrary-field alteration and Albanese base change led back to de Jong's regular alteration theorem and the same pure-inseparable descent issue. We did not substitute a smooth-over-k alteration for a regular alteration without checking the field hypotheses.

We proved the support lemma in `B2_norm_notes.tex`: the full Picard-sheaf pullback kernel of a proper generically finite map between normal integral varieties is killed by the generic degree, using its normal finite Stein factor. Primary statements and proofs opened directly: Stacks 31.18.2 (0BCY), 31.18.6 (0BD2), 31.13.12 (0EBJ), 31.13.13 (0AY6), and 30.5.2 (02KH). Flat base change for the open immersion is what preserves Hartogs extension on nonreduced test schemes. Combined with B.1g and a fixed-Jacobian embedding, this gives a uniform bound for kernels along a fixed regular alteration. There is no finite example and hence no finite computation associated with these general lemmas. The uniform bound for images needed to settle the weak imperfect-field stabilization remains unproved.


## 20 November 2026, 02:20–02:44 UTC: source-scope audits and remaining B.2 search

We opened SGA4 XVIII3.2.5, originalpp585–586, at https://www.normalesup.org/~forgogozo/SGA4/18/18.pdf and IX2.11, originalp20, at https://www.normalesup.org/~forgogozo/SGA4/09/09.pdf. The relative-duality theorem allows the arbitrary quasi-compact quasi-separated base needed in D.10. We opened Raynaud1972 Chapter4 section4 Proposition5, originalp30, at https://www.numdam.org/item/CM_1972__24_1_11_0.pdf: its blowup preserves the whole specified quasiprojective open. The D.5/Prop5 audit used the supplied primary transcription Codex_K29-02/K29-02_transcription.tex, scans191 and196–197.

For the B.2 image gate we searched `geometrically normal normalized graph Albanese`, `What Determines an Algebraic Variety 11.3`, and `smooth alteration imperfect arbitrary field`. Primary author-hosted draft copies at https://max.lieblich.us/wp-content/uploads/2021/09/reconstructionweb.pdf and https://williamsawin.com/ReconstructionBook.pdf both contain Lemma10.3.5 and section10.3.9 with an explicit perfect-field hypothesis (printed177–178). They therefore cannot be cited for imperfect-field geometric Cartierization. Conrad's alteration notes at https://math.stanford.edu/~conrad/249BW17Page/handouts/249B_2017.pdf explain why regularity rather than k-smoothness is the general arbitrary-field conclusion, and why finite inseparable constants enter the proof. The sharper possibility of smooth alterations for a geometrically normal proper input is still under investigation; no such theorem has been used.

## 20 November 2026, 02:50 UTC: principal-completion audit for A.2

Independently opened Hall–Rydh, Mayer–Vietoris squares in algebraic geometry, author PDF https://people.kth.se/~dary/mayer-vietoris20210707.pdf, Remark6.7, pp21–22: for affine henselian pairs in a weak Mayer–Vietoris square, cohomology of the open complements agrees for every torsion abelian sheaf. The noetherian statement is attributed there precisely to Fujiwara Corollary6.6.4; completion is an explicit special case. Independently opened Kurano–Shimomoto, Ideal-adic completion of quasi-excellent rings (after Gabber), https://www.isc.meiji.ac.jp/~kurano/ronbun/kurano40.pdf, Theorem5.1 p7, lifting quasi-excellence from A/I when A is I-adically complete and noetherian. These exact hypotheses validate root's t-adic completion proof for a strict henselian regular equicharacteristic-zero surface after inverting a parameter. The original Nagata–Gabber example therefore does not give persistent failure under all further shrinking.

## Complementary sources opened after 02:50 UTC

Bhatt–Mathew, The arc-topology, arXiv1807.04725v4, Theorem6.11 printedp50, https://arxiv.org/pdf/1807.04725v4, was independently opened: its full derived comparison is for every torsion etale sheaf and every finitely generated henselian ideal. Bhatt–Carvajal-Rojas–Graf–Schwede–Tucker, arXiv1611.03884, https://arxiv.org/pdf/1611.03884, Proposition3.2 pp3–4 and Corollary4.2 with second proof pp6–8, supply D's finite-local-fundamental-group criterion without a quasiprojectivity assumption. Lipman1969, https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf, Definition1.1 and Proposition1.2(2) printedpp199–200, and Theorem12.1(i) printedpp220–221, were independently opened for B's arbitrary-field surface stabilization proof. The latter theorem needs properness, fibres of dimension at most1 and H1(O)=0, and concludes triviality of a line bundle of degree zero on every exceptional integral curve.

The new arithmetic search asks whether non-Galois towers of number fields can preserve infinitely many direct-limit Pic/p classes while forcing eventual inertness at every fixed prime. Successive cyclic p-extensions with growing finite local inertness prescriptions could ensure finite splitting, bounded ramification at each prime, and infinite local residue degree; class-group growth alone would not prove persistence. Searches for positive mu without completely split primes led to Hubbard–Washington's noncyclotomic examples and work on variation of Iwasawa invariants, but no class-group mod-p injectivity theorem with the required local prescriptions has yet been verified.

## 20 November 2026, 03:40 UTC: cofinal Picard obstruction and overring audit

For the threefold construction, independently opened Achter, Casalaina-Martin and Vial, author manuscript dated17March2025, https://www.math.colostate.edu/~achter/math/alb.pdf, Theorem3.2 and Remark3.3, printedpp12-13. The latter states the precise duality between the Albanese variety and the maximal abelian subvariety of the Picard scheme for proper geometrically reduced schemes. Published metadata identifies Annales de l Institut Fourier76(2)(2026),789-828, DOI10.5802/aif.3721. The finite separable marking is essential: extending only after an algebraic closure would not preserve the obstructing k-DVR. B supplied the primary Milne2021 chord-and-tangent locator and exact elliptic certificate.

For the A.2 overring audit, independently opened https://stacks.math.columbia.edu/tag/00PG, Lemma10.119.12, whose statement includes every intermediate ring in a finite extension of the fraction field of a one-dimensional Noetherian domain. Read the full downloaded Swanson-Huneke Integral Closure Theorem4.10.5 proof, pp90-92: normalization in the own fraction field is Krull, without a finiteness assumption. The theorem exactly supports the DVR intersection used by root.

## 04:06 UTC — the alteration realization and no-torus audits

Opened Stacks https://stacks.math.columbia.edu/tag/0B8F, Lemma79.10.2: separated group algebraic spaces locally of finite type over a field are schemes. Opened https://stacks.math.columbia.edu/tag/05Y8, Proposition97.11.5 and base-change Lemma97.11.2 for Weil restriction. These sources avoid an unstated quasiprojectivity step for the comparison group. Read deJong1997 local primary source Situation5.3 p613, Theorem5.13 and Corollary5.15 pp619-620 again: over kperf regularity gives smoothness, but finite separable constants must be retained. The new semilinear descent proof treats these explicitly.

## 04:18–04:26 UTC: arithmetic construction primary checks

- Milne, CFT v4.03: https://www.jmilne.org/math/CourseNotes/CFT.pdf; read local primary PDF text at V3.5–3.6p158, Exercise3.15p160, transfer V3.18p162, Chebotarev V3.23p164; III1.8p100 and VIII4.2p241. Web opens turn327394974view0, turn955067931view3, turn908530816view2. Ray-class existence, ideal-extension compatibility, and local/global Brauer assertions verified.
- Milne, ANT v3.08: https://www.jmilne.org/math/CourseNotes/ANT.pdf, Theorem4.3p70; web turn955067931view2 and turn908530816view3. Read exact Minkowski bound and its ideal-norm formulation.
- Popescu–Vraciu1985: https://www.numdam.org/item/RSMUP_1985__74__39_0.pdf, theorem pp40–41 and corollaryp42; web turn955067931view1 and turn110184022view1. Independently checked finite-splitting/discrete-valuation criterion; the text supplies a direct proof too.
- Stacks https://stacks.math.columbia.edu/tag/07QS, Proposition15.53.3(4); web turn110184022view0. Read exact characteristic-zero Dedekind excellence assertion and proof references.
- NSW electronic primary text sources/NSW/NSW2.3.txt lines28504–28525: Proposition8.3.18 gives cd2≤2 for a totally imaginary number field with all primes allowed. The descent to cd1 in the constructed limit is proved in the manuscript by permutation modules.

### 2026-11-20: surface local and global additions

- Opened Carvajal-Rojas–Yasuda2025 published primary PDF https://ems.press/content/serial-article-files/50862 ; Proposition6.5 proof pp742–744, different/depth discussion. Its KLT comparison does not give a uniform positive normalized fierce-different bound. Our explicit q-family refutes such a bound.
- Opened de Smit author PDF https://pub.math.leidenuniv.nl/~smitbde/papers/de_smit_ram_gps.pdf ; §§2–4 double ramification filtration. No unproved consequence used.
- Opened Tanaka2014 published full PDF via Cambridge DOI10.1215/00277630-2801646 ; Propositions3.25–3.26 pp23–24 have one exceptional curve; Theorem5.3 proof p50 explicitly uses proper Q-factorial surface projectivity in characteristic p.
- Opened Stacks0B5Y,0B5U,0C6R,0C6Q,02OC,02KH for the direct finite-thickening proof of rational-tree Q-factoriality.
- Opened Fujino2012 published PDF https://ems.press/content/serial-article-files/41165 ; Lemma2.2 p344, and author's logsurface24.pdf pp6–7. Recorded global C convention; reproduced the characteristic-independent proof with an explicit positive self-intersection check. Opened Stacks0C5P for projectivity of proper regular surfaces.

### Graded-cone lift sources

- Published ILO XXI, Theorem1.4, p529, explicitly gives finite H1 of every normal excellent strictly local surface puncture with every finite group. Re-read local published text; this is stronger than relying on a global smallness consequence.
- Opened Milne author https://www.jmilne.org/math/CourseNotes/AGS.pdf , VI Theorem11.1 pp82-85, including the arbitrary-Hopf-algebra limit step. Root independently opened Takeuchi1972 Theorem3.1.
- Opened https://www.jmilne.org/math/Books/iAG2022.pdf , Corollary16.16 p329 and Theorem16.13 pp328-329.
- Opened Stacks0B3D,00R4,09XD,09XI and0ALI. Exact scope includes arbitrary test rings for henselian/idempotent statements.
- Esnault-Shusterman-Srinivas author141_ess.pdf Theorem2.5 concerns ramification killed by one finite cover; it does not supply a consequence from a numerical different bound alone. Hiranouchi bounded-modulus smallness results likewise do not close the residual full finite-generation question.


### 2026-11-20 05:26--05:30 UTC: weighted graded extraction

Primary sources opened and read directly:

- https://stacks.math.columbia.edu/tag/0EGH — Lemma 10.56.2, sufficiently divisible standard Veronese; proof read.
- https://stacks.math.columbia.edu/tag/03GV — Lemma 37.19.2, normalization commutes with smooth base change.
- https://stacks.math.columbia.edu/tag/02RS — Lemma 42.18.1, norm formula for principal divisors; no separability assumption.
- https://stacks.math.columbia.edu/tag/0BG4 — Lemmas 54.11.1, 54.11.3, 54.11.6, respectively completed local rings at special-fibre points, descent of primary blow-ups, and descent/base-change of finite normalization when the completed complement is normal. Full proofs read.
- https://stacks.math.columbia.edu/tag/0BFK and https://stacks.math.columbia.edu/tag/0H7S — normality and regularity ascend along regular maps.
- https://stacks.math.columbia.edu/tag/0AG0 — regular local rings are UFDs.
- https://stacks.math.columbia.edu/tag/02M9 — finite locally free constant-rank modules over semilocal rings are free.
- https://stacks.math.columbia.edu/tag/01CM — Lemma 17.22.5, internal Hom of a finitely presented module commutes with flat pullback, giving reflexive-power descent.

Searches used both engines and exact official Stacks pages. The proof avoids citing a characteristic-zero toric Q-factoriality theorem and avoids assuming Q-factoriality ascends to completion.


### 2026-11-20 05:35--05:41 UTC: proper curve fibrations

- Read `parts/C/sources/sga1/smf_doc-math_3_01.tex`, Expose X Definition1.1/Corollary1.4 originalpp261--263, Theorem2.6 pp272--273, and ExposeXIII Corollary2.12 pp392--393. The exact homotopy hypothesis is proper and separable, where separable means flat with geometrically reduced fibres.
- https://stacks.math.columbia.edu/tag/054L and /03QO: etale smooth coordinates and a section over a strictly henselian local base.
- https://stacks.math.columbia.edu/tag/03H0: full Stein factorization, geometric connectedness and the relative normalization.
- https://stacks.math.columbia.edu/tag/05DT: Lemma10.44.2, separability is equivalent to reduced tensor product with F^(1/p). Full proof read.
- https://stacks.math.columbia.edu/tag/037P: relative algebraic closedness gives geometric irreducibility.
- https://stacks.math.columbia.edu/tag/0C0E: geometric reducedness is open for flat proper finitely presented morphisms.

No smoothness assertion is inferred from geometric reducedness. No finite-generator claim is inferred merely from smallness: the finite inertia images are killed explicitly before applying the proper-curve theorem.

### 2026-11-20 05:49--05:55 UTC: logarithmic fibration sources
- Opened full author primary PDF https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf ; read Proposition2.1 pp13--14, Theorem2.3 pp14--16, PropositionA.10 pp57--58 in the preserved primary PDF/text. Base trivial log structure removes the reduced-covering-point limit; the tame category is explicitly defined at codimension-one boundary points. Existing key Hoshi2006B is used.
- Independently opened https://stacks.math.columbia.edu/tag/0BXT (Lemma33.27.4), /0B8Y (Lemma33.43.8), /0EXY (Lemma15.116.9), /0EYD (Lemma58.31.1), /04DY (Theorem59.45.2 in Section59.45). Full exact statements and proofs read. The first normalization makes the generic curve geometrically normal; further pure base change separates the finite marked residue fields while preserving smoothness.

### 2026-11-20 05:56--06:00 UTC: generic arithmetic image and wild-source audit
- Opened https://stacks.math.columbia.edu/tag/0BTX and /056V; read complete exact statements and proofs. Read original SGA1 X2.9 proof in preserved primary TeX lines17180--17261.
- For B wild-source companion, reopened https://stacks.math.columbia.edu/tag/0BMB and /0A48; read complete purity and proper-henselian finite-etale comparison. Inspected the full22-assertion certificate and its preserved output without rewriting B files.

### 2026-11-20 06:07--06:15 UTC: projective targets and bases
- Opened and read complete https://stacks.math.columbia.edu/tag/0BFP and /03H0 for the Stein/birational target reduction.
- Opened and read complete /03GV, /02VN, /09EB, /09EE, /09EH and /0BUA for normalization under smooth base change, fpqc etale descent, degree formula, wild inertia and inverse limits. The current09EE explicitly corrects the earlier inseparable-residue description; only the valid group/order statements are used.
- Reread /037P and /0BXT to distinguish geometric irreducibility from reducedness over a higher-dimensional base function field and to justify finite pure geometric normalization.
