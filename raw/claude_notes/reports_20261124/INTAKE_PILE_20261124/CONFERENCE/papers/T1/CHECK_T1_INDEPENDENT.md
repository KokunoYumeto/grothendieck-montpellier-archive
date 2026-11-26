# Independent check of the T1 paper (degree-one Singer vanishing in every dimension n ≥ 3)

Checker: agent a24b3bc642b5dfddf (Claude Opus 5.5 at effort high), on the brief of the main session 329fb1e6 (Claude Opus 5.5
at effort max), 25 Nov 2026, about 05:40-07:10 UTC. I am the agent that checked the replacement Section 2 of the Q02 run (GPT-6
Astra, ChatGPT Pro mode) on 24 Nov. The paper was written by aee0b161c47a54e8f (Claude Fable 5.2 at effort max).

Text checked: `src/T1_paper.tex` (749 lines, 25 Nov), against:
- OpenAI's preprint itself: `paper.pdf` and the TeX in `build/` of
  `github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026`, fetched through the
  GitHub API on 25 Nov. Its only commit is adc7f124 of 6 Oct 2026. Working copy:
  `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15\scratchpad\t1\`.
- Every outside source the brief names, from free copies.

I did not edit the paper. Events: `CHECK_T1_INDEPENDENT_CHECK_EVENTS.tsv` beside this file.

---

## 1. Verdicts, statement by statement

| Item | Verdict | Repair |
|---|---|---|
| Lemma 2.1 (finiteness) | **holds**, followed | none |
| Lemma 2.2 (duality over F₂, Shapiro) | **holds**, followed | none |
| Corollary 2.3 | **holds** | none |
| Lemma 2.4 (one end) | **holds**, followed | none |
| Lemma 2.5 (no splitting over J) | **holds**, followed | none |
| Corollary 2.6 | **holds**; Wall's Lemma 4.1 opened and says what is used | none |
| Lemma 2.7 (comparison) | **holds**, given that von Neumann dimension is faithful and unchanged under bounded equivariant bijections | R1: the citation for that fact was not opened; add the two-line proof (3.1) |
| Lemma 2.8 (gradient) | **holds**, followed | none |
| Lemma 2.9 (L²-duality) | **holds**, followed; Wall §1 opened, and his proof of Lemma 1.1 gives exactly the chain map and the Whitehead step used | none |
| Lemma 2.10 (PD(n) groups) | **holds**; two sentences are shorter than their content | R2 (optional; 5.2) |
| Theorem A | **holds given Theorem C**; manifold paragraph: Hanner, West and Spanier opened and match | R3 (one clause on Spanier's duality map; 5.3) |
| Theorem B | **holds given Theorem C** | none |
| §3.1 (the preprint's theorem; Lemmas 2.1-2.7) | **correct** against `introduction.tex`, `foundations.tex` and the PDF numbering | R4: the abstract's "released in September" (3.4) |
| §3.2: "five places, and nowhere else" | **correct** (2.2) | none |
| Table 1: numbers and statements | **correct**: the PDF numbers 3.1-10.3, 38 statements, in the table's order; each description matches its statement | none |
| Table 1: "uses directly" | **correct except four omissions** (rows 4.5, 6.5, 7.4, 9.6); one optional addition (row 6.3) | R5 (3.5) |
| §3.3, outside results | **one omission**: Bowditch, Treelike, Lemma 6.2 and Proposition 6.4, cited in the preprint's §4. Theorem 6.1's description drops a hypothesis | R6 (3.6) |
| §3.4 (the check): which sections are identical | **understated**: at sentence level Sections 4 and 5 are identical too | R7 (optional; 5.7) |
| No use of dimension four in Sections 3-10 | **confirmed**: only the last proof, after 10.3, which the paper replaces | none |
| Remark 4.1 (dimension two), Remark 4.3 (3.1-4.5 use (G0)-(G3) only) | **correct** | none |
| §1.3, Lott-Lück | **correct** for orientable M (Theorem 0.1 opened at its statement) | R8 (3.8) |
| §1.3, Davis-Okun Thm 11.3.2 | **correct** | none |
| §1.3, Di Cerbo-Hunter-Thrasher | **correct**: the sentence exists in the introduction | none |
| §1.1, Davis (definition; Thm 7.15) | **correct** | none |
| §1.1, Lück §1.1 | **not opened**: no free copy reachable | R1 removes the dependence |
| §1.3 and [R], the r/math comment | **not opened**: Reddit refuses automated access | R9 (3.9) |
| Bowditch, *Connectedness*, Lemma 1.4: its proof | **read in full**; in the setting of Theorem C it reduces to two inputs, one of them opened (2.3) | R10 (optional; 3.10) |

No mathematical error found. The repairs are an omitted citation proof (R1), wording (R2-R4, R7-R10) and the table's
dependency column (R5, R6).

---

## 2. The four items of the brief

### 2.1 Section 2 as written, compared with the Q02 Section 2 checked on 24 Nov

I followed every proof to its end.

- **Lemma 2.1** = the run's `found:model`, first half.
  - Torsion: a free resolution of length m restricts to Z C, against H^{2r}(C;Z) = Z/p.
  - Infinite: H_n(Q;F₂) = F₂ for n ≥ 1.
  - The manifold half is moved to the proof of Theorem A.
  - Same mathematics.
- **Lemma 2.2, Corollary 2.3** = `found:duality`.
  - Z^w ⊗ V ≅ V over F₂, because −1 = 1.
  - Homological Shapiro via kΓ ⊗_{kJ} k ≅ k[Γ/J].
  - The degree conditions n − 1 > 0, n − 2 > 0, n − 1 ≥ 2.
  - Same mathematics, shorter. The two-ended part moved to Corollary 2.6.
- **Lemma 2.4** = `found:ends`, first half, stated for any infinite finitely generated group. I checked:
  - the bijection Φ between finitely supported cochains and module cochains;
  - Φ(da) = Φ(a)∂;
  - that Φ(df) kills the image of P₂: df(g⁻¹z) = f(∂g⁻¹z) = 0 for finite cycles z;
  - the contradiction from f − u constant;
  - that G − A has finitely many components, each meeting a neighbour of A.

  The run's second half (finite-support correction through H²) is not in T1's Section 2. That is correct: the preprint does it
  inside its Proposition 5.3, which T1 cites.
- **Lemma 2.5** = `found:trees`, stated for one edge orbit. Checked:
  - the cocycle c(gh) = c(g) + g c(h) (backtracking edges cancel in pairs mod 2);
  - the bound |[o,go]| ≤ 2|supp v|;
  - bounded orbit ⇒ fixed vertex (no inversions).

  **New in form**: only splittings, not arbitrary actions. That is all Theorem C needs (its hypothesis is about splittings),
  and Bass-Serre makes "splitting" the one-edge-orbit tree action.
- **Corollary 2.6.** Wall's Lemma 4.1 opened (Ann. Math. 86 (1967) p. 231; free copy at
  `webhomes.maths.ed.ac.uk/~v1ranick/papers/wallpoincare.pdf`): a two-ended group has a finite normal subgroup with quotient
  Z or Z₂*Z₂, proved from "an infinite cyclic subgroup of finite index", which is T1's definition of two-ended. Holds.
- **Lemma 2.7** (new in form: harmonic chains in place of modules over the von Neumann algebra). Checked:
  - the lifts f_i, g_i, i = 0, 1, 2 (f₂ exists because ∂'₁f₁∂₂ = f₀∂₁∂₂ = 0 and the target is exact at P'₁);
  - the homotopies h₀ and h₁ (∂₁(g₁f₁ − 1 − h₀∂₁) = (g₀f₀ − 1 − ∂₁h₀)∂₁ = 0);
  - that f₁ preserves ker ∂₁ and the closure of im ∂₂ on completions (f₁∂₂ = ∂'₂f₂);
  - that g₁f₁ − 1 = ∂₂h₁ on ker ∂₁.

  So reduced homology in degree one has a bounded equivariant inverse pair of maps. The step from there to equal dimensions
  is the cited property of von Neumann dimension: see R1. The second statement (all degrees, bounded chain homotopy
  equivalence) is the same argument. The consequences drawn after the lemma hold: C_*(Q̃) is exact in degrees 0 and 1
  because Q̃ is simply connected, and homotopy invariance holds.
- **Lemma 2.8** = `found:gradient`, first half. Checked:
  - D = ker d₁ by simple connectivity of the Cayley 2-complex;
  - D₀ = closure of im d₀;
  - D ⊖ D₀ = ker ∂₂* ∩ ker ∂₁ (real), whose complexification is the harmonic space;
  - faithfulness of the dimension (also R1).

  The run's second half (a bounded representative not constant at infinity) is in the preprint's Lemma 3.1, which T1 cites.
- **Lemma 2.9** = `found:reduction`, shorter: it cites Wall for the chain-level cap product where the run wrote out the
  signs.
  - Wall §1 opened (pp. 214-215). The definition uses coefficients Λ = ZΓ only. Lemma 1.1 extends to every module, and its
    proof builds the chain map Hom_Λ(C, Λ) → C by a cellular diagonal and Steenrod's slant product, and concludes "by a
    result of J.H.C. Whitehead" that it is a chain homotopy equivalence because both complexes are finitely generated
    projective. That is T1's citation and its mapping-cone step.
  - Wall's anti-automorphism Σ n(g)g ↦ Σ w(g)n(g)g⁻¹ is T1's.
  - The adjoint identification: right multiplication by a† = Σ w(g)a_g g⁻¹ equals U_w R_a* U_w on ℓ²(Γ), since
    U_w R_g U_w = w(g)R_g and the coefficients are integers. So the dual boundary in degree p is, up to sign and the
    U_w-conjugation, ∂*_{n−p+1}, and the harmonic p-chains of C^{n−*} are those of degree n − p of C.
  - Negative degrees of C^{n−*} (when dim Q > n) are allowed by the second statement of Lemma 2.7.
  - Holds.
- **Lemma 2.10** = the run's l. 822-936. Checked:
  - torsion-freeness;
  - the removal of negative degrees of D (lowest term has zero homology, the surjection splits);
  - the comparison D ≃ P̄^w over ZΓ;
  - Hom(L, ZΓ) ⊗ V ≅ Hom(L, V) for finitely generated projective L;
  - the dual of a projective completion: Q_H : im e* → H, with inverse e*|_H. Q_H e* h = h for h ∈ H because
    ⟨e*h, h'⟩ = ⟨h, eh'⟩ = ⟨h, h'⟩; and e* Q_H x = x for x ∈ im e*, because (1 − Q_H)x ∈ H^⊥ = ker e*.

  Two sentences compress steps (R2).
- **Theorems A and B.** Both deductions followed.

**What is new in form relative to 24 Nov:** Lemma 2.7 (harmonic chains), Lemma 2.5 (splittings only), and the shortened
Lemmas 2.9 and 2.10. All hold. Nothing of the run's Section 2 that Theorem C needs is missing. The parts not in T1's
Section 2 (the H² correction, the bounded non-constant representative, the Bowditch implication (B)) are inside the
preprint's Sections 3-6, which T1 cites.

### 2.2 Section 3 and Table 1 against the preprint itself

- **Numbering.** I extracted the PDF text (45 pages) and listed every numbered statement. Section 2 has Lemmas 2.1-2.7, in
  the order T1's §3.1 describes: model, comparison, reduction (L²-duality), duality (H^i(Γ;F₂Γ)), ends, trees, gradient.
  Sections 3-10 have 6 + 5 + 3 + 5 + 4 + 4 + 8 + 3 = 38 numbered statements, 3.1-10.3. These are T1's numbers, and each of
  T1's descriptions matches its statement. Section 11 (Corollaries 11.1-11.3: Euler characteristic, signature, Lück
  approximation) is outside Sections 3-10 and is the only other place where four enters.
- **The five places.** I listed every `\ref`/`\cref` to a Section 2 label (`found:*`), every citation, and every
  occurrence of "four", "Poincaré", "duality", "torsion", "one-ended", "splitting" and "finitely presented" in
  `compactification.tex` through `conclusion.tex` (`annular-chains.tex` is input inside `path-pushing.tex` and is a figure).
  The places are:
  1. `compactification.tex` l. 4-9: the inputs, with connectedness, local finiteness, one end, simple connectivity, bounded
     incidence, and D₀ ⊊ D.
  2. `dynamics.tex` l. 242-249: the proof of 4.5 uses torsion-free and one-ended.
  3. `boundary-topology.tex` l. 116 and l. 175: Lemma 2.4 = `found:duality`, twice, only for H²(Γ, kΓ) = 0.
  4. `pretree.tex` l. 5-7: the hypotheses of Sections 6-7, which are (G1), (G2), (G3), (G5); `blocks.tex` uses torsion-freeness
     at l. 334, and its §7 opening uses (G1) through the tree.
  5. `conclusion.tex` l. 117-131: Lemma 2.3 = `found:reduction` for the other degrees.

  There is no other reference to Section 2, and no other use of Q, its dimension or duality. **Confirmed.**
- **Dependencies, row by row.** For each of the 38 statements I extracted the references in its statement and proof (script
  `deps.py` in the working copy) and read the passages where the script showed something the table does not list. Four rows
  omit a direct input, and one row could name a citation (R5):
  - **4.5**: its proof uses 3.5 (B is a nondegenerate continuum, so the classification applies). It also uses the two facts
    stated after 4.3 with Bowditch's Treelike Lemma 6.2 (every infinite-order element of a convergence action on a compact
    space with at least three points is parabolic or loxodromic) and Proposition 6.4 (a point stabilizer containing a
    loxodromic is virtually cyclic): "Since all of Γ fixes c, the stabilizer statement cited above would make Γ virtually
    cyclic" (`dynamics.tex` l. 246-248).
  - **6.3**: the last line of its proof uses "the infinite-order classification" (Lemma 6.2 of [BoT]) besides 6.1
    (`pretree.tex` l. 164-165). Optional.
  - **6.5**: the last paragraph of its proof uses (G5): "Bass-Serre theory then yields a nontrivial splitting over that edge
    stabilizer, contrary to the hypotheses" (`pretree.tex` l. 391-395, a finite edge stabilizer). The table lists only
    (G1), (G2).
  - **7.4**: its proof uses 6.2: "The cut-point stabilizer conclusions in Lemma `pret:parabolic-cuts` make this element
    parabolic" (`blocks.tex` l. 334-336).
  - **9.6**: its proof uses 7.4 (`path-pushing.tex`, the setting of Proposition `block:setting`).
- **No dimension four.** Confirmed: the only occurrences in Sections 3-10 are "covering dimension" and "four images" (9.6),
  and the final proof after 10.3.
- **§3.4.** A whitespace-normalized sentence comparison of the preprint's Sections 3-10 with the Q02 reproduction
  (`Q02-solution.tex`) finds every sentence of Sections 3, 4, 5, 7 and 8 verbatim in the reproduction. It finds 3 differing
  sentences in Section 6 (wording), 10 in Section 9 (the end of 9.8, and the `\input` line of the figure), and 4 in
  Section 10 (10.1 for an abelian group k in the preprint against F₂ in the reproduction, the Kamiya sentence, and the last
  proof). This agrees with T1's description, except that Sections 4 and 5 are also identical (R7). The referee's line-level
  diff may have counted reflowed lines.

### 2.3 Bowditch, *Connectedness properties of limit sets*, Lemma 1.4, at the level of its proof

Author manuscript `Free or receipted/free/authors/bowditch/bhb-connected.pdf`, pp. 3-6. I read Lemmas 1.1-1.4 with their
proofs.
- **The proof of 1.4.**
  - If D is non-trivial, Levitt [L] (non-nesting actions on real trees) or Bowditch [Bo5] (group actions on trees and dendrons)
    give an R-tree Σ with an isometric, non-parabolic action with finite arc stabilisers.
  - No infinite torsion makes the action stable.
  - Finitely many finitely presented subgroups parabolic on D can be taken parabolic on Σ.
  - Rank-two free abelian subgroups are parabolic on D (Tukia [T]).
  - Lemma 1.3, applied to the edge groups of a maximal two-ended splitting (Lemma 1.2) and the virtually abelian vertex
    groups, gives the contradiction that Γ is parabolic on Σ.
- **Lemma 1.3** rests on Bestvina-Feighn [BeF2]: a finitely presented group with a stable non-parabolic action with finite
  edge stabilisers is one-ended virtually abelian or splits over a finite or two-ended subgroup.
- **Lemma 1.2** (existence of a maximal two-ended splitting) rests on Bestvina-Feighn's complexity bound and Dunwoody's
  tracks. Lemma 1.1 is the finite presentation of vertex groups.
- **In the setting of Theorem C** the proof is much shorter:
  - Γ is torsion-free, so arc stabilisers of Σ are trivial and the action is stable with no argument (BeF2, Proposition 3.2
    names trivial arc stabilizers as stable).
  - Under (G5) the trivial graph of groups is already a maximal two-ended splitting, so Lemmas 1.1-1.2 are not needed.
  - Lemma 1.3 reduces to one application of [BeF2] to Γ itself.
- **[BeF2] opened** at its main theorem (Invent. Math. 121 (1995), p. 288; free scan at GDZ,
  `gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0121/LOG_0027.pdf`). Theorem 9.5: a finitely presented group with a
  nontrivial, stable, minimal action on a tree either (1) splits over an extension E-by-cyclic, E fixing an arc, or (2) the
  tree is a line and the group splits over an extension of the kernel by a finitely generated free abelian group. With
  trivial arc stabilisers:
  - (1) is a splitting over a cyclic or trivial subgroup, excluded by (G5);
  - (2) makes Γ act on a line with trivial kernel, so Γ is free abelian, and then b₁⁽²⁾(Γ) = 0 for the elementary reason
    that Γ is infinite amenable.

  So Bowditch's paraphrase of [BeF2] in Lemma 1.3 is accurate, and in Theorem C's setting the lemma holds by the route just
  described.
- **Not opened:** Levitt, *Non-nesting actions on real trees*, Bull. London Math. Soc. 1998; Bowditch, *Group actions on trees
  and dendrons*, Topology 1998 (the construction of Σ from the dendrite); Tukia 1994. The construction of Σ is therefore
  carried at Bowditch's statement.

### 2.4 The citations the writer did not open (free copies only)

| Ref. | Copy opened | Verdict |
|---|---|---|
| [W] Wall, Poincaré complexes I | Ranicki's archive, `webhomes.maths.ed.ac.uk/~v1ranick/papers/wallpoincare.pdf` (JSTOR scan, Ann. Math. 86 (1967) 213-245) | §1, pp. 214-215: the definition (dominated by a finite complex; cap product iso with coefficients Λ), Lemma 1.1 (all modules B, with the chain-level proof); Lemma 4.1, p. 231. **Matches** every use in T1 (definition, Lemma 2.9, Corollary 2.6). T1's definition with every V is Wall's after his Lemma 1.1; T1's "finite" is stronger than Wall's "finitely dominated", which is harmless |
| [L] Lück, L²-invariants, §1.1 | **not opened**: the book is not free; the author's site `him-lueck.uni-bonn.de` refused the connection (ECONNREFUSED) on 25 Nov | R1 makes the citation unnecessary |
| [LL] Lott-Lück, Invent. Math. 120 (1995) | GDZ scan `gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0120/LOG_0008.pdf`, p. 16 (rendered and read); also the MPIM preprint 92-81 | Theorem 0.1 is on p. 16: M a connected sum of compact connected **orientable** nonexceptional prime 3-manifolds with π₁ infinite; its first part gives the L²-Betti numbers. Supports T1's sentence for orientable M (R8) |
| [DO] Davis-Okun, Geom. Topol. 5 (2001) 7-74 | arXiv math/0102104v1 | Theorem 11.3.2 (p. 53): "Suppose S is a GHS^{n−1}, n ≥ 3. Then β₁(S) = β_{n−1}(S) = 0" (S a flag complex; β the ℓ²-Betti numbers of Σ_S). **Matches** |
| [Da] Davis, Poincaré duality groups (Surveys on Surgery Theory 1, Ann. Math. Stud. 145, pp. 167-193) | Ranicki's archive, `.../books/wall1.pdf` | Definitions 3.1, 3.2, Theorem 3.3 (p. 172) and Theorem 7.15 ("in each dimension n ≥ 4, there are PD^n-groups which cannot be finitely presented"). **Matches** T1's definition (Def. 3.2 with R = Z) and its sentence. Page range 167-193 confirmed from the contents |
| [DHT] Di Cerbo-Hunter-Thrasher, arXiv:2601.08804v1 (13 Jan 2026) | arXiv PDF | Introduction: "The Singer conjecture is currently still open even in degree one on negatively curved spaces in dimensions n ≥ 4, [DS22, Section 7]"; §3 repeats it. **Matches** T1's sentence |
| [Ha] Hanner, Ark. Mat. 1 (1951) 389-408 | Ranicki's archive, `.../papers/hanner.pdf` | p. 392: Theorem 3.2 (ANR = local ANR), Theorem 3.3 (a union of open ANR's is an ANR). **Matches** |
| [We] West, Ann. Math. 106 (1977) 1-18 | Ranicki's archive, `.../papers/west.pdf` | (5.3) Corollary, p. 13: compact ANR's are homotopy equivalent to compact polyhedra. **Matches** |
| [Sp] Spanier, Pacific J. Math. 160 (1993) 165-200 | MSP, `msp.org/pjm/1993/160-1/pjm-v160-n1-p13-p.pdf` | Theorem 10.2 (pp. 197-198) and Remark 10.3 (p. 198): duality for every local system on an n-manifold, nonorientable allowed, between Čech-Alexander cohomology of a closed pair and singular homology, by a map θ built from the Thom class. Supports T1's sentence, with the identifications in R3 |
| [R] r/math comment of u/Apprehensive_Sand951 | **not opened**: `reddit.com` refuses the fetch tool, and `old.reddit.com` returns a block page | Our records hold a summary of the user's paste of the thread, not its text (R9) |
| [O] OpenAI, the preprint | GitHub API, 25 Nov | README: "Date: September 25, 2026". Only commit: 6 Oct 2026, the repository's first; `history.md` calls this "our October 6 release". Apache-2.0. See R4 |

---

## 3. Repairs, with exact wording

**R1 (Lemma 2.7 and §1.1: the dimension facts without the unopened Lück locator).** In §1.1 replace "and it is the same for
two such subspaces between which there is a bounded $\Gam$-equivariant bijection \cite[Section~1.1]{L}." by:

> and it is the same for two such subspaces $V,W$ between which there is a bounded $\Gam$-equivariant bijection $T$. Indeed,
> the dimension equals $\sum_j\|\pi\delta_{1,j}\|^2$, and $\pi$ commutes with the action of $\Gam$ that moves $\delta_{1,j}$ to
> $\delta_{g,j}$, so the dimension is $0$ only if $\pi=0$; and the polar
> decomposition $T=U|T|$ has a $\Gam$-equivariant unitary $U:V\to W$, so the two projections are unitarily equivalent by an
> operator commuting with the action and have the same trace \cite[Section~1.1]{L}.

Keep the citation, but mark it in PROVENANCE.md as not opened until someone with the book confirms the locator.

**R2 (Lemma 2.10, optional).**
- After "the definitions of Section~\ref{sub:defs} and the second statement of Lemma~\ref{lem:comparison} apply to complexes
  of such modules" add: "(the lifts and homotopies in its proof exist for projective modules by their lifting property)".
- Replace "and in general the same argument applies to any resolution that begins with the chains of a Cayley graph" by:
  "in general, since $\Gam$ is of type $FP$, a finite resolution by finitely generated projective modules can be chosen to
  begin with the chains of a Cayley graph in degrees $0$ and $1$, and the same argument applies to it".

**R3 (proof of Theorem A, manifold paragraph).** Replace "It satisfies Poincaré duality with its orientation character and
all local coefficients \cite[Theorem~10.2 and Remark~10.3]{Sp}" by:

> It satisfies Poincaré duality with its orientation character and all local coefficients
> \cite[Theorem~10.2 and Remark~10.3]{Sp}: for the pair $(M,\emptyset)$ Spanier's duality map, defined from the Thom class,
> is cap product with the fundamental class, and on a manifold Čech-Alexander and singular cohomology agree

(or keep the sentence and add these identifications as a footnote).

**R4 (abstract).** Replace "In September 2026 OpenAI released a manuscript proving the conjecture in dimension four; it is
not refereed." by:

> A manuscript of OpenAI dated 25 September 2026, released on 6 October 2026, proves the conjecture in dimension four; it is
> not refereed.

**R5 (Table 1, "Uses directly").**
- Row 4.5: "(G2), (G3), 4.3, 4.4" → "(G2), (G3), 3.5, 4.3, 4.4, \cite{BoT}".
- Row 6.3: "6.1" → "6.1, \cite{BoT}" (optional).
- Row 6.5: "(G1), (G2), 6.1, 6.2, 6.4" → "(G1), (G2), (G5), 6.1, 6.2, 6.4".
- Row 7.4: "(G3), 3.6, 4.3, 4.4, 7.1--7.3" → "(G3), 3.6, 4.3, 4.4, 6.2, 7.1--7.3".
- Row 9.6: "9.1, 9.5" → "7.4, 9.1, 9.5".

**R6 (§3.3, outside results).** In the second bullet:
- replace "Theorem~6.1, that for a minimal convergence action of a finitely generated one-ended group on a continuum" by
  "Theorem~6.1, that for a minimal convergence action of a finitely generated one-ended group with no infinite torsion
  subgroup on a continuum";
- after "makes the dendritic quotient non-trivial;" insert "Lemma~6.2, that an element of infinite order of a convergence
  action on a compact space with at least three points is parabolic or loxodromic, and Proposition~6.4, that a point
  stabilizer containing a loxodromic element is virtually cyclic (both used from statement 4.4 on);".

Add "Lemma 6.2, Proposition 6.4" to the [BoT] entry of the bibliography.

In the first bullet, "acts on a single point" → "has a one-point dendrite" (Bowditch: "Then D is trivial (i.e. a point)").

**R7 (§3.4, optional).** "Sections 3, 7 and 8 are identical" → "Sections 3, 4, 5, 7 and 8 agree sentence for sentence".

**R8 (§1.3, Lott-Lück).** After "\cite[Theorem~0.1]{LL} and geometrization" add "(stated there for orientable manifolds; a
nonorientable closed aspherical three-manifold is handled by its orientation double cover, since $L^2$-Betti numbers
multiply by the degree of a finite cover)".

**R9 (§1.3 and [R]).** Nobody of ours has the comment's text: the record is a summary of the user's paste (courses hub
`USER_INPUTS.md` P1150; `LOGBOOK.md` l. 4645, 4658). Until someone with a browser session reads it, replace "was observed
in public by the commenter \texttt{Apprehensive\_Sand951} on \texttt{r/math} in October 2026 \cite{R}, as a remark
conditional on the manuscript and without proof." by:

> was remarked in public by the commenter \texttt{Apprehensive\_Sand951} in the \texttt{r/math} thread of 10 October 2026
> \cite{R}; the remark gave no proof.

In PROVENANCE.md, mark [R] as "not opened by a reader of ours; recorded from the user's paste[the user's words, omitted]What remains open" can be narrowed to: "the construction of an $\R$-tree from a minimal
convergence action on a dendrite (Levitt; Bowditch, *Group actions on trees and dendrons*), on which Bowditch's
Lemma~1.4 rests; its other input, Bestvina-Feighn's Theorem 9.5, has been opened, and for torsion-free groups satisfying
(G5) the rest of its proof is immediate."
