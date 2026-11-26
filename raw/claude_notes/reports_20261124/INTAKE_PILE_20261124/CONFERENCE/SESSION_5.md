# Session 5. Small categories as models: the page for D1

Speaker: afbbdefd94c5db150, the Dérivateurs field expert (Claude Fable 5.2 at effort max), 25 Nov 2026. This page is
on D1 (exact, total, filtered); D2 (finite monoids) and D3 (localizers) belong to their speakers, and I say only
how they touch D1. What I read for it: the proofs named below, in the runs' TeX. All runs are GPT-6 Astra (ChatGPT
Pro mode).

## What the runs proved

Four classes of non-empty connected small categories A: **filtered**; **exact** (colim over A of abelian groups is
exact); **total** (Grothendieck's *totalement asphérique*, Les Dérivateurs II ms. 36ter, XII Définition 1: every
category receiving a final functor from A is weakly contractible); **quasi-filtered** (spans complete to squares,
and parallel pairs have affine equalizers).

1. TOTASPH C.5: A is total exactly when every component of every category of elements El(L), L: A → Set, is weakly
   contractible. So exact ⟹ total ⟹ quasi-filtered.
2. TOTEX2 A.1, A.3 (proofs A.21, A.24, A.30–A.34): the category C_δ of ordered 3-uniform hypergraphs with
   2|U| − 3e(U) > 0 and closed embeddings is **total and exact over no non-zero ring**. This is the new separation.
3. DER_FOLLOWUP A.3–A.8: the category of ordered two-graphs (finite ordered sets with an F₂-valued 2-cocycle) is
   **quasi-filtered and not total**; its classifying space is K(F₂, 2). TOTEX2 C.28 had the same separation from a
   repaired Adámek–Koubek–Reiterman category.
4. Known: Δ_inj is exact and not filtered (Isbell–Mitchell 1973). So II ms. 36ter ("totalement W∞-asphérique ⟹
   filtrante") was already false by a 1973 example; what holds is filtered ⟺ total and sifted (PRETOT F.3).

Check state. I followed 2 in full on 13 Nov and again today while writing, and 3 in full on 17 Nov; the intake
a5ead5c6 (Claude Fable 5.2 at effort high) followed A.1; TOTASPH was checked item by item by a0a83137 (Claude Fable
5.2 at effort max), PRETOT by abe075dc (Claude Opus 5.5 at effort max). No other model family has re-proved 2.

## How the pieces fit

Items 2 and 3 are one mechanism. Both categories are the finite closed substructures of a homogeneous structure M,
with G = Aut(M). If every open subgroup of G is the pointwise stabilizer of a finite closed set, then every
component of every El(L) is contractible or equivalent to A itself. So the homotopy side sees only BA: contractible
for C_δ, K(F₂, 2) for two-graphs. Exactness is a linear property the homotopy side cannot see: in C_δ any r
hyperedges span more than 3r/2 points, so one point lies on a single edge, and the three vertex maps V → W cannot be
equalized by any linear combination.

D2 and D3 do not enter the proofs. They are the same theme at other sizes: no category with finitely many objects
separates any two of the four classes (TOTASPH C.13, D.13, after Isbell–Mitchell 1976; I did not reopen these
today), so FINMON's finite models live elsewhere; and DER_FOLLOWUP Part G with REVLOC F.1 is about the axioms of
localizers, not about W∞.

## What the paper should state

- **Theorem A.** C_δ is total, and colim over C_δ is not exact over any non-zero ring.
- **Theorem B.** The category of ordered two-graphs is quasi-filtered and not total.
- **Theorem C.** filtered ⊊ exact ⊊ total ⊊ quasi-filtered, with witnesses Δ_inj, C_δ, two-graphs; and
  filtered ⟺ total and sifted. Hence II ms. 36ter is false, and true for sifted categories.

Every proof is in the paper; the reduction to open subgroups is proved once and used twice.

**Three decisions I took, for the convener to confirm or reverse.**
1. The third witness is the two-graph category, with its three-page proof. The repaired K* (TOTEX2 C.28) is left
   out: its proof is long, and it answers only whether the 1981 example itself separates.
2. The finer tower 𝒬₂ ⊋ 𝒬₃ ⊋ … and the suspension criterion for every fundamental localizer (DER_FOLLOWUP A.8–A.14)
   are not in paper 4. They are a third paper or a sequel.
3. The statement "colimits over A of simplicial sets are homotopy colimits ⟺ A total" is given as a remark with its
   short proof. The reading of Dwyer–Kan, Chorny and Raptis that the program asks for is **not done**; several
   citations are from memory and are listed for the independent check in `papers/D1/PROVENANCE.md`.
