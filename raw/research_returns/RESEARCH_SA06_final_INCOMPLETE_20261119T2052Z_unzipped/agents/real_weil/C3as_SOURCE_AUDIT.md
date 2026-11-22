# Primary-source and proof audit for C.3as

The final full proof is C3_top_all_dimensions.tex; the old draft is a comment-only supersession pointer. It is
new research, not reconstructed post-reset work. Its exact conclusion is
an integral additive exponent-p quotient in every positive characteristic
and every local dimension at least three. Rational and characteristic-zero
top quotients are not settled.

## Exact inputs actually opened

1. **Mukai, RIMS1736, December 2011, full 18-page author preprint.**
   https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1736.pdf.
   Own local copy: sources/mukai2011_raynaud.pdf. Example1.3 and Lemma1.4
   give the plane curve; Theorem1's proof and Proposition1.7, pp.4–6,
   give the exact differential's local primitives and smooth inseparable
   divisor. Definition2.1, Lemma2.2 and Proposition2.3, pp.7–8, give
   the normalized cyclic step. Section2.4, pp.11–12, gives the descending
   divisibility tower. These exact pages were freshly read for C.3as.
   The conflicting divisor/root signs are not silently imported:
   the proof derives the negative base term from the positive normal
   bundle and disjointness. The local root parameter, normal cocycle,
   all-dimensional Nakai proof and differential order are re-proved.
   Published 2013 metadata is verified; full publisher PDF is still
   NOT OBTAINED, and no assertion about its signs is made.

2. **Kerz, full 29-page author PDF dated 29 April 2008.**
   https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf.
   Local copy: ../cycles/sources/Kerz2009Milnor.pdf.
   Theorems7.1 and7.5, author pp.21–22, were freshly opened and read.
   Their scope is regular schemes containing a field, with sufficiently
   large residue fields; all residue fields here contain the infinite
   algebraically closed coefficient field. The theorem itself gives
   the integral Milnor Bloch formula on the actual regular resolution.
   No unproved higher Quillen tangent statement is used.

3. **Braunling, NYJM19 (2013), 545–564, full published primary PDF.**
   https://nyjm.albany.edu/j/2013/19-28p.pdf.
   Local copy: ../cycles/sources/Braunling2013.pdf.
   Sections3–4, pp.557–560, were freshly read. The cup-product
   diagram and divisor formula give intersection compatibility;
   the differential symbol map, residue squares and equation24 give
   the exact integral residue normalization. In the proof the local
   complete-intersection formula is derived from these operations.
   Its coefficient is one, with no factorial.

4. **Stacks Project, Section48.27, Tag0FVU.**
   https://stacks.math.columbia.edu/tag/0FVU.
   Freshly opened Lemma48.27.1 and Remarks48.27.2–3,6. Functoriality
   identifies the point Koszul trace with the dual of k→k, fixing
   the scalar normalization. This is the ordinary proper Serre trace
   on the projective exceptional variety.

5. **Gorchinskiy–Osipov, arXiv1505.03780v1, 14 May 2015.**
   https://arxiv.org/pdf/1505.03780.
   Full primary PDF opened, Definition2.7 and Example2.8, author
   pp.4–5, inspected while exploring a tangent Milnor-group route.
   Theorem2.9 requires 1/2 and weak5-fold stability. It is **not used**
   to cover characteristic two. The final construction uses the
   direct dlog/conormal projection on the regular resolution and
   needs no tangent-group isomorphism.

## Exact computation retained

Program code/check_top_all_dimensions.py checks the integer tower, root
classes, Bezout normalization, normal cocycle exponent, divisor
divisibility, positive top intersection formula and local residue signs.
The finite sample is five primes (2,3,5,7,11) and projective dimensions2–6,
plus exterior signs in dimensions2–12. Every check passed; measured
runtime0.001628408001124626seconds. Source, stdout and JSON are retained.
The universal geometric and cohomological proofs are separate from these
finite checks.

The initial complete draft compiled cleanly in four passes, with no
undefined citations or overfull boxes, in2.658338540000841seconds. The
draft wrapper's timestamped output and JSON are retained. Root subsequently completed a full independent proof/source audit and authorized final registration; its certification is recorded separately.

## Independent audit received

Cycles completed a full independent mathematical and primary-source
audit at2026-11-19T10:36:47.902442+00:00, with PASS and no requested
mathematical correction. Its detailed source/proof notes and canonical
events are ../cycles/C3as_all_characteristic_top_independent_REVIEW.md
and the corresponding CHECK_EVENTS.tsv. Frobenius additionally read
the complete draft and found no immediate proof error, but explicitly
did not claim a further full primary-source certification because its
parent assigned another priority.

The final renamed proof completed a fresh four-pass wrapper build at
10:41:52.924939 UTC, runtime3.1085856950012385seconds, with no undefined
citations or overfull boxes. This final verification is recorded in
C3as_final_CHECK_EVENTS.tsv and code/compile_C3as_final.out.
