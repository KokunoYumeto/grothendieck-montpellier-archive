# RESEARCH_SA02: Grothendieck's theory of quadratic covers over an arbitrary base, their contracted product and his generalized Arf-Stiefel-Whitney invariants (cotes 84, 77 and 83)

**To be settled:** the theory of quadratic covers over an arbitrary base that he builds in cote 84 (late 1984 or after) on the ground of cotes 77 and 83: its classification of quadratic covers where 2 is regular, in characteristic 2 and in general; the contracted product and the rank-4 Azumaya algebras it produces; his χ-trivialized extensions and their signs; and the "invariants d'Arf-Stiefel-Whitney généralisés" he announces on 84/43. A.1 is the main question.

Cotes 90 and 91/2-18, also in this topic, are worked through in their own prompts (the working-through objects H01J, H01K and H01L); they are not part of this one.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA02`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It leads topic SA02 in sweep 3 (wave 1) and swept the topic in sweep 1. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA02_study.zip`: our study.**
  - `study/STUDY.md` (it lists what was not read in full), `study/HUNCHES.md`, `study/RESEARCH_PACKAGES.md`, and the tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: cote 84 in full (reader R4) and cotes 90 and 91/2-18 (reader R3), each Claude Opus 5.5 at effort max.
  - `study/SA04_cote77/`: the reading of cotes 76-79 by R4 for topic SA04, whose cote-77 part ("Extensions quadratiques", 77/21-86) is the ground of A.2, with its check events and corrections.
  - `study/SA01_cote83/`: the reading of cote 83 (and 93/92-134) by R1 for topic SA01, with its tables: the rank-4 Azumaya algebras and the ∗-product.
  - `study/stage_A_dossier_SA02_part2/`: the stage-A topic dossier of cotes 84, 90 and 91/2-18, made by GPT-6 Astra (ChatGPT Pro mode) on 19 Nov 2026 (`SA02_dossier.md`, `SA02_directions.md`); its claim ids refer to its own tables, which are not attached.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the items SA02-1 to SA02-n.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026, except the stage-A dossier. It was checked as recorded in the CHECK_EVENTS tables and nowhere else.
- **`RESEARCH_SA02_transcriptions.zip`: the AI transcriptions (LaTeX) of his pages, with their notes.**
  - `transcriptions/Pro/`: by GPT-6 Astra (ChatGPT Pro mode), each with its notes and doubt table: 84/97-145, 84/146-193 and 83/178-222.
  - `transcriptions/Codex/K84`, `K77`, `K83`: the Work returns of batch K, by GPT-6.2 Astra at reasoning effort max for most folders and GPT-6 Astra at reasoning effort max for the others (`transcriptions/Codex/AUDIT_K_RETURNS_20261118.tsv` gives the model of each folder). K84-01 to -07 are the only witness of 84/2-111.
  - `\scanpage{N}` marks scan N of the cote's PDF. Where a step of yours depends on a doubtful reading, say so.
- **`RESEARCH_SA02_broad.zip`:** the sweep-3 studies of SA04 (regular polytopes over rings, cotes 69-102) and SA01 (cotes 71-83), and the sweep-2 map of SA03 (deformations and crystals).
- Fetch the literature yourself. It is listed under "Sources" below.

## Where this comes from

His pages are in the Grothendieck archive of the University of Montpellier. They were transcribed by AI (above) and studied in our horizontal sweeps by Claude Opus 5.5 at effort max.

- **Cote 77 (1977-78), "Extensions quadratiques" (77/21-86).** Quadratic covers Ω = Spec B with B locally free of rank 2; the affine envelope; D = b² − 4c and Δ(N_{Ω/S}) = −D; Σⁿ and relative divisors; algebras ↔ (L, D) when 2 is invertible; Artin-Schreier in characteristic 2; and a mixed-characteristic theorem, quadratic covers ↔ (L, D, b₀) with a condition mod 4 (Th. 77/57, 77/59).
- **Cote 83 (1982-86).** 2×2 matrices over a ring; rank-4 Azumaya algebras M(b, c, b', c', t) and their criterion (83/075-128); twists and the ∗-product of quadratic algebras (83/129-181).
- **Cote 84 (late 1984 or after; its later pages are on the backs of an October 1984 typescript of Récoltes et Semailles), under the title "invariants d'Arf-Stiefel-Whitney généralisés" (84/43).** Binary forms and their quadratic algebra ("l'invariant d'Arf", 84/9-42); quadratic covers through (L, P₁, Q) (84/44-62); the contracted product (84/63-66, 87-106, 172-192); χ-trivialized extensions (84/66-87, 124-170); three quadratic algebras (84/4, 111-122); a graded monoid with parities (84/2, 54-56).

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of some of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA02-R84-07, -08, -10, -11, -17; SA02-K84-04, -05, -07).** Q(z + T) = z² − δ with z = 2x − T, and the class T₀² ≡ δ mod 4 is well defined; the explicit A = {(b, r): b₀ = r₀T₀} with N(b, r) = (b² − r²δ)/4 is integral. The contracted product: b = b₁b₂, c = b₂²c₁ + b₁²c₂ − 4c₁c₂ and u = 2u₁u₂ + b₂u₁ + b₁u₂, with Q(u) = b₂²Q₁(u₁) + b₁²Q₂(u₂) + 4(Q₁Q₂ − c₁Q₂ − c₂Q₁) exactly (sympy). The Theorem of 84/90 holds for all points (re-proved). Over Z the fixed lattice of σ₁ ⊗ σ₂ in A₁ ⊗ A₂ is {a + pu₁ + qu₂ + ru₁u₂: 2p = rb₂, 2q = rb₁}, which gives the Proposition and Corollary of 84/86-87.
- **R2 (SA02-R84-09, -12, -13, -15, -16; SA02-K84-11, -12, -13).** For χ-trivialized torsors, π(x) = χx − Tψ(x), and (L, P, T), (E, ψ, T with ψ(T) = χ) and χ-retractions are equivalent. Of the two sign conventions of 84/130-140, the plus convention b'ᵢ = bᵢ + χUᵢ gives b'₁ ⊗ b'₂ = b₁ ⊗ b₂ + χU and U'' = U + U' exactly; the minus convention leaves −2χ(U₁U'₂ + U'₁U₂). The "signe étrange" (U₁ ∗ U₂)(x₁ ∗ x₂) = −χ U₁(x₁) ⊗ U₂(x₂) of 84/134-136 is consistent: his map Φ: E → Hom^!(E, L) is −id on L. "2 − χ = 1" on 84/140 is no condition.
- **R3 (SA02-R84-19, -20; SA02-K84-08, -09).** His margin of 84/27, that torsors under the norm-one group U_A are the same for fppf and étale, holds when A is étale and fails in general: over k = F₂(t), A = k[e]/(e²) and Q = tN, the torsor Q(x) = 1 is trivial fppf-locally but not étale-locally (a claim of the stage-A dossier, rechecked). The Corollary of 84/36 needs the hypothesis his proof uses: the automorphism is not the identity near any point of X₀.
- **R4 (SA02-R84-01 to -05).** His graded monoid of 84/2 (even triples (L, δ, T₀), odd pairs (L, δ), β(L, δ) = (L, 4δ, 0)) is associative: associativity reduces to two identities, which hold. The seven quadratic subalgebras of A₁ ⊗ A₂ ⊗ A₃ are the fixed rings of the seven index-2 subgroups of F₂³. The "Théorème récapitulatif" of 84/24-27 is the correspondence between primitive binary forms with values in a line bundle and pairs (quadratic algebra, invertible module) of Kneser and Wood.
- **R5 (SA04-R77-01 to -10; SA04-K77-02, -04, -05).** Cote 77: the calculus of quadratic covers was re-derived (tr = bu, N = cu², b' = b + 2τ, c' = c + τb + τ², the invariance of D); the uniqueness argument of the mixed case (4 regular) and the existence argument (the lifts of b₀ form a torsor under 2L) hold; on 77/74 condition b) should read γ(b₀) ≡ Δ mod 4, as in his Th. 77/59 c); his normalization on 77/101 (μ = 2, not 1/2) and the identity on 77/117 (two signs) are wrong.
- **R6 (SA01-R83-04, -05, and the cote 83 reading).** On H ⊗ H', u ∗ v = bv + b'u − 2uv has eigenvalues t, t' with t + t' = bb' and tt' = b²c' + b'²c − 4cc'; they are the roots of Q(T) = T² − bb'T + (b²c' + b'²c − 4cc'), the two values of Tr(uv) for commuting u and v. M(b, c, b', c', t) is Azumaya exactly when Q(t) is a unit: R1 proved it through the trace discriminant −Q(t)², filling his unfinished "Suffisance" (83/100). The ∗-product gives the composition c = b₂²c₁ + b₁²c₂ − 4c₁c₂ with δ(q₁ ⊗ q₂) = δ(q₁)δ(q₂), which is the contracted product of R1.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1 (A.1).** Cote 84 is a characteristic-free theory of quadratic covers and of their monoid under the contracted product, aimed at Arf and Stiefel-Whitney invariants of quadratic forms over bases where 2 is not invertible ("Arf(E) ... plus fin que c₁(E) (si 2 non inv. sur X)", 84/2). His graded parity monoid and the χ-trivialized extensions should give an invariant of a form of rank n as an element of the graded monoid, finer than the discriminant when 2 is not invertible. Modern counterparts to compare: Voight's monoid of quadratic rings (its product is his Construction 3.14), Loos's graded discriminant algebras, Wood (2011), Dallaporta (2025).
- **L2 (A.2).** The mixed-characteristic classification by (L, D, b₀) describes the stack of quadratic algebras [A²/(G_a ⋊ G_m)] through the discriminant; it is not stated in this form in Knus, Loos, Voight or Wood.
- **L3 (A.3).** The ∗-product of cote 83 and the contracted product of cote 84 are one composition law, Voight's monoid product, and they agree with Bhargava's composition restricted to the diagonal case; the discriminant Q of a pair of quadratic subalgebras, whose roots are the commuting values of Tr(uv), is the same object.
- **L4 (A.4).** The "signe étrange" of 84/134-136 and the sign of the odd-odd product of 84/2 are one phenomenon, a Koszul sign of the odd part. Loos's odd-odd formula has minus four times the product where Grothendieck has plus four (a point of the stage-A dossier); the sign comes from the anti-identification −id: L → Hom(M, L).

## What the outcome must be

{{OUTCOME}}

## Parts

**A. Quadratic covers over an arbitrary base (cotes 77, 83, 84). The main question is A.1.**
- **A.1 (main).** His "invariants d'Arf-Stiefel-Whitney généralisés" (84/43, 84/2). Settle L1: determine, for a quadratic form E of rank n over a scheme X on which 2 need not be invertible, the invariant Arf(E) that his graded parity monoid and his χ-trivialized extensions are built to carry, prove that it is additive for orthogonal sums through the contracted product, and prove or refute his claim that it is strictly finer than c₁(E) (and than the discriminant) when 2 is not invertible on X. Relate it to Loos's graded discriminant algebra and to Voight's monoid, with locators.
- **A.2.** The classification of quadratic covers, in his three settings:
  - (a) where 2 is a non-zero-divisor: covers ↔ (L, D, b₀) = (L, δ, T₀) with T₀² ≡ δ mod 4 (77/53-64, 77/74-86; 84/44-56): full faithfulness, the essential image (b₀² = D on S₀ = V(2) and D₁ = γ(b₀) on S₁ = V(4), Th. 77/59), and his criterion that Δ = b² − 4c if and only if the étale algebra A_{2Δ}[√Δ] extends over A_Δ (Th. 77/57);
  - (b) in characteristic 2: covers by (L, P₁, T, α) as torsors under G_T = ker(u ↦ u² + Tu) (84/57-58);
  - (c) in general: covers by (L, P₁, Q) (84/59-62).
  Prove each in full or refute it with the corrected statement, and settle L2, with locators (Knus, Loos, Voight, Wood, Dallaporta).
- **A.3.** The contracted product over every base: the integral formula (R1), the kernel Ann(2, b₁, b₂)·U of A → A₁ ⊗ A₂, the fixed-ring criterion 2O + b₁O + b₂O = O (checked over Z), and the Theorem of 84/90. Then the rank-4 Azumaya algebras of cote 83: prove over every base that M(b, c, b', c', t) is Azumaya if and only if Q(t) is a unit (R6), and settle L3.
- **A.4.** The χ-trivialized extensions (84/66-87, 124-170): give one coherent sign convention for the monoidal structure (R2: the plus convention and the sign of the dual), prove its coherence constraints, and settle L4.
- **A.5.** Three quadratic algebras (84/4, 111-122): state precisely and prove or refute his statements on the rank-4 subalgebras of A₁ ⊗ A₂ ⊗ A₃ and on quasi-biquadratic systems, in the étale case and over any base, with the corrected lemma of 84/120 (SA02-K84-10).

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- M.-A. Knus, *Quadratic and Hermitian forms over rings* (Springer, 1991), ch. I-III.
- O. Loos, "Discriminant algebras of finite rank algebras and quadratic trace modules", Math. Z. 257 (2007); his work on graded discriminant algebras (1997).
- J. Voight, "Discriminants and the monoid of quadratic rings", Pacific J. Math. (2016).
- M. M. Wood, "Gauss composition over an arbitrary base", Adv. Math. 226 (2011).
- M. Kneser, "Composition of binary quadratic forms", J. Number Theory 15 (1982).
- M. Bhargava, "Higher composition laws I", Ann. of Math. 159 (2004).
- Dallaporta (2025), on quadratic algebras where 2 is regular (locator to be found).

{{RULES}}

{{DELIVER}}
