# A finite-format metric route, and its remaining obstruction

19 November 2026, 20:08–20:24 UTC. We write these working notes as
GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent
`/root/higher_comparison2`, with inherited effort configuration.
We do not promote an additional main-gate result from this route.

## Original source newly opened

Erik Walsberg, *On the Topology of Metric Spaces Definable in
o-minimal expansions of fields*, original arXiv:1510.07291v2,
<https://arxiv.org/pdf/1510.07291>.
We opened the full original PDF and read §3.2, p. 7; Theorem 7.1,
p. 16; the accompanying real-field explanation, p. 17; and
Corollary 7.24, p. 26. Tool retrieval records are
`turn164145656view0`, `turn846223869view0`,
`turn846223869view1` and `turn846223869view2`.

The main theorem says that a definable metric space either has an
infinite definable discrete subspace or is definably homeomorphic to
a definable subset of Euclidean space. The paper explicitly treats
uniform metrics on definable families of bounded functions, and its
corollary gives a uniform definable version of the affineness theorem.
This is the original theorem, not the repository abstract or a later
thesis quoting it.

## Application to one finite formula format

Let `K` be a fixed closed bounded definable set over an arbitrary
o-minimal expansion of a real closed field. Let a finite formula
format parameterize graphs of actual definable homeomorphisms of
`K`, possibly satisfying fixed marked-set or boundary conditions.
First retain only admissible coefficients. Quotient the coefficients
by equality of their whole graph, using a definable realization of
this quotient. Write `H` for the resulting definable set of actual
homeomorphisms in this one format.

The following is a definable metric on `H`:

`d(h,g)=max_x |h(x)-g(x)| + max_x |h^{-1}(x)-g^{-1}(x)|`.

The maxima exist by definable compactness of `K`. Each term is
definable from the graph formulas, and equality of maps has already
been removed by the quotient. The second term makes both evaluation
and inverse evaluation explicit; for compact `K` it gives the usual
homeomorphism topology over the reals.

Over the real field, this metric space is a subspace of the product
of two separable uniform function spaces on the compact metric set
`K`. Thus it is separable, so it cannot have an uncountable discrete
subspace. Every infinite real definable set is uncountable. Walsberg's
theorem therefore makes `H` affine.

There is also an all-real-closed-fields argument, using the graph
cell lemma already proved in A.116/A.133. Suppose a definable
`d`-discrete subset `D` of `H` were infinite. Choose a definable
coefficient representative for each element. Hardt-trivialize its
graph projection and pass to a positive-dimensional parameter cell.
The compact graph fibre and its projection bijection to `K` give
jointly continuous evaluation and inverse evaluation on that cell.
The parameter map from the cell to `H` is consequently continuous
for `d`: compactness of `K`, applied locally in the parameter cell,
makes the maxima tend to zero. A nonconstant continuous definable
injection of a definably connected positive-dimensional cell into a
discrete metric space is impossible. Indeed the inverse image of a
singleton and its complement are disjoint nonempty definable open
sets. Hence `D` must be finite, and Walsberg's theorem again makes
`H` affine.

In the graph argument, a parameter cell is locally closed. Around
any of its points we may therefore choose a closed bounded
neighbourhood inside that cell. The Hardt fibre is definably compact,
so the projection-preserving continuous bijection from its product
with this neighbourhood has continuous inverse. This is why the
joint-continuity claim does not assume that arbitrary coefficient
convergence already implies uniform graph convergence.

## What this supplies

After adjoining the identity to the format if necessary, ordinary
definable triangulation of the affine model gives local definable
contractions at the identity. More precisely, for a prescribed
positive `epsilon` there is a positive `delta` and a definable
contraction of a neighbourhood containing the `delta` ball to the
identity, staying inside the `epsilon` ball. The identity can be
kept fixed during the contraction.

These are contractions through actual homeomorphisms. They give
joint evaluation and joint inverse evaluation because the metric
controls both uniformly. Thus, within the chosen finite format,
they supply a true relative-identity operator on whole definable
parameter families. They do not merely contract coefficients in
a topology unrelated to the corresponding maps.

## The comparison gate remains

The positive radius and the output formula depend on the chosen
finite format. PL approximation of an arbitrary semialgebraic
homeomorphism generally increases its number of affine pieces as
the accuracy improves. Including such an approximation in a larger
format changes the contraction neighbourhood. We still have no
theorem ensuring that the approximation is close enough for the
new neighbourhood. The finite-format affineness result does not
remove this circular dependence.

Likewise, definable choice of extensions on coefficient cells does
not ensure continuity across their boundaries. Contractibility of
an individual fibre does not by itself make its projection a
fibration or supply a continuous local section. A controlled
extension theorem, with the relevant common finite format and
boundary conditions, remains necessary for that attempted sewing
argument.

Thus this route gives a rigorous metric justification for the
finite-format local-contraction step, in all real closed fields,
but it proves no new higher PL-to-semialgebraic concordance
comparison. It is not counted as qualifying movement.

## Additional bounded source checks in this interval

We reopened Mnëv, arXiv:0708.4039v3, §12, Proposition 52 and Lemma 11,
pp. 84–86, and §14, Lemma 12, pp. 90–93. The input is explicitly
jointly PL. The existing attached cube-root/Hudson counterexample
already rules out simply applying that small-slope assertion to
semialgebraic input. We did not count this rereading as a new method
obstruction.

We also opened Shiota, *Triangulations of non-proper semialgebraic
Thom maps*, original
<https://maths.anu.edu.au/files/CMAProc43_Shiota.pdf>,
Theorem 1.2, pp. 127–128, and its controlled-tube hypotheses on
pp. 129–130. The statement requires an actual Thom `C1` map or
the specified controlled tube systems. It therefore cannot bypass
the smooth-product-without-Thom-stratification example A5.015.
Original retrieval records: `turn577847092view1` and
`turn264897707search5`.

A bounded exact-title search for the unresolved Hartshorne (1968)
and Ogus (1973) originals again returned the Annals metadata,
later references and abstract pages, not their theorem text.
Records `turn808412771search0`–`turn808412771search9` do not close
either original-source comparison gate. No access-control bypass
or author contact was attempted.
