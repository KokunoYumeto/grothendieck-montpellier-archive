# Rank-four sign bundles and the equivariant smoothing source

AI-produced by GPT-6 Astra, OpenAI, 20 November 2026.

This is a source-scope and attempted-route audit, not a new comparison theorem.
The target remains the ordinary PL-to-TOP component kernel for P(RP3).

## Original actually inspected

Lashof--Rothenberg, *G-smoothing theory*, PSPM 32, Part 1 (1978), 211--266.
The publicly retrieved file in this workspace contains only printed pages
211--221, not all 56 pages:
`/workspace/scratch/6b22741c5cd2/source_external/LashofRothenberg1978.pdf`.
The original URL is
<https://ncatlab.org/nlab/files/LashofRothenbergGSmoothingTheory.pdf>.
I read the OCR of all eleven pages and explicitly viewed the original scan of
printed page 212, at
`source_external/LashofRothenberg1978_excerpt/page_02.png` outside the authored root.
The independent root scope note is
`notes/root_Lashof_Rothenberg_scope_20261120.md`.

The introduction's item 7 on page 212 classifies equivariant smoothings by
equivariant tangent-vector-bundle reductions; it does not state that every
locally linear action possesses such a reduction. Its dimension exclusions
apply to every fixed-point manifold, including that of the trivial subgroup,
and separately to boundary fixed-point manifolds. Item 5 requires the Bierstone
condition and classifies sliced concordance; its conclusion is not ordinary
projection-preserving reduction of a specified bundle.

Theorem 8 of Section 1 on page 220 identifies the fixed parts of the universal
bundle-classifying space with classifying spaces of centralizers. Theorem 10
on pages 220--221 identifies the reduction fibre over a representation component
as the indicated union of centralizer quotients. It does not evaluate those
quotients in the rank-four sign case. These are bona fide bundle statements,
but their obstruction groups are precisely the groups that still need control.

## The total-space dimension trick and its limits

A loop of odd rank-four PL germs suggests a sign-representation microbundle
over S2. Its total-space dimension is six and its fixed-set dimension is two,
so merely checking dimensions in item 7 does not exclude the total space.
That observation is insufficient for either of the following reasons.

First, the theorem requires an equivariant tangent-vector-bundle reduction.
For a general PL germ loop, nonequivariant low connectivity of PL/O does not
produce an equivariant reduction. Restriction to the fixed zero section retains
the rank-four sign-normal data. In a kernel problem the assumed TOP nullhomotopy
does provide TOP triviality of that normal data, but it does not supply a
compatible reduction of the given PL data, nor an isotopy of its bundle
projection. Applying the TOP smoothing theorem can change the PL structure;
one cannot assume the resulting smoothing is compatible with the original
equivariant PL microbundle.

Second, the tangent representation along the fixed section is
(-1)^4 plus two trivial directions. Its centralizer is the stabilized object
with two fixed directions. The ordinary RP3 germ problem concerns the
unstabilized rank-four sign centralizer. Removing the two fixed directions is
not justified by smoothing the total six-manifold. Item 8 on page 213 explicitly
relates stabilization in fixed directions to pseudo-isotopy fibres. Item 9's
stability theorem on page 214 imposes fixed-manifold dimension at least five,
which does not cover the fixed S2 here.

Even if a compatible smoothing of the total space were separately obtained,
its existence alone would not establish a smooth or PL reduction preserving
the original projection. No such relative unstable bundle theorem occurs in
the inspected eleven-page excerpt. This is a limitation of this proposed
argument, not a proof that the desired reduction is impossible, and it does
not assert that the uninspected remainder of the original paper lacks one.

## Additional public-source inspection

The ordinary Lashof--Rothenberg paper *Microbundles and smoothing*, Topology 3
(1965), 357--388, was opened at
<https://www.maths.gla.ac.uk/~mpowell/Lashof-Rothenberg-smoothing-microbundles.pdf>
(web ref turn367511596view1). Its precise fibre-preserving PD-to-PL construction
in Theorem 2.1, pages 362--363, explains projection preservation when a PD family
is already present. It does not manufacture the missing equivariant PD family
from a TOP isotopy. Theorem 2.2 is the ordinary PL_n-to-PD_n comparison.

The author's public UCR directory indexes were also inspected by following
their displayed links, not by guessing private paths. They exposed several
other original papers but no identified copy of the Kwasik--Schultz K2 article.
No access-control workaround or author contact was used.

**Outcome:** the rank-six total-space observation does not presently narrow
the rank-four ordinary comparison kernel. No main-gate movement is claimed.
