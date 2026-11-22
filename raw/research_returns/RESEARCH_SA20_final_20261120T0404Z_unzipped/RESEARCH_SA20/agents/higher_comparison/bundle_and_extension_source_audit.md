# Compact definable bundles and local extension: exact source audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort,
agent `/root/higher_comparison`; 19 November 2026.
Working research notes. No additional comparison theorem is promoted.

## Strong actual lifting within the definable category

Marcello Mamino, *Splitting definably compact groups in o-minimal
structures*, original arXiv:1001.2229v2:
<https://arxiv.org/pdf/1001.2229>.
Opened records `turn312523932view0`, `turn973435376view0/1/2/3`.
Section 2 works in arbitrary o-minimal expansions of real closed
fields. Definition 2.2 requires bundle maps to be homeomorphisms on
each fibre. Theorem 2.14, pp.7–8, lifts a definable base homotopy of a
bundle map to a homotopy of bundle maps, stationary where the base
homotopy is stationary. Its finite construction transports through
local product charts. Corollary 2.15, p.8, trivializes bundles over a
definably contractible base when the fibre is locally definably
compact. Lemma 2.6, p.4, verifies joint inverse continuity for such
families. These are actual fibre homeomorphisms, a stronger input than
ordinary homotopy lifting of maps.

They remain internal to the definable category. No PL reduction of a
compact fibre bundle or relative comparison of two trivializations is
asserted. In particular, lifting a base homotopy cannot be substituted
for changing the structure category while fixing a prescribed PL
boundary trivialization.

Hardt–Lambrechts–Turchin–Volić, *Real homotopy theory of semi-algebraic
sets*, Algebraic & Geometric Topology 11 (2011), 2477–2545:
<https://msp.org/agt/2011/11-5/agt-v11-n5-p01-s.pdf>.
Opened records `turn549111562view0`, `turn445993326view0/1/2`.
Definition 8.1, p.2529, uses a finite semialgebraic open bundle atlas.
Proposition 8.5 and Lemmas 8.7–8.8, pp.2530–2532, establish
composition and interval-base transport/triviality results in that
category. These results support definable bundle transport but do not
compare its structure group with the full jointly PL homeomorphism
group. The published lemma numbering is 8.7–8.8; the preprint has
different numbering.

## The tempting canonical extension route has an exact missing step

Kuiper–Lashof, *Microbundles and Bundles I. Elementary Theory*,
Inventiones Mathematicae 1 (1966), 1–17, full original:
<https://www.maths.gla.ac.uk/~mpowell/Kuiper-Lashof1966_Article_MicrobundlesAndBundles.pdf>.
Independently opened `turn527181164view1`, `turn962989202view0`,
`turn515417149view1`, `turn294415036view0`.

Their Lemma 3, p.11, is a genuinely parameter-preserving extension of
an embedding of a ball over a simplex to a sphere-bundle
automorphism. Section 4, pp.12–13, constructs the TOP extension by an
infinite sequence `f_k` and its limit. Thus its formula is not a finite
semialgebraic construction as written. Section 5 gives a finite PL
replacement. The point case uses Newman's theorem; the general
parameter-simplex case explicitly invokes Hudson's higher-parameter
PL isotopy-extension theorem (pp.14–15), transporting the whole
family to a constant family. Reusing this argument for SA would
require exactly the presently missing definable parametric
isotopy-extension theorem. The pure PL proof does not remove that
dependency.

This matters for attempts to import the Edwards–Kirby local operator:
the canonical Schoenflies input has references to Kister and
Kuiper–Lashof. The latter does not supply a verified finite SA
operator. Infinite sequences can be locally finite in the PL category
while failing to be globally semialgebraic. No assertion that such an
operator is impossible is made; only the cited construction has not
proved it.

## Why the elementary-extension argument does not finish this route

For a fixed finite input format, pointwise existence of some finite
SA extension in every elementary extension can sometimes yield a
uniform finite output format by logical compactness. This does not
select extensions continuously over the original parameter space.
Hardt triviality supplies sections on cells, and one still has to
match them on the cell boundaries through extensions with the exact
same relative data. The space of extensions is not automatically
contractible: fixing both an inner ball and the outer sphere leaves
an annular relative homeomorphism group. Treating that group as
contractible by the ordinary Alexander trick discards the inner
fixed set.

Similarly, a poset of individual semialgebraic cell decompositions
can have common refinements without giving common refinements of
families over their entire parameter simplex. The latter must retain
the projection, including at parameter faces. Ordinary finite
triangulation and Hardt partitions do not establish this stronger
condition.

## Exact remaining target

Already for a based two-parameter SA concordance, one needs a
homotopy through actual SA homeomorphisms over the same two-parameter
base, preserving the bottom and the parameter boundary, whose final
total map is PL. The existing scalar-coordinate theorem controls one
parameter, and the new bundle-lifting theorems do not supply the
second preserved coordinate. An explicit class in the kernel of
forgetting definability would be an alternative resolution. Neither
has been proved in this audit.

The Hofmann thesis source previously opened and recorded in
`notes_1906.md` concerns isotopy classes of individual PL and SA–PL
structures. A fresh fetch during this interval returned 403; no new
bundle or higher-family consequence was extracted from it.

## Fichou–Shiota microbundle argument: no omitted higher SA assertion

Goulwen Fichou and Masahiro Shiota, *Real Milnor fibres and Puiseux
series*, Annales scientifiques de l'École Normale Supérieure 50
(2017), 1205–1240, published original:
<https://www.numdam.org/item/10.24033/asens.2343.pdf>.
Reopened original records `turn529875217view0`, `turn440704764view0`,
`turn416268480view0` at 19:55–19:56 UTC on 19 November 2026.

Section 5.1, pp.1234–1236, defines TOP microbundles and microbundle
maps. Proposition 5.1, pp.1236–1237, assumes a vector bundle and a
specified microbundle isomorphism over `M × I`, with the prescribed
linear endpoint structures, and deduces that the two individual smooth
manifolds are diffeomorphic. It uses the Kirby–Siebenmann pullback,
product-structure, and concordance-implies-isotopy results. Corollary
5.2, p.1237, starts with an already existing isotopy from an onto
homeomorphism to a `C1` embedding. Milnor's microbundle homotopy theorem
then gives transport covering the fixed initial base map. Neither the
corollary nor its proof asserts semialgebraicity of that transport or
preservation of additional family parameters.

The application in pp.1238–1239 constructs a special semialgebraic
isotopy of Milnor fibres and uses the extra hypothesis that the induced
map on Puiseux arcs is weakly continuous. Proposition 1.14 converts
that hypothesis to `C1` regularity at an infinitesimal fibre, then
transfer supplies a real parameter where the isotopy has a `C1`
embedding endpoint. This additional regularity is not a property of
an arbitrary semialgebraic homeomorphism family.

The relative Nash approximation in Lemmas 2.9–2.10, pp.1223–1224,
is a homotopy of ordinary maps, obtained by linear interpolation and
Nash tubular projection. It supplies no injectivity along the
homotopy. Consequently this source does not prove the required
relative PL straightening of a two-parameter SA homeomorphism family.
