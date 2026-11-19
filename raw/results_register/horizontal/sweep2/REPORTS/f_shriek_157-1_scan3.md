# "f^! existe-t-il pour X → e ?" (Les Dérivateurs, cote 157-1, scan 3)

Claude Opus 5.5 at effort max (agent a34c04448e8299803), horizontal sweep 2 part 2, 18 Nov 2026. Item SA32-22. Image:
`grothendieck_archive_montpellier/21_derivateurs/157-1.pdf`, page 3.

## Where
| what | where |
|---|---|
| the question | cote 157-1, scan 3 (archive pencil number 2): a single landscape sheet between the contents sheet (scan 2, chapters I-XIX) and "Dérivateurs. 1. Préliminaires ..." (scan 4, ms. p. 1) |
| his notation for the adjoints | scan 4, ms. p. 1 (`K157-1-01_transcription.tex`, from L46) |
| notes | `K157-1-01_mathnotes.md` L9, L33, L43; `K157-1-01_notes.md` first row (scan 003) |
| research | no register statement answers it. Related: RESIDUE:I.8 (for spectra or D(k), the universally ambidextrous discrete fibrations are the finite discrete bifibrations); BISITE:D.8 (stable sheaf-cosheaf equivalence and the shriek operation); BISITE:F.11 |

## What the page says (decided on the image)
"f! existe-t-il pour X → e ? (pour les dérivateurs habituels.)": capital X, an arrow to e, "f" with a superscript "!".
Nothing else is on the sheet.

## What f^! means here (his scan 4)
- "Notations provisoires: f^? f_! f^* f_* f^!". This is the string of successive adjoints of the inverse image f^*.
- So **f^! is the right adjoint of f_***, and f^? is the left adjoint of f_!. In his presheaf convention A(I) =
  Hom(I°, A).
- For f: X → e, f_* is the homotopy limit over X°. The question asks whether the homotopy limit has a right adjoint.
- The same page states the non-derived facts:
  - (b) "même si A est abélienne ... les bi-adjoints n'existent pas toujours", and even for an open immersion f^! need
    not exist;
  - (c) for a closed immersion and a pointed A, f^! exists.
- The Codex note glosses the question as "existence of the exceptional inverse image for the map to e". By his
  notation, the right adjoint of f_* is meant, not the right adjoint of f_! (refinement, CORRECTIONS.tsv).

## He comes back to it on scan 19 (K157-1-02, transcription L48-L54, L109, L182)
- "Questions analogues pour les f^!, pour imm. fermées, (pour f^?, pour f imm. ouvertes)": he asks whether morphisms
  of derivators commute with these further adjoints.
- Margin: "Non ! Le cas des cat. triangulées est 'misleading', car, pour celles-ci, 'exactitude à g. et à dr.'
  reviennent au même." This is the stable-against-unstable distinction of the reconstruction below.
- "Je devrais demander à Thomason s'il a regardé, pour un morphisme ..."
- Later on the same pages: "On va appliquer cette philosophie aux foncteurs f^*, f_!, f_* (et éventuellement f^!, f^?)";
  a functor written f^!_D (L182).

## Status
- His question; open on the pages. No register statement settles it.
- My reconstruction, not checked by a run or a proof check (lead for sweep 3). Work in the underlying presentable
  ∞-categories: a right adjoint of holim exists iff holim preserves colimits.
  - **X with a final object:** f_* is evaluation at that object, so f^! exists in every derivator.
  - **Stable derivators (spectra, D(Ab)):** f^! exists when X is homotopy finite, since finite limits commute with
    colimits there. It fails for an infinite discrete X.
  - **HOT:** f^! fails already for X discrete with two objects, since the product does not preserve coproducts.
  - So "pour les dérivateurs habituels" the answer is: not in general; yes for a final object, and yes for homotopy
    finite X in the stable case.
- The register's ambidexterity statements (RESIDUE:I.8) bear on the stable case, where f_! ≅ f_* up to twist for
  finite discrete fibrations.

## Corrections and refinements
1. Refinement of the Codex gloss: "exceptional inverse image" here means the right adjoint of f_* (his notation, scan 4).
2. Reading decided on the image: capital X, "pour les dérivateurs habituels".
