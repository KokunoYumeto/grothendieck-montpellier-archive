# Generic surfaces and finite punctures: source and proof audit

## Checked result, 20 November 2026, 10:49 UTC

The complete source is `D_generic_surface_finite_punctures.tex`, with labels
`D:generic-surface-finite-punctures` and
`D:normal-finite-puncture-quantitative-transfer`.
Root, B, C, and D have passed the complete actual proof. B and C independently
checked the exact arbitrary-characteristic Bertini input. Both headings were
promoted at 10:49:06 UTC, after adding the explicit equation `q=p^f` in the
bounded-scalar item. No finite certificate is appropriate for this general
geometric proof.

The target is the fundamental group of the original scheme over `k`. We do not
assert surjectivity onto the fundamental group after the transcendental base
extension. A single fixed tower of geometric generic hyperplanes works for all
original finite covers; there is no countable-choice or intersection-of-opens
argument. We use the closure of the final smooth open surface, not a claim
that the entire hyperplane section of a singular Chow model is normal.

## Exact primary sources opened and read in full

1. Stacks, Tag `0200`, Lemma 30.18.1 and complete proof. A separated finite-type
   scheme over a noetherian base admits a proper quasi-projective modification
   which is an isomorphism over a dense open. For proper integral `S`, the reduced
   closure of that open gives the integral projective Chow model required here.
   URL: https://stacks.math.columbia.edu/tag/0200
2. Stacks, section `0G4C`, Lemmas 37.32.1, 37.32.2, and 37.32.3 with complete
   proofs, especially exact conditions (3) and (4) of Lemma 37.32.3 (`0G4F`).
   The individual `0G4F` endpoint timed out, while the full lemma and proof were
   successfully opened in the section. At a closed point of a finite etale
   cover of a smooth immersed scheme, two transverse pulled-back hyperplanes
   give the required codimension-two component; a third section nonzero at
   that point avoids the component. The linear system is basepoint-free.
   URL: https://stacks.math.columbia.edu/tag/0G4C
3. Stacks, Tag `0FD6`, Lemma 33.47.3 and complete proof. A general hyperplane
   section of a smooth immersed scheme is smooth. The finite etale pullback
   is then smooth too, so geometric irreducibility from the preceding source
   becomes geometric integrality.
   URL: https://stacks.math.columbia.edu/tag/0FD6
4. Stacks, section `035E`, normalization Lemmas 29.55.8--11 and their proofs.
   Normalization is finite for our finite-type field schemes and unchanged on
   the smooth open surface. Composing this finite normalization with the closed
   image embedding makes the inverse image of the finite omitted set finite.
   URL: https://stacks.math.columbia.edu/tag/035E
5. Landesman, *A Lefschetz theorem for intersections with projective varieties*,
   arXiv:2005.10708v1, 21 May 2020. We read Remark 1.5 (printed p.2), Proposition
   2.1, Lemma 2.2, Corollary 2.3, and their complete proofs (pp.4--6). Remark 1.5
   explicitly distinguishes generic parameters from a single closed parameter
   in positive characteristic. Corollary 2.3 directly concerns curve sections;
   our final proof instead uses the exact Stacks hyperplane statement
   successively, avoiding a dimension substitution in that corollary.
   URL: https://arxiv.org/pdf/2005.10708

## Independent-audit scope

- B freshly read all Stacks passages above, including Chow and normalization;
  B did not reopen Landesman because the direct proof is complete without it.
- C freshly read the full Bertini passages and the full Landesman proposition,
  lemma, and corollary; C reused earlier checked Chow/normalization inputs.
- Root passed the actual proof and freshly read the full Bertini passages;
  its fresh full Chow0200, normalization29.55.6--11, and Landesman Remark1.5/Proposition2.1/Lemma2.2/Corollary2.3 source rereads subsequently passed.
- The inherited surface H1 and representation results are previously proved
  inputs. Inflation in degree one and injectivity on conjugacy classes under
  surjective precomposition give the transfer directly. Degree-two inflation
  may have a kernel, so there is deliberately no H2 conclusion.

## Boundary of the reduction

The omitted set must be finite. For a positive-dimensional codimension-two
set, the image surface can contain a boundary curve; the checked blowup-of-a-
line example `D:Chow-surface-boundary-obstruction` shows this for every ample
surface divisor on that Chow modification. We have not repaired this in
general. Full finite generation for punctured normal proper surfaces, hence
full finite generation in the present reduction, remains open beyond the
separately established geometric classes.

## Root final fresh source confirmation

Root subsequently completed full fresh reads of Chow0200, normalization29.55.6--11, and Landesman Remark1.5 plus complete Proposition2.1/Lemma2.2/Corollary2.3 proofs. The full normal theorem source audit therefore has no pending source item.
