# Work isolated during the CP12 freeze

Current integrated TeX, bibliography and CHECK_EVENTS were left unchanged after the root freeze.

## Actual visual QA

Separately opened montages 9, 10, 11 and 12 and visually inspected pages 256--269 and305, fifteen pages total. PASS. The repaired two-category display on p266 fits; equation96 onp267 and E.3.1 onp269 have clear tags; bibliography p305 is clean. No clipping, overlap, missing glyphs or escaped formulas observed. Root received the verdict.

## Ordinary arbitrary-embedding extension

New A3_ordinary_arbitrary_embedding.tex gives generic ordinarity in |M^n| for every n>=3 on every ordinary characteristic-two abelian surface, hence r=chi(M)n^2-1 for any given projective embedding once ambient restriction is surjective. Status Candidate pending root audit. Monodromy full mathematical proof PASS; it did not claim new source reopening or a code rerun. Prior primary-source lemmas were read before use. The new code/ordinary_arbitrary_embedding_checks.py checked254 n-values and32512 norm/degree identities in0.012083560999599285seconds, full output retained. Root and reduction-descent have the complete draft for audit.

## Higher-even supersingular rectangular probes

New ss_higher_even_rectangular_probe.py retains every bounded trial and full witness matrix for m=6,12,24,48,96 with n=3. Witness stable ranks are16,34,70,142,286, respectively. Runtime0.6945195179941948seconds. No all-valuation theorem is inferred. The first three natural sparse continuations of the original 6x3 witness were then tested at q=m/2=3,6,12,24,48; their rank sequences are fully retained in ss_sparse_even_family_probe.output.json. They pass atq3 but lose stable rank later, so this route is unsuccessful as written. Runtime0.1254310340009397seconds. A uniform construction or geometric induction is still needed.


## Bounded literature search

Searches for generic p-rank in linear systems on abelian surfaces returned no directly applicable theorem for the higher-even supersingular rectangular problem. Queries included “p-rank general curve ample divisor supersingular abelian surface generic Cartier operator”, “generic p rank curves abelian surfaces linear system Raynaud Cartier”, exact “p-rank” “linear system” “abelian surface”, and “ordinary” “hyperplane sections” “abelian varieties”. The known conditional Illusie theorem reappeared via the Lefschetz torsion cycles paper; its hypothesis requires ordinary linear complete intersections and was not treated as a theorem for an arbitrary fixed ambient surface. No new source from this search has been used to prove a claim.
