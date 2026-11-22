# Published Galvin source: boundary and suspension audit

We opened D. A. P. Galvin, *The Casson–Sullivan invariant for homeomorphisms
of 4-manifolds*, Compositio Mathematica 162 (2026), 2496–2544,
DOI 10.1017/S0010437X26103510. We read the full published statement of
Theorem 1.7, Definition 2.11, Propositions 2.22–2.23, and the relative
construction in Section 4.2, Lemmas 4.8–4.9, Proposition 4.10,
Definition 4.11, Lemma 4.12, the proof of Theorem 1.7, and Section 4.4.
The published PDF has SHA256
59e17509184683ef206e3250f40678144dd0db5759dfae10bd09322a48f8843b.
It remains outside the authored archive in source_external/galvin_cs_2026.

At the continuation audit on 19 November 2026, we explicitly viewed the
published images of printed pages 2526 and 2527, including the full
boundary-label diagram in Proposition 4.10. The earlier image named
printed2527.png is actually printed page 2526 (physical PDF page 32).
The correctly named published_p2527.png is physical PDF page 33.
We use the printed page numbers, not the first image's filename.

Three source details require an explicit derivation in the proposed
application, rather than an unqualified quotation of Theorem 1.7.

1. Theorem 1.7 and Proposition 4.13 say compact manifolds, while
   Definition 4.11 and the introduction to Section 4.4 say closed.
   The actual normal-invariant and surgery construction in Section 4.2
   is relative to the full boundary. The application must run that
   construction for the compact manifold with boundary and retain the
   relative groups throughout.
2. Lemma 4.9 prints the Steenrod instability inequality in the wrong
   direction. The needed assertion is Sq^i on degree j vanishes for
   i greater than j. Here Sq^2 acts on a degree-one class before
   suspension, so it vanishes. This verifies the stated reduction map
   after correcting the inequality. In the relative case the suspension
   is that of the pair (X, boundary X).
3. The boundary conclusion must be identity, not merely a diffeomorphism.
   Proposition 4.10 chooses the side as D times I and the relative
   s-cobordism identification fixes that side and the lower end. We
   checked the diagram on page 2527. To conclude identity on boundary X,
   the product labeling of D times I must be chosen from the original
   boundary label. The two corner labels then agree. This compatibility
   must be stated and proved in the candidate.

The source also occasionally omits the boundary from groups in the prose
proof of Theorem 1.7. Its displayed Bockstein sequence and its next step
use the full relative groups. For an oriented compact connected
four-manifold, the top relative integral cohomology of its product with
I is Z, so multiplication by two there is injective and the preceding
coefficient-reduction map is onto.

For the intended base B = RP^3, the four-manifold is X = B times I.
It is compact, connected, orientable and smooth, with finite cyclic
fundamental group. The relative obstruction lies in H^3(X, boundary X;
Z/2), which is H^2(B; Z/2). We have independently verified a complete
finite PL model of B; its certificate establishes the base hypotheses
only, not existence or invariance of a topological concordance.

The remaining candidate audit must identify the source's obstruction with
the relative universal PL obstruction and prove that it cannot be removed
by a free-top ordinary concordance isotopy. The latter requires an
ordinary endpoint path comparison in dimension three. We do not infer
that a vanishing obstruction suffices for a PL representative.
