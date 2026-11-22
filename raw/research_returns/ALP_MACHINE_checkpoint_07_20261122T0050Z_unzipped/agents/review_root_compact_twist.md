# Whole-proof review of AM-R-008 and its general-level application

Reviewer: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE.
21 November 2026 UTC.

**Outcome: the complete mathematical proof passes in its stated
target-level scope.** The inline typesetting defects observed in
the first saved version were reported separately and do not change
this mathematical review.

I read every part of compact_determinant_twist_accounting.md,
including the conventions, invariant coefficient lattices and
final limitations. The group level is normal in the full lattice
stabilizer and has exactly the asserted determinant image:
the diagonal section proves the reverse inclusion. The torus
class-one decomposition then leaves a special-unitary factor.
The use of strong approximation has the correct factor order,
and normality allows its compact factor to move across the
chosen compact determinant lift. No determinant bound for the
special-unitary factor is inadvertently inferred.

In the left-equivariant coefficient-valued convention, the
inverse infinity character in the twisted coefficient action
is correct. For a stabilizer element its determinant is in
the determinant of the right level; rational triviality
then makes the infinity twist act as1. Thus the invariant
coefficient subspaces are literally the same. Every class
scalar is a root of unity, so the displayed diagonal map
preserves the full local lattice content and every complex
mass norm with unchanged weights. It is an actual integral
isometry, not only an equality in a Grothendieck group.

The application caveat is that ALP-LIFT-10's named $K_M$
is a source torus stabilizer. It does not by itself prove
that the first target theta functions have the particular
group level chosen in AM-R-008. The theorem already has
enough information to avoid this confusion, and the
following general-level version makes the application
transparent.

## Proposed extension to any compatible actual target level

Let $K$ be any open compact subgroup of the standard
target stabilizer $K_0$, and put $D=\det K$.
It is open in $K_{T,0}$ because the determinant map
has the continuous local section
$t\mapsto\operatorname{diag}(t,1,\ldots,1)$.
Choose representatives $a$ of the finite quotient
$K_{T,0}/(\mu_{14}D)$ and put
$s(a)=\operatorname{diag}(a,1,\ldots,1)$.
Then, without any normality assumption on $K$,
\[
 G(\mathbb A_{F,f})
     =\bigcup_aG(F)\,SU(I_n)(F_{v_{11}})\,s(a)K .
 \tag{Q1}
\]

For a full proof, write
$\det g=t_0ak_D$, with $t_0\in T(F)$ and
$k_D\in D$. By the definition of $D$, choose
$k\in K$ of determinant $k_D$; the lift need not
be the diagonal section. Put
$h=s(t_0)^{-1}gk^{-1}s(a)^{-1}\in SU(\mathbb A_{F,f})$.
Use strong approximation with the actual conjugated
compact
\[
                  L=s(a)Ks(a)^{-1}\cap SU(\mathbb A_{F,f}).
 \tag{Q2}
\]
It gives $h=\delta u_{11}\ell$, with
$\delta\in SU(F)$ and $\ell\in L$. Consequently
\[
 g=s(t_0)\delta\,u_{11}s(a)\,
                   (s(a)^{-1}\ell s(a))k,
 \tag{Q3}
\]
whose last two factors are in $K$. This proves (Q1).
The determinant of its representative is the compact
idele $a$. No commutation of factors at11 was used.
Representatives may now have compact support at more
primes than7 and29; the conclusion needed for the
twist is compactness, not that support restriction.

If $\gamma_f|_D=1$, the entire proof of AM-R-008
sections2–3 applies word for word to these representatives.
In particular stabilizers have determinants in $D$,
their invariant coefficient subspaces agree, and the
class-value map is the diagonal multiplication by
$\gamma_f(a)$. This proves its exact integral and
metric conclusion for an arbitrary compatible actual
target level.

For ALP-LIFT-11's constructed character, every compact
value has order dividing28. Any finite collection of
actual first Schwartz vectors has a compact-open
target stabilizer; refining it inside
$K_0\cap\ker(\gamma_f\circ\det)$ produces a level
to which this argument applies. This proves there is
no additional arithmetic loss in the twist on that
chosen module. It does not compute the original
stabilizer index, the cost of any refinement relative
to a separately fixed level, the original mass, or
the identification with a pinned arithmetic row.

The extension uses the same torus class calculation
and the same primary strong-approximation theorem
already checked in the review of AM-R-007. No new
formal proof-assistant execution is claimed.
