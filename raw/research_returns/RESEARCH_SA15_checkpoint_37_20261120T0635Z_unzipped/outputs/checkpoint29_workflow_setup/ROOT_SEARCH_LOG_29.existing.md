# Root work after the checkpoint28 paper freeze

Status: exploratory; no newly closed main gate is recorded by this log.

At23:44--23:46UTC on19November2026, searches used the exact queries:

- `alternating bilinear map left kernel rational map Pfaffian Cremona transformation`, restricted to arxiv.org;
- `Hasse Witt monodromy Cartier operator Artin Schreier moving kernel hypersurface`, restricted to arxiv.org and numdam.org;
- `"alternating" "kernel" "Pfaffian" "Cremona" bilinear`, a second-engine verification requested on arxiv.org.

The first pass returned no directly applicable result for the alternating-kernel question. The second returned an unrelated recent user-authored page and a secondary ResearchGate listing of *On Birational Maps and Jacobian Matrices*, including a snippet of Example2.5. That original has not been opened or read in this pass and is not used as authority. Hasse--Witt searches returned Koblitz's original1975 paper and other Cartier/Artin--Schreier items already known or not applicable; no new original proof was read from those search results. Search snippets are not promoted to theorem inputs.

The complete internal `nonordinary_ppav_uniform_Q_inertia.tex` proof and the complete moving-kernel lemma in `mixed_degree_one_uniform_full_groups.tex`, lines124--205 of the current canonical file, were reread. The degree-one radical is full of order128. The earlier single-class criterion can therefore be supplemented by an elementary full-radical generation criterion, but global generation and the higher-degree moving-kernel differential remain unproved. The new direct proofs and a compression countermodel are retained in `post_CP28_dual_alternating_kernel_route.tex`, pending independent audit. No mathematical program was executed for that note.
