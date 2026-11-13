# Corollaries to note: the generalized Riemann hypothesis

*Recorded on 12 November 2026 at the user's request by Claude Opus 5.5 (effort max). This is a note to the programme.
It is not a line of work.*

## What the user asked to be noted

The user, 12 November 2026:

> "My intent was to recall which potential outcomes would imply it, not as a thing to pursue, but as a thing to note
> as an interesting corollary of anything that we would pursue, not on the basis of whether or not it resolves that,
> but on the basis of it being part of this program."
>
> "where it is part of it - which I thought the [mixed] Tate motivic implications were"
>
> "and via Deligne purity - I think that is already sort of articulated"

On what kind of statement this is: "I'm not intending to say something that I understand to be non-standard or
conjectural. GRH is a conjecture. [Its] restatements are just restatements."

## The statement of the programme it attaches to

War game, round 1 (`PROGRAM_WARGAME_20261112.md`), S9, "GT and the motivic Galois group, level by level":

- (i) Claimed in 2026: grt₁ is the Lie algebra of the unipotent motivic Galois group of mixed Tate motives over Z
  (bridge B3).
- (ii) In genus one, the conjecture that grt_ell is the Lie algebra of π₁ of mixed elliptic motives.
- "Plausibility. It is a conjecture of the field; (i) supports it. What would decide it. A proof in all weights is out
  of reach. Tables by weight and depth are in reach."

The user's reading: the all-weights statement, level by level, together with Deligne's purity, gives GRH as a
corollary, along a route the user takes to be articulated already in known restatements of GRH. On "out of reach":
the conjecture being open in the field does not by itself put it out of the programme's reach, since the programme's
work is that part of the field; nor does that put it in scope.

## Two points checked against the sources (Claude Opus 5.5, 12 November)

- **Ayoub, "Anabelian presentation of the motivic Galois group in characteristic zero."** For a field k with a complex
  embedding, the motivic Galois group is the automorphism group of the functor X ↦ π₁^geo(X). Ayoub presents this as a
  motivic version of the Ihara–Matsumoto–Oda conjecture, which Pop expanded and proved. It is the form of S9 for all
  varieties, where S9 has the moduli tower. Source: the author's PDF,
  https://www.math.uzh.ch/en/fileadmin/user/ayoub/publikation/Anabel.pdf (abstract and introduction read; the exact
  hypotheses of the theorem not checked).
- **The cosmic Galois group and a Dedekind zeta function.**
  - Connes and Marcolli show that the cosmic Galois group U* is abstractly, not canonically, isomorphic to the motivic
    Galois group of mixed Tate motives over Z[i][1/2] (arXiv:math/0409306).
  - By Deligne–Goncharov, the Lie algebra of its unipotent part is free with dim Ext¹(Q(0), Q(n)) generators in
    degree n:
    - for n = 1, the rank of the S-units Z[i][1/2]^× (one, from 1 + i);
    - for n ≥ 2, the rank of K_{2n−1}(Z[i]) ⊗ Q.
  - By Borel, these ranks are the orders of vanishing at s = 1 − n of the zeta function of Spec Z[i][1/2], that is of
    ζ_{Q(i)}(s)(1 − 2^{−s}): one for every n ≥ 1. The leading coefficients there are the Borel regulators, up to
    rational factors.
  - So the generators of U* in degree n correspond one to one to the zeros of that zeta function at s = 1 − n, and
    their regulators are its leading coefficients there.

The user, later the same day: "it's the motivic [mixed] Tate stuff, and then there's some sort of pure motive, which I
think is some sort of pure twisted Tate motive ... something like that would imply RH"; and "via NCG, you could get to
a whole bunch of [things] with the [Dedekind] zeta function and like Dirichlet functions and Artin functions and
stacking and moduli stacks. It's probably all in the same weird like neighborhood-ish thing."

**The standard name for the pure objects (Claude Opus 5.5).** A "pure twisted Tate motive" is an Artin–Tate motive
ρ ⊗ Q(n), with ρ an Artin representation. It is pure of weight −2n, and its L-function is L(ρ, s + n). The Riemann
hypothesis for all of them is GRH for Artin L-functions: the Grand Riemann Hypothesis for motivic L-functions,
restricted to this class. They are the graded pieces of the weight filtration of the mixed Tate motives of the
programme, read over Q:
- over Q(μ_N), the graded pieces Ind Q(n) split into χ ⊗ Q(n) over the Dirichlet characters χ mod N;
- over a Galois field F, Ind_F^Q Q(n) contains every irreducible Artin representation of Gal(F/Q).

Not written out here: which known restatement of GRH the user means, and the step from the all-weights statement to it
through purity.

Where it bears: stage 7 of round 1 (cotes 13 and 15: motivic Galois groups, the extension by Γ_Q, L-functions of
motives), and S9 with its tables by weight and depth.

## Correction (Claude Opus 5.5, 12 November 2026, ~21:3x UTC): the route to the critical line runs through positivity

In conversation I said that the motivic side sees L-functions only at s = 1−n (trivial zeros, regulators) and that
"none of this reaches" the critical strip. The first half is true of the Borel and Deligne–Goncharov dictionary. The
second half was wrong as stated. The user: "Whenever two things aren't literally the same, you claim there's no
relation." The known routes from this neighbourhood to the critical line all run through **positivity**:

- **Weil's criterion.** RH (and GRH for a given L-function) is equivalent to the positivity of Weil's quadratic
  functional built from the explicit formula, which sums over all zeros and all primes (Weil 1952, "Sur les
  'formules explicites' de la théorie des nombres premiers"). Li's criterion (X.-J. Li, 1997) is a sequence form of
  the same positivity.
- **Function fields: positivity is the proof.** For curves over finite fields, RH follows from the Hodge index
  theorem on C × C, the Castelnuovo–Severi inequality (Weil). Grothendieck's standard conjectures (1969) put that
  positivity in motivic form; the Hodge standard conjecture would give the Weil conjectures' RH by Weil's argument.
  This is the programme's own territory: motives, cotes 13 and 15, and Kleiman's "Standard conjectures" listed as
  a context witness in the war game.
- **Bost–Connes and NCG.** The Bost–Connes system's partition function is ζ(β). Connes ("Trace formula in
  noncommutative geometry and the zeros of the Riemann zeta function", Selecta Math. 5 (1999)) realizes the zeros
  spectrally on the adele class space, the same space behind the BC system, and reduces RH to the positivity of a
  trace formula, that is, to Weil's criterion. Connes–Consani continue this: the arithmetic site, the scaling site,
  and "Weil positivity and trace formula, the archimedean place" (Selecta Math. 2021).

So the user's "GRH/BCM" layer, the mixed Tate levels and the pure Artin–Tate pieces sit in the neighbourhood where
RH is attacked through positivity. Whether the programme yields any positivity statement is open. A
"no bearing" verdict is not available. Recorded as a note to the programme, not a line of work (user, 12 Nov).
