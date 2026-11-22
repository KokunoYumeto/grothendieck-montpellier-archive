**The attached files.** Besides this file there is one ZIP, `SA08_de_Rham_cote_136_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA08_study.zip` is the folder `RESEARCH_SA08_study/`), so there is nothing more to unpack; every other file is at the top level under its own name.

**The same files in this Space.** Every file of `SA08_de_Rham_cote_136_night.zip` may also be in this Space's files, flat, each named `P007__` followed by its file name; `P007__SPACE_INDEX.tsv` gives, for each such name, its path inside the ZIP. Where they are there, use them as you would the unpacked ZIP; where a Space file and the ZIP differ, the ZIP decides; where they are not there, unpack the ZIP.

# RESEARCH_SA08: Grothendieck's divided-power de Rham complex of 1975-76 and its sequels (cote 136): the multiplicative comparison over k{T}, the automorphisms and the Steenrod question, and faisceautisation

**What is to be settled, in three Parts:**
- **A.** The multiplicative theory of his divided-power ("PD") de Rham cochains. This covers:
  - the cohomology over k{T} as an algebra;
  - the recovery of the cohomology ring from the weighted cochains (the "shadows");
  - the binomial bridge.

  A.1 is the main question.
- **B.** The automorphisms of the simplicial PD de Rham algebra:
  - his "three-data theorem" with its missing condition;
  - the group Ω;
  - whether Steenrod squares come from these automorphisms.
- **C.** Faisceautisation: his "Non" for the cosimplicial topos, universal flasqueness, and his uniqueness conjecture.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA08`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a34c04448e8299803, on 19 Nov 2026. It is the
deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at
effort max).

## What is attached

- **`RESEARCH_SA08_study.zip`: our study of cote 136.**
  - `study/STUDY.md`: the topic worked through, item by item.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the full readings, each with its tables.
    - `136_002-141.md`, by the reader a1f628dde2f29df92;
    - `136_142-376.md`, by aa2156d1c23970b0d, for scans 142-281;
    - `136_282-376.md`, by aa2156d1, for scans 282-376 and the rest of 235-281.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the topic's items SA08-1 to SA08-35.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded
    in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA08_transcriptions.zip`: the AI transcriptions (LaTeX) of cote 136.**
  - Seven packages by GPT-6 Astra (ChatGPT Pro mode), each with notes and doubts: scans 2-46, 47-94, 95-141, 142-188,
    189-234, 235-281 and 282-327.
  - Three folders by GPT-6 Astra at reasoning effort max in Codex web: K136-01 to K136-03, scans 328-376.
  - `\scanpage{N}` marks scan N of the cote's PDF; the archive's sheet number is N−1.
  - The transcriptions carry `\unsure{a|b}` marks. The readings decided some readings on the scan images, and their
    CORRECTIONS tables give them. Where a step of yours depends on a doubtful reading, say so.
  - About seventy faces of the bundle are reused pages of the SGA 7 IX typescript (Grothendieck, LNM 288). They are
    known material, not part of this work.
- **No literature is attached.** Fetch the sources listed under "Sources", preferring the arXiv LaTeX source.

## Where this comes from

**The pages.** Cote 136 of the Grothendieck archive at the University of Montpellier is a bundle of about 375 scans,
mostly from 1975-76. Scan 3 reads "Complexe DR à p.d. et ombres des modules" and "Plan conf. IHES en 1976". The bundle
holds:
1. **The construction (scans 4-12).** Sullivan's rational de Rham forms on the simplices make no sense over Z. He
   replaces them by the simplicial PD algebra 𝒜(S, S^+, t), with the universal choice S = k{T} (the divided-power
   polynomial ring) and t = T. This gives a bigraded cochain object C^{••}_DRpd(X, k) = Hom(X_*, Γ^•Φ ⊗ Λ^•Ψ) on
   simplicial sets X. Here Φ is the simplicial module of functions on the vertices, and Ψ = Φ/k.
2. **The theory of "ombres" (scans 20-45 and 244-281).** It recovers modules from their weighted tails τ_N(M ⊗ k{T}).
3. **Integration of forms and his de Rham theorem (scans 48-72).**
4. **Faisceautisation in a topos and "De Rham structures" (scans 74-121).**
5. **The dual coalgebra model (scans 123-159).**
6. **The automorphisms of the simplicial PD algebra (scans 162-212).** Here he hopes for Steenrod squares in
   characteristic 2. Folio 142, just before these leaves, is a computer printout of 16 August 1982.
7. **The four complexes of divided-power algebra and the homotopy computations (scans 215-241).**

**Our reading of them.** Sweep 3 of our horizontal reading (18-19 Nov 2026) read scans 2-281 in full: scans 2-141 by
a1f628dd, and scans 142-281 by aa2156d1, both Claude Opus 5.5 at effort max. On 19 Nov aa2156d1 read scans 282-376,
so all of cote 136 is now read. Every proof on the pages was re-derived as a check event, and every slip was located.

**Other work.**
- H. Cartan's "Théories cohomologiques" (Invent. Math. 35, 1976) is a published account of this construction. Check
  how far it goes.
- Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has a modernised reading of cote 136 and a Lean
  file, Folder136.lean. You may consult them. Credit any point taken from them to "Michel Hua's project", and quote
  phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it
(Rules of proof, 7).

- **R1 (S3-136-002-141-CE001 to CE004; CE-B18). The weightwise comparison.** For every simplicial set X and ring k,
  H^{p,i}_DRpd(X, k) ≅ H^i(X, k) for i ≤ p, and 0 for i > p. This includes the endpoint i = p, by dimension shifting.
  Multiplication by T^{(a)} acts from weight n to weight n+a by the binomial coefficient C(n+a, a), so products appear
  weighted.
- **R2 (S3-136-002-141-CE008). His Remark a) (scan 12).** C_DRS(X, k ⊗ Q) ≅ C^{••}_DRpd(X, k)/(T − 1) holds for every
  simplicial set, with his literal cochains of unbounded weight. It fails for finite-weight cochains on infinite X.
- **R3 (CE013, CE016). The rigidity of the tail.**
  - Théorème 1 (scan 23): if C(j,i)(x_j − x_i) = 0 for j > i ≥ N, then x_i = x_N.
  - The weighted theorem (scans 27-34): M ⊗ k{T} ≅ φ_{0N}τ_N(M ⊗ k{T}) in degrees ≥ 0.
  - Both are proved on the pages; the slips are listed.
- **R4 (CE018). The Ext corollary of scan 27, in its first case.** For k = M = F_p, i = 0, N = 1, Ext^n(τ_N S, S) = 0
  for n ≥ 1 for graded modules. It is false ungraded, where Hom(S^+, S) ⊋ S. The general case is unproved.
- **R5 (CE022). Shadows of CP².** H^*(CP²; Z) admits no PD structure, but its shadow algebra does:
  γ_m(xT^{(n)}) = x^m(T^{(n)})^{(m)}. The descent of the cochain-level PD structure to cohomology is not proved.
- **R6 (CE023, CE027). The weight-zero corner.** C^{0,q}(X) = Z^q(X; k), the cocycles. The strictly alternating
  product on ⊕_qΛ^qΨ induces C(p+q, p)·cup on cohomology.
- **R7 (CE-A12, CO-A03, CE-B02, CO-B01). The three-data theorem (scans 162-164).**
  - Homomorphisms φ: 𝒜_S → 𝒜_{S'} correspond to data (φ_0, A', (B'_i)) under his three conditions together with a
    fourth that the page omits:
    (M) c_{ij}B'_{i+j} = A'^{(i)}B'_j + A'^{(j)}B'_i for all i, j ≥ 1.
  - (M) says that X^{(i)} ↦ B'_i is a derivation along φ_A.
  - Over a Z-torsion-free S', every homomorphism commutes with the divided powers. Over an F_p-algebra, the B's are
    free on the B'_{p^m}.
  - Counterexample to the list without (M): over F_2, A' = X_0 and B'_2 = 1.
  - His own vertex-reversal identity on scan 192 gives (M) at i = j = 1.
- **R8 (CE-A15). His margins of scans 170 and 172 are false in general.** They claim the condition is "vide si 2
  inversible". A reduced counterexample over F_3: A' = 0, B'_3 = T^{(5)}.
- **R9 (CE-A21, CE-A22). Ω (scan 178), corrected.** With (M) and 2B = 0, the B-part is free on B_1, B_2, B_4, …, under
  a convergence condition. Ω is the ind-scheme G_m ⋉ (pro-unipotent A-part) ⋉ ∏_{(j,h)} ⊕_m ₂G_a, not an affine scheme.
- **R10 (CE-B12, CE-B14, CE-B16, CE-C02, CE-C04). Four statements of his are false as written.**
  - The weight vanishing of scan 222: n is the weight, not the cohomological degree.
  - "Γ^i(Ψ) et Sym^i(Ψ) sont des K(k,i)" (scan 229).
  - "Γ^p(Ψ) ≃ K(k,p)" (scan 239). It is contractible when p! is a unit.
  - The valuation criterion of scan 241. The equality holds iff i+1 ≢ 0 mod p².
- **R11 (CE034, CE036).**
  - DR_sp(X, k)_0 is a point, because k{T} is an initial object.
  - "flasque + plat ⇒ homotope à 0" (scan 100) is false: the constant k_* in Δ̂ is Γ-acyclic and not contractible.
- **R12 (CE-D01 to CE-D06). The equalizer recovery of scan 275 holds for every k-module M.**
  - On 279 the ink has τ_N, which makes "Le foncteur τ_N i_* est pl. fid." trivial.
  - The σ_N statement that the line before sets up is true.
- **R13 (CE-F02 to CE-F06). PD structure on Hom out of a coalgebra (scans 329-335).**
  - For a flat cocommutative coalgebra A, the iterated coproducts give a PD structure on Hom(A, J) ⊂ Hom(A, B), the
    composition axiom included. This answers his question ① of 324 for flat A.
  - A non-flat counterexample is in the Pro notes N43.
  - The coefficient of γ^p(γ^q(x)) on 334 has p and q swapped: γ²(γ³(x)) = 10γ⁶(x).
- **R14 (CE-F10 to CE-F13; CO-F04). The notes of scans 362-376.**
  - The décalage of 362 (L_r Sym^i K(M, n+1) ≃ L_{r−i} Λ^i K(M, n)) holds. It answers his question on 229 for
    L = M[1].
  - The first of his three Koszul sequences there is not exact over Z.
  - "Sq¹Sq² = Sq³ + Sq²Sq¹ (?)" (365) is false: Adem gives Sq¹Sq² = Sq³. Michel Hua's project found this first.
  - 374-376 restate Breen's computation of Ext(G_a, G_a), unchecked.
- **R15 (CE-E01 to CE-E08, CE-F01). Projective structures on curves.**
  - The split bundle P(Ω^{-1} ⊕ Ω) of 327 carries no holomorphic connection for g ≥ 2. His boxed task needs the
    nonsplit oper bundle.
  - Lifting the uniformizing representation to SL(2,R) (328) gives degree g − 1, the degree of a theta
    characteristic.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1 (the PD-Rees algebra).** H^*_DRpd(X; k{T}, (T), T) ≅ ⊕_i H^i(X; k) ⊗_k I^{[i]} as graded k{T}-algebras, where
  I^{[i]} = span_k{T^{(p)} : p ≥ i}. Consequences:
  - the map to H^*(X; k{T}) is injective, with cokernel ⊕_i H^i(X; k) ⊗ k{T}/I^{[i]};
  - the shadow categories of scans 244-281 study exactly the modules P ⊗ I^{[N]}.
- **L2 (the binomial bridge).** C^{••}_DRpd(X, Z) is the associated graded, for the degree filtration, of a cochain
  model built from integer-valued polynomials on the simplices. Grounds: gr Int(Z) ≅ Γ_Z(T).
- **L3 (the weight-zero corner).** The ring ⊕_q Λ^qΨ supplies the products and divided powers on DR^{0,*} that he asks
  for on scan 77 ("plus les axiomes divers qu'il faut").
- **L4 (operations).** Ω acts on cohomology only through the determinant Δ, in every characteristic. So the
  characteristic-2 automorphisms induce no Steenrod squares, and his marginal "Non" on scan 182 is right.
- **L5 (universal flasqueness).** A simplicial abelian group that is acyclic on every slice Δ̂/X is contractible.
- **L6 (cosimplicial topos).** In the topos of cosimplicial sets no mono Z → Φ exists with flat cokernel and universally
  flasque Γ^iΦ, Λ^iΦ.
- **L8 (the target of the operations).** If Ω acts on the PD de Rham cohomology over F_p by operations, these have
  coefficients in G_a. They lie in the algebra 𝒜 of scan 374 (the P^i with the Adem relations, P^0 acting as Frobenius),
  not in the Steenrod algebra.
- **L7 (dating).** The leaves of scans 144-212 were written in 1982-83, near Pursuing Stacks §§117-139. The proof of
  this lead is documentary; give your reasons and sources, but do not let it take time from A-C.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most
of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the
smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach
stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter
search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then
push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided
step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for all rings proved over
a field or over Q without saying so; a step that replaces a claim by a convenient special case without naming it; a
reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions are AI-made and carry
doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA08_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The multiplicative theory. The main question is A.1.**
- **A.1 (main).** Determine H^*_DRpd(X; k{T}, (T), T) as a graded k{T}-algebra, for every simplicial set X and every
  ring k, with its products.
  - Prove L1, or refute it and give the correct statement with its proof.
  - Include the action of every T^{(a)} and the compatibility of the weight isomorphisms of R1 with products.
  - Then extend the answer to an arbitrary PD triple (S, S^+, t), and to the completion that scans 233-239 begin. Do
    the completion under the hypothesis k{T} ≅ Gr*(S) and say what holds without it.
- **A.2.** His main claim (scans 11-12): the ring H^*(X; Z), and RΓ(X, Z) with its product in D(Z), are recovered
  functorially from C^{••}_DRpd(X, Z) with its products, through the shadows.
  - Prove it or refute it with the correct statement.
  - This includes the Ext corollary of scan 27 in general: Ext^n(τ_{N−i}(S)[−i], M ⊗_k S) = 0 for n > 0, for graded
    S-modules (R4).
  - It also includes his "?" on the derived unit of scan 273.
- **A.3.** Divided powers on shadows (R5). Determine whether the PD structure of the cochains induces a PD structure on
  the weighted cohomology ⊕_i H^i(X; k) ⊗ I^{[i]} in every case, and what it is.
- **A.4.** Prove or refute L2. If it holds, compare the filtered model with Toën's affine stacks and Horel's binomial
  cochains, and with Mandell's E∞ theorem: say exactly what the 1976 object recovers of the integral homotopy type of a
  nilpotent space of finite type. If it fails, determine what the associated graded is.
- **A.5.** Prove or refute L3: the products and divided powers on DR^{0,*} of scan 77 are those of ⊕_q Λ^qΨ, and with
  them DR is a PD-DGA with the shadow properties.

**B. Automorphisms and operations.**
- **B.1.** State the three-data theorem with condition (M) for every PD triple, and prove it (R7, R8).
  - Determine Ω (scans 174-180) exactly, as a functor on rings with its group law (R9).
  - Prove the converse of his determinant criterion: Δ(φ) a unit ⇒ φ an automorphism.
- **B.2.** His sentence on scan 180, "seules les op. évidentes (se factorisent par Δ)". Determine the action of Ω on
  H^*(Hom(X, Â_k)), including the φ_0-semilinear action on the coefficients k{{T}}, and prove L4 or refute it.
- **B.3.** The Steenrod question (scan 182). In characteristic 2, determine the operations on H^*(X; F_2) induced by
  the B-automorphisms, and by the automorphisms of his τ_ω functor.
  - Decide whether any Steenrod square arises, and prove the answer.
  - The reduction in `study/RESEARCH_PACKAGES.md` (SA08-RP3) gives a cocycle computation on Δ[i+1]/∂Δ[i+1] for each
    component.
- **B.4.** The decompositions of G_k drawn on scan 208, marked "(??)". Determine the structure of G_k and of
  G_k ∩ H_k for every ring k (torsion included), and prove it.
- **B.5.** Prove or refute L8, as part of B.3: determine where the operations induced by Ω, over F_p, sit with respect
  to the algebra 𝒜 of scan 374 and to the Steenrod algebra.
- **B.6.** His question of 352. Does the exterior product on Z^• = Λ^•Ψ_* extend functorially to a "½-algèbre
  différentielle" structure on Λ^{•+1}Φ_* (348-352)? Determine the indeterminacy, decide whether it is a cup-1
  structure, and compare it with the Eilenberg-Zilber and E∞ structures of 357-361.
- **B.7.** His questions of 324:
  - determine the class of cocommutative coalgebras A for which Hom(A, J) carries the PD structure of R13 (flat A is
    proved, and there is a non-flat counterexample);
  - decide the uniqueness of u_n = u_1^{(n)};
  - settle his dual question ②.
- **B.8.** Check every statement of 374-376 against Breen's papers, and prove or refute each with an exact citation: the
  theorem on H^*(K(O, m), O), "de F torsion (i > 1)", the perfect-site corollary ("Milne(?)"), and Ext^{2i}(G_a, G_a).

**C. Faisceautisation.**
- **C.1.** Prove or refute L6, his double-underlined "Non" of scan 91.
- **C.2.** Prove or refute L5, and with it repair, or refute, the argument of scan 100 and the Prop. of scan 98 for
  universally flasque structures.
- **C.3.** His uniqueness conjecture for admissible generalized de Rham theories (scans 117-121: "connexe et simplement
  connexe ?", conjectures a) and b)). Determine the correct statement and prove it, or show by an example which form
  fails.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- H. Cartan, "Théories cohomologiques", Invent. Math. 35 (1976). D. Sullivan, "Infinitesimal computations in topology",
  Publ. Math. IHÉS 47 (1977).
- B. Toën, "Le problème de la schématisation de Grothendieck revisité", Épijournal Géom. Algébrique 4 (2020).
  G. Horel, "Binomial rings and homotopy theory". M. Mandell, "Cochains and homotopy type", Publ. Math. IHÉS 103 (2006),
  and "E∞ algebras and p-adic homotopy theory", Topology 40 (2001).
- N. Roby, "Lois polynômes et lois formelles en théorie des modules", Ann. ENS 80 (1963), and "Les algèbres à
  puissances divisées", Bull. Sci. Math. 89 (1965). P. Berthelot, *Cohomologie cristalline des schémas de
  caractéristique p > 0*, LNM 407, ch. I. Séminaire H. Cartan 7 (1954-55).
- L. Illusie, *Complexe cotangent et déformations* I, LNM 239, ch. I (décalage, Γ and Λ of simplicial modules).
  A. Dold and D. Puppe, "Homologie nicht-additiver Funktoren", Ann. Inst. Fourier 11 (1961).
- N. Steenrod and D. Epstein, *Cohomology Operations* (1962). J. P. May, "A general algebraic approach to Steenrod
  operations", LNM 168 (1970).
- Y. Félix, S. Halperin, J.-C. Thomas, *Rational Homotopy Theory*, §10. M. Cenkl, "Cohomology operations from higher
  products in the de Rham complex", and M. Cenkl and T. Porter on integral de Rham theory (as the Pro notes cite them).
- R. Kageyama, arXiv:2211.03289 and arXiv:2405.11570 (the PD simplex), as cited in Michel Hua's project.
- SGA 4 V (flasque sheaves); P. Goerss and J. Jardine, *Simplicial Homotopy Theory*.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the ring k and its torsion, the PD triple, the class of simplicial sets,
   gradings and completions, the weight convention). Do not replace it by a convenient special case. If you prove a
   special case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it lives (graded modules over k{T}, simplicial
   modules, cosimplicial algebras, D(k)), and each extra property you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "pass to the completion") comes with its comparison map and a proof
   that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism of graded algebras; isomorphism of k{T}-modules
   only; quasi-isomorphism; homotopy equivalence of simplicial modules; isomorphism in D(k) as against an isomorphism
   with products.
5. Check the edge cases in scope: characteristic 2 and 3 and torsion in k; k not flat over Z; infinite simplicial sets
   and cochains of unbounded weight against finite weights; graded against ungraded modules; weight 0 and the endpoint
   i = p; t = 0.
6. A counterexample is given completely and, when finite, checked by a program whose code and output you attach. One
   verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep
   the two apart.
7. No authority. Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Known results are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never
   invent a reference; mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper
   (the arXiv e-print) where one exists.

## What to deliver

One ZIP containing:
- `RESEARCH_SA08_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA08_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA08_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA08_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted,
  with the statement number); then what you read, what you computed (every program with its scope, counts and run time),
  and every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry ids such as S3-136-002-141-CE008 and CE-A12; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA08_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
