# Independent check of D3, "Weak fundamental localizers that are not fundamental localizers, and Corollaire 7.7.2 of Grothendieck's *Les Dérivateurs*"

Checker: afceadd46f7598ec4 (Claude Fable 5.2 at effort max), 25 Nov 2026, on the brief of the main session 329fb1e6
(Claude Opus 5.5 at effort max), `agent_notes/afceadd4_D3_CHECK_BRIEF_20261125.md`. The note was written by
a34c04448e8299803 (Claude Opus 5.5 at effort max) from four runs of GPT-6 Astra (ChatGPT Pro mode). I did not write any
part of it and did not edit it. I am a Claude model, as the writer is: this check is not a check by another model
family. Work file: `agent_notes/afceadd46f7598ec4_NOTES.md` (blocks "D3 check, log 1-3").

Checked text: `src/D3_paper.tex` as of 25 Nov 2026 (984 lines, 65,573 bytes); line numbers below refer to that file. I
read it whole. Numbering is that of the built paper: Theorems A, B and Corollary C (introduction); Lemmas 3.1-3.5;
Section 4.1-4.4 with Lemma 4.1; Lemma 5.1, Proposition 5.2; Sections 6 (the passage), 7 (open), 8 (method).

Check types in `CHECK_D3_INDEPENDENT_CHECK_EVENTS.tsv`: the seven types of the check rubric, in the wording that
`CHECK_EVENTS.tsv` of this paper already uses, so that the two files merge: "targeted proof check", "independent
re-proof", "computation or formal certificate", "used and rechecked in this run" (the rubric's "checked in use"),
"carried as background without fault found" ("survived exposure"), "discussed in an expert conference", "refuted, with
the refined statement's id".

**Result in one paragraph.** I found no mathematical error in any statement of the note. Theorems A and B and
Corollary C hold as stated. The five places that only the writer had read are correct line by line. Proposition 5.2
and the whole of Section 5 agree with Cisinski's text at every place cited, and with Rădulescu-Banu's. One
justification has a gap that is closed in two lines (Section 7, item 2: R1). One sentence of Section 6 credits
footnote 56 with something it does not say, and it is the sentence most likely to be read the wrong way (R2). The
rest are precisions of locators, credit and wording (R3-R15). On footnote 56 the writer's reading is the right one, and
three of our files have it backwards (Section 3.7 and Section 8). Beyond the brief, three questions that the note
leaves open are decided in Section 6 of this report, with proofs, one of them its first open problem, and a fourth is
sketched; those arguments are mine and nobody else has read them.

## 1. Verdicts

| Statement | Verdict |
|---|---|
| Lemma 3.1 [lem:absolute] | correct; Quillen's Theorem A and its dual form opened |
| Lemma 3.2 [lem:inverse-image] | correct |
| Lemma 3.3 [lem:grothendieck] and the two collages | correct (adjunction and the formula checked) |
| Lemma 3.4 [lem:mv] | correct |
| **Lemma 3.5** [lem:retracts] (Loc (8 bis) gives retract closure) | **correct**, every line; one optional precision (R12) |
| Theorem A, first sentences (Loc (1), (2), (3) for the four classes; aspherical = weakly contractible) | correct |
| Theorem A(a): W_π fails Loc (3 bis) over BC₂ | correct (re-derived) |
| Theorem A(a): W_π fails Loc (1 bis), Loc (8 bis) | correct |
| **Theorem A(a): W_π fails Loc (6′a)** | **correct**; the six-element ordered set also checked by program |
| Lemma 4.1 [lem:quotient] and the strong saturation of W_circ | correct (followed in full, the empty space included) |
| Theorem A(b): W_circ fails Loc (3 bis) for 10 → 6 over {o<+, o<−} | correct |
| **Theorem A(b): W_circ fails Loc (6′a)** | **correct** |
| Theorem A(c): W_tor strongly saturated; Loc (2), (3); the witness 77 → 53; Loc (6′a) fails | correct; sizes and degree recounted by program |
| Theorem A(c): Loc (8), Loc (9) for W_tor | no fault found; read, not re-derived in every detail (checked at the intakes) |
| **The sentence on the degrees of face-poset maps** (Section 4.3, used again in 4.4) | **correct**, for every simplicial map, also the non-injective one of 4.4; optional wording (R11) |
| Theorem A(d): Loc (1), (2), (3), Loc (6′a) for W_fin | correct |
| Theorem A(d): the category P (58 objects, 518 arrows), j: Q → P, the mapping torus | correct; numbers recounted by program; homology re-derived |
| Theorem A(d): Loc (3 bis) and Loc (8 bis) fail; Loc (9) | correct; Loc (9) read, not re-derived in every detail; its locator needs a precision (R3) |
| (F1), (F2), (F3) of Section 5 | correct; every cited place of Cisinski opened |
| **Lemma 5.1** [lem:pushout], the mapping-cylinder proof | **correct**, every line |
| Theorem B(i) | correct; Rădulescu-Banu Def. 1.1.1, Lemma 1.4.2, Def. 7.2.6, Th. 7.2.7 opened and their numbers confirmed |
| Theorem B(ii), sufficiency | correct; Cisinski Déf. 1.4.1, Rem. 1.1.3, Prop. 3.4.25, Déf. 4.2.11, Th. 4.2.15, Rem. 4.2.16 opened |
| **Proposition 5.2** (necessity) | **correct**; it is the argument of Cisinski's own proof of Cor. 4.2.22, applied to pushouts |
| Corollary C | correct |
| Section 6: what Grothendieck states, pages, lines, quotations | all exact; one sentence misattributes (R2); one precision (R9) |
| Section 7, item 2: "By Lemma 3.5 it satisfies Loc (1 bis)" | **true, but the justification has a gap**: Lemma 3.5 gives retracts, not Loc (1)(c). Closed in R1 |
| Section 7, items 1 and 3 (open questions) | item 1 can be answered (no), and two of the three entries of item 3 can be decided: Section 6 of this report |
| Abstract and introduction | no claim beyond what is proved, except "the smallest witness" (R6) and the credit line (R10) |

## 2. Who had checked what (step one)

From `results_register/who_checked.py`, 25 Nov 2026:

- BISITE A.32 (W_π): every step followed on 24 Nov by the cluster reader of the intake pile (Claude Opus 5.5 at effort
  high).
- RESIDUE B.2-B.4 (W_circ): targeted proof checks of 19 Nov; B.3 also re-derived there. The register leaves the
  checker of these rows unnamed ("?"); `PROVENANCE.md` names a8081d1b (Claude Opus 5.5 at effort max), also for the
  rows of DER_LOCALIZERS below.
- REVLOC F.1 (W_tor): targeted proof checks of 18 Nov (sweep 1, Claude Opus 5.5 at effort max) and of 24 Nov (Claude
  Opus 5.5 at effort high).
- DER_LOCALIZERS A5.1-A5.4: targeted proof checks of 19 Nov by a8081d1b; the homological step of A5.3 again on 24 Nov.
- **REVLOC F.1.1 = DER_FOLLOWUP G.9 (the sufficiency in Theorem B(ii)): no reader outside the runs had followed the
  proof with the cited theorems open.** The register has "statement compared" (sweep 1), "carried as background" and
  "audit read ... Cisinski 2006 and Rădulescu-Banu 2009 not opened" (a8081d1b). For that reason I checked the whole of
  Section 5 against the sources, not only Proposition 5.2.

I did not redo the runs' proofs. Where the table above says "correct" for a part that comes from a run, I followed it
as the note states it, which was needed to check the writer's additions built on it.

## 3. The seven items of the brief

### 3.1 The failures of Loc (6′a) for W_π and for W_circ (lines 531-536, 592-597)

**W_π.** X is the ordered set {0, 1, 2, 3, q, m} with 0<1, 0<3, 2<1, 2<3, 0<m, q<m. X₁ = {0,1,2,3,q} is a sieve
(nothing lies below 0, 2 or q; below 1 and 3 lie 0 and 2), and X₂ = {0,q,m} is a sieve (below m lie 0 and q). They
exhaust X, and X₀ = {0,q} is discrete with two points, since 0 and q are incomparable. X₁ is the square {0,1,2,3}, a
circle, together with the isolated point q; so X₀ → X₁ is bijective on components and its source is not connected:
it satisfies (π). X₂ has the greatest element m, so it is connected and contractible; the order complex of X is a
connected graph with six vertices and six edges, a circle. So X₂ → X is a map between connected categories that is
not a weak equivalence: it is not in W_π. The premise of Loc (6′a) holds and the conclusion fails. Correct. My program
confirms the sieves, the cover, the numbers of components (2, 2, 1, 1) and the Euler characteristic 0.

**W_circ.** X = M_v ∪ {t}, with t above every element of C₈ and unrelated to C₄; it is an ordered set (nothing of C₄
lies below an element of C₈). X₁ = M_v is a sieve because t is below nothing; X₂ = C₈ ∪ {t} is a sieve because C₈ is
a sieve of the collage; X₀ = C₈. The inclusion C₈ → M_v composed with the retraction M_v → C₄ (a left adjoint, in
W_∞) is v, of degree 2; both ends are circles, so the inclusion is in W_circ. By Lemma 3.4, BX is the homotopy pushout
of BM_v ← BC₈ → point, the cofibre of a map of degree 2 of the circle, the real projective plane. X₂ has the greatest
element t. So X₂ → X is a map from a contractible space to RP²: not a weak equivalence, and RP² is not a circle. Not
in W_circ. Correct.

Both use Loc (6′a) exactly as Grothendieck states it (XVI, printed p. 13, part a): if i₁: X₀ → X₁ is in W, then
j₁: X₂ → X₃ is in W), which is the form of the note.

### 3.2 Lemma 3.5 (lines 475-488)

With e = sr one has ee = srsr = sr = e and re = rsr = r, so the maps r form a cone on g → g → g → ⋯ (all transition
maps e). If c_{n+1}e = c_n for all n, then c_n e = c_{n+1}ee = c_{n+1}e = c_n, hence c_n = c_{n+1}e = c_{n+1}: all c_n
are equal to c₀, and c₀e = c₀. Then φ = c₀s satisfies φr = c₀sr = c₀e = c₀, and any φ with φr = c₀ is φrs = c₀s. So f,
with the cone r, is a colimit of the sequence in the category of arrows, where colimits are formed on sources and
targets separately; Loc (8 bis) gives f ∈ W. Correct. The lemma needs no saturation axiom, as stated, if "the functor
colim A_i → colim B_i" in Loc (8) is read for any colimit, which is how Grothendieck writes it (f is the colimit of
the f_i); see R12.

### 3.3 Lemma 5.1, the mapping-cylinder proof (lines 786-814)

- M = (X × Δ¹) ⊔_{X×{1}} Z, with ι₀ (a monomorphism, since X × {0} and X × {1} are disjoint), ι_Z and ρ; ρι₀ = g,
  ρι_Z = id; ρ and ι_Z are weak homotopy equivalences. Correct.
- T′ = Y ⊔_X M along the monomorphisms k and ι₀: in a category of presheaves the two legs of such a pushout are
  monomorphisms, their union is T′ and their intersection is X. Correct.
- For a simplicial subset U of T′, Δ/U is a full subcategory of Δ/T′ and a sieve: an arrow ([m], y) → ([n], x) is a
  map θ with θ*x = y, and x ∈ U gives y ∈ U. So Δ/Y and Δ/M form an MV square with intersection Δ/X, and the
  inclusion Δ/X → Δ/Y is Δ/k ∈ W. Loc (6′a) gives Δ/M → Δ/T′ ∈ W. Correct, with the roles X₁ = Δ/Y, X₂ = Δ/M.
- T′ ⊔_M Z = (Y ⊔_X M) ⊔_M Z = Y ⊔_X Z, where X → Z is ρι₀ = g; so T′ → T is the pushout of ρ along M → T′, a weak
  homotopy equivalence because simplicial sets are left proper (Rădulescu-Banu, Lemma 1.4.2, "Excision", opened: in a
  precofibration category the pushout of a weak equivalence between cofibrant objects along a cofibration is a weak
  equivalence).
- Z → T is Z → M → T′ → T, and Δ/− sends the three maps to W_∞, W and W_∞ (by (F1)). So Z → T ∈ V. Correct.

No step uses Loc (3 bis), Loc (8) or Loc (9).

### 3.4 Proposition 5.2 and Section 5, against Cisinski 2006

Source: the local copy named in `PROVENANCE.md`
(`derivateurs_companion_20261109/pro_prompts_20261110_work/_downloads/Cisinski_Ast308/smf_ast_308.pdf`), read in the
text extraction `work/ast308.txt`. What the cited places say, and whether the note uses them rightly:

| Place | What it says | Use in the note |
|---|---|---|
| Déf. 1.1.2, Rem. 1.1.3 | stability under pushouts ("images directes") and transfinite compositions; Rem. 1.1.3: equivalent form with X(i) → X(i+1) in the class and continuity at limit points | the "continuous" sequences of the proof of Theorem B(ii) are the form of Rem. 1.1.3: right. The note does not cite the remark (R13, optional) |
| Déf. 1.4.1 | A-localizer: L1 two out of three; L2 trivial fibrations; L3 the monomorphisms in W stable under pushouts and transfinite compositions | as cited |
| 1.4.12 | weakly saturated: FS1 identities, FS2 two out of three, FS3 (ri = 1, ir ∈ W ⇒ i ∈ W) | as cited |
| Cor. 2.1.21 | the Δ-localizer W_∞ is generated by the maps Δ_m → Δ_0 | as cited, for (F1) |
| Déf. 3.3.2 (headed "Grothendieck") | fundamental localizer: LA weakly saturated, LB, LC (the relative form) | as cited |
| Prop. 3.4.25 | every Δ-localizer is regular | as cited |
| §4.1, first line | the section fixes an arbitrary fundamental localizer W: so 4.1.21-4.1.29 hold for every fundamental localizer | needed, and true |
| Ex. 4.1.21 | Δ is a test category | as cited |
| Th. 4.1.26, last assertions | for a test functor i with final objects, ε_C: A/i*C → C is aspherical, and (i*)⁻¹(W_Â) = W | this is (F2) and (F3) for fundamental localizers: right |
| Ex. 4.1.29 | the inclusion Δ → Cat is a test functor, and i* is the nerve | as cited |
| Prop. 4.2.9 | for a fundamental localizer W and a W-local test category A, W_Â = i_A⁻¹W is a regular A-localizer | as cited in Proposition 5.2 |
| Déf. 4.2.11 | test A-localizer: regular, and a → final object in W for representable a | as cited |
| Th. 4.2.15 | W ↦ W_Cat is an increasing bijection from test A-localizers to fundamental localizers modelable by A, with inverse W ↦ i_A⁻¹W | as cited; it is stated for all test localizers, accessible or not, which is needed since V need not be accessible |
| Rem. 4.2.16 | W_Cat = (i_A*)⁻¹W, and W_Cat = (i*)⁻¹W for every W_Cat-test functor i with final objects | gives N⁻¹V = V_Cat: right |
| Cor. 4.2.19 and its proof | the minimal fundamental localizer is formed of the functors whose nerve is an ∞-equivalence; the proof says that it corresponds to the minimal test Δ-localizer | as cited, for (F1) |
| **Cor. 4.2.22** | every fundamental localizer is stable under filtered colimits; proof: W = N⁻¹i_Δ⁻¹W (4.1.26, 4.1.29), i_Δ⁻¹W is a regular Δ-localizer (4.2.9), regular localizers are stable under filtered colimits (3.4.41), the nerve commutes with them | as cited: this is Loc (8) |
| 6.1.12 | weak fundamental localizer: La, Lb, Lc; every fundamental localizer is a weak one; the remark on test categories | as cited |
| Prop. 6.1.16, Cor. 6.1.17, Th. 6.1.18 | as the note describes them in Sections 1.4 and 1.6 | as cited |

**Proposition 5.2.** For a fundamental localizer W: Loc (8) is Cor. 4.2.22. V = i_Δ⁻¹W is a regular Δ-localizer (Prop.
4.2.9; Δ is a W-test category by Ex. 4.1.21), and W = N⁻¹V (the equality that Cisinski writes in the proof of Cor.
4.2.22, from 4.1.26 and 4.1.29). For an MV square, NX is the union of NX₁ and NX₂ with intersection NX₀ (Lemma 3.4),
hence the pushout NX₁ ⊔_{NX₀} NX₂. If X₀ → X₁ is in W, then NX₀ → NX₁ is a monomorphism in V, its pushout NX₂ → NX is
in V by L3, and X₂ → X is in W. Correct. It is Cisinski's proof of Cor. 4.2.22 with "pushout" in place of "filtered
colimit", as the note says in Section 1.6.

**Theorem B(ii), sufficiency.** (L1) and (L2) hold because V satisfies two out of three and contains the weak
homotopy equivalences (trivial fibrations are such). (L3): pushouts by Lemma 5.1; transfinite compositions by
induction, with Loc (8) at limit ordinals, where Δ/X_β is the filtered colimit of the Δ/X_β′ (objects and arrows of
Δ/X are sums of sets X_n, and filtered colimits in Cat are formed on objects and arrows). So V is a Δ-localizer,
regular by Prop. 3.4.25, a test localizer by Déf. 4.2.11. By Th. 4.2.15 V_Cat is a fundamental localizer, and by Rem.
4.2.16 with Ex. 4.1.29 V_Cat = N⁻¹V; by (F3) N⁻¹V = W. Correct. There is no circle: Ex. 4.1.29 is applied to the
fundamental localizer V_Cat, and Th. 4.2.15 does not presuppose that W is fundamental.

**Theorem B(i).** Rădulescu-Banu, arXiv:math/0610009v4 (source in `work/rb/x/`): Def. 1.1.1 lists CF1-CF6 and calls
"precofibration category" the axioms CF1-CF4; Def. 7.2.6 is weak saturation (WS1-WS3; WS3 is typed "ri = 1_B", a slip
for 1_A, as `PROVENANCE.md` notes); Th. 7.2.7 says that for a category with weak equivalences admitting a
precofibration structure, weakly saturated, two out of six, closed under retracts and saturated are equivalent. I
confirmed the four numbers by counting the numbered environments of the source (the theorem counter runs within
sections: chapter 7 is `chap-applications.tex`, Section 7.2 "Saturation" has two lemmas, two theorems and two
definitions before the theorem). The verification of CF1-CF4 for (sSet, V, monomorphisms) in the note is right, and the
passage from V saturated to W strongly saturated through the nerve is right.

### 3.5 The sentence on the degrees of the face-poset maps (lines 618-621)

For a simplicial map g: K → L the induced map of face posets σ ↦ g(σ) has as nerve the simplicial map sd K → sd L
sending the barycentre of σ to the barycentre of g(σ). Let x be a point of |K| and σ the smallest simplex containing
it; x lies in a simplex of sd K whose vertices are barycentres of faces σ₀ ⊂ ⋯ ⊂ σ_k = σ, so its image under the
realization of the nerve lies in the convex hull of the barycentres of the g(σ_i), inside the closed simplex g(σ);
and |g|(x) lies in g(σ) too. The straight-line homotopy inside g(σ) is therefore defined and continuous, and the two
maps |K| → |L| are homotopic. So Bf has the degree of |h|, which is 2. Correct. The argument does not need g to be
injective on simplices, which matters because it is used again in Section 4.4 for the map u that collapses three
edges of the hexagon. Quillen states the same fact as an Example right after Theorem A (the map of ordered sets of
simplices induced by a simplicial map of simplicial complexes realizes that map); it could be cited there (R11).

### 3.6 The citations made from memory

| Citation | Opened | Result |
|---|---|---|
| Hatcher, Th. 4.5 | yes (my text copy of the book from the author's page, `derivateurs_companion_20261109/pro_reviews_max_20261112/1_CATHOT/work/lit/txt/hatcher_AT.txt`) | Whitehead's theorem for maps between connected CW complexes inducing isomorphisms on all π_n: as cited in Lemma 4.1 |
| Hatcher, Th. 4.32 | yes (same copy) | the Hurewicz theorem for (n−1)-connected spaces, n ≥ 2: as cited; "simply connected and acyclic implies weakly contractible" follows by induction on n |
| Quillen 1973, §1, "Cor. 1", "Cor. 2" | yes (`.../txt/quillen.txt`) | right statements: after Proposition 2 come Corollary 1 (a functor with a left or a right adjoint is a homotopy equivalence) and Corollary 2 (a category with an initial or a final object is contractible). But §1 has a second pair, Corollaries 1 and 2 of Proposition 3 (filtering categories): the locator is ambiguous (R5) |
| Quillen 1973, §1, Theorem A | yes | stated for the categories Y\f; the next sentence gives the dual form for f/Y, which is the form the note needs. The note re-derives the dual form by opposite categories; it can cite Quillen's sentence (R5) |
| Maltsiniotis, Astérisque 301, 1.1.2 | yes (local copy of the author's version of 2020, `.../_downloads/Maltsiniotis_Ast301/prstnewprov2020.pdf`) | 1.1.2 defines "localisateur fondamental faible" by La (weakly saturated), Lb, Lc: as cited. Also relevant there: Prop. 1.1.21 (R4) and the Introduction (R13) |
| Brown, *Topology and Groupoids*, §6.7 | yes (the author's free electronic version, `https://groupoids.org.uk/pdffiles/topgrpds-e.pdf`, fetched 25 Nov 2026) | Section 6.7 is "The fundamental groupoid of a union of spaces" (p. 240); its main result 6.7.2 says that for subspaces X₁, X₂ whose interiors cover X, with X₀ their intersection, and a set A of base points meeting every path component of X₀, X₁ and X₂, the square of fundamental groupoids on A is a pushout: as cited. Two standard steps are left to the reader of the note: subcomplexes are replaced by open neighbourhoods of which they are deformation retracts, and the pushout of an equivalence of groupoids that is injective on objects is an equivalence |
| Thomason 1979 | not opened | cited only in the overview; Lemma 3.4 proves the two cases that the proofs use. Standard |

### 3.7 Footnote 56 and Corollaire 7.7.2: what is stated, what is doubted, which reading is right

The edition the note uses: Chapitre XVI, *Les localiseurs fondamentaux*, deciphered and transcribed by M. Künzer,
edited by M. Künzer, J. Malgoire and G. Maltsiniotis, version of 18 March 2019. I read it in our transcription
`derivateurs_companion_20261109/corrected_french_20261111/DER_XVI.tex` and looked at the page itself as an image
(`packages/DER_XVI/DER_XVI_pages.pdf`, page 57 of the file, printed page 55).

**Printed page 55**, counting every line below the running head, the bracketed manuscript-page markers included:

- lines 3-9: Proposition 7.7.1;
- lines 10-15: the N.B.: if a localiseur fondamental W in Cat satisfies Loc (6′ a, 8, 9), then HOT_W is a true
  derivator; it was seen in 7.6 (ms. page 111) that then W = W_{HOT_W}, a sentence that carries the footnote mark 55,
  "hence":
- **lines 16-17: Corollaire 7.7.2, the implication Loc (6′ a, 8, 9) ⟹ Loc (1 ter, 3 bis), with the footnote mark 56
  on its right-hand side** (manuscript page 118);
- foot of the page, first footnote line, footnote 55: that this was under the hypothesis Loc (3 bis), with a warning
  against a vicious circle;
- foot of the page, second footnote line, footnote 56: "Loc (3 bis) pas prouvé, probablement faux."

The editors' statement at the head of the chapter says that their own additions are in typewriter type between
brackets; footnotes 55 and 56 are in roman, so they are Grothendieck's own annotations.

**What Grothendieck states.** For a localiseur fondamental (Loc (1), (2), (3)), the three axioms Loc (6′a), Loc (8),
Loc (9) imply Loc (1 ter) and Loc (3 bis).

**What the footnote doubts.** The mark 56 stands on the conclusion of that implication. The footnote says of its
Loc (3 bis) half two things: that it has not been proved (the argument used W = W_{HOT_W}, which footnote 55 has just
said was proved under Loc (3 bis)), and that it is probably false, that is, that Loc (6′a), (8), (9) probably do not
imply Loc (3 bis).

**Which reading is right.** By Theorem B(ii), which I checked against its sources, Loc (6′a) and Loc (8) do imply
Loc (3 bis) for a localiseur fondamental. So the corollary is true as printed, even without Loc (9). The first half of
the footnote ("pas prouvé") was right; **the second half ("probablement faux") is not borne out for the corollary as
printed.** The doubt becomes true only for weaker hypotheses: without Loc (6′a) (W_tor) or without Loc (8) (W_fin).
This is the reading of DER_LOCALIZERS A5.4 and of REVLOC F.1.1, and the reading of the note (abstract; Sections 1.3,
6; Corollary C). The same reading was already written down on 17 Nov 2026 by afbbdefd (Claude Fable 5.2 at effort
max) in `derivateurs_companion_20261109/pro_prompts_max_20261112_work/INTAKE_DER_FOLLOWUP_FINMON_20261117.md`, lines
279 and 509-511 ("Corollaire 7.7.2 is true as he states it; the footnote's 'probablement faux' is wrong; W̃ shows only
that Loc (6′ a) cannot be dropped").

**The files that have it backwards** (three, not two; exact replacements in Section 8 of this report):

1. `reports_20261124/INTAKE_PILE_20261124/DERIVATEURS.md`, item 4, lines 68-69: "Grothendieck's 'probablement faux' is
   right as printed". This contradicts the sentence before it in the same item ("Loc (6′ a) + Loc (8) suffice without
   Loc (9)").
2. `derivateurs_companion_20261109/pro_prompts_max_20261112_work/INTAKE_S2COUNT_REVLOC_20261117.md`, line 32 (a5ead5c6,
   Claude Fable 5.2 at effort high): F.1 "decides Grothendieck's doubt ... in his favour". The class of F.1 does not
   satisfy Loc (6′a), so it is no counterexample to the corollary, and F.1.1 in the same row proves the corollary.
3. `claude_math_notes/NOTES_20261117.md`, lines 66-68 (Claude Opus 5.5 at effort max, per the check register): the
   same sentence.

The note itself is right, but one of its sentences can still be read the wrong way: R2.

## 4. Other points checked

- **The axioms as Grothendieck prints them.** Loc (1) a, b, c; Loc (1 bis) = Loc (1) and "d) W stable par facteurs
  directs"; Loc (1 ter); Loc (2); Loc (3) with footnote 1 (printed p. 1, ms. pp. 1-2); Rappel 1 (pp. 1-2); Définition
  1.1 and Loc (3 bis) (p. 2, ms. pp. 2-3); the MV diagrams with "ouverts" (p. 12) and Loc 6′ (p. 13, ms. p. 17′);
  Loc (8), Loc (8 bis) (p. 40, where Loc (8 bis) is said to be the case I = N); Loc (9) (p. 41); footnote 53 (p. 53,
  announcing that Loc (6 a, 8, 9) already implies Loc (3 bis)); §7.8 and footnotes 57, 58 (p. 56). The note states
  and quotes all of them exactly.
- **Loc (9).** XVI 5.3.1-5.3.2 are stated for classes that satisfy Loc (8): Grothendieck says before Proposition
  5.3.1 that he restricts to that case for simplicity. For W_tor the note's verification is Cor. 5.3.2 with π = ℵ₀. W_fin does not satisfy Loc (8),
  so for it the definition is the general one, to which XVI 5.2 refers: Chapitre XVIII (same edition, version of 17
  December 2025), Définition 4.13.1, printed pp. 104-105 (a part S of Ob M is accessible if it is strictly full, the
  full subcategory is accessible, and the inclusion is accessible), with Définition 4.8.7, p. 72 (M is
  π₀-accessible if it is equivalent to some Ind_{π₀}(C), C small). The two facts that the note proves for W_fin
  (closed under ℵ₁-filtered colimits in the category of arrows; every member an ℵ₁-directed union of countable
  members) give these three conditions. So the claim "W_fin satisfies Loc (9)" stands; the locator "(this is the form
  of Loc (9) in [XVI, 5.3.1-5.3.2])" does not cover it (R3). Of Chapter XVIII I read only those two definitions
  (`corrected_french_20261111/DER_XVIII-c.tex` line 1148, `DER_XVIII-b.tex` line 1334).
- **Sieves or cosieves.** The note says that Loc (6′a) means the same in both conventions because W = W° under Loc (1),
  (2), (3) (XVI, Rappel 1). Theorem B is about weak fundamental localizers, which are only weakly saturated; for them
  W = W° is Maltsiniotis, Prop. 1.1.21 (opened). R4.
- **Numbers.** My program `work/CHECK_D3_INDEPENDENT_counts.py` (standard library; output
  `work/CHECK_D3_INDEPENDENT_counts.out`) recounts 50 and 26 simplices, 77 and 53 elements, 10 and 6, 38 and 20, 58
  objects, 518 arrows (146 + 74 + 164 + 134), and the degrees 2 (h) and 1, 2 (u, v). All as in the note.
- **The PDF.** Build log: no overfull box, one underfull line (the bibliography entry of the edition), 17 pages. I
  looked at all 17 pages on contact sheets; nothing runs off the page. `D3_paper.pdf` and `src/D3_paper.pdf` are the
  same file.
- **MSC.** 55U35 (abstract and axiomatic homotopy theory in algebraic topology) and 18N40 (homotopical algebra,
  Quillen model categories, derivators) are the right codes. If a third is wanted: 18N50 (simplicial sets), since the
  positive theorem goes through localizers of simplicial sets.

## 5. Repairs, with exact wording

Each repair gives the text to find in `src/D3_paper.tex` and its replacement; a replacement may be re-wrapped.

**R1 (gap in a justification; Section 7, item 2, lines 921-924).** Lemma 3.5 gives closure under retracts. Loc (1 bis)
is Loc (1) together with retracts, and Loc (1)(c) is not part of weak saturation. The claim is true: replace

```tex
\item \emph{Strong saturation without gluing.} Does a weak fundamental localizer satisfying
Loc~(8) and Loc~(9) satisfy Loc~(1~ter)? By Lemma~\ref{lem:retracts} it satisfies
Loc~(1~bis), and $\Wtor$, which fails Loc~($6'$a), is strongly saturated; we have no example
either way.
```

by

```tex
\item \emph{Strong saturation without gluing.} Does a weak fundamental localizer satisfying
Loc~(8) and Loc~(9) satisfy Loc~(1~ter)? It satisfies Loc~(1~bis). It is closed under retracts
by Lemma~\ref{lem:retracts}. It satisfies Loc~(1)(c): if $f\colon X\to Y$ and $g\colon Y\to X$
have $gf$ and $fg$ in $W$, the canonical maps from $X$ and from $Y$ to the colimits $X_\infty$
of $X\xrightarrow{gf}X\xrightarrow{gf}\cdots$ and $Y_\infty$ of
$Y\xrightarrow{fg}Y\xrightarrow{fg}\cdots$ lie in $W$ by Loc~(8~bis), being the colimits of the
arrows $(gf)^n$ and $(fg)^n$; the map $X_\infty\to Y_\infty$ induced by $f$ is an isomorphism,
with inverse induced by $g$; so $f\in W$ by two out of three, and likewise $g$. The class
$\Wtor$, which fails Loc~($6'$a), is strongly saturated; we have no example either way.
```

(The maps (gf)ⁿ: X → X form a sequence of arrows with constant source and transition maps (id, gf); f commutes with
the transition maps because f(gf) = (fg)f, and g maps the n-th Y to the (n+1)-st X because (gf)g = g(fg); the two
composites of the induced maps are induced by the transition maps, hence identities.) Alternatively, strengthen Lemma
3.5 to: "A class W that contains the isomorphisms, satisfies two out of three and satisfies Loc (8 bis) satisfies
Loc (1 bis)."

**R2 (a sentence that credits the footnote with what it does not say; Section 6, lines 897-903).** Replace

```tex
with the localizer of a derivator before Loc~(3~bis) is established. Footnote~56 is right that
the argument of \S7.7 does not prove Loc~(3~bis), and right that Loc~(3~bis) can fail for a
localiseur fondamental satisfying almost all of these axioms: it fails as soon as Loc~($6'$a) is
dropped, even with Loc~(1~ter), (8) and (9) (the class $\Wtor$), and as soon as Loc~(8) is dropped,
even with Loc~(1~ter), ($6'$a) and (9) (the class $\Wfin$). Under the hypotheses of the
corollary, however, Loc~(3~bis) holds, and so does Loc~(1~ter) (Theorem~B(i)); Loc~(9) plays no
part.
```

by

```tex
with the localizer of a derivator before Loc~(3~bis) is established. So footnote~56 is right in
its first half and wrong in its second. The argument of \S7.7 does not prove Loc~(3~bis); but
under the hypotheses of the corollary Loc~(3~bis) is not false: it holds, and so does
Loc~(1~ter) (Theorem~B(i)), and Loc~(9) plays no part. The doubt is borne out only for weaker
hypotheses: Loc~(3~bis) fails as soon as Loc~($6'$a) is dropped, even with Loc~(1~ter), (8) and
(9) (the class $\Wtor$), and as soon as Loc~(8) is dropped, even with Loc~(1~ter), ($6'$a) and
(9) (the class $\Wfin$).
```

For the same reason, in the abstract (lines 70-72, and `ABSTRACT.md`) replace

```tex
So Corollaire~7.7.2 holds,
and holds without Loc~(9), while neither of its other two hypotheses can be omitted; the
footnote's doubt is borne out only when one of them is dropped.
```

by

```tex
So Corollaire~7.7.2 holds,
and holds without Loc~(9): the footnote's ``probablement faux'' is not borne out. Neither of
the other two hypotheses can be omitted, and the doubt becomes true as soon as one of them is
dropped.
```

**R3 (locator; Section 1.1, lines 158-159).** Replace

```tex
makes $W$ an $\aleph_1$-accessible full subcategory, closed under $\aleph_1$-filtered colimits
(this is the form of Loc~(9) in \cite[XVI, 5.3.1--5.3.2]{Der}).
```

by

```tex
makes $W$ an $\aleph_1$-accessible full subcategory, closed under $\aleph_1$-filtered colimits.
This is what Loc~(9) asks. By \cite[XVI, 5.2]{Der} a part of $\Fl(\Cat)$ is accessible in the
sense of Chapter~XVIII of the manuscript: it is closed under isomorphism, the full subcategory
it defines is accessible, that is, equivalent to a category of ind-objects of a small category,
and its inclusion is an accessible functor \cite[D\'ef.~4.13.1 and~4.8.7]{DerXVIII}. For a
class satisfying Loc~(8), the existence of the countable sub-functors is the criterion of
\cite[XVI, Cor.~5.3.2]{Der} for $\pi=\aleph_0$.
```

and add to the bibliography

```tex
\bibitem{DerXVIII} A.~Grothendieck, \emph{Les D\'erivateurs}, Chapitre~XVIII, \emph{Cat\'egories
 et ensembles accessibles}, same edition, version of 17~December 2025, pp.~72 and 104--105.
```

At the end of Section 4.4 (line 761) "this is the form of Loc (9) of Section 1.1" can stay.

**R4 (precision; Section 1.1, lines 149-153).** Replace

```tex
between opposite categories \cite[XVI, Rappel~1]{Der}; since passing to opposite categories
exchanges sieves and cosieves, Loc~($6'$a) has the same meaning in either convention for all
the classes considered here.
```

by

```tex
between opposite categories \cite[XVI, Rappel~1]{Der}, and the same holds for every weak
fundamental localizer \cite[Prop.~1.1.21]{Mal05}; since passing to opposite categories
exchanges sieves and cosieves, Loc~($6'$a) has the same meaning in either convention for every
weak fundamental localizer.
```

**R5 (locators; lines 399, 402-405, 440).** In line 399 replace `\cite[\S1, Cor.~2]{Qui73}` by
`\cite[\S1, Corollary~2 of Proposition~2]{Qui73}`; in line 440 replace `\cite[\S1, Cor.~1]{Qui73}` by
`\cite[\S1, Corollary~1 of Proposition~2]{Qui73}`. In lines 402-405 replace

```tex
\cite[\S1, Th.~A]{Qui73}, in the form for the comma categories $A/b$ (obtained from the stated
form by passing to opposite categories, which does not change classifying spaces), shows that
```

by

```tex
\cite[\S1, Th.~A]{Qui73}, in its dual formulation for the comma categories $A/b$, which Quillen
states right after the theorem, shows that
```

**R6 (wording; abstract, lines 65-66, and `ABSTRACT.md`).** No minimality is proved. Replace "The smallest witness
is a functor" by "The smallest of our witnesses is a functor".

**R7 (wording: two Theorems A).** The paper's Theorem A and Quillen's Theorem A meet in one sentence ("Theorem A
shows ... that the absolute form of Theorem A does not imply the relative form"). Replace:

- line 126: `\emph{(Absolute Theorem A.)}` by `\emph{(Quillen's Theorem~A, absolute form.)}`;
- line 128: `\emph{(Relative Theorem A.)}` by `\emph{(Quillen's Theorem~A, relative form.)}`;
- lines 264-265: "that the absolute form of Theorem~A does not imply the relative form." by "that the absolute form of
  Quillen's Theorem~A, Loc~(3), does not imply the relative form, Loc~(3~bis).";
- line 342: "The absolute form of Theorem~A constrains" by "The absolute form of Quillen's Theorem~A, Loc~(3),
  constrains";
- line 764, the title of Section 5: "Gluing and filtered colimits give relative Theorem A" by "Gluing and filtered
  colimits give Loc (3 bis)".

**R8 (wording; Section 1.4, lines 290-291).** Footnotes 57 and 58 ask for one condition, not two. Replace "notes that
recovering $W$ from $\mathrm{HOT}_W$ needs it; both conditions are met automatically." by "notes that recovering $W$
from $\mathrm{HOT}_W$ needs it; the axiom that both footnotes ask for holds automatically."

**R9 (records; Section 6, lines 884-885).** The count 16-17 leaves out the running head. Replace "(counting every line
of the page, including the editors' manuscript-page markers;" by "(counting every line of the page below the running
head, including the editors' manuscript-page markers;".

**R10 (credit; title footnote, lines 44-45, and abstract, lines 74-76).** The necessity half of Theorem B(ii)
(Proposition 5.2), Lemma 3.5, the failures of Loc (6′a) for W_π and W_circ and the proof of Lemma 5.1 are the
writer's, as Section 8 says; the two summary lines say that all results are the runs'. Replace in the title footnote
"The results are due to runs of GPT-6 Astra (OpenAI, ChatGPT Pro mode), and the text was written by Claude Opus~5.5
(Anthropic) at effort max;" by "The four classes and the sufficiency in Theorem~B are due to runs of GPT-6 Astra
(OpenAI, ChatGPT Pro mode); the necessity, some complements and the text are by Claude Opus~5.5 (Anthropic) at effort
max;". Replace in the abstract "The mathematics was found by GPT-6 Astra (OpenAI, ChatGPT Pro mode) and the text
written by Claude Opus~5.5 (Anthropic) at effort max;" by "The four classes and the sufficiency of the two axioms
were found by GPT-6 Astra (OpenAI, ChatGPT Pro mode); their necessity and the text are by Claude Opus~5.5 (Anthropic)
at effort max;".

**R11 (optional wording; Section 4.3, lines 618-621).** Replace

```tex
barycentre of each simplex to the barycentre of its image, and on realizations it is homotopic to
$|g|$ by the straight-line homotopy, which stays in the image of each simplex; so $Bf$ has
degree $2$.
```

by

```tex
barycentre of each simplex to the barycentre of its image. On realizations it is homotopic to
$|g|$: a point of a simplex $\sigma$ is sent by both maps into the simplex $g(\sigma)$, and the
straight-line homotopy inside $g(\sigma)$ joins them (compare the Example after Theorem~A in
\cite[\S1]{Qui73}); $g$ need not be injective on simplices. So $Bf$ has degree $2$.
```

**R12 (optional precision; Lemma 3.5 and Loc (8), lines 142-145).** After "the functor $\colim_i A_i\to\colim_i B_i$
lies in $W$" add "(for any choice of the colimits)". Lemma 3.5 uses the axiom for the colimit f that its proof
constructs.

**R13 (optional credit and context; Sections 1.5, 1.6 and the proof of Theorem B(ii)).**

- Section 1.5, after "are Cisinski's; the proof of Theorem~B rests on them." add: "Cisinski also proves that every
  fundamental localizer is strongly saturated \cite[Prop.~4.2.4]{Cis06}, which Grothendieck had conjectured;
  Theorem~B(i) extends this to the weak fundamental localizers that satisfy Loc~($6'$a)." (Opened: Prop. 4.2.4,
  which says that every fundamental localizer is strongly saturated and hence closed under retracts; the attribution
  of the conjecture to Grothendieck is in Maltsiniotis, in the footnote just before Proposition 3.1.10 of the 2020
  version.)
- Section 1.6, before "We know of no earlier example": "Maltsiniotis says in his introduction what the relative axiom
  is used for: the stability of trivial cofibrations of presheaves under pushout, and the stability of weak
  equivalences under filtered colimits and under retracts \cite[Introduction]{Mal05}. The class $\Wpi$ has none of
  the three corresponding properties (Loc~($6'$a), Loc~(8~bis), Loc~(1~bis)), so these uses are not avoidable."
  (Opened in the author's version of 2020, p. 12, where the Introduction lists these uses of the stronger axiom, among
  others. The page number of the printed volume is not known to me.)
- Proof of Theorem B(ii), line 838: after "continuous at limit ordinals" add "(the form of
  \cite[Rem.~1.1.3]{Cis06})".

**R14 (optional precision; Section 4.4, lines 681-682).** Replace "for every component $c$ of the source of $f$
outside the finitely many components bad for $gf$ or $fg$" by "for every component $c$ of the source of $f$ such that
$c$ is not bad for $gf$ and $f(c)$ is not bad for $fg$, that is, for all but finitely many $c$".

**R15 (records).**

- `PROVENANCE.md`, "Sources": "Prop. 5.3.1, Cor. 5.3.2 (p. 41)" should read "Prop. 5.3.1 (pp. 41-42), Cor. 5.3.2
  (p. 42)". Hatcher (Th. 4.5, 4.32), Quillen (§1, Proposition 2 with its Corollaries 1 and 2, Theorem A),
  Maltsiniotis (1.1.2, Prop. 1.1.21, Introduction) and Brown (6.7.2) are now opened, by this check; Thomason is
  not.
- Section 8, "Checks", lines 959-961: replace "the arguments that are the writer's own have been checked by nobody
  else." by "the arguments that are the writer's own were checked line by line on 25~November 2026 by Claude
  Fable~5.2 at effort max, which also checked Section~\ref{sec:positive} against the cited statements of
  \cite{Cis06} and \cite{RB09}, opened \cite{Bro06}, \cite{Hat02}, \cite{Qui73} and \cite{Mal05} at the places cited, and recounted
  the finite witnesses with a program of its own. That checker is a model of the same family as the writer." The
  sentence before it ("All these checks are by models of a family other than the one that found the results") stays
  true.
- Abstract, lines 76-77: "the proofs were checked by Claude Opus~5.5 at efforts max and high." becomes "the proofs
  were checked by Claude Opus~5.5 at efforts max and high and by Claude Fable~5.2 at effort max."
- The report of this check is `CHECK_D3_INDEPENDENT.md`; its rows are in `CHECK_D3_INDEPENDENT_CHECK_EVENTS.tsv`, to
  be merged into `CHECK_EVENTS.tsv`.

## 6. Findings beyond the brief

These four arguments are mine (Claude Fable 5.2 at effort max, 25 Nov 2026). Nobody else has read them. If any goes
into the note it needs its own check, and Section 8 of the note has to say whose it is.

### 6.1 Open problem 1 of the note is answered: Loc (8) cannot be replaced by Loc (8 bis)

Section 7, item 1 asks: "Does a weak fundamental localizer satisfying Loc (6′a) and Loc (8 bis) satisfy Loc (3 bis)?"
No. Let W_ctbl be the class of functors u such that Π₁(Bu) is an equivalence, H_*(Bu; Z) is an isomorphism, and Bu
restricts to a weak homotopy equivalence on all but **countably** many components. Call a component bad as in
Section 4.4.

1. Loc (1), (2), (3), strong saturation: word for word as for W_fin, with "countably many" for "finitely many" (a
   union of two countable sets is countable; an aspherical category is simply connected and acyclic). Strong
   saturation by Theorem B(i) and step 2.
2. Loc (6′a): the proof of Section 4.4, where S̄ is now the countable image of the bad components of i.
3. Loc (8 bis): let u = colim u_n over N with u_n: A_n → B_n in W_ctbl. The first two conditions pass to the colimit.
   Let c be a component of the target B such that no bad component of any u_n maps into c. The objects of B_n lying
   over c form a union B_n^c of components of B_n, the corresponding components of A_n form A_n^c, and u_n restricts
   to a weak equivalence A_n^c → B_n^c, a disjoint union of weak equivalences. The parts over c of A and B are the
   colimits of the A_n^c and B_n^c, and a sequential colimit of weak equivalences is a weak equivalence. So c is not
   bad. Hence every bad component of u receives a bad component of some u_n: the bad components of u are countably
   many.
4. Loc (3 bis) fails: over the discrete category on an uncountable set Λ, the coproduct of Λ copies of the functor
   j: Q → P of Section 4.4 has comparison j ∈ W_fin ⊆ W_ctbl over every point, and uncountably many bad components.

So W_ctbl is a strongly saturated localiseur fondamental with Loc (6′a) and Loc (8 bis) and without Loc (3 bis). It
fails Loc (8), as Theorem B(ii) requires (the coproduct over Λ is the filtered colimit of the coproducts over the
countable subsets). Corollary C(ii) can be sharpened accordingly: in Corollaire 7.7.2, Loc (8) cannot be weakened to
Loc (8 bis).

For the second question of item 1 (stability under arbitrary coproducts in place of Loc (8)) I have only a sketch,
which points to yes: with Loc (6′a) the triple (sSet, V, monomorphisms) is a precofibration category, so the gluing
lemma holds in it (Rădulescu-Banu, Lemma 1.4.1); the homotopy colimit of a chain is built from coproducts, pushouts
along monomorphisms and one countable sequence (simplicial replacement), and a countable sequence is itself a pushout
of coproducts (the telescope); comparing a continuous chain of monomorphisms in V with the constant chain on its first
term would give the transfinite compositions. I have not written this out, and I do not claim it.

### 6.2 Table 1, the entry "Loc (8)" for W_circ: it fails, already Loc (8 bis)

Let Z be the group of integers regarded as a category with one object, d: Z → Z the functor n ↦ 2n, and D the diagram
on the ordered set N with D(k) = Z and D(k ≤ l) = d^{l−k}. Let T be the Grothendieck construction of D and T_n its
full subcategory over {0, …, n}, which is the Grothendieck construction of the restriction of D. By Lemma 3.3 for the
greatest element n, the functor r_n: T_n → Z, which sends an arrow (k ≤ l, m) to 2^{n−l}m, has a right adjoint; so
BT_n is a circle. The inclusion u_n: T_0 → T_n satisfies r_n u_n = dⁿ, of degree 2ⁿ; so u_n ∈ W_circ. The arrows u_n,
with the maps (id, T_n ⊂ T_{n+1}), form a sequence in the category of arrows with colimit the inclusion u: T_0 → T.
Since r_{n+1} restricted to T_n is d r_n, the fundamental group of BT is the colimit of Z → Z → ⋯ with all maps
multiplication by 2, that is Z[1/2], and π₁(Bu) is the inclusion of Z. So u is not a weak equivalence, and BT is not
homotopy equivalent to a circle, Z[1/2] not being isomorphic to Z. Hence u ∉ W_circ: W_circ does not satisfy
Loc (8 bis).

If this is added: Theorem A(b) becomes "W_circ is strongly saturated and satisfies neither Loc (6′a) nor
Loc (8 bis)", the entry of Table 1 becomes "no", and Section 7, item 3 loses "Loc (8)".

### 6.3 Table 1, the entry "Loc (9)" for W_π: it fails

By XVIII, Déf. 4.13.1 and 4.8.7 (Section 4 above), an accessible part is in particular a full subcategory equivalent
to some Ind_{π₀}(C), which has all colimits over ordered sets in which every subset of cardinality at most π₀ is
bounded. I show that the full subcategory W_π of the category of arrows lacks such colimits for every π₀.

Let κ be a regular cardinal, Ω a set of cardinality at least κ, and I the set of subsets of Ω of cardinality less than
κ, ordered by inclusion; every subset of I of cardinality less than κ is bounded. Let G be the group of order two. For
i in I let A_i be the sum of BG and the discrete category on Ω ∖ i, let B_i be the discrete category on {*} ⊔ (Ω ∖ i),
and let u_i: A_i → B_i collapse BG to * and be the identity elsewhere. For i ⊂ j the transition maps send the points
of j ∖ i to the object of BG and to *. Each u_i is bijective on components and A_i is not connected, so u_i ∈ W_π. The
colimit in the category of arrows is BG → e, which is not in W_π.

Suppose the diagram had a colimit w: P → R in the full subcategory W_π. It would be a reflection of BG → e: a map
λ = (α: BG → P, β: e → R) through which every map from BG → e to a member of W_π factors uniquely. (i) P is connected.
If not, let P₀ be the component containing α(BG), P₁ the rest, and R₀, R₁ the corresponding parts of R. The class
contains w ⊔ id_e, and there are two maps from w to it that agree on λ: the inclusion, and the map that is the
identity on P₀, R₀ and sends P₁ and R₁ to the new point. (ii) So w is in W_∞. Map BG → e to
(BG ⊔ e → e ⊔ e) ∈ W_π by the inclusion of the first summands; the factorization gives a functor ν: P → BG ⊔ e with
να the inclusion of BG, and P being connected, ν is a retraction P → BG of α. But wα is constant and Bw is a homotopy
equivalence, so Bα is null-homotopic, and then so is the identity of the classifying space of BG, which is the
infinite real projective space. Contradiction.

So W_π is not an accessible part of the category of arrows: Loc (9) fails for W_π. This rests on my reading of two
definitions of Chapter XVIII, of which I read nothing else.

### 6.4 Table 1, the entry "Loc (9)" for W_circ: it holds (sketch)

W_circ is closed under ℵ₁-filtered colimits in the category of arrows. In an ℵ₁-directed index set, either the indices
with u_i ∈ W_∞ are cofinal, and then the colimit is in W_∞, or the indices where source and target are circles are
cofinal. In that case the fundamental group of the colimit of the sources is an ℵ₁-directed colimit of copies of Z
along multiplications by integers; such a group is torsion free and all its countable subgroups are cyclic, so it is 0
or Z, and the higher homotopy groups vanish; the same for the targets; and H₁(−; Q) of the colimit map is a colimit of
isomorphisms. So the colimit is a map of circles inducing an isomorphism on H₁(−; Q), or a map between contractible
categories. And every member of W_circ is an ℵ₁-directed union of countable sub-functors in W_circ, by the
construction of Section 4.3 with the requests that make the inclusions of the countable subcategories weak
equivalences. With Section 6.2 this would make W_circ a class with Loc (1 ter), (9) and without Loc (6′a), (8). I have
not written the details.

## 7. Abstract, introduction, wording

- The abstract and the introduction claim nothing beyond what is proved, with two exceptions: "The smallest witness"
  (R6) and the credit lines (R10). After this check the sentence on who checked needs R15.
- The statements about Cisinski and Maltsiniotis in Sections 1, 1.4-1.6 agree with their texts (Section 3.4 above;
  Maltsiniotis 1.1.2 and Introduction opened).
- "We know of no earlier example ...; Maltsiniotis's and Cisinski's treatments give none": I searched the text of
  both books for a remark that the question is open or settled ("on ignore", "ne sait pas", "conjecture") and found
  none about weak against strong localizers. Maltsiniotis's Introduction says only that the stronger axiom is useful
  for certain finer results, which it lists.
- Notation is reused across Sections 4.2-4.4: C_m (an ordered set in 4.2, a polygon in 4.3, said so), P and Q
  (ordered sets in 4.3, categories in 4.4), u and v (the crown map v of 4.2, the two maps of 4.4, and generic
  functors), S (the base in Loc (3 bis) and in 4.2, a pole and the spheres S_n in 4.4). Nothing is wrong; renaming the
  poles or the spheres of 4.4 would spare the reader.
- Section 1.4: "by finite examples" is true of three of the four witnesses; the witness for W_fin is an infinite
  coproduct of one finite functor, as Theorem A(d) says.

## 8. Corrections for other files (I did not edit them)

1. `reports_20261124/INTAKE_PILE_20261124/DERIVATEURS.md`, item 4, lines 68-69. Replace "So Loc (6′ a) and Loc (8) are
   each necessary and Loc (9) is irrelevant; Grothendieck's "probablement faux" is right as printed." by "So Loc (6′ a)
   and Loc (8) are each necessary and Loc (9) is irrelevant. Corollaire 7.7.2 is true as printed; of footnote 56, 'pas
   prouvé' was right and 'probablement faux' is not borne out, except when Loc (6′ a) or Loc (8) is dropped."
2. `derivateurs_companion_20261109/pro_prompts_max_20261112_work/INTAKE_S2COUNT_REVLOC_20261117.md`, line 32. Replace
   "This decides Grothendieck's doubt at XVI ms. 118, footnote 56 ("Loc (3 bis) pas prouvé, probablement faux") in his
   favour, and closes POLES A.16" by "F.1 shows that Loc (6′ a) cannot be dropped from Corollaire 7.7.2 (XVI ms. 118),
   and F.1.1 proves the corollary as printed, so the 'probablement faux' of footnote 56 is not borne out; F.1 also
   answers POLES A.16, which BISITE A.32 had answered first".
3. `claude_math_notes/NOTES_20261117.md`, lines 66-68: the same replacement as in 2.
4. `papers/D3/PROVENANCE.md`: the section "Footnote 56: a reading to correct elsewhere" names two files; there are
   three, and the right reading was already recorded on 17 Nov in `INTAKE_DER_FOLLOWUP_FINMON_20261117.md`, lines 279
   and 509-511 (afbbdefd, Claude Fable 5.2 at effort max). Also R15.

## 9. Not covered

- The runs' own proofs and programs were not redone (the brief). Loc (8) and Loc (9) for W_tor and Loc (9) for W_fin
  were read with attention and not re-derived in every detail.
- Cisinski's and Rădulescu-Banu's proofs: I opened the statements cited and the proofs of Th. 4.2.15, Cor. 4.2.19 and
  Cor. 4.2.22; I did not check Cisinski's theory behind them. Rădulescu-Banu's text is an arXiv preprint.
- Thomason 1979 was not opened. Of Chapter XVIII only Définitions 4.8.7 and 4.13.1 were read.
- No literature search (not in the brief; the gate is in `PROVENANCE.md`).
- A check by a model of another family has not been made.
