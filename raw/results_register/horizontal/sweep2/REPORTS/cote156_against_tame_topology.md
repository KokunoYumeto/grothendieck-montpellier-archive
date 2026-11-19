# Cote 156 (1986) against the tame-topology axioms of cotes 120-121

By the broad agent a0c4bb37 (Claude Opus 5.5 at effort max), horizontal sweep 2, part 2, 18 Nov 2026.

**What this report rests on.**
- Cote 156-4 and 156-8: every line of the transcriptions that states an axiom, a definition or a data structure. The script listed them, 39 and 53 lines.
- Cote 120: the axiom table M1-M11 of the Pro notes MPL_152+120 (A120 rows, 120/003-023).
- Cote 121 and the rest of 156: the sweep items and their notes.
- 156-5, 156-6, 156-7 and 156-9 were not read beyond their item statements and axiom lines. No Work math notes exist for 156-4 to 156-9, only Codex's notes on the sheets. These parts still need a mathematical reading.
- Nothing here was read on a scan image.

## Where it is
| what | cote, dates on the sheets | notes and transcriptions | items (tags) |
|---|---|---|---|
| the tame-topology axioms M0-M11: graph calculus, finite unions, compact graphs, scalar functions | 120/003-023 | Pro `returns/MPL_152+120_unzipped/MPL_152+120_notes.md` (axiom table A120); Work notes K120 | SA10-19 = SA20-12 (H00K) |
| the later drafts: canonical adapted partitions, incidence orders, conservativity, effective epimorphisms | 121/001-073 | Pro `MPL_121_001-048`, `MPL_121_049-073+153+155` | SA11-3 = SA20-15 (H00M), SA11-4, SA20-13 |
| comparison with o-minimal structures (the notes' work, not his claim) | 120-121 | the same | SA10-4, SA11-4, SA20-10, SA10-5 (Shiota) |
| the "remords" (December 1981): his reconsideration of the realization | 120 | the same | SA10-3 = SA20-9 (H00L) |
| forms, segments, filtering, networks, cuttings, rives and mailles | 156-1, 156-2 (5-6 June 1986) | Pro `MPL_156-1+156-2` | SA21-1 to SA21-7 |
| networks via cuttings: tronçons | 156-3 (8 June 1986) | Codex J156-3-01 to -05 | SA21-12 |
| Analysis situs, first draft: contrées, figures, multistrata, subdivisions; axioms Cont 1-5 / Fig 1-4, then C1-C7 | 156-4 (10-13 June 1986) | Codex J156-4-01 to -11 (`codex_web_20261113/returns/J156-4-*/out/`) | SA21-13 |
| Sorite ensembliste: the two order relations | 156-5 (15-18 June) | J156-5-* | SA21-14 |
| Analysis situs, second draft: ateliers | 156-6 (18 June) | J156-6-* | SA21-10 |
| Analysis situs, third draft (Chap. VII) | 156-7 (23 June) | J156-7-*, H156-01 | SA21-10, SA21-15 |
| CF VIII: magasins généraux, oriented multistrata, polyhedral ateliers, axioms for lieux and constructible supports | 156-8 (27 June-4 July) | J156-8-* | SA21-15 |
| GF IX, with reused Récoltes et Semailles typescript leaves (terminus post quem May 1986) | 156-9 (to 15 July 1986) | J156-9-* | SA21-11, H01T |

## What the pages contain
- **Cote 120: an axiom system for tame sets inside ℝⁿ.** It is an extrinsic, coordinate-based system:
  - M1-M3: coordinate maps and their images and inverse images;
  - M4: products;
  - M5: finite unions;
  - M6: the separation function q;
  - M7: extension of scalar functions;
  - M8: exhaustion of ℝ by compacts;
  - M9: Hausdorff;
  - M10: compact neighbourhood bases;
  - M11: the field operations, with a moderate bound.

  The notes realize the axioms in the definable (o-minimal) model. Whether they are the o-minimal axioms is the notes' question, not settled on the pages (SA20-10).
- **Cote 121: the later drafts** (SA11-3, SA20-15). They introduce canonical adapted partitions, the incidence order of a partition, conservativity and effective epimorphisms.
- **Cote 156-4 (10-13 June 1986): an intrinsic axiom system, with no coordinates.**
  - The data form a contrée: multistrata M with a refinement relation ≪, and figures, which are closed sets of pairwise compatible multistrata.
  - First axioms, Cont 1-5 / Fig 1-4:
    - the elementary figure F_X = M_{≤X} is a figure;
    - figures are closed and pairwise compatible;
    - closed subsets of figures are figures;
    - compatibility of figures is tested on multistrata.
  - Second system, C1-C7 (13 June):
    - C1: each X has a smallest figure containing it;
    - C4: subdivisions of a sub-figure extend;
    - C5: compatibility;
    - C6: induced subdivisions exist and are unique;
    - C7: subdivisions glue (recollement).
  - Third reformulation: figures with two orders, ≤ and ⪯. Bounded families have suprema, and the irreducible figures are the multistrata.
  - He says he will first fix a geometric terminology rather than a good system of axioms ("au lieu de dégager un bon syst. d'axiomes, dégager une terminologie géométrique"), 156-4/33.
- **Cote 156-8 (CF VIII): the axioms are reorganized.**
  - Magasins (M, ≤, ≪, |∘|), with axioms Mag 1-Mag 4, reformulated as Mag 1′-4′.
  - Ateliers, with axioms At1-At5.
  - The lieux are the minimal multistrata, with axioms for lieux, ombres and multiombres.
  - "L'innovation d'avant-hier faisant tomber tout le fouillis des axiomes de compatibilité-disjonction" (156-8/31): the relation |∘| replaces the compatibility and disjunction axioms of 156-4.
  - A maquette, a T₀ ultrafinite topological space, is a local magasin (156-8/3).

## What depends on what (my reading of the two axiom lists)
1. **Two routes to the same goal.** Cote 120 axiomatizes tame spaces from outside, as systems of compact sets in ℝⁿ. Cote 156 axiomatizes the combinatorial structure that a tame space carries: strata (multistrata), closed unions of strata (figures), refinements and subdivisions. The tame spaces become its realizations, the "réalisations topologiques" of 156-2.
2. **The bridge is cote 121.** Its adapted partitions with their incidence orders give exactly the data of a contrée or magasin:
   - strata ordered by incidence give (M, ≤);
   - refinements of partitions give ≪;
   - closed unions of strata give figures.

   This is my inference: neither cote states the correspondence.
3. **Subdivisions.** C4, C6 and C7 (extension, induced and glued subdivisions) are the combinatorial form of what M5 (unions) and the triangulation and stratification statements of 120-121 provide in ℝⁿ.
4. **Maquettes and question P01.** The maquettes of 156-8 (finite T₀ spaces) are finite posets. So the 156 structures meet the notes' question P01 (SA21-8): a form as a tame space recovered from a pro-object of finite posets or T₀ spaces.
5. **The realization question.** The remords of December 1981 (SA10-3, H00L) bears on the realization functor that would connect the two systems. Its date is a source question.

## Agreements, conflicts, corrections
- **The 156 axioms change between drafts within weeks.** Cont/Fig, then C1-C7, then the two orders, then Mag and At. Any later use must say which draft. Within 156-4 the numbering is unstable: struck "Cont 2|Cont 3|Cont 4" are renumbered as Fig 1-4.
- **None of the 156 axiom systems is shown consistent or realized on the pages.** The items record self-flagged steps ("il faut un axiome pour l'assurer", 156-4/42; "il y a quelque chose à prouver", 156-4/51) and an extra stability axiom for infinite gluings (156-8/20).
- **The o-minimal comparison** (SA10-4, SA11-4, SA20-10) concerns cote 120 only. It does not reach 156, whose axioms are not about subsets of ℝⁿ.
- **No research-run statement sits on cote 156.** The register has none on these pages (`GLOBAL/INTERLINKS/ITEM_REGISTER.tsv`). The links of the tame-topology items into the register go through the FINMON and STRATA runs on finite models, not through these pages.

## For part 3
- **A mathematical reading** of 156-4 to 156-9 in full. Codex left notes on the sheets only.
- **Write the correspondence** from 121's adapted partitions to 156's magasins (point 2 above), and decide whether the magasin axioms Mag 1-4 hold for the incidence data of a tame (o-minimal) stratification.
- **Date the remords** and read what it changes in the realization.
