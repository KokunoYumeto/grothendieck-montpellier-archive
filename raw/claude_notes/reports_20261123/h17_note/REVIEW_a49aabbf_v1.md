# H17, editor's comments before writing (v1)

Claude Fable 5.2 at effort max (agent a49aabbf5ed57bb8e), 23 Nov 2026. The mathematics is by GPT-6 Astra (ChatGPT Pro
mode). Written after the referee pass (`REFEREE_E42_E43_A6_a49aabbf.md`) and before the note.

## What we want to say

1. **A theorem the field will recognize.** Relation (IV) of Nakamura–Schneps (Invent. Math. 2000) holds for every
   element of GT̂. Nakamura–Schneps left the equalities G_Q ⊂ 𝕀Γ ⊂ GT̂ open; Lochak–Nakamura–Schneps (arXiv:2602.12462,
   February 2026, §1) still call it unclear whether the added condition cuts out a proper subgroup. Consequence:
   every element of GT̂ is the product of an element of Hatcher–Lochak–Schneps's group Λ and a Galois element.
2. **The application that is H17.** A character δ with values in F₂, defined on the group given by the two- and
   three-cycle relations alone, compares the two elliptic points of the modular curve at level 12. It vanishes on
   the normalized elements of GT̂. So every character of the hexagon group that extends δ and is trivial on Galois
   elements is trivial on GT̂.
3. The title has to carry (1). "Δ vanishes on GT̂" names an object nobody outside our files knows.

## Whom the draft material would not serve

- **The newcomer.** The runs' texts open with result numbers and frames. Nothing says what was open, or that the
  second theorem is a statement about two CM elliptic curves (y² = x³ − x and y² = x³ + 1) seen from the cusp.
- **The expert.** The proof exists in two versions spread over three runs, one resting on a claim far beyond the
  literature (the whole tower in every genus). The expert needs one chain, with the published theorems named:
  Hatcher–Lochak–Schneps (Theorems 2 and 4), Boggi–Zalesskii (Theorem A), Hoshi–Minamide–Mochizuki (Corollary C).
- **The people whose work it is.** (IV) is Nakamura's and Nakamura–Schneps's relation; Λ and the pants-complex
  action are Hatcher–Lochak–Schneps's; "(IV) implies (R)" is Schneps's (Math. Nachr. 2006, p. 670). The note must
  say that what is added is the step from Galois elements to all of GT̂, and nothing about (III′).

## Decisions

1. **One chain.** The route through Λ. The exit-system statements (all genera) are not used and not mentioned.
2. **Finite subgroups by citation.** The note cites Boggi–Zalesskii's Theorem A for the three finite-subgroup
   steps (C₂² in genus zero; C₃² and C₂ in genus one). The run's own Smith-theory proof of the same steps stays in
   the workbench. This is a change of route in the write-up, not of a statement; recorded in RECORDS.md.
3. **A definition of δ that needs no other file.** The run defines the shear by a formula in ρ₂ proved elsewhere. The
   note defines it by the unique unipotent intertwiner at level 12 (ten lines) and proves t ≡ −ρ₂ mod 3.
4. **The Galois part is stated as a hypothesis.** The tower argument does not cover Galois elements, which are not
   normalized. The note proves vanishing on normalized elements and states the corollary for characters trivial on
   G_Q. That the run's Δ is such a character, and that it is nonzero on the hexagon group, are cited as results of
   the longer text, not proved in the note.
5. **The twelve-point configuration** is used only to prove that the centralizer of the elliptic involution has
   its full profinite topology; the action stays at nine points. Recorded as an editorial simplification.

## Kind of note

**Needs a short pass, done here.** Hexagon has no post on GT̂ (search of 23 Nov: 0 works). On arXiv in 2026:
Lochak–Nakamura–Schneps 2602.12462 (read at the source on 18 Nov), Basualdo Bonatto–Robertson 2606.01466v2 (abstract
and §1 read: the Nakamura–Schneps subgroup acts on a completed modular operad of mapping class groupoids), Collas's
survey 2603.02848v2 (abstract read). None states (IV) on GT̂ or a result on δ. Ours does not overlap or supersede
theirs: it removes (IV) from the definition of the subgroup they act with.

## Before posting

- The user's word; the authors' line.
- A second reader for §§4 and 7 of the note (the two geometric chains), since the note's proofs are my rewriting.
- Hoshi–Minamide–Mochizuki opened at the source for Corollary C and its compatibility with forgetting.
- A decision on the Galois vanishing and the nonvanishing on the hexagon group: either a check of those two results
  of the longer text, or the note goes out with them marked as not proved here (as written).
