# Version-specific source-scope rejection during the higher-restriction search

Status: a precise objection to the literal open-complement Lemma3.2 in the opened author version and in the subsequently retrieved indexed published text. This is **not a refutation of the paper's main torsion theorem**, and no numbered proof in this package uses this lemma or the torsion paper. Dependency scan completed2026-11-19 13:18:23UTC. The existing Patel--Ravindra references concern two different infinitesimal papers and are explicitly comparative searches, not inputs to the counterexamples.

## Source actually read

Deepam Patel and G.V. Ravindra, *Lefschetz theorems for torsion algebraic cycles in codimension2*,18-page author PDF:
https://www.math.purdue.edu/~patel471/torsionWL.pdf

Read the introduction's Theorem1.3/Remark1, Theorem2.5, Corollary2.7/Remark4, the entire Theorem3.1/Lemma3.2 argument on authorp7, and Corollaries3.3--3.4 on authorp8. The paper's main claim concerns torsion in codimension2 of smooth projective varieties. Its positive-characteristic remark concerns prime-to-p torsion. It does not state the required general rational theorem for strictly local punctures.

The separate one-page author erratum was also opened and read completely:
https://www.math.purdue.edu/~patel471/torsion_erratum.pdf
It corrects the use of the algebraic intermediate Jacobian in Proposition5.1 and places an additional hypothesis on Theorem1.7 and Proposition5.2; it says that its correction affects Section5. It does not address the open-complement lemma examined below. No inference about whether a further correction exists is made.

Published metadata: *Advances in Mathematics*316(2017),554--575, DOI10.1016/j.aim.2017.05.018. Direct opening of the published PDF at https://www.math.umsl.edu/~girivaru/torsion.pdf timed out, and the publisher full-page opening returned403. Therefore the objection below is assigned to the actual18-page author file and its authorp7 locator, not silently to an uninspected published page.

**Publication comparison after the checkpoint freeze:** searching within the indexed UMSL primary PDF subsequently returned its complete text of printedpp561--563. Those pages were read in full. Published Lemma3.2 is on printedp562 and has the same proper-intersection conclusion and the same mixed-support sequence. The preceding published Corollary2.7/Remark4 and following Corollaries3.3--3.4 were also read in that primary text. A separate attempt to download the full published binary returned503, and a screenshot attempt timed out. Thus the publication comparison is an actual primary text inspection, not a claimed fresh published-binary download or visual inspection. The initial access failures above remain part of the record.

## Literal counterexample to the open-complement lemma

Work over C. Let Y=P4 with homogeneous coordinates(x0:x1:x2:x3:x4), let X be the hyperplane x0=0, let Z be the plane x0=x2=0, and let V be the quadric x0x1−x2x3=0. Then X is a smooth ample divisor of Y. The quadric V is irreducible: the rank-four quadratic polynomial cannot factor as two linear forms (such a product has quadratic-form rank at most two). Its only singular point is v=(0:0:0:0:1), by the four partial derivatives x1,x0,−x3,−x2; this point lies on Z. Thus V is smooth away from Z and contains Z, as permitted by the preceding Bertini setup. It intersects X properly, with X∩V the union of the distinct hyperplanes x2=0 and x3=0 in X. That intersection is also smooth away from Z. The plane ideal is generated in degree one and V belongs to its degree-two linear system.

The target complement has the explicit chart

    X−V ≅ A2 × G_m,

obtained by setting x2=1 and using x1,x4 as affine coordinates and x3 as the nonzero coordinate. Hence H1(X−V,Q)=Q.

Projection away from v makes Y−{v} the total space of a line bundle over P3, and restricts Y−V to that line bundle over P3−Q, where Q={x0x1−x2x3=0}⊂P3 is a smooth quadric. The fibres are contractible complex affine lines, so H1(Y−V,Q)=H1(P3−Q,Q). The Gysin sequence for the smooth divisor Q gives

    0 → H1(P3−Q,Q) → H0(Q,Q)(−1) → H2(P3,Q),

where the last map is multiplication by deg(Q)=2. It is injective, so H1(Y−V,Q)=0. The restriction map is therefore 0→Q and is not an isomorphism, even though 1<dim(X)=3. This contradicts the literal conclusion of Lemma3.2 under its stated proper-intersection hypotheses. The same calculation can be expressed in prime-to-characteristic étale cohomology, but the complex example already suffices for the author-version statement.

## The precise failed proof step and scope boundary

The displayed sequence in the author proof uses compactly supported cohomology of (Y−X)−V followed by ordinary cohomology of Y−V and X−V. The ambient Y−V is not proper. The standard open/closed localization sequence with compact supports places compact supports on all three terms; it does not give the mixed sequence displayed there. Artin vanishing for the first compact-support group therefore does not establish that asserted ordinary-cohomology isomorphism.

This is a source-rejection diagnostic only. It does not imply that every subsequent theorem is false, and it supplies no counterexample to their Chow-torsion theorem. A corrected proof may use further hypotheses or another argument; none is assumed here. In particular this source is not used to bridge the rational, actual-family, or singular-support lifting gaps of the current local problem.

The generality clause does not remove this example. Quadrics containing the fixed plane Z have rank at most four, since their quadratic form vanishes on the three-dimensional vector subspace of that plane. The rank-four locus is nonempty and open, and its singular point lies on Z. On X every such general equation is x2 times a second independent linear form. The displayed quadric is a representative of this open geometry, and the same H1 discrepancy holds throughout it. The minimum degree generating the plane ideal is one, and degree two is exactly the preceding corollary's minimum-plus-one choice.

## Finite verification and independent check

Retained program: `code/check_torsion_open_lemma.py`; complete stdout: the matching `.out`; structured output: `output/torsion_open_lemma_check.json`. The run began2026-11-19T13:22:00.042647UTC and took11.189450071seconds including concurrent primary downloads. Its exact symbolic algebra portion took0.085755596seconds and passed all11 checks: base-plane incidence, singular ideal and vertex, rank four, irreducibility, two distinct plane factors, the target chart, smoothness of the base quadric, generic rank bound/nonempty rank-four locus, and injectivity of the one-dimensional degree-two Gysin matrix. The program does not numerically compute topology or claim to test a Chow-torsion theorem. The cohomological identification is the proof above.

The author PDF and erratum were successfully saved under `sources/`, with SHA256 hashes in that JSON. The published binary download failure is retained there; its indexed primary text was separately read as described above. Frobenius independently checked the entire counterexample, including generality, the two complement cohomology groups and the precise mixed-support error, and independently read the author lemma plus indexed publishedp562. That review expressly made no conclusion about the paper's main theorem. No new numbered result or main-task movement is claimed from this source rejection.

Root then independently reconstructed the complete P4 counterexample and reported a pass, freshly reading the author Corollary2.7/Remark4, Theorem3.1/Lemma3.2 and the complete Section5 erratum. Its receipt was recorded at13:26:29UTC. Root's direct published opening timed out; no published-text inspection is attributed to that separate audit. The exact independent-reproof scope is the explicit source-lemma counterexample, not a re-proof or refutation of a main theorem of the torsion paper.
