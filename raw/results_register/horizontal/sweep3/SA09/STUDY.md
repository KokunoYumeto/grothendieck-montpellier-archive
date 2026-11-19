# SA09, the de Rham notes continued (cotes 137 and 138): sweep 3, the topic worked through

## Who did what

- Integrated on 19 Nov 2026 by Claude Opus 5.5 at effort max (agent a34c04448e8299803).
- The reading itself is that of the sweep-3 reader a188625c776c7aca7 (Claude Opus 5.5 at effort max), launched by the
  main session on 18 Nov at about 23:00 UTC with `../READER_BRIEF_a34c04448e8299803.md`.
- The full reading, with every check and every reading decided on the image, is `readings/SA09_137-138.md`.
- This file gives the topic in order, with the places, and what is proved, checked, wrong and open.
- The check events (52) and corrections (28) are in CHECK_EVENTS.tsv and CORRECTIONS.tsv. Item ids are those of
  `../../sweep2/SA09/WHAT_IS_WHERE.md`.

## What was read

- **Read in full:** the five Pro transcriptions (137 scans 2-86; 138 scans 1-133).
- **Read for the claims checked:** the Pro notes. Their findings are credited as "the Pro notes of <package>".
- **Not opened** (budget): the doubts files line by line, and the Codex-web returns K137-01 to K138-05.
- **Credited witness:** Michel Hua's project (137.modern.tex, 138.modern.tex). It is never the basis of a reading.
- **Cote 139 is not studied.** The sweep-2 map places there only the Prix Émile Picard medal (K139-01).

## Cote 137, scans 2-86: ∂-perfect complexes, the walking complex, multiplicative structures, polynomial categories

The cote is an integral framework for "cochains with divided powers". It has four parts:
- the classification of the simplicial objects built from Φ (functions on the vertices) and Ψ = Φ/kT (SA09-2);
- the universal additive categories they generate (SA09-3);
- the products (SA09-4);
- the polynomial structure meant to carry the Γ-operations (SA09-6).

The de Rham comparison of scan 73 ties it to the PD de Rham complex of cote 136.

### SA09-2 · ∂-perfect "½-simplicial" complexes (scans 2-20)

Checked:
- Lemma 1 and its NB (scan 2). They are the exact characterisation of projective objects.
- The Cor.: Γ^iΦ ⊗ Λ^jΨ and Λ^iΦ ⊗ Λ^jΨ are projective (i > 0).
- **The Théorème of scan 4.** The weight-n PD Koszul complex of Φ → Ψ maps to the ∧T complex Λ^{•+1}Φ, and all
  connecting maps are isomorphisms. So weight n of the PD de Rham complex is a truncated flasque resolution of k.
  Divided powers are essential: the Sym version is exact only after inverting factorials.
- The rank Lemma of scan 7. Its margin limit lacks a factor 1/N!.
- The splitting Prop. of scan 8 (not canonical).
- Prop. 2 of scan 10, stability under ⊗, with his margin "faux" against Λ^i, Γ^i rightly kept: Γ²(Λ¹Ψ) has
  π_1 = Z/2.
- Realizability: μ_0 = 0 ⇔ f(−1) = χ(ν).
- The classification over a principal ring (scans 16-19). Over Z, Φ(i,2) ≇ Φ(i,3) although their ranks agree.

Wrong, with corrections:
- **Lemma 2 (scan 4)** fails for q = q' under the revised hypothesis "(projectif)". On the image the proof line reads
  π_•(L_•) = 0, which is flasqueness. Restore "flasque", or π_0(L) = 0.
- **Scan 12.** The ink reads "(bien sûr, ils seront même str. spéciaux!)". This is false for the Ψ case over Z: Λ²(Λ²Ψ)
  has π_3 = Z/2.
- **Def. 1 / Prop. 1 e) (scans 14-15)** are false in both directions. The counterexamples are those of the Pro notes
  R023 and R024. The true form: over k regular noetherian with L_n of finite type, L^! is bounded ⇔ the fibre rank
  functions are polynomial of bounded degree.
- **Scan 17.** One of the two struck μ_i is his slip: rk L^!_i = μ_i + μ_{i+1} + β_i + β_{i+1} + ν_i.

### SA09-3 · the dévissage theorem and the walking complex (scans 20-64)

Checked:
- **The Hom tables (scans 21-27)**, against Dold-Puppe. The index slips on scans 22-25 are decided by the mathematics.
- **The walking complex (scans 40-47).** Additive functors out of the C^i are cochain complexes (Prop. 1).
- **Prop. 2 (scan 43).** Decided on the image at 600 dpi: the ink has the shifted pairing Hom(x, C^{n+1}), which is
  the mathematically right one.
- **Prop. 5.** C^* = DP(C^•) is the universal cosimplicial object of k-additive Karoubian categories.
- **The Σ-exact theorem (scans 49-56)** is the universal property of the Frobenius category of bounded complexes of
  free modules. Full faithfulness is proved on the pages.
- **The relative homological algebra (scans 58-64)**, including R^iF(Ψ^0) = H^i(F(C^•)) ("sauf erreur": rightly).

Wrong:
- **The density claim of scan 29** is false for Set-valued functors. The additive statement survives.
- **Over a principal ring that is not a field,** the essential image of the Σ-exact theorem needs more kernels than
  those of the d^i. The kernels of (x, y) ↦ (dx − ny, dy) for non-units n are also needed.

### SA09-4 · multiplicative structures (scans 65-72)

- The tensor product, the ideal K and the missing unit are checked.
- The existence of the multiplicative extension (scans 70-71) is now complete. The Σ-kernel presentation supplies the
  step that the Pro notes M08 left open.
- Tot(C^• * C^•) gives a graded-commutative cup product on H^*(C^•).

### SA09-5 · the de Rham comparison (scans 38-39, 73-74)

- **His programme (scans 38-39):** C^* with its extra structure is to be determined by the de Rham-Sullivan complex in
  characteristic 0, or by the PD de Rham complex for any k. Whether it recovers the homotopy type is his question.
- **Scan 73, re-derived from the scan-4 theorem:** the weight-n PD de Rham complex, transported, is homotopic to the
  good truncation τ_{≤n}C^• by a unique homotopy class.
- This is the same weightwise comparison that the SA08 readers proved for cote 136 (scans 8-10 and 233).

### SA09-6 · polynomial categories (scans 75-86)

- The axioms are checked: Hom from the target's group structure, Γ^0(X) = 1, and the bialgebras Γ^*(X).
- The composition law through α_{q,p} is checked.
- The struck uniqueness of the grading is rightly withdrawn: λ^n ≡ λ^{n'} mod p for all λ iff (p−1) | (n−n').
- "Je l'avais oublié" (scan 83) is a real omission. The axiom 1 ≅ Γ^q(1) does not follow from the others.
- P_n(X,Y) = Hom(Γ^n X, Y) are Roby's homogeneous polynomial laws.
- His closing question, whether f ↦ Γ^p(f) is a polynomial law on the Hom modules, is the structure later used for
  strict polynomial functors (Friedlander-Suslin 1997). See HUNCHES H2.

### SA09-1 and SA09-7 · codicology and his marks (cote 137)

- Scans 3 and 5 are reused English typescript leaves ("APPENDIX H (Hirsch Method)", "The Model of a Riemannian
  Manifold"). They come from D. Sullivan's minimal-model work (to verify); placed only, credited.
- Scan 6 is a blank sheet, checked on the image. Scan 59 is an upside-down cancelled sheet.
- His marks are checked:
  - "faux" (scan 10): right;
  - "?" (scan 12): right;
  - "à vérifier" (scan 34): justified;
  - "Il faudrait prouver" (scan 51): proved, apart from the essential image, which needs the correction above;
  - "sauf erreur" (scan 64): right.

## Cote 138, scans 1-133: descent of covers, the Fermat tower, the tower of punctured spheres, maps and the Galois action

The dated sheets run from 11 Jan 1977 (scan 106) to June 1978 (scans 43-69), with one sheet of 1980 (scan 3). Each
date bounds only its own sheet from below.

The mathematics is the Galois action on covers of P¹ minus three points, carried through:
- the Fermat (abelian) tower;
- the dihedral and spherical towers;
- the moduli of pinned maps.

**The reader's conclusion, from the Pro notes' placements:** cote 138 is a first draft of La Longue Marche Part I.
- The "à bouts" groupoids, the orientation and peripheral set-up, the Galois transport, the special profinite groups
  and the modular comparison each have their counterpart in LM140-2 (§1, §12, §19, §23, §37).
- The LM transcription itself was not searched in this sweep.

### SA09-10 · descent of covers and fields of definition (scans 4-17)

Checked:
- 𝒢 = Γ ⋉ 𝔾 for a descent datum.
- The criterion for 𝒢' → 𝒢 to be surjective.
- The obstruction to descending a pair to a finite level lies in H²(Γ_i, z), with indeterminacy Hom(Γ_i, z).
- The cases Card S = 2, 3, ≥ 4. A small omission for Card S = 2: t ↦ a/t is missing from 𝔾.

### SA09-11 and SA09-12 · the Fermat tower (scans 18-44)

Checked:
- The sextic Belyi map g(z) = 27z²(z−1)²/(4(z²−z+1)³). The unsure sign is decided by computation:
  4(z²−z+1)³ − 27z²(z−1)² = (2z³−3z²−3z+2)².
- The Fermat-curve computations: χ = 2 − (n−1)(n−2), the torsors E(α)_n, the Jordan block on π_3.
- The octahedron as C_2 (scan 44), with its group 𝔖_4 = (Z/2)² ⋊ 𝔖_3.

**His question "est-on = surjectif ?" (scan 36), answered.**
- The image of Γ for the Kummer torsor of 2 has finite index, but it is not surjective. The obstruction sits at level
  8: √2 = ζ_8 + ζ_8^{-1} ∈ Q(μ_8), so the index is exactly 2.
- The Pro notes of MPL_138_001-045 (C07) found the level-eight answer first; the reader re-derived it.
- Scan 20 ("image de dim n+1 ?", "image d'indice fini ???"): both yes, by the Kummer theory of independent elements
  (Bashmakov, Ribet; to verify).
- A notation clash in (43) on ζ_n is a correction for the apparatus.

### SA09-14 and SA09-13 · explicit covers and the tower of punctured spheres (scans 46-89)

Checked:
- The dihedral cover and the cubic identity. The inserted coefficient 3 is right; the struck 9 is wrong.
- The odd power on the conic. His question "x', y', z' fonctions rat. ?" is answered yes.
- The tame signature list (scan 66).
- The (N,2,2) reduction (scan 68).
- Functors out of a groupoid (scans 58-61). "Aut(C) → 𝔖_{C_0} surjection" needs C connected.
- The bipyramid relation ρ_2^+ρ_1^+ρ_0^+ = id.
- The paradigm of curves, except (g,ν) = (0,2) and (1,0).
- **The special profinite groups (scans 80-89).** Ã_ν → 𝔖_{ν+1} × Ẑ* is surjective, asserted without proof and true.
  π → A_ν° is injective for ν ≥ 2 and not for ν = 1.
- **Scan 85.** The reversal t_ν is an involution up to inner automorphisms. The first index of g_i is under an ink blot;
  the relation forces λ_1.

Slip: scan 84 has μ_{ν+1} where the cyclotomic character χ is meant. Scan 85 has the right form.

**Open on the page:**
- His wish 𝒯_2^! ≃ 𝒯_ν^! (scan 87), the "Lego" principle of the Esquisse.
- The 𝔖_3-invariance target Γ → 𝒯_2^{𝔖_3} (scans 86-87), the first form of the GT symmetry relations.

### SA09-15 to SA09-18 · maps, their moduli and the Galois action (scans 90-133)

Checked:
- 𝒯_ν and the pure spherical braid group modulo its centre. "c'est faux pour ν = 2" is right.
- The torsor formalism (scans 93-96).

**Refuted: "La catégorie des cartes orientées 𝒞_0-épinglées est rigide" (scans 98-99).** The one-vertex torus map
(E = Z/4, σ = +2) has a pinned automorphism of order 2. So the count "(classes) × ∏ a_n!b_n!c_n!" needs the
orbit-size form. This counterexample is the same as the Pro notes MM02 and Michel Hua's project.

**The degree-6 catalogue (scan 117).**
- Every triple satisfies the genus-0 count. The unsure "1_2" readings are decided by Riemann-Hurwitz.
- "f) 4 sommets … impossible" (scan 118) is right.

**The small Belyi maps (scans 104-112).**
- The listed maps are checked.
- "δ = 4" for ②'' must be δ = 2.
- Permutation tables I and II are checked. An enumeration finds 3 maps of passport [3,2,1; 2,2,1,1; 6]; the tables
  list two.
- **Wrong (scan 111):** his roots of δ, c = 16/25 ± (24/25)i, should be 16/25 ± (12/25)i. The halving was missed.

**Operations on maps (scans 121-132).**
- The Théorème of scan 126 is checked.
- **Refuted (scans 129-131):** the orange of order n is preserved by every z ↦ az with a > 0. So "pas d'automorphismes
  hol. ≠ id" is false, as the Pro notes OP33 say. The exception list is incomplete, and the groups in cases I-III are
  real, not Aff(1,ℂ).

**SA09-9, what cote 138 shows before Belyi (1979).**
- It shows a Γ-action on the finite sets of maps and the moduli schemes M^α, which "peut ne pas être triviale".
- It does not show faithfulness, and not Belyi's theorem.

## How the topic connects

- **Cote 137** builds the abstract home (the universal cosimplicial object and the Σ-exact theorem) of cote 136's PD
  de Rham cochains. The weightwise comparison is the same on both sides: SA09-5 against SA08-4.
- **Cote 138** leaves the de Rham line for the Galois action on covers and maps. It is the earliest layer in the
  archive of the La Longue Marche programme: the dated sheets of 1977-78 come before Belyi's theorem, while the
  Fermat-tower sheets are undated.
- **The dependencies, closed by reading,** are in DEPENDS.tsv.
