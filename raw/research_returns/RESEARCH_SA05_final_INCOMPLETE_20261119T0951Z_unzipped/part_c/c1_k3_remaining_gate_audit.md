# C.1: audit of the remaining K3 exterior-power gate

Audit date: 19 November 2026, 05:27–05:38 UTC.
Status: no new vanishing theorem and no smaller proved gate obtained.
This is a failed-method record, not a claimed resolution of C.1(c).

## 1. Exact object still to be annihilated

For a complex projective K3 surface S of Picard number rho, set
T=t2(S), of cohomological dimension d=22-rho. The proved reduction in
`c:k3-transcendental-gate` identifies the all-powers narrow-ring assertion
with vanishing of the normalized alternating idempotent

    e_(d+1)=(1/(d+1)!) sum_(sigma in S_(d+1)) sign(sigma) sigma

on T^(tensor(d+1)). It is a correspondence on S^(2(d+1)); at rho=1,
this uses44 factors. Its expression uses divisor projectors outside
the requested narrow ring. The first corresponding universal narrow
relation remains the alternating h2 projector on46 factors.

## 2. Nilpotence is not progress for this idempotent

The projector satisfies e^2=e in Chow, before realization. Hence e^r=e
for every positive r. Its composition-nilpotence is therefore equivalent
to e=0. Rephrasing the missing vanishing as nilpotence of this single
idempotent does not prove a weaker assertion.

One might instead ask for nilpotence of every homologically or
numerically trivial self-correspondence of S. That statement concerns
End(h(S)), whereas e belongs to End(T^(tensor(d+1))). No tensor stability
of the relevant nilpotence ideals has been proved in this argument.
It is invalid to omit that distinction. The opened primary statement
of Jannsen, *On finite-dimensional motives and Murre's conjecture*
(2006 author preprint), Theorem0.2, p2, imposes its nilpotence condition
on **every power** X^N. We did not use this theorem as a proof of the
missing K3 case or claim to have independently reconstructed its entire
proof.

Primary source:
https://epub.uni-regensburg.de/556/1/05-2006.pdf
Opened reference: turn128396147view1.

## 3. Contraction does not lower the first missing relation

In any rigid symmetric Q-linear category, let A_m be the normalized
alternator and let delta be the categorical dimension of the object.
Taking the partial trace in the last tensor factor gives the exact
identity

    ptr_last(A_m)=((delta-m+1)/m) A_(m-1).

To verify it, separate permutations fixing the last letter from the
others. The former give delta/m times A_(m-1). Removing the last letter
from its nontrivial cycle changes the sign and gives exactly m-1 copies
of each permutation on the remaining letters, contributing
-(m-1)/m times A_(m-1). For T, delta=d. Thus at m=d+1 the partial trace
is zero. The first exterior obstruction cannot be recovered from a
smaller one by this contraction. This calculation explains the failure
of this proposed proof operation; it does not rule out other geometric
arguments.

## 4. Specialization has the wrong direction for the proposed proof

Specialization of Chow correspondences preserves a vanishing identity,
so a generic finite-dimensionality identity specializes. Vanishing of
an identity on some special fibres does not provide a reverse map or
injectivity of specialization. A dense collection of special fibres
with finite-dimensional motives supplies no uniform rational
equivalence over the generic fibre in the present argument. We have not
proved a bounded-complexity spreading assertion that would change this.

The Picard projector also needs care. When rho jumps, the specialization
of the generic transcendental motive can contain additional Tate
summands; it must not simply be identified with the transcendental
motive of the special fibre. Pedrini's *On the motive of a K3 surface*,
Clay Mathematics Proceedings9, printed pp62–63, Propositions4.2–4.3,
was opened with its proofs. The usable direction of Proposition4.3 is
generic finite-dimensionality implies special finite-dimensionality;
the direct-summand formulation retains the Picard-jump terms. It gives
no reverse-specialization proof for a general K3 surface.

Primary source (complete volume):
https://www.claymath.org/library/proceedings/cmip09c.pdf
Opened reference: turn364931297view2.

## 5. A valid conditional relative route still has a missing premise

Voisin's *Bloch's conjecture for Catanese and Barlow surfaces*,
Journal of Differential Geometry97 (2014),149–175, was opened.
Proposition1.3 and its proof on p155 give composition-nilpotence for
specified fibrewise codimension-two correspondences after the relative
cohomological correction and under the rational-connectedness hypothesis
on a compactified relative square. Theorems3.5–3.6, pp167–168, with
Lemmas3.7–3.8 and the proof on pp168–172, turn algebraicity of the general
Kuga–Satake correspondence into a Chow-theoretic abelian-motive splitting
for their stated families. Thus a separate general nilpotence conjecture
is not needed in that conditional route.

The remaining algebraicity assumption is not established here. Moreover,
the exterior projector above has codimension2(d+1) on a much higher
power; Proposition1.3's codimension-two argument cannot be applied to it
merely because its cohomological realization vanishes. We therefore do
not claim that this route is a strictly weaker equivalent condition than
Kimura finite-dimensionality, or that it resolves the general surface.

Primary source:
https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/JDG-97-1-A8-Voisin.pdf
Opened references: turn128396147view0; turn911008769view0/1/2;
turn364931297view0/1; turn438504793view1/2. The full Proposition1.3
proof and the Kuga–Satake construction/lifting proof were read.

## 6. Current-source check and unchanged status

The further current-source searches did not identify a theorem proving
the general Chow exterior-power vanishing. The already opened July2026
hyper-Kummer paper proves specified special families. A November2026
search result for Laterveer's genus-seven Fano paper still states the
K3 tautological injectivity/finite-dimensionality equivalence; that search
result is corroborative only and is not used as a proof or as evidence
that no future solution can exist. The withdrawn October4 K3 Hodge
preprint and an unsupported general Ayoub claim remain excluded.

The proved finite criteria under C+ are substantial criteria, but the
minimal rectangular Schur condition is itself equivalent to Kimura
finite-dimensionality under that hypothesis (Del Padrone–Mazza,
Theorem3.2, already fully checked). Nothing in the present follow-up
proves that condition for a general K3 surface. The main statement and
central result index must retain the unresolved status.
