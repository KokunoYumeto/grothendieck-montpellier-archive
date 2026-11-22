# RESEARCH_SA16_SA18: Grothendieck's elliptic curves and abelian varieties dossiers (cotes 62-64 and 45-56). Galois cohomology with infinitesimal kernels over fields of dimension ≤ 1 (45:2-17), the Fourier transform of abelian schemes over a base (cote 47), the abelian subscheme of Pic and purity for good reduction (cotes 49, 51), Chevalley groups over Z from their Lie algebras (45:37-42), tori outside Borel subgroups (45:45-57), coherence (cote 55), and the moduli of elliptic curves (cotes 62-64)

To be settled: the main question (Part A) is his theorem of 45:2-17, which the readings found resting on a false step.
- His Lemma 4 (45:8-9) uses N_G(𝔥)·K = G for 𝔥 a Cartan subalgebra of an infinitesimal kernel K, and SL_2 with its
  Frobenius kernel refutes that step.
- Let k have characteristic p, with Br(K') = 0 for every finite separable K'/k (for example F̄_p(t)).
- The question: is H^1_fppf(k, G) → H^1_fppf(k, G/K) onto for every affine algebraic group G and every infinitesimal
  normal subgroup K, and is every nonabelian H^2 class of an algebraic lien over k neutral? Settle both, proved or
  refuted.

The same dossiers carry further questions, Parts B-I, one cluster of related questions.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA16_SA18`.
Drafted on 19 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), agent a28ea31fa17dd65e1, at the word of the main
session (Claude Opus 5.5 at effort max), from the sweep-3 readings of these cotes. The readers, both Claude Opus 5.5 at
effort max, read against the scans:
- acce857b533827439 read cotes 45-56 in full;
- a56665404be0d8be6 read cotes 62, 63 and 64 in full.

Every page of these cotes has been read in sweep 3. Part I takes up the open steps that the cote 63 and 64 readings
found.

Related prompts: RESEARCH_SA14_SA19 (Picard and Jacobians), RESEARCH_SA15 (crystals; good reduction and Néron models,
cote 100) and RESEARCH_SA06 (motifs II). Their questions are not to be done here.

## What is attached

One file, `RESEARCH_SA16_SA18_background.zip` (1.4 MB; LaTeX and text only, no scans, no PDF). `MANIFEST.tsv` at its
root lists every file with its origin and SHA256.
- `sweep3_SA18/` and `sweep3_SA16/`: the sweep-3 study of each topic.
  - `STUDY.md`;
  - `HUNCHES.md`: the Leads, with their grounds;
  - `RESEARCH_PACKAGES.md`: the questions as the reader framed them, with the strongest reduction known and the
    material;
  - `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`;
  - `readings/c45_c56.md`, `readings/c62_c64.md` (cote 62 scans 2-50, and cote 64) and `readings/c62b_c63.md`
    (cote 62 scans 51-97, and cote 63): the item-by-item readings, with their TSVs.
- `sweep2_SA16_WHAT_IS_WHERE.md`, `sweep2_SA18_WHAT_IS_WHERE.md`: the item maps (SA16-n, SA18-n). The readings use
  these item ids.
- `sweep2_reports/hands_formulaire_and_tate.md`, `sweep2_reports/cote47_scan009_chi_factor.md`: readings decided on the
  scan images.
- `broad_layer/SA15_readings_c9_c100.md`: the sweep-3 reading of cotes 9 and 100 (good reduction of abelian schemes,
  Néron models, p-divisible groups).
- `transcriptions/pro/<package>/`: the transcriptions by GPT-6 Astra (ChatGPT Pro mode), one `.tex` per scan, with the
  package's notes. Packages:
  - MPL_62_002-050 and MPL_64_002-039, 040-077, 078-115, 116-157;
  - MPL_45_033-080 and MPL_46_002-048;
  - the cote-47 and cote-54 pages of MPL_16+47+54+44;
  - the cote-56 pages of MPL_11_043-058+56.
- `transcriptions/codex/<folder>/`: the transcriptions by Codex web / ChatGPT Work (GPT-6.2 Astra at Max), with notes and
  math notes:
  - cote 62: K62-01 to K62-03;
  - cote 63: H63-01 to H63-09, K63-01, K63-02;
  - cotes 45 and 46: K45-01, K45-02, C45-01, C46-01, K46-01 to K46-03;
  - cotes 47 to 52: K47-01, H48-01, K49-01, K50-01, K51-01, K51-02, K52-01;
  - cote 53: J53-01 to J53-05;
  - cotes 54 to 56: K54-01, K55-01, K56-01 to K56-03.

His pages are diplomatic transcriptions: `\unsure{a|b}` marks a reading in doubt (the first is what the ink shows),
`\illegible` marks unreadable ink, and `\deleted{...}` and `\inserted{...}` keep his corrections. Quote his statements
from the transcription with the page as `cote:scan`.

## Where this comes from

The pages are Alexandre Grothendieck's manuscripts in the Fonds Grothendieck at the Université de Montpellier:
- cotes 45-56, "Variétés abéliennes":
  - Galois cohomology of algebraic groups, Borel subgroups, Brauer-Severi varieties (45, 46);
  - the Fourier transform of abelian schemes (47);
  - a plan of EGA "VII" (48);
  - Picard of abelian schemes (49);
  - notes on Lang's book (50);
  - good reduction after Shimura and Koizumi (51);
  - Torelli for families (52);
  - a course on group schemes, 1973 (53);
  - duality in the cohomology of abelian varieties (54);
  - compact Stein spaces (55).
- cotes 62-64, "Courbes elliptiques":
  - his manuscript "Modules des courbes elliptiques" (62);
  - the Tate-Deligne Formulaire and kept typescripts (63);
  - levels, pinnings, cusps and connections on the moduli (64).

The transcriptions are AI-produced: by GPT-6 Astra (ChatGPT Pro mode), and by Codex web / ChatGPT Work (GPT-6.2 Astra at
Max). The sweeps are by Claude Opus 5.5 at effort max. No research run has yet worked on these cotes.

## Results this prompt builds on (status on 19 Nov 2026)

Each result was obtained or checked once, by a sweep-3 reader (Claude Opus 5.5 at effort max) or in sweep 2 on the scan
image. The proof is in the reading named, and the check events are in `CHECK_EVENTS.tsv`. None has been checked
independently. Check each one where you use it.

- **R1 (45:8-9; c45_c56).** The step N_G(𝔥)·K = G of his Lemma 4 is false: SL_2 with its Frobenius kernel is a
  counterexample. His surjectivity theorem for H^1 and his theorem on nonabelian H^2 over fields of dimension ≤ 1 are
  therefore unproved for non-solvable infinitesimal kernels. The rest of his theorems on 45:2-17 stands. By his Lemmas 3
  and 5 and the commutator dévissage, the question reduces to K of height one with perfect restricted Lie algebra.
- **R2 (47:3-11; c45_c56).** The Fourier box of 47:11 drops the convolution. The corrected identity
  ψ_D(ab) = (−1)^g ψ_D(a) * ψ_D(b) in CH(Â)_Q, over a base, is reduced to Todd(H^1_dR(A/S)) = 1 in CH_Q(S). Over a field
  of characteristic 0 this follows from Esnault-Viehweg (2002, cited from memory). Sweep 2 decided 47:9 on the scan
  (`cote47_scan009_chi_factor.md`): his slip χ^(k−1) for χ^k, and his weaker divisibility claim is true.
- **R3 (45:59).** His claim "vrai pour les formes intérieures" fails for inner forms: SL_1(D) is a counterexample.
- **R4 (55:17).** His "non-algebraic torus" is a product of elliptic curves.
- **R5 (45:37-42).** dim H^1(pgl_2, pgl_2) = 3 in characteristic 2, so his construction of the Chevalley groups over Z as
  Aut^0 of the Chevalley Lie algebra fails at p = 2 for PGL_2. On the page, the vanishing of H^0, H^1 and H^2 of
  (𝔤, 𝔤) implies that Aut^0 is smooth and equal to G.
- **R6 (51:17-23).**
  - In residue characteristic 0 he proves the existence of an abelian subscheme A ⊂ Pic_{X/S} with
    |A| = ∪_s |Pic^0(X_s)|.
  - Otherwise ("Sinon, il faut regarder de plus près") the question reduces to the triviality of a finite p-group kernel
    of A → P over a DVR.
  - His point c): H^1(S, G) ⊂ H^1(K, G) for regular S.
- **R7 (62:42-50; c62_c64 §1.5).** His invariant of a pointed genus-zero curve with a trisection is described thus:
  - The triples with invariant 1 are classified by H^1(S, μ_3), not "H^1(S, Z/3)" as written on 62:48.
  - His criteria of 62:19 answer his question "quels i conviennent ??" (62:46) over a DVR with 6 invertible, and over a
    regular S by purity of the branch locus.
  - [U/S_3] is the moduli of elliptic curves over Z[1/6] rigidified by −1.
- **R8 (63:32 and the Formulaire hands; sweep 2).** The margin "faux si S pas connexe" is right, and his own 63:96
  confirms it (c62b_c63 §2.3). The margins are probably in his hand: 6:39 is in Tate's hand, while 6:38 and 6:40-46
  are his.
- **R9 (64:116-121; c62_c64 §2.4). The level-4 pinning fixes α.**
  - From the relative level-4 Jacobi pinning (x_i)_{i∈J}, with 2x_i = ε_i and Σ x_i = 0:
    ∏_i (p(x_i) − p(ε_i))^2 = ∏_i f'(ζ_i) = −Δ_0^2.
  - So ∏_i (p(x_i) − p(ε_i)) = ±√−1·Δ_0, where Δ_0 = ∏_cyclic (p(ε_i) − p(ε_j)) depends only on the cyclic order of J.
  - The pinning therefore determines α (ω_J = μ_4^*), the first datum of the Legendre pinning. κ up to sign is what
    remains.
  - On 64:118 his formula for z_i^2 is to be read as −(a_1 ζ_i + 2a_2 − 3ζ_λ ζ_μ) and
    z_i^2 = 2ζ_i z_i − (a_2 − 2ζ_λ ζ_μ). Its simplest form is (z_i − ζ_i)^2 = (ζ_i − ζ_λ)(ζ_i − ζ_μ), which is valid
    also for ζ_i = 0.
- **R10 (64:103-108; c62_c64 §2.4). The derivation on the pole filtration.**
  - Θ_δ induces multiplication by −nδ on F_n/F_(n−1) (his own Prop. 3 on 62:7-8), not by δ as on 64:103.
  - Hence Ker Θ_δ = k·1_E holds only in characteristic 0; in characteristic p ≥ 3 every p-th power is killed.
  - With p' = Θ_δ p: ε_3(p') = −2δ^3, p'^2 = 4(p^3 + a_1 p^2 + a_2 p + a_3) and Θ P' = 2(3P^2 + 2a_1 P + a_2). This
    replaces his boxed p'^2 = p^3 + .... Equivalently, keep his (28) and (32)-(33) and set p' = −(1/2) Θ_δ p.
- **R11 (64:44-65; c62_c64 §2.2). The octahedral configuration.**
  - The Theorem and Corollary 1 of 64:52-53 hold in residue characteristics ≠ 2, 5.
  - In characteristic 5, Δ = {0, ∞, ±1, ±i} is all of P^1(F_5) and Aut(X, Δ) = PGL_2(F_5) ≅ S_5. The stabilizer of
    two points of Δ is μ_4, and there are five regular octahedral structures.
  - a) ⇔ b) holds in characteristic ≠ 2, and c) ⇔ b) holds when the opposition is part of the data.
  - His margins on 64:50 saw the exception; his text does not carry it.
  - 64:25 was decided on the ink: "qui \deleted{ne} sont \deleted{pas} dans V". His text is right: the face diagonals
    have stabilizers in V.
  - On 64:64 his slip is to be read as t ± √(t(t − 1)). On 64:65, the ratio is 1 for 0 and ∞, and −1 for 1 and t.
- **R12 (62:59-97; c62b_c63 §1.3-1.4). The classical formulas of his "Théorie transcendante".** His slips are
  corrected in `CORRECTIONS.tsv`:
  - σ is odd;
  - σ(z + 2ω_i) = −e^{2η_i(z + ω_i)} σ(z);
  - ζ(u) = 1/u − (c_1/3) u^3 − ...;
  - e_3 = (1/3)(π/2ω_1)^2 [θ_1(0)^4 − θ_2(0)^4];
  - g_2 = 20c_1 (62:62), and 4(p − e_1)(p − e_2)(p − e_3) (62:80);
  - J(i) = 1 for g_3 = 0 (62:93);
  - dn = 1/ch for k = 1 (62:94).

  Use the corrected forms in Part I.3.

## Leads

The Leads are the hunches in `sweep3_SA18/HUNCHES.md` (H1-H14) and in `sweep3_SA16/HUNCHES.md` (H-62-1 to H-62-3,
H-63-1, H-63-2, H-64-1 to H-64-4). They are inferences by Claude, Anthropic, and every one is to be checked in full:
proved, or refuted with the corrected statement. Which Parts use which Leads:
- Parts A-G use H1, H2, H6, H8, H9, H11 and H12 of SA18;
- Part H uses H-62-1 to H-62-3;
- Part I uses H-64-1, H-64-3, H-63-1 and H-63-2.

Each of the others (H3-H5, H7, H10, H13 and H14 of SA18; H-64-2 and H-64-4 of SA16) is settled where it bears on a
part, in the report's table:
- H-64-2: f_2^t as the Lattès map of the doubling (64:63-65).
- H-64-4: the "invariant modulaire exceptionnel" of 64:156 is 1728 = 2^6 3^3.
- H7: Oda's theorem and 54:7.
- H10: the genus-3 case of 52:10.
- H13: the degree slips of 56:15.
- H14: the datings.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation with a
complete counterexample, with every hypothesis and the failure verified (the group, scheme, ring, curve or family given
completely, and checked by a program when finite or computable), and the strongest true statement proved in its place.
Nothing else finishes an item. Partly settled is not an outcome. The cases proved, the computations run, the
obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working
on: record them as you go, then attack the obstruction, starting from that instance. "Known" counts only with the
derivation of the statement used here from the cited theorem, after opening the source. An item that begins with
"Determine" is done when the object asked for is given explicitly, with a proof that it is the whole answer.

For Part A in particular:
- Every group named states its structure: smooth or not, connected or not, reductive, semisimple or unipotent, which
  Frobenius kernel, which twisted form.
- Every cohomology class names its topology (fppf or étale) and its coefficients.
- A refutation gives the field k, the group G, the kernel K and the class with no lift (or the non-neutral lien),
  with the computation that shows it.

Not acceptable:
- a survey, or "open, see [reference]";
- a plan, an outline or a sample;
- proving R1-R12 again in place of the items, except where a Part asks for it;
- a result of the readings used without the check above;
- a statement for every p, every g or every group proved for some, without saying so;
- a step that replaces a claim by a convenient special case without naming it;
- a reading of his pages changed to fit the mathematics without saying what the transcription reads and why you read it
  otherwise.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA16_SA18_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Infinitesimal kernels over fields of dimension ≤ 1 (45:2-17; SA18-2, SA18-6; R1; Lead H12). The main question.**
1. For k of characteristic p with Br(K') = 0 for every finite separable K'/k, prove or refute that
   H^1_fppf(k, G) → H^1_fppf(k, G/K) is onto for every affine algebraic group G and infinitesimal normal subgroup K.
2. Prove or refute that every nonabelian H^2 class of an algebraic lien over such a k is neutral.
3. Start from R1's reduction: K of height one with perfect restricted Lie algebra, such as the Frobenius kernels of
   semisimple groups and their twisted forms.
4. Determine the exact class of kernels K for which his Lemma 4, or a correct replacement, holds.

**B. The Fourier transform of abelian schemes over a base (47:3-11, 54; SA18-13, SA18-14; R2; Lead H6).** For an
abelian scheme A/S of relative dimension g over a smooth base S over a field, prove or refute
ψ_D(ab) = (−1)^g ψ_D(a) * ψ_D(b) in CH(Â)_Q with no Todd factor. Equivalently, prove or refute
Todd(H^1_dR(A/S)) = 1 in CH_Q(S). Do it in characteristic 0, then in characteristic p. Settle the duality statements
of cote 54 that rest on it.

**C. The abelian subscheme of Pic in every characteristic (49:3-10, 51:17-22; SA18-17; R6; Lead H8).** For f: X → S
smooth projective with geometrically connected fibres over a reduced locally noetherian S, prove or refute that there is
a unique abelian subscheme A ⊂ Pic_{X/S} with |A| = ∪_s |Pic^0(X_s)|. The case to decide is residue characteristic
p > 0, where the question is the finite p-group kernel of A → P over a DVR.

**D. Purity for good reduction (51:9-12, 51:23; SA18-17, SA15-19; R6; Lead H9).**
1. His question "Analogue th. de pureté pour la bonne réduction des schémas abéliens?": for torsors under abelian schemes
   over a regular S, prove or refute that the set of points where P_K has good reduction is the complement of a closed
   set of pure codimension one.
2. Settle the underlying purity statement for abelian schemes in each case: mixed characteristic with e ≤ p − 1,
   e > p − 1, and equal characteristic. Give the proof, or the counterexample, with its source.

**E. Chevalley groups over Z from their Lie algebras (45:18-42; SA18-1; R5; Lead H1).** For each simple root system Φ and
prime p, and for the adjoint and simply connected Chevalley Lie algebras 𝔤 over F_p:
1. Determine H^i(𝔤, 𝔤) for i = 0, 1, 2.
2. Prove or refute that Aut^0_{Z[1/N]}(𝔤_Z) is the adjoint Chevalley group scheme exactly over the primes where these
   vanish (his 45:38: "cela suffirait à construire les Tchevalley sur Z").

Compute rank ≤ 4 and p ≤ 7 by program, then prove the general statement.

**F. Maximal tori of quasi-split type outside Borel subgroups (45:45-57; SA18-2; Lead H2).** For G quasi-split over a
field k with quasi-split maximal torus T_1, prove or refute his Question 1 of 45:55 ("J'en doute"): must a maximal torus
T ≅ T_1 (as k-tori) lie in a Borel subgroup over k?
- Over finite fields this is a statement about twisted conjugacy classes in W(Φ) ⋊ ⟨τ⟩. Compute it for every type,
  starting with ^3D_4 and ^2E_6.
- Then settle it in general.

**G. Contractions of finitely generated ideals over coherent rings (55:2-12; SA18-18; Lead H11).** Prove or refute his
question of 55:8: if A is coherent and J ⊂ A[T] is finitely generated, is J ∩ A finitely generated? If false, give an
explicit counterexample (Soublin's ring ∏_n Q[[x, y]] is the first place to look). Then settle the coherence question
for compact Stein algebras of finite presentation, which the page reduces to it.

**H. The trisection invariant on the moduli of elliptic curves (62:19, 62:42-50; SA16-4, SA16-5; R7; Lead H-62-1).**
1. For S normal and not regular, determine which i ∈ Γ(S, O_S) "conviennent" (62:46): those for which the fibre over i is
   an S_3-torsor unramified over S, with t and t − 1 units. Purity of the branch locus can fail here.
2. Give the answer in terms of local conditions, prove it, and give a counterexample where the regular-case criterion
   fails.
3. Prove the description of [U/S_3] as the moduli of elliptic curves over Z[1/6] rigidified by −1, with his invariant i
   as j_G.

**I. His open steps on cotes 63 and 64 (SA16-3, SA16-9, SA16-10, SA16-12, SA16-14, SA16-19; the reader's packages R2, R3,
R5 and R6 of `sweep3_SA16/RESEARCH_PACKAGES.md`, in the reader's own numbering, distinct from the Results above; Leads H-64-1, H-64-3, H-63-1, H-63-2).** Four questions, each to be proved or
refuted:

1. **The level-4 Legendre pinning (64:93, 64:116-126; R9, R10).** His open step on 64:121 reads "et la condition c)
   s'écrit Dieu sait comment --- il faudra y revenir".
   - Let E/S have 2 invertible, with a relative level-4 Jacobi pinning (x_i)_{i∈J}, 2x_i = ε_i, Σ x_i = 0.
   - Construct a Legendre pinning (α, κ) that depends functorially on (E, (x_i)) and is compatible with base change,
     or prove that none exists.
   - Write his condition c) explicitly.
   - By R9 the pinning already fixes α (ω_J = μ_4^*). What remains is κ up to sign: a canonical square root of a
     degree-2 quantity in the z_i, z'_i. F_t is the explicit line of Σ_i (ζ_j − ζ_k) e_i.
   - Decide whether the Legendre-pinned moduli space U_{0,3} × μ_4^* of 64:86 receives the level-4 moduli space
     canonically.
2. **Octahedral structures in characteristic 5 (64:44-53; R11).**
   - Describe the scheme of regular octahedral structures on a divisor Δ of degree 6 in a P^1-bundle over Z[1/2].
   - Prove or refute that it is finite étale of degree 1 away from 5, and of degree 5 over the points of
     characteristic 5 where Δ = P^1(F_5).
   - State and prove the Theorem and Corollary 1 of 64:52-53 in their corrected form, uniformly over Z[1/2], with the
     characteristic-5 case made explicit.
   - The stabilizer computation of the reading (μ_4 at 5) and PGL_2(F_5) ≅ S_5 are the starting point.
3. **His questions on the two splittings of H^1 (63:66-77; R12; Lead H-63-1).**
   - (a) For which τ in the upper half-plane is α(τ) = 0, that is, the Hodge complement ω̄ proportional to η = xω?
     Prove that the zeros of α in a fundamental domain are exactly τ = i and τ = e^{2πi/3}, or refute it with another
     zero.
   - (b) For E over Q̄ with ω algebraic, prove that α is algebraic if and only if E has complex multiplication, or
     refute one direction.
   - Known so far:
     - α ω^2 is canonical;
     - α vanishes at i (η_2 = −i η_1 for the square lattice) and at e^{2πi/3}, by the same symmetry;
     - his series of 63:69-71 for η_1 and η_2 converge absolutely.
   - Place α ω^2 against the non-holomorphic form E_2^*, as Lead H-63-1 proposes, and use the literature on E_2^* at
     CM points with exact locators.
4. **The divisors of c_4 and c_6 at the two supersingular points (63:96-100; Lead H-63-2).**
   - Write c_4 and c_6 as elements of W(F̄_p)[[t]] up to units, with t = a_1 for p = 2 and t = b_2 for p = 3.
   - Decide which surjection SL_2(F_3) → F_4^* gives the action on the vertical tangent line at the point a of 63:100.
   - This completes his description of the divisors of c_4 and c_6 on the modular site (63:96), and of the four
     components of V(c_4) ∩ M_3 at 2, which have a common tangent.
   - The regularity results of `readings/c62b_c63.md` §2.3 and the Newton polygon of c_4 at 2 (one segment of
     slope −1) are the starting point.
   - Then settle Lead H-63-2: whether the level-3 picture at 2 and the characteristic-5 exception of Part I.2 are the
     same phenomenon.

For every page that a question of this Part uses, record every correction to the transcriptions, giving what the
transcription reads and the reading you propose.

**J. Statement of results.** Every result of Parts A-I and every settled Lead, numbered, with its status. For each
statement of his that you prove or refute, give his statement in French with the page, then the correct statement.

## Rules of proof (they bind every statement you deliver)

Known results (published papers, books, the standard literature) are cited with exact locators (paper, section, theorem number, page) and are not re-proved. The exception is a short proof of a form the source does not state. Every new result of yours is proved in full.

1. State the actual claim with all its data: the field (perfect or not, its characteristic, its cohomological dimension),
   the base (reduced, normal, regular, excellent, its residue characteristics), the topology (fppf, étale, Zariski), the
   group (smooth or not, connected or not, which form), the relative dimension g, and the ring of coefficients of Chow
   groups. Do not replace it by a convenient special case. If you prove a special case, name it as one and keep the
   general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property you use
   (a morphism of group schemes, of liens, of torsors, of abelian schemes; over which base). Compositions must
   type-check.
3. Every reduction ("we may assume", "after a finite separable extension", "pass to the strict henselization", "reduce
   to height one") comes with a proof that the property needed transfers in the direction needed.
4. Conventions are named and kept:
   - Cartier duality and the dual abelian scheme;
   - the sign of A ≅ Â^;
   - the normalization of the Fourier transform (Mukai or Beauville);
   - the Chevalley basis and its signs;
   - the λ-line normalization of j (classical j or 1 − j/1728);
   - geometric or arithmetic Frobenius.
5. Check the edge cases in scope: p = 2, 3 and 5; g = 1 and g ≥ 2; height one and higher heights; imperfect fields;
   inner and outer forms; non-regular normal bases.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you
   attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart.
7. No authority. The transcriptions, the Pro notes, the Codex web notes, the readings, R1-R12 and the Leads (inferences
   by Claude, Anthropic) are all to be checked where used; the Leads in full. If one is wrong, say so plainly and show
   where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and you
   go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened. The literature to search first:
   - Giraud, Cohomologie non abélienne;
   - Demazure-Gabriel;
   - Springer (1966) on nonabelian H^2;
   - Serre, Cohomologie galoisienne;
   - Mukai (1981), Beauville (1983), Deninger-Murre (1991), Esnault-Viehweg (2002), van der Geer (1999);
   - FGA VI, and Kleiman, "The Picard scheme";
   - Faltings-Chai V.6, Vasiu-Zink, de Jong-Oort;
   - Hogeweij, Hiss and Strade on Chevalley Lie algebras;
   - Carter, Finite Groups of Lie Type;
   - Glaz (LNM 1371) and Soublin (1970);
   - Deligne-Rapoport, Katz-Mazur.

   These locators are cited from memory and are unverified: open each before you rely on it.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to deliver

One ZIP containing:
- `RESEARCH_SA16_SA18_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement is
  used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), with complete proofs;
  English, first person plural; his statements quoted in French with the page.
- `RESEARCH_SA16_SA18_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `RESEARCH_SA16_SA18_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA16_SA18_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with
  the statement number); then what you read, what you computed (every computation with its scope, inputs, run time and
  output files), and every correction to R1-R12, to the Leads, to the readings and to the transcriptions, with the page.
- `CHECK_EVENTS.tsv` and `PROGRESS_LEDGER.md`.
- `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched. Remarks taken from
Michel Hua's project are credited to it.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.
**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `RESEARCH_SA16_SA18_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `RESEARCH_SA16_SA18_checkpoint_<NN>_part<k>.zip`, the file list in the first part.
