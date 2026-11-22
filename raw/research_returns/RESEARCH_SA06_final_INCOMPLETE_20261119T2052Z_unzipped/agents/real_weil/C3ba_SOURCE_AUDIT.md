# C.3ba: integral ordinary quotients in all higher codimensions

Status: finalized after complete independent root and cycles proof/source
reviews. Root certified at2026-11-19T11:52:50.332166UTC; cycles completed
at11:49:14UTC. Final proof: C3_positive_characteristic_all_quotients.tex.
The former draft is a comment-only supersession pointer. The requested
wording repair is included: only the finite-type bundle map is asserted
to have pure relative dimension; the strict-local factor is asserted
flat and the cycle codimension is checked by regular immersions.
The statement and original check history are registered.

## Exact conclusion and limitation

For every algebraically closed field k of characteristic p>0 and every
2<=r<=N-1, an explicit excellent normal strict-local N-dimensional
cone with regular puncture X has an actual ordinary quotient
B^r(X) surjecting onto (k,+). This refutes integral finiteness even
over Fpbar. The exhibited additive quotient has exponent p. It gives
no nonzero rational quotient, no characteristic-zero conclusion, and
no kernel or cokernel on the ordinary algebraically trivial subgroup.

The base data are exactly the proved C.3as projective r-fold, ample
line bundle L, cotangent section eta, and individually selected actual
closed curves. The new data are P^m times V, m=N-r-1, with O(1)
external-tensored with L, followed by its full section ring and the
pointed strict henselization at the vertex. Degree-one generation is
not assumed. The contraction and regularity statements use precisely
the full-section-ring proof already certified in C.3as.

## Actual morphism and cycle calculation

The section z0 induces a bundle map of resolutions and the graded
ring map a_n -> z0^n a_n. Its pointed map of strict henselizations is
specified by the universal property. It need not induce a morphism
of punctures: the z0=0 chart can map to the original exceptional
divisor. Every pullback is therefore taken on resolutions first.

Flatness is proved over every coefficient ring B by the explicit free
B[t]-basis 1,u^a,(t')^b of B[u,t'], where t maps to u t'. A graph
argument handles an etale target factor, and the finite-relations
criterion handles its filtered ind-etale limit. No torsion-free-over-B
criterion is substituted for flatness. The selected curves are regular
and regularly embedded with codimension r; their flat inverse images
remain regular immersions of that codimension. Thus no arbitrary
ind-etale fibre-dimension assertion is needed to define their cycles.

The integral Milnor Bloch formula and dlog give the conormal detector.
The direct differential summand from V, coherent Kunneth, the fixed
Serre pairing with eta, and coefficient extraction at z0 define its
scalar value. The full exceptional image is killed using the literal
zero-section Chow identity and flat strict-local base change. Ordinary
actual curve-family differences are p-divisible, hence killed by this
exponent-p target. The supported local regular sequence pulls back to
(s_1,...,s_(r-1),z-b(z0/zj)t'_j). Its integral residue has exactly the
global coefficient b z0; evaluation at z0 gives b. This proves
surjectivity on actual cycles, with no formal-family algebraization.

## Freshly opened primary sources

- Stacks Lemma33.29.1, Tag0BED, full statement and its product-Cech
  proof were opened and read:
  https://stacks.math.columbia.edu/tag/0BED . The proper separated
  product hypotheses hold for P^m and V. The O(1) higher-cohomology
  vanishing gives the displayed single-factor Kunneth identification.
- Stacks Section61.7, Tag097H, full definitions and the displayed
  ind-etale stability lemmas were opened:
  https://stacks.math.columbia.edu/tag/097H . The actual flatness
  assertion is independently proved in this draft, rather than
  attributed to an unstated theorem in that section.
- Kerz, The Gersten conjecture for Milnor K-theory, complete29-page
  author PDF dated29April2008, freshly reopened:
  https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf .
  Theorem7.1 on authorp21 and Theorem7.5 on authorp22 were read
  explicitly. The regular noetherian schemes contain k, and all
  residue fields are infinite, so the integral hypotheses apply.
- Braunling, Bad intersections and constructive aspects of the
  Bloch--Quillen formula, published NYJM19(2013),545-564, complete PDF freshly
  reopened: https://nyjm.albany.edu/j/2013/19-28p.pdf . Sections3-4,
  especially the cup-product diagram(22) on pp557-558 and residue
  squares/equation(24) on pp559-560, supply the exact product and
  residue compatibilities used in the supported dlog computation.
- The Serre trace normalization, Stacks Section48.27/Tag0FVU,
  is the previously independently certified C.3as input. Its role
  is unchanged; no new fresh opening is claimed in this audit.

New bibliography key D_StacksSegreCohomology is retained in
C3ba_references.bib. The exact Kerz/Braunling keys are reused from
the already registered cycles/absolute_picard_references.bib.

## Exact finite certificate and standalone build

code/check_segre_integral_quotients.py and its full stdout/JSON retain
961 monomial normal-form checks,132 dimension/residue-orientation
checks, and24 graded-map/differential checks. All pass. Runtime:
0.0410557839932153seconds. The program checks finite symbolic algebra;
the geometric flatness, strict-local maps, actual cycles, boundary
annihilation and divisibility are proved in the text.

The revised draft passed the full LuaLaTeX/BibTeX/final-two-pass wrapper
at2026-11-19T11:44:21.601775UTC in2.735625212000741seconds, with zero
diagnostics. A preceding missing display terminator and overlong
display were repaired; their original failure logs are preserved.
The additional flatness wording revision passed a fresh four-stage
wrapper at2026-11-19T11:47:22.911809UTC in2.596334490997833seconds,
with zero diagnostics. Complete timestamped logs and JSON are retained.

The root's first complete proof read and fresh Kunneth source check
passed the core argument. Final registration followed the revised-text receipt. Checkpoint12 has now been saved and its
mutation freeze released. Cycles has independently read the entire
revised proof and C.3as, freshly read Stacks0BED and Kerz7.1/7.5, and
reported a complete pass; its detailed review and original event are
being saved separately. This note does not claim a reviewer reran
the finite program.


## Independent final receipts

Root read the entire revised proof, fresh Kunneth source, complete exact
certificate program and aggregate/representative output. The final
receipt is at11:52:50.332166UTC, with the root review retained at
research/notes/ROOT_C3ba_SEGRE_AUDIT.md and original root events.
Cycles independently read the full proof and antecedent C.3as, freshly
read Stacks0BED and Kerz7.1/7.5, and completed its pass at11:49:14UTC.
Its full review and canonical event are at agents/cycles/
C3ba_positive_characteristic_all_quotients_independent_REVIEW.md and
the matching CHECK_EVENTS.tsv. Neither reviewer claims an independent
finite-program rerun. The final renamed wrapper is recorded separately.

Final renamed proof passed all four wrapper stages at 2026-11-19T11:53:37.570587+00:00, runtime2.992506432005seconds, zero diagnostics. Canonical final event retained separately.
